from src.dataset import BudgetSelection, EvidenceUnit, Paragraph, Question
from src.evaluator import EvaluationWeights, evaluate_selection, reward_from_evaluation


def make_paragraphs() -> dict[str, Paragraph]:
    return {
        "p01": Paragraph("p01", "Correct start time.", 20),
        "p02": Paragraph("p02", "Correct cart location.", 20),
        "p03": Paragraph("p03", "Alternative cart location.", 22),
        "p04": Paragraph("p04", "Optional owner.", 18),
        "p05": Paragraph("p05", "Wrong similar distractor.", 25),
        "p06": Paragraph("p06", "Unrelated extra detail.", 16),
    }


def make_question() -> Question:
    return Question(
        id="q01",
        text="When does calibration begin and where is the cart staged?",
        answer="It begins at 06:30 and the cart is staged beside Hangar 2.",
        category="direct",
        required_evidence_units=(
            EvidenceUnit("start_time", ("p01",)),
            EvidenceUnit("cart_location", ("p02", "p03")),
        ),
        optional_support_units=(
            EvidenceUnit("owner", ("p04",)),
        ),
        budget_ground_truth={
            128: (BudgetSelection(("p01", "p02")), BudgetSelection(("p01", "p03"))),
            256: (BudgetSelection(("p01", "p02", "p04")),),
            512: (BudgetSelection(("p01", "p02", "p03", "p04")),),
            1024: (BudgetSelection(("p01", "p02", "p03", "p04")),),
        },
        redundancy_groups=(("p02", "p03"),),
        distractor_groups=(("p05", "p01"),),
    )


def test_evaluator_scores_complete_selection_with_optional_support() -> None:
    result = evaluate_selection(
        make_question(),
        selected_ids=("p01", "p03", "p04"),
        budget=128,
        paragraphs_by_id=make_paragraphs(),
    )

    assert result.budget_valid is True
    assert result.token_used == 60
    assert result.required_units_covered == 2
    assert result.required_unit_recall == 1.0
    assert result.complete_hit is True
    assert result.optional_units_covered == 1
    assert result.optional_support_recall == 1.0
    assert result.evidence_precision == 1.0
    assert result.evidence_f1 == 1.0
    assert result.extra_chunk_count == 0
    assert result.distractor_count == 0


def test_evaluator_penalizes_missing_required_unit_and_distractor() -> None:
    result = evaluate_selection(
        make_question(),
        selected_ids=("p01", "p05"),
        budget=128,
        paragraphs_by_id=make_paragraphs(),
    )

    assert result.budget_valid is True
    assert result.required_units_covered == 1
    assert result.required_unit_recall == 0.5
    assert result.complete_hit is False
    assert result.evidence_precision == 0.5
    assert result.extra_chunk_count == 1
    assert result.distractor_count == 1


def test_evaluator_marks_over_budget_selection_invalid_but_still_scores_evidence() -> None:
    result = evaluate_selection(
        make_question(),
        selected_ids=("p01", "p02", "p04"),
        budget=50,
        paragraphs_by_id=make_paragraphs(),
    )

    assert result.token_used == 58
    assert result.budget_valid is False
    assert result.complete_hit is True
    assert result.optional_support_recall == 1.0


def test_evaluator_exposes_best_budget_ground_truth_overlap() -> None:
    result = evaluate_selection(
        make_question(),
        selected_ids=("p01", "p02", "p04", "p06"),
        budget=256,
        paragraphs_by_id=make_paragraphs(),
    )

    assert result.ground_truth_selection_hit is False
    assert result.best_ground_truth_jaccard == 0.75


def test_reward_prefers_complete_clean_selection_over_distractor_selection() -> None:
    clean = evaluate_selection(
        make_question(),
        selected_ids=("p01", "p02", "p04"),
        budget=128,
        paragraphs_by_id=make_paragraphs(),
    )
    noisy = evaluate_selection(
        make_question(),
        selected_ids=("p01", "p05"),
        budget=128,
        paragraphs_by_id=make_paragraphs(),
    )

    assert reward_from_evaluation(clean) > reward_from_evaluation(noisy)


def test_reward_weights_are_configurable_for_rl_experiments() -> None:
    result = evaluate_selection(
        make_question(),
        selected_ids=("p01", "p05"),
        budget=128,
        paragraphs_by_id=make_paragraphs(),
    )

    default_reward = reward_from_evaluation(result)
    harsh_reward = reward_from_evaluation(
        result,
        EvaluationWeights(distractor_penalty=2.0, extra_chunk_penalty=1.0),
    )

    assert harsh_reward < default_reward
