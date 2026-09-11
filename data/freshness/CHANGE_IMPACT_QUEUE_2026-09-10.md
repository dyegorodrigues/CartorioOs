# GX Cartório OS — Change Impact Queue

Snapshot: 2026-09-10
Status: infraestrutura operacional do Freshness Firewall; NÃO é material de estudo.

## Objetivo
Toda mudança normativa/jurisprudencial deve gerar um impacto rastreável nas superfícies derivadas do mesmo nó. Nenhuma atualização deve depender de alguém lembrar manualmente de corrigir MASTER, REVIEW, Q→A e questões separadamente.

## Estados
`DETECTED → SOURCE_VERIFIED → PROPOSITIONS_MAPPED → EXAM_SNAPSHOT_CHECKED → SURFACES_PATCHED → QUESTIONS_REVALIDATED → CLOSED`

## Campos obrigatórios
- Change ID
- ato/decisão e data
- vigência
- source URL
- propositions affected
- CURRENT_LAW
- EXAM_SNAPSHOT_LAW por prova-alvo
- affected surfaces
- historical question impact
- owner/action
- state

## Queue inicial

| Change ID | Evento | Proposições/nós | Impacto principal | ENAC 2026.2 | Estado |
|---|---|---|---|---|---|
| CHG-696-2026 | Res. CNJ 696/2026 | arquitetura do concurso inteira | fases, pesos, conteúdo nacional, disciplinas objective-only, oral | governa o exame/concursos; não confundir com conteúdo jurídico material | PROPOSITIONS_MAPPED |
| CHG-218-2026 | Prov. 218 — Justiça Aberta | CNN-JA-136/136A, deveres/fiscalização | novo desenho do sistema + dever funcional de atualização | verificar vigência x cutoff | PROPOSITIONS_MAPPED |
| CHG-219-2026 | Prov. 219 — vacâncias | CNN-VAC-073/RGV, RG7 | substitui/atualiza fluxo nacional de vacância e dados da RGV | verificar vigência x cutoff | PROPOSITIONS_MAPPED |
| CHG-220-2026 | Prov. 220 — incapacidade permanente | CNN-INC-220, extinção art.39 III | procedimento nacional novo | verificar vigência x cutoff | PROPOSITIONS_MAPPED |
| CHG-227-2026 | Prov. 227 — solvência trabalhista | CNN-SOLV*, arts.20/31/36 | declaração, fiscalização, consequência disciplinar/cautelar | vigência com vacatio; calcular EFFECTIVE_FROM para snapshot | PROPOSITIONS_MAPPED |
| CHG-224-2026 | Prov. 224 — Constrijud | LRP-RI-CONSTR-012, ordens judiciais/RI | novo fluxo eletrônico nacional de constrição | verificar vigência x cutoff | SOURCE_VERIFIED |
| CHG-228-2026 | Prov. 228 — extratos RI | LRP-RI-EXTRATO-011 | nova disciplina de extratos eletrônicos | verificar vigência x cutoff | SOURCE_VERIFIED |
| CHG-229-2026 | Prov. 229 — SERP | LRP-RI-ELETR-009 + CNN/SERP | interoperabilidade/Meu Registro/sistemas nacionais | verificar vigência x cutoff | SOURCE_VERIFIED |
| CHG-246-2026 | Prov. 246 — alienação fiduciária | LRP-RI-AFID-013 | forma/título e integração jurisprudencial | verificar vigência x cutoff | SOURCE_VERIFIED |
| CHG-253-2026 | Prov. 253 — CENPROT | Protesto/publicidade | certidões/consultas após sustação | publicado antes cutoff; vigência concreta precisa ser checada | SOURCE_VERIFIED |

## Regra de cascata
Quando um Change ID chega a `PROPOSITIONS_MAPPED`, o sistema identifica automaticamente as futuras superfícies dependentes:
`MASTER → REVIEW → LEI SECA → Q→A → FLASHCARDS → QUESTION EXPLANATIONS → SIMULADOS → OUTPUT RUBRICS`.

Quando ainda não há superfície learner-facing publicada, o patch ocorre no Atlas/ledger/depth budget e evita gerar conteúdo velho.

## Regra para questões históricas
Após mudança, cada questão recebe:
- VALID_CURRENT;
- PARTIAL;
- FORM_ONLY;
- RETIRED.

Nunca apagar silenciosamente uma questão histórica: preservar a evidência e registrar por que deixou de servir como assessment atual.

## Regra de prova-alvo
Cada prova cria seu próprio snapshot:
`CURRENT LAW` pode ser diferente de `EXAM SNAPSHOT LAW` por cláusula de anterioridade normativa do edital.

ENAC 2026.2: preceito com vigência iniciada a menos de 90 dias da prova não entra; revogado no mesmo período pode entrar. Data prevista 22/11/2026 → cutoff aritmético 24/08/2026, sempre usando vigência efetiva.

## Próxima execução
- preencher EFFECTIVE_FROM de cada ato 2026;
- ligar às questões históricas já classificadas;
- automatizar checklist de revalidação antes de gerar material/simulado;
- criar snapshot específico para primeiro ENAC 2027 quando edital existir.