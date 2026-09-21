from __future__ import annotations

import csv
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from statistics import mean

from PIL import Image, ImageDraw, ImageFont

from src.dataset import BUDGETS, ContentCollection, Paragraph, Question
from src.evaluator import evaluate_selection
from src.knapsack_features import feature_based_knapsack_selector
from src.selectors import budget_fill_selector, keyword_overlap_selector, random_selector


BASELINE_METHODS = ("budget_fill", "keyword_overlap", "random", "feature_knapsack")


@dataclass(frozen=True)
class BenchmarkRow:
    method: str
    content_id: str
    question_id: str
    category: str
    budget: int
    selected_ids: tuple[str, ...]
    token_used: int
    budget_utilization: float
    required_unit_recall: float
    complete_hit: bool
    optional_support_recall: float
    evidence_precision: float
    evidence_f1: float
    extra_chunk_count: int
    distractor_count: int
    ground_truth_selection_hit: bool
    best_ground_truth_jaccard: float


@dataclass(frozen=True)
class MethodSummary:
    method: str
    average_evidence_f1: float
    complete_hit_rate: float
    average_required_recall: float
    average_optional_support_recall: float
    average_budget_utilization: float
    average_distractor_count: float


@dataclass(frozen=True)
class BenchmarkSummary:
    row_count: int
    method_summaries: dict[str, MethodSummary]


@dataclass(frozen=True)
class BenchmarkReport:
    rows_json: Path
    summary_json: Path
    rows_csv: Path
    collage_png: Path


def run_baseline_benchmark(contents: tuple[ContentCollection, ...]) -> tuple[BenchmarkRow, ...]:
    rows: list[BenchmarkRow] = []
    for content in contents:
        paragraphs = content.paragraphs
        paragraphs_by_id = {paragraph.id: paragraph for paragraph in paragraphs}
        for question in content.questions:
            for budget in BUDGETS:
                for method in BASELINE_METHODS:
                    selected = _select(method, question, paragraphs, budget)
                    evaluation = evaluate_selection(
                        question=question,
                        selected_ids=selected,
                        budget=budget,
                        paragraphs_by_id=paragraphs_by_id,
                    )
                    rows.append(
                        BenchmarkRow(
                            method=method,
                            content_id=content.id,
                            question_id=question.id,
                            category=question.category,
                            budget=budget,
                            selected_ids=selected,
                            token_used=evaluation.token_used,
                            budget_utilization=evaluation.budget_utilization,
                            required_unit_recall=evaluation.required_unit_recall,
                            complete_hit=evaluation.complete_hit,
                            optional_support_recall=evaluation.optional_support_recall,
                            evidence_precision=evaluation.evidence_precision,
                            evidence_f1=evaluation.evidence_f1,
                            extra_chunk_count=evaluation.extra_chunk_count,
                            distractor_count=evaluation.distractor_count,
                            ground_truth_selection_hit=evaluation.ground_truth_selection_hit,
                            best_ground_truth_jaccard=evaluation.best_ground_truth_jaccard,
                        )
                    )
    return tuple(rows)


def aggregate_results(rows: tuple[BenchmarkRow, ...]) -> BenchmarkSummary:
    method_summaries = {}
    for method in BASELINE_METHODS:
        method_rows = tuple(row for row in rows if row.method == method)
        method_summaries[method] = MethodSummary(
            method=method,
            average_evidence_f1=_mean(row.evidence_f1 for row in method_rows),
            complete_hit_rate=_mean(float(row.complete_hit) for row in method_rows),
            average_required_recall=_mean(row.required_unit_recall for row in method_rows),
            average_optional_support_recall=_mean(
                row.optional_support_recall for row in method_rows
            ),
            average_budget_utilization=_mean(
                min(row.budget_utilization, 1.0) for row in method_rows
            ),
            average_distractor_count=_mean(row.distractor_count for row in method_rows),
        )
    return BenchmarkSummary(row_count=len(rows), method_summaries=method_summaries)


def create_baseline_report(
    contents: tuple[ContentCollection, ...],
    output_dir: Path,
) -> BenchmarkReport:
    output_dir.mkdir(parents=True, exist_ok=True)
    rows = run_baseline_benchmark(contents)
    summary = aggregate_results(rows)

    rows_json = output_dir / "baseline_rows.json"
    summary_json = output_dir / "baseline_summary.json"
    rows_csv = output_dir / "baseline_rows.csv"
    collage_png = output_dir / "baseline_collage.png"

    rows_json.write_text(
        json.dumps([_json_ready(asdict(row)) for row in rows], indent=2),
        encoding="utf-8",
    )
    summary_json.write_text(
        json.dumps(
            {
                "row_count": summary.row_count,
                "method_summaries": {
                    method: asdict(method_summary)
                    for method, method_summary in summary.method_summaries.items()
                },
            },
            indent=2,
        ),
        encoding="utf-8",
    )
    _write_csv(rows_csv, rows)
    _write_collage(collage_png, rows, summary)

    return BenchmarkReport(
        rows_json=rows_json,
        summary_json=summary_json,
        rows_csv=rows_csv,
        collage_png=collage_png,
    )


