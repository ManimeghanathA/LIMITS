from __future__ import annotations

import re
from itertools import combinations
from math import ceil
from typing import Any

from src.dataset import BudgetSelection, EvidenceUnit, Paragraph, Question
from src.knapsack_features import (
    FeatureWeights,
    build_candidate_input,
    build_feature_utility,
    feature_based_knapsack_selector,
    select_feature_candidates,
)
from src.semantic_features import SemanticScorer
from src.utility import InteractionUtility


def parse_manual_paragraphs(text: str) -> tuple[Paragraph, ...]:
    blocks = tuple(block.strip() for block in re.split(r"\n\s*\n+", text) if block.strip())
    return tuple(
        Paragraph(
            id=f"m{index:02d}",
            text=block,
            tokens=_estimate_tokens(block),
        )
        for index, block in enumerate(blocks, start=1)
    )


def manual_question(text: str) -> Question:
    return Question(
        id="manual_question",
        text=text.strip(),
        answer="Manual question",
        category="direct",
        required_evidence_units=(EvidenceUnit("manual", ("manual",)),),
        budget_ground_truth={
            128: (BudgetSelection(("manual",)),),
            256: (BudgetSelection(("manual",)),),
            512: (BudgetSelection(("manual",)),),
            1024: (BudgetSelection(("manual",)),),
        },
    )


def build_knapsack_trace(
    question: Question,
    paragraphs: tuple[Paragraph, ...],
    budget: int,
    weights: FeatureWeights = FeatureWeights(),
    semantic_scorer: SemanticScorer | None = None,
) -> dict[str, Any]:
    candidates = select_feature_candidates(
        question,
        paragraphs,
        budget,
        max_candidates=15,
        weights=weights,
        semantic_scorer=semantic_scorer,
    )
    public = build_candidate_input(question, candidates, budget)
    utility = build_feature_utility(
        question,
        candidates,
        budget,
        weights=weights,
        semantic_scorer=semantic_scorer,
    )
    result = feature_based_knapsack_selector(
        question,
        paragraphs,
        budget,
        max_candidates=15,
        weights=weights,
        semantic_scorer=semantic_scorer,
    )
    selected = frozenset(result.selected_ids)

    return {
        "question": question.text,
        "budget": budget,
        "candidateLimit": 15,
        "paragraphs": [_paragraph_payload(paragraph) for paragraph in paragraphs],
        "candidates": [_paragraph_payload(paragraph) for paragraph in candidates],
        "scoreRows": _score_rows(question, candidates, budget, utility, semantic_scorer),
        "interactionRows": _interaction_rows(utility),
        "subsetRows": _subset_rows(public.chunks, budget, utility, selected),
        "breakdown": _score_breakdown(selected, utility),
        "final": {
            "selectedIds": list(result.selected_ids),
            "tokenUsed": result.total_tokens,
            "score": round(result.score, 4),
        },
    }


def _paragraph_payload(paragraph: Paragraph) -> dict[str, Any]:
    return {
        "id": paragraph.id,
        "text": paragraph.text,
        "tokens": paragraph.tokens,
    }


def _score_rows(
    question: Question,
    candidates: tuple[Paragraph, ...],
    budget: int,
    utility: InteractionUtility,
    semantic_scorer: SemanticScorer | None,
) -> list[dict[str, Any]]:
    query_terms = _terms(question.text)
    rows = []
    for index, paragraph in enumerate(candidates, start=1):
        paragraph_terms = _terms(paragraph.text)
        overlap = len(query_terms & paragraph_terms)
        coverage = overlap / len(query_terms) if query_terms else 0.0
        semantic = 0.0
        if semantic_scorer is not None:
            semantic = max(0.0, semantic_scorer.similarity(question.text, paragraph.text))
        rows.append(
            {
                "rank": index,
                "id": paragraph.id,
                "text": paragraph.text,
                "tokens": paragraph.tokens,
                "queryOverlap": round(coverage, 4),
                "termHits": overlap,
                "semanticSimilarity": round(semantic, 4),
                "tokenPressure": round(paragraph.tokens / budget, 4),
                "individualScore": round(utility.individual.get(paragraph.id, 0.0), 4),
            }
        )
    return rows


