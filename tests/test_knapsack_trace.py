from src.dataset import BudgetSelection, EvidenceUnit, Paragraph, Question
from src.knapsack_trace import build_knapsack_trace, parse_manual_paragraphs


class StaticSemanticScorer:
    def __init__(self, scores: dict[tuple[str, str], float] | None = None) -> None:
        self.scores = scores or {}

    def similarity(self, left: str, right: str) -> float:
        return self.scores.get((left, right), self.scores.get((right, left), 0.0))


def make_question() -> Question:
    return Question(
        id="q01",
        text="Where is the sensor cart staged during calibration?",
        answer="The sensor cart is staged beside Hangar 2.",
        category="direct",
        required_evidence_units=(EvidenceUnit("location", ("p01",)),),
        budget_ground_truth={
            128: (BudgetSelection(("p01",)),),
            256: (BudgetSelection(("p01",)),),
            512: (BudgetSelection(("p01",)),),
            1024: (BudgetSelection(("p01",)),),
        },
    )


def make_paragraphs() -> tuple[Paragraph, ...]:
    return (
        Paragraph("p01", "The sensor cart is staged beside Hangar 2.", 20),
        Paragraph("p02", "The sensor cart includes a red charging cable.", 18),
        Paragraph("p03", "Lunch arrives near Bay 7.", 22),
        Paragraph("p04", "Hangar 3 stores paint filters.", 19),
    )


def test_parse_manual_paragraphs_creates_plain_numbered_paragraphs() -> None:
    paragraphs = parse_manual_paragraphs("First paragraph.\n\nSecond paragraph is longer.")

    assert [paragraph.id for paragraph in paragraphs] == ["m01", "m02"]
    assert paragraphs[0].text == "First paragraph."
    assert paragraphs[0].tokens > 0


def test_build_knapsack_trace_exposes_candidate_scores_and_final_selection() -> None:
    trace = build_knapsack_trace(
        question=make_question(),
        paragraphs=make_paragraphs(),
        budget=40,
        semantic_scorer=StaticSemanticScorer(),
    )

    assert trace["budget"] == 40
    assert trace["candidateLimit"] == 15
    assert trace["final"]["tokenUsed"] <= 40
    assert "p01" in trace["final"]["selectedIds"]
    assert trace["scoreRows"][0]["id"] == "p01"
    assert {"individual", "pairSynergy", "tripleSynergy", "redundancyPenalty", "total"} <= set(trace["breakdown"])
    assert trace["subsetRows"]
