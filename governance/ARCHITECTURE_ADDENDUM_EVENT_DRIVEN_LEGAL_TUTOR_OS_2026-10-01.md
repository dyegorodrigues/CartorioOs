# ARCHITECTURE ADDENDUM — EVENT-DRIVEN LEGAL TUTOR OS
**Date:** 2026-10-01
**Source:** recovered prior-conversation architecture analysis supplied by user
**Status:** adopted as design input; current-product claims about third-party systems remain benchmark evidence, not authority

## Why this changes the project
The system is not only:
knowledge graph + MASTER + questions + scheduler.

It must also maintain an explicit **event-driven learning state** so every learner action can change the next decision.

## 1. Canonical entity
The canonical unit is NOT:
- edital subtopic;
- Notion page;
- PDF chapter;
- article of law;
- flashcard.

The canonical unit is the **legal knowledge atom / proposition / concept**.

Examples of views pointing to the same object:
- edital item;
- statute article;
- question;
- revision queue;
- bank profile;
- error ledger;
- oral/discursive production;
- flashcard;
- search.

## 2. Six engines

### 2.1 Knowledge Graph
Concepts, propositions, statutes, precedents, doctrines, exceptions, authors and relations.

### 2.2 Evidence Graph
Real questions → required knowledge → distractors → bank → career → phase → date → legal state.

### 2.3 Learner Model
Mastery, confidence, speed, confusions, forgetting, production ability, recurrence of errors.

### 2.4 Event Engine
Possible event vocabulary:
- READ
- ANSWERED
- CORRECT_CONFIDENT
- CORRECT_UNCERTAIN
- WRONG_CONCEPT
- WRONG_EXCEPTION
- WRONG_READING
- RECALLED
- FAILED_RECALL
- EXPLAINED_ORALLY
- FAILED_ORAL
- REVIEWED_LAW
- CREATED_NOTE
- JUDGMENT_UPDATED

Events update learner state; pages do not.

### 2.5 Decision Engine
Chooses the next action using:
- edital coverage;
- exam date / macro clock;
- mastery;
- forgetting risk;
- incidence evidence;
- error type;
- available time;
- learner speed by task type.

### 2.6 Presentation Layer
MASTER, statute view, precedent view, questions, flashcards, maps, summaries, oral/discursive and ESTUDAR AGORA are views over the same knowledge/evidence state.

## 3. Two-speed legal knowledge

### CORE legal
Slow-changing, consolidated, audited:
- concepts;
- structures;
- settled doctrine where needed;
- stable statutory propositions;
- consolidated precedents.

### LIVE legal
Hot incoming events:
- new statute/amendment;
- new STF/STJ precedent;
- informativo;
- overruling/distinguishing;
- new exam/question;
- new edital.

A LIVE event never silently rewrites CORE.

Pipeline:
NEW_EVENT → link to affected atoms → classify impact → verify official source → decide confirm/change/exception/supersede → patch CORE → retain historical state.

## 4. Multiple routes, single object
One legal proposition can be reached through:
- curriculum;
- statute;
- bank;
- revision;
- errors;
- oral/discursive;
- search;
- daily queue.

No semantic duplication merely because the view changes.

## 5. Incidence must be auditable
Never store only:
HIGH / MEDIUM / LOW.

Store the evidence behind the label:
- career;
- bank;
- time window;
- number of relevant questions;
- direct vs indirect;
- objective/discursive/oral;
- literal/statute;
- doctrine;
- jurisprudence;
- case/inference;
- last observed occurrence;
- sample size;
- confidence;
- source links / question IDs.

Incidence is a query over evidence, not an editorial opinion.

## 6. Personal time model
Do not estimate study workload by generic page counts.

Learn personal rates for:
- dense theory;
- familiar theory;
- statute;
- new statute;
- easy questions;
- complex FGV/Cebraspe questions;
- precedent review;
- oral production;
- discursive production.

Planning progressively shifts from guessed time to measured personal time.

## 7. Notes as structured evidence
A learner note can signal cognition.

Example:
“confundo fragmentariedade com subsidiariedade”

Possible structured consequence:
- attach note to both atoms;
- create confusion edge;
- schedule future contrast;
- prioritize discriminative questions.

Notes are not merely text storage.

## 8. Production from the beginning
Objective and production are parallel dimensions of mastery.

Progression:
- explain in 1–2 sentences;
- 60-second oral answer;
- short structured answer;
- timed discursive;
- full practical/oral performance when relevant.

## 9. Negative requirements learned from benchmarks
Do NOT:
- turn 5,000 subtopics into templated AI mini-articles;
- use unauditable “high incidence” labels;
- make the learner integrate PDFs, statutes, questions and jurisprudence manually;
- silently overwrite historical law/question states;
- duplicate the same knowledge under multiple edital headings;
- create infinite schedule debt after missed days.

## 10. Transparent decision queue
ESTUDAR AGORA should eventually show:
- exact next task;
- estimated personal time;
- why this task now;
- what evidence triggered it;
- clear stop condition.

Example:
AGORA · 24 min
Legalidade penal · lex stricta vs lex scripta
Why:
- 2/4 errors;
- one high-confidence wrong answer;
- last successful recall 11 days ago;
- recurrent in current target corpus.
Do:
2 min recall → 7 min repair → 6 questions → 1 oral explanation.

## 11. Implication for current Penal pilot
Do not model “Introdução ao Direito Penal” merely as a page.
Model:
- knowledge atoms;
- evidence links;
- statute links;
- question links;
- production atoms;
- aliases;
- learner-event hooks;
then render a fluent study page from that model.

## 12. Current architecture formula
**Magistrar-style verticalized curriculum insight**
+ **knowledge graph**
+ **evidence graph**
+ **learner model**
+ **event engine**
+ **decision engine**
+ **presentation layer**
+ **Legal LIVE pipeline**
= Legal Tutor OS.

## 13. Current order of execution
1. finish corpus coverage manifest for Penal intro;
2. decompose questions at alternative/assertion level;
3. build proposition graph + aliases + distractors;
4. identify CORE vs overlay by career;
5. reserve held-out;
6. only then render the first study unit;
7. instrument it conceptually for event/state tracking;
8. postpone heavy automation/GitHub Actions until the content model survives user study + held-out validation.
