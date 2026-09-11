# GX Cartório OS — Held-Out Registry v0.2
## Regime Geral / Lei 8.935 / CNN

Snapshot: 2026-09-11
Status: SEALED METADATA + INCIDENT LOG. NÃO usar conteúdo reservado no BUILD.

## Regra
Este arquivo registra identidade e recorte das provas reservadas. **Não transcrever, resumir, classificar nem consultar enunciados reservados antes do freeze do material que será validado.**

Se uma questão reservada tiver sido vista antes da hora, se o locator estiver incorreto ou se a identidade do caderno não for demonstrável, o pool é `INVALID/CONTAMINATED` e deve ser substituído. Nunca fingir independência.

## Incident H1 — locator incorreto detectado em 11/09/2026
O registry v0.1 dizia:
`Vunesp/TJSP 13º Concurso, Prova 04 — Q5–Q15`.

Na primeira tentativa de abertura **após o BUILD freeze**, a checagem do cabeçalho/rodapé do PDF demonstrou que o locator usado não era TJSP: tratava-se do **Concurso de Outorga do Estado de Alagoas nº 01/2023, Vunesp**, cujo edital de gabarito aparece expressamente no próprio documento.

Consequência:
- o suposto H1/TJSP nunca teve identidade de fonte corretamente estabelecida;
- Q5–Q8 visualizadas no locator errado são AL/local e **não contam como validação** do material;
- Q9–Q15 do locator errado não precisam ser abertas;
- qualquer alegação anterior de “Vunesp/TJSP Q1–Q4 usadas no BUILD” deve ser tratada como `PROVENANCE_ERROR` até localizar o caderno correto;
- o material congelado NÃO recebe selo S2 com base nesse pool.

Status do antigo H1: `INVALID_LOCATOR / RETIRED`.

## H1R — Replacement pool Vunesp/TJSP
- concurso-alvo: Vunesp/TJSP, 13º Concurso de Outorga, código TJSP2305;
- página oficial confirmada: `https://www.vunesp.com.br/TJSP2305`;
- a aba “Provas e Gabaritos” da página oficial atualmente exige login na Área do Candidato;
- portanto, nenhum PDF encontrado por busca externa pode ser promovido a H1R sem validação explícita de cabeçalho/concurso/prova;
- status: `PENDING_VERIFIED_LOCATOR`.

Regra: ao localizar caderno público verificável do TJSP2305, registrar URL/metadados e recorte **antes** de abrir questões.

## H2 — Consulplan/TJMG Edital 1/2024
- fonte oficial localizada: edital/documentos do concurso;
- objetivo: encontrar caderno oficial/publicamente verificável e selar bloco de Regime Geral antes da leitura;
- status: `PENDING_LOCATOR`.

## H3 — IESES/TJPA 2026
- fonte: prova 6015 Tipo 1 + gabarito oficial;
- BUILD já utilizou Q2 e Q10; outras questões iniciais já foram visualizadas;
- status: `PARTIALLY_CONTAMINATED`;
- não usar como held-out limpo sem recorte previamente selado e demonstravelmente não visto.

## H4 — Future post-696 state exam
- reservar automaticamente ao menos 20% do primeiro concurso estadual publicado integralmente sob Res. 696/2026, estratificado por cluster;
- status: `FUTURE_RESERVED`.

## H5 — Replacement multibank pool
Como H1 falhou por proveniência, deve ser criado um pool adicional de banca estadual diferente das principais fontes BUILD, preferencialmente:
1. Consulplan, se o caderno oficial puder ser localizado e identificado sem abrir conteúdo;
2. outro caderno Vunesp de Cartório com PDF público e cabeçalho verificável;
3. IESES apenas com recorte documentalmente não exposto;
4. Cebraspe/FGV somente se necessário, pois já dominam o BUILD.

Status: `TO_BE_SEALED_BEFORE_READING`.

## Separação BUILD / VALIDATION / CHALLENGE
### BUILD confirmado
- ENAC 2025.1, 2025.2, 2026.1 já catalogados;
- FGV estaduais MS/RN/ES já estudados;
- Cebraspe BA/RO + challenge oral TJPE/TJDFT já estudados;
- IESES/PA recortes conhecidos;
- fontes primárias: CF, Lei 8.935, STF, CNN/CNJ.

### BUILD com provenance a corrigir
- referências anteriores a “Vunesp/TJSP Q1–Q4” NÃO são mais consideradas evidência TJSP até locator correto. Se o conteúdo analisado veio do PDF AL, reclassificar como `Vunesp/TJAL 2023` e, quando regra local, não usar para prioridade nacional.

### VALIDATION HELD-OUT
- H1R + H2 + H4 + H5, somente depois de metadados selados e fonte validada.

### CHALLENGE
- questões/casos oficiais não reservados, outras formas/bancas e adversariais sintéticos com QA.

## Critério de falha do material
1. `MATERIAL_GAP` — proposição necessária não ensinada;
2. `STRUCTURE_GAP` — informação existia, mas não estava conectada/recuperável;
3. `DEPTH_GAP` — ensinada rasa demais;
4. `FRESHNESS_GAP` — snapshot desatualizado;
5. `TRANSFER_GAP` — base existia, faltou aplicação/discriminação;
6. `OUT_OF_SCOPE` — conteúdo legitimamente fora do módulo;
7. `BAD_QUESTION` — problema de questão/gabarito após verificação;
8. `PROVENANCE_ERROR` — origem/identidade da questão ou caderno não foi validada.

## Gate de validação
- S2 exige held-out suficiente e diversificado;
- fonte e identidade do caderno fazem parte do gate, não são mero detalhe;
- o mesmo enunciado em versões diferentes conta uma vez;
- questão anulada não valida suficiência;
- após patch, reteste deve usar questão ainda limpa.

## Anti-leak
Nenhum agente deve abrir H1R/H2/H4/H5 antes de seu recorte ser formalmente selado.
