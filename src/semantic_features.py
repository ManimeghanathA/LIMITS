from __future__ import annotations

from functools import lru_cache
from typing import Protocol

import numpy as np
from sentence_transformers import SentenceTransformer


FIXED_EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"


class SemanticScorer(Protocol):
    def similarity(self, left: str, right: str) -> float:
        """Return semantic similarity in approximately [-1, 1]."""


class SentenceTransformerSemanticScorer:
    def __init__(self, model_name: str = FIXED_EMBEDDING_MODEL) -> None:
        self.model_name = model_name

    def similarity(self, left: str, right: str) -> float:
        left_vector = _embed(self.model_name, left)
        right_vector = _embed(self.model_name, right)
        return float(np.dot(left_vector, right_vector))


@lru_cache(maxsize=4096)
def _embed(model_name: str, text: str) -> np.ndarray:
    model = _load_model(model_name)
    return model.encode(text, normalize_embeddings=True)


@lru_cache(maxsize=1)
def _load_model(model_name: str) -> SentenceTransformer:
    return SentenceTransformer(model_name)
