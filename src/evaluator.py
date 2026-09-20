from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping

from src.dataset import Paragraph, Question


@dataclass(frozen=True)
class EvaluationResult:
    selected_ids: tuple[str, ...]
    budget: int
    token_used: int
    budget_valid: bool
    budget_utilization: float
    required_units_total: int
    required_units_covered: int
    required_unit_recall: float
    complete_hit: bool
    optional_units_total: int
    optional_units_covered: int
    optional_support_recall: float
    evidence_precision: float
    evidence_f1: float
    extra_chunk_count: int
    distractor_count: int
    ground_truth_selection_hit: bool
    best_ground_truth_jaccard: float


@dataclass(frozen=True)
class EvaluationWeights:
    required_recall_weight: float = 1.0
    complete_hit_bonus: float = 1.0
    optional_support_weight: float = 0.25
    precision_weight: float = 0.25
    over_budget_penalty: float = 1.0
    extra_chunk_penalty: float = 0.2
    distractor_penalty: float = 0.4


def evaluate_selection(
    question: Question,
    selected_ids: tuple[str, ...],
    budget: int,
    paragraphs_by_id: Mapping[str, Paragraph],
) -> EvaluationResult:
    if len(selected_ids) != len(set(selected_ids)):
        raise ValueError("selected ids must be unique")

    unknown = set(selected_ids) - set(paragraphs_by_id)
    if unknown:
        raise ValueError(f"selection references unknown paragraphs: {sorted(unknown)}")

    selected_set = frozenset(selected_ids)
    token_used = sum(paragraphs_by_id[item].tokens for item in selected_ids)
    budget_valid = token_used <= budget
    budget_utilization = token_used / budget if budget > 0 else 0.0

    required_units_covered = _count_covered_units(
        selected_set, question.required_evidence_units
    )
    required_units_total = len(question.required_evidence_units)
    required_unit_recall = _ratio(required_units_covered, required_units_total)
    complete_hit = required_units_covered == required_units_total

    optional_units_covered = _count_covered_units(
        selected_set, question.optional_support_units
    )
    optional_units_total = len(question.optional_support_units)
    optional_support_recall = _ratio(optional_units_covered, optional_units_total)

    relevant_ids = _unit_alternatives(
        question.required_evidence_units + question.optional_support_units
    )
    relevant_selected_count = len(selected_set & relevant_ids)
    evidence_precision = _ratio(relevant_selected_count, len(selected_set))
    evidence_f1 = _f1(evidence_precision, required_unit_recall)

    extra_chunk_count = len(selected_set - relevant_ids)
    distractor_ids = frozenset(
        item for group in question.distractor_groups for item in group
    ) - relevant_ids
    distractor_count = len(selected_set & distractor_ids)

    ground_truth_sets = tuple(
        frozenset(selection.selected)
        for selection in question.budget_ground_truth.get(budget, ())
    )
    ground_truth_selection_hit = selected_set in ground_truth_sets
    best_ground_truth_jaccard = max(
        (_jaccard(selected_set, ground_truth) for ground_truth in ground_truth_sets),
        default=0.0,
    )

    return EvaluationResult(
        selected_ids=selected_ids,
        budget=budget,
        token_used=token_used,
        budget_valid=budget_valid,
        budget_utilization=budget_utilization,
        required_units_total=required_units_total,
        required_units_covered=required_units_covered,
        required_unit_recall=required_unit_recall,
        complete_hit=complete_hit,
        optional_units_total=optional_units_total,
        optional_units_covered=optional_units_covered,
        optional_support_recall=optional_support_recall,
        evidence_precision=evidence_precision,
        evidence_f1=evidence_f1,
        extra_chunk_count=extra_chunk_count,
        distractor_count=distractor_count,
        ground_truth_selection_hit=ground_truth_selection_hit,
        best_ground_truth_jaccard=best_ground_truth_jaccard,
    )


def reward_from_evaluation(
    result: EvaluationResult,
    weights: EvaluationWeights = EvaluationWeights(),
) -> float:
    reward = weights.required_recall_weight * result.required_unit_recall
    reward += weights.complete_hit_bonus if result.complete_hit else 0.0
    reward += weights.optional_support_weight * result.optional_support_recall
    reward += weights.precision_weight * result.evidence_precision
    reward -= weights.extra_chunk_penalty * result.extra_chunk_count
    reward -= weights.distractor_penalty * result.distractor_count
    if not result.budget_valid:
        reward -= weights.over_budget_penalty
    return float(reward)


def _count_covered_units(selected: frozenset[str], units: tuple) -> int:
    return sum(not selected.isdisjoint(unit.alternatives) for unit in units)


def _unit_alternatives(units: tuple) -> frozenset[str]:
    return frozenset(item for unit in units for item in unit.alternatives)


def _ratio(numerator: int, denominator: int) -> float:
    if denominator == 0:
        return 0.0
    return numerator / denominator


def _f1(precision: float, recall: float) -> float:
    if precision + recall == 0:
        return 0.0
    return 2 * precision * recall / (precision + recall)


def _jaccard(left: frozenset[str], right: frozenset[str]) -> float:
    if not left and not right:
        return 1.0
    return len(left & right) / len(left | right)
