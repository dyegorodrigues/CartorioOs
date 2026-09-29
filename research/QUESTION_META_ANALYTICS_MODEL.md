# GX Cartório OS — Question Meta-Analytics Model

## Objetivo
Transformar corpus de questões em decisões pedagógicas sem confundir frequência bruta com probabilidade real de cobrança.

## Quatro modelos separados
### 1. Domain Incidence Model
Pergunta: **o que o domínio de concursos de cartório cobra?**

Usa concursos de cartório multibanca e, com peso menor, carreiras jurídicas comparáveis para microtemas comuns.

### 2. Bank Style Model
Pergunta: **como a banca formula e discrimina?**

Restrito a banca + janela temporal + família de concurso + fase.

### 3. Phase Performance Model
Pergunta: **como o mesmo conhecimento é exigido em objetiva, discursiva, prática e oral?**

Mapeia answer atoms, profundidade, necessidade de fundamentação, integração e pressão temporal.

### 4. Temporal Drift Model
Pergunta: **o comportamento de cobrança mudou?**

Compara janelas temporais, mudanças normativas, alterações de edital e mudanças de banca/família de certame.

## Features quantitativas candidatas
- frequência absoluta e relativa normalizada pelo tamanho da prova;
- cobertura por tema/subtema/microtema;
- recorrência entre edições;
- persistência temporal;
- intervalo desde a última cobrança;
- diversidade de bancas;
- diversidade de fases;
- densidade de casos;
- tamanho/complexidade do enunciado;
- incidência de jurisprudência;
- incidência de CNJ/regulação operacional;
- recência da fonte jurídica;
- interdisciplinaridade;
- taxa de comandos negativos;
- mecanismo de distrator;
- índice de anulação/controvérsia;
- complexidade jurídica L1–L4.

## Features qualitativas/semânticas
- conceito nuclear exigido;
- variável decisiva;
- tipo de raciocínio;
- confusões exploradas;
- fonte jurídica dominante;
- linguagem típica;
- forma de contextualização;
- padrão de repergunta/oral;
- answer atoms esperados;
- conexões entre microtemas.

## Predição
Nenhuma “chance de cair” é canônica por frequência simples.

Quando houver amostra suficiente, preferir:
- probabilidades calibradas;
- intervalos de incerteza;
- shrinkage/hierarquia para microtemas com poucos itens;
- separação por banca e fase;
- backtest temporal, treinando em anos anteriores e testando em anos posteriores;
- comparação contra baseline simples.

Se modelo sofisticado não superar baseline simples fora da amostra, não será usado para priorização.

## Sinais de prioridade
A prioridade de estudo pode combinar:
- superfície/obrigatoriedade no edital;
- incidência de domínio;
- estilo da banca-alvo;
- valor de transferência;
- dependências;
- confusabilidade;
- volatilidade normativa;
- mastery/retention individual;
- fase-alvo;
- incerteza do próprio modelo.

Baixa incidência nunca implica exclusão automática.

## Meta-análise de alternativas
Por questão objetiva, classificar cada alternativa quando útil:
- correta por regra direta;
- errada por competência;
- errada por requisito;
- errada por prazo/momento;
- errada por efeito;
- errada por legitimidade;
- errada por exceção;
- errada por instituto próximo;
- errada por jurisprudência superada;
- errada por literalidade/lista;
- errada por excesso/absolutização.

## Comentários de terceiros
Comentários de QConcursos, TEC, cursinhos e doutrina podem explicar raciocínio ou revelar controvérsia, mas não substituem:
1. gabarito/espelho oficial;
2. resposta a recurso;
3. fonte jurídica primária;
4. snapshot vigente.

## Direito histórico × atual
Toda série 2010–presente precisa separar mudança de cobrança de mudança do próprio Direito. Não atribuir à banca uma mudança de estilo quando a explicação suficiente é alteração legislativa/jurisprudencial.

## Regra anti-pseudo-ciência
Não produzir percentuais de previsão apenas porque o sistema consegue calculá-los. A precisão exibida deve ser compatível com tamanho e qualidade da amostra.