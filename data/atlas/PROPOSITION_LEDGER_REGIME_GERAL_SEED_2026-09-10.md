# GX Cartório OS — Proposition Ledger Seed
## N/R — Regime Jurídico Geral / Lei 8.935 + Constituição + STF

Snapshot: 2026-09-10
Status: SEED ENRIQUECIDO COM C0 ENAC + C1 CROSS-PHASE; ainda expandir corpus estadual/histórico

> Regra: este arquivo não é material de estudo. É a base de decisão do Compiler.

## Fontes primárias-base
- Lei 8.935/1994 vigente: https://www.planalto.gov.br/ccivil_03/leis/l8935.htm
- CF/88, art. 236.
- STF Tema 779: https://portal.stf.jus.br/jurisprudenciaRepercussao/tema.asp?num=779
- STF Tema 777: https://portal.stf.jus.br/jurisprudenciarepercussao/tema.asp?num=777
- ENAC 2025.1, 2025.2, 2026.1: prova Tipo 1 + gabarito definitivo FGV.
- TJMS/FGV 2026: objetiva + escrita/prática + espelho.
- TJRN/FGV 2026: escrita/prática.
- TJES/FGV 2025/2026: escrita/prática + espelho.
- TJBA/Cebraspe 2026: escrita/prática, com REGIME TAG pré-696 para validade de fase.

## Campos de prioridade
- `Study`: importância de aprender/compreender.
- `Memory`: necessidade de recuperação literal/precisa.
- `Question`: retorno de treino por questão.
- `Output`: importância de produção escrita/prática/oral sob regime atual e corpus válido.

L=low, M=medium, H=high, VH=very high, TBD=aguardar corpus.

## Ledger

| ID | Proposição examinável | Fonte atual | Evidência C0/C1 já verificada | Forma cognitiva | Memory | Study | Question | Output | Estado |
|---|---|---|---|---|---|---|---|---|---|
| RG-NAT-001 | Serviços notariais/registro são organização técnica e administrativa destinada a publicidade, autenticidade, segurança e eficácia dos atos jurídicos | L8935 art. 1 | escopo ENAC; contagem direta específica ainda pendente | definição/literalidade | M | H | M | M | BUILD CANDIDATE |
| RG-NAT-002 | Notário/tabelião e registrador são profissionais do Direito dotados de fé pública, com exercício delegado | L8935 art. 3 + CF 236 | transversal em casos escritos; frequência direta ainda pendente | conceito estrutural | H | H | H | H | CORE CANDIDATE |
| RG-COMP-011 | Tabelião de protesto deve protocolar de imediato documentos de dívida para prova do descumprimento | L8935 art. 11 I | ENAC 2025.1 Q50, gab. C | competência/literalidade | H | M | H | L/M | C0 DIRECT |
| RG-ING-014 | Ingresso exige concurso, nacionalidade brasileira, capacidade civil, quitações, bacharelado em Direito e conduta condigna; não existe requisito geral de 3 anos de atividade jurídica | L8935 art. 14 + art. 15 §2 | ENAC 2025.2 Q36, gab. C | requisito + anti-transferência de outra carreira | H | H | H | M | C0 DIRECT |
| RG-PRE-020A | Titular pode contratar escreventes, substitutos e auxiliares como empregados sob legislação trabalhista; gestão/prepostos obedecem estrutura legal | L8935 art. 20 | TJBA/Cebraspe discursiva aborda contratação/interinos; regime de fase deve ser lido com tag | regra + contraste titular/interino | M | H | H | H | P1/P2 |
| RG-PRE-020B | Substitutos podem praticar atos próprios simultaneamente com titular, exceto lavrar testamentos em tabelionato de notas | L8935 art. 20 §4 | corpus objetivo específico ainda a ampliar | exceção literal | H | M | H | M | MEMORY CANDIDATE |
| RG-RESP-022 | Notários/registradores respondem civilmente por prejuízos que causarem por culpa/dolo, pessoalmente ou por substitutos/escreventes, com regresso; pretensão prescreve em 3 anos da lavratura | L8935 art. 22 | ENAC 2025.2 Q52 gab. D; ENAC 2026.1 Q42 gab. D | responsabilidade + regresso + boundary de prazo | VH | VH | VH | H | C0 RECURRING |
| RG-RESP-T777 | Estado responde objetivamente por danos causados por tabeliães/registradores no exercício das funções, com dever de regresso em dolo/culpa | STF Tema 777, RE 842846 | TJMS/FGV escrita; TJRN/FGV Discursiva 2; TJES/FGV Q3; TJBA/Cebraspe discursiva em contexto de interino | tese vinculante + aplicação processual | H | VH | H | VH | CROSS-EXAM OUTPUT |
| RG-INC-025 | Advocacia/cargo público etc. são incompatíveis com atividade; diplomação em mandato eletivo e posse nos demais casos implicam afastamento | L8935 art. 25 | ENAC 2025.2 Q41, gab. D | regra composta + incompatibilidade | H | H | H | M/H | C0 DIRECT |
| RG-IMP-027 | Titular não pode praticar pessoalmente ato de interesse próprio, do cônjuge ou de parentes em linha reta/colateral, consanguíneos ou afins, até 3º grau | L8935 art. 27 | ENAC 2025.2 Q41: 4º grau fora; ENAC 2026.1 Q53: 3º grau dentro; TJMS/FGV 2026 Q4 também explora fronteira | boundary pair + palavra fatal `pessoalmente` / `3º grau` | VH | H | VH | L/M | C0 RECURRING + C1 |
| RG-DIR-028 | Titular goza de independência, recebe emolumentos integrais e só perde delegação nas hipóteses legais | L8935 art. 28 | pano de fundo explícito ENAC 2025.1 Q39 | estrutura de regime | M | H | M | M | C0 CONTEXT |
| RG-DIR-029I | Direito de exercer opção nos casos de desmembramento/desdobramento da serventia | L8935 art. 29 I | ENAC 2025.1 Q39, gab. B | classificação direito x dever | H | M | H | L | C0 DIRECT |
| RG-DIR-029II | Direito de organizar associações OU sindicatos de classe e deles participar | L8935 art. 29 II | ENAC 2026.1 Q51, gab. E | near-literal + `ou` | H | M | H | L | C0 DIRECT |
| RG-DEV-030V | Dever de proceder de forma a dignificar a função tanto nas atividades profissionais COMO na vida privada | L8935 art. 30 V | ENAC 2026.1 Q51, gab. E | near-literal + extensão da regra | H | M | H | M | C0 DIRECT |
| RG-DEV-030 | Demais deveres incluem livros/documentos, eficiência, sigilo, tabela/emolumentos, prazos, fiscalização tributária, acesso documental, dúvidas, normas técnicas e meios eletrônicos | L8935 art. 30 | ENAC 2025.1 Q39 usa vários deveres como distratores; TJRO/Cebraspe Q1 explora fiscalização tributária no plano escrito | lista semântica + role swap + integração tributária | TBD/H | H | H | H | NEEDS HEATMAP |
| RG-DISC-031 | Infrações disciplinares incluem inobservância normativa, conduta atentatória, cobrança indevida/excessiva, violação de sigilo e descumprimento dos deveres | L8935 art. 31 | regime disciplinar C0 aparece diretamente em questões de sanção; inciso-a-inciso a contar | classificação | TBD/H | H | H | H | NEEDS HEATMAP |
| RG-PEN-032III | Suspensão é de 90 dias, prorrogável por mais 30 | L8935 art. 32 III | ENAC 2025.2 Q53, gab. C | boundary numérico | VH | M | VH | M/H | C0 DIRECT |
| RG-PEN-033III | Suspensão aplica-se em reiterado descumprimento dos deveres ou falta grave | L8935 art. 33 III | ENAC 2025.2 Q53, gab. C | gatilho → sanção | H | H | VH | H | C0 DIRECT |
| RG-LOSS-035 | Perda da delegação depende de sentença judicial transitada em julgado OU decisão em processo administrativo pelo juízo competente, assegurada ampla defesa | L8935 art. 35 | ENAC 2025.2 Q43 gab. B; TJRN/FGV Discursiva 2 cobra aplicação ao caso | falsa exclusividade + competência/aplicação | VH | H | VH | VH | C0 + C1 OUTPUT |
| RG-INT-T779 | Substitutos/interinos de serventia vaga não se equiparam a titulares concursados; são agentes estatais e submetem-se ao teto do art. 37 XI | STF Tema 779, RE 808202 | TJBA/Cebraspe discursiva Q1 + TJMS/FGV discursiva Q1 | jurisprudência + distinção de regime | H | VH | H | VH | CROSS-BANK OUTPUT |
| RG-INT-ADI1183 | Interinidade decorrente de vacância não pode resultar em substituição ininterrupta por preposto não concursado por mais de 6 meses, conforme decisão/modulação STF | STF ADI 1183 | TJRN/FGV Discursiva 2 pergunta diretamente >6 meses e solução constitucional; BA tangencia seleção/controle | jurisprudência avançada + boundary temporal | H | VH | H | VH | C1 DIRECT OUTPUT |

## C0 Direct Signal Board — primeira contagem
Esta contagem é por questões já classificadas, não por menção textual automática completa.

| Família | ENAC 2025.1 | ENAC 2025.2 | ENAC 2026.1 | Sinal |
|---|---:|---:|---:|---|
| Direitos/deveres arts. 29–30 | Q39 | — | Q51 | recorrência interedição |
| Responsabilidade art. 22 | — | Q52 | Q42 | recorrência consecutiva |
| Impedimento art. 27 | — | Q41 | Q53 | recorrência consecutiva + C1 FGV estadual |
| Disciplina arts. 31–35 | — | Q43, Q53 | — | cluster forte em 2025.2 |
| Ingresso art. 14 | — | Q36 | — | cobrança direta |
| Competência protesto art. 11 | Q50 | — | — | cobrança direta |

Não inferir que ausência nesta tabela = tema não cobrado. Próxima passagem incorpora CNN/CNJ, CF 236 e questões que examinam o mesmo regime sem citar L8935.

## Cross-Phase Signal Board — C1 contemporâneo
| Família | FGV/MS | FGV/RN | FGV/ES | Cebraspe/BA | Cebraspe/RO | Consequência |
|---|---|---|---|---|---|---|
| Responsabilidade Estado/delegatário | escrita | Disc.2 | Q3 | discursiva | Q1 tributária distingue responsabilidade civil | P2/OUTPUT alto |
| Perda/delegação/regime disciplinar | — | Disc.2 | — | — | — | art.35: objetiva + escrita |
| Interinidade/preposto | escrita | Disc.2 | — | discursiva | — | jurisprudência obrigatória de alto valor |
| Dever de fiscalização tributária | objetiva/Lei 8935 em corpus geral | — | — | — | Q1 | conectar art.30 XI + CTN/LRP/STF |

Este quadro mede presença na amostra, não frequência histórica.

## Padrões de distrator já comprovados
### Boundary
- 3º x 4º grau;
- 3 x 5 anos;
- 90 + 30.

### Role swap
Direito do art. 29 misturado com deveres do art. 30.

### Conjunctive alternative
ENAC 2025.2 Q41 exige acertar simultaneamente mandato eletivo + advocacia + parentesco.

### Borrowed requirement
ENAC 2025.2 Q36 explora a falsa intuição de `3 anos de atividade jurídica`, típica de outras carreiras.

### Near-literal fatal connective
- associações **ou** sindicatos;
- atividade profissional **e** vida privada;
- perda judicial **ou** administrativa.

## Consequência pedagógica
### Cluster art. 27
Formato indicado:
- lei seca destacada;
- diagrama de graus mínimo;
- contrast pair `tio 3º proibido ↔ primo 4º fora`;
- assessment espaçado;
- não precisa longa dissertação para aprender a regra.

### Cluster art. 22 + Tema 777
Formato indicado:
- mapa `delegatário → culpa/dolo → ato próprio/preposto → regresso → 3 anos`;
- contraste explícito com responsabilidade objetiva do Estado;
- objetiva primeiro; depois cases e OUTPUT atoms, pois o cluster reaparece em escrita de várias seleções.

### Cluster arts. 29–30
Não usar tabela gigante para decorar plana. Organizar:
1. direitos (poucos);
2. deveres por função semântica;
3. palavras fatais;
4. itens recorrentes;
5. Q→A + role-swap questions;
6. satélites como responsabilidade tributária somente quando o subtema exigir.

### Regime disciplinar/interinidade
Ensinar como grafo:
`status do agente → competência/limite → conduta → sanção/perda → procedimento → substituição/interinidade → teto/controle`.

## Próxima expansão
1. C0: CF 236 + CNN/CNJ que pertencem a Regime Geral.
2. C1/C2: heatmap arts. 20–36 por banca e Estado.
3. CNN/CNJ + LRP proposition ledgers.
4. Vincular cada questão a `BUILD/VALIDATION/HELD-OUT/CHALLENGE` antes de gerar material.
5. Emitir primeiro Depth Budget formal somente após essa expansão.