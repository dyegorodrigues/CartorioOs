# GX Cartório OS — Exam Atlas Wave 7
## LRP / OUTPUT / bank-form evidence

Data: 2026-09-11
Status: BUILD/CHALLENGE research; NÃO é material de estudo.

## Objetivo
Ampliar o corpus de Registro de Imóveis / LRP e testar a regra arquitetural:
`KNOWLEDGE_ATOMS ≠ BANK/EDITAL PACKAGING`.

## Fontes oficiais desta onda
1. Resolução CNJ 696/2026 vigente:
   https://atos.cnj.jus.br/atos/detalhar/7011
2. FGV — IV Concurso TJRS 2026:
   https://conhecimento.fgv.br/concursos/tjrsnotarial26
   Edital retificado: https://conhecimento.fgv.br/sites/default/files/concursos/edital-001-2026-tjrs-notarial-e-registral-retificado-27_02-002.pdf
3. Cebraspe — TJRO 2025/2026, prova escrita/prática:
   https://cdn.cebraspe.org.br/concursos/tj_ro_25_notarios/arquivos/32B4DC2ED8B45B6722BCC47D5FBE2BFE1BC24D0BDF310308F96C680E40166DFA.pdf
4. Cebraspe — TJRO, padrão definitivo de peça prática (remoção):
   https://cdn.cebraspe.org.br/concursos/tj_ro_25_notarios/arquivos/9BD159BEAA0E8BA80BCC3649F2B2EC0783D54F3D1C12187D506EA887485A6350.pdf
5. Vunesp — TJSP 13º Concurso:
   https://www.vunesp.com.br/TJSP2305

## Achados

### 1. LRP/RI não pode ser estudada como lista de artigos
O padrão definitivo do TJRO/Cebraspe exigiu elaboração de **ata notarial de justificação de posse para fins de usucapião extrajudicial**.

A resposta oficial integra:
- art. 1.071 CPC;
- art. 216-A LRP;
- arts. 399 e seguintes do Provimento 149/CNJ;
- aspectos formais da ata;
- qualificação dos interessados/advogado/cônjuge ou companheiro/titular registral;
- narrativa fática probatória.

Consequência GX: o nó `usucapião extrajudicial` deve ser modelado como **Integrated Procedure Graph**, não como memorização plana de um dispositivo.

### 2. Peça prática prova EXECUÇÃO, não apenas conhecimento declarativo
No TJRO, a banca não pediu “explique usucapião extrajudicial”. Pediu produzir um ato notarial adequado.

Portanto o Compiler deve distinguir:
- KNOW: requisitos/fundamento;
- DISCRIMINATE: qual instrumento é cabível;
- EXECUTE: estrutura, qualificação, narrativa, fundamentos e fecho do ato;
- QA: erros formais e jurídicos que zeram/subtraem pontos.

Isso reforça M5/M6 e o caminho:
`worked example → completion/fading → skeleton → micropeça → peça completa`.

### 3. Cebraspe atomiza conteúdo e forma
A prova escrita/prática do TJRO explicita que dissertação e peça têm pontuação própria de conteúdo + escrita/estrutura, com limite de linhas e desconsideração do excedente.

Consequência GX:
- Rubric de conteúdo e rubric de forma devem ser separadas;
- treinamento deve medir `legal atoms hit-rate` e `packaging compliance` separadamente;
- uma resposta juridicamente boa pode perder por não cumprir formato/linhas, e vice-versa.

### 4. TJRS/FGV 2026 reforça amplitude prática do core notarial/registral
O edital atual do TJRS lista, no núcleo notarial, atos notariais em espécie, testamentos, ata notarial, procurações, doações, cessões, união estável, reconhecimento de filhos, escrituras imobiliárias, certidões, ITBI/ITCMD, autenticações, firmas etc.

Não usar a amplitude do edital como licença para primeira passagem enciclopédica.

Consequência GX:
- `OFFICIAL SCOPE` define universo possível;
- `EXAM CORPUS` + centralidade + custo decidem P1/P2/P3;
- especialidades precisam de mapa de atos/procedimentos antes de detalhes.

### 5. Vunesp/SP permanece excelente CHALLENGE de literalidade/sistematização
A página oficial do 13º Concurso mantém provas/gabaritos e 212 vagas.

O pool H1 do Regime Geral já selou Q5–Q15 de uma prova Vunesp, portanto NÃO abrir esse conteúdo até freeze do material.

Vunesp continua útil em BUILD/CHALLENGE somente por recortes não selados e previamente registrados.

## Nova taxonomia de nós práticos
Para N/R/RI/Notas, classificar nós como:

### RULE NODE
Ex.: prazo, competência, impedimento, requisito curto.
Superfície dominante: lei seca + contrast pair + objective lab.

### PROCEDURE NODE
Ex.: usucapião extrajudicial, retificação, dúvida registral.
Superfície dominante: fluxo + requisitos + decision points + casos.

### ACT NODE
Ex.: escritura, ata, nota devolutiva, registro/averbação específica.
Superfície dominante: model sheet textual + skeleton + execução.

### SYSTEM NODE
Ex.: SERP, Justiça Aberta, CENPROT, Constrijud.
Superfície dominante: arquitetura, atores, entradas/saídas, obrigação/fiscalização, freshness.

### JURISPRUDENCE NODE
Ex.: Tema 777/779, ADI 1183.
Superfície dominante: tese + fato-gatilho + consequência + contraste.

Um mesmo macrotema pode conter os cinco tipos.

## Implicação para o primeiro material N/R
O próximo specimen não deve demonstrar apenas RULE NODE. Deve provar que o GX consegue representar ao menos:
1. uma regra literal curta;
2. uma distinção jurisprudencial;
3. um mini-procedimento;
4. um output atom/skeleton.

Caso contrário, o protótipo pode parecer bom em Lei 8.935 e falhar justamente no que diferencia Cartório de carreiras jurídicas genéricas.

## Próxima onda
- aprofundar LRP seed em `prenotação/qualificação → dúvida → indisponibilidade → usucapião → retificação`;
- ligar cada procedure node a questões objetivas e output oficiais;
- triangular FGV/Cebraspe/Vunesp/IESES sem vazar held-out;
- produzir Depth Budget LRP v0.1 somente após ledger mínimo por procedure;
- manter Freshness Firewall sobre Prov.149 e atos modificadores 2026.
