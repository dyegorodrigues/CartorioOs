# GX Cartório OS — Depth Budget v0.3
## N/R — Regime Jurídico Geral

Snapshot: 2026-09-11
Status: pós-CHALLENGE + pós-HELD-OUT H7; pronto para novo BUILD freeze. NÃO estudar ainda.

## Por que existe v0.3
O specimen v0.1, derivado do budget v0.2, foi congelado e testado contra um recorte do TJSC/Cebraspe 2023. Três questões in-scope revelaram três omissões reais:
- circunscrição territorial básica (arts.8–13);
- microfluxo do art.36 (afastamento/interventor/renda);
- previdência e contagem recíproca (art.40).

O objetivo do patch é **aumentar suficiência sem virar enciclopédia**.

## Arquitetura v0.3
`RG0 natureza/delegação → RG0B atribuições/territorialidade → RG1 ingresso → RG2 gestão/prepostos → RG3 responsabilidade → RG4 incompatibilidades/impedimentos → RG5 independência/direitos/deveres → RG6 disciplina/perda/intervenção → RG7 vacância/interinidade → RG8 extinção/previdência + overlays CNN`

## Budget por cluster

| Cluster | P1 | P2 | P3+ | Memory | Questions | Output | Conf. |
|---|---|---|---|---|---|---|---|
| RG0 Natureza/CF236 | caráter privado por delegação; serviço público delegado; profissional do Direito/fé pública; fiscalização; serventia sem personalidade autônoma | legitimidade/processo e conexões constitucionais | doutrina histórica | H | H | H | A |
| **RG0B Atribuições/territorialidade** | competência básica dos serviços; tabelião de notas: livre escolha, mas não atua fora do Município da delegação; RI + RCPN sujeitos à circunscrição geográfica do art.12 | peculiaridades territoriais de protesto/outros serviços ficam nas especialidades | normas locais/cartografia específica | H | H/VH | M | A |
| RG1 Ingresso arts.14–19 | requisitos; bacharel x 10 anos; provimento/remoção; falso amigo 3 anos | procedimento recorrente/Res696 | edital local | VH | VH | M | A |
| RG2 Gestão/prepostos arts.20–21 | categorias, vínculo, substituto/escrevente/auxiliar, gestão do titular | limites de atos, testamento, supervisão | minúcias trabalhistas | H | H/VH | H | A/B |
| RG3 Responsabilidade arts.22–24 + Tema777 | culpa/dolo atual; prepostos; regresso; 3 anos; Estado x delegatário; civil x penal | temporalidade pré/pós Lei13.286; Tema777; legitimidade | controvérsias raras | VH | VH | VH | A |
| RG4 Incompatibilidades/impedimentos arts.25–27 | incompatibilidades; afastamento; pessoalmente; até 3º grau | casos compostos | residual | VH | VH | M | A |
| RG5 Independência/direitos/deveres arts.28–30 | independência; direitos; deveres por função; palavras fatais | heatmap por inciso; publicidade/sigilo; digital/CNJ | residual/local | H seletiva | VH | H | A/B |
| **RG6 Disciplina/perda/intervenção arts.31–36** | infração→pena→procedimento; 90+30; perda judicial OU administrativa; ampla defesa; **art.36: afastamento preventivo + interventor + metade da renda/conta especial** | proporcionalidade, culpa de supervisão, Prov227, TAC/medidas quando cabíveis | PAD local | VH | VH | VH | A |
| RG7 Vacância/interinidade | titular x interino; continuidade; Tema779; mapa da vacância | Prov219; ADI1183/>6m; Prov220 | operacional/anexos | H | H | VH | A/B |
| **RG8 Extinção/previdência** | mapa das hipóteses de extinção relevantes; art.40: previdência social federal + contagem recíproca de tempo em sistemas diversos | aposentadoria/invalidez e jurisprudência constitucional quando questão exigir | previdenciário profundo | H seletiva | H | M | A/B |
| CNN Justiça Aberta | função/dever de atualização | fiscalização/consequência | campos/relatórios | M/H | H future | M | B/C |
| CNN Solvência 227 | arquitetura declaração/fiscalização | prazo/exceções/risco/PAD | documentos integrais | H seletiva | H future | H | B/C |

## P1 MUST-KNOW v0.3
Além do core já preservado:
- **art.8/9**: livre escolha do tabelião de notas não autoriza prática de atos fora do Município da delegação;
- **art.12**: RI e RCPN estão sujeitos às normas de circunscrição geográfica;
- **art.36**: afastamento preventivo, interventor quando cabível, titular recebe metade da renda líquida e metade fica em conta especial durante a intervenção;
- **art.40**: vínculo à previdência social federal + contagem recíproca de tempo de serviço em sistemas diversos.

## P1 MUST-UNDERSTAND
- competência territorial básica é parte do Regime Geral, mas detalhes de cada especialidade têm casa própria;
- art.36 é cautelar/procedimental e não se confunde com a pena de suspensão do art.32;
- previdência do art.40 não significa sujeição automática dos delegatários ao regime constitucional de aposentadoria compulsória de servidor público.

## Novo contraste obrigatório
| A | B | Diferença |
|---|---|---|
| suspensão como sanção | afastamento preventivo/intervenção | pena disciplinar x medida cautelar de apuração |
| livre escolha do tabelião de notas | limite territorial de atuação do tabelião | escolha do usuário x competência territorial do agente |
| art.40 previdência federal | aposentadoria compulsória de servidor | vínculo previdenciário x natureza constitucional da delegação |

## P2 preservado
- Tema777 em aplicação;
- temporalidade art.22;
- Tema779;
- ADI1183;
- Prov219/220/227;
- publicidade x sigilo;
- responsabilidade tributária;
- proporcionalidade disciplinar;
- heatmap fino art.30.

## Podas mantidas
Não incluir no P1:
- todos os limites territoriais das especialidades;
- direito previdenciário completo;
- todos os efeitos patrimoniais de cada forma de extinção;
- PAD estadual minucioso;
- histórico completo de alterações legislativas.

## Gate para novo freeze
- specimen v0.2 deve incorporar exclusivamente patches H7 + correções anteriores;
- Q2/Q3/Q4 TJSC passam a BUILD evidence consumida e não podem validar v0.2;
- novo held-out deve ser selado antes de sua leitura;
- S2 continua NÃO atingido até reteste independente.

## Estado
**APROVADO PARA NOVO BUILD FREEZE INTERNO.**
Confiança do Regime Geral agora: A- no core nacional, ainda sem selo S2.

## Errata HOT — auditoria 12/09/2026

O rótulo de confiança acima era julgamento editorial, não medida empírica. A incorporação ao specimen v0.2 foi incompleta: o art.36 ainda não explicitava prazo cautelar/correção/destino; RG0B não ensinava atribuições específicas cobradas na Q20/TJES. O patch de trabalho atual é `material/specimens/REGIME_GERAL_AUDIT_PATCH_V0.3_2026-09-12.md`; IDs incorporados ao ledger RG. Estado: BUILD corrigido, não novo freeze validado. Referências Vunesp/SP do seed estão em quarentena de proveniência.
