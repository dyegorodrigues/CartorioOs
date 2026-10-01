# WORK HANDOFF — LEGAL TUTOR OS
**Date:** 2026-10-01
**Repository:** dyegorodrigues/CartorioOs
**Branch:** chatgpt/legal-tutor-os-core-2026-09-30
**Mode recommendation:** ChatGPT Work + GPT-6 Astra (if available)
**Status:** active research/audit; NOT complete

## Mission
Continue autonomously building the evidence-driven Legal Tutor OS for Brazilian legal-career exams. Do NOT ask the user to administrate the workflow. Do NOT write the next study chapter yet.

The current pilot is **Introdução ao Direito Penal**, but the target is **multi-career legal exams**, not Delegate-only:
- Delegado PF + estaduais
- Magistratura / ENAM
- Ministério Público
- Defensoria
- AGU / Procuradorias
- other legal careers when they add relevant evidence

## Current architectural commitments
1. Canonical entity = legal knowledge atom/proposition, not edital subtopic or Notion page.
2. Three synchronized views:
   - edital tree
   - pedagogical route
   - legal graph
3. Three spines:
   - conceptual/pedagogical
   - normative
   - evidentiary/exam
4. Six engines:
   - Knowledge Graph
   - Evidence Graph
   - Learner Model
   - Event Engine
   - Decision Engine
   - Presentation Layer
5. CORE legal vs LIVE legal.
6. Incidence must be auditable, never just HIGH/MEDIUM/LOW.
7. Question banks are discovery/commentary sources, not semantic ground truth.
8. Official source > official jurisprudence > official exam/key > doctrine > prep material.
9. Historical questions remain historical. Adapted questions must be explicitly marked.
10. No silent correction/merge of legacy material.

## Current user-facing editorial requirements
The user rejected prior MASTER pages as too technical/confusing.
Future study material must:
- be fluent and easy to learn from;
- be visually modular;
- use bold/semantic emphasis naturally;
- use strategic tables only when they help discrimination;
- use natural parenthetical reconnections without labels like “Retome:” or “Reconexão:”;
- integrate real questions progressively;
- be self-sufficient but not encyclopedic;
- include exactly what is needed to perform at high level, with minimal waste;
- keep architecture/governance hidden from the learner surface.

## Rejected / prototype pages
Do NOT treat these as valid MASTER:
- 03 — PILOTO REJEITADO | Penal · Fundamentos 001–003
- 04 — PILOTO REJEITADO | Penal · Dogmática, Criminologia, Política Criminal e Funções
- 05 — PILOTO REJEITADO | Penal · Teoria do Bem Jurídico
- “PILOTO EM AUDITORIA — 1. Conceito e Objeto do Direito Penal” is readable but insufficient, not approved.

## Canonical working files in GitHub
Read these first:
- governance/CURRENT_SESSION_POINTER_LEGAL_TUTOR_OS.json
- governance/LEGAL_TUTOR_OS_CHECKPOINT_2026-09-30.md
- governance/ARCHITECTURE_ADDENDUM_EVENT_DRIVEN_LEGAL_TUTOR_OS_2026-10-01.md
- research/CORPUS_COVERAGE_MANIFEST_2026-10-01.md
- research/PENAL_INTRO_MULTICAREER_AUDIT_V0_1.md
- research/PENAL_INTRO_QUESTION_CORPUS_SEED_V0_1.csv
- research/PENAL_INTRO_ALT_ASSERTION_MATRIX_V0_1.csv
- research/PENAL_INTRO_KNOWLEDGE_MAP_V0_1.md
- research/PENAL_INTRO_TERMINOLOGY_ALIAS_REGISTRY_V0_1.md
- research/QUESTION_QA_CONFLICT_LEDGER_V0_1.md
- research/SOURCE_REGISTRY_V0_1.md

## Notion working pages
Audit root:
https://app.notion.com/p/3ec42424cdbc8164b737f35ad5c9b28e

Knowledge map:
https://app.notion.com/p/3ec42424cdbc81829acece8a33db49c4

Alternative/distractor matrix:
https://app.notion.com/p/3ec42424cdbc81ff85befcbc50a5afa1

Question QA/conflict ledger:
https://app.notion.com/p/3ec42424cdbc81b48736c0086c4f9e89

