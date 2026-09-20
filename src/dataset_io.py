from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from src.dataset import BudgetSelection, ContentCollection, EvidenceUnit, Paragraph, Question


def load_content_collections(path: Path) -> tuple[ContentCollection, ...]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    return tuple(_content_from_dict(item) for item in payload["contents"])


def _content_from_dict(item: dict[str, Any]) -> ContentCollection:
    paragraphs = tuple(
        Paragraph(id=paragraph["id"], text=paragraph["text"], tokens=paragraph["tokens"])
        for paragraph in item["paragraphs"]
    )
    questions = tuple(_question_from_dict(question) for question in item["questions"])
    return ContentCollection(id=item["id"], paragraphs=paragraphs, questions=questions)


def _question_from_dict(item: dict[str, Any]) -> Question:
    budget_ground_truth = {
        int(budget): tuple(
            BudgetSelection(tuple(selection)) for selection in selections
        )
        for budget, selections in item["budget_ground_truth"].items()
    }
    return Question(
        id=item["id"],
        text=item["text"],
        answer=item["answer"],
        category=item["category"],
        required_evidence_units=tuple(
            _evidence_unit_from_dict(unit) for unit in item["required_evidence_units"]
        ),
        optional_support_units=tuple(
            _evidence_unit_from_dict(unit) for unit in item.get("optional_support_units", ())
        ),
        budget_ground_truth=budget_ground_truth,
        redundancy_groups=tuple(tuple(group) for group in item.get("redundancy_groups", ())),
        distractor_groups=tuple(tuple(group) for group in item.get("distractor_groups", ())),
    )


def _evidence_unit_from_dict(item: dict[str, Any]) -> EvidenceUnit:
    return EvidenceUnit(
        name=item["name"],
        alternatives=tuple(item["alternatives"]),
    )
