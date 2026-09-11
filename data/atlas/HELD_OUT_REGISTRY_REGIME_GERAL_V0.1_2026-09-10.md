# GX Cartório OS — Held-Out Registry v0.5
## Regime Geral / Lei 8.935 / CNN

Snapshot: 2026-09-11
Status: ACTIVE VALIDATION REGISTRY. NÃO usar conteúdo reservado no BUILD.

## Regra
Registrar identidade/recorte **antes** de abrir conteúdo. Se fonte/caderno/versão não forem demonstráveis, o pool é inválido. Se conteúdo reservado for visto antes do freeze, marcar contaminado e substituir.

## Incident H1 — locator incorreto
O antigo `H1 — Vunesp/TJSP 13º Concurso, Prova 04 Q5–Q15` foi invalidado em 11/09/2026 porque o PDF usado era, na verdade, do **TJAL/Vunesp 2023**.

Consequências:
- Q5–Q8 do locator errado não contam como validação;
- referências anteriores a “TJSP Q1–Q4” ficam `PROVENANCE_ERROR`;
- regra local de Alagoas não pode elevar prioridade nacional.

Status: `INVALID_LOCATOR / RETIRED`.

## H1R — Vunesp/TJSP 13º Concurso
- código oficial: TJSP2305;
- página oficial: `https://www.vunesp.com.br/TJSP2305`;
- aba de provas exige login;
- nenhum PDF externo será aceito sem cabeçalho verificável.

Status: `PENDING_VERIFIED_LOCATOR`.

## H2 — Consulplan/TJMG Edital 1/2024
- página oficial confirmada;
- concurso sofreu suspensão/nulidade parcial antes de produzir caderno utilizável.

Status: `NO_USABLE_EXAM_YET / PARKED`.

## H3 — IESES/TJPA 2026
- Q2/Q10 e outras questões iniciais já expostas/BUILD.

Status: `PARTIALLY_CONTAMINATED`.

## H4 — Future post-696 state exam
Reservar automaticamente >=20% do primeiro concurso estadual integralmente publicado sob Res.696/2026.

Status: `FUTURE_RESERVED`.

## H5 — Vunesp/TJGO2001
- página oficial: `https://www.vunesp.com.br/TJGO2001`;
- 292 vagas;
- gabarito oficial público localizado;
- PROVIMENTO, versão 1, Q1–Q10 seladas;
- caderno verificável ainda não localizado.

Status: `SEALED / PENDING_QUESTION_BOOK_LOCATOR`.

## H6 — Cebraspe/TJRR 2025 — CONSUMED FOR SCOPE CHECK
Metadados:
- PROVIMENTO;
- caderno oficial Cebraspe: `4803314D33BB8A8908C1320C7E9B9F21B1788DB04B66E34226DCEB250B89DB40.pdf`;
- Q1–Q4 haviam sido contaminadas por snippet de busca;
- Q5–Q10 foram seladas antes da abertura e depois consumidas legitimamente.

### Resultado Q5–Q10
- Q5: Apostila da Haia/Res.228 → especialidade/notarial-system, `OUT_OF_SCOPE` do specimen Regime Geral;
- Q6: atos/documentos de tabelionato de notas → `OUT_OF_SCOPE`;
- Q7: procurações/mandato/PLD-mediação → `OUT_OF_SCOPE`;
- Q8: usucapião extrajudicial → RI/procedure, `OUT_OF_SCOPE` do Regime Geral, mas útil para o novo Depth Budget RI;
- Q9: protesto/qualificação → `OUT_OF_SCOPE`;
- Q10: CENPROT → `OUT_OF_SCOPE` e **anulada no gabarito definitivo**.

Conclusão: H6 não aprova nem reprova Regime Geral. Ele valida a regra de não forçar questão de especialidade contra módulo errado.

Status: `CONSUMED / ALL OUT_OF_SCOPE FOR CURRENT MODULE`.

## H7 — Cebraspe/TJSC Edital 015/2022 — SEALED BEFORE LOCATOR SEARCH
Criado para obter held-out com maior chance de Regime Geral, antes de pesquisar o caderno.

Metadados conhecidos sem leitura do caderno reservado:
- concurso: TJSC, Edital 015/2022, atividade notarial e registral;
- banca: Cebraspe;
- fonte oficial do concurso: TJSC/Cebraspe;
- prova objetiva de provimento aplicada em 18/06/2023 segundo cronograma oficial;
- corpus oral TJSC já foi usado historicamente em outra frente, mas **a objetiva deste recorte não foi usada no BUILD Regime Geral**.

### Recorte selado antes da busca de locator
- modalidade: **PROVIMENTO**;
- questões: **Q1–Q20**;
- finalidade: após localizar o caderno oficial, identificar apenas quais questões pertencem a Regime Geral e usar essas como validação; demais serão OUT_OF_SCOPE;
- não abrir Q21+ nesta rodada.

Status: `SEALED / READY_FOR_LOCATOR_SEARCH`.

## BUILD confirmado
- ENAC 2025.1/2025.2/2026.1;
- FGV MS/RN/ES;
- Cebraspe BA/RO;
- challenge oral TJPE/TJDFT;
- IESES/PA recortes conhecidos;
- CF, Lei 8.935, STF, CNN/CNJ.

## Gap taxonomy
MATERIAL_GAP / STRUCTURE_GAP / DEPTH_GAP / FRESHNESS_GAP / TRANSFER_GAP / OUT_OF_SCOPE / BAD_QUESTION / PROVENANCE_ERROR.

## Gate S2
S2 exige questões in-scope limpas e diversificadas. Um pool só com OUT_OF_SCOPE não conta como aprovação.

## Anti-leak
Não abrir H1R/H4, Q11+ de H5 ou Q21+ de H7 nesta rodada.
