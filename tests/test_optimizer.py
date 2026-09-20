from src.contracts import CandidateChunk, CandidateInput
from src.optimizer import optimize_interactions
from src.utility import InteractionUtility


def test_optimizer_selects_weak_items_that_unlock_third_order_synergy() -> None:
    public = CandidateInput(
        "multi-hop question",
        (
            CandidateChunk("a", "first bridge", 2),
            CandidateChunk("b", "second bridge", 2),
            CandidateChunk("c", "final bridge", 2),
            CandidateChunk("d", "query-similar distractor", 5),
        ),
        token_budget=6,
    )
    utility = InteractionUtility(
        individual={"a": 0.2, "b": 0.2, "c": 0.2, "d": 5.0},
        triple_synergy={frozenset({"a", "b", "c"}): 10.0},
    )

    result = optimize_interactions(public, utility)

    assert result.selected_ids == ("a", "b", "c")
    assert result.score == 10.6


def test_optimizer_avoids_redundant_duplicate() -> None:
    public = CandidateInput(
        "question",
        (
            CandidateChunk("original", "fact", 2),
            CandidateChunk("duplicate", "same fact", 2),
            CandidateChunk("bridge", "needed bridge", 2),
        ),
        token_budget=4,
    )
    utility = InteractionUtility(
        individual={"original": 4.0, "duplicate": 4.0, "bridge": 3.0},
        pair_redundancy={frozenset({"original", "duplicate"}): 5.0},
    )

    result = optimize_interactions(public, utility)

    assert set(result.selected_ids) in ({"original", "bridge"}, {"duplicate", "bridge"})
    assert result.total_tokens == 4


def test_optimizer_rejects_utility_ids_missing_from_candidate_pool() -> None:
    public = CandidateInput("question", (CandidateChunk("a", "fact", 1),), 1)
    utility = InteractionUtility(individual={"missing": 1.0})

    try:
        optimize_interactions(public, utility)
    except ValueError as error:
        assert "unknown" in str(error)
    else:
        raise AssertionError("unknown utility ids must be rejected")
