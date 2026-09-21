# Baseline Failure Analysis

## Method Reasoning

- `budget_fill`: A position-order sanity baseline that fills budget without understanding the query.
- `keyword_overlap`: A query-aware lexical baseline that exposes whether interaction terms add value.
- `random`: A stochastic lower-bound baseline showing the task is not solved by candidate density alone.

## Feature Knapsack Deep Analysis

- Feature knapsack completed 106/120 method-question-budget cases.
- It missed at least one required evidence unit in 14/120 cases.
- It selected at least one distractor in 50/120 cases.
- Average selected token count is 222.4, so it often stops below larger budgets.

### Bias Risks

- Lexical overlap bias: query words can dominate when useful chunks use different wording.
- Prefilter bias: exact optimization only sees the top-ranked candidate subset.
- Short chunk bias: candidate ranking prefers lower token cost on ties.
- Synthetic wording bias: current formulas may fit the first authored content style.
- Distractor overlap bias: same-entity wrong facts can look valuable under keyword coverage.

### Formula Tuning Targets

- Prioritize complete-hit recovery in category: three_hop.
- Reduce distractor selection before increasing optional-support reward.
- Inspect whether failures come from prefilter loss or utility scoring after prefiltering.
- Tune redundancy and complementarity weights only after checking missing-unit patterns.

## Worst Feature-Knapsack Cases

- c_q01_direct budget 128: F1=0.000, complete=False, missing=['student_access', 'annex_alias'], distractors=['c04'], selected=['c04', 'c13', 'c16', 'c24']
- c_q01_direct budget 256: F1=0.000, complete=False, missing=['student_access', 'annex_alias'], distractors=['c04'], selected=['c03', 'c04', 'c13', 'c15', 'c16', 'c24']
- c_q01_direct budget 512: F1=0.000, complete=False, missing=['student_access', 'annex_alias'], distractors=['c04'], selected=['c03', 'c04', 'c13', 'c15', 'c16', 'c21', 'c24']
- c_q01_direct budget 1024: F1=0.000, complete=False, missing=['student_access', 'annex_alias'], distractors=['c04'], selected=['c03', 'c04', 'c13', 'c15', 'c16', 'c21', 'c24']
- c_q08_two_hop budget 256: F1=0.480, complete=False, missing=['collector'], distractors=[], selected=['c01', 'c11', 'c12', 'c27', 'c29', 'c30', 'c32', 'c35']
- q13_three_hop budget 128: F1=0.600, complete=False, missing=['log', 'reviewer'], distractors=['p22'], selected=['p09', 'p10', 'p22', 'p36']
- q07_two_hop budget 128: F1=0.706, complete=False, missing=['open_condition'], distractors=['p26'], selected=['p02', 'p03', 'p26', 'p40']
- c_q05_direct budget 128: F1=0.706, complete=False, missing=['owner_location'], distractors=[], selected=['c17', 'c18', 'c20', 'c25']
- c_q09_two_hop budget 128: F1=0.706, complete=False, missing=['reviewer_location'], distractors=[], selected=['c33', 'c34', 'c36', 'c37']
- c_q13_three_hop budget 128: F1=0.706, complete=False, missing=['office'], distractors=[], selected=['c33', 'c34', 'c36', 'c37']
