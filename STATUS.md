# GX Cartório OS — Estado Atual

Atualizado em 10/09/2026.

## Branch HOT
`chatgpt/gx-cartorio-v0.1`

## Handoff HOT
Antes de qualquer retomada, ler:
`handoff/NEXT_SESSION_POINTER_2026-09-10.md`

Esse ponteiro incorpora as exigências autorais mais recentes sobre eficiência extrema, oral/discursiva/prática progressivas, lei seca guiada, controle de carga de revisão, ADHD-aware UX, evolução/reuso dos objetos de estudo e preservação de histórico jurídico versus adaptação à lei vigente.

## Missão canônica
Levar o candidato de conhecimento competitivo enferrujado/próximo de zero até **prontidão verificável para aprovação e boa classificação em concursos de outorga de delegações notariais e registrais**, sem transformar o processo em gestão manual de cursinho.

Objetivo não é erudição máxima. Teoria, fundamentos, doutrina e prática entram quando aumentam:
- compreensão;
- retenção;
- acerto e discriminação;
- velocidade;
- resolução de caso;
- discursiva;
- peça prática;
- oral;
- margem competitiva para escolha da delegação.

## Horizonte real
- **2026:** bootstrap do tutor + início da preparação real. ENAC 2026.2 não será prestado por decisão autoral.
- **primeira edição ENAC 2027:** primeiro alvo de habilitação.
- **fim de 2027:** alvo desejado de prontidão competitiva ampla e possibilidade real de aprovação.
- **2028:** teto/buffer máximo, não duração padrão planejada.

A data exata das edições 2027 não será inventada antes de publicação oficial.

## Baseline regulatório atual
Resolução CNJ 696/2026 vigente.

### ENAC
- habilitatório/eliminatório, não classificatório;
- ampla concorrência: ≥60% no total;
- certificado válido por 6 anos;
- pelo menos duas edições por ano.

### Concurso estadual
A objetiva, quando mantida em vez de substituída pelo ENAC, continua uma barreira relevante: para ampla concorrência, a Resolução 696 prevê mínimo de 50% em N/R, 60% total e convocação limitada por colocação/vaga.

Pesos finais nacionais:
- discursiva: 70%;
- oral: 25%;
- títulos: 5%.

Discursiva inclui no mínimo dissertação + peça prática + três questões discursivas.

**Consequência:** o GX não otimiza para `60 raspando no ENAC`. O certificado é limiar; o conhecimento além do corte transfere diretamente para objetiva estadual, escrita, prática e oral.

## Currículo
- matérias ENAC atual: **11/11**;
- temas oficiais de alto nível: **181/181**;
- subitens oficiais N/R: **138/138**;
- Dual Spine preservada: edital visível/segmentado + grafo interno.

### Grafo operacional v0.1
Priorizar duas relações que mudam decisão:
- `requires`;
- `confusable_with`.

Não construir ontologia ornamental antes da necessidade.

## Mastery canônico
Escala única M0–M7:
- M0 não visto;
- M1 reconhece com apoio;
- M2 recupera núcleo sem apoio;
- M3 discrimina;
- M4 aplica em item/caso inédito;
- M5 produz escrito;
- M6 executa prática;
- M7 sustenta oral/reperguntas.

`Retention/stability` é eixo separado. O drift anterior 0–6 versus M0–M7 foi corrigido em `architecture/LEARNING_SYSTEM.md`.

## Ordem pedagógica
N/R entra **desde o primeiro ciclo**, porque combina maior peso atual + baixa exposição prévia + alto valor de transferência + necessidade de muitos ciclos de consolidação.

Civil, Constitucional, Administrativo e demais fundações entram em espiral e `foundation just in time`. O candidato continua enxergando Discipline Maps coerentes, sem sopa interdisciplinar.

## Corpus ENAC histórico — estado real
Passagem 1 concluída como **indexação/classificação histórica**:
- 2025.1: 100/100;
- 2025.2: 100/100;
- 2026.1: 100/100 canônicas;
- total lógico: **300/300**;
- anuladas: 6/300;
- 4 registros antigos de bootstrap do 2026.1 permanecem excluídos das métricas.

### Correção de nomenclatura
`300/300` não significa corpus plenamente reconstruído.

Ainda faltam em escala integral:
- enunciado/alternativas em representação operacional;
- fundamento por item;
- reconstrução alternativa por alternativa;
- rationale oficial de recursos quando disponível;
- microtema fino;
- snapshots histórico/atual revalidados;
- difficulty empírica.

Ver `research/ENAC_300_CORPUS_GATE.md`.

## Limite estatístico reconhecido
180 questões N/R em 138 subitens e apenas três edições não sustentam pseudo-precisão de frequência microtemática nem série temporal robusta.

O GX separa:
- **Domain Incidence Model:** agrega concursos de cartório multibanca com proveniência para responder `o que o domínio cobra?`;
- **Bank Style Model:** fica restrito a banca + janela + família + fase para responder `como esta banca cobra?`.

Prioridade usa múltiplos sinais: matriz, superfície do edital, incidência de domínio, estilo da banca, dependências, transferência, volatilidade normativa e desempenho individual.

## Material
Experiência do candidato permanece:
`MAP → MASTER → REVIEW → RECALL → EXAM → REFERENCE`.

