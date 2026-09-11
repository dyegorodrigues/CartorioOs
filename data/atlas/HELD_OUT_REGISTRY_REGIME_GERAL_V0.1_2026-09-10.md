# GX Cartório OS — Held-Out Registry v0.7
## Regime Geral / Lei 8.935 / CNN

Snapshot: 2026-09-11
Status: ACTIVE VALIDATION REGISTRY. NÃO usar conteúdo reservado no BUILD.

## Regra
Registrar identidade/recorte **antes** de abrir conteúdo. Se fonte/caderno/versão não forem demonstráveis, o pool é inválido. Conteúdo visto antes do freeze vira contaminado.

## H1 — antigo TJSP locator
INVALID_LOCATOR / RETIRED. O PDF era TJAL/Vunesp 2023.

## H1R — Vunesp/TJSP2305
Página oficial confirmada; provas/gabaritos exigem login. Pendente locator verificável.

## H2 — Consulplan/TJMG 2024
PARKED: sem caderno utilizável nesta fase devido à suspensão/nulidade parcial.

## H3 — IESES/TJPA 2026
PARTIALLY_CONTAMINATED por uso prévio de questões iniciais.

## H4 — Future post-696 state exam
FUTURE_RESERVED: >=20% do primeiro concurso estadual integralmente publicado sob Res.696/2026.

## H5 — Vunesp/TJGO2001
PROVIMENTO v1 Q1–Q10 seladas; página/gabarito confirmados; caderno verificável ainda pendente.

## H6 — Cebraspe/TJRR 2025
CONSUMED / ALL OUT_OF_SCOPE para Regime Geral.

## H7 — Cebraspe/TJSC 2023
CONSUMED / IN-SCOPE FAILURE.
Q2 art.12 → MATERIAL_GAP.
Q3 art.36 → MATERIAL_GAP + DEPTH_GAP.
Q4 art.40 → MATERIAL_GAP.
Specimen v0.1 falhou S2 e foi patchado.

## H8 — Cebraspe/TJPE 2024 — SEALED BEFORE LOCATOR SEARCH
Criado após freeze do specimen v0.2 e **antes de pesquisar/abrir o caderno objetivo**.

Metadados conhecidos sem leitura do recorte:
- concurso: Tribunal de Justiça de Pernambuco, 2º Concurso Público para Outorga de Delegações de Notas e de Registro;
- banca: Cebraspe;
- edital/certame 2024;
- a frente BUILD já usou prova oral/prática do TJPE como CHALLENGE, mas **não usou a objetiva deste recorte para escrever o Regime Geral v0.2**.

### Recorte selado
- modalidade-alvo: **PROVIMENTO**;
- questões: **Q1–Q20**;
- objetivo: localizar itens de Regime Geral no bloco e confrontar com v0.2;
- questões de especialidades/constitucional/local serão OUT_OF_SCOPE;
- Q21+ permanecem fora desta rodada.

### Protocolo
1. localizar caderno oficial Cebraspe;
2. validar cabeçalho/modalidade;
3. abrir somente Q1–Q20;
4. localizar gabarito definitivo oficial;
5. classificar escopo/gaps;
6. jamais usar as questões consumidas para validar versão patchada posterior.

Status: `SEALED / READY_FOR_LOCATOR_SEARCH`.

## Build atual após H7
- `DEPTH_BUDGET_REGIME_GERAL_V0.3_2026-09-11.md`;
- `REGIME_GERAL_INTERNAL_FREEZE_V0.2_2026-09-11.md`.

## Gap taxonomy
MATERIAL_GAP / STRUCTURE_GAP / DEPTH_GAP / FRESHNESS_GAP / TRANSFER_GAP / OUT_OF_SCOPE / BAD_QUESTION / PROVENANCE_ERROR.

## Gate S2
S2 permanece NÃO ATINGIDO. H8 será o próximo teste limpo se o caderno/gabarito forem validados.

## Anti-leak
Não abrir H1R/H4/H5; em H8 não abrir Q21+ nesta rodada.
