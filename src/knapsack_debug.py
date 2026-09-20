from __future__ import annotations

import json
from collections import Counter
from dataclasses import asdict, dataclass
from pathlib import Path

from src.dataset import BUDGETS, ContentCollection, Paragraph, Question
from src.evaluator import evaluate_selection
from src.knapsack_features import (
    FeatureWeights,
    build_feature_utility,
    feature_based_knapsack_selector,
    select_feature_candidates,
)


@dataclass(frozen=True)
class CandidateDebug:
    id: str
    tokens: int
    individual_score: float
    selected: bool
    is_required_alternative: bool
    is_distractor: bool


@dataclass(frozen=True)
class RequiredUnitDebug:
    name: str
    alternatives: tuple[str, ...]
    alternatives_in_prefilter: tuple[str, ...]
    alternatives_selected: tuple[str, ...]


@dataclass(frozen=True)
class KnapsackDebugCase:
    content_id: str
    question_id: str
    category: str
    budget: int
    complete_hit: bool
    evidence_f1: float
    selected_ids: tuple[str, ...]
    token_used: int
    missing_required_units: tuple[str, ...]
    selected_distractors: tuple[str, ...]
    failure_cause: str
    top_candidates: tuple[CandidateDebug, ...]
    required_units: tuple[RequiredUnitDebug, ...]


@dataclass(frozen=True)
class KnapsackDebugReport:
    cases: tuple[KnapsackDebugCase, ...]
    failure_cause_counts: dict[str, int]


@dataclass(frozen=True)
class KnapsackDebugReportFiles:
    debug_json: Path
    debug_md: Path


def debug_knapsack(
    contents: tuple[ContentCollection, ...],
    max_candidates: int = 10,
    weights: FeatureWeights = FeatureWeights(),
) -> KnapsackDebugReport:
    cases = []
    for content in contents:
        paragraphs_by_id = {paragraph.id: paragraph for paragraph in content.paragraphs}
        for question in content.questions:
            for budget in BUDGETS:
                cases.append(
                    _debug_case(
                        content.id,
                        question,
                        content.paragraphs,
                        paragraphs_by_id,
                        budget,
                        max_candidates,
                        weights,
                    )
                )
    counts = Counter(case.failure_cause for case in cases if not case.complete_hit)
    return KnapsackDebugReport(cases=tuple(cases), failure_cause_counts=dict(counts))


def create_knapsack_debug_report(
    contents: tuple[ContentCollection, ...],
    output_dir: Path,
) -> KnapsackDebugReportFiles:
    output_dir.mkdir(parents=True, exist_ok=True)
    report = debug_knapsack(contents)
    debug_json = output_dir / "knapsack_debug.json"
    debug_md = output_dir / "knapsack_debug.md"
    debug_json.write_text(
        json.dumps(
            {
                "failure_cause_counts": report.failure_cause_counts,
                "cases": [_json_ready(asdict(case)) for case in report.cases],
            },
            indent=2,
        ),
        encoding="utf-8",
    )
    debug_md.write_text(_markdown(report), encoding="utf-8")
    return KnapsackDebugReportFiles(debug_json=debug_json, debug_md=debug_md)


