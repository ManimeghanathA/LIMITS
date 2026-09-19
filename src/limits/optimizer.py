from __future__ import annotations

from .contracts import CandidateInput, SelectionResult
from .oracle import exhaustive_select
from .utility import InteractionUtility


def optimize_interactions(
    public: CandidateInput,
    utility: InteractionUtility,
) -> SelectionResult:
    """Exactly optimize explicit interactions for a small candidate pool."""
    candidate_ids = frozenset(chunk.id for chunk in public.chunks)
    unknown = utility.referenced_ids - candidate_ids
    if unknown:
        raise ValueError(f"utility references unknown candidate ids: {sorted(unknown)}")
    return exhaustive_select(public, utility)
