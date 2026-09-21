from __future__ import annotations

import re
from dataclasses import dataclass
from itertools import combinations

from src.contracts import CandidateChunk, CandidateInput, SelectionResult
from src.dataset import Paragraph, Question
from src.optimizer import optimize_interactions
from src.semantic_features import SemanticScorer, SentenceTransformerSemanticScorer
from src.utility import InteractionUtility


STOPWORDS = frozenset(
    {
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
)


@dataclass(frozen=True)
class FeatureWeights:
    individual_query_overlap: float = 3.0
    individual_term_hits: float = 0.15
    semantic_query_similarity: float = 0.5
    seed_linkage: float = 3.0
    semantic_seed_linkage: float = 0.3
    selection_penalty: float = 1.0
    budget_token_penalty: float = 1.0
    pair_complementarity: float = 2.0
    pair_linkage: float = 1.3
    semantic_pair_linkage: float = 0.0
    triple_complementarity: float = 1.25
    redundancy: float = 1.5
    semantic_redundancy: float = 0.75
    semantic_redundancy_threshold: float = 0.72
    redundancy_weight: float = 0.75


def build_candidate_input(
    question: Question,
    paragraphs: tuple[Paragraph, ...],
    budget: int,
) -> CandidateInput:
    return CandidateInput(
        query=question.text,
        chunks=tuple(
            CandidateChunk(
                id=paragraph.id,
                text=paragraph.text,
                token_cost=paragraph.tokens,
            )
            for paragraph in paragraphs
        ),
        token_budget=budget,
    )


def build_feature_utility(
    question: Question,
    paragraphs: tuple[Paragraph, ...],
    budget: int,
    weights: FeatureWeights = FeatureWeights(),
    semantic_scorer: SemanticScorer | None = None,
) -> InteractionUtility:
    scorer = semantic_scorer or SentenceTransformerSemanticScorer()
    query_terms = _terms(question.text)
    paragraph_terms = {
        paragraph.id: _terms(paragraph.text) for paragraph in paragraphs
    }
    base_individual = _base_individual_scores(
        question,
        query_terms,
        paragraph_terms,
        paragraphs,
        budget,
        weights,
        scorer,
    )
    seeds = _lexical_seeds(paragraphs, base_individual, min(4, len(paragraphs)))
    individual = _seed_linked_individual_scores(
        question,
        paragraphs,
        paragraph_terms,
        base_individual,
        seeds,
        weights,
        scorer,
    )
    text_by_id = {paragraph.id: paragraph.text for paragraph in paragraphs}
    pair_synergy = _pair_synergy(query_terms, paragraph_terms, text_by_id, weights, scorer)
    triple_synergy = _triple_synergy(query_terms, paragraph_terms, weights)
    pair_redundancy = _pair_redundancy(paragraph_terms, text_by_id, weights, scorer)

    return InteractionUtility(
        individual=individual,
        pair_synergy=pair_synergy,
        pair_redundancy=pair_redundancy,
        triple_synergy=triple_synergy,
        redundancy_weight=weights.redundancy_weight,
    )


def feature_based_knapsack_selector(
    question: Question,
    paragraphs: tuple[Paragraph, ...],
    budget: int,
    max_candidates: int = 15,
    weights: FeatureWeights = FeatureWeights(),
    semantic_scorer: SemanticScorer | None = None,
) -> SelectionResult:
    scorer = semantic_scorer or SentenceTransformerSemanticScorer()
    candidates = select_feature_candidates(question, paragraphs, budget, max_candidates, weights, scorer)
    public = build_candidate_input(question, candidates, budget)
    scoped_utility = build_feature_utility(question, candidates, budget, weights, scorer)
    return optimize_interactions(public, scoped_utility)


def select_feature_candidates(
    question: Question,
    paragraphs: tuple[Paragraph, ...],
    budget: int,
    max_candidates: int = 15,
    weights: FeatureWeights = FeatureWeights(),
    semantic_scorer: SemanticScorer | None = None,
) -> tuple[Paragraph, ...]:
    scorer = semantic_scorer or SentenceTransformerSemanticScorer()
    query_terms = _terms(question.text)
    paragraph_terms = {
        paragraph.id: _terms(paragraph.text) for paragraph in paragraphs
    }
    base_individual = _base_individual_scores(
        question,
        query_terms,
        paragraph_terms,
        paragraphs,
        budget,
        weights,
        scorer,
    )
    lexical_individual = {
        paragraph.id: _individual_score(query_terms, paragraph_terms[paragraph.id], weights)
        for paragraph in paragraphs
    }
    semantic_individual = {
        paragraph.id: scorer.similarity(question.text, paragraph.text)
        for paragraph in paragraphs
    }
    seeds = _candidate_pool_seeds(
        paragraphs,
        lexical_individual,
        semantic_individual,
        max_candidates,
    )
    individual = _seed_linked_individual_scores(
        question,
        paragraphs,
        paragraph_terms,
        base_individual,
        seeds,
        weights,
        scorer,
    )
    seed_ids = frozenset(seed.id for seed in seeds)
    ranked = sorted(
        (paragraph for paragraph in paragraphs if paragraph.id not in seed_ids),
        key=lambda paragraph: (
            -individual.get(paragraph.id, 0.0),
            paragraph.tokens,
            paragraph.id,
        ),
    )
    return tuple(seeds + tuple(ranked[: max_candidates - len(seeds)]))


def _candidate_pool_seeds(
    paragraphs: tuple[Paragraph, ...],
    lexical_individual: dict[str, float],
    semantic_individual: dict[str, float],
    max_candidates: int,
) -> tuple[Paragraph, ...]:
    lexical_count = min(5, max_candidates)
    semantic_count = min(5, max_candidates)
    lexical_ranked = sorted(
        paragraphs,
        key=lambda paragraph: (
            -lexical_individual.get(paragraph.id, 0.0),
            paragraph.tokens,
            paragraph.id,
        ),
    )
    semantic_ranked = sorted(
        paragraphs,
        key=lambda paragraph: (
            -semantic_individual.get(paragraph.id, 0.0),
            paragraph.tokens,
            paragraph.id,
        ),
    )
    seeds: list[Paragraph] = []
    seen: set[str] = set()
    for group, count in ((lexical_ranked, lexical_count), (semantic_ranked, semantic_count)):
        represented = 0
        for paragraph in group:
            if paragraph.id in seen:
                represented += 1
                if represented >= count:
                    break
                continue
            seeds.append(paragraph)
            seen.add(paragraph.id)
            represented += 1
            if len(seeds) >= max_candidates:
                return tuple(seeds)
            if represented >= count:
                break
    return tuple(seeds)


def _individual_score(
    query_terms: frozenset[str],
    paragraph_terms: frozenset[str],
    weights: FeatureWeights,
) -> float:
    overlap = query_terms & paragraph_terms
    coverage = len(overlap) / len(query_terms) if query_terms else 0.0
    return weights.individual_query_overlap * coverage + weights.individual_term_hits * len(overlap)


def _base_individual_scores(
    question: Question,
    query_terms: frozenset[str],
    paragraph_terms: dict[str, frozenset[str]],
    paragraphs: tuple[Paragraph, ...],
    budget: int,
    weights: FeatureWeights,
    semantic_scorer: SemanticScorer,
) -> dict[str, float]:
    return {
        paragraph.id: (
            _individual_score(
                query_terms=query_terms,
                paragraph_terms=paragraph_terms[paragraph.id],
                weights=weights,
            )
            + weights.semantic_query_similarity
            * max(0.0, semantic_scorer.similarity(question.text, paragraph.text))
            - weights.budget_token_penalty * (paragraph.tokens / budget)
        )
        for paragraph in paragraphs
    }


def _lexical_seeds(
    paragraphs: tuple[Paragraph, ...],
    individual: dict[str, float],
    seed_count: int,
) -> tuple[Paragraph, ...]:
    lexical_ranked = sorted(
        paragraphs,
        key=lambda paragraph: (
            -individual.get(paragraph.id, 0.0),
            paragraph.tokens,
            paragraph.id,
        ),
    )
    return tuple(lexical_ranked[:seed_count])


def _seed_linked_individual_scores(
    question: Question,
    paragraphs: tuple[Paragraph, ...],
    paragraph_terms: dict[str, frozenset[str]],
    base_individual: dict[str, float],
    seeds: tuple[Paragraph, ...],
    weights: FeatureWeights,
    semantic_scorer: SemanticScorer,
) -> dict[str, float]:
    return {
        paragraph.id: (
            _candidate_prefilter_score(
                question,
                paragraph,
                seeds,
                base_individual,
                paragraph_terms,
                weights,
                semantic_scorer,
            )
            - weights.selection_penalty
        )
        for paragraph in paragraphs
    }


def _pair_synergy(
    query_terms: frozenset[str],
    paragraph_terms: dict[str, frozenset[str]],
    text_by_id: dict[str, str],
    weights: FeatureWeights,
    semantic_scorer: SemanticScorer,
) -> dict[frozenset[str], float]:
    values = {}
    for left, right in combinations(paragraph_terms, 2):
        left_coverage = _coverage(query_terms, paragraph_terms[left])
        right_coverage = _coverage(query_terms, paragraph_terms[right])
        combined = _coverage(query_terms, paragraph_terms[left] | paragraph_terms[right])
        gain = combined - max(left_coverage, right_coverage)
        link = _seed_link_score(paragraph_terms[left], paragraph_terms[right])
        score = weights.pair_complementarity * max(gain, 0.0)
        if link > 0:
            score += weights.pair_linkage * link
        score += weights.semantic_pair_linkage * max(
            0.0,
            semantic_scorer.similarity(text_by_id[left], text_by_id[right]),
        )
        if score > 0:
            values[frozenset({left, right})] = score
    return values


def _triple_synergy(
    query_terms: frozenset[str],
    paragraph_terms: dict[str, frozenset[str]],
    weights: FeatureWeights,
) -> dict[frozenset[str], float]:
    values = {}
    for first, second, third in combinations(paragraph_terms, 3):
        terms = paragraph_terms[first] | paragraph_terms[second] | paragraph_terms[third]
        best_pair = max(
            _coverage(query_terms, paragraph_terms[left] | paragraph_terms[right])
            for left, right in combinations((first, second, third), 2)
        )
        gain = _coverage(query_terms, terms) - best_pair
        if gain > 0:
            values[frozenset({first, second, third})] = weights.triple_complementarity * gain
    return values


def _pair_redundancy(
    paragraph_terms: dict[str, frozenset[str]],
    text_by_id: dict[str, str],
    weights: FeatureWeights,
    semantic_scorer: SemanticScorer,
) -> dict[frozenset[str], float]:
    values = {}
    for left, right in combinations(paragraph_terms, 2):
        lexical_similarity = _jaccard(paragraph_terms[left], paragraph_terms[right])
        semantic_similarity = max(
            0.0,
            semantic_scorer.similarity(text_by_id[left], text_by_id[right]),
        )
        semantic_excess = max(
            0.0,
            semantic_similarity - weights.semantic_redundancy_threshold,
        )
        semantic_penalty = 0.0
        if weights.semantic_redundancy_threshold < 1:
            semantic_penalty = semantic_excess / (1 - weights.semantic_redundancy_threshold)
        similarity = (
            weights.redundancy * lexical_similarity
            + weights.semantic_redundancy * semantic_penalty
        )
        if similarity > 0:
            values[frozenset({left, right})] = similarity
    return values


def _coverage(query_terms: frozenset[str], terms: frozenset[str]) -> float:
    if not query_terms:
        return 0.0
    return len(query_terms & terms) / len(query_terms)


def _jaccard(left: frozenset[str], right: frozenset[str]) -> float:
    if not left and not right:
        return 0.0
    return len(left & right) / len(left | right)


def _candidate_prefilter_score(
    question: Question,
    paragraph: Paragraph,
    seeds: tuple[Paragraph, ...],
    individual: dict[str, float],
    paragraph_terms: dict[str, frozenset[str]],
    weights: FeatureWeights,
    semantic_scorer: SemanticScorer,
) -> float:
    best_link = 0.0
    best_semantic_link = 0.0
    for seed in seeds:
        if seed.id == paragraph.id:
            continue
        best_link = max(
            best_link,
            _seed_link_score(paragraph_terms[paragraph.id], paragraph_terms[seed.id]),
        )
        best_semantic_link = max(
            best_semantic_link,
            semantic_scorer.similarity(seed.text, paragraph.text),
        )
    return (
        individual.get(paragraph.id, 0.0)
        + weights.seed_linkage * best_link
        + weights.semantic_seed_linkage * max(0.0, best_semantic_link)
    )


def _seed_link_score(left: frozenset[str], right: frozenset[str]) -> float:
    if not left or not right:
        return 0.0
    return len(left & right) / min(len(left), len(right))


def _terms(text: str) -> frozenset[str]:
    terms = re.findall(r"[a-z0-9]+", text.lower())
    return frozenset(term for term in terms if term not in STOPWORDS)