Terminology/aliases:
https://app.notion.com/p/3ec42424cdbc81ca9a8ff1359bfc9c36

## Important current findings
- Current corpus is NOT exhaustive.
- PC-PI 2026 / FGV official questions have already been decomposed at alternative level:
  - Q42: insignificance + legality + minimum intervention + fragmentarity + dogmatic-level errors.
  - Q71: Classical School + Beccaria + free will + humanization/rationalization + legality.
  - Q72: minimalism + selectivity + analogy/legal limits; official key is disputed by expert commentary.
- TJPR 2026 / FGV Q32 shows one item can combine insignificance, adequacy social, fragmentarity, offensiveness and dogmatic-category errors.
- MPRJ 2026 shows foundational concepts reappear embedded in applied Penal cases.
- TJPE 2026 objective was published 29/09/2026 and must be included as fresh evidence.
- PC-DF 2026 was discovered only on a second freshness sweep, proving one-pass search is insufficient.
- “Subsidiariedade” has at least two distinct legal atoms:
  1. criminal-law intervention / ultima ratio
  2. apparent conflict of criminal norms
  These must be separated and linked by a homonym/confusion edge.
- Official sources themselves can conflict in metadata; do not normalize silently.

## Benchmarks to inspect/use
The user specifically wants the best ideas from:
- Dedicação Delta theoretical PDFs
- DD Legis / Mapa de Incidência
- Legislação Destacada
- old Estratégia PDFs/formatting
- current Estratégia LDI as a negative/positive benchmark
- user’s legacy Notion materials
- Magistrar/CÉREBRO architecture as a benchmark for curriculum/event orchestration, not an authority

Do not copy any benchmark blindly. Extract useful patterns and test them against exam evidence.

## Required next execution
Do this autonomously, in this order:

### A. Finish target-exam enumeration
For 2023-01-01 through 2026-10-01, enumerate relevant legal-career exams by:
- career
- bank
- year
- phase
- official source availability
- objective/discursive/oral

Run a SECOND adversarial freshness sweep for the last 60 days before calling the universe enumerated.

### B. Ingest the recent corpus first
Prioritize 2026, then 2025, 2024, 2023.
For each exam:
- locate official exam and official key;
- locate official discursive/oral materials where available;
- use QConcursos/TEC/Gran/Strategy comments only as discovery/adversarial commentary;
- semantically identify all items relevant to the Intro-Penal knowledge cluster even if site tags differ.

### C. Decompose at alternative/assertion level
For every relevant item record:
- exact exam identity
- phase
- source confidence
- knowledge atom(s)
- aliases/nomenclature
- author/doctrine
- statute/jurisprudence if applicable
- distractor mechanism
- official answer
- expert disagreement
- legal-state date
- defect/ambiguity status
- editorial implication

### D. Build/update the evidence graph
Continuously update:
- knowledge map
- aliases
- distractor taxonomy
- QA/conflict ledger
- source registry
- career overlays

### E. Reserve held-out
Before writing the next study unit, reserve a real held-out set not used to determine wording/depth.

### F. Only after A–E
Render ONE integrated study unit for **Introdução ao Direito Penal**.
It must be:
- fluent
- visually modular
- self-sufficient
- evidence-driven
- concise relative to the exam need
- capable of supporting objective + oral + discursive output
- free of engineering jargon on the learner surface

Then validate:
1. user readability
2. held-out exam sufficiency

## Do not
- do not claim exhaustive coverage until the manifest supports it;
- do not rewrite the study chapter prematurely;
- do not limit the corpus to PC-PI or Delegado;
- do not trust bank subject tags blindly;
- do not treat official key as doctrine when the item is controversial;
- do not build GitHub Actions/automation before the content/evidence model survives the pilot;
- do not ask the user what to do next unless a real authorization or missing credential blocks execution.

## Completion criterion for this Work run
Return with:
1. an updated coverage manifest;
2. the expanded deduplicated evidence corpus;
3. the alternative/assertion matrix;
4. the alias/confusion map;
5. the question QA/conflict ledger;
6. the career overlay map;
7. the reserved held-out set;
8. a readiness verdict: READY_TO_RENDER or NOT_READY_TO_RENDER;
9. if READY_TO_RENDER, produce the single integrated Intro-Penal study unit and validate it against held-out;
10. preserve every intermediate artifact in GitHub/Notion without overwriting legacy sources.
