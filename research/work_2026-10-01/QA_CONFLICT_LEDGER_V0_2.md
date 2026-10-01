# QA e conflitos — rodada Work de 01/10/2026

Este registro complementa o ledger v0.1; nenhum original foi corrigido silenciosamente. “Resolvido” descreve o problema identificado, não aprovação de todo o tema jurídico.

| ID | Achado e evidência | Decisão / estado |
|---|---|---|
| WQA-001 | `MPRJ_2026_Q23` legado dizia que o consentimento era irrelevante. Isso corresponde à alternativa B, rejeitada. Caderno tipo1 + gabarito preliminar Q23=D + aviso oficial de manutenção após recursos (`FGV_PAGE_011_DOC_71/70/67`). STJ AREsp2.330.912 confirma a distinção contextual. | **Erro do corpus legado corrigido na nova versão.** Não é conflito entre a banca e o STJ. Legado permanece no ledger de migração. |
| WQA-002 | Datas de publicação foram usadas como aplicação. Documentos de gabarito: MPRJ31/05, MPMT14/06, ENAM07/06, TJPR22/02, TJBA24/05; datas2026. | Corrigir campos novos com fonte individual em `TARGET_EXAM_UNIVERSE_V0_2.csv`. Diferença publicação/aplicação não é, sozinha, contradição oficial. |
| WQA-003 | AGU/Procurador Federal, edital2022, tem aplicação **07/05/2023** no gabarito `CEB_AGU_22_PROCURADOR_FEDERAL_DOC_12`. | **Incluído na janela.** Não excluir ciclo inteiro pelo ano do edital. |
| WQA-004 | “Sem rótulos introdutórios” foi transformado em sinal negativo de relevância. TJPEQ41/Q48 cobram limites de extensão e abolitio; PCDFQ74 tem justificativa expressa de ultima ratio, fora do recorte que a classificação secundária sugeria. | **Sinais negativos legados rebaixados a descoberta parcial**, nunca prova de ausência semântica. |
| WQA-005 | DPE-RO2025 FGV, DPE-RS2023 FGV e MPES26FGV são páginas de pessoal de apoio; MPES25promotor é outro concurso. | Excluídos do núcleo de carreira. Reserva DPE-RO errada conservada como tentativa rejeitada, substituída por DPE-PE. |
| WQA-006 | PCPIQ72 tem gabarito B/II; v0.1 relata comentário Estratégia favorável também aI. | **Aberto.** O comentário não foi readquirido nesta rodada. Não resolver por consenso inventado nem estender benefício por analogia a partir da crítica criminológica. |
| WQA-007 | PDF de gabarito PCPI informa aplicação25/01/2025; ciclo e demais registros apontam2026. Publicação27/01/2026 é outro campo. | Conservar conflito literal do PDF; **data de aplicação ainda não fechada no CSV novo**. Precisa triangulação com convocação oficial. |
| WQA-008 | TJPE gabarito encontrado é preliminar (`FGV_PAGE_006_DOC_17`), disponibilizado junto ao caderno em setembro. | **PRELIMINARY** em todos os registros novos. Não chamar definitivo nem supor julgamento de recursos futuro. |
| WQA-009 | TJBAQ48: alternativaE fala em tentativa de furto; enunciado menciona saque do numerário. Pode haver tensão sobre inversão da posse. | **Hipótese de defeito, não erro demonstrado.** Não entrou no corpus de regras. Exige exame integral do fato e precedente antes de qualquer crítica definitiva. |
| WQA-010 | PCDF caderno com justificativas preliminares contém respostas posteriormente anuladas: Q67,Q69, entre outras, estãoX no definitivo (`DOC_1`). | Justificativa pública não sobrepõe gabarito definitivo. Q73/Q74 novas permanecemE no definitivo; verificadas. |
| WQA-011 | PCDF edital11 publicado30/09 fixa oral em **10 e11/10/2026** (`CEB_PCDF_LATEST_1`, item3.1). Legado apontava08–11/10. | Metadado futuro atualizado; **não contar oral ainda não aplicada como questão real2026**. |
| WQA-012 | MPMS documento do edital14 também contém edital15; no texto deste há prazo final de recurso19/06/2024 em contexto2026. | Anomalia de data preservada, sem contaminar o gabarito anexo. Não corrigir PDF nem inferir cronograma. |
| WQA-013 | MPPA discursiva2023 art.28 é anterior ao Tema506/STF. | **HISTORICAL_RUBRIC**. Não converter em regra geral vigente sobre todas as drogas; separar despenalização histórica, cannabis para uso pessoal e outras substâncias. |
| WQA-014 | Acesso direto STJ retornou403; STF502; MPSP403; CNJ403; MPT500. Algumas fontes STJ puderam ser lidas pelo serviço web. FUNDATEC retornou202, não prova legível. | Manter a falha HTTP e a evidência web como modos de acesso distintos. Snapshot de busca não equivale ao PDF oficial integral arquivado. |
| WQA-015 | Download PF discursiva falhou inicialmente por espaço/Unicode na URL oficial. | Corrigida a codificação no coletor e criada tentativa `CEB_PF_25_DOC_59_RETRY1`; falha inicial mantida no log. Não foi bloqueio de credencial. |
| WQA-016 | Reservas contêm prova inteira e chave; conteúdo não extraído no BUILD. A exposição em conversas anteriores não pôde ser integralmente auditada. | **RESERVED_NOT_VALIDATED**, sem alegar isolamento absoluto ou suficiência medida. Validar após congelamento e substituir qualquer item contaminado. |
| WQA-017 | Autor no enunciado não torna equivalentes todas as teorias atribuídas a ele. MPMSQ14V cobra prevenção positiva limitadora/Hassemer. | Não promover automaticamente “Direito de Intervenção” a necessidade do núcleo só pelo nome do autor. |
| WQA-018 | Página MPF30 tem link rotulado Prova Objetiva apontando ao mesmo endereço de gabarito preliminar. | **Metadado oficial a resolver**; não contar rótulo como aquisição de caderno. Preservado no catálogo. |
| WQA-019 | PC-RO2022, PC-PB2022 e programas orais antigos aparecem no legado. | Referência histórica/descoberta, fora da incidência2023–2026 até prova de aplicação na janela. Não desapareceram: constam da migração. |
| WQA-020 | 143 linhas de catálogo incluem candidatos, índices institucionais e nove exclusões/páginas-pai. | Não anunciar “143 provas auditadas”. O denominador nacional continua aberto. |

