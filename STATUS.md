# GX Cartório OS — Estado Atual

Atualizado em 10/09/2026 22:40 BRT.

## Branch / handoff HOT
- branch: `chatgpt/gx-cartorio-v0.1`
- ler primeiro: `handoff/NEXT_SESSION_POINTER_2026-09-10.md`

## Missão canônica
Levar candidato com conhecimento jurídico enferrujado/próximo de zero até **prontidão verificável para ENAC + concurso estadual + discursiva + peça prática + oral**, horizonte 2027–2028, com eficiência extrema e administração manual mínima.

## Constraint autoral HOT
**NÃO INICIAR ESTUDO AINDA.** Usuário autorizou execução autônoma. Não entregar Missão 01, não atribuir mastery, não pedir microdecisões.

## Work Order A — CONCLUÍDO / CONGELADO
`material/EDITORIAL_STANDARD.md`.
Preservar M0–M7, retention separado, objetiva permanente, output progressivo por pertinência de fase, voz como recall, lei seca guiada, Q→A/flashcards seletivos, revisão cumulativa, throughput adaptativo, One-Home Rule, Sufficiency Gate e Freshness Firewall.

## Baseline regulatório
Res. CNJ 696/2026: https://atos.cnj.jus.br/atos/detalhar/7011

- objetiva estadual: eliminatória/sem peso final quando aplicada e substituível por ENAC conforme regime;
- discursiva 70%; oral 25%; títulos 5%;
- Penal, PP, Trabalho e PTrab = exclusivamente ENAC/objetiva no baseline nacional atual;
- oral novo: pergunta escrita/predefinida, reperguntas guiadas, 90% conteúdo jurídico + 10% articulação técnica.

Toda prova histórica recebe `REGIME_TAG`, `CONTENT_VALIDITY`, `PHASE_VALIDITY`.

## Freshness Firewall — avanço crítico
Arquivo HOT: `research/CNN_CNJ_FRESHNESS_DELTA_MAP_2026-09-10.md`.

O CNN/Provimento 149 é corpus versionado. Foram mapeados deltas 2026 relevantes (Prov. 211, 212, 214, 217, 218, 219, 220, 224, 225, 227, 228, 229, 237, 242, 246, 253).

### ENAC 2026.2 — regra de snapshot
Edital FGV/CNJ prevê prova em 22/11/2026 e exclui preceitos cuja vigência tenha iniciado menos de 90 dias antes; preceitos revogados no período podem ser cobrados.
Cutoff aritmético = **24/08/2026**, sempre pela data de VIGÊNCIA, não publicação.

O sistema agora distingue:
`CURRENT_LAW` x `EXAM_SNAPSHOT_LAW`.

Criado `data/freshness/CHANGE_IMPACT_QUEUE_2026-09-10.md` para cascata:
`mudança → proposições → snapshot de prova → MASTER/REVIEW/Q→A/questões/simulados/output`.

## Compiler invisível
`OFFICIAL SCOPE → SOURCES → EXAM CORPUS → PROPOSITIONS → INCIDENCE/CONSEQUENCE → DEPTH BUDGET → CANONICAL TREE → BUILD/VALIDATION/CHALLENGE → FRESHNESS → PATCH`.

Learner-facing futuro:
`MAP → MASTER P1 → LEI SECA GUIADA → REVIEW → Q→A → OBJECTIVE LAB → OUTPUT LAB`.

## Suficiência
S0 untested → S1 build → S2 held-out → S3 challenge/multibanca → S4 learner-demonstrated → S5 maintenance-stable.
Nunca prometer `resolve qualquer questão futura`.

## Specimens
- Penal/PEN1 v0.2 = congelado como protótipo visual; NÃO estudar.
- Specimen B = adiado.
- Próximo learner-facing só depois de Atlas + held-out + Depth Budget.

## Market audit
`research/CARTORIO_PREP_ECOSYSTEM_DEEP_AUDIT_2026_09_10.md`.
Auditados VFK, Estratégia, Registrando/CP Iuris, Themas, Decorando Lei Seca, PreparaEnac, YK e Juspodivm. Absorver funções, não copiar produtos.

