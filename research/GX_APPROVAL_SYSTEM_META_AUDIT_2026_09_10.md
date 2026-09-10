# GX Cartório OS — Meta-auditoria do sistema de aprovação

Data: 2026-09-10
Status: PESQUISA / CONTRATO DE PROJETO, não material de estudo

## Decisão executiva

O candidato NÃO iniciará estudo nesta etapa. O objetivo atual é construir, auditar e demonstrar a máquina editorial e pedagógica antes de ativar o runtime de estudo.

O GX não deve exigir que o candidato compreenda sua arquitetura interna. A interface learner-facing futura deve parecer simples: mapa claro → conteúdo → lei seca guiada → recuperação → questões → revisão → avanço. Toda engenharia de edital, fontes, corpus, atualização, profundidade e telemetria fica nos bastidores.

## 1. Achados estruturais de alta confiança

### 1.1 O concurso atual exige duas otimizações diferentes

ENAC 2026.2: 100 questões objetivas, com distribuição atual de 60 N/R, 14 Civil, 8 Constitucional, 4 Administrativo, 4 Tributário, 4 Empresarial, 2 Processo Civil, 1 Penal, 1 Processo Penal, 1 Trabalho e 1 Processo do Trabalho.

A Resolução CNJ 696/2026 estabelece, no modelo estadual, objetiva eliminatória e sem peso final; discursiva = 70%; oral = 25%; títulos = 5%.

Consequência: o GX não pode ser nem um curso de objetiva disfarçado, nem um curso de segunda fase aplicado a um iniciante. Precisa haver cobertura objetiva permanente + produção progressiva apenas quando houver repertório.

### 1.2 Há um filtro de eficiência enorme por disciplina

A Resolução 696/2026 determina que Penal, Processo Penal, Trabalho e Processo do Trabalho sejam exigidos exclusivamente no ENAC e na prova objetiva.

Consequência: no baseline nacional atual, não se gasta orçamento curricular de discursiva/oral/peça nessas quatro disciplinas. Isso é um exemplo de eficiência baseada em regra oficial, não em palpite.

### 1.3 O edital atual desmonta a importação cega de materiais de Delegado

No ENAC 2026.2, Direito Penal tem apenas 1 questão e o programa começa por Aplicação da Lei Penal (arts. 1–12), Crime (13–25), Imputabilidade, Concurso de Pessoas, Penas etc., além de tipos/leis selecionados. Não há, como item autônomo, um grande bloco de teoria do bem jurídico, escolas penais ou aprofundamentos doutrinários gerais.

Materiais de Delegado podem revelar nomenclaturas ou armadilhas transferíveis, mas sua profundidade não pode ser importada para Cartório sem exam proof específico.

### 1.4 Poder Constituinte é, de fato, o item 1 de Constitucional no ENAC 2026.2

Isso não torna Teoria da Constituição inteira um pré-requisito. O GX deve fornecer apenas um bootstrap mínimo para que um aluno enferrujado compreenda o nó, sem criar um curso paralelo antes do edital.

## 2. O que a autópsia dos PDFs antigos mostrou

### Padrão Estratégia
- boa linearidade de sumário e separação por temas;
- banco de questões por carreiras pode ajudar a enxergar transferência;
- quadros comparativos são úteis quando comprimem uma decisão real;
- risco: materiais simplificados/revisão pressupõem uma base em outro produto;
- risco: material de carreira diferente transporta profundidade e seleção inadequadas para Cartório.

### Padrão Dedicação Delta
- boa integração de lei, alertas, questões e alguns contrastes;
- boa ideia funcional de separar artigos relacionados de artigos prioritários para leitura literal;
- risco: núcleo, aprofundamento, autores, controvérsias, nomenclaturas e questões recentes aparecem muitas vezes no mesmo plano visual;
- isso faz conteúdo raro parecer tão urgente quanto conteúdo nuclear;
- o candidato perde a noção de endereço lógico e prioridade.

### Regra derivada
Profundidade disponível ≠ profundidade obrigatória na primeira passagem.

Cada proposição deve receber estado explícito:
- CORE-P1: aprender na primeira passagem;
- MEM: memorizar literalmente ou reconstruir com alta precisão;
- DISC: discriminar de instituto parecido / pegadinha;
- P2/P3: aprofundar apenas em passagem posterior;
- OUTPUT: relevante para discursiva/oral/prática;
- REF: referência consultável, sem cobrança de retenção ordinária;
- REJECT: não justifica custo no alvo atual.

## 3. Ciência da aprendizagem: o que entra e o que NÃO vira religião

### Entra
- retrieval practice: recuperar ativamente depois de aquisição;
- spacing: reaparecimento ao longo do tempo;
- successive relearning: recuperar até desempenho adequado e reaprender em sessões espaçadas;
- worked examples / scaffolding para novatos em tarefas complexas;
- guidance fading: retirar apoio conforme o esquema mental se forma;
- interleaving quando a finalidade é discriminar categorias/institutos semelhantes.

### Não entra como dogma
- número fixo universal de questões por dia;
- 24h/7d/30d como calendário rígido para todo conteúdo;
- flashcard para cada frase;
- interleaving caótico desde M0;
- discursiva completa antes de repertório;
- transformar tempo de bloco em carga diária fixa.

A cadência deve ser adaptativa por esquecimento, valor probatório, erro, velocidade e horizonte.

## 4. Evidência qualitativa de aprovados em Cartório

Entrevistas de aprovados mostram recorrência de alguns comportamentos, sem constituírem fórmula causal universal:
- resolução muito volumosa de questões ao longo de meses/anos;
- lei seca presente, especialmente perto das provas;
- revisão por questões e material próprio/trechos selecionados;
- foco muda após aprovação de fase: treino de peça/discursiva e depois oral;
- simulados e treino de fala aparecem na preparação específica de oral;
- candidatos diferentes estudam 1 ou 2 disciplinas/dia e têm cargas horárias muito diferentes.

Regra GX: extrair invariantes úteis, não copiar cronograma pessoal de aprovado.

## 5. Novo modelo: Evidence-to-Mastery Compiler

### Motor A — Compiler curricular, invisível ao candidato

1. INGEST OFFICIAL SCOPE
   - edital vigente + resolução + retificações.
2. SOURCE REGISTRY
   - Constituição/leis/CNJ/STF/STJ e demais autoridades necessárias.
3. EXAM CORPUS
   - ENAC;
   - estaduais de outorga, todas as bancas relevantes;
   - FGV prioritária;
   - carreiras jurídicas adjacentes somente como transfer evidence.
4. PROPOSITION EXTRACTION
   - cada questão vira proposição jurídica, operação cognitiva, distrator, fonte, fase, banca, data e dificuldade.
5. INCIDENCE x CONSEQUENCE
   - frequência não é suficiente; considera também poder de discriminar candidato e importância para fases posteriores.
6. DEPTH BUDGET
   - determina P1/P2/P3/OUTPUT/REF.
7. CANONICAL KNOWLEDGE TREE
   - uma árvore lógica única, com One-Home Rule e Terminology Registry.
8. BUILD / VALIDATION / CHALLENGE SPLIT
   - parte do corpus fica escondida da redação para testar suficiência.
9. FRESHNESS FIREWALL
   - verifica vigência, superação, edição normativa e snapshot temporal.
10. PATCH LOOP
   - questão legítima não resolvível pelo material → CONTENT/DISCRIMINATION/STRUCTURE/FRESHNESS GAP → corrigir nó canônico.

### Motor B — superfícies learner-facing

Todas derivadas da MESMA árvore:

1. MAPA DE ENTRADA
   - onde estamos, para que serve, o que vem antes/depois, peso e operação principal.
2. MASTER P1
   - primeira exposição progressiva, suficiente para construir esquema + começar objetiva.
3. LEI SECA GUIADA
   - artigos exatos + o que notar + o que memorizar + por que é cobrado.
4. REVIEW
   - compressão da mesma árvore, sem reorganizar a matéria de outro jeito.
