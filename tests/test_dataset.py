import pytest

from src.dataset import (
    BUDGETS,
    BudgetSelection,
    ContentCollection,
    EvidenceUnit,
    Paragraph,
    Question,
    validate_content,
)


def make_paragraphs() -> tuple[Paragraph, ...]:
    return tuple(
        Paragraph(id=f"p{i:02d}", text=f"Paragraph {i} contains curated information.", tokens=30 if i < 5 else 105)
        for i in range(1, 14)
    )


def make_question(category: str, index: int = 1) -> Question:
    size = {"direct": 1, "two_hop": 2, "three_hop": 3}[category]
    evidence = tuple(f"p{i:02d}" for i in range(1, size + 1))
    selections = {budget: (BudgetSelection(selected=evidence),) for budget in BUDGETS}
    return Question(
        id=f"{category}_{index}",
        text=f"A {category} question?",
        answer="Known answer",
        category=category,
        required_evidence_units=tuple(
            EvidenceUnit(name=f"{category}_{index}_{evidence_id}", alternatives=(evidence_id,))
            for evidence_id in evidence
        ),
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


def test_direct_question_can_have_multiple_supporting_evidence_paragraphs() -> None:
    evidence = ("p01", "p02", "p03")
    selections = {budget: (BudgetSelection(selected=evidence),) for budget in BUDGETS}
    direct = Question(
        id="direct_1",
        text="Which teams contributed to the operating review?",
        answer="The finance, rollout, and support teams contributed.",
        category="direct",
        required_evidence_units=(
            EvidenceUnit("finance_team", ("p01",)),
            EvidenceUnit("rollout_team", ("p02",)),
            EvidenceUnit("support_team", ("p03",)),
        ),
        budget_ground_truth=selections,
    )
    questions = (direct,) + tuple(
        q for q in make_collection().questions if q.id != direct.id
    )

    validate_content(ContentCollection("content_01", make_paragraphs(), questions))


def test_question_without_every_budget_is_rejected() -> None:
    question = make_question("direct")
    incomplete = Question(
        id=question.id,
        text=question.text,
        answer=question.answer,
        category=question.category,
        required_evidence_units=question.required_evidence_units,
        budget_ground_truth={128: (BudgetSelection(("p01",)),)},
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
    invalid_selections[128] = (BudgetSelection(("p01", "p02")),)
    changed = Question(
        id=question.id,
        text=question.text,
        answer=question.answer,
        category=question.category,
        required_evidence_units=question.required_evidence_units,
        budget_ground_truth=invalid_selections,
    )
    questions = (changed,) + tuple(
        q for q in make_collection().questions if q.id != changed.id
    )

    with pytest.raises(ValueError, match="required evidence"):
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


def test_category_does_not_force_ground_truth_evidence_set_size() -> None:
    question = make_question("two_hop")
    expanded = Question(
        id=question.id,
        text=question.text,
        answer=question.answer,
        category=question.category,
        required_evidence_units=(
            EvidenceUnit("first_fact", ("p01",)),
            EvidenceUnit("second_fact", ("p02",)),
            EvidenceUnit("supporting_context", ("p03",)),
        ),
        budget_ground_truth={budget: (BudgetSelection(("p01", "p02", "p03")),) for budget in BUDGETS},
    )
    questions = (expanded,) + tuple(
        q for q in make_collection().questions if q.id != expanded.id
    )

    validate_content(ContentCollection("content_01", make_paragraphs(), questions))


def test_three_hop_question_can_require_mixed_support_larger_than_three_chunks() -> None:
    question = make_question("three_hop")
    mixed_evidence = ("p01", "p02", "p03", "p04")
    expanded = Question(
        id=question.id,
        text=question.text,
        answer=question.answer,
        category=question.category,
        required_evidence_units=tuple(
            EvidenceUnit(f"required_{evidence_id}", (evidence_id,))
            for evidence_id in mixed_evidence
        ),
        budget_ground_truth={budget: (BudgetSelection(mixed_evidence),) for budget in BUDGETS},
    )
    questions = (expanded,) + tuple(
        q for q in make_collection().questions if q.id != expanded.id
    )

    validate_content(ContentCollection("content_01", make_paragraphs(), questions))


def test_each_category_requires_five_to_ten_questions() -> None:
    collection = make_collection()
    reduced = tuple(q for q in collection.questions if q.id != "direct_5")

    with pytest.raises(ValueError, match="direct.*5 to 10"):
        validate_content(ContentCollection(collection.id, collection.paragraphs, reduced))


def test_budget_can_have_multiple_acceptable_ground_truth_selections() -> None:
    question = make_question("direct")
    replacement = Question(
        id=question.id,
        text=question.text,
        answer=question.answer,
        category=question.category,
        required_evidence_units=(
            EvidenceUnit("desk_location", ("p01", "p02")),
        ),
        budget_ground_truth={
            budget: (BudgetSelection(("p01",)), BudgetSelection(("p02",)))
            for budget in BUDGETS
        },
    )
    questions = (replacement,) + tuple(
        q for q in make_collection().questions if q.id != replacement.id
    )

    validate_content(ContentCollection("content_01", make_paragraphs(), questions))


def test_budget_selection_must_satisfy_every_required_evidence_unit() -> None:
    question = make_question("two_hop")
    replacement = Question(
        id=question.id,
        text=question.text,
        answer=question.answer,
        category=question.category,
        required_evidence_units=(
            EvidenceUnit("approver", ("p01", "p02")),
            EvidenceUnit("storage", ("p03",)),
        ),
        budget_ground_truth={
            budget: (BudgetSelection(("p01",)),)
            for budget in BUDGETS
        },
    )
    questions = (replacement,) + tuple(
        q for q in make_collection().questions if q.id != replacement.id
    )

    with pytest.raises(ValueError, match="lacks required evidence"):
        validate_content(ContentCollection("content_01", make_paragraphs(), questions))
