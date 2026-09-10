# GX Cartório OS — Next Session Pointer — 2026-09-10

## Purpose
This file is the HOT handoff for the next ChatGPT conversation. Resume from here without reopening architecture from scratch.

## User mission
Prepare from near-zero/rusty legal knowledge to **competitive mastery for approval in ENAC + state objective + discursive + practical + oral stages**, targeting readiness by the end of 2027 and 2028 as absolute buffer ceiling.

The user does **not** want to optimize for a passing floor. The design target is maximum practical exam performance, ideally approaching gabarito-level reliability, while avoiding useless content and manual study administration.

## Latest authorial requirements
1. **Extreme efficiency:** every unit of study must justify its cost by one or more of: comprehension, retention, discrimination, transfer, objective accuracy, written production, practical execution, oral performance, or legal freshness.
2. **No encyclopedic waste:** 100% syllabus coverage does not mean equal depth. Use foundation/core/high-yield/tail/reference budgets.
3. **Self-sufficient material:** candidate should not need to compare 4–5 apostilas to know whether something important is missing. The system should contain the necessary path, sources, questions, explanations, review and output training.
4. **Linear/coherent visible progression by discipline:** preserve syllabus/discipline architecture so the user always knows where he is. Internal graph connections may support learning but must not create a soup.
5. **Question-driven engineering at scale:** for each topic/subtopic, mine and classify relevant questions across legal-career levels and banks, with provenance, time window, legal snapshot and current-law revalidation. Historical items may be adapted for current-law practice only when clearly labeled; original historical evidence must remain intact.
6. **Do not use one undifferentiated mega-corpus.** Maintain:
   - Domain Incidence Model = what the domain asks across banks;
   - Bank Style Model = how a specific bank/period/family/phase asks.
7. **Oral corpus is first-class.** Collect official oral questions, published oral scripts/espelhos where available, practical cases and follow-up patterns. Build oral practice progressively from simple recall to structured case answers and reperguntas.
8. **Discursive/practical are progressive, not postponed.** Start with micro-outputs, then issue spotting, answer atoms, legal basis, structured paragraphs, full discursive, practical instrument/act and timed execution.
9. **Question difficulty ladder:** easy recall -> medium discrimination -> hard application -> elite/hard case synthesis. Difficulty should be empirical/behavioral when possible, not decorative labels.
10. **Dry law / lei seca is important.** Do not replace statute reading with summaries. Build guided statute reading around high-value provisions, distinctions, lists, deadlines, competence, exceptions and wording-sensitive points. Use retrieval and cloze/QA selectively, not transcription.
11. **No manual summaries by the candidate as default.** The user historically wastes time transcribing. The system should generate/refactor notes and ask the user mainly to retrieve, explain, solve and produce.
12. **Spaced review must remain tractable.** Do not create a review avalanche. Review queues must prioritize forgetting risk × exam value × learner gap × transfer, and compress/reuse items over time. Retire or reduce low-value prompts as evidence accumulates.
13. **Reusable evolving study objects:** questions, flashcards, oral prompts, mini-discursives and review prompts should be versioned, improved, merged, retired or discarded based on usefulness and learner evidence. Do not endlessly accumulate.
14. **ADHD-aware UX:** candidate reports attention problems and rapid forgetting. Use short coherent blocks, visible location, explicit objective, progressive challenge, active response, low executive burden, and avoid dense visual clutter / too many badges / too many simultaneous tasks. Do not medicalize or assume every failure is ADHD.
15. **Audio is a core interaction mode:** user may answer oral questions by voice; analyze the transcript for legal atoms, precision, structure, missing elements, confidence, concision and follow-up readiness.
16. **Vocabulary and legal expression:** progressively train precise legal vocabulary and concise oral/written formulation without turning the study into stylistic ornament.
17. **Freshness Firewall remains mandatory:** historical source snapshot != current law. Never silently modernize an old item and then present it as historical evidence. Keep original + current adaptation separated.
18. **Predictive analysis must be calibrated:** use recency, recurrence, syllabus surface, legal change, bank/family style and domain incidence, but no fake microtopic probabilities from tiny samples. Backtest when corpus allows.

