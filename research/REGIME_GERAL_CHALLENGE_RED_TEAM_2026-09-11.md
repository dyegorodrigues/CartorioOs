# GX Cartório OS — Regime Geral Challenge Red-Team

Data: 2026-09-11
Status: CHALLENGE. Não usar como held-out. NÃO é material de estudo.

## Objetivo
Tentar quebrar o Depth Budget Regime Geral v0.1 usando corpus oficial que não foi reservado como HELD-OUT.

Pergunta:
> existe cobrança legítima, dentro de Cartório, cuja resolução dependa de proposição relevante que o budget v0.1 tratou rasa demais ou omitiu?

## Challenge corpus usado
- TJPE/Cebraspe 2024 — prova oral, Direito Notarial e Registral, Malote 1 Ponto 4.
- TJPE/Cebraspe 2024 — prova oral, Direito Civil, Malote 4 Ponto 1.
- TJPE/Cebraspe 2024 — prova oral, Malote 4 Ponto 3 / responsabilidade temporal.
- TJDFT/Cebraspe 2019 — prova oral com padrão oficial sobre responsabilidade e natureza da delegação.

Não usar perguntas do pool H1/H2/H4.

## Falha 1 — responsabilidade civil precisava de eixo temporal explícito

### Budget v0.1
RG3 já continha:
- culpa/dolo;
- prepostos;
- direito de regresso;
- prazo de 3 anos;
- Estado x delegatário;
- Tema 777.

### Challenge
TJPE/Cebraspe perguntou expressamente por ato praticado em **2015** e exigiu distinguir o regime anterior e posterior à Lei 13.286/2016.

O padrão oficial considera relevante:
- ato anterior à mudança legal → responsabilidade do notário/registrador sob redação anterior;
- após Lei 13.286/2016 → art.22 passa a responsabilidade subjetiva;
- Tema 777/STF não elimina a necessidade de tratar a dimensão temporal;
- precedentes do STJ analisam prospectividade do novo regime.

### Diagnóstico
`DEPTH_GAP` no v0.1.

Não é necessário jogar todo o histórico legislativo em P1, mas o eixo temporal precisa existir em P2 e aparecer no MASTER como alerta de fato antigo.

### Patch
Adicionar em RG3:
`DATA DO FATO → REDAÇÃO APLICÁVEL DO ART.22 → REGIME DO DELEGATÁRIO → RESPONSABILIDADE DO ESTADO/TEMA777`.

## Falha 2 — responsabilidade disciplinar de prepostos não pode ser confundida com responsabilidade civil

### Challenge
TJPE oral perguntou:
1. se notários/registradores respondem por atos dos prepostos;
2. como proporcionalidade atua na responsabilização disciplinar.

Padrão oficial diferencia:
- art.22 = responsabilidade civil perante terceiros;
- art.24 = individualização criminal;
- responsabilidade disciplinar por atos de prepostos não é automaticamente objetiva;
- culpa in eligendo / in vigilando podem ser relevantes;
- proporcionalidade incide na resposta disciplinar e na escolha/graduação de medidas.

### Diagnóstico
`STRUCTURE_GAP` potencial: v0.1 aproxima responsabilidade civil, penal e disciplina, mas não marca suficientemente os planos.

### Patch
RG3/RG6 devem compartilhar um quadro:

| Plano | Pergunta | Critério-base |
|---|---|---|
| Civil | quem indeniza? | art.22 + Tema777 + temporalidade |
| Penal | quem responde pelo crime? | individualização art.24 |
| Disciplinar | quem responde administrativamente e por qual sanção? | infração, culpa/supervisão, proporcionalidade, arts.31–36 + normas aplicáveis |

## Falha 3 — proporcionalidade disciplinar merece OUTPUT P2

O v0.1 colocava procedimento/sanção em P1/P2, mas não explicitava proporcionalidade.

TJPE oral exige raciocínio que vai além de listar penas:
- gravidade da conduta;
- adequação da resposta;
- possibilidade de medida menos severa quando juridicamente cabível;
- graduação da sanção.

### Diagnóstico
`DEPTH_GAP` moderado para oral/output.

### Patch
Não promover para memorização literal P1.
Adicionar a RG6/P2 como `SANCTION REASONING NODE`.

## Falha 4 — natureza jurídica da atividade é pequena em volume, grande em centralidade

TJDFT/Cebraspe oral exigiu explicar o regime de delegação, em paralelo à responsabilidade.

Isso confirma que RG0 não deve ser tratado como introdução decorativa.

### Patch
P1 precisa fixar com precisão:
- serviço público delegado;
- exercício em caráter privado;
- profissional do Direito dotado de fé pública;
- fiscalização pelo Judiciário;
- ausência de personalidade jurídica autônoma do tabelionato/serventia como regra estrutural relevante para legitimidade processual.

O último ponto sobe de P2/implícito para **P1 conceptual boundary**, sem exigir longa doutrina.

## O que NÃO mudou
O challenge NÃO justificou:
- história acadêmica longa da atividade;
- todas as teorias administrativas de delegação;
- detalhamento integral de PAD estadual;
- todos os precedentes sobre responsabilidade.

O budget continua devendo ser compacto.

## Patch summary

### RG0
Adicionar:
- serventia/tabelionato não é pessoa jurídica autônoma para responder como se fosse sujeito distinto do delegatário;
- distinguir delegação da pessoa/estrutura material da serventia.

### RG3
Adicionar P2:
- eixo temporal pré/pós Lei 13.286/2016;
- matriz `fato → lei aplicável → responsabilidade do delegatário → Estado`;
- contraste civil x penal x disciplinar.

### RG6
Adicionar P2/OUTPUT:
- proporcionalidade na responsabilização disciplinar;
- culpa de supervisão/escolha em contexto de prepostos quando pertinente;
- reasoning de sanção, não só tabela de penas.

## Resultado do red-team
Depth Budget v0.1: **NÃO reprovado**, mas requer patch antes de freeze.

Classificação:
- Material structure: boa.
- Literal core: boa.
- Civil responsibility: forte, mas faltava temporalidade.
- Discipline/output: submodelado.
- Nature/delegation: centralidade correta, mas uma distinção processual precisava subir.

## Próxima ação
Criar Depth Budget Regime Geral v0.2 incorporando os patches, depois congelar BUILD corpus e iniciar drafting interno do primeiro material N/R sem abrir HELD-OUT.
