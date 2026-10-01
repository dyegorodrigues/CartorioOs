# Work run — Legal Tutor OS — 01/10/2026

**Veredito: NOT_READY_TO_RENDER.** Rodada de pesquisa e auditoria preservada; não foi produzido material de estudo. O inventário multicarreira foi ampliado substancialmente, mas não foi fechado como exaustivo. Esta entrega cumpre a saída de auditoria prevista no handoff para um resultado NOT_READY; não declara concluída a missão inteira de corpus.

Repositório: `dyegorodrigues/CartorioOs` · branch `chatgpt/legal-tutor-os-core-2026-09-30` · base preservada: `11a00a95585b416992c29e3d2ece0c0f9817190d`.

## Resultado verificável

| Medida | Resultado e limite |
|---|---|
| Universo de descoberta |143 candidatos/ciclos/índices, incluindo 9 exclusões ou páginas-pai; **não 143 provas auditadas** |
| Catálogo de documentos oficiais |4.449 links únicos por página de certame, incluindo editais, resultados e avisos |
| Fontes adquiridas |263 registros de tentativa;254 arquivos com hash conferido;122 PDFs, incluindo chaves, avisos, reservas e candidatos excluídos |
| Frescor |Duas passagens;223 eventos de publicação na janela conservadora 02/08–01/10; universo ainda não saturado |
| Corpus deduplicado |39 questões selecionadas: 31 com decomposição nova e 8 herdadas parcialmente reconciliadas |
| Assertivas |141: 104 novas e 37 herdadas; 59 linhas do legado têm destino explícito no ledger de migração |
| Fases reais |35 objetivas, 3 discursivas e 1 oral; editais e convocações não entram nessa conta |
| Carreiras |Delegado 19; MP 12; Defensoria 4; Magistratura 3; Advocacia Pública 1 |
| Conhecimento e nomenclatura |81 endereços candidatos, 15 registros de aliases e 12 arestas de confusão; sem promoção automática a verdade jurídica |
| Held-out |5 arquivos ativos selados: 2 cadernos objetivos com respectivas chaves e 1 conjunto oral; **validação não executada** |
| Integridade |PASS: identidades, referências, isolamento local da reserva e preservação byte a byte do legado |

O número de arquivos não mede cobertura semântica. A coleta não demonstra ausência de conteúdo em documentos não lidos. As contagens por carreira descrevem apenas a seleção deste lote; não autorizam ranking de incidência nacional.

## Achados que alteram o mapa

- **MPRJ2026Q23:** a versão anterior tomou um distrator por regra. O gabarito é D, mantido após recursos; a correção está explícita no novo corpus e no ledger.
- **PF2025Q52–54 e MPMS2026Q14:** teoria do bem jurídico e autoria precisam de discriminação precisa. MPMS acrescenta Kant, Hegel, Feuerbach, Welzel, Jakobs e Hassemer sem tornar suas teorias intercambiáveis.
- **TJPE2026Q41/Q48 e PCDF2026Q74:** a triagem anterior por rótulos deixou passar legalidade, abolitio e ultima ratio. Os antigos sinais negativos não sustentam ausência semântica.
- **AGU edital 2022:** objetiva aplicada 07/05/2023 pertence à janela. Datas de publicação de outras provas também foram separadas das datas de aplicação.
- **Fases avançadas:** pergunta oral real PF aplicada 19/07/2026 e espelhos escritos MPPA/MPRJ foram decompostos por exigência de resposta. Oral PCDF 10–11/10 permanece futura no corte.

## Entregáveis do handoff

