# GX Cartório OS — Held-Out Registry v0.8
## Regime Geral / Lei 8.935 / CNN

Snapshot: 2026-09-11
Status: ACTIVE VALIDATION REGISTRY. NÃO usar conteúdo reservado no BUILD.

## Regra
Registrar identidade/recorte antes de abrir conteúdo. Qualquer questão exibida por snippet de busca antes da abertura formal deixa de ser held-out independente.

## Pools anteriores
- H1 antigo TJSP locator: `INVALID_LOCATOR / RETIRED` (era TJAL/Vunesp 2023).
- H1R TJSP2305: `PENDING_VERIFIED_LOCATOR`.
- H2 TJMG/Consulplan: `PARKED`.
- H3 TJPA/IESES: `PARTIALLY_CONTAMINATED`.
- H4 primeiro pós-696 integral: `FUTURE_RESERVED`.
- H5 TJGO/Vunesp: `SEALED / PENDING_QUESTION_BOOK_LOCATOR`.
- H6 TJRR/Cebraspe: `CONSUMED / ALL OUT_OF_SCOPE`.
- H7 TJSC/Cebraspe: `CONSUMED / IN-SCOPE FAILURE`; specimen v0.1 falhou S2 e foi patchado para v0.2.

## H8 — Cebraspe/TJPE 2024 — RECUT AFTER LOCATOR SEARCH
H8 original foi selado como PROVIMENTO Q1–Q20 antes de qualquer busca do caderno.

A busca de locator localizou caderno oficial Cebraspe:
`https://cdn.cebraspe.org.br/concursos/tj_pe_24_notarios/arquivos/005_TJPE_001_01.PDF`

Porém o mecanismo de busca exibiu automaticamente texto de Q1, Q2, Q4, Q5 e Q6 antes da abertura formal. Para evitar autoengano:
- Q1–Q6 passam a `CONTAMINATED_BY_LOCATOR_SNIPPET`;
- nenhuma delas poderá validar v0.2, mesmo que Q1 seja claramente Regime Geral;
- antes de abrir o restante, o pool limpo é recortado novamente.

### Recorte limpo H8R
- concurso: TJPE 2º Concurso, Cebraspe, 2024;
- caderno oficial já validado pelo cabeçalho;
- modalidade: PROVIMENTO;
- questões limpas seladas agora: **Q7–Q20**;
- Q21+ continuam fora desta rodada;
- objetivo: identificar itens Regime Geral e confrontar com `REGIME_GERAL_INTERNAL_FREEZE_V0.2`.

### Protocolo H8R
1. abrir apenas Q7–Q20;
2. localizar gabarito definitivo oficial;
3. classificar cada questão em IN_SCOPE / OUT_OF_SCOPE;
4. para IN_SCOPE, mapear proposition ID e cobertura do specimen v0.2;
5. registrar gap sem editar retroativamente o freeze;
6. se houver patch, reteste posterior usa outro pool limpo.

Status H8: `Q1–Q6 CONTAMINATED; H8R Q7–Q20 SEALED / READY`.

## Build atual
- `DEPTH_BUDGET_REGIME_GERAL_V0.3_2026-09-11.md`;
- `REGIME_GERAL_INTERNAL_FREEZE_V0.2_2026-09-11.md`.

## Gap taxonomy
MATERIAL_GAP / STRUCTURE_GAP / DEPTH_GAP / FRESHNESS_GAP / TRANSFER_GAP / OUT_OF_SCOPE / BAD_QUESTION / PROVENANCE_ERROR.

## Gate S2
S2 permanece NÃO ATINGIDO. Apenas questões IN_SCOPE limpas de H8R podem contribuir para o reteste.

## Anti-leak
Não abrir H1R/H4/H5; em TJPE não abrir Q21+ nesta rodada.
