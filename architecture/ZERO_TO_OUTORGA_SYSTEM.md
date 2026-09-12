# GX Cartório OS — Zero to Outorga System

Status: architecture v0.1

## Mission
Prepare a candidate from rusty or near-zero operational knowledge to competitive mastery for Brazilian notarial and registry delegations under the current national framework, without forcing separate study systems for ENAC, objective state exams, discursive exams, practical pieces and oral exams.

The system optimizes for **verified legal mastery under exam constraints**, not hours watched, pages consumed or number of PDFs completed.

## Core design principle
**One legal knowledge base, four performance renderers.**

A canonical knowledge unit is authored once and then exercised as:
1. objective recognition/discrimination;
2. written analytical production;
3. practical/procedural production;
4. oral retrieval and defense.

## Layer 1 — Target model
Maintain a versioned representation of:
- current ENAC rules and syllabus;
- current CNJ national contest framework;
- target-state overlays;
- organizer/bank profiles by period and exam family;
- historical matrix drift;
- phase weights and admissible consultation materials.

No study priority is valid without identifying the target version.

## Layer 2 — Canonical curriculum graph
Represent the official syllabus completely, then enrich it only at useful granularity.

Hierarchy for navigation:
`Matéria → Tema → Subtema → Microtema`

Cross-links for reasoning:
- prerequisites;
- sibling distinctions;
- statutes and regulatory acts;
- jurisprudence;
- professional procedure;
- question clusters;
- state overlays;
- phase outputs;
- learner errors.

The tree is a map. The graph is the system.

## Layer 3 — Source-of-truth legal model
Each examinable proposition should eventually have:
- statement of rule;
- scope;
- prerequisites/elements;
- exception(s);
- legal effect;
- authority;
- historical snapshot;
- current snapshot;
- freshness status;
- controversy flag when relevant.

Primary authority dominates secondary commentary.

## Layer 4 — Question Intelligence
Questions are evidence, not merely exercises.

For each item capture when available:
- exam, year, bank and phase;
- stem architecture;
- microtopic(s);
- source family;
- official answer/mirror;
- alternative-by-alternative reasoning;
- distractor mechanism;
- cognitive demand;
- interdisciplinarity;
- normative freshness;
- annulment/resource history;
- relation to other semantically similar items;
- target adherence;
- learner outcome, confidence and latency.

### Corpus hierarchy
A. current/direct ENAC or target-state exam;
B. same domain + same bank;
C. same microtopic + same bank in high-level legal careers;
D. cartório + other major bank;
E. same microtopic + other high-quality legal exams;
F. GX synthetic, only after grounding and validation.

Low-complexity questions may serve foundation drills but never redefine the high-level bank model.

## Layer 5 — Bank Intelligence
Profile banks as time-sensitive distributions, not personalities.

Measure:
- case density;
- stem length;
- literal-law vs application;
- jurisprudential load;
- use of regulatory acts;
- novelty/recency of legal sources;
- distractor mechanisms;
- interdisciplinarity;
- negative-command frequency;
- ambiguity/annulment patterns;
- discursive mirror structure;
- practical-piece expectations;
- oral question/re-question structure when evidence exists.

Compare by period and exam family. Never infer AI authorship from style alone.

## Layer 6 — Material architecture
Every important knowledge cluster can generate six interfaces:

### MAP
Orientation: what exists, why it matters and how it connects.

### MASTER
Full study material at exam-appropriate depth.

### REVIEW
High-density revision material.

### RECALL
Active-retrieval prompts, flashcards, oral prompts and reconstruction tasks.

### EXAM
Official questions, cases, discursive prompts, practical pieces and simulations.

### REFERENCE
Deep doctrine, historical context, long jurisprudential notes and source excerpts that are useful but should not block the main learning path.

## Layer 7 — Pedagogical progression
For a new cluster:
1. orientation map;
2. prerequisite check;
3. minimal conceptual foundation;
4. worked legal example;
5. short retrieval;
6. immediate question/case;
7. feedback and error classification;
8. second retrieval from memory;
9. spaced revisit;
10. interleaved discrimination against similar institutes;
11. phase conversion to discursive/practical/oral when relevance justifies it.

