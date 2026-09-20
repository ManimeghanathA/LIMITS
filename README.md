# LIMITS

**Learning to Identify Minimal Information under Token and Synergy constraints**

LIMITS is a context-selection project for RAG-style systems. The goal is to choose the most useful evidence chunks for a query under a fixed token budget, so the final LLM receives enough context to answer accurately without unnecessary computation cost.

The project is being built in two major stages:

1. A strong feature-based knapsack baseline for token-constrained evidence selection.
2. A sequential reinforcement learning selector that decides whether to include, skip, or stop while tracking remaining budget.

The current focus is building the dataset, evaluator, baseline selectors, and first benchmark pipeline. RL is intentionally not implemented yet.

## Current Baseline Snapshot

The current baseline report is generated from `content_01_aero_support` across all 15 questions and all four budgets.

![Baseline benchmark collage](reports/baselines/baseline_collage.png)

Knapsack documentation:

```text
DOCS/KNAPSACK.md
```

Generated artifacts:

```text
reports/baselines/baseline_rows.json
reports/baselines/baseline_rows.csv
reports/baselines/baseline_summary.json
reports/baselines/baseline_collage.png
reports/baselines/failure_analysis.json
reports/baselines/failure_analysis.md
```

Current baseline summary:

| Method | Evidence F1 | Complete Hit Rate | Required Recall | Optional Support Recall | Budget Utilization | Avg Distractors |
|---|---:|---:|---:|---:|---:|---:|
| `budget_fill` | 0.169 | 0.417 | 0.574 | 0.183 | 0.947 | 0.883 |
| `keyword_overlap` | 0.540 | 0.850 | 0.954 | 0.725 | 0.954 | 0.833 |
| `random` | 0.170 | 0.333 | 0.461 | 0.367 | 0.950 | 0.517 |
| `feature_knapsack` | 0.675 | 0.817 | 0.933 | 0.658 | 0.647 | 0.733 |

This benchmark is still an early comparison, but it now includes the first transparent feature-based knapsack. The current knapsack uses public text features only, prefilters to a small candidate pool, and then exactly optimizes individual, pairwise, and third-order interaction scores under the token budget.

The first failure analysis shows:

```text
feature_knapsack complete cases: 49/60
missing required evidence cases: 11/60
cases with selected distractors: 37/60
main weak category: three_hop
```

This means the current knapsack is useful but not yet robust. The next improvement phase should focus on reducing distractor selection and recovering missing evidence units before adding new complexity.

## Current Project Direction

In a real setting, the selector should receive only:

```text
query
candidate paragraphs/chunks
token budget
```

It should output:

```text
selected paragraph/chunk ids with total tokens <= budget
```

The selector should not be given direct access to ground-truth labels, dependency depth, or hop labels during inference. Those labels exist only for dataset construction, training reward, evaluation, and analysis.

## Dataset Design

The first validated content collection is stored in:

```text
data/limits_dataset.json
```

It currently contains:

- 1 content collection: `content_01_aero_support`
- 40 candidate paragraphs
- candidate pool larger than 1024 tokens
- 15 questions total
- 5 direct questions
- 5 two-hop questions
- 5 three-hop questions
- budget constraints: `128`, `256`, `512`, `1024`

Question category is metadata only. It helps us analyze results by difficulty, but it should not control what the model sees.

## Evidence Model

The dataset now uses evidence units instead of one fixed ground-truth list.

Each question can define:

- `required_evidence_units`: evidence needs that must be satisfied for the answer to be complete.
- `optional_support_units`: useful supporting context that higher budgets may include.
- `budget_ground_truth`: multiple acceptable selections for each budget.
- `redundancy_groups`: genuinely valid alternative evidence.
- `distractor_groups`: similar, outdated, contradictory, or partial chunks that should not count as correct evidence.

Example idea:

```text
required evidence:
  start_time: p05
  cart_location: p06 or p19

valid 128-token answers:
  [p05, p06]
  [p05, p19]

valid higher-budget answers:
  [p05, p06, p32]
  [p05, p19, p32]
```

This avoids unfairly forcing the model to match one authored paragraph when multiple evidence combinations can answer the question.

## Validation Rules Implemented

The dataset validator currently checks:

- content id is valid
- paragraph ids are unique
- paragraph token counts are positive
- total candidate tokens exceed 1024
- question ids are unique
- each category has 5 to 10 questions
- every question has required evidence units
- evidence alternatives reference known paragraphs
- required evidence can fit under the 128-token budget
- every budget has at least one acceptable ground-truth selection
- every ground-truth selection stays within its budget
- every ground-truth selection satisfies all required evidence units
- redundancy and distractor groups reference known paragraphs

## Current Source Layout

```text
src/
  benchmark.py      baseline benchmark runner and report generation
  contracts.py      basic benchmark data contracts
  dataset.py        dataset dataclasses and validation
  dataset_io.py     JSON dataset loader
  dataset_summary.py dataset health summaries
  evidence.py       evidence scoring helpers
  evaluator.py      method-agnostic selection evaluator and RL reward signal
  knapsack_features.py public feature builder and feature-based knapsack selector
  optimizer.py      current exact interaction optimizer wrapper
  oracle.py         exhaustive exact oracle for small candidate pools
  selectors.py      simple baseline selectors
  synthetic.py      small synthetic examples
  utility.py        interaction utility model

scripts/
  run_baseline_benchmark.py
  run_failure_analysis.py

tests/
  test_benchmark.py
  test_dataset.py
  test_dataset_io.py
  test_dataset_summary.py
  test_evaluator.py
  test_selectors.py
  test_contracts.py
  test_evidence.py
  test_optimizer.py
  test_oracle.py
  test_synthetic.py
  test_utility.py
```

## Current Verification

The full test suite currently passes:

```text
python -m pytest -q
56 passed
```

## Next Tasks

1. Improve the feature-based knapsack scoring formula:
   - reduce distractor inclusion
   - improve complete-hit rate
   - tune redundancy and complementarity weights
   - inspect failures by question and budget

2. Add benchmark failure analysis:
   - per-question selected chunks
   - missing required units
   - selected distractors
   - budget waste and underuse

3. Add plots by category and budget:
   - direct vs two-hop vs three-hop
   - 128 vs 256 vs 512 vs 1024

4. After the knapsack baseline is stable, start the RL environment:
   - actions: `INCLUDE`, `SKIP`, `STOP`
   - state: query, current candidate, selected context summary, remaining budget
   - reward: evaluator-based final evidence quality under budget
