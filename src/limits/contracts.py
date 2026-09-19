from __future__ import annotations

from dataclasses import dataclass, field
from types import MappingProxyType
from typing import Mapping


@dataclass(frozen=True)
class CandidateChunk:
    id: str
    text: str
    token_cost: int
    metadata: Mapping[str, str] = field(default_factory=dict)

    def __post_init__(self) -> None:
        if not self.id.strip():
            raise ValueError("chunk id must not be empty")
        if not self.text.strip():
            raise ValueError("chunk text must not be empty")
        if self.token_cost <= 0:
            raise ValueError("token cost must be positive")
        object.__setattr__(self, "metadata", MappingProxyType(dict(self.metadata)))


@dataclass(frozen=True)
class CandidateInput:
    query: str
    chunks: tuple[CandidateChunk, ...]
    token_budget: int

    def __post_init__(self) -> None:
        if not self.query.strip():
            raise ValueError("query must not be empty")
        if not self.chunks:
            raise ValueError("at least one candidate chunk is required")
        if self.token_budget <= 0:
            raise ValueError("token budget must be positive")
        ids = [chunk.id for chunk in self.chunks]
        if len(ids) != len(set(ids)):
            raise ValueError("candidate chunk ids must be unique")


@dataclass(frozen=True)
class ExampleLabels:
    answer: str
    support_sets: tuple[frozenset[str], ...]
    hop_depth: int
    feasible: bool
    entity_ids: frozenset[str] = frozenset()

    def __post_init__(self) -> None:
        if not self.answer.strip():
            raise ValueError("answer must not be empty")
        if not self.support_sets or any(not support for support in self.support_sets):
            raise ValueError("at least one non-empty support set is required")
        if self.hop_depth <= 0:
            raise ValueError("hop depth must be positive")


@dataclass(frozen=True)
class BenchmarkExample:
    public: CandidateInput
    labels: ExampleLabels
    split: str
    template_family: str

    def __post_init__(self) -> None:
        if self.split not in {"train", "validation", "test"}:
            raise ValueError("split must be train, validation, or test")
        candidate_ids = {chunk.id for chunk in self.public.chunks}
        referenced = set().union(*self.labels.support_sets)
        unknown = referenced - candidate_ids
        if unknown:
            raise ValueError(f"support sets reference unknown candidate ids: {sorted(unknown)}")


@dataclass(frozen=True)
class SelectionResult:
    selected_ids: tuple[str, ...]
    total_tokens: int
    score: float

