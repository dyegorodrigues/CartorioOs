# GX Cartório OS — Proposition Ledger Seed
## N/R — Regime Jurídico Geral / Lei 8.935 + Constituição + STF

Snapshot: 2026-09-10
Status: SEED ENRIQUECIDO C0 + C1/C2 MULTIBANCA; ainda não é material de estudo

> Regra: este arquivo é base de decisão do Compiler. Não usar como superfície de estudo.

> **Errata HOT — 12/09/2026:** as atribuições históricas a “Vunesp/SP 13º” abaixo ficam em `PROVENANCE_PENDING / EXCLUDE_INCIDENCE`, inclusive no Signal Board. O registry RG identificou locator TJSP que era TJAL, e o locator substituto segue pendente. Sem pareamento questão/caderno/gabarito não promover essas menções como confirmação de TJSP, mesmo que a regra jurídica seja correta. A auditoria não reatribuiu automaticamente cada item ao TJAL.

## Fontes primárias-base
- Lei 8.935/1994 vigente: https://www.planalto.gov.br/ccivil_03/leis/l8935.htm
- CF/88, art. 236.
- STF Tema 779.
- STF Tema 777.
- ENAC 2025.1, 2025.2, 2026.1 — FGV, prova + gabarito oficiais.
- TJMS/TJRN/TJES — FGV, corpus contemporâneo objetivo/escrito/prático.
- TJRO/TJRR/TJBA — Cebraspe, corpus contemporâneo/histórico com REGIME_TAG.
- TJPA 2026 — IESES, prova Tipo 1 e gabarito oficial.
- TJSP 13º Concurso — Vunesp, prova oficial localizada; usar conteúdo como sinal de cobrança e só atribuir acerto quando gabarito oficial estiver pareado.

## Campos
Study = compreender/aprender; Memory = recuperação literal; Question = retorno de treino; Output = escrita/prática/oral sob regime válido.
L=low, M=medium, H=high, VH=very high.

## Ledger

| ID | Proposição examinável | Fonte atual | Evidência verificada | Forma cognitiva | Memory | Study | Question | Output | Estado |
|---|---|---|---|---|---|---|---|---|---|
| RG-NAT-001 | Serviços N/R constituem organização técnica e administrativa destinada a publicidade, autenticidade, segurança e eficácia dos atos jurídicos | L8935 art. 1 | escopo ENAC; recorrência indireta; contagem direta ainda pendente | definição/literalidade | M | H | M | M | BUILD |
| RG-NAT-002 | Notário/registrador são profissionais do Direito dotados de fé pública e exercem atividade delegada | L8935 art. 3 + CF 236 | IESES/PA 2026 Q2 cobra natureza constitucional; casos escritos usam estrutura | conceito estrutural | H | VH | H | H | MULTIBANK CORE |
| RG-COMP-011 | Tabelião de protesto protocola de imediato documento de dívida apresentado | L8935 art. 11 I | ENAC 2025.1 Q50 | competência/literalidade | H | M | H | L/M | C0 DIRECT |
| RG-ING-014 | Requisitos de ingresso; exceção dos não bacharéis com 10 anos de função; não existe requisito geral de 3 anos de atividade jurídica | L8935 arts. 14–15 | ENAC 2025.2 Q36; Vunesp/SP 13º Concurso Q1 explora exatamente requisitos e tempo do não bacharel | requisito + falso amigo de carreira | H | H | VH | M | CROSS-BANK DIRECT |
| RG-PRE-020A | Titular pode contratar escreventes, substitutos e auxiliares como empregados sob legislação trabalhista | L8935 art. 20 | Vunesp/SP Q2 cobra regime de contratação; casos Cebraspe BA envolvem prepostos/interinos | regra + sujeitos | H | H | VH | H | CROSS-BANK DIRECT |
| RG-PRE-020B | Substitutos podem praticar atos próprios simultaneamente com titular, exceto lavrar testamentos em notas | L8935 art. 20 §4 | Vunesp/SP Q2 contém distratores sobre atuação apenas na ausência; corpus adicional pendente | exceção literal | H | H | H | M | MULTIBANK SIGNAL |
| RG-GEST-021 | Gerenciamento administrativo e financeiro é responsabilidade exclusiva do titular, inclusive custeio, investimento, pessoal e atribuições/remuneração de prepostos | L8935 art. 21 | Vunesp/SP Q3 traz formulação literal como alternativa; cruzamento com Prov. 227/2026 | literal + gestão | H | H | H | H | C1 DIRECT SIGNAL |
| RG-RESP-022 | Delegatário responde civilmente por prejuízos decorrentes de culpa ou dolo, pessoalmente e por substitutos/escreventes autorizados, com regresso; prazo prescricional de 3 anos da lavratura | L8935 art. 22 | ENAC 2025.2 Q52; ENAC 2026.1 Q42; IESES/PA 2026 Q10, gabarito Tipo 1 = E; Vunesp/SP Q3 também explora prazo/regresso | responsabilidade + boundary | VH | VH | VH | H | C0 RECURRING + MULTIBANK |
| RG-RESP-023 | Responsabilidade civil independe da criminal; criminal é individualizada | L8935 arts. 23–24 | IESES/PA Q10 e Vunesp/SP Q3 usam dependência civil/criminal como distrator | contraste | H | H | H | M | MULTIBANK DISTRACTOR |
| RG-RESP-T777 | Estado responde objetivamente por danos causados no exercício da função, com regresso por dolo/culpa | STF Tema 777 | escrita FGV MS/RN/ES + Cebraspe BA | jurisprudência + sujeitos | H | VH | H | VH | CROSS-BANK OUTPUT |
| RG-INC-025 | Incompatibilidades com advocacia/cargo etc.; mandato eletivo e posse geram afastamento conforme regra legal | L8935 art. 25 | ENAC 2025.2 Q41 | regra composta | H | H | H | M/H | C0 DIRECT |
| RG-IMP-027 | Impedimento pessoal em ato próprio/cônjuge/parentes até 3º grau | L8935 art. 27 | ENAC 2025.2 Q41; ENAC 2026.1 Q53; FGV estadual | boundary 3º/4º + `pessoalmente` | VH | H | VH | L/M | RECURRING |
| RG-DIR-028 | Independência no exercício, emolumentos integrais e perda apenas nas hipóteses legais | L8935 art. 28 | ENAC 2025.1 Q39 contexto | regime | M | H | M | M | C0 CONTEXT |
| RG-DIR-029I | Direito de opção em desmembramento/desdobramento | L8935 art. 29 I | ENAC 2025.1 Q39 | direito x dever | H | M | H | L | C0 DIRECT |
| RG-DIR-029II | Direito de organizar associações OU sindicatos e participar | L8935 art. 29 II | ENAC 2026.1 Q51 | conectivo fatal | H | M | H | L | C0 DIRECT |
| RG-DEV-030V | Dignificar função nas atividades profissionais e na vida privada | L8935 art. 30 V | ENAC 2026.1 Q51 | extensão literal | H | M | H | M | C0 DIRECT |
| RG-DEV-030VI | Guardar sigilo sobre documentação e assuntos reservados conhecidos em razão da função | L8935 art. 30 VI | Cebraspe/BA histórico possui recurso oficial centrado na tensão sigilo/publicidade; revalidar uso contemporâneo | conflito conceitual | H | H | H | H | C2 OUTPUT SIGNAL |
| RG-DEV-030XI | Fiscalizar recolhimento dos impostos incidentes sobre atos praticados | L8935 art. 30 XI | Cebraspe/RO escrita integra responsabilidade tributária/fiscalização; presença em currículos atuais | integração tributária | H | H | H | H | CROSS-NODE |
| RG-DEV-030 | Demais deveres do art. 30 | L8935 art. 30 | ENAC 2025.1 Q39 usa deveres como distratores; heatmap por inciso em construção | lista semântica/role swap | H seletiva | H | H | H | NEEDS INCISO HEATMAP |
| RG-DISC-031 | Infrações disciplinares: inobservância normativa, conduta atentatória, cobrança indevida/excessiva, sigilo, descumprimento de deveres | L8935 art. 31 | cluster disciplinar ENAC + ponte Prov. 227/2026 art. 17 | classificação + integração | H | H | H | H | CORE/P2 |
| RG-PEN-032III | Suspensão = 90 dias, prorrogável por mais 30 | L8935 art. 32 III | ENAC 2025.2 Q53 | boundary numérico | VH | M | VH | M/H | C0 DIRECT |
| RG-PEN-033III | Suspensão em reiterado descumprimento dos deveres ou falta grave | L8935 art. 33 III | ENAC 2025.2 Q53 | gatilho→sanção | H | H | VH | H | C0 DIRECT |
| RG-LOSS-035 | Perda por sentença judicial transitada em julgado OU decisão administrativa competente, com ampla defesa | L8935 art. 35 | ENAC 2025.2 Q43; TJRN/FGV Disc.2 | falsa exclusividade + output | VH | H | VH | VH | C0+C1 OUTPUT |
| RG-CAUT-036 | Durante processo disciplinar, autoridade pode afastar preventivamente e designar interventor nos termos legais | L8935 art. 36 + atos CNJ supervenientes | Prov. 227/2026 reconecta cautelar ao risco trabalhista grave | procedimento/consequência | H | H | H | H | RECENTLY RECONTEXTUALIZED |
| RG-INT-T779 | Interinos não se equiparam a titulares concursados; agentes estatais sujeitos ao teto | STF Tema 779 | FGV/MS + Cebraspe/BA escrita | jurisprudência | H | VH | H | VH | CROSS-BANK OUTPUT |
| RG-INT-ADI1183 | Interinidade por vacância não pode perpetuar preposto não concursado >6 meses conforme STF/modulação | STF ADI 1183 | FGV/RN discursiva direta | jurisprudência + boundary temporal | H | VH | H | VH | C1 DIRECT OUTPUT |

## Incremento de auditoria — 12/09/2026

Subdivisões de RG0B/RG6, não nova arquitetura:

| ID | Fundamento | Cobertura/uso |
|---|---|---|
| RG-ATTR-AUTH-001 | Lei 8.935, arts.7º V e 11 III | TJES Remoção Q20/C: atribuição de autenticação/quitação; gap corrigido, item consumido |
| RG-DISC-PREV-001 | art.36 caput | prazo cautelar explicitado no patch; não derivar da sanção art.32 |
| RG-DISC-INTERVENTOR-002 | art.36 §1º | critério de conveniência para os serviços corrigido |
| RG-DISC-RENDA-003 | art.36 §§2º–3º | renda líquida/conta/correção/destino; Q22/B consumida |

Fonte legal conferida em 12/09; derivação em `material/specimens/REGIME_GERAL_AUDIT_PATCH_V0.3_2026-09-12.md`. Nenhum novo PASS independente. Os demais fundamentos do seed não foram recertificados.

## Direct Signal Board ampliado — qualificações Vunesp/SP suspensas pela errata acima

| Família | ENAC | IESES/PA 2026 | Vunesp/SP 13º | FGV/Cebraspe output | Sinal atual |
|---|---|---|---|---|---|
| ingresso arts.14–15 | direto | — | Q1 direto | — | HIGH/VH objective |
| prepostos/gestão arts.20–21 | indireto | — | Q2–Q3 direto | BA/RN integram regime | HIGH |
| responsabilidade arts.22–24 + Tema777 | recorrente | Q10 direto, gab. E | Q3 explora | MS/RN/ES/BA | VERY HIGH cross-phase |
| art.27 impedimento | recorrente | — | corpus adicional | FGV estadual | VERY HIGH memory/question |
| arts.29–30 | recorrente | — | prova contém direitos/deveres | output histórico/tributário | HIGH/VH |
| disciplina arts.31–36 | direto | — | corpus adicional | RN + atos CNJ | HIGH/VH |

## Grammar multibanca
FGV: boundary, role-swap, alternativa conjuntiva, falso amigo de outra carreira, conectivo/palavra fatal.
IESES/PA 2026: forte near-literalidade com alternativas que alteram apenas um elemento da regra; mistura Constituição, Lei 8.935 e CNN logo nas primeiras questões; evidencia valor de lei seca muito bem estruturada, mas não só decoreba.
Vunesp/SP: sequência sistemática artigo-a-artigo em Regime Geral, com alternativas próximas da literalidade e falsos limites temporais; exige domínio organizado do texto legal.
Cebraspe: composição I/II/III, casos operacionais e integração entre norma nacional, consequência e especialidade; não reduzir a certo/errado.

## Consequência pedagógica consolidada
P1 de Regime Geral deve ensinar a arquitetura inteira em ordem lógica e cobrir os boundaries baratos já comprovados. Não pode ser um resumo magro, porque IESES/Vunesp testam literalidade distribuída, enquanto FGV/Cebraspe exigem transferência e integração.

Mas P1 também não deve virar comentário enciclopédico artigo por artigo. Profundidade jurisprudencial, atos CNJ recentes e conflitos de responsabilidade entram em P2/OUTPUT conforme evidência.

## Estado de suficiência
Ainda S1 em construção. Multibanca melhorou, mas falta:
- heatmap exaustivo por inciso art.30;
- mais Vunesp/Consulplan;
- reservar held-out antes de material learner-facing;
- snapshot pós-696 futuro para confirmar novas tendências.
