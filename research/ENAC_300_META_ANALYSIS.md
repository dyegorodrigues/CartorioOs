# ENAC 300 — Meta-análise auditada

Data: 28/09/2026  
Status: **CANÔNICO PARA FATOS MEDIDOS / TAGS ANALÍTICAS 300/300 / RELAÇÕES 299/300 COM 1 MATRIX-DRIFT INTENCIONAL**

> Este documento substitui `ENAC_300_META_ANALYSIS_DRAFT.md` como ponto de leitura atual. O draft histórico permanece preservado.

## 1. Escopo e regra de honestidade estatística

O corpus histórico direto do ENAC contém três edições completas já aplicadas pela FGV:

- ENAC 2025.1;
- ENAC 2025.2;
- ENAC 2026.1.

A auditoria estruturada de 14/09/2026 confirmou **300 registros canônicos**, 100 por edição, todos validados como oficiais e sem contar quatro registros antigos de bootstrap excluídos das métricas.

Nem todo campo analítico está preenchido nos 300. Portanto cada estatística deste documento declara seu denominador real.

Regra: **ausência de tag não significa ausência do fenômeno**.

---

# 2. Fatos 300/300

## 2.1 Distribuição histórica por disciplina

| Disciplina | 2025.1 | 2025.2 | 2026.1 | Total histórico |
|---|---:|---:|---:|---:|
| Notarial e Registral | 60 | 60 | 60 | **180** |
| Civil | 14 | 14 | 14 | **42** |
| Constitucional | 9 | 9 | 9 | **27** |
| Administrativo | 4 | 4 | 4 | **12** |
| Tributário | 4 | 4 | 4 | **12** |
| Empresarial | 4 | 4 | 4 | **12** |
| Processo Civil | 2 | 2 | 2 | **6** |
| Penal | 1 | 1 | 1 | **3** |
| Processo Penal | 1 | 1 | 1 | **3** |
| Conhecimentos Gerais | 1 | 1 | 1 | **3** |
| **Total** | **100** | **100** | **100** | **300** |

## 2.2 Anulações

Seis questões foram anuladas no gabarito definitivo:

- 2025.1: Q54, Q88, Q94;
- 2025.2: Q24;
- 2026.1: Q87, Q95.

Logo:

- 294 itens têm resposta definitiva não anulada;
- 6 permanecem no corpus para conteúdo, ambiguidade e QA da banca, mas não oferecem resposta jurídica canônica.

## 2.3 Matrix drift para o alvo atual

O ENAC 2026.2 mantém 100 questões, porém altera a composição:

- N/R 60;
- Civil 14;
- Constitucional 8;
- Administrativo 4;
- Tributário 4;
- Empresarial 4;
- Processo Civil 2;
- Penal 1;
- Processo Penal 1;
- Trabalho 1;
- Processo do Trabalho 1.

Consequências:

1. Conhecimentos Gerais é bloco histórico, não alvo atual;
2. Trabalho e Processo do Trabalho possuem **zero histórico ENAC direto** nas três edições analisadas;
3. Constitucional possui 27 itens históricos, mas sua oportunidade futura caiu de 9 para 8 por prova;
4. comparações futuras precisam ser normalizadas por exposição possível, não apenas por contagem bruta.

---

# 3. Estado de completude das anotações

Reparo relacional e taxonômico concluído em 28/09/2026, com recontagem estruturada antes do limite de consultas do workspace.

## 3.1 Relação questão → currículo

| Edição | Ligadas | sem vínculo |
|---|---:|---:|
| 2025.1 | **100** | 0 |
| 2025.2 | **99** | **1** |
| 2026.1 | **100** | 0 |
| **Total** | **299** | **1** |

O único item sem vínculo é **ENAC 2025.2 Q100 — Debate público sobre medicamentos para obesidade**. É um caso deliberado de `MATRIX_DRIFT`: Conhecimentos Gerais existia nas três edições históricas, mas não integra a matriz ENAC 2026.2. Não criar nó jurídico artificial apenas para zerar a coluna.

Portanto:
- cobertura bruta: **299/300 = 99,67%**;
- cobertura dos itens juridicamente mapeáveis ao currículo atual neste corpus: **299/299 = 100%**;
- 1 item permanece `INTENTIONAL_UNMAPPED / MATRIX_DRIFT`.

