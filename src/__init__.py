"""LIMITS context-selection research toolkit."""

from .contracts import BenchmarkExample, CandidateChunk, CandidateInput, ExampleLabels
from .dataset import BUDGETS, BudgetSelection, ContentCollection, EvidenceUnit, Paragraph, Question
from .dataset_summary import ContentSummary, DatasetSummary, summarize_content, summarize_dataset
from .evaluator import EvaluationResult, EvaluationWeights, evaluate_selection, reward_from_evaluation
from .selectors import budget_fill_selector, keyword_overlap_selector, random_selector

__all__ = [
    "BUDGETS",
    "BenchmarkExample",
    "BudgetSelection",
    "CandidateChunk",
    "CandidateInput",
    "ContentCollection",
    "ContentSummary",
    "DatasetSummary",
    "EvidenceUnit",
    "EvaluationResult",
    "EvaluationWeights",
    "ExampleLabels",
    "Paragraph",
    "Question",
    "budget_fill_selector",
    "evaluate_selection",
    "keyword_overlap_selector",
    "random_selector",
    "reward_from_evaluation",
    "summarize_content",
    "summarize_dataset",
]

