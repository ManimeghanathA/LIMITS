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

- individual: `9.645`
- pair synergy: `2.742`
- triple synergy: `0.000`
- redundancy penalty: `1.128`
- total: `11.260`

Improvement hint: Add wrong-context or contradiction-aware features; a distractor beat required evidence.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `p01` | selected, required | 4.614 | 27 | The Atlas night support desk moved to Bay 7 after the January ventilation review. |
| `p21` | selected, distractor | 2.299 | 31 | A retired memo says the Atlas night desk moved to Bay 5, but that memo was withdrawn. |
| `p16` | selected, optional | 1.175 | 30 | Bay 4 still hosts the legacy simulator desk and gets misdirected support calls. |
| `p35` | selected, distractor | 1.557 | 33 | A facilities bulletin mentions Bay 7 catering deliveries unrelated to the night desk. |
| `p13` | optional | 0.597 | 31 | The old Bay 5 help-desk sign remains on a storage door near the simulator. |
| `p28` | - | 0.112 | 29 | Ground power files Binder Blue after the battery cart is returned. |
| `p02` | - | 0.079 | 28 | Mira Patel is the duty lead who approves urgent avionics replacement requests for Atlas. |
| `p24` | - | 0.079 | 29 | Dev Rao signs the release sheet after the structural team entry appears. |
| `p31` | - | 0.079 | 29 | The ground power team owns the battery health printout process for Atlas staging. |
| `p04` | - | 0.051 | 29 | Cage D opens only after the secure tool room records Mira Patel's approval code. |

### PASS content_01_aero_support / q01_direct / budget 256

Question: Where is the Atlas night support desk after the ventilation review?

Selected: `['p01', 'p02', 'p04', 'p16', 'p21', 'p28', 'p31', 'p35']`
Tokens: `236/256`
F1: `0.400` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `['p21', 'p35']`

Score breakdown:

- individual: `9.966`
- pair synergy: `8.358`
- triple synergy: `2.500`
- redundancy penalty: `1.872`
- total: `18.952`

Improvement hint: Add wrong-context or contradiction-aware features; a distractor beat required evidence.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `p01` | selected, required | 4.614 | 27 | The Atlas night support desk moved to Bay 7 after the January ventilation review. |
| `p21` | selected, distractor | 2.299 | 31 | A retired memo says the Atlas night desk moved to Bay 5, but that memo was withdrawn. |
| `p16` | selected, optional | 1.175 | 30 | Bay 4 still hosts the legacy simulator desk and gets misdirected support calls. |
| `p35` | selected, distractor | 1.557 | 33 | A facilities bulletin mentions Bay 7 catering deliveries unrelated to the night desk. |
| `p13` | optional | 0.597 | 31 | The old Bay 5 help-desk sign remains on a storage door near the simulator. |
| `p28` | selected | 0.112 | 29 | Ground power files Binder Blue after the battery cart is returned. |
| `p02` | selected | 0.079 | 28 | Mira Patel is the duty lead who approves urgent avionics replacement requests for Atlas. |
| `p24` | - | 0.079 | 29 | Dev Rao signs the release sheet after the structural team entry appears. |
| `p31` | selected | 0.079 | 29 | The ground power team owns the battery health printout process for Atlas staging. |
| `p04` | selected | 0.051 | 29 | Cage D opens only after the secure tool room records Mira Patel's approval code. |

### PASS content_01_aero_support / q01_direct / budget 512

Question: Where is the Atlas night support desk after the ventilation review?

Selected: `['p01', 'p02', 'p04', 'p13', 'p16', 'p21', 'p24', 'p28', 'p31', 'p35']`
Tokens: `296/512`
F1: `0.462` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `['p21', 'p35']`

Score breakdown:

- individual: `10.641`
- pair synergy: `12.821`
- triple synergy: `4.643`
- redundancy penalty: `2.668`
- total: `25.437`

Improvement hint: Add wrong-context or contradiction-aware features; a distractor beat required evidence.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `p01` | selected, required | 4.614 | 27 | The Atlas night support desk moved to Bay 7 after the January ventilation review. |
| `p21` | selected, distractor | 2.299 | 31 | A retired memo says the Atlas night desk moved to Bay 5, but that memo was withdrawn. |
| `p16` | selected, optional | 1.175 | 30 | Bay 4 still hosts the legacy simulator desk and gets misdirected support calls. |
| `p35` | selected, distractor | 1.557 | 33 | A facilities bulletin mentions Bay 7 catering deliveries unrelated to the night desk. |
| `p13` | selected, optional | 0.597 | 31 | The old Bay 5 help-desk sign remains on a storage door near the simulator. |
| `p28` | selected | 0.112 | 29 | Ground power files Binder Blue after the battery cart is returned. |
| `p02` | selected | 0.079 | 28 | Mira Patel is the duty lead who approves urgent avionics replacement requests for Atlas. |
| `p24` | selected | 0.079 | 29 | Dev Rao signs the release sheet after the structural team entry appears. |
| `p31` | selected | 0.079 | 29 | The ground power team owns the battery health printout process for Atlas staging. |
| `p04` | selected | 0.051 | 29 | Cage D opens only after the secure tool room records Mira Patel's approval code. |

### PASS content_01_aero_support / q01_direct / budget 1024

Question: Where is the Atlas night support desk after the ventilation review?

Selected: `['p01', 'p02', 'p04', 'p13', 'p16', 'p21', 'p24', 'p28', 'p31', 'p35']`
Tokens: `296/1024`
F1: `0.462` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `['p21', 'p35']`

Score breakdown:

- individual: `10.641`
- pair synergy: `12.821`
- triple synergy: `4.643`
- redundancy penalty: `2.668`
- total: `25.437`

Improvement hint: Add wrong-context or contradiction-aware features; a distractor beat required evidence.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `p01` | selected, required | 4.614 | 27 | The Atlas night support desk moved to Bay 7 after the January ventilation review. |
| `p21` | selected, distractor | 2.299 | 31 | A retired memo says the Atlas night desk moved to Bay 5, but that memo was withdrawn. |
| `p16` | selected, optional | 1.175 | 30 | Bay 4 still hosts the legacy simulator desk and gets misdirected support calls. |
| `p35` | selected, distractor | 1.557 | 33 | A facilities bulletin mentions Bay 7 catering deliveries unrelated to the night desk. |
| `p13` | selected, optional | 0.597 | 31 | The old Bay 5 help-desk sign remains on a storage door near the simulator. |
| `p28` | selected | 0.112 | 29 | Ground power files Binder Blue after the battery cart is returned. |
| `p02` | selected | 0.079 | 28 | Mira Patel is the duty lead who approves urgent avionics replacement requests for Atlas. |
| `p24` | selected | 0.079 | 29 | Dev Rao signs the release sheet after the structural team entry appears. |
| `p31` | selected | 0.079 | 29 | The ground power team owns the battery health printout process for Atlas staging. |
| `p04` | selected | 0.051 | 29 | Cage D opens only after the secure tool room records Mira Patel's approval code. |

### PASS content_01_aero_support / q02_direct / budget 128

Question: Who approves urgent avionics replacement requests for Atlas?

Selected: `['p02', 'p03', 'p26', 'p40']`
Tokens: `115/128`
F1: `0.667` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `[]`

Score breakdown:

- individual: `12.536`
- pair synergy: `2.998`
- triple synergy: `0.000`
- redundancy penalty: `1.218`
- total: `14.316`

Improvement hint: Successful selection; inspect extra chunks only if precision or token cost becomes the priority.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `p02` | selected, required | 4.600 | 28 | Mira Patel is the duty lead who approves urgent avionics replacement requests for Atlas. |
| `p40` | selected, optional | 2.650 | 29 | Urgent replacement requests are marked red before they reach Mira Patel for approval. |
| `p03` | selected | 2.643 | 27 | Approved urgent avionics replacements are stored in Cage D. |
| `p26` | selected | 2.643 | 31 | A superseded training note says urgent avionics replacements are stored in Cage C. |
| `p14` | optional | 0.750 | 32 | A parts summary mentions Mira Patel and Cage D but says she approves hydraulic seals. |
| `p25` | - | 0.707 | 31 | Routine avionics labels are kept in the general parts cabinet, not the restricted cage. |
| `p23` | - | 0.486 | 30 | Torque kits are tracked by the secure tool room but are not stored in Cage D. |
| `p01` | - | 0.150 | 27 | The Atlas night support desk moved to Bay 7 after the January ventilation review. |
| `p31` | - | 0.150 | 29 | The ground power team owns the battery health printout process for Atlas staging. |
| `p09` | - | 0.150 | 30 | Atlas field reports link the aft temperature warning to insulation rubbing the left harness. |

### PASS content_01_aero_support / q02_direct / budget 256

Question: Who approves urgent avionics replacement requests for Atlas?

Selected: `['p02', 'p03', 'p09', 'p14', 'p25', 'p26', 'p31', 'p40']`
Tokens: `237/256`
F1: `0.545` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `[]`

Score breakdown:

- individual: `14.293`
- pair synergy: `10.462`
- triple synergy: `3.542`
- redundancy penalty: `2.334`
- total: `25.963`

Improvement hint: Successful selection; inspect extra chunks only if precision or token cost becomes the priority.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `p02` | selected, required | 4.600 | 28 | Mira Patel is the duty lead who approves urgent avionics replacement requests for Atlas. |
| `p40` | selected, optional | 2.650 | 29 | Urgent replacement requests are marked red before they reach Mira Patel for approval. |
| `p03` | selected | 2.643 | 27 | Approved urgent avionics replacements are stored in Cage D. |
| `p26` | selected | 2.643 | 31 | A superseded training note says urgent avionics replacements are stored in Cage C. |
| `p14` | selected, optional | 0.750 | 32 | A parts summary mentions Mira Patel and Cage D but says she approves hydraulic seals. |
| `p25` | selected | 0.707 | 31 | Routine avionics labels are kept in the general parts cabinet, not the restricted cage. |
| `p23` | - | 0.486 | 30 | Torque kits are tracked by the secure tool room but are not stored in Cage D. |
| `p01` | - | 0.150 | 27 | The Atlas night support desk moved to Bay 7 after the January ventilation review. |
| `p31` | selected | 0.150 | 29 | The ground power team owns the battery health printout process for Atlas staging. |
| `p09` | selected | 0.150 | 30 | Atlas field reports link the aft temperature warning to insulation rubbing the left harness. |

### PASS content_01_aero_support / q02_direct / budget 512

Question: Who approves urgent avionics replacement requests for Atlas?

Selected: `['p01', 'p02', 'p03', 'p09', 'p14', 'p23', 'p25', 'p26', 'p31', 'p40']`
Tokens: `294/512`
F1: `0.462` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `[]`

Score breakdown:

- individual: `14.929`
- pair synergy: `13.799`
- triple synergy: `5.000`
- redundancy penalty: `3.123`
- total: `30.605`

Improvement hint: Successful selection; inspect extra chunks only if precision or token cost becomes the priority.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `p02` | selected, required | 4.600 | 28 | Mira Patel is the duty lead who approves urgent avionics replacement requests for Atlas. |
| `p40` | selected, optional | 2.650 | 29 | Urgent replacement requests are marked red before they reach Mira Patel for approval. |
| `p03` | selected | 2.643 | 27 | Approved urgent avionics replacements are stored in Cage D. |
| `p26` | selected | 2.643 | 31 | A superseded training note says urgent avionics replacements are stored in Cage C. |
| `p14` | selected, optional | 0.750 | 32 | A parts summary mentions Mira Patel and Cage D but says she approves hydraulic seals. |
| `p25` | selected | 0.707 | 31 | Routine avionics labels are kept in the general parts cabinet, not the restricted cage. |
| `p23` | selected | 0.486 | 30 | Torque kits are tracked by the secure tool room but are not stored in Cage D. |
| `p01` | selected | 0.150 | 27 | The Atlas night support desk moved to Bay 7 after the January ventilation review. |
| `p31` | selected | 0.150 | 29 | The ground power team owns the battery health printout process for Atlas staging. |
| `p09` | selected | 0.150 | 30 | Atlas field reports link the aft temperature warning to insulation rubbing the left harness. |

### PASS content_01_aero_support / q02_direct / budget 1024

Question: Who approves urgent avionics replacement requests for Atlas?

Selected: `['p01', 'p02', 'p03', 'p09', 'p14', 'p23', 'p25', 'p26', 'p31', 'p40']`
Tokens: `294/1024`
F1: `0.462` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `[]`

Score breakdown:

- individual: `14.929`
- pair synergy: `13.799`
- triple synergy: `5.000`
- redundancy penalty: `3.123`
- total: `30.605`

Improvement hint: Successful selection; inspect extra chunks only if precision or token cost becomes the priority.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `p02` | selected, required | 4.600 | 28 | Mira Patel is the duty lead who approves urgent avionics replacement requests for Atlas. |
| `p40` | selected, optional | 2.650 | 29 | Urgent replacement requests are marked red before they reach Mira Patel for approval. |
| `p03` | selected | 2.643 | 27 | Approved urgent avionics replacements are stored in Cage D. |
| `p26` | selected | 2.643 | 31 | A superseded training note says urgent avionics replacements are stored in Cage C. |
| `p14` | selected, optional | 0.750 | 32 | A parts summary mentions Mira Patel and Cage D but says she approves hydraulic seals. |
| `p25` | selected | 0.707 | 31 | Routine avionics labels are kept in the general parts cabinet, not the restricted cage. |
| `p23` | selected | 0.486 | 30 | Torque kits are tracked by the secure tool room but are not stored in Cage D. |
| `p01` | selected | 0.150 | 27 | The Atlas night support desk moved to Bay 7 after the January ventilation review. |
| `p31` | selected | 0.150 | 29 | The ground power team owns the battery health printout process for Atlas staging. |
| `p09` | selected | 0.150 | 30 | Atlas field reports link the aft temperature warning to insulation rubbing the left harness. |

### PASS content_01_aero_support / q03_direct / budget 128

Question: When does winter calibration begin and where is the sensor cart staged?

Selected: `['p05', 'p06', 'p19', 'p32']`
Tokens: `116/128`
F1: `1.000` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `[]`

Score breakdown:

- individual: `9.143`
- pair synergy: `2.710`
- triple synergy: `0.000`
- redundancy penalty: `1.142`
- total: `10.711`

Improvement hint: Successful selection; inspect extra chunks only if precision or token cost becomes the priority.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `p06` | selected, required | 3.893 | 29 | The sensor cart must be staged beside Hangar 2 during winter calibration. |
| `p32` | selected, optional | 1.836 | 30 | The rollout coordinator checks that the sensor cart has arrived before calibration begins. |
| `p05` | selected, required | 1.257 | 28 | The winter calibration window begins at 06:30 before the first engine run. |
| `p19` | selected, required | 2.157 | 29 | Hangar 2 has limited power during winter calibration, so staging must be early. |
| `p18` | optional | 0.957 | 30 | The sensor cart carries tablet mounts and a red charging cable under its tray. |
| `p33` | distractor | 0.529 | 30 | Hangar 3 accepts overnight staging only for paint-shop air filters, not Atlas calibration carts. |
| `p07` | - | 0.200 | 27 | Hangar 2 staging requires the previous evening battery health printout. |
| `p28` | - | 0.112 | 29 | Ground power files Binder Blue after the battery cart is returned. |
| `p30` | - | 0.079 | 28 | Dev Rao is not responsible for catering, hydraulic seal approval, or Orion calibration. |
| `p17` | distractor | 0.079 | 33 | A contractor guide lists 07:15 as a calibration start time, but it applies to Orion. |

### PASS content_01_aero_support / q03_direct / budget 256

Question: When does winter calibration begin and where is the sensor cart staged?

Selected: `['p05', 'p06', 'p18', 'p19', 'p28', 'p30', 'p32', 'p33']`
Tokens: `233/256`
F1: `0.769` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `['p33']`

Score breakdown:

- individual: `10.819`
- pair synergy: `8.047`
- triple synergy: `0.000`
- redundancy penalty: `2.285`
- total: `16.581`

Improvement hint: Add wrong-context or contradiction-aware features; a distractor beat required evidence.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `p06` | selected, required | 3.893 | 29 | The sensor cart must be staged beside Hangar 2 during winter calibration. |
| `p32` | selected, optional | 1.836 | 30 | The rollout coordinator checks that the sensor cart has arrived before calibration begins. |
| `p05` | selected, required | 1.257 | 28 | The winter calibration window begins at 06:30 before the first engine run. |
| `p19` | selected, required | 2.157 | 29 | Hangar 2 has limited power during winter calibration, so staging must be early. |
| `p18` | selected, optional | 0.957 | 30 | The sensor cart carries tablet mounts and a red charging cable under its tray. |
| `p33` | selected, distractor | 0.529 | 30 | Hangar 3 accepts overnight staging only for paint-shop air filters, not Atlas calibration carts. |
| `p07` | - | 0.200 | 27 | Hangar 2 staging requires the previous evening battery health printout. |
| `p28` | selected | 0.112 | 29 | Ground power files Binder Blue after the battery cart is returned. |
| `p30` | selected | 0.079 | 28 | Dev Rao is not responsible for catering, hydraulic seal approval, or Orion calibration. |
| `p17` | distractor | 0.079 | 33 | A contractor guide lists 07:15 as a calibration start time, but it applies to Orion. |

### PASS content_01_aero_support / q03_direct / budget 512

Question: When does winter calibration begin and where is the sensor cart staged?

Selected: `['p05', 'p06', 'p07', 'p17', 'p18', 'p19', 'p28', 'p30', 'p32', 'p33']`
Tokens: `293/512`
F1: `0.667` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `['p17', 'p33']`

Score breakdown:

- individual: `11.098`
- pair synergy: `10.475`
- triple synergy: `0.000`
- redundancy penalty: `3.143`
- total: `18.429`

Improvement hint: Add wrong-context or contradiction-aware features; a distractor beat required evidence.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `p06` | selected, required | 3.893 | 29 | The sensor cart must be staged beside Hangar 2 during winter calibration. |
| `p32` | selected, optional | 1.836 | 30 | The rollout coordinator checks that the sensor cart has arrived before calibration begins. |
| `p05` | selected, required | 1.257 | 28 | The winter calibration window begins at 06:30 before the first engine run. |
| `p19` | selected, required | 2.157 | 29 | Hangar 2 has limited power during winter calibration, so staging must be early. |
| `p18` | selected, optional | 0.957 | 30 | The sensor cart carries tablet mounts and a red charging cable under its tray. |
| `p33` | selected, distractor | 0.529 | 30 | Hangar 3 accepts overnight staging only for paint-shop air filters, not Atlas calibration carts. |
| `p07` | selected | 0.200 | 27 | Hangar 2 staging requires the previous evening battery health printout. |
| `p28` | selected | 0.112 | 29 | Ground power files Binder Blue after the battery cart is returned. |
| `p30` | selected | 0.079 | 28 | Dev Rao is not responsible for catering, hydraulic seal approval, or Orion calibration. |
| `p17` | selected, distractor | 0.079 | 33 | A contractor guide lists 07:15 as a calibration start time, but it applies to Orion. |

### PASS content_01_aero_support / q03_direct / budget 1024

Question: When does winter calibration begin and where is the sensor cart staged?

Selected: `['p05', 'p06', 'p07', 'p17', 'p18', 'p19', 'p28', 'p30', 'p32', 'p33']`
Tokens: `293/1024`
F1: `0.667` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `['p17', 'p33']`

Score breakdown:

- individual: `11.098`
- pair synergy: `10.475`
- triple synergy: `0.000`
- redundancy penalty: `3.143`
- total: `18.429`

Improvement hint: Add wrong-context or contradiction-aware features; a distractor beat required evidence.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `p06` | selected, required | 3.893 | 29 | The sensor cart must be staged beside Hangar 2 during winter calibration. |
| `p32` | selected, optional | 1.836 | 30 | The rollout coordinator checks that the sensor cart has arrived before calibration begins. |
| `p05` | selected, required | 1.257 | 28 | The winter calibration window begins at 06:30 before the first engine run. |
| `p19` | selected, required | 2.157 | 29 | Hangar 2 has limited power during winter calibration, so staging must be early. |
| `p18` | selected, optional | 0.957 | 30 | The sensor cart carries tablet mounts and a red charging cable under its tray. |
| `p33` | selected, distractor | 0.529 | 30 | Hangar 3 accepts overnight staging only for paint-shop air filters, not Atlas calibration carts. |
| `p07` | selected | 0.200 | 27 | Hangar 2 staging requires the previous evening battery health printout. |
| `p28` | selected | 0.112 | 29 | Ground power files Binder Blue after the battery cart is returned. |
| `p30` | selected | 0.079 | 28 | Dev Rao is not responsible for catering, hydraulic seal approval, or Orion calibration. |
| `p17` | selected, distractor | 0.079 | 33 | A contractor guide lists 07:15 as a calibration start time, but it applies to Orion. |

### PASS content_01_aero_support / q04_direct / budget 128

Question: Which binder holds the previous evening battery health printout?

Selected: `['p07', 'p08', 'p31', 'p34']`
Tokens: `115/128`
F1: `0.857` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `[]`

Score breakdown:

- individual: `12.844`
- pair synergy: `3.261`
- triple synergy: `0.000`
- redundancy penalty: `1.448`
- total: `14.657`

Improvement hint: Successful selection; inspect extra chunks only if precision or token cost becomes the priority.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `p08` | selected, required | 4.546 | 28 | The previous evening battery health printout is filed in Binder Blue. |
| `p07` | selected | 3.968 | 27 | Hangar 2 staging requires the previous evening battery health printout. |
| `p31` | selected, optional | 2.269 | 29 | The ground power team owns the battery health printout process for Atlas staging. |
| `p34` | selected, optional | 2.061 | 31 | Binder Green contains fueling checklists and does not contain battery health printouts. |
| `p28` | required | 1.482 | 29 | Ground power files Binder Blue after the battery cart is returned. |
| `p19` | - | 0.200 | 29 | Hangar 2 has limited power during winter calibration, so staging must be early. |
| `p20` | - | 0.154 | 30 | A spare binder shelf label near the fuel records cabinet also says amber. |
| `p06` | - | -0.133 | 29 | The sensor cart must be staged beside Hangar 2 during winter calibration. |
| `p33` | - | -0.133 | 30 | Hangar 3 accepts overnight staging only for paint-shop air filters, not Atlas calibration carts. |
| `p38` | - | -0.467 | 27 | The aft temperature warning should not be routed to the electrical corrosion queue. |

### PASS content_01_aero_support / q04_direct / budget 256

Question: Which binder holds the previous evening battery health printout?

Selected: `['p07', 'p08', 'p19', 'p20', 'p28', 'p31', 'p33', 'p34']`
Tokens: `233/256`
F1: `0.667` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `[]`

Score breakdown:

- individual: `14.546`
- pair synergy: `7.736`
- triple synergy: `0.000`
- redundancy penalty: `3.026`
- total: `19.256`

Improvement hint: Successful selection; inspect extra chunks only if precision or token cost becomes the priority.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `p08` | selected, required | 4.546 | 28 | The previous evening battery health printout is filed in Binder Blue. |
| `p07` | selected | 3.968 | 27 | Hangar 2 staging requires the previous evening battery health printout. |
| `p31` | selected, optional | 2.269 | 29 | The ground power team owns the battery health printout process for Atlas staging. |
| `p34` | selected, optional | 2.061 | 31 | Binder Green contains fueling checklists and does not contain battery health printouts. |
| `p28` | selected, required | 1.482 | 29 | Ground power files Binder Blue after the battery cart is returned. |
| `p19` | selected | 0.200 | 29 | Hangar 2 has limited power during winter calibration, so staging must be early. |
| `p20` | selected | 0.154 | 30 | A spare binder shelf label near the fuel records cabinet also says amber. |
| `p06` | - | -0.133 | 29 | The sensor cart must be staged beside Hangar 2 during winter calibration. |
| `p33` | selected | -0.133 | 30 | Hangar 3 accepts overnight staging only for paint-shop air filters, not Atlas calibration carts. |
| `p38` | - | -0.467 | 27 | The aft temperature warning should not be routed to the electrical corrosion queue. |

### PASS content_01_aero_support / q04_direct / budget 512

Question: Which binder holds the previous evening battery health printout?

Selected: `['p06', 'p07', 'p08', 'p19', 'p20', 'p28', 'p31', 'p33', 'p34']`
Tokens: `262/512`
F1: `0.615` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `[]`

Score breakdown:

- individual: `14.413`
- pair synergy: `9.096`
- triple synergy: `0.000`
- redundancy penalty: `3.745`
- total: `19.764`

Improvement hint: Successful selection; inspect extra chunks only if precision or token cost becomes the priority.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `p08` | selected, required | 4.546 | 28 | The previous evening battery health printout is filed in Binder Blue. |
| `p07` | selected | 3.968 | 27 | Hangar 2 staging requires the previous evening battery health printout. |
| `p31` | selected, optional | 2.269 | 29 | The ground power team owns the battery health printout process for Atlas staging. |
| `p34` | selected, optional | 2.061 | 31 | Binder Green contains fueling checklists and does not contain battery health printouts. |
| `p28` | selected, required | 1.482 | 29 | Ground power files Binder Blue after the battery cart is returned. |
| `p19` | selected | 0.200 | 29 | Hangar 2 has limited power during winter calibration, so staging must be early. |
| `p20` | selected | 0.154 | 30 | A spare binder shelf label near the fuel records cabinet also says amber. |
| `p06` | selected | -0.133 | 29 | The sensor cart must be staged beside Hangar 2 during winter calibration. |
| `p33` | selected | -0.133 | 30 | Hangar 3 accepts overnight staging only for paint-shop air filters, not Atlas calibration carts. |
| `p38` | - | -0.467 | 27 | The aft temperature warning should not be routed to the electrical corrosion queue. |

