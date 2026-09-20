from __future__ import annotations

from dataclasses import dataclass, field
from types import MappingProxyType
from typing import Mapping


InteractionKey = frozenset[str]


@dataclass(frozen=True)
class InteractionUtility:
    """Explicit utility through third-order interactions."""

    individual: Mapping[str, float] = field(default_factory=dict)
    pair_synergy: Mapping[InteractionKey, float] = field(default_factory=dict)
    pair_redundancy: Mapping[InteractionKey, float] = field(default_factory=dict)
    triple_synergy: Mapping[InteractionKey, float] = field(default_factory=dict)
    redundancy_weight: float = 1.0

    def __post_init__(self) -> None:
        if self.redundancy_weight < 0:
            raise ValueError("redundancy weight must be non-negative")
        self._validate_arity(self.pair_synergy, 2, "pair synergy")
        self._validate_arity(self.pair_redundancy, 2, "pair redundancy")
        self._validate_arity(self.triple_synergy, 3, "triple synergy")
        for name in ("individual", "pair_synergy", "pair_redundancy", "triple_synergy"):
            object.__setattr__(self, name, MappingProxyType(dict(getattr(self, name))))

    @staticmethod
    def _validate_arity(values: Mapping[InteractionKey, float], expected: int, name: str) -> None:
        if any(len(key) != expected for key in values):
            raise ValueError(f"{name} keys must have arity {expected}")

    @property
    def referenced_ids(self) -> frozenset[str]:
        ids = set(self.individual)
        for interactions in (self.pair_synergy, self.pair_redundancy, self.triple_synergy):
            for key in interactions:
                ids.update(key)
        return frozenset(ids)

    def __call__(self, selected: frozenset[str]) -> float:
        value = sum(self.individual.get(chunk_id, 0.0) for chunk_id in selected)
        value += sum(score for key, score in self.pair_synergy.items() if key <= selected)
        value -= self.redundancy_weight * sum(
            score for key, score in self.pair_redundancy.items() if key <= selected
        )
        value += sum(score for key, score in self.triple_synergy.items() if key <= selected)
        return float(value)

