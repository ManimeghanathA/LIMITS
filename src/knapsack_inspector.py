from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from pathlib import Path

from src.dataset import BUDGETS, ContentCollection, Paragraph, Question
from src.evaluator import evaluate_selection
from src.knapsack_features import (
    FeatureWeights,
    build_candidate_input,
    build_feature_utility,
    feature_based_knapsack_selector,
    select_feature_candidates,
)
from src.utility import InteractionUtility


@dataclass(frozen=True)
class ScoreBreakdown:
    individual_sum: float
    pair_synergy_sum: float
    triple_synergy_sum: float
    redundancy_penalty: float
    total_score: float


@dataclass(frozen=True)
class CandidateInspectionRow:
    id: str
    tokens: int
    importance_score: float
    selected: bool
    is_required_alternative: bool
    is_optional_alternative: bool
    is_distractor: bool
    text: str


@dataclass(frozen=True)
class KnapsackInspectionCase:
    content_id: str
    question_id: str
    category: str
    question: str
    budget: int
    complete_hit: bool
    evidence_f1: float
    required_recall: float
    selected_ids: tuple[str, ...]
    token_used: int
    missing_required_units: tuple[str, ...]
    selected_distractors: tuple[str, ...]
    score_breakdown: ScoreBreakdown
    candidate_rows: tuple[CandidateInspectionRow, ...]
    improvement_hint: str


@dataclass(frozen=True)
class KnapsackInspectionReport:
    cases: tuple[KnapsackInspectionCase, ...]


@dataclass(frozen=True)
class KnapsackInspectionReportFiles:
    inspection_json: Path
    inspection_md: Path


def inspect_knapsack(
    contents: tuple[ContentCollection, ...],
    max_candidates: int = 15,
    weights: FeatureWeights = FeatureWeights(),
) -> KnapsackInspectionReport:
    cases: list[KnapsackInspectionCase] = []
    for content in contents:
        paragraphs_by_id = {paragraph.id: paragraph for paragraph in content.paragraphs}
        for question in content.questions:
            for budget in BUDGETS:
                cases.append(
                    _inspect_case(
                        content.id,
                        question,
                        content.paragraphs,
                        paragraphs_by_id,
                        budget,
                        max_candidates,
                        weights,
                    )
                )
    return KnapsackInspectionReport(cases=tuple(cases))


def create_knapsack_inspection_report(
    contents: tuple[ContentCollection, ...],
    output_dir: Path,
) -> KnapsackInspectionReportFiles:
    output_dir.mkdir(parents=True, exist_ok=True)
    report = inspect_knapsack(contents)
    inspection_json = output_dir / "knapsack_inspection.json"
    inspection_md = output_dir / "knapsack_inspection.md"
    inspection_json.write_text(
        json.dumps([_json_ready(asdict(case)) for case in report.cases], indent=2),
        encoding="utf-8",
    )
    inspection_md.write_text(_markdown(report), encoding="utf-8")
    return KnapsackInspectionReportFiles(
        inspection_json=inspection_json,
        inspection_md=inspection_md,
    )


def _inspect_case(
    content_id: str,
    question: Question,
    paragraphs: tuple[Paragraph, ...],
    paragraphs_by_id: dict[str, Paragraph],
    budget: int,
    max_candidates: int,
    weights: FeatureWeights,
) -> KnapsackInspectionCase:
    candidates = select_feature_candidates(question, paragraphs, budget, max_candidates, weights)
    public = build_candidate_input(question, candidates, budget)
    utility = build_feature_utility(question, candidates, budget, weights)
    result = feature_based_knapsack_selector(
        question,
        paragraphs,
        budget,
        max_candidates=max_candidates,
        weights=weights,
    )
    evaluation = evaluate_selection(question, result.selected_ids, budget, paragraphs_by_id)
    selected = frozenset(result.selected_ids)
    required_ids = frozenset(
        item for unit in question.required_evidence_units for item in unit.alternatives
    )
    optional_ids = frozenset(
        item for unit in question.optional_support_units for item in unit.alternatives
    )
    relevant_ids = required_ids | optional_ids
    distractor_ids = frozenset(
        item for group in question.distractor_groups for item in group
    ) - relevant_ids
    selected_distractors = tuple(sorted(selected & distractor_ids))
    missing = tuple(
        unit.name
        for unit in question.required_evidence_units
        if selected.isdisjoint(unit.alternatives)
    )
    rows = tuple(
        CandidateInspectionRow(
            id=paragraph.id,
            tokens=paragraph.tokens,
            importance_score=utility.individual.get(paragraph.id, 0.0),
            selected=paragraph.id in selected,
            is_required_alternative=paragraph.id in required_ids,
            is_optional_alternative=paragraph.id in optional_ids,
            is_distractor=paragraph.id in distractor_ids,
            text=paragraph.text,
        )
        for paragraph in candidates
    )
    return KnapsackInspectionCase(
        content_id=content_id,
        question_id=question.id,
        category=question.category,
        question=question.text,
        budget=budget,
        complete_hit=evaluation.complete_hit,
        evidence_f1=evaluation.evidence_f1,
        required_recall=evaluation.required_unit_recall,
        selected_ids=result.selected_ids,
        token_used=result.total_tokens,
        missing_required_units=missing,
        selected_distractors=selected_distractors,
        score_breakdown=_score_breakdown(selected, utility),
        candidate_rows=rows,
        improvement_hint=_improvement_hint(missing, selected_distractors, result.total_tokens, public.token_budget),
    )