5. Q→A / RECALL
   - varredura do módulo por perguntas, respostas recolhíveis/ocultáveis.
6. OBJECTIVE LAB
   - aprendizagem → discriminação → mista → cronometrada → multibanca → held-out.
7. OUTPUT LAB
   - apenas nos nós/fases pertinentes: átomos → esqueleto → parágrafo → discursiva/peça → oral → repergunta.
8. ERROR PATCH
   - erro pessoal vira patch no endereço canônico correto, não uma pilha paralela de caderno de erros.

## 6. Estratégia de cobertura: não tentar M7 antes de seguir

### Passagem 1 — Cobertura + esquema + sobrevivência objetiva
Objetivo: atravessar o edital inteiro em profundidade P1 adequada, formar mapas e chegar a reconhecimento/recuperação/discriminação objetiva básica.

### Passagem 2 — Dureza de prova
Objetivo: aprofundar somente onde corpus mostrou retorno: jurisprudência, exceções, nomenclaturas, controvérsias, casos, multibanca e mistura.

### Passagem 3+ — robustez e produção
Objetivo: manter objetiva afiada e expandir escrita/prática/oral nos nós pertinentes; inserir overlays estaduais e DNA da banca concreta.

Nós de alta relevância podem amadurecer para OUTPUT antes de a primeira passagem global terminar. O sistema é assíncrono por nó, não uma escada única.

## 7. Definição operacional de 'material autossuficiente'

Nunca mais declarar 'com este material você resolve qualquer questão' por opinião da própria IA.

Um material recebe selo de suficiência somente para um ESCOPO + NÍVEL + SNAPSHOT definidos e após:
- validation set não usado para redigir;
- challenge set multibanca/transferível;
- source check;
- ausência de gap legítimo relevante;
- desempenho do candidato após intervalo.

Suficiência é graduada:
- S0 não testado;
- S1 build-covered;
- S2 validation-covered;
- S3 multibank/challenge-covered;
- S4 learner-demonstrated;
- S5 maintenance-stable.

Nunca usar '100% completo' como afirmação absoluta sobre provas futuras.

## 8. Calibração editorial pareada

O B0 deixa de depender de um único tema que o candidato não lembra bem.

### Specimen A — Direito Penal, Aplicação da Lei Penal
Função: auditoria humana de legibilidade/ordem usando um domínio mais familiar. Como Penal é objetivo-only no regime nacional atual, esse specimen também demonstra poda agressiva de profundidade inútil.

### Specimen B — Constitucional, Poder Constituinte
Função: provar transformação cross-phase porque Constitucional pode chegar à discursiva/oral e há histórico de cobrança cartorária.

O candidato não estudará nenhum deles nesta fase. São protótipos para inspeção.

## 9. Critério para liberar o estudo real

Somente depois de existir um specimen que demonstre:
- primeira exposição confortável;
- árvore lógica evidente;
- marcação inequívoca do que ENTENDER / MEMORIZAR / RECONHECER / APROFUNDAR DEPOIS;
- lei seca localizada;
- revisão realmente curta;
- Q→A que reconstrói o módulo;
- objetiva real ou QA-validada;
- prova de suficiência baseada em held-out;
- throughput plausível para 2027;
- nenhum incentivo para o candidato microgerenciar o sistema.

## Fontes externas principais verificadas nesta auditoria
- CNJ, Resolução 696/2026: https://atos.cnj.jus.br/atos/detalhar/7011
- FGV, ENAC 2026.2: https://conhecimento.fgv.br/exames/enac/4exame
- Nature Reviews Psychology, spacing/retrieval: https://www.nature.com/articles/s44159-022-00089-1
- Rawson & Dunlosky, successive relearning: https://www.psychologicalscience.org/journals/current-directions/09637214221100484/
- Educational Psychology Review, cognitive load / expertise reversal: https://link.springer.com/article/10.1007/s10648-023-09817-2

## Próxima entrega
Construir os dois specimens learner-facing sem ativar estudo, começando pelo Specimen A, e submetê-los à auditoria: old-material red-team + corpus real + source check + compression check + held-out design.