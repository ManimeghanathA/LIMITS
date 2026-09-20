import pytest

from src.dataset import (
    BUDGETS,
    BudgetSelection,
    ContentCollection,
    Paragraph,
    Question,
    validate_content,
)


def make_paragraphs() -> tuple[Paragraph, ...]:
    return tuple(
        Paragraph(id=f"p{i:02d}", text=f"Paragraph {i} contains curated information.", tokens=30 if i < 4 else 100)
        for i in range(1, 14)
    )


def make_question(category: str, index: int = 1) -> Question:
    size = {"direct": 1, "two_hop": 2, "three_hop": 3}[category]
    evidence = tuple(f"p{i:02d}" for i in range(1, size + 1))
    selections = {budget: BudgetSelection(selected=evidence) for budget in BUDGETS}
    return Question(
        id=f"{category}_{index}",
        text=f"A {category} question?",
        answer="Known answer",
        category=category,
        valid_evidence_sets=(evidence,),
        budget_ground_truth=selections,
    )


def make_collection() -> ContentCollection:
    questions = tuple(
        make_question(category, index)
        for category in ("direct", "two_hop", "three_hop")
        for index in range(1, 6)
    )
    return ContentCollection("content_01", make_paragraphs(), questions)


def test_valid_collection_has_all_categories_and_budgets() -> None:
    collection = make_collection()

    validate_content(collection)

    assert len(collection.questions) == 15
    assert set(collection.questions[0].budget_ground_truth) == set(BUDGETS)


def test_question_without_every_budget_is_rejected() -> None:
    question = make_question("direct")
    incomplete = Question(
        id=question.id,
        text=question.text,
        answer=question.answer,
        category=question.category,
        valid_evidence_sets=question.valid_evidence_sets,
        budget_ground_truth={128: BudgetSelection(("p01",))},
    )
    collection = ContentCollection(
        "content_01",
        make_collection().paragraphs,
        (incomplete,) + make_collection().questions[1:],
    )

    with pytest.raises(ValueError, match="all budgets"):
        validate_content(collection)


def test_ground_truth_must_be_answerable_and_fit_its_budget() -> None:
    question = make_question("three_hop")
    invalid_selections = dict(question.budget_ground_truth)
    invalid_selections[128] = BudgetSelection(("p01", "p02"))
    changed = Question(
        id=question.id,
        text=question.text,
        answer=question.answer,
        category=question.category,
        valid_evidence_sets=question.valid_evidence_sets,
        budget_ground_truth=invalid_selections,
    )
    questions = (changed,) + tuple(
        q for q in make_collection().questions if q.id != changed.id
    )

    with pytest.raises(ValueError, match="complete evidence"):
        validate_content(ContentCollection("content_01", make_paragraphs(), questions))


def test_smallest_budget_must_hold_the_required_evidence() -> None:
    paragraphs = list(make_paragraphs())
    paragraphs[0] = Paragraph("p01", "Long required paragraph", 90)
    paragraphs[1] = Paragraph("p02", "Another long required paragraph", 90)

    with pytest.raises(ValueError, match="budget 128"):
        validate_content(ContentCollection("content_01", tuple(paragraphs), make_collection().questions))


def test_candidate_pool_must_exceed_largest_budget() -> None:
    paragraphs = tuple(Paragraph(f"p{i}", f"Paragraph {i}", 40) for i in range(1, 10))

    with pytest.raises(ValueError, match="exceed 1024"):
        validate_content(ContentCollection("content_01", paragraphs, make_collection().questions))


def test_category_requires_matching_evidence_order() -> None:
    question = make_question("three_hop")
    malformed = Question(
        id=question.id,
        text=question.text,
        answer=question.answer,
        category=question.category,
        valid_evidence_sets=(("p01", "p02"),),
        budget_ground_truth=question.budget_ground_truth,
    )
    questions = (malformed,) + tuple(
        q for q in make_collection().questions if q.id != malformed.id
    )

    with pytest.raises(ValueError, match="three_hop.*3"):
        validate_content(ContentCollection("content_01", make_paragraphs(), questions))


def test_each_category_requires_five_to_ten_questions() -> None:
    collection = make_collection()
    reduced = tuple(q for q in collection.questions if q.id != "direct_5")

    with pytest.raises(ValueError, match="direct.*5 to 10"):
        validate_content(ContentCollection(collection.id, collection.paragraphs, reduced))
