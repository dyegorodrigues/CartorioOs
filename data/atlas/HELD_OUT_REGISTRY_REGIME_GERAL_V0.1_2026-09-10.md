# GX Cartório OS — Held-Out Registry v0.6
## Regime Geral / Lei 8.935 / CNN

Snapshot: 2026-09-11
Status: ACTIVE VALIDATION REGISTRY. NÃO usar conteúdo reservado no BUILD.

## Regra
Registrar identidade/recorte **antes** de abrir conteúdo. Se fonte/caderno/versão não forem demonstráveis, o pool é inválido. Se conteúdo reservado for visto antes do freeze, marcar contaminado e substituir.

## Incident H1 — locator incorreto
O antigo `H1 — Vunesp/TJSP 13º Concurso, Prova 04 Q5–Q15` foi invalidado porque o locator era TJAL/Vunesp 2023.

Status: `INVALID_LOCATOR / RETIRED`.

## H1R — Vunesp/TJSP 13º Concurso
- código oficial: TJSP2305;
- página oficial confirmada;
- provas/gabaritos exigem login;
- nenhum PDF externo será promovido sem cabeçalho verificável.

Status: `PENDING_VERIFIED_LOCATOR`.

## H2 — Consulplan/TJMG Edital 1/2024
Concurso suspenso/nulo em parte antes de produzir caderno utilizável para esta validação.

Status: `NO_USABLE_EXAM_YET / PARKED`.

## H3 — IESES/TJPA 2026
Questões iniciais já expostas/BUILD.

Status: `PARTIALLY_CONTAMINATED`.

## H4 — Future post-696 state exam
Reservar automaticamente >=20% do primeiro concurso estadual integralmente publicado sob Res.696/2026.

Status: `FUTURE_RESERVED`.

## H5 — Vunesp/TJGO2001
- página oficial/gabarito oficial confirmados;
- PROVIMENTO versão 1 Q1–Q10 seladas;
- caderno público verificável ainda não localizado.

Status: `SEALED / PENDING_QUESTION_BOOK_LOCATOR`.

## H6 — Cebraspe/TJRR 2025 — CONSUMED / OUT OF SCOPE
Q5–Q10 foram seladas e abertas legitimamente. Todas recaíram em especialidades fora do specimen Regime Geral; Q10 foi anulada.

Resultado: não aprova nem reprova Regime Geral.

Status: `CONSUMED / ALL OUT_OF_SCOPE`.

## H7 — Cebraspe/TJSC 2023 — CONSUMED / FAILED S2
Recorte foi selado ANTES de localizar o caderno:
- PROVIMENTO;
- Q1–Q20;
- caderno oficial Cebraspe `719_TJSCPROVIMENTO_001_01.PDF`;
- gabarito definitivo oficial identificado.

### Resultado in-scope
- **Q2 — circunscrição territorial, art.12** → `MATERIAL_GAP`;
- **Q3 — art.36, afastamento preventivo/interventor/renda** → `MATERIAL_GAP + DEPTH_GAP`;
- **Q4 — art.40, previdência/contagem recíproca** → `MATERIAL_GAP`.

Demais Q1/Q5–Q20 ficaram fora do escopo Regime Geral ou em especialidades/constitucional/local.

Conclusão: `REGIME_GERAL_INTERNAL_FREEZE_V0.1` **FALHOU S2**. As três questões consumidas agora são BUILD evidence para o patch e jamais validarão v0.2.

Relatório: `research/REGIME_GERAL_HELD_OUT_VALIDATION_H7_TJSC_2023_2026-09-11.md`.

Status: `CONSUMED / IN-SCOPE FAILURE / PATCHED`.

## Build após H7
- Depth Budget atualizado para `DEPTH_BUDGET_REGIME_GERAL_V0.3_2026-09-11.md`;
- specimen interno atualizado para `REGIME_GERAL_INTERNAL_FREEZE_V0.2_2026-09-11.md`;
- patches: RG0B territorialidade; art.36 completo; RG8 previdência/contagem recíproca.

## Próximo held-out
Novo pool precisa ser selado antes da leitura e conter chances reais de Regime Geral. Preferências:
1. objetiva Cebraspe de outro Estado não usada no BUILD;
2. Vunesp/TJGO se caderno verificável aparecer;
3. outra banca/Estado com caderno oficial e gabarito definitivo.

## Gap taxonomy
MATERIAL_GAP / STRUCTURE_GAP / DEPTH_GAP / FRESHNESS_GAP / TRANSFER_GAP / OUT_OF_SCOPE / BAD_QUESTION / PROVENANCE_ERROR.

## Gate S2
S2 permanece **NÃO ATINGIDO**. Só poderá subir após v0.2 sobreviver a novo held-out limpo e diversificado.

## Anti-leak
Não abrir H1R/H4 nem conteúdo de H5 sem locator verificável. Novo pool deve ser registrado antes da abertura.