### PASS content_01_aero_support / q04_direct / budget 1024

Question: Which binder holds the previous evening battery health printout?

Selected: `['p06', 'p07', 'p08', 'p19', 'p20', 'p28', 'p31', 'p33', 'p34']`
Tokens: `262/1024`
F1: `0.615` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `[]`

Score breakdown:

- individual: `14.413`
- pair synergy: `9.096`
- triple synergy: `0.000`
- redundancy penalty: `3.745`
- total: `19.764`

Improvement hint: Successful selection; inspect extra chunks only if precision or token cost becomes the priority.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `p08` | selected, required | 4.546 | 28 | The previous evening battery health printout is filed in Binder Blue. |
| `p07` | selected | 3.968 | 27 | Hangar 2 staging requires the previous evening battery health printout. |
| `p31` | selected, optional | 2.269 | 29 | The ground power team owns the battery health printout process for Atlas staging. |
| `p34` | selected, optional | 2.061 | 31 | Binder Green contains fueling checklists and does not contain battery health printouts. |
| `p28` | selected, required | 1.482 | 29 | Ground power files Binder Blue after the battery cart is returned. |
| `p19` | selected | 0.200 | 29 | Hangar 2 has limited power during winter calibration, so staging must be early. |
| `p20` | selected | 0.154 | 30 | A spare binder shelf label near the fuel records cabinet also says amber. |
| `p06` | selected | -0.133 | 29 | The sensor cart must be staged beside Hangar 2 during winter calibration. |
| `p33` | selected | -0.133 | 30 | Hangar 3 accepts overnight staging only for paint-shop air filters, not Atlas calibration carts. |
| `p38` | - | -0.467 | 27 | The aft temperature warning should not be routed to the electrical corrosion queue. |

### PASS content_01_aero_support / q05_direct / budget 128

Question: Who reviews the amber maintenance ledger?

Selected: `['p11', 'p12', 'p29', 'p37']`
Tokens: `118/128`
F1: `0.667` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `[]`

Score breakdown:

- individual: `14.500`
- pair synergy: `3.677`
- triple synergy: `0.000`
- redundancy penalty: `1.348`
- total: `16.829`

Improvement hint: Successful selection; inspect extra chunks only if precision or token cost becomes the priority.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `p12` | selected, required | 4.675 | 27 | Shift controller Dev Rao reviews the amber maintenance ledger. |
| `p11` | selected | 3.025 | 28 | Structural inspections must be logged in the amber maintenance ledger before release. |
| `p37` | selected, optional | 3.775 | 31 | A clerk may shelve the amber ledger beside fuel records after Dev Rao reviews it. |
| `p29` | selected | 3.025 | 32 | Cabin panel reviews are logged in the white trim notebook, not the amber ledger. |
| `p39` | - | 2.333 | 28 | Release paperwork is held until the amber ledger contains the structural inspection entry. |
| `p20` | distractor | 0.918 | 30 | A spare binder shelf label near the fuel records cabinet also says amber. |
| `p22` | - | 0.700 | 30 | The electrical team reviews right-harness corrosion alerts, not left-harness insulation rubs. |
| `p24` | required | 0.100 | 29 | Dev Rao signs the release sheet after the structural team entry appears. |
| `p30` | optional | -0.050 | 28 | Dev Rao is not responsible for catering, hydraulic seal approval, or Orion calibration. |
| `p04` | - | -0.300 | 29 | Cage D opens only after the secure tool room records Mira Patel's approval code. |

### PASS content_01_aero_support / q05_direct / budget 256

Question: Who reviews the amber maintenance ledger?

Selected: `['p11', 'p12', 'p20', 'p22', 'p24', 'p29', 'p37', 'p39']`
Tokens: `235/256`
F1: `0.545` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `['p20']`

Score breakdown:

- individual: `18.552`
- pair synergy: `9.246`
- triple synergy: `0.000`
- redundancy penalty: `3.367`
- total: `24.431`

Improvement hint: Add wrong-context or contradiction-aware features; a distractor beat required evidence.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `p12` | selected, required | 4.675 | 27 | Shift controller Dev Rao reviews the amber maintenance ledger. |
| `p11` | selected | 3.025 | 28 | Structural inspections must be logged in the amber maintenance ledger before release. |
| `p37` | selected, optional | 3.775 | 31 | A clerk may shelve the amber ledger beside fuel records after Dev Rao reviews it. |
| `p29` | selected | 3.025 | 32 | Cabin panel reviews are logged in the white trim notebook, not the amber ledger. |
| `p39` | selected | 2.333 | 28 | Release paperwork is held until the amber ledger contains the structural inspection entry. |
| `p20` | selected, distractor | 0.918 | 30 | A spare binder shelf label near the fuel records cabinet also says amber. |
| `p22` | selected | 0.700 | 30 | The electrical team reviews right-harness corrosion alerts, not left-harness insulation rubs. |
| `p24` | selected, required | 0.100 | 29 | Dev Rao signs the release sheet after the structural team entry appears. |
| `p30` | optional | -0.050 | 28 | Dev Rao is not responsible for catering, hydraulic seal approval, or Orion calibration. |
| `p04` | - | -0.300 | 29 | Cage D opens only after the secure tool room records Mira Patel's approval code. |

### PASS content_01_aero_support / q05_direct / budget 512

Question: Who reviews the amber maintenance ledger?

Selected: `['p04', 'p11', 'p12', 'p20', 'p22', 'p24', 'p29', 'p30', 'p37', 'p39']`
Tokens: `292/512`
F1: `0.571` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `['p20']`

Score breakdown:

- individual: `18.202`
- pair synergy: `10.815`
- triple synergy: `0.000`
- redundancy penalty: `4.099`
- total: `24.918`

Improvement hint: Add wrong-context or contradiction-aware features; a distractor beat required evidence.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `p12` | selected, required | 4.675 | 27 | Shift controller Dev Rao reviews the amber maintenance ledger. |
| `p11` | selected | 3.025 | 28 | Structural inspections must be logged in the amber maintenance ledger before release. |
| `p37` | selected, optional | 3.775 | 31 | A clerk may shelve the amber ledger beside fuel records after Dev Rao reviews it. |
| `p29` | selected | 3.025 | 32 | Cabin panel reviews are logged in the white trim notebook, not the amber ledger. |
| `p39` | selected | 2.333 | 28 | Release paperwork is held until the amber ledger contains the structural inspection entry. |
| `p20` | selected, distractor | 0.918 | 30 | A spare binder shelf label near the fuel records cabinet also says amber. |
| `p22` | selected | 0.700 | 30 | The electrical team reviews right-harness corrosion alerts, not left-harness insulation rubs. |
| `p24` | selected, required | 0.100 | 29 | Dev Rao signs the release sheet after the structural team entry appears. |
| `p30` | selected, optional | -0.050 | 28 | Dev Rao is not responsible for catering, hydraulic seal approval, or Orion calibration. |
| `p04` | selected | -0.300 | 29 | Cage D opens only after the secure tool room records Mira Patel's approval code. |

### PASS content_01_aero_support / q05_direct / budget 1024

Question: Who reviews the amber maintenance ledger?

Selected: `['p04', 'p11', 'p12', 'p20', 'p22', 'p24', 'p29', 'p30', 'p37', 'p39']`
Tokens: `292/1024`
F1: `0.571` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `['p20']`

Score breakdown:

- individual: `18.202`
- pair synergy: `10.815`
- triple synergy: `0.000`
- redundancy penalty: `4.099`
- total: `24.918`

Improvement hint: Add wrong-context or contradiction-aware features; a distractor beat required evidence.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `p12` | selected, required | 4.675 | 27 | Shift controller Dev Rao reviews the amber maintenance ledger. |
| `p11` | selected | 3.025 | 28 | Structural inspections must be logged in the amber maintenance ledger before release. |
| `p37` | selected, optional | 3.775 | 31 | A clerk may shelve the amber ledger beside fuel records after Dev Rao reviews it. |
| `p29` | selected | 3.025 | 32 | Cabin panel reviews are logged in the white trim notebook, not the amber ledger. |
| `p39` | selected | 2.333 | 28 | Release paperwork is held until the amber ledger contains the structural inspection entry. |
| `p20` | selected, distractor | 0.918 | 30 | A spare binder shelf label near the fuel records cabinet also says amber. |
| `p22` | selected | 0.700 | 30 | The electrical team reviews right-harness corrosion alerts, not left-harness insulation rubs. |
| `p24` | selected, required | 0.100 | 29 | Dev Rao signs the release sheet after the structural team entry appears. |
| `p30` | selected, optional | -0.050 | 28 | Dev Rao is not responsible for catering, hydraulic seal approval, or Orion calibration. |
| `p04` | selected | -0.300 | 29 | Cage D opens only after the secure tool room records Mira Patel's approval code. |

### PASS content_01_aero_support / q06_two_hop / budget 128

Question: Where are urgent avionics replacements approved by Mira Patel stored?

Selected: `['p02', 'p03', 'p26', 'p40']`
Tokens: `115/128`
F1: `0.857` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `['p26']`

Score breakdown:

- individual: `13.343`
- pair synergy: `4.617`
- triple synergy: `0.000`
- redundancy penalty: `1.218`
- total: `16.742`

Improvement hint: Add wrong-context or contradiction-aware features; a distractor beat required evidence.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `p03` | selected, required | 4.236 | 27 | Approved urgent avionics replacements are stored in Cage D. |
| `p02` | selected, required | 3.014 | 28 | Mira Patel is the duty lead who approves urgent avionics replacement requests for Atlas. |
| `p26` | selected, distractor | 3.657 | 31 | A superseded training note says urgent avionics replacements are stored in Cage C. |
| `p40` | selected, optional | 2.436 | 29 | Urgent replacement requests are marked red before they reach Mira Patel for approval. |
| `p14` | distractor | 1.257 | 32 | A parts summary mentions Mira Patel and Cage D but says she approves hydraulic seals. |
| `p04` | - | 1.214 | 29 | Cage D opens only after the secure tool room records Mira Patel's approval code. |
| `p23` | - | 1.064 | 30 | Torque kits are tracked by the secure tool room but are not stored in Cage D. |
| `p25` | optional | 0.636 | 31 | Routine avionics labels are kept in the general parts cabinet, not the restricted cage. |
| `p36` | - | -0.200 | 30 | A duplicate aft-warning note says cold starts can make insulation rub the left harness. |
| `p27` | - | -0.425 | 27 | The secure tool room records approval codes for restricted cages. |

### PASS content_01_aero_support / q06_two_hop / budget 256

Question: Where are urgent avionics replacements approved by Mira Patel stored?

Selected: `['p02', 'p03', 'p04', 'p14', 'p23', 'p25', 'p26', 'p40']`
Tokens: `237/256`
F1: `0.667` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `['p14', 'p26']`

Score breakdown:

- individual: `17.514`
- pair synergy: `14.679`
- triple synergy: `0.536`
- redundancy penalty: `3.734`
- total: `28.995`

Improvement hint: Add wrong-context or contradiction-aware features; a distractor beat required evidence.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `p03` | selected, required | 4.236 | 27 | Approved urgent avionics replacements are stored in Cage D. |
| `p02` | selected, required | 3.014 | 28 | Mira Patel is the duty lead who approves urgent avionics replacement requests for Atlas. |
| `p26` | selected, distractor | 3.657 | 31 | A superseded training note says urgent avionics replacements are stored in Cage C. |
| `p40` | selected, optional | 2.436 | 29 | Urgent replacement requests are marked red before they reach Mira Patel for approval. |
| `p14` | selected, distractor | 1.257 | 32 | A parts summary mentions Mira Patel and Cage D but says she approves hydraulic seals. |
| `p04` | selected | 1.214 | 29 | Cage D opens only after the secure tool room records Mira Patel's approval code. |
| `p23` | selected | 1.064 | 30 | Torque kits are tracked by the secure tool room but are not stored in Cage D. |
| `p25` | selected, optional | 0.636 | 31 | Routine avionics labels are kept in the general parts cabinet, not the restricted cage. |
| `p36` | - | -0.200 | 30 | A duplicate aft-warning note says cold starts can make insulation rub the left harness. |
| `p27` | - | -0.425 | 27 | The secure tool room records approval codes for restricted cages. |

### PASS content_01_aero_support / q06_two_hop / budget 512

Question: Where are urgent avionics replacements approved by Mira Patel stored?

Selected: `['p02', 'p03', 'p04', 'p14', 'p23', 'p25', 'p26', 'p27', 'p40']`
Tokens: `264/512`
F1: `0.615` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `['p14', 'p26']`

Score breakdown:

- individual: `17.089`
- pair synergy: `16.179`
- triple synergy: `0.536`
- redundancy penalty: `4.404`
- total: `29.400`

Improvement hint: Add wrong-context or contradiction-aware features; a distractor beat required evidence.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `p03` | selected, required | 4.236 | 27 | Approved urgent avionics replacements are stored in Cage D. |
| `p02` | selected, required | 3.014 | 28 | Mira Patel is the duty lead who approves urgent avionics replacement requests for Atlas. |
| `p26` | selected, distractor | 3.657 | 31 | A superseded training note says urgent avionics replacements are stored in Cage C. |
| `p40` | selected, optional | 2.436 | 29 | Urgent replacement requests are marked red before they reach Mira Patel for approval. |
| `p14` | selected, distractor | 1.257 | 32 | A parts summary mentions Mira Patel and Cage D but says she approves hydraulic seals. |
| `p04` | selected | 1.214 | 29 | Cage D opens only after the secure tool room records Mira Patel's approval code. |
| `p23` | selected | 1.064 | 30 | Torque kits are tracked by the secure tool room but are not stored in Cage D. |
| `p25` | selected, optional | 0.636 | 31 | Routine avionics labels are kept in the general parts cabinet, not the restricted cage. |
| `p36` | - | -0.200 | 30 | A duplicate aft-warning note says cold starts can make insulation rub the left harness. |
| `p27` | selected | -0.425 | 27 | The secure tool room records approval codes for restricted cages. |

### PASS content_01_aero_support / q06_two_hop / budget 1024

Question: Where are urgent avionics replacements approved by Mira Patel stored?

Selected: `['p02', 'p03', 'p04', 'p14', 'p23', 'p25', 'p26', 'p27', 'p40']`
Tokens: `264/1024`
F1: `0.615` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `['p14', 'p26']`

Score breakdown:

- individual: `17.089`
- pair synergy: `16.179`
- triple synergy: `0.536`
- redundancy penalty: `4.404`
- total: `29.400`

Improvement hint: Add wrong-context or contradiction-aware features; a distractor beat required evidence.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `p03` | selected, required | 4.236 | 27 | Approved urgent avionics replacements are stored in Cage D. |
| `p02` | selected, required | 3.014 | 28 | Mira Patel is the duty lead who approves urgent avionics replacement requests for Atlas. |
| `p26` | selected, distractor | 3.657 | 31 | A superseded training note says urgent avionics replacements are stored in Cage C. |
| `p40` | selected, optional | 2.436 | 29 | Urgent replacement requests are marked red before they reach Mira Patel for approval. |
| `p14` | selected, distractor | 1.257 | 32 | A parts summary mentions Mira Patel and Cage D but says she approves hydraulic seals. |
| `p04` | selected | 1.214 | 29 | Cage D opens only after the secure tool room records Mira Patel's approval code. |
| `p23` | selected | 1.064 | 30 | Torque kits are tracked by the secure tool room but are not stored in Cage D. |
| `p25` | selected, optional | 0.636 | 31 | Routine avionics labels are kept in the general parts cabinet, not the restricted cage. |
| `p36` | - | -0.200 | 30 | A duplicate aft-warning note says cold starts can make insulation rub the left harness. |
| `p27` | selected | -0.425 | 27 | The secure tool room records approval codes for restricted cages. |

### FAIL content_01_aero_support / q07_two_hop / budget 128

Question: What must happen before Cage D can be opened for an urgent avionics replacement?

Selected: `['p02', 'p03', 'p26', 'p40']`
Tokens: `115/128`
F1: `0.706` Required recall: `0.667`
Missing required units: `['open_condition']`
Selected distractors: `['p26']`

Score breakdown:

- individual: `9.936`
- pair synergy: `3.731`
- triple synergy: `0.000`
- redundancy penalty: `1.218`
- total: `12.449`

Improvement hint: Add wrong-context or contradiction-aware features; a distractor beat required evidence.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `p03` | selected, required | 3.143 | 27 | Approved urgent avionics replacements are stored in Cage D. |
| `p02` | selected, required | 2.050 | 28 | Mira Patel is the duty lead who approves urgent avionics replacement requests for Atlas. |
| `p40` | selected, optional | 2.050 | 29 | Urgent replacement requests are marked red before they reach Mira Patel for approval. |
| `p26` | selected, distractor | 2.693 | 31 | A superseded training note says urgent avionics replacements are stored in Cage C. |
| `p23` | optional | 1.386 | 30 | Torque kits are tracked by the secure tool room but are not stored in Cage D. |
| `p14` | - | 1.000 | 32 | A parts summary mentions Mira Patel and Cage D but says she approves hydraulic seals. |
| `p04` | required | 0.957 | 29 | Cage D opens only after the secure tool room records Mira Patel's approval code. |
| `p25` | - | 0.957 | 31 | Routine avionics labels are kept in the general parts cabinet, not the restricted cage. |
| `p11` | - | 0.433 | 28 | Structural inspections must be logged in the amber maintenance ledger before release. |
| `p36` | - | 0.250 | 30 | A duplicate aft-warning note says cold starts can make insulation rub the left harness. |

### PASS content_01_aero_support / q07_two_hop / budget 256

Question: What must happen before Cage D can be opened for an urgent avionics replacement?

Selected: `['p02', 'p03', 'p04', 'p11', 'p14', 'p23', 'p26', 'p40']`
Tokens: `234/256`
F1: `0.769` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `['p26']`

Score breakdown:

- individual: `13.712`
- pair synergy: `13.652`
- triple synergy: `2.750`
- redundancy penalty: `3.184`
- total: `26.930`

Improvement hint: Add wrong-context or contradiction-aware features; a distractor beat required evidence.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `p03` | selected, required | 3.143 | 27 | Approved urgent avionics replacements are stored in Cage D. |
| `p02` | selected, required | 2.050 | 28 | Mira Patel is the duty lead who approves urgent avionics replacement requests for Atlas. |
| `p40` | selected, optional | 2.050 | 29 | Urgent replacement requests are marked red before they reach Mira Patel for approval. |
| `p26` | selected, distractor | 2.693 | 31 | A superseded training note says urgent avionics replacements are stored in Cage C. |
| `p23` | selected, optional | 1.386 | 30 | Torque kits are tracked by the secure tool room but are not stored in Cage D. |
| `p14` | selected | 1.000 | 32 | A parts summary mentions Mira Patel and Cage D but says she approves hydraulic seals. |
| `p04` | selected, required | 0.957 | 29 | Cage D opens only after the secure tool room records Mira Patel's approval code. |
| `p25` | - | 0.957 | 31 | Routine avionics labels are kept in the general parts cabinet, not the restricted cage. |
| `p11` | selected | 0.433 | 28 | Structural inspections must be logged in the amber maintenance ledger before release. |
| `p36` | - | 0.250 | 30 | A duplicate aft-warning note says cold starts can make insulation rub the left harness. |

### PASS content_01_aero_support / q07_two_hop / budget 512

Question: What must happen before Cage D can be opened for an urgent avionics replacement?

Selected: `['p02', 'p03', 'p04', 'p11', 'p14', 'p23', 'p25', 'p26', 'p36', 'p40']`
Tokens: `295/512`
F1: `0.667` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `['p26']`

Score breakdown:

- individual: `14.919`
- pair synergy: `18.687`
- triple synergy: `7.125`
- redundancy penalty: `3.945`
- total: `36.786`

Improvement hint: Add wrong-context or contradiction-aware features; a distractor beat required evidence.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `p03` | selected, required | 3.143 | 27 | Approved urgent avionics replacements are stored in Cage D. |
| `p02` | selected, required | 2.050 | 28 | Mira Patel is the duty lead who approves urgent avionics replacement requests for Atlas. |
| `p40` | selected, optional | 2.050 | 29 | Urgent replacement requests are marked red before they reach Mira Patel for approval. |
| `p26` | selected, distractor | 2.693 | 31 | A superseded training note says urgent avionics replacements are stored in Cage C. |
| `p23` | selected, optional | 1.386 | 30 | Torque kits are tracked by the secure tool room but are not stored in Cage D. |
| `p14` | selected | 1.000 | 32 | A parts summary mentions Mira Patel and Cage D but says she approves hydraulic seals. |
| `p04` | selected, required | 0.957 | 29 | Cage D opens only after the secure tool room records Mira Patel's approval code. |
| `p25` | selected | 0.957 | 31 | Routine avionics labels are kept in the general parts cabinet, not the restricted cage. |
| `p11` | selected | 0.433 | 28 | Structural inspections must be logged in the amber maintenance ledger before release. |
| `p36` | selected | 0.250 | 30 | A duplicate aft-warning note says cold starts can make insulation rub the left harness. |

### PASS content_01_aero_support / q07_two_hop / budget 1024

Question: What must happen before Cage D can be opened for an urgent avionics replacement?

Selected: `['p02', 'p03', 'p04', 'p11', 'p14', 'p23', 'p25', 'p26', 'p36', 'p40']`
Tokens: `295/1024`
F1: `0.667` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `['p26']`

Score breakdown:

- individual: `14.919`
- pair synergy: `18.687`
- triple synergy: `7.125`
- redundancy penalty: `3.945`
- total: `36.786`

Improvement hint: Add wrong-context or contradiction-aware features; a distractor beat required evidence.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `p03` | selected, required | 3.143 | 27 | Approved urgent avionics replacements are stored in Cage D. |
| `p02` | selected, required | 2.050 | 28 | Mira Patel is the duty lead who approves urgent avionics replacement requests for Atlas. |
| `p40` | selected, optional | 2.050 | 29 | Urgent replacement requests are marked red before they reach Mira Patel for approval. |
| `p26` | selected, distractor | 2.693 | 31 | A superseded training note says urgent avionics replacements are stored in Cage C. |
| `p23` | selected, optional | 1.386 | 30 | Torque kits are tracked by the secure tool room but are not stored in Cage D. |
| `p14` | selected | 1.000 | 32 | A parts summary mentions Mira Patel and Cage D but says she approves hydraulic seals. |
| `p04` | selected, required | 0.957 | 29 | Cage D opens only after the secure tool room records Mira Patel's approval code. |
| `p25` | selected | 0.957 | 31 | Routine avionics labels are kept in the general parts cabinet, not the restricted cage. |
| `p11` | selected | 0.433 | 28 | Structural inspections must be logged in the amber maintenance ledger before release. |
| `p36` | selected | 0.250 | 30 | A duplicate aft-warning note says cold starts can make insulation rub the left harness. |

### PASS content_01_aero_support / q08_two_hop / budget 128

Question: What document is needed for Hangar 2 staging during winter calibration?

Selected: `['p06', 'p07', 'p19', 'p33']`
Tokens: `115/128`
F1: `0.857` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `['p33']`

Score breakdown:

- individual: `11.075`
- pair synergy: `2.943`
- triple synergy: `0.000`
- redundancy penalty: `1.098`
- total: `12.920`

Improvement hint: Add wrong-context or contradiction-aware features; a distractor beat required evidence.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `p19` | selected, required | 4.150 | 29 | Hangar 2 has limited power during winter calibration, so staging must be early. |
| `p06` | selected, required | 3.625 | 29 | The sensor cart must be staged beside Hangar 2 during winter calibration. |
| `p07` | selected, required | 1.775 | 27 | Hangar 2 staging requires the previous evening battery health printout. |
| `p33` | selected, distractor | 1.525 | 30 | Hangar 3 accepts overnight staging only for paint-shop air filters, not Atlas calibration carts. |
| `p08` | optional | 1.075 | 28 | The previous evening battery health printout is filed in Binder Blue. |
| `p31` | optional | 1.058 | 29 | The ground power team owns the battery health printout process for Atlas staging. |
| `p05` | - | 0.850 | 28 | The winter calibration window begins at 06:30 before the first engine run. |
| `p32` | - | 0.625 | 30 | The rollout coordinator checks that the sensor cart has arrived before calibration begins. |
| `p30` | - | 0.325 | 28 | Dev Rao is not responsible for catering, hydraulic seal approval, or Orion calibration. |
| `p17` | - | 0.025 | 33 | A contractor guide lists 07:15 as a calibration start time, but it applies to Orion. |

### PASS content_01_aero_support / q08_two_hop / budget 256

Question: What document is needed for Hangar 2 staging during winter calibration?

Selected: `['p05', 'p06', 'p07', 'p08', 'p19', 'p31', 'p32', 'p33']`
Tokens: `230/256`
F1: `0.769` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `['p33']`

Score breakdown:

- individual: `14.683`
- pair synergy: `8.554`
- triple synergy: `0.000`
- redundancy penalty: `3.122`
- total: `20.115`

