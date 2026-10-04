# Contrato de Claim — Tutor OS V2

`Claim` é a menor unidade de conhecimento que pode ser revisada, atualizada, cobrada e reutilizada de modo independente.

Este contrato complementa `QUESTION_CONTRACT.md`.

## Forma mínima

Exemplo estrutural:

```json
{
  "id": "PEN-DP01-C01-CL001",
  "topic_ids": ["PEN-DP01-C01-T01"],
  "kind": "concept",
  "statement": "Redação autoral e sintética da proposição.",
  "render_role": "core",
  "source_refs": [
    {
      "source_id": "GRAN-ENAM-PEN-01",
      "locator": "pp. 7-8",
      "role": "primary_study"
    }
  ],
  "authority_ids": [],
  "depends_on_claim_ids": [],
  "freshness": {
    "class": "stable_doctrine",
    "status": "needs_review",
    "checked_at": null
  },
  "review_status": "draft"
}
```

## Campos

### Identidade

- `id`: global, estável e nunca reciclado.
- `topic_ids`: um ou mais tópicos ensinados.
- `kind`: `concept`, `rule`, `exception`, `distinction`, `classification`, `doctrine`, `jurisprudence`, `exam_pattern` ou `example`.

### Conteúdo

- `statement`: redação autoral do conteúdo.
- `render_role`: `core`, `attention`, `exception`, `trap`, `comparison`, `law`, `jurisprudence`, `depth` ou `example`.
- material comercial pode fundamentar o Claim, mas o repositório público não recebe transcrição extensa.

### Proveniência

`source_refs` registra:

- `source_id`;
- `locator` — página/seção suficiente para reencontrar a informação;
- `role`: `primary_study`, `depth_audit`, `official_authority`, `exam_evidence` ou `review_pattern`.

`authority_ids` referencia leis, precedentes, súmulas ou atos oficiais versionados quando necessários.

### Dependências

`depends_on_claim_ids` expressa pré-requisito sem duplicar explicação.

A dependência deve ser acíclica.

## Freshness

`freshness.class`:

- `stable_doctrine`;
- `legislation`;
- `jurisprudence`;
- `exam_pattern`;
- `mixed`.

`freshness.status`:

- `needs_review`;
- `current`;
- `possibly_stale`;
- `superseded`.

`checked_at` só é preenchido após a conferência exigida pelo tipo de Claim.

Um Claim normativo/jurisprudencial não pode ser promovido a `current` apenas porque uma apostila recente o afirma.

## Revisão

`review_status`:

- `draft`;
- `needs_review`;
- `reviewed`.

Para `reviewed`, guardar futuramente um digest calculado a partir do próprio Claim, das autoridades e das fontes relevantes.

## Dependência de questões

O V2 acrescentará `claim_ids` às questões.

O digest de uma questão revisada deve considerar somente:

1. redação da questão/resposta/explicação;
2. Claims ligados em `claim_ids`;
3. registros ligados em `law_ids`;
4. metadados oficiais indispensáveis.

Não deve incluir o texto inteiro do módulo.

Assim, editar um exemplo distante no capítulo não invalida uma pergunta sem relação com ele.

## Migração compatível

Durante a migração:

- `topic_ids` continua obrigatório;
- `claim_ids` pode entrar progressivamente;
- módulos antigos continuam válidos;
- a promoção para `study_ready` exigirá Claims para toda proposição examinável relevante.

## Delta de edição

Para comparar DD 2025, DD 2026 ou outra edição, classificar o Claim:

- `unchanged`;
- `new`;
- `changed`;
- `removed_from_new_edition`;
- `needs_official_check`;
- `superseded`.

Ausência em edição nova não significa revogação.

## Regras de integridade

1. nenhum ID reciclado;
2. nenhum Claim jurídico volátil sem proveniência;
3. nenhuma cópia longa de fonte comercial no repositório;
4. texto legal literal fica no registro de lei, não escondido no Claim;
5. questão oficial preserva contexto e gabarito histórico;
6. mudança automática só pode marcar revisão, nunca certificar conteúdo jurídico.
