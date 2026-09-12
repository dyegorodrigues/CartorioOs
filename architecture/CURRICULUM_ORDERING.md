# GX Cartório OS — Curriculum Ordering

Atualizado em 09/09/2026.

## Goal
Choose study order by legal dependency + exam value + learner state, not by the printed order of the edital and not by subject silos.

## Anti-tree-bias rule
The syllabus tree is a **navigation and coverage interface**, not the ontology of knowledge.

The real model is multidimensional. A single concept can simultaneously relate to:
- multiple syllabus nodes;
- prerequisite concepts from other subjects;
- statutes, CNJ acts and jurisprudence;
- question clusters from multiple banks;
- objective, discursive, practical and oral outputs;
- learner errors and retention state.

Therefore the UI may show `Matéria → Tema → Subtema → Microtema`, while the scheduler and mastery engine operate over a graph.

## Operational graph v0.1
Do not instantiate a decorative ontology.

Two cross-links have immediate scheduler value and are therefore first-class:
- `requires` — a prerequisite that can reduce readiness for the target node;
- `confusable_with` — a pair whose discrimination should be trained explicitly.

Sources, questions, jurisprudence, phase relevance and freshness remain linked metadata/evidence. New edge types are created only when they change a real decision or useful query.

## Core views run together

### A. Coverage view
Mirrors the official syllabus. Guarantees nothing is forgotten.

### B. Dependency view
Represents concepts that must be understood before another concept becomes cognitively stable.

Examples:
- constitutional delegation/public-service framework → general notarial/registry regime;
- legal act / legal transaction / form / validity / effectiveness → notarial acts and registry qualification;
- property / possession / real rights / acquisition modes → Registro de Imóveis;
- legal personality / associations / foundations → RCPJ;
- family / succession → RCPN, Notes, inventories and partitions;
- obligations / credit instruments → Protest;
- administrative principles / responsibility → delegation, inspection and disciplinary regime;
- tax incidence → deeds, transfers, registration and fiscal requirements.

### C. Exam-value view
Weights nodes by current edital, domain incidence evidence, target-bank evidence, state overlay, structural surface, normative volatility, cross-phase transfer and learner weakness.

### D. Evidence view
Connects propositions to primary authority, historical questions, official keys/mirrors, competing interpretations and freshness status.

### E. Performance view
Tracks M0–M7 separately from retention/stability.

## Ordering function
The scheduler chooses the highest-value **learnable next node**, but no exact predictive formula is canonical before learner data exists.

The former pure product
`exam_value × learner_gap × forgetting_risk × transfer_value × readiness × freshness_confidence`
is retained only as conceptual intuition. A pure product is brittle because one absent/near-zero factor can collapse priority.

### Bootstrap score
Until calibrated, use normalized components with explicit priors/floors rather than zeros:
- `exam_value` — official matrix + structural syllabus surface;
- `learner_gap` — prior high at baseline, replaced by evidence;
- `forgetting_risk` — prior moderate, then retention evidence;
- `transfer_value` — objective/discursive/practical/oral reuse;
- `readiness` — prerequisite status, with blocking only when genuinely necessary;
- `freshness_risk` — volatility/revalidation need;
- `target_urgency` — proximity to real exam/campaign.

A weighted additive/log scoring rule may be implemented once normalized data exist. Weights must be testable and recalibrated against actual performance, not chosen for mathematical appearance.

## Statistical priors when historical frequency is sparse
The 300 historical ENAC questions are not enough for stable frequency estimates across 138 N/R subtopics. Therefore priority may use multiple independent signals:
- official weight;
- number/surface of explicit syllabus requirements;
- domain incidence from broader cartório corpus;
- target-bank style evidence;
- legal dependency/centrality;
- cross-phase transfer;
- normative volatility;
- individual error/retention evidence.

Never turn a tiny microtopic cell into a precise `chance de cair`.

## Spiral progression
Avoid two bad extremes:
- finishing all Civil before touching Cartório;
- jumping into technical registry law with no conceptual anchors.

Use a spiral:
1. orientation map;
2. minimal foundations;
3. immediate extrajudicial application;
4. retrieval prompt;
5. question/case;
6. error diagnosis;
7. return to foundations with more depth as dependencies recur;
8. cross-subject integration;
9. phase-specific output practice.

## Initial macro-sequence for a rusty candidate
This is a provisional pedagogy prior, not a fixed calendar.

**N/R begins in the first study cycle.** It is both the largest current objective block and the domain with the least prior exposure, so it needs the longest calendar for repeated consolidation.

Suggested spiral:
1. global map of the career, ENAC and state contests;
2. general regime of notarial/registry services + first principles of the extrajudicial system;
3. early N/R foundations and qualification logic;
4. Civil/Constitutional foundations pulled **just in time** as N/R nodes require them;
5. early specialization modules: RI, Notes, RCPN/RCPJ/RTD/Protest, each paired with its prerequisite foundations;
6. Administrative, Tax and Business integrated where they affect real extrajudicial problems while preserving coherent Discipline Maps;
7. procedural subjects where needed for doubt proceedings, judicial/extrajudicial interaction and full edital coverage;
8. low-weight objective-only subjects maintained in efficient cycles unless a target edital changes their relevance.

This does not mean `study 60% of the clock in N/R` mechanically. Allocation is adaptive.

## One knowledge base, multiple outputs
High-value knowledge is authored once in a canonical knowledge unit, then rendered into:
- objective discrimination;
- short-answer retrieval;
- case analysis;
- discursive answer;
- practical piece / procedural solution;
- oral response and follow-up questions.

## Phase depth
A node can have different target mastery levels.

Canonical scale: M0–M7 defined in `LEARNING_SYSTEM.md` / `ZERO_TO_OUTORGA_SYSTEM.md`.

Examples:
- low-weight objective-only topic: target may stop at stable M3/M4;
- high-value N/R topic: progression to M5–M7 as evidence and phase relevance justify.

Production begins in microdoses early; it does not wait for the ENAC certificate. Its share grows as the base becomes stable and a state contest approaches.

## Adaptive pacing and target horizon
- 2026: re-entry, base construction and real learner telemetry;
- first ENAC edition in 2027: first habilitation target;
- end of 2027: desired broad competitive readiness;
- 2028: maximum buffer, not default duration.

Weekly load expands only after stable execution. The first optimization target for a rusty candidate is **consistency + correct reconstruction + retention**, not maximal daily volume.