| Saída | Arquivo |
|---|---|
| Manifesto de cobertura |[COVERAGE_MANIFEST_V0_2.md](COVERAGE_MANIFEST_V0_2.md) |
| Universo e fases |[TARGET_EXAM_UNIVERSE_V0_2.csv](TARGET_EXAM_UNIVERSE_V0_2.csv), [PHASE_COVERAGE.csv](PHASE_COVERAGE.csv) |
| Corpus e matriz |[QUESTION_CORPUS_V0_2.csv](QUESTION_CORPUS_V0_2.csv), [ASSERTION_MATRIX_V0_2.csv](ASSERTION_MATRIX_V0_2.csv) |
| Aliases/confusões |[ALIAS_REGISTRY_V0_2.csv](ALIAS_REGISTRY_V0_2.csv), [ALIAS_CONFUSION_EDGES.csv](ALIAS_CONFUSION_EDGES.csv) |
| QA/conflitos |[QA_CONFLICT_LEDGER_V0_2.md](QA_CONFLICT_LEDGER_V0_2.md), [LEGACY_MIGRATION_LEDGER.csv](LEGACY_MIGRATION_LEDGER.csv) |
| Grafo, mapa e overlays |[EVIDENCE_GRAPH_V0_2.json](EVIDENCE_GRAPH_V0_2.json), [KNOWLEDGE_AND_CAREER_MAP.md](KNOWLEDGE_AND_CAREER_MAP.md), [CAREER_OVERLAY_V0_2.csv](CAREER_OVERLAY_V0_2.csv) |
| Held-out |[HELD_OUT_LOCK.json](HELD_OUT_LOCK.json), [HELD_OUT_PROTOCOL.md](HELD_OUT_PROTOCOL.md) |
| Readiness |[READINESS.json](READINESS.json) |
| Registro de fontes |[SOURCE_REGISTRY_V0_2.csv](SOURCE_REGISTRY_V0_2.csv), [OFFICIAL_DOCUMENT_CATALOGUE.csv](OFFICIAL_DOCUMENT_CATALOGUE.csv) |
| Frescor, revisão e preservação |[FRESHNESS_AUDIT.md](FRESHNESS_AUDIT.md), [SEMANTIC_REVIEW_LOG.csv](SEMANTIC_REVIEW_LOG.csv), [VALIDATION_REPORT.json](VALIDATION_REPORT.json), [LEGACY_PRESERVATION.json](LEGACY_PRESERVATION.json) |

`sources/` conserva bytes e metadados de aquisição; `text/` e `columns/` são extrações derivadas; `discovery/` conserva pesquisas e leituras das cinco páginas Notion de trabalho. O arquivo `CEBRASPE_APP.js` é o script público que permitiu localizar a API pública. Nenhum recurso de candidato autenticado foi usado. Tentativas malsucedidas permanecem nos logs; o problema de codificação da URL PF teve retry separado.

## Gates que continuam abertos

1. Fechar o inventário por instituição/ano e eliminar ambiguidades de ciclo, janela e páginas-pai; a grade de 540 células estaduais está **não encerrada**, não “sem concursos”. Completar também famílias federais e procuradorias relevantes.
2. Ler semanticamente os cadernos inteiros priorizados de 2026, depois 2025/2024/2023, inclusive as fases escritas e orais efetivamente públicas. Busca literal continua sendo só triagem.
3. Concluir proveniência dos legados, cotejo normativo e jurisprudencial, atribuição doutrinária e pesquisa de dissenso por item. Gabarito preliminar TJPE e disputa PCPIQ72 não estão resolvidos.
4. Só depois congelar a unidade, abrir a reserva, medir suficiência e colher a validação de legibilidade do usuário. Não há nota simulada nem aprovação editorial inferida.

Fila concreta em [NEXT_EXECUTION_QUEUE.csv](NEXT_EXECUTION_QUEUE.csv). Ela é um estado de retomada para execução autônoma, não uma solicitação ao usuário para administrar tarefas. Esta rodada não instala execução em segundo plano.

## Reprodução local

Os scripts geram índices e validações a partir dos snapshots. Não são GitHub Actions nem um motor de estudo automatizado.

```bash
python research/work_2026-10-01/catalogue.py
python research/work_2026-10-01/curate.py
python research/work_2026-10-01/graph.py
python research/work_2026-10-01/audit.py
```

`extract.py` requer PyMuPDF e `pdftotext`; recusa os nomes `HELDOUT_`. `harvest.py` realiza aquisição somente quando explicitamente executado com um manifesto. Os scripts de reconstrução não fazem rede. A ausência de erro de integridade não é aprovação dos gates jurídicos ou de cobertura.