def _score_breakdown(selected: frozenset[str], utility: InteractionUtility) -> ScoreBreakdown:
    individual = sum(utility.individual.get(chunk_id, 0.0) for chunk_id in selected)
    pair_synergy = sum(score for key, score in utility.pair_synergy.items() if key <= selected)
    triple_synergy = sum(
        score for key, score in utility.triple_synergy.items() if key <= selected
    )
    redundancy = utility.redundancy_weight * sum(
        score for key, score in utility.pair_redundancy.items() if key <= selected
    )
    total = individual + pair_synergy + triple_synergy - redundancy
    return ScoreBreakdown(
        individual_sum=individual,
        pair_synergy_sum=pair_synergy,
        triple_synergy_sum=triple_synergy,
        redundancy_penalty=redundancy,
        total_score=total,
    )


def _improvement_hint(
    missing_required_units: tuple[str, ...],
    selected_distractors: tuple[str, ...],
    token_used: int,
    budget: int,
) -> str:
    if selected_distractors:
        return "Add wrong-context or contradiction-aware features; a distractor beat required evidence."
    if missing_required_units and token_used >= budget * 0.9:
        return "Tight-budget tradeoff; improve importance ranking so required evidence beats optional/filler chunks."
    if missing_required_units:
        return "Scoring issue; required evidence was available but not valuable enough under current utility."
    return "Successful selection; inspect extra chunks only if precision or token cost becomes the priority."


def _markdown(report: KnapsackInspectionReport) -> str:
    lines = [
        "# Knapsack Question Inspection",
        "",
        "## How To Read This Report",
        "",
        "- `importance` is the public individual score used before pair/triple interactions.",
        "- `individual`, `pair`, `triple`, and `redundancy` show why the selected subset won.",
        "- Required, optional, and distractor flags are evaluation labels only; the selector does not receive them.",
        "- Use failed cases to design public features, not to feed labels into inference.",
        "",
        "## Improvement Ideas",
        "",
        "- Estimate paragraph importance using query overlap plus connection to strong seed paragraphs.",
        "- Reward pairwise paragraph links when one chunk explains or completes another chunk.",
        "- Penalize extra chunks through a selection penalty so larger budgets do not force context bloat.",
        "- Next likely improvement: contradiction/wrong-context detection for chunks containing words such as `not`, `superseded`, `wrong`, or mismatched locations/departments.",
        "",
        "## Cases",
        "",
    ]
    for case in report.cases:
        marker = "PASS" if case.complete_hit else "FAIL"
        lines.extend(
            [
                f"### {marker} {case.content_id} / {case.question_id} / budget {case.budget}",
                "",
                f"Question: {case.question}",
                "",
                f"Selected: `{list(case.selected_ids)}`",
                f"Tokens: `{case.token_used}/{case.budget}`",
                f"F1: `{case.evidence_f1:.3f}` Required recall: `{case.required_recall:.3f}`",
                f"Missing required units: `{list(case.missing_required_units)}`",
                f"Selected distractors: `{list(case.selected_distractors)}`",
                "",
                "Score breakdown:",
                "",
                f"- individual: `{case.score_breakdown.individual_sum:.3f}`",
                f"- pair synergy: `{case.score_breakdown.pair_synergy_sum:.3f}`",
                f"- triple synergy: `{case.score_breakdown.triple_synergy_sum:.3f}`",
                f"- redundancy penalty: `{case.score_breakdown.redundancy_penalty:.3f}`",
                f"- total: `{case.score_breakdown.total_score:.3f}`",
                "",
                f"Improvement hint: {case.improvement_hint}",
                "",
                "| id | flags | importance | tokens | text |",
                "|---|---|---:|---:|---|",
            ]
        )
        for row in case.candidate_rows:
            flags = []
            if row.selected:
                flags.append("selected")
            if row.is_required_alternative:
                flags.append("required")
            if row.is_optional_alternative:
                flags.append("optional")
            if row.is_distractor:
                flags.append("distractor")
            lines.append(
                f"| `{row.id}` | {', '.join(flags) or '-'} | "
                f"{row.importance_score:.3f} | {row.tokens} | {row.text} |"
            )
        lines.append("")
    return "\n".join(lines)


def _json_ready(item):
    if isinstance(item, tuple):
        return list(item)
    if isinstance(item, dict):
        return {key: _json_ready(value) for key, value in item.items()}
    if isinstance(item, list):
        return [_json_ready(value) for value in item]
    return item
