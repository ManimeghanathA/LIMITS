# Feature-Based Knapsack Baseline

This document explains the current knapsack baseline in LIMITS. It is intentionally transparent and will evolve as the scoring formula improves.

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
src/knapsack_features.py
```

The benchmark calls it through:

```text
feature_based_knapsack_selector(...)
```

The pipeline is:

```text
question + candidate paragraphs
  -> tokenize query and paragraphs
  -> compute public text features
  -> rank candidates by individual score
  -> keep top 10 candidates
  -> build an InteractionUtility
  -> exact optimize the reduced pool under budget
  -> return selected chunk ids
```

The top-10 prefilter exists because exact subset search over all 40 candidates would be too slow. This is a practical compromise, but it is also a possible bias source.

## Tokenization

The scorer lowercases text, extracts alphanumeric terms, and removes a small stopword list:

```text
a, an, and, are, at, be, by, for, in, is, it, of, on, or,
the, to, what, when, where, which, who, why
```

This is simple and inspectable, but it also means the current model is lexical. It does not yet understand synonyms, paraphrases, or deeper semantics.

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

## Individual Score

Each chunk receives an individual score based on query-term overlap:

```text
coverage = |query_terms ∩ paragraph_terms| / |query_terms|
term_hits = |query_terms ∩ paragraph_terms|

individual =
  3.0 * coverage
  + 0.15 * term_hits
```

This means chunks that directly mention query terms rank higher.

Current risk:

```text
Wrong but query-similar chunks can score highly.
Low-overlap but necessary bridge chunks may be missed during prefiltering.
```

## Pair Synergy

For every pair, the system checks whether the pair covers more query terms than either chunk alone:

```text
gain =
  coverage(chunk_i ∪ chunk_j)
  - max(coverage(chunk_i), coverage(chunk_j))

pair_synergy = 2.0 * gain
```

This is meant to reward complementary chunks.

Current risk:

```text
Complementarity is still measured lexically.
It may reward two partial keyword chunks even if they do not logically connect.
```

## Triple Synergy

For every triple, the system checks whether the three chunks cover more query terms than the best pair among them:

```text
gain =
  coverage(chunk_i ∪ chunk_j ∪ chunk_k)
  - best_pair_coverage

triple_synergy = 1.25 * gain
```

This is the first transparent approximation of higher-order context synergy.

Current risk:

```text
This is not true reasoning yet.
It only measures extra query-term coverage from a three-chunk combination.
```

## Redundancy Penalty

For every pair, redundancy is estimated using Jaccard similarity over paragraph terms:

```text
redundancy = 1.5 * Jaccard(paragraph_terms_i, paragraph_terms_j)
```

The final utility subtracts this value.

Current risk:

```text
Valid alternatives and wrong similar distractors can both look redundant.
The model does not yet know contradiction or factual correctness.
```

## Exact Optimization

After prefiltering to the top 10 candidates, the existing exact optimizer evaluates feasible subsets and returns the best one under budget.

Tie-breaking prefers:

```text
higher utility
lower token usage
stable sorted ids
```

This behavior is useful because the selector does not need to fill the budget if the scoring formula thinks extra chunks do not help.

## Current Benchmark Status

On `content_01_aero_support`, the current report shows:

```text
feature_knapsack evidence F1:        0.675
feature_knapsack complete hit rate:  0.817
feature_knapsack required recall:    0.933
feature_knapsack optional recall:    0.658
feature_knapsack budget utilization: 0.647
```

The early interpretation:

```text
The model is doing more than naive keyword selection because it gets higher evidence F1 while using less budget.
But it is not proven robust yet.
```

## Known Bias Risks

- Lexical overlap bias.
- Prefilter bias.
- Short chunk bias.
- Synthetic wording bias.
- Distractor overlap bias.
- No semantic paraphrase understanding.
- No contradiction detection.
- No learned notion of answerability.

## Next Improvement Direction

Before tuning blindly, use:

```text
reports/baselines/failure_analysis.md
reports/baselines/failure_analysis.json
```

The next formula work should focus on:

- failures where required units are missing,
- cases where distractors are selected,
- cases where prefiltering removes useful low-overlap chunks,
- category-specific weakness,
- budget-specific weakness.

Only after this should we tune weights or add new features.
