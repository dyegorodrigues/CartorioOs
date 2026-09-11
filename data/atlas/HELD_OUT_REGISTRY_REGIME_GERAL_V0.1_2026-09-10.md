# GX Cartório OS — Held-Out Registry v0.12
## Regime Geral / Lei 8.935 / CNN

Snapshot: 2026-09-11
Status: ACTIVE VALIDATION REGISTRY. NÃO usar conteúdo reservado no BUILD.

## Regra
Registrar identidade/recorte antes de abrir conteúdo. Questão exibida por snippet ou retorno ampliado de ferramenta antes de reserva formal deixa de ser held-out independente. **S2 exige fonte de questão/gabarito suficientemente verificável; banco secundário sozinho não substitui caderno oficial quando este não foi localizado.**

## Pools encerrados/pendentes
- H1 antigo TJSP locator: `INVALID_LOCATOR / RETIRED` (era TJAL/Vunesp 2023).
- H1R TJSP2305: `PENDING_VERIFIED_LOCATOR`.
- H2 TJMG/Consulplan: `PARKED`.
- H3 TJPA/IESES: `PARTIALLY_CONTAMINATED`.
- H4 primeiro pós-696 integral: `FUTURE_RESERVED`.
- H5 TJGO/Vunesp: `SEALED / PENDING_QUESTION_BOOK_LOCATOR`.
- H6 TJRR/Cebraspe: `CONSUMED / ALL OUT_OF_SCOPE`.
- H7 TJSC/Cebraspe: `CONSUMED / IN-SCOPE FAILURE`; v0.1 falhou S2 e foi patchado.
- H8 TJPE/Provimento: `CONSUMED / ALL OUT_OF_SCOPE OR ADJACENT`.
- H9 TJPE/Remoção: `CONSUMED / 1 IN-SCOPE PASS`.
- H10 TJMT/Cebraspe: `PARKED / NO USABLE QUESTION BOOK LOCATED`.

## H11 — IESES/TJTO 2022 — PARKED AS SECONDARY DISCOVERY
H11 foi selado antes da busca web. A pesquisa confirmou oficialmente no TJTO:
- concurso 2022;
- banca IESES;
- 34 vagas de provimento + 17 de remoção.

Foi localizada página de prova no QConcursos e uma reprodução do caderno em fonte secundária. A busca exibiu trechos de algumas questões, inclusive material N/R, antes que um caderno oficial IESES/TJTO pudesse ser localizado.

### Consequência
- o concurso permanece útil como **DISCOVERY/CHALLENGE multibanca**;
- não será usado como prova S2 enquanto não houver caderno/gabarito oficial ou reprodução com proveniência forte verificável;
- recorte Q1–Q20 deixa de ser held-out limpo por exposição parcial nos resultados de busca.

Status: `PARTIALLY CONTAMINATED / SECONDARY-ONLY / NOT S2`.

## Build atual
- `DEPTH_BUDGET_REGIME_GERAL_V0.3_2026-09-11.md`;
- `REGIME_GERAL_INTERNAL_FREEZE_V0.2_2026-09-11.md`.

## Evidência limpa atual para v0.2
- H9-Q1 = `PASS IN_SCOPE`.
- Ainda insuficiente para S2.

## Gap taxonomy
MATERIAL_GAP / STRUCTURE_GAP / DEPTH_GAP / FRESHNESS_GAP / TRANSFER_GAP / OUT_OF_SCOPE / BAD_QUESTION / PROVENANCE_ERROR / DUPLICATE_NOT_INDEPENDENT.

## Gate S2
S2 permanece **NÃO ATINGIDO**. Não baixar o padrão só porque locators antigos são difíceis. Preferir esperar/localizar corpus oficial adicional a fingir validação independente.

## Anti-leak
Não abrir H1R/H4/H5. Próximo pool deve ser registrado antes da pesquisa do caderno.
