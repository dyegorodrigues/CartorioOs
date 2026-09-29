# GX Cartório OS — Depth Budget RI v0.2

Snapshot: 2026-09-11
Status: BUILD refinado; pré-freeze learner-facing.

## Mudanças sobre v0.1
1. separa `prazo-base de qualificação` de `duração/cessação da prenotação` para evitar memorização falsa de um único prazo;
2. inclui art. 206-A como boundary de pagamento/prenotação;
3. formaliza `dúvida` como procedure node autônomo;
4. divide usucapião em knowledge/procedure/output;
5. trata sistemas 2026 como overlay HOT, não como núcleo enciclopédico de P1;
6. adiciona rubrics operacionais de RI como requisito de BUILD.

## Tronco P1
`APRESENTAÇÃO → PROTOCOLO/PRENOTAÇÃO → PRIORIDADE → QUALIFICAÇÃO → REGISTRO/AVERBAÇÃO OU EXIGÊNCIA → DÚVIDA QUANDO CABÍVEL → SAÍDA`.

## Must-know P1
- art. 186: número de ordem determina prioridade do título e preferência dos direitos reais;
- art. 188: registro ou nota devolutiva em 10 dias; hipóteses legais do §1º em 5 dias;
- art. 198: exigência escrita, única, articulada, clara e objetiva; discordância/impossibilidade abre caminho à dúvida;
- dúvida: impugnação em 15 dias; decisão administrativa; procedência/improcedência produzem saídas distintas;
- art. 205: efeitos da prenotação cessam após 20 dias quando a falta de registro decorre de omissão do interessado em atender exigências; Reurb-S possui regra de 40 dias;
- art. 206-A: pagamento e manutenção/finalização do protocolo possuem disciplina própria;
- arts. 212–213: retificação administrativa saneia omissão/imprecisão/inverdade sem excluir via judicial;
- art. 216-A: usucapião extrajudicial tramita no RI competente, com advogado e documentação legal, e rejeição não impede ação judicial.

## P1 must-understand
- prioridade registral não é simples cronologia do negócio material;
- `10 dias`, `5 dias`, `15 dias` e `20 dias` pertencem a eventos jurídicos diferentes;
- qualificação negativa não é sentença sobre domínio;
- nota devolutiva é ato técnico controlável, não lista arbitrária de exigências;
- ata notarial instrui usucapião, mas o reconhecimento/registro depende do procedimento perante RI;
- retificação não é aquisição patrimonial disfarçada.

## P2 obrigatório pelo corpus
- conflitos de prioridade e indisponibilidade superveniente;
- segunda hipoteca/prioridades especiais quando a banca demonstrar;
- impugnação justificada x injustificada em usucapião;
- notificações e unidade autônoma de condomínio;
- qualificação e nota devolutiva em caso integrado;
- saneamento/retificação sob CNN atual;
- CNIB/Constrijud/SERP quando a questão depende do fluxo nacional vigente.

## P3 — produção avançada

Redigir nota devolutiva, fundamentar dúvida e executar skeleton de ato quando a fase e o domínio justificarem. A produção usa os mesmos IDs do núcleo jurídico.

## P4 — referência residual
- minúcia tecnológica interna dos operadores;
- listas extensas de documentos sem evidência de cobrança;
- exceções estaduais antes de edital-alvo;
- doutrina histórica de princípios sem impacto em decisão/questão.

## Depth matrix
| Nó | P1 | P2 | Output | Freshness |
|---|---|---|---|---|
| Protocolo/prioridade | VH | VH | H | M |
| Prazo/nota devolutiva | VH | H | H | M |
| Qualificação | H | VH | VH | H |
| Dúvida | H | H/VH | H | M |
| Usucapião | H | VH | VH | H |
| Retificação | M/H | H | H | H |
| Indisponibilidade | M/H | VH | H | VH |
| Sistemas 2026 | arquitetura M | H/VH | H | VH |

## Evidência multibanca já demonstrada
- FGV/ENAC: usucapião, prioridade, indisponibilidade, aplicação procedimental;
- Cebraspe/TJRO: qualificação registral e peça prática com atuação profissional;
- IESES/TJPA: prenotação, princípios/livros e literalidade estruturante.

## Gate para freeze RI
- procedure rubrics existentes;
- fontes vigentes revalidadas;
- BUILD/CHALLENGE separados;
- RI-H1/RI-H2 mantidos selados;
- challenge pré-freeze encontra e corrige gaps;
- somente depois gerar `RI_INTERNAL_FREEZE_V0.1` e abrir held-out.

## Correção de auditoria — 12/09/2026

Os rótulos anteriores de confiança eram julgamento editorial, não medida empírica. Freeze é preservação de versão, não certificado de freshness ou de challenge. Não foi localizada documentação suficiente para dar esses gates como cumpridos na rodada de 12/09.

Ligar ao P1 os patches `LRP-RI-DUVIDA-014`, `LRP-RI-PAGAMENTO-015` e `LRP-RI-PRAZO-SANCAO-016`; `LRP-RI-CITACAO-017` é contraste pontual. Conteúdo e derivações estão em `material/specimens/LRP_RI_AUDIT_PATCH_V0.3_2026-09-12.md`. Estado: BUILD corrigido; S2 pendente e overlays HOT não certificados.
