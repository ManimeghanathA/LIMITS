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
  -> choose lexical seed candidates
  -> expand candidates using seed-linked paragraph overlap
  -> keep 10 candidates
  -> build an InteractionUtility
  -> exact optimize the reduced pool under budget
  -> return selected chunk ids
```

The top-10 prefilter exists because exact subset search over all 40 candidates would be too slow. This is a practical compromise, but it is also a possible bias source.

The current seed-linked prefilter was added because earlier diagnostics showed that low-overlap bridge evidence was being removed before the optimizer could consider it.

```text
reports/baselines/knapsack_debug.md
```

Among incomplete knapsack selections, the current breakdown is:

```text
scoring_failure: 11
distractor_failure: 5
```

The current debug report has no prefilter failures, which means the next serious improvement is scoring quality inside the reduced candidate pool and wrong-context/distractor handling.

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
- selection penalty
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

The selection penalty is included inside the individual chunk score, so extra chunks must earn enough public-feature value to justify being selected.

## Individual Score

Each chunk receives an individual score based on query-term overlap and seed linkage.

First, lexical seed chunks are ranked by query overlap:

```text
coverage = |query_terms ∩ paragraph_terms| / |query_terms|
term_hits = |query_terms ∩ paragraph_terms|

lexical_score =
  3.0 * coverage
  + 0.15 * term_hits
```

Then each non-seed chunk can receive value if it shares terms with one of the lexical seeds:

```text
seed_link =
  max over lexical seeds:
    |paragraph_terms ∩ seed_terms| / min(|paragraph_terms|, |seed_terms|)

individual =
  lexical_score
  + 3.0 * seed_link
  - 0.8 selection_penalty
```

This means chunks that directly mention query terms rank higher, while bridge chunks can still survive if they connect to a strong seed.

Current risk:

```text
Wrong but query-similar chunks can score highly.
Wrong chunks that share terms with a strong seed may also receive value.
```

## Pair Synergy

For every pair, the system checks whether the pair covers more query terms than either chunk alone:

```text
gain =
  coverage(chunk_i ∪ chunk_j)
  - max(coverage(chunk_i), coverage(chunk_j))

pair_synergy = 2.0 * gain
```

It also rewards paragraph-to-paragraph linkage:

```text
pair_link =
  |paragraph_terms_i ∩ paragraph_terms_j|
  / min(|paragraph_terms_i|, |paragraph_terms_j|)

pair_synergy =
  2.0 * query_complementarity_gain
  + 1.2 * pair_link
```

This is meant to reward complementary chunks and bridge chunks that are connected to answer-bearing evidence even when they have weak direct query overlap.

Current risk:

```text
Complementarity is still measured lexically.
It may reward two chunks that share surface terms even if they do not logically connect.
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

The current redundancy weight is:

```text
redundancy_weight = 0.75
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

Across the two current content collections, the current report shows:

```text
feature_knapsack evidence F1:        0.709
feature_knapsack complete hit rate:  0.867
feature_knapsack required recall:    0.943
feature_knapsack optional recall:    0.842
feature_knapsack budget utilization: 0.626
```

The early interpretation:

```text
The model is now substantially stronger than keyword overlap on evidence F1, complete-hit rate, and required recall while using much less of the token budget.
Its remaining weakness is distractor selection and fine-grained scoring inside hard candidate pools.
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
- category-specific weakness,
- budget-specific weakness.

Only after this should we tune weights or add new features.

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
