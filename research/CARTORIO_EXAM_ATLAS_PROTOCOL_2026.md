# GX Cartório OS — Cartório Exam Atlas Protocol

Data: 2026-09-10
Status: HOT research protocol

## Missão
Construir um mapa reproduzível do que realmente é cobrado em concursos de Cartório, em qual profundidade, por qual banca, em qual fase e com que consequência pedagógica.

O Atlas não é apostila. Ele é a camada de inteligência que decide o que a apostila deve conter.

## Unidade mínima
A unidade estatística não é apenas disciplina ou capítulo. É a PROPOSIÇÃO JURÍDICA examinável.

Exemplo abstrato:
`lei posterior mais benéfica retroage inclusive após trânsito em julgado`

Cada proposição recebe:
- disciplina;
- macrobloco;
- módulo;
- nó e subnó;
- aliases/nomenclaturas;
- fonte primária atual;
- data de validade/revalidação;
- banca;
- TJ/ENAC;
- ano;
- fase;
- modalidade;
- dificuldade;
- tipo cognitivo;
- tipo de distrator;
- literalidade vs conceito vs jurisprudência vs caso;
- frequência observada;
- recência;
- peso da evidência;
- consequência para P1/P2/P3+;
- memorizar/entender/discriminar/aplicar/produzir.

## Proveniência obrigatória
Nível A — prova + gabarito oficiais.
Nível B — fonte oficial da banca/TJ/CNJ, mas metadado incompleto.
Nível C — livro/banco secundário com identificação suficiente da questão.
Nível D — cursinho/material sem prova original localizada.

Prioridade e profundidade não podem ser determinadas exclusivamente por C/D.

## Famílias de corpus
### C0 — ENAC oficial
Todas as edições FGV, todas as questões, anuladas preservadas, classificação por proposição e distrator.

### C1 — Cartório estadual atual
Concursos sob regime contemporâneo, com atenção especial ao pós-ENAC e pós-Resolução 696/2026.

### C2 — Cartório estadual histórico
Amostra ampla por banca/Estado/ano para detectar recorrência, profundidade e aliases.

### C3 — transferência de banca
FGV OAB/ENAM/carreiras jurídicas, Cebraspe carreiras jurídicas etc., somente para estudar gramática de banca quando a proposição coincide. Nunca contar como frequência de Cartório.

### C4 — desafio jurídico
Questões de Magistratura, MP, Defensoria, Delegado e afins para descobrir cauda de profundidade. Peso pedagógico só sobe se houver pertinência de escopo ou evidência em Cartório.

## Modalidade
Separar rigorosamente:
- OBJETIVA;
- DISCURSIVA;
- PEÇA PRÁTICA;
- ORAL.

Uma cobrança em oral não aumenta automaticamente a prioridade de memorizar um detalhe para objetiva. Ela pode alterar o `OUTPUT DEPTH` do nó.

## Banco examinador
Não declarar “bancas dominantes” por impressão.

Primeiro censo atual já mostra diversidade:
- FGV em concursos atuais como MS/RN/RS;
- Cebraspe em BA/CE/MT/RO/RR;
- Vunesp em SP;
- IESES em PA;
- Consulplan em PB;
- outros e bancas a definir permanecem no radar.

Esses dados são snapshot de 2026 e não substituem o censo histórico.

## Tipos cognitivos a marcar
- reconhecimento literal;
- exceção literal;
- comparação/contraste;
- nomenclatura/alias;
- conceito/doutrina;
- jurisprudência;
- integração entre fontes;
- aplicação a caso;
- sequência/procedimento;
- cálculo/prazo/quórum;
- identificação de ato/peça;
- fundamentação escrita;
- resposta oral + repergunta.

## Tipos de distrator
- inversão regra/exceção;
- troca de sujeito/competência;
- troca de prazo/quórum;
- absoluto indevido (`sempre`, `nunca`, `somente`);
- termo jurídico próximo;
- alias falso;
- mistura de institutos;
- jurisprudência superada;
- lei local indevidamente generalizada;
- caso com premissa jurídica falsa;
- redação quase literal com uma palavra fatal.

## Score de incidência
O Atlas não reduzirá decisão a frequência bruta. Cada proposição recebe score composto por:
- peso no edital/matriz atual;
- frequência no corpus Cartório;
- recência;
- repetição entre bancas;
- consequência de erro;
- centralidade/pré-requisito;
- custo de aprendizagem;
- volatilidade jurídica;
- fase em que pode ser cobrada.

O score produz quatro decisões diferentes:
1. `STUDY PRIORITY`;
2. `MEMORY PRIORITY`;
3. `QUESTION PRIORITY`;
4. `OUTPUT PRIORITY`.

Assim, uma proposição pode ser pouco frequente, mas barata e fatal se esquecida, devendo ser memorizada; ou frequente, mas conceitualmente derivável, exigindo mais compreensão do que flashcards.

## Depth Budget
Para cada nó:
- P1 CORE: sobreviver objetivas básicas/intermediárias e construir mapa mental;
- P2 EXAM DEPTH: exceções, jurisprudência, aliases e casos realmente demonstrados;
- P3+ ROBUSTNESS: cauda, banca específica, cross-node e output avançado.

Nenhuma camada profunda entra em P1 só porque aparece em um tratado ou material de Delegado.

## Questões no aprendizado
### Encoding Check
Pode ser aplicado logo após aquisição. Serve para corrigir compreensão. Não alimenta mastery de retenção.

### Assessment
Deve ter atraso/espaçamento e mistura suficientes. Alimenta mastery.

### Held-out Validation
Questão legítima não usada para construir aquela versão do material. Testa suficiência do material.

### Challenge
Outra banca, outra formulação, caso adversarial ou cross-node. Testa robustez.

## Freshness Firewall
Toda proposição volátil precisa registrar:
- fonte vigente;
- snapshot;
- evento que força revalidação;
- jurisprudência vinculante/repetitiva/relevante;
- revogação ou alteração normativa.

Questão antiga pode continuar útil como forma cognitiva, mas seu gabarito/conteúdo precisa ser revalidado antes de uso pedagógico.

## Produto derivado
Só depois do Atlas, o Compiler gera:
`MAP → MASTER P1 → LEI SECA GUIADA → REVIEW → Q→A → FLASHCARDS SELETIVOS → OBJECTIVE LAB → OUTPUT LAB`

Todas as superfícies apontam para os mesmos IDs de proposição.

## Próxima execução
1. inventariar concursos de Cartório e bancas por janela temporal;
2. localizar fontes oficiais e PDFs de prova/gabarito;
3. completar ENAC C0;
4. construir primeiro slice C1/C2 para N/R + Civil + Constitucional;
5. usar Penal/PEN1 apenas como benchmark de pipeline;
6. recalibrar Specimen A após o Atlas, sem ampliar por ansiedade.