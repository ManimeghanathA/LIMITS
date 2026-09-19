from __future__ import annotations

import random

from .contracts import BenchmarkExample, CandidateChunk, CandidateInput, ExampleLabels


_ENTITIES = {
    "train": ("Aster", "Beryl", "Cobalt", "Dahlia", "Ember"),
    "validation": ("Fjord", "Garnet", "Helix", "Indigo", "Jasper"),
    "test": ("Kestrel", "Lumen", "Mica", "Nacre", "Onyx"),
}

_RELATIONS = ("founded", "supplies", "operates")


def _chunk(chunk_id: str, text: str, kind: str) -> CandidateChunk:
    return CandidateChunk(
        id=chunk_id,
        text=text,
        token_cost=max(1, len(text.split())),
        metadata={"kind": kind},
    )


def generate_example(seed: int, split: str, hop_depth: int) -> BenchmarkExample:
    if split not in _ENTITIES:
        raise ValueError("split must be train, validation, or test")
    if hop_depth not in {1, 2, 3}:
        raise ValueError("initial benchmark supports hop depths 1 through 3")

    rng = random.Random(seed)
    entities = _ENTITIES[split]
    start = rng.randrange(len(entities))
    chain = tuple(entities[(start + index) % len(entities)] for index in range(hop_depth + 1))

    support = []
    for index in range(hop_depth):
        relation = _RELATIONS[index]
        support.append(
            _chunk(
                f"s{index}",
                f"{chain[index]} {relation} {chain[index + 1]}.",
                "support",
            )
        )

    distractors = [
        _chunk("d_wrong", f"{chain[0]} {_RELATIONS[0]} {entities[(start + 2) % len(entities)]}.", "wrong_relation"),
        _chunk("d_redundant", f"Records confirm that {support[0].text.lower()}", "redundant"),
        _chunk("d_disconnected", f"{entities[-1]} archives annual weather reports.", "disconnected"),
    ]
    chunks = support + distractors
    rng.shuffle(chunks)

    support_ids = frozenset(chunk.id for chunk in support)
    support_cost = sum(chunk.token_cost for chunk in support)
    total_cost = sum(chunk.token_cost for chunk in chunks)
    budget = min(total_cost - 1, support_cost + max(1, support_cost // 3))
    public = CandidateInput(
        query=f"Starting from {chain[0]}, which entity is reached after {hop_depth} relation step(s)?",
        chunks=tuple(chunks),
        token_budget=budget,
    )
    labels = ExampleLabels(
        answer=chain[-1],
        support_sets=(support_ids,),
        hop_depth=hop_depth,
        feasible=True,
        entity_ids=frozenset(chain),
    )
    return BenchmarkExample(public, labels, split, f"{split}_chain_v1")


def permute_example(example: BenchmarkExample, seed: int) -> BenchmarkExample:
    chunks = list(example.public.chunks)
    original_ids = [chunk.id for chunk in chunks]
    random.Random(seed).shuffle(chunks)
    if len(chunks) > 1 and [chunk.id for chunk in chunks] == original_ids:
        chunks = chunks[1:] + chunks[:1]
    public = CandidateInput(example.public.query, tuple(chunks), example.public.token_budget)
    return BenchmarkExample(public, example.labels, example.split, example.template_family)
