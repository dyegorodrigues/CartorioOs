# GX Cartório OS — Held-Out Registry v0.9
## Regime Geral / Lei 8.935 / CNN

Snapshot: 2026-09-11
Status: ACTIVE VALIDATION REGISTRY. NÃO usar conteúdo reservado no BUILD.

## Regra
Registrar identidade/recorte antes de abrir conteúdo. Questão exibida por snippet de busca antes da abertura formal deixa de ser held-out independente.

## Pools anteriores
- H1 antigo TJSP locator: `INVALID_LOCATOR / RETIRED` (era TJAL/Vunesp 2023).
- H1R TJSP2305: `PENDING_VERIFIED_LOCATOR`.
- H2 TJMG/Consulplan: `PARKED`.
- H3 TJPA/IESES: `PARTIALLY_CONTAMINATED`.
- H4 primeiro pós-696 integral: `FUTURE_RESERVED`.
- H5 TJGO/Vunesp: `SEALED / PENDING_QUESTION_BOOK_LOCATOR`.
- H6 TJRR/Cebraspe: `CONSUMED / ALL OUT_OF_SCOPE`.
- H7 TJSC/Cebraspe: `CONSUMED / IN-SCOPE FAILURE`; v0.1 falhou S2 e foi patchado.

## H8 — Cebraspe/TJPE 2024 PROVIMENTO — CONSUMED FOR SCOPE
Caderno oficial:
`https://cdn.cebraspe.org.br/concursos/tj_pe_24_notarios/arquivos/005_TJPE_001_01.PDF`

Q1–Q6 foram contaminadas por snippet do locator. H8R Q7–Q20 foram seladas antes da abertura e consumidas legitimamente.

### Resultado H8R Q7–Q20
- Q7 LGPD/proteção de dados → CROSS-SYSTEM/overlay, fora do specimen Regime Geral básico;
- Q8 imóvel rural/CAR/alienação fiduciária → especialidade/Civil-RI;
- Q9 CNIB → RI/system node;
- Q10 princípios registrais → RI;
- Q11–Q15 RCPN → especialidade;
- Q16 RCPJ → especialidade;
- Q17 RTD/territorialidade → especialidade;
- Q18 adjudicação compulsória → RI/Civil;
- Q19 condomínio/incorporação → RI/Civil;
- Q20 Lei 10.169/emolumentos → nó próprio `EMOLUMENTOS`, adjacente ao Regime Geral, mas não pertencente ao scope freeze RG0–RG8.

Conclusão: H8R não traz item in-scope do specimen Regime Geral v0.2. Não conta como aprovação nem reprovação.

Status: `CONSUMED / ALL OUT_OF_SCOPE OR ADJACENT`.

## H9 — Cebraspe/TJPE 2024 REMOÇÃO — SEALED BEFORE QUESTION SEARCH
Criado após o freeze v0.2 e antes de localizar/abrir o caderno de REMOÇÃO.

Metadados confirmados:
- mesmo concurso TJPE/Cebraspe 2024;
- modalidade: **REMOÇÃO**;
- gabarito preliminar/definitivo foi localizado em busca anterior e revelou apenas letras, não os enunciados reservados;
- conhecer letras do gabarito não contaminou o conteúdo do freeze, mas fica registrado como `ANSWER_KEY_PRESEEN` para transparência.

### Recorte selado
- questões: **Q1–Q6** da prova de REMOÇÃO;
- finalidade: obter itens de Regime Geral que não sejam simples duplicatas textuais do caderno de provimento;
- se a questão for idêntica/materialmente equivalente a uma já vista, classificar `DUPLICATE_NOT_INDEPENDENT`;
- Q7+ não abrir nesta rodada.

### Protocolo
1. localizar caderno oficial de remoção;
2. validar cabeçalho/modalidade;
3. abrir somente Q1–Q6;
4. comparar identidade/estrutura com provimento;
5. mapear in-scope/out-of-scope;
6. somente questões materialmente independentes podem contribuir para S2.

Status: `SEALED / READY_FOR LOCATOR SEARCH`.

## Build atual
- `DEPTH_BUDGET_REGIME_GERAL_V0.3_2026-09-11.md`;
- `REGIME_GERAL_INTERNAL_FREEZE_V0.2_2026-09-11.md`.

## Gap taxonomy
MATERIAL_GAP / STRUCTURE_GAP / DEPTH_GAP / FRESHNESS_GAP / TRANSFER_GAP / OUT_OF_SCOPE / BAD_QUESTION / PROVENANCE_ERROR / DUPLICATE_NOT_INDEPENDENT.

## Gate S2
S2 permanece NÃO ATINGIDO.

## Anti-leak
Não abrir H1R/H4/H5; em H9 não abrir Q7+.