def _interaction_rows(utility: InteractionUtility) -> dict[str, list[dict[str, Any]]]:
    pair_rows = [
        {"ids": sorted(key), "score": round(score, 4)}
        for key, score in utility.pair_synergy.items()
    ]
    redundancy_rows = [
        {"ids": sorted(key), "penalty": round(score * utility.redundancy_weight, 4)}
        for key, score in utility.pair_redundancy.items()
    ]
    triple_rows = [
        {"ids": sorted(key), "score": round(score, 4)}
        for key, score in utility.triple_synergy.items()
    ]
    return {
        "pairSynergy": sorted(pair_rows, key=lambda row: (-row["score"], row["ids"]))[:24],
        "redundancy": sorted(redundancy_rows, key=lambda row: (-row["penalty"], row["ids"]))[:24],
        "tripleSynergy": sorted(triple_rows, key=lambda row: (-row["score"], row["ids"]))[:18],
    }


def _subset_rows(chunks, budget: int, utility: InteractionUtility, selected: frozenset[str]) -> list[dict[str, Any]]:
    chunk_by_id = {chunk.id: chunk for chunk in chunks}
    rows = [
        _subset_payload(frozenset(), chunk_by_id, budget, utility, selected, "empty baseline")
    ]
    singleton_rows = [
        _subset_payload(frozenset({chunk.id}), chunk_by_id, budget, utility, selected, "single candidate")
        for chunk in chunks
    ]
    pair_rows = [
        _subset_payload(frozenset({left.id, right.id}), chunk_by_id, budget, utility, selected, "pair candidate")
        for left, right in combinations(chunks, 2)
    ]
    feasible = [row for row in singleton_rows + pair_rows if row["status"] != "over budget"]
    over_budget = [row for row in singleton_rows + pair_rows if row["status"] == "over budget"]
    rows.extend(sorted(feasible, key=lambda row: (-row["utility"], row["tokenCost"], row["ids"]))[:24])
    rows.extend(over_budget[:8])
    if selected and not any(set(row["ids"]) == selected for row in rows):
        rows.append(_subset_payload(selected, chunk_by_id, budget, utility, selected, "final selected subset"))
    best_score = float("-inf")
    for row in rows:
        if row["status"] == "over budget":
            continue
        if row["utility"] > best_score:
            row["status"] = "current best"
            best_score = row["utility"]
    for row in rows:
        if set(row["ids"]) == selected:
            row["status"] = "final best"
    return rows


def _subset_payload(
    ids: frozenset[str],
    chunk_by_id,
    budget: int,
    utility: InteractionUtility,
    selected: frozenset[str],
    note: str,
) -> dict[str, Any]:
    token_cost = sum(chunk_by_id[item].token_cost for item in ids)
    over_budget = token_cost > budget
    return {
        "ids": sorted(ids),
        "tokenCost": token_cost,
        "utility": round(float(utility(ids)), 4) if not over_budget else None,
        "status": "over budget" if over_budget else "considered",
        "selectedOverlap": len(ids & selected),
        "note": note,
    }


def _score_breakdown(selected: frozenset[str], utility: InteractionUtility) -> dict[str, float]:
    individual = sum(utility.individual.get(chunk_id, 0.0) for chunk_id in selected)
    pair_synergy = sum(score for key, score in utility.pair_synergy.items() if key <= selected)
    triple_synergy = sum(score for key, score in utility.triple_synergy.items() if key <= selected)
    redundancy = utility.redundancy_weight * sum(
        score for key, score in utility.pair_redundancy.items() if key <= selected
    )
    total = individual + pair_synergy + triple_synergy - redundancy
    return {
        "individual": round(individual, 4),
        "pairSynergy": round(pair_synergy, 4),
        "tripleSynergy": round(triple_synergy, 4),
        "redundancyPenalty": round(redundancy, 4),
        "total": round(total, 4),
    }


def _estimate_tokens(text: str) -> int:
    return max(1, ceil(len(re.findall(r"\S+", text)) * 1.35))


def _terms(text: str) -> frozenset[str]:
    stopwords = {
        "a",
        "an",
        "and",
        "are",
        "at",
        "be",
        "by",
        "for",
        "in",
        "is",
        "it",
        "of",
        "on",
        "or",
        "the",
        "to",
        "what",
        "when",
        "where",
        "which",
        "who",
        "why",
    }
    return frozenset(
        term for term in re.findall(r"[a-z0-9]+", text.lower()) if term not in stopwords
    )
