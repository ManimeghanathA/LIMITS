# Knapsack Debug Report

## Failure Cause Summary

- `distractor_failure`: 5
- `prefilter_failure`: 28
- `scoring_failure`: 5

## Worst Cases

- c_q01_direct budget 128: cause=prefilter_failure, F1=0.000, missing=['student_access', 'annex_alias'], distractors=['c04'], selected=['c04', 'c06', 'c16', 'c24']
- c_q01_direct budget 256: cause=prefilter_failure, F1=0.000, missing=['student_access', 'annex_alias'], distractors=['c04'], selected=['c04', 'c06', 'c16', 'c24']
- c_q01_direct budget 512: cause=prefilter_failure, F1=0.000, missing=['student_access', 'annex_alias'], distractors=['c04'], selected=['c04', 'c06', 'c16', 'c24']
- c_q01_direct budget 1024: cause=prefilter_failure, F1=0.000, missing=['student_access', 'annex_alias'], distractors=['c04'], selected=['c04', 'c06', 'c16', 'c24']
- q07_two_hop budget 128: cause=distractor_failure, F1=0.000, missing=['approver', 'storage', 'open_condition'], distractors=['p26'], selected=['p11', 'p23', 'p26', 'p40']
- c_q13_three_hop budget 128: cause=prefilter_failure, F1=0.400, missing=['liaison', 'office'], distractors=[], selected=['c20', 'c33', 'c36', 'c40']
- c_q15_three_hop budget 128: cause=prefilter_failure, F1=0.400, missing=['code', 'collector'], distractors=[], selected=['c20', 'c28', 'c29', 'c32']
- c_q08_two_hop budget 512: cause=prefilter_failure, F1=0.414, missing=['collector'], distractors=[], selected=['c01', 'c05', 'c11', 'c12', 'c24', 'c27', 'c29', 'c30', 'c32', 'c35']
- c_q08_two_hop budget 1024: cause=prefilter_failure, F1=0.414, missing=['collector'], distractors=[], selected=['c01', 'c05', 'c11', 'c12', 'c24', 'c27', 'c29', 'c30', 'c32', 'c35']
- c_q08_two_hop budget 256: cause=prefilter_failure, F1=0.480, missing=['collector'], distractors=[], selected=['c01', 'c05', 'c12', 'c24', 'c29', 'c30', 'c32', 'c35']
- q07_two_hop budget 256: cause=distractor_failure, F1=0.571, missing=['storage'], distractors=['p26'], selected=['p02', 'p04', 'p11', 'p14', 'p23', 'p25', 'p26', 'p40']
- c_q13_three_hop budget 256: cause=prefilter_failure, F1=0.571, missing=['office'], distractors=[], selected=['c20', 'c33', 'c34', 'c36', 'c37', 'c40']

## Next Tuning Direction

- If `prefilter_failure` dominates, improve candidate ranking before changing optimizer weights.
- If `scoring_failure` dominates, tune pair/triple synergy and redundancy penalties.
- If `distractor_failure` dominates, add wrong-context or contradiction-aware features.
- Do not tune on aggregate F1 alone; complete-hit and missing-unit recovery matter most.
