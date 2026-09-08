# GX Cartório OS — Multi-Bank Corpus Strategy

Status: v0.2 research protocol

## Objective
Build a large question corpus without diluting the style of the target exam. Questions are not interchangeable. Every item receives provenance, legal-complexity, freshness, phase and adherence metadata.

## Corpus hierarchy

### Tier A — target-direct
1. ENAC official questions, prioritizing the newest editions.
2. Current target-state contest questions when a specific edital/bank is known.

### Tier B — same domain + same bank
3. FGV cartório contests beyond ENAC (e.g. ES, MS, RN, SC historical), including objective, written/practical and available correction mirrors.
4. For a state target, cartório contests run by that same state bank.

### Tier C — same subject + same bank
5. FGV questions in Civil, Constitutional, Administrative, Tax, Business, Procedure and other syllabus fields from **high-complexity legal careers** when the microtopic overlaps the Cartório curriculum: magistracy/ENAM, MP, defensoria, procuradorias/advocacy, tribunals and other genuinely useful legal selections.
6. Same rule for the target state bank.

### Tier D — same domain + other banks
7. Cartório contests from Cebraspe, Vunesp and other relevant organizers. Valuable for domain coverage, rare subtopics, written/practical material and robustness, but they never redefine the style model of FGV/target bank by themselves.

### Tier E — same subject + other banks
8. High-quality questions on the same microtopic from other major legal-exam banks, used mainly for retrieval, discrimination and transfer.

### Tier F — foundation drill
9. Questions from lower-complexity or non-core careers may be used **only when they isolate an elementary legal proposition that the learner needs to automate** (e.g. constitutional competence, basic civil concept, literal statutory requirement).
10. These items receive low style-inference weight and cannot be used to infer the DNA of a high-level legal examination.

### Tier G — synthetic GX
11. New questions generated only after grounding in current primary authority and calibrated against documented patterns. Synthetic questions are always labeled.

## Legal-complexity class
Each question receives one class independent from bank:
- `L4 — Cartório / magistratura / advanced legal professional`;
- `L3 — high-level legal career`;
- `L2 — general higher-education legal/administrative`;
- `L1 — foundation / medium-level drill`.

Default teaching and bank-modeling corpus prioritizes L4/L3. L1/L2 are auxiliary and topic-specific.

## Why not restrict the corpus to cartório only?
Some ENAC subjects have very few questions per edition. A single Penal or Processual Penal item cannot sustain a complete learning model. The system therefore expands sideways by **same microtopic + same bank + comparable legal complexity**, and only then to other banks.

Example:
- ENAC Penal item exposes a microtopic;
- FGV magistracy/ENAM/prosecutorial questions deepen the same Penal microtopic and reveal FGV framing;
- Cebraspe/Vunesp legal-career questions provide transfer and alternative traps;
- lower-level questions may drill the bare rule if the learner lacks the foundation.

## Adherence score
Each item receives a 0–100 `Aderência ao alvo` score based on:
- same exam family;
- same bank;
- same legal domain;
- same microtopic;
- comparable legal-complexity class;
- recency;
- current-law compatibility;
- same cognitive demand;
- same phase (objective / discursive / practical / oral).

The score prioritizes training. It is not a probability forecast.

## Anti-contamination rule
Patterns from secondary banks or lower-complexity exams may expand legal coverage and test transfer, but do not alter the inferred style of the main bank unless independently supported by target-bank evidence.

## Bank DNA profile
For each relevant bank, maintain a **versioned, time-windowed profile** with:
- stem length and case density;
- literal-law vs application balance;
- jurisprudence usage;
- statutory recency;
- distractor mechanisms;
- negative commands (`incorreta`, `exceto`, etc.);
- interdisciplinarity;
- depth and legal-complexity expectation;
- recurring source families;
- annulment / controversy patterns;
- written/practical correction patterns when available;
- evidence of style drift over time.

A bank is not modeled as a timeless personality. Profiles are estimated by period and newer evidence can outweigh older evidence.

## Question-to-source reverse engineering
For high-value items, attempt to identify the likely source family behind the proposition:
- Constitution / statute / code;
- CNJ/Corregedoria act;
- STF/STJ/TJ precedent;
- binding theme/súmula;
- doctrinal controversy;
- operational regulation;
- recent legislative innovation.

Do not claim the examiner literally consulted a specific book unless evidence exists. The goal is to reconstruct **the authoritative knowledge path needed to answer**, not invent an examiner bibliography.

## Answer triangulation protocol
A third-party explanation is evidence, not authority. For a high-value question:
1. preserve the official statement and official key/mirror;
2. inspect official resource/annulment reasons when available;
3. reconstruct the legal basis independently from primary/current sources;
4. compare qualified commentaries only after the primary reconstruction;
5. record conflicts explicitly;
6. if current law differs from historical law, preserve both snapshots;
7. never teach a historical answer as current doctrine without labeling the temporal frame.

For discursive/practical items, official correction mirrors receive special weight because they expose what the examining institution rewarded.

## Freshness weighting
Suggested prior before empirical calibration:
- current ENAC cycle: 1.00
- previous ENAC cycle: 0.95
- second previous ENAC cycle: 0.90
- recent same-bank cartório: 0.85
- older same-bank cartório: 0.70
- recent other-bank cartório: 0.65
- same-topic same-bank L4/L3 legal career: 0.60
- same-topic other-bank L4/L3 legal career: 0.40
- lower-complexity foundation drill: <= 0.20 for bank-style inference

These are priors, not final learned weights.

## Required metadata per question
- source URL / official file when possible;
- year and contest;
- bank;
- phase;
- provenance tier;
- legal-complexity class;
- curriculum node(s);
- primary authority/source family;
- correct answer / official mirror;
- cognitive demand;
- distractor mechanism;
- historical-law snapshot;
- current-law snapshot;
- date-sensitive rule flag;
- adherence score;
- validation status;
- learner result, confidence and latency.

## Validation rule
No synthetic or third-party-commented question becomes canonical merely because it appears plausible. Canonical answer logic must be reconciled against official key/mirror when available and authoritative law in the relevant temporal snapshot.
