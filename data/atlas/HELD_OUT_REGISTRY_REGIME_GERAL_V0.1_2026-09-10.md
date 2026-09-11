# GX Cartório OS — Held-Out Registry v0.3
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
- o concurso sofreu suspensão/nulidade parcial antes de produzir um caderno objetivo utilizável como held-out atual;
- por isso, H2 não é mais prioridade imediata de validação.

Status: `NO_USABLE_EXAM_YET / PARKED`.

## H3 — IESES/TJPA 2026
- prova 6015 Tipo 1 + gabarito oficiais;
- Q2/Q10 já usados no BUILD e outras questões iniciais já expostas;
- não usar como held-out sem recorte comprovadamente não visto.

Status: `PARTIALLY_CONTAMINATED`.

## H4 — Future post-696 state exam
Reservar automaticamente ao menos 20% do primeiro concurso estadual integralmente publicado sob Res.696/2026, estratificado por cluster.

Status: `FUTURE_RESERVED`.

## H5 — Vunesp/TJGO2001 — SEALED BEFORE READING
Pool substituto multibanca criado **antes de abrir o caderno de questões**.

Metadados já confirmados sem leitura do caderno:
- banca: Fundação Vunesp;
- concurso: Tribunal de Justiça de Goiás, Concurso Público para Outorga de Delegações de Notas e de Registro;
- código oficial da página: `TJGO2001`;
- página oficial: `https://www.vunesp.com.br/TJGO2001`;
- 292 vagas;
- prova objetiva teve versões e gabarito oficial público; o edital de gabarito identifica expressamente o concurso.

### Recorte selado
- modalidade: **PROVIMENTO**;
- versão-alvo: **VERSÃO 1**;
- questões reservadas: **Q1–Q10**;
- objetivo: identificar quais itens pertencem legitimamente a Regime Geral e testar o specimen congelado; itens de especialidades ou legislação local serão `OUT_OF_SCOPE`, não falha artificial do módulo.

### Protocolo de abertura
1. localizar caderno público oficial/verificável;
2. validar cabeçalho/modalidade/versão;
3. abrir somente Q1–Q10;
4. usar gabarito oficial correspondente;
5. não consultar Q11+ nesta rodada.

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
- H5 agora é o pool limpo utilizável;
- H1R permanece pendente;
- H4 permanece futuro.

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
Não abrir H1R/H4 nem Q11+ de H5 nesta rodada.
