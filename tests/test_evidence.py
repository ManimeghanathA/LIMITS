import pytest

from src.evidence import score_evidence


def test_evidence_scoring_uses_best_of_multiple_valid_support_sets() -> None:
    metrics = score_evidence(
        selected_ids={"a", "d"},
        support_sets=({"a", "b", "c"}, {"a", "d"}),
    )

    assert metrics.precision == 1.0
    assert metrics.recall == 1.0
    assert metrics.f1 == 1.0
    assert metrics.complete_support is True
    assert metrics.exact_support is True


def test_extra_chunks_reduce_precision_but_preserve_answerability() -> None:
    metrics = score_evidence(
        selected_ids={"a", "b", "noise"},
        support_sets=({"a", "b"},),
    )

    assert metrics.precision == pytest.approx(2 / 3)
    assert metrics.recall == 1.0
    assert metrics.f1 == pytest.approx(0.8)
    assert metrics.complete_support is True
    assert metrics.exact_support is False


def test_empty_selection_has_zero_scores() -> None:
    metrics = score_evidence(set(), ({"a"},))

    assert metrics.precision == 0.0
    assert metrics.recall == 0.0
    assert metrics.f1 == 0.0
    assert metrics.complete_support is False

