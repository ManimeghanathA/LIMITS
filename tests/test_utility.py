import pytest

from limits.utility import InteractionUtility


def test_interaction_utility_combines_all_supported_orders() -> None:
    utility = InteractionUtility(
        individual={"a": 2.0, "b": 3.0, "c": 1.0},
        pair_synergy={frozenset({"a", "b"}): 4.0},
        pair_redundancy={frozenset({"b", "c"}): 1.5},
        triple_synergy={frozenset({"a", "b", "c"}): 8.0},
        redundancy_weight=2.0,
    )

    assert utility(frozenset({"a", "b", "c"})) == pytest.approx(15.0)


def test_interactions_only_apply_when_every_member_is_selected() -> None:
    utility = InteractionUtility(
        individual={"a": 1.0, "b": 1.0, "c": 1.0},
        pair_synergy={frozenset({"a", "b"}): 5.0},
        triple_synergy={frozenset({"a", "b", "c"}): 20.0},
    )

    assert utility(frozenset({"a"})) == 1.0
    assert utility(frozenset({"a", "c"})) == 2.0
    assert utility(frozenset({"a", "b"})) == 7.0


@pytest.mark.parametrize(
    ("field", "key"),
    [
        ("pair_synergy", frozenset({"a"})),
        ("pair_redundancy", frozenset({"a", "b", "c"})),
        ("triple_synergy", frozenset({"a", "b"})),
    ],
)
def test_interaction_arity_is_validated(field: str, key: frozenset[str]) -> None:
    arguments = {field: {key: 1.0}}

    with pytest.raises(ValueError, match="arity"):
        InteractionUtility(**arguments)