Improvement hint: Add wrong-context or contradiction-aware features; a distractor beat required evidence.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `p19` | selected, required | 4.150 | 29 | Hangar 2 has limited power during winter calibration, so staging must be early. |
| `p06` | selected, required | 3.625 | 29 | The sensor cart must be staged beside Hangar 2 during winter calibration. |
| `p07` | selected, required | 1.775 | 27 | Hangar 2 staging requires the previous evening battery health printout. |
| `p33` | selected, distractor | 1.525 | 30 | Hangar 3 accepts overnight staging only for paint-shop air filters, not Atlas calibration carts. |
| `p08` | selected, optional | 1.075 | 28 | The previous evening battery health printout is filed in Binder Blue. |
| `p31` | selected, optional | 1.058 | 29 | The ground power team owns the battery health printout process for Atlas staging. |
| `p05` | selected | 0.850 | 28 | The winter calibration window begins at 06:30 before the first engine run. |
| `p32` | selected | 0.625 | 30 | The rollout coordinator checks that the sensor cart has arrived before calibration begins. |
| `p30` | - | 0.325 | 28 | Dev Rao is not responsible for catering, hydraulic seal approval, or Orion calibration. |
| `p17` | - | 0.025 | 33 | A contractor guide lists 07:15 as a calibration start time, but it applies to Orion. |

### PASS content_01_aero_support / q08_two_hop / budget 512

Question: What document is needed for Hangar 2 staging during winter calibration?

Selected: `['p05', 'p06', 'p07', 'p08', 'p17', 'p19', 'p30', 'p31', 'p32', 'p33']`
Tokens: `291/512`
F1: `0.667` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `['p33']`

Score breakdown:

- individual: `15.033`
- pair synergy: `11.063`
- triple synergy: `0.000`
- redundancy penalty: `3.817`
- total: `22.279`

Improvement hint: Add wrong-context or contradiction-aware features; a distractor beat required evidence.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `p19` | selected, required | 4.150 | 29 | Hangar 2 has limited power during winter calibration, so staging must be early. |
| `p06` | selected, required | 3.625 | 29 | The sensor cart must be staged beside Hangar 2 during winter calibration. |
| `p07` | selected, required | 1.775 | 27 | Hangar 2 staging requires the previous evening battery health printout. |
| `p33` | selected, distractor | 1.525 | 30 | Hangar 3 accepts overnight staging only for paint-shop air filters, not Atlas calibration carts. |
| `p08` | selected, optional | 1.075 | 28 | The previous evening battery health printout is filed in Binder Blue. |
| `p31` | selected, optional | 1.058 | 29 | The ground power team owns the battery health printout process for Atlas staging. |
| `p05` | selected | 0.850 | 28 | The winter calibration window begins at 06:30 before the first engine run. |
| `p32` | selected | 0.625 | 30 | The rollout coordinator checks that the sensor cart has arrived before calibration begins. |
| `p30` | selected | 0.325 | 28 | Dev Rao is not responsible for catering, hydraulic seal approval, or Orion calibration. |
| `p17` | selected | 0.025 | 33 | A contractor guide lists 07:15 as a calibration start time, but it applies to Orion. |

### PASS content_01_aero_support / q08_two_hop / budget 1024

Question: What document is needed for Hangar 2 staging during winter calibration?

Selected: `['p05', 'p06', 'p07', 'p08', 'p17', 'p19', 'p30', 'p31', 'p32', 'p33']`
Tokens: `291/1024`
F1: `0.667` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `['p33']`

Score breakdown:

- individual: `15.033`
- pair synergy: `11.063`
- triple synergy: `0.000`
- redundancy penalty: `3.817`
- total: `22.279`

Improvement hint: Add wrong-context or contradiction-aware features; a distractor beat required evidence.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `p19` | selected, required | 4.150 | 29 | Hangar 2 has limited power during winter calibration, so staging must be early. |
| `p06` | selected, required | 3.625 | 29 | The sensor cart must be staged beside Hangar 2 during winter calibration. |
| `p07` | selected, required | 1.775 | 27 | Hangar 2 staging requires the previous evening battery health printout. |
| `p33` | selected, distractor | 1.525 | 30 | Hangar 3 accepts overnight staging only for paint-shop air filters, not Atlas calibration carts. |
| `p08` | selected, optional | 1.075 | 28 | The previous evening battery health printout is filed in Binder Blue. |
| `p31` | selected, optional | 1.058 | 29 | The ground power team owns the battery health printout process for Atlas staging. |
| `p05` | selected | 0.850 | 28 | The winter calibration window begins at 06:30 before the first engine run. |
| `p32` | selected | 0.625 | 30 | The rollout coordinator checks that the sensor cart has arrived before calibration begins. |
| `p30` | selected | 0.325 | 28 | Dev Rao is not responsible for catering, hydraulic seal approval, or Orion calibration. |
| `p17` | selected | 0.025 | 33 | A contractor guide lists 07:15 as a calibration start time, but it applies to Orion. |

### PASS content_01_aero_support / q09_two_hop / budget 128

Question: Which team should handle the usual cause of the aft temperature warning?

Selected: `['p09', 'p10', 'p36', 'p38']`
Tokens: `116/128`
F1: `1.000` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `[]`

Score breakdown:

- individual: `8.797`
- pair synergy: `2.812`
- triple synergy: `0.000`
- redundancy penalty: `1.457`
- total: `10.152`

Improvement hint: Successful selection; inspect extra chunks only if precision or token cost becomes the priority.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `p38` | selected, optional | 2.300 | 27 | The aft temperature warning should not be routed to the electrical corrosion queue. |
| `p10` | selected, required | 2.442 | 29 | When the aft temperature warning appears, left harness inspection is assigned to structural. |
| `p09` | selected, required | 2.442 | 30 | Atlas field reports link the aft temperature warning to insulation rubbing the left harness. |
| `p36` | selected, required | 1.614 | 30 | A duplicate aft-warning note says cold starts can make insulation rub the left harness. |
| `p22` | optional | 0.725 | 30 | The electrical team reviews right-harness corrosion alerts, not left-harness insulation rubs. |
| `p24` | - | 0.392 | 29 | Dev Rao signs the release sheet after the structural team entry appears. |
| `p31` | - | 0.025 | 29 | The ground power team owns the battery health printout process for Atlas staging. |
| `p39` | - | -0.133 | 28 | Release paperwork is held until the amber ledger contains the structural inspection entry. |
| `p26` | - | -0.200 | 31 | A superseded training note says urgent avionics replacements are stored in Cage C. |
| `p11` | - | -0.467 | 28 | Structural inspections must be logged in the amber maintenance ledger before release. |

### PASS content_01_aero_support / q09_two_hop / budget 256

Question: Which team should handle the usual cause of the aft temperature warning?

Selected: `['p09', 'p10', 'p22', 'p24', 'p31', 'p36', 'p38', 'p39']`
Tokens: `232/256`
F1: `0.769` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `[]`

Score breakdown:

- individual: `9.805`
- pair synergy: `8.507`
- triple synergy: `0.000`
- redundancy penalty: `2.810`
- total: `15.502`

Improvement hint: Successful selection; inspect extra chunks only if precision or token cost becomes the priority.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `p38` | selected, optional | 2.300 | 27 | The aft temperature warning should not be routed to the electrical corrosion queue. |
| `p10` | selected, required | 2.442 | 29 | When the aft temperature warning appears, left harness inspection is assigned to structural. |
| `p09` | selected, required | 2.442 | 30 | Atlas field reports link the aft temperature warning to insulation rubbing the left harness. |
| `p36` | selected, required | 1.614 | 30 | A duplicate aft-warning note says cold starts can make insulation rub the left harness. |
| `p22` | selected, optional | 0.725 | 30 | The electrical team reviews right-harness corrosion alerts, not left-harness insulation rubs. |
| `p24` | selected | 0.392 | 29 | Dev Rao signs the release sheet after the structural team entry appears. |
| `p31` | selected | 0.025 | 29 | The ground power team owns the battery health printout process for Atlas staging. |
| `p39` | selected | -0.133 | 28 | Release paperwork is held until the amber ledger contains the structural inspection entry. |
| `p26` | - | -0.200 | 31 | A superseded training note says urgent avionics replacements are stored in Cage C. |
| `p11` | - | -0.467 | 28 | Structural inspections must be logged in the amber maintenance ledger before release. |

### PASS content_01_aero_support / q09_two_hop / budget 512

Question: Which team should handle the usual cause of the aft temperature warning?

Selected: `['p09', 'p10', 'p22', 'p24', 'p31', 'p36', 'p38', 'p39']`
Tokens: `232/512`
F1: `0.769` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `[]`

Score breakdown:

- individual: `9.805`
- pair synergy: `8.507`
- triple synergy: `0.000`
- redundancy penalty: `2.810`
- total: `15.502`

Improvement hint: Successful selection; inspect extra chunks only if precision or token cost becomes the priority.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `p38` | selected, optional | 2.300 | 27 | The aft temperature warning should not be routed to the electrical corrosion queue. |
| `p10` | selected, required | 2.442 | 29 | When the aft temperature warning appears, left harness inspection is assigned to structural. |
| `p09` | selected, required | 2.442 | 30 | Atlas field reports link the aft temperature warning to insulation rubbing the left harness. |
| `p36` | selected, required | 1.614 | 30 | A duplicate aft-warning note says cold starts can make insulation rub the left harness. |
| `p22` | selected, optional | 0.725 | 30 | The electrical team reviews right-harness corrosion alerts, not left-harness insulation rubs. |
| `p24` | selected | 0.392 | 29 | Dev Rao signs the release sheet after the structural team entry appears. |
| `p31` | selected | 0.025 | 29 | The ground power team owns the battery health printout process for Atlas staging. |
| `p39` | selected | -0.133 | 28 | Release paperwork is held until the amber ledger contains the structural inspection entry. |
| `p26` | - | -0.200 | 31 | A superseded training note says urgent avionics replacements are stored in Cage C. |
| `p11` | - | -0.467 | 28 | Structural inspections must be logged in the amber maintenance ledger before release. |

### PASS content_01_aero_support / q09_two_hop / budget 1024

Question: Which team should handle the usual cause of the aft temperature warning?

Selected: `['p09', 'p10', 'p22', 'p24', 'p31', 'p36', 'p38', 'p39']`
Tokens: `232/1024`
F1: `0.769` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `[]`

Score breakdown:

- individual: `9.805`
- pair synergy: `8.507`
- triple synergy: `0.000`
- redundancy penalty: `2.810`
- total: `15.502`

Improvement hint: Successful selection; inspect extra chunks only if precision or token cost becomes the priority.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `p38` | selected, optional | 2.300 | 27 | The aft temperature warning should not be routed to the electrical corrosion queue. |
| `p10` | selected, required | 2.442 | 29 | When the aft temperature warning appears, left harness inspection is assigned to structural. |
| `p09` | selected, required | 2.442 | 30 | Atlas field reports link the aft temperature warning to insulation rubbing the left harness. |
| `p36` | selected, required | 1.614 | 30 | A duplicate aft-warning note says cold starts can make insulation rub the left harness. |
| `p22` | selected, optional | 0.725 | 30 | The electrical team reviews right-harness corrosion alerts, not left-harness insulation rubs. |
| `p24` | selected | 0.392 | 29 | Dev Rao signs the release sheet after the structural team entry appears. |
| `p31` | selected | 0.025 | 29 | The ground power team owns the battery health printout process for Atlas staging. |
| `p39` | selected | -0.133 | 28 | Release paperwork is held until the amber ledger contains the structural inspection entry. |
| `p26` | - | -0.200 | 31 | A superseded training note says urgent avionics replacements are stored in Cage C. |
| `p11` | - | -0.467 | 28 | Structural inspections must be logged in the amber maintenance ledger before release. |

### PASS content_01_aero_support / q10_two_hop / budget 128

Question: Who reviews the required log after a structural inspection?

Selected: `['p12', 'p24', 'p37', 'p39']`
Tokens: `115/128`
F1: `1.000` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `[]`

Score breakdown:

- individual: `5.925`
- pair synergy: `4.310`
- triple synergy: `0.208`
- redundancy penalty: `1.145`
- total: `9.298`

Improvement hint: Successful selection; inspect extra chunks only if precision or token cost becomes the priority.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `p39` | selected, required | 1.400 | 28 | Release paperwork is held until the amber ledger contains the structural inspection entry. |
| `p10` | - | 1.167 | 29 | When the aft temperature warning appears, left harness inspection is assigned to structural. |
| `p24` | selected, required | 1.400 | 29 | Dev Rao signs the release sheet after the structural team entry appears. |
| `p37` | selected, optional | 1.400 | 31 | A clerk may shelve the amber ledger beside fuel records after Dev Rao reviews it. |
| `p12` | selected, required | 1.725 | 27 | Shift controller Dev Rao reviews the amber maintenance ledger. |
| `p11` | required | 1.183 | 28 | Structural inspections must be logged in the amber maintenance ledger before release. |
| `p09` | - | 0.867 | 30 | Atlas field reports link the aft temperature warning to insulation rubbing the left harness. |
| `p29` | - | 0.750 | 32 | Cabin panel reviews are logged in the white trim notebook, not the amber ledger. |
| `p36` | - | 0.533 | 30 | A duplicate aft-warning note says cold starts can make insulation rub the left harness. |
| `p22` | - | 0.517 | 30 | The electrical team reviews right-harness corrosion alerts, not left-harness insulation rubs. |

### PASS content_01_aero_support / q10_two_hop / budget 256

Question: Who reviews the required log after a structural inspection?

Selected: `['p10', 'p11', 'p12', 'p22', 'p24', 'p29', 'p37', 'p39']`
Tokens: `234/256`
F1: `0.769` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `[]`

Score breakdown:

- individual: `9.542`
- pair synergy: `13.496`
- triple synergy: `1.250`
- redundancy penalty: `3.420`
- total: `20.868`

Improvement hint: Successful selection; inspect extra chunks only if precision or token cost becomes the priority.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `p39` | selected, required | 1.400 | 28 | Release paperwork is held until the amber ledger contains the structural inspection entry. |
| `p10` | selected | 1.167 | 29 | When the aft temperature warning appears, left harness inspection is assigned to structural. |
| `p24` | selected, required | 1.400 | 29 | Dev Rao signs the release sheet after the structural team entry appears. |
| `p37` | selected, optional | 1.400 | 31 | A clerk may shelve the amber ledger beside fuel records after Dev Rao reviews it. |
| `p12` | selected, required | 1.725 | 27 | Shift controller Dev Rao reviews the amber maintenance ledger. |
| `p11` | selected, required | 1.183 | 28 | Structural inspections must be logged in the amber maintenance ledger before release. |
| `p09` | - | 0.867 | 30 | Atlas field reports link the aft temperature warning to insulation rubbing the left harness. |
| `p29` | selected | 0.750 | 32 | Cabin panel reviews are logged in the white trim notebook, not the amber ledger. |
| `p36` | - | 0.533 | 30 | A duplicate aft-warning note says cold starts can make insulation rub the left harness. |
| `p22` | selected | 0.517 | 30 | The electrical team reviews right-harness corrosion alerts, not left-harness insulation rubs. |

### PASS content_01_aero_support / q10_two_hop / budget 512

Question: Who reviews the required log after a structural inspection?

Selected: `['p09', 'p10', 'p11', 'p12', 'p22', 'p24', 'p29', 'p36', 'p37', 'p39']`
Tokens: `294/512`
F1: `0.667` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `[]`

Score breakdown:

- individual: `10.942`
- pair synergy: `15.896`
- triple synergy: `1.250`
- redundancy penalty: `4.679`
- total: `23.409`

Improvement hint: Successful selection; inspect extra chunks only if precision or token cost becomes the priority.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `p39` | selected, required | 1.400 | 28 | Release paperwork is held until the amber ledger contains the structural inspection entry. |
| `p10` | selected | 1.167 | 29 | When the aft temperature warning appears, left harness inspection is assigned to structural. |
| `p24` | selected, required | 1.400 | 29 | Dev Rao signs the release sheet after the structural team entry appears. |
| `p37` | selected, optional | 1.400 | 31 | A clerk may shelve the amber ledger beside fuel records after Dev Rao reviews it. |
| `p12` | selected, required | 1.725 | 27 | Shift controller Dev Rao reviews the amber maintenance ledger. |
| `p11` | selected, required | 1.183 | 28 | Structural inspections must be logged in the amber maintenance ledger before release. |
| `p09` | selected | 0.867 | 30 | Atlas field reports link the aft temperature warning to insulation rubbing the left harness. |
| `p29` | selected | 0.750 | 32 | Cabin panel reviews are logged in the white trim notebook, not the amber ledger. |
| `p36` | selected | 0.533 | 30 | A duplicate aft-warning note says cold starts can make insulation rub the left harness. |
| `p22` | selected | 0.517 | 30 | The electrical team reviews right-harness corrosion alerts, not left-harness insulation rubs. |

### PASS content_01_aero_support / q10_two_hop / budget 1024

Question: Who reviews the required log after a structural inspection?

Selected: `['p09', 'p10', 'p11', 'p12', 'p22', 'p24', 'p29', 'p36', 'p37', 'p39']`
Tokens: `294/1024`
F1: `0.667` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `[]`

Score breakdown:

- individual: `10.942`
- pair synergy: `15.896`
- triple synergy: `1.250`
- redundancy penalty: `4.679`
- total: `23.409`

Improvement hint: Successful selection; inspect extra chunks only if precision or token cost becomes the priority.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `p39` | selected, required | 1.400 | 28 | Release paperwork is held until the amber ledger contains the structural inspection entry. |
| `p10` | selected | 1.167 | 29 | When the aft temperature warning appears, left harness inspection is assigned to structural. |
| `p24` | selected, required | 1.400 | 29 | Dev Rao signs the release sheet after the structural team entry appears. |
| `p37` | selected, optional | 1.400 | 31 | A clerk may shelve the amber ledger beside fuel records after Dev Rao reviews it. |
| `p12` | selected, required | 1.725 | 27 | Shift controller Dev Rao reviews the amber maintenance ledger. |
| `p11` | selected, required | 1.183 | 28 | Structural inspections must be logged in the amber maintenance ledger before release. |
| `p09` | selected | 0.867 | 30 | Atlas field reports link the aft temperature warning to insulation rubbing the left harness. |
| `p29` | selected | 0.750 | 32 | Cabin panel reviews are logged in the white trim notebook, not the amber ledger. |
| `p36` | selected | 0.533 | 30 | A duplicate aft-warning note says cold starts can make insulation rub the left harness. |
| `p22` | selected | 0.517 | 30 | The electrical team reviews right-harness corrosion alerts, not left-harness insulation rubs. |

### FAIL content_01_aero_support / q11_three_hop / budget 128

Question: Which restricted location becomes accessible after Mira Patel approves the urgent replacement and the tool room records the code?

Selected: `['p02', 'p04', 'p27', 'p40']`
Tokens: `113/128`
F1: `0.800` Required recall: `0.667`
Missing required units: `['storage']`
Selected distractors: `[]`

Score breakdown:

- individual: `10.836`
- pair synergy: `4.067`
- triple synergy: `0.179`
- redundancy penalty: `1.001`
- total: `14.081`

Improvement hint: Scoring issue; required evidence was available but not valuable enough under current utility.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `p04` | selected, required | 3.625 | 29 | Cage D opens only after the secure tool room records Mira Patel's approval code. |
| `p02` | selected, required | 2.521 | 28 | Mira Patel is the duty lead who approves urgent avionics replacement requests for Atlas. |
| `p27` | selected, required | 2.532 | 27 | The secure tool room records approval codes for restricted cages. |
| `p40` | selected, optional | 2.157 | 29 | Urgent replacement requests are marked red before they reach Mira Patel for approval. |
| `p23` | optional | 1.292 | 30 | Torque kits are tracked by the secure tool room but are not stored in Cage D. |
| `p14` | distractor | 1.216 | 32 | A parts summary mentions Mira Patel and Cage D but says she approves hydraulic seals. |
| `p37` | - | 0.429 | 31 | A clerk may shelve the amber ledger beside fuel records after Dev Rao reviews it. |
| `p03` | required | 0.421 | 27 | Approved urgent avionics replacements are stored in Cage D. |
| `p26` | distractor | 0.164 | 31 | A superseded training note says urgent avionics replacements are stored in Cage C. |
| `p20` | - | -0.061 | 30 | A spare binder shelf label near the fuel records cabinet also says amber. |

### PASS content_01_aero_support / q11_three_hop / budget 256

Question: Which restricted location becomes accessible after Mira Patel approves the urgent replacement and the tool room records the code?

Selected: `['p02', 'p03', 'p04', 'p14', 'p23', 'p27', 'p37', 'p40']`
Tokens: `233/256`
F1: `0.857` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `['p14']`

Score breakdown:

- individual: `14.194`
- pair synergy: `11.973`
- triple synergy: `2.054`
- redundancy penalty: `2.958`
- total: `25.263`

Improvement hint: Add wrong-context or contradiction-aware features; a distractor beat required evidence.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `p04` | selected, required | 3.625 | 29 | Cage D opens only after the secure tool room records Mira Patel's approval code. |
| `p02` | selected, required | 2.521 | 28 | Mira Patel is the duty lead who approves urgent avionics replacement requests for Atlas. |
| `p27` | selected, required | 2.532 | 27 | The secure tool room records approval codes for restricted cages. |
| `p40` | selected, optional | 2.157 | 29 | Urgent replacement requests are marked red before they reach Mira Patel for approval. |
| `p23` | selected, optional | 1.292 | 30 | Torque kits are tracked by the secure tool room but are not stored in Cage D. |
| `p14` | selected, distractor | 1.216 | 32 | A parts summary mentions Mira Patel and Cage D but says she approves hydraulic seals. |
| `p37` | selected | 0.429 | 31 | A clerk may shelve the amber ledger beside fuel records after Dev Rao reviews it. |
| `p03` | selected, required | 0.421 | 27 | Approved urgent avionics replacements are stored in Cage D. |
| `p26` | distractor | 0.164 | 31 | A superseded training note says urgent avionics replacements are stored in Cage C. |
| `p20` | - | -0.061 | 30 | A spare binder shelf label near the fuel records cabinet also says amber. |

### PASS content_01_aero_support / q11_three_hop / budget 512

Question: Which restricted location becomes accessible after Mira Patel approves the urgent replacement and the tool room records the code?

Selected: `['p02', 'p03', 'p04', 'p14', 'p20', 'p23', 'p26', 'p27', 'p37', 'p40']`
Tokens: `294/512`
F1: `0.750` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `['p14', 'p26']`

Score breakdown:

- individual: `14.297`
- pair synergy: `16.177`
- triple synergy: `3.393`
- redundancy penalty: `4.266`
- total: `29.602`

Improvement hint: Add wrong-context or contradiction-aware features; a distractor beat required evidence.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `p04` | selected, required | 3.625 | 29 | Cage D opens only after the secure tool room records Mira Patel's approval code. |
| `p02` | selected, required | 2.521 | 28 | Mira Patel is the duty lead who approves urgent avionics replacement requests for Atlas. |
| `p27` | selected, required | 2.532 | 27 | The secure tool room records approval codes for restricted cages. |
| `p40` | selected, optional | 2.157 | 29 | Urgent replacement requests are marked red before they reach Mira Patel for approval. |
| `p23` | selected, optional | 1.292 | 30 | Torque kits are tracked by the secure tool room but are not stored in Cage D. |
| `p14` | selected, distractor | 1.216 | 32 | A parts summary mentions Mira Patel and Cage D but says she approves hydraulic seals. |
| `p37` | selected | 0.429 | 31 | A clerk may shelve the amber ledger beside fuel records after Dev Rao reviews it. |
| `p03` | selected, required | 0.421 | 27 | Approved urgent avionics replacements are stored in Cage D. |
| `p26` | selected, distractor | 0.164 | 31 | A superseded training note says urgent avionics replacements are stored in Cage C. |
| `p20` | selected | -0.061 | 30 | A spare binder shelf label near the fuel records cabinet also says amber. |

### PASS content_01_aero_support / q11_three_hop / budget 1024

Question: Which restricted location becomes accessible after Mira Patel approves the urgent replacement and the tool room records the code?

Selected: `['p02', 'p03', 'p04', 'p14', 'p20', 'p23', 'p26', 'p27', 'p37', 'p40']`
Tokens: `294/1024`
F1: `0.750` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `['p14', 'p26']`

Score breakdown:

- individual: `14.297`
- pair synergy: `16.177`
- triple synergy: `3.393`
- redundancy penalty: `4.266`
- total: `29.602`

Improvement hint: Add wrong-context or contradiction-aware features; a distractor beat required evidence.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `p04` | selected, required | 3.625 | 29 | Cage D opens only after the secure tool room records Mira Patel's approval code. |
| `p02` | selected, required | 2.521 | 28 | Mira Patel is the duty lead who approves urgent avionics replacement requests for Atlas. |
| `p27` | selected, required | 2.532 | 27 | The secure tool room records approval codes for restricted cages. |
| `p40` | selected, optional | 2.157 | 29 | Urgent replacement requests are marked red before they reach Mira Patel for approval. |
| `p23` | selected, optional | 1.292 | 30 | Torque kits are tracked by the secure tool room but are not stored in Cage D. |
| `p14` | selected, distractor | 1.216 | 32 | A parts summary mentions Mira Patel and Cage D but says she approves hydraulic seals. |
| `p37` | selected | 0.429 | 31 | A clerk may shelve the amber ledger beside fuel records after Dev Rao reviews it. |
| `p03` | selected, required | 0.421 | 27 | Approved urgent avionics replacements are stored in Cage D. |
| `p26` | selected, distractor | 0.164 | 31 | A superseded training note says urgent avionics replacements are stored in Cage C. |
| `p20` | selected | -0.061 | 30 | A spare binder shelf label near the fuel records cabinet also says amber. |

