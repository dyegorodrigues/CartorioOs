# ENAC 300 — Meta-análise auditada

Data: 14/09/2026  
Status: **CANÔNICO PARA FATOS MEDIDOS / PARCIAL PARA CAMPOS AINDA INCOMPLETOS**

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

A auditoria direta no Question Intelligence Lab encontrou:

## 3.1 Relação questão → currículo

| Edição | Ligadas | Órfãs |
|---|---:|---:|
| 2025.1 | 0 | **100** |
| 2025.2 | 72 | **28** |
| 2026.1 | 99 | **1** |
| **Total** | **171** | **129** |

Cobertura relacional: **57,0%**.

Portanto ainda é proibido publicar um ranking quantitativo fino por nó da mega-árvore como se todo o corpus estivesse mapeado.

## 3.2 Família da fonte

Campo preenchido em 200/300; o ENAC 2026.1 ainda está 100/100 vazio nesse atributo.

Nos **200 itens efetivamente anotados** (2025.1 + 2025.2):

| Família predominante | n | % de 200 |
|---|---:|---:|
| Constituição/lei/código | 77 | **38,5%** |
| Mista | 43 | **21,5%** |
| CNJ/Corregedoria | 33 | **16,5%** |
| STF/STJ/TJ | 31 | **15,5%** |
| Regulação operacional | 13 | **6,5%** |
| Doutrina | 3 | **1,5%** |

Isto não significa que somente 15,5% das questões “usem jurisprudência”. O campo registra a família predominante da passagem 1 e ainda não representa todas as fontes decisivas/auxiliares de cada item.

## 3.3 Mecanismo do distrator

Campo preenchido em 200/300; ENAC 2026.1 ainda está 100/100 sem essa tag.

O campo é multi-select. Uma questão pode conter múltiplos mecanismos.

| Mecanismo | Questões com a tag | % de 200 |
|---|---:|---:|
| Requisito | 155 | **77,5%** |
| Efeito jurídico | 133 | **66,5%** |
| Competência | 63 | **31,5%** |
| Exceção | 57 | **28,5%** |
| Conceito próximo | 56 | **28,0%** |
| Literalidade/lista | 51 | **25,5%** |
| Prazo/momento | 33 | **16,5%** |
| Judicialização | 19 | **9,5%** |
| Responsabilidade | 19 | **9,5%** |
| Legitimidade | 10 | **5,0%** |

### Sinal mais robusto até aqui

Nas duas edições anotadas separadamente, `Requisito` e `Efeito jurídico` permanecem em 1º e 2º lugares:

- 2025.1: requisito 82; efeito 74;
- 2025.2: requisito 73; efeito 59.

Isso sustenta uma hipótese forte de desenho pedagógico: para grande parte do conteúdo, saber apenas “o conceito” é insuficiente. É preciso ensinar **regra → requisito → limite → consequência**.

Ainda não rotular esses percentuais como `DNA 300` até anotar e revisar 2026.1.

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

Mesmo após este fechamento, permanecem proibidos:

- “tema X tem 83% de chance de cair”;
- ranking completo por 330 nós com base em apenas 171 relações;
- porcentagem 300/300 de mecanismos de distrator;
- porcentagem 300/300 de família de fonte;
- tendência temporal forte com três edições;
- inferir irrelevância porque o tema não apareceu em três provas;
- usar outra banca para fabricar amostra de estilo FGV;
- usar questão histórica sem revalidar o Direito atual;
- confundir indexação 300/300 com reconstrução jurídica 300/300.

---

# 11. Próximo lote empírico obrigatório

A arquitetura da meta-análise está suficientemente fechada. O próximo ganho real vem de reparar dados e reconstruir itens, não de criar mais camadas conceituais.

Ordem operacional:

1. relacionar os 129 itens órfãos aos nós curriculares;
2. preencher família de fonte do ENAC 2026.1;
3. preencher mecanismos de distrator do ENAC 2026.1;
4. executar QA cego amostral contra cadernos oficiais;
5. recalcular estatísticas 300/300;
6. produzir Reconstruction Cards pelos clusters que entram no material;
7. cruzar esses nós com FGV estadual e Cartório multibanca;
8. criar Depth Budgets por proposição/cluster;
9. manter held-out separado antes de validar material.

---

# 12. Artefatos relacionados

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
