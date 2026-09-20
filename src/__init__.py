"""LIMITS context-selection research toolkit."""

from .contracts import BenchmarkExample, CandidateChunk, CandidateInput, ExampleLabels
from .dataset import BUDGETS, BudgetSelection, ContentCollection, EvidenceUnit, Paragraph, Question
from .evaluator import EvaluationResult, EvaluationWeights, evaluate_selection, reward_from_evaluation

__all__ = [
    "BUDGETS",
    "BenchmarkExample",
    "BudgetSelection",
    "CandidateChunk",
    "CandidateInput",
    "ContentCollection",
    "EvidenceUnit",
    "EvaluationResult",
    "EvaluationWeights",
    "ExampleLabels",
    "Paragraph",
    "Question",
    "evaluate_selection",
    "reward_from_evaluation",
]

