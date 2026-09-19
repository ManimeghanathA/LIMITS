from limits.synthetic import generate_example, permute_example


def test_generation_is_deterministic_for_a_seed() -> None:
    first = generate_example(seed=17, split="train", hop_depth=3)
    second = generate_example(seed=17, split="train", hop_depth=3)

    assert first == second


def test_permutation_changes_order_without_changing_semantics() -> None:
    example = generate_example(seed=3, split="train", hop_depth=2)
    permuted = permute_example(example, seed=91)

    assert tuple(c.id for c in permuted.public.chunks) != tuple(
        c.id for c in example.public.chunks
    )
    assert {c.id for c in permuted.public.chunks} == {
        c.id for c in example.public.chunks
    }
    assert permuted.labels == example.labels


def test_splits_use_distinct_entities_and_template_families() -> None:
    train = generate_example(seed=7, split="train", hop_depth=2)
    test = generate_example(seed=7, split="test", hop_depth=2)

    assert train.template_family != test.template_family
    assert train.labels.entity_ids.isdisjoint(test.labels.entity_ids)


def test_example_contains_support_and_hard_distractor_types() -> None:
    example = generate_example(seed=11, split="validation", hop_depth=3)
    kinds = {chunk.metadata["kind"] for chunk in example.public.chunks}

    assert len(example.labels.support_sets[0]) == 3
    assert {"support", "wrong_relation", "redundant", "disconnected"} <= kinds


def test_budget_is_sufficient_for_minimal_support_but_not_all_chunks() -> None:
    example = generate_example(seed=5, split="train", hop_depth=3)
    chunks = {chunk.id: chunk for chunk in example.public.chunks}
    support_cost = sum(chunks[item].token_cost for item in example.labels.support_sets[0])
    total_cost = sum(chunk.token_cost for chunk in example.public.chunks)

    assert example.public.token_budget >= support_cost
    assert example.public.token_budget < total_cost

