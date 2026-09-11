# GX Cartório OS — Estado Atual

Atualizado em 10/09/2026.

## Branch / handoff HOT
- branch: `chatgpt/gx-cartorio-v0.1`
- ler primeiro: `handoff/NEXT_SESSION_POINTER_2026-09-10.md`

## Missão canônica
Levar candidato com conhecimento jurídico enferrujado/próximo de zero até **prontidão verificável para ENAC + concurso estadual + discursiva + peça prática + oral**, horizonte 2027–2028, com eficiência extrema e administração manual mínima.

Objetivo é desempenho de teto por evidência, não volume ornamental nem promessa de IA.

## Constraint autoral HOT
**NÃO INICIAR ESTUDO AINDA.**

O usuário quer primeiro provar a máquina e o material. Não entregar Missão 01, não atribuir mastery e não exigir auditoria jurídica dele.

## Work Order A — CONCLUÍDO / CONGELADO
`material/EDITORIAL_STANDARD.md` = Editorial Standard v1.0.

Preservar:
- mastery M0–M7 + retention separado;
- objetiva permanente;
- oral/discursiva/prática progressivas e apenas onde a fase vigente permite;
- voz cedo como recall;
- lei seca guiada;
- Q→A e flashcards seletivos;
- revisão cumulativa;
- throughput adaptativo;
- One-Home Rule;
- Sufficiency Gate;
- Freshness Firewall.

Não reabrir arquitetura por estética; somente por falha observável.

## Baseline regulatório — Resolução CNJ 696/2026
Fonte oficial vigente: https://atos.cnj.jus.br/atos/detalhar/7011

- objetiva estadual: eliminatória, sem peso final, substituível por ENAC nos termos da Resolução;
- discursiva: 70%;
- oral: 25%;
- títulos: 5%;
- Penal, Processo Penal, Trabalho e Processo do Trabalho: exclusivamente ENAC/objetiva;
- nova matriz prioriza conteúdo nacional/uniforme e atividade N/R;
- oral sob novo regime: 90% conteúdo jurídico + 10% articulação técnica; pergunta escrita, pontos/perguntas predefinidos e reperguntas guiadas.

### Regra crítica de historicidade
Toda prova recebe `REGIME_TAG` + duas validades:
- `CONTENT_VALIDITY`;
- `PHASE_VALIDITY`.

Ex.: Penal em discursiva de edital pré-696 continua útil como forma/conteúdo histórico, mas NÃO eleva OUTPUT penal no baseline atual.

## Compiler invisível
`OFFICIAL SCOPE → SOURCES → EXAM CORPUS → PROPOSITIONS → INCIDENCE/CONSEQUENCE → DEPTH BUDGET → CANONICAL TREE → BUILD/VALIDATION/CHALLENGE → FRESHNESS → PATCH`

Learner-facing futuro:
`MAP → MASTER P1 → LEI SECA GUIADA → REVIEW → Q→A/RECALL → OBJECTIVE LAB → OUTPUT LAB quando pertinente`

## Suficiência
Nunca dizer `resolve qualquer questão futura`.

S0 untested → S1 build → S2 held-out → S3 challenge/multibanca → S4 learner-demonstrated → S5 maintenance-stable.

Pergunta operacional: **há questão legítima dentro do escopo/nível cuja solução dependa de proposição que o material não ensinou?** Se sim, material falhou primeiro.

## Estratégia de cobertura
- P1: mapa mental + core + sobrevivência objetiva;
- P2: exam depth por corpus, exceções, jurisprudência, aliases, integração;
- P3+: robustez, manutenção e OUTPUT.

Não levar o primeiro nó a M7 antes de cobrir o currículo.

## Specimens
### Specimen A — Penal / Aplicação da Lei Penal
v0.2 no Notion foi melhora clara segundo o usuário, mas fica **CONGELADO COMO PROTÓTIPO**. Não estudar, não ampliar por ansiedade.

### Specimen B
ADIADO. Não produzir antes de o Atlas entregar depth budget robusto.

## Materiais legados do usuário
Estratégia/DD e novos PDFs (trilhas, CC, LINDB, CP comentado) = **benchmark não canônico**.
Usar para UX, aliases, possíveis lacunas e organização. Nunca transplantar incidência de Delegado para Cartório.

Achado: trilha Estratégia pode ser coerente conceitualmente, mas foi desenhada para 28h/semana, 756 tarefas e 18/semana. O GX deve adaptar a trilha ao candidato, não o contrário.

## Deep Audit de mercado
Arquivo: `research/CARTORIO_PREP_ECOSYSTEM_DEEP_AUDIT_2026_09_10.md`

Auditados: VFK, Estratégia Cartórios, Registrando/CP Iuris, Themas, Decorando Lei Seca, PreparaEnac, YK, Juspodivm.

Absorver funções, não produtos:
- reservatório profundo sem fila linear;
- mapeamento/incidência;
- lei esquematizada;
- question engine com fundamento;
- rotina real/adaptação;
- atualização;
- treino de todas as fases.

## Cartório Exam Atlas — HOT
Protocolo: `research/CARTORIO_EXAM_ATLAS_PROTOCOL_2026.md`

### Wave 1 — censo contemporâneo
`research/CARTORIO_EXAM_ATLAS_WAVE1_CURRENT_CENSUS_2026-09-10.md`

Onda selecionada 2024–2026:
- Cebraspe: BA, MT, RO, RR, CE;
- FGV: MS, RN, ES, RS;
- Consulplan: PB, MG;
- IESES: PA;
- Vunesp: SP.

Não tratar essa contagem como ranking histórico.

### Wave 2 — TJMS/FGV = GOLD_CORPUS_001
`research/CARTORIO_EXAM_ATLAS_WAVE2_TJMS_FGV_2026_CROSS_PHASE.md`

Mesmo concurso fornece objetiva + escrita/prática + espelho. Confirmado que OUTPUT é integrado e decomponível em átomos jurídicos. Criado conceito `Integrated Case Graph`.

### Wave 3 — TJBA/Cebraspe
`research/CARTORIO_EXAM_ATLAS_WAVE3_TJBA_CEBRASPE_2026_TRANSITION.md`

Confirmado risco de transição regulatória e necessidade de `REGIME_TAG`.

### Wave 4 — ENAC / Lei 8.935 first pass
`research/CARTORIO_EXAM_ATLAS_WAVE4_ENAC_LEI8935_FIRST_PASS.md`

Evidência C0 direta já mostra recorrências:
- art. 22 responsabilidade: ENAC 2025.2 + 2026.1;
- arts. 29–30 direitos/deveres: 2025.1 + 2026.1;
- art. 27 impedimento: 2025.2 + 2026.1, além de TJMS/FGV;
- regime disciplinar arts. 31–35: bloco relevante no 2025.2;
- ingresso art. 14 e competência protesto art. 11 também cobrados.

Padrões FGV emergentes a continuar testando: boundary, role-swap, alternativa conjuntiva, requisito importado de outra carreira, palavra/conectivo fatal.

### Wave 5 — OUTPUT FGV x Cebraspe
`research/CARTORIO_EXAM_ATLAS_WAVE5_OUTPUT_TRIANGULATION_FGV_CEBRASPE_2026.md`

Triangulação:
- FGV: TJMS + TJRN + TJES;
- Cebraspe: TJBA + TJRO.

Descobertas:
- `KNOWLEDGE_ATOMS` devem ser separados de `BANK/EDITAL PACKAGING`;
- FGV varia formato/linhas/quantidade conforme edital, mas casos integrados e espelhos atomizados aparecem repetidamente;
- RN cobrou teoria constitucional abstrata (Friedrich Müller) dentro de conflito registral real;
- RN também cobrou Tema 777 + perda da delegação + substituição >6 meses no mesmo caso;
- ES espelha peça e discursivas por átomos jurídicos;
- Cebraspe BA/RO explicita subitens/pontuação e RO cobra qualificação registral/nota devolutiva em peça de imóvel rural.

## Oral Corpus seed
`research/CARTORIO_ORAL_CORPUS_SEED_RES696_2026.md`

Novo baseline 696 torna o oral mais reproduzível:
`PERGUNTA ESCRITA → ATOMS → RESPOSTA → REPERGUNTA GUIADA → RUBRIC`.

- FGV ES/RN atuais: documentos públicos de convocação/forma, mas não promover relatos informais a corpus oficial.
- Cebraspe histórico possui malotes públicos com pergunta + padrão de resposta; usar com REGIME_TAG.

## Learning Engine evidence
`research/LEARNING_ENGINE_LEGAL_REASONING_EVIDENCE_2026-09-10.md`

Preservar:
- retrieval + spacing;
- feedback obrigatório para treino útil;
- worked examples e fading em produção complexa;
- encoding check ≠ assessment.

## Proposition Ledger N/R — Regime Geral
`data/atlas/PROPOSITION_LEDGER_REGIME_GERAL_SEED_2026-09-10.md`

Atualizado com C0 e C1. Sinais fortes já observados:
- RG-RESP-022: responsabilidade art. 22 = recorrência ENAC;
- RG-IMP-027: 3º/4º grau = recorrência ENAC + estadual;
- RG-RESP-T777: escrita FGV MS/RN/ES + Cebraspe BA;
- RG-LOSS-035: objetiva ENAC + escrita RN;
- RG-INT-ADI1183: escrita RN diretamente sobre >6 meses;
- arts. 29–30: cluster recorrente e candidato a organização semântica/heatmap.

## Próximo HOT autônomo
1. expandir C0 para CF art. 236 + CNN/CNJ dentro de Regime Geral;
2. construir heatmap C1/C2 dos arts. 20–36 Lei 8.935;
3. abrir proposition ledgers de CNN/CNJ e LRP;
4. coletar oral oficial público com REGIME_TAG e acompanhar o novo padrão 696;
5. triangular objective grammar FGV x Cebraspe;
6. produzir **primeiro Depth Budget formal de Regime Geral** somente após essas expansões;
7. só depois voltar a material learner-facing.

### Anti-drift
Não:
- iniciar estudo agora;
- fabricar Specimen B antes do Atlas;
- transformar volume em KPI;
- usar cursinho/material de Delegado como cânone;
- contar OAB/MP/Magistratura como frequência de Cartório;
- usar prova antiga sem revalidar conteúdo/fase;
- declarar suficiência sem held-out;
- exigir microgestão do usuário.