# GX Cartório OS — Depth Budget v0.2
## N/R — Regime Jurídico Geral

Snapshot: 2026-09-11
Status: pós-CHALLENGE; pronto para BUILD freeze interno. NÃO estudar ainda.

## Mudança em relação à v0.1
A v0.1 sobreviveu ao red-team, mas recebeu três patches estruturais:
1. responsabilidade agora tem eixo temporal pré/pós Lei 13.286/2016;
2. civil, penal e disciplinar foram explicitamente separados;
3. proporcionalidade disciplinar e responsabilidade por supervisão de prepostos entram em P2/output.

## Arquitetura
`RG0 natureza/delegação → RG1 ingresso → RG2 gestão/prepostos → RG3 responsabilidade → RG4 incompatibilidades/impedimentos → RG5 independência/direitos/deveres → RG6 disciplina/perda/extinção → RG7 vacância/interinidade + CNN`

## Budget por cluster

| Cluster | P1 | P2 | P3+ | Memory | Questions | Output | Conf. |
|---|---|---|---|---|---|---|---|
| RG0 Natureza/CF236 | caráter privado por delegação; serviço público delegado; profissional do Direito/fé pública; fiscalização; serventia não é sujeito autônomo separado do delegatário | legitimidade processual e conexões constitucionais | doutrina histórica/teorias só se corpus exigir | H | H | H | A |
| RG1 Ingresso arts.14–19 | requisitos; bacharel x 10 anos; provimento/remoção; falso amigo `3 anos atividade jurídica` | regras procedimentais recorrentes/Res696 | detalhes locais/edital | VH | VH | M | A |
| RG2 Gestão/prepostos arts.20–21 | categorias de prepostos; vínculo trabalhista; substitutos; gestão do titular | limites de atuação; testamento; supervisão; interinidade | minúcias laborais/local | H | H/VH | H | A/B |
| RG3 Responsabilidade arts.22–24 + Tema777 | sujeitos; culpa/dolo atual; prepostos; regresso; prazo 3 anos; Estado x delegatário; civil x criminal | **eixo temporal pré/pós Lei 13.286/2016**; Tema777; legitimidade; caso antigo; responsabilidade disciplinar não se confunde com civil | conflitos jurisprudenciais raros e processuais | VH | VH | VH | A |
| RG4 Incompatibilidades/impedimentos arts.25–27 | incompatibilidades; afastamento; `pessoalmente`; parentes até 3º; 3º x 4º | casos compostos/mandato/função pública | residual | VH | VH | M | A |
| RG5 Independência/direitos/deveres arts.28–30 | independência; direitos; deveres agrupados; sigilo, eficiência, emolumentos, tributos, normas técnicas | heatmap por inciso; publicidade x sigilo; deveres digitais/CNJ | residual/local | H seletiva | VH | H | A/B |
| RG6 Disciplina arts.31–36 + art.39 | grafo infração→pena→procedimento; suspensão 90+30; perda judicial OU administrativa; ampla defesa | **proporcionalidade disciplinar**; culpa in eligendo/in vigilando; gradação da sanção; TAC/medidas quando legalmente cabíveis; afastamento/interventor; Prov227 | PAD local/controverso | VH | VH | VH | A/B |
| RG7 Vacância/interinidade | titular x interino; continuidade; teto Tema779; mapa de vacância | Prov219; ADI1183/>6m; Prov220; seleção/efeitos | campos/anexos operacionais | H | H | VH | A/B |
| CNN Justiça Aberta | função + dever de atualização | fiscalização/consequência | campos/relatórios | M/H | H future | M | B/C |
| CNN Solvência 227 | arquitetura declaração/fiscalização/ponte arts.20/31/36 | prazo, exceções, risco/PAD/interventor | documentos/bens integrais | H seletiva | H future | H | B/C |

## P1 MUST-KNOW
- art.14/15: requisitos e 10 anos do não bacharel;
- art.20: titular/substituto/escrevente/auxiliar;
- art.22 atual: culpa ou dolo, prepostos, regresso, 3 anos;
- art.25: incompatibilidades/afastamento;
- art.27: pessoalmente + cônjuge/parentes até 3º grau;
- arts.29–30: DIREITO x DEVER;
- art.32 III: 90 + 30;
- art.35: judicial OU administrativa + ampla defesa.

## P1 MUST-UNDERSTAND
- `atividade pública delegada` não significa órgão estatal comum;
- serventia não possui personalidade jurídica autônoma para ser tratada como sujeito independente do delegatário;
- titular ≠ substituto ≠ escrevente ≠ interino;
- responsabilidade civil do delegatário ≠ objetiva do Estado ≠ penal ≠ disciplinar;
- direito/dever/infração/sanção formam cadeia;
- CNN é overlay operacional e regulatório, não substitui Lei 8.935/CF.

## P2 — responsabilidade temporal
Regra de decisão:
`DATA DO ATO DANOSO → REDAÇÃO VIGENTE DO ART.22 → REGIME DO DELEGATÁRIO → ESTADO/TEMA777 → NEXO/REGRESSO`.

O candidato não precisa decorar catálogo jurisprudencial, mas precisa reconhecer que fatos anteriores à Lei 13.286/2016 podem exigir regime diferente do texto atual.

## P2 — matriz dos três planos

| Plano | Pergunta | Base mental |
|---|---|---|
| Civil | quem indeniza e em qual regime? | art.22 + temporalidade + Tema777 |
| Penal | quem responde pelo ilícito penal? | individualização art.24 |
| Disciplinar | há infração funcional e qual resposta? | arts.31–36 + culpa/supervisão + proporcionalidade |

## P2 — sanction reasoning
Para output/oral:
`CONDUTA → DEVER VIOLADO → GRAVIDADE → CULPA/SUPERVISÃO → MEDIDA CABÍVEL → PROPORCIONALIDADE → SANÇÃO`.

Não ensinar apenas tabela de penas.

## P3+/REFERENCE
Continuam fora da primeira passagem:
- história doutrinária longa;
- todos os precedentes de responsabilidade;
- minúcia estadual de PAD sem edital;
- anexos/campos integrais de atos CNJ;
- controvérsias acadêmicas sem efeito de prova.

## Surfaces
### MAP
RG0–RG7 + três planos de responsabilidade.

### MASTER P1
Compacto, mas autossuficiente para primeira passagem.

### LAW STRIP
Texto integral dos artigos curtos + destaque de palavras fatais.

### Q→A
Recuperação de P1 + contrastes entre planos.

### OBJECTIVE LAB
FGV boundaries, Cebraspe composição/procedimento, IESES literalidade, Vunesp sistemática, sem usar held-out selado.

### OUTPUT LAB
Prioridade:
- responsabilidade Estado/delegatário;
- temporalidade;
- disciplina/proporcionalidade;
- perda da delegação;
- interinidade/vacância.

Formato:
`atoms → outline → microanswer → resposta completa`.

## Freeze Gate
Esta v0.2 pode alimentar o primeiro BUILD freeze quando:
- corpus BUILD for explicitamente fechado;
- nenhuma questão H1/H2/H4 for aberta;
- Freshness CNN for aplicada ao snapshot;
- draft learner-facing carregar IDs das proposições.

## Estado
**APROVADO PARA BUILD FREEZE INTERNO.**
Ainda NÃO é autorização para estudo nem selo de suficiência.
