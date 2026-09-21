from pathlib import Path

from src.dataset_io import load_content_collections
from src.knapsack_debug import create_knapsack_debug_report, debug_knapsack
from src.knapsack_features import build_feature_utility, select_feature_candidates


class StaticSemanticScorer:
    def __init__(self, scores: dict[tuple[str, str], float] | None = None) -> None:
        self.scores = scores or {}

    def similarity(self, left: str, right: str) -> float:
        return self.scores.get((left, right), self.scores.get((right, left), 0.0))


def test_knapsack_debug_identifies_remaining_scoring_failures_after_prefilter_expansion() -> None:
    contents = load_content_collections(Path("data/limits_dataset.json"))

    report = debug_knapsack(contents)
    failure_causes = {case.failure_cause for case in report.cases if not case.complete_hit}

    assert report.failure_cause_counts.get("prefilter_failure", 0) == 0
    assert "scoring_failure" in failure_causes


def test_knapsack_debug_records_candidate_scores_and_missing_units() -> None:
    contents = load_content_collections(Path("data/limits_dataset.json"))

    report = debug_knapsack(contents)
    failed = next(case for case in report.cases if not case.complete_hit)

    assert failed.top_candidates
    assert failed.missing_required_units
    assert all(candidate.individual_score is not None for candidate in failed.top_candidates)


def test_knapsack_debug_report_writes_json_and_markdown(tmp_path: Path) -> None:
    contents = load_content_collections(Path("data/limits_dataset.json"))

    output = create_knapsack_debug_report(contents, tmp_path)

    assert output.debug_json.exists()
    assert output.debug_md.exists()
    text = output.debug_md.read_text(encoding="utf-8")
    assert "Knapsack Debug Report" in text
    assert "Failure Cause Summary" in text
    assert "Next Tuning Direction" in text


def test_feature_candidate_prefilter_keeps_bridge_evidence_with_low_query_overlap() -> None:
    contents = load_content_collections(Path("data/limits_dataset.json"))
    clinic = next(content for content in contents if content.id == "content_02_clinic_access")
    question = next(question for question in clinic.questions if question.id == "c_q01_direct")
    by_id = {paragraph.id: paragraph for paragraph in clinic.paragraphs}
    scorer = StaticSemanticScorer({(by_id["c01"].text, by_id["c02"].text): 0.9})

    candidates = select_feature_candidates(
        question,
        clinic.paragraphs,
        budget=128,
        max_candidates=15,
        semantic_scorer=scorer,
    )
    candidate_ids = {paragraph.id for paragraph in candidates}

    assert "c01" in candidate_ids
    assert "c02" in candidate_ids


def test_feature_utility_values_seed_linked_bridge_evidence_above_unlinked_chunks() -> None:
    contents = load_content_collections(Path("data/limits_dataset.json"))
    clinic = next(content for content in contents if content.id == "content_02_clinic_access")
    question = next(question for question in clinic.questions if question.id == "c_q01_direct")

    utility = build_feature_utility(
        question,
        clinic.paragraphs,
        budget=128,
        semantic_scorer=StaticSemanticScorer(),
    )

    assert utility.individual["c02"] > utility.individual["c21"]


def test_feature_utility_rewards_connected_bridge_pairs() -> None:
    contents = load_content_collections(Path("data/limits_dataset.json"))
    clinic = next(content for content in contents if content.id == "content_02_clinic_access")
    question = next(question for question in clinic.questions if question.id == "c_q08_two_hop")

    utility = build_feature_utility(
        question,
        clinic.paragraphs,
        budget=128,
        semantic_scorer=StaticSemanticScorer(),
    )

    assert utility.pair_synergy[frozenset({"c30", "c31"})] > 0
