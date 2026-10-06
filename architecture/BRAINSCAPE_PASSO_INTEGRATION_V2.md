# BRAINSCAPE / PASSO / MRC INTEGRATION V2
**Data:** 05/10/2026
**Status:** vigente para reconstrução do C01 V2

## Princípio
Brainscape não é “um banco para copiar”. É um **corpus de engenharia de recuperação**.

A unidade de decisão não é o deck. É a pergunta.

Cada pergunta candidata é comparada com:
1. árvore curricular DD;
2. Claims auditados;
3. Gran/estrutura didática;
4. incidência de prova;
5. perguntas semelhantes em outros decks;
6. utilidade cognitiva para primeira aprendizagem e revisão.

## O que cada fonte faz melhor

### DD
- esqueleto;
- profundidade;
- terminologia;
- tópicos que não podem sumir.

### Gran
- gramática visual;
- ordem didática;
- síntese sem virar lista seca.

### Passo
- perguntas-mãe;
- revisão reconstrutiva;
- progressão natural de assunto.

### Brainscape
- descobrir boas formulações;
- detectar dúvidas recorrentes;
- aliases;
- decomposição de conceitos;
- resposta curta/rápida;
- lacunas entre teoria e recall.

### MRC / Trutas / OAB
- C/E;
- discriminação;
- aplicação;
- comentários curtos;
- lei seca.

### Provas reais
- árbitro de suficiência;
- linguagem;
- profundidade;
- distratores;
- autores/teorias que realmente aparecem.

## Três camadas de perguntas no material

### A. Perguntas progressivas de aprendizagem
Entram logo depois do tópico.
Podem ser mais granulares.
Função: aprender/reaprender.

### B. Perguntas-mãe de reconstrução
Entram no fechamento.
Função: reconstruir unidade inteira, estilo Passo/oral/discursiva.

### C. Aplicação
- C/E;
- mini-caso;
- questão real;
- alternativas comentadas.

Função: provar que o conhecimento é utilizável.

## Política de promoção de cards

Cada card candidato recebe um dos estados:

- `KEEP_CORE`: núcleo que merece recuperação própria;
- `KEEP_ADVANCED`: Delegado+/precisão;
- `MERGE_OR_CHILD`: conteúdo útil, mas melhor dentro da resposta/tabela ou como pergunta-filho condicional;
- `REWRITE_AUDIT`: tema útil, formulação atual insegura;
- `DEFER_OTHER_NODE`: pertence melhor a outro capítulo;
- `PENDING_EVIDENCE`: não promover sem evidência de cobrança;
- `REJECT`: redundante, confuso ou de baixo valor.

## Exemplo concreto do CSV Claude

### “O Direito Penal é formado só por regras?”
**Decisão:** `MERGE_OR_CHILD`.

A distinção regras/princípios é útil para entender a definição, mas não merece automaticamente um card nuclear no C01. Ela:
- pode aparecer dentro da explicação “conjunto de princípios e regras”;
- só vira pergunta própria se edital/prova/corpus mostrar valor;
- não deve abrir um desvio grande para teoria geral do Direito.

Esse é o tipo de card que parecia “natural” no material Claude, mas que o Tutor OS precisa filtrar.

## Autores e nomes próprios

Autor não entra porque “parece sofisticado”.

Promover autor se:
1. aparece em questão real;
2. é alias inseparável da teoria;
3. diferencia correntes cobradas;
4. é necessário para oral/discursiva;
5. DD + corpus mostram recorrência.

Exemplos:
- **Roxin × Jakobs** → CORE;
- **Liszt / Magna Carta do delinquente** → útil porque a fórmula cai;
- **Arturo Rocco** → precisão porque já apareceu como distrator de Delegado;
- definições individuais de vários autores → `PENDING_EVIDENCE` se não agregarem poder de resposta.

## Primeira triagem do CSV Claude

86 pares pergunta/resposta foram examinados.

Distribuição inicial:
- 37 `KEEP_CORE`
- 17 `KEEP_ADVANCED`
- 9 `KEEP_PARENT`
- 9 `MERGE_OR_CHILD`
- 6 `REWRITE_AUDIT`
- 4 `DEFER_OTHER_NODE`
- 2 `PENDING_EVIDENCE`
- 2 perguntas-mãe boas com resposta a reescrever

Conclusão: **não importar as 86 cegamente**.

A estrutura de duas velocidades é boa; o conteúdo precisa passar pelo filtro.

## Exemplos de reescrita obrigatória
- terceira via;
- Terza Scuola;
- função promocional;
- “corrente prevalece: Roxin” quando apresentada como absoluto;
- fórmulas de monista/dualista/radical/moderado sem contexto;
- Hassemer com Lei de Improbidade como se fosse implementação formal brasileira.

## Regra de revisão espaçada

O banco pode ter muitas perguntas.

O aluno não revisa todas sempre.

Seleção futura considera:
- CORE;
- incidência;
- erro individual;
- confiança;
- tempo de resposta;
- esquecimento;
- proximidade da prova.

Assim, o sistema pode ser rico sem virar sobrecarga diária.

## Regra final
Pergunta boa não é a mais bonita nem a mais “difícil”.

Pergunta boa:
- está no lugar certo da progressão;
- usa linguagem jurídica real;
- recupera algo que foi ensinado;
- melhora capacidade de resolver prova;
- tem resposta suficientemente explicativa;
- não duplica outro item sem ganho cognitivo.
