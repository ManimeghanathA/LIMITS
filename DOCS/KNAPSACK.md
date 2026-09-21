# Feature-Based Knapsack Baseline

This document explains the current knapsack baseline in LIMITS. It is intentionally transparent and should evolve as the scoring formula improves.

## Purpose

The knapsack baseline selects context chunks under a token budget. It receives only public inference-time inputs:

```text
query
candidate paragraphs
token budget
```

It does not receive:

```text
ground-truth evidence labels
question category as a feature
required evidence units
optional support units
distractor labels
```

Those labels are only used by the evaluator after selection.

## Current Pipeline

The current selector is implemented in:

```text
src/semantic_features.py
src/knapsack_features.py
```

The benchmark calls it through:

```text
feature_based_knapsack_selector(...)
```

The pipeline is:

```text
question + candidate paragraphs + token budget
  -> compute sparse lexical features
  -> compute fixed MiniLM dense similarities
  -> build a mixed sparse+dense 15-candidate pool
  -> build an InteractionUtility
  -> exact optimize the reduced pool under budget
  -> return selected chunk ids
```

The embedding backend is fixed:

```text
sentence-transformers/all-MiniLM-L6-v2
```

There is no fallback mode. If this dependency or model is unavailable, the benchmark should fail clearly rather than changing behavior silently.

The 15-candidate prefilter exists because exact subset search over all 40 candidates is expensive. This remains a possible bias source, but the current debug report shows no prefilter failures, so the harder problem right now is scoring quality inside the candidate pool.

```text
reports/baselines/knapsack_debug.md
```

Among incomplete knapsack selections, the current breakdown is:

```text
scoring_failure: 9
distractor_failure: 7
```

## Tokenization

The sparse scorer lowercases text, extracts alphanumeric terms, and removes a small stopword list:

```text
a, an, and, are, at, be, by, for, in, is, it, of, on, or,
the, to, what, when, where, which, who, why
```

These sparse features are deliberately still present. The current benchmark is not dense-only; it combines keyword hints with semantic similarity.

## Utility Function

The optimizer maximizes:

```text
individual chunk value
+ pair synergy
+ triple synergy
- redundancy penalty
```

subject to:

```text
total selected tokens <= budget
```

This is represented by `InteractionUtility`:

```text
U(S) =
  sum individual[i]
  + sum pair_synergy[i,j]
  + sum triple_synergy[i,j,k]
  - redundancy_weight * sum pair_redundancy[i,j]
```

Current `redundancy_weight`:

```text
0.75
```

The exact optimizer does not force the selected context to fill the full budget. A paragraph must earn enough utility to justify its token cost and selection penalty.

## Individual Score

Each chunk receives an individual score from sparse query evidence, dense query similarity, seed linkage, and token cost.

Sparse query overlap:

```text
coverage = |query_terms ∩ paragraph_terms| / |query_terms|
term_hits = |query_terms ∩ paragraph_terms|

sparse_query_score =
  3.0 * coverage
  + 0.15 * term_hits
```

Dense query similarity:

```text
dense_query_score = 0.5 * max(0, cosine(query_embedding, paragraph_embedding))
```

Budget-aware token penalty:

```text
token_penalty = 1.0 * paragraph_tokens / budget
```

Seed linkage:

```text
sparse_seed_link =
  max over seeds:
    |paragraph_terms ∩ seed_terms| / min(|paragraph_terms|, |seed_terms|)

dense_seed_link =
  max over seeds:
    cosine(seed_embedding, paragraph_embedding)
```

Final individual score:

```text
individual =
  sparse_query_score
  + dense_query_score
  + 3.0 * sparse_seed_link
  + 0.3 * max(0, dense_seed_link)
  - 1.0 * selection_penalty
  - token_penalty
```

This gives direct evidence a route through query relevance and gives bridge evidence a route through connection to strong seeds.

## Candidate Pool

The selector keeps up to 15 candidates before exact optimization.

The pool is built from:

```text
up to 5 strongest sparse query-overlap candidates
up to 5 strongest dense query-similarity candidates
remaining candidates ranked by hybrid individual score
```

Duplicate candidates are not added twice, but overlap between sparse and dense top lists counts as representation from both signals. That prevents one scoring family from crowding out the other.

## Pair Synergy

For every pair, the system checks whether the pair covers more query terms than either chunk alone:

```text
gain =
  coverage(chunk_i ∪ chunk_j)
  - max(coverage(chunk_i), coverage(chunk_j))
```

It also rewards paragraph-to-paragraph sparse linkage:

```text
pair_link =
  |paragraph_terms_i ∩ paragraph_terms_j|
  / min(|paragraph_terms_i|, |paragraph_terms_j|)
```

