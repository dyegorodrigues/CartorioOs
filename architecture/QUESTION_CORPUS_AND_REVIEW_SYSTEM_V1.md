# Arquitetura do Corpus de Questões, Prompts e Revisão — V1
**Data:** 05/10/2026
**Status:** vigente para o piloto PEN-DP01-C01

## 1. Problema que esta arquitetura resolve

O projeto terá milhares de objetos de aprendizagem provenientes de fontes muito diferentes:
- questões oficiais;
- perguntas subjetivas do tipo Passo Estratégico;
- cards/decks Brainscape;
- assertivas C/E de decks Anki/MRC;
- lei seca ativa;
- questões discursivas, peças e oral;
- perguntas autorais do Tutor OS.

Tratar tudo como “flashcard” destruiria a informação de origem, finalidade e profundidade.

## 2. Três bancos lógicos

### A. EXAM CORPUS — cobrança real
Uma linha por questão/item oficial ou por unidade avaliativa oficial.

Campos mínimos:
- `question_id`
- disciplina / módulo / tópico / microtópico / claim_ids
- banca
- concurso/carreira/órgão
- ano e data
- fase: objetiva/discursiva/prática/oral
- número/caderno
- fonte oficial
- gabarito preliminar e definitivo
- situação: válida/anulada/controvertida
- complexidade
- mecanismo de cobrança
- mecanismo de distrator
- normas/jurisprudência relacionadas
- snapshot jurídico da época
- revisão à luz do direito atual
- comentário editorial
- status de ingestão/auditoria

**Objetivo:** dizer o que realmente foi cobrado e como.

### B. LEARNING PROMPT CORPUS — recuperação e aprendizagem
Uma linha por pergunta útil observada ou construída.

Origem possível:
- Passo Estratégico
- Brainscape
- MRC/Anki
- material antigo do usuário
- questão oficial transformada
- autoria Tutor OS

Campos:
- `prompt_id`
- `source_id`
- localização no deck/material
- tópico/microtópico/claim_ids
- função cognitiva
- posição pedagógica
- estilo da pergunta
- granularidade
- pré-requisitos
- qualidade estimada
- problemas detectados
- decisão: `mine_pattern / candidate / reject / adapted`

**Importante:** no repositório público, não guardar cópia integral de bancos comerciais/decks de terceiros. Guardar metadados, sínteses e padrões. Texto integral só quando juridicamente permitido e necessário em plano controlado.

### C. ANSWER PATTERN CORPUS — como responder bem
Não é conteúdo jurídico independente. Classifica formatos de resposta que funcionam.

Exemplos:
- definição nuclear + explicação;
- tabela comparativa;
- resposta comentada + resposta-relâmpago;
- C/E + fundamento;
- regra + exceção + exemplo;
- questão comentada alternativa por alternativa;
- resposta oral de 30s / 90s;
- rubrica discursiva por answer atoms.

**Objetivo:** separar “o que ensinar” de “como apresentar a resposta”.

## 3. Taxonomia de função cognitiva

- `orientation` — situa o aluno / mapa;
- `learning` — ajuda a aprender ou reaprender;
- `recall_parent` — pergunta-mãe;
- `recall_precision` — detalhe necessário;
- `contrast` — diferencia institutos;
- `law_literal` — lei seca;
- `true_false` — julgamento C/E;
- `application` — caso/alternativa;
- `exam_official` — questão oficial;
- `discursive` — produção escrita;
- `oral` — produção oral;
- `practical` — peça/procedimento.

## 4. Relação com a árvore curricular

A árvore DD/editais é a espinha.

Cada item do corpus aponta para:
`subject -> booklet -> module -> topic -> microtopic -> claim`

O corpus NÃO cria a árvore por popularidade de cards.

O fluxo correto é:
1. árvore curricular;
2. Claims/conteúdo;
3. mapear perguntas/questões para os nós;
4. detectar nós sem treino;
5. detectar perguntas sem fundamento curricular;
6. corrigir cobertura.

## 5. Cobertura comparativa

Para cada microtópico o sistema poderá responder:

| Pergunta | Exemplo de saída futura |
|---|---|
| DD ensina? | sim / parcial / não |
| Gran ensina? | sim / parcial / não |
| Passo pergunta? | 3 prompts relevantes |
| Brainscape pergunta? | 17 prompts em 5 decks |
| MRC possui assertiva? | 4 |
| Questões oficiais? | 12 |
| Objetiva? | 10 |
| Discursiva/oral? | 2 |
| Lei seca conectada? | 1 art. |
| Material Tutor OS cobre? | sim / bug curricular |

Esse quadro permite comparar teoria × recuperação × prova.

## 6. Banco oficial não é banco de comentários aleatórios

Comentários de QConcursos, TEC, cursinhos, professores e alunos podem ser minerados em camada separada:

`commentary_candidate`

Registrar:
- origem;
- autor/tipo quando disponível;
- qual raciocínio explica;
- se traz fonte;
- se diverge do gabarito;
- se revela controvérsia;
- decisão editorial.

Nunca substituir automaticamente:
1. gabarito/espelho oficial;
2. recurso oficial;
3. fonte jurídica primária.

## 7. Escala

Não gerar um arquivo por questão.

Armazenamento lógico:
- CSV/JSONL particionado por matéria/ano ou módulo;
- índices leves no GitHub;
- textos integrais/artefatos volumosos em plano controlado;
- builders geram apenas o recorte necessário para estudo.

Exemplo:
`corpus/exams/penal/2025.jsonl`
`corpus/prompts/penal/dp01.jsonl`
`corpus/answer_patterns/registry.json`

## 8. Repetição sem duplicação

Uma questão pode testar cinco Claims.
Um Claim pode aparecer em cinquenta questões.
Uma pergunta-mãe pode substituir oito microcartões redundantes.

Não duplicar teoria dentro de cada pergunta. Ligar por IDs.

## 9. Revisão espaçada futura

O conteúdo canônico fica no corpus.
O estado do aluno fica separado e privado:
- última tentativa;
- acerto;
- confiança;
- latência;
- tipo de erro;
- próxima revisão.

Isso permite mudar o algoritmo de revisão sem duplicar os cards.

## 10. Regra de pesquisa Brainscape/Passo

Cada deck/material recebe primeiro uma ficha de fonte:
- escopo;
- número de cards;
- ordem;
- densidade;
- estilo dominante;
- qualidade de respostas;
- lacunas;
- nível;
- atualização aparente.

Depois, para o microtópico atual:
1. ler cards pertinentes;
2. classificar função;
3. mapear para árvore;
4. detectar duplicatas semânticas;
5. registrar formulações especialmente boas;
6. auditar juridicamente;
7. só então adaptar/criar prompt Tutor OS.

## 11. Preferência do usuário

Não presumir um único estilo.

Construir um **Calibration Set** com amostra representativa:
- pergunta-mãe curta;
- pergunta-mãe + resposta longa;
- resposta em tabela;
- resposta comentada + turbo;
- C/E comentado;
- mini-caso;
- comparação.

O usuário avalia exemplos lado a lado. A escolha calibra renderização e proporção de estilos, não a correção jurídica.

## 12. Gate de promoção

Um prompt só vira item do aluno quando:
- conteúdo-base está auditado;
- pergunta é clara e progressiva;
- resposta ensina/revisa;
- nomenclatura de prova está preservada;
- granularidade tem justificativa;
- não há item melhor cobrindo a mesma função;
- há vínculo com Claim(s);
- se volátil, freshness audit concluída.
