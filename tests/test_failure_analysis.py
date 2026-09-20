from pathlib import Path

from src.dataset_io import load_content_collections
from src.failure_analysis import (
    analyze_benchmark_failures,
    create_failure_analysis_report,
)


def test_failure_analysis_records_knapsack_missing_units_and_distractors() -> None:
    contents = load_content_collections(Path("data/limits_dataset.json"))

    analysis = analyze_benchmark_failures(contents)
    knapsack_rows = [row for row in analysis.rows if row.method == "feature_knapsack"]

    assert knapsack_rows
    assert any(row.missing_required_units for row in knapsack_rows)
    assert any(row.selected_distractors for row in knapsack_rows)


def test_failure_analysis_contains_method_reasoning_for_non_knapsack_methods() -> None:
    contents = load_content_collections(Path("data/limits_dataset.json"))

    analysis = analyze_benchmark_failures(contents)

    assert "budget_fill" in analysis.method_reasoning
    assert "keyword_overlap" in analysis.method_reasoning
    assert "random" in analysis.method_reasoning
    assert "feature_knapsack" not in analysis.method_reasoning


def test_failure_analysis_report_writes_json_and_markdown(tmp_path: Path) -> None:
    contents = load_content_collections(Path("data/limits_dataset.json"))

    report = create_failure_analysis_report(contents, tmp_path)

    assert report.analysis_json.exists()
    assert report.analysis_md.exists()
    markdown = report.analysis_md.read_text(encoding="utf-8")
    assert "Feature Knapsack Deep Analysis" in markdown
    assert "Bias Risks" in markdown
    assert "Formula Tuning Targets" in markdown
