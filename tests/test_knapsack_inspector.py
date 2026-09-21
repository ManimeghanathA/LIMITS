from pathlib import Path

from src.dataset_io import load_content_collections
from src.knapsack_inspector import create_knapsack_inspection_report, inspect_knapsack


def test_knapsack_inspector_creates_one_case_per_question_budget() -> None:
    contents = load_content_collections(Path("data/limits_dataset.json"))

    report = inspect_knapsack(contents)

    question_count = sum(len(content.questions) for content in contents)
    assert len(report.cases) == question_count * 4


def test_knapsack_inspector_records_score_breakdown_for_selected_subset() -> None:
    contents = load_content_collections(Path("data/limits_dataset.json"))

    report = inspect_knapsack(contents)
    case = next(item for item in report.cases if item.selected_ids)

    assert case.score_breakdown.total_score != 0
    assert case.candidate_rows
    assert all(row.importance_score is not None for row in case.candidate_rows)


def test_knapsack_inspection_report_writes_markdown(tmp_path: Path) -> None:
    contents = load_content_collections(Path("data/limits_dataset.json"))

    output = create_knapsack_inspection_report(contents, tmp_path)

    assert output.inspection_md.exists()
    text = output.inspection_md.read_text(encoding="utf-8")
    assert "Knapsack Question Inspection" in text
    assert "How To Read This Report" in text
    assert "Improvement Ideas" in text
