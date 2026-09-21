from src.dataset import EvidenceUnit, Paragraph, Question
from src.knapsack_features import build_feature_utility, select_feature_candidates


class StaticSemanticScorer:
    def __init__(self, scores: dict[tuple[str, str], float]) -> None:
        self.scores = scores

    def similarity(self, left: str, right: str) -> float:
        return self.scores.get((left, right), self.scores.get((right, left), 0.0))


def _question(text: str = "Where does the access issue go?") -> Question:
    return Question(
        id="q",
        text=text,
        category="direct",
        answer="North Annex",
        required_evidence_units=(EvidenceUnit(name="answer", alternatives=("p01",)),),
        optional_support_units=(),
        budget_ground_truth={128: (("p01",),)},
        redundancy_groups=(),
        distractor_groups=(),
    )


def test_feature_candidate_pool_defaults_to_fifteen() -> None:
    question = _question()
    paragraphs = tuple(
        Paragraph(id=f"p{index:02d}", text=f"access issue paragraph {index}", tokens=10)
        for index in range(20)
    )

    candidates = select_feature_candidates(
        question,
        paragraphs,
        budget=128,
        semantic_scorer=StaticSemanticScorer({}),
    )

    assert len(candidates) == 15


def test_dense_query_similarity_increases_individual_importance() -> None:
    question = _question("Where should a badge problem be resolved?")
    paragraphs = (
        Paragraph(id="p01", text="Blue lanyard problems are resolved at the learning office.", tokens=12),
        Paragraph(id="p02", text="The cafeteria menu changes on Monday.", tokens=12),
    )
    scorer = StaticSemanticScorer({(question.text, paragraphs[0].text): 0.9})

    utility = build_feature_utility(
        question,
        paragraphs,
        budget=128,
        semantic_scorer=scorer,
    )

    assert utility.individual["p01"] > utility.individual["p02"]


def test_semantic_redundancy_penalizes_paraphrase_pairs() -> None:
    question = _question("Where is student access handled?")
    paragraphs = (
        Paragraph(id="p01", text="Student access is handled at the North Annex.", tokens=12),
        Paragraph(id="p02", text="The learning office resolves learner entry problems.", tokens=12),
    )
    scorer = StaticSemanticScorer({(paragraphs[0].text, paragraphs[1].text): 0.92})

    utility = build_feature_utility(
        question,
        paragraphs,
        budget=128,
        semantic_scorer=scorer,
    )

    assert utility.pair_redundancy[frozenset({"p01", "p02"})] > 0
