from __future__ import annotations

import random
import re

from src.dataset import Paragraph


def budget_fill_selector(paragraphs: tuple[Paragraph, ...], budget: int) -> tuple[str, ...]:
    selected: list[str] = []
    remaining = budget
    for paragraph in paragraphs:
        if paragraph.tokens <= remaining:
            selected.append(paragraph.id)
            remaining -= paragraph.tokens
    return tuple(selected)


def random_selector(
    paragraphs: tuple[Paragraph, ...],
    budget: int,
    seed: int | None = None,
) -> tuple[str, ...]:
    shuffled = list(paragraphs)
    random.Random(seed).shuffle(shuffled)
    return budget_fill_selector(tuple(shuffled), budget)


def keyword_overlap_selector(
    query: str,
    paragraphs: tuple[Paragraph, ...],
    budget: int,
) -> tuple[str, ...]:
    query_terms = _terms(query)
    ranked = sorted(
        paragraphs,
        key=lambda paragraph: (
            -len(query_terms & _terms(paragraph.text)),
            paragraph.tokens,
            paragraph.id,
        ),
    )
    return budget_fill_selector(tuple(ranked), budget)


def _terms(text: str) -> frozenset[str]:
    return frozenset(re.findall(r"[a-z0-9]+", text.lower()))