def _debug_case(
    content_id: str,
    question: Question,
    paragraphs: tuple[Paragraph, ...],
    paragraphs_by_id: dict[str, Paragraph],
    budget: int,
    max_candidates: int,
    weights: FeatureWeights,
) -> KnapsackDebugCase:
    utility = build_feature_utility(question, paragraphs, weights)
    top = select_feature_candidates(question, paragraphs, max_candidates, weights)
    top_ids = frozenset(paragraph.id for paragraph in top)
    required_ids = frozenset(
        item for unit in question.required_evidence_units for item in unit.alternatives
    )
    relevant_ids = frozenset(
        item
        for unit in question.required_evidence_units + question.optional_support_units
        for item in unit.alternatives
    )
    distractor_ids = frozenset(
        item for group in question.distractor_groups for item in group
    ) - relevant_ids

    result = feature_based_knapsack_selector(
        question,
        paragraphs,
        budget,
        max_candidates=max_candidates,
        weights=weights,
    )
    selected = frozenset(result.selected_ids)
    evaluation = evaluate_selection(question, result.selected_ids, budget, paragraphs_by_id)

    required_units = tuple(
        RequiredUnitDebug(
            name=unit.name,
            alternatives=unit.alternatives,
            alternatives_in_prefilter=tuple(item for item in unit.alternatives if item in top_ids),
            alternatives_selected=tuple(item for item in unit.alternatives if item in selected),
        )
        for unit in question.required_evidence_units
    )
    missing = tuple(
        unit.name for unit in required_units if not unit.alternatives_selected
    )
    selected_distractors = tuple(sorted(selected & distractor_ids))

    return KnapsackDebugCase(
        content_id=content_id,
        question_id=question.id,
        category=question.category,
        budget=budget,
        complete_hit=evaluation.complete_hit,
        evidence_f1=evaluation.evidence_f1,
        selected_ids=result.selected_ids,
        token_used=result.total_tokens,
        missing_required_units=missing,
        selected_distractors=selected_distractors,
        failure_cause=_failure_cause(missing, required_units, selected_distractors),
        top_candidates=tuple(
            CandidateDebug(
                id=paragraph.id,
                tokens=paragraph.tokens,
                individual_score=utility.individual.get(paragraph.id, 0.0),
                selected=paragraph.id in selected,
                is_required_alternative=paragraph.id in required_ids,
                is_distractor=paragraph.id in distractor_ids,
            )
            for paragraph in top
        ),
        required_units=required_units,
    )


def _failure_cause(
    missing: tuple[str, ...],
    required_units: tuple[RequiredUnitDebug, ...],
    selected_distractors: tuple[str, ...],
) -> str:
    if not missing:
        return "none"
    missing_units = [unit for unit in required_units if unit.name in missing]
    if any(not unit.alternatives_in_prefilter for unit in missing_units):
        return "prefilter_failure"
    if selected_distractors:
        return "distractor_failure"
    return "scoring_failure"


def _markdown(report: KnapsackDebugReport) -> str:
    lines = [
        "# Knapsack Debug Report",
        "",
        "## Failure Cause Summary",
        "",
    ]
    for cause, count in sorted(report.failure_cause_counts.items()):
        lines.append(f"- `{cause}`: {count}")
    lines.extend(["", "## Worst Cases", ""])
    worst = sorted(
        (case for case in report.cases if not case.complete_hit),
        key=lambda case: (case.evidence_f1, -len(case.selected_distractors), case.question_id),
    )[:12]
    for case in worst:
        lines.append(
            "- "
            f"{case.question_id} budget {case.budget}: "
            f"cause={case.failure_cause}, F1={case.evidence_f1:.3f}, "
            f"missing={list(case.missing_required_units)}, "
            f"distractors={list(case.selected_distractors)}, "
            f"selected={list(case.selected_ids)}"
        )
    lines.extend(
        [
            "",
            "## Next Tuning Direction",
            "",
            "- If `prefilter_failure` dominates, improve candidate ranking before changing optimizer weights.",
            "- If `scoring_failure` dominates, tune pair/triple synergy and redundancy penalties.",
            "- If `distractor_failure` dominates, add wrong-context or contradiction-aware features.",
            "- Do not tune on aggregate F1 alone; complete-hit and missing-unit recovery matter most.",
            "",
        ]
    )
    return "\n".join(lines)


def _json_ready(item):
    if isinstance(item, tuple):
        return list(item)
    if isinstance(item, dict):
        return {key: _json_ready(value) for key, value in item.items()}
    if isinstance(item, list):
        return [_json_ready(value) for value in item]
    return item
