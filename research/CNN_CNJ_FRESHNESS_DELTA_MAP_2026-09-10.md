# GX Cartório OS — CNN/CNJ Freshness Delta Map

Snapshot: 2026-09-10
Status: infraestrutura HOT do Freshness Firewall; NÃO é material de estudo.

## Fonte-base canônica
- Provimento CNJ 149/2023 — CNN/CN/CNJ-Extra, texto compilado oficial: https://atos.cnj.jus.br/atos/detalhar/5243
- Resolução CNJ 696/2026 — regime atual dos concursos de outorga: https://atos.cnj.jus.br/atos/detalhar/7011
- ENAC 2026.2 — Edital 2/2026 FGV/CNJ: https://conhecimento.fgv.br/sites/default/files/concursos/minuta-edital-enac-2026.2-27.08.26-versao-final.pdf

## Regra-mãe
O Provimento 149/2023 está formalmente `ALTERADO`, não é um PDF congelado. O GX deve tratar o CNN/CNJ como um corpus versionado. Questão antiga continua útil como evidência de cobrança, mas nenhuma proposição vira MASTER atual sem revalidação contra o texto compilado vigente e atos modificadores supervenientes.

## Regra especial ENAC 2026.2 — janela normativa de 90 dias
O edital vigente do ENAC 2026.2 estabelece que:
- preceitos normativos cuja vigência tenha se iniciado **menos de 90 dias antes da prova** não serão objeto do exame;
- preceitos revogados dentro desse mesmo período poderão ser cobrados.

Prova prevista: **22/11/2026**.
Cutoff aritmético de 90 dias: **24/08/2026**.

Consequência operacional para o snapshot 2026.2:
- atos com vigência iniciada em 24/08/2026 ou antes entram no radar material, ressalvada regra específica de vigência;
- atos com vigência posterior a 24/08/2026 ficam fora do conteúdo material do ENAC 2026.2, embora possam governar o próprio exame ou afetar concursos estaduais posteriores;
- atos revogados após 24/08/2026 podem continuar cobrados no ENAC 2026.2 conforme a cláusula do edital;
- o GX deve manter `CURRENT LAW` e `EXAM SNAPSHOT LAW` como campos distintos.

Essa regra impede um erro clássico de atualização: ensinar apenas o direito mais novo quando o edital congelou parte do universo normativo em data anterior.

## Deltas relevantes de 2026 já confirmados em fonte oficial CNJ

