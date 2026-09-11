# GX Cartório OS — Held-Out Registry v0.10
## Regime Geral / Lei 8.935 / CNN

Snapshot: 2026-09-11
Status: ACTIVE VALIDATION REGISTRY. NÃO usar conteúdo reservado no BUILD.

## Regra
Registrar identidade/recorte antes de abrir conteúdo. Questão exibida por snippet ou retorno ampliado de ferramenta antes de reserva formal deixa de ser held-out independente.

## Pools encerrados/pendentes
- H1 antigo TJSP locator: `INVALID_LOCATOR / RETIRED` (era TJAL/Vunesp 2023).
- H1R TJSP2305: `PENDING_VERIFIED_LOCATOR`.
- H2 TJMG/Consulplan: `PARKED`.
- H3 TJPA/IESES: `PARTIALLY_CONTAMINATED`.
- H4 primeiro pós-696 integral: `FUTURE_RESERVED`.
- H5 TJGO/Vunesp: `SEALED / PENDING_QUESTION_BOOK_LOCATOR`.
- H6 TJRR/Cebraspe: `CONSUMED / ALL OUT_OF_SCOPE`.
- H7 TJSC/Cebraspe: `CONSUMED / IN-SCOPE FAILURE`; v0.1 falhou S2 e foi patchado.
- H8 TJPE/Provimento: `CONSUMED / ALL OUT_OF_SCOPE OR ADJACENT` após recorte limpo Q7–Q20.

## H9 — Cebraspe/TJPE 2024 REMOÇÃO — CONSUMED
Recorte Q1–Q6 foi selado antes da busca do caderno. Caderno oficial validado:
`https://cdn.cebraspe.org.br/concursos/tj_pe_24_notarios/arquivos/005_TJPE_002_01.PDF`

Gabarito definitivo oficial Q1–Q6: C, C, D, A, A, B.

### Resultado
- **Q1 — independência do delegatário x fiscalização judicial** → IN_SCOPE e materialmente independente da prova de provimento. O specimen v0.2 ensina independência, titular como gestor e fiscalização judicial; a alternativa correta decorre diretamente da combinação desses átomos. `COVERED / TRANSFER EXPECTED / PASS`.
- Q2 assinatura eletrônica → OUT_OF_SCOPE/cross-system.
- Q3 fusão/reorganização local PE → OUT_OF_SCOPE/STATE OVERLAY.
- Q4–Q6 notas/escrituras/testamento → OUT_OF_SCOPE/especialidade.

### Evento de ferramenta
Ao localizar Q6, o retorno expandido exibiu também Q7–Q29. Como esses itens não estavam no recorte H9, não afetam a validade de Q1–Q6, mas **Q7–Q29 do mesmo caderno ficam contaminadas para qualquer futuro held-out**.

Conclusão: v0.2 obteve **1 PASS in-scope independente**, insuficiente sozinho para S2.

Status: `CONSUMED / 1 IN-SCOPE PASS / INSUFFICIENT DIVERSITY`.

## H10 — Cebraspe/TJMT 2024/2025 — SEALED BEFORE LOCATOR SEARCH
Criado antes de qualquer busca de caderno/questões TJMT no web desta rodada.

Pré-checagem interna do repositório: nenhuma questão TJMT apareceu no BUILD atual do Regime Geral.

Metadados conhecidos:
- Tribunal de Justiça de Mato Grosso;
- concurso de outorga de delegações notariais/registro recente, banca Cebraspe;
- concurso listado na frente histórica/market census, sem uso de questões no specimen v0.2.

### Recorte selado
- modalidade-alvo: **PROVIMENTO**;
- questões: **Q1–Q20**;
- finalidade: buscar itens de Regime Geral independentes do BUILD e de TJSC/TJPE;
- especialidades/local serão OUT_OF_SCOPE;
- se busca de locator exibir parte do conteúdo, recortar novamente ANTES de abrir o restante.

Status: `SEALED / READY_FOR_LOCATOR SEARCH`.

## Build atual
- `DEPTH_BUDGET_REGIME_GERAL_V0.3_2026-09-11.md`;
- `REGIME_GERAL_INTERNAL_FREEZE_V0.2_2026-09-11.md`.

## Gap taxonomy
MATERIAL_GAP / STRUCTURE_GAP / DEPTH_GAP / FRESHNESS_GAP / TRANSFER_GAP / OUT_OF_SCOPE / BAD_QUESTION / PROVENANCE_ERROR / DUPLICATE_NOT_INDEPENDENT.

## Gate S2
S2 permanece NÃO ATINGIDO. Evidência limpa atual para v0.2: H9-Q1 = PASS. Precisamos diversidade adicional.

## Anti-leak
Não abrir H1R/H4/H5. Em H10 não abrir Q21+ nesta rodada.
