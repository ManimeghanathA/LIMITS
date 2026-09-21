# Knapsack Question Inspection

## How To Read This Report

- `importance` is the public individual score used before pair/triple interactions.
- `individual`, `pair`, `triple`, and `redundancy` show why the selected subset won.
- Required, optional, and distractor flags are evaluation labels only; the selector does not receive them.
- Use failed cases to design public features, not to feed labels into inference.

## Improvement Ideas

- Estimate paragraph importance using query overlap plus connection to strong seed paragraphs.
- Reward pairwise paragraph links when one chunk explains or completes another chunk.
- Penalize extra chunks through a selection penalty so larger budgets do not force context bloat.
- Next likely improvement: contradiction/wrong-context detection for chunks containing words such as `not`, `superseded`, `wrong`, or mismatched locations/departments.

## Cases

### PASS content_01_aero_support / q01_direct / budget 128

Question: Where is the Atlas night support desk after the ventilation review?

Selected: `['p01', 'p16', 'p21', 'p35']`
Tokens: `121/128`
F1: `0.667` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `['p21', 'p35']`

Score breakdown:

- individual: `9.578`
- pair synergy: `2.923`
- triple synergy: `0.000`
- redundancy penalty: `1.128`
- total: `11.374`

Improvement hint: Add wrong-context or contradiction-aware features; a distractor beat required evidence.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `p01` | selected, required | 4.815 | 27 | The Atlas night support desk moved to Bay 7 after the January ventilation review. |
| `p21` | selected, distractor | 2.347 | 31 | A retired memo says the Atlas night desk moved to Bay 5, but that memo was withdrawn. |
| `p16` | selected, optional | 0.973 | 30 | Bay 4 still hosts the legacy simulator desk and gets misdirected support calls. |
| `p35` | selected, distractor | 1.443 | 33 | A facilities bulletin mentions Bay 7 catering deliveries unrelated to the night desk. |
| `p02` | - | -0.093 | 28 | Mira Patel is the duty lead who approves urgent avionics replacement requests for Atlas. |
| `p31` | - | 0.005 | 29 | The ground power team owns the battery health printout process for Atlas staging. |
| `p13` | optional | 0.509 | 31 | The old Bay 5 help-desk sign remains on a storage door near the simulator. |
| `p33` | - | -0.096 | 30 | Hangar 3 accepts overnight staging only for paint-shop air filters, not Atlas calibration carts. |
| `p28` | - | -0.196 | 29 | Ground power files Binder Blue after the battery cart is returned. |
| `p40` | - | -1.126 | 29 | Urgent replacement requests are marked red before they reach Mira Patel for approval. |
| `p07` | - | -0.968 | 27 | Hangar 2 staging requires the previous evening battery health printout. |
| `p08` | - | -1.005 | 28 | The previous evening battery health printout is filed in Binder Blue. |
| `p04` | - | -0.151 | 29 | Cage D opens only after the secure tool room records Mira Patel's approval code. |
| `p24` | - | -0.158 | 29 | Dev Rao signs the release sheet after the structural team entry appears. |
| `p03` | - | -1.003 | 27 | Approved urgent avionics replacements are stored in Cage D. |

### PASS content_01_aero_support / q01_direct / budget 256

Question: Where is the Atlas night support desk after the ventilation review?

Selected: `['p01', 'p13', 'p16', 'p21', 'p24', 'p28', 'p31', 'p35']`
Tokens: `239/256`
F1: `0.545` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `['p21', 'p35']`

Score breakdown:

- individual: `10.672`
- pair synergy: `9.085`
- triple synergy: `1.964`
- redundancy penalty: `2.253`
- total: `19.469`

Improvement hint: Add wrong-context or contradiction-aware features; a distractor beat required evidence.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `p01` | selected, required | 4.920 | 27 | The Atlas night support desk moved to Bay 7 after the January ventilation review. |
| `p21` | selected, distractor | 2.468 | 31 | A retired memo says the Atlas night desk moved to Bay 5, but that memo was withdrawn. |
| `p16` | selected, optional | 1.090 | 30 | Bay 4 still hosts the legacy simulator desk and gets misdirected support calls. |
| `p35` | selected, distractor | 1.572 | 33 | A facilities bulletin mentions Bay 7 catering deliveries unrelated to the night desk. |
| `p02` | - | 0.016 | 28 | Mira Patel is the duty lead who approves urgent avionics replacement requests for Atlas. |
| `p31` | selected | 0.119 | 29 | The ground power team owns the battery health printout process for Atlas staging. |
| `p13` | selected, optional | 0.630 | 31 | The old Bay 5 help-desk sign remains on a storage door near the simulator. |
| `p33` | - | 0.022 | 30 | Hangar 3 accepts overnight staging only for paint-shop air filters, not Atlas calibration carts. |
| `p28` | selected | -0.083 | 29 | Ground power files Binder Blue after the battery cart is returned. |
| `p40` | - | -1.013 | 29 | Urgent replacement requests are marked red before they reach Mira Patel for approval. |
| `p07` | - | -0.862 | 27 | Hangar 2 staging requires the previous evening battery health printout. |
| `p08` | - | -0.896 | 28 | The previous evening battery health printout is filed in Binder Blue. |
| `p04` | - | -0.038 | 29 | Cage D opens only after the secure tool room records Mira Patel's approval code. |
| `p24` | selected | -0.045 | 29 | Dev Rao signs the release sheet after the structural team entry appears. |
| `p14` | - | -0.572 | 32 | A parts summary mentions Mira Patel and Cage D but says she approves hydraulic seals. |

### PASS content_01_aero_support / q01_direct / budget 512

Question: Where is the Atlas night support desk after the ventilation review?

Selected: `['p01', 'p02', 'p04', 'p13', 'p14', 'p16', 'p21', 'p24', 'p28', 'p31', 'p33', 'p35']`
Tokens: `358/512`
F1: `0.400` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `['p21', 'p35']`

Score breakdown:

- individual: `10.799`
- pair synergy: `16.806`
- triple synergy: `6.429`
- redundancy penalty: `3.461`
- total: `30.573`

Improvement hint: Add wrong-context or contradiction-aware features; a distractor beat required evidence.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `p01` | selected, required | 4.973 | 27 | The Atlas night support desk moved to Bay 7 after the January ventilation review. |
| `p21` | selected, distractor | 2.528 | 31 | A retired memo says the Atlas night desk moved to Bay 5, but that memo was withdrawn. |
| `p16` | selected, optional | 1.149 | 30 | Bay 4 still hosts the legacy simulator desk and gets misdirected support calls. |
| `p35` | selected, distractor | 1.636 | 33 | A facilities bulletin mentions Bay 7 catering deliveries unrelated to the night desk. |
| `p02` | selected | 0.071 | 28 | Mira Patel is the duty lead who approves urgent avionics replacement requests for Atlas. |
| `p31` | selected | 0.175 | 29 | The ground power team owns the battery health printout process for Atlas staging. |
| `p13` | selected, optional | 0.691 | 31 | The old Bay 5 help-desk sign remains on a storage door near the simulator. |
| `p33` | selected | 0.080 | 30 | Hangar 3 accepts overnight staging only for paint-shop air filters, not Atlas calibration carts. |
| `p28` | selected | -0.027 | 29 | Ground power files Binder Blue after the battery cart is returned. |
| `p40` | - | -0.956 | 29 | Urgent replacement requests are marked red before they reach Mira Patel for approval. |
| `p07` | - | -0.809 | 27 | Hangar 2 staging requires the previous evening battery health printout. |
| `p08` | - | -0.841 | 28 | The previous evening battery health printout is filed in Binder Blue. |
| `p04` | selected | 0.019 | 29 | Cage D opens only after the secure tool room records Mira Patel's approval code. |
| `p24` | selected | 0.012 | 29 | Dev Rao signs the release sheet after the structural team entry appears. |
| `p14` | selected | -0.509 | 32 | A parts summary mentions Mira Patel and Cage D but says she approves hydraulic seals. |

### PASS content_01_aero_support / q01_direct / budget 1024

Question: Where is the Atlas night support desk after the ventilation review?

Selected: `['p01', 'p02', 'p04', 'p13', 'p14', 'p16', 'p21', 'p24', 'p28', 'p31', 'p33', 'p35']`
Tokens: `358/1024`
F1: `0.400` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `['p21', 'p35']`

Score breakdown:

- individual: `11.149`
- pair synergy: `16.806`
- triple synergy: `6.429`
- redundancy penalty: `3.461`
- total: `30.923`

Improvement hint: Add wrong-context or contradiction-aware features; a distractor beat required evidence.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `p01` | selected, required | 5.000 | 27 | The Atlas night support desk moved to Bay 7 after the January ventilation review. |
| `p21` | selected, distractor | 2.559 | 31 | A retired memo says the Atlas night desk moved to Bay 5, but that memo was withdrawn. |
| `p16` | selected, optional | 1.178 | 30 | Bay 4 still hosts the legacy simulator desk and gets misdirected support calls. |
| `p35` | selected, distractor | 1.669 | 33 | A facilities bulletin mentions Bay 7 catering deliveries unrelated to the night desk. |
| `p02` | selected | 0.098 | 28 | Mira Patel is the duty lead who approves urgent avionics replacement requests for Atlas. |
| `p31` | selected | 0.204 | 29 | The ground power team owns the battery health printout process for Atlas staging. |
| `p13` | selected, optional | 0.721 | 31 | The old Bay 5 help-desk sign remains on a storage door near the simulator. |
| `p33` | selected | 0.110 | 30 | Hangar 3 accepts overnight staging only for paint-shop air filters, not Atlas calibration carts. |
| `p28` | selected | 0.002 | 29 | Ground power files Binder Blue after the battery cart is returned. |
| `p40` | - | -0.928 | 29 | Urgent replacement requests are marked red before they reach Mira Patel for approval. |
| `p07` | - | -0.783 | 27 | Hangar 2 staging requires the previous evening battery health printout. |
| `p08` | - | -0.814 | 28 | The previous evening battery health printout is filed in Binder Blue. |
| `p04` | selected | 0.047 | 29 | Cage D opens only after the secure tool room records Mira Patel's approval code. |
| `p24` | selected | 0.040 | 29 | Dev Rao signs the release sheet after the structural team entry appears. |
| `p14` | selected | -0.478 | 32 | A parts summary mentions Mira Patel and Cage D but says she approves hydraulic seals. |

### PASS content_01_aero_support / q02_direct / budget 128

Question: Who approves urgent avionics replacement requests for Atlas?

Selected: `['p02', 'p03', 'p26', 'p40']`
Tokens: `115/128`
F1: `0.667` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `[]`

Score breakdown:

- individual: `12.602`
- pair synergy: `3.192`
- triple synergy: `0.000`
- redundancy penalty: `1.533`
- total: `14.261`

Improvement hint: Successful selection; inspect extra chunks only if precision or token cost becomes the priority.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `p02` | selected, required | 4.669 | 28 | Mira Patel is the duty lead who approves urgent avionics replacement requests for Atlas. |
| `p40` | selected, optional | 2.512 | 29 | Urgent replacement requests are marked red before they reach Mira Patel for approval. |
| `p03` | selected | 2.735 | 27 | Approved urgent avionics replacements are stored in Cage D. |
| `p26` | selected | 2.685 | 31 | A superseded training note says urgent avionics replacements are stored in Cage C. |
| `p01` | - | 0.009 | 27 | The Atlas night support desk moved to Bay 7 after the January ventilation review. |
| `p31` | - | 0.071 | 29 | The ground power team owns the battery health printout process for Atlas staging. |
| `p21` | - | -0.044 | 31 | A retired memo says the Atlas night desk moved to Bay 5, but that memo was withdrawn. |
| `p25` | - | 0.643 | 31 | Routine avionics labels are kept in the general parts cabinet, not the restricted cage. |
| `p14` | optional | 0.478 | 32 | A parts summary mentions Mira Patel and Cage D but says she approves hydraulic seals. |
| `p07` | - | -1.037 | 27 | Hangar 2 staging requires the previous evening battery health printout. |
| `p33` | - | -0.058 | 30 | Hangar 3 accepts overnight staging only for paint-shop air filters, not Atlas calibration carts. |
| `p23` | - | 0.268 | 30 | Torque kits are tracked by the secure tool room but are not stored in Cage D. |
| `p35` | - | -1.131 | 33 | A facilities bulletin mentions Bay 7 catering deliveries unrelated to the night desk. |
| `p08` | - | -1.074 | 28 | The previous evening battery health printout is filed in Binder Blue. |
| `p28` | - | -1.102 | 29 | Ground power files Binder Blue after the battery cart is returned. |

### PASS content_01_aero_support / q02_direct / budget 256

Question: Who approves urgent avionics replacement requests for Atlas?

Selected: `['p01', 'p02', 'p03', 'p14', 'p21', 'p25', 'p26', 'p40']`
Tokens: `236/256`
F1: `0.545` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `[]`

Score breakdown:

- individual: `14.608`
- pair synergy: `11.653`
- triple synergy: `3.542`
- redundancy penalty: `3.026`
- total: `26.777`

Improvement hint: Successful selection; inspect extra chunks only if precision or token cost becomes the priority.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `p02` | selected, required | 4.779 | 28 | Mira Patel is the duty lead who approves urgent avionics replacement requests for Atlas. |
| `p40` | selected, optional | 2.626 | 29 | Urgent replacement requests are marked red before they reach Mira Patel for approval. |
| `p03` | selected | 2.841 | 27 | Approved urgent avionics replacements are stored in Cage D. |
| `p26` | selected | 2.806 | 31 | A superseded training note says urgent avionics replacements are stored in Cage C. |
| `p01` | selected | 0.114 | 27 | The Atlas night support desk moved to Bay 7 after the January ventilation review. |
| `p31` | - | 0.184 | 29 | The ground power team owns the battery health printout process for Atlas staging. |
| `p21` | selected | 0.077 | 31 | A retired memo says the Atlas night desk moved to Bay 5, but that memo was withdrawn. |
| `p25` | selected | 0.764 | 31 | Routine avionics labels are kept in the general parts cabinet, not the restricted cage. |
| `p14` | selected, optional | 0.603 | 32 | A parts summary mentions Mira Patel and Cage D but says she approves hydraulic seals. |
| `p07` | - | -0.932 | 27 | Hangar 2 staging requires the previous evening battery health printout. |
| `p33` | - | 0.060 | 30 | Hangar 3 accepts overnight staging only for paint-shop air filters, not Atlas calibration carts. |
| `p23` | - | 0.385 | 30 | Torque kits are tracked by the secure tool room but are not stored in Cage D. |
| `p35` | - | -1.002 | 33 | A facilities bulletin mentions Bay 7 catering deliveries unrelated to the night desk. |
| `p08` | - | -0.965 | 28 | The previous evening battery health printout is filed in Binder Blue. |
| `p28` | - | -0.989 | 29 | Ground power files Binder Blue after the battery cart is returned. |

### PASS content_01_aero_support / q02_direct / budget 512

Question: Who approves urgent avionics replacement requests for Atlas?

Selected: `['p01', 'p02', 'p03', 'p14', 'p21', 'p23', 'p25', 'p26', 'p31', 'p33', 'p40']`
Tokens: `325/512`
F1: `0.429` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `[]`

Score breakdown:

- individual: `15.872`
- pair synergy: `17.782`
- triple synergy: `6.458`
- redundancy penalty: `4.201`
- total: `35.911`

Improvement hint: Successful selection; inspect extra chunks only if precision or token cost becomes the priority.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `p02` | selected, required | 4.833 | 28 | Mira Patel is the duty lead who approves urgent avionics replacement requests for Atlas. |
| `p40` | selected, optional | 2.682 | 29 | Urgent replacement requests are marked red before they reach Mira Patel for approval. |
| `p03` | selected | 2.894 | 27 | Approved urgent avionics replacements are stored in Cage D. |
| `p26` | selected | 2.866 | 31 | A superseded training note says urgent avionics replacements are stored in Cage C. |
| `p01` | selected | 0.167 | 27 | The Atlas night support desk moved to Bay 7 after the January ventilation review. |
| `p31` | selected | 0.241 | 29 | The ground power team owns the battery health printout process for Atlas staging. |
| `p21` | selected | 0.137 | 31 | A retired memo says the Atlas night desk moved to Bay 5, but that memo was withdrawn. |
| `p25` | selected | 0.824 | 31 | Routine avionics labels are kept in the general parts cabinet, not the restricted cage. |
| `p14` | selected, optional | 0.666 | 32 | A parts summary mentions Mira Patel and Cage D but says she approves hydraulic seals. |
| `p07` | - | -0.879 | 27 | Hangar 2 staging requires the previous evening battery health printout. |
| `p33` | selected | 0.118 | 30 | Hangar 3 accepts overnight staging only for paint-shop air filters, not Atlas calibration carts. |
| `p23` | selected | 0.443 | 30 | Torque kits are tracked by the secure tool room but are not stored in Cage D. |
| `p35` | - | -0.938 | 33 | A facilities bulletin mentions Bay 7 catering deliveries unrelated to the night desk. |
| `p08` | - | -0.910 | 28 | The previous evening battery health printout is filed in Binder Blue. |
| `p28` | - | -0.932 | 29 | Ground power files Binder Blue after the battery cart is returned. |

### PASS content_01_aero_support / q02_direct / budget 1024

Question: Who approves urgent avionics replacement requests for Atlas?

Selected: `['p01', 'p02', 'p03', 'p14', 'p21', 'p23', 'p25', 'p26', 'p31', 'p33', 'p40']`
Tokens: `325/1024`
F1: `0.429` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `[]`

Score breakdown:

- individual: `16.189`
- pair synergy: `17.782`
- triple synergy: `6.458`
- redundancy penalty: `4.201`
- total: `36.229`

Improvement hint: Successful selection; inspect extra chunks only if precision or token cost becomes the priority.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `p02` | selected, required | 4.861 | 28 | Mira Patel is the duty lead who approves urgent avionics replacement requests for Atlas. |
| `p40` | selected, optional | 2.711 | 29 | Urgent replacement requests are marked red before they reach Mira Patel for approval. |
| `p03` | selected | 2.920 | 27 | Approved urgent avionics replacements are stored in Cage D. |
| `p26` | selected | 2.897 | 31 | A superseded training note says urgent avionics replacements are stored in Cage C. |
| `p01` | selected | 0.193 | 27 | The Atlas night support desk moved to Bay 7 after the January ventilation review. |
| `p31` | selected | 0.269 | 29 | The ground power team owns the battery health printout process for Atlas staging. |
| `p21` | selected | 0.168 | 31 | A retired memo says the Atlas night desk moved to Bay 5, but that memo was withdrawn. |
| `p25` | selected | 0.855 | 31 | Routine avionics labels are kept in the general parts cabinet, not the restricted cage. |
| `p14` | selected, optional | 0.697 | 32 | A parts summary mentions Mira Patel and Cage D but says she approves hydraulic seals. |
| `p07` | - | -0.853 | 27 | Hangar 2 staging requires the previous evening battery health printout. |
| `p33` | selected | 0.147 | 30 | Hangar 3 accepts overnight staging only for paint-shop air filters, not Atlas calibration carts. |
| `p23` | selected | 0.473 | 30 | Torque kits are tracked by the secure tool room but are not stored in Cage D. |
| `p35` | - | -0.906 | 33 | A facilities bulletin mentions Bay 7 catering deliveries unrelated to the night desk. |
| `p08` | - | -0.883 | 28 | The previous evening battery health printout is filed in Binder Blue. |
| `p28` | - | -0.904 | 29 | Ground power files Binder Blue after the battery cart is returned. |

### PASS content_01_aero_support / q03_direct / budget 128

Question: When does winter calibration begin and where is the sensor cart staged?

Selected: `['p05', 'p06', 'p19', 'p32']`
Tokens: `116/128`
F1: `1.000` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `[]`

Score breakdown:

- individual: `9.432`
- pair synergy: `2.888`
- triple synergy: `0.000`
- redundancy penalty: `1.142`
- total: `11.178`

Improvement hint: Successful selection; inspect extra chunks only if precision or token cost becomes the priority.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `p06` | selected, required | 4.053 | 29 | The sensor cart must be staged beside Hangar 2 during winter calibration. |
| `p32` | selected, optional | 1.933 | 30 | The rollout coordinator checks that the sensor cart has arrived before calibration begins. |
| `p05` | selected, required | 1.283 | 28 | The winter calibration window begins at 06:30 before the first engine run. |
| `p19` | selected, required | 2.163 | 29 | Hangar 2 has limited power during winter calibration, so staging must be early. |
| `p18` | optional | 0.800 | 30 | The sensor cart carries tablet mounts and a red charging cable under its tray. |
| `p17` | distractor | 0.043 | 33 | A contractor guide lists 07:15 as a calibration start time, but it applies to Orion. |
| `p33` | distractor | 0.461 | 30 | Hangar 3 accepts overnight staging only for paint-shop air filters, not Atlas calibration carts. |
| `p30` | - | -0.140 | 28 | Dev Rao is not responsible for catering, hydraulic seal approval, or Orion calibration. |
| `p07` | - | 0.093 | 27 | Hangar 2 staging requires the previous evening battery health printout. |
| `p28` | - | -0.119 | 29 | Ground power files Binder Blue after the battery cart is returned. |
| `p31` | - | -0.434 | 29 | The ground power team owns the battery health printout process for Atlas staging. |
| `p34` | - | -0.574 | 31 | Binder Green contains fueling checklists and does not contain battery health printouts. |
| `p11` | - | -0.674 | 28 | Structural inspections must be logged in the amber maintenance ledger before release. |
| `p23` | - | -0.996 | 30 | Torque kits are tracked by the secure tool room but are not stored in Cage D. |
| `p37` | - | -0.770 | 31 | A clerk may shelve the amber ledger beside fuel records after Dev Rao reviews it. |

### PASS content_01_aero_support / q03_direct / budget 256

Question: When does winter calibration begin and where is the sensor cart staged?

Selected: `['p05', 'p06', 'p18', 'p19', 'p28', 'p32', 'p33', 'p34']`
Tokens: `236/256`
F1: `0.769` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `['p33']`

Score breakdown:

- individual: `10.921`
- pair synergy: `9.488`
- triple synergy: `1.429`
- redundancy penalty: `2.126`
- total: `19.711`

Improvement hint: Add wrong-context or contradiction-aware features; a distractor beat required evidence.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `p06` | selected, required | 4.166 | 29 | The sensor cart must be staged beside Hangar 2 during winter calibration. |
| `p32` | selected, optional | 2.050 | 30 | The rollout coordinator checks that the sensor cart has arrived before calibration begins. |
| `p05` | selected, required | 1.393 | 28 | The winter calibration window begins at 06:30 before the first engine run. |
| `p19` | selected, required | 2.276 | 29 | Hangar 2 has limited power during winter calibration, so staging must be early. |
| `p18` | selected, optional | 0.917 | 30 | The sensor cart carries tablet mounts and a red charging cable under its tray. |
| `p17` | distractor | 0.172 | 33 | A contractor guide lists 07:15 as a calibration start time, but it applies to Orion. |
| `p33` | selected, distractor | 0.578 | 30 | Hangar 3 accepts overnight staging only for paint-shop air filters, not Atlas calibration carts. |
| `p30` | - | -0.031 | 28 | Dev Rao is not responsible for catering, hydraulic seal approval, or Orion calibration. |
| `p07` | - | 0.199 | 27 | Hangar 2 staging requires the previous evening battery health printout. |
| `p28` | selected | -0.006 | 29 | Ground power files Binder Blue after the battery cart is returned. |
| `p31` | - | -0.320 | 29 | The ground power team owns the battery health printout process for Atlas staging. |
| `p34` | selected | -0.453 | 31 | Binder Green contains fueling checklists and does not contain battery health printouts. |
| `p11` | - | -0.565 | 28 | Structural inspections must be logged in the amber maintenance ledger before release. |
| `p23` | - | -0.879 | 30 | Torque kits are tracked by the secure tool room but are not stored in Cage D. |
| `p37` | - | -0.649 | 31 | A clerk may shelve the amber ledger beside fuel records after Dev Rao reviews it. |

### PASS content_01_aero_support / q03_direct / budget 512

Question: When does winter calibration begin and where is the sensor cart staged?

Selected: `['p05', 'p06', 'p07', 'p17', 'p18', 'p19', 'p28', 'p30', 'p31', 'p32', 'p33', 'p34']`
Tokens: `353/512`
F1: `0.588` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `['p17', 'p33']`

Score breakdown:

- individual: `11.629`
- pair synergy: `16.203`
- triple synergy: `2.143`
- redundancy penalty: `4.340`
- total: `25.635`

Improvement hint: Add wrong-context or contradiction-aware features; a distractor beat required evidence.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `p06` | selected, required | 4.223 | 29 | The sensor cart must be staged beside Hangar 2 during winter calibration. |
| `p32` | selected, optional | 2.109 | 30 | The rollout coordinator checks that the sensor cart has arrived before calibration begins. |
| `p05` | selected, required | 1.447 | 28 | The winter calibration window begins at 06:30 before the first engine run. |
| `p19` | selected, required | 2.333 | 29 | Hangar 2 has limited power during winter calibration, so staging must be early. |
| `p18` | selected, optional | 0.975 | 30 | The sensor cart carries tablet mounts and a red charging cable under its tray. |
| `p17` | selected, distractor | 0.236 | 33 | A contractor guide lists 07:15 as a calibration start time, but it applies to Orion. |
| `p33` | selected, distractor | 0.636 | 30 | Hangar 3 accepts overnight staging only for paint-shop air filters, not Atlas calibration carts. |
| `p30` | selected | 0.024 | 28 | Dev Rao is not responsible for catering, hydraulic seal approval, or Orion calibration. |
| `p07` | selected | 0.252 | 27 | Hangar 2 staging requires the previous evening battery health printout. |
| `p28` | selected | 0.051 | 29 | Ground power files Binder Blue after the battery cart is returned. |
| `p31` | selected | -0.264 | 29 | The ground power team owns the battery health printout process for Atlas staging. |
| `p34` | selected | -0.392 | 31 | Binder Green contains fueling checklists and does not contain battery health printouts. |
| `p11` | - | -0.510 | 28 | Structural inspections must be logged in the amber maintenance ledger before release. |
| `p23` | - | -0.821 | 30 | Torque kits are tracked by the secure tool room but are not stored in Cage D. |
| `p37` | - | -0.589 | 31 | A clerk may shelve the amber ledger beside fuel records after Dev Rao reviews it. |

### PASS content_01_aero_support / q03_direct / budget 1024

Question: When does winter calibration begin and where is the sensor cart staged?

Selected: `['p05', 'p06', 'p07', 'p17', 'p18', 'p19', 'p28', 'p30', 'p31', 'p32', 'p33', 'p34']`
Tokens: `353/1024`
F1: `0.588` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `['p17', 'p33']`

Score breakdown:

- individual: `11.974`
- pair synergy: `16.203`
- triple synergy: `2.143`
- redundancy penalty: `4.340`
- total: `25.979`

Improvement hint: Add wrong-context or contradiction-aware features; a distractor beat required evidence.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `p06` | selected, required | 4.251 | 29 | The sensor cart must be staged beside Hangar 2 during winter calibration. |
| `p32` | selected, optional | 2.138 | 30 | The rollout coordinator checks that the sensor cart has arrived before calibration begins. |
| `p05` | selected, required | 1.475 | 28 | The winter calibration window begins at 06:30 before the first engine run. |
| `p19` | selected, required | 2.361 | 29 | Hangar 2 has limited power during winter calibration, so staging must be early. |
| `p18` | selected, optional | 1.005 | 30 | The sensor cart carries tablet mounts and a red charging cable under its tray. |
| `p17` | selected, distractor | 0.268 | 33 | A contractor guide lists 07:15 as a calibration start time, but it applies to Orion. |
| `p33` | selected, distractor | 0.666 | 30 | Hangar 3 accepts overnight staging only for paint-shop air filters, not Atlas calibration carts. |
| `p30` | selected | 0.051 | 28 | Dev Rao is not responsible for catering, hydraulic seal approval, or Orion calibration. |
| `p07` | selected | 0.278 | 27 | Hangar 2 staging requires the previous evening battery health printout. |
| `p28` | selected | 0.079 | 29 | Ground power files Binder Blue after the battery cart is returned. |
| `p31` | selected | -0.235 | 29 | The ground power team owns the battery health printout process for Atlas staging. |
| `p34` | selected | -0.362 | 31 | Binder Green contains fueling checklists and does not contain battery health printouts. |
| `p11` | - | -0.483 | 28 | Structural inspections must be logged in the amber maintenance ledger before release. |
| `p23` | - | -0.791 | 30 | Torque kits are tracked by the secure tool room but are not stored in Cage D. |
| `p37` | - | -0.559 | 31 | A clerk may shelve the amber ledger beside fuel records after Dev Rao reviews it. |

### PASS content_01_aero_support / q04_direct / budget 128

Question: Which binder holds the previous evening battery health printout?

Selected: `['p07', 'p08', 'p31', 'p34']`
Tokens: `115/128`
F1: `0.857` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `[]`

Score breakdown:

- individual: `13.062`
- pair synergy: `3.486`
- triple synergy: `0.000`
- redundancy penalty: `1.448`
- total: `15.099`

Improvement hint: Successful selection; inspect extra chunks only if precision or token cost becomes the priority.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `p08` | selected, required | 4.721 | 28 | The previous evening battery health printout is filed in Binder Blue. |
| `p07` | selected | 4.018 | 27 | Hangar 2 staging requires the previous evening battery health printout. |
| `p31` | selected, optional | 2.231 | 29 | The ground power team owns the battery health printout process for Atlas staging. |
| `p34` | selected, optional | 2.092 | 31 | Binder Green contains fueling checklists and does not contain battery health printouts. |
| `p28` | required | 1.471 | 29 | Ground power files Binder Blue after the battery cart is returned. |
| `p20` | - | 0.072 | 30 | A spare binder shelf label near the fuel records cabinet also says amber. |
| `p19` | - | 0.064 | 29 | Hangar 2 has limited power during winter calibration, so staging must be early. |
| `p33` | - | -0.322 | 30 | Hangar 3 accepts overnight staging only for paint-shop air filters, not Atlas calibration carts. |
| `p06` | - | -0.341 | 29 | The sensor cart must be staged beside Hangar 2 during winter calibration. |
| `p37` | - | -0.991 | 31 | A clerk may shelve the amber ledger beside fuel records after Dev Rao reviews it. |
| `p01` | - | -0.707 | 27 | The Atlas night support desk moved to Bay 7 after the January ventilation review. |
| `p39` | - | -0.684 | 28 | Release paperwork is held until the amber ledger contains the structural inspection entry. |
| `p18` | - | -1.048 | 30 | The sensor cart carries tablet mounts and a red charging cable under its tray. |
| `p38` | - | -0.724 | 27 | The aft temperature warning should not be routed to the electrical corrosion queue. |
| `p29` | - | -0.725 | 32 | Cabin panel reviews are logged in the white trim notebook, not the amber ledger. |

### PASS content_01_aero_support / q04_direct / budget 256

Question: Which binder holds the previous evening battery health printout?

Selected: `['p07', 'p08', 'p19', 'p20', 'p28', 'p31', 'p33', 'p34']`
Tokens: `233/256`
F1: `0.667` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `[]`

Score breakdown:

- individual: `15.258`
- pair synergy: `8.238`
- triple synergy: `0.000`
- redundancy penalty: `3.026`
- total: `20.470`

Improvement hint: Successful selection; inspect extra chunks only if precision or token cost becomes the priority.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `p08` | selected, required | 4.830 | 28 | The previous evening battery health printout is filed in Binder Blue. |
| `p07` | selected | 4.123 | 27 | Hangar 2 staging requires the previous evening battery health printout. |
| `p31` | selected, optional | 2.344 | 29 | The ground power team owns the battery health printout process for Atlas staging. |
| `p34` | selected, optional | 2.213 | 31 | Binder Green contains fueling checklists and does not contain battery health printouts. |
| `p28` | selected, required | 1.585 | 29 | Ground power files Binder Blue after the battery cart is returned. |
| `p20` | selected | 0.189 | 30 | A spare binder shelf label near the fuel records cabinet also says amber. |
| `p19` | selected | 0.177 | 29 | Hangar 2 has limited power during winter calibration, so staging must be early. |
| `p33` | selected | -0.204 | 30 | Hangar 3 accepts overnight staging only for paint-shop air filters, not Atlas calibration carts. |
| `p06` | - | -0.228 | 29 | The sensor cart must be staged beside Hangar 2 during winter calibration. |
| `p37` | - | -0.869 | 31 | A clerk may shelve the amber ledger beside fuel records after Dev Rao reviews it. |
| `p01` | - | -0.601 | 27 | The Atlas night support desk moved to Bay 7 after the January ventilation review. |
| `p18` | - | -0.931 | 30 | The sensor cart carries tablet mounts and a red charging cable under its tray. |
| `p39` | - | -0.575 | 28 | Release paperwork is held until the amber ledger contains the structural inspection entry. |
| `p29` | - | -0.600 | 32 | Cabin panel reviews are logged in the white trim notebook, not the amber ledger. |
| `p32` | - | -0.949 | 30 | The rollout coordinator checks that the sensor cart has arrived before calibration begins. |

### PASS content_01_aero_support / q04_direct / budget 512

Question: Which binder holds the previous evening battery health printout?

Selected: `['p06', 'p07', 'p08', 'p19', 'p20', 'p28', 'p31', 'p33', 'p34']`
Tokens: `262/512`
F1: `0.615` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `[]`

Score breakdown:

- individual: `15.542`
- pair synergy: `9.711`
- triple synergy: `0.000`
- redundancy penalty: `3.745`
- total: `21.508`