### FAIL content_01_aero_support / q12_three_hop / budget 128

Question: Which team files the binder needed for the document required by Hangar 2 staging?

Selected: `['p06', 'p08', 'p19', 'p31']`
Tokens: `115/128`
F1: `0.857` Required recall: `0.750`
Missing required units: `['printout']`
Selected distractors: `[]`

Score breakdown:

- individual: `7.475`
- pair synergy: `2.743`
- triple synergy: `0.278`
- redundancy penalty: `0.759`
- total: `9.737`

Improvement hint: Scoring issue; required evidence was available but not valuable enough under current utility.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `p07` | required | 1.650 | 27 | Hangar 2 staging requires the previous evening battery health printout. |
| `p19` | selected, required | 2.450 | 29 | Hangar 2 has limited power during winter calibration, so staging must be early. |
| `p06` | selected, required | 1.967 | 29 | The sensor cart must be staged beside Hangar 2 during winter calibration. |
| `p28` | required | 0.500 | 29 | Ground power files Binder Blue after the battery cart is returned. |
| `p08` | selected, required | 1.558 | 28 | The previous evening battery health printout is filed in Binder Blue. |
| `p31` | selected, required | 1.500 | 29 | The ground power team owns the battery health printout process for Atlas staging. |
| `p33` | distractor | 0.917 | 30 | Hangar 3 accepts overnight staging only for paint-shop air filters, not Atlas calibration carts. |
| `p34` | distractor | 0.350 | 31 | Binder Green contains fueling checklists and does not contain battery health printouts. |
| `p32` | optional | 0.100 | 30 | The rollout coordinator checks that the sensor cart has arrived before calibration begins. |
| `p24` | - | 0.017 | 29 | Dev Rao signs the release sheet after the structural team entry appears. |

### PASS content_01_aero_support / q12_three_hop / budget 256

Question: Which team files the binder needed for the document required by Hangar 2 staging?

Selected: `['p06', 'p07', 'p08', 'p19', 'p28', 'p31', 'p33', 'p34']`
Tokens: `232/256`
F1: `0.857` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `['p33', 'p34']`

Score breakdown:

- individual: `10.892`
- pair synergy: `12.767`
- triple synergy: `2.222`
- redundancy penalty: `3.570`
- total: `22.311`

Improvement hint: Add wrong-context or contradiction-aware features; a distractor beat required evidence.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `p07` | selected, required | 1.650 | 27 | Hangar 2 staging requires the previous evening battery health printout. |
| `p19` | selected, required | 2.450 | 29 | Hangar 2 has limited power during winter calibration, so staging must be early. |
| `p06` | selected, required | 1.967 | 29 | The sensor cart must be staged beside Hangar 2 during winter calibration. |
| `p28` | selected, required | 0.500 | 29 | Ground power files Binder Blue after the battery cart is returned. |
| `p08` | selected, required | 1.558 | 28 | The previous evening battery health printout is filed in Binder Blue. |
| `p31` | selected, required | 1.500 | 29 | The ground power team owns the battery health printout process for Atlas staging. |
| `p33` | selected, distractor | 0.917 | 30 | Hangar 3 accepts overnight staging only for paint-shop air filters, not Atlas calibration carts. |
| `p34` | selected, distractor | 0.350 | 31 | Binder Green contains fueling checklists and does not contain battery health printouts. |
| `p32` | optional | 0.100 | 30 | The rollout coordinator checks that the sensor cart has arrived before calibration begins. |
| `p24` | - | 0.017 | 29 | Dev Rao signs the release sheet after the structural team entry appears. |

### PASS content_01_aero_support / q12_three_hop / budget 512

Question: Which team files the binder needed for the document required by Hangar 2 staging?

Selected: `['p06', 'p07', 'p08', 'p19', 'p24', 'p28', 'p31', 'p32', 'p33', 'p34']`
Tokens: `291/512`
F1: `0.824` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `['p33', 'p34']`

Score breakdown:

- individual: `11.008`
- pair synergy: `15.396`
- triple synergy: `4.028`
- redundancy penalty: `4.092`
- total: `26.340`

Improvement hint: Add wrong-context or contradiction-aware features; a distractor beat required evidence.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `p07` | selected, required | 1.650 | 27 | Hangar 2 staging requires the previous evening battery health printout. |
| `p19` | selected, required | 2.450 | 29 | Hangar 2 has limited power during winter calibration, so staging must be early. |
| `p06` | selected, required | 1.967 | 29 | The sensor cart must be staged beside Hangar 2 during winter calibration. |
| `p28` | selected, required | 0.500 | 29 | Ground power files Binder Blue after the battery cart is returned. |
| `p08` | selected, required | 1.558 | 28 | The previous evening battery health printout is filed in Binder Blue. |
| `p31` | selected, required | 1.500 | 29 | The ground power team owns the battery health printout process for Atlas staging. |
| `p33` | selected, distractor | 0.917 | 30 | Hangar 3 accepts overnight staging only for paint-shop air filters, not Atlas calibration carts. |
| `p34` | selected, distractor | 0.350 | 31 | Binder Green contains fueling checklists and does not contain battery health printouts. |
| `p32` | selected, optional | 0.100 | 30 | The rollout coordinator checks that the sensor cart has arrived before calibration begins. |
| `p24` | selected | 0.017 | 29 | Dev Rao signs the release sheet after the structural team entry appears. |

### PASS content_01_aero_support / q12_three_hop / budget 1024

Question: Which team files the binder needed for the document required by Hangar 2 staging?

Selected: `['p06', 'p07', 'p08', 'p19', 'p24', 'p28', 'p31', 'p32', 'p33', 'p34']`
Tokens: `291/1024`
F1: `0.824` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `['p33', 'p34']`

Score breakdown:

- individual: `11.008`
- pair synergy: `15.396`
- triple synergy: `4.028`
- redundancy penalty: `4.092`
- total: `26.340`

Improvement hint: Add wrong-context or contradiction-aware features; a distractor beat required evidence.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `p07` | selected, required | 1.650 | 27 | Hangar 2 staging requires the previous evening battery health printout. |
| `p19` | selected, required | 2.450 | 29 | Hangar 2 has limited power during winter calibration, so staging must be early. |
| `p06` | selected, required | 1.967 | 29 | The sensor cart must be staged beside Hangar 2 during winter calibration. |
| `p28` | selected, required | 0.500 | 29 | Ground power files Binder Blue after the battery cart is returned. |
| `p08` | selected, required | 1.558 | 28 | The previous evening battery health printout is filed in Binder Blue. |
| `p31` | selected, required | 1.500 | 29 | The ground power team owns the battery health printout process for Atlas staging. |
| `p33` | selected, distractor | 0.917 | 30 | Hangar 3 accepts overnight staging only for paint-shop air filters, not Atlas calibration carts. |
| `p34` | selected, distractor | 0.350 | 31 | Binder Green contains fueling checklists and does not contain battery health printouts. |
| `p32` | selected, optional | 0.100 | 30 | The rollout coordinator checks that the sensor cart has arrived before calibration begins. |
| `p24` | selected | 0.017 | 29 | Dev Rao signs the release sheet after the structural team entry appears. |

### FAIL content_01_aero_support / q13_three_hop / budget 128

Question: Who reviews the record after the team assigned to the aft warning completes its required log?

Selected: `['p09', 'p10', 'p22', 'p36']`
Tokens: `119/128`
F1: `0.600` Required recall: `0.500`
Missing required units: `['log', 'reviewer']`
Selected distractors: `['p22']`

Score breakdown:

- individual: `6.302`
- pair synergy: `3.758`
- triple synergy: `0.000`
- redundancy penalty: `1.384`
- total: `8.675`

Improvement hint: Add wrong-context or contradiction-aware features; a distractor beat required evidence.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `p10` | selected, required | 2.135 | 29 | When the aft temperature warning appears, left harness inspection is assigned to structural. |
| `p38` | optional | 1.045 | 27 | The aft temperature warning should not be routed to the electrical corrosion queue. |
| `p24` | required | 0.712 | 29 | Dev Rao signs the release sheet after the structural team entry appears. |
| `p09` | selected, required | 1.712 | 30 | Atlas field reports link the aft temperature warning to insulation rubbing the left harness. |
| `p36` | selected, required | 1.409 | 30 | A duplicate aft-warning note says cold starts can make insulation rub the left harness. |
| `p22` | selected, distractor | 1.045 | 30 | The electrical team reviews right-harness corrosion alerts, not left-harness insulation rubs. |
| `p37` | optional | 0.945 | 31 | A clerk may shelve the amber ledger beside fuel records after Dev Rao reviews it. |
| `p12` | required | 0.373 | 27 | Shift controller Dev Rao reviews the amber maintenance ledger. |
| `p39` | required | 0.100 | 28 | Release paperwork is held until the amber ledger contains the structural inspection entry. |
| `p28` | - | -0.044 | 29 | Ground power files Binder Blue after the battery cart is returned. |

### FAIL content_01_aero_support / q13_three_hop / budget 256

Question: Who reviews the record after the team assigned to the aft warning completes its required log?

Selected: `['p09', 'p10', 'p12', 'p22', 'p24', 'p36', 'p37', 'p38']`
Tokens: `233/256`
F1: `0.808` Required recall: `0.750`
Missing required units: `['log']`
Selected distractors: `['p22']`

Score breakdown:

- individual: `9.377`
- pair synergy: `12.007`
- triple synergy: `1.818`
- redundancy penalty: `3.114`
- total: `20.088`

Improvement hint: Add wrong-context or contradiction-aware features; a distractor beat required evidence.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `p10` | selected, required | 2.135 | 29 | When the aft temperature warning appears, left harness inspection is assigned to structural. |
| `p38` | selected, optional | 1.045 | 27 | The aft temperature warning should not be routed to the electrical corrosion queue. |
| `p24` | selected, required | 0.712 | 29 | Dev Rao signs the release sheet after the structural team entry appears. |
| `p09` | selected, required | 1.712 | 30 | Atlas field reports link the aft temperature warning to insulation rubbing the left harness. |
| `p36` | selected, required | 1.409 | 30 | A duplicate aft-warning note says cold starts can make insulation rub the left harness. |
| `p22` | selected, distractor | 1.045 | 30 | The electrical team reviews right-harness corrosion alerts, not left-harness insulation rubs. |
| `p37` | selected, optional | 0.945 | 31 | A clerk may shelve the amber ledger beside fuel records after Dev Rao reviews it. |
| `p12` | selected, required | 0.373 | 27 | Shift controller Dev Rao reviews the amber maintenance ledger. |
| `p39` | required | 0.100 | 28 | Release paperwork is held until the amber ledger contains the structural inspection entry. |
| `p28` | - | -0.044 | 29 | Ground power files Binder Blue after the battery cart is returned. |

### PASS content_01_aero_support / q13_three_hop / budget 512

Question: Who reviews the record after the team assigned to the aft warning completes its required log?

Selected: `['p09', 'p10', 'p12', 'p22', 'p24', 'p28', 'p36', 'p37', 'p38', 'p39']`
Tokens: `290/512`
F1: `0.889` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `['p22']`

Score breakdown:

- individual: `9.433`
- pair synergy: `14.532`
- triple synergy: `2.727`
- redundancy penalty: `3.817`
- total: `22.875`

Improvement hint: Add wrong-context or contradiction-aware features; a distractor beat required evidence.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `p10` | selected, required | 2.135 | 29 | When the aft temperature warning appears, left harness inspection is assigned to structural. |
| `p38` | selected, optional | 1.045 | 27 | The aft temperature warning should not be routed to the electrical corrosion queue. |
| `p24` | selected, required | 0.712 | 29 | Dev Rao signs the release sheet after the structural team entry appears. |
| `p09` | selected, required | 1.712 | 30 | Atlas field reports link the aft temperature warning to insulation rubbing the left harness. |
| `p36` | selected, required | 1.409 | 30 | A duplicate aft-warning note says cold starts can make insulation rub the left harness. |
| `p22` | selected, distractor | 1.045 | 30 | The electrical team reviews right-harness corrosion alerts, not left-harness insulation rubs. |
| `p37` | selected, optional | 0.945 | 31 | A clerk may shelve the amber ledger beside fuel records after Dev Rao reviews it. |
| `p12` | selected, required | 0.373 | 27 | Shift controller Dev Rao reviews the amber maintenance ledger. |
| `p39` | selected, required | 0.100 | 28 | Release paperwork is held until the amber ledger contains the structural inspection entry. |
| `p28` | selected | -0.044 | 29 | Ground power files Binder Blue after the battery cart is returned. |

### PASS content_01_aero_support / q13_three_hop / budget 1024

Question: Who reviews the record after the team assigned to the aft warning completes its required log?

Selected: `['p09', 'p10', 'p12', 'p22', 'p24', 'p28', 'p36', 'p37', 'p38', 'p39']`
Tokens: `290/1024`
F1: `0.889` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `['p22']`

Score breakdown:

- individual: `9.433`
- pair synergy: `14.532`
- triple synergy: `2.727`
- redundancy penalty: `3.817`
- total: `22.875`

Improvement hint: Add wrong-context or contradiction-aware features; a distractor beat required evidence.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `p10` | selected, required | 2.135 | 29 | When the aft temperature warning appears, left harness inspection is assigned to structural. |
| `p38` | selected, optional | 1.045 | 27 | The aft temperature warning should not be routed to the electrical corrosion queue. |
| `p24` | selected, required | 0.712 | 29 | Dev Rao signs the release sheet after the structural team entry appears. |
| `p09` | selected, required | 1.712 | 30 | Atlas field reports link the aft temperature warning to insulation rubbing the left harness. |
| `p36` | selected, required | 1.409 | 30 | A duplicate aft-warning note says cold starts can make insulation rub the left harness. |
| `p22` | selected, distractor | 1.045 | 30 | The electrical team reviews right-harness corrosion alerts, not left-harness insulation rubs. |
| `p37` | selected, optional | 0.945 | 31 | A clerk may shelve the amber ledger beside fuel records after Dev Rao reviews it. |
| `p12` | selected, required | 0.373 | 27 | Shift controller Dev Rao reviews the amber maintenance ledger. |
| `p39` | selected, required | 0.100 | 28 | Release paperwork is held until the amber ledger contains the structural inspection entry. |
| `p28` | selected | -0.044 | 29 | Ground power files Binder Blue after the battery cart is returned. |

### FAIL content_01_aero_support / q14_three_hop / budget 128

Question: Before winter calibration, which binder should be checked for the printout required by Hangar 2 staging?

Selected: `['p06', 'p07', 'p08', 'p19']`
Tokens: `113/128`
F1: `0.857` Required recall: `0.750`
Missing required units: `['start_time']`
Selected distractors: `[]`

Score breakdown:

- individual: `9.616`
- pair synergy: `3.591`
- triple synergy: `0.114`
- redundancy penalty: `1.210`
- total: `12.110`

Improvement hint: Scoring issue; required evidence was available but not valuable enough under current utility.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `p19` | selected, required | 3.114 | 29 | Hangar 2 has limited power during winter calibration, so staging must be early. |
| `p07` | selected, required | 1.891 | 27 | Hangar 2 staging requires the previous evening battery health printout. |
| `p06` | selected, required | 2.691 | 29 | The sensor cart must be staged beside Hangar 2 during winter calibration. |
| `p05` | required | 1.068 | 28 | The winter calibration window begins at 06:30 before the first engine run. |
| `p08` | selected, required | 1.920 | 28 | The previous evening battery health printout is filed in Binder Blue. |
| `p31` | optional | 1.379 | 29 | The ground power team owns the battery health printout process for Atlas staging. |
| `p33` | distractor | 1.218 | 30 | Hangar 3 accepts overnight staging only for paint-shop air filters, not Atlas calibration carts. |
| `p32` | optional | 0.945 | 30 | The rollout coordinator checks that the sensor cart has arrived before calibration begins. |
| `p34` | distractor | 0.289 | 31 | Binder Green contains fueling checklists and does not contain battery health printouts. |
| `p11` | - | -0.044 | 28 | Structural inspections must be logged in the amber maintenance ledger before release. |

### PASS content_01_aero_support / q14_three_hop / budget 256

Question: Before winter calibration, which binder should be checked for the printout required by Hangar 2 staging?

Selected: `['p05', 'p06', 'p07', 'p08', 'p19', 'p31', 'p32', 'p33']`
Tokens: `230/256`
F1: `0.933` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `['p33']`

Score breakdown:

- individual: `14.227`
- pair synergy: `12.781`
- triple synergy: `2.841`
- redundancy penalty: `3.122`
- total: `26.727`

Improvement hint: Add wrong-context or contradiction-aware features; a distractor beat required evidence.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `p19` | selected, required | 3.114 | 29 | Hangar 2 has limited power during winter calibration, so staging must be early. |
| `p07` | selected, required | 1.891 | 27 | Hangar 2 staging requires the previous evening battery health printout. |
| `p06` | selected, required | 2.691 | 29 | The sensor cart must be staged beside Hangar 2 during winter calibration. |
| `p05` | selected, required | 1.068 | 28 | The winter calibration window begins at 06:30 before the first engine run. |
| `p08` | selected, required | 1.920 | 28 | The previous evening battery health printout is filed in Binder Blue. |
| `p31` | selected, optional | 1.379 | 29 | The ground power team owns the battery health printout process for Atlas staging. |
| `p33` | selected, distractor | 1.218 | 30 | Hangar 3 accepts overnight staging only for paint-shop air filters, not Atlas calibration carts. |
| `p32` | selected, optional | 0.945 | 30 | The rollout coordinator checks that the sensor cart has arrived before calibration begins. |
| `p34` | distractor | 0.289 | 31 | Binder Green contains fueling checklists and does not contain battery health printouts. |
| `p11` | - | -0.044 | 28 | Structural inspections must be logged in the amber maintenance ledger before release. |

### PASS content_01_aero_support / q14_three_hop / budget 512

Question: Before winter calibration, which binder should be checked for the printout required by Hangar 2 staging?

Selected: `['p05', 'p06', 'p07', 'p08', 'p11', 'p19', 'p31', 'p32', 'p33', 'p34']`
Tokens: `289/512`
F1: `0.824` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `['p33', 'p34']`

Score breakdown:

- individual: `14.472`
- pair synergy: `16.926`
- triple synergy: `6.705`
- redundancy penalty: `3.864`
- total: `34.239`

Improvement hint: Add wrong-context or contradiction-aware features; a distractor beat required evidence.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `p19` | selected, required | 3.114 | 29 | Hangar 2 has limited power during winter calibration, so staging must be early. |
| `p07` | selected, required | 1.891 | 27 | Hangar 2 staging requires the previous evening battery health printout. |
| `p06` | selected, required | 2.691 | 29 | The sensor cart must be staged beside Hangar 2 during winter calibration. |
| `p05` | selected, required | 1.068 | 28 | The winter calibration window begins at 06:30 before the first engine run. |
| `p08` | selected, required | 1.920 | 28 | The previous evening battery health printout is filed in Binder Blue. |
| `p31` | selected, optional | 1.379 | 29 | The ground power team owns the battery health printout process for Atlas staging. |
| `p33` | selected, distractor | 1.218 | 30 | Hangar 3 accepts overnight staging only for paint-shop air filters, not Atlas calibration carts. |
| `p32` | selected, optional | 0.945 | 30 | The rollout coordinator checks that the sensor cart has arrived before calibration begins. |
| `p34` | selected, distractor | 0.289 | 31 | Binder Green contains fueling checklists and does not contain battery health printouts. |
| `p11` | selected | -0.044 | 28 | Structural inspections must be logged in the amber maintenance ledger before release. |

### PASS content_01_aero_support / q14_three_hop / budget 1024

Question: Before winter calibration, which binder should be checked for the printout required by Hangar 2 staging?

Selected: `['p05', 'p06', 'p07', 'p08', 'p11', 'p19', 'p31', 'p32', 'p33', 'p34']`
Tokens: `289/1024`
F1: `0.824` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `['p33', 'p34']`

Score breakdown:

- individual: `14.472`
- pair synergy: `16.926`
- triple synergy: `6.705`
- redundancy penalty: `3.864`
- total: `34.239`

Improvement hint: Add wrong-context or contradiction-aware features; a distractor beat required evidence.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `p19` | selected, required | 3.114 | 29 | Hangar 2 has limited power during winter calibration, so staging must be early. |
| `p07` | selected, required | 1.891 | 27 | Hangar 2 staging requires the previous evening battery health printout. |
| `p06` | selected, required | 2.691 | 29 | The sensor cart must be staged beside Hangar 2 during winter calibration. |
| `p05` | selected, required | 1.068 | 28 | The winter calibration window begins at 06:30 before the first engine run. |
| `p08` | selected, required | 1.920 | 28 | The previous evening battery health printout is filed in Binder Blue. |
| `p31` | selected, optional | 1.379 | 29 | The ground power team owns the battery health printout process for Atlas staging. |
| `p33` | selected, distractor | 1.218 | 30 | Hangar 3 accepts overnight staging only for paint-shop air filters, not Atlas calibration carts. |
| `p32` | selected, optional | 0.945 | 30 | The rollout coordinator checks that the sensor cart has arrived before calibration begins. |
| `p34` | selected, distractor | 0.289 | 31 | Binder Green contains fueling checklists and does not contain battery health printouts. |
| `p11` | selected | -0.044 | 28 | Structural inspections must be logged in the amber maintenance ledger before release. |

### FAIL content_01_aero_support / q15_three_hop / budget 128

Question: Who signs off after the structural team handles the aft temperature warning workflow?

Selected: `['p09', 'p10', 'p24', 'p38']`
Tokens: `115/128`
F1: `0.857` Required recall: `0.750`
Missing required units: `['log']`
Selected distractors: `[]`

Score breakdown:

- individual: `8.100`
- pair synergy: `3.533`
- triple synergy: `0.000`
- redundancy penalty: `0.931`
- total: `10.702`

Improvement hint: Scoring issue; required evidence was available but not valuable enough under current utility.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `p10` | selected, required | 2.667 | 29 | When the aft temperature warning appears, left harness inspection is assigned to structural. |
| `p24` | selected, required | 1.667 | 29 | Dev Rao signs the release sheet after the structural team entry appears. |
| `p38` | selected, optional | 1.550 | 27 | The aft temperature warning should not be routed to the electrical corrosion queue. |
| `p09` | selected, required | 2.217 | 30 | Atlas field reports link the aft temperature warning to insulation rubbing the left harness. |
| `p36` | required | 1.464 | 30 | A duplicate aft-warning note says cold starts can make insulation rub the left harness. |
| `p22` | distractor | 0.650 | 30 | The electrical team reviews right-harness corrosion alerts, not left-harness insulation rubs. |
| `p39` | required | 0.550 | 28 | Release paperwork is held until the amber ledger contains the structural inspection entry. |
| `p37` | - | 0.550 | 31 | A clerk may shelve the amber ledger beside fuel records after Dev Rao reviews it. |
| `p11` | required | 0.317 | 28 | Structural inspections must be logged in the amber maintenance ledger before release. |
| `p28` | - | -0.017 | 29 | Ground power files Binder Blue after the battery cart is returned. |

### PASS content_01_aero_support / q15_three_hop / budget 256

Question: Who signs off after the structural team handles the aft temperature warning workflow?

Selected: `['p09', 'p10', 'p22', 'p24', 'p36', 'p37', 'p38', 'p39']`
Tokens: `234/256`
F1: `0.857` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `['p22']`

Score breakdown:

- individual: `11.314`
- pair synergy: `10.856`
- triple synergy: `1.375`
- redundancy penalty: `2.980`
- total: `20.565`

Improvement hint: Add wrong-context or contradiction-aware features; a distractor beat required evidence.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `p10` | selected, required | 2.667 | 29 | When the aft temperature warning appears, left harness inspection is assigned to structural. |
| `p24` | selected, required | 1.667 | 29 | Dev Rao signs the release sheet after the structural team entry appears. |
| `p38` | selected, optional | 1.550 | 27 | The aft temperature warning should not be routed to the electrical corrosion queue. |
| `p09` | selected, required | 2.217 | 30 | Atlas field reports link the aft temperature warning to insulation rubbing the left harness. |
| `p36` | selected, required | 1.464 | 30 | A duplicate aft-warning note says cold starts can make insulation rub the left harness. |
| `p22` | selected, distractor | 0.650 | 30 | The electrical team reviews right-harness corrosion alerts, not left-harness insulation rubs. |
| `p39` | selected, required | 0.550 | 28 | Release paperwork is held until the amber ledger contains the structural inspection entry. |
| `p37` | selected | 0.550 | 31 | A clerk may shelve the amber ledger beside fuel records after Dev Rao reviews it. |
| `p11` | required | 0.317 | 28 | Structural inspections must be logged in the amber maintenance ledger before release. |
| `p28` | - | -0.017 | 29 | Ground power files Binder Blue after the battery cart is returned. |