## Cartório Exam Atlas — estado
Protocolo: `research/CARTORIO_EXAM_ATLAS_PROTOCOL_2026.md`.

### Waves 1–5
- Wave1: censo contemporâneo multibanca.
- Wave2: TJMS/FGV gold corpus cross-phase.
- Wave3: TJBA/Cebraspe e transição regulatória.
- Wave4: ENAC/Lei 8.935 first pass.
- Wave5: FGV x Cebraspe OUTPUT; regra `KNOWLEDGE_ATOMS ≠ BANK/EDITAL_PACKAGING`.

### Wave6 — Regime Geral heatmap
`research/CARTORIO_EXAM_ATLAS_WAVE6_REGIME_GERAL_HEATMAP_2026-09-10.md`.

Além de ENAC/FGV/Cebraspe, o corpus foi ampliado com:
- IESES/TJPA 2026, prova + gabarito oficiais;
- Vunesp/TJSP 13º concurso, prova oficial;
- sinais de Consulplan/TJMG preservados para ampliar/held-out quando o caderno oficial for localizado.

Sinais multibanca fortes em Regime Geral:
- ingresso arts.14–15;
- prepostos/gestão arts.20–21;
- responsabilidade arts.22–24 + Tema777;
- impedimento art.27;
- direitos/deveres arts.29–30;
- disciplina/perda arts.31–36.

IESES/PA 2026 Q10 + gabarito oficial reforça art.22. Vunesp/SP recente testa em sequência ingresso, prepostos, gestão e responsabilidade da Lei 8.935.

## Ledgers
### Lei 8.935 / Regime Geral
`data/atlas/PROPOSITION_LEDGER_REGIME_GERAL_SEED_2026-09-10.md`
Agora C0 + C1/C2 multibanca.

### CNN/CNJ / Regime Geral
`data/atlas/PROPOSITION_LEDGER_CNN_REGIME_GERAL_SEED_2026-09-10.md`
Inclui Justiça Aberta, vacâncias, incapacidade permanente e solvência trabalhista.

### LRP
`data/atlas/PROPOSITION_LEDGER_LRP_SEED_2026-09-10.md`
Aberto com prenotação, qualificação, usucapião, indisponibilidade, retificação, RTD, sistemas eletrônicos, extratos, Constrijud e alienação fiduciária.

## Primeiro Depth Budget formal
`data/atlas/DEPTH_BUDGET_REGIME_GERAL_V0.1_2026-09-10.md`.

Arquitetura pedagógica v0.1:
`RG0 natureza/CF236 → RG1 ingresso → RG2 gestão/prepostos → RG3 responsabilidade → RG4 incompatibilidades/impedimentos → RG5 independência/direitos/deveres → RG6 disciplina/perda/extinção → RG7 vacância/interinidade + CNN`.

Budget separa P1/P2/P3+, MUST-KNOW literal, MUST-UNDERSTAND, output e podas. Confiança global B+; aprovado para continuar pesquisa, NÃO para estudo.

## Regra de questões
- Encoding Check = imediato, não mastery.
- Assessment = atrasado/misturado.
- Held-out = fora do build, testa material.
- Challenge = outra banca/formulação/cross-node.

## Próximo HOT autônomo
1. formalizar reserva HELD-OUT por banca/cluster antes de qualquer specimen N/R;
2. terminar heatmap do art.30 por inciso e expandir Vunesp/IESES/Consulplan;
3. aprofundar LRP C0/C1 e separar RI/RTD/RCPN quando densidade justificar;
4. preencher `EFFECTIVE_FROM` dos deltas CNN e ligar questões impactadas no Change Impact Queue;
5. criar primeiro `BUILD CORPUS vs HELD-OUT CORPUS` de Regime Geral;
6. fazer red-team do Depth Budget v0.1;
7. somente então construir primeiro specimen N/R learner-facing.

## Anti-drift
Não iniciar aula; não usar cursinho/material legado como cânone; não importar frequência de OAB/Delegado; não usar prova antiga sem revalidação; não transformar páginas/horas em KPI; não fabricar specimen antes de held-out; não exigir microgestão do usuário.