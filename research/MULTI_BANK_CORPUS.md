# GX Cartório OS — Multi-Bank Corpus Strategy

Status: v0.1 research protocol

## Objective
Build a large question corpus without diluting the style of the target exam. Questions are not treated as interchangeable. Every item receives a provenance class and an adherence score.

## Corpus hierarchy

### Tier A — target-direct
1. ENAC official questions, prioritizing the newest editions.
2. Current target-state contest questions when a specific edital/bank is known.

### Tier B — same domain + same bank
3. FGV cartório contests beyond ENAC (e.g. ES, MS, RN, SC historical), including objective, written/practical and available correction mirrors.
4. For a state target, cartório contests run by that same state bank.

### Tier C — same subject + same bank
5. FGV questions in Civil, Constitutional, Administrative, Tax, Business and Procedure from high-level legal careers when the microtopic overlaps the Cartório curriculum.
6. Same rule for the target state bank.

### Tier D — same domain + other banks
7. Cartório contests from Cebraspe, Vunesp and other relevant organizers. These are valuable for domain coverage, rare subtopics, written/practical material and robustness, but must never redefine the style model of FGV/target bank.

### Tier E — same subject + other banks
8. High-quality questions on the same microtopic from other major legal-exam banks, used mainly for retrieval, discrimination and transfer.

### Tier F — synthetic GX
9. New questions generated only after grounding in current primary authority and calibrated against documented patterns. Synthetic questions are always labeled as such.

## Adherence score
Each item should receive a 0–100 `Aderência ao alvo` score based on:
- same exam family;
- same bank;
- same legal domain;
- same microtopic;
- recency;
- current-law compatibility;
- same cognitive demand;
- same phase (objective / discursive / practical / oral).

The score is a prioritization aid, not a claim that a question predicts the future.

## Anti-contamination rule
Patterns from secondary banks may expand legal coverage and test transfer, but they do not change the inferred style of the main bank unless independently supported by target-bank evidence.

Example: a Cebraspe doctrinal controversy can expose a legal edge case. It does not prove FGV will charge that edge case or use that framing.

## Bank profile
For each relevant bank, maintain a versioned profile with:
- typical stem length and case density;
- frequency of literal-law vs application;
- use of jurisprudence;
- structure of distractors;
- negative commands (`incorreta`, `exceto`, etc.);
- interdisciplinarity;
- expected depth;
- annulment / controversy patterns;
- written/practical correction patterns when available.

Profiles are evidence-derived and time-sensitive. Older patterns decay in weight when newer evidence materially differs.

## Freshness weighting
Suggested default weighting before empirical calibration:
- current ENAC cycle: 1.00
- previous ENAC cycle: 0.95
- second previous ENAC cycle: 0.90
- recent same-bank cartório: 0.85
- older same-bank cartório: 0.70
- recent other-bank cartório: 0.65
- same-topic same-bank legal career: 0.60
- same-topic other-bank legal career: 0.40

These values are initial priors and must be recalibrated after corpus analysis.

## Required metadata per question
- source URL / official file when possible;
- year and contest;
- bank;
- phase;
- provenance tier;
- curriculum node(s);
- primary authority;
- correct answer / official mirror;
- cognitive demand;
- distractor mechanism;
- date-sensitive rule flag;
- adherence score;
- validation status;
- learner result, confidence and latency.

## Validation rule
No synthetic or third-party-commented question becomes canonical merely because it appears plausible. Canonical answer logic must be reconciled against the official key/mirror when available and current primary legal authority.