## Fontes jurídicas lidas via web

- [STJ — consentimento e medida protetiva, 15/09/2023](https://www.stj.jus.br/sites/portalp/Paginas/Comunicacao/Noticias/2023/15092023-Permissao-da-vitima-para-aproximacao-do-reu-afasta-violacao-de-medida-protetiva-da-Lei-Maria-da-Penha.aspx): notícia institucional e identificação do AREsp2.330.912; `discovery/legal_primary_open.json`.
- [STJ — poluição/Tema1377, 07/11/2025](https://www.stj.jus.br/sites/portalp/Paginas/Comunicacao/Noticias/2025/07112025-Crime-de-poluicao-ambiental-e-formal-e-se-configura-mesmo-sem-efetiva-ocorrencia-de-dano-a-saude.aspx): tese se refere à primeira parte do caput do art.54. Não universalizar para todo tipo ambiental.
- [STJ — acórdão publicado25/11/2024](https://scon.stj.jus.br/SCON/GetInteiroTeorDoAcordao?dt_publicacao=25%2F11%2F2024&num_registro=202302395256): a segunda parte do antigo art.89 não foi reproduzida; a primeira não foi automaticamente abolida. Votos e histórico do processo não devem ser confundidos com a conclusão vencedora.

As buscas não equivalem a revisão sistemática de todo dissenso. Campo não investigado continua `NOT_SEARCHED_SYSTEMATICALLY`.