A restrição anterior contra ranking quantitativo por nó motivada por 171 relações deixa de valer. Permanecem, porém, as restrições de tamanho amostral, dependência entre múltiplos vínculos e necessidade de QA jurídico.

## 3.2 Família da fonte

A recontagem de completude confirmou:
- 2025.1: 100/100 preenchidas;
- 2025.2: 100/100 preenchidas;
- 2026.1: 100/100 preenchidas.

Logo o campo está **300/300 preenchido**.

Os percentuais antigos de 200 itens abaixo não devem mais ser usados como fotografia atual. A recontagem agregada 300/300 por família ficou pendente porque o workspace atingiu o limite de `Query Data Source` logo depois da verificação de completude. Até nova consulta, não publicar novos percentuais por família.

## 3.3 Mecanismo do distrator

A recontagem de completude confirmou:
- 2025.1: 100/100 com tag;
- 2025.2: 100/100 com tag;
- 2026.1: 100/100 com tag.

Logo o campo está **300/300 preenchido**.

O campo continua multi-select: uma questão pode conter múltiplos mecanismos. Os agregados antigos de 200 itens servem apenas como histórico de calibração, não como estatística final. A nova distribuição 300/300 deve ser recalculada quando a consulta estruturada estiver novamente disponível.

## 3.4 Validação e anulações

Os três blocos permanecem 100/100 com `Validação = Oficial`.

Anulações confirmadas na base:
- 2025.1: 3;
- 2025.2: 1;
- 2026.1: 2;
- total: **6/300**.

As anuladas permanecem úteis para conteúdo, ambiguidade e QA de banca, mas não fornecem resposta jurídica canônica.

## 3.5 QA cego amostral

Foi iniciada releitura diretamente no caderno oficial FGV 2025.2, inclusive conferência visual do PDF. A amostra deste lote incluiu Q43, Q44, Q76, Q77, Q78, Q79, Q84, Q86, Q87, Q88 e Q90.

Resultado do recorte: **nenhum drift material de tema** foi encontrado entre o enunciado oficial e os vínculos curriculares adicionados.

Isto é QA amostral, não certificação jurídica 300/300.

---

# 4. Padrões qualitativos repetidos nas três edições

As três classificações foram produzidas separadamente e convergem em oito padrões.

## 4.1 N/R é um domínio integrador, não uma ilha

Questões formalmente N/R puxam Civil, garantias, família, sucessões, responsabilidade, processo, tributação e regras administrativas.

Consequência: uma apostila-silo de “Notarial e Registral” perde pré-requisitos que a FGV trata como embutidos no problema.

## 4.2 Civil funciona como infraestrutura do extrajudicial

Direitos reais, contratos, capacidade, família e sucessões reaparecem dentro ou ao redor de RI, Notas e RCPN.

Consequência: os 14% formais de Civil subestimam sua centralidade pedagógica no grafo.

## 4.3 A FGV cartorializa matérias externas

Constitucional, Administrativo, Tributário, Empresarial, Penal e Processo frequentemente são apresentados em contextos de serventia, imóvel, emolumento, delegação, protesto ou atividade extrajudicial.

Consequência: aprender a base geral é necessário, mas exemplos e transferência devem retornar ao universo cartorial sempre que houver evidência.

## 4.4 Aplicação e literalidade coexistem

Há casos concretos e decisões operacionais, mas também listas, requisitos, definições, doutrina, jurisprudência e redação quase literal.

Consequência: não escolher entre “só lei seca” e “só caso”. O scheduler precisa alternar conforme a natureza da proposição.

## 4.5 Uma variável pequena frequentemente decide a alternativa

Nas classificações e no Atlas aparecem repetidamente:

- sujeito/competência;
- requisito;
- prazo/momento;
- efeito jurídico;
- legitimidade;
- exceção;
- judicial x extrajudicial;
- esfera de responsabilidade;
- conceito juridicamente próximo.

Isto é compatível com os mecanismos anotados nas duas primeiras edições e com a análise de questões FGV estaduais.

## 4.6 Freshness é parte da matéria

SERP, CNIB/CNN, centrais, atos CNJ, desjudicialização, garantias e procedimentos eletrônicos surgem no corpus.

Consequência: o Freshness Firewall é componente curricular, não clipping de notícias.

