# GX Cartório OS — Held-Out Registry v0.1
## Regime Geral / Lei 8.935 / CNN

Snapshot: 2026-09-10
Status: SEALED METADATA. NÃO usar conteúdo reservado no BUILD.

## Regra
Este arquivo registra apenas identidade e recorte das provas reservadas. **Não transcrever, resumir, classificar nem consultar enunciados reservados antes do freeze do specimen/material que será validado.**

Se uma questão reservada tiver sido acidentalmente vista ou usada em pesquisa de construção, ela deve ser marcada `CONTAMINATED` e substituída.

## Pools

### H1 — Vunesp/TJSP 13º Concurso
- fonte: Vunesp/TJSP, 13º Concurso de Outorga, Prova 04 — Registros Públicos, Notas e Protesto;
- BUILD já contaminado/consultado: Q1–Q4;
- HELD-OUT inicial: **Q5–Q15**, sem inspeção de conteúdo nesta fase;
- objetivo: testar literalidade sistemática, organização da Lei 8.935 e possíveis proposições não ensinadas;
- status: `SEALED`.

### H2 — Consulplan/TJMG Edital 1/2024, concurso em curso/recente
- fonte oficial localizada: edital e documentos Consulplan/TJMG;
- prova objetiva: 100 múltipla escolha; disciplinas incluem Direito N/R e demais áreas;
- caderno oficial específico ainda não localizado no index público nesta sessão;
- reserva: **primeiro bloco nacional de Regime Geral do caderno oficial quando localizado**, antes de leitura;
- status: `PENDING_LOCATOR`;
- regra: ao localizar o PDF, registrar hash/URL e números das questões antes de abrir seu conteúdo.

### H3 — IESES/TJPA 2026
- fonte: prova 6015 Tipo 1 + gabarito oficial;
- BUILD já utilizado: Q2 e Q10; outras questões iniciais foram visualizadas no PDF e portanto não devem ser tratadas como held-out limpo;
- não reservar questões já exibidas/consultadas;
- futuro held-out somente após escolher um recorte não exposto e registrar antes de abrir;
- status: `PARTIALLY_CONTAMINATED`.

### H4 — Future post-696 state exam
- reservar automaticamente **ao menos 20% do primeiro concurso estadual publicado integralmente sob Res. 696/2026**, estratificado por cluster;
- esse pool será o melhor teste de generalização para a arquitetura nova;
- status: `FUTURE_RESERVED`.

## Separação BUILD / VALIDATION / CHALLENGE
- BUILD: ENAC já analisados + FGV MS/RN/ES + Cebraspe BA/RO + IESES Q2/Q10 + Vunesp Q1–Q4 + fontes primárias.
- VALIDATION HELD-OUT: H1 + H2 + H4, somente após material freeze.
- CHALLENGE: questões de outra banca/forma, novas formulações sintéticas adversariais separadas e corpus cross-node.

## Critério de falha do material
Após freeze, cada held-out errada deve ser diagnosticada como:
1. `MATERIAL_GAP` — proposição necessária não ensinada;
2. `STRUCTURE_GAP` — informação existia, mas não estava mentalmente conectada/recuperável;
3. `DEPTH_GAP` — foi ensinada rasa demais para o nível legítimo da questão;
4. `FRESHNESS_GAP` — material/snapshot desatualizado;
5. `TRANSFER_GAP` — base estava presente, mas faltou ensinar aplicação/discriminação;
6. `OUT_OF_SCOPE` — questão depende legitimamente de conteúdo fora do módulo;
7. `BAD_QUESTION` — questão/gabarito problemático, só após verificação robusta.

O aluno só recebe `LEARNER_GAP` depois que o material demonstrou cobertura/estrutura/profundidade adequadas e houve oportunidade real de aquisição/revisão.

## Gate de validação
- S2 exige held-out suficiente e diversificado, não uma única questão;
- o mesmo enunciado em versões/tipos diferentes conta uma vez;
- questão anulada não valida suficiência, mas pode revelar gap/distrator;
- material é corrigido após falha e precisa ser retestado com questão ainda não contaminada.

## Anti-leak
Qualquer agente/IA retomando o projeto deve ler este arquivo e **não abrir H1/H2/H4 antes do freeze de material**.
Se conteúdo for aberto por engano: marcar `CONTAMINATED`, nunca fingir independência do teste.