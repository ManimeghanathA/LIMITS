from pathlib import Path

from src.benchmark import (
    BASELINE_METHODS,
    aggregate_results,
    create_baseline_report,
    run_baseline_benchmark,
)
from src.dataset import BUDGETS
from src.dataset_io import load_content_collections


def test_run_baseline_benchmark_returns_one_row_per_method_question_and_budget() -> None:
    contents = load_content_collections(Path("data/limits_dataset.json"))

    rows = run_baseline_benchmark(contents)

    expected_count = 15 * len(BUDGETS) * len(BASELINE_METHODS)
    assert len(rows) == expected_count
    assert {row.method for row in rows} == set(BASELINE_METHODS)
    assert all(row.token_used <= row.budget for row in rows)


def test_aggregate_results_reports_method_level_metrics() -> None:
    contents = load_content_collections(Path("data/limits_dataset.json"))

    summary = aggregate_results(run_baseline_benchmark(contents))

    assert set(summary.method_summaries) == set(BASELINE_METHODS)
    for method_summary in summary.method_summaries.values():
        assert 0.0 <= method_summary.average_evidence_f1 <= 1.0
        assert 0.0 <= method_summary.complete_hit_rate <= 1.0
        assert 0.0 <= method_summary.average_budget_utilization <= 1.0


def test_create_baseline_report_writes_json_csv_and_collage(tmp_path: Path) -> None:
    contents = load_content_collections(Path("data/limits_dataset.json"))

    report = create_baseline_report(contents, tmp_path)

    assert report.rows_json.exists()
    assert report.summary_json.exists()
    assert report.rows_csv.exists()
    assert report.collage_png.exists()
    assert report.collage_png.stat().st_size > 0
