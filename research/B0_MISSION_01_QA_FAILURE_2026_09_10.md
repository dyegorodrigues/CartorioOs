# B0 Mission 01 — QA Failure Analysis

Atualizado em 10/09/2026.

## Trigger
O candidato questionou a validade das quatro questões sintéticas iniciais e apontou que, com o pouco que recorda, nenhuma parecia possuir alternativa correta.

## Verificação jurídica
O texto atual do art. 60 da CF/88 confirma:
- procedimento especial para emenda;
- legitimados específicos;
- votação em dois turnos em cada Casa;
- quórum de 3/5;
- limitações materiais e circunstanciais.

Portanto, os gabaritos técnicos propostos (`1-C, 2-B, 3-A, 4-A`) são juridicamente defensáveis dentro da doutrina constitucional dominante sobre rigidez e poder constituinte derivado.

## Falha real
**As questões são inadequadas como treino objetivo de concurso.**

Problemas:
1. distratores excessivamente absurdos;
2. alternativas corretas praticamente repetem a explicação imediatamente anterior;
3. pouca discriminação entre candidato que entendeu profundamente e candidato que apenas reconheceu palavras;
4. baixo realismo de banca;
5. foram apresentadas com aparência de `Node Check` sem qualidade suficiente para gerar evidência de mastery.

Classificação: `QUESTION_DEFECT / ASSESSMENT_QUALITY_GAP`.

## Consequência
- não usar essas quatro questões para medir mastery;
- não atribuir erro/acerto do candidato a learner model a partir delas;
- manter apenas como exemplos de checkpoint didático, se necessário;
- treino objetivo válido deve priorizar questões oficiais ou sintéticas adversariais produzidas após engenharia de distratores e validação jurídica.

## Novo gate para questão sintética de medição
Além de fundamento e gabarito demonstrável, exigir:
1. pelo menos dois distratores plausíveis para alguém com conhecimento parcial;
2. nenhuma alternativa correta por simples eco lexical do material recém-lido;
3. cada distrator mapeado a erro real: regra/exceção, competência, classificação, nomenclatura, snapshot, consequência ou inferência excessiva;
4. teste de ambiguidade;
5. revisão semântica para verificar se mais de uma alternativa pode ser defendida;
6. nível cognitivo declarado: reconhecimento, discriminação, aplicação ou síntese.

## Lição metodológica
`Questão juridicamente correta` e `boa questão de concurso` são critérios diferentes.

O GX precisa provar ambos antes de usar item como evidência de domínio.