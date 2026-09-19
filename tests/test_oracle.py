from limits.contracts import CandidateChunk, CandidateInput
from limits.oracle import exhaustive_select


def test_oracle_finds_conditional_three_item_utility_under_budget() -> None:
    public = CandidateInput(
        query="Who owns the laboratory used by the inventor?",
        chunks=tuple(CandidateChunk(name, name, 2) for name in ("a", "b", "c", "d")),
        token_budget=6,
    )

    def utility(selected: frozenset[str]) -> float:
        return 10.0 if {"a", "b", "c"} <= selected else float(len(selected & {"a", "b", "c"}))

    result = exhaustive_select(public, utility)

    assert result.selected_ids == ("a", "b", "c")
    assert result.total_tokens == 6
    assert result.score == 10.0


def test_oracle_prefers_lower_token_cost_when_scores_tie() -> None:
    public = CandidateInput(
        query="question",
        chunks=(
            CandidateChunk("long", "long", 4),
            CandidateChunk("short", "short", 2),
        ),
        token_budget=4,
    )

    result = exhaustive_select(public, lambda selected: 1.0 if selected else 0.0)

    assert result.selected_ids == ("short",)
    assert result.total_tokens == 2


def test_oracle_never_exceeds_budget() -> None:
    public = CandidateInput(
        query="question",
        chunks=tuple(CandidateChunk(str(i), str(i), 3) for i in range(4)),
        token_budget=5,
    )

    result = exhaustive_select(public, lambda selected: float(len(selected)))

    assert len(result.selected_ids) == 1
    assert result.total_tokens <= public.token_budget