Current pair score:

```text
pair_synergy =
  2.0 * max(0, query_complementarity_gain)
  + 1.2 * pair_link
```

Dense pair linkage exists in the code but is currently weighted as `0.0`. During tuning it increased context bloat and distractor selection, so it is disabled in the canonical formula for now.

## Triple Synergy

For every triple, the system checks whether the three chunks cover more query terms than the best pair among them:

```text
gain =
  coverage(chunk_i ∪ chunk_j ∪ chunk_k)
  - best_pair_coverage

triple_synergy = 1.25 * max(0, gain)
```

This is the current explicit third-order synergy approximation. It is useful for transparent optimization, but it is not the same as true logical reasoning.

## Redundancy Penalty

Redundancy is computed for every pair of selected chunks. If paragraph `i` is redundant with both `j` and `k`, the selected subset receives both pair penalties:

```text
penalty(i,j) + penalty(i,k)
```

Sparse redundancy:

```text
lexical_jaccard =
  |paragraph_terms_i ∩ paragraph_terms_j|
  / |paragraph_terms_i ∪ paragraph_terms_j|
```

Dense redundancy only activates above a similarity threshold:

```text
semantic_excess = max(0, dense_similarity - 0.72)
semantic_penalty = semantic_excess / (1 - 0.72)
```

Final pair redundancy:

```text
pair_redundancy =
  1.5 * lexical_jaccard
  + 0.75 * semantic_penalty
```

Final utility subtracts:

```text
0.75 * sum(pair_redundancy)
```

This handles exact overlap and some paraphrased duplication. It still cannot reliably distinguish a valid paraphrase from a semantically similar but wrong distractor; that requires a stronger verifier.

## Contradiction Handling

The current canonical knapsack does not use a manual contradiction penalty.

Reason:

```text
Manual word rules can falsely mark true evidence as contradictory.
```

A better future path is to add a meaning-aware NLI or cross-encoder verifier. That can estimate whether two chunks support, contradict, or are unrelated to each other without relying on guessed words like "old", "new", "wrong", or "changed".

## Exact Optimization

After prefiltering to 15 candidates, the exact optimizer evaluates feasible subsets and returns the best one under budget.

Maximum subset count:

```text
2^15 = 32768
```

Tie-breaking prefers:

```text
higher utility
lower token usage
stable sorted ids
```

This behavior is important because the benchmark should select enough evidence, not simply fill the budget.

## Current Benchmark Status

Across the two current content collections, the current report shows:

```text
feature_knapsack evidence F1:        0.713
feature_knapsack complete hit rate:  0.867
feature_knapsack required recall:    0.935
feature_knapsack optional recall:    0.850
feature_knapsack budget utilization: 0.632
feature_knapsack avg distractors:    0.617
```

Interpretation:

```text
The model is much stronger than budget fill, random selection, and keyword overlap on evidence F1, complete-hit rate, and required recall while using less budget.
The remaining weakness is not candidate recall. It is ranking true evidence above wrong but plausible distractors.
```

## Known Bias Risks

- Lexical overlap bias: reduced by dense query/seed similarity, but not eliminated.
- Prefilter bias: reduced by a 15-candidate sparse+dense pool, but still present.
- Short chunk bias: token penalty is intentional, but can over-favor compact chunks.
- Synthetic wording bias: still present until the dataset expands beyond two contents.
- Distractor overlap bias: still the main hard failure type.
- No contradiction detection: intentionally deferred until we use a real verifier.
- No learned notion of answerability: this is where RL or a learned reranker may later help.

## Debugging the Knapsack

Use this command to regenerate the knapsack diagnostic report:

```text
python scripts/run_knapsack_debug.py
```

Use this command to regenerate the full question-by-question inspection report:

```text
python scripts/run_knapsack_inspection.py
```

The inspection report is stored at:

```text
reports/baselines/knapsack_inspection.md
```

It shows, for every question and budget:

- selected paragraph ids,
- missing required evidence units,
- selected distractors,
- candidate-pool rows,
- individual importance score per candidate,
- selected subset score breakdown,
- and a suggested improvement direction.

The report classifies each incomplete selection into:

- `prefilter_failure`: at least one missing required evidence unit had no valid alternative inside the top candidate pool.
- `scoring_failure`: the required evidence entered the candidate pool but the optimizer still skipped it.
- `distractor_failure`: missing required evidence coincided with selected distractor chunks.

This matters because each cause needs a different fix:

- prefilter failures need better candidate ranking or a wider candidate pool,
- scoring failures need better individual, pair, triple, or redundancy scoring,
- distractor failures need contradiction/wrong-context features instead of raw lexical overlap.
