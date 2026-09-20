from __future__ import annotations

from collections import Counter
from dataclasses import dataclass

from src.dataset import BUDGETS, ContentCollection


@dataclass(frozen=True)
class ContentSummary:
    content_id: str
    paragraph_count: int
    total_tokens: int
    question_count: int
    category_counts: dict[str, int]
    average_required_units: float
    average_optional_units: float
    average_ground_truth_selections_by_budget: dict[int, float]
    questions_with_budget_growth: int
    redundancy_group_count: int
    distractor_group_count: int


@dataclass(frozen=True)
class DatasetSummary:
    content_count: int
    paragraph_count: int
    total_tokens: int
    question_count: int
    category_counts: dict[str, int]


def summarize_content(content: ContentCollection) -> ContentSummary:
    question_count = len(content.questions)
    category_counts = Counter(question.category for question in content.questions)
    average_ground_truth_selections_by_budget = {
        budget: _average(
            len(question.budget_ground_truth[budget]) for question in content.questions
        )
        for budget in BUDGETS
    }

    return ContentSummary(
        content_id=content.id,
        paragraph_count=len(content.paragraphs),
        total_tokens=sum(paragraph.tokens for paragraph in content.paragraphs),
        question_count=question_count,
        category_counts=dict(category_counts),
        average_required_units=_average(
            len(question.required_evidence_units) for question in content.questions
        ),
        average_optional_units=_average(
            len(question.optional_support_units) for question in content.questions
        ),
        average_ground_truth_selections_by_budget=average_ground_truth_selections_by_budget,
        questions_with_budget_growth=sum(
            _has_budget_growth(question) for question in content.questions
        ),
        redundancy_group_count=sum(
            len(question.redundancy_groups) for question in content.questions
        ),
        distractor_group_count=sum(
            len(question.distractor_groups) for question in content.questions
        ),
    )


def summarize_dataset(contents: tuple[ContentCollection, ...]) -> DatasetSummary:
    category_counts: Counter[str] = Counter()
    for content in contents:
        category_counts.update(question.category for question in content.questions)

    return DatasetSummary(
        content_count=len(contents),
        paragraph_count=sum(len(content.paragraphs) for content in contents),
        total_tokens=sum(
            paragraph.tokens for content in contents for paragraph in content.paragraphs
        ),
        question_count=sum(len(content.questions) for content in contents),
        category_counts=dict(category_counts),
    )


def _has_budget_growth(question) -> bool:
    smallest = min(
        len(selection.selected) for selection in question.budget_ground_truth[min(BUDGETS)]
    )
    largest = max(
        len(selection.selected) for selection in question.budget_ground_truth[max(BUDGETS)]
    )
    return largest > smallest


def _average(values) -> float:
    values = tuple(values)
    if not values:
        return 0.0
    return sum(values) / len(values)