Direção editorial após auditoria:
- reduzir duplicação canônica;
- MASTER/Knowledge Unit como fonte semântica principal;
- EXAM como aplicações/itens;
- REFERENCE como fontes/profundidade;
- MAP/REVIEW/RECALL preferencialmente derivados, não cópias manuais divergentes.

## Freshness Firewall
Ativo. Direito histórico, direito atual e cutoff do alvo permanecem separados.

Volatilidade normativa pode aumentar prioridade de revalidação/estudo, mas não será tratada como prova automática de maior incidência.

## Retention engine
- heurísticas apenas como bootstrap;
- FSRS é candidato para recalls atômicos/flashcards;
- não substitui mastery M0–M7 nem o scheduler completo;
- modelos complexos de knowledge tracing não entram sem dados individuais suficientes.

## Stack gratuita atual
### GitHub
Source of Truth de arquitetura, protocolos, estado HOT e pesquisa. Repositório atual é **público**.

### Notion Free
Human Knowledge Portal + bancos existentes, provisoriamente.

A limitação observada é da consulta SQL avançada. `rows` e `view` continuam opções para leituras delimitadas, então Notion não foi descartado.

### Google Drive
Corpus oficial, PDFs, espelhos e assets.

### Google Sheets
Candidato futuro para telemetria/analytics. **Não criado/promovido em produção**. Só após necessidade real + schema + sandbox + reconciliação.

### SQLite
Não adotado como data plane imediato: binário, diff ruim e sem transação SQL persistente disponível através do runtime GitHub atual. Reavaliar apenas se houver aplicação própria/runtime adequado.

## Auditoria externa de 09/09/2026
A nota externa foi tratada como hipótese, não como autoridade.

Cross-review canônica:
`research/EXTERNAL_AUDIT_CROSS_REVIEW_2026_09_09.md`

Principais achados adotados:
- Passagem 1 é índice/classificação, não corpus integral;
- mastery precisava ser unificado;
- N/R deve começar cedo;
- 300 itens não sustentam estatística microtemática fina;
- separar incidência de domínio de estilo de banca;
- reduzir ontologia operacional;
- reduzir duplicação de material;
- coletar desempenho real do candidato cedo;
- espelhos oficiais/prática precisam virar corpus prioritário.

Principais achados rejeitados/ajustados:
- pressão para fazer ENAC 2026.2;
- `qualquer ponto >60 é desperdício`;
- desvalorizar objetiva estadual porque peso final =0;
- SQLite/Git como solução imediata automática;
- afirmar que Notion inteiro ficou inviável após cota SQL;
- afirmar que o repositório é privado;
- percentuais inventados no red team.

## Próximo bloco de trabalho
### 1. Editorial Standard v1.0
- congelar gramática visual pequena e estável;
- limitar densidade de labels/callouts;
- definir remissões e regras anti-duplicação;
- formalizar lei seca, jurisprudência, doutrina e teoria dentro do MASTER;
- manter REVIEW/RECALL derivados.

### 2. Primeiro piloto canônico ponta a ponta
Passar um tópico real por:
`edital -> fontes primárias -> jurisprudência atual -> ENAC/FGV -> FGV cartório/estadual -> corpus multibanca do domínio -> oral/discursiva/prática -> Reconstruction Cards -> depth budget -> MASTER -> REVIEW -> RECALL -> EXAM -> QA/freshness`.

### 3. Corpus operacional
- tornar enunciados/alternativas acessíveis ao runtime sem republicação desnecessária;
- produzir Reconstruction Cards junto dos nós que entram no estudo;
- capturar fundamentos e respostas oficiais a recursos prioritariamente;
- abrir camada específica de oral/discursiva/prática com histórico e adaptação vigente separados.

### 4. Lei seca guiada + controle de carga de revisão
- leitura literal seletiva e justificável;
- recall de listas/prazos/competência/exceções;
- fila ponderada por valor de prova × risco de esquecimento × lacuna × transferência × freshness;
- fundir, aposentar ou reduzir prompts saturados para impedir avalanche de revisão.

### 5. Minimum Viable Tutor
- alinhar runtime à escala M0–M7;
- escolher nó;
- orientar;
- ensinar bloco curto e coerente;
- retrieval;
- questão/caso;
- diagnosticar;
- registrar mastery + retenção;
- agendar;
- selecionar próxima ação.

### 6. Learner model
Após começar o estudo, registrar apenas sinais com valor decisório:
- resposta;
- confiança prévia;
- correção;
- latência aproximada quando útil;
- necessidade de pista;
- causa do erro;
- intervalo;
- modalidade;
- distinguir traço cognitivo geral de dificuldade específica do domínio.

## Regra anti-procrastinação arquitetural
A infraestrutura deve chegar rapidamente a **Minimum Viable Tutor**. Depois disso, mudança de arquitetura só recebe prioridade quando:
- corrige falha observada;
- reduz carga executiva do candidato;
- melhora segurança jurídica;
- melhora evidência de aprendizagem;
- ou aumenta capacidade de preparação para uma fase real.

O tempo autônomo da IA trabalhando na engenharia não é `tempo de estudo` do candidato. O candidato deve passar a maior parte de sua energia estudando, não administrando o sistema.

## Regra de qualidade
Nenhuma incidência, previsão, prioridade ou material vira canônico sem origem documentada e nível de confiança compatível com a evidência. Complexidade arquitetural só é aceita quando muda uma decisão real.
