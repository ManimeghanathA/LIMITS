from __future__ import annotations

from dataclasses import dataclass
from typing import Collection, Iterable


@dataclass(frozen=True)
class EvidenceMetrics:
    precision: float
    recall: float
    f1: float
    complete_support: bool
    exact_support: bool
    matched_support: frozenset[str]


def score_evidence(
    selected_ids: Collection[str],
    support_sets: Iterable[Collection[str]],
) -> EvidenceMetrics:
    selected = frozenset(selected_ids)
    supports = tuple(frozenset(support) for support in support_sets)
    if not supports or any(not support for support in supports):
        raise ValueError("support sets must be non-empty")

    def scores(support: frozenset[str]) -> tuple[float, float, float]:
        overlap = len(selected & support)
        precision = overlap / len(selected) if selected else 0.0
        recall = overlap / len(support)
        f1 = 2 * precision * recall / (precision + recall) if precision + recall else 0.0
        return precision, recall, f1

    matched = max(supports, key=lambda support: (scores(support)[2], -len(support), sorted(support)))
    precision, recall, f1 = scores(matched)
    return EvidenceMetrics(
        precision=precision,
        recall=recall,
        f1=f1,
        complete_support=any(support <= selected for support in supports),
        exact_support=selected in supports,
        matched_support=matched,
    )

