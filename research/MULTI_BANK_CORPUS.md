# GX Cartório OS — Multi-Bank Corpus Strategy

Status: v0.3 research protocol — atualizado em 09/09/2026.

## Objective
Build a large question corpus without diluting the style of the target exam. Questions are not interchangeable. Every item receives provenance, legal-complexity, freshness, phase and adherence metadata.

## Two-estimator architecture
The system answers two different questions with different pooling rules.

### 1. Domain Incidence Model
Question: **What does the cartório domain actually test?**

May combine:
- ENAC;
- FGV state cartório;
- Cebraspe/Vunesp/other cartório exams;
- written/practical corpora.

Purpose:
- enlarge thematic coverage;
- estimate domain recurrence at useful granularity;
- identify rare but recurrent institutes;
- inform Depth Budget.

Bank provenance is retained as a covariate; it is not erased.

### 2. Bank Style Model
Question: **How does a specific bank turn law into assessment?**

Must be restricted by:
- bank;
- recent time window;
- legal-complexity class;
- exam family;
- phase.

Purpose:
- stem architecture;
- case density;
- command types;
- source mix;
- cognitive demand;
- distractor mechanisms;
- ambiguity/annulment;
- written/practical mirror behavior.

Other banks never enlarge the sample for a target bank's style estimate.

## Corpus hierarchy
### Tier A — target-direct
1. ENAC official questions, prioritizing newest editions.
2. Current target-state contest questions when a specific edital/bank is known.

### Tier B — same domain + same bank
3. FGV cartório contests beyond ENAC, including objective, written/practical and available correction mirrors.
4. For a state target, cartório contests run by the same organizer.

### Tier C — same subject + same bank
5. FGV questions from high-complexity legal careers when the microtopic overlaps the Cartório curriculum: ENAM/magistracy, MP, defensoria, procuradorias and genuinely comparable selections.
6. Same rule for the target-state bank.

These are especially useful for bank-style transfer in general legal subjects with little ENAC history, but should be tagged by exam family.

### Tier D — same domain + other banks
7. Cartório contests from Cebraspe, Vunesp and other relevant organizers. High value for the **Domain Incidence Model**, rare subtopics, written/practical material and robustness.

### Tier E — same subject + other banks
8. High-quality questions on the same microtopic from other major legal-exam banks, mainly for retrieval, discrimination and transfer.

### Tier F — foundation drill
9. Lower-complexity questions may be used only when they isolate an elementary proposition the learner needs to automate.
10. They do not inform L4 bank-style conclusions.

### Tier G — synthetic GX
11. New questions generated only after grounding in current primary authority and calibration against documented patterns. Always labeled `Sintética GX`.

## Legal-complexity class
- `L4 — Cartório / magistratura / advanced legal professional`;
- `L3 — high-level legal career`;
- `L2 — general higher-education legal/administrative`;
- `L1 — foundation / medium-level drill`.

Default exam-modeling prioritizes L4/L3. L1/L2 are auxiliary.

## Why expansion is necessary
The ENAC historical core currently provides 300 indexed items, only 180 formally N/R across three editions. That is insufficient for stable fine-grained incidence over 138 official N/R subitems and extremely sparse for low-weight subjects.

Expansion is therefore not merely `more questions`; it provides statistical coverage for the **domain** while preserving a narrower target-bank style model.

Example:
- ENAC Penal identifies target relevance;
- FGV L4/L3 same-topic items deepen FGV framing;
- other cartório banks show domain recurrence;
- other high-level banks test transfer;
- L1/L2 drills repair basic roots if needed.

## Adherence score
Each item may receive a 0–100 `Aderência ao alvo` training score based on:
- same exam family;
- same bank;
- same legal domain;
- same microtopic;
- comparable complexity;
- recency;
- current-law compatibility;
- same cognitive demand;
- same phase.

This score prioritizes training. It is not a probability forecast or a substitute for the two estimators.

## Anti-contamination rule
- Domain recurrence may pool banks with provenance/pesos.
- Bank style may not.
- A Cebraspe item can increase confidence that an institute matters in cartório without changing the inferred FGV distractor profile.
- A same-topic FGV ENAM item may inform FGV general style with lower exam-family weight, but it does not become ENAC evidence.

## Bank DNA profile
For each relevant bank maintain a versioned/time-windowed profile:
- stem length and case density;
- literal-law vs application balance;
- jurisprudence usage;
- statutory/regulatory recency;
- distractor mechanisms;
- negative commands;
- interdisciplinarity;
- depth/legal complexity;
- source families;
- annulment/controversy patterns;
- written/practical correction patterns;
- observable style drift.

A bank is a distribution, not a timeless personality.

## Statistical discipline
Do not infer precise microtopic probabilities from tiny cells.

Permitted:
- aggregate descriptive features from complete exams;
- domain incidence after pooling appropriately labeled cartório corpora;
- qualitative/time-window hypotheses with sample size and confidence;
- priors from structural syllabus surface and recent normative changes.

Not permitted:
- `chance de cair = 83%` from a handful of items;
- pooling banks to manufacture FGV sample size;
- treating three ENAC editions as a long time series.

## Question-to-source reverse engineering
For high-value items identify the authoritative path sufficient to solve them:
- Constitution/statute/code;
- CNJ/Corregedoria act;
- STF/STJ/TJ precedent;
- binding theme/súmula;
- doctrinal controversy when genuinely required;
- operational regulation;
- recent legislative innovation.

Do not invent a specific examiner bibliography without evidence.

## Answer triangulation protocol
1. preserve/link official statement and official key/mirror;
2. inspect official resource/annulment rationale when available;
3. reconstruct legal basis independently from primary historical/current sources;
4. compare qualified commentary afterward;
5. record conflicts explicitly;
6. preserve historical/current snapshots separately;
7. never teach a historical answer as current doctrine without temporal labeling.

For discursive/practical items, official correction mirrors receive special weight because they reveal rewarded answer atoms.

## Freshness weighting
Recency is a prior, not truth. Suggested initial weights from older versions remain **experimental**, not canonic. They may be replaced after empirical calibration.

Normative volatility may increase study/revalidation priority but does not itself prove higher exam incidence.

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

For operational retesting, the system also needs access to stem and alternatives. These may be stored in a controlled data plane linked to the official artifact rather than unnecessarily republished in the public repository.

## Validation rule
No synthetic or third-party-commented question becomes canonical merely because it appears plausible. Canonical answer logic must be reconciled against official key/mirror when available and authoritative law in the relevant temporal snapshot.
