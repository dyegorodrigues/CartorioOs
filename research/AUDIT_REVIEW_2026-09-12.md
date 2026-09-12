# Auditoria crítica — Cartório OS

Data: 12/09/2026. Base remota: `a502b45245d014ac080ed161a8653868026f7330`.
Escopo: revisão da rodada autônoma de 12/09, com verificações pontuais nas bases que ela avaliou. Não é auditoria integral de currículo, ENAC, Notion ou de todas as normas vigentes.

## Veredito

A direção arquitetural permanece aproveitável, mas a execução continha erros jurídicos e exageros de validação. O principal problema não era falta de mais pesquisa: era atribuir força probatória maior do que a evidência permitia. Corrigir o material não demonstra que ele passou; citar fonte oficial não demonstra que seu artigo final foi lido; mudar de modelo não torna uma revisão no mesmo contexto automaticamente independente.

**Dois patches editoriais v0.3 produzidos; zero novos passes independentes; nenhum S2 nem liberação de estudo.** O histórico de erros foi preservado.

## Achados e correções

| ID / gravidade | Problema confirmado | Tratamento |
|---|---|---|
| A01 MUST | Prov.255 marcado vigente na publicação e anterior ao cutoff | Art.119 tem 30 dias de vacatio. Corrigidos Freshness, fila de impacto e registros operacionais. |
| A02 MUST | RG-Q22 marcado PASS sem átomos expressos no specimen | PASS revogado; prazo cautelar/correção e desfecho patrimonial explicitados no patch. |
| A03 MUST | Rubrica e specimen de dúvida colocavam impugnação antes da remessa | Corrigidos gatilho da remessa, ramo da impugnação e saídas após trânsito. |
| A04 MUST | Pagamento ensinado sem conexão explícita com relógio do registro | Incluído art.206-A §7º e sua derivação de revisão. |
| A05 MUST | Q11/TJPA usada como triangulação sem informar anulação | Mantida como descoberta, excluída de confirmação/score válido. |
| A06 MUST | Ausência de trilha cega e exposição de itens vizinhos | Rebaixada força da evidência para cobertura; registrada quarentena, sem reaproveitamento limpo. |
| A07 SHOULD | P3 empregado como referência residual | P3/P4 separados nos budgets ativos RI v0.2 e Emolumentos. Nomenclaturas antigas de outros documentos não foram migradas integralmente. |
| A08 MUST | Próximo marco sugeria encerramento automático da Rodada 1 | Saída não demonstrada; preparar verificações da fábrica não cumpre gate de promoção. |
| A09 MUST | RG0B ensinava território, mas não atribuições básicas da Q20 | Patch específico de arts.7º V e 11 III. Questão consumida, não novo held-out. |
| A10 SHOULD | Q15/RI gerou dois gaps obrigatórios, embora E dependesse diretamente da sanção | Mantido gap decisivo do art.188 §2º; título registrável tratado como discriminação auxiliar, sem inflar P1. |
| A11 MUST | Registry corrigia locator TJSP/TJAL, mas ledger RG ainda anunciava confirmação Vunesp/SP | Propagada quarentena às menções e ao Signal Board, sem reatribuir questões a outro certame por suposição. |

### A01 — conflito entre metadado e dispositivo

