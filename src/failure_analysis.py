from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from pathlib import Path

from src.benchmark import BenchmarkRow, run_baseline_benchmark
from src.dataset import ContentCollection, Question


@dataclass(frozen=True)
class FailureAnalysisRow:
    method: str
    content_id: str
    question_id: str
    category: str
    budget: int
    selected_ids: tuple[str, ...]
    complete_hit: bool
    evidence_f1: float
    required_unit_recall: float
    optional_support_recall: float
    token_used: int
    missing_required_units: tuple[str, ...]
    covered_required_units: tuple[str, ...]
    covered_optional_units: tuple[str, ...]
    selected_distractors: tuple[str, ...]
    extra_selected_ids: tuple[str, ...]


@dataclass(frozen=True)
class FailureAnalysis:
    rows: tuple[FailureAnalysisRow, ...]
    method_reasoning: dict[str, str]
    knapsack_findings: tuple[str, ...]
    bias_risks: tuple[str, ...]
    tuning_targets: tuple[str, ...]


@dataclass(frozen=True)
class FailureAnalysisReport:
    analysis_json: Path
    analysis_md: Path


METHOD_REASONING = {
    "budget_fill": "A position-order sanity baseline that fills budget without understanding the query.",
    "keyword_overlap": "A query-aware lexical baseline that exposes whether interaction terms add value.",
    "random": "A stochastic lower-bound baseline showing the task is not solved by candidate density alone.",
}


def analyze_benchmark_failures(contents: tuple[ContentCollection, ...]) -> FailureAnalysis:
    benchmark_rows = run_baseline_benchmark(contents)
    question_by_key = {
        (content.id, question.id): question
        for content in contents
        for question in content.questions
    }
    rows = tuple(
        _analyze_row(row, question_by_key[(row.content_id, row.question_id)])
        for row in benchmark_rows
    )
    knapsack_rows = tuple(row for row in rows if row.method == "feature_knapsack")
    return FailureAnalysis(
        rows=rows,
        method_reasoning=METHOD_REASONING,
        knapsack_findings=_knapsack_findings(knapsack_rows),
        bias_risks=_bias_risks(),
        tuning_targets=_tuning_targets(knapsack_rows),
    )


def create_failure_analysis_report(
    contents: tuple[ContentCollection, ...],
    output_dir: Path,
) -> FailureAnalysisReport:
    output_dir.mkdir(parents=True, exist_ok=True)
    analysis = analyze_benchmark_failures(contents)
    analysis_json = output_dir / "failure_analysis.json"
    analysis_md = output_dir / "failure_analysis.md"
    analysis_json.write_text(
        json.dumps(
            {
                "rows": [_json_ready(asdict(row)) for row in analysis.rows],
                "method_reasoning": analysis.method_reasoning,
                "knapsack_findings": list(analysis.knapsack_findings),
                "bias_risks": list(analysis.bias_risks),
                "tuning_targets": list(analysis.tuning_targets),
            },
            indent=2,
        ),
        encoding="utf-8",
    )
    analysis_md.write_text(_markdown(analysis), encoding="utf-8")
    return FailureAnalysisReport(analysis_json=analysis_json, analysis_md=analysis_md)


def _analyze_row(row: BenchmarkRow, question: Question) -> FailureAnalysisRow:
    selected = frozenset(row.selected_ids)
    required = question.required_evidence_units
    optional = question.optional_support_units
    relevant_ids = frozenset(
        item for unit in required + optional for item in unit.alternatives
    )
    distractor_ids = frozenset(
        item for group in question.distractor_groups for item in group
    ) - relevant_ids
    return FailureAnalysisRow(
        method=row.method,
        content_id=row.content_id,
        question_id=row.question_id,
        category=row.category,
        budget=row.budget,
        selected_ids=row.selected_ids,
        complete_hit=row.complete_hit,
        evidence_f1=row.evidence_f1,
        required_unit_recall=row.required_unit_recall,
        optional_support_recall=row.optional_support_recall,
        token_used=row.token_used,
        missing_required_units=tuple(
            unit.name for unit in required if selected.isdisjoint(unit.alternatives)
        ),
        covered_required_units=tuple(
            unit.name for unit in required if not selected.isdisjoint(unit.alternatives)
        ),
        covered_optional_units=tuple(
            unit.name for unit in optional if not selected.isdisjoint(unit.alternatives)
        ),
        selected_distractors=tuple(sorted(selected & distractor_ids)),
        extra_selected_ids=tuple(sorted(selected - relevant_ids)),
    )


def _knapsack_findings(rows: tuple[FailureAnalysisRow, ...]) -> tuple[str, ...]:
    total = len(rows)
    complete = sum(row.complete_hit for row in rows)
    distractor_cases = sum(bool(row.selected_distractors) for row in rows)
    missing_cases = sum(bool(row.missing_required_units) for row in rows)
    avg_tokens = sum(row.token_used for row in rows) / total if total else 0.0
    return (
        f"Feature knapsack completed {complete}/{total} method-question-budget cases.",
        f"It missed at least one required evidence unit in {missing_cases}/{total} cases.",
        f"It selected at least one distractor in {distractor_cases}/{total} cases.",
        f"Average selected token count is {avg_tokens:.1f}, so it often stops below larger budgets.",
    )


def _bias_risks() -> tuple[str, ...]:
    return (
        "Lexical overlap bias: query words can dominate when useful chunks use different wording.",
        "Prefilter bias: exact optimization only sees the top-ranked candidate subset.",
        "Short chunk bias: candidate ranking prefers lower token cost on ties.",
        "Synthetic wording bias: current formulas may fit the first authored content style.",
        "Distractor overlap bias: same-entity wrong facts can look valuable under keyword coverage.",
    )


def _tuning_targets(rows: tuple[FailureAnalysisRow, ...]) -> tuple[str, ...]:
    category_failures: dict[str, int] = {}
    for row in rows:
        if not row.complete_hit:
            category_failures[row.category] = category_failures.get(row.category, 0) + 1
    worst_category = max(category_failures, key=category_failures.get, default="none")
    return (
        f"Prioritize complete-hit recovery in category: {worst_category}.",
        "Reduce distractor selection before increasing optional-support reward.",
        "Inspect whether failures come from prefilter loss or utility scoring after prefiltering.",
        "Tune redundancy and complementarity weights only after checking missing-unit patterns.",
    )


def _markdown(analysis: FailureAnalysis) -> str:
    lines = ["# Baseline Failure Analysis", "", "## Method Reasoning", ""]
    for method, reasoning in analysis.method_reasoning.items():
        lines.append(f"- `{method}`: {reasoning}")
    lines.extend(["", "## Feature Knapsack Deep Analysis", ""])
    for finding in analysis.knapsack_findings:
        lines.append(f"- {finding}")
    lines.extend(["", "### Bias Risks", ""])
    for risk in analysis.bias_risks:
        lines.append(f"- {risk}")
    lines.extend(["", "### Formula Tuning Targets", ""])
    for target in analysis.tuning_targets:
        lines.append(f"- {target}")
    lines.extend(["", "## Worst Feature-Knapsack Cases", ""])
    worst = sorted(
        (row for row in analysis.rows if row.method == "feature_knapsack"),
        key=lambda row: (row.complete_hit, row.evidence_f1, -len(row.selected_distractors)),
    )[:10]
    for row in worst:
        lines.append(
            "- "
            f"{row.question_id} budget {row.budget}: "
            f"F1={row.evidence_f1:.3f}, complete={row.complete_hit}, "
            f"missing={list(row.missing_required_units)}, "
            f"distractors={list(row.selected_distractors)}, "
            f"selected={list(row.selected_ids)}"
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
