# GX Cartório OS — Oral, Discursive & Practical Corpus Protocol

## Missão
Construir um corpus rastreável de desempenho jurídico real que permita transformar cada unidade do currículo em treinamento progressivo para objetiva, discursiva, peça/prática e oral.

O objetivo não é coletar perguntas por volume. É reconstruir **como o conhecimento é exigido quando o candidato precisa produzir Direito sem alternativas**.

## Fontes prioritárias
1. provas orais oficiais de concursos de cartório, com malotes/pontos/padrões de resposta quando publicados;
2. provas escritas/práticas oficiais de cartório + espelhos + recursos;
3. FGV, Cebraspe, Vunesp e outras bancas em concursos jurídicos L4/L3 para microtemas comparáveis;
4. espelhos/discursivas de magistratura, procuradorias e carreiras jurídicas apenas quando a habilidade e o microtema forem transferíveis;
5. materiais secundários apenas para descoberta/comentário, nunca como substitutos da fonte oficial.

## Janela temporal
Busca histórica ampla, preferencialmente 2010–presente, sem pressupor que tudo seja juridicamente atual.

Cada item histórico recebe dois estados:
- **snapshot histórico**: resposta correta segundo o direito e o edital da época;
- **snapshot atual**: como a questão deve ser respondida sob o direito vigente.

Questão antiga nunca é silenciosamente reescrita. Quando adaptada para treino atual, a adaptação recebe novo ID e vínculo explícito com a fonte histórica.

## Tipos de item
- Recall factual/conceitual
- Distinção/comparação
- Fundamento/artigo/regra
- Caso objetivo sem alternativas
- Mini-discursiva
- Discursiva estruturada
- Peça/ato/procedimento
- Oral nuclear
- Oral estruturada
- Oral com repergunta
- Oral caso prático

## Campos mínimos de reconstrução
- origem e ano;
- banca;
- carreira/família do concurso;
- fase;
- disciplina;
- nó/microtema;
- enunciado/pergunta operacional;
- padrão de resposta/espelho oficial, se houver;
- answer atoms esperados;
- fonte jurídica histórica;
- fonte jurídica atual;
- mecanismo de dificuldade;
- transferibilidade para cartório;
- necessidade de atualização;
- status de validação.

## Answer Atom Model
Toda resposta produtiva deve ser decomponível, quando aplicável, em átomos como:
- identificação do instituto;
- competência;
- regra;
- fundamento;
- requisitos;
- exceção;
- efeito jurídico;
- procedimento/ordem dos atos;
- conclusão;
- distinção de instituto próximo;
- jurisprudência/regulação relevante.

O candidato é diagnosticado pelos átomos ausentes ou frágeis, não apenas pela nota global.

## Escala de dificuldade do corpus
D0 — reconhecimento/definição simples
D1 — recuperação direta sem alternativa
D2 — distinção entre conceitos próximos
D3 — aplicação curta em caso
D4 — caso com múltiplas variáveis/distratores
D5 — mini-discursiva/explicação estruturada
D6 — peça/procedimento ou oral com repergunta
D7 — integração hard: múltiplos institutos + exceções + atualização + pressão temporal

Dificuldade observada no candidato pode divergir da dificuldade editorial do item.

## Engenharia temporal e multibanca
Separar sempre:
- **Domain Incidence**: o que concursos de cartório e carreiras comparáveis cobram sobre o microtema;
- **Bank Style**: como uma banca específica formula e avalia;
- **Phase Style**: como o conhecimento muda entre objetiva, escrita, prática e oral.

Não misturar estilos de banca para inferir DNA da banca-alvo.

## Corpus oral oficial
Priorizar malotes, pontos e padrões de resposta publicados por tribunais/bancas. Quando houver somente edital/critério de avaliação e não perguntas públicas, registrar o certame sem inventar questões.

## Atualização jurídica
Antes de promover um item para treino atual:
1. verificar vigência da norma-base;
2. verificar alterações legislativas/regulatórias;
3. verificar jurisprudência vinculante/relevante posterior;
4. verificar eventual mudança no Código Nacional de Normas/CNJ;
5. classificar: vigente / parcialmente superado / superado / histórico útil.

## Regra de completude
`Todas as questões existentes` é meta de busca, não alegação de completude absoluta da internet. O corpus deve registrar fontes pesquisadas, cobertura por certame e lacunas conhecidas.

## Saída editorial
O corpus não vira uma pilha de questões no MASTER. Ele informa:
- o que precisa estar explicado;
- que distinções merecem tabela;
- que exceções precisam de cor/alerta;
- o que deve ser memorizado;
- quais variações entram no EXAM;
- quais answer atoms entram na discursiva/oral;
- quais itens ficam apenas em REFERENCE.
