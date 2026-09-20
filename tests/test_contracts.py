import pytest

from src.contracts import BenchmarkExample, CandidateChunk, CandidateInput, ExampleLabels


def test_candidate_input_rejects_duplicate_chunk_ids() -> None:
    chunks = (
        CandidateChunk("c1", "first fact", 2),
        CandidateChunk("c1", "second fact", 2),
    )

    with pytest.raises(ValueError, match="unique"):
        CandidateInput("question", chunks, token_budget=8)


@pytest.mark.parametrize("budget", [-1, 0])
def test_candidate_input_requires_positive_budget(budget: int) -> None:
    with pytest.raises(ValueError, match="positive"):
        CandidateInput(
            "question",
            (CandidateChunk("c1", "fact", 1),),
            token_budget=budget,
        )


def test_labels_must_reference_public_candidate_ids() -> None:
    public = CandidateInput(
        "question",
        (CandidateChunk("c1", "fact", 1),),
        token_budget=4,
    )
    labels = ExampleLabels(
        answer="answer",
        support_sets=(frozenset({"missing"}),),
        hop_depth=1,
        feasible=True,
    )

    with pytest.raises(ValueError, match="unknown"):
        BenchmarkExample(public, labels, split="train", template_family="train_chain")


def test_public_input_contains_no_ground_truth_labels() -> None:
    public = CandidateInput(
        "question",
        (CandidateChunk("c1", "fact", 1),),
        token_budget=4,
    )

    assert not hasattr(public, "answer")
    assert not hasattr(public, "support_sets")

