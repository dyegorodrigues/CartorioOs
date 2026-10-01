# Manifesto de cobertura — v0.2 — 01/10/2026

**NOT_READY_TO_RENDER. Não exaustivo.** Este manifesto sucede a fotografia anterior sem apagá-la. Janela de aplicação: 01/01/2023 a 01/10/2026; ciclo de edital e publicação não substituem aplicação.

## O que os arquivos medem

| Camada | Regra de contagem | Resultado |
|---|---|---:|
| Descoberta |Identidade de página/ciclo candidato; índices e exclusões sinalizados |143 |
| Exclusões/deduplicação explícita |Apoio administrativo, juiz leigo ou páginas-pai |9 |
| Datas objetivas verificadas |Data de aplicação lida em documento oficial específico |16 |
| Documentos relacionados |URL única dentro da página do certame; inclui aviso, edital, chave e caderno |4.449 |
| Arquivos com hash |Aquisição preservada; não presume leitura |254 |
| PDFs |Inclui chaves, reservas, editais e provas; não é quantidade de exames |122 |
| Decomposição nova |Questão real, com caderno e resposta oficial identificados |31 |
| Herança parcial |Paráfrases legadas com pendências explicitadas |8 |
| Assertivas |Linha atômica de alternativa, item C/E ou exigência do espelho |141 |

Há 9 registros de tentativa falha; um foi resolvido por retry de codificação PF. Falhas de acesso restantes não foram transformadas em ausência de fonte. Leitura via serviço web de algumas fontes jurídicas foi conservada em `discovery/`, separada de download integral.

## Critério de relevância

`DIRECT`: o item exige reconhecer ou discriminar uma proposição do cluster introdutório. `BRIDGE`: aplica fundamentos a tipo, caso, princípio, norma, temporalidade ou saída escrita/oral. Adjacência não obriga inserir todo o assunto na primeira unidade. Marcadores de edital, calendário, rótulo de site e programa oral não são questões.

O corpus não contém todo Penal. Tipos particulares são preservados quando demonstram uma transferência específica. Questões só parcialmente lidas ou ainda sem identidade/gabarito fechados não recebem status de auditoria integral. Os três legados com proveniência secundária pendente continuam identificados, em vez de desaparecerem.

## Cobertura por fase e carreira

| Carreira | Objetiva | Discursiva | Oral | Limite da conclusão |
|---|---:|---:|---:|---|
| Delegado |18|0|1|Amostra inclui herança e concentra PF/FGV; várias polícias pendentes. |
| Magistratura |3|0|0|TJPR/TJPE; ENAM e outros tribunais não foram encerrados semanticamente. |
| Ministério Público |9|3|0|MPRJ/MPMS/MPPA; não representa todos os MPs nem MPF/MPT/MPM. |
| Defensoria |4|0|0|Concentração DPERJ; oral DPEAC localizada/lida em um ponto adjacente, sem inflar corpus. |
| Advocacia Pública |1|0|0|ALERJ; demais provas localizadas não comprovam menor necessidade introdutória. |

## Universo ainda aberto

FGV e Cebraspe tiveram catálogo oficial expandido; FCC e fontes próprias também foram consultadas. Isso não encerra concursos próprios, Vunesp, Fundatec, outras bancas, procuradorias municipais ou fases finais de ciclos anteriores. `INSTITUTION_YEAR_CLOSURE_GRID.csv` explicita 27 UFs × 5 famílias × 4 anos sem atestar ausência. Essa grade é um **controle de fechamento**, não um denominador de provas nem a afirmação de que existam 540 certames.

`PHASE_COVERAGE.csv` tem três linhas por candidato, com número de links de caderno, padrão e avisos. Classificação de link é triagem. Documento oral com programa, sorteio, resultado ou convocação não é pergunta real automaticamente.

## Resultado dos gates

| Gate | Estado | Evidência |
|---|---|---|
| A — enumeração |FAIL|Não há fechamento institucional; segunda passagem encontrou omissões. |
| B — ingestão/revisão semântica |FAIL|Documentos adquiridos excedem os efetivamente revisados; nenhum negativo de exame integral foi certificado. |
| C — decomposição |PARTIAL|31 novas e 8 herdadas; fontes primárias, dissenso, datas e identidade de certos legados pendentes. |
| D — grafo/aliases/overlays |PARTIAL|Projeções auditáveis existem; proposições candidatas ainda não aprovadas como texto jurídico. |
| E — reserva |RESERVED_NOT_VALIDATED|5 arquivos selados, sem leitura no BUILD; contaminação histórica e suficiência não encerradas. |
| F — render/validação |BLOCKED|Nenhuma unidade, escore held-out ou aprovação de legibilidade foi produzido. |

O passo legítimo é completar o corpus e os controles indicados na fila. Um arquivo extenso, um número grande de downloads ou o resultado PASS de integridade não substituem esses gates.
