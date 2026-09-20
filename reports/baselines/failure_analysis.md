# Baseline Failure Analysis

## Method Reasoning

- `budget_fill`: A position-order sanity baseline that fills budget without understanding the query.
- `keyword_overlap`: A query-aware lexical baseline that exposes whether interaction terms add value.
- `random`: A stochastic lower-bound baseline showing the task is not solved by candidate density alone.

## Feature Knapsack Deep Analysis

- Feature knapsack completed 82/120 method-question-budget cases.
- It missed at least one required evidence unit in 38/120 cases.
- It selected at least one distractor in 49/120 cases.
- Average selected token count is 186.2, so it often stops below larger budgets.

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

- q07_two_hop budget 128: F1=0.000, complete=False, missing=['approver', 'storage', 'open_condition'], distractors=['p26'], selected=['p11', 'p23', 'p26', 'p40']
- c_q01_direct budget 128: F1=0.000, complete=False, missing=['student_access', 'annex_alias'], distractors=['c04'], selected=['c04', 'c16', 'c24']
- c_q01_direct budget 256: F1=0.000, complete=False, missing=['student_access', 'annex_alias'], distractors=['c04'], selected=['c04', 'c16', 'c24']
- c_q01_direct budget 512: F1=0.000, complete=False, missing=['student_access', 'annex_alias'], distractors=['c04'], selected=['c04', 'c16', 'c24']
- c_q01_direct budget 1024: F1=0.000, complete=False, missing=['student_access', 'annex_alias'], distractors=['c04'], selected=['c04', 'c16', 'c24']
- c_q13_three_hop budget 128: F1=0.400, complete=False, missing=['liaison', 'office'], distractors=[], selected=['c20', 'c33', 'c36', 'c40']
- c_q15_three_hop budget 128: F1=0.400, complete=False, missing=['code', 'collector'], distractors=[], selected=['c20', 'c28', 'c29', 'c32']
- c_q08_two_hop budget 512: F1=0.414, complete=False, missing=['collector'], distractors=[], selected=['c01', 'c05', 'c11', 'c12', 'c24', 'c27', 'c29', 'c30', 'c32', 'c35']
- c_q08_two_hop budget 1024: F1=0.414, complete=False, missing=['collector'], distractors=[], selected=['c01', 'c05', 'c11', 'c12', 'c24', 'c27', 'c29', 'c30', 'c32', 'c35']
- c_q08_two_hop budget 256: F1=0.480, complete=False, missing=['collector'], distractors=[], selected=['c01', 'c05', 'c12', 'c24', 'c29', 'c30', 'c32', 'c35']
