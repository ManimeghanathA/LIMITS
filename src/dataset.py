from __future__ import annotations

from dataclasses import dataclass, field
from types import MappingProxyType
from typing import Mapping


BUDGETS = (128, 256, 512, 1024)
CATEGORY_ORDER = {"direct": 1, "two_hop": 2, "three_hop": 3}


@dataclass(frozen=True)
class Paragraph:
    id: str
    text: str
    tokens: int

    def __post_init__(self) -> None:
        if not self.id.strip():
            raise ValueError("paragraph id must not be empty")
        if not self.text.strip():
            raise ValueError("paragraph text must not be empty")
        if self.tokens <= 0:
            raise ValueError("paragraph tokens must be positive")


@dataclass(frozen=True)
class BudgetSelection:
    selected: tuple[str, ...]

    def __post_init__(self) -> None:
        if not self.selected:
            raise ValueError("a budget selection must not be empty")
        if len(self.selected) != len(set(self.selected)):
            raise ValueError("a budget selection must contain unique paragraph ids")


@dataclass(frozen=True)
class Question:
    id: str
    text: str
    answer: str
    category: str
    valid_evidence_sets: tuple[tuple[str, ...], ...]
    budget_ground_truth: Mapping[int, BudgetSelection]
    redundancy_groups: tuple[tuple[str, ...], ...] = ()

    def __post_init__(self) -> None:
        if not self.id.strip() or not self.text.strip() or not self.answer.strip():
            raise ValueError("question id, text, and answer must not be empty")
        if self.category not in CATEGORY_ORDER:
            raise ValueError(f"unknown question category: {self.category}")
        if not self.valid_evidence_sets:
            raise ValueError("a question requires at least one valid evidence set")
        object.__setattr__(
            self,
            "budget_ground_truth",
            MappingProxyType(dict(self.budget_ground_truth)),
        )


@dataclass(frozen=True)
class ContentCollection:
    id: str
    paragraphs: tuple[Paragraph, ...]
    questions: tuple[Question, ...]


def validate_content(content: ContentCollection) -> None:
    if not content.id.strip():
        raise ValueError("content id must not be empty")
    if not content.paragraphs:
        raise ValueError("content must contain candidate paragraphs")

    paragraph_ids = [paragraph.id for paragraph in content.paragraphs]
    if len(paragraph_ids) != len(set(paragraph_ids)):
        raise ValueError("paragraph ids must be unique")
    paragraph_by_id = {paragraph.id: paragraph for paragraph in content.paragraphs}

    total_tokens = sum(paragraph.tokens for paragraph in content.paragraphs)
    if total_tokens <= max(BUDGETS):
        raise ValueError("candidate paragraph tokens must exceed 1024")

    question_ids = [question.id for question in content.questions]
    if len(question_ids) != len(set(question_ids)):
        raise ValueError("question ids must be unique")

    for category in CATEGORY_ORDER:
        count = sum(question.category == category for question in content.questions)
        if not 5 <= count <= 10:
            raise ValueError(f"{category} must contain 5 to 10 questions")

    known_ids = set(paragraph_by_id)
    for question in content.questions:
        required_order = CATEGORY_ORDER[question.category]
        for evidence in question.valid_evidence_sets:
            if len(evidence) != required_order:
                raise ValueError(
                    f"{question.category} questions require evidence sets of size {required_order}"
                )
            if len(evidence) != len(set(evidence)):
                raise ValueError(f"question {question.id} has repeated evidence ids")
            unknown = set(evidence) - known_ids
            if unknown:
                raise ValueError(f"question {question.id} references unknown evidence: {sorted(unknown)}")
            evidence_cost = sum(paragraph_by_id[item].tokens for item in evidence)
            if evidence_cost > min(BUDGETS):
                raise ValueError(
                    f"question {question.id} evidence does not fit budget 128"
                )

        if set(question.budget_ground_truth) != set(BUDGETS):
            raise ValueError(f"question {question.id} must define ground truth for all budgets")

        valid_sets = tuple(frozenset(items) for items in question.valid_evidence_sets)
        for budget in BUDGETS:
            selected = question.budget_ground_truth[budget].selected
            unknown = set(selected) - known_ids
            if unknown:
                raise ValueError(
                    f"question {question.id} budget {budget} selects unknown paragraphs: {sorted(unknown)}"
                )
            selected_cost = sum(paragraph_by_id[item].tokens for item in selected)
            if selected_cost > budget:
                raise ValueError(
                    f"question {question.id} selection exceeds budget {budget}"
                )
            selected_set = frozenset(selected)
            if not any(evidence <= selected_set for evidence in valid_sets):
                raise ValueError(
                    f"question {question.id} budget {budget} lacks complete evidence"
                )

        for group in question.redundancy_groups:
            if len(group) < 2:
                raise ValueError("redundancy groups require at least two paragraphs")
            unknown = set(group) - known_ids
            if unknown:
                raise ValueError(
                    f"question {question.id} redundancy group references unknown paragraphs"
                )
