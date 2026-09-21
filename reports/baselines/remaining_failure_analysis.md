# Remaining Knapsack Failure Analysis

This report analyzes the 14 remaining failed feature-knapsack question-budget cases after the balanced `pair_linkage = 1.3` checkpoint.

## Summary

- Failed cases: `14/120`
- By category: `{'two_hop': 3, 'three_hop': 6, 'direct': 5}`
- By budget: `{'128': 9, '256': 3, '512': 1, '1024': 1}`
- Failure causes: `{"distractor_failure": 7, "scoring_failure": 7}`

## Repeated Patterns

- The largest single unresolved issue is `c_q01_direct`, which fails for all four budgets.
- Most failures happen at `128` tokens, where one extra wrong chunk can displace a required final-hop chunk.
- The required chunks usually enter the 15-candidate pool. This is mostly scoring, not retrieval/prefilter loss.
- Similarity and sparse overlap are not enough for wrong-context distractors. The system needs a support/verifier signal.

## Failed Cases

### content_01_aero_support / q07_two_hop / budget 128

- Category: `two_hop`
- F1: `0.706`
- Missing required units: `['open_condition']`
- Selected ids: `['p02', 'p03', 'p26', 'p40']`
- Selected required alternatives: `['p03', 'p02']`
- Unselected required alternatives in candidate pool: `['p04', 'p27']`
- Selected distractors: `['p26']`
- Diagnosis: wrong-context distractor outranked or co-selected with true evidence.
- Next useful signal: `support/contradiction verifier`

Required candidate scores: `p03:3.411*, p02:1.924*, p04:0.928, p27:-0.498`

Distractor candidate scores: `p26:2.858*`

### content_01_aero_support / q11_three_hop / budget 128

- Category: `three_hop`
- F1: `0.800`
- Missing required units: `['storage']`
- Selected ids: `['p02', 'p04', 'p27', 'p40']`
- Selected required alternatives: `['p04', 'p02', 'p27']`
- Unselected required alternatives in candidate pool: `['p03']`
- Selected distractors: `[]`
- Diagnosis: final-hop evidence scored too weakly or was crowded by loosely linked context.
- Next useful signal: `query-conditioned support score or path-completion score`

Required candidate scores: `p04:3.631*, p02:2.458*, p27:2.565*, p03:0.245`

Distractor candidate scores: `p14:1.031, p26:-0.072`

### content_01_aero_support / q13_three_hop / budget 128

- Category: `three_hop`
- F1: `0.600`
- Missing required units: `['log', 'reviewer']`
- Selected ids: `['p09', 'p10', 'p22', 'p36']`
- Selected required alternatives: `['p10', 'p09', 'p36']`
- Unselected required alternatives in candidate pool: `['p24', 'p11', 'p39', 'p12']`
- Selected distractors: `['p22']`
- Diagnosis: wrong-context distractor outranked or co-selected with true evidence.
- Next useful signal: `support/contradiction verifier`

Required candidate scores: `p10:2.165*, p24:0.540, p09:1.690*, p11:-0.189, p39:0.013, p12:0.240, p36:1.305*`

Distractor candidate scores: `p22:0.951*, p29:-0.248`

### content_01_aero_support / q13_three_hop / budget 256

- Category: `three_hop`
- F1: `0.808`
- Missing required units: `['log']`
- Selected ids: `['p09', 'p10', 'p12', 'p22', 'p24', 'p36', 'p37', 'p38']`
- Selected required alternatives: `['p10', 'p24', 'p09', 'p12', 'p36']`
- Unselected required alternatives in candidate pool: `['p11', 'p39']`
- Selected distractors: `['p22']`
- Diagnosis: wrong-context distractor outranked or co-selected with true evidence.
- Next useful signal: `support/contradiction verifier`

Required candidate scores: `p10:1.549*, p24:0.891*, p09:1.808*, p11:-0.041, p39:0.162, p12:1.547*, p36:1.341*`

Distractor candidate scores: `p22:1.023*, p29:0.507`

### content_01_aero_support / q14_three_hop / budget 128

- Category: `three_hop`
- F1: `0.857`
- Missing required units: `['start_time']`
- Selected ids: `['p06', 'p07', 'p08', 'p19']`
- Selected required alternatives: `['p19', 'p07', 'p06', 'p08']`
- Unselected required alternatives in candidate pool: `['p05', 'p28']`
- Selected distractors: `[]`
- Diagnosis: final-hop evidence scored too weakly or was crowded by loosely linked context.
- Next useful signal: `query-conditioned support score or path-completion score`

Required candidate scores: `p19:3.211*, p07:1.944*, p06:2.708*, p05:0.953, p08:1.864*, p28:-0.260`

Distractor candidate scores: `p33:1.215, p34:0.156, p17:-0.243`

### content_01_aero_support / q15_three_hop / budget 128

- Category: `three_hop`
- F1: `0.857`
- Missing required units: `['log']`
- Selected ids: `['p09', 'p10', 'p24', 'p38']`
- Selected required alternatives: `['p10', 'p24', 'p09']`
- Unselected required alternatives in candidate pool: `['p36', 'p11', 'p39']`
- Selected distractors: `[]`
- Diagnosis: final-hop evidence scored too weakly or was crowded by loosely linked context.
- Next useful signal: `query-conditioned support score or path-completion score`

Required candidate scores: `p10:2.794*, p24:1.546*, p09:2.275*, p36:1.439, p11:0.217, p39:0.439`

Distractor candidate scores: `p22:0.562, p29:-0.759`

### content_02_clinic_access / c_q01_direct / budget 128