## 4.7 O tempo jurídico precisa de três snapshots

Para cada regra volátil:

1. direito vigente na data da questão histórica;
2. direito cobrável segundo o marco temporal do edital-alvo;
3. direito vigente hoje.

Sem essa separação, questão antiga pode ensinar resposta superada.

## 4.8 A disciplina formal não basta como unidade analítica

O objeto útil é a **proposição jurídica examinável**, ligada a tema, microtema, fonte, operação cognitiva e distrator.

---

# 5. O que concursos FGV estaduais acrescentam ao ENAC

O ENAC oferece alvo objetivo direto. Concursos estaduais FGV acrescentam algo que o ENAC não consegue oferecer sozinho: **evidência de output**.

A triangulação já realizada sobre TJMS, TJRN e TJES recentes mostrou:

## 5.1 Casos multiproposição

Uma única questão/peça pode exigir sequência de decisões em vários diplomas e ramos.

## 5.2 Espelho atomizado

Mesmo respostas longas são pontuadas por unidades jurídicas concretas. O treino avançado não deve ser “escrever bonito”, e sim identificar e produzir os átomos esperados com estrutura.

## 5.3 Teoria abstrata entra quando funcional ao caso

Constitucional e outras matérias gerais podem atingir profundidade alta quando o caso cartorial exige. Isso justifica profundidade seletiva, não enciclopedismo.

## 5.4 Packaging varia por edital

A FGV já utilizou combinações diferentes de peça, dissertação, discursivas, tempo e limite de linhas.

Consequência: estudar o Direito uma vez e adaptar a embalagem ao edital; não criar uma única “redação FGV padrão”.

---

# 6. O que outras bancas acrescentam sem contaminar o modelo FGV

Cebraspe, Vunesp, IESES, Consulplan e outras bancas de Cartório servem para o **Domain Incidence Model**:

- detectar institutos que o domínio cobra mesmo quando não apareceram em apenas três ENACs;
- descobrir aliases e formulações diferentes;
- testar robustez;
- ampliar corpus de discursiva, peça e oral;
- localizar cauda examinável.

Elas não entram no denominador do **Bank Style Model FGV**.

Exemplo já observado no Atlas: Cebraspe recente pode usar múltipla escolha com composição de assertivas e casos, portanto sequer deve ser caricaturado como “Certo/Errado”.

---

# 7. Clusters de alta conectividade já autorizados como prioridade de ANÁLISE

Isto não é ainda um ranking final de estudo individual.

1. Registro de Imóveis + direitos reais + garantias;
2. desjudicialização: usucapião, adjudicação, inventário/divórcio e procedimentos conexos;
3. RCPN + família + nome + filiação + atos estrangeiros;
4. Tabelionato de Notas + capacidade + família + sucessões;
5. Protesto + crédito + Empresarial + Tributário;
6. SERP/CNIB/CNN/centrais eletrônicas + regulação CNJ;
7. delegação + prepostos + responsabilidade + disciplina + interinidade;
8. parcelamento/incorporação/regularização fundiária;
9. proteção de dados/compliance/PLD-FT.

Razão: esses clusters aparecem reiteradamente nas leituras das provas e possuem alta centralidade entre disciplinas e fases.

---

# 8. Mudança estratégica trazida pela Resolução CNJ 696/2026

A preparação não deve tratar todas as fases como se fossem apenas “mais questões”.

## ENAC

Habilitação nacional prévia.

## Objetiva estadual, quando existir

Para ir à discursiva, a Resolução 696/2026 exige cumulativamente:

- mínimo de 50% em N/R;
- mínimo de 60% no total;
- classificação até 12 candidatos por vaga, ressalvadas as regras específicas de cotas.

Logo `passar no ENAC` e `ser competitivo na objetiva estadual` são riscos diferentes.

## Classificação final

- discursiva: **70%**;
- oral: **25%**, exclusivamente classificatória;
- títulos: **5%**.

A discursiva exige no mínimo 1 dissertação, 1 peça e 3 questões discursivas. Para chegar à oral, o corte normativo da discursiva corresponde a 42/70.

Penal, Processo Penal, Trabalho e Processo do Trabalho ficam restritos ao ENAC/objetiva. O teto de produção avançada nacional concentra-se em:

- N/R;
- Constitucional;
- Civil;
- Administrativo;
- Tributário;
- Processo Civil;
- Empresarial.

