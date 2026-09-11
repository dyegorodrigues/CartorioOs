# GX Cartório OS — Held-Out Registry v0.4
## Regime Geral / Lei 8.935 / CNN

Snapshot: 2026-09-11
Status: SEALED METADATA + INCIDENT LOG. NÃO usar conteúdo reservado no BUILD.

## Regra
Registrar identidade/recorte **antes** de abrir conteúdo. Se fonte, caderno ou versão não forem demonstráveis, o pool é inválido. Se conteúdo reservado for visto antes do freeze, marcar contaminado e substituir.

## Incident H1 — locator incorreto
O antigo `H1 — Vunesp/TJSP 13º Concurso, Prova 04 Q5–Q15` foi invalidado em 11/09/2026.

A primeira checagem do PDF após o BUILD freeze demonstrou que o locator usado era, na verdade, do **Concurso de Outorga do Estado de Alagoas nº 01/2023, Vunesp**. Q5–Q8 visualizadas nesse documento local não contam como validação. Referências anteriores a “TJSP Q1–Q4” ficam marcadas `PROVENANCE_ERROR` até correção.

Status: `INVALID_LOCATOR / RETIRED`.

## H1R — Vunesp/TJSP 13º Concurso
- código oficial: `TJSP2305`;
- página oficial confirmada: `https://www.vunesp.com.br/TJSP2305`;
- 212 vagas na página oficial atual;
- “Provas e Gabaritos” exige login na Área do Candidato;
- nenhum PDF externo será promovido sem cabeçalho/concurso/prova verificáveis.

Status: `PENDING_VERIFIED_LOCATOR`.

## H2 — Consulplan/TJMG Edital 1/2024
- página oficial Consulplan confirmada;
- concurso sofreu suspensão/nulidade parcial antes de produzir caderno objetivo utilizável nesta fase.

Status: `NO_USABLE_EXAM_YET / PARKED`.

## H3 — IESES/TJPA 2026
- prova 6015 Tipo 1 + gabarito oficiais;
- Q2/Q10 já usados no BUILD e outras questões iniciais já expostas.

Status: `PARTIALLY_CONTAMINATED`.

## H4 — Future post-696 state exam
Reservar automaticamente ao menos 20% do primeiro concurso estadual integralmente publicado sob Res.696/2026, estratificado por cluster.

Status: `FUTURE_RESERVED`.

## H5 — Vunesp/TJGO2001
- banca: Vunesp;
- página oficial: `https://www.vunesp.com.br/TJGO2001`;
- 292 vagas;
- gabarito oficial público localizado;
- modalidade/versão reservada: PROVIMENTO, versão 1, Q1–Q10;
- caderno público oficial/verificável ainda não localizado sem ambiguidade.

Status: `SEALED / PENDING_QUESTION_BOOK_LOCATOR`.

## H6 — Cebraspe/TJRR 2025 — CLEAN RECUT SEALED
Uma busca de locator exibiu automaticamente conteúdo de Q1–Q4 do caderno de provimento, tornando Q1–Q4 contaminadas para validação independente. **Antes de abrir qualquer conteúdo posterior**, foi criado este recorte.

Metadados confirmados:
- concurso: TJRR Notários, Edital 2025;
- banca: Cebraspe;
- fonte oficial CDN Cebraspe;
- caderno objetivo de PROVIMENTO identificado por cabeçalho oficial;
- locator do caderno: `https://cdn.cebraspe.org.br/concursos/tj_rr_25/arquivos/4803314D33BB8A8908C1320C7E9B9F21B1788DB04B66E34226DCEB250B89DB40.pdf`;
- outro caderno oficial também foi localizado, mas não será misturado;
- prova possui 100 questões, 0,10 por acerto, conforme edital.

### Contaminação conhecida
- Q1–Q4: `CONTAMINATED_BY_SEARCH_SNIPPET`.

### Recorte limpo selado
- Q5–Q10: **SEALED BEFORE READING**;
- finalidade: validação externa do specimen Regime Geral congelado;
- se alguma dessas questões tratar de especialidade fora do módulo, classificar `OUT_OF_SCOPE` sem forçar falha.

### Protocolo
1. abrir somente trecho Q5–Q10;
2. localizar gabarito definitivo oficial correspondente;
3. mapear proposição necessária;
4. confrontar com `REGIME_GERAL_INTERNAL_FREEZE_V0.1`;
5. registrar gap;
6. não consultar Q11+ nessa rodada.

Status: `SEALED / READY_FOR_VALIDATION`.

## BUILD confirmado
- ENAC 2025.1, 2025.2, 2026.1;
- FGV estaduais MS/RN/ES;
- Cebraspe BA/RO;
- challenge oral oficial TJPE/TJDFT;
- IESES/PA recortes conhecidos;
- CF, Lei 8.935, STF, CNN/CNJ.

## BUILD com provenance corrigida
Qualquer dado anteriormente atribuído a Vunesp/TJSP a partir do locator errado deve ser reclassificado como Vunesp/TJAL 2023 quando confirmado, e regra local de Alagoas não pode elevar prioridade nacional.

## VALIDATION HELD-OUT
- H6 = pronto e limpo Q5–Q10;
- H5 = selado, aguardando locator do caderno;
- H1R = pendente;
- H4 = futuro.

## Gap taxonomy
1. MATERIAL_GAP
2. STRUCTURE_GAP
3. DEPTH_GAP
4. FRESHNESS_GAP
5. TRANSFER_GAP
6. OUT_OF_SCOPE
7. BAD_QUESTION
8. PROVENANCE_ERROR

## Gate S2
- fonte/caderno/versão validados;
- questões não usadas no BUILD;
- diversidade suficiente;
- falha gera patch;
- questão consumida nunca é reutilizada como prova independente após patch.

## Anti-leak
Não abrir H1R/H4, Q11+ de H6 ou conteúdo de H5 além do necessário para validar o locator antes de sua abertura formal.