### PASS content_01_aero_support / q15_three_hop / budget 512

Question: Who signs off after the structural team handles the aft temperature warning workflow?

Selected: `['p09', 'p10', 'p11', 'p22', 'p24', 'p28', 'p36', 'p37', 'p38', 'p39']`
Tokens: `291/512`
F1: `0.824` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `['p22']`

Score breakdown:

- individual: `11.614`
- pair synergy: `14.722`
- triple synergy: `3.750`
- redundancy penalty: `3.715`
- total: `26.371`

Improvement hint: Add wrong-context or contradiction-aware features; a distractor beat required evidence.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `p10` | selected, required | 2.667 | 29 | When the aft temperature warning appears, left harness inspection is assigned to structural. |
| `p24` | selected, required | 1.667 | 29 | Dev Rao signs the release sheet after the structural team entry appears. |
| `p38` | selected, optional | 1.550 | 27 | The aft temperature warning should not be routed to the electrical corrosion queue. |
| `p09` | selected, required | 2.217 | 30 | Atlas field reports link the aft temperature warning to insulation rubbing the left harness. |
| `p36` | selected, required | 1.464 | 30 | A duplicate aft-warning note says cold starts can make insulation rub the left harness. |
| `p22` | selected, distractor | 0.650 | 30 | The electrical team reviews right-harness corrosion alerts, not left-harness insulation rubs. |
| `p39` | selected, required | 0.550 | 28 | Release paperwork is held until the amber ledger contains the structural inspection entry. |
| `p37` | selected | 0.550 | 31 | A clerk may shelve the amber ledger beside fuel records after Dev Rao reviews it. |
| `p11` | selected, required | 0.317 | 28 | Structural inspections must be logged in the amber maintenance ledger before release. |
| `p28` | selected | -0.017 | 29 | Ground power files Binder Blue after the battery cart is returned. |

### PASS content_01_aero_support / q15_three_hop / budget 1024

Question: Who signs off after the structural team handles the aft temperature warning workflow?

Selected: `['p09', 'p10', 'p11', 'p22', 'p24', 'p28', 'p36', 'p37', 'p38', 'p39']`
Tokens: `291/1024`
F1: `0.824` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `['p22']`

Score breakdown:

- individual: `11.614`
- pair synergy: `14.722`
- triple synergy: `3.750`
- redundancy penalty: `3.715`
- total: `26.371`

Improvement hint: Add wrong-context or contradiction-aware features; a distractor beat required evidence.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `p10` | selected, required | 2.667 | 29 | When the aft temperature warning appears, left harness inspection is assigned to structural. |
| `p24` | selected, required | 1.667 | 29 | Dev Rao signs the release sheet after the structural team entry appears. |
| `p38` | selected, optional | 1.550 | 27 | The aft temperature warning should not be routed to the electrical corrosion queue. |
| `p09` | selected, required | 2.217 | 30 | Atlas field reports link the aft temperature warning to insulation rubbing the left harness. |
| `p36` | selected, required | 1.464 | 30 | A duplicate aft-warning note says cold starts can make insulation rub the left harness. |
| `p22` | selected, distractor | 0.650 | 30 | The electrical team reviews right-harness corrosion alerts, not left-harness insulation rubs. |
| `p39` | selected, required | 0.550 | 28 | Release paperwork is held until the amber ledger contains the structural inspection entry. |
| `p37` | selected | 0.550 | 31 | A clerk may shelve the amber ledger beside fuel records after Dev Rao reviews it. |
| `p11` | selected, required | 0.317 | 28 | Structural inspections must be logged in the amber maintenance ledger before release. |
| `p28` | selected | -0.017 | 29 | Ground power files Binder Blue after the battery cart is returned. |

### FAIL content_02_clinic_access / c_q01_direct / budget 128

Question: Where should a visiting student fix a badge denial?

Selected: `['c04', 'c15', 'c16', 'c24']`
Tokens: `123/128`
F1: `0.000` Required recall: `0.000`
Missing required units: `['student_access', 'annex_alias']`
Selected distractors: `['c04']`

Score breakdown:

- individual: `4.683`
- pair synergy: `1.400`
- triple synergy: `0.000`
- redundancy penalty: `0.565`
- total: `5.519`

Improvement hint: Add wrong-context or contradiction-aware features; a distractor beat required evidence.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `c04` | selected, distractor | 2.467 | 31 | A badge denial for visiting students should be fixed at reception by the visitor badge desk. |
| `c24` | selected | 1.167 | 30 | Expired wristband replacement points to the security map label after a badge denial. |
| `c16` | selected | 0.517 | 31 | Slate courier envelopes before night audit should be signed at the blood desk. |
| `c01` | required | -0.467 | 27 | Blue-lanyard observers receive a temporary pass from the learning office, not from reception. |
| `c15` | selected | 0.533 | 31 | The archive cart is signed out by Omar Singh before the night audit. |
| `c13` | - | 0.486 | 27 | Courier envelopes marked slate are routed to diagnostic imaging. |
| `c03` | optional | -0.050 | 28 | Reception prints visitor badges only for family members and vendors. |
| `c02` | required | -0.050 | 29 | The learning office is called the North Annex counter in weekend notes. |
| `c35` | - | -0.050 | 30 | Mateo Ruiz works from the small office behind registration. |
| `c21` | - | -0.200 | 27 | Expired wristbands are replaced at the intake island. |

### FAIL content_02_clinic_access / c_q01_direct / budget 256

Question: Where should a visiting student fix a badge denial?

Selected: `['c03', 'c04', 'c13', 'c15', 'c16', 'c24']`
Tokens: `178/256`
F1: `0.000` Required recall: `0.000`
Missing required units: `['student_access', 'annex_alias']`
Selected distractors: `['c04']`

Score breakdown:

- individual: `5.119`
- pair synergy: `2.214`
- triple synergy: `0.000`
- redundancy penalty: `0.956`
- total: `6.378`

Improvement hint: Add wrong-context or contradiction-aware features; a distractor beat required evidence.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `c04` | selected, distractor | 2.467 | 31 | A badge denial for visiting students should be fixed at reception by the visitor badge desk. |
| `c24` | selected | 1.167 | 30 | Expired wristband replacement points to the security map label after a badge denial. |
| `c16` | selected | 0.517 | 31 | Slate courier envelopes before night audit should be signed at the blood desk. |
| `c01` | required | -0.467 | 27 | Blue-lanyard observers receive a temporary pass from the learning office, not from reception. |
| `c15` | selected | 0.533 | 31 | The archive cart is signed out by Omar Singh before the night audit. |
| `c13` | selected | 0.486 | 27 | Courier envelopes marked slate are routed to diagnostic imaging. |
| `c03` | selected, optional | -0.050 | 28 | Reception prints visitor badges only for family members and vendors. |
| `c02` | required | -0.050 | 29 | The learning office is called the North Annex counter in weekend notes. |
| `c35` | - | -0.050 | 30 | Mateo Ruiz works from the small office behind registration. |
| `c21` | - | -0.200 | 27 | Expired wristbands are replaced at the intake island. |

### PASS content_02_clinic_access / c_q01_direct / budget 512

Question: Where should a visiting student fix a badge denial?

Selected: `['c01', 'c02', 'c03', 'c04', 'c13', 'c15', 'c16', 'c24', 'c35']`
Tokens: `264/512`
F1: `0.500` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `['c04']`

Score breakdown:

- individual: `4.552`
- pair synergy: `3.248`
- triple synergy: `0.000`
- redundancy penalty: `1.417`
- total: `6.383`

Improvement hint: Add wrong-context or contradiction-aware features; a distractor beat required evidence.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `c04` | selected, distractor | 2.467 | 31 | A badge denial for visiting students should be fixed at reception by the visitor badge desk. |
| `c24` | selected | 1.167 | 30 | Expired wristband replacement points to the security map label after a badge denial. |
| `c16` | selected | 0.517 | 31 | Slate courier envelopes before night audit should be signed at the blood desk. |
| `c01` | selected, required | -0.467 | 27 | Blue-lanyard observers receive a temporary pass from the learning office, not from reception. |
| `c15` | selected | 0.533 | 31 | The archive cart is signed out by Omar Singh before the night audit. |
| `c13` | selected | 0.486 | 27 | Courier envelopes marked slate are routed to diagnostic imaging. |
| `c03` | selected, optional | -0.050 | 28 | Reception prints visitor badges only for family members and vendors. |
| `c02` | selected, required | -0.050 | 29 | The learning office is called the North Annex counter in weekend notes. |
| `c35` | selected | -0.050 | 30 | Mateo Ruiz works from the small office behind registration. |
| `c21` | - | -0.200 | 27 | Expired wristbands are replaced at the intake island. |

### PASS content_02_clinic_access / c_q01_direct / budget 1024

Question: Where should a visiting student fix a badge denial?

Selected: `['c01', 'c02', 'c03', 'c04', 'c13', 'c15', 'c16', 'c24', 'c35']`
Tokens: `264/1024`
F1: `0.500` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `['c04']`

Score breakdown:

- individual: `4.552`
- pair synergy: `3.248`
- triple synergy: `0.000`
- redundancy penalty: `1.417`
- total: `6.383`

Improvement hint: Add wrong-context or contradiction-aware features; a distractor beat required evidence.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `c04` | selected, distractor | 2.467 | 31 | A badge denial for visiting students should be fixed at reception by the visitor badge desk. |
| `c24` | selected | 1.167 | 30 | Expired wristband replacement points to the security map label after a badge denial. |
| `c16` | selected | 0.517 | 31 | Slate courier envelopes before night audit should be signed at the blood desk. |
| `c01` | selected, required | -0.467 | 27 | Blue-lanyard observers receive a temporary pass from the learning office, not from reception. |
| `c15` | selected | 0.533 | 31 | The archive cart is signed out by Omar Singh before the night audit. |
| `c13` | selected | 0.486 | 27 | Courier envelopes marked slate are routed to diagnostic imaging. |
| `c03` | selected, optional | -0.050 | 28 | Reception prints visitor badges only for family members and vendors. |
| `c02` | selected, required | -0.050 | 29 | The learning office is called the North Annex counter in weekend notes. |
| `c35` | selected | -0.050 | 30 | Mateo Ruiz works from the small office behind registration. |
| `c21` | - | -0.200 | 27 | Expired wristbands are replaced at the intake island. |

### PASS content_02_clinic_access / c_q02_direct / budget 128

Question: Who initials access for the sedation cabinet keys?

Selected: `['c05', 'c06', 'c08', 'c23']`
Tokens: `115/128`
F1: `0.667` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `['c08']`

Score breakdown:

- individual: `7.407`
- pair synergy: `3.436`
- triple synergy: `0.500`
- redundancy penalty: `0.858`
- total: `10.485`

Improvement hint: Add wrong-context or contradiction-aware features; a distractor beat required evidence.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `c05` | selected, required | 3.325 | 27 | The sedation cabinet releases keys after the orange ledger is initialed. |
| `c08` | selected, distractor | 3.325 | 30 | Sedation cabinet keys are approved by pharmacy when the orange ledger is missing. |
| `c06` | selected, required | 0.807 | 28 | Orange ledger initials are supplied by the recovery charge nurse. |
| `c23` | selected | -0.050 | 30 | Coral map labels are maintained by facilities, not by the access team. |
| `c22` | - | 0.200 | 29 | The intake island is labeled Coral on the floor map. |
| `c12` | - | -0.371 | 31 | The quiet room after evening overflow is handled by the triage nurse for pediatric fever cases. |
| `c01` | - | -0.425 | 27 | Blue-lanyard observers receive a temporary pass from the learning office, not from reception. |
| `c07` | optional | -0.425 | 29 | Pharmacy keeps a separate green narcotics book for medication counts. |
| `c27` | - | -0.425 | 29 | Remote-care scheduling uses the amber queue after noon. |
| `c30` | - | -0.425 | 29 | Microbiology batches after-hours samples under code M-14. |

### PASS content_02_clinic_access / c_q02_direct / budget 256

Question: Who initials access for the sedation cabinet keys?

Selected: `['c05', 'c06', 'c08', 'c22', 'c23']`
Tokens: `144/256`
F1: `0.571` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `['c08']`

Score breakdown:

- individual: `7.607`
- pair synergy: `3.836`
- triple synergy: `0.500`
- redundancy penalty: `1.045`
- total: `10.898`

Improvement hint: Add wrong-context or contradiction-aware features; a distractor beat required evidence.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `c05` | selected, required | 3.325 | 27 | The sedation cabinet releases keys after the orange ledger is initialed. |
| `c08` | selected, distractor | 3.325 | 30 | Sedation cabinet keys are approved by pharmacy when the orange ledger is missing. |
| `c06` | selected, required | 0.807 | 28 | Orange ledger initials are supplied by the recovery charge nurse. |
| `c23` | selected | -0.050 | 30 | Coral map labels are maintained by facilities, not by the access team. |
| `c22` | selected | 0.200 | 29 | The intake island is labeled Coral on the floor map. |
| `c12` | - | -0.371 | 31 | The quiet room after evening overflow is handled by the triage nurse for pediatric fever cases. |
| `c01` | - | -0.425 | 27 | Blue-lanyard observers receive a temporary pass from the learning office, not from reception. |
| `c07` | optional | -0.425 | 29 | Pharmacy keeps a separate green narcotics book for medication counts. |
| `c27` | - | -0.425 | 29 | Remote-care scheduling uses the amber queue after noon. |
| `c30` | - | -0.425 | 29 | Microbiology batches after-hours samples under code M-14. |

### PASS content_02_clinic_access / c_q02_direct / budget 512

Question: Who initials access for the sedation cabinet keys?

Selected: `['c05', 'c06', 'c08', 'c22', 'c23']`
Tokens: `144/512`
F1: `0.571` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `['c08']`

Score breakdown:

- individual: `7.607`
- pair synergy: `3.836`
- triple synergy: `0.500`
- redundancy penalty: `1.045`
- total: `10.898`

Improvement hint: Add wrong-context or contradiction-aware features; a distractor beat required evidence.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `c05` | selected, required | 3.325 | 27 | The sedation cabinet releases keys after the orange ledger is initialed. |
| `c08` | selected, distractor | 3.325 | 30 | Sedation cabinet keys are approved by pharmacy when the orange ledger is missing. |
| `c06` | selected, required | 0.807 | 28 | Orange ledger initials are supplied by the recovery charge nurse. |
| `c23` | selected | -0.050 | 30 | Coral map labels are maintained by facilities, not by the access team. |
| `c22` | selected | 0.200 | 29 | The intake island is labeled Coral on the floor map. |
| `c12` | - | -0.371 | 31 | The quiet room after evening overflow is handled by the triage nurse for pediatric fever cases. |
| `c01` | - | -0.425 | 27 | Blue-lanyard observers receive a temporary pass from the learning office, not from reception. |
| `c07` | optional | -0.425 | 29 | Pharmacy keeps a separate green narcotics book for medication counts. |
| `c27` | - | -0.425 | 29 | Remote-care scheduling uses the amber queue after noon. |
| `c30` | - | -0.425 | 29 | Microbiology batches after-hours samples under code M-14. |

### PASS content_02_clinic_access / c_q02_direct / budget 1024

Question: Who initials access for the sedation cabinet keys?

Selected: `['c05', 'c06', 'c08', 'c22', 'c23']`
Tokens: `144/1024`
F1: `0.571` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `['c08']`

Score breakdown:

- individual: `7.607`
- pair synergy: `3.836`
- triple synergy: `0.500`
- redundancy penalty: `1.045`
- total: `10.898`

Improvement hint: Add wrong-context or contradiction-aware features; a distractor beat required evidence.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `c05` | selected, required | 3.325 | 27 | The sedation cabinet releases keys after the orange ledger is initialed. |
| `c08` | selected, distractor | 3.325 | 30 | Sedation cabinet keys are approved by pharmacy when the orange ledger is missing. |
| `c06` | selected, required | 0.807 | 28 | Orange ledger initials are supplied by the recovery charge nurse. |
| `c23` | selected | -0.050 | 30 | Coral map labels are maintained by facilities, not by the access team. |
| `c22` | selected | 0.200 | 29 | The intake island is labeled Coral on the floor map. |
| `c12` | - | -0.371 | 31 | The quiet room after evening overflow is handled by the triage nurse for pediatric fever cases. |
| `c01` | - | -0.425 | 27 | Blue-lanyard observers receive a temporary pass from the learning office, not from reception. |
| `c07` | optional | -0.425 | 29 | Pharmacy keeps a separate green narcotics book for medication counts. |
| `c27` | - | -0.425 | 29 | Remote-care scheduling uses the amber queue after noon. |
| `c30` | - | -0.425 | 29 | Microbiology batches after-hours samples under code M-14. |

### PASS content_02_clinic_access / c_q03_direct / budget 128

Question: Who handles the quiet room after evening overflow begins?

Selected: `['c09', 'c10', 'c11', 'c12']`
Tokens: `118/128`
F1: `1.000` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `[]`

Score breakdown:

- individual: `6.252`
- pair synergy: `2.324`
- triple synergy: `0.000`
- redundancy penalty: `0.678`
- total: `7.898`

Improvement hint: Successful selection; inspect extra chunks only if precision or token cost becomes the priority.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `c12` | selected, optional | 2.950 | 31 | The quiet room after evening overflow is handled by the triage nurse for pediatric fever cases. |
| `c09` | selected, required | 1.214 | 28 | The quiet room uses a dove marker on the scheduling board. |
| `c11` | selected, required | 1.024 | 30 | Behavioral-health overflow is coordinated by Lina Park after 18:00. |
| `c05` | - | 0.154 | 27 | The sedation cabinet releases keys after the orange ledger is initialed. |
| `c08` | - | 1.075 | 30 | Sedation cabinet keys are approved by pharmacy when the orange ledger is missing. |
| `c10` | selected, required | 1.064 | 29 | Dove markers are assigned to behavioral-health overflow patients. |
| `c27` | - | 0.636 | 29 | Remote-care scheduling uses the amber queue after noon. |
| `c39` | - | 0.207 | 29 | Cultural services keeps evening interpreters on the violet roster. |
| `c30` | - | 0.154 | 29 | Microbiology batches after-hours samples under code M-14. |
| `c24` | - | 0.154 | 30 | Expired wristband replacement points to the security map label after a badge denial. |

### PASS content_02_clinic_access / c_q03_direct / budget 256

Question: Who handles the quiet room after evening overflow begins?

Selected: `['c05', 'c09', 'c10', 'c11', 'c12', 'c24', 'c27', 'c39']`
Tokens: `233/256`
F1: `0.667` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `[]`

Score breakdown:

- individual: `7.402`
- pair synergy: `7.570`
- triple synergy: `1.964`
- redundancy penalty: `1.509`
- total: `15.428`

Improvement hint: Successful selection; inspect extra chunks only if precision or token cost becomes the priority.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `c12` | selected, optional | 2.950 | 31 | The quiet room after evening overflow is handled by the triage nurse for pediatric fever cases. |
| `c09` | selected, required | 1.214 | 28 | The quiet room uses a dove marker on the scheduling board. |
| `c11` | selected, required | 1.024 | 30 | Behavioral-health overflow is coordinated by Lina Park after 18:00. |
| `c05` | selected | 0.154 | 27 | The sedation cabinet releases keys after the orange ledger is initialed. |
| `c08` | - | 1.075 | 30 | Sedation cabinet keys are approved by pharmacy when the orange ledger is missing. |
| `c10` | selected, required | 1.064 | 29 | Dove markers are assigned to behavioral-health overflow patients. |
| `c27` | selected | 0.636 | 29 | Remote-care scheduling uses the amber queue after noon. |
| `c39` | selected | 0.207 | 29 | Cultural services keeps evening interpreters on the violet roster. |
| `c30` | - | 0.154 | 29 | Microbiology batches after-hours samples under code M-14. |
| `c24` | selected | 0.154 | 30 | Expired wristband replacement points to the security map label after a badge denial. |

### PASS content_02_clinic_access / c_q03_direct / budget 512

Question: Who handles the quiet room after evening overflow begins?

Selected: `['c05', 'c08', 'c09', 'c10', 'c11', 'c12', 'c24', 'c27', 'c30', 'c39']`
Tokens: `292/512`
F1: `0.571` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `[]`

Score breakdown:

- individual: `8.631`
- pair synergy: `9.877`
- triple synergy: `2.500`
- redundancy penalty: `2.349`
- total: `18.659`

Improvement hint: Successful selection; inspect extra chunks only if precision or token cost becomes the priority.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `c12` | selected, optional | 2.950 | 31 | The quiet room after evening overflow is handled by the triage nurse for pediatric fever cases. |
| `c09` | selected, required | 1.214 | 28 | The quiet room uses a dove marker on the scheduling board. |
| `c11` | selected, required | 1.024 | 30 | Behavioral-health overflow is coordinated by Lina Park after 18:00. |
| `c05` | selected | 0.154 | 27 | The sedation cabinet releases keys after the orange ledger is initialed. |
| `c08` | selected | 1.075 | 30 | Sedation cabinet keys are approved by pharmacy when the orange ledger is missing. |
| `c10` | selected, required | 1.064 | 29 | Dove markers are assigned to behavioral-health overflow patients. |
| `c27` | selected | 0.636 | 29 | Remote-care scheduling uses the amber queue after noon. |
| `c39` | selected | 0.207 | 29 | Cultural services keeps evening interpreters on the violet roster. |
| `c30` | selected | 0.154 | 29 | Microbiology batches after-hours samples under code M-14. |
| `c24` | selected | 0.154 | 30 | Expired wristband replacement points to the security map label after a badge denial. |

### PASS content_02_clinic_access / c_q03_direct / budget 1024

Question: Who handles the quiet room after evening overflow begins?

Selected: `['c05', 'c08', 'c09', 'c10', 'c11', 'c12', 'c24', 'c27', 'c30', 'c39']`
Tokens: `292/1024`
F1: `0.571` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `[]`

Score breakdown:

- individual: `8.631`
- pair synergy: `9.877`
- triple synergy: `2.500`
- redundancy penalty: `2.349`
- total: `18.659`

Improvement hint: Successful selection; inspect extra chunks only if precision or token cost becomes the priority.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `c12` | selected, optional | 2.950 | 31 | The quiet room after evening overflow is handled by the triage nurse for pediatric fever cases. |
| `c09` | selected, required | 1.214 | 28 | The quiet room uses a dove marker on the scheduling board. |
| `c11` | selected, required | 1.024 | 30 | Behavioral-health overflow is coordinated by Lina Park after 18:00. |
| `c05` | selected | 0.154 | 27 | The sedation cabinet releases keys after the orange ledger is initialed. |
| `c08` | selected | 1.075 | 30 | Sedation cabinet keys are approved by pharmacy when the orange ledger is missing. |
| `c10` | selected, required | 1.064 | 29 | Dove markers are assigned to behavioral-health overflow patients. |
| `c27` | selected | 0.636 | 29 | Remote-care scheduling uses the amber queue after noon. |
| `c39` | selected | 0.207 | 29 | Cultural services keeps evening interpreters on the violet roster. |
| `c30` | selected | 0.154 | 29 | Microbiology batches after-hours samples under code M-14. |
| `c24` | selected | 0.154 | 30 | Expired wristband replacement points to the security map label after a badge denial. |

### PASS content_02_clinic_access / c_q04_direct / budget 128

Question: Who signs out the cart for slate courier envelopes?

Selected: `['c13', 'c14', 'c15', 'c16']`
Tokens: `119/128`
F1: `1.000` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `[]`

Score breakdown:

- individual: `10.045`
- pair synergy: `4.573`
- triple synergy: `0.000`
- redundancy penalty: `1.145`
- total: `13.474`

Improvement hint: Successful selection; inspect extra chunks only if precision or token cost becomes the priority.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `c13` | selected, required | 2.864 | 27 | Courier envelopes marked slate are routed to diagnostic imaging. |
| `c14` | selected, required | 2.864 | 30 | Diagnostic imaging sends slate envelopes to the archive cart near lift B. |
| `c16` | selected, optional | 2.483 | 31 | Slate courier envelopes before night audit should be signed at the blood desk. |
| `c15` | selected, required | 1.833 | 31 | The archive cart is signed out by Omar Singh before the night audit. |
| `c04` | - | -0.133 | 31 | A badge denial for visiting students should be fixed at reception by the visitor badge desk. |
| `c38` | - | -0.300 | 30 | Language assistance is booked by the cultural services desk. |
| `c31` | - | -0.467 | 30 | Code M-14 batches are collected by night runner Sima Chen. |
| `c36` | - | -0.467 | 31 | Bronze chart stickers are cleared by the triage physician before insurance review. |
| `c01` | - | -0.800 | 27 | Blue-lanyard observers receive a temporary pass from the learning office, not from reception. |
| `c05` | - | -0.800 | 27 | The sedation cabinet releases keys after the orange ledger is initialed. |

### PASS content_02_clinic_access / c_q04_direct / budget 256

Question: Who signs out the cart for slate courier envelopes?

Selected: `['c04', 'c13', 'c14', 'c15', 'c16']`
Tokens: `150/256`
F1: `0.889` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `[]`

Score breakdown:

- individual: `9.912`
- pair synergy: `4.840`
- triple synergy: `0.000`
- redundancy penalty: `1.277`
- total: `13.475`