## Important evidence from old user backups
User uploaded old Penal/Constitutional/Administrative study-system backups. Key lessons already extracted:
- Good instincts worth preserving: advance organizer/map before depth; coherent discipline sequence; self-sufficient theory; remissions/cross-references; tables; objective + discursive + oral; review layer; active study.
- Failure modes to prevent: duplicated versions inside same material, logs/agent instructions mixed with study content, too many labels/callouts, every detail promoted to core, unsupported claims of 'high incidence', architecture names overtaking content, progressive formatting drift.
- Therefore freeze a small visual grammar and single canonical Knowledge Unit with derived MAP/REVIEW/RECALL views.

## Current material experiments
- N/R Entry Map in Notion: `00 — Mapa de Entrada: o que é o sistema notarial e registral`.
- N/R regime pilot: `01 — Regime jurídico dos serviços notariais e de registro — PILOTO`.
- Constitutional control demo: MASTER + REVIEW + RECALL + EXAM Lab. These are editorial experiments, not full canonical standard yet.

## Current corpus state
- ENAC 2025.1: 100/100 indexed/classified passage 1.
- ENAC 2025.2: 100/100 indexed/classified passage 1.
- ENAC 2026.1: 100/100 canonical indexed/classified passage 1.
- Total logical: 300/300.
- Six annulled items preserved.
- Passage 1 is **not** full reconstruction. It lacks full item text/alternatives/rationale/resources/current-law snapshot at scale.

## Next work order — DO NOT restart architecture brainstorming
### A. Freeze Editorial Standard v1.0
Create a concrete style contract from the demos + old-backup lessons:
- visual grammar;
- maximum callout density;
- cross-reference syntax;
- paragraph/table rules;
- what belongs in MASTER vs REVIEW vs RECALL vs EXAM vs REFERENCE;
- how law, jurisprudence, doctrine, theory and questions are visually marked;
- anti-duplication rules.

### B. Build one full end-to-end canonical pilot
Prefer a topic with sufficient official sources and question coverage. It must pass:
`edital -> primary law -> current jurisprudence -> ENAC/FGV -> state/cartório FGV -> domain multibank -> oral/discursive/practical corpus -> Reconstruction Cards -> depth budget -> MASTER -> REVIEW -> RECALL -> EXAM -> QA -> freshness check`.

The pilot must prove **self-sufficiency and efficiency**, not just visual polish.

### C. Oral + written corpus layer
Create/extend a registry for:
- source/court/bank/year/phase;
- exact oral/discursive/practical prompt when lawfully available;
- official mirror/criteria if available;
- legal atoms expected;
- difficulty/cognitive demand;
- historical-law snapshot;
- current-law adaptation separately;
- follow-up questions/reperguntas where evidence exists.

### D. Lei seca protocol
Formalize guided statute study:
- what is read verbatim;
- what is converted to recall;
- how lists/deadlines/competence/exceptions are trained;
- when a provision leaves high-frequency review;
- how current version is revalidated.

### E. Review-load control
Formalize queue budget so spaced practice does not become massive:
- due reviews are not all equal;
- prioritize by `exam value × forgetting risk × learner gap × transfer × freshness`;
- merge equivalent prompts;
- retire saturated low-value cards;
- prefer reconstruction/case over duplicate flashcards when appropriate.

### F. Minimum Viable Tutor gate
Before broad material production, ensure runtime can:
`choose node -> orient -> teach small coherent chunk -> retrieval -> item/case -> diagnose -> register M0–M7 + retention -> schedule -> pick next action`.

## Core quality gate
A canonical unit must answer YES to all:
1. Does it cover the relevant syllabus surface without silent gaps?
2. Can the candidate understand it from near-zero prerequisite state using JIT foundations?
3. Is every high-cost detail justified by exam/transfer value?
4. Are primary sources and freshness explicit?
5. Does it include enough variation to resist distractors rather than memorize one wording?
6. Does it train at least objective output and, where phase-relevant, progressive written/oral/practical output?
7. Can review be derived without rereading the whole chapter?
8. Are cross-references helpful but not noisy?
9. Is the candidate's executive burden close to zero?
10. Can the system later explain why this content had this priority/depth?

## Next-chat reanchor instruction
Open next conversation with:
`Reancore o GX Cartório OS na branch chatgpt/gx-cartorio-v0.1. Leia STATUS.md e handoff/NEXT_SESSION_POINTER_2026-09-10.md. Não reinicie a arquitetura. Continue pelo Work Order A, preservando o horizonte 2027–2028, a regra de eficiência extrema, oral/discursiva/prática progressivas, lei seca guiada e o Freshness Firewall.`
