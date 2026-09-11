# GX Cartório OS — Change Impact Queue

Snapshot: 2026-09-10
Status: infraestrutura operacional do Freshness Firewall; NÃO é material de estudo.

## Objetivo
Toda mudança normativa/jurisprudencial deve gerar um impacto rastreável nas superfícies derivadas do mesmo nó. Nenhuma atualização deve depender de alguém lembrar manualmente de corrigir MASTER, REVIEW, Q→A e questões separadamente.

## Estados
`DETECTED → SOURCE_VERIFIED → PROPOSITIONS_MAPPED → EXAM_SNAPSHOT_CHECKED → SURFACES_PATCHED → QUESTIONS_REVALIDATED → CLOSED`

## Campos obrigatórios
Change ID; ato/decisão; publicação; EFFECTIVE_FROM; source; propositions; CURRENT_LAW; EXAM_SNAPSHOT_LAW; surfaces; historical-question impact; state.

## ENAC 2026.2 snapshot rule
- prova prevista: 22/11/2026;
- cutoff aritmético de 90 dias: 24/08/2026;
- o edital exclui preceitos cuja **vigência** tenha iniciado menos de 90 dias antes da prova e admite cobrança dos revogados dentro do período;
- portanto publicação e vigência são campos diferentes.

## Queue

| Change ID | Evento | EFFECTIVE_FROM confirmado nesta passagem | Proposições/nós | ENAC 2026.2 snapshot | Estado |
|---|---|---|---|---|---|
| CHG-696-2026 | Res. CNJ 696/2026 | vigente conforme ato oficial | arquitetura do concurso | governa arquitetura; não tratar como simples conteúdo material | PROPOSITIONS_MAPPED |
| CHG-218-2026 | Prov. 218 — Justiça Aberta | data da publicação (art.4) | CNN-JA-136/136A | anterior ao cutoff; elegível em princípio | EXAM_SNAPSHOT_CHECKED |
| CHG-219-2026 | Prov. 219 — vacâncias | data da publicação (art.15) | CNN-VAC-073/RGV, RG7 | anterior ao cutoff; elegível em princípio | EXAM_SNAPSHOT_CHECKED |
| CHG-220-2026 | Prov. 220 — incapacidade permanente | data da publicação (art.24) | CNN-INC-220, art.39 III | anterior ao cutoff; elegível em princípio | EXAM_SNAPSHOT_CHECKED |
| CHG-227-2026 | Prov. 227 — solvência trabalhista | após 60 dias da publicação no DJe de 11/06/2026 | CNN-SOLV*, arts.20/31/36 | vigência se inicia antes de 24/08; elegível em princípio. Primeiro ano tem prazo especial de 30 dias após entrada em vigor | EXAM_SNAPSHOT_CHECKED |
| CHG-224-2026 | Prov. 224 — Constrijud | PENDENTE de confirmação artigo final | LRP-RI-CONSTR-012 | provavelmente anterior ao cutoff; não promover até confirmar | SOURCE_VERIFIED |
| CHG-228-2026 | Prov. 228 — extratos RI | data da publicação (art.6) | LRP-RI-EXTRATO-011 | anterior ao cutoff; elegível em princípio | EXAM_SNAPSHOT_CHECKED |
| CHG-229-2026 | Prov. 229 — SERP/Meu Registro | data da publicação (art.4); implantação operacional progressiva | LRP-RI-ELETR-009 + CNN/SERP | preceitos vigentes antes cutoff; distinguir vigência normativa de cronograma técnico | EXAM_SNAPSHOT_CHECKED |
| CHG-246-2026 | Prov. 246 — alienação fiduciária | data da publicação (art.3) | LRP-RI-AFID-013 | anterior ao cutoff; elegível em princípio | EXAM_SNAPSHOT_CHECKED |
| CHG-253-2026 | Prov. 253 — CENPROT | data da publicação (art.5); sistemas têm 90 dias para adequação | Protesto/publicidade | publicação/vigência antes cutoff; regra material pode ser elegível embora implementação sistêmica tenha prazo | EXAM_SNAPSHOT_CHECKED |

## Distinção nova: NORMATIVE EFFECTIVE x OPERATIONAL DEADLINE
Não confundir:
- `norma entrou em vigor`;
- `sistema/serventia ganhou X dias para implementar`.

Exemplos:
- Prov. 229 vigora na publicação, mas implantação do ecossistema é progressiva;
- Prov. 253 vigora na publicação, mas CENPROT/tabeliães têm 90 dias para adequar sistemas.

Questão pode explorar justamente essa diferença. O Atlas deve manter `EFFECTIVE_FROM` e `IMPLEMENT_BY` separados.

## Regra de cascata
`mudança → proposition IDs → CURRENT_LAW / EXAM_SNAPSHOT_LAW → MASTER → REVIEW → lei seca → Q→A → flashcards → question explanations → simulados → output rubrics`.

Enquanto o material learner-facing ainda não existe, a correção ocorre no Atlas/depth budget e evita gerar conteúdo velho.

## Questões históricas após mudança
- VALID_CURRENT;
- PARTIAL;
- FORM_ONLY;
- RETIRED.

Nunca apagar silenciosamente questão histórica. Nunca usar PARTIAL/FORM_ONLY em mastery sem contextualizar ou reescrever.

## Próxima execução
1. confirmar EFFECTIVE_FROM/IMPLEMENT_BY dos atos 224, 225, 237, 242 e demais deltas;
2. ligar cada change ID a questões ENAC/estaduais afetadas;
3. produzir checker de snapshot antes de simulado/material;
4. criar snapshot do primeiro ENAC 2027 quando o edital existir.