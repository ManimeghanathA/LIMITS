# Knapsack Debug Report

## Failure Cause Summary

- `distractor_failure`: 5
- `scoring_failure`: 11

## Worst Cases

- c_q01_direct budget 128: cause=distractor_failure, F1=0.000, missing=['student_access', 'annex_alias'], distractors=['c04'], selected=['c04', 'c15', 'c16', 'c24']
- c_q01_direct budget 256: cause=distractor_failure, F1=0.000, missing=['student_access', 'annex_alias'], distractors=['c04'], selected=['c03', 'c04', 'c13', 'c15', 'c16', 'c24']
- c_q13_three_hop budget 128: cause=scoring_failure, F1=0.400, missing=['liaison', 'office'], distractors=[], selected=['c33', 'c36', 'c37', 'c40']
- c_q08_two_hop budget 256: cause=scoring_failure, F1=0.480, missing=['collector'], distractors=[], selected=['c01', 'c05', 'c24', 'c27', 'c29', 'c30', 'c32', 'c35']
- q13_three_hop budget 128: cause=distractor_failure, F1=0.600, missing=['log', 'reviewer'], distractors=['p22'], selected=['p09', 'p10', 'p22', 'p36']
- q07_two_hop budget 128: cause=distractor_failure, F1=0.706, missing=['open_condition'], distractors=['p26'], selected=['p02', 'p03', 'p26', 'p40']
- c_q05_direct budget 128: cause=scoring_failure, F1=0.706, missing=['owner_location'], distractors=[], selected=['c17', 'c18', 'c20', 'c25']
- c_q08_two_hop budget 128: cause=scoring_failure, F1=0.706, missing=['collector'], distractors=[], selected=['c29', 'c30', 'c32', 'c35']
- c_q09_two_hop budget 128: cause=scoring_failure, F1=0.706, missing=['reviewer_location'], distractors=[], selected=['c33', 'c34', 'c36', 'c37']
- c_q10_two_hop budget 128: cause=scoring_failure, F1=0.706, missing=['roster'], distractors=[], selected=['c33', 'c37', 'c38', 'c40']
- c_q15_three_hop budget 128: cause=scoring_failure, F1=0.706, missing=['collector'], distractors=[], selected=['c28', 'c29', 'c30', 'c32']
- q11_three_hop budget 128: cause=scoring_failure, F1=0.800, missing=['storage'], distractors=[], selected=['p02', 'p04', 'p27', 'p40']

## Next Tuning Direction

- If `prefilter_failure` dominates, improve candidate ranking before changing optimizer weights.
- If `scoring_failure` dominates, tune pair/triple synergy and redundancy penalties.
- If `distractor_failure` dominates, add wrong-context or contradiction-aware features.
- Do not tune on aggregate F1 alone; complete-hit and missing-unit recovery matter most.
