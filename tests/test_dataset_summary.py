from pathlib import Path

from src.dataset_io import load_content_collections
from src.dataset_summary import summarize_content, summarize_dataset


def test_summarize_content_reports_core_dataset_shape() -> None:
    content = load_content_collections(Path("data/limits_dataset.json"))[0]

    summary = summarize_content(content)

    assert summary.content_id == "content_01_aero_support"
    assert summary.paragraph_count == 40
    assert summary.total_tokens > 1024
    assert summary.question_count == 15
    assert summary.category_counts == {"direct": 5, "two_hop": 5, "three_hop": 5}


def test_summarize_content_reports_evidence_and_budget_health() -> None:
    content = load_content_collections(Path("data/limits_dataset.json"))[0]

    summary = summarize_content(content)

    assert summary.average_required_units > 0
    assert summary.average_optional_units > 0
    assert summary.average_ground_truth_selections_by_budget[128] > 1
    assert summary.questions_with_budget_growth >= 12
    assert summary.redundancy_group_count > 0
    assert summary.distractor_group_count > 0


def test_summarize_dataset_aggregates_multiple_contents() -> None:
    content = load_content_collections(Path("data/limits_dataset.json"))[0]

    summary = summarize_dataset((content, content))

    assert summary.content_count == 2
    assert summary.paragraph_count == 80
    assert summary.question_count == 30
    assert summary.category_counts == {"direct": 10, "two_hop": 10, "three_hop": 10}
