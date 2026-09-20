from pathlib import Path

from src.dataset import BUDGETS, validate_content
from src.dataset_io import load_content_collections


def test_loads_and_validates_first_dataset_content() -> None:
    dataset_path = Path("data/limits_dataset.json")

    contents = load_content_collections(dataset_path)

    assert len(contents) == 1
    content = contents[0]
    validate_content(content)
    assert content.id == "content_01_aero_support"
    assert len(content.questions) == 15
    assert len(content.paragraphs) >= 30
    assert sum(paragraph.tokens for paragraph in content.paragraphs) > 1024
    assert all(set(question.budget_ground_truth) == set(BUDGETS) for question in content.questions)


def test_first_dataset_content_has_required_question_categories() -> None:
    contents = load_content_collections(Path("data/limits_dataset.json"))
    content = contents[0]

    category_counts = {
        category: sum(question.category == category for question in content.questions)
        for category in ("direct", "two_hop", "three_hop")
    }

    assert category_counts == {"direct": 5, "two_hop": 5, "three_hop": 5}


def test_direct_dataset_questions_can_use_multi_paragraph_support_without_hop_synergy() -> None:
    contents = load_content_collections(Path("data/limits_dataset.json"))
    direct_questions = [
        question for question in contents[0].questions if question.category == "direct"
    ]

    assert any(
        len(question.required_evidence_units) > 1
        for question in direct_questions
    )


def test_first_dataset_content_has_mixed_evidence_patterns() -> None:
    content = load_content_collections(Path("data/limits_dataset.json"))[0]

    assert any(
        question.category == "two_hop"
        and len(question.required_evidence_units) >= 3
        for question in content.questions
    )
    assert any(
        question.category == "three_hop"
        and len(question.required_evidence_units) >= 4
        for question in content.questions
    )


def test_each_budget_can_have_multiple_acceptable_ground_truth_selections() -> None:
    content = load_content_collections(Path("data/limits_dataset.json"))[0]

    assert any(
        len(question.budget_ground_truth[128]) > 1
        for question in content.questions
    )
    assert any(
        len(question.budget_ground_truth[budget]) > 1
        for question in content.questions
        for budget in BUDGETS
    )


def test_higher_budgets_add_useful_support_for_most_questions() -> None:
    content = load_content_collections(Path("data/limits_dataset.json"))[0]

    broader_questions = 0
    for question in content.questions:
        smallest_selection_size = min(
            len(selection.selected) for selection in question.budget_ground_truth[128]
        )
        largest_selection_size = max(
            len(selection.selected) for selection in question.budget_ground_truth[1024]
        )
        if largest_selection_size > smallest_selection_size:
            broader_questions += 1

    assert broader_questions >= 12


def test_wrong_similar_chunks_are_distractors_not_valid_alternatives() -> None:
    content = load_content_collections(Path("data/limits_dataset.json"))[0]
    question = next(item for item in content.questions if item.id == "q03_direct")
    alternatives = {
        alternative
        for unit in question.required_evidence_units + question.optional_support_units
        for alternative in unit.alternatives
    }
    distractors = {item for group in question.distractor_groups for item in group}

    assert "p17" not in alternatives
    assert "p17" in distractors


def test_multi_hop_budget_answers_are_scattered_in_candidate_order() -> None:
    content = load_content_collections(Path("data/limits_dataset.json"))[0]
    position_by_id = {
        paragraph.id: index for index, paragraph in enumerate(content.paragraphs)
    }

    for question in content.questions:
        if question.category == "direct":
            continue
        for selection in question.budget_ground_truth[128]:
            positions = [position_by_id[evidence_id] for evidence_id in selection.selected]
            assert max(positions) - min(positions) >= 4
