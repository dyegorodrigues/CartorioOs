# QUESTION QA & CONFLICT LEDGER v0.1
**Date:** 2026-10-01
**Purpose:** prevent bad, ambiguous, misclassified, stale or internally inconsistent questions/materials from silently becoming canonical knowledge.

## Status codes
- OFFICIAL_METADATA_CONFLICT
- OFFICIAL_KEY_DOCTRINAL_DISPUTE
- SECONDARY_SOURCE_CONFLICT
- LEGACY_MATERIAL_SUSPECT_REFERENCE
- HISTORICAL_STATE_REQUIRED
- QUESTION_DEFECT_SUSPECTED
- SOURCE_PROVENANCE_PENDING

---

## QQA-001 — PC-PI 2026 / FGV / Delegado / official date inconsistency
**Status:** OFFICIAL_METADATA_CONFLICT

### Evidence
- Official FGV contest page lists **Prova Objetiva: 27/01/2026**.
- The official definitive-key PDF header says **“GABARITO DEFINITIVO DA PROVA APLICADA NO DIA 25/01/2025”**.
- Strategy's post-exam commented PDF says the objective exam was applied **25/01/2026**.

### Handling
Do NOT silently normalize the date. Store all three observations and mark metadata_conflict. The legal-content answers can still be used, but temporal metadata needs explicit reconciliation before incidence statistics by exact exam date.

### Sources
- FGV official competition page: https://conhecimento.fgv.br/concursos/pcpi25/1
- FGV official definitive key: https://conhecimento.fgv.br/sites/default/files/concursos/pcpi-delegado-gabarito-definitivo.pdf
- Strategy commented exam: https://cj.estrategia.com/portal/wp-content/uploads/2026/01/26141918/Prova-comentada-PC-PI.pdf

---

## QQA-002 — PC-PI 2026 / FGV / Q72 (Type 1) / minimalism & selectivity
**Status:** OFFICIAL_KEY_DOCTRINAL_DISPUTE + QUESTION_DEFECT_SUSPECTED

### Official item
I. links art. 168-A treatment to minimum intervention / ultima ratio / criminological minimalism.
II. uses the contrast between arts. 168 and 168-A to discuss penal selectivity and criminalization.
III. says the Delegate should analogically extend extinction of punishability to common appropriation.

**Official definitive Type 1 key:** **B = II only**.

### External expert commentary
Strategy's commented exam explicitly says the item is **appealable**, because statements I and II may both be defensible. It treats III as clearly wrong because the Delegate cannot create an unprovided extinction-of-punishability hypothesis merely from a criminological critique.

### Why this matters
This is exactly the type of contemporary question the Tutor OS must NOT “learn” naively from the official key.

Store separately:
- official answer;
- doctrinal proposition;
- commentary disagreement;
- legal-positive limit;
- confidence in each atom.

### Editorial rule produced
When a question blends **critical criminology** with **positive criminal law**, the MASTER must teach the boundary: critical diagnosis can expose selectivity or question criminal policy, but it does not automatically authorize the law applier to disregard legality.

### Sources
- Official FGV exam: https://conhecimento.fgv.br/sites/default/files/concursos/delegado-de-policia-cns100-tipo-1.pdf
- Official key: https://conhecimento.fgv.br/sites/default/files/concursos/pcpi-delegado-gabarito-definitivo.pdf
- Strategy commented exam: https://cj.estrategia.com/portal/wp-content/uploads/2026/01/26141918/Prova-comentada-PC-PI.pdf

---

## QQA-003 — PC-RS 2025 / FUNDATEC / functions & characteristics
**Status:** SOURCE_PROVENANCE_PENDING + DOCTRINAL_ATTRIBUTION_REQUIRED

### Evidence
Third-party banks reproduce the item on promotional function, fragmentarity, subsidiarity/ultima ratio, and sanctioning nature. They report the expected combination as II and III.

Official Polícia Civil RS records confirm the 2025 Delegado contest existed, FUNDATEC administered the preliminary exam, preliminary keys were published 22/12/2025, definitive results followed in 2026, and the competition continued through oral stages in Sep 2026.

### Risk
The phrase “segundo a doutrina majoritária” is itself a source-selection problem. Some prep doctrine catalogues a promotional function, but the item rejects the specific formulation “superando a mera proteção de bens jurídicos”.

### Handling
Do not teach “função promocional não existe”. Teach that doctrinal catalogues differ; legitimacy/formulation is contested; the exact proposition can be false because it makes Penal law a primary social-engineering tool overriding protection/ultima ratio; named-author attribution matters.

### Sources
- PC-RS official contest page: https://pc.rs.gov.br/concurso-publico-para-delegado-de-policia-2025
- QConcursos / Gran / other banks for item discovery; official question PDF still to be archived into corpus.

---

## QQA-004 — DD Código Penal legacy reference: “art. 233, CPP – crime de ato obsceno”
**Status:** LEGACY_MATERIAL_SUSPECT_REFERENCE

The prep PDF used in the legacy corpus contains a reference extracted as “Art. 233, CPP – crime de ato obsceno”. Crime de ato obsceno is ordinarily associated with **art. 233 of the Código Penal**, not CPP. Before any sentence based on this example enters CORE, inspect the page/visual source and validate against official legislation.

### Handling
- preserve raw source;
- mark as suspect;
- never silently correct the archived source;
- if confirmed typo, CORE uses correct official source and genealogy records the legacy error.

---

## QQA-005 — PC-PI 2026 / Q71 / Classical School
**Status:** DOCTRINAL_ATTRIBUTION_REQUIRED

Official Type 1 key marks **C** as the incorrect alternative. The current Strategy commented material frames the classical/positivist 'defesa social' comparison in a way that may not map perfectly onto the official structure of all alternatives.

### Handling
Before promoting a compact “Classical School = X” table:
- verify Beccaria's function-of-penalty formulation in authoritative doctrine;
- distinguish broad historical movement from positions of individual authors;
- do not treat one multiple-choice key as a complete history of classical criminology.

### Editorial impact
Schools/evolution cannot remain a “Magistratura-only” node: current FGV Delegado 2026 directly tested it. But it should remain its own coherent module, connected to legality and criminology, rather than bloating the first concept paragraph.

---

## General QA rule
A real question can be:
1. correct and clean;
2. legally historical;
3. ambiguous;
4. doctrinally contested;
5. source-misclassified;
6. officially keyed but pedagogically unsafe;
7. defective.

Only category (1), after source validation, can be used as a clean training target without warning. The others remain valuable evidence, but must carry their status.