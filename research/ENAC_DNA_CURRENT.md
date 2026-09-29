# DNA ATUAL — ENAC + Concursos Estaduais

Status: baseline v0.2 — reconciliado em 14/09/2026 com a Resolução CNJ 696/2026 e o Edital do 4º ENAC 2026.2.

Este documento descreve **estrutura de avaliação e consequências para preparação**. A mega-árvore e a metodologia de meta-análise ficam em `research/ENAC_EDITAL_MEGA_TREE_META_ANALYSIS_2026-09-14.md`.

## 1. Estrutura nacional vigente

A Resolução CNJ 696/2026 tornou a habilitação no ENAC requisito obrigatório para inscrição preliminar nos concursos estaduais. O certificado de habilitação tem validade de seis anos, ressalvadas as regras específicas da resolução.

### ENAC 2026.2

100 questões de múltipla escolha:

- Direito Notarial e Registral: 60;
- Direito Civil: 14;
- Direito Constitucional: 8;
- Direito Administrativo: 4;
- Direito Tributário: 4;
- Direito Empresarial: 4;
- Direito Processual Civil: 2;
- Direito Penal: 1;
- Direito Processual Penal: 1;
- Direito do Trabalho: 1;
- Direito Processual do Trabalho: 1.

A matriz deve privilegiar raciocínio e resolução de problemas relacionados à atividade notarial e registral.

## 2. ENAC não é sinônimo de prova objetiva estadual

O ENAC é a habilitação nacional prévia. Já o concurso estadual pode possuir prova objetiva própria ou substituí-la pelo ENAC, conforme o edital e a Resolução 696/2026.

Quando houver **prova objetiva estadual própria**, a passagem para a prova discursiva exige cumulativamente:

1. pelo menos **50% de acertos em Direito Notarial e Registral**;
2. pelo menos **60% de acertos no total da objetiva**;
3. classificação dentro do limite de até **12 candidatos por vaga**, ressalvadas as regras específicas de ações afirmativas previstas na resolução.

Consequência arquitetural: manter separados `ENAC_PASS_RISK` e `STATE_OBJECTIVE_RANK_RISK`. Passar no ENAC não demonstra, por si só, competitividade em uma objetiva estadual classificatória por corte posicional.

## 3. Concurso estadual sob a Resolução 696/2026

Etapas relevantes para preparação:

- prova objetiva, quando prevista, eliminatória e sem peso na nota final, podendo ser substituída pelo ENAC;
- prova discursiva;
- prova oral;
- títulos;
- demais etapas habilitatórias/documentais previstas na resolução.

### Peso classificatório final

- Discursiva: **70%**;
- Oral: **25%**;
- Títulos: **5%**.

### Discursiva

A resolução exige, no mínimo:

- 1 dissertação;
- 1 peça prática;
- 3 questões discursivas.

Para prosseguir à prova oral, o candidato precisa atingir o mínimo previsto na resolução, correspondente a **60% dos 70 pontos da discursiva = 42 pontos**.

A preparação deve decompor cada saída em problemas, fundamentos, aplicação e conclusão, preservando a gramática concreta exigida por cada edital/banca.

### Oral

A prova oral vale 25 pontos e é **exclusivamente classificatória**. A composição normativa da nota reserva **90% ao conteúdo jurídico** e **10% à articulação técnica objetiva**, nos termos da Resolução 696/2026.

### Títulos

Valem 5% da nota final.

## 4. Disciplinas e teto de profundidade por fase

A Resolução 696/2026 determina que:

- Direito Penal;
- Direito Processual Penal;
- Direito do Trabalho;
- Direito Processual do Trabalho

sejam cobrados exclusivamente no ENAC e na prova objetiva estadual, quando esta existir.

Logo o núcleo nacional que precisa sustentar **produção discursiva/prática/oral** concentra-se em sete disciplinas:

1. Direito Notarial e Registral;
2. Direito Constitucional;
3. Direito Civil;
4. Direito Administrativo;
5. Direito Tributário;
6. Direito Processual Civil;
7. Direito Empresarial.

Isso não elimina as quatro matérias objetivas. Apenas altera o `OUTPUT DEPTH` exigido.

## 5. Núcleo nacional + overlay estadual

A Resolução 696/2026 estrutura conteúdo e matriz de competências nacionais. O edital estadual pode acrescentar conteúdo local oficialmente delimitado, como Constituição/Lei Orgânica local, legislação estadual/distrital, código de normas e atos do respectivo Tribunal/Corregedoria.

Consequência arquitetural:

- `National Core`: conhecimento reaproveitável nacionalmente;
- `State Overlay`: delta local por concurso.

O overlay deve ser versionado e nunca contaminar o núcleo nacional como se fosse regra brasileira geral.

## 6. Corpus obrigatório da engenharia reversa

### ENAC oficial

- 2025.1: caderno + gabarito definitivo + recursos oficiais quando disponíveis;
- 2025.2: idem;
- 2026.1: idem;
- 2026.2: edital vigente; prova a incorporar após aplicação.

Passagem 1 atual: **300/300 itens históricos indexados/classificados**, com 6 anulações preservadas. Isso não significa 300 questões juridicamente reconstruídas alternativa por alternativa.

### Concursos estaduais

Priorizar concursos recentes, mantendo `REGIME_TAG`, `PHASE_VALIDITY` e `CONTENT_VALIDITY`.

- FGV Cartório amplia simultaneamente evidência de domínio e estilo FGV;
- Cebraspe/Vunesp/IESES/Consulplan e outras bancas ampliam evidência de domínio e robustez;
- provas escritas, peças e espelhos são especialmente valiosos para definir `OUTPUT DEPTH`.

### FGV de outras carreiras

ENAM, magistratura, MP, Defensoria, Procuradorias e exames comparáveis podem informar **gramática FGV** quando microtema, complexidade e operação cognitiva forem compatíveis.

Não contam como incidência de Cartório e não aumentam artificialmente o tamanho da amostra ENAC.

## 7. Dois estimadores separados

### Domain Incidence Model

Pergunta: `o que concursos de Cartório cobram?`

Pode combinar ENAC + concursos estaduais multibanca, mantendo proveniência e fase.

### Bank Style Model

Pergunta: `como a banca X constrói avaliação?`

Restringe-se à banca, janela temporal, família de exame, complexidade e fase pertinentes.

Regra anti-contaminação: uma questão Cebraspe pode reforçar que um instituto é relevante para Cartório; ela não altera o perfil de distratores da FGV.

## 8. Evidência atual do estilo FGV

A evidência ENAC + FGV estadual recente sustenta, em diferentes graus:

- uso frequente de casos contextualizados;
- cartorialização de matérias externas;
- aplicação combinada de mais de um diploma/nó;
- alternativas decididas por competência, sujeito, requisito, prazo, exceção ou efeito jurídico;
- `near-literal traps`, em que um conectivo ou qualificador muda a conclusão;
- `boundary traps`, com limites numéricos e categorias próximas;
- `role swaps`, como direito/dever, regra/exceção e sujeito/competência;
- `alternative bundling`, em que uma proposição errada derruba a alternativa inteira;
- relevância prática de freshness em atos CNJ, sistemas eletrônicos, desjudicialização e mudanças legislativas;
- em escrita/prática, casos multiproposição e espelhos decomponíveis em átomos jurídicos.

Esses sinais orientam treino. Não são uma teoria eterna da banca e não autorizam percentuais finos sem corpus comparável maior.

## 9. Taxonomia de análise de cada questão

Cada questão relevante deve receber:

- exame, ano e banca;
- disciplina formal;
- tema/subtema/microtema;
- especialidade extrajudicial;
- fonte principal e secundária;
- fase;
- `REGIME_TAG`;
- operação cognitiva;
- tipo de caso;
- estrutura do comando;
- mecanismo dos distratores;
- alteração normativa posterior;
- gabarito preliminar/definitivo/anulação;
- rationale oficial de recurso, quando houver;
- snapshot histórico e snapshot atual;
- potencial de transferência para objetiva/discursiva/peça/oral.

## 10. Métricas da meta-análise

### Quantitativas defensáveis

- frequência agregada por disciplina/cluster;
- recorrência por edição/banca com denominador explícito;
- concentração por especialidade;
- distribuição de operação cognitiva;
- fonte/diploma em células com amostra suficiente;
- mecanismos de distrator em amostra QA-validada;
- anulação/controversa.

### Qualitativas

- literalidade vs aplicação;
- profundidade jurídica;
- arquitetura dos distratores;
- formato do caso;
- integração normativa;
- densidade de atualização normativa.

### Semânticas

Agrupar itens diferentes que testam a mesma proposição nuclear, preservando aliases e snapshots jurídicos.

### Preditivas

Gerar **índice de prioridade**, nunca profecia de incidência. Combinar, com incerteza explícita:

- peso oficial;
- recorrência de domínio;
- evidência da banca-alvo;
- centralidade/pré-requisito;
- confusabilidade;
- transferibilidade entre fases;
- consequência de erro;
- volatilidade normativa;
- custo de aprendizagem;
- dificuldade e retenção individuais quando houver telemetria real.

## 11. Fontes-base

- CNJ Resolução 696/2026: https://atos.cnj.jus.br/atos/detalhar/7011
- FGV ENAC: https://conhecimento.fgv.br/exames/exame-nacional-dos-cartorios-enac
- FGV ENAC 2026.2: https://conhecimento.fgv.br/exames/enac/4exame
- FGV ENAC 2026.1: https://conhecimento.fgv.br/exames/enac/3exame
- FGV ENAC 2025.2: https://conhecimento.fgv.br/exames/enac/2exame
- FGV ENAC 2025.1: https://conhecimento.fgv.br/exames/enac/1
- Código Nacional de Normas: https://atos.cnj.jus.br/atos/detalhar/5243

## 12. Regra operacional

**Edital define cobertura. Evidência define profundidade. Grafo define ordem. Banca define embalagem. Telemetria real define adaptação individual.**