| Ato | Data | Situação | Tema | Artigos/nós atingidos já identificados | Volatilidade | Impacto no Atlas |
|---|---|---|---|---|---|---|
| Prov. 211 | 28/01/2026 | vigente | papel de segurança / transição digital | revoga arts. 461 e 461-A; regra de emissão física sob solicitação | medium | Notas/RCPN/certidões; não manter regra antiga de papel como absoluta |
| Prov. 212 | 20/02/2026 | vigente | gratuidade de informações para Fazenda | art. 184-A §9 | high | emolumentos/fiscal/RI; questão histórica precisa conferir gratuidade nacional atual |
| Prov. 214 | 26/02/2026 | vigente | TI + extinção de cláusulas resolutivas | arts. 88 §4, 206 e 439-A, entre outros ajustes | high | LGPD/TI + RI; conecta CNN ao Prov. 213 e legislação material |
| Prov. 217 | 09/03/2026 | vigente | indisponibilidade / circunscrição | art. 320-I §2 | high | RI: matrícula/transcrição, circunscrição atual/origem, abertura de matrícula |
| Prov. 218 | 13/03/2026 | vigente | Sistema Justiça Aberta | arts. 136 e ss. | high | Regime Geral/fiscalização/dados; alimentação é dever funcional |
| Prov. 219 | 20/03/2026 | vigente | relação geral de vacâncias | disciplina própria + remissão do CNN art. 73 | very high | vacância/interinidade/concurso; também integrado à Res. 696/2026 |
| Prov. 220 | 22/04/2026 | vigente | incapacidade permanente de delegatário | procedimento nacional ligado ao art. 39 III da Lei 8.935 | very high | extinção da delegação, devido processo, regime administrativo |
| Prov. 224 | 12/05/2026 | vigente | Constrijud / Serp-Jud | nova Seção art. 320-X e seguintes | very high | RI: ordens judiciais, prenotação, qualificação, fluxo eletrônico |
| Prov. 225 | 20/05/2026 | vigente | publicidade de protestos / ordens judiciais | bloco CENPROT/protesto | high | Protesto: certidões, sustação, litigância abusiva/predatória |
| Prov. 227 | 09/06/2026 | vigente | solvência trabalhista do delegatário | provimento autônomo, ligado a L8935 arts. 20, 31 I e 36 | very high | Regime Geral: empregador/prepostos, declaração anual, fiscalização/PAD; não linearizar tudo em P1 sem corpus |
| Prov. 228 | 16/06/2026 | vigente | extratos eletrônicos no RI | art. 208 II b + arts. 210-A a 210-Q | very high | RI/SERP: extrato, emitente, qualificação, nota devolutiva, responsabilidade, interoperabilidade |
| Prov. 229 | 16/06/2026 | vigente | ecossistema SERP / Meu Registro / interoperabilidade | art. 228-J e seguintes | very high | arquitetura nacional dos registros eletrônicos e operadores nacionais |
| Prov. 237 | 13/07/2026 | vigente | CNS/acervo/certidões + reprodução assistida | múltiplos nós RCPN/acervo | high | identificação de acervo, sucessão de serventias, RCPN |
| Prov. 242 | 21/07/2026 | vigente | base nacional RTDPJ | art. 256-A e seguintes | very high | RTD/PJ, SERP, identificadores nacionais, governança de dados |
| Prov. 246 | 28/07/2026 | vigente | alienação fiduciária / forma do instrumento | art. 440-AO | very high | RI/alienação fiduciária; adequação explícita a STF + STJ + Lei 9.514 |
| Prov. 253 | 18/08/2026 | vigente | CENPROT / certidões após sustação | bloco Protesto/CENPROT | very high | Protesto: resposta deve refletir situação jurídica atual do registro |
| Prov. 255 | 19/08/2026 | **VACATIO em 12/09: art.119 prevê 30 dias após publicação** | Consolidação Nacional da Execução Efetiva | execução de títulos no Poder Judiciário; conexões registrais dependem de dispositivo específico | high cross-system | preceitos novos fora da janela ENAC 2026.2; watchlist 2027, sem promoção automática |

### ENAC 2026.2 eligibility overlay desta tabela
Todos os atos acima estão datados antes do cutoff de 24/08/2026. A elegibilidade concreta ainda depende da **data de início de vigência** de cada preceito, porque alguns atos têm vacatio específica. O campo `EXAM_2026_2_ELIGIBLE` deve ser calculado pela vigência, não apenas pela publicação.

**Errata auditada em 12/09/2026:** a classificação anterior do Provimento 255 como vigente desde a publicação estava errada. O art.119 determina 30 dias de vacatio. O DJe nº197 foi disponibilizado em 20/08; não confundir disponibilização com publicação jurídica. Mesmo usando 20/08 como limite inicial conservador, o início de vigência não seria anterior a 19/09, portanto posterior ao cutoff de 24/08 e ao snapshot de 12/09. A data jurídica exata permanece pendente de conferência da publicação; isso não impede excluir seus **preceitos inovadores** pelo item 8.8.1 do edital atual. Normas antigas eventualmente reproduzidas continuam avaliadas por sua fonte e vigência próprias.

Além disso, art.118 prevê implementação obrigatória das plataformas em 120 dias **da respectiva homologação/validação**, não da publicação. Não inventar data de homologação nem converter automaticamente esse prazo em data-calendário. O ato trata execução de títulos judiciais/extrajudiciais no Judiciário; a palavra “extrajudicial” não demonstra, sozinha, novo procedimento de cartório.

A [ficha oficial CNJ 6981](https://atos.cnj.jus.br/atos/detalhar/6981) tem rótulo cadastral “Vigente”, mas também reproduz a vacatio de 30 dias do art.119. Registrar ambos: o rótulo geral não substitui o cálculo temporal para uma data de referência nem a cláusula de exclusão do edital.

Fontes conferidas: [DJe CNJ, pp.51 e 70, cópia TSE](https://sintse.tse.jus.br/documentos/2026/Ago/21/diario-da-justica-eletronico-cnj-edicao-anterior/provimento-no-255-de-19-de-agosto-de-2026-institui-a-consolidacao-nacional-da-execucao-efetiva-e), [cópia STJ, arts.118–119](https://www.stj.jus.br/internet_docs/biblioteca/clippinglegislacao/Prt_255_2026_CNJ.pdf) e edital FGV acima, itens 8.1 e 8.8.1. Conferência pontual: não recertifica os demais atos desta tabela nem cobre eventuais modificadores ainda não auditados.

## Provimentos autônomos que NÃO devem desaparecer por estarem fora do corpo textual do CNN
Dois riscos do modelo “só leia o Provimento 149 compilado”:
1. ato autônomo relevante pode dialogar com o CNN sem estar totalmente absorvido nele;
2. concurso pode cobrar a regra nacional vigente pelo ato autônomo.

Exemplos já confirmados:
- Prov. 219/2026 — vacâncias;
- Prov. 220/2026 — incapacidade permanente;
- Prov. 227/2026 — solvência trabalhista;
- Prov. 228/2026 — extratos eletrônicos RI.

## Relação com CF art. 236 e Lei 8.935
Freshness não é só `qual é o artigo atual?`. O Compiler precisa manter arestas explícitas:
- CF art. 236 → delegação privada, fiscalização judicial, emolumentos e concurso;
- Lei 8.935 → regime orgânico do delegatário;
- CNN/CNJ → uniformização administrativa/operacional nacional;
- jurisprudência STF/STJ → limites, responsabilidade, interinidade e interpretação;
- Res. 696/2026 → o que pode ser cobrado e em qual fase.

## Tags temporais por proposição
Cada proposição derivada de CNN/CNJ deve registrar:
- `SOURCE_ID` + artigo atual;
- `SNAPSHOT_DATE`;
- `EFFECTIVE_FROM`;
- `LAST_KNOWN_MODIFIER`;
- `SPECIALTY`;
- `VOLATILITY = stable | volatile | recently_changed`;
- `REVALIDATE_ON`: novo provimento/resolução/lei/tema vinculante ou antes de simulado/prova-alvo;
- `CURRENT_LAW`;
- `EXAM_SNAPSHOT_LAW`;
- `CONTENT_VALIDITY` de questões históricas;
- `PHASE_VALIDITY` quando a arquitetura do concurso mudou.

## Regra de uso de questão antiga
- `VALID_CURRENT`: forma e regra material atuais;
- `FORM_ONLY`: distrator/estrutura útil, direito material alterado;
- `PARTIAL`: parte da questão ainda serve;
- `RETIRED`: não usar pedagogicamente salvo história normativa.

Questão `FORM_ONLY/PARTIAL` nunca entra em cálculo de mastery sem reescrita/explicitação da mudança.

## Triagem pedagógica dos deltas
`RECENTLY_CHANGED` não significa automaticamente `DECORE AGORA`.

O Compiler cruza:
1. centralidade no currículo atual;
2. incidência observada;
3. probabilidade de cobrança por novidade normativa;
4. custo cognitivo;
5. especialidade e fase;
6. dependências.

Exemplo: Prov. 227/2026 é recente e importante para Regime Geral, mas seu detalhamento patrimonial completo pode ficar em P2/REFERENCE enquanto P1 registra a arquitetura, dever declaratório, fiscalização e vínculo com arts. 20/31/36 da Lei 8.935.

## Watchlist imediata 2027
Antes de qualquer liberação de estudo/simulado:
- pesquisar novos atos CNJ que alterem Prov. 149/2023;
- pesquisar atos que alterem/integrem Prov. 219, 220, 227, 228 e 229;
- revalidar Res. 696/2026 e editais ENAC;
- calcular automaticamente o cutoff normativo específico de cada edital;
- revalidar Lei 6.015, Lei 8.935, Lei 9.492, Lei 9.514 e Lei 14.382;
- revalidar temas vinculantes STF/STJ ligados aos nós estudados.

## Próxima expansão
1. ligar cada delta a IDs de proposição do Atlas;
2. marcar questões ENAC/estaduais afetadas;
3. criar `CHANGE_IMPACT_QUEUE` para patches automáticos em MASTER/REVIEW/Q→A/questões;
4. incorporar `CURRENT_LAW x EXAM_SNAPSHOT_LAW` ao Depth Budget e simulados.
