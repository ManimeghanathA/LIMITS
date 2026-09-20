# Baseline Failure Analysis

## Method Reasoning

- `budget_fill`: A position-order sanity baseline that fills budget without understanding the query.
- `keyword_overlap`: A query-aware lexical baseline that exposes whether interaction terms add value.
- `random`: A stochastic lower-bound baseline showing the task is not solved by candidate density alone.

## Feature Knapsack Deep Analysis

- Feature knapsack completed 49/60 method-question-budget cases.
- It missed at least one required evidence unit in 11/60 cases.
- It selected at least one distractor in 37/60 cases.
- Average selected token count is 219.7, so it often stops below larger budgets.

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
- q07_two_hop budget 256: F1=0.571, complete=False, missing=['storage'], distractors=['p26'], selected=['p02', 'p04', 'p11', 'p14', 'p23', 'p25', 'p26', 'p40']
- q13_three_hop budget 128: F1=0.600, complete=False, missing=['cause', 'log'], distractors=['p22'], selected=['p10', 'p22', 'p24', 'p37']
- q11_three_hop budget 256: F1=0.645, complete=False, missing=['storage'], distractors=['p14'], selected=['p01', 'p02', 'p04', 'p14', 'p23', 'p27', 'p37', 'p40']
- q13_three_hop budget 512: F1=0.724, complete=False, missing=['log'], distractors=['p22'], selected=['p01', 'p04', 'p09', 'p10', 'p12', 'p22', 'p24', 'p36', 'p37', 'p38']
- q13_three_hop budget 1024: F1=0.724, complete=False, missing=['log'], distractors=['p22'], selected=['p01', 'p04', 'p09', 'p10', 'p12', 'p22', 'p24', 'p36', 'p37', 'p38']
- q12_three_hop budget 128: F1=0.750, complete=False, missing=['printout'], distractors=['p33'], selected=['p06', 'p28', 'p31', 'p33']
- q13_three_hop budget 256: F1=0.750, complete=False, missing=['log'], distractors=['p22'], selected=['p01', 'p10', 'p12', 'p22', 'p24', 'p36', 'p37', 'p38']
- q14_three_hop budget 128: F1=0.750, complete=False, missing=['binder'], distractors=['p33'], selected=['p05', 'p06', 'p07', 'p33']
- q11_three_hop budget 128: F1=0.800, complete=False, missing=['storage'], distractors=[], selected=['p02', 'p04', 'p27', 'p40']