def _select(
    method: str,
    question: Question,
    paragraphs: tuple[Paragraph, ...],
    budget: int,
) -> tuple[str, ...]:
    if method == "budget_fill":
        return budget_fill_selector(paragraphs, budget)
    if method == "keyword_overlap":
        return keyword_overlap_selector(question.text, paragraphs, budget)
    if method == "random":
        seed = hash((question.id, budget, method)) & 0xFFFFFFFF
        return random_selector(paragraphs, budget, seed=seed)
    if method == "feature_knapsack":
        return feature_based_knapsack_selector(
            question,
            paragraphs,
            budget,
        ).selected_ids
    raise ValueError(f"unknown method: {method}")


def _write_csv(path: Path, rows: tuple[BenchmarkRow, ...]) -> None:
    fieldnames = [field for field in asdict(rows[0])] if rows else []
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            item = _json_ready(asdict(row))
            writer.writerow(item)


def _write_collage(path: Path, rows: tuple[BenchmarkRow, ...], summary: BenchmarkSummary) -> None:
    panels = (
        _bar_panel(
            "Complete Hit Rate",
            {method: item.complete_hit_rate for method, item in summary.method_summaries.items()},
        ),
        _bar_panel(
            "Average Evidence F1",
            {method: item.average_evidence_f1 for method, item in summary.method_summaries.items()},
        ),
        _line_panel("Evidence F1 vs Budget", rows, "evidence_f1"),
        _line_panel("Complete Hit vs Budget", rows, "complete_hit"),
        _bar_panel(
            "Budget Utilization",
            {
                method: item.average_budget_utilization
                for method, item in summary.method_summaries.items()
            },
        ),
        _bar_panel(
            "Distractor Count",
            {
                method: min(item.average_distractor_count, 1.0)
                for method, item in summary.method_summaries.items()
            },
        ),
    )
    width, height = 1200, 900
    image = Image.new("RGB", (width, height), "white")
    positions = ((0, 0), (400, 0), (800, 0), (0, 450), (400, 450), (800, 450))
    for panel, position in zip(panels, positions):
        image.paste(panel, position)
    image.save(path)


def _bar_panel(title: str, values: dict[str, float]) -> Image.Image:
    image = Image.new("RGB", (400, 450), "#ffffff")
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default()
    draw.text((18, 18), title, fill="#111111", font=font)
    colors = _method_colors()
    bar_width = 62
    base_y = 370
    max_height = 250
    for index, method in enumerate(BASELINE_METHODS):
        value = values.get(method, 0.0)
        height = int(max(0.0, min(value, 1.0)) * max_height)
        x = 28 + index * 90
        draw.rectangle((x, base_y - height, x + bar_width, base_y), fill=colors[method])
        draw.text((x, base_y + 12), method.replace("_", "\n"), fill="#111111", font=font)
        draw.text((x, base_y - height - 18), f"{value:.2f}", fill="#111111", font=font)
    draw.line((30, base_y, 370, base_y), fill="#333333")
    return image


def _line_panel(title: str, rows: tuple[BenchmarkRow, ...], metric: str) -> Image.Image:
    image = Image.new("RGB", (400, 450), "#ffffff")
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default()
    draw.text((18, 18), title, fill="#111111", font=font)
    colors = _method_colors()
    left, top, right, bottom = 55, 70, 360, 370
    draw.rectangle((left, top, right, bottom), outline="#cccccc")
    x_by_budget = {
        budget: left + int((right - left) * index / (len(BUDGETS) - 1))
        for index, budget in enumerate(BUDGETS)
    }
    for budget, x in x_by_budget.items():
        draw.text((x - 16, bottom + 12), str(budget), fill="#111111", font=font)
    for method in BASELINE_METHODS:
        points = []
        for budget in BUDGETS:
            budget_rows = [
                row for row in rows if row.method == method and row.budget == budget
            ]
            value = _mean(float(getattr(row, metric)) for row in budget_rows)
            x = x_by_budget[budget]
            y = bottom - int(max(0.0, min(value, 1.0)) * (bottom - top))
            points.append((x, y))
            draw.ellipse((x - 4, y - 4, x + 4, y + 4), fill=colors[method])
        draw.line(points, fill=colors[method], width=3)
    legend_y = 395
    for index, method in enumerate(BASELINE_METHODS):
        x = 15 + index * 95
        draw.rectangle((x, legend_y, x + 10, legend_y + 10), fill=colors[method])
        draw.text((x + 14, legend_y - 2), method, fill="#111111", font=font)
    return image


def _method_colors() -> dict[str, str]:
    return {
        "budget_fill": "#4c78a8",
        "keyword_overlap": "#f58518",
        "random": "#54a24b",
        "feature_knapsack": "#b279a2",
    }


def _json_ready(item):
    if isinstance(item, tuple):
        return list(item)
    if isinstance(item, dict):
        return {key: _json_ready(value) for key, value in item.items()}
    if isinstance(item, list):
        return [_json_ready(value) for value in item]
    return item


def _mean(values) -> float:
    values = tuple(values)
    if not values:
        return 0.0
    return mean(values)