Avoid passive marathons. Retrieval is interspersed during learning, not postponed until the end of a giant module.

## Layer 8 — Error-driven adaptation
Wrong answers are classified, not merely counted.

Possible causes include:
- missing concept;
- forgotten rule;
- exception failure;
- confusion between nearby institutes;
- outdated law;
- reading error;
- attention error;
- weak issue spotting;
- weak legal organization;
- practical-procedure gap;
- oral retrieval failure;
- time-pressure failure.

Each cause maps to a different intervention.

## Layer 9 — Mastery thresholds
A topic is not mastered because it was read.

Evidence ladder:
M0 — unseen;
M1 — can recognize with support;
M2 — can retrieve core rule without support;
M3 — can discriminate from close alternatives;
M4 — can solve a novel objective/case problem;
M5 — can produce a legally complete written answer;
M6 — can execute practical/procedural output where applicable;
M7 — can explain and defend orally under time/re-questioning.

Not every topic needs M7. Phase relevance determines target threshold.

## Layer 10 — Daily scheduler
Daily study is selected from evidence, not a static calendar.

Inputs:
- exam proximity;
- syllabus weight;
- bank adherence;
- prerequisite readiness;
- learner mastery;
- forgetting risk;
- recent errors;
- freshness risk;
- cross-phase transfer;
- available time/energy.

Typical daily packet:
- 3–5 min orientation/retrieval warm-up;
- 20–40 min new learning;
- embedded retrieval/questions;
- 15–30 min old-node review or error repair;
- short phase-output task on selected days;
- automatic logging and next-review scheduling.

The packet size adapts to real performance.

## Layer 11 — Weekly and monthly control
### Weekly
- coverage gained;
- retention stability;
- error recurrence;
- accuracy by bank/microtopic;
- confidence calibration;
- discursive/oral output quality;
- bottleneck detection;
- load adjustment.

### Monthly
- full mixed simulation appropriate to current stage;
- curriculum-gap audit;
- bank-profile refresh;
- freshness audit;
- forecast update;
- material refactoring when the data show that an explanation or sequence is inefficient.

## Layer 12 — Phase preparation
### Objective / ENAC
Prioritize speed, discrimination, issue spotting, current law and bank calibration.

### Discursive
Train answer decomposition into scoring atoms because current national rules require analytical expected-answer points. Build from microdiscursives early rather than starting only after objective approval.

### Practical piece
Train procedural identification, legal instrument selection, structure, legal basis, order of acts and consultation navigation under permitted materials.

### Oral
Train retrieval without writing, concise opening answers, structured expansion, handling follow-up questions and technical articulation.

## Layer 13 — Consultation-material fluency
Because current national rules allow restricted legal-material consultation in the discursive stage, the candidate must develop navigation fluency in allowed statutes/acts rather than treating the vade mecum as an emergency crutch.

Train:
- source selection;
- index navigation;
- remissions;
- time-to-find;
- when not to consult;
- converting located text into scored legal reasoning.

## Layer 14 — Predictive analytics with calibration
Forecasts may estimate:
- probability of clearing a threshold;
- expected score range;
- weak-node contribution to risk;
- likely forgetting before target date;
- marginal gain from an extra hour on a node;
- readiness by output mode.

Predictions must carry confidence and be recalibrated against actual simulations. No deterministic 'chance to fall' claims from tiny samples.

## Layer 15 — Quality gates
No material becomes canonical unless:
- linked to current target curriculum or justified prerequisite;
- legally sourced;
- freshness checked;
- depth appropriate to phase;
- explanation has a clear learning purpose;
- question evidence is provenance-labeled;
- unresolved controversies are disclosed;
- synthetic content is explicitly labeled.

## Final objective
The candidate should eventually be able to look at any relevant fact pattern and do four things from the same internal knowledge graph:
1. identify the legal issue;
2. select and justify the correct rule;
3. execute the appropriate notarial/registry or exam response;
4. explain the reasoning clearly under time pressure.

That is the operational definition of preparation for outorga, not completion of a course library.