Improvement hint: Successful selection; inspect extra chunks only if precision or token cost becomes the priority.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `p08` | selected, required | 4.885 | 28 | The previous evening battery health printout is filed in Binder Blue. |
| `p07` | selected | 4.176 | 27 | Hangar 2 staging requires the previous evening battery health printout. |
| `p31` | selected, optional | 2.401 | 29 | The ground power team owns the battery health printout process for Atlas staging. |
| `p34` | selected, optional | 2.274 | 31 | Binder Green contains fueling checklists and does not contain battery health printouts. |
| `p28` | selected, required | 1.641 | 29 | Ground power files Binder Blue after the battery cart is returned. |
| `p20` | selected | 0.248 | 30 | A spare binder shelf label near the fuel records cabinet also says amber. |
| `p19` | selected | 0.234 | 29 | Hangar 2 has limited power during winter calibration, so staging must be early. |
| `p33` | selected | -0.146 | 30 | Hangar 3 accepts overnight staging only for paint-shop air filters, not Atlas calibration carts. |
| `p06` | selected | -0.171 | 29 | The sensor cart must be staged beside Hangar 2 during winter calibration. |
| `p37` | - | -0.809 | 31 | A clerk may shelve the amber ledger beside fuel records after Dev Rao reviews it. |
| `p18` | - | -0.872 | 30 | The sensor cart carries tablet mounts and a red charging cable under its tray. |
| `p01` | - | -0.548 | 27 | The Atlas night support desk moved to Bay 7 after the January ventilation review. |
| `p39` | - | -0.520 | 28 | Release paperwork is held until the amber ledger contains the structural inspection entry. |
| `p29` | - | -0.538 | 32 | Cabin panel reviews are logged in the white trim notebook, not the amber ledger. |
| `p32` | - | -0.890 | 30 | The rollout coordinator checks that the sensor cart has arrived before calibration begins. |

### PASS content_01_aero_support / q04_direct / budget 1024

Question: Which binder holds the previous evening battery health printout?

Selected: `['p06', 'p07', 'p08', 'p19', 'p20', 'p28', 'p31', 'p33', 'p34']`
Tokens: `262/1024`
F1: `0.615` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `[]`

Score breakdown:

- individual: `15.798`
- pair synergy: `9.711`
- triple synergy: `0.000`
- redundancy penalty: `3.745`
- total: `21.764`

Improvement hint: Successful selection; inspect extra chunks only if precision or token cost becomes the priority.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `p08` | selected, required | 4.912 | 28 | The previous evening battery health printout is filed in Binder Blue. |
| `p07` | selected | 4.203 | 27 | Hangar 2 staging requires the previous evening battery health printout. |
| `p31` | selected, optional | 2.429 | 29 | The ground power team owns the battery health printout process for Atlas staging. |
| `p34` | selected, optional | 2.304 | 31 | Binder Green contains fueling checklists and does not contain battery health printouts. |
| `p28` | selected, required | 1.670 | 29 | Ground power files Binder Blue after the battery cart is returned. |
| `p20` | selected | 0.277 | 30 | A spare binder shelf label near the fuel records cabinet also says amber. |
| `p19` | selected | 0.262 | 29 | Hangar 2 has limited power during winter calibration, so staging must be early. |
| `p33` | selected | -0.116 | 30 | Hangar 3 accepts overnight staging only for paint-shop air filters, not Atlas calibration carts. |
| `p06` | selected | -0.143 | 29 | The sensor cart must be staged beside Hangar 2 during winter calibration. |
| `p37` | - | -0.779 | 31 | A clerk may shelve the amber ledger beside fuel records after Dev Rao reviews it. |
| `p18` | - | -0.843 | 30 | The sensor cart carries tablet mounts and a red charging cable under its tray. |
| `p01` | - | -0.522 | 27 | The Atlas night support desk moved to Bay 7 after the January ventilation review. |
| `p39` | - | -0.493 | 28 | Release paperwork is held until the amber ledger contains the structural inspection entry. |
| `p29` | - | -0.506 | 32 | Cabin panel reviews are logged in the white trim notebook, not the amber ledger. |
| `p32` | - | -0.861 | 30 | The rollout coordinator checks that the sensor cart has arrived before calibration begins. |

### PASS content_01_aero_support / q05_direct / budget 128

Question: Who reviews the amber maintenance ledger?

Selected: `['p11', 'p12', 'p29', 'p37']`
Tokens: `118/128`
F1: `0.667` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `[]`

Score breakdown:

- individual: `14.636`
- pair synergy: `3.900`
- triple synergy: `0.000`
- redundancy penalty: `1.348`
- total: `17.188`

Improvement hint: Successful selection; inspect extra chunks only if precision or token cost becomes the priority.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `p12` | selected, required | 4.794 | 27 | Shift controller Dev Rao reviews the amber maintenance ledger. |
| `p11` | selected | 3.035 | 28 | Structural inspections must be logged in the amber maintenance ledger before release. |
| `p37` | selected, optional | 3.812 | 31 | A clerk may shelve the amber ledger beside fuel records after Dev Rao reviews it. |
| `p29` | selected | 2.995 | 32 | Cabin panel reviews are logged in the white trim notebook, not the amber ledger. |
| `p39` | - | 2.417 | 28 | Release paperwork is held until the amber ledger contains the structural inspection entry. |
| `p20` | distractor | 0.892 | 30 | A spare binder shelf label near the fuel records cabinet also says amber. |
| `p22` | - | 0.407 | 30 | The electrical team reviews right-harness corrosion alerts, not left-harness insulation rubs. |
| `p24` | required | -0.121 | 29 | Dev Rao signs the release sheet after the structural team entry appears. |
| `p30` | optional | -0.326 | 28 | Dev Rao is not responsible for catering, hydraulic seal approval, or Orion calibration. |
| `p10` | - | -0.735 | 29 | When the aft temperature warning appears, left harness inspection is assigned to structural. |
| `p04` | - | -0.611 | 29 | Cage D opens only after the secure tool room records Mira Patel's approval code. |
| `p27` | - | -0.668 | 27 | The secure tool room records approval codes for restricted cages. |
| `p32` | - | -0.693 | 30 | The rollout coordinator checks that the sensor cart has arrived before calibration begins. |
| `p40` | - | -0.705 | 29 | Urgent replacement requests are marked red before they reach Mira Patel for approval. |
| `p34` | - | -0.713 | 31 | Binder Green contains fueling checklists and does not contain battery health printouts. |

### PASS content_01_aero_support / q05_direct / budget 256

Question: Who reviews the amber maintenance ledger?

Selected: `['p11', 'p12', 'p20', 'p22', 'p24', 'p29', 'p37', 'p39']`
Tokens: `235/256`
F1: `0.545` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `['p20']`

Score breakdown:

- individual: `19.149`
- pair synergy: `9.809`
- triple synergy: `0.000`
- redundancy penalty: `3.452`
- total: `25.505`

Improvement hint: Add wrong-context or contradiction-aware features; a distractor beat required evidence.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `p12` | selected, required | 4.899 | 27 | Shift controller Dev Rao reviews the amber maintenance ledger. |
| `p11` | selected | 3.144 | 28 | Structural inspections must be logged in the amber maintenance ledger before release. |
| `p37` | selected, optional | 3.933 | 31 | A clerk may shelve the amber ledger beside fuel records after Dev Rao reviews it. |
| `p29` | selected | 3.120 | 32 | Cabin panel reviews are logged in the white trim notebook, not the amber ledger. |
| `p39` | selected | 2.526 | 28 | Release paperwork is held until the amber ledger contains the structural inspection entry. |
| `p20` | selected, distractor | 1.009 | 30 | A spare binder shelf label near the fuel records cabinet also says amber. |
| `p22` | selected | 0.524 | 30 | The electrical team reviews right-harness corrosion alerts, not left-harness insulation rubs. |
| `p24` | selected, required | -0.008 | 29 | Dev Rao signs the release sheet after the structural team entry appears. |
| `p30` | optional | -0.217 | 28 | Dev Rao is not responsible for catering, hydraulic seal approval, or Orion calibration. |
| `p10` | - | -0.621 | 29 | When the aft temperature warning appears, left harness inspection is assigned to structural. |
| `p04` | - | -0.498 | 29 | Cage D opens only after the secure tool room records Mira Patel's approval code. |
| `p27` | - | -0.563 | 27 | The secure tool room records approval codes for restricted cages. |
| `p32` | - | -0.576 | 30 | The rollout coordinator checks that the sensor cart has arrived before calibration begins. |
| `p40` | - | -0.592 | 29 | Urgent replacement requests are marked red before they reach Mira Patel for approval. |
| `p34` | - | -0.592 | 31 | Binder Green contains fueling checklists and does not contain battery health printouts. |

### PASS content_01_aero_support / q05_direct / budget 512

Question: Who reviews the amber maintenance ledger?

Selected: `['p04', 'p11', 'p12', 'p20', 'p22', 'p24', 'p27', 'p29', 'p30', 'p37', 'p39']`
Tokens: `319/512`
F1: `0.533` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `['p20']`

Score breakdown:

- individual: `18.494`
- pair synergy: `12.808`
- triple synergy: `0.000`
- redundancy penalty: `4.703`
- total: `26.600`

Improvement hint: Add wrong-context or contradiction-aware features; a distractor beat required evidence.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `p12` | selected, required | 4.952 | 27 | Shift controller Dev Rao reviews the amber maintenance ledger. |
| `p11` | selected | 3.199 | 28 | Structural inspections must be logged in the amber maintenance ledger before release. |
| `p37` | selected, optional | 3.994 | 31 | A clerk may shelve the amber ledger beside fuel records after Dev Rao reviews it. |
| `p29` | selected | 3.183 | 32 | Cabin panel reviews are logged in the white trim notebook, not the amber ledger. |
| `p39` | selected | 2.581 | 28 | Release paperwork is held until the amber ledger contains the structural inspection entry. |
| `p20` | selected, distractor | 1.067 | 30 | A spare binder shelf label near the fuel records cabinet also says amber. |
| `p22` | selected | 0.583 | 30 | The electrical team reviews right-harness corrosion alerts, not left-harness insulation rubs. |
| `p24` | selected, required | 0.049 | 29 | Dev Rao signs the release sheet after the structural team entry appears. |
| `p30` | selected, optional | -0.162 | 28 | Dev Rao is not responsible for catering, hydraulic seal approval, or Orion calibration. |
| `p10` | - | -0.565 | 29 | When the aft temperature warning appears, left harness inspection is assigned to structural. |
| `p04` | selected | -0.441 | 29 | Cage D opens only after the secure tool room records Mira Patel's approval code. |
| `p27` | selected | -0.510 | 27 | The secure tool room records approval codes for restricted cages. |
| `p32` | - | -0.517 | 30 | The rollout coordinator checks that the sensor cart has arrived before calibration begins. |
| `p34` | - | -0.532 | 31 | Binder Green contains fueling checklists and does not contain battery health printouts. |
| `p40` | - | -0.535 | 29 | Urgent replacement requests are marked red before they reach Mira Patel for approval. |

### PASS content_01_aero_support / q05_direct / budget 1024

Question: Who reviews the amber maintenance ledger?

Selected: `['p04', 'p10', 'p11', 'p12', 'p20', 'p22', 'p24', 'p27', 'p29', 'p30', 'p37', 'p39']`
Tokens: `348/1024`
F1: `0.500` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `['p20']`

Score breakdown:

- individual: `18.269`
- pair synergy: `13.820`
- triple synergy: `0.000`
- redundancy penalty: `5.159`
- total: `26.930`

Improvement hint: Add wrong-context or contradiction-aware features; a distractor beat required evidence.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `p12` | selected, required | 4.978 | 27 | Shift controller Dev Rao reviews the amber maintenance ledger. |
| `p11` | selected | 3.227 | 28 | Structural inspections must be logged in the amber maintenance ledger before release. |
| `p37` | selected, optional | 4.024 | 31 | A clerk may shelve the amber ledger beside fuel records after Dev Rao reviews it. |
| `p29` | selected | 3.214 | 32 | Cabin panel reviews are logged in the white trim notebook, not the amber ledger. |
| `p39` | selected | 2.609 | 28 | Release paperwork is held until the amber ledger contains the structural inspection entry. |
| `p20` | selected, distractor | 1.097 | 30 | A spare binder shelf label near the fuel records cabinet also says amber. |
| `p22` | selected | 0.612 | 30 | The electrical team reviews right-harness corrosion alerts, not left-harness insulation rubs. |
| `p24` | selected, required | 0.077 | 29 | Dev Rao signs the release sheet after the structural team entry appears. |
| `p30` | selected, optional | -0.135 | 28 | Dev Rao is not responsible for catering, hydraulic seal approval, or Orion calibration. |
| `p10` | selected | -0.536 | 29 | When the aft temperature warning appears, left harness inspection is assigned to structural. |
| `p04` | selected | -0.413 | 29 | Cage D opens only after the secure tool room records Mira Patel's approval code. |
| `p27` | selected | -0.484 | 27 | The secure tool room records approval codes for restricted cages. |
| `p32` | - | -0.488 | 30 | The rollout coordinator checks that the sensor cart has arrived before calibration begins. |
| `p34` | - | -0.501 | 31 | Binder Green contains fueling checklists and does not contain battery health printouts. |
| `p40` | - | -0.507 | 29 | Urgent replacement requests are marked red before they reach Mira Patel for approval. |

### PASS content_01_aero_support / q06_two_hop / budget 128

Question: Where are urgent avionics replacements approved by Mira Patel stored?

Selected: `['p02', 'p03', 'p26', 'p40']`
Tokens: `115/128`
F1: `0.857` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `['p26']`

Score breakdown:

- individual: `13.660`
- pair synergy: `4.811`
- triple synergy: `0.000`
- redundancy penalty: `1.533`
- total: `16.938`

Improvement hint: Add wrong-context or contradiction-aware features; a distractor beat required evidence.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `p03` | selected, required | 4.393 | 27 | Approved urgent avionics replacements are stored in Cage D. |
| `p02` | selected, required | 3.061 | 28 | Mira Patel is the duty lead who approves urgent avionics replacement requests for Atlas. |
| `p26` | selected, distractor | 3.771 | 31 | A superseded training note says urgent avionics replacements are stored in Cage C. |
| `p40` | selected, optional | 2.435 | 29 | Urgent replacement requests are marked red before they reach Mira Patel for approval. |
| `p04` | - | 1.062 | 29 | Cage D opens only after the secure tool room records Mira Patel's approval code. |
| `p14` | distractor | 1.129 | 32 | A parts summary mentions Mira Patel and Cage D but says she approves hydraulic seals. |
| `p27` | - | -0.550 | 27 | The secure tool room records approval codes for restricted cages. |
| `p23` | - | 0.900 | 30 | Torque kits are tracked by the secure tool room but are not stored in Cage D. |
| `p25` | optional | 0.584 | 31 | Routine avionics labels are kept in the general parts cabinet, not the restricted cage. |
| `p37` | - | -1.044 | 31 | A clerk may shelve the amber ledger beside fuel records after Dev Rao reviews it. |
| `p36` | - | -0.559 | 30 | A duplicate aft-warning note says cold starts can make insulation rub the left harness. |
| `p21` | - | -0.773 | 31 | A retired memo says the Atlas night desk moved to Bay 5, but that memo was withdrawn. |
| `p11` | - | -0.680 | 28 | Structural inspections must be logged in the amber maintenance ledger before release. |
| `p31` | - | -0.696 | 29 | The ground power team owns the battery health printout process for Atlas staging. |
| `p28` | - | -1.036 | 29 | Ground power files Binder Blue after the battery cart is returned. |

### PASS content_01_aero_support / q06_two_hop / budget 256

Question: Where are urgent avionics replacements approved by Mira Patel stored?

Selected: `['p02', 'p03', 'p04', 'p14', 'p23', 'p25', 'p26', 'p40']`
Tokens: `237/256`
F1: `0.667` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `['p14', 'p26']`

Score breakdown:

- individual: `18.260`
- pair synergy: `15.331`
- triple synergy: `0.536`
- redundancy penalty: `4.049`
- total: `30.077`

Improvement hint: Add wrong-context or contradiction-aware features; a distractor beat required evidence.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `p03` | selected, required | 4.499 | 27 | Approved urgent avionics replacements are stored in Cage D. |
| `p02` | selected, required | 3.170 | 28 | Mira Patel is the duty lead who approves urgent avionics replacement requests for Atlas. |
| `p26` | selected, distractor | 3.892 | 31 | A superseded training note says urgent avionics replacements are stored in Cage C. |
| `p40` | selected, optional | 2.548 | 29 | Urgent replacement requests are marked red before they reach Mira Patel for approval. |
| `p04` | selected | 1.175 | 29 | Cage D opens only after the secure tool room records Mira Patel's approval code. |
| `p14` | selected, distractor | 1.254 | 32 | A parts summary mentions Mira Patel and Cage D but says she approves hydraulic seals. |
| `p27` | - | -0.444 | 27 | The secure tool room records approval codes for restricted cages. |
| `p23` | selected | 1.018 | 30 | Torque kits are tracked by the secure tool room but are not stored in Cage D. |
| `p25` | selected, optional | 0.705 | 31 | Routine avionics labels are kept in the general parts cabinet, not the restricted cage. |
| `p37` | - | -0.923 | 31 | A clerk may shelve the amber ledger beside fuel records after Dev Rao reviews it. |
| `p36` | - | -0.442 | 30 | A duplicate aft-warning note says cold starts can make insulation rub the left harness. |
| `p21` | - | -0.652 | 31 | A retired memo says the Atlas night desk moved to Bay 5, but that memo was withdrawn. |
| `p11` | - | -0.571 | 28 | Structural inspections must be logged in the amber maintenance ledger before release. |
| `p31` | - | -0.583 | 29 | The ground power team owns the battery health printout process for Atlas staging. |
| `p28` | - | -0.922 | 29 | Ground power files Binder Blue after the battery cart is returned. |

### PASS content_01_aero_support / q06_two_hop / budget 512

Question: Where are urgent avionics replacements approved by Mira Patel stored?

Selected: `['p02', 'p03', 'p04', 'p14', 'p23', 'p25', 'p26', 'p27', 'p40']`
Tokens: `264/512`
F1: `0.615` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `['p14', 'p26']`

Score breakdown:

- individual: `18.331`
- pair synergy: `16.956`
- triple synergy: `0.536`
- redundancy penalty: `4.719`
- total: `31.103`

Improvement hint: Add wrong-context or contradiction-aware features; a distractor beat required evidence.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `p03` | selected, required | 4.551 | 27 | Approved urgent avionics replacements are stored in Cage D. |
| `p02` | selected, required | 3.225 | 28 | Mira Patel is the duty lead who approves urgent avionics replacement requests for Atlas. |
| `p26` | selected, distractor | 3.953 | 31 | A superseded training note says urgent avionics replacements are stored in Cage C. |
| `p40` | selected, optional | 2.605 | 29 | Urgent replacement requests are marked red before they reach Mira Patel for approval. |
| `p04` | selected | 1.231 | 29 | Cage D opens only after the secure tool room records Mira Patel's approval code. |
| `p14` | selected, distractor | 1.316 | 32 | A parts summary mentions Mira Patel and Cage D but says she approves hydraulic seals. |
| `p27` | selected | -0.392 | 27 | The secure tool room records approval codes for restricted cages. |
| `p23` | selected | 1.076 | 30 | Torque kits are tracked by the secure tool room but are not stored in Cage D. |
| `p25` | selected, optional | 0.765 | 31 | Routine avionics labels are kept in the general parts cabinet, not the restricted cage. |
| `p37` | - | -0.862 | 31 | A clerk may shelve the amber ledger beside fuel records after Dev Rao reviews it. |
| `p36` | - | -0.383 | 30 | A duplicate aft-warning note says cold starts can make insulation rub the left harness. |
| `p21` | - | -0.591 | 31 | A retired memo says the Atlas night desk moved to Bay 5, but that memo was withdrawn. |
| `p11` | - | -0.516 | 28 | Structural inspections must be logged in the amber maintenance ledger before release. |
| `p31` | - | -0.526 | 29 | The ground power team owns the battery health printout process for Atlas staging. |
| `p28` | - | -0.866 | 29 | Ground power files Binder Blue after the battery cart is returned. |

### PASS content_01_aero_support / q06_two_hop / budget 1024

Question: Where are urgent avionics replacements approved by Mira Patel stored?

Selected: `['p02', 'p03', 'p04', 'p14', 'p23', 'p25', 'p26', 'p27', 'p40']`
Tokens: `264/1024`
F1: `0.615` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `['p14', 'p26']`

Score breakdown:

- individual: `18.589`
- pair synergy: `16.956`
- triple synergy: `0.536`
- redundancy penalty: `4.719`
- total: `31.361`

Improvement hint: Add wrong-context or contradiction-aware features; a distractor beat required evidence.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `p03` | selected, required | 4.578 | 27 | Approved urgent avionics replacements are stored in Cage D. |
| `p02` | selected, required | 3.252 | 28 | Mira Patel is the duty lead who approves urgent avionics replacement requests for Atlas. |
| `p26` | selected, distractor | 3.983 | 31 | A superseded training note says urgent avionics replacements are stored in Cage C. |
| `p40` | selected, optional | 2.633 | 29 | Urgent replacement requests are marked red before they reach Mira Patel for approval. |
| `p04` | selected | 1.260 | 29 | Cage D opens only after the secure tool room records Mira Patel's approval code. |
| `p14` | selected, distractor | 1.347 | 32 | A parts summary mentions Mira Patel and Cage D but says she approves hydraulic seals. |
| `p27` | selected | -0.365 | 27 | The secure tool room records approval codes for restricted cages. |
| `p23` | selected | 1.106 | 30 | Torque kits are tracked by the secure tool room but are not stored in Cage D. |
| `p25` | selected, optional | 0.796 | 31 | Routine avionics labels are kept in the general parts cabinet, not the restricted cage. |
| `p37` | - | -0.832 | 31 | A clerk may shelve the amber ledger beside fuel records after Dev Rao reviews it. |
| `p36` | - | -0.354 | 30 | A duplicate aft-warning note says cold starts can make insulation rub the left harness. |
| `p21` | - | -0.561 | 31 | A retired memo says the Atlas night desk moved to Bay 5, but that memo was withdrawn. |
| `p11` | - | -0.489 | 28 | Structural inspections must be logged in the amber maintenance ledger before release. |
| `p31` | - | -0.498 | 29 | The ground power team owns the battery health printout process for Atlas staging. |
| `p28` | - | -0.837 | 29 | Ground power files Binder Blue after the battery cart is returned. |

### FAIL content_01_aero_support / q07_two_hop / budget 128

Question: What must happen before Cage D can be opened for an urgent avionics replacement?

Selected: `['p02', 'p03', 'p26', 'p40']`
Tokens: `115/128`
F1: `0.706` Required recall: `0.667`
Missing required units: `['open_condition']`
Selected distractors: `['p26']`

Score breakdown:

- individual: `10.050`
- pair synergy: `3.926`
- triple synergy: `0.000`
- redundancy penalty: `1.533`
- total: `12.443`

Improvement hint: Add wrong-context or contradiction-aware features; a distractor beat required evidence.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `p03` | selected, required | 3.411 | 27 | Approved urgent avionics replacements are stored in Cage D. |
| `p02` | selected, required | 1.924 | 28 | Mira Patel is the duty lead who approves urgent avionics replacement requests for Atlas. |
| `p40` | selected, optional | 1.856 | 29 | Urgent replacement requests are marked red before they reach Mira Patel for approval. |
| `p26` | selected, distractor | 2.858 | 31 | A superseded training note says urgent avionics replacements are stored in Cage C. |
| `p11` | - | 0.176 | 28 | Structural inspections must be logged in the amber maintenance ledger before release. |
| `p04` | required | 0.928 | 29 | Cage D opens only after the secure tool room records Mira Patel's approval code. |
| `p25` | - | 0.973 | 31 | Routine avionics labels are kept in the general parts cabinet, not the restricted cage. |
| `p23` | optional | 1.309 | 30 | Torque kits are tracked by the secure tool room but are not stored in Cage D. |
| `p27` | required | -0.498 | 27 | The secure tool room records approval codes for restricted cages. |
| `p14` | - | 0.816 | 32 | A parts summary mentions Mira Patel and Cage D but says she approves hydraulic seals. |
| `p39` | - | -1.014 | 28 | Release paperwork is held until the amber ledger contains the structural inspection entry. |
| `p15` | - | -1.128 | 29 | The general parts cabinet contains fasteners, cable labels, and cleaning cloths. |
| `p12` | - | -1.107 | 27 | Shift controller Dev Rao reviews the amber maintenance ledger. |
| `p29` | - | -1.150 | 32 | Cabin panel reviews are logged in the white trim notebook, not the amber ledger. |
| `p36` | - | -0.088 | 30 | A duplicate aft-warning note says cold starts can make insulation rub the left harness. |

### PASS content_01_aero_support / q07_two_hop / budget 256

Question: What must happen before Cage D can be opened for an urgent avionics replacement?

Selected: `['p02', 'p03', 'p04', 'p11', 'p14', 'p23', 'p26', 'p40']`
Tokens: `234/256`
F1: `0.769` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `['p26']`

Score breakdown:

- individual: `14.194`
- pair synergy: `14.207`
- triple synergy: `2.750`
- redundancy penalty: `3.499`
- total: `27.651`

Improvement hint: Add wrong-context or contradiction-aware features; a distractor beat required evidence.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `p03` | selected, required | 3.517 | 27 | Approved urgent avionics replacements are stored in Cage D. |
| `p02` | selected, required | 2.034 | 28 | Mira Patel is the duty lead who approves urgent avionics replacement requests for Atlas. |
| `p40` | selected, optional | 1.970 | 29 | Urgent replacement requests are marked red before they reach Mira Patel for approval. |
| `p26` | selected, distractor | 2.979 | 31 | A superseded training note says urgent avionics replacements are stored in Cage C. |
| `p11` | selected | 0.286 | 28 | Structural inspections must be logged in the amber maintenance ledger before release. |
| `p04` | selected, required | 1.041 | 29 | Cage D opens only after the secure tool room records Mira Patel's approval code. |
| `p25` | - | 1.094 | 31 | Routine avionics labels are kept in the general parts cabinet, not the restricted cage. |
| `p23` | selected, optional | 1.427 | 30 | Torque kits are tracked by the secure tool room but are not stored in Cage D. |
| `p27` | required | -0.393 | 27 | The secure tool room records approval codes for restricted cages. |
| `p14` | selected | 0.941 | 32 | A parts summary mentions Mira Patel and Cage D but says she approves hydraulic seals. |
| `p39` | - | -0.905 | 28 | Release paperwork is held until the amber ledger contains the structural inspection entry. |
| `p15` | - | -1.015 | 29 | The general parts cabinet contains fasteners, cable labels, and cleaning cloths. |
| `p12` | - | -1.001 | 27 | Shift controller Dev Rao reviews the amber maintenance ledger. |
| `p29` | - | -1.025 | 32 | Cabin panel reviews are logged in the white trim notebook, not the amber ledger. |
| `p36` | - | 0.029 | 30 | A duplicate aft-warning note says cold starts can make insulation rub the left harness. |

### PASS content_01_aero_support / q07_two_hop / budget 512

Question: What must happen before Cage D can be opened for an urgent avionics replacement?

Selected: `['p02', 'p03', 'p04', 'p11', 'p14', 'p23', 'p25', 'p26', 'p27', 'p36', 'p40']`
Tokens: `322/512`
F1: `0.706` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `['p26']`

Score breakdown:

- individual: `15.554`
- pair synergy: `21.003`
- triple synergy: `7.125`
- redundancy penalty: `4.931`
- total: `38.751`

Improvement hint: Add wrong-context or contradiction-aware features; a distractor beat required evidence.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `p03` | selected, required | 3.570 | 27 | Approved urgent avionics replacements are stored in Cage D. |
| `p02` | selected, required | 2.088 | 28 | Mira Patel is the duty lead who approves urgent avionics replacement requests for Atlas. |
| `p40` | selected, optional | 2.026 | 29 | Urgent replacement requests are marked red before they reach Mira Patel for approval. |
| `p26` | selected, distractor | 3.040 | 31 | A superseded training note says urgent avionics replacements are stored in Cage C. |
| `p11` | selected | 0.340 | 28 | Structural inspections must be logged in the amber maintenance ledger before release. |
| `p04` | selected, required | 1.098 | 29 | Cage D opens only after the secure tool room records Mira Patel's approval code. |
| `p25` | selected | 1.155 | 31 | Routine avionics labels are kept in the general parts cabinet, not the restricted cage. |
| `p23` | selected, optional | 1.485 | 30 | Torque kits are tracked by the secure tool room but are not stored in Cage D. |
| `p27` | selected, required | -0.340 | 27 | The secure tool room records approval codes for restricted cages. |
| `p14` | selected | 1.003 | 32 | A parts summary mentions Mira Patel and Cage D but says she approves hydraulic seals. |
| `p39` | - | -0.850 | 28 | Release paperwork is held until the amber ledger contains the structural inspection entry. |
| `p15` | - | -0.958 | 29 | The general parts cabinet contains fasteners, cable labels, and cleaning cloths. |
| `p12` | - | -0.949 | 27 | Shift controller Dev Rao reviews the amber maintenance ledger. |
| `p29` | - | -0.962 | 32 | Cabin panel reviews are logged in the white trim notebook, not the amber ledger. |
| `p36` | selected | 0.088 | 30 | A duplicate aft-warning note says cold starts can make insulation rub the left harness. |

### PASS content_01_aero_support / q07_two_hop / budget 1024

Question: What must happen before Cage D can be opened for an urgent avionics replacement?

Selected: `['p02', 'p03', 'p04', 'p11', 'p14', 'p23', 'p25', 'p26', 'p27', 'p36', 'p40']`
Tokens: `322/1024`
F1: `0.706` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `['p26']`

Score breakdown:

- individual: `15.868`
- pair synergy: `21.003`
- triple synergy: `7.125`
- redundancy penalty: `4.931`
- total: `39.065`

Improvement hint: Add wrong-context or contradiction-aware features; a distractor beat required evidence.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `p03` | selected, required | 3.596 | 27 | Approved urgent avionics replacements are stored in Cage D. |
| `p02` | selected, required | 2.116 | 28 | Mira Patel is the duty lead who approves urgent avionics replacement requests for Atlas. |
| `p40` | selected, optional | 2.054 | 29 | Urgent replacement requests are marked red before they reach Mira Patel for approval. |
| `p26` | selected, distractor | 3.070 | 31 | A superseded training note says urgent avionics replacements are stored in Cage C. |
| `p11` | selected | 0.368 | 28 | Structural inspections must be logged in the amber maintenance ledger before release. |
| `p04` | selected, required | 1.126 | 29 | Cage D opens only after the secure tool room records Mira Patel's approval code. |
| `p25` | selected | 1.185 | 31 | Routine avionics labels are kept in the general parts cabinet, not the restricted cage. |
| `p23` | selected, optional | 1.515 | 30 | Torque kits are tracked by the secure tool room but are not stored in Cage D. |
| `p27` | selected, required | -0.314 | 27 | The secure tool room records approval codes for restricted cages. |
| `p14` | selected | 1.035 | 32 | A parts summary mentions Mira Patel and Cage D but says she approves hydraulic seals. |
| `p39` | - | -0.823 | 28 | Release paperwork is held until the amber ledger contains the structural inspection entry. |
| `p15` | - | -0.930 | 29 | The general parts cabinet contains fasteners, cable labels, and cleaning cloths. |
| `p12` | - | -0.922 | 27 | Shift controller Dev Rao reviews the amber maintenance ledger. |
| `p29` | - | -0.931 | 32 | Cabin panel reviews are logged in the white trim notebook, not the amber ledger. |
| `p36` | selected | 0.117 | 30 | A duplicate aft-warning note says cold starts can make insulation rub the left harness. |

### PASS content_01_aero_support / q08_two_hop / budget 128

Question: What document is needed for Hangar 2 staging during winter calibration?

Selected: `['p06', 'p07', 'p19', 'p33']`
Tokens: `115/128`
F1: `0.857` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `['p33']`

Score breakdown:

- individual: `11.374`
- pair synergy: `3.126`
- triple synergy: `0.000`
- redundancy penalty: `1.098`
- total: `13.403`

Improvement hint: Add wrong-context or contradiction-aware features; a distractor beat required evidence.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `p19` | selected, required | 4.303 | 29 | Hangar 2 has limited power during winter calibration, so staging must be early. |
| `p06` | selected, required | 3.707 | 29 | The sensor cart must be staged beside Hangar 2 during winter calibration. |
| `p07` | selected, required | 1.833 | 27 | Hangar 2 staging requires the previous evening battery health printout. |
| `p33` | selected, distractor | 1.532 | 30 | Hangar 3 accepts overnight staging only for paint-shop air filters, not Atlas calibration carts. |
| `p05` | - | 0.760 | 28 | The winter calibration window begins at 06:30 before the first engine run. |
| `p31` | optional | 0.934 | 29 | The ground power team owns the battery health printout process for Atlas staging. |
| `p08` | optional | 0.932 | 28 | The previous evening battery health printout is filed in Binder Blue. |
| `p32` | - | 0.561 | 30 | The rollout coordinator checks that the sensor cart has arrived before calibration begins. |
| `p30` | - | 0.093 | 28 | Dev Rao is not responsible for catering, hydraulic seal approval, or Orion calibration. |
| `p17` | - | -0.130 | 33 | A contractor guide lists 07:15 as a calibration start time, but it applies to Orion. |
| `p34` | distractor | -0.376 | 31 | Binder Green contains fueling checklists and does not contain battery health printouts. |
| `p18` | - | -0.464 | 30 | The sensor cart carries tablet mounts and a red charging cable under its tray. |
| `p11` | - | -0.635 | 28 | Structural inspections must be logged in the amber maintenance ledger before release. |
| `p38` | - | -0.696 | 27 | The aft temperature warning should not be routed to the electrical corrosion queue. |
| `p01` | - | -0.714 | 27 | The Atlas night support desk moved to Bay 7 after the January ventilation review. |

### PASS content_01_aero_support / q08_two_hop / budget 256

Question: What document is needed for Hangar 2 staging during winter calibration?

Selected: `['p05', 'p06', 'p07', 'p08', 'p19', 'p31', 'p32', 'p33']`
Tokens: `230/256`
F1: `0.769` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `['p33']`

Score breakdown:

- individual: `15.461`
- pair synergy: `9.058`
- triple synergy: `0.000`
- redundancy penalty: `3.122`
- total: `21.397`

Improvement hint: Add wrong-context or contradiction-aware features; a distractor beat required evidence.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `p19` | selected, required | 4.416 | 29 | Hangar 2 has limited power during winter calibration, so staging must be early. |
| `p06` | selected, required | 3.820 | 29 | The sensor cart must be staged beside Hangar 2 during winter calibration. |
| `p07` | selected, required | 1.938 | 27 | Hangar 2 staging requires the previous evening battery health printout. |
| `p33` | selected, distractor | 1.649 | 30 | Hangar 3 accepts overnight staging only for paint-shop air filters, not Atlas calibration carts. |
| `p05` | selected | 0.870 | 28 | The winter calibration window begins at 06:30 before the first engine run. |
| `p31` | selected, optional | 1.047 | 29 | The ground power team owns the battery health printout process for Atlas staging. |
| `p08` | selected, optional | 1.041 | 28 | The previous evening battery health printout is filed in Binder Blue. |
| `p32` | selected | 0.679 | 30 | The rollout coordinator checks that the sensor cart has arrived before calibration begins. |
| `p30` | - | 0.202 | 28 | Dev Rao is not responsible for catering, hydraulic seal approval, or Orion calibration. |
| `p17` | - | -0.001 | 33 | A contractor guide lists 07:15 as a calibration start time, but it applies to Orion. |
| `p34` | distractor | -0.255 | 31 | Binder Green contains fueling checklists and does not contain battery health printouts. |
| `p18` | - | -0.347 | 30 | The sensor cart carries tablet mounts and a red charging cable under its tray. |
| `p11` | - | -0.525 | 28 | Structural inspections must be logged in the amber maintenance ledger before release. |
| `p38` | - | -0.591 | 27 | The aft temperature warning should not be routed to the electrical corrosion queue. |
| `p01` | - | -0.608 | 27 | The Atlas night support desk moved to Bay 7 after the January ventilation review. |

### PASS content_01_aero_support / q08_two_hop / budget 512

Question: What document is needed for Hangar 2 staging during winter calibration?

Selected: `['p05', 'p06', 'p07', 'p08', 'p17', 'p19', 'p30', 'p31', 'p32', 'p33', 'p34']`
Tokens: `322/512`
F1: `0.625` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `['p33', 'p34']`

Score breakdown:

- individual: `16.035`
- pair synergy: `12.978`
- triple synergy: `0.000`
- redundancy penalty: `4.375`
- total: `24.639`

Improvement hint: Add wrong-context or contradiction-aware features; a distractor beat required evidence.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `p19` | selected, required | 4.473 | 29 | Hangar 2 has limited power during winter calibration, so staging must be early. |
| `p06` | selected, required | 3.877 | 29 | The sensor cart must be staged beside Hangar 2 during winter calibration. |
| `p07` | selected, required | 1.991 | 27 | Hangar 2 staging requires the previous evening battery health printout. |
| `p33` | selected, distractor | 1.708 | 30 | Hangar 3 accepts overnight staging only for paint-shop air filters, not Atlas calibration carts. |
| `p05` | selected | 0.924 | 28 | The winter calibration window begins at 06:30 before the first engine run. |
| `p31` | selected, optional | 1.104 | 29 | The ground power team owns the battery health printout process for Atlas staging. |
| `p08` | selected, optional | 1.096 | 28 | The previous evening battery health printout is filed in Binder Blue. |
| `p32` | selected | 0.737 | 30 | The rollout coordinator checks that the sensor cart has arrived before calibration begins. |
| `p30` | selected | 0.257 | 28 | Dev Rao is not responsible for catering, hydraulic seal approval, or Orion calibration. |
| `p17` | selected | 0.063 | 33 | A contractor guide lists 07:15 as a calibration start time, but it applies to Orion. |
| `p34` | selected, distractor | -0.195 | 31 | Binder Green contains fueling checklists and does not contain battery health printouts. |
| `p18` | - | -0.289 | 30 | The sensor cart carries tablet mounts and a red charging cable under its tray. |
| `p11` | - | -0.471 | 28 | Structural inspections must be logged in the amber maintenance ledger before release. |
| `p38` | - | -0.538 | 27 | The aft temperature warning should not be routed to the electrical corrosion queue. |
| `p01` | - | -0.556 | 27 | The Atlas night support desk moved to Bay 7 after the January ventilation review. |

### PASS content_01_aero_support / q08_two_hop / budget 1024

Question: What document is needed for Hangar 2 staging during winter calibration?

Selected: `['p05', 'p06', 'p07', 'p08', 'p17', 'p18', 'p19', 'p30', 'p31', 'p32', 'p33', 'p34']`
Tokens: `352/1024`
F1: `0.588` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `['p33', 'p34']`

Score breakdown:

- individual: `16.090`
- pair synergy: `13.474`
- triple synergy: `0.000`
- redundancy penalty: `4.605`
- total: `24.959`

Improvement hint: Add wrong-context or contradiction-aware features; a distractor beat required evidence.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `p19` | selected, required | 4.501 | 29 | Hangar 2 has limited power during winter calibration, so staging must be early. |
| `p06` | selected, required | 3.905 | 29 | The sensor cart must be staged beside Hangar 2 during winter calibration. |
| `p07` | selected, required | 2.017 | 27 | Hangar 2 staging requires the previous evening battery health printout. |
| `p33` | selected, distractor | 1.737 | 30 | Hangar 3 accepts overnight staging only for paint-shop air filters, not Atlas calibration carts. |
| `p05` | selected | 0.952 | 28 | The winter calibration window begins at 06:30 before the first engine run. |
| `p31` | selected, optional | 1.132 | 29 | The ground power team owns the battery health printout process for Atlas staging. |
| `p08` | selected, optional | 1.123 | 28 | The previous evening battery health printout is filed in Binder Blue. |
| `p32` | selected | 0.767 | 30 | The rollout coordinator checks that the sensor cart has arrived before calibration begins. |
| `p30` | selected | 0.284 | 28 | Dev Rao is not responsible for catering, hydraulic seal approval, or Orion calibration. |
| `p17` | selected | 0.095 | 33 | A contractor guide lists 07:15 as a calibration start time, but it applies to Orion. |
| `p34` | selected, distractor | -0.164 | 31 | Binder Green contains fueling checklists and does not contain battery health printouts. |
| `p18` | selected | -0.259 | 30 | The sensor cart carries tablet mounts and a red charging cable under its tray. |
| `p11` | - | -0.443 | 28 | Structural inspections must be logged in the amber maintenance ledger before release. |
| `p38` | - | -0.512 | 27 | The aft temperature warning should not be routed to the electrical corrosion queue. |
| `p01` | - | -0.529 | 27 | The Atlas night support desk moved to Bay 7 after the January ventilation review. |

### PASS content_01_aero_support / q09_two_hop / budget 128

Question: Which team should handle the usual cause of the aft temperature warning?

Selected: `['p09', 'p10', 'p36', 'p38']`
Tokens: `116/128`
F1: `1.000` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `[]`

Score breakdown:

- individual: `9.021`
- pair synergy: `3.046`
- triple synergy: `0.000`
- redundancy penalty: `1.777`
- total: `10.290`

Improvement hint: Successful selection; inspect extra chunks only if precision or token cost becomes the priority.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `p38` | selected, optional | 2.331 | 27 | The aft temperature warning should not be routed to the electrical corrosion queue. |
| `p10` | selected, required | 2.531 | 29 | When the aft temperature warning appears, left harness inspection is assigned to structural. |
| `p09` | selected, required | 2.537 | 30 | Atlas field reports link the aft temperature warning to insulation rubbing the left harness. |
| `p36` | selected, required | 1.622 | 30 | A duplicate aft-warning note says cold starts can make insulation rub the left harness. |
| `p24` | - | 0.167 | 29 | Dev Rao signs the release sheet after the structural team entry appears. |
| `p19` | - | -0.946 | 29 | Hangar 2 has limited power during winter calibration, so staging must be early. |
| `p06` | - | -0.981 | 29 | The sensor cart must be staged beside Hangar 2 during winter calibration. |
| `p22` | optional | 0.664 | 30 | The electrical team reviews right-harness corrosion alerts, not left-harness insulation rubs. |
| `p07` | - | -0.999 | 27 | Hangar 2 staging requires the previous evening battery health printout. |
| `p31` | - | -0.217 | 29 | The ground power team owns the battery health printout process for Atlas staging. |
| `p39` | - | -0.445 | 28 | Release paperwork is held until the amber ledger contains the structural inspection entry. |
| `p33` | - | -0.745 | 30 | Hangar 3 accepts overnight staging only for paint-shop air filters, not Atlas calibration carts. |
| `p37` | - | -1.199 | 31 | A clerk may shelve the amber ledger beside fuel records after Dev Rao reviews it. |
| `p12` | - | -1.073 | 27 | Shift controller Dev Rao reviews the amber maintenance ledger. |
| `p11` | - | -0.682 | 28 | Structural inspections must be logged in the amber maintenance ledger before release. |

### PASS content_01_aero_support / q09_two_hop / budget 256

Question: Which team should handle the usual cause of the aft temperature warning?

Selected: `['p09', 'p10', 'p22', 'p24', 'p31', 'p36', 'p38', 'p39']`
Tokens: `232/256`
F1: `0.769` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `[]`

Score breakdown:

- individual: `10.095`
- pair synergy: `8.966`
- triple synergy: `0.000`
- redundancy penalty: `3.130`
- total: `15.931`

Improvement hint: Successful selection; inspect extra chunks only if precision or token cost becomes the priority.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `p38` | selected, optional | 2.436 | 27 | The aft temperature warning should not be routed to the electrical corrosion queue. |
| `p10` | selected, required | 2.644 | 29 | When the aft temperature warning appears, left harness inspection is assigned to structural. |
| `p09` | selected, required | 2.654 | 30 | Atlas field reports link the aft temperature warning to insulation rubbing the left harness. |
| `p36` | selected, required | 1.739 | 30 | A duplicate aft-warning note says cold starts can make insulation rub the left harness. |
| `p24` | selected | 0.281 | 29 | Dev Rao signs the release sheet after the structural team entry appears. |
| `p19` | - | -0.832 | 29 | Hangar 2 has limited power during winter calibration, so staging must be early. |
| `p06` | - | -0.868 | 29 | The sensor cart must be staged beside Hangar 2 during winter calibration. |
| `p22` | selected, optional | 0.781 | 30 | The electrical team reviews right-harness corrosion alerts, not left-harness insulation rubs. |
| `p07` | - | -0.893 | 27 | Hangar 2 staging requires the previous evening battery health printout. |
| `p31` | selected | -0.104 | 29 | The ground power team owns the battery health printout process for Atlas staging. |
| `p39` | selected | -0.336 | 28 | Release paperwork is held until the amber ledger contains the structural inspection entry. |
| `p33` | - | -0.628 | 30 | Hangar 3 accepts overnight staging only for paint-shop air filters, not Atlas calibration carts. |
| `p37` | - | -1.078 | 31 | A clerk may shelve the amber ledger beside fuel records after Dev Rao reviews it. |
| `p12` | - | -0.967 | 27 | Shift controller Dev Rao reviews the amber maintenance ledger. |
| `p11` | - | -0.572 | 28 | Structural inspections must be logged in the amber maintenance ledger before release. |

### PASS content_01_aero_support / q09_two_hop / budget 512

Question: Which team should handle the usual cause of the aft temperature warning?

Selected: `['p09', 'p10', 'p22', 'p24', 'p31', 'p36', 'p38', 'p39']`
Tokens: `232/512`
F1: `0.769` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `[]`

Score breakdown:

- individual: `10.549`
- pair synergy: `8.966`
- triple synergy: `0.000`
- redundancy penalty: `3.130`
- total: `16.384`

Improvement hint: Successful selection; inspect extra chunks only if precision or token cost becomes the priority.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `p38` | selected, optional | 2.489 | 27 | The aft temperature warning should not be routed to the electrical corrosion queue. |
| `p10` | selected, required | 2.701 | 29 | When the aft temperature warning appears, left harness inspection is assigned to structural. |
| `p09` | selected, required | 2.713 | 30 | Atlas field reports link the aft temperature warning to insulation rubbing the left harness. |
| `p36` | selected, required | 1.798 | 30 | A duplicate aft-warning note says cold starts can make insulation rub the left harness. |
| `p24` | selected | 0.337 | 29 | Dev Rao signs the release sheet after the structural team entry appears. |
| `p19` | - | -0.776 | 29 | Hangar 2 has limited power during winter calibration, so staging must be early. |
| `p06` | - | -0.812 | 29 | The sensor cart must be staged beside Hangar 2 during winter calibration. |
| `p22` | selected, optional | 0.839 | 30 | The electrical team reviews right-harness corrosion alerts, not left-harness insulation rubs. |
| `p07` | - | -0.840 | 27 | Hangar 2 staging requires the previous evening battery health printout. |
| `p31` | selected | -0.047 | 29 | The ground power team owns the battery health printout process for Atlas staging. |
| `p39` | selected | -0.281 | 28 | Release paperwork is held until the amber ledger contains the structural inspection entry. |
| `p33` | - | -0.569 | 30 | Hangar 3 accepts overnight staging only for paint-shop air filters, not Atlas calibration carts. |
| `p37` | - | -1.018 | 31 | A clerk may shelve the amber ledger beside fuel records after Dev Rao reviews it. |
| `p12` | - | -0.914 | 27 | Shift controller Dev Rao reviews the amber maintenance ledger. |
| `p11` | - | -0.517 | 28 | Structural inspections must be logged in the amber maintenance ledger before release. |

### PASS content_01_aero_support / q09_two_hop / budget 1024

Question: Which team should handle the usual cause of the aft temperature warning?

Selected: `['p09', 'p10', 'p22', 'p24', 'p31', 'p36', 'p38', 'p39']`
Tokens: `232/1024`
F1: `0.769` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `[]`

Score breakdown:

- individual: `10.775`
- pair synergy: `8.966`
- triple synergy: `0.000`
- redundancy penalty: `3.130`
- total: `16.611`

Improvement hint: Successful selection; inspect extra chunks only if precision or token cost becomes the priority.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `p38` | selected, optional | 2.515 | 27 | The aft temperature warning should not be routed to the electrical corrosion queue. |
| `p10` | selected, required | 2.729 | 29 | When the aft temperature warning appears, left harness inspection is assigned to structural. |
| `p09` | selected, required | 2.742 | 30 | Atlas field reports link the aft temperature warning to insulation rubbing the left harness. |
| `p36` | selected, required | 1.827 | 30 | A duplicate aft-warning note says cold starts can make insulation rub the left harness. |
| `p24` | selected | 0.366 | 29 | Dev Rao signs the release sheet after the structural team entry appears. |
| `p19` | - | -0.747 | 29 | Hangar 2 has limited power during winter calibration, so staging must be early. |
| `p06` | - | -0.783 | 29 | The sensor cart must be staged beside Hangar 2 during winter calibration. |
| `p22` | selected, optional | 0.869 | 30 | The electrical team reviews right-harness corrosion alerts, not left-harness insulation rubs. |
| `p07` | - | -0.814 | 27 | Hangar 2 staging requires the previous evening battery health printout. |
| `p31` | selected | -0.019 | 29 | The ground power team owns the battery health printout process for Atlas staging. |
| `p39` | selected | -0.254 | 28 | Release paperwork is held until the amber ledger contains the structural inspection entry. |
| `p33` | - | -0.540 | 30 | Hangar 3 accepts overnight staging only for paint-shop air filters, not Atlas calibration carts. |
| `p37` | - | -0.987 | 31 | A clerk may shelve the amber ledger beside fuel records after Dev Rao reviews it. |
| `p12` | - | -0.888 | 27 | Shift controller Dev Rao reviews the amber maintenance ledger. |
| `p11` | - | -0.490 | 28 | Structural inspections must be logged in the amber maintenance ledger before release. |

### PASS content_01_aero_support / q10_two_hop / budget 128

Question: Who reviews the required log after a structural inspection?

Selected: `['p12', 'p24', 'p37', 'p39']`
Tokens: `115/128`
F1: `1.000` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `[]`

Score breakdown:

- individual: `5.694`
- pair synergy: `4.503`
- triple synergy: `0.208`
- redundancy penalty: `1.145`
- total: `9.260`

Improvement hint: Successful selection; inspect extra chunks only if precision or token cost becomes the priority.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `p39` | selected, required | 1.431 | 28 | Release paperwork is held until the amber ledger contains the structural inspection entry. |
| `p10` | - | 1.007 | 29 | When the aft temperature warning appears, left harness inspection is assigned to structural. |
| `p24` | selected, required | 1.259 | 29 | Dev Rao signs the release sheet after the structural team entry appears. |
| `p37` | selected, optional | 1.322 | 31 | A clerk may shelve the amber ledger beside fuel records after Dev Rao reviews it. |
| `p01` | - | -0.117 | 27 | The Atlas night support desk moved to Bay 7 after the January ventilation review. |
| `p11` | required | 1.370 | 28 | Structural inspections must be logged in the amber maintenance ledger before release. |
| `p29` | - | 0.632 | 32 | Cabin panel reviews are logged in the white trim notebook, not the amber ledger. |
| `p12` | selected, required | 1.682 | 27 | Shift controller Dev Rao reviews the amber maintenance ledger. |
| `p09` | - | 0.732 | 30 | Atlas field reports link the aft temperature warning to insulation rubbing the left harness. |
| `p21` | - | -1.137 | 31 | A retired memo says the Atlas night desk moved to Bay 5, but that memo was withdrawn. |
| `p22` | - | 0.344 | 30 | The electrical team reviews right-harness corrosion alerts, not left-harness insulation rubs. |
| `p36` | - | 0.290 | 30 | A duplicate aft-warning note says cold starts can make insulation rub the left harness. |
| `p35` | - | -1.166 | 33 | A facilities bulletin mentions Bay 7 catering deliveries unrelated to the night desk. |
| `p38` | - | 0.083 | 27 | The aft temperature warning should not be routed to the electrical corrosion queue. |
| `p04` | - | 0.081 | 29 | Cage D opens only after the secure tool room records Mira Patel's approval code. |

### PASS content_01_aero_support / q10_two_hop / budget 256

Question: Who reviews the required log after a structural inspection?

Selected: `['p04', 'p10', 'p11', 'p12', 'p24', 'p29', 'p37', 'p39']`
Tokens: `233/256`
F1: `0.769` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `[]`

Score breakdown:

- individual: `9.695`
- pair synergy: `13.785`
- triple synergy: `2.083`
- redundancy penalty: `3.234`
- total: `22.329`

Improvement hint: Successful selection; inspect extra chunks only if precision or token cost becomes the priority.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `p39` | selected, required | 1.540 | 28 | Release paperwork is held until the amber ledger contains the structural inspection entry. |
| `p10` | selected | 1.121 | 29 | When the aft temperature warning appears, left harness inspection is assigned to structural. |
| `p24` | selected, required | 1.372 | 29 | Dev Rao signs the release sheet after the structural team entry appears. |
| `p37` | selected, optional | 1.443 | 31 | A clerk may shelve the amber ledger beside fuel records after Dev Rao reviews it. |
| `p01` | - | -0.011 | 27 | The Atlas night support desk moved to Bay 7 after the January ventilation review. |
| `p11` | selected, required | 1.479 | 28 | Structural inspections must be logged in the amber maintenance ledger before release. |
| `p29` | selected | 0.757 | 32 | Cabin panel reviews are logged in the white trim notebook, not the amber ledger. |
| `p12` | selected, required | 1.787 | 27 | Shift controller Dev Rao reviews the amber maintenance ledger. |
| `p09` | - | 0.849 | 30 | Atlas field reports link the aft temperature warning to insulation rubbing the left harness. |
| `p21` | - | -1.016 | 31 | A retired memo says the Atlas night desk moved to Bay 5, but that memo was withdrawn. |
| `p22` | - | 0.461 | 30 | The electrical team reviews right-harness corrosion alerts, not left-harness insulation rubs. |
| `p36` | - | 0.407 | 30 | A duplicate aft-warning note says cold starts can make insulation rub the left harness. |
| `p35` | - | -1.037 | 33 | A facilities bulletin mentions Bay 7 catering deliveries unrelated to the night desk. |
| `p04` | selected | 0.195 | 29 | Cage D opens only after the secure tool room records Mira Patel's approval code. |
| `p38` | - | 0.189 | 27 | The aft temperature warning should not be routed to the electrical corrosion queue. |

### PASS content_01_aero_support / q10_two_hop / budget 512

Question: Who reviews the required log after a structural inspection?

Selected: `['p01', 'p04', 'p09', 'p10', 'p11', 'p12', 'p22', 'p24', 'p29', 'p36', 'p37', 'p38', 'p39']`
Tokens: `377/512`
F1: `0.556` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `[]`

Score breakdown:

- individual: `12.326`
- pair synergy: `23.229`
- triple synergy: `5.000`
- redundancy penalty: `6.232`
- total: `34.324`

Improvement hint: Successful selection; inspect extra chunks only if precision or token cost becomes the priority.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `p39` | selected, required | 1.595 | 28 | Release paperwork is held until the amber ledger contains the structural inspection entry. |
| `p10` | selected | 1.177 | 29 | When the aft temperature warning appears, left harness inspection is assigned to structural. |
| `p24` | selected, required | 1.429 | 29 | Dev Rao signs the release sheet after the structural team entry appears. |
| `p37` | selected, optional | 1.504 | 31 | A clerk may shelve the amber ledger beside fuel records after Dev Rao reviews it. |
| `p01` | selected | 0.042 | 27 | The Atlas night support desk moved to Bay 7 after the January ventilation review. |
| `p11` | selected, required | 1.534 | 28 | Structural inspections must be logged in the amber maintenance ledger before release. |
| `p29` | selected | 0.819 | 32 | Cabin panel reviews are logged in the white trim notebook, not the amber ledger. |
| `p12` | selected, required | 1.840 | 27 | Shift controller Dev Rao reviews the amber maintenance ledger. |
| `p09` | selected | 0.908 | 30 | Atlas field reports link the aft temperature warning to insulation rubbing the left harness. |
| `p21` | - | -0.955 | 31 | A retired memo says the Atlas night desk moved to Bay 5, but that memo was withdrawn. |
| `p22` | selected | 0.520 | 30 | The electrical team reviews right-harness corrosion alerts, not left-harness insulation rubs. |
| `p36` | selected | 0.466 | 30 | A duplicate aft-warning note says cold starts can make insulation rub the left harness. |
| `p35` | - | -0.972 | 33 | A facilities bulletin mentions Bay 7 catering deliveries unrelated to the night desk. |
| `p04` | selected | 0.251 | 29 | Cage D opens only after the secure tool room records Mira Patel's approval code. |
| `p38` | selected | 0.241 | 27 | The aft temperature warning should not be routed to the electrical corrosion queue. |

### PASS content_01_aero_support / q10_two_hop / budget 1024

Question: Who reviews the required log after a structural inspection?

Selected: `['p01', 'p04', 'p09', 'p10', 'p11', 'p12', 'p22', 'p24', 'p29', 'p36', 'p37', 'p38', 'p39']`
Tokens: `377/1024`
F1: `0.556` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `[]`

Score breakdown:

- individual: `12.694`
- pair synergy: `23.229`
- triple synergy: `5.000`
- redundancy penalty: `6.232`
- total: `34.692`

Improvement hint: Successful selection; inspect extra chunks only if precision or token cost becomes the priority.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `p39` | selected, required | 1.622 | 28 | Release paperwork is held until the amber ledger contains the structural inspection entry. |
| `p10` | selected | 1.206 | 29 | When the aft temperature warning appears, left harness inspection is assigned to structural. |
| `p24` | selected, required | 1.457 | 29 | Dev Rao signs the release sheet after the structural team entry appears. |
| `p37` | selected, optional | 1.534 | 31 | A clerk may shelve the amber ledger beside fuel records after Dev Rao reviews it. |
| `p01` | selected | 0.068 | 27 | The Atlas night support desk moved to Bay 7 after the January ventilation review. |
| `p11` | selected, required | 1.561 | 28 | Structural inspections must be logged in the amber maintenance ledger before release. |
| `p29` | selected | 0.851 | 32 | Cabin panel reviews are logged in the white trim notebook, not the amber ledger. |
| `p12` | selected, required | 1.866 | 27 | Shift controller Dev Rao reviews the amber maintenance ledger. |
| `p09` | selected | 0.937 | 30 | Atlas field reports link the aft temperature warning to insulation rubbing the left harness. |
| `p21` | - | -0.925 | 31 | A retired memo says the Atlas night desk moved to Bay 5, but that memo was withdrawn. |
| `p22` | selected | 0.549 | 30 | The electrical team reviews right-harness corrosion alerts, not left-harness insulation rubs. |
| `p36` | selected | 0.495 | 30 | A duplicate aft-warning note says cold starts can make insulation rub the left harness. |
| `p35` | - | -0.940 | 33 | A facilities bulletin mentions Bay 7 catering deliveries unrelated to the night desk. |
| `p04` | selected | 0.280 | 29 | Cage D opens only after the secure tool room records Mira Patel's approval code. |
| `p38` | selected | 0.268 | 27 | The aft temperature warning should not be routed to the electrical corrosion queue. |

### FAIL content_01_aero_support / q11_three_hop / budget 128

Question: Which restricted location becomes accessible after Mira Patel approves the urgent replacement and the tool room records the code?

Selected: `['p02', 'p04', 'p27', 'p40']`
Tokens: `113/128`
F1: `0.800` Required recall: `0.667`
Missing required units: `['storage']`
Selected distractors: `[]`

Score breakdown:

- individual: `10.745`
- pair synergy: `4.240`
- triple synergy: `0.179`
- redundancy penalty: `1.001`
- total: `14.162`

Improvement hint: Scoring issue; required evidence was available but not valuable enough under current utility.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `p04` | selected, required | 3.631 | 29 | Cage D opens only after the secure tool room records Mira Patel's approval code. |
| `p02` | selected, required | 2.458 | 28 | Mira Patel is the duty lead who approves urgent avionics replacement requests for Atlas. |
| `p27` | selected, required | 2.565 | 27 | The secure tool room records approval codes for restricted cages. |
| `p40` | selected, optional | 2.091 | 29 | Urgent replacement requests are marked red before they reach Mira Patel for approval. |
| `p14` | distractor | 1.031 | 32 | A parts summary mentions Mira Patel and Cage D but says she approves hydraulic seals. |
| `p39` | - | -0.944 | 28 | Release paperwork is held until the amber ledger contains the structural inspection entry. |
| `p23` | optional | 1.148 | 30 | Torque kits are tracked by the secure tool room but are not stored in Cage D. |
| `p11` | - | -0.636 | 28 | Structural inspections must be logged in the amber maintenance ledger before release. |
| `p37` | - | 0.226 | 31 | A clerk may shelve the amber ledger beside fuel records after Dev Rao reviews it. |
| `p24` | - | -0.306 | 29 | Dev Rao signs the release sheet after the structural team entry appears. |
| `p03` | required | 0.245 | 27 | Approved urgent avionics replacements are stored in Cage D. |
| `p25` | - | -0.256 | 31 | Routine avionics labels are kept in the general parts cabinet, not the restricted cage. |
| `p26` | distractor | -0.072 | 31 | A superseded training note says urgent avionics replacements are stored in Cage C. |
| `p12` | - | -0.945 | 27 | Shift controller Dev Rao reviews the amber maintenance ledger. |
| `p20` | - | -0.354 | 30 | A spare binder shelf label near the fuel records cabinet also says amber. |

### PASS content_01_aero_support / q11_three_hop / budget 256

Question: Which restricted location becomes accessible after Mira Patel approves the urgent replacement and the tool room records the code?

Selected: `['p02', 'p03', 'p04', 'p14', 'p23', 'p27', 'p37', 'p40']`
Tokens: `233/256`
F1: `0.857` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `['p14']`

Score breakdown:

- individual: `14.304`
- pair synergy: `12.507`
- triple synergy: `2.054`
- redundancy penalty: `2.958`
- total: `25.906`

Improvement hint: Add wrong-context or contradiction-aware features; a distractor beat required evidence.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `p04` | selected, required | 3.744 | 29 | Cage D opens only after the secure tool room records Mira Patel's approval code. |
| `p02` | selected, required | 2.568 | 28 | Mira Patel is the duty lead who approves urgent avionics replacement requests for Atlas. |
| `p27` | selected, required | 2.670 | 27 | The secure tool room records approval codes for restricted cages. |
| `p40` | selected, optional | 2.205 | 29 | Urgent replacement requests are marked red before they reach Mira Patel for approval. |
| `p14` | selected, distractor | 1.156 | 32 | A parts summary mentions Mira Patel and Cage D but says she approves hydraulic seals. |
| `p39` | - | -0.835 | 28 | Release paperwork is held until the amber ledger contains the structural inspection entry. |
| `p23` | selected, optional | 1.265 | 30 | Torque kits are tracked by the secure tool room but are not stored in Cage D. |
| `p11` | - | -0.526 | 28 | Structural inspections must be logged in the amber maintenance ledger before release. |
| `p37` | selected | 0.347 | 31 | A clerk may shelve the amber ledger beside fuel records after Dev Rao reviews it. |
| `p24` | - | -0.193 | 29 | Dev Rao signs the release sheet after the structural team entry appears. |
| `p03` | selected, required | 0.350 | 27 | Approved urgent avionics replacements are stored in Cage D. |
| `p25` | - | -0.134 | 31 | Routine avionics labels are kept in the general parts cabinet, not the restricted cage. |
| `p26` | distractor | 0.049 | 31 | A superseded training note says urgent avionics replacements are stored in Cage C. |
| `p12` | - | -0.839 | 27 | Shift controller Dev Rao reviews the amber maintenance ledger. |
| `p20` | - | -0.237 | 30 | A spare binder shelf label near the fuel records cabinet also says amber. |

### PASS content_01_aero_support / q11_three_hop / budget 512

Question: Which restricted location becomes accessible after Mira Patel approves the urgent replacement and the tool room records the code?

Selected: `['p02', 'p03', 'p04', 'p11', 'p12', 'p14', 'p20', 'p23', 'p24', 'p25', 'p26', 'p27', 'p37', 'p39', 'p40']`
Tokens: `437/512`
F1: `0.571` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `['p14', 'p26']`

Score breakdown:

- individual: `12.442`
- pair synergy: `26.062`
- triple synergy: `7.946`
- redundancy penalty: `7.620`
- total: `38.831`

Improvement hint: Add wrong-context or contradiction-aware features; a distractor beat required evidence.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `p04` | selected, required | 3.801 | 29 | Cage D opens only after the secure tool room records Mira Patel's approval code. |
| `p02` | selected, required | 2.622 | 28 | Mira Patel is the duty lead who approves urgent avionics replacement requests for Atlas. |
| `p27` | selected, required | 2.723 | 27 | The secure tool room records approval codes for restricted cages. |
| `p40` | selected, optional | 2.261 | 29 | Urgent replacement requests are marked red before they reach Mira Patel for approval. |
| `p14` | selected, distractor | 1.218 | 32 | A parts summary mentions Mira Patel and Cage D but says she approves hydraulic seals. |
| `p39` | selected | -0.780 | 28 | Release paperwork is held until the amber ledger contains the structural inspection entry. |
| `p23` | selected, optional | 1.324 | 30 | Torque kits are tracked by the secure tool room but are not stored in Cage D. |
| `p11` | selected | -0.471 | 28 | Structural inspections must be logged in the amber maintenance ledger before release. |
| `p37` | selected | 0.407 | 31 | A clerk may shelve the amber ledger beside fuel records after Dev Rao reviews it. |
| `p24` | selected | -0.137 | 29 | Dev Rao signs the release sheet after the structural team entry appears. |
| `p03` | selected, required | 0.403 | 27 | Approved urgent avionics replacements are stored in Cage D. |
| `p25` | selected | -0.074 | 31 | Routine avionics labels are kept in the general parts cabinet, not the restricted cage. |
| `p26` | selected, distractor | 0.110 | 31 | A superseded training note says urgent avionics replacements are stored in Cage C. |
| `p12` | selected | -0.786 | 27 | Shift controller Dev Rao reviews the amber maintenance ledger. |
| `p20` | selected | -0.178 | 30 | A spare binder shelf label near the fuel records cabinet also says amber. |

### PASS content_01_aero_support / q11_three_hop / budget 1024

Question: Which restricted location becomes accessible after Mira Patel approves the urgent replacement and the tool room records the code?

Selected: `['p02', 'p03', 'p04', 'p11', 'p12', 'p14', 'p20', 'p23', 'p24', 'p25', 'p26', 'p27', 'p37', 'p39', 'p40']`
Tokens: `437/1024`
F1: `0.571` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `['p14', 'p26']`

Score breakdown:

- individual: `12.869`
- pair synergy: `26.062`
- triple synergy: `7.946`
- redundancy penalty: `7.620`
- total: `39.257`

Improvement hint: Add wrong-context or contradiction-aware features; a distractor beat required evidence.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `p04` | selected, required | 3.829 | 29 | Cage D opens only after the secure tool room records Mira Patel's approval code. |
| `p02` | selected, required | 2.650 | 28 | Mira Patel is the duty lead who approves urgent avionics replacement requests for Atlas. |
| `p27` | selected, required | 2.749 | 27 | The secure tool room records approval codes for restricted cages. |
| `p40` | selected, optional | 2.289 | 29 | Urgent replacement requests are marked red before they reach Mira Patel for approval. |
| `p14` | selected, distractor | 1.249 | 32 | A parts summary mentions Mira Patel and Cage D but says she approves hydraulic seals. |
| `p39` | selected | -0.753 | 28 | Release paperwork is held until the amber ledger contains the structural inspection entry. |
| `p23` | selected, optional | 1.353 | 30 | Torque kits are tracked by the secure tool room but are not stored in Cage D. |
| `p11` | selected | -0.444 | 28 | Structural inspections must be logged in the amber maintenance ledger before release. |
| `p37` | selected | 0.437 | 31 | A clerk may shelve the amber ledger beside fuel records after Dev Rao reviews it. |
| `p24` | selected | -0.108 | 29 | Dev Rao signs the release sheet after the structural team entry appears. |
| `p03` | selected, required | 0.429 | 27 | Approved urgent avionics replacements are stored in Cage D. |
| `p25` | selected | -0.044 | 31 | Routine avionics labels are kept in the general parts cabinet, not the restricted cage. |
| `p26` | selected, distractor | 0.140 | 31 | A superseded training note says urgent avionics replacements are stored in Cage C. |
| `p12` | selected | -0.760 | 27 | Shift controller Dev Rao reviews the amber maintenance ledger. |
| `p20` | selected | -0.149 | 30 | A spare binder shelf label near the fuel records cabinet also says amber. |

### PASS content_01_aero_support / q12_three_hop / budget 128

Question: Which team files the binder needed for the document required by Hangar 2 staging?

Selected: `['p07', 'p08', 'p19', 'p31']`
Tokens: `113/128`
F1: `1.000` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `[]`

Score breakdown:

- individual: `7.035`
- pair synergy: `3.682`
- triple synergy: `0.278`
- redundancy penalty: `1.294`
- total: `9.701`

Improvement hint: Successful selection; inspect extra chunks only if precision or token cost becomes the priority.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `p07` | selected, required | 1.674 | 27 | Hangar 2 staging requires the previous evening battery health printout. |
| `p19` | selected, required | 2.490 | 29 | Hangar 2 has limited power during winter calibration, so staging must be early. |
| `p06` | required | 1.912 | 29 | The sensor cart must be staged beside Hangar 2 during winter calibration. |
| `p28` | required | 0.283 | 29 | Ground power files Binder Blue after the battery cart is returned. |
| `p31` | selected, required | 1.400 | 29 | The ground power team owns the battery health printout process for Atlas staging. |
| `p33` | distractor | 0.882 | 30 | Hangar 3 accepts overnight staging only for paint-shop air filters, not Atlas calibration carts. |
| `p24` | - | -0.493 | 29 | Dev Rao signs the release sheet after the structural team entry appears. |
| `p08` | selected, required | 1.470 | 28 | The previous evening battery health printout is filed in Binder Blue. |
| `p34` | distractor | 0.183 | 31 | Binder Green contains fueling checklists and does not contain battery health printouts. |
| `p39` | - | -0.971 | 28 | Release paperwork is held until the amber ledger contains the structural inspection entry. |
| `p32` | optional | -0.060 | 30 | The rollout coordinator checks that the sensor cart has arrived before calibration begins. |
| `p37` | - | -0.739 | 31 | A clerk may shelve the amber ledger beside fuel records after Dev Rao reviews it. |
| `p20` | - | -0.529 | 30 | A spare binder shelf label near the fuel records cabinet also says amber. |
| `p12` | - | -1.103 | 27 | Shift controller Dev Rao reviews the amber maintenance ledger. |
| `p11` | - | -0.656 | 28 | Structural inspections must be logged in the amber maintenance ledger before release. |

### PASS content_01_aero_support / q12_three_hop / budget 256

Question: Which team files the binder needed for the document required by Hangar 2 staging?

Selected: `['p06', 'p07', 'p08', 'p19', 'p28', 'p31', 'p33', 'p34']`
Tokens: `232/256`
F1: `0.857` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `['p33', 'p34']`

Score breakdown:

- individual: `11.201`
- pair synergy: `13.349`
- triple synergy: `2.222`
- redundancy penalty: `3.570`
- total: `23.203`

Improvement hint: Add wrong-context or contradiction-aware features; a distractor beat required evidence.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `p07` | selected, required | 1.780 | 27 | Hangar 2 staging requires the previous evening battery health printout. |
| `p19` | selected, required | 2.603 | 29 | Hangar 2 has limited power during winter calibration, so staging must be early. |
| `p06` | selected, required | 2.025 | 29 | The sensor cart must be staged beside Hangar 2 during winter calibration. |
| `p28` | selected, required | 0.397 | 29 | Ground power files Binder Blue after the battery cart is returned. |
| `p31` | selected, required | 1.513 | 29 | The ground power team owns the battery health printout process for Atlas staging. |
| `p33` | selected, distractor | 0.999 | 30 | Hangar 3 accepts overnight staging only for paint-shop air filters, not Atlas calibration carts. |
| `p24` | - | -0.380 | 29 | Dev Rao signs the release sheet after the structural team entry appears. |
| `p08` | selected, required | 1.580 | 28 | The previous evening battery health printout is filed in Binder Blue. |
| `p34` | selected, distractor | 0.304 | 31 | Binder Green contains fueling checklists and does not contain battery health printouts. |
| `p39` | - | -0.862 | 28 | Release paperwork is held until the amber ledger contains the structural inspection entry. |
| `p32` | optional | 0.057 | 30 | The rollout coordinator checks that the sensor cart has arrived before calibration begins. |
| `p37` | - | -0.618 | 31 | A clerk may shelve the amber ledger beside fuel records after Dev Rao reviews it. |
| `p20` | - | -0.411 | 30 | A spare binder shelf label near the fuel records cabinet also says amber. |
| `p12` | - | -0.997 | 27 | Shift controller Dev Rao reviews the amber maintenance ledger. |
| `p11` | - | -0.547 | 28 | Structural inspections must be logged in the amber maintenance ledger before release. |

### PASS content_01_aero_support / q12_three_hop / budget 512

Question: Which team files the binder needed for the document required by Hangar 2 staging?

Selected: `['p06', 'p07', 'p08', 'p11', 'p12', 'p19', 'p20', 'p24', 'p28', 'p31', 'p32', 'p33', 'p34', 'p37', 'p39']`
Tokens: `435/512`
F1: `0.636` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `['p33', 'p34']`

Score breakdown:

- individual: `8.293`
- pair synergy: `23.602`
- triple synergy: `5.278`
- redundancy penalty: `6.980`
- total: `30.192`

Improvement hint: Add wrong-context or contradiction-aware features; a distractor beat required evidence.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `p07` | selected, required | 1.833 | 27 | Hangar 2 staging requires the previous evening battery health printout. |
| `p19` | selected, required | 2.660 | 29 | Hangar 2 has limited power during winter calibration, so staging must be early. |
| `p06` | selected, required | 2.082 | 29 | The sensor cart must be staged beside Hangar 2 during winter calibration. |
| `p28` | selected, required | 0.453 | 29 | Ground power files Binder Blue after the battery cart is returned. |
| `p31` | selected, required | 1.570 | 29 | The ground power team owns the battery health printout process for Atlas staging. |
| `p33` | selected, distractor | 1.058 | 30 | Hangar 3 accepts overnight staging only for paint-shop air filters, not Atlas calibration carts. |
| `p24` | selected | -0.323 | 29 | Dev Rao signs the release sheet after the structural team entry appears. |
| `p08` | selected, required | 1.634 | 28 | The previous evening battery health printout is filed in Binder Blue. |
| `p34` | selected, distractor | 0.365 | 31 | Binder Green contains fueling checklists and does not contain battery health printouts. |
| `p39` | selected | -0.807 | 28 | Release paperwork is held until the amber ledger contains the structural inspection entry. |
| `p32` | selected, optional | 0.116 | 30 | The rollout coordinator checks that the sensor cart has arrived before calibration begins. |
| `p37` | selected | -0.558 | 31 | A clerk may shelve the amber ledger beside fuel records after Dev Rao reviews it. |
| `p20` | selected | -0.353 | 30 | A spare binder shelf label near the fuel records cabinet also says amber. |
| `p11` | selected | -0.492 | 28 | Structural inspections must be logged in the amber maintenance ledger before release. |
| `p12` | selected | -0.945 | 27 | Shift controller Dev Rao reviews the amber maintenance ledger. |

### PASS content_01_aero_support / q12_three_hop / budget 1024

Question: Which team files the binder needed for the document required by Hangar 2 staging?

Selected: `['p06', 'p07', 'p08', 'p11', 'p12', 'p19', 'p20', 'p24', 'p28', 'p31', 'p32', 'p33', 'p34', 'p37', 'p39']`
Tokens: `435/1024`
F1: `0.636` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `['p33', 'p34']`

Score breakdown:

- individual: `8.717`
- pair synergy: `23.602`
- triple synergy: `5.278`
- redundancy penalty: `6.980`
- total: `30.617`

Improvement hint: Add wrong-context or contradiction-aware features; a distractor beat required evidence.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `p07` | selected, required | 1.859 | 27 | Hangar 2 staging requires the previous evening battery health printout. |
| `p19` | selected, required | 2.688 | 29 | Hangar 2 has limited power during winter calibration, so staging must be early. |
| `p06` | selected, required | 2.110 | 29 | The sensor cart must be staged beside Hangar 2 during winter calibration. |
| `p28` | selected, required | 0.482 | 29 | Ground power files Binder Blue after the battery cart is returned. |
| `p31` | selected, required | 1.598 | 29 | The ground power team owns the battery health printout process for Atlas staging. |
| `p33` | selected, distractor | 1.087 | 30 | Hangar 3 accepts overnight staging only for paint-shop air filters, not Atlas calibration carts. |
| `p24` | selected | -0.295 | 29 | Dev Rao signs the release sheet after the structural team entry appears. |
| `p08` | selected, required | 1.662 | 28 | The previous evening battery health printout is filed in Binder Blue. |
| `p34` | selected, distractor | 0.395 | 31 | Binder Green contains fueling checklists and does not contain battery health printouts. |
| `p39` | selected | -0.780 | 28 | Release paperwork is held until the amber ledger contains the structural inspection entry. |
| `p32` | selected, optional | 0.145 | 30 | The rollout coordinator checks that the sensor cart has arrived before calibration begins. |
| `p37` | selected | -0.527 | 31 | A clerk may shelve the amber ledger beside fuel records after Dev Rao reviews it. |
| `p20` | selected | -0.323 | 30 | A spare binder shelf label near the fuel records cabinet also says amber. |
| `p11` | selected | -0.465 | 28 | Structural inspections must be logged in the amber maintenance ledger before release. |
| `p12` | selected | -0.918 | 27 | Shift controller Dev Rao reviews the amber maintenance ledger. |

### FAIL content_01_aero_support / q13_three_hop / budget 128

Question: Who reviews the record after the team assigned to the aft warning completes its required log?

Selected: `['p09', 'p10', 'p22', 'p36']`
Tokens: `119/128`
F1: `0.600` Required recall: `0.500`
Missing required units: `['log', 'reviewer']`
Selected distractors: `['p22']`

Score breakdown:

- individual: `6.112`
- pair synergy: `3.980`
- triple synergy: `0.000`
- redundancy penalty: `1.704`
- total: `8.388`

Improvement hint: Add wrong-context or contradiction-aware features; a distractor beat required evidence.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `p10` | selected, required | 2.165 | 29 | When the aft temperature warning appears, left harness inspection is assigned to structural. |
| `p38` | optional | 0.997 | 27 | The aft temperature warning should not be routed to the electrical corrosion queue. |
| `p24` | required | 0.540 | 29 | Dev Rao signs the release sheet after the structural team entry appears. |
| `p09` | selected, required | 1.690 | 30 | Atlas field reports link the aft temperature warning to insulation rubbing the left harness. |
| `p22` | selected, distractor | 0.951 | 30 | The electrical team reviews right-harness corrosion alerts, not left-harness insulation rubs. |
| `p11` | required | -0.189 | 28 | Structural inspections must be logged in the amber maintenance ledger before release. |
| `p39` | required | 0.013 | 28 | Release paperwork is held until the amber ledger contains the structural inspection entry. |
| `p12` | required | 0.240 | 27 | Shift controller Dev Rao reviews the amber maintenance ledger. |
| `p37` | optional | 0.770 | 31 | A clerk may shelve the amber ledger beside fuel records after Dev Rao reviews it. |
| `p36` | selected, required | 1.305 | 30 | A duplicate aft-warning note says cold starts can make insulation rub the left harness. |
| `p29` | distractor | -0.248 | 32 | Cabin panel reviews are logged in the white trim notebook, not the amber ledger. |
| `p30` | - | -0.425 | 28 | Dev Rao is not responsible for catering, hydraulic seal approval, or Orion calibration. |
| `p31` | - | -0.297 | 29 | The ground power team owns the battery health printout process for Atlas staging. |
| `p04` | - | -0.322 | 29 | Cage D opens only after the secure tool room records Mira Patel's approval code. |
| `p01` | - | -0.324 | 27 | The Atlas night support desk moved to Bay 7 after the January ventilation review. |

### FAIL content_01_aero_support / q13_three_hop / budget 256

Question: Who reviews the record after the team assigned to the aft warning completes its required log?

Selected: `['p09', 'p10', 'p12', 'p22', 'p24', 'p36', 'p37', 'p38']`
Tokens: `233/256`
F1: `0.808` Required recall: `0.750`
Missing required units: `['log']`
Selected distractors: `['p22']`

Score breakdown:

- individual: `10.153`
- pair synergy: `12.523`
- triple synergy: `1.818`
- redundancy penalty: `3.434`
- total: `21.060`

Improvement hint: Add wrong-context or contradiction-aware features; a distractor beat required evidence.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `p10` | selected, required | 1.549 | 29 | When the aft temperature warning appears, left harness inspection is assigned to structural. |
| `p38` | selected, optional | 1.103 | 27 | The aft temperature warning should not be routed to the electrical corrosion queue. |
| `p24` | selected, required | 0.891 | 29 | Dev Rao signs the release sheet after the structural team entry appears. |
| `p09` | selected, required | 1.808 | 30 | Atlas field reports link the aft temperature warning to insulation rubbing the left harness. |
| `p22` | selected, distractor | 1.023 | 30 | The electrical team reviews right-harness corrosion alerts, not left-harness insulation rubs. |
| `p11` | required | -0.041 | 28 | Structural inspections must be logged in the amber maintenance ledger before release. |
| `p39` | required | 0.162 | 28 | Release paperwork is held until the amber ledger contains the structural inspection entry. |
| `p12` | selected, required | 1.547 | 27 | Shift controller Dev Rao reviews the amber maintenance ledger. |
| `p37` | selected, optional | 0.891 | 31 | A clerk may shelve the amber ledger beside fuel records after Dev Rao reviews it. |
| `p36` | selected, required | 1.341 | 30 | A duplicate aft-warning note says cold starts can make insulation rub the left harness. |
| `p29` | distractor | 0.507 | 32 | Cabin panel reviews are logged in the white trim notebook, not the amber ledger. |
| `p30` | - | -0.315 | 28 | Dev Rao is not responsible for catering, hydraulic seal approval, or Orion calibration. |
| `p31` | - | -0.184 | 29 | The ground power team owns the battery health printout process for Atlas staging. |
| `p04` | - | -0.009 | 29 | Cage D opens only after the secure tool room records Mira Patel's approval code. |
| `p01` | - | -0.223 | 27 | The Atlas night support desk moved to Bay 7 after the January ventilation review. |

### PASS content_01_aero_support / q13_three_hop / budget 512

Question: Who reviews the record after the team assigned to the aft warning completes its required log?

Selected: `['p04', 'p09', 'p10', 'p11', 'p12', 'p22', 'p24', 'p28', 'p29', 'p30', 'p31', 'p36', 'p37', 'p38', 'p39']`
Tokens: `436/512`
F1: `0.750` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `['p22', 'p29']`

Score breakdown:

- individual: `10.520`
- pair synergy: `25.623`
- triple synergy: `7.727`
- redundancy penalty: `7.181`
- total: `36.690`

Improvement hint: Add wrong-context or contradiction-aware features; a distractor beat required evidence.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `p10` | selected, required | 2.335 | 29 | When the aft temperature warning appears, left harness inspection is assigned to structural. |
| `p38` | selected, optional | 1.155 | 27 | The aft temperature warning should not be routed to the electrical corrosion queue. |
| `p24` | selected, required | 0.947 | 29 | Dev Rao signs the release sheet after the structural team entry appears. |
| `p09` | selected, required | 1.866 | 30 | Atlas field reports link the aft temperature warning to insulation rubbing the left harness. |
| `p22` | selected, distractor | 1.127 | 30 | The electrical team reviews right-harness corrosion alerts, not left-harness insulation rubs. |
| `p11` | selected, required | 0.014 | 28 | Structural inspections must be logged in the amber maintenance ledger before release. |
| `p39` | selected, required | -0.017 | 28 | Release paperwork is held until the amber ledger contains the structural inspection entry. |
| `p12` | selected, required | 1.600 | 27 | Shift controller Dev Rao reviews the amber maintenance ledger. |
| `p37` | selected, optional | -0.007 | 31 | A clerk may shelve the amber ledger beside fuel records after Dev Rao reviews it. |
| `p36` | selected, required | 1.481 | 30 | A duplicate aft-warning note says cold starts can make insulation rub the left harness. |
| `p29` | selected, distractor | 0.570 | 32 | Cabin panel reviews are logged in the white trim notebook, not the amber ledger. |
| `p30` | selected | -0.264 | 28 | Dev Rao is not responsible for catering, hydraulic seal approval, or Orion calibration. |
| `p31` | selected | -0.145 | 29 | The ground power team owns the battery health printout process for Atlas staging. |
| `p04` | selected | 0.020 | 29 | Cage D opens only after the secure tool room records Mira Patel's approval code. |
| `p28` | selected | -0.162 | 29 | Ground power files Binder Blue after the battery cart is returned. |

### PASS content_01_aero_support / q13_three_hop / budget 1024

Question: Who reviews the record after the team assigned to the aft warning completes its required log?

Selected: `['p04', 'p09', 'p10', 'p11', 'p12', 'p22', 'p24', 'p28', 'p29', 'p30', 'p31', 'p36', 'p37', 'p38', 'p39']`
Tokens: `436/1024`
F1: `0.750` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `['p22', 'p29']`

Score breakdown:

- individual: `10.946`
- pair synergy: `25.623`
- triple synergy: `7.727`
- redundancy penalty: `7.181`
- total: `37.115`

Improvement hint: Add wrong-context or contradiction-aware features; a distractor beat required evidence.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `p10` | selected, required | 2.364 | 29 | When the aft temperature warning appears, left harness inspection is assigned to structural. |
| `p38` | selected, optional | 1.182 | 27 | The aft temperature warning should not be routed to the electrical corrosion queue. |
| `p24` | selected, required | 0.976 | 29 | Dev Rao signs the release sheet after the structural team entry appears. |
| `p09` | selected, required | 1.895 | 30 | Atlas field reports link the aft temperature warning to insulation rubbing the left harness. |
| `p22` | selected, distractor | 1.156 | 30 | The electrical team reviews right-harness corrosion alerts, not left-harness insulation rubs. |
| `p11` | selected, required | 0.041 | 28 | Structural inspections must be logged in the amber maintenance ledger before release. |
| `p39` | selected, required | 0.010 | 28 | Release paperwork is held until the amber ledger contains the structural inspection entry. |
| `p12` | selected, required | 1.626 | 27 | Shift controller Dev Rao reviews the amber maintenance ledger. |
| `p37` | selected, optional | 0.023 | 31 | A clerk may shelve the amber ledger beside fuel records after Dev Rao reviews it. |
| `p36` | selected, required | 1.510 | 30 | A duplicate aft-warning note says cold starts can make insulation rub the left harness. |
| `p29` | selected, distractor | 0.601 | 32 | Cabin panel reviews are logged in the white trim notebook, not the amber ledger. |
| `p30` | selected | -0.237 | 28 | Dev Rao is not responsible for catering, hydraulic seal approval, or Orion calibration. |
| `p31` | selected | -0.116 | 29 | The ground power team owns the battery health printout process for Atlas staging. |
| `p04` | selected | 0.048 | 29 | Cage D opens only after the secure tool room records Mira Patel's approval code. |
| `p28` | selected | -0.134 | 29 | Ground power files Binder Blue after the battery cart is returned. |

### FAIL content_01_aero_support / q14_three_hop / budget 128

Question: Before winter calibration, which binder should be checked for the printout required by Hangar 2 staging?

Selected: `['p06', 'p07', 'p08', 'p19']`
Tokens: `113/128`
F1: `0.857` Required recall: `0.750`
Missing required units: `['start_time']`
Selected distractors: `[]`

Score breakdown:

- individual: `9.727`
- pair synergy: `3.769`
- triple synergy: `0.114`
- redundancy penalty: `1.210`
- total: `12.400`

Improvement hint: Scoring issue; required evidence was available but not valuable enough under current utility.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `p19` | selected, required | 3.211 | 29 | Hangar 2 has limited power during winter calibration, so staging must be early. |
| `p07` | selected, required | 1.944 | 27 | Hangar 2 staging requires the previous evening battery health printout. |
| `p06` | selected, required | 2.708 | 29 | The sensor cart must be staged beside Hangar 2 during winter calibration. |
| `p05` | required | 0.953 | 28 | The winter calibration window begins at 06:30 before the first engine run. |
| `p33` | distractor | 1.215 | 30 | Hangar 3 accepts overnight staging only for paint-shop air filters, not Atlas calibration carts. |
| `p32` | optional | 0.899 | 30 | The rollout coordinator checks that the sensor cart has arrived before calibration begins. |
| `p08` | selected, required | 1.864 | 28 | The previous evening battery health printout is filed in Binder Blue. |
| `p31` | optional | 1.259 | 29 | The ground power team owns the battery health printout process for Atlas staging. |
| `p34` | distractor | 0.156 | 31 | Binder Green contains fueling checklists and does not contain battery health printouts. |
| `p30` | - | 0.024 | 28 | Dev Rao is not responsible for catering, hydraulic seal approval, or Orion calibration. |
| `p17` | distractor | -0.243 | 33 | A contractor guide lists 07:15 as a calibration start time, but it applies to Orion. |
| `p11` | - | -0.210 | 28 | Structural inspections must be logged in the amber maintenance ledger before release. |
| `p38` | - | -0.237 | 27 | The aft temperature warning should not be routed to the electrical corrosion queue. |
| `p28` | required | -0.260 | 29 | Ground power files Binder Blue after the battery cart is returned. |
| `p40` | - | -0.689 | 29 | Urgent replacement requests are marked red before they reach Mira Patel for approval. |

### PASS content_01_aero_support / q14_three_hop / budget 256

Question: Before winter calibration, which binder should be checked for the printout required by Hangar 2 staging?

Selected: `['p05', 'p06', 'p07', 'p08', 'p19', 'p28', 'p31', 'p33', 'p38']`
Tokens: `256/256`
F1: `0.875` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `['p33']`

Score breakdown:

- individual: `13.657`
- pair synergy: `14.559`
- triple synergy: `5.682`
- redundancy penalty: `3.281`
- total: `30.617`

Improvement hint: Add wrong-context or contradiction-aware features; a distractor beat required evidence.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `p19` | selected, required | 3.324 | 29 | Hangar 2 has limited power during winter calibration, so staging must be early. |
| `p07` | selected, required | 2.050 | 27 | Hangar 2 staging requires the previous evening battery health printout. |
| `p06` | selected, required | 2.822 | 29 | The sensor cart must be staged beside Hangar 2 during winter calibration. |
| `p05` | selected, required | 1.062 | 28 | The winter calibration window begins at 06:30 before the first engine run. |
| `p33` | selected, distractor | 1.332 | 30 | Hangar 3 accepts overnight staging only for paint-shop air filters, not Atlas calibration carts. |
| `p32` | optional | 1.016 | 30 | The rollout coordinator checks that the sensor cart has arrived before calibration begins. |
| `p08` | selected, required | 1.973 | 28 | The previous evening battery health printout is filed in Binder Blue. |
| `p31` | selected, optional | 1.372 | 29 | The ground power team owns the battery health printout process for Atlas staging. |
| `p34` | distractor | 0.277 | 31 | Binder Green contains fueling checklists and does not contain battery health printouts. |
| `p30` | - | 0.133 | 28 | Dev Rao is not responsible for catering, hydraulic seal approval, or Orion calibration. |
| `p17` | distractor | -0.115 | 33 | A contractor guide lists 07:15 as a calibration start time, but it applies to Orion. |
| `p11` | - | -0.101 | 28 | Structural inspections must be logged in the amber maintenance ledger before release. |
| `p38` | selected | -0.131 | 27 | The aft temperature warning should not be routed to the electrical corrosion queue. |
| `p28` | selected, required | -0.147 | 29 | Ground power files Binder Blue after the battery cart is returned. |
| `p40` | - | -0.576 | 29 | Urgent replacement requests are marked red before they reach Mira Patel for approval. |

### PASS content_01_aero_support / q14_three_hop / budget 512

Question: Before winter calibration, which binder should be checked for the printout required by Hangar 2 staging?

Selected: `['p05', 'p06', 'p07', 'p08', 'p11', 'p17', 'p19', 'p28', 'p30', 'p31', 'p32', 'p33', 'p34', 'p38', 'p40']`
Tokens: `435/512`
F1: `0.696` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `['p17', 'p33', 'p34']`

Score breakdown:

- individual: `15.142`
- pair synergy: `30.072`
- triple synergy: `23.068`
- redundancy penalty: `5.834`
- total: `62.448`

Improvement hint: Add wrong-context or contradiction-aware features; a distractor beat required evidence.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `p19` | selected, required | 3.381 | 29 | Hangar 2 has limited power during winter calibration, so staging must be early. |
| `p07` | selected, required | 2.103 | 27 | Hangar 2 staging requires the previous evening battery health printout. |
| `p06` | selected, required | 2.878 | 29 | The sensor cart must be staged beside Hangar 2 during winter calibration. |
| `p05` | selected, required | 1.117 | 28 | The winter calibration window begins at 06:30 before the first engine run. |
| `p33` | selected, distractor | 1.391 | 30 | Hangar 3 accepts overnight staging only for paint-shop air filters, not Atlas calibration carts. |
| `p32` | selected, optional | 1.075 | 30 | The rollout coordinator checks that the sensor cart has arrived before calibration begins. |
| `p08` | selected, required | 2.028 | 28 | The previous evening battery health printout is filed in Binder Blue. |
| `p31` | selected, optional | 1.429 | 29 | The ground power team owns the battery health printout process for Atlas staging. |
| `p34` | selected, distractor | 0.338 | 31 | Binder Green contains fueling checklists and does not contain battery health printouts. |
| `p30` | selected | 0.188 | 28 | Dev Rao is not responsible for catering, hydraulic seal approval, or Orion calibration. |
| `p17` | selected, distractor | -0.050 | 33 | A contractor guide lists 07:15 as a calibration start time, but it applies to Orion. |
| `p11` | selected | -0.046 | 28 | Structural inspections must be logged in the amber maintenance ledger before release. |
| `p38` | selected | -0.078 | 27 | The aft temperature warning should not be routed to the electrical corrosion queue. |
| `p28` | selected, required | -0.090 | 29 | Ground power files Binder Blue after the battery cart is returned. |
| `p40` | selected | -0.519 | 29 | Urgent replacement requests are marked red before they reach Mira Patel for approval. |

### PASS content_01_aero_support / q14_three_hop / budget 1024

Question: Before winter calibration, which binder should be checked for the printout required by Hangar 2 staging?

Selected: `['p05', 'p06', 'p07', 'p08', 'p11', 'p17', 'p19', 'p28', 'p30', 'p31', 'p32', 'p33', 'p34', 'p38', 'p40']`
Tokens: `435/1024`
F1: `0.696` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `['p17', 'p33', 'p34']`

Score breakdown:

- individual: `15.567`
- pair synergy: `30.072`
- triple synergy: `23.068`
- redundancy penalty: `5.834`
- total: `62.873`

Improvement hint: Add wrong-context or contradiction-aware features; a distractor beat required evidence.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `p19` | selected, required | 3.409 | 29 | Hangar 2 has limited power during winter calibration, so staging must be early. |
| `p07` | selected, required | 2.129 | 27 | Hangar 2 staging requires the previous evening battery health printout. |
| `p06` | selected, required | 2.907 | 29 | The sensor cart must be staged beside Hangar 2 during winter calibration. |
| `p05` | selected, required | 1.144 | 28 | The winter calibration window begins at 06:30 before the first engine run. |
| `p33` | selected, distractor | 1.420 | 30 | Hangar 3 accepts overnight staging only for paint-shop air filters, not Atlas calibration carts. |
| `p32` | selected, optional | 1.104 | 30 | The rollout coordinator checks that the sensor cart has arrived before calibration begins. |
| `p08` | selected, required | 2.055 | 28 | The previous evening battery health printout is filed in Binder Blue. |
| `p31` | selected, optional | 1.457 | 29 | The ground power team owns the battery health printout process for Atlas staging. |
| `p34` | selected, distractor | 0.368 | 31 | Binder Green contains fueling checklists and does not contain battery health printouts. |
| `p30` | selected | 0.215 | 28 | Dev Rao is not responsible for catering, hydraulic seal approval, or Orion calibration. |
| `p17` | selected, distractor | -0.018 | 33 | A contractor guide lists 07:15 as a calibration start time, but it applies to Orion. |
| `p11` | selected | -0.019 | 28 | Structural inspections must be logged in the amber maintenance ledger before release. |
| `p38` | selected | -0.052 | 27 | The aft temperature warning should not be routed to the electrical corrosion queue. |
| `p28` | selected, required | -0.062 | 29 | Ground power files Binder Blue after the battery cart is returned. |
| `p40` | selected | -0.491 | 29 | Urgent replacement requests are marked red before they reach Mira Patel for approval. |

### FAIL content_01_aero_support / q15_three_hop / budget 128

Question: Who signs off after the structural team handles the aft temperature warning workflow?

Selected: `['p09', 'p10', 'p24', 'p38']`
Tokens: `115/128`
F1: `0.857` Required recall: `0.750`
Missing required units: `['log']`
Selected distractors: `[]`

Score breakdown:

- individual: `8.209`
- pair synergy: `3.678`
- triple synergy: `0.000`
- redundancy penalty: `1.077`
- total: `10.809`

Improvement hint: Scoring issue; required evidence was available but not valuable enough under current utility.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `p10` | selected, required | 2.794 | 29 | When the aft temperature warning appears, left harness inspection is assigned to structural. |
| `p24` | selected, required | 1.546 | 29 | Dev Rao signs the release sheet after the structural team entry appears. |
| `p38` | selected, optional | 1.593 | 27 | The aft temperature warning should not be routed to the electrical corrosion queue. |
| `p09` | selected, required | 2.275 | 30 | Atlas field reports link the aft temperature warning to insulation rubbing the left harness. |
| `p36` | required | 1.439 | 30 | A duplicate aft-warning note says cold starts can make insulation rub the left harness. |
| `p11` | required | 0.217 | 28 | Structural inspections must be logged in the amber maintenance ledger before release. |
| `p39` | required | 0.439 | 28 | Release paperwork is held until the amber ledger contains the structural inspection entry. |
| `p22` | distractor | 0.562 | 30 | The electrical team reviews right-harness corrosion alerts, not left-harness insulation rubs. |
| `p37` | - | 0.277 | 31 | A clerk may shelve the amber ledger beside fuel records after Dev Rao reviews it. |
| `p12` | optional | -0.236 | 27 | Shift controller Dev Rao reviews the amber maintenance ledger. |
| `p29` | distractor | -0.759 | 32 | Cabin panel reviews are logged in the white trim notebook, not the amber ledger. |
| `p31` | - | -0.244 | 29 | The ground power team owns the battery health printout process for Atlas staging. |
| `p01` | - | -0.259 | 27 | The Atlas night support desk moved to Bay 7 after the January ventilation review. |
| `p28` | - | -0.298 | 29 | Ground power files Binder Blue after the battery cart is returned. |
| `p04` | - | -0.298 | 29 | Cage D opens only after the secure tool room records Mira Patel's approval code. |

### PASS content_01_aero_support / q15_three_hop / budget 256

Question: Who signs off after the structural team handles the aft temperature warning workflow?

Selected: `['p09', 'p10', 'p22', 'p24', 'p36', 'p37', 'p38', 'p39']`
Tokens: `234/256`
F1: `0.857` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `['p22']`

Score breakdown:

- individual: `11.841`
- pair synergy: `11.344`
- triple synergy: `1.375`
- redundancy penalty: `3.300`
- total: `21.260`