O [texto CNJ](https://atos.cnj.jus.br/atos/detalhar/6981), a [reprodução STJ](https://www.stj.jus.br/internet_docs/biblioteca/clippinglegislacao/Prt_255_2026_CNJ.pdf) e o [DJe reproduzido pelo TSE](https://sintse.tse.jus.br/documentos/2026/Ago/21/diario-da-justica-eletronico-cnj-edicao-anterior/provimento-no-255-de-19-de-agosto-de-2026-institui-a-consolidacao-nacional-da-execucao-efetiva-e), p.70, confirmam a vacatio. A ficha CNJ usa “Vigente”; o cadastro não dispensa interpretação temporal do art.119.

O [edital ENAC 2026.2](https://conhecimento.fgv.br/sites/default/files/concursos/minuta-edital-enac-2026.2-27.08.26-versao-final.pdf), itens 8.1/8.8.1, fixa prova provável em 22/11 e exclui vigência iniciada menos de 90 dias antes. Cutoff: 24/08. Mesmo o limite inferior conservador de vigência do Prov.255 é posterior: seus preceitos novos não passam nesse filtro. Isso não retira conteúdo antigo reproduzido, nem fixa regra para edital 2027 ainda não examinado.

Data jurídica exata de publicação e homologação das plataformas continuam pendentes. Art.118 usa outro gatilho, não a publicação. Não houve inventário exaustivo de modificadores nesta auditoria.

### A02/A09 — menção não equivale a ensino

No RG v0.2, a seção cautelar dizia “prazo legal”, enquanto 90+30 aparecia apenas na sanção; faltava correção monetária. O critério de intervenção também substituía conveniência para os serviços por conveniência à apuração. Q22/B e Q20/C foram conferidas no [caderno FGV Remoção, pp.7](https://conhecimento.fgv.br/sites/default/files/concursos/atividade-notarial-e-de-registro-ingresso-por-remocaocar-001-tipo-1-copia.pdf), no [gabarito definitivo, p.1](https://conhecimento.fgv.br/sites/default/files/concursos/gabarito-definitivo-tjes-notarial.pdf) e na [Lei 8.935](https://www.planalto.gov.br/ccivil_03/leis/l8935.htm). O patch explica o que faltava; não reclassifica retrospectivamente a base como suficiente.

### A03/A04 — grafo errado pode ensinar erro com eficiência

A [LRP](https://www.planalto.gov.br/ccivil_03/leis/l6015compilada.htm), arts.198 §1º, 199, 203 e 206-A §7º, refuta a sequência e a omissão encontradas. Um fluxo visual ou uma Q→A herda os erros da proposição de origem. Por isso a correção foi ligada a IDs e propagada à rubrica, não feita somente em prosa avulsa.

### A05 — fonte oficial também contém itens inutilizáveis para pontuar

O [gabarito IESES 6104](https://iesesconcursos.nyc3.cdn.digitaloceanspaces.com/2025/tjpa_001_2025/documentos/gabaritos/6104.pdf) marca Q11 como X e define X como anulada. A anulação não torna a questão inútil para descoberta, mas impede apresentá-la como resposta válida confirmada. Não foi inferido o motivo da anulação.

### A06 — limites reais da independência

Os SHA locais registram a sequência relatada na máquina original, mas as quatro alterações foram consolidadas em um único commit remoto. Não apagar essa diferença. Os três textos frozen permanecem byte a byte iguais, com SHA-256 no ledger de auditoria. Isso prova integridade da versão atual, não reconstrói por si a ordem de exposição da sessão anterior.

Prova e gabarito conhecidos permitem comparar átomos presentes/ausentes. Não permitem alegar desempenho de aluno, taxa de generalização ou resolução cega. Tampouco um modelo diferente garante ausência de conhecimento prévio da questão. Um próximo teste independente precisa de escopo/versionamento/resposta e referências selados antes da consulta ao gabarito, além de rastreio de exposição e duplicidade.

Não foi aberto novo pool. H1/H2/H4/H5 e vizinhos expostos foram sinalizados. O PASS antigo RG-H9-Q1 permanece como registro histórico não reauditado, sem transferência automática para v0.3.

## Hipóteses que a auditoria rejeitou

- **“Q14/TJES Remoção é necessariamente gap de retificação.”** Não: a questão é de averbação de valores no SFH/Lei 4.380, e não saneamento de assento LRP212–213. A exclusão foi fundamentada, não usada para esconder falta de ensino. Continua candidata a nó futuro.
- **“Toda explicação ausente de um distrator exige aprofundar o MASTER.”** Não: distinguir átomo decisivo, discriminação útil e referência residual; evitar enciclopédia por reação a uma prova.
- **“Mais provas abertas resolverão a validação.”** Não sem escopo, versão, amostra pertinente e isolamento de exposição. Nenhum loop de coleta foi iniciado.
- **“Esta revisão encerra a Rodada 3 porque o usuário escolheu Astra.”** Não: o contexto é compartilhado; é revisão crítica, não certificação de auditor independente.

## O que foi implementado e testado

Correções jurídicas: overlays `REGIME_GERAL_AUDIT_PATCH_V0.3_2026-09-12.md` e `LRP_RI_AUDIT_PATCH_V0.3_2026-09-12.md`. Integração: rubrica RI, ledgers RI/RG, budgets ativos, relatórios, registries, Freshness, STATUS e handoff. Sem redesign da árvore, mudança de mastery ou sessão de aluno.

`data/audit/validation_review_2026-09-12.json` registra cinco decisões auditadas e três hashes de bases. `scripts/audit_checks.py` verifica invariantes; os testes usam fixtures sintéticas explicitamente separadas de provas reais.

Reprodução:

```bash
python3 -B -m unittest discover -s tests -v
python3 -B scripts/audit_checks.py
git diff --check
```

Os testes mecânicos verificam: limites de 89/90/91 dias, data desconhecida sem aprovação, norma ainda não vigente, falso PASS sem átomos, item anulado/fora de escopo, reutilização BUILD, fonte/snapshot não verificados, resposta não selada, IDs duplicados, alteração de frozen e bloqueio de liberação. **Não testam verdade jurídica, suficiência editorial, retenção nem aprovação futura.**

## Saída e pendências delimitadas

Rodada 1 permanece sem saída demonstrada. Prioridades imediatas: consolidar as versões corrigidas sem múltiplas verdades; conferir fontes HOT necessárias ao escopo; preparar cobertura por proposição e critérios prévios de teste. Preparar a fábrica é permitido; promover o produto continua condicionado aos gates e à decisão de iniciar estudo.

Esta auditoria não reconciliou novamente as 304 linhas Notion, não reconstruiu os 300 ENAC, não atualizou Contest History e não revalidou integralmente CNN/STF/STJ. Não confundir o lote de correções com conclusão dessas frentes. A contenção de rodadas continua: registrar/rebaixar módulos insuficientes, sem engenharia infinita nem falsa aprovação.