- Category: `direct`
- F1: `0.000`
- Missing required units: `['student_access', 'annex_alias']`
- Selected ids: `['c04', 'c13', 'c16', 'c24']`
- Selected required alternatives: `[]`
- Unselected required alternatives in candidate pool: `['c01', 'c02']`
- Selected distractors: `['c04']`
- Diagnosis: wrong-context distractor outranked or co-selected with true evidence.
- Next useful signal: `support/contradiction verifier`

Required candidate scores: `c01:-0.594, c02:-1.032`

Distractor candidate scores: `c04:2.661*`

### content_02_clinic_access / c_q01_direct / budget 256

- Category: `direct`
- F1: `0.000`
- Missing required units: `['student_access', 'annex_alias']`
- Selected ids: `['c03', 'c04', 'c13', 'c15', 'c16', 'c24']`
- Selected required alternatives: `[]`
- Unselected required alternatives in candidate pool: `['c01', 'c02']`
- Selected distractors: `['c04']`
- Diagnosis: wrong-context distractor outranked or co-selected with true evidence.
- Next useful signal: `support/contradiction verifier`

Required candidate scores: `c01:-0.489, c02:-0.918`

Distractor candidate scores: `c04:2.783*`

### content_02_clinic_access / c_q01_direct / budget 512

- Category: `direct`
- F1: `0.000`
- Missing required units: `['student_access', 'annex_alias']`
- Selected ids: `['c03', 'c04', 'c13', 'c15', 'c16', 'c21', 'c24']`
- Selected required alternatives: `[]`
- Unselected required alternatives in candidate pool: `['c01', 'c02']`
- Selected distractors: `['c04']`
- Diagnosis: wrong-context distractor outranked or co-selected with true evidence.
- Next useful signal: `support/contradiction verifier`

Required candidate scores: `c01:-0.436, c02:-0.862`

Distractor candidate scores: `c04:2.843*`

### content_02_clinic_access / c_q01_direct / budget 1024

- Category: `direct`
- F1: `0.000`
- Missing required units: `['student_access', 'annex_alias']`
- Selected ids: `['c03', 'c04', 'c13', 'c15', 'c16', 'c21', 'c24']`
- Selected required alternatives: `[]`
- Unselected required alternatives in candidate pool: `['c01', 'c02']`
- Selected distractors: `['c04']`
- Diagnosis: wrong-context distractor outranked or co-selected with true evidence.
- Next useful signal: `support/contradiction verifier`

Required candidate scores: `c01:-0.409, c02:-0.833`

Distractor candidate scores: `c04:2.873*`

### content_02_clinic_access / c_q05_direct / budget 128

- Category: `direct`
- F1: `0.706`
- Missing required units: `['owner_location']`
- Selected ids: `['c17', 'c18', 'c20', 'c25']`
- Selected required alternatives: `['c17', 'c18']`
- Unselected required alternatives in candidate pool: `['c19']`
- Selected distractors: `[]`
- Diagnosis: final-hop evidence scored too weakly or was crowded by loosely linked context.
- Next useful signal: `query-conditioned support score or path-completion score`

Required candidate scores: `c17:2.223*, c18:2.014*, c19:0.307`

### content_02_clinic_access / c_q08_two_hop / budget 256

- Category: `two_hop`
- F1: `0.480`
- Missing required units: `['collector']`
- Selected ids: `['c01', 'c11', 'c12', 'c27', 'c29', 'c30', 'c32', 'c35']`
- Selected required alternatives: `['c29', 'c30']`
- Unselected required alternatives in candidate pool: `['c31']`
- Selected distractors: `[]`
- Diagnosis: final-hop evidence scored too weakly or was crowded by loosely linked context.
- Next useful signal: `query-conditioned support score or path-completion score`

Required candidate scores: `c29:2.761*, c30:1.615*, c31:0.547`

### content_02_clinic_access / c_q09_two_hop / budget 128

- Category: `two_hop`
- F1: `0.706`
- Missing required units: `['reviewer_location']`
- Selected ids: `['c33', 'c34', 'c36', 'c37']`
- Selected required alternatives: `['c33', 'c34']`
- Unselected required alternatives in candidate pool: `['c35']`
- Selected distractors: `[]`
- Diagnosis: final-hop evidence scored too weakly or was crowded by loosely linked context.
- Next useful signal: `query-conditioned support score or path-completion score`

Required candidate scores: `c33:3.040*, c34:0.628*, c35:-0.273`

### content_02_clinic_access / c_q13_three_hop / budget 128

- Category: `three_hop`
- F1: `0.706`
- Missing required units: `['office']`
- Selected ids: `['c33', 'c34', 'c36', 'c37']`
- Selected required alternatives: `['c33', 'c34']`
- Unselected required alternatives in candidate pool: `['c35']`
- Selected distractors: `[]`
- Diagnosis: final-hop evidence scored too weakly or was crowded by loosely linked context.
- Next useful signal: `query-conditioned support score or path-completion score`

Required candidate scores: `c33:3.709*, c34:0.583*, c35:-0.283`

## Decision For Task 3

The next knapsack upgrade should not be another broad weight sweep. The current sparse+dense similarity formula has reached the point where more tuning mostly trades F1 against complete-hit.

Recommended next upgrade: add a **query-conditioned support/verifier score** as a public inference-time feature.

Candidate implementation order:

1. Add an offline analysis script that scores `(query, chunk)` and `(query, selected_seed, candidate_chunk)` support with a cross-encoder or NLI-style model.
2. Compare support scores on the 14 failures before changing the selector.
3. If the signal separates true evidence from wrong-context distractors, add it to `FeatureWeights` and rerun all reports.
4. If it does not separate them, do not add it; move to dataset expansion before further model complexity.