Improvement hint: Successful selection; inspect extra chunks only if precision or token cost becomes the priority.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `c13` | selected, required | 2.864 | 27 | Courier envelopes marked slate are routed to diagnostic imaging. |
| `c14` | selected, required | 2.864 | 30 | Diagnostic imaging sends slate envelopes to the archive cart near lift B. |
| `c16` | selected, optional | 2.483 | 31 | Slate courier envelopes before night audit should be signed at the blood desk. |
| `c15` | selected, required | 1.833 | 31 | The archive cart is signed out by Omar Singh before the night audit. |
| `c04` | selected | -0.133 | 31 | A badge denial for visiting students should be fixed at reception by the visitor badge desk. |
| `c38` | - | -0.300 | 30 | Language assistance is booked by the cultural services desk. |
| `c31` | - | -0.467 | 30 | Code M-14 batches are collected by night runner Sima Chen. |
| `c36` | - | -0.467 | 31 | Bronze chart stickers are cleared by the triage physician before insurance review. |
| `c01` | - | -0.800 | 27 | Blue-lanyard observers receive a temporary pass from the learning office, not from reception. |
| `c05` | - | -0.800 | 27 | The sedation cabinet releases keys after the orange ledger is initialed. |

### PASS content_02_clinic_access / c_q04_direct / budget 512

Question: Who signs out the cart for slate courier envelopes?

Selected: `['c04', 'c13', 'c14', 'c15', 'c16']`
Tokens: `150/512`
F1: `0.889` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `[]`

Score breakdown:

- individual: `9.912`
- pair synergy: `4.840`
- triple synergy: `0.000`
- redundancy penalty: `1.277`
- total: `13.475`

Improvement hint: Successful selection; inspect extra chunks only if precision or token cost becomes the priority.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `c13` | selected, required | 2.864 | 27 | Courier envelopes marked slate are routed to diagnostic imaging. |
| `c14` | selected, required | 2.864 | 30 | Diagnostic imaging sends slate envelopes to the archive cart near lift B. |
| `c16` | selected, optional | 2.483 | 31 | Slate courier envelopes before night audit should be signed at the blood desk. |
| `c15` | selected, required | 1.833 | 31 | The archive cart is signed out by Omar Singh before the night audit. |
| `c04` | selected | -0.133 | 31 | A badge denial for visiting students should be fixed at reception by the visitor badge desk. |
| `c38` | - | -0.300 | 30 | Language assistance is booked by the cultural services desk. |
| `c31` | - | -0.467 | 30 | Code M-14 batches are collected by night runner Sima Chen. |
| `c36` | - | -0.467 | 31 | Bronze chart stickers are cleared by the triage physician before insurance review. |
| `c01` | - | -0.800 | 27 | Blue-lanyard observers receive a temporary pass from the learning office, not from reception. |
| `c05` | - | -0.800 | 27 | The sedation cabinet releases keys after the orange ledger is initialed. |

### PASS content_02_clinic_access / c_q04_direct / budget 1024

Question: Who signs out the cart for slate courier envelopes?

Selected: `['c04', 'c13', 'c14', 'c15', 'c16']`
Tokens: `150/1024`
F1: `0.889` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `[]`

Score breakdown:

- individual: `9.912`
- pair synergy: `4.840`
- triple synergy: `0.000`
- redundancy penalty: `1.277`
- total: `13.475`

Improvement hint: Successful selection; inspect extra chunks only if precision or token cost becomes the priority.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `c13` | selected, required | 2.864 | 27 | Courier envelopes marked slate are routed to diagnostic imaging. |
| `c14` | selected, required | 2.864 | 30 | Diagnostic imaging sends slate envelopes to the archive cart near lift B. |
| `c16` | selected, optional | 2.483 | 31 | Slate courier envelopes before night audit should be signed at the blood desk. |
| `c15` | selected, required | 1.833 | 31 | The archive cart is signed out by Omar Singh before the night audit. |
| `c04` | selected | -0.133 | 31 | A badge denial for visiting students should be fixed at reception by the visitor badge desk. |
| `c38` | - | -0.300 | 30 | Language assistance is booked by the cultural services desk. |
| `c31` | - | -0.467 | 30 | Code M-14 batches are collected by night runner Sima Chen. |
| `c36` | - | -0.467 | 31 | Bronze chart stickers are cleared by the triage physician before insurance review. |
| `c01` | - | -0.800 | 27 | Blue-lanyard observers receive a temporary pass from the learning office, not from reception. |
| `c05` | - | -0.800 | 27 | The sedation cabinet releases keys after the orange ledger is initialed. |

### FAIL content_02_clinic_access / c_q05_direct / budget 128

Question: Where is the person who completes transport paperwork located?

Selected: `['c17', 'c18', 'c20', 'c25']`
Tokens: `117/128`
F1: `0.706` Required recall: `0.667`
Missing required units: `['owner_location']`
Selected distractors: `[]`

Score breakdown:

- individual: `9.893`
- pair synergy: `1.560`
- triple synergy: `0.000`
- redundancy penalty: `0.738`
- total: `10.715`

Improvement hint: Tight-budget tradeoff; improve importance ranking so required evidence beats optional/filler chunks.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `c20` | selected, optional | 4.450 | 31 | The person located at billing completes transport paperwork for red discharge packets. |
| `c17` | selected, required | 2.200 | 29 | The red discharge packet means the patient needs transport paperwork. |
| `c18` | selected, required | 1.900 | 29 | Transport paperwork is completed by the mobility coordinator. |
| `c28` | - | 0.283 | 31 | Silver consent telehealth follow-up slots open through in-person surgery clearance. |
| `c25` | selected | 1.343 | 28 | The silver consent sleeve indicates telehealth follow-up. |
| `c26` | - | 0.700 | 30 | Telehealth follow-up slots are opened by the remote-care scheduler. |
| `c19` | required | 0.400 | 31 | The mobility coordinator sits beside the west stairwell during afternoon rounds. |
| `c37` | - | -0.300 | 28 | The pearl sticker means language assistance is requested. |
| `c29` | - | -0.371 | 27 | A lavender tray tag means samples go to microbiology. |
| `c33` | - | -0.371 | 28 | The bronze sticker on a chart means insurance review is pending. |

### PASS content_02_clinic_access / c_q05_direct / budget 256

Question: Where is the person who completes transport paperwork located?

Selected: `['c17', 'c18', 'c19', 'c20', 'c25', 'c26', 'c28']`
Tokens: `209/256`
F1: `0.727` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `[]`

Score breakdown:

- individual: `11.276`
- pair synergy: `4.945`
- triple synergy: `0.000`
- redundancy penalty: `1.999`
- total: `14.222`

Improvement hint: Successful selection; inspect extra chunks only if precision or token cost becomes the priority.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `c20` | selected, optional | 4.450 | 31 | The person located at billing completes transport paperwork for red discharge packets. |
| `c17` | selected, required | 2.200 | 29 | The red discharge packet means the patient needs transport paperwork. |
| `c18` | selected, required | 1.900 | 29 | Transport paperwork is completed by the mobility coordinator. |
| `c28` | selected | 0.283 | 31 | Silver consent telehealth follow-up slots open through in-person surgery clearance. |
| `c25` | selected | 1.343 | 28 | The silver consent sleeve indicates telehealth follow-up. |
| `c26` | selected | 0.700 | 30 | Telehealth follow-up slots are opened by the remote-care scheduler. |
| `c19` | selected, required | 0.400 | 31 | The mobility coordinator sits beside the west stairwell during afternoon rounds. |
| `c37` | - | -0.300 | 28 | The pearl sticker means language assistance is requested. |
| `c29` | - | -0.371 | 27 | A lavender tray tag means samples go to microbiology. |
| `c33` | - | -0.371 | 28 | The bronze sticker on a chart means insurance review is pending. |

### PASS content_02_clinic_access / c_q05_direct / budget 512

Question: Where is the person who completes transport paperwork located?

Selected: `['c17', 'c18', 'c19', 'c20', 'c25', 'c26', 'c28']`
Tokens: `209/512`
F1: `0.727` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `[]`

Score breakdown:

- individual: `11.276`
- pair synergy: `4.945`
- triple synergy: `0.000`
- redundancy penalty: `1.999`
- total: `14.222`

Improvement hint: Successful selection; inspect extra chunks only if precision or token cost becomes the priority.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `c20` | selected, optional | 4.450 | 31 | The person located at billing completes transport paperwork for red discharge packets. |
| `c17` | selected, required | 2.200 | 29 | The red discharge packet means the patient needs transport paperwork. |
| `c18` | selected, required | 1.900 | 29 | Transport paperwork is completed by the mobility coordinator. |
| `c28` | selected | 0.283 | 31 | Silver consent telehealth follow-up slots open through in-person surgery clearance. |
| `c25` | selected | 1.343 | 28 | The silver consent sleeve indicates telehealth follow-up. |
| `c26` | selected | 0.700 | 30 | Telehealth follow-up slots are opened by the remote-care scheduler. |
| `c19` | selected, required | 0.400 | 31 | The mobility coordinator sits beside the west stairwell during afternoon rounds. |
| `c37` | - | -0.300 | 28 | The pearl sticker means language assistance is requested. |
| `c29` | - | -0.371 | 27 | A lavender tray tag means samples go to microbiology. |
| `c33` | - | -0.371 | 28 | The bronze sticker on a chart means insurance review is pending. |

### PASS content_02_clinic_access / c_q05_direct / budget 1024

Question: Where is the person who completes transport paperwork located?

Selected: `['c17', 'c18', 'c19', 'c20', 'c25', 'c26', 'c28']`
Tokens: `209/1024`
F1: `0.727` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `[]`

Score breakdown:

- individual: `11.276`
- pair synergy: `4.945`
- triple synergy: `0.000`
- redundancy penalty: `1.999`
- total: `14.222`

Improvement hint: Successful selection; inspect extra chunks only if precision or token cost becomes the priority.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `c20` | selected, optional | 4.450 | 31 | The person located at billing completes transport paperwork for red discharge packets. |
| `c17` | selected, required | 2.200 | 29 | The red discharge packet means the patient needs transport paperwork. |
| `c18` | selected, required | 1.900 | 29 | Transport paperwork is completed by the mobility coordinator. |
| `c28` | selected | 0.283 | 31 | Silver consent telehealth follow-up slots open through in-person surgery clearance. |
| `c25` | selected | 1.343 | 28 | The silver consent sleeve indicates telehealth follow-up. |
| `c26` | selected | 0.700 | 30 | Telehealth follow-up slots are opened by the remote-care scheduler. |
| `c19` | selected, required | 0.400 | 31 | The mobility coordinator sits beside the west stairwell during afternoon rounds. |
| `c37` | - | -0.300 | 28 | The pearl sticker means language assistance is requested. |
| `c29` | - | -0.371 | 27 | A lavender tray tag means samples go to microbiology. |
| `c33` | - | -0.371 | 28 | The bronze sticker on a chart means insurance review is pending. |

### PASS content_02_clinic_access / c_q06_two_hop / budget 128

Question: Which map label points to the place for expired wristband replacement?

Selected: `['c21', 'c22', 'c23', 'c24']`
Tokens: `116/128`
F1: `0.857` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `['c24']`

Score breakdown:

- individual: `6.007`
- pair synergy: `2.041`
- triple synergy: `0.000`
- redundancy penalty: `0.659`
- total: `7.390`

Improvement hint: Add wrong-context or contradiction-aware features; a distractor beat required evidence.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `c24` | selected, distractor | 3.271 | 30 | Expired wristband replacement points to the security map label after a badge denial. |
| `c21` | selected, required | 0.979 | 27 | Expired wristbands are replaced at the intake island. |
| `c22` | selected, required | 0.979 | 29 | The intake island is labeled Coral on the floor map. |
| `c23` | selected, optional | 0.779 | 30 | Coral map labels are maintained by facilities, not by the access team. |
| `c04` | - | -0.133 | 31 | A badge denial for visiting students should be fixed at reception by the visitor badge desk. |
| `c01` | - | -0.425 | 27 | Blue-lanyard observers receive a temporary pass from the learning office, not from reception. |
| `c05` | - | -0.425 | 27 | The sedation cabinet releases keys after the orange ledger is initialed. |
| `c27` | - | -0.425 | 29 | Remote-care scheduling uses the amber queue after noon. |
| `c30` | - | -0.467 | 29 | Microbiology batches after-hours samples under code M-14. |
| `c11` | - | -0.467 | 30 | Behavioral-health overflow is coordinated by Lina Park after 18:00. |

### PASS content_02_clinic_access / c_q06_two_hop / budget 256

Question: Which map label points to the place for expired wristband replacement?

Selected: `['c04', 'c21', 'c22', 'c23', 'c24']`
Tokens: `147/256`
F1: `0.750` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `['c24']`

Score breakdown:

- individual: `5.874`
- pair synergy: `2.308`
- triple synergy: `0.000`
- redundancy penalty: `0.791`
- total: `7.391`

Improvement hint: Add wrong-context or contradiction-aware features; a distractor beat required evidence.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `c24` | selected, distractor | 3.271 | 30 | Expired wristband replacement points to the security map label after a badge denial. |
| `c21` | selected, required | 0.979 | 27 | Expired wristbands are replaced at the intake island. |
| `c22` | selected, required | 0.979 | 29 | The intake island is labeled Coral on the floor map. |
| `c23` | selected, optional | 0.779 | 30 | Coral map labels are maintained by facilities, not by the access team. |
| `c04` | selected | -0.133 | 31 | A badge denial for visiting students should be fixed at reception by the visitor badge desk. |
| `c01` | - | -0.425 | 27 | Blue-lanyard observers receive a temporary pass from the learning office, not from reception. |
| `c05` | - | -0.425 | 27 | The sedation cabinet releases keys after the orange ledger is initialed. |
| `c27` | - | -0.425 | 29 | Remote-care scheduling uses the amber queue after noon. |
| `c30` | - | -0.467 | 29 | Microbiology batches after-hours samples under code M-14. |
| `c11` | - | -0.467 | 30 | Behavioral-health overflow is coordinated by Lina Park after 18:00. |

### PASS content_02_clinic_access / c_q06_two_hop / budget 512

Question: Which map label points to the place for expired wristband replacement?

Selected: `['c04', 'c21', 'c22', 'c23', 'c24']`
Tokens: `147/512`
F1: `0.750` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `['c24']`

Score breakdown:

- individual: `5.874`
- pair synergy: `2.308`
- triple synergy: `0.000`
- redundancy penalty: `0.791`
- total: `7.391`

Improvement hint: Add wrong-context or contradiction-aware features; a distractor beat required evidence.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `c24` | selected, distractor | 3.271 | 30 | Expired wristband replacement points to the security map label after a badge denial. |
| `c21` | selected, required | 0.979 | 27 | Expired wristbands are replaced at the intake island. |
| `c22` | selected, required | 0.979 | 29 | The intake island is labeled Coral on the floor map. |
| `c23` | selected, optional | 0.779 | 30 | Coral map labels are maintained by facilities, not by the access team. |
| `c04` | selected | -0.133 | 31 | A badge denial for visiting students should be fixed at reception by the visitor badge desk. |
| `c01` | - | -0.425 | 27 | Blue-lanyard observers receive a temporary pass from the learning office, not from reception. |
| `c05` | - | -0.425 | 27 | The sedation cabinet releases keys after the orange ledger is initialed. |
| `c27` | - | -0.425 | 29 | Remote-care scheduling uses the amber queue after noon. |
| `c30` | - | -0.467 | 29 | Microbiology batches after-hours samples under code M-14. |
| `c11` | - | -0.467 | 30 | Behavioral-health overflow is coordinated by Lina Park after 18:00. |

### PASS content_02_clinic_access / c_q06_two_hop / budget 1024

Question: Which map label points to the place for expired wristband replacement?

Selected: `['c04', 'c21', 'c22', 'c23', 'c24']`
Tokens: `147/1024`
F1: `0.750` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `['c24']`

Score breakdown:

- individual: `5.874`
- pair synergy: `2.308`
- triple synergy: `0.000`
- redundancy penalty: `0.791`
- total: `7.391`

Improvement hint: Add wrong-context or contradiction-aware features; a distractor beat required evidence.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `c24` | selected, distractor | 3.271 | 30 | Expired wristband replacement points to the security map label after a badge denial. |
| `c21` | selected, required | 0.979 | 27 | Expired wristbands are replaced at the intake island. |
| `c22` | selected, required | 0.979 | 29 | The intake island is labeled Coral on the floor map. |
| `c23` | selected, optional | 0.779 | 30 | Coral map labels are maintained by facilities, not by the access team. |
| `c04` | selected | -0.133 | 31 | A badge denial for visiting students should be fixed at reception by the visitor badge desk. |
| `c01` | - | -0.425 | 27 | Blue-lanyard observers receive a temporary pass from the learning office, not from reception. |
| `c05` | - | -0.425 | 27 | The sedation cabinet releases keys after the orange ledger is initialed. |
| `c27` | - | -0.425 | 29 | Remote-care scheduling uses the amber queue after noon. |
| `c30` | - | -0.467 | 29 | Microbiology batches after-hours samples under code M-14. |
| `c11` | - | -0.467 | 30 | Behavioral-health overflow is coordinated by Lina Park after 18:00. |

### PASS content_02_clinic_access / c_q07_two_hop / budget 128

Question: Which queue opens slots for silver consent telehealth follow-up?

Selected: `['c25', 'c26', 'c27', 'c28']`
Tokens: `118/128`
F1: `1.000` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `[]`

Score breakdown:

- individual: `11.736`
- pair synergy: `3.271`
- triple synergy: `0.156`
- redundancy penalty: `1.175`
- total: `13.989`

Improvement hint: Successful selection; inspect extra chunks only if precision or token cost becomes the priority.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `c28` | selected, optional | 4.493 | 31 | Silver consent telehealth follow-up slots open through in-person surgery clearance. |
| `c25` | selected, required | 3.968 | 28 | The silver consent sleeve indicates telehealth follow-up. |
| `c26` | selected, required | 2.800 | 30 | Telehealth follow-up slots are opened by the remote-care scheduler. |
| `c27` | selected, required | 0.475 | 29 | Remote-care scheduling uses the amber queue after noon. |
| `c09` | - | 0.057 | 28 | The quiet room uses a dove marker on the scheduling board. |
| `c05` | - | -0.425 | 27 | The sedation cabinet releases keys after the orange ledger is initialed. |
| `c30` | - | -0.425 | 29 | Microbiology batches after-hours samples under code M-14. |
| `c11` | - | -0.425 | 30 | Behavioral-health overflow is coordinated by Lina Park after 18:00. |
| `c24` | - | -0.425 | 30 | Expired wristband replacement points to the security map label after a badge denial. |
| `c12` | - | -0.425 | 31 | The quiet room after evening overflow is handled by the triage nurse for pediatric fever cases. |

### PASS content_02_clinic_access / c_q07_two_hop / budget 256

Question: Which queue opens slots for silver consent telehealth follow-up?

Selected: `['c09', 'c25', 'c26', 'c27', 'c28']`
Tokens: `146/256`
F1: `0.889` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `[]`

Score breakdown:

- individual: `11.793`
- pair synergy: `3.614`
- triple synergy: `0.156`
- redundancy penalty: `1.348`
- total: `14.216`

Improvement hint: Successful selection; inspect extra chunks only if precision or token cost becomes the priority.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `c28` | selected, optional | 4.493 | 31 | Silver consent telehealth follow-up slots open through in-person surgery clearance. |
| `c25` | selected, required | 3.968 | 28 | The silver consent sleeve indicates telehealth follow-up. |
| `c26` | selected, required | 2.800 | 30 | Telehealth follow-up slots are opened by the remote-care scheduler. |
| `c27` | selected, required | 0.475 | 29 | Remote-care scheduling uses the amber queue after noon. |
| `c09` | selected | 0.057 | 28 | The quiet room uses a dove marker on the scheduling board. |
| `c05` | - | -0.425 | 27 | The sedation cabinet releases keys after the orange ledger is initialed. |
| `c30` | - | -0.425 | 29 | Microbiology batches after-hours samples under code M-14. |
| `c11` | - | -0.425 | 30 | Behavioral-health overflow is coordinated by Lina Park after 18:00. |
| `c24` | - | -0.425 | 30 | Expired wristband replacement points to the security map label after a badge denial. |
| `c12` | - | -0.425 | 31 | The quiet room after evening overflow is handled by the triage nurse for pediatric fever cases. |

### PASS content_02_clinic_access / c_q07_two_hop / budget 512

Question: Which queue opens slots for silver consent telehealth follow-up?

Selected: `['c09', 'c25', 'c26', 'c27', 'c28']`
Tokens: `146/512`
F1: `0.889` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `[]`

Score breakdown:

- individual: `11.793`
- pair synergy: `3.614`
- triple synergy: `0.156`
- redundancy penalty: `1.348`
- total: `14.216`

Improvement hint: Successful selection; inspect extra chunks only if precision or token cost becomes the priority.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `c28` | selected, optional | 4.493 | 31 | Silver consent telehealth follow-up slots open through in-person surgery clearance. |
| `c25` | selected, required | 3.968 | 28 | The silver consent sleeve indicates telehealth follow-up. |
| `c26` | selected, required | 2.800 | 30 | Telehealth follow-up slots are opened by the remote-care scheduler. |
| `c27` | selected, required | 0.475 | 29 | Remote-care scheduling uses the amber queue after noon. |
| `c09` | selected | 0.057 | 28 | The quiet room uses a dove marker on the scheduling board. |
| `c05` | - | -0.425 | 27 | The sedation cabinet releases keys after the orange ledger is initialed. |
| `c30` | - | -0.425 | 29 | Microbiology batches after-hours samples under code M-14. |
| `c11` | - | -0.425 | 30 | Behavioral-health overflow is coordinated by Lina Park after 18:00. |
| `c24` | - | -0.425 | 30 | Expired wristband replacement points to the security map label after a badge denial. |
| `c12` | - | -0.425 | 31 | The quiet room after evening overflow is handled by the triage nurse for pediatric fever cases. |

### PASS content_02_clinic_access / c_q07_two_hop / budget 1024

Question: Which queue opens slots for silver consent telehealth follow-up?

Selected: `['c09', 'c25', 'c26', 'c27', 'c28']`
Tokens: `146/1024`
F1: `0.889` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `[]`

Score breakdown:

- individual: `11.793`
- pair synergy: `3.614`
- triple synergy: `0.156`
- redundancy penalty: `1.348`
- total: `14.216`

Improvement hint: Successful selection; inspect extra chunks only if precision or token cost becomes the priority.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `c28` | selected, optional | 4.493 | 31 | Silver consent telehealth follow-up slots open through in-person surgery clearance. |
| `c25` | selected, required | 3.968 | 28 | The silver consent sleeve indicates telehealth follow-up. |
| `c26` | selected, required | 2.800 | 30 | Telehealth follow-up slots are opened by the remote-care scheduler. |
| `c27` | selected, required | 0.475 | 29 | Remote-care scheduling uses the amber queue after noon. |
| `c09` | selected | 0.057 | 28 | The quiet room uses a dove marker on the scheduling board. |
| `c05` | - | -0.425 | 27 | The sedation cabinet releases keys after the orange ledger is initialed. |
| `c30` | - | -0.425 | 29 | Microbiology batches after-hours samples under code M-14. |
| `c11` | - | -0.425 | 30 | Behavioral-health overflow is coordinated by Lina Park after 18:00. |
| `c24` | - | -0.425 | 30 | Expired wristband replacement points to the security map label after a badge denial. |
| `c12` | - | -0.425 | 31 | The quiet room after evening overflow is handled by the triage nurse for pediatric fever cases. |

### FAIL content_02_clinic_access / c_q08_two_hop / budget 128

Question: Who collects after-hours samples from lavender tray tags?

Selected: `['c29', 'c30', 'c32', 'c35']`
Tokens: `116/128`
F1: `0.706` Required recall: `0.667`
Missing required units: `['collector']`
Selected distractors: `[]`

Score breakdown:

- individual: `7.611`
- pair synergy: `2.912`
- triple synergy: `0.312`
- redundancy penalty: `0.602`
- total: `10.233`

Improvement hint: Tight-budget tradeoff; improve importance ranking so required evidence beats optional/filler chunks.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `c32` | selected, optional | 3.014 | 30 | Lavender tray tags mean samples go to radiology during downtime. |
| `c29` | selected, required | 2.489 | 27 | A lavender tray tag means samples go to microbiology. |
| `c30` | selected, required | 1.632 | 29 | Microbiology batches after-hours samples under code M-14. |
| `c01` | - | -0.275 | 27 | Blue-lanyard observers receive a temporary pass from the learning office, not from reception. |
| `c31` | required | 0.533 | 30 | Code M-14 batches are collected by night runner Sima Chen. |
| `c35` | selected | 0.475 | 30 | Mateo Ruiz works from the small office behind registration. |
| `c05` | - | 0.100 | 27 | The sedation cabinet releases keys after the orange ledger is initialed. |
| `c27` | - | 0.100 | 29 | Remote-care scheduling uses the amber queue after noon. |
| `c11` | - | 0.058 | 30 | Behavioral-health overflow is coordinated by Lina Park after 18:00. |
| `c24` | - | 0.058 | 30 | Expired wristband replacement points to the security map label after a badge denial. |

### FAIL content_02_clinic_access / c_q08_two_hop / budget 256

Question: Who collects after-hours samples from lavender tray tags?

Selected: `['c01', 'c05', 'c24', 'c27', 'c29', 'c30', 'c32', 'c35']`
Tokens: `229/256`
F1: `0.480` Required recall: `0.667`
Missing required units: `['collector']`
Selected distractors: `[]`

Score breakdown:

- individual: `7.594`
- pair synergy: `7.845`
- triple synergy: `2.500`
- redundancy penalty: `1.145`
- total: `16.795`

Improvement hint: Scoring issue; required evidence was available but not valuable enough under current utility.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `c32` | selected, optional | 3.014 | 30 | Lavender tray tags mean samples go to radiology during downtime. |
| `c29` | selected, required | 2.489 | 27 | A lavender tray tag means samples go to microbiology. |
| `c30` | selected, required | 1.632 | 29 | Microbiology batches after-hours samples under code M-14. |
| `c01` | selected | -0.275 | 27 | Blue-lanyard observers receive a temporary pass from the learning office, not from reception. |
| `c31` | required | 0.533 | 30 | Code M-14 batches are collected by night runner Sima Chen. |
| `c35` | selected | 0.475 | 30 | Mateo Ruiz works from the small office behind registration. |
| `c05` | selected | 0.100 | 27 | The sedation cabinet releases keys after the orange ledger is initialed. |
| `c27` | selected | 0.100 | 29 | Remote-care scheduling uses the amber queue after noon. |
| `c11` | - | 0.058 | 30 | Behavioral-health overflow is coordinated by Lina Park after 18:00. |
| `c24` | selected | 0.058 | 30 | Expired wristband replacement points to the security map label after a badge denial. |

### PASS content_02_clinic_access / c_q08_two_hop / budget 512

Question: Who collects after-hours samples from lavender tray tags?

Selected: `['c01', 'c05', 'c11', 'c24', 'c27', 'c29', 'c30', 'c31', 'c32', 'c35']`
Tokens: `289/512`
F1: `0.571` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `[]`

Score breakdown:

- individual: `8.186`
- pair synergy: `9.945`
- triple synergy: `3.125`
- redundancy penalty: `1.735`
- total: `19.521`

Improvement hint: Successful selection; inspect extra chunks only if precision or token cost becomes the priority.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `c32` | selected, optional | 3.014 | 30 | Lavender tray tags mean samples go to radiology during downtime. |
| `c29` | selected, required | 2.489 | 27 | A lavender tray tag means samples go to microbiology. |
| `c30` | selected, required | 1.632 | 29 | Microbiology batches after-hours samples under code M-14. |
| `c01` | selected | -0.275 | 27 | Blue-lanyard observers receive a temporary pass from the learning office, not from reception. |
| `c31` | selected, required | 0.533 | 30 | Code M-14 batches are collected by night runner Sima Chen. |
| `c35` | selected | 0.475 | 30 | Mateo Ruiz works from the small office behind registration. |
| `c05` | selected | 0.100 | 27 | The sedation cabinet releases keys after the orange ledger is initialed. |
| `c27` | selected | 0.100 | 29 | Remote-care scheduling uses the amber queue after noon. |
| `c11` | selected | 0.058 | 30 | Behavioral-health overflow is coordinated by Lina Park after 18:00. |
| `c24` | selected | 0.058 | 30 | Expired wristband replacement points to the security map label after a badge denial. |

### PASS content_02_clinic_access / c_q08_two_hop / budget 1024

Question: Who collects after-hours samples from lavender tray tags?

Selected: `['c01', 'c05', 'c11', 'c24', 'c27', 'c29', 'c30', 'c31', 'c32', 'c35']`
Tokens: `289/1024`
F1: `0.571` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `[]`

Score breakdown:

- individual: `8.186`
- pair synergy: `9.945`
- triple synergy: `3.125`
- redundancy penalty: `1.735`
- total: `19.521`

Improvement hint: Successful selection; inspect extra chunks only if precision or token cost becomes the priority.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `c32` | selected, optional | 3.014 | 30 | Lavender tray tags mean samples go to radiology during downtime. |
| `c29` | selected, required | 2.489 | 27 | A lavender tray tag means samples go to microbiology. |
| `c30` | selected, required | 1.632 | 29 | Microbiology batches after-hours samples under code M-14. |
| `c01` | selected | -0.275 | 27 | Blue-lanyard observers receive a temporary pass from the learning office, not from reception. |
| `c31` | selected, required | 0.533 | 30 | Code M-14 batches are collected by night runner Sima Chen. |
| `c35` | selected | 0.475 | 30 | Mateo Ruiz works from the small office behind registration. |
| `c05` | selected | 0.100 | 27 | The sedation cabinet releases keys after the orange ledger is initialed. |
| `c27` | selected | 0.100 | 29 | Remote-care scheduling uses the amber queue after noon. |
| `c11` | selected | 0.058 | 30 | Behavioral-health overflow is coordinated by Lina Park after 18:00. |
| `c24` | selected | 0.058 | 30 | Expired wristband replacement points to the security map label after a badge denial. |

### FAIL content_02_clinic_access / c_q09_two_hop / budget 128

Question: Where does the bronze chart insurance reviewer work?

Selected: `['c33', 'c34', 'c36', 'c37']`
Tokens: `116/128`
F1: `0.706` Required recall: `0.667`
Missing required units: `['reviewer_location']`
Selected distractors: `[]`

Score breakdown:

- individual: `6.636`
- pair synergy: `1.579`
- triple synergy: `0.000`
- redundancy penalty: `0.823`
- total: `7.391`

Improvement hint: Tight-budget tradeoff; improve importance ranking so required evidence beats optional/filler chunks.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `c33` | selected, required | 2.864 | 28 | The bronze sticker on a chart means insurance review is pending. |
| `c36` | selected, optional | 2.864 | 31 | Bronze chart stickers are cleared by the triage physician before insurance review. |
| `c34` | selected, required | 0.707 | 29 | Pending insurance reviews are handled by claims liaison Mateo Ruiz. |
| `c01` | - | -0.800 | 27 | Blue-lanyard observers receive a temporary pass from the learning office, not from reception. |
| `c37` | selected | 0.200 | 28 | The pearl sticker means language assistance is requested. |
| `c02` | - | -0.050 | 29 | The learning office is called the North Annex counter in weekend notes. |
| `c35` | required | -0.050 | 30 | Mateo Ruiz works from the small office behind registration. |
| `c29` | - | -0.371 | 27 | A lavender tray tag means samples go to microbiology. |
| `c17` | - | -0.371 | 29 | The red discharge packet means the patient needs transport paperwork. |
| `c40` | - | -0.371 | 31 | Pearl sticker language help roster requests go to financial counseling at registration. |

### PASS content_02_clinic_access / c_q09_two_hop / budget 256

Question: Where does the bronze chart insurance reviewer work?

Selected: `['c02', 'c33', 'c34', 'c35', 'c36', 'c37', 'c40']`
Tokens: `206/256`
F1: `0.727` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `[]`

Score breakdown:

- individual: `6.164`
- pair synergy: `2.950`
- triple synergy: `0.000`
- redundancy penalty: `1.455`
- total: `7.660`

Improvement hint: Successful selection; inspect extra chunks only if precision or token cost becomes the priority.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `c33` | selected, required | 2.864 | 28 | The bronze sticker on a chart means insurance review is pending. |
| `c36` | selected, optional | 2.864 | 31 | Bronze chart stickers are cleared by the triage physician before insurance review. |
| `c34` | selected, required | 0.707 | 29 | Pending insurance reviews are handled by claims liaison Mateo Ruiz. |
| `c01` | - | -0.800 | 27 | Blue-lanyard observers receive a temporary pass from the learning office, not from reception. |
| `c37` | selected | 0.200 | 28 | The pearl sticker means language assistance is requested. |
| `c02` | selected | -0.050 | 29 | The learning office is called the North Annex counter in weekend notes. |
| `c35` | selected, required | -0.050 | 30 | Mateo Ruiz works from the small office behind registration. |
| `c29` | - | -0.371 | 27 | A lavender tray tag means samples go to microbiology. |
| `c17` | - | -0.371 | 29 | The red discharge packet means the patient needs transport paperwork. |
| `c40` | selected | -0.371 | 31 | Pearl sticker language help roster requests go to financial counseling at registration. |

### PASS content_02_clinic_access / c_q09_two_hop / budget 512

Question: Where does the bronze chart insurance reviewer work?

Selected: `['c02', 'c33', 'c34', 'c35', 'c36', 'c37', 'c40']`
Tokens: `206/512`
F1: `0.727` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `[]`

Score breakdown:

- individual: `6.164`
- pair synergy: `2.950`
- triple synergy: `0.000`
- redundancy penalty: `1.455`
- total: `7.660`

Improvement hint: Successful selection; inspect extra chunks only if precision or token cost becomes the priority.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `c33` | selected, required | 2.864 | 28 | The bronze sticker on a chart means insurance review is pending. |
| `c36` | selected, optional | 2.864 | 31 | Bronze chart stickers are cleared by the triage physician before insurance review. |
| `c34` | selected, required | 0.707 | 29 | Pending insurance reviews are handled by claims liaison Mateo Ruiz. |
| `c01` | - | -0.800 | 27 | Blue-lanyard observers receive a temporary pass from the learning office, not from reception. |
| `c37` | selected | 0.200 | 28 | The pearl sticker means language assistance is requested. |
| `c02` | selected | -0.050 | 29 | The learning office is called the North Annex counter in weekend notes. |
| `c35` | selected, required | -0.050 | 30 | Mateo Ruiz works from the small office behind registration. |
| `c29` | - | -0.371 | 27 | A lavender tray tag means samples go to microbiology. |
| `c17` | - | -0.371 | 29 | The red discharge packet means the patient needs transport paperwork. |
| `c40` | selected | -0.371 | 31 | Pearl sticker language help roster requests go to financial counseling at registration. |

### PASS content_02_clinic_access / c_q09_two_hop / budget 1024

Question: Where does the bronze chart insurance reviewer work?

Selected: `['c02', 'c33', 'c34', 'c35', 'c36', 'c37', 'c40']`
Tokens: `206/1024`
F1: `0.727` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `[]`

Score breakdown:

- individual: `6.164`
- pair synergy: `2.950`
- triple synergy: `0.000`
- redundancy penalty: `1.455`
- total: `7.660`

Improvement hint: Successful selection; inspect extra chunks only if precision or token cost becomes the priority.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `c33` | selected, required | 2.864 | 28 | The bronze sticker on a chart means insurance review is pending. |
| `c36` | selected, optional | 2.864 | 31 | Bronze chart stickers are cleared by the triage physician before insurance review. |
| `c34` | selected, required | 0.707 | 29 | Pending insurance reviews are handled by claims liaison Mateo Ruiz. |
| `c01` | - | -0.800 | 27 | Blue-lanyard observers receive a temporary pass from the learning office, not from reception. |
| `c37` | selected | 0.200 | 28 | The pearl sticker means language assistance is requested. |
| `c02` | selected | -0.050 | 29 | The learning office is called the North Annex counter in weekend notes. |
| `c35` | selected, required | -0.050 | 30 | Mateo Ruiz works from the small office behind registration. |
| `c29` | - | -0.371 | 27 | A lavender tray tag means samples go to microbiology. |
| `c17` | - | -0.371 | 29 | The red discharge packet means the patient needs transport paperwork. |
| `c40` | selected | -0.371 | 31 | Pearl sticker language help roster requests go to financial counseling at registration. |

### FAIL content_02_clinic_access / c_q10_two_hop / budget 128

Question: Which roster supports pearl sticker language help?

Selected: `['c33', 'c37', 'c38', 'c40']`
Tokens: `117/128`
F1: `0.706` Required recall: `0.667`
Missing required units: `['roster']`
Selected distractors: `[]`

Score breakdown:

- individual: `8.300`
- pair synergy: `2.105`
- triple synergy: `0.000`
- redundancy penalty: `0.834`
- total: `9.570`

Improvement hint: Tight-budget tradeoff; improve importance ranking so required evidence beats optional/filler chunks.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `c40` | selected, optional | 3.950 | 31 | Pearl sticker language help roster requests go to financial counseling at registration. |
| `c37` | selected, required | 2.650 | 28 | The pearl sticker means language assistance is requested. |
| `c33` | selected | 0.850 | 28 | The bronze sticker on a chart means insurance review is pending. |
| `c39` | required | 0.279 | 29 | Cultural services keeps evening interpreters on the violet roster. |
| `c36` | - | 0.914 | 31 | Bronze chart stickers are cleared by the triage physician before insurance review. |
| `c38` | selected, required | 0.850 | 30 | Language assistance is booked by the cultural services desk. |
| `c34` | - | 0.057 | 29 | Pending insurance reviews are handled by claims liaison Mateo Ruiz. |
| `c29` | - | -0.300 | 27 | A lavender tray tag means samples go to microbiology. |
| `c17` | - | -0.300 | 29 | The red discharge packet means the patient needs transport paperwork. |
| `c07` | - | -0.371 | 29 | Pharmacy keeps a separate green narcotics book for medication counts. |

### PASS content_02_clinic_access / c_q10_two_hop / budget 256

Question: Which roster supports pearl sticker language help?

Selected: `['c33', 'c34', 'c36', 'c37', 'c38', 'c39', 'c40']`
Tokens: `206/256`
F1: `0.727` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `[]`

Score breakdown:

- individual: `9.550`
- pair synergy: `4.855`
- triple synergy: `0.208`
- redundancy penalty: `1.728`
- total: `12.885`

Improvement hint: Successful selection; inspect extra chunks only if precision or token cost becomes the priority.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `c40` | selected, optional | 3.950 | 31 | Pearl sticker language help roster requests go to financial counseling at registration. |
| `c37` | selected, required | 2.650 | 28 | The pearl sticker means language assistance is requested. |
| `c33` | selected | 0.850 | 28 | The bronze sticker on a chart means insurance review is pending. |
| `c39` | selected, required | 0.279 | 29 | Cultural services keeps evening interpreters on the violet roster. |
| `c36` | selected | 0.914 | 31 | Bronze chart stickers are cleared by the triage physician before insurance review. |
| `c38` | selected, required | 0.850 | 30 | Language assistance is booked by the cultural services desk. |
| `c34` | selected | 0.057 | 29 | Pending insurance reviews are handled by claims liaison Mateo Ruiz. |
| `c29` | - | -0.300 | 27 | A lavender tray tag means samples go to microbiology. |
| `c17` | - | -0.300 | 29 | The red discharge packet means the patient needs transport paperwork. |
| `c07` | - | -0.371 | 29 | Pharmacy keeps a separate green narcotics book for medication counts. |

### PASS content_02_clinic_access / c_q10_two_hop / budget 512

Question: Which roster supports pearl sticker language help?

Selected: `['c33', 'c34', 'c36', 'c37', 'c38', 'c39', 'c40']`
Tokens: `206/512`
F1: `0.727` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `[]`

Score breakdown:

- individual: `9.550`
- pair synergy: `4.855`
- triple synergy: `0.208`
- redundancy penalty: `1.728`
- total: `12.885`

Improvement hint: Successful selection; inspect extra chunks only if precision or token cost becomes the priority.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `c40` | selected, optional | 3.950 | 31 | Pearl sticker language help roster requests go to financial counseling at registration. |
| `c37` | selected, required | 2.650 | 28 | The pearl sticker means language assistance is requested. |
| `c33` | selected | 0.850 | 28 | The bronze sticker on a chart means insurance review is pending. |
| `c39` | selected, required | 0.279 | 29 | Cultural services keeps evening interpreters on the violet roster. |
| `c36` | selected | 0.914 | 31 | Bronze chart stickers are cleared by the triage physician before insurance review. |
| `c38` | selected, required | 0.850 | 30 | Language assistance is booked by the cultural services desk. |
| `c34` | selected | 0.057 | 29 | Pending insurance reviews are handled by claims liaison Mateo Ruiz. |
| `c29` | - | -0.300 | 27 | A lavender tray tag means samples go to microbiology. |
| `c17` | - | -0.300 | 29 | The red discharge packet means the patient needs transport paperwork. |
| `c07` | - | -0.371 | 29 | Pharmacy keeps a separate green narcotics book for medication counts. |

### PASS content_02_clinic_access / c_q10_two_hop / budget 1024

Question: Which roster supports pearl sticker language help?

Selected: `['c33', 'c34', 'c36', 'c37', 'c38', 'c39', 'c40']`
Tokens: `206/1024`
F1: `0.727` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `[]`

Score breakdown:

- individual: `9.550`
- pair synergy: `4.855`
- triple synergy: `0.208`
- redundancy penalty: `1.728`
- total: `12.885`

Improvement hint: Successful selection; inspect extra chunks only if precision or token cost becomes the priority.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `c40` | selected, optional | 3.950 | 31 | Pearl sticker language help roster requests go to financial counseling at registration. |
| `c37` | selected, required | 2.650 | 28 | The pearl sticker means language assistance is requested. |
| `c33` | selected | 0.850 | 28 | The bronze sticker on a chart means insurance review is pending. |
| `c39` | selected, required | 0.279 | 29 | Cultural services keeps evening interpreters on the violet roster. |
| `c36` | selected | 0.914 | 31 | Bronze chart stickers are cleared by the triage physician before insurance review. |
| `c38` | selected, required | 0.850 | 30 | Language assistance is booked by the cultural services desk. |
| `c34` | selected | 0.057 | 29 | Pending insurance reviews are handled by claims liaison Mateo Ruiz. |
| `c29` | - | -0.300 | 27 | A lavender tray tag means samples go to microbiology. |
| `c17` | - | -0.300 | 29 | The red discharge packet means the patient needs transport paperwork. |
| `c07` | - | -0.371 | 29 | Pharmacy keeps a separate green narcotics book for medication counts. |

### PASS content_02_clinic_access / c_q11_three_hop / budget 128

Question: Who coordinates the quiet room when the dove marker appears after 18:00?

Selected: `['c09', 'c10', 'c11', 'c12']`
Tokens: `118/128`
F1: `1.000` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `[]`

Score breakdown:

- individual: `5.783`
- pair synergy: `3.244`
- triple synergy: `0.139`
- redundancy penalty: `0.678`
- total: `8.489`

Improvement hint: Successful selection; inspect extra chunks only if precision or token cost becomes the priority.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `c09` | selected, required | 1.990 | 28 | The quiet room uses a dove marker on the scheduling board. |
| `c11` | selected, required | 1.317 | 30 | Behavioral-health overflow is coordinated by Lina Park after 18:00. |
| `c12` | selected, optional | 1.507 | 31 | The quiet room after evening overflow is handled by the triage nurse for pediatric fever cases. |
| `c05` | - | 0.058 | 27 | The sedation cabinet releases keys after the orange ledger is initialed. |
| `c08` | - | 1.075 | 30 | Sedation cabinet keys are approved by pharmacy when the orange ledger is missing. |
| `c10` | selected, required | 0.969 | 29 | Dove markers are assigned to behavioral-health overflow patients. |
| `c27` | - | 0.540 | 29 | Remote-care scheduling uses the amber queue after noon. |
| `c30` | - | 0.058 | 29 | Microbiology batches after-hours samples under code M-14. |
| `c24` | - | 0.058 | 30 | Expired wristband replacement points to the security map label after a badge denial. |
| `c06` | - | 0.057 | 28 | Orange ledger initials are supplied by the recovery charge nurse. |

### PASS content_02_clinic_access / c_q11_three_hop / budget 256

Question: Who coordinates the quiet room when the dove marker appears after 18:00?

Selected: `['c05', 'c08', 'c09', 'c10', 'c11', 'c12', 'c24', 'c27']`
Tokens: `234/256`
F1: `0.667` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `[]`

Score breakdown:

- individual: `7.515`
- pair synergy: `6.974`
- triple synergy: `0.139`
- redundancy penalty: `1.954`
- total: `12.674`

Improvement hint: Successful selection; inspect extra chunks only if precision or token cost becomes the priority.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `c09` | selected, required | 1.990 | 28 | The quiet room uses a dove marker on the scheduling board. |
| `c11` | selected, required | 1.317 | 30 | Behavioral-health overflow is coordinated by Lina Park after 18:00. |
| `c12` | selected, optional | 1.507 | 31 | The quiet room after evening overflow is handled by the triage nurse for pediatric fever cases. |
| `c05` | selected | 0.058 | 27 | The sedation cabinet releases keys after the orange ledger is initialed. |
| `c08` | selected | 1.075 | 30 | Sedation cabinet keys are approved by pharmacy when the orange ledger is missing. |
| `c10` | selected, required | 0.969 | 29 | Dove markers are assigned to behavioral-health overflow patients. |
| `c27` | selected | 0.540 | 29 | Remote-care scheduling uses the amber queue after noon. |
| `c30` | - | 0.058 | 29 | Microbiology batches after-hours samples under code M-14. |
| `c24` | selected | 0.058 | 30 | Expired wristband replacement points to the security map label after a badge denial. |
| `c06` | - | 0.057 | 28 | Orange ledger initials are supplied by the recovery charge nurse. |

### PASS content_02_clinic_access / c_q11_three_hop / budget 512

Question: Who coordinates the quiet room when the dove marker appears after 18:00?

Selected: `['c05', 'c06', 'c08', 'c09', 'c10', 'c11', 'c12', 'c24', 'c27', 'c30']`
Tokens: `291/512`
F1: `0.571` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `[]`

Score breakdown:

- individual: `7.631`
- pair synergy: `8.976`
- triple synergy: `0.139`
- redundancy penalty: `2.695`
- total: `14.050`

Improvement hint: Successful selection; inspect extra chunks only if precision or token cost becomes the priority.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `c09` | selected, required | 1.990 | 28 | The quiet room uses a dove marker on the scheduling board. |
| `c11` | selected, required | 1.317 | 30 | Behavioral-health overflow is coordinated by Lina Park after 18:00. |
| `c12` | selected, optional | 1.507 | 31 | The quiet room after evening overflow is handled by the triage nurse for pediatric fever cases. |
| `c05` | selected | 0.058 | 27 | The sedation cabinet releases keys after the orange ledger is initialed. |
| `c08` | selected | 1.075 | 30 | Sedation cabinet keys are approved by pharmacy when the orange ledger is missing. |
| `c10` | selected, required | 0.969 | 29 | Dove markers are assigned to behavioral-health overflow patients. |
| `c27` | selected | 0.540 | 29 | Remote-care scheduling uses the amber queue after noon. |
| `c30` | selected | 0.058 | 29 | Microbiology batches after-hours samples under code M-14. |
| `c24` | selected | 0.058 | 30 | Expired wristband replacement points to the security map label after a badge denial. |
| `c06` | selected | 0.057 | 28 | Orange ledger initials are supplied by the recovery charge nurse. |

### PASS content_02_clinic_access / c_q11_three_hop / budget 1024

Question: Who coordinates the quiet room when the dove marker appears after 18:00?

Selected: `['c05', 'c06', 'c08', 'c09', 'c10', 'c11', 'c12', 'c24', 'c27', 'c30']`
Tokens: `291/1024`
F1: `0.571` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `[]`

Score breakdown:

- individual: `7.631`
- pair synergy: `8.976`
- triple synergy: `0.139`
- redundancy penalty: `2.695`
- total: `14.050`

Improvement hint: Successful selection; inspect extra chunks only if precision or token cost becomes the priority.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `c09` | selected, required | 1.990 | 28 | The quiet room uses a dove marker on the scheduling board. |
| `c11` | selected, required | 1.317 | 30 | Behavioral-health overflow is coordinated by Lina Park after 18:00. |
| `c12` | selected, optional | 1.507 | 31 | The quiet room after evening overflow is handled by the triage nurse for pediatric fever cases. |
| `c05` | selected | 0.058 | 27 | The sedation cabinet releases keys after the orange ledger is initialed. |
| `c08` | selected | 1.075 | 30 | Sedation cabinet keys are approved by pharmacy when the orange ledger is missing. |
| `c10` | selected, required | 0.969 | 29 | Dove markers are assigned to behavioral-health overflow patients. |
| `c27` | selected | 0.540 | 29 | Remote-care scheduling uses the amber queue after noon. |
| `c30` | selected | 0.058 | 29 | Microbiology batches after-hours samples under code M-14. |
| `c24` | selected | 0.058 | 30 | Expired wristband replacement points to the security map label after a badge denial. |
| `c06` | selected | 0.057 | 28 | Orange ledger initials are supplied by the recovery charge nurse. |

### PASS content_02_clinic_access / c_q12_three_hop / budget 128

Question: Who signs before slate courier envelopes reach the night audit path?

Selected: `['c13', 'c14', 'c15', 'c16']`
Tokens: `119/128`
F1: `1.000` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `[]`

Score breakdown:

- individual: `9.662`
- pair synergy: `3.351`
- triple synergy: `0.000`
- redundancy penalty: `1.145`
- total: `11.868`

