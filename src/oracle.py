from __future__ import annotations

from collections.abc import Callable
from itertools import combinations

from .contracts import CandidateInput, SelectionResult


UtilityFunction = Callable[[frozenset[str]], float]


def exhaustive_select(public: CandidateInput, utility: UtilityFunction) -> SelectionResult:
    """Return the exact best feasible subset for small benchmark instances."""
    best_ids: tuple[str, ...] = ()
    best_tokens = 0
    best_score = float(utility(frozenset()))

    for size in range(1, len(public.chunks) + 1):
        for subset in combinations(public.chunks, size):
            total_tokens = sum(chunk.token_cost for chunk in subset)
            if total_tokens > public.token_budget:
                continue
            ids = tuple(sorted(chunk.id for chunk in subset))
            score = float(utility(frozenset(ids)))
            candidate_key = (score, -total_tokens, tuple(reversed(ids)))
            best_key = (best_score, -best_tokens, tuple(reversed(best_ids)))
            if candidate_key > best_key:
                best_ids = ids
                best_tokens = total_tokens
                best_score = score

    return SelectionResult(best_ids, best_tokens, best_score)