Improvement hint: Add wrong-context or contradiction-aware features; a distractor beat required evidence.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `p10` | selected, required | 2.908 | 29 | When the aft temperature warning appears, left harness inspection is assigned to structural. |
| `p24` | selected, required | 1.659 | 29 | Dev Rao signs the release sheet after the structural team entry appears. |
| `p38` | selected, optional | 1.698 | 27 | The aft temperature warning should not be routed to the electrical corrosion queue. |
| `p09` | selected, required | 2.393 | 30 | Atlas field reports link the aft temperature warning to insulation rubbing the left harness. |
| `p36` | selected, required | 1.557 | 30 | A duplicate aft-warning note says cold starts can make insulation rub the left harness. |
| `p11` | required | 0.326 | 28 | Structural inspections must be logged in the amber maintenance ledger before release. |
| `p39` | selected, required | 0.548 | 28 | Release paperwork is held until the amber ledger contains the structural inspection entry. |
| `p22` | selected, distractor | 0.680 | 30 | The electrical team reviews right-harness corrosion alerts, not left-harness insulation rubs. |
| `p37` | selected | 0.398 | 31 | A clerk may shelve the amber ledger beside fuel records after Dev Rao reviews it. |
| `p12` | optional | -0.130 | 27 | Shift controller Dev Rao reviews the amber maintenance ledger. |
| `p29` | distractor | -0.634 | 32 | Cabin panel reviews are logged in the white trim notebook, not the amber ledger. |
| `p31` | - | -0.131 | 29 | The ground power team owns the battery health printout process for Atlas staging. |
| `p01` | - | -0.154 | 27 | The Atlas night support desk moved to Bay 7 after the January ventilation review. |
| `p28` | - | -0.185 | 29 | Ground power files Binder Blue after the battery cart is returned. |
| `p04` | - | -0.185 | 29 | Cage D opens only after the secure tool room records Mira Patel's approval code. |

### PASS content_01_aero_support / q15_three_hop / budget 512

Question: Who signs off after the structural team handles the aft temperature warning workflow?

Selected: `['p01', 'p04', 'p09', 'p10', 'p11', 'p12', 'p22', 'p24', 'p28', 'p29', 'p31', 'p36', 'p37', 'p38', 'p39']`
Tokens: `435/512`
F1: `0.696` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `['p22', 'p29']`

Score breakdown:

- individual: `11.598`
- pair synergy: `26.294`
- triple synergy: `10.500`
- redundancy penalty: `6.900`
- total: `41.492`

Improvement hint: Add wrong-context or contradiction-aware features; a distractor beat required evidence.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `p10` | selected, required | 2.964 | 29 | When the aft temperature warning appears, left harness inspection is assigned to structural. |
| `p24` | selected, required | 1.716 | 29 | Dev Rao signs the release sheet after the structural team entry appears. |
| `p38` | selected, optional | 1.751 | 27 | The aft temperature warning should not be routed to the electrical corrosion queue. |
| `p09` | selected, required | 2.451 | 30 | Atlas field reports link the aft temperature warning to insulation rubbing the left harness. |
| `p36` | selected, required | 1.615 | 30 | A duplicate aft-warning note says cold starts can make insulation rub the left harness. |
| `p11` | selected, required | 0.381 | 28 | Structural inspections must be logged in the amber maintenance ledger before release. |
| `p39` | selected, required | 0.603 | 28 | Release paperwork is held until the amber ledger contains the structural inspection entry. |
| `p22` | selected, distractor | 0.738 | 30 | The electrical team reviews right-harness corrosion alerts, not left-harness insulation rubs. |
| `p37` | selected | 0.459 | 31 | A clerk may shelve the amber ledger beside fuel records after Dev Rao reviews it. |
| `p12` | selected, optional | -0.078 | 27 | Shift controller Dev Rao reviews the amber maintenance ledger. |
| `p29` | selected, distractor | -0.572 | 32 | Cabin panel reviews are logged in the white trim notebook, not the amber ledger. |
| `p31` | selected | -0.074 | 29 | The ground power team owns the battery health printout process for Atlas staging. |
| `p01` | selected | -0.101 | 27 | The Atlas night support desk moved to Bay 7 after the January ventilation review. |
| `p28` | selected | -0.128 | 29 | Ground power files Binder Blue after the battery cart is returned. |
| `p04` | selected | -0.128 | 29 | Cage D opens only after the secure tool room records Mira Patel's approval code. |

### PASS content_01_aero_support / q15_three_hop / budget 1024

Question: Who signs off after the structural team handles the aft temperature warning workflow?

Selected: `['p01', 'p04', 'p09', 'p10', 'p11', 'p12', 'p22', 'p24', 'p28', 'p29', 'p31', 'p36', 'p37', 'p38', 'p39']`
Tokens: `435/1024`
F1: `0.696` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `['p22', 'p29']`

Score breakdown:

- individual: `12.023`
- pair synergy: `26.294`
- triple synergy: `10.500`
- redundancy penalty: `6.900`
- total: `41.917`

Improvement hint: Add wrong-context or contradiction-aware features; a distractor beat required evidence.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `p10` | selected, required | 2.993 | 29 | When the aft temperature warning appears, left harness inspection is assigned to structural. |
| `p24` | selected, required | 1.744 | 29 | Dev Rao signs the release sheet after the structural team entry appears. |
| `p38` | selected, optional | 1.777 | 27 | The aft temperature warning should not be routed to the electrical corrosion queue. |
| `p09` | selected, required | 2.481 | 30 | Atlas field reports link the aft temperature warning to insulation rubbing the left harness. |
| `p36` | selected, required | 1.645 | 30 | A duplicate aft-warning note says cold starts can make insulation rub the left harness. |
| `p11` | selected, required | 0.408 | 28 | Structural inspections must be logged in the amber maintenance ledger before release. |
| `p39` | selected, required | 0.631 | 28 | Release paperwork is held until the amber ledger contains the structural inspection entry. |
| `p22` | selected, distractor | 0.768 | 30 | The electrical team reviews right-harness corrosion alerts, not left-harness insulation rubs. |
| `p37` | selected | 0.489 | 31 | A clerk may shelve the amber ledger beside fuel records after Dev Rao reviews it. |
| `p12` | selected, optional | -0.051 | 27 | Shift controller Dev Rao reviews the amber maintenance ledger. |
| `p29` | selected, distractor | -0.541 | 32 | Cabin panel reviews are logged in the white trim notebook, not the amber ledger. |
| `p31` | selected | -0.046 | 29 | The ground power team owns the battery health printout process for Atlas staging. |
| `p01` | selected | -0.074 | 27 | The Atlas night support desk moved to Bay 7 after the January ventilation review. |
| `p28` | selected | -0.100 | 29 | Ground power files Binder Blue after the battery cart is returned. |
| `p04` | selected | -0.100 | 29 | Cage D opens only after the secure tool room records Mira Patel's approval code. |

### FAIL content_02_clinic_access / c_q01_direct / budget 128

Question: Where should a visiting student fix a badge denial?

Selected: `['c04', 'c13', 'c16', 'c24']`
Tokens: `119/128`
F1: `0.000` Required recall: `0.000`
Missing required units: `['student_access', 'annex_alias']`
Selected distractors: `['c04']`

Score breakdown:

- individual: `4.309`
- pair synergy: `1.468`
- triple synergy: `0.000`
- redundancy penalty: `0.506`
- total: `5.271`

Improvement hint: Add wrong-context or contradiction-aware features; a distractor beat required evidence.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `c04` | selected, distractor | 2.661 | 31 | A badge denial for visiting students should be fixed at reception by the visitor badge desk. |
| `c24` | selected | 1.096 | 30 | Expired wristband replacement points to the security map label after a badge denial. |
| `c16` | selected | 0.263 | 31 | Slate courier envelopes before night audit should be signed at the blood desk. |
| `c01` | required | -0.594 | 27 | Blue-lanyard observers receive a temporary pass from the learning office, not from reception. |
| `c05` | - | -0.723 | 27 | The sedation cabinet releases keys after the orange ledger is initialed. |
| `c03` | optional | -0.132 | 28 | Reception prints visitor badges only for family members and vendors. |
| `c36` | - | -0.640 | 31 | Bronze chart stickers are cleared by the triage physician before insurance review. |
| `c08` | - | -1.060 | 30 | Sedation cabinet keys are approved by pharmacy when the orange ledger is missing. |
| `c33` | - | -0.990 | 28 | The bronze sticker on a chart means insurance review is pending. |
| `c15` | - | 0.303 | 31 | The archive cart is signed out by Omar Singh before the night audit. |
| `c13` | selected | 0.288 | 27 | Courier envelopes marked slate are routed to diagnostic imaging. |
| `c06` | - | -1.064 | 28 | Orange ledger initials are supplied by the recovery charge nurse. |
| `c02` | required | -1.032 | 29 | The learning office is called the North Annex counter in weekend notes. |
| `c21` | - | -0.327 | 27 | Expired wristbands are replaced at the intake island. |
| `c35` | - | -1.107 | 30 | Mateo Ruiz works from the small office behind registration. |

### FAIL content_02_clinic_access / c_q01_direct / budget 256

Question: Where should a visiting student fix a badge denial?

Selected: `['c03', 'c04', 'c13', 'c15', 'c16', 'c24']`
Tokens: `178/256`
F1: `0.000` Required recall: `0.000`
Missing required units: `['student_access', 'annex_alias']`
Selected distractors: `['c04']`

Score breakdown:

- individual: `5.175`
- pair synergy: `2.371`
- triple synergy: `0.000`
- redundancy penalty: `0.956`
- total: `6.590`

Improvement hint: Add wrong-context or contradiction-aware features; a distractor beat required evidence.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `c04` | selected, distractor | 2.783 | 31 | A badge denial for visiting students should be fixed at reception by the visitor badge desk. |
| `c24` | selected | 1.213 | 30 | Expired wristband replacement points to the security map label after a badge denial. |
| `c16` | selected | 0.385 | 31 | Slate courier envelopes before night audit should be signed at the blood desk. |
| `c01` | required | -0.489 | 27 | Blue-lanyard observers receive a temporary pass from the learning office, not from reception. |
| `c05` | - | -0.618 | 27 | The sedation cabinet releases keys after the orange ledger is initialed. |
| `c03` | selected, optional | -0.023 | 28 | Reception prints visitor badges only for family members and vendors. |
| `c36` | - | -0.519 | 31 | Bronze chart stickers are cleared by the triage physician before insurance review. |
| `c08` | - | -0.942 | 30 | Sedation cabinet keys are approved by pharmacy when the orange ledger is missing. |
| `c33` | - | -0.880 | 28 | The bronze sticker on a chart means insurance review is pending. |
| `c15` | selected | 0.424 | 31 | The archive cart is signed out by Omar Singh before the night audit. |
| `c13` | selected | 0.394 | 27 | Courier envelopes marked slate are routed to diagnostic imaging. |
| `c06` | - | -0.955 | 28 | Orange ledger initials are supplied by the recovery charge nurse. |
| `c02` | required | -0.918 | 29 | The learning office is called the North Annex counter in weekend notes. |
| `c21` | - | -0.221 | 27 | Expired wristbands are replaced at the intake island. |
| `c35` | - | -0.990 | 30 | Mateo Ruiz works from the small office behind registration. |

### FAIL content_02_clinic_access / c_q01_direct / budget 512

Question: Where should a visiting student fix a badge denial?

Selected: `['c03', 'c04', 'c13', 'c15', 'c16', 'c21', 'c24']`
Tokens: `205/512`
F1: `0.000` Required recall: `0.000`
Missing required units: `['student_access', 'annex_alias']`
Selected distractors: `['c04']`

Score breakdown:

- individual: `5.354`
- pair synergy: `2.631`
- triple synergy: `0.000`
- redundancy penalty: `1.036`
- total: `6.949`

Improvement hint: Add wrong-context or contradiction-aware features; a distractor beat required evidence.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `c04` | selected, distractor | 2.843 | 31 | A badge denial for visiting students should be fixed at reception by the visitor badge desk. |
| `c24` | selected | 1.272 | 30 | Expired wristband replacement points to the security map label after a badge denial. |
| `c16` | selected | 0.445 | 31 | Slate courier envelopes before night audit should be signed at the blood desk. |
| `c01` | required | -0.436 | 27 | Blue-lanyard observers receive a temporary pass from the learning office, not from reception. |
| `c05` | - | -0.565 | 27 | The sedation cabinet releases keys after the orange ledger is initialed. |
| `c03` | selected, optional | 0.032 | 28 | Reception prints visitor badges only for family members and vendors. |
| `c36` | - | -0.458 | 31 | Bronze chart stickers are cleared by the triage physician before insurance review. |
| `c08` | - | -0.884 | 30 | Sedation cabinet keys are approved by pharmacy when the orange ledger is missing. |
| `c33` | - | -0.826 | 28 | The bronze sticker on a chart means insurance review is pending. |
| `c15` | selected | 0.485 | 31 | The archive cart is signed out by Omar Singh before the night audit. |
| `c13` | selected | 0.446 | 27 | Courier envelopes marked slate are routed to diagnostic imaging. |
| `c06` | - | -0.900 | 28 | Orange ledger initials are supplied by the recovery charge nurse. |
| `c02` | required | -0.862 | 29 | The learning office is called the North Annex counter in weekend notes. |
| `c21` | selected | -0.169 | 27 | Expired wristbands are replaced at the intake island. |
| `c35` | - | -0.931 | 30 | Mateo Ruiz works from the small office behind registration. |

### FAIL content_02_clinic_access / c_q01_direct / budget 1024

Question: Where should a visiting student fix a badge denial?

Selected: `['c03', 'c04', 'c13', 'c15', 'c16', 'c21', 'c24']`
Tokens: `205/1024`
F1: `0.000` Required recall: `0.000`
Missing required units: `['student_access', 'annex_alias']`
Selected distractors: `['c04']`

Score breakdown:

- individual: `5.554`
- pair synergy: `2.631`
- triple synergy: `0.000`
- redundancy penalty: `1.036`
- total: `7.149`

Improvement hint: Add wrong-context or contradiction-aware features; a distractor beat required evidence.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `c04` | selected, distractor | 2.873 | 31 | A badge denial for visiting students should be fixed at reception by the visitor badge desk. |
| `c24` | selected | 1.301 | 30 | Expired wristband replacement points to the security map label after a badge denial. |
| `c16` | selected | 0.475 | 31 | Slate courier envelopes before night audit should be signed at the blood desk. |
| `c01` | required | -0.409 | 27 | Blue-lanyard observers receive a temporary pass from the learning office, not from reception. |
| `c05` | - | -0.539 | 27 | The sedation cabinet releases keys after the orange ledger is initialed. |
| `c03` | selected, optional | 0.059 | 28 | Reception prints visitor badges only for family members and vendors. |
| `c36` | - | -0.428 | 31 | Bronze chart stickers are cleared by the triage physician before insurance review. |
| `c08` | - | -0.855 | 30 | Sedation cabinet keys are approved by pharmacy when the orange ledger is missing. |
| `c33` | - | -0.798 | 28 | The bronze sticker on a chart means insurance review is pending. |
| `c15` | selected | 0.515 | 31 | The archive cart is signed out by Omar Singh before the night audit. |
| `c13` | selected | 0.473 | 27 | Courier envelopes marked slate are routed to diagnostic imaging. |
| `c06` | - | -0.873 | 28 | Orange ledger initials are supplied by the recovery charge nurse. |
| `c02` | required | -0.833 | 29 | The learning office is called the North Annex counter in weekend notes. |
| `c21` | selected | -0.142 | 27 | Expired wristbands are replaced at the intake island. |
| `c35` | - | -0.902 | 30 | Mateo Ruiz works from the small office behind registration. |

### PASS content_02_clinic_access / c_q02_direct / budget 128

Question: Who initials access for the sedation cabinet keys?

Selected: `['c05', 'c06', 'c08', 'c23']`
Tokens: `115/128`
F1: `0.667` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `['c08']`

Score breakdown:

- individual: `7.470`
- pair synergy: `3.555`
- triple synergy: `0.500`
- redundancy penalty: `1.094`
- total: `10.431`

Improvement hint: Add wrong-context or contradiction-aware features; a distractor beat required evidence.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `c05` | selected, required | 3.541 | 27 | The sedation cabinet releases keys after the orange ledger is initialed. |
| `c08` | selected, distractor | 3.502 | 30 | Sedation cabinet keys are approved by pharmacy when the orange ledger is missing. |
| `c06` | selected, required | 0.742 | 28 | Orange ledger initials are supplied by the recovery charge nurse. |
| `c23` | selected | -0.314 | 30 | Coral map labels are maintained by facilities, not by the access team. |
| `c01` | - | -0.612 | 27 | Blue-lanyard observers receive a temporary pass from the learning office, not from reception. |
| `c28` | - | -0.973 | 31 | Silver consent telehealth follow-up slots open through in-person surgery clearance. |
| `c26` | - | -0.992 | 30 | Telehealth follow-up slots are opened by the remote-care scheduler. |
| `c25` | - | -0.997 | 28 | The silver consent sleeve indicates telehealth follow-up. |
| `c22` | - | 0.012 | 29 | The intake island is labeled Coral on the floor map. |
| `c27` | - | -0.676 | 29 | Remote-care scheduling uses the amber queue after noon. |
| `c02` | - | -1.009 | 29 | The learning office is called the North Annex counter in weekend notes. |
| `c35` | - | -1.064 | 30 | Mateo Ruiz works from the small office behind registration. |
| `c07` | optional | -0.573 | 29 | Pharmacy keeps a separate green narcotics book for medication counts. |
| `c12` | - | -0.704 | 31 | The quiet room after evening overflow is handled by the triage nurse for pediatric fever cases. |
| `c24` | - | -0.665 | 30 | Expired wristband replacement points to the security map label after a badge denial. |

### PASS content_02_clinic_access / c_q02_direct / budget 256

Question: Who initials access for the sedation cabinet keys?

Selected: `['c05', 'c06', 'c08', 'c22', 'c23']`
Tokens: `144/256`
F1: `0.571` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `['c08']`

Score breakdown:

- individual: `8.044`
- pair synergy: `3.989`
- triple synergy: `0.500`
- redundancy penalty: `1.281`
- total: `11.252`

Improvement hint: Add wrong-context or contradiction-aware features; a distractor beat required evidence.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `c05` | selected, required | 3.646 | 27 | The sedation cabinet releases keys after the orange ledger is initialed. |
| `c08` | selected, distractor | 3.619 | 30 | Sedation cabinet keys are approved by pharmacy when the orange ledger is missing. |
| `c06` | selected, required | 0.851 | 28 | Orange ledger initials are supplied by the recovery charge nurse. |
| `c23` | selected | -0.197 | 30 | Coral map labels are maintained by facilities, not by the access team. |
| `c01` | - | -0.506 | 27 | Blue-lanyard observers receive a temporary pass from the learning office, not from reception. |
| `c28` | - | -0.852 | 31 | Silver consent telehealth follow-up slots open through in-person surgery clearance. |
| `c26` | - | -0.875 | 30 | Telehealth follow-up slots are opened by the remote-care scheduler. |
| `c25` | - | -0.888 | 28 | The silver consent sleeve indicates telehealth follow-up. |
| `c22` | selected | 0.126 | 29 | The intake island is labeled Coral on the floor map. |
| `c27` | - | -0.562 | 29 | Remote-care scheduling uses the amber queue after noon. |
| `c02` | - | -0.895 | 29 | The learning office is called the North Annex counter in weekend notes. |
| `c35` | - | -0.946 | 30 | Mateo Ruiz works from the small office behind registration. |
| `c07` | optional | -0.460 | 29 | Pharmacy keeps a separate green narcotics book for medication counts. |
| `c12` | - | -0.583 | 31 | The quiet room after evening overflow is handled by the triage nurse for pediatric fever cases. |
| `c24` | - | -0.548 | 30 | Expired wristband replacement points to the security map label after a badge denial. |

### PASS content_02_clinic_access / c_q02_direct / budget 512

Question: Who initials access for the sedation cabinet keys?

Selected: `['c05', 'c06', 'c08', 'c22', 'c23']`
Tokens: `144/512`
F1: `0.571` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `['c08']`

Score breakdown:

- individual: `8.326`
- pair synergy: `3.989`
- triple synergy: `0.500`
- redundancy penalty: `1.281`
- total: `11.533`

Improvement hint: Add wrong-context or contradiction-aware features; a distractor beat required evidence.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `c05` | selected, required | 3.699 | 27 | The sedation cabinet releases keys after the orange ledger is initialed. |
| `c08` | selected, distractor | 3.677 | 30 | Sedation cabinet keys are approved by pharmacy when the orange ledger is missing. |
| `c06` | selected, required | 0.906 | 28 | Orange ledger initials are supplied by the recovery charge nurse. |
| `c23` | selected | -0.139 | 30 | Coral map labels are maintained by facilities, not by the access team. |
| `c01` | - | -0.453 | 27 | Blue-lanyard observers receive a temporary pass from the learning office, not from reception. |
| `c28` | - | -0.791 | 31 | Silver consent telehealth follow-up slots open through in-person surgery clearance. |
| `c26` | - | -0.816 | 30 | Telehealth follow-up slots are opened by the remote-care scheduler. |
| `c25` | - | -0.833 | 28 | The silver consent sleeve indicates telehealth follow-up. |
| `c22` | selected | 0.182 | 29 | The intake island is labeled Coral on the floor map. |
| `c27` | - | -0.506 | 29 | Remote-care scheduling uses the amber queue after noon. |
| `c02` | - | -0.839 | 29 | The learning office is called the North Annex counter in weekend notes. |
| `c35` | - | -0.888 | 30 | Mateo Ruiz works from the small office behind registration. |
| `c07` | optional | -0.403 | 29 | Pharmacy keeps a separate green narcotics book for medication counts. |
| `c12` | - | -0.522 | 31 | The quiet room after evening overflow is handled by the triage nurse for pediatric fever cases. |
| `c24` | - | -0.489 | 30 | Expired wristband replacement points to the security map label after a badge denial. |

### PASS content_02_clinic_access / c_q02_direct / budget 1024

Question: Who initials access for the sedation cabinet keys?

Selected: `['c05', 'c06', 'c08', 'c22', 'c23']`
Tokens: `144/1024`
F1: `0.571` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `['c08']`

Score breakdown:

- individual: `8.466`
- pair synergy: `3.989`
- triple synergy: `0.500`
- redundancy penalty: `1.281`
- total: `11.673`

Improvement hint: Add wrong-context or contradiction-aware features; a distractor beat required evidence.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `c05` | selected, required | 3.725 | 27 | The sedation cabinet releases keys after the orange ledger is initialed. |
| `c08` | selected, distractor | 3.707 | 30 | Sedation cabinet keys are approved by pharmacy when the orange ledger is missing. |
| `c06` | selected, required | 0.933 | 28 | Orange ledger initials are supplied by the recovery charge nurse. |
| `c23` | selected | -0.109 | 30 | Coral map labels are maintained by facilities, not by the access team. |
| `c01` | - | -0.427 | 27 | Blue-lanyard observers receive a temporary pass from the learning office, not from reception. |
| `c28` | - | -0.761 | 31 | Silver consent telehealth follow-up slots open through in-person surgery clearance. |
| `c26` | - | -0.787 | 30 | Telehealth follow-up slots are opened by the remote-care scheduler. |
| `c25` | - | -0.806 | 28 | The silver consent sleeve indicates telehealth follow-up. |
| `c22` | selected | 0.211 | 29 | The intake island is labeled Coral on the floor map. |
| `c27` | - | -0.477 | 29 | Remote-care scheduling uses the amber queue after noon. |
| `c02` | - | -0.810 | 29 | The learning office is called the North Annex counter in weekend notes. |
| `c35` | - | -0.859 | 30 | Mateo Ruiz works from the small office behind registration. |
| `c07` | optional | -0.375 | 29 | Pharmacy keeps a separate green narcotics book for medication counts. |
| `c12` | - | -0.492 | 31 | The quiet room after evening overflow is handled by the triage nurse for pediatric fever cases. |
| `c24` | - | -0.460 | 30 | Expired wristband replacement points to the security map label after a badge denial. |

### PASS content_02_clinic_access / c_q03_direct / budget 128

Question: Who handles the quiet room after evening overflow begins?

Selected: `['c09', 'c10', 'c11', 'c12']`
Tokens: `118/128`
F1: `1.000` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `[]`

Score breakdown:

- individual: `5.898`
- pair synergy: `2.446`
- triple synergy: `0.000`
- redundancy penalty: `0.678`
- total: `7.666`

Improvement hint: Successful selection; inspect extra chunks only if precision or token cost becomes the priority.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `c12` | selected, optional | 2.951 | 31 | The quiet room after evening overflow is handled by the triage nurse for pediatric fever cases. |
| `c09` | selected, required | 1.180 | 28 | The quiet room uses a dove marker on the scheduling board. |
| `c11` | selected, required | 0.912 | 30 | Behavioral-health overflow is coordinated by Lina Park after 18:00. |
| `c05` | - | -0.109 | 27 | The sedation cabinet releases keys after the orange ledger is initialed. |
| `c10` | selected, required | 0.856 | 29 | Dove markers are assigned to behavioral-health overflow patients. |
| `c19` | - | -0.943 | 31 | The mobility coordinator sits beside the west stairwell during afternoon rounds. |
| `c27` | - | 0.485 | 29 | Remote-care scheduling uses the amber queue after noon. |
| `c08` | - | -1.134 | 30 | Sedation cabinet keys are approved by pharmacy when the orange ledger is missing. |
| `c18` | - | -1.082 | 29 | Transport paperwork is completed by the mobility coordinator. |
| `c39` | - | 0.003 | 29 | Cultural services keeps evening interpreters on the violet roster. |
| `c30` | - | -0.131 | 29 | Microbiology batches after-hours samples under code M-14. |
| `c26` | - | -0.176 | 30 | Telehealth follow-up slots are opened by the remote-care scheduler. |
| `c06` | - | -0.706 | 28 | Orange ledger initials are supplied by the recovery charge nurse. |
| `c24` | - | -0.230 | 30 | Expired wristband replacement points to the security map label after a badge denial. |
| `c32` | - | -1.046 | 30 | Lavender tray tags mean samples go to radiology during downtime. |

### PASS content_02_clinic_access / c_q03_direct / budget 256

Question: Who handles the quiet room after evening overflow begins?

Selected: `['c05', 'c09', 'c10', 'c11', 'c12', 'c27', 'c30', 'c39']`
Tokens: `232/256`
F1: `0.667` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `[]`

Score breakdown:

- individual: `7.052`
- pair synergy: `7.858`
- triple synergy: `1.964`
- redundancy penalty: `1.524`
- total: `15.351`

Improvement hint: Successful selection; inspect extra chunks only if precision or token cost becomes the priority.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `c12` | selected, optional | 3.072 | 31 | The quiet room after evening overflow is handled by the triage nurse for pediatric fever cases. |
| `c09` | selected, required | 1.289 | 28 | The quiet room uses a dove marker on the scheduling board. |
| `c11` | selected, required | 1.029 | 30 | Behavioral-health overflow is coordinated by Lina Park after 18:00. |
| `c05` | selected | -0.004 | 27 | The sedation cabinet releases keys after the orange ledger is initialed. |
| `c10` | selected, required | 0.970 | 29 | Dove markers are assigned to behavioral-health overflow patients. |
| `c19` | - | -0.822 | 31 | The mobility coordinator sits beside the west stairwell during afternoon rounds. |
| `c27` | selected | 0.598 | 29 | Remote-care scheduling uses the amber queue after noon. |
| `c08` | - | -1.017 | 30 | Sedation cabinet keys are approved by pharmacy when the orange ledger is missing. |
| `c18` | - | -0.969 | 29 | Transport paperwork is completed by the mobility coordinator. |
| `c39` | selected | 0.116 | 29 | Cultural services keeps evening interpreters on the violet roster. |
| `c30` | selected | -0.018 | 29 | Microbiology batches after-hours samples under code M-14. |
| `c26` | - | -0.059 | 30 | Telehealth follow-up slots are opened by the remote-care scheduler. |
| `c06` | - | -0.597 | 28 | Orange ledger initials are supplied by the recovery charge nurse. |
| `c24` | - | -0.113 | 30 | Expired wristband replacement points to the security map label after a badge denial. |
| `c32` | - | -0.929 | 30 | Lavender tray tags mean samples go to radiology during downtime. |

### PASS content_02_clinic_access / c_q03_direct / budget 512

Question: Who handles the quiet room after evening overflow begins?

Selected: `['c05', 'c09', 'c10', 'c11', 'c12', 'c24', 'c26', 'c27', 'c30', 'c39']`
Tokens: `292/512`
F1: `0.571` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `[]`

Score breakdown:

- individual: `7.451`
- pair synergy: `9.784`
- triple synergy: `2.500`
- redundancy penalty: `1.998`
- total: `17.737`

Improvement hint: Successful selection; inspect extra chunks only if precision or token cost becomes the priority.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `c12` | selected, optional | 3.132 | 31 | The quiet room after evening overflow is handled by the triage nurse for pediatric fever cases. |
| `c09` | selected, required | 1.344 | 28 | The quiet room uses a dove marker on the scheduling board. |
| `c11` | selected, required | 1.087 | 30 | Behavioral-health overflow is coordinated by Lina Park after 18:00. |
| `c05` | selected | 0.049 | 27 | The sedation cabinet releases keys after the orange ledger is initialed. |
| `c10` | selected, required | 1.026 | 29 | Dove markers are assigned to behavioral-health overflow patients. |
| `c19` | - | -0.761 | 31 | The mobility coordinator sits beside the west stairwell during afternoon rounds. |
| `c27` | selected | 0.655 | 29 | Remote-care scheduling uses the amber queue after noon. |
| `c08` | - | -0.959 | 30 | Sedation cabinet keys are approved by pharmacy when the orange ledger is missing. |
| `c18` | - | -0.912 | 29 | Transport paperwork is completed by the mobility coordinator. |
| `c39` | selected | 0.173 | 29 | Cultural services keeps evening interpreters on the violet roster. |
| `c30` | selected | 0.039 | 29 | Microbiology batches after-hours samples under code M-14. |
| `c26` | selected | -0.000 | 30 | Telehealth follow-up slots are opened by the remote-care scheduler. |
| `c06` | - | -0.542 | 28 | Orange ledger initials are supplied by the recovery charge nurse. |
| `c24` | selected | -0.054 | 30 | Expired wristband replacement points to the security map label after a badge denial. |
| `c32` | - | -0.870 | 30 | Lavender tray tags mean samples go to radiology during downtime. |

### PASS content_02_clinic_access / c_q03_direct / budget 1024

Question: Who handles the quiet room after evening overflow begins?

Selected: `['c05', 'c09', 'c10', 'c11', 'c12', 'c24', 'c26', 'c27', 'c30', 'c39']`
Tokens: `292/1024`
F1: `0.571` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `[]`

Score breakdown:

- individual: `7.736`
- pair synergy: `9.784`
- triple synergy: `2.500`
- redundancy penalty: `1.998`
- total: `18.022`

Improvement hint: Successful selection; inspect extra chunks only if precision or token cost becomes the priority.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `c12` | selected, optional | 3.163 | 31 | The quiet room after evening overflow is handled by the triage nurse for pediatric fever cases. |
| `c09` | selected, required | 1.371 | 28 | The quiet room uses a dove marker on the scheduling board. |
| `c11` | selected, required | 1.117 | 30 | Behavioral-health overflow is coordinated by Lina Park after 18:00. |
| `c05` | selected | 0.075 | 27 | The sedation cabinet releases keys after the orange ledger is initialed. |
| `c10` | selected, required | 1.055 | 29 | Dove markers are assigned to behavioral-health overflow patients. |
| `c19` | - | -0.731 | 31 | The mobility coordinator sits beside the west stairwell during afternoon rounds. |
| `c27` | selected | 0.683 | 29 | Remote-care scheduling uses the amber queue after noon. |
| `c08` | - | -0.929 | 30 | Sedation cabinet keys are approved by pharmacy when the orange ledger is missing. |
| `c18` | - | -0.884 | 29 | Transport paperwork is completed by the mobility coordinator. |
| `c39` | selected | 0.201 | 29 | Cultural services keeps evening interpreters on the violet roster. |
| `c30` | selected | 0.067 | 29 | Microbiology batches after-hours samples under code M-14. |
| `c26` | selected | 0.029 | 30 | Telehealth follow-up slots are opened by the remote-care scheduler. |
| `c06` | - | -0.515 | 28 | Orange ledger initials are supplied by the recovery charge nurse. |
| `c24` | selected | -0.025 | 30 | Expired wristband replacement points to the security map label after a badge denial. |
| `c32` | - | -0.841 | 30 | Lavender tray tags mean samples go to radiology during downtime. |

### PASS content_02_clinic_access / c_q04_direct / budget 128

Question: Who signs out the cart for slate courier envelopes?

Selected: `['c13', 'c14', 'c15', 'c16']`
Tokens: `119/128`
F1: `1.000` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `[]`

Score breakdown:

- individual: `10.188`
- pair synergy: `4.760`
- triple synergy: `0.000`
- redundancy penalty: `1.277`
- total: `13.670`

Improvement hint: Successful selection; inspect extra chunks only if precision or token cost becomes the priority.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `c13` | selected, required | 2.990 | 27 | Courier envelopes marked slate are routed to diagnostic imaging. |
| `c14` | selected, required | 2.938 | 30 | Diagnostic imaging sends slate envelopes to the archive cart near lift B. |
| `c16` | selected, optional | 2.509 | 31 | Slate courier envelopes before night audit should be signed at the blood desk. |
| `c15` | selected, required | 1.751 | 31 | The archive cart is signed out by Omar Singh before the night audit. |
| `c01` | - | -0.989 | 27 | Blue-lanyard observers receive a temporary pass from the learning office, not from reception. |
| `c20` | - | -0.935 | 31 | The person located at billing completes transport paperwork for red discharge packets. |
| `c17` | - | -1.021 | 29 | The red discharge packet means the patient needs transport paperwork. |
| `c18` | - | -0.913 | 29 | Transport paperwork is completed by the mobility coordinator. |
| `c02` | - | -0.999 | 29 | The learning office is called the North Annex counter in weekend notes. |
| `c35` | - | -1.022 | 30 | Mateo Ruiz works from the small office behind registration. |
| `c04` | - | -0.426 | 31 | A badge denial for visiting students should be fixed at reception by the visitor badge desk. |
| `c03` | - | -0.963 | 28 | Reception prints visitor badges only for family members and vendors. |
| `c38` | - | -0.610 | 30 | Language assistance is booked by the cultural services desk. |
| `c23` | - | -1.071 | 30 | Coral map labels are maintained by facilities, not by the access team. |
| `c28` | - | -1.099 | 31 | Silver consent telehealth follow-up slots open through in-person surgery clearance. |

### PASS content_02_clinic_access / c_q04_direct / budget 256

Question: Who signs out the cart for slate courier envelopes?

Selected: `['c13', 'c14', 'c15', 'c16']`
Tokens: `119/256`
F1: `1.000` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `[]`

Score breakdown:

- individual: `10.653`
- pair synergy: `4.760`
- triple synergy: `0.000`
- redundancy penalty: `1.277`
- total: `14.135`

Improvement hint: Successful selection; inspect extra chunks only if precision or token cost becomes the priority.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `c13` | selected, required | 3.096 | 27 | Courier envelopes marked slate are routed to diagnostic imaging. |
| `c14` | selected, required | 3.055 | 30 | Diagnostic imaging sends slate envelopes to the archive cart near lift B. |
| `c16` | selected, optional | 2.630 | 31 | Slate courier envelopes before night audit should be signed at the blood desk. |
| `c15` | selected, required | 1.872 | 31 | The archive cart is signed out by Omar Singh before the night audit. |
| `c01` | - | -0.884 | 27 | Blue-lanyard observers receive a temporary pass from the learning office, not from reception. |
| `c20` | - | -0.813 | 31 | The person located at billing completes transport paperwork for red discharge packets. |
| `c17` | - | -0.908 | 29 | The red discharge packet means the patient needs transport paperwork. |
| `c18` | - | -0.800 | 29 | Transport paperwork is completed by the mobility coordinator. |
| `c02` | - | -0.886 | 29 | The learning office is called the North Annex counter in weekend notes. |
| `c35` | - | -0.904 | 30 | Mateo Ruiz works from the small office behind registration. |
| `c04` | - | -0.305 | 31 | A badge denial for visiting students should be fixed at reception by the visitor badge desk. |
| `c03` | - | -0.853 | 28 | Reception prints visitor badges only for family members and vendors. |
| `c38` | - | -0.492 | 30 | Language assistance is booked by the cultural services desk. |
| `c23` | - | -0.954 | 30 | Coral map labels are maintained by facilities, not by the access team. |
| `c28` | - | -0.978 | 31 | Silver consent telehealth follow-up slots open through in-person surgery clearance. |

### PASS content_02_clinic_access / c_q04_direct / budget 512

Question: Who signs out the cart for slate courier envelopes?

Selected: `['c13', 'c14', 'c15', 'c16']`
Tokens: `119/512`
F1: `1.000` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `[]`

Score breakdown:

- individual: `10.885`
- pair synergy: `4.760`
- triple synergy: `0.000`
- redundancy penalty: `1.277`
- total: `14.368`

Improvement hint: Successful selection; inspect extra chunks only if precision or token cost becomes the priority.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `c13` | selected, required | 3.148 | 27 | Courier envelopes marked slate are routed to diagnostic imaging. |
| `c14` | selected, required | 3.114 | 30 | Diagnostic imaging sends slate envelopes to the archive cart near lift B. |
| `c16` | selected, optional | 2.690 | 31 | Slate courier envelopes before night audit should be signed at the blood desk. |
| `c15` | selected, required | 1.933 | 31 | The archive cart is signed out by Omar Singh before the night audit. |
| `c01` | - | -0.831 | 27 | Blue-lanyard observers receive a temporary pass from the learning office, not from reception. |
| `c20` | - | -0.753 | 31 | The person located at billing completes transport paperwork for red discharge packets. |
| `c17` | - | -0.851 | 29 | The red discharge packet means the patient needs transport paperwork. |
| `c18` | - | -0.743 | 29 | Transport paperwork is completed by the mobility coordinator. |
| `c02` | - | -0.829 | 29 | The learning office is called the North Annex counter in weekend notes. |
| `c35` | - | -0.846 | 30 | Mateo Ruiz works from the small office behind registration. |
| `c04` | - | -0.245 | 31 | A badge denial for visiting students should be fixed at reception by the visitor badge desk. |
| `c03` | - | -0.798 | 28 | Reception prints visitor badges only for family members and vendors. |
| `c38` | - | -0.434 | 30 | Language assistance is booked by the cultural services desk. |
| `c23` | - | -0.895 | 30 | Coral map labels are maintained by facilities, not by the access team. |
| `c28` | - | -0.918 | 31 | Silver consent telehealth follow-up slots open through in-person surgery clearance. |

### PASS content_02_clinic_access / c_q04_direct / budget 1024

Question: Who signs out the cart for slate courier envelopes?

Selected: `['c13', 'c14', 'c15', 'c16']`
Tokens: `119/1024`
F1: `1.000` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `[]`

Score breakdown:

- individual: `11.001`
- pair synergy: `4.760`
- triple synergy: `0.000`
- redundancy penalty: `1.277`
- total: `14.484`

Improvement hint: Successful selection; inspect extra chunks only if precision or token cost becomes the priority.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `c13` | selected, required | 3.175 | 27 | Courier envelopes marked slate are routed to diagnostic imaging. |
| `c14` | selected, required | 3.143 | 30 | Diagnostic imaging sends slate envelopes to the archive cart near lift B. |
| `c16` | selected, optional | 2.721 | 31 | Slate courier envelopes before night audit should be signed at the blood desk. |
| `c15` | selected, required | 1.963 | 31 | The archive cart is signed out by Omar Singh before the night audit. |
| `c01` | - | -0.805 | 27 | Blue-lanyard observers receive a temporary pass from the learning office, not from reception. |
| `c20` | - | -0.723 | 31 | The person located at billing completes transport paperwork for red discharge packets. |
| `c17` | - | -0.823 | 29 | The red discharge packet means the patient needs transport paperwork. |
| `c18` | - | -0.715 | 29 | Transport paperwork is completed by the mobility coordinator. |
| `c02` | - | -0.801 | 29 | The learning office is called the North Annex counter in weekend notes. |
| `c35` | - | -0.817 | 30 | Mateo Ruiz works from the small office behind registration. |
| `c04` | - | -0.214 | 31 | A badge denial for visiting students should be fixed at reception by the visitor badge desk. |
| `c03` | - | -0.771 | 28 | Reception prints visitor badges only for family members and vendors. |
| `c38` | - | -0.405 | 30 | Language assistance is booked by the cultural services desk. |
| `c23` | - | -0.866 | 30 | Coral map labels are maintained by facilities, not by the access team. |
| `c28` | - | -0.888 | 31 | Silver consent telehealth follow-up slots open through in-person surgery clearance. |

### FAIL content_02_clinic_access / c_q05_direct / budget 128

Question: Where is the person who completes transport paperwork located?

Selected: `['c17', 'c18', 'c20', 'c25']`
Tokens: `117/128`
F1: `0.706` Required recall: `0.667`
Missing required units: `['owner_location']`
Selected distractors: `[]`

Score breakdown:

- individual: `10.067`
- pair synergy: `1.690`
- triple synergy: `0.000`
- redundancy penalty: `0.874`
- total: `10.883`

Improvement hint: Tight-budget tradeoff; improve importance ranking so required evidence beats optional/filler chunks.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `c20` | selected, optional | 4.558 | 31 | The person located at billing completes transport paperwork for red discharge packets. |
| `c17` | selected, required | 2.223 | 29 | The red discharge packet means the patient needs transport paperwork. |
| `c18` | selected, required | 2.014 | 29 | Transport paperwork is completed by the mobility coordinator. |
| `c28` | - | 0.059 | 31 | Silver consent telehealth follow-up slots open through in-person surgery clearance. |
| `c01` | - | -0.976 | 27 | Blue-lanyard observers receive a temporary pass from the learning office, not from reception. |
| `c13` | - | -0.875 | 27 | Courier envelopes marked slate are routed to diagnostic imaging. |
| `c35` | - | -0.939 | 30 | Mateo Ruiz works from the small office behind registration. |
| `c25` | selected | 1.272 | 28 | The silver consent sleeve indicates telehealth follow-up. |
| `c14` | - | -0.986 | 30 | Diagnostic imaging sends slate envelopes to the archive cart near lift B. |
| `c26` | - | 0.585 | 30 | Telehealth follow-up slots are opened by the remote-care scheduler. |
| `c16` | - | -0.945 | 31 | Slate courier envelopes before night audit should be signed at the blood desk. |
| `c19` | required | 0.307 | 31 | The mobility coordinator sits beside the west stairwell during afternoon rounds. |
| `c34` | - | -1.001 | 29 | Pending insurance reviews are handled by claims liaison Mateo Ruiz. |
| `c02` | - | -1.025 | 29 | The learning office is called the North Annex counter in weekend notes. |
| `c37` | - | -0.516 | 28 | The pearl sticker means language assistance is requested. |

### PASS content_02_clinic_access / c_q05_direct / budget 256

Question: Where is the person who completes transport paperwork located?

Selected: `['c17', 'c18', 'c19', 'c20', 'c25', 'c26', 'c28']`
Tokens: `209/256`
F1: `0.727` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `[]`

Score breakdown:

- individual: `11.835`
- pair synergy: `5.290`
- triple synergy: `0.000`
- redundancy penalty: `2.207`
- total: `14.918`

Improvement hint: Successful selection; inspect extra chunks only if precision or token cost becomes the priority.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `c20` | selected, optional | 4.679 | 31 | The person located at billing completes transport paperwork for red discharge packets. |
| `c17` | selected, required | 2.336 | 29 | The red discharge packet means the patient needs transport paperwork. |
| `c18` | selected, required | 2.128 | 29 | Transport paperwork is completed by the mobility coordinator. |
| `c28` | selected | 0.180 | 31 | Silver consent telehealth follow-up slots open through in-person surgery clearance. |
| `c01` | - | -0.871 | 27 | Blue-lanyard observers receive a temporary pass from the learning office, not from reception. |
| `c13` | - | -0.769 | 27 | Courier envelopes marked slate are routed to diagnostic imaging. |
| `c35` | - | -0.822 | 30 | Mateo Ruiz works from the small office behind registration. |
| `c25` | selected | 1.381 | 28 | The silver consent sleeve indicates telehealth follow-up. |
| `c14` | - | -0.869 | 30 | Diagnostic imaging sends slate envelopes to the archive cart near lift B. |
| `c26` | selected | 0.703 | 30 | Telehealth follow-up slots are opened by the remote-care scheduler. |
| `c16` | - | -0.824 | 31 | Slate courier envelopes before night audit should be signed at the blood desk. |
| `c19` | selected, required | 0.428 | 31 | The mobility coordinator sits beside the west stairwell during afternoon rounds. |
| `c34` | - | -0.888 | 29 | Pending insurance reviews are handled by claims liaison Mateo Ruiz. |
| `c02` | - | -0.912 | 29 | The learning office is called the North Annex counter in weekend notes. |
| `c37` | - | -0.407 | 28 | The pearl sticker means language assistance is requested. |

### PASS content_02_clinic_access / c_q05_direct / budget 512

Question: Where is the person who completes transport paperwork located?

Selected: `['c17', 'c18', 'c19', 'c20', 'c25', 'c26', 'c28']`
Tokens: `209/512`
F1: `0.727` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `[]`

Score breakdown:

- individual: `12.243`
- pair synergy: `5.290`
- triple synergy: `0.000`
- redundancy penalty: `2.207`
- total: `15.326`

Improvement hint: Successful selection; inspect extra chunks only if precision or token cost becomes the priority.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `c20` | selected, optional | 4.740 | 31 | The person located at billing completes transport paperwork for red discharge packets. |
| `c17` | selected, required | 2.393 | 29 | The red discharge packet means the patient needs transport paperwork. |
| `c18` | selected, required | 2.184 | 29 | Transport paperwork is completed by the mobility coordinator. |
| `c28` | selected | 0.241 | 31 | Silver consent telehealth follow-up slots open through in-person surgery clearance. |
| `c01` | - | -0.818 | 27 | Blue-lanyard observers receive a temporary pass from the learning office, not from reception. |
| `c13` | - | -0.717 | 27 | Courier envelopes marked slate are routed to diagnostic imaging. |
| `c35` | - | -0.764 | 30 | Mateo Ruiz works from the small office behind registration. |
| `c25` | selected | 1.436 | 28 | The silver consent sleeve indicates telehealth follow-up. |
| `c14` | - | -0.810 | 30 | Diagnostic imaging sends slate envelopes to the archive cart near lift B. |
| `c26` | selected | 0.761 | 30 | Telehealth follow-up slots are opened by the remote-care scheduler. |
| `c16` | - | -0.764 | 31 | Slate courier envelopes before night audit should be signed at the blood desk. |
| `c19` | selected, required | 0.489 | 31 | The mobility coordinator sits beside the west stairwell during afternoon rounds. |
| `c34` | - | -0.832 | 29 | Pending insurance reviews are handled by claims liaison Mateo Ruiz. |
| `c02` | - | -0.855 | 29 | The learning office is called the North Annex counter in weekend notes. |
| `c37` | - | -0.352 | 28 | The pearl sticker means language assistance is requested. |

### PASS content_02_clinic_access / c_q05_direct / budget 1024

Question: Where is the person who completes transport paperwork located?

Selected: `['c17', 'c18', 'c19', 'c20', 'c25', 'c26', 'c28']`
Tokens: `209/1024`
F1: `0.727` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `[]`

Score breakdown:

- individual: `12.447`
- pair synergy: `5.290`
- triple synergy: `0.000`
- redundancy penalty: `2.207`
- total: `15.530`

Improvement hint: Successful selection; inspect extra chunks only if precision or token cost becomes the priority.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `c20` | selected, optional | 4.770 | 31 | The person located at billing completes transport paperwork for red discharge packets. |
| `c17` | selected, required | 2.421 | 29 | The red discharge packet means the patient needs transport paperwork. |
| `c18` | selected, required | 2.212 | 29 | Transport paperwork is completed by the mobility coordinator. |
| `c28` | selected | 0.271 | 31 | Silver consent telehealth follow-up slots open through in-person surgery clearance. |
| `c01` | - | -0.792 | 27 | Blue-lanyard observers receive a temporary pass from the learning office, not from reception. |
| `c13` | - | -0.690 | 27 | Courier envelopes marked slate are routed to diagnostic imaging. |
| `c35` | - | -0.734 | 30 | Mateo Ruiz works from the small office behind registration. |
| `c25` | selected | 1.463 | 28 | The silver consent sleeve indicates telehealth follow-up. |
| `c14` | - | -0.781 | 30 | Diagnostic imaging sends slate envelopes to the archive cart near lift B. |
| `c26` | selected | 0.790 | 30 | Telehealth follow-up slots are opened by the remote-care scheduler. |
| `c16` | - | -0.733 | 31 | Slate courier envelopes before night audit should be signed at the blood desk. |
| `c19` | selected, required | 0.519 | 31 | The mobility coordinator sits beside the west stairwell during afternoon rounds. |
| `c34` | - | -0.803 | 29 | Pending insurance reviews are handled by claims liaison Mateo Ruiz. |
| `c02` | - | -0.827 | 29 | The learning office is called the North Annex counter in weekend notes. |
| `c37` | - | -0.325 | 28 | The pearl sticker means language assistance is requested. |

### PASS content_02_clinic_access / c_q06_two_hop / budget 128

Question: Which map label points to the place for expired wristband replacement?

Selected: `['c21', 'c22', 'c23', 'c24']`
Tokens: `116/128`
F1: `0.857` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `['c24']`

Score breakdown:

- individual: `6.017`
- pair synergy: `2.164`
- triple synergy: `0.000`
- redundancy penalty: `0.659`
- total: `7.522`

Improvement hint: Add wrong-context or contradiction-aware features; a distractor beat required evidence.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `c24` | selected, distractor | 3.394 | 30 | Expired wristband replacement points to the security map label after a badge denial. |
| `c21` | selected, required | 1.100 | 27 | Expired wristbands are replaced at the intake island. |
| `c22` | selected, required | 0.815 | 29 | The intake island is labeled Coral on the floor map. |
| `c23` | selected, optional | 0.707 | 30 | Coral map labels are maintained by facilities, not by the access team. |
| `c01` | - | -0.587 | 27 | Blue-lanyard observers receive a temporary pass from the learning office, not from reception. |
| `c36` | - | -0.935 | 31 | Bronze chart stickers are cleared by the triage physician before insurance review. |
| `c33` | - | -0.915 | 28 | The bronze sticker on a chart means insurance review is pending. |
| `c37` | - | -1.007 | 28 | The pearl sticker means language assistance is requested. |
| `c34` | - | -1.161 | 29 | Pending insurance reviews are handled by claims liaison Mateo Ruiz. |
| `c02` | - | -1.006 | 29 | The learning office is called the North Annex counter in weekend notes. |
| `c35` | - | -1.150 | 30 | Mateo Ruiz works from the small office behind registration. |
| `c04` | - | -0.421 | 31 | A badge denial for visiting students should be fixed at reception by the visitor badge desk. |
| `c40` | - | -0.998 | 31 | Pearl sticker language help roster requests go to financial counseling at registration. |
| `c29` | - | -1.022 | 27 | A lavender tray tag means samples go to microbiology. |
| `c17` | - | -1.049 | 29 | The red discharge packet means the patient needs transport paperwork. |

### PASS content_02_clinic_access / c_q06_two_hop / budget 256

Question: Which map label points to the place for expired wristband replacement?

Selected: `['c21', 'c22', 'c23', 'c24']`
Tokens: `116/256`
F1: `0.857` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `['c24']`

Score breakdown:

- individual: `6.470`
- pair synergy: `2.164`
- triple synergy: `0.000`
- redundancy penalty: `0.659`
- total: `7.975`

Improvement hint: Add wrong-context or contradiction-aware features; a distractor beat required evidence.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `c24` | selected, distractor | 3.512 | 30 | Expired wristband replacement points to the security map label after a badge denial. |
| `c21` | selected, required | 1.206 | 27 | Expired wristbands are replaced at the intake island. |
| `c22` | selected, required | 0.928 | 29 | The intake island is labeled Coral on the floor map. |
| `c23` | selected, optional | 0.825 | 30 | Coral map labels are maintained by facilities, not by the access team. |
| `c01` | - | -0.481 | 27 | Blue-lanyard observers receive a temporary pass from the learning office, not from reception. |
| `c36` | - | -0.814 | 31 | Bronze chart stickers are cleared by the triage physician before insurance review. |
| `c33` | - | -0.806 | 28 | The bronze sticker on a chart means insurance review is pending. |
| `c37` | - | -0.897 | 28 | The pearl sticker means language assistance is requested. |
| `c34` | - | -1.048 | 29 | Pending insurance reviews are handled by claims liaison Mateo Ruiz. |
| `c02` | - | -0.893 | 29 | The learning office is called the North Annex counter in weekend notes. |
| `c35` | - | -1.033 | 30 | Mateo Ruiz works from the small office behind registration. |
| `c04` | - | -0.300 | 31 | A badge denial for visiting students should be fixed at reception by the visitor badge desk. |
| `c40` | - | -0.877 | 31 | Pearl sticker language help roster requests go to financial counseling at registration. |
| `c17` | - | -0.936 | 29 | The red discharge packet means the patient needs transport paperwork. |
| `c29` | - | -0.916 | 27 | A lavender tray tag means samples go to microbiology. |

### PASS content_02_clinic_access / c_q06_two_hop / budget 512

Question: Which map label points to the place for expired wristband replacement?

Selected: `['c21', 'c22', 'c23', 'c24']`
Tokens: `116/512`
F1: `0.857` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `['c24']`

Score breakdown:

- individual: `6.697`
- pair synergy: `2.164`
- triple synergy: `0.000`
- redundancy penalty: `0.659`
- total: `8.201`

Improvement hint: Add wrong-context or contradiction-aware features; a distractor beat required evidence.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `c24` | selected, distractor | 3.570 | 30 | Expired wristband replacement points to the security map label after a badge denial. |
| `c21` | selected, required | 1.258 | 27 | Expired wristbands are replaced at the intake island. |
| `c22` | selected, required | 0.985 | 29 | The intake island is labeled Coral on the floor map. |
| `c23` | selected, optional | 0.883 | 30 | Coral map labels are maintained by facilities, not by the access team. |
| `c01` | - | -0.428 | 27 | Blue-lanyard observers receive a temporary pass from the learning office, not from reception. |
| `c36` | - | -0.754 | 31 | Bronze chart stickers are cleared by the triage physician before insurance review. |
| `c33` | - | -0.751 | 28 | The bronze sticker on a chart means insurance review is pending. |
| `c37` | - | -0.843 | 28 | The pearl sticker means language assistance is requested. |
| `c34` | - | -0.992 | 29 | Pending insurance reviews are handled by claims liaison Mateo Ruiz. |
| `c02` | - | -0.836 | 29 | The learning office is called the North Annex counter in weekend notes. |
| `c35` | - | -0.974 | 30 | Mateo Ruiz works from the small office behind registration. |
| `c04` | - | -0.240 | 31 | A badge denial for visiting students should be fixed at reception by the visitor badge desk. |
| `c40` | - | -0.816 | 31 | Pearl sticker language help roster requests go to financial counseling at registration. |
| `c17` | - | -0.879 | 29 | The red discharge packet means the patient needs transport paperwork. |
| `c29` | - | -0.863 | 27 | A lavender tray tag means samples go to microbiology. |

### PASS content_02_clinic_access / c_q06_two_hop / budget 1024

Question: Which map label points to the place for expired wristband replacement?

Selected: `['c21', 'c22', 'c23', 'c24']`
Tokens: `116/1024`
F1: `0.857` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `['c24']`

Score breakdown:

- individual: `6.810`
- pair synergy: `2.164`
- triple synergy: `0.000`
- redundancy penalty: `0.659`
- total: `8.315`

Improvement hint: Add wrong-context or contradiction-aware features; a distractor beat required evidence.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `c24` | selected, distractor | 3.599 | 30 | Expired wristband replacement points to the security map label after a badge denial. |
| `c21` | selected, required | 1.285 | 27 | Expired wristbands are replaced at the intake island. |
| `c22` | selected, required | 1.013 | 29 | The intake island is labeled Coral on the floor map. |
| `c23` | selected, optional | 0.912 | 30 | Coral map labels are maintained by facilities, not by the access team. |
| `c01` | - | -0.402 | 27 | Blue-lanyard observers receive a temporary pass from the learning office, not from reception. |
| `c36` | - | -0.723 | 31 | Bronze chart stickers are cleared by the triage physician before insurance review. |
| `c33` | - | -0.724 | 28 | The bronze sticker on a chart means insurance review is pending. |
| `c37` | - | -0.815 | 28 | The pearl sticker means language assistance is requested. |
| `c34` | - | -0.963 | 29 | Pending insurance reviews are handled by claims liaison Mateo Ruiz. |
| `c02` | - | -0.808 | 29 | The learning office is called the North Annex counter in weekend notes. |
| `c35` | - | -0.945 | 30 | Mateo Ruiz works from the small office behind registration. |
| `c04` | - | -0.210 | 31 | A badge denial for visiting students should be fixed at reception by the visitor badge desk. |
| `c40` | - | -0.786 | 31 | Pearl sticker language help roster requests go to financial counseling at registration. |
| `c17` | - | -0.851 | 29 | The red discharge packet means the patient needs transport paperwork. |
| `c29` | - | -0.837 | 27 | A lavender tray tag means samples go to microbiology. |

### PASS content_02_clinic_access / c_q07_two_hop / budget 128

Question: Which queue opens slots for silver consent telehealth follow-up?

Selected: `['c25', 'c26', 'c27', 'c28']`
Tokens: `118/128`
F1: `1.000` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `[]`

Score breakdown:

- individual: `12.081`
- pair synergy: `3.461`
- triple synergy: `0.156`
- redundancy penalty: `1.247`
- total: `14.451`

Improvement hint: Successful selection; inspect extra chunks only if precision or token cost becomes the priority.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `c28` | selected, optional | 4.654 | 31 | Silver consent telehealth follow-up slots open through in-person surgery clearance. |
| `c25` | selected, required | 4.099 | 28 | The silver consent sleeve indicates telehealth follow-up. |
| `c26` | selected, required | 2.851 | 30 | Telehealth follow-up slots are opened by the remote-care scheduler. |
| `c27` | selected, required | 0.476 | 29 | Remote-care scheduling uses the amber queue after noon. |
| `c01` | - | -0.962 | 27 | Blue-lanyard observers receive a temporary pass from the learning office, not from reception. |
| `c33` | - | -0.968 | 28 | The bronze sticker on a chart means insurance review is pending. |
| `c36` | - | -1.031 | 31 | Bronze chart stickers are cleared by the triage physician before insurance review. |
| `c37` | - | -1.073 | 28 | The pearl sticker means language assistance is requested. |
| `c34` | - | -1.055 | 29 | Pending insurance reviews are handled by claims liaison Mateo Ruiz. |
| `c09` | - | -0.157 | 28 | The quiet room uses a dove marker on the scheduling board. |
| `c02` | - | -1.059 | 29 | The learning office is called the North Annex counter in weekend notes. |
| `c35` | - | -1.167 | 30 | Mateo Ruiz works from the small office behind registration. |
| `c17` | - | -0.999 | 29 | The red discharge packet means the patient needs transport paperwork. |
| `c40` | - | -1.031 | 31 | Pearl sticker language help roster requests go to financial counseling at registration. |
| `c05` | - | -0.613 | 27 | The sedation cabinet releases keys after the orange ledger is initialed. |

### PASS content_02_clinic_access / c_q07_two_hop / budget 256

Question: Which queue opens slots for silver consent telehealth follow-up?

Selected: `['c09', 'c25', 'c26', 'c27', 'c28']`
Tokens: `146/256`
F1: `0.889` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `[]`

Score breakdown:

- individual: `12.494`
- pair synergy: `3.832`
- triple synergy: `0.156`
- redundancy penalty: `1.420`
- total: `15.062`

Improvement hint: Successful selection; inspect extra chunks only if precision or token cost becomes the priority.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `c28` | selected, optional | 4.776 | 31 | Silver consent telehealth follow-up slots open through in-person surgery clearance. |
| `c25` | selected, required | 4.208 | 28 | The silver consent sleeve indicates telehealth follow-up. |
| `c26` | selected, required | 2.969 | 30 | Telehealth follow-up slots are opened by the remote-care scheduler. |
| `c27` | selected, required | 0.590 | 29 | Remote-care scheduling uses the amber queue after noon. |
| `c01` | - | -0.857 | 27 | Blue-lanyard observers receive a temporary pass from the learning office, not from reception. |
| `c33` | - | -0.859 | 28 | The bronze sticker on a chart means insurance review is pending. |
| `c36` | - | -0.909 | 31 | Bronze chart stickers are cleared by the triage physician before insurance review. |
| `c37` | - | -0.964 | 28 | The pearl sticker means language assistance is requested. |
| `c34` | - | -0.942 | 29 | Pending insurance reviews are handled by claims liaison Mateo Ruiz. |
| `c09` | selected | -0.048 | 28 | The quiet room uses a dove marker on the scheduling board. |
| `c02` | - | -0.945 | 29 | The learning office is called the North Annex counter in weekend notes. |
| `c35` | - | -1.050 | 30 | Mateo Ruiz works from the small office behind registration. |
| `c17` | - | -0.886 | 29 | The red discharge packet means the patient needs transport paperwork. |
| `c40` | - | -0.910 | 31 | Pearl sticker language help roster requests go to financial counseling at registration. |
| `c05` | - | -0.507 | 27 | The sedation cabinet releases keys after the orange ledger is initialed. |

### PASS content_02_clinic_access / c_q07_two_hop / budget 512

Question: Which queue opens slots for silver consent telehealth follow-up?

Selected: `['c09', 'c25', 'c26', 'c27', 'c28']`
Tokens: `146/512`
F1: `0.889` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `[]`

Score breakdown:

- individual: `12.779`
- pair synergy: `3.832`
- triple synergy: `0.156`
- redundancy penalty: `1.420`
- total: `15.347`

Improvement hint: Successful selection; inspect extra chunks only if precision or token cost becomes the priority.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `c28` | selected, optional | 4.836 | 31 | Silver consent telehealth follow-up slots open through in-person surgery clearance. |
| `c25` | selected, required | 4.263 | 28 | The silver consent sleeve indicates telehealth follow-up. |
| `c26` | selected, required | 3.027 | 30 | Telehealth follow-up slots are opened by the remote-care scheduler. |
| `c27` | selected, required | 0.646 | 29 | Remote-care scheduling uses the amber queue after noon. |
| `c01` | - | -0.804 | 27 | Blue-lanyard observers receive a temporary pass from the learning office, not from reception. |
| `c33` | - | -0.804 | 28 | The bronze sticker on a chart means insurance review is pending. |
| `c36` | - | -0.849 | 31 | Bronze chart stickers are cleared by the triage physician before insurance review. |
| `c37` | - | -0.909 | 28 | The pearl sticker means language assistance is requested. |
| `c34` | - | -0.885 | 29 | Pending insurance reviews are handled by claims liaison Mateo Ruiz. |
| `c09` | selected | 0.007 | 28 | The quiet room uses a dove marker on the scheduling board. |
| `c02` | - | -0.889 | 29 | The learning office is called the North Annex counter in weekend notes. |
| `c35` | - | -0.991 | 30 | Mateo Ruiz works from the small office behind registration. |
| `c17` | - | -0.830 | 29 | The red discharge packet means the patient needs transport paperwork. |
| `c40` | - | -0.849 | 31 | Pearl sticker language help roster requests go to financial counseling at registration. |
| `c05` | - | -0.454 | 27 | The sedation cabinet releases keys after the orange ledger is initialed. |

### PASS content_02_clinic_access / c_q07_two_hop / budget 1024

Question: Which queue opens slots for silver consent telehealth follow-up?

Selected: `['c09', 'c25', 'c26', 'c27', 'c28']`
Tokens: `146/1024`
F1: `0.889` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `[]`

Score breakdown:

- individual: `12.921`
- pair synergy: `3.832`
- triple synergy: `0.156`
- redundancy penalty: `1.420`
- total: `15.490`

Improvement hint: Successful selection; inspect extra chunks only if precision or token cost becomes the priority.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `c28` | selected, optional | 4.866 | 31 | Silver consent telehealth follow-up slots open through in-person surgery clearance. |
| `c25` | selected, required | 4.290 | 28 | The silver consent sleeve indicates telehealth follow-up. |
| `c26` | selected, required | 3.057 | 30 | Telehealth follow-up slots are opened by the remote-care scheduler. |
| `c27` | selected, required | 0.675 | 29 | Remote-care scheduling uses the amber queue after noon. |
| `c01` | - | -0.777 | 27 | Blue-lanyard observers receive a temporary pass from the learning office, not from reception. |
| `c33` | - | -0.777 | 28 | The bronze sticker on a chart means insurance review is pending. |
| `c36` | - | -0.819 | 31 | Bronze chart stickers are cleared by the triage physician before insurance review. |
| `c37` | - | -0.882 | 28 | The pearl sticker means language assistance is requested. |
| `c34` | - | -0.857 | 29 | Pending insurance reviews are handled by claims liaison Mateo Ruiz. |
| `c09` | selected | 0.034 | 28 | The quiet room uses a dove marker on the scheduling board. |
| `c02` | - | -0.860 | 29 | The learning office is called the North Annex counter in weekend notes. |
| `c35` | - | -0.962 | 30 | Mateo Ruiz works from the small office behind registration. |
| `c17` | - | -0.801 | 29 | The red discharge packet means the patient needs transport paperwork. |
| `c40` | - | -0.819 | 31 | Pearl sticker language help roster requests go to financial counseling at registration. |
| `c05` | - | -0.428 | 27 | The sedation cabinet releases keys after the orange ledger is initialed. |

### PASS content_02_clinic_access / c_q08_two_hop / budget 128

Question: Who collects after-hours samples from lavender tray tags?

Selected: `['c29', 'c30', 'c31', 'c32']`
Tokens: `116/128`
F1: `1.000` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `[]`

Score breakdown:

- individual: `7.742`
- pair synergy: `2.837`
- triple synergy: `0.000`
- redundancy penalty: `1.050`
- total: `9.529`

Improvement hint: Successful selection; inspect extra chunks only if precision or token cost becomes the priority.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `c32` | selected, optional | 3.155 | 30 | Lavender tray tags mean samples go to radiology during downtime. |
| `c29` | selected, required | 2.655 | 27 | A lavender tray tag means samples go to microbiology. |
| `c30` | selected, required | 1.502 | 29 | Microbiology batches after-hours samples under code M-14. |
| `c01` | - | -0.498 | 27 | Blue-lanyard observers receive a temporary pass from the learning office, not from reception. |
| `c05` | - | -0.158 | 27 | The sedation cabinet releases keys after the orange ledger is initialed. |
| `c02` | - | -0.985 | 29 | The learning office is called the North Annex counter in weekend notes. |
| `c27` | - | -0.062 | 29 | Remote-care scheduling uses the amber queue after noon. |
| `c08` | - | -1.043 | 30 | Sedation cabinet keys are approved by pharmacy when the orange ledger is missing. |
| `c31` | selected, required | 0.430 | 30 | Code M-14 batches are collected by night runner Sima Chen. |
| `c35` | - | -0.569 | 30 | Mateo Ruiz works from the small office behind registration. |
| `c06` | - | -0.973 | 28 | Orange ledger initials are supplied by the recovery charge nurse. |
| `c24` | - | -0.140 | 30 | Expired wristband replacement points to the security map label after a badge denial. |
| `c09` | - | -0.130 | 28 | The quiet room uses a dove marker on the scheduling board. |
| `c11` | - | -0.175 | 30 | Behavioral-health overflow is coordinated by Lina Park after 18:00. |
| `c12` | - | -0.189 | 31 | The quiet room after evening overflow is handled by the triage nurse for pediatric fever cases. |

### FAIL content_02_clinic_access / c_q08_two_hop / budget 256

Question: Who collects after-hours samples from lavender tray tags?

Selected: `['c01', 'c11', 'c12', 'c27', 'c29', 'c30', 'c32', 'c35']`
Tokens: `233/256`
F1: `0.480` Required recall: `0.667`
Missing required units: `['collector']`
Selected distractors: `[]`

Score breakdown:

- individual: `6.730`
- pair synergy: `8.149`
- triple synergy: `2.500`
- redundancy penalty: `1.315`
- total: `16.064`

Improvement hint: Tight-budget tradeoff; improve importance ranking so required evidence beats optional/filler chunks.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `c32` | selected, optional | 3.273 | 30 | Lavender tray tags mean samples go to radiology during downtime. |
| `c29` | selected, required | 2.761 | 27 | A lavender tray tag means samples go to microbiology. |
| `c30` | selected, required | 1.615 | 29 | Microbiology batches after-hours samples under code M-14. |
| `c01` | selected | -0.392 | 27 | Blue-lanyard observers receive a temporary pass from the learning office, not from reception. |
| `c05` | - | -0.052 | 27 | The sedation cabinet releases keys after the orange ledger is initialed. |
| `c02` | - | -0.872 | 29 | The learning office is called the North Annex counter in weekend notes. |
| `c27` | selected | 0.051 | 29 | Remote-care scheduling uses the amber queue after noon. |
| `c08` | - | -0.926 | 30 | Sedation cabinet keys are approved by pharmacy when the orange ledger is missing. |
| `c31` | required | 0.547 | 30 | Code M-14 batches are collected by night runner Sima Chen. |
| `c35` | selected | -0.452 | 30 | Mateo Ruiz works from the small office behind registration. |
| `c06` | - | -0.864 | 28 | Orange ledger initials are supplied by the recovery charge nurse. |
| `c24` | - | -0.023 | 30 | Expired wristband replacement points to the security map label after a badge denial. |
| `c09` | - | -0.021 | 28 | The quiet room uses a dove marker on the scheduling board. |
| `c11` | selected | -0.058 | 30 | Behavioral-health overflow is coordinated by Lina Park after 18:00. |
| `c12` | selected | -0.068 | 31 | The quiet room after evening overflow is handled by the triage nurse for pediatric fever cases. |

### PASS content_02_clinic_access / c_q08_two_hop / budget 512

Question: Who collects after-hours samples from lavender tray tags?

Selected: `['c01', 'c05', 'c09', 'c11', 'c12', 'c24', 'c27', 'c29', 'c30', 'c31', 'c32', 'c35']`
Tokens: `348/512`
F1: `0.500` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `[]`

Score breakdown:

- individual: `7.861`
- pair synergy: `12.864`
- triple synergy: `3.750`
- redundancy penalty: `2.541`
- total: `21.933`

Improvement hint: Successful selection; inspect extra chunks only if precision or token cost becomes the priority.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `c32` | selected, optional | 3.331 | 30 | Lavender tray tags mean samples go to radiology during downtime. |
| `c29` | selected, required | 2.814 | 27 | A lavender tray tag means samples go to microbiology. |
| `c30` | selected, required | 1.672 | 29 | Microbiology batches after-hours samples under code M-14. |
| `c01` | selected | -0.340 | 27 | Blue-lanyard observers receive a temporary pass from the learning office, not from reception. |
| `c05` | selected | 0.001 | 27 | The sedation cabinet releases keys after the orange ledger is initialed. |
| `c02` | - | -0.815 | 29 | The learning office is called the North Annex counter in weekend notes. |
| `c27` | selected | 0.108 | 29 | Remote-care scheduling uses the amber queue after noon. |
| `c08` | - | -0.868 | 30 | Sedation cabinet keys are approved by pharmacy when the orange ledger is missing. |
| `c31` | selected, required | 0.606 | 30 | Code M-14 batches are collected by night runner Sima Chen. |
| `c35` | selected | -0.393 | 30 | Mateo Ruiz works from the small office behind registration. |
| `c06` | - | -0.809 | 28 | Orange ledger initials are supplied by the recovery charge nurse. |
| `c24` | selected | 0.036 | 30 | Expired wristband replacement points to the security map label after a badge denial. |
| `c09` | selected | 0.034 | 28 | The quiet room uses a dove marker on the scheduling board. |
| `c11` | selected | 0.001 | 30 | Behavioral-health overflow is coordinated by Lina Park after 18:00. |
| `c12` | selected | -0.008 | 31 | The quiet room after evening overflow is handled by the triage nurse for pediatric fever cases. |

### PASS content_02_clinic_access / c_q08_two_hop / budget 1024

Question: Who collects after-hours samples from lavender tray tags?

Selected: `['c01', 'c05', 'c09', 'c11', 'c12', 'c24', 'c27', 'c29', 'c30', 'c31', 'c32', 'c35']`
Tokens: `348/1024`
F1: `0.500` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `[]`

Score breakdown:

- individual: `8.201`
- pair synergy: `12.864`
- triple synergy: `3.750`
- redundancy penalty: `2.541`
- total: `22.273`

Improvement hint: Successful selection; inspect extra chunks only if precision or token cost becomes the priority.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `c32` | selected, optional | 3.360 | 30 | Lavender tray tags mean samples go to radiology during downtime. |
| `c29` | selected, required | 2.840 | 27 | A lavender tray tag means samples go to microbiology. |
| `c30` | selected, required | 1.700 | 29 | Microbiology batches after-hours samples under code M-14. |
| `c01` | selected | -0.313 | 27 | Blue-lanyard observers receive a temporary pass from the learning office, not from reception. |
| `c05` | selected | 0.027 | 27 | The sedation cabinet releases keys after the orange ledger is initialed. |
| `c02` | - | -0.787 | 29 | The learning office is called the North Annex counter in weekend notes. |
| `c27` | selected | 0.136 | 29 | Remote-care scheduling uses the amber queue after noon. |
| `c08` | - | -0.838 | 30 | Sedation cabinet keys are approved by pharmacy when the orange ledger is missing. |
| `c31` | selected, required | 0.635 | 30 | Code M-14 batches are collected by night runner Sima Chen. |
| `c35` | selected | -0.364 | 30 | Mateo Ruiz works from the small office behind registration. |
| `c06` | - | -0.782 | 28 | Orange ledger initials are supplied by the recovery charge nurse. |
| `c24` | selected | 0.065 | 30 | Expired wristband replacement points to the security map label after a badge denial. |
| `c09` | selected | 0.061 | 28 | The quiet room uses a dove marker on the scheduling board. |
| `c11` | selected | 0.030 | 30 | Behavioral-health overflow is coordinated by Lina Park after 18:00. |
| `c12` | selected | 0.023 | 31 | The quiet room after evening overflow is handled by the triage nurse for pediatric fever cases. |

### FAIL content_02_clinic_access / c_q09_two_hop / budget 128

Question: Where does the bronze chart insurance reviewer work?

Selected: `['c33', 'c34', 'c36', 'c37']`
Tokens: `116/128`
F1: `0.706` Required recall: `0.667`
Missing required units: `['reviewer_location']`
Selected distractors: `[]`

Score breakdown:

- individual: `6.633`
- pair synergy: `1.710`
- triple synergy: `0.000`
- redundancy penalty: `0.939`
- total: `7.404`

Improvement hint: Tight-budget tradeoff; improve importance ranking so required evidence beats optional/filler chunks.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `c33` | selected, required | 3.040 | 28 | The bronze sticker on a chart means insurance review is pending. |
| `c36` | selected, optional | 2.979 | 31 | Bronze chart stickers are cleared by the triage physician before insurance review. |
| `c34` | selected, required | 0.628 | 29 | Pending insurance reviews are handled by claims liaison Mateo Ruiz. |
| `c01` | - | -1.015 | 27 | Blue-lanyard observers receive a temporary pass from the learning office, not from reception. |
| `c05` | - | -0.722 | 27 | The sedation cabinet releases keys after the orange ledger is initialed. |
| `c24` | - | -0.943 | 30 | Expired wristband replacement points to the security map label after a badge denial. |
| `c16` | - | -0.676 | 31 | Slate courier envelopes before night audit should be signed at the blood desk. |
| `c08` | - | -1.062 | 30 | Sedation cabinet keys are approved by pharmacy when the orange ledger is missing. |
| `c13` | - | -1.046 | 27 | Courier envelopes marked slate are routed to diagnostic imaging. |
| `c15` | - | -0.719 | 31 | The archive cart is signed out by Omar Singh before the night audit. |
| `c37` | selected | -0.014 | 28 | The pearl sticker means language assistance is requested. |
| `c06` | - | -0.999 | 28 | Orange ledger initials are supplied by the recovery charge nurse. |
| `c02` | - | -1.010 | 29 | The learning office is called the North Annex counter in weekend notes. |
| `c35` | required | -0.273 | 30 | Mateo Ruiz works from the small office behind registration. |
| `c21` | - | -0.321 | 27 | Expired wristbands are replaced at the intake island. |

### PASS content_02_clinic_access / c_q09_two_hop / budget 256

Question: Where does the bronze chart insurance reviewer work?

Selected: `['c33', 'c34', 'c35', 'c36', 'c37']`
Tokens: `146/256`
F1: `0.889` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `[]`

Score breakdown:

- individual: `6.930`
- pair synergy: `2.035`
- triple synergy: `0.000`
- redundancy penalty: `1.100`
- total: `7.866`

Improvement hint: Successful selection; inspect extra chunks only if precision or token cost becomes the priority.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `c33` | selected, required | 3.150 | 28 | The bronze sticker on a chart means insurance review is pending. |
| `c36` | selected, optional | 3.100 | 31 | Bronze chart stickers are cleared by the triage physician before insurance review. |
| `c34` | selected, required | 0.741 | 29 | Pending insurance reviews are handled by claims liaison Mateo Ruiz. |
| `c01` | - | -0.910 | 27 | Blue-lanyard observers receive a temporary pass from the learning office, not from reception. |
| `c05` | - | -0.616 | 27 | The sedation cabinet releases keys after the orange ledger is initialed. |
| `c24` | - | -0.826 | 30 | Expired wristband replacement points to the security map label after a badge denial. |
| `c16` | - | -0.555 | 31 | Slate courier envelopes before night audit should be signed at the blood desk. |
| `c08` | - | -0.945 | 30 | Sedation cabinet keys are approved by pharmacy when the orange ledger is missing. |
| `c15` | - | -0.598 | 31 | The archive cart is signed out by Omar Singh before the night audit. |
| `c13` | - | -0.940 | 27 | Courier envelopes marked slate are routed to diagnostic imaging. |
| `c37` | selected | 0.095 | 28 | The pearl sticker means language assistance is requested. |
| `c06` | - | -0.890 | 28 | Orange ledger initials are supplied by the recovery charge nurse. |
| `c02` | - | -0.897 | 29 | The learning office is called the North Annex counter in weekend notes. |
| `c35` | selected, required | -0.155 | 30 | Mateo Ruiz works from the small office behind registration. |
| `c21` | - | -0.215 | 27 | Expired wristbands are replaced at the intake island. |

### PASS content_02_clinic_access / c_q09_two_hop / budget 512

Question: Where does the bronze chart insurance reviewer work?

Selected: `['c33', 'c34', 'c35', 'c36', 'c37']`
Tokens: `146/512`
F1: `0.889` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `[]`

Score breakdown:

- individual: `7.216`
- pair synergy: `2.035`
- triple synergy: `0.000`
- redundancy penalty: `1.100`
- total: `8.151`

Improvement hint: Successful selection; inspect extra chunks only if precision or token cost becomes the priority.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `c33` | selected, required | 3.204 | 28 | The bronze sticker on a chart means insurance review is pending. |
| `c36` | selected, optional | 3.161 | 31 | Bronze chart stickers are cleared by the triage physician before insurance review. |
| `c34` | selected, required | 0.798 | 29 | Pending insurance reviews are handled by claims liaison Mateo Ruiz. |
| `c01` | - | -0.857 | 27 | Blue-lanyard observers receive a temporary pass from the learning office, not from reception. |
| `c05` | - | -0.563 | 27 | The sedation cabinet releases keys after the orange ledger is initialed. |
| `c24` | - | -0.768 | 30 | Expired wristband replacement points to the security map label after a badge denial. |
| `c16` | - | -0.494 | 31 | Slate courier envelopes before night audit should be signed at the blood desk. |
| `c08` | - | -0.887 | 30 | Sedation cabinet keys are approved by pharmacy when the orange ledger is missing. |
| `c15` | - | -0.537 | 31 | The archive cart is signed out by Omar Singh before the night audit. |
| `c13` | - | -0.887 | 27 | Courier envelopes marked slate are routed to diagnostic imaging. |
| `c37` | selected | 0.150 | 28 | The pearl sticker means language assistance is requested. |
| `c06` | - | -0.835 | 28 | Orange ledger initials are supplied by the recovery charge nurse. |
| `c02` | - | -0.840 | 29 | The learning office is called the North Annex counter in weekend notes. |
| `c35` | selected, required | -0.097 | 30 | Mateo Ruiz works from the small office behind registration. |
| `c21` | - | -0.163 | 27 | Expired wristbands are replaced at the intake island. |

### PASS content_02_clinic_access / c_q09_two_hop / budget 1024

Question: Where does the bronze chart insurance reviewer work?

Selected: `['c33', 'c34', 'c35', 'c36', 'c37']`
Tokens: `146/1024`
F1: `0.889` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `[]`

Score breakdown:

- individual: `7.358`
- pair synergy: `2.035`
- triple synergy: `0.000`
- redundancy penalty: `1.100`
- total: `8.294`

Improvement hint: Successful selection; inspect extra chunks only if precision or token cost becomes the priority.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `c33` | selected, required | 3.232 | 28 | The bronze sticker on a chart means insurance review is pending. |
| `c36` | selected, optional | 3.191 | 31 | Bronze chart stickers are cleared by the triage physician before insurance review. |
| `c34` | selected, required | 0.826 | 29 | Pending insurance reviews are handled by claims liaison Mateo Ruiz. |
| `c01` | - | -0.831 | 27 | Blue-lanyard observers receive a temporary pass from the learning office, not from reception. |
| `c05` | - | -0.537 | 27 | The sedation cabinet releases keys after the orange ledger is initialed. |
| `c24` | - | -0.738 | 30 | Expired wristband replacement points to the security map label after a badge denial. |
| `c16` | - | -0.464 | 31 | Slate courier envelopes before night audit should be signed at the blood desk. |
| `c08` | - | -0.857 | 30 | Sedation cabinet keys are approved by pharmacy when the orange ledger is missing. |
| `c15` | - | -0.507 | 31 | The archive cart is signed out by Omar Singh before the night audit. |
| `c13` | - | -0.861 | 27 | Courier envelopes marked slate are routed to diagnostic imaging. |
| `c37` | selected | 0.177 | 28 | The pearl sticker means language assistance is requested. |
| `c06` | - | -0.808 | 28 | Orange ledger initials are supplied by the recovery charge nurse. |
| `c02` | - | -0.812 | 29 | The learning office is called the North Annex counter in weekend notes. |
| `c35` | selected, required | -0.068 | 30 | Mateo Ruiz works from the small office behind registration. |
| `c21` | - | -0.136 | 27 | Expired wristbands are replaced at the intake island. |

### PASS content_02_clinic_access / c_q10_two_hop / budget 128

Question: Which roster supports pearl sticker language help?

Selected: `['c37', 'c38', 'c39', 'c40']`
Tokens: `118/128`
F1: `1.000` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `[]`

Score breakdown:

- individual: `8.294`
- pair synergy: `2.586`
- triple synergy: `0.000`
- redundancy penalty: `0.834`
- total: `10.045`

Improvement hint: Successful selection; inspect extra chunks only if precision or token cost becomes the priority.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `c40` | selected, optional | 4.015 | 31 | Pearl sticker language help roster requests go to financial counseling at registration. |
| `c37` | selected, required | 2.747 | 28 | The pearl sticker means language assistance is requested. |
| `c33` | - | 0.624 | 28 | The bronze sticker on a chart means insurance review is pending. |
| `c39` | selected, required | 0.754 | 29 | Cultural services keeps evening interpreters on the violet roster. |
| `c38` | selected, required | 0.779 | 30 | Language assistance is booked by the cultural services desk. |
| `c23` | - | -1.025 | 30 | Coral map labels are maintained by facilities, not by the access team. |
| `c36` | - | -1.079 | 31 | Bronze chart stickers are cleared by the triage physician before insurance review. |
| `c22` | - | -1.092 | 29 | The intake island is labeled Coral on the floor map. |
| `c34` | - | -1.131 | 29 | Pending insurance reviews are handled by claims liaison Mateo Ruiz. |
| `c16` | - | -0.588 | 31 | Slate courier envelopes before night audit should be signed at the blood desk. |
| `c17` | - | -0.594 | 29 | The red discharge packet means the patient needs transport paperwork. |
| `c29` | - | -0.614 | 27 | A lavender tray tag means samples go to microbiology. |
| `c07` | - | -0.682 | 29 | Pharmacy keeps a separate green narcotics book for medication counts. |
| `c24` | - | -1.061 | 30 | Expired wristband replacement points to the security map label after a badge denial. |
| `c04` | - | -0.680 | 31 | A badge denial for visiting students should be fixed at reception by the visitor badge desk. |

### PASS content_02_clinic_access / c_q10_two_hop / budget 256

Question: Which roster supports pearl sticker language help?

Selected: `['c33', 'c37', 'c38', 'c39', 'c40']`
Tokens: `146/256`
F1: `0.889` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `[]`

Score breakdown:

- individual: `9.489`
- pair synergy: `3.871`
- triple synergy: `0.208`
- redundancy penalty: `1.109`
- total: `12.459`

Improvement hint: Successful selection; inspect extra chunks only if precision or token cost becomes the priority.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `c40` | selected, optional | 4.136 | 31 | Pearl sticker language help roster requests go to financial counseling at registration. |
| `c37` | selected, required | 2.856 | 28 | The pearl sticker means language assistance is requested. |
| `c33` | selected | 0.734 | 28 | The bronze sticker on a chart means insurance review is pending. |
| `c39` | selected, required | 0.867 | 29 | Cultural services keeps evening interpreters on the violet roster. |
| `c38` | selected, required | 0.896 | 30 | Language assistance is booked by the cultural services desk. |
| `c23` | - | -0.908 | 30 | Coral map labels are maintained by facilities, not by the access team. |
| `c36` | - | -0.958 | 31 | Bronze chart stickers are cleared by the triage physician before insurance review. |
| `c22` | - | -0.979 | 29 | The intake island is labeled Coral on the floor map. |
| `c34` | - | -1.018 | 29 | Pending insurance reviews are handled by claims liaison Mateo Ruiz. |
| `c16` | - | -0.467 | 31 | Slate courier envelopes before night audit should be signed at the blood desk. |
| `c17` | - | -0.480 | 29 | The red discharge packet means the patient needs transport paperwork. |
| `c29` | - | -0.509 | 27 | A lavender tray tag means samples go to microbiology. |
| `c07` | - | -0.568 | 29 | Pharmacy keeps a separate green narcotics book for medication counts. |
| `c24` | - | -0.943 | 30 | Expired wristband replacement points to the security map label after a badge denial. |
| `c04` | - | -0.559 | 31 | A badge denial for visiting students should be fixed at reception by the visitor badge desk. |

### PASS content_02_clinic_access / c_q10_two_hop / budget 512

Question: Which roster supports pearl sticker language help?

Selected: `['c33', 'c37', 'c38', 'c39', 'c40']`
Tokens: `146/512`
F1: `0.889` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `[]`

Score breakdown:

- individual: `9.774`
- pair synergy: `3.871`
- triple synergy: `0.208`
- redundancy penalty: `1.109`
- total: `12.744`

Improvement hint: Successful selection; inspect extra chunks only if precision or token cost becomes the priority.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `c40` | selected, optional | 4.196 | 31 | Pearl sticker language help roster requests go to financial counseling at registration. |
| `c37` | selected, required | 2.911 | 28 | The pearl sticker means language assistance is requested. |
| `c33` | selected | 0.788 | 28 | The bronze sticker on a chart means insurance review is pending. |
| `c39` | selected, required | 0.924 | 29 | Cultural services keeps evening interpreters on the violet roster. |
| `c38` | selected, required | 0.955 | 30 | Language assistance is booked by the cultural services desk. |
| `c23` | - | -0.850 | 30 | Coral map labels are maintained by facilities, not by the access team. |
| `c36` | - | -0.898 | 31 | Bronze chart stickers are cleared by the triage physician before insurance review. |
| `c22` | - | -0.922 | 29 | The intake island is labeled Coral on the floor map. |
| `c34` | - | -0.961 | 29 | Pending insurance reviews are handled by claims liaison Mateo Ruiz. |
| `c16` | - | -0.406 | 31 | Slate courier envelopes before night audit should be signed at the blood desk. |
| `c17` | - | -0.424 | 29 | The red discharge packet means the patient needs transport paperwork. |
| `c29` | - | -0.456 | 27 | A lavender tray tag means samples go to microbiology. |
| `c07` | - | -0.512 | 29 | Pharmacy keeps a separate green narcotics book for medication counts. |
| `c24` | - | -0.885 | 30 | Expired wristband replacement points to the security map label after a badge denial. |
| `c04` | - | -0.498 | 31 | A badge denial for visiting students should be fixed at reception by the visitor badge desk. |

### PASS content_02_clinic_access / c_q10_two_hop / budget 1024

Question: Which roster supports pearl sticker language help?

Selected: `['c33', 'c37', 'c38', 'c39', 'c40']`
Tokens: `146/1024`
F1: `0.889` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `[]`

Score breakdown:

- individual: `9.916`
- pair synergy: `3.871`
- triple synergy: `0.208`
- redundancy penalty: `1.109`
- total: `12.887`

Improvement hint: Successful selection; inspect extra chunks only if precision or token cost becomes the priority.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `c40` | selected, optional | 4.226 | 31 | Pearl sticker language help roster requests go to financial counseling at registration. |
| `c37` | selected, required | 2.938 | 28 | The pearl sticker means language assistance is requested. |
| `c33` | selected | 0.816 | 28 | The bronze sticker on a chart means insurance review is pending. |
| `c39` | selected, required | 0.952 | 29 | Cultural services keeps evening interpreters on the violet roster. |
| `c38` | selected, required | 0.984 | 30 | Language assistance is booked by the cultural services desk. |
| `c23` | - | -0.820 | 30 | Coral map labels are maintained by facilities, not by the access team. |
| `c36` | - | -0.867 | 31 | Bronze chart stickers are cleared by the triage physician before insurance review. |
| `c22` | - | -0.894 | 29 | The intake island is labeled Coral on the floor map. |
| `c34` | - | -0.933 | 29 | Pending insurance reviews are handled by claims liaison Mateo Ruiz. |
| `c16` | - | -0.376 | 31 | Slate courier envelopes before night audit should be signed at the blood desk. |
| `c17` | - | -0.395 | 29 | The red discharge packet means the patient needs transport paperwork. |
| `c29` | - | -0.430 | 27 | A lavender tray tag means samples go to microbiology. |
| `c07` | - | -0.483 | 29 | Pharmacy keeps a separate green narcotics book for medication counts. |
| `c24` | - | -0.855 | 30 | Expired wristband replacement points to the security map label after a badge denial. |
| `c04` | - | -0.468 | 31 | A badge denial for visiting students should be fixed at reception by the visitor badge desk. |

### PASS content_02_clinic_access / c_q11_three_hop / budget 128

Question: Who coordinates the quiet room when the dove marker appears after 18:00?

Selected: `['c09', 'c10', 'c11', 'c12']`
Tokens: `118/128`
F1: `1.000` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `[]`

Score breakdown:

- individual: `6.022`
- pair synergy: `3.367`
- triple synergy: `0.139`
- redundancy penalty: `0.678`
- total: `8.850`

Improvement hint: Successful selection; inspect extra chunks only if precision or token cost becomes the priority.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `c09` | selected, required | 2.083 | 28 | The quiet room uses a dove marker on the scheduling board. |
| `c11` | selected, required | 1.704 | 30 | Behavioral-health overflow is coordinated by Lina Park after 18:00. |
| `c12` | selected, optional | 1.356 | 31 | The quiet room after evening overflow is handled by the triage nurse for pediatric fever cases. |
| `c05` | - | -0.216 | 27 | The sedation cabinet releases keys after the orange ledger is initialed. |
| `c10` | selected, required | 0.879 | 29 | Dove markers are assigned to behavioral-health overflow patients. |
| `c01` | - | -0.954 | 27 | Blue-lanyard observers receive a temporary pass from the learning office, not from reception. |
| `c27` | - | 0.360 | 29 | Remote-care scheduling uses the amber queue after noon. |
| `c08` | - | -1.143 | 30 | Sedation cabinet keys are approved by pharmacy when the orange ledger is missing. |
| `c06` | - | -0.649 | 28 | Orange ledger initials are supplied by the recovery charge nurse. |
| `c24` | - | -0.270 | 30 | Expired wristband replacement points to the security map label after a badge denial. |
| `c26` | - | -1.036 | 30 | Telehealth follow-up slots are opened by the remote-care scheduler. |
| `c30` | - | -0.284 | 29 | Microbiology batches after-hours samples under code M-14. |
| `c02` | - | -1.005 | 29 | The learning office is called the North Annex counter in weekend notes. |
| `c35` | - | -1.152 | 30 | Mateo Ruiz works from the small office behind registration. |
| `c39` | - | -0.587 | 29 | Cultural services keeps evening interpreters on the violet roster. |

### PASS content_02_clinic_access / c_q11_three_hop / budget 256

Question: Who coordinates the quiet room when the dove marker appears after 18:00?

Selected: `['c05', 'c09', 'c10', 'c11', 'c12', 'c24', 'c27', 'c30']`
Tokens: `233/256`
F1: `0.667` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `[]`

Score breakdown:

- individual: `6.522`
- pair synergy: `7.686`
- triple synergy: `0.139`
- redundancy penalty: `1.771`
- total: `12.576`

Improvement hint: Successful selection; inspect extra chunks only if precision or token cost becomes the priority.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `c09` | selected, required | 2.192 | 28 | The quiet room uses a dove marker on the scheduling board. |
| `c11` | selected, required | 1.822 | 30 | Behavioral-health overflow is coordinated by Lina Park after 18:00. |
| `c12` | selected, optional | 1.477 | 31 | The quiet room after evening overflow is handled by the triage nurse for pediatric fever cases. |
| `c05` | selected | -0.111 | 27 | The sedation cabinet releases keys after the orange ledger is initialed. |
| `c10` | selected, required | 0.992 | 29 | Dove markers are assigned to behavioral-health overflow patients. |
| `c01` | - | -0.848 | 27 | Blue-lanyard observers receive a temporary pass from the learning office, not from reception. |
| `c27` | selected | 0.473 | 29 | Remote-care scheduling uses the amber queue after noon. |
| `c08` | - | -1.026 | 30 | Sedation cabinet keys are approved by pharmacy when the orange ledger is missing. |
| `c06` | - | -0.540 | 28 | Orange ledger initials are supplied by the recovery charge nurse. |
| `c24` | selected | -0.153 | 30 | Expired wristband replacement points to the security map label after a badge denial. |
| `c26` | - | -0.919 | 30 | Telehealth follow-up slots are opened by the remote-care scheduler. |
| `c30` | selected | -0.170 | 29 | Microbiology batches after-hours samples under code M-14. |
| `c02` | - | -0.892 | 29 | The learning office is called the North Annex counter in weekend notes. |
| `c35` | - | -1.035 | 30 | Mateo Ruiz works from the small office behind registration. |
| `c39` | - | -0.474 | 29 | Cultural services keeps evening interpreters on the violet roster. |

### PASS content_02_clinic_access / c_q11_three_hop / budget 512

Question: Who coordinates the quiet room when the dove marker appears after 18:00?

Selected: `['c05', 'c09', 'c10', 'c11', 'c12', 'c24', 'c27', 'c30']`
Tokens: `233/512`
F1: `0.667` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `[]`

Score breakdown:

- individual: `6.977`
- pair synergy: `7.686`
- triple synergy: `0.139`
- redundancy penalty: `1.771`
- total: `13.031`

Improvement hint: Successful selection; inspect extra chunks only if precision or token cost becomes the priority.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `c09` | selected, required | 2.247 | 28 | The quiet room uses a dove marker on the scheduling board. |
| `c11` | selected, required | 1.880 | 30 | Behavioral-health overflow is coordinated by Lina Park after 18:00. |
| `c12` | selected, optional | 1.538 | 31 | The quiet room after evening overflow is handled by the triage nurse for pediatric fever cases. |
| `c05` | selected | -0.058 | 27 | The sedation cabinet releases keys after the orange ledger is initialed. |
| `c10` | selected, required | 1.049 | 29 | Dove markers are assigned to behavioral-health overflow patients. |
| `c01` | - | -0.796 | 27 | Blue-lanyard observers receive a temporary pass from the learning office, not from reception. |
| `c27` | selected | 0.530 | 29 | Remote-care scheduling uses the amber queue after noon. |
| `c08` | - | -0.967 | 30 | Sedation cabinet keys are approved by pharmacy when the orange ledger is missing. |
| `c06` | - | -0.485 | 28 | Orange ledger initials are supplied by the recovery charge nurse. |
| `c24` | selected | -0.094 | 30 | Expired wristband replacement points to the security map label after a badge denial. |
| `c26` | - | -0.860 | 30 | Telehealth follow-up slots are opened by the remote-care scheduler. |
| `c30` | selected | -0.114 | 29 | Microbiology batches after-hours samples under code M-14. |
| `c02` | - | -0.836 | 29 | The learning office is called the North Annex counter in weekend notes. |
| `c35` | - | -0.976 | 30 | Mateo Ruiz works from the small office behind registration. |
| `c39` | - | -0.417 | 29 | Cultural services keeps evening interpreters on the violet roster. |

### PASS content_02_clinic_access / c_q11_three_hop / budget 1024

Question: Who coordinates the quiet room when the dove marker appears after 18:00?

Selected: `['c05', 'c09', 'c10', 'c11', 'c12', 'c24', 'c27', 'c30']`
Tokens: `233/1024`
F1: `0.667` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `[]`

Score breakdown:

- individual: `7.205`
- pair synergy: `7.686`
- triple synergy: `0.139`
- redundancy penalty: `1.771`
- total: `13.259`

Improvement hint: Successful selection; inspect extra chunks only if precision or token cost becomes the priority.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `c09` | selected, required | 2.274 | 28 | The quiet room uses a dove marker on the scheduling board. |
| `c11` | selected, required | 1.909 | 30 | Behavioral-health overflow is coordinated by Lina Park after 18:00. |
| `c12` | selected, optional | 1.568 | 31 | The quiet room after evening overflow is handled by the triage nurse for pediatric fever cases. |
| `c05` | selected | -0.032 | 27 | The sedation cabinet releases keys after the orange ledger is initialed. |
| `c10` | selected, required | 1.077 | 29 | Dove markers are assigned to behavioral-health overflow patients. |
| `c01` | - | -0.769 | 27 | Blue-lanyard observers receive a temporary pass from the learning office, not from reception. |
| `c27` | selected | 0.558 | 29 | Remote-care scheduling uses the amber queue after noon. |
| `c08` | - | -0.938 | 30 | Sedation cabinet keys are approved by pharmacy when the orange ledger is missing. |
| `c06` | - | -0.458 | 28 | Orange ledger initials are supplied by the recovery charge nurse. |
| `c24` | selected | -0.065 | 30 | Expired wristband replacement points to the security map label after a badge denial. |
| `c26` | - | -0.831 | 30 | Telehealth follow-up slots are opened by the remote-care scheduler. |
| `c30` | selected | -0.085 | 29 | Microbiology batches after-hours samples under code M-14. |
| `c02` | - | -0.807 | 29 | The learning office is called the North Annex counter in weekend notes. |
| `c35` | - | -0.947 | 30 | Mateo Ruiz works from the small office behind registration. |
| `c39` | - | -0.389 | 29 | Cultural services keeps evening interpreters on the violet roster. |

### PASS content_02_clinic_access / c_q12_three_hop / budget 128

Question: Who signs before slate courier envelopes reach the night audit path?

Selected: `['c13', 'c14', 'c15', 'c16']`
Tokens: `119/128`
F1: `1.000` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `[]`

Score breakdown:

- individual: `9.907`
- pair synergy: `3.538`
- triple synergy: `0.000`
- redundancy penalty: `1.277`
- total: `12.168`

Improvement hint: Successful selection; inspect extra chunks only if precision or token cost becomes the priority.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `c16` | selected, optional | 3.542 | 31 | Slate courier envelopes before night audit should be signed at the blood desk. |
| `c13` | selected, required | 2.488 | 27 | Courier envelopes marked slate are routed to diagnostic imaging. |
| `c15` | selected, required | 1.936 | 31 | The archive cart is signed out by Omar Singh before the night audit. |
| `c14` | selected, required | 1.941 | 30 | Diagnostic imaging sends slate envelopes to the archive cart near lift B. |
| `c31` | - | -0.238 | 30 | Code M-14 batches are collected by night runner Sima Chen. |
| `c20` | - | -0.932 | 31 | The person located at billing completes transport paperwork for red discharge packets. |
| `c17` | - | -0.991 | 29 | The red discharge packet means the patient needs transport paperwork. |
| `c30` | - | -1.147 | 29 | Microbiology batches after-hours samples under code M-14. |
| `c18` | - | -0.939 | 29 | Transport paperwork is completed by the mobility coordinator. |
| `c36` | - | -0.266 | 31 | Bronze chart stickers are cleared by the triage physician before insurance review. |
| `c04` | - | -0.414 | 31 | A badge denial for visiting students should be fixed at reception by the visitor badge desk. |
| `c38` | - | -0.627 | 30 | Language assistance is booked by the cultural services desk. |
| `c28` | - | -1.085 | 31 | Silver consent telehealth follow-up slots open through in-person surgery clearance. |
| `c01` | - | -0.949 | 27 | Blue-lanyard observers receive a temporary pass from the learning office, not from reception. |
| `c27` | - | -0.952 | 29 | Remote-care scheduling uses the amber queue after noon. |

### PASS content_02_clinic_access / c_q12_three_hop / budget 256

Question: Who signs before slate courier envelopes reach the night audit path?

Selected: `['c13', 'c14', 'c15', 'c16', 'c31', 'c36']`
Tokens: `180/256`
F1: `0.800` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `[]`

Score breakdown:

- individual: `10.106`
- pair synergy: `5.227`
- triple synergy: `0.278`
- redundancy penalty: `1.535`
- total: `14.076`

Improvement hint: Successful selection; inspect extra chunks only if precision or token cost becomes the priority.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `c16` | selected, optional | 3.663 | 31 | Slate courier envelopes before night audit should be signed at the blood desk. |
| `c13` | selected, required | 2.594 | 27 | Courier envelopes marked slate are routed to diagnostic imaging. |
| `c15` | selected, required | 2.057 | 31 | The archive cart is signed out by Omar Singh before the night audit. |
| `c14` | selected, required | 2.058 | 30 | Diagnostic imaging sends slate envelopes to the archive cart near lift B. |
| `c31` | selected | -0.121 | 30 | Code M-14 batches are collected by night runner Sima Chen. |
| `c20` | - | -0.811 | 31 | The person located at billing completes transport paperwork for red discharge packets. |
| `c17` | - | -0.878 | 29 | The red discharge packet means the patient needs transport paperwork. |
| `c30` | - | -1.034 | 29 | Microbiology batches after-hours samples under code M-14. |
| `c18` | - | -0.825 | 29 | Transport paperwork is completed by the mobility coordinator. |
| `c36` | selected | -0.145 | 31 | Bronze chart stickers are cleared by the triage physician before insurance review. |
| `c04` | - | -0.293 | 31 | A badge denial for visiting students should be fixed at reception by the visitor badge desk. |
| `c38` | - | -0.510 | 30 | Language assistance is booked by the cultural services desk. |
| `c28` | - | -0.964 | 31 | Silver consent telehealth follow-up slots open through in-person surgery clearance. |
| `c27` | - | -0.839 | 29 | Remote-care scheduling uses the amber queue after noon. |
| `c01` | - | -0.844 | 27 | Blue-lanyard observers receive a temporary pass from the learning office, not from reception. |

### PASS content_02_clinic_access / c_q12_three_hop / budget 512

Question: Who signs before slate courier envelopes reach the night audit path?

Selected: `['c13', 'c14', 'c15', 'c16', 'c31', 'c36']`
Tokens: `180/512`
F1: `0.800` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `[]`

Score breakdown:

- individual: `10.458`
- pair synergy: `5.227`
- triple synergy: `0.278`
- redundancy penalty: `1.535`
- total: `14.428`

Improvement hint: Successful selection; inspect extra chunks only if precision or token cost becomes the priority.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `c16` | selected, optional | 3.724 | 31 | Slate courier envelopes before night audit should be signed at the blood desk. |
| `c13` | selected, required | 2.646 | 27 | Courier envelopes marked slate are routed to diagnostic imaging. |
| `c15` | selected, required | 2.118 | 31 | The archive cart is signed out by Omar Singh before the night audit. |
| `c14` | selected, required | 2.117 | 30 | Diagnostic imaging sends slate envelopes to the archive cart near lift B. |
| `c31` | selected | -0.062 | 30 | Code M-14 batches are collected by night runner Sima Chen. |
| `c20` | - | -0.750 | 31 | The person located at billing completes transport paperwork for red discharge packets. |
| `c17` | - | -0.821 | 29 | The red discharge packet means the patient needs transport paperwork. |
| `c30` | - | -0.977 | 29 | Microbiology batches after-hours samples under code M-14. |
| `c18` | - | -0.769 | 29 | Transport paperwork is completed by the mobility coordinator. |
| `c36` | selected | -0.085 | 31 | Bronze chart stickers are cleared by the triage physician before insurance review. |
| `c04` | - | -0.232 | 31 | A badge denial for visiting students should be fixed at reception by the visitor badge desk. |
| `c38` | - | -0.451 | 30 | Language assistance is booked by the cultural services desk. |
| `c28` | - | -0.904 | 31 | Silver consent telehealth follow-up slots open through in-person surgery clearance. |
| `c27` | - | -0.782 | 29 | Remote-care scheduling uses the amber queue after noon. |
| `c01` | - | -0.791 | 27 | Blue-lanyard observers receive a temporary pass from the learning office, not from reception. |

### PASS content_02_clinic_access / c_q12_three_hop / budget 1024

Question: Who signs before slate courier envelopes reach the night audit path?

Selected: `['c13', 'c14', 'c15', 'c16', 'c31', 'c36']`
Tokens: `180/1024`
F1: `0.800` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `[]`

Score breakdown:

- individual: `10.634`
- pair synergy: `5.227`
- triple synergy: `0.278`
- redundancy penalty: `1.535`
- total: `14.603`

Improvement hint: Successful selection; inspect extra chunks only if precision or token cost becomes the priority.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `c16` | selected, optional | 3.754 | 31 | Slate courier envelopes before night audit should be signed at the blood desk. |
| `c13` | selected, required | 2.673 | 27 | Courier envelopes marked slate are routed to diagnostic imaging. |
| `c15` | selected, required | 2.148 | 31 | The archive cart is signed out by Omar Singh before the night audit. |
| `c14` | selected, required | 2.146 | 30 | Diagnostic imaging sends slate envelopes to the archive cart near lift B. |
| `c31` | selected | -0.033 | 30 | Code M-14 batches are collected by night runner Sima Chen. |
| `c20` | - | -0.720 | 31 | The person located at billing completes transport paperwork for red discharge packets. |
| `c17` | - | -0.793 | 29 | The red discharge packet means the patient needs transport paperwork. |
| `c30` | - | -0.949 | 29 | Microbiology batches after-hours samples under code M-14. |
| `c18` | - | -0.740 | 29 | Transport paperwork is completed by the mobility coordinator. |
| `c36` | selected | -0.054 | 31 | Bronze chart stickers are cleared by the triage physician before insurance review. |
| `c04` | - | -0.202 | 31 | A badge denial for visiting students should be fixed at reception by the visitor badge desk. |
| `c38` | - | -0.422 | 30 | Language assistance is booked by the cultural services desk. |
| `c28` | - | -0.873 | 31 | Silver consent telehealth follow-up slots open through in-person surgery clearance. |
| `c27` | - | -0.754 | 29 | Remote-care scheduling uses the amber queue after noon. |
| `c01` | - | -0.764 | 27 | Blue-lanyard observers receive a temporary pass from the learning office, not from reception. |

### FAIL content_02_clinic_access / c_q13_three_hop / budget 128

Question: Where is the reviewer for a bronze insurance chart sticker located?

Selected: `['c33', 'c34', 'c36', 'c37']`
Tokens: `116/128`
F1: `0.706` Required recall: `0.667`
Missing required units: `['office']`
Selected distractors: `[]`

Score breakdown:

- individual: `8.569`
- pair synergy: `2.377`
- triple synergy: `0.000`
- redundancy penalty: `0.939`
- total: `10.007`

Improvement hint: Tight-budget tradeoff; improve importance ranking so required evidence beats optional/filler chunks.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `c33` | selected, required | 3.709 | 28 | The bronze sticker on a chart means insurance review is pending. |
| `c36` | selected, optional | 2.997 | 31 | Bronze chart stickers are cleared by the triage physician before insurance review. |
| `c37` | selected | 1.281 | 28 | The pearl sticker means language assistance is requested. |
| `c34` | selected, required | 0.583 | 29 | Pending insurance reviews are handled by claims liaison Mateo Ruiz. |
| `c20` | - | -0.373 | 31 | The person located at billing completes transport paperwork for red discharge packets. |
| `c24` | - | -0.892 | 30 | Expired wristband replacement points to the security map label after a badge denial. |
| `c40` | - | 0.118 | 31 | Pearl sticker language help roster requests go to financial counseling at registration. |
| `c17` | - | -0.637 | 29 | The red discharge packet means the patient needs transport paperwork. |
| `c18` | - | -1.046 | 29 | Transport paperwork is completed by the mobility coordinator. |
| `c38` | - | -0.521 | 30 | Language assistance is booked by the cultural services desk. |
| `c21` | - | -0.986 | 27 | Expired wristbands are replaced at the intake island. |
| `c35` | required | -0.283 | 30 | Mateo Ruiz works from the small office behind registration. |
| `c04` | - | -1.112 | 31 | A badge denial for visiting students should be fixed at reception by the visitor badge desk. |
| `c22` | - | -1.086 | 29 | The intake island is labeled Coral on the floor map. |
| `c29` | - | -0.688 | 27 | A lavender tray tag means samples go to microbiology. |

### PASS content_02_clinic_access / c_q13_three_hop / budget 256

Question: Where is the reviewer for a bronze insurance chart sticker located?

Selected: `['c20', 'c33', 'c34', 'c35', 'c36', 'c37', 'c40']`
Tokens: `208/256`
F1: `0.727` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `[]`

Score breakdown:

- individual: `8.844`
- pair synergy: `6.033`
- triple synergy: `0.833`
- redundancy penalty: `1.496`
- total: `14.214`

Improvement hint: Successful selection; inspect extra chunks only if precision or token cost becomes the priority.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `c33` | selected, required | 3.818 | 28 | The bronze sticker on a chart means insurance review is pending. |
| `c36` | selected, optional | 3.118 | 31 | Bronze chart stickers are cleared by the triage physician before insurance review. |
| `c37` | selected | 1.391 | 28 | The pearl sticker means language assistance is requested. |
| `c34` | selected, required | 0.696 | 29 | Pending insurance reviews are handled by claims liaison Mateo Ruiz. |
| `c20` | selected | -0.252 | 31 | The person located at billing completes transport paperwork for red discharge packets. |
| `c24` | - | -0.775 | 30 | Expired wristband replacement points to the security map label after a badge denial. |
| `c40` | selected | 0.239 | 31 | Pearl sticker language help roster requests go to financial counseling at registration. |
| `c17` | - | -0.524 | 29 | The red discharge packet means the patient needs transport paperwork. |
| `c18` | - | -0.933 | 29 | Transport paperwork is completed by the mobility coordinator. |
| `c38` | - | -0.404 | 30 | Language assistance is booked by the cultural services desk. |
| `c35` | selected, required | -0.166 | 30 | Mateo Ruiz works from the small office behind registration. |
| `c21` | - | -0.880 | 27 | Expired wristbands are replaced at the intake island. |
| `c04` | - | -0.991 | 31 | A badge denial for visiting students should be fixed at reception by the visitor badge desk. |
| `c22` | - | -0.973 | 29 | The intake island is labeled Coral on the floor map. |
| `c29` | - | -0.583 | 27 | A lavender tray tag means samples go to microbiology. |

### PASS content_02_clinic_access / c_q13_three_hop / budget 512

Question: Where is the reviewer for a bronze insurance chart sticker located?

Selected: `['c20', 'c33', 'c34', 'c35', 'c36', 'c37', 'c38', 'c40']`
Tokens: `238/512`
F1: `0.667` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `[]`

Score breakdown:

- individual: `8.905`
- pair synergy: `6.683`
- triple synergy: `0.833`
- redundancy penalty: `1.796`
- total: `14.626`

Improvement hint: Successful selection; inspect extra chunks only if precision or token cost becomes the priority.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `c33` | selected, required | 3.873 | 28 | The bronze sticker on a chart means insurance review is pending. |
| `c36` | selected, optional | 3.178 | 31 | Bronze chart stickers are cleared by the triage physician before insurance review. |
| `c37` | selected | 1.445 | 28 | The pearl sticker means language assistance is requested. |
| `c34` | selected, required | 0.752 | 29 | Pending insurance reviews are handled by claims liaison Mateo Ruiz. |
| `c20` | selected | -0.191 | 31 | The person located at billing completes transport paperwork for red discharge packets. |
| `c24` | - | -0.716 | 30 | Expired wristband replacement points to the security map label after a badge denial. |
| `c40` | selected | 0.299 | 31 | Pearl sticker language help roster requests go to financial counseling at registration. |
| `c17` | - | -0.467 | 29 | The red discharge packet means the patient needs transport paperwork. |
| `c18` | - | -0.876 | 29 | Transport paperwork is completed by the mobility coordinator. |
| `c38` | selected | -0.345 | 30 | Language assistance is booked by the cultural services desk. |
| `c35` | selected, required | -0.107 | 30 | Mateo Ruiz works from the small office behind registration. |
| `c21` | - | -0.828 | 27 | Expired wristbands are replaced at the intake island. |
| `c04` | - | -0.930 | 31 | A badge denial for visiting students should be fixed at reception by the visitor badge desk. |
| `c22` | - | -0.916 | 29 | The intake island is labeled Coral on the floor map. |
| `c29` | - | -0.530 | 27 | A lavender tray tag means samples go to microbiology. |

### PASS content_02_clinic_access / c_q13_three_hop / budget 1024

Question: Where is the reviewer for a bronze insurance chart sticker located?

Selected: `['c20', 'c33', 'c34', 'c35', 'c36', 'c37', 'c38', 'c40']`
Tokens: `238/1024`
F1: `0.667` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `[]`

Score breakdown:

- individual: `9.137`
- pair synergy: `6.683`
- triple synergy: `0.833`
- redundancy penalty: `1.796`
- total: `14.858`

Improvement hint: Successful selection; inspect extra chunks only if precision or token cost becomes the priority.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `c33` | selected, required | 3.900 | 28 | The bronze sticker on a chart means insurance review is pending. |
| `c36` | selected, optional | 3.208 | 31 | Bronze chart stickers are cleared by the triage physician before insurance review. |
| `c37` | selected | 1.473 | 28 | The pearl sticker means language assistance is requested. |
| `c34` | selected, required | 0.781 | 29 | Pending insurance reviews are handled by claims liaison Mateo Ruiz. |
| `c20` | selected | -0.161 | 31 | The person located at billing completes transport paperwork for red discharge packets. |
| `c24` | - | -0.687 | 30 | Expired wristband replacement points to the security map label after a badge denial. |
| `c40` | selected | 0.330 | 31 | Pearl sticker language help roster requests go to financial counseling at registration. |
| `c17` | - | -0.439 | 29 | The red discharge packet means the patient needs transport paperwork. |
| `c18` | - | -0.848 | 29 | Transport paperwork is completed by the mobility coordinator. |
| `c38` | selected | -0.316 | 30 | Language assistance is booked by the cultural services desk. |
| `c35` | selected, required | -0.078 | 30 | Mateo Ruiz works from the small office behind registration. |
| `c21` | - | -0.801 | 27 | Expired wristbands are replaced at the intake island. |
| `c04` | - | -0.900 | 31 | A badge denial for visiting students should be fixed at reception by the visitor badge desk. |
| `c22` | - | -0.888 | 29 | The intake island is labeled Coral on the floor map. |
| `c29` | - | -0.504 | 27 | A lavender tray tag means samples go to microbiology. |

### PASS content_02_clinic_access / c_q14_three_hop / budget 128

Question: Who opens follow-up slots connected to a silver consent sleeve after noon?

Selected: `['c25', 'c26', 'c27', 'c28']`
Tokens: `118/128`
F1: `1.000` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `[]`

Score breakdown:

- individual: `10.198`
- pair synergy: `4.061`
- triple synergy: `0.250`
- redundancy penalty: `1.247`
- total: `13.262`

Improvement hint: Successful selection; inspect extra chunks only if precision or token cost becomes the priority.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `c25` | selected, required | 3.666 | 28 | The silver consent sleeve indicates telehealth follow-up. |
| `c28` | selected, optional | 3.680 | 31 | Silver consent telehealth follow-up slots open through in-person surgery clearance. |
| `c26` | selected, required | 2.039 | 30 | Telehealth follow-up slots are opened by the remote-care scheduler. |
| `c27` | selected, required | 0.813 | 29 | Remote-care scheduling uses the amber queue after noon. |
| `c05` | - | -0.131 | 27 | The sedation cabinet releases keys after the orange ledger is initialed. |
| `c01` | - | -0.918 | 27 | Blue-lanyard observers receive a temporary pass from the learning office, not from reception. |
| `c08` | - | -1.005 | 30 | Sedation cabinet keys are approved by pharmacy when the orange ledger is missing. |
| `c06` | - | -0.979 | 28 | Orange ledger initials are supplied by the recovery charge nurse. |
| `c09` | - | -0.107 | 28 | The quiet room uses a dove marker on the scheduling board. |
| `c24` | - | -0.151 | 30 | Expired wristband replacement points to the security map label after a badge denial. |
| `c11` | - | -0.176 | 30 | Behavioral-health overflow is coordinated by Lina Park after 18:00. |
| `c02` | - | -1.009 | 29 | The learning office is called the North Annex counter in weekend notes. |
| `c12` | - | -0.238 | 31 | The quiet room after evening overflow is handled by the triage nurse for pediatric fever cases. |
| `c30` | - | -0.249 | 29 | Microbiology batches after-hours samples under code M-14. |
| `c35` | - | -1.124 | 30 | Mateo Ruiz works from the small office behind registration. |

### PASS content_02_clinic_access / c_q14_three_hop / budget 256

Question: Who opens follow-up slots connected to a silver consent sleeve after noon?

Selected: `['c05', 'c11', 'c12', 'c24', 'c25', 'c26', 'c27', 'c28']`
Tokens: `236/256`
F1: `0.667` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `[]`

Score breakdown:

- individual: `10.425`
- pair synergy: `8.162`
- triple synergy: `1.250`
- redundancy penalty: `1.964`
- total: `17.872`

Improvement hint: Successful selection; inspect extra chunks only if precision or token cost becomes the priority.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `c25` | selected, required | 3.776 | 28 | The silver consent sleeve indicates telehealth follow-up. |
| `c28` | selected, optional | 3.801 | 31 | Silver consent telehealth follow-up slots open through in-person surgery clearance. |
| `c26` | selected, required | 2.157 | 30 | Telehealth follow-up slots are opened by the remote-care scheduler. |
| `c27` | selected, required | 0.926 | 29 | Remote-care scheduling uses the amber queue after noon. |
| `c05` | selected | -0.025 | 27 | The sedation cabinet releases keys after the orange ledger is initialed. |
| `c01` | - | -0.813 | 27 | Blue-lanyard observers receive a temporary pass from the learning office, not from reception. |
| `c08` | - | -0.887 | 30 | Sedation cabinet keys are approved by pharmacy when the orange ledger is missing. |
| `c06` | - | -0.870 | 28 | Orange ledger initials are supplied by the recovery charge nurse. |
| `c09` | - | 0.002 | 28 | The quiet room uses a dove marker on the scheduling board. |
| `c24` | selected | -0.034 | 30 | Expired wristband replacement points to the security map label after a badge denial. |
| `c11` | selected | -0.059 | 30 | Behavioral-health overflow is coordinated by Lina Park after 18:00. |
| `c12` | selected | -0.117 | 31 | The quiet room after evening overflow is handled by the triage nurse for pediatric fever cases. |
| `c02` | - | -0.896 | 29 | The learning office is called the North Annex counter in weekend notes. |
| `c30` | - | -0.136 | 29 | Microbiology batches after-hours samples under code M-14. |
| `c35` | - | -1.007 | 30 | Mateo Ruiz works from the small office behind registration. |

### PASS content_02_clinic_access / c_q14_three_hop / budget 512

Question: Who opens follow-up slots connected to a silver consent sleeve after noon?

Selected: `['c05', 'c09', 'c11', 'c12', 'c24', 'c25', 'c26', 'c27', 'c28', 'c30']`
Tokens: `293/512`
F1: `0.571` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `[]`

Score breakdown:

- individual: `10.863`
- pair synergy: `10.263`
- triple synergy: `1.500`
- redundancy penalty: `2.606`
- total: `20.019`

Improvement hint: Successful selection; inspect extra chunks only if precision or token cost becomes the priority.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `c25` | selected, required | 3.830 | 28 | The silver consent sleeve indicates telehealth follow-up. |
| `c28` | selected, optional | 3.862 | 31 | Silver consent telehealth follow-up slots open through in-person surgery clearance. |
| `c26` | selected, required | 2.215 | 30 | Telehealth follow-up slots are opened by the remote-care scheduler. |
| `c27` | selected, required | 0.983 | 29 | Remote-care scheduling uses the amber queue after noon. |
| `c05` | selected | 0.028 | 27 | The sedation cabinet releases keys after the orange ledger is initialed. |
| `c01` | - | -0.760 | 27 | Blue-lanyard observers receive a temporary pass from the learning office, not from reception. |
| `c08` | - | -0.829 | 30 | Sedation cabinet keys are approved by pharmacy when the orange ledger is missing. |
| `c06` | - | -0.815 | 28 | Orange ledger initials are supplied by the recovery charge nurse. |
| `c09` | selected | 0.057 | 28 | The quiet room uses a dove marker on the scheduling board. |
| `c24` | selected | 0.025 | 30 | Expired wristband replacement points to the security map label after a badge denial. |
| `c11` | selected | -0.000 | 30 | Behavioral-health overflow is coordinated by Lina Park after 18:00. |
| `c12` | selected | -0.057 | 31 | The quiet room after evening overflow is handled by the triage nurse for pediatric fever cases. |
| `c02` | - | -0.839 | 29 | The learning office is called the North Annex counter in weekend notes. |
| `c30` | selected | -0.080 | 29 | Microbiology batches after-hours samples under code M-14. |
| `c35` | - | -0.949 | 30 | Mateo Ruiz works from the small office behind registration. |

### PASS content_02_clinic_access / c_q14_three_hop / budget 1024

Question: Who opens follow-up slots connected to a silver consent sleeve after noon?

Selected: `['c05', 'c09', 'c11', 'c12', 'c24', 'c25', 'c26', 'c27', 'c28', 'c30']`
Tokens: `293/1024`
F1: `0.571` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `[]`

Score breakdown:

- individual: `11.149`
- pair synergy: `10.263`
- triple synergy: `1.500`
- redundancy penalty: `2.606`
- total: `20.305`

Improvement hint: Successful selection; inspect extra chunks only if precision or token cost becomes the priority.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `c25` | selected, required | 3.858 | 28 | The silver consent sleeve indicates telehealth follow-up. |
| `c28` | selected, optional | 3.892 | 31 | Silver consent telehealth follow-up slots open through in-person surgery clearance. |
| `c26` | selected, required | 2.244 | 30 | Telehealth follow-up slots are opened by the remote-care scheduler. |
| `c27` | selected, required | 1.011 | 29 | Remote-care scheduling uses the amber queue after noon. |
| `c05` | selected | 0.054 | 27 | The sedation cabinet releases keys after the orange ledger is initialed. |
| `c01` | - | -0.733 | 27 | Blue-lanyard observers receive a temporary pass from the learning office, not from reception. |
| `c08` | - | -0.799 | 30 | Sedation cabinet keys are approved by pharmacy when the orange ledger is missing. |
| `c06` | - | -0.788 | 28 | Orange ledger initials are supplied by the recovery charge nurse. |
| `c09` | selected | 0.084 | 28 | The quiet room uses a dove marker on the scheduling board. |
| `c24` | selected | 0.054 | 30 | Expired wristband replacement points to the security map label after a badge denial. |
| `c11` | selected | 0.029 | 30 | Behavioral-health overflow is coordinated by Lina Park after 18:00. |
| `c12` | selected | -0.026 | 31 | The quiet room after evening overflow is handled by the triage nurse for pediatric fever cases. |
| `c02` | - | -0.811 | 29 | The learning office is called the North Annex counter in weekend notes. |
| `c30` | selected | -0.051 | 29 | Microbiology batches after-hours samples under code M-14. |
| `c35` | - | -0.919 | 30 | Mateo Ruiz works from the small office behind registration. |

### PASS content_02_clinic_access / c_q15_three_hop / budget 128

Question: Which person collects the coded batch for lavender tray samples?

Selected: `['c29', 'c30', 'c31', 'c32']`
Tokens: `116/128`
F1: `1.000` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `[]`

Score breakdown:

- individual: `6.561`
- pair synergy: `1.837`
- triple synergy: `0.000`
- redundancy penalty: `1.050`
- total: `7.347`

Improvement hint: Successful selection; inspect extra chunks only if precision or token cost becomes the priority.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `c29` | selected, required | 2.789 | 27 | A lavender tray tag means samples go to microbiology. |
| `c32` | selected, optional | 2.729 | 30 | Lavender tray tags mean samples go to radiology during downtime. |
| `c30` | selected, required | 0.534 | 29 | Microbiology batches after-hours samples under code M-14. |
| `c20` | - | -0.423 | 31 | The person located at billing completes transport paperwork for red discharge packets. |
| `c28` | - | -0.148 | 31 | Silver consent telehealth follow-up slots open through in-person surgery clearance. |
| `c31` | selected, required | 0.509 | 30 | Code M-14 batches are collected by night runner Sima Chen. |
| `c25` | - | -1.028 | 28 | The silver consent sleeve indicates telehealth follow-up. |
| `c17` | - | 0.626 | 29 | The red discharge packet means the patient needs transport paperwork. |
| `c26` | - | -1.082 | 30 | Telehealth follow-up slots are opened by the remote-care scheduler. |
| `c18` | - | 0.188 | 29 | Transport paperwork is completed by the mobility coordinator. |
| `c37` | - | -0.550 | 28 | The pearl sticker means language assistance is requested. |
| `c27` | - | -0.630 | 29 | Remote-care scheduling uses the amber queue after noon. |
| `c40` | - | -0.619 | 31 | Pearl sticker language help roster requests go to financial counseling at registration. |
| `c16` | - | -0.980 | 31 | Slate courier envelopes before night audit should be signed at the blood desk. |
| `c05` | - | -0.682 | 27 | The sedation cabinet releases keys after the orange ledger is initialed. |

### PASS content_02_clinic_access / c_q15_three_hop / budget 256

Question: Which person collects the coded batch for lavender tray samples?

Selected: `['c17', 'c18', 'c20', 'c28', 'c29', 'c30', 'c31', 'c32']`
Tokens: `236/256`
F1: `0.667` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `[]`

Score breakdown:

- individual: `7.727`
- pair synergy: `5.571`
- triple synergy: `0.000`
- redundancy penalty: `2.064`
- total: `11.234`

Improvement hint: Successful selection; inspect extra chunks only if precision or token cost becomes the priority.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `c29` | selected, required | 2.894 | 27 | A lavender tray tag means samples go to microbiology. |
| `c32` | selected, optional | 2.846 | 30 | Lavender tray tags mean samples go to radiology during downtime. |
| `c30` | selected, required | 0.647 | 29 | Microbiology batches after-hours samples under code M-14. |
| `c20` | selected | -0.302 | 31 | The person located at billing completes transport paperwork for red discharge packets. |
| `c28` | selected | -0.027 | 31 | Silver consent telehealth follow-up slots open through in-person surgery clearance. |
| `c31` | selected, required | 0.626 | 30 | Code M-14 batches are collected by night runner Sima Chen. |
| `c25` | - | -0.919 | 28 | The silver consent sleeve indicates telehealth follow-up. |
| `c17` | selected | 0.739 | 29 | The red discharge packet means the patient needs transport paperwork. |
| `c26` | - | -0.965 | 30 | Telehealth follow-up slots are opened by the remote-care scheduler. |
| `c18` | selected | 0.302 | 29 | Transport paperwork is completed by the mobility coordinator. |
| `c37` | - | -0.441 | 28 | The pearl sticker means language assistance is requested. |
| `c27` | - | -0.517 | 29 | Remote-care scheduling uses the amber queue after noon. |
| `c40` | - | -0.498 | 31 | Pearl sticker language help roster requests go to financial counseling at registration. |
| `c16` | - | -0.859 | 31 | Slate courier envelopes before night audit should be signed at the blood desk. |
| `c05` | - | -0.576 | 27 | The sedation cabinet releases keys after the orange ledger is initialed. |

### PASS content_02_clinic_access / c_q15_three_hop / budget 512

Question: Which person collects the coded batch for lavender tray samples?

Selected: `['c17', 'c18', 'c20', 'c28', 'c29', 'c30', 'c31', 'c32', 'c37', 'c40']`
Tokens: `295/512`
F1: `0.571` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `[]`

Score breakdown:

- individual: `7.364`
- pair synergy: `6.984`
- triple synergy: `0.000`
- redundancy penalty: `2.636`
- total: `11.712`

Improvement hint: Successful selection; inspect extra chunks only if precision or token cost becomes the priority.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `c29` | selected, required | 2.947 | 27 | A lavender tray tag means samples go to microbiology. |
| `c32` | selected, optional | 2.905 | 30 | Lavender tray tags mean samples go to radiology during downtime. |
| `c30` | selected, required | 0.704 | 29 | Microbiology batches after-hours samples under code M-14. |
| `c20` | selected | -0.241 | 31 | The person located at billing completes transport paperwork for red discharge packets. |
| `c28` | selected | 0.034 | 31 | Silver consent telehealth follow-up slots open through in-person surgery clearance. |
| `c31` | selected, required | 0.685 | 30 | Code M-14 batches are collected by night runner Sima Chen. |
| `c25` | - | -0.864 | 28 | The silver consent sleeve indicates telehealth follow-up. |
| `c17` | selected | 0.796 | 29 | The red discharge packet means the patient needs transport paperwork. |
| `c26` | - | -0.906 | 30 | Telehealth follow-up slots are opened by the remote-care scheduler. |
| `c18` | selected | 0.358 | 29 | Transport paperwork is completed by the mobility coordinator. |
| `c37` | selected | -0.386 | 28 | The pearl sticker means language assistance is requested. |
| `c27` | - | -0.461 | 29 | Remote-care scheduling uses the amber queue after noon. |
| `c40` | selected | -0.437 | 31 | Pearl sticker language help roster requests go to financial counseling at registration. |
| `c16` | - | -0.799 | 31 | Slate courier envelopes before night audit should be signed at the blood desk. |
| `c05` | - | -0.523 | 27 | The sedation cabinet releases keys after the orange ledger is initialed. |

### PASS content_02_clinic_access / c_q15_three_hop / budget 1024

Question: Which person collects the coded batch for lavender tray samples?

Selected: `['c17', 'c18', 'c20', 'c28', 'c29', 'c30', 'c31', 'c32', 'c37', 'c40']`
Tokens: `295/1024`
F1: `0.571` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `[]`

Score breakdown:

- individual: `7.652`
- pair synergy: `6.984`
- triple synergy: `0.000`
- redundancy penalty: `2.636`
- total: `12.000`

Improvement hint: Successful selection; inspect extra chunks only if precision or token cost becomes the priority.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `c29` | selected, required | 2.973 | 27 | A lavender tray tag means samples go to microbiology. |
| `c32` | selected, optional | 2.934 | 30 | Lavender tray tags mean samples go to radiology during downtime. |
| `c30` | selected, required | 0.732 | 29 | Microbiology batches after-hours samples under code M-14. |
| `c20` | selected | -0.211 | 31 | The person located at billing completes transport paperwork for red discharge packets. |
| `c28` | selected | 0.064 | 31 | Silver consent telehealth follow-up slots open through in-person surgery clearance. |
| `c31` | selected, required | 0.714 | 30 | Code M-14 batches are collected by night runner Sima Chen. |
| `c25` | - | -0.837 | 28 | The silver consent sleeve indicates telehealth follow-up. |
| `c17` | selected | 0.824 | 29 | The red discharge packet means the patient needs transport paperwork. |
| `c26` | - | -0.877 | 30 | Telehealth follow-up slots are opened by the remote-care scheduler. |
| `c18` | selected | 0.387 | 29 | Transport paperwork is completed by the mobility coordinator. |
| `c37` | selected | -0.359 | 28 | The pearl sticker means language assistance is requested. |
| `c27` | - | -0.432 | 29 | Remote-care scheduling uses the amber queue after noon. |
| `c40` | selected | -0.407 | 31 | Pearl sticker language help roster requests go to financial counseling at registration. |
| `c16` | - | -0.768 | 31 | Slate courier envelopes before night audit should be signed at the blood desk. |
| `c05` | - | -0.497 | 27 | The sedation cabinet releases keys after the orange ledger is initialed. |
