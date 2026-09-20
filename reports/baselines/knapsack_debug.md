# Knapsack Debug Report

## Failure Cause Summary

- `distractor_failure`: 10
- `scoring_failure`: 14

## Worst Cases

- c_q01_direct budget 128: cause=distractor_failure, F1=0.000, missing=['student_access', 'annex_alias'], distractors=['c04'], selected=['c04', 'c13', 'c15', 'c24']
- c_q01_direct budget 512: cause=distractor_failure, F1=0.308, missing=['student_access'], distractors=['c04'], selected=['c02', 'c03', 'c04', 'c13', 'c15', 'c16', 'c21', 'c24', 'c35']
- c_q01_direct budget 1024: cause=distractor_failure, F1=0.308, missing=['student_access'], distractors=['c04'], selected=['c02', 'c03', 'c04', 'c13', 'c15', 'c16', 'c21', 'c24', 'c35']
- c_q01_direct budget 256: cause=distractor_failure, F1=0.333, missing=['student_access'], distractors=['c04'], selected=['c02', 'c03', 'c04', 'c13', 'c15', 'c16', 'c24', 'c35']
- c_q13_three_hop budget 128: cause=scoring_failure, F1=0.400, missing=['liaison', 'office'], distractors=[], selected=['c20', 'c33', 'c36', 'c40']
- c_q08_two_hop budget 256: cause=scoring_failure, F1=0.480, missing=['collector'], distractors=[], selected=['c01', 'c05', 'c24', 'c27', 'c29', 'c30', 'c32', 'c35']
- q07_two_hop budget 256: cause=distractor_failure, F1=0.571, missing=['open_condition'], distractors=['p26'], selected=['p02', 'p03', 'p11', 'p14', 'p23', 'p26', 'p36', 'p40']
- q13_three_hop budget 128: cause=distractor_failure, F1=0.600, missing=['log', 'reviewer'], distractors=['p22'], selected=['p09', 'p10', 'p22', 'p37']
- q10_two_hop budget 128: cause=scoring_failure, F1=0.600, missing=['log_requirement'], distractors=[], selected=['p10', 'p12', 'p24', 'p37']
- q03_direct budget 128: cause=scoring_failure, F1=0.667, missing=['start_time'], distractors=[], selected=['p06', 'p18', 'p19', 'p32']
- q07_two_hop budget 128: cause=distractor_failure, F1=0.706, missing=['open_condition'], distractors=['p26'], selected=['p02', 'p03', 'p26', 'p40']
- c_q03_direct budget 128: cause=scoring_failure, F1=0.706, missing=['overflow_meaning'], distractors=[], selected=['c08', 'c09', 'c11', 'c12']

## Next Tuning Direction

- If `prefilter_failure` dominates, improve candidate ranking before changing optimizer weights.
- If `scoring_failure` dominates, tune pair/triple synergy and redundancy penalties.
- If `distractor_failure` dominates, add wrong-context or contradiction-aware features.
- Do not tune on aggregate F1 alone; complete-hit and missing-unit recovery matter most.