Improvement hint: Successful selection; inspect extra chunks only if precision or token cost becomes the priority.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `c16` | selected, optional | 3.433 | 31 | Slate courier envelopes before night audit should be signed at the blood desk. |
| `c13` | selected, required | 2.364 | 27 | Courier envelopes marked slate are routed to diagnostic imaging. |
| `c15` | selected, required | 1.983 | 31 | The archive cart is signed out by Omar Singh before the night audit. |
| `c14` | selected, required | 1.881 | 30 | Diagnostic imaging sends slate envelopes to the archive cart near lift B. |
| `c31` | - | 0.017 | 30 | Code M-14 batches are collected by night runner Sima Chen. |
| `c36` | - | 0.017 | 31 | Bronze chart stickers are cleared by the triage physician before insurance review. |
| `c04` | - | -0.133 | 31 | A badge denial for visiting students should be fixed at reception by the visitor badge desk. |
| `c38` | - | -0.300 | 30 | Language assistance is booked by the cultural services desk. |
| `c01` | - | -0.800 | 27 | Blue-lanyard observers receive a temporary pass from the learning office, not from reception. |
| `c05` | - | -0.800 | 27 | The sedation cabinet releases keys after the orange ledger is initialed. |

### PASS content_02_clinic_access / c_q12_three_hop / budget 256

Question: Who signs before slate courier envelopes reach the night audit path?

Selected: `['c04', 'c13', 'c14', 'c15', 'c16', 'c31', 'c36']`
Tokens: `211/256`
F1: `0.727` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `[]`

Score breakdown:

- individual: `9.562`
- pair synergy: `5.262`
- triple synergy: `0.278`
- redundancy penalty: `1.534`
- total: `13.568`

Improvement hint: Successful selection; inspect extra chunks only if precision or token cost becomes the priority.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `c16` | selected, optional | 3.433 | 31 | Slate courier envelopes before night audit should be signed at the blood desk. |
| `c13` | selected, required | 2.364 | 27 | Courier envelopes marked slate are routed to diagnostic imaging. |
| `c15` | selected, required | 1.983 | 31 | The archive cart is signed out by Omar Singh before the night audit. |
| `c14` | selected, required | 1.881 | 30 | Diagnostic imaging sends slate envelopes to the archive cart near lift B. |
| `c31` | selected | 0.017 | 30 | Code M-14 batches are collected by night runner Sima Chen. |
| `c36` | selected | 0.017 | 31 | Bronze chart stickers are cleared by the triage physician before insurance review. |
| `c04` | selected | -0.133 | 31 | A badge denial for visiting students should be fixed at reception by the visitor badge desk. |
| `c38` | - | -0.300 | 30 | Language assistance is booked by the cultural services desk. |
| `c01` | - | -0.800 | 27 | Blue-lanyard observers receive a temporary pass from the learning office, not from reception. |
| `c05` | - | -0.800 | 27 | The sedation cabinet releases keys after the orange ledger is initialed. |

### PASS content_02_clinic_access / c_q12_three_hop / budget 512

Question: Who signs before slate courier envelopes reach the night audit path?

Selected: `['c04', 'c13', 'c14', 'c15', 'c16', 'c31', 'c36']`
Tokens: `211/512`
F1: `0.727` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `[]`

Score breakdown:

- individual: `9.562`
- pair synergy: `5.262`
- triple synergy: `0.278`
- redundancy penalty: `1.534`
- total: `13.568`

Improvement hint: Successful selection; inspect extra chunks only if precision or token cost becomes the priority.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `c16` | selected, optional | 3.433 | 31 | Slate courier envelopes before night audit should be signed at the blood desk. |
| `c13` | selected, required | 2.364 | 27 | Courier envelopes marked slate are routed to diagnostic imaging. |
| `c15` | selected, required | 1.983 | 31 | The archive cart is signed out by Omar Singh before the night audit. |
| `c14` | selected, required | 1.881 | 30 | Diagnostic imaging sends slate envelopes to the archive cart near lift B. |
| `c31` | selected | 0.017 | 30 | Code M-14 batches are collected by night runner Sima Chen. |
| `c36` | selected | 0.017 | 31 | Bronze chart stickers are cleared by the triage physician before insurance review. |
| `c04` | selected | -0.133 | 31 | A badge denial for visiting students should be fixed at reception by the visitor badge desk. |
| `c38` | - | -0.300 | 30 | Language assistance is booked by the cultural services desk. |
| `c01` | - | -0.800 | 27 | Blue-lanyard observers receive a temporary pass from the learning office, not from reception. |
| `c05` | - | -0.800 | 27 | The sedation cabinet releases keys after the orange ledger is initialed. |

### PASS content_02_clinic_access / c_q12_three_hop / budget 1024

Question: Who signs before slate courier envelopes reach the night audit path?

Selected: `['c04', 'c13', 'c14', 'c15', 'c16', 'c31', 'c36']`
Tokens: `211/1024`
F1: `0.727` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `[]`

Score breakdown:

- individual: `9.562`
- pair synergy: `5.262`
- triple synergy: `0.278`
- redundancy penalty: `1.534`
- total: `13.568`

Improvement hint: Successful selection; inspect extra chunks only if precision or token cost becomes the priority.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `c16` | selected, optional | 3.433 | 31 | Slate courier envelopes before night audit should be signed at the blood desk. |
| `c13` | selected, required | 2.364 | 27 | Courier envelopes marked slate are routed to diagnostic imaging. |
| `c15` | selected, required | 1.983 | 31 | The archive cart is signed out by Omar Singh before the night audit. |
| `c14` | selected, required | 1.881 | 30 | Diagnostic imaging sends slate envelopes to the archive cart near lift B. |
| `c31` | selected | 0.017 | 30 | Code M-14 batches are collected by night runner Sima Chen. |
| `c36` | selected | 0.017 | 31 | Bronze chart stickers are cleared by the triage physician before insurance review. |
| `c04` | selected | -0.133 | 31 | A badge denial for visiting students should be fixed at reception by the visitor badge desk. |
| `c38` | - | -0.300 | 30 | Language assistance is booked by the cultural services desk. |
| `c01` | - | -0.800 | 27 | Blue-lanyard observers receive a temporary pass from the learning office, not from reception. |
| `c05` | - | -0.800 | 27 | The sedation cabinet releases keys after the orange ledger is initialed. |

### FAIL content_02_clinic_access / c_q13_three_hop / budget 128

Question: Where is the reviewer for a bronze insurance chart sticker located?

Selected: `['c33', 'c36', 'c37', 'c40']`
Tokens: `118/128`
F1: `0.400` Required recall: `0.333`
Missing required units: `['liaison', 'office']`
Selected distractors: `[]`

Score breakdown:

- individual: `8.579`
- pair synergy: `2.524`
- triple synergy: `0.000`
- redundancy penalty: `0.909`
- total: `10.193`

Improvement hint: Tight-budget tradeoff; improve importance ranking so required evidence beats optional/filler chunks.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `c33` | selected, required | 3.514 | 28 | The bronze sticker on a chart means insurance review is pending. |
| `c36` | selected, optional | 2.864 | 31 | Bronze chart stickers are cleared by the triage physician before insurance review. |
| `c37` | selected | 0.850 | 28 | The pearl sticker means language assistance is requested. |
| `c34` | required | 0.707 | 29 | Pending insurance reviews are handled by claims liaison Mateo Ruiz. |
| `c40` | selected | 1.350 | 31 | Pearl sticker language help roster requests go to financial counseling at registration. |
| `c38` | - | 0.200 | 30 | Language assistance is booked by the cultural services desk. |
| `c35` | required | -0.050 | 30 | Mateo Ruiz works from the small office behind registration. |
| `c20` | - | -0.150 | 31 | The person located at billing completes transport paperwork for red discharge packets. |
| `c29` | - | -0.300 | 27 | A lavender tray tag means samples go to microbiology. |
| `c17` | - | -0.300 | 29 | The red discharge packet means the patient needs transport paperwork. |

### PASS content_02_clinic_access / c_q13_three_hop / budget 256

Question: Where is the reviewer for a bronze insurance chart sticker located?

Selected: `['c20', 'c33', 'c34', 'c35', 'c36', 'c37', 'c38', 'c40']`
Tokens: `238/256`
F1: `0.667` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `[]`

Score breakdown:

- individual: `9.286`
- pair synergy: `6.400`
- triple synergy: `0.833`
- redundancy penalty: `1.680`
- total: `14.839`

Improvement hint: Successful selection; inspect extra chunks only if precision or token cost becomes the priority.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `c33` | selected, required | 3.514 | 28 | The bronze sticker on a chart means insurance review is pending. |
| `c36` | selected, optional | 2.864 | 31 | Bronze chart stickers are cleared by the triage physician before insurance review. |
| `c37` | selected | 0.850 | 28 | The pearl sticker means language assistance is requested. |
| `c34` | selected, required | 0.707 | 29 | Pending insurance reviews are handled by claims liaison Mateo Ruiz. |
| `c40` | selected | 1.350 | 31 | Pearl sticker language help roster requests go to financial counseling at registration. |
| `c38` | selected | 0.200 | 30 | Language assistance is booked by the cultural services desk. |
| `c35` | selected, required | -0.050 | 30 | Mateo Ruiz works from the small office behind registration. |
| `c20` | selected | -0.150 | 31 | The person located at billing completes transport paperwork for red discharge packets. |
| `c29` | - | -0.300 | 27 | A lavender tray tag means samples go to microbiology. |
| `c17` | - | -0.300 | 29 | The red discharge packet means the patient needs transport paperwork. |

### PASS content_02_clinic_access / c_q13_three_hop / budget 512

Question: Where is the reviewer for a bronze insurance chart sticker located?

Selected: `['c17', 'c20', 'c29', 'c33', 'c34', 'c35', 'c36', 'c37', 'c38', 'c40']`
Tokens: `294/512`
F1: `0.571` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `[]`

Score breakdown:

- individual: `8.686`
- pair synergy: `8.086`
- triple synergy: `0.833`
- redundancy penalty: `2.524`
- total: `15.081`

Improvement hint: Successful selection; inspect extra chunks only if precision or token cost becomes the priority.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `c33` | selected, required | 3.514 | 28 | The bronze sticker on a chart means insurance review is pending. |
| `c36` | selected, optional | 2.864 | 31 | Bronze chart stickers are cleared by the triage physician before insurance review. |
| `c37` | selected | 0.850 | 28 | The pearl sticker means language assistance is requested. |
| `c34` | selected, required | 0.707 | 29 | Pending insurance reviews are handled by claims liaison Mateo Ruiz. |
| `c40` | selected | 1.350 | 31 | Pearl sticker language help roster requests go to financial counseling at registration. |
| `c38` | selected | 0.200 | 30 | Language assistance is booked by the cultural services desk. |
| `c35` | selected, required | -0.050 | 30 | Mateo Ruiz works from the small office behind registration. |
| `c20` | selected | -0.150 | 31 | The person located at billing completes transport paperwork for red discharge packets. |
| `c29` | selected | -0.300 | 27 | A lavender tray tag means samples go to microbiology. |
| `c17` | selected | -0.300 | 29 | The red discharge packet means the patient needs transport paperwork. |

### PASS content_02_clinic_access / c_q13_three_hop / budget 1024

Question: Where is the reviewer for a bronze insurance chart sticker located?

Selected: `['c17', 'c20', 'c29', 'c33', 'c34', 'c35', 'c36', 'c37', 'c38', 'c40']`
Tokens: `294/1024`
F1: `0.571` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `[]`

Score breakdown:

- individual: `8.686`
- pair synergy: `8.086`
- triple synergy: `0.833`
- redundancy penalty: `2.524`
- total: `15.081`

Improvement hint: Successful selection; inspect extra chunks only if precision or token cost becomes the priority.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `c33` | selected, required | 3.514 | 28 | The bronze sticker on a chart means insurance review is pending. |
| `c36` | selected, optional | 2.864 | 31 | Bronze chart stickers are cleared by the triage physician before insurance review. |
| `c37` | selected | 0.850 | 28 | The pearl sticker means language assistance is requested. |
| `c34` | selected, required | 0.707 | 29 | Pending insurance reviews are handled by claims liaison Mateo Ruiz. |
| `c40` | selected | 1.350 | 31 | Pearl sticker language help roster requests go to financial counseling at registration. |
| `c38` | selected | 0.200 | 30 | Language assistance is booked by the cultural services desk. |
| `c35` | selected, required | -0.050 | 30 | Mateo Ruiz works from the small office behind registration. |
| `c20` | selected | -0.150 | 31 | The person located at billing completes transport paperwork for red discharge packets. |
| `c29` | selected | -0.300 | 27 | A lavender tray tag means samples go to microbiology. |
| `c17` | selected | -0.300 | 29 | The red discharge packet means the patient needs transport paperwork. |

### PASS content_02_clinic_access / c_q14_three_hop / budget 128

Question: Who opens follow-up slots connected to a silver consent sleeve after noon?

Selected: `['c25', 'c26', 'c27', 'c28']`
Tokens: `118/128`
F1: `1.000` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `[]`

Score breakdown:

- individual: `10.086`
- pair synergy: `3.871`
- triple synergy: `0.250`
- redundancy penalty: `1.175`
- total: `13.032`

Improvement hint: Successful selection; inspect extra chunks only if precision or token cost becomes the priority.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `c25` | selected, required | 3.593 | 28 | The silver consent sleeve indicates telehealth follow-up. |
| `c28` | selected, optional | 3.593 | 31 | Silver consent telehealth follow-up slots open through in-person surgery clearance. |
| `c26` | selected, required | 2.050 | 30 | Telehealth follow-up slots are opened by the remote-care scheduler. |
| `c27` | selected, required | 0.850 | 29 | Remote-care scheduling uses the amber queue after noon. |
| `c09` | - | 0.057 | 28 | The quiet room uses a dove marker on the scheduling board. |
| `c05` | - | 0.025 | 27 | The sedation cabinet releases keys after the orange ledger is initialed. |
| `c30` | - | 0.025 | 29 | Microbiology batches after-hours samples under code M-14. |
| `c11` | - | 0.025 | 30 | Behavioral-health overflow is coordinated by Lina Park after 18:00. |
| `c24` | - | 0.025 | 30 | Expired wristband replacement points to the security map label after a badge denial. |
| `c12` | - | 0.025 | 31 | The quiet room after evening overflow is handled by the triage nurse for pediatric fever cases. |

### PASS content_02_clinic_access / c_q14_three_hop / budget 256

Question: Who opens follow-up slots connected to a silver consent sleeve after noon?

Selected: `['c05', 'c11', 'c12', 'c24', 'c25', 'c26', 'c27', 'c28']`
Tokens: `236/256`
F1: `0.667` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `[]`

Score breakdown:

- individual: `10.186`
- pair synergy: `7.841`
- triple synergy: `1.250`
- redundancy penalty: `1.891`
- total: `17.386`

Improvement hint: Successful selection; inspect extra chunks only if precision or token cost becomes the priority.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `c25` | selected, required | 3.593 | 28 | The silver consent sleeve indicates telehealth follow-up. |
| `c28` | selected, optional | 3.593 | 31 | Silver consent telehealth follow-up slots open through in-person surgery clearance. |
| `c26` | selected, required | 2.050 | 30 | Telehealth follow-up slots are opened by the remote-care scheduler. |
| `c27` | selected, required | 0.850 | 29 | Remote-care scheduling uses the amber queue after noon. |
| `c09` | - | 0.057 | 28 | The quiet room uses a dove marker on the scheduling board. |
| `c05` | selected | 0.025 | 27 | The sedation cabinet releases keys after the orange ledger is initialed. |
| `c30` | - | 0.025 | 29 | Microbiology batches after-hours samples under code M-14. |
| `c11` | selected | 0.025 | 30 | Behavioral-health overflow is coordinated by Lina Park after 18:00. |
| `c24` | selected | 0.025 | 30 | Expired wristband replacement points to the security map label after a badge denial. |
| `c12` | selected | 0.025 | 31 | The quiet room after evening overflow is handled by the triage nurse for pediatric fever cases. |

### PASS content_02_clinic_access / c_q14_three_hop / budget 512

Question: Who opens follow-up slots connected to a silver consent sleeve after noon?

Selected: `['c05', 'c09', 'c11', 'c12', 'c24', 'c25', 'c26', 'c27', 'c28', 'c30']`
Tokens: `293/512`
F1: `0.571` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `[]`

Score breakdown:

- individual: `10.268`
- pair synergy: `9.827`
- triple synergy: `1.500`
- redundancy penalty: `2.534`
- total: `19.061`

Improvement hint: Successful selection; inspect extra chunks only if precision or token cost becomes the priority.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `c25` | selected, required | 3.593 | 28 | The silver consent sleeve indicates telehealth follow-up. |
| `c28` | selected, optional | 3.593 | 31 | Silver consent telehealth follow-up slots open through in-person surgery clearance. |
| `c26` | selected, required | 2.050 | 30 | Telehealth follow-up slots are opened by the remote-care scheduler. |
| `c27` | selected, required | 0.850 | 29 | Remote-care scheduling uses the amber queue after noon. |
| `c09` | selected | 0.057 | 28 | The quiet room uses a dove marker on the scheduling board. |
| `c05` | selected | 0.025 | 27 | The sedation cabinet releases keys after the orange ledger is initialed. |
| `c30` | selected | 0.025 | 29 | Microbiology batches after-hours samples under code M-14. |
| `c11` | selected | 0.025 | 30 | Behavioral-health overflow is coordinated by Lina Park after 18:00. |
| `c24` | selected | 0.025 | 30 | Expired wristband replacement points to the security map label after a badge denial. |
| `c12` | selected | 0.025 | 31 | The quiet room after evening overflow is handled by the triage nurse for pediatric fever cases. |

### PASS content_02_clinic_access / c_q14_three_hop / budget 1024

Question: Who opens follow-up slots connected to a silver consent sleeve after noon?

Selected: `['c05', 'c09', 'c11', 'c12', 'c24', 'c25', 'c26', 'c27', 'c28', 'c30']`
Tokens: `293/1024`
F1: `0.571` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `[]`

Score breakdown:

- individual: `10.268`
- pair synergy: `9.827`
- triple synergy: `1.500`
- redundancy penalty: `2.534`
- total: `19.061`

Improvement hint: Successful selection; inspect extra chunks only if precision or token cost becomes the priority.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `c25` | selected, required | 3.593 | 28 | The silver consent sleeve indicates telehealth follow-up. |
| `c28` | selected, optional | 3.593 | 31 | Silver consent telehealth follow-up slots open through in-person surgery clearance. |
| `c26` | selected, required | 2.050 | 30 | Telehealth follow-up slots are opened by the remote-care scheduler. |
| `c27` | selected, required | 0.850 | 29 | Remote-care scheduling uses the amber queue after noon. |
| `c09` | selected | 0.057 | 28 | The quiet room uses a dove marker on the scheduling board. |
| `c05` | selected | 0.025 | 27 | The sedation cabinet releases keys after the orange ledger is initialed. |
| `c30` | selected | 0.025 | 29 | Microbiology batches after-hours samples under code M-14. |
| `c11` | selected | 0.025 | 30 | Behavioral-health overflow is coordinated by Lina Park after 18:00. |
| `c24` | selected | 0.025 | 30 | Expired wristband replacement points to the security map label after a badge denial. |
| `c12` | selected | 0.025 | 31 | The quiet room after evening overflow is handled by the triage nurse for pediatric fever cases. |

### FAIL content_02_clinic_access / c_q15_three_hop / budget 128

Question: Which person collects the coded batch for lavender tray samples?

Selected: `['c28', 'c29', 'c30', 'c32']`
Tokens: `117/128`
F1: `0.706` Required recall: `0.667`
Missing required units: `['collector']`
Selected distractors: `[]`

Score breakdown:

- individual: `6.048`
- pair synergy: `2.019`
- triple synergy: `0.000`
- redundancy penalty: `0.602`
- total: `7.465`

Improvement hint: Tight-budget tradeoff; improve importance ranking so required evidence beats optional/filler chunks.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `c29` | selected, required | 2.650 | 27 | A lavender tray tag means samples go to microbiology. |
| `c32` | selected, optional | 2.650 | 30 | Lavender tray tags mean samples go to radiology during downtime. |
| `c30` | selected, required | 0.636 | 29 | Microbiology batches after-hours samples under code M-14. |
| `c20` | - | -0.221 | 31 | The person located at billing completes transport paperwork for red discharge packets. |
| `c17` | - | 0.700 | 29 | The red discharge packet means the patient needs transport paperwork. |
| `c31` | required | 0.533 | 30 | Code M-14 batches are collected by night runner Sima Chen. |
| `c18` | - | 0.400 | 29 | Transport paperwork is completed by the mobility coordinator. |
| `c28` | selected | 0.112 | 31 | Silver consent telehealth follow-up slots open through in-person surgery clearance. |
| `c37` | - | -0.300 | 28 | The pearl sticker means language assistance is requested. |
| `c33` | - | -0.371 | 28 | The bronze sticker on a chart means insurance review is pending. |

### PASS content_02_clinic_access / c_q15_three_hop / budget 256

Question: Which person collects the coded batch for lavender tray samples?

Selected: `['c17', 'c18', 'c20', 'c28', 'c29', 'c30', 'c31', 'c32']`
Tokens: `236/256`
F1: `0.667` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `[]`

Score breakdown:

- individual: `7.460`
- pair synergy: `5.274`
- triple synergy: `0.000`
- redundancy penalty: `1.801`
- total: `10.933`

Improvement hint: Successful selection; inspect extra chunks only if precision or token cost becomes the priority.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `c29` | selected, required | 2.650 | 27 | A lavender tray tag means samples go to microbiology. |
| `c32` | selected, optional | 2.650 | 30 | Lavender tray tags mean samples go to radiology during downtime. |
| `c30` | selected, required | 0.636 | 29 | Microbiology batches after-hours samples under code M-14. |
| `c20` | selected | -0.221 | 31 | The person located at billing completes transport paperwork for red discharge packets. |
| `c17` | selected | 0.700 | 29 | The red discharge packet means the patient needs transport paperwork. |
| `c31` | selected, required | 0.533 | 30 | Code M-14 batches are collected by night runner Sima Chen. |
| `c18` | selected | 0.400 | 29 | Transport paperwork is completed by the mobility coordinator. |
| `c28` | selected | 0.112 | 31 | Silver consent telehealth follow-up slots open through in-person surgery clearance. |
| `c37` | - | -0.300 | 28 | The pearl sticker means language assistance is requested. |
| `c33` | - | -0.371 | 28 | The bronze sticker on a chart means insurance review is pending. |

### PASS content_02_clinic_access / c_q15_three_hop / budget 512

Question: Which person collects the coded batch for lavender tray samples?

Selected: `['c17', 'c18', 'c20', 'c28', 'c29', 'c30', 'c31', 'c32']`
Tokens: `236/512`
F1: `0.667` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `[]`

Score breakdown:

- individual: `7.460`
- pair synergy: `5.274`
- triple synergy: `0.000`
- redundancy penalty: `1.801`
- total: `10.933`

Improvement hint: Successful selection; inspect extra chunks only if precision or token cost becomes the priority.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `c29` | selected, required | 2.650 | 27 | A lavender tray tag means samples go to microbiology. |
| `c32` | selected, optional | 2.650 | 30 | Lavender tray tags mean samples go to radiology during downtime. |
| `c30` | selected, required | 0.636 | 29 | Microbiology batches after-hours samples under code M-14. |
| `c20` | selected | -0.221 | 31 | The person located at billing completes transport paperwork for red discharge packets. |
| `c17` | selected | 0.700 | 29 | The red discharge packet means the patient needs transport paperwork. |
| `c31` | selected, required | 0.533 | 30 | Code M-14 batches are collected by night runner Sima Chen. |
| `c18` | selected | 0.400 | 29 | Transport paperwork is completed by the mobility coordinator. |
| `c28` | selected | 0.112 | 31 | Silver consent telehealth follow-up slots open through in-person surgery clearance. |
| `c37` | - | -0.300 | 28 | The pearl sticker means language assistance is requested. |
| `c33` | - | -0.371 | 28 | The bronze sticker on a chart means insurance review is pending. |

### PASS content_02_clinic_access / c_q15_three_hop / budget 1024

Question: Which person collects the coded batch for lavender tray samples?

Selected: `['c17', 'c18', 'c20', 'c28', 'c29', 'c30', 'c31', 'c32']`
Tokens: `236/1024`
F1: `0.667` Required recall: `1.000`
Missing required units: `[]`
Selected distractors: `[]`

Score breakdown:

- individual: `7.460`
- pair synergy: `5.274`
- triple synergy: `0.000`
- redundancy penalty: `1.801`
- total: `10.933`

Improvement hint: Successful selection; inspect extra chunks only if precision or token cost becomes the priority.

| id | flags | importance | tokens | text |
|---|---|---:|---:|---|
| `c29` | selected, required | 2.650 | 27 | A lavender tray tag means samples go to microbiology. |
| `c32` | selected, optional | 2.650 | 30 | Lavender tray tags mean samples go to radiology during downtime. |
| `c30` | selected, required | 0.636 | 29 | Microbiology batches after-hours samples under code M-14. |
| `c20` | selected | -0.221 | 31 | The person located at billing completes transport paperwork for red discharge packets. |
| `c17` | selected | 0.700 | 29 | The red discharge packet means the patient needs transport paperwork. |
| `c31` | selected, required | 0.533 | 30 | Code M-14 batches are collected by night runner Sima Chen. |
| `c18` | selected | 0.400 | 29 | Transport paperwork is completed by the mobility coordinator. |
| `c28` | selected | 0.112 | 31 | Silver consent telehealth follow-up slots open through in-person surgery clearance. |
| `c37` | - | -0.300 | 28 | The pearl sticker means language assistance is requested. |
| `c33` | - | -0.371 | 28 | The bronze sticker on a chart means insurance review is pending. |