---

# 9. Consequência para a Mega-Árvore

Cada proposição deve possuir, sem colapsar tudo num número mágico:

- escopo oficial;
- peso da matriz;
- recorrência no domínio;
- evidência da banca-alvo;
- centralidade no grafo;
- confusabilidade;
- freshness;
- transferência entre fases;
- consequência do erro;
- custo de aprendizagem;
- dificuldade individual futura;
- risco de retenção futuro.

Desses sinais derivam quatro prioridades independentes:

1. `STUDY PRIORITY`;
2. `MEMORY PRIORITY`;
3. `QUESTION PRIORITY`;
4. `OUTPUT PRIORITY`.

Uma regra pode ser rara, barata e fatal se esquecida: alta memória, baixa densidade teórica. Outra pode ser central e derivável: alta compreensão, menos flashcard literal.

---

# 10. O que NÃO pode ser afirmado ainda

Mesmo após o reparo estrutural, permanecem proibidos:

- “tema X tem 83% de chance de cair”;
- tendência temporal forte com três edições;
- tratar múltiplos vínculos de uma questão como observações estatisticamente independentes;
- inferir irrelevância porque o tema não apareceu em três provas;
- usar outra banca para fabricar amostra de estilo FGV;
- usar questão histórica sem revalidar o Direito atual;
- confundir indexação/linkagem 300/300 com reconstrução jurídica 300/300;
- chamar QA amostral de certificação integral;
- forçar Conhecimentos Gerais histórico para dentro do currículo jurídico atual;
- publicar novos percentuais 300/300 de fonte/distrator antes da recontagem agregada.

---

# 11. Próximo lote empírico obrigatório

A arquitetura e o reparo estrutural estão suficientemente fechados. O ganho seguinte é transformar os 300 itens anotados em estatística confiável e depois em decisão pedagógica.

Ordem operacional:

1. quando `Query Data Source` voltar, recalcular agregados 300/300 de família de fonte e mecanismos de distrator;
2. preservar Q100/2025.2 como `INTENTIONAL_UNMAPPED / MATRIX_DRIFT`;
3. ampliar QA cego estratificado entre 2025.1, 2025.2 e 2026.1;
4. produzir o primeiro heatmap quantitativo por nó/subtema, explicitando denominador e múltiplos vínculos;
5. cruzar o **Domain Incidence Model** com cartório multibanca;
6. cruzar separadamente o **FGV Bank Style Model** com FGV estadual/cartório e FGV comparável, com pesos distintos;
7. gerar Reconstruction Cards para clusters materialmente prioritários;
8. atribuir Depth Budgets por proposição/cluster;
9. manter held-out separado antes de validar material learner-facing;
10. continuar sem iniciar estudo real ou atribuir mastery.

---

# 12. Artefatos relacionados

- `research/ENAC_LINK_REPAIR_AND_BLIND_QA_2026-09-28.md` — checkpoint do reparo relacional, completude 300/300 e QA cego amostral;
- `research/ENAC_EDITAL_MEGA_TREE_META_ANALYSIS_2026-09-14.md` — arquitetura consolidada da mega-árvore;
- `research/ENAC_300_STRUCTURED_QA_2026-09-14.md` — auditoria exata do data source;
- `research/ENAC_300_CORPUS_GATE.md` — limites e regra de Passagem 2;
- `research/MULTI_BANK_CORPUS.md` — dois estimadores e hierarquia de corpus;
- `research/CARTORIO_EXAM_ATLAS_PROTOCOL_2026.md` — protocolo de proposições e corpus;
- `research/CARTORIO_EXAM_ATLAS_WAVE5_OUTPUT_TRIANGULATION_FGV_CEBRASPE_2026.md` — output FGV x Cebraspe;
- `research/CARTORIO_EXAM_ATLAS_WAVE6_REGIME_GERAL_HEATMAP_2026-09-10.md` — primeiro heatmap jurídico fino;
- `research/ENAC_DNA_CURRENT.md` — baseline atual de fases e Resolução 696/2026.

## Síntese

**O edital diz o que não pode faltar. O corpus diz onde a prova aperta. O grafo diz o que sustenta o quê. A banca diz como o conhecimento é disfarçado. A fase diz qual saída precisa ser produzida.**
