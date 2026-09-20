from pathlib import Path

from src.dataset_io import load_content_collections
from src.knapsack_debug import create_knapsack_debug_report, debug_knapsack


def test_knapsack_debug_identifies_prefilter_and_scoring_failures() -> None:
    contents = load_content_collections(Path("data/limits_dataset.json"))

    report = debug_knapsack(contents)
    failure_causes = {case.failure_cause for case in report.cases if not case.complete_hit}

    assert "prefilter_failure" in failure_causes
    assert "scoring_failure" in failure_causes


def test_knapsack_debug_records_candidate_scores_and_missing_units() -> None:
    contents = load_content_collections(Path("data/limits_dataset.json"))

    report = debug_knapsack(contents)
    failed = next(case for case in report.cases if not case.complete_hit)

    assert failed.top_candidates
    assert failed.missing_required_units
    assert all(candidate.individual_score >= 0 for candidate in failed.top_candidates)


def test_knapsack_debug_report_writes_json_and_markdown(tmp_path: Path) -> None:
    contents = load_content_collections(Path("data/limits_dataset.json"))

    output = create_knapsack_debug_report(contents, tmp_path)

    assert output.debug_json.exists()
    assert output.debug_md.exists()
    text = output.debug_md.read_text(encoding="utf-8")
    assert "Knapsack Debug Report" in text
    assert "Failure Cause Summary" in text
    assert "Next Tuning Direction" in text
