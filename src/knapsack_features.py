from __future__ import annotations

import re
from dataclasses import dataclass
from itertools import combinations

from src.contracts import CandidateChunk, CandidateInput, SelectionResult
from src.dataset import Paragraph, Question
from src.optimizer import optimize_interactions
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
    seed_linkage: float = 3.0
    selection_penalty: float = 0.5
    pair_complementarity: float = 2.0
    triple_complementarity: float = 1.25
    redundancy: float = 1.5
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
    weights: FeatureWeights = FeatureWeights(),
) -> InteractionUtility:
    query_terms = _terms(question.text)
    paragraph_terms = {
        paragraph.id: _terms(paragraph.text) for paragraph in paragraphs
    }
    base_individual = _base_individual_scores(query_terms, paragraph_terms, paragraphs, weights)
    seeds = _lexical_seeds(paragraphs, base_individual, min(4, len(paragraphs)))
    individual = _seed_linked_individual_scores(
        paragraphs,
        paragraph_terms,
        base_individual,
        seeds,
        weights,
    )
    pair_synergy = _pair_synergy(query_terms, paragraph_terms, weights)
    triple_synergy = _triple_synergy(query_terms, paragraph_terms, weights)
    pair_redundancy = _pair_redundancy(paragraph_terms, weights)

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
    max_candidates: int = 10,
    weights: FeatureWeights = FeatureWeights(),
) -> SelectionResult:
    candidates = select_feature_candidates(question, paragraphs, max_candidates, weights)
    public = build_candidate_input(question, candidates, budget)
    scoped_utility = build_feature_utility(question, candidates, weights)
    return optimize_interactions(public, scoped_utility)


def select_feature_candidates(
    question: Question,
    paragraphs: tuple[Paragraph, ...],
    max_candidates: int = 10,
    weights: FeatureWeights = FeatureWeights(),
) -> tuple[Paragraph, ...]:
    query_terms = _terms(question.text)
    paragraph_terms = {
        paragraph.id: _terms(paragraph.text) for paragraph in paragraphs
    }
    base_individual = _base_individual_scores(query_terms, paragraph_terms, paragraphs, weights)
    seed_count = min(4, len(paragraphs), max_candidates)
    seeds = _lexical_seeds(paragraphs, base_individual, seed_count)
    individual = _seed_linked_individual_scores(
        paragraphs,
        paragraph_terms,
        base_individual,
        seeds,
        weights,
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


def _individual_score(
    query_terms: frozenset[str],
    paragraph_terms: frozenset[str],
    weights: FeatureWeights,
) -> float:
    overlap = query_terms & paragraph_terms
    coverage = len(overlap) / len(query_terms) if query_terms else 0.0
    return weights.individual_query_overlap * coverage + weights.individual_term_hits * len(overlap)


def _base_individual_scores(
    query_terms: frozenset[str],
    paragraph_terms: dict[str, frozenset[str]],
    paragraphs: tuple[Paragraph, ...],
    weights: FeatureWeights,
) -> dict[str, float]:
    return {
        paragraph.id: _individual_score(
            query_terms=query_terms,
            paragraph_terms=paragraph_terms[paragraph.id],
            weights=weights,
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
    paragraphs: tuple[Paragraph, ...],
    paragraph_terms: dict[str, frozenset[str]],
    base_individual: dict[str, float],
    seeds: tuple[Paragraph, ...],
    weights: FeatureWeights,
) -> dict[str, float]:
    return {
        paragraph.id: (
            _candidate_prefilter_score(
                paragraph,
                seeds,
                base_individual,
                paragraph_terms,
                weights,
            )
            - weights.selection_penalty
        )
        for paragraph in paragraphs
    }


def _pair_synergy(
    query_terms: frozenset[str],
    paragraph_terms: dict[str, frozenset[str]],
    weights: FeatureWeights,
) -> dict[frozenset[str], float]:
    values = {}
    for left, right in combinations(paragraph_terms, 2):
        left_coverage = _coverage(query_terms, paragraph_terms[left])
        right_coverage = _coverage(query_terms, paragraph_terms[right])
        combined = _coverage(query_terms, paragraph_terms[left] | paragraph_terms[right])
        gain = combined - max(left_coverage, right_coverage)
        if gain > 0:
            values[frozenset({left, right})] = weights.pair_complementarity * gain
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
    weights: FeatureWeights,
) -> dict[frozenset[str], float]:
    values = {}
    for left, right in combinations(paragraph_terms, 2):
        similarity = _jaccard(paragraph_terms[left], paragraph_terms[right])
        if similarity > 0:
            values[frozenset({left, right})] = weights.redundancy * similarity
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
    paragraph: Paragraph,
    seeds: tuple[Paragraph, ...],
    individual: dict[str, float],
    paragraph_terms: dict[str, frozenset[str]],
    weights: FeatureWeights,
) -> float:
    best_link = 0.0
    for seed in seeds:
        if seed.id == paragraph.id:
            continue
        best_link = max(
            best_link,
            _seed_link_score(paragraph_terms[paragraph.id], paragraph_terms[seed.id]),
        )
    return individual.get(paragraph.id, 0.0) + weights.seed_linkage * best_link


def _seed_link_score(left: frozenset[str], right: frozenset[str]) -> float:
    if not left or not right:
        return 0.0
    return len(left & right) / min(len(left), len(right))


def _terms(text: str) -> frozenset[str]:
    terms = re.findall(r"[a-z0-9]+", text.lower())
    return frozenset(term for term in terms if term not in STOPWORDS)
