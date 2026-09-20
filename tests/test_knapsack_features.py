from src.dataset import BudgetSelection, EvidenceUnit, Paragraph, Question
from src.knapsack_features import (
    build_candidate_input,
    build_feature_utility,
    feature_based_knapsack_selector,
)


def make_question() -> Question:
    return Question(
        id="q01",
        text="Where is the sensor cart staged during calibration?",
        answer="The sensor cart is staged beside Hangar 2.",
        category="two_hop",
        required_evidence_units=(
            EvidenceUnit("location", ("p01",)),
        ),
        optional_support_units=(),
        budget_ground_truth={
            128: (BudgetSelection(("p01",)),),
            256: (BudgetSelection(("p01",)),),
            512: (BudgetSelection(("p01",)),),
            1024: (BudgetSelection(("p01",)),),
        },
    )


def make_paragraphs() -> tuple[Paragraph, ...]:
    return (
        Paragraph("p01", "The sensor cart is staged beside Hangar 2.", 20),
        Paragraph("p02", "The sensor cart includes a red charging cable.", 18),
        Paragraph("p03", "Lunch arrives near Bay 7.", 22),
        Paragraph("p04", "Hangar 3 stores paint filters.", 19),
    )


def test_build_candidate_input_uses_public_question_and_paragraph_fields() -> None:
    public = build_candidate_input(make_question(), make_paragraphs(), budget=128)

    assert public.query == "Where is the sensor cart staged during calibration?"
    assert public.token_budget == 128
    assert [chunk.id for chunk in public.chunks] == ["p01", "p02", "p03", "p04"]
    assert public.chunks[0].token_cost == 20


def test_feature_utility_scores_query_matching_chunk_above_unrelated_chunk() -> None:
    utility = build_feature_utility(make_question(), make_paragraphs())

    assert utility.individual["p01"] > utility.individual["p03"]
    assert utility.individual["p02"] > utility.individual["p03"]


def test_feature_utility_adds_redundancy_for_overlapping_chunks() -> None:
    utility = build_feature_utility(make_question(), make_paragraphs())

    assert utility.pair_redundancy[frozenset({"p01", "p02"})] > 0


def test_feature_utility_adds_pair_synergy_for_complementary_query_coverage() -> None:
    paragraphs = (
        Paragraph("p01", "sensor cart", 10),
        Paragraph("p02", "staged calibration", 10),
        Paragraph("p03", "unrelated lunch", 10),
    )

    utility = build_feature_utility(make_question(), paragraphs)

    assert utility.pair_synergy[frozenset({"p01", "p02"})] > 0
    assert utility.pair_synergy.get(frozenset({"p01", "p03"}), 0.0) == 0.0


def test_feature_utility_does_not_depend_on_ground_truth_labels() -> None:
    question = make_question()
    changed_labels = Question(
        id=question.id,
        text=question.text,
        answer=question.answer,
        category=question.category,
        required_evidence_units=(EvidenceUnit("different", ("p03",)),),
        optional_support_units=(),
        budget_ground_truth=question.budget_ground_truth,
    )

    assert build_feature_utility(question, make_paragraphs()) == build_feature_utility(
        changed_labels, make_paragraphs()
    )


def test_feature_based_knapsack_selector_returns_budget_valid_selection() -> None:
    result = feature_based_knapsack_selector(
        make_question(),
        make_paragraphs(),
        budget=40,
        max_candidates=4,
    )

    assert result.total_tokens <= 40
    assert "p01" in result.selected_ids
