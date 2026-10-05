# Perguntas ligadas ao conteúdo

Uma linha JSON por pergunta em `questions.jsonl`. Banco vazio significa trabalho pendente; não gerar centenas de itens genéricos para preencher contagens.

Campos obrigatórios:

| Campo | Uso |
|---|---|
| `id` | Identificador global estável |
| `kind` | `learning`, `recall`, `comparison`, `application`, `official`, `oral` ou `discursive` |
| `origin` | `authored`, `adapted` ou `official` |
| `prompt` | Pergunta clara, com pré-requisitos compatíveis |
| `answer` | Resposta correta |
| `explanation` | Explicação suficiente e raciocínio; não repetir o gabarito |
| `topic_ids` | Um ou mais tópicos ensinados no catálogo |
| `source_ids` | Fontes verificáveis registradas |
| `law_ids` | Zero ou mais dispositivos versionados |
| `requires_question_ids` | Pré-requisitos entre perguntas, quando necessários |
| `difficulty` | `very_easy`, `easy`, `medium`, `hard`, `very_hard`; estimativa editorial |
| `order` | Ordem pedagógica local; não representa frequência em prova |
| `review_status` | `draft`, `needs_review` ou `reviewed` |

Para `reviewed`, exigir `review.checked_at` e `review.basis_digest`, obtido pela função `basis_digest` do validador. O digest inclui o enunciado, a resposta, a explicação, tópicos, fontes, dispositivos e os textos ligados. Mudança dessa base invalida a revisão técnica; ausência de mudança não comprova atualização de fonte externa.

Questões oficiais e adaptadas exigem `exam`: `board`, `contest`, `year`, `phase`, `question_number`, `original_url`, `answer_key_url`, `final_answer`, `status` (`valid`, `annulled`, `unknown`). Somente a questão oficial conserva o rótulo `kind: official`; adaptações devem usar o tipo de exercício correspondente e declarar as transformações em `adaptation_note`. Comentário de alternativas pode ser registrado em `options` com texto, correção e justificativa. Guardar `historical_legal_context` e `current_law_note` quando houver mudança relevante.

Perguntas orais/discursivas exigem `rubric`: elementos esperados, relações explicativas e critérios de avaliação. Não reduzir a rubrica a palavras-chave soltas. Questões anuladas e gabaritos pendentes não devem gerar uma pontuação comum de acerto.

Lei seca: cada registro em `law_registry.json` exige `id`, `instrument`, `article`, `version`, `text`, `official_url`, `checked_at`, `topic_ids`. `text` é literal; comentários entram em campo separado. Uma lei pode se relacionar a vários módulos. Versões históricas conservam IDs próprios.

Progressão preferencial: pergunta que ensina a base → distinção → justificativa → exemplo → exceção → aplicação → produção. Revisão espaçada posterior usa o mesmo item; não precisa de outra cópia da explicação para cada tela.

## V2 — vínculo por Claim

Novas perguntas podem incluir `claim_ids`, apontando apenas para as proposições que fundamentam a resposta. Durante a migração, `topic_ids` continua obrigatório e `claim_ids` é progressivo; um módulo só poderá alcançar `study_ready` quando seus itens de estudo estiverem ligados aos Claims pertinentes.

O `basis_digest` atual continua sendo a proteção de compatibilidade do V1. Para o V2, a revisão será migrada para um digest cirúrgico composto pela própria pergunta + `claim_ids` + `law_ids` + metadados oficiais necessários, evitando invalidar itens por edição não relacionada no mesmo capítulo. Até essa migração, perguntas V2 permanecem `draft` ou `needs_review`.


## V3 — resposta em duas velocidades

Para itens conceituais relevantes, o Tutor OS pode adicionar:
- `quick_answer`: resposta-relâmpago para revisão posterior;
- `commentary`: explicação complementar, nuances, distinções e erros frequentes;
- `distractor_notes`: mecanismos de alternativas erradas quando derivados de prova;
- `response_modes`: quais saídas fazem sentido (`study`, `quick_review`, `oral`, `discursive`).

Regras:
1. `quick_answer` nunca substitui `answer` + `explanation` na primeira aprendizagem.
2. pergunta-mãe pode cobrir vários Claims; não criar microcartões só para aumentar contagem.
3. pergunta de contraste só entra depois de os dois conceitos terem sido ensinados.
4. perguntas oriundas de terceiros são padrões/candidatos; o item final deve ser auditado e ter redação própria quando não for questão oficial.
