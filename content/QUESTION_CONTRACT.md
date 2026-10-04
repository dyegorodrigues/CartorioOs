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
