# GX Cartório OS — Proposition Ledger Seed
## N/R — Regime Jurídico Geral / Lei 8.935 + Constituição + STF

Snapshot: 2026-09-10
Status: SEED, expandir com ENAC + corpus estadual

> Regra: este arquivo não é material de estudo. É a base de decisão do Compiler.

## Fontes primárias-base
- Lei 8.935/1994 vigente: https://www.planalto.gov.br/ccivil_03/leis/l8935.htm
- CF/88, art. 236.
- STF Tema 779: https://portal.stf.jus.br/jurisprudenciaRepercussao/tema.asp?num=779
- STF Tema 777: https://portal.stf.jus.br/jurisprudenciarepercussao/tema.asp?num=777
- TJMS/FGV 2026 prova + gabarito + escrita/espelho.
- TJBA/Cebraspe 2026 escrita/prática.

## Ledger

| ID | Proposição examinável | Fonte atual | Evidência de prova nesta onda | Forma cognitiva observada | Memory | Study | Question | Output | Estado |
|---|---|---|---|---|---|---|---|---|---|
| RG-NAT-001 | Serviços notariais/registro são organização técnica e administrativa destinada a publicidade, autenticidade, segurança e eficácia dos atos jurídicos | L8935 art. 1 | escopo ENAC; corpus específico ainda a contar | definição/literalidade | M | H | M | M | BUILD CANDIDATE |
| RG-NAT-002 | Notário/tabelião e registrador são profissionais do Direito dotados de fé pública, com exercício delegado | L8935 art. 3 + CF 236 | transversal em casos escritos; frequência ainda não contada | conceito estrutural | H | H | H | H | CORE CANDIDATE |
| RG-PRE-020A | Titular pode contratar escreventes, substitutos e auxiliares como empregados sob legislação trabalhista; gestão/prepostos obedecem estrutura legal | L8935 art. 20 | TJBA/Cebraspe discursiva aborda contratação de escreventes/interinos e regime constitucional | regra + contraste titular/interino | M | H | H | H | P1/P2 |
| RG-PRE-020B | Substitutos podem praticar atos próprios simultaneamente com titular, exceto lavrar testamentos em tabelionato de notas | L8935 art. 20 §4 | corpus objetivo específico ainda a contar | exceção literal | H | M | H | M | MEMORY CANDIDATE |
| RG-IMP-027 | Titular não pode praticar pessoalmente ato de interesse próprio, do cônjuge ou de parentes em linha reta/colateral, consanguíneos ou afins, até 3º grau | L8935 art. 27 | TJMS/FGV 2026 Q4, gabarito B | caso de parentesco + palavra fatal `pessoalmente`/`3º grau` | VH | H | VH | L | VALIDATED EXAMPLE |
| RG-INT-T779 | Substitutos/interinos de serventia vaga não se equiparam a titulares concursados; são agentes estatais e submetem-se ao teto do art. 37 XI | STF Tema 779, RE 808202 | TJBA/Cebraspe discursiva Q1; TJMS/FGV discursiva Q1 pergunta teto de substituto | jurisprudência + distinção de regime | H | VH | H | VH | CROSS-BANK OUTPUT |
| RG-INT-ADI1183 | Interinidade decorrente de vacância não pode resultar em substituição ininterrupta por preposto não concursado por mais de 6 meses; decisão STF condiciona solução após prazo e preserva atos/modulação | STF ADI 1183, decisão/modulação 2024 | questão BA tangencia controle prévio/seleção; incidência específica ainda a contar | jurisprudência avançada + limite temporal | M/H | H | M | H | P2 CANDIDATE |
| RG-RESP-T777 | Estado responde objetivamente por danos causados por tabeliães/registradores no exercício das funções, com dever de regresso em dolo/culpa | STF Tema 777, RE 842846 | BA discursiva pergunta responsabilidade estatal no contexto dos interinos; não assumir identidade perfeita dos fatos | tese vinculante / responsabilidade | H | VH | H | VH | CORE/P2 |
| RG-RESP-022 | Notários/registradores respondem civilmente por prejuízos causados por dolo/culpa, pessoalmente ou por substitutos/escreventes autorizados, com regresso; pretensão em 3 anos da lavratura do ato | L8935 art. 22 | corpus específico desta onda ainda a contar | literalidade + integração com Tema 777 | H | H | H | H | CORE CANDIDATE |
| RG-DIR-028 | Titular goza de independência no exercício, recebe emolumentos integrais e só perde delegação nas hipóteses legais | L8935 art. 28 | conexão com distinção titular x interino; frequência ainda a contar | estrutura de regime | M | H | M | M | CORE CANDIDATE |
| RG-DEV-030 | Deveres do notário/registrador incluem eficiência, sigilo, tabela/emolumentos, prazos, fiscalização tributária, acesso documental, suscitação de dúvidas e observância de normas técnicas | L8935 art. 30 | escopo/regime geral; corpus granular ainda a contar | lista extensa, demanda incidence map por inciso | TBD | H | TBD | M | NEEDS ARTICLE HEATMAP |
| RG-DISC-031 | Infrações disciplinares incluem inobservância normativa, conduta atentatória, cobrança indevida/excessiva, violação de sigilo e descumprimento dos deveres do art. 30 | L8935 art. 31 | TJMS objetiva possui disciplina local, mas não usar como frequência nacional | classificação/lista | TBD | M/H | TBD | M | NEEDS CORPUS |

Legenda: L=low, M=medium, H=high, VH=very high, TBD=aguardar corpus.

## Primeiros insights de engenharia

### 1. Mesmo capítulo, pedagogias diferentes
`RG-IMP-027` é regra curta, barata e altamente testável. Melhor superfície:
- lei seca destacada;
- contraste de graus;
- flashcard/recall curto;
- questões espaçadas.

`RG-INT-T779`, por outro lado, exige:
- diferença titular x interino;
- fundamento constitucional;
- tese STF;
- consequências remuneratórias;
- integração com contratação/interinidade;
- treino escrito/oral quando a fase permitir.

Não usar o mesmo template de estudo para ambos.

### 2. Fonte legislativa e jurisprudência não devem competir
Lei 8.935 art. 22 e STF Tema 777 precisam aparecer como uma conexão explícita. O aluno deve saber `quem responde em qual plano` em vez de memorizar duas frases desconectadas.

### 3. Lista longa precisa de heatmap interno
Art. 30 não deve virar flashcard gigante. O Atlas precisa contar cobrança por inciso e agrupar deveres por função. Só então decidir quais palavras exigem memória literal.

### 4. Cross-bank output já observado
Tema 779 apareceu como problema de escrita tanto na FGV/TJMS quanto Cebraspe/TJBA nesta onda recente. Isso NÃO é ainda frequência histórica, mas já justifica alta prioridade de `OUTPUT EVIDENCE` e investigação no ENAC/objetivas.

## Próxima expansão
1. Varredura C0 ENAC para Lei 8.935 por artigo/proposição.
2. Contar C1/C2 estatal para arts. 1,3,20–22,25–39.
3. Separar titular, preposto, substituto, interino/interventor.
4. Fazer heatmap dos arts. 30–36.
5. Integrar CNN/CNJ-Extra nos nós equivalentes.
6. Só depois emitir prioridades numéricas.