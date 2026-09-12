# Três questões FGV reconstruídas e comparadas com o material

Data: 12/09/2026. Base examinada: commit `b1ab79f8631094522e80b06af34866adb4b96da1`.
Estado: **regressão de cobertura após BUILD, com gabarito conhecido; zero novos passes independentes**.

Foram conferidas as 15 alternativas de três questões já consumidas do TJES/FGV 2025, com leitura das páginas dos cadernos e do gabarito definitivo. A comparação encontrou uma explicação jurídica incorreta na versão de trabalho do RI. Ela foi corrigida na fonte editorial e nas derivações. As três letras oficiais continuam sustentadas pelos dispositivos examinados, mas isso não demonstra suficiência geral dos módulos.

## Fontes e localização

| Identidade | Fonte primária | Localização conferida |
|---|---|---|
| Concurso | [Página FGV/TJES](https://conhecimento.fgv.br/concursos/tjesnotarial25) | Lista cadernos publicados em 28/07/2025 e gabarito definitivo em 26/08/2025; essas são datas de publicação dos arquivos, não a data da prova |
| Remoção, Tipo 1, Q20 e Q22 | [Caderno oficial](https://conhecimento.fgv.br/sites/default/files/concursos/atividade-notarial-e-de-registro-ingresso-por-remocaocar-001-tipo-1-copia.pdf) | Página impressa 7 / página PDF 7 |
| Provimento, Tipo 1, Q15 | [Caderno oficial](https://conhecimento.fgv.br/sites/default/files/concursos/atividade-notarial-e-de-registro-ingresso-por-provimentocar-002-tipo-1-copia.pdf) | Página impressa 6 / página PDF 6 |
| Respostas definitivas | [Gabarito oficial](https://conhecimento.fgv.br/sites/default/files/concursos/gabarito-definitivo-tjes-notarial.pdf) | Página 1, Remoção/1: Q20 C e Q22 B; página 2, Provimento/1: Q15 E. Nenhuma dessas três está anulada |

Os PDFs recebidos têm hashes no [índice de rastreabilidade](../data/atlas/FGV_TJES_RECONSTRUCTION_INDEX_2026-09-12.json). Os cadernos integrais não foram copiados para o material. Abaixo há sínteses autorais das alternativas e comentários próprios, para consulta junto ao original.

## Base legal histórica e atual

As questões pedem aplicação das leis indicadas no próprio enunciado. Conferidos os dispositivos selecionados da [Lei 8.935](https://www.planalto.gov.br/ccivil_03/leis/l8935.htm) e da [LRP](https://www.planalto.gov.br/ccivil_03/leis/l6015compilada.htm). Na LRP, o regime do art. 188 foi confrontado também com a [Lei 14.382/2022](https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2022/lei/l14382.htm), arts. 11 e 21: a alteração pertinente já vigorava em 2022, antes do certame de 2025. O art. 167 I 21 e os dispositivos selecionados da Lei 8.935 não apresentam, nos textos consultados, alteração superveniente capaz de inverter essas três respostas.

Conclusão delimitada: os fundamentos legais selecionados sustentam o gabarito histórico e a leitura atual em 12/09/2026. Não foi reconstruído o snapshot integral do edital, nem revalidada toda a jurisprudência ou o CNN. Essa conclusão não muda `exam_snapshot: NOT_ASSESSED` dos workbooks inteiros.

<a id="q20-rem"></a>

## Remoção Q20 — atribuição e exclusividade

O item compara autenticação de cópias com recebimento de títulos protocolizados para pagamento. **Gabarito definitivo: C.** Fundamentos: Lei 8.935, arts. 7º V e 11 III.

| Alternativa | Síntese da proposta | Comentário jurídico |
|---|---|---|
| A | Troca especialidades e afasta exclusividade da autenticação | Incorreta. A autenticação pertence com exclusividade a notas; o recebimento descrito pertence privativamente a protesto. A troca de sujeitos já invalida a proposta. |
| B | Acerta especialidades, mas elimina uma exclusividade | Incorreta. Não basta acertar quem faz: a primeira atribuição tem caráter exclusivo expresso no art. 7º. A segunda parte correta não salva a primeira. |
| C | Notas autentica; protesto recebe; exclusividades preservadas | Correta. As duas partes mantêm os sujeitos e os qualificadores dos dispositivos legais. |
| D | Concentra as duas operações em protesto | Incorreta. A primeira operação foi atribuída à especialidade errada. |
| E | Concentra as duas operações em notas | Incorreta. A segunda operação foi atribuída à especialidade errada. Não confundir com outras hipóteses legais em que notas pode receber valores. |

**Onde se aprende:** `RG-ATTR-AUTH-001`, no [MASTER de Regime Geral](../material/working/RG_AFASTAMENTO_INTERVENCAO_V0.1.md#rg-attr-auth-001). Uma regra composta cobre a resposta correta e o erro decisivo das quatro incorretas. Não foi criada uma regra nova para cada alternativa nem uma contagem de cinco incidências.

**Mecanismo observado neste item:** troca de atribuição e supressão de qualificador. É descrição desta questão; não uma estimativa da frequência desse mecanismo em toda a FGV.

<a id="q22-rem"></a>

## Remoção Q22 — afastamento e renda

O caso trata de investigação disciplinar e consequências do afastamento necessário à apuração. **Gabarito definitivo: B.** Núcleo decisivo: art. 36 caput e §2º da Lei 8.935.

| Alternativa | Síntese da proposta | Comentário jurídico |
|---|---|---|
| A | Prazo de 60 + 30 e juros compensatórios | Incorreta já pelo primeiro prazo: o caput prevê 90 dias, com prorrogação por mais 30. A parcela depositada tem correção monetária prevista no §2º; o dispositivo não acrescenta juros compensatórios como requisito. Isso não é uma tese geral sobre todo rendimento bancário. |
| B | Prazo de 90 + 30 e divisão líquida corrigida | Correta. Combina necessidade do afastamento, duração e tratamento da renda durante a medida. Não exige deduzir o prazo da pena disciplinar do art. 32. |
| C | Prazo de 60 + 30 e base bruta | Incorreta por dois elementos independentes: duração inicial e base de cálculo. A lei usa renda líquida. |
| D | Nega previsão de suspensão e propõe atuação conjunta | Incorreta desde a premissa: a suspensão preventiva tem previsão expressa no art. 36. A intervenção para responder pela serventia durante o afastamento também não é apresentada nesse dispositivo como a administração conjunta proposta. |
| E | Restringe a medida a procedimento exclusivo no CNJ | Incorreta. A Lei 8.935 disciplina atuação do juízo competente nos arts. 35 §1º, 36 e 37; não impõe a exclusividade e o referendo descritos. Isso não afasta competências próprias do CNJ. |

**Onde se aprende:** `RG-DISC-PREV-001` e `RG-DISC-RENDA-003` contêm os elementos necessários para reconhecer B e rejeitar A/C/D. `RG-DISC-INTERVENTOR-002` e `RG-LOSS-035-AFASTAMENTO` ajudam na comparação de autoridade e hipótese. Para a fundamentação completa de E, esta reconstrução acrescenta a remissão ao art. 37 como complemento da análise; não a apresenta como parágrafo que já estivesse no workbook.

O destino do saldo após absolvição ou condenação, ensinado no material pelo art. 36 §3º, **não foi cobrado como requisito da alternativa B**. É conhecimento conectado, não uma segunda incidência contada. A antiga falta de correção monetária estava no material; o novo recorte já a ensina. A regressão não transforma a base antiga em aprovada.

<a id="q15-prov"></a>

## Provimento Q15 — título, prazo e consequência disciplinar

O título apresentado é uma citação relativa a imóvel em ação pessoal reipersecutória. **Gabarito definitivo: E.** Fundamentos decisivos: LRP, art. 188 §2º, e Lei 8.935, art. 32 IV.

| Alternativa | Síntese da proposta | Comentário jurídico |
|---|---|---|
| A | Nota devolutiva em 15 dias | Incorreta. O prazo geral do art. 188 é de 10 dias, ressalvadas suas exceções. A narrativa não oferece uma exceção que estabeleça os 15 propostos. Não inferir que todo título terá sempre o prazo geral. |
| B | Ingresso exclusivamente em RTD | Incorreta. O ato descrito é previsto para o Registro de Imóveis no art. 167 I 21. |
| C | Averbação em 30 dias | Incorreta. A modalidade é registro na hipótese indicada. Esse erro já basta, sem inventar um prazo geral de averbação para rejeitar a proposta. |
| D | Protocolo substitui registro se não houver impugnação | Incorreta. Prenotação e registro não são equivalentes. Os arts. 186 e 188 distinguem prioridade do título e realização do ato; o silêncio indicado não produz a conversão automática alegada. |
| E | Descumprimento pode levar à perda da delegação | Correta. O art. 188 §2º remete ao elenco do art. 32 da Lei 8.935, que inclui a perda. Reconhecer essa possibilidade não significa aplicá-la automaticamente nem dispensar defesa e os requisitos da sanção. |

**Onde se aprende:** `LRP-RI-PRAZO-SANCAO-016` resolve E; `LRP-RI-NOTA-018`, na explicação do MASTER, resolve A; `LRP-RI-CITACAO-017` resolve B/C; a base `RI-BASE-PROTOCOLO` discrimina D. A identificação do título continua sendo discriminação útil, não um segundo requisito para afirmar a consequência sancionatória de E.

## Correção encontrada e aplicada

Na versão de trabalho anterior, a explicação de `LRP-RI-PRAZO-SANCAO-016` atribuía ao dispositivo o verbo **poderá**. O art. 188 §2º usa **ensejará**. A possibilidade mencionada na questão refere-se à pena específica de perda da delegação, não a uma escolha discricionária sobre existir ou não a remissão sancionatória.

A fonte editorial agora preserva essa diferença: a inobservância enseja a aplicação do regime sancionatório; o elenco não determina sozinho a perda automática. A resposta E e a conclusão negativa de `GX-RI-05` continuam corretas, mas sua justificativa precisava do reparo. Gravidade: **MUST / erro de explicação jurídica**.

A alteração invalidou a revisão editorial de `GX-RI-05`, e o gerador a recusou como previsto. O caso foi reexaminado contra os dois artigos e teve seu registro de revisão atualizado. MASTER, REVIEW, Q→A e a base dos casos foram regenerados; nenhum arquivo congelado foi reescrito. Os 29 testes existentes e a conferência das derivações passaram após a correção. Os testes não detectaram o erro jurídico: a leitura da fonte o detectou.

## O que a comparação permite concluir

| Pergunta | Resposta deste lote |
|---|---|
| As três letras oficiais são sustentadas pela análise feita? | Sim: C, B e E, nos dispositivos delimitados |
| O material contém os elementos decisivos das três corretas? | Sim, após corrigir a explicação de RI |
| A justificativa completa de cada distrator já estava integralmente no workbook? | Não: por exemplo, a remissão ao art. 37 para Q22/E é complemento explicitado aqui |
| Foram analisadas as cinco alternativas de cada item? | Sim, com a distinção acima entre ensino existente e complemento da análise |
| Isso equivale a três novos acertos independentes ou a S2? | Não. Seleção dirigida por falhas conhecidas, material construído após exposição e gabarito previamente conhecido |
| Os dois módulos completos estão liberados? | Não. Estes recortes não resolvem a suficiência integral dos pilotos |

## Exposição e próximo trabalho

Nesta reconstrução foram consultadas páginas dos dois cadernos e páginas integrais de seus gabaritos Tipo 1. Retornos ampliados também exibiram itens vizinhos. Os dois cadernos ficam integralmente **BUILD/CHALLENGE_ONLY** para testes futuros neste projeto, inclusive qualquer reapresentação de suas mesmas questões em outro tipo. Não tentar recuperar independência escolhendo números ainda não classificados. Isso não afirma que suas 200 questões foram analisadas.

O trabalho pendente continua concreto: completar cobertura e fontes dos pilotos inteiros, obter a evidência externa mínima ainda faltante dentro da contenção de rodadas e realizar a auditoria independente prevista. Os comentários deste lote não são a Passagem 2 dos 300 ENAC nem alteram seus contadores. Não houve aula, atualização de mastery, migração de questões para o Notion ou abertura de outro pool reservado.
