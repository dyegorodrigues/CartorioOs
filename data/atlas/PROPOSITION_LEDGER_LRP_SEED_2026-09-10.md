# GX Cartório OS — Proposition Ledger Seed
## Lei 6.015/1973 / Registro de Imóveis e interfaces CNN

Snapshot: 2026-09-10
Status: SEED MULTIBANCA; NÃO é material de estudo.

## Objetivo
Abrir o primeiro ledger da LRP com proposições demonstradas em ENAC e concursos estaduais recentes, preservando separação entre lei-base, especialidade, jurisprudência e deltas CNN/CNJ de 2026.

## Fontes desta semente
- Lei 6.015/1973 vigente — Planalto.
- Provimento CNJ 149/2023 compilado + modificadores de 2026.
- ENAC 2025.1, 2025.2, 2026.1 — FGV.
- TJRO 2025 — Cebraspe, objetiva oficial.
- TJRR 2025 — Cebraspe, objetiva oficial.
- TJPA 2026 — IESES, objetiva/gabarito oficiais.
- corpus escrito/prático FGV/Cebraspe já catalogado no Atlas.

## Ledger inicial

| ID | Proposição/família examinável | Fonte-base | Evidência observada | Cognitive form | Study | Memory | Question | Output | Freshness |
|---|---|---|---|---|---|---|---|---|---|
| LRP-RI-PRENOT-001 | Prenotação estabelece prioridade e produz efeitos próprios; duração/prazos dependem do regime vigente | LRP arts. 182 e ss. + Lei 14.382/CNN | ENAC 2025.1 Q13 toca prorrogação na usucapião; oral histórico TJSC 2022 cobra prazo/efeitos; ENAC 2026.1 Q35 usa prioridade diante de indisponibilidade superveniente | caso + boundary temporal | VH | H | VH | VH | HIGH |
| LRP-RI-QUAL-002 | Registrador realiza qualificação do título e pode registrar, formular exigência/nota devolutiva ou adotar procedimento específico | LRP + CNN | Cebraspe/TJRO 2025 Q6 e prova prática RO; ENAC 2026.1 incorpora qualificação em casos complexos | application/procedure | VH | M/H | VH | VH | MED/HIGH |
| LRP-RI-HIP-003 | Segunda hipoteca com referência à anterior não inscrita obedece regime específico de prenotação/precedência | LRP regra específica | Cebraspe/TJRO 2025 Q6 | literal-procedural trap | H | H | H | M | MED |
| LRP-RI-USUC-004 | Usucapião extrajudicial exige requerimento e documentação legal, inclusive ata notarial; prenotação/procedimento têm regras próprias | LRP art. 216-A + CNN | ENAC 2025.1 Q13; ENAC 2025.2 Q5; IESES/PA 2026 Q8; FGV/Cebraspe escritos usam usucapião/qualificação | recurring case/procedure | VH | H | VH | VH | HIGH |
| LRP-RI-USUC-IMP | Impugnação na usucapião extrajudicial não conduz automaticamente ao mesmo resultado em toda hipótese; registrador precisa qualificar a impugnação conforme regime vigente | LRP/CNN | ENAC 2026.1 questão de impugnação e tentativa consensual frustrada | case distinction | VH | M | VH | H | HIGH |
| LRP-RI-INDISP-005 | Indisponibilidade deve ser tratada em conjunto com prenotação/prioridade e regras da CNIB | LRP + CNN CNIB | ENAC 2026.1 Q35; Prov. 217/2026 e Prov. 224/2026 alteram ecossistema | integrated current case | VH | H | VH | VH | VERY HIGH / RECENT |
| LRP-RI-RETIF-006 | Retificação registral corrige assento/descrição e possui limites; não é via autônoma de aquisição patrimonial | LRP art. 213 e jurisprudência STJ | Cebraspe/TJRO 2025 Q59 | jurisprudence + false purpose | H | M/H | H | H | MED |
| LRP-RTD-IDIOMA-007 | Documento estrangeiro pode ingressar no RTD para conservação em hipóteses específicas, distinguindo conservação de eficácia perante terceiros | LRP RTD | ENAC 2026.1 questão sobre documento em idioma estrangeiro sem tradução | exception/functional distinction | H | H | H | M | MED |
| LRP-RTD-ATTR-008 | Atribuições de RTD devem ser distinguidas de RI e outros registros | LRP arts. RTD | Cebraspe/TJRR 2025 Q21 | role/competence swap | H | H | H | M | MED |
| LRP-RI-ELETR-009 | Apresentação eletrônica de título e protocolo operam via sistema nacional, com regras de recepção/prenotação | Lei 14.382 + LRP + CNN/SERP | ENAC 2025.2 Q24; Prov. 228/229 de 2026 ampliam arquitetura | system/procedure | VH | M/H | VH | H | VERY HIGH |
| LRP-RI-GARAGEM-010 | Regime registral de vagas de garagem depende de sua natureza jurídica/individualização e do desenho condominial | CC/LRP/incorporação | ENAC 2026.1 Q33 | integrated civil+registry case | H | L/M | H | H | MED |
| LRP-RI-EXTRATO-011 | Extrato eletrônico passa a ter disciplina nacional detalhada para apresentação e qualificação no RI | CNN arts. 210-A a 210-Q / Prov.228/2026 | mudança normativa recente; corpus pós-mudança ainda não existe | new system/procedure | H/VH | TBD | H future | H | VERY HIGH / NEW |
| LRP-RI-CONSTR-012 | Ordens de constrição imobiliária passam por ecossistema Constrijud/Serp-Jud, com disciplina nacional de protocolo/qualificação/cumprimento | CNN art. 320-X+ / Prov.224/2026 | mudança 2026; conexão direta com casos de indisponibilidade e ordens judiciais | system + judicial integration | H/VH | TBD | H future | VH | VERY HIGH / NEW |
| LRP-RI-AFID-013 | Alienação fiduciária e forma/título registrável precisam ser lidas no regime material e nas atualizações CNN/STF/STJ | Lei 9.514 + CNN art. 440-AO/Prov.246 | escrita FGV/RN integra alienação fiduciária; mudança CNN 2026 | cross-source case | VH | M | H | VH | VERY HIGH |

## Padrões já demonstrados

### 1. FGV ENAC está longe de mera literalidade
No RI, a FGV já combina:
- prenotação + indisponibilidade;
- incorporação + natureza da vaga;
- usucapião + processamento de impugnação;
- sistemas eletrônicos + protocolo.

P1 precisa dar mapa e literalidade decisiva, mas sem capacidade de aplicar a regra em caso o candidato não sobrevive ao corpus recente.

### 2. Cebraspe explora procedimento e finalidade
TJRO/TJRR recentes mostram:
- qualificação e providência do registrador;
- finalidade da retificação;
- atribuições de RTD;
- composição de alternativas com mais de uma assertiva.

### 3. IESES pode cobrar estrutura nacional de forma quase literal
TJPA 2026 abre a prova com Constituição, Lei 9.492, Prov.149, ata notarial, usucapião e responsabilidade. Isso reforça uma base de lei/norma visualmente forte, sem concluir que o exame inteiro é decoreba.

## One-Home Rule proposta
`LRP` é o lar principal de:
- escrituração/publicidade/atribuições legais dos registros;
- RI: matrícula, títulos, prenotação, qualificação, dúvida, retificação, usucapião e atos registráveis;
- RTD/PJ/RCPN quando o núcleo for regra registral da LRP.

`CNN` fica como overlay operacional/nacional e não deve duplicar a teoria-base da LRP.
`Civil` contém negócio/direito material que o caso aplica.
`Processual` entra apenas quando indispensável para efeitos/processos.

## Depth implication preliminar
- Prenotação/qualificação/usucapião/indisponibilidade = P1 forte e P2 robusto.
- Sistemas eletrônicos atuais = P1 arquitetura + P2 procedimentos relevantes; alta necessidade de freshness.
- Questões raras/específicas (ex. segunda hipoteca) podem entrar como P2/Question-first, salvo aumento de recorrência.
- Normas 2026 sem histórico recebem `RECENCY BONUS`, não promoção automática a memorização total.

## Próxima expansão
1. indexar todas as questões de LRP nas 300 questões ENAC já catalogadas;
2. separar RI/RCPN/RTD/PJ por subledgers quando densidade justificar;
3. cruzar Vunesp/IESES/Consulplan estaduais;
4. marcar questões BUILD vs HELD-OUT antes do primeiro material N/R;
5. criar Depth Budget específico do primeiro módulo após triangulação.