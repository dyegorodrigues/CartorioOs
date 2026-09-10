# GX Cartório OS — Next Session Pointer — 2026-09-10

## Purpose
HOT handoff para continuidade sem reabrir arquitetura do zero.

## Branch HOT
`chatgpt/gx-cartorio-v0.1`

## Missão e horizonte
Levar o candidato de conhecimento competitivo enferrujado/próximo de zero até **prontidão verificável para aprovação e boa classificação em ENAC + objetiva estadual + discursiva + prática + oral**.

Horizonte autoral:
- 2026: bootstrap + início do estudo real; ENAC 2026.2 fora do alvo por decisão autoral;
- primeira edição ENAC 2027: primeiro alvo de habilitação;
- fim de 2027: prontidão competitiva ampla desejada;
- 2028: teto/buffer máximo, não duração padrão.

O alvo não é `passar raspando`. É reduzir sistematicamente classes de erro e aproximar desempenho de teto/gabarito sem transformar o estudo em enciclopédia ou administração manual de cursinho.

## Baseline regulatório atual
Resolução CNJ 696/2026 vigente.

Consequência de fase:
- objetiva estadual, quando mantida em vez de substituída pelo ENAC, continua eliminatória;
- discursiva = 70% da nota final;
- oral = 25%;
- títulos = 5%.

Portanto o GX não abandona objetiva e também não adia toda produção até depois dela.

---

# ESTADO HOT

## Work Order A — CONCLUÍDO / CONGELADO
`material/EDITORIAL_STANDARD.md` = **Editorial Standard v1.0**, congelado em 10/09/2026.

Arquivos alinhados:
- `architecture/LEARNING_SYSTEM.md`;
- `architecture/MINIMUM_VIABLE_TUTOR.md`;
- `research/LEARNING_METHOD_VALIDATION_2026_09_10.md`.

### Progressão canônica
- **M0:** input guiado, mapa, leitura/explicação, lei seca guiada, exemplos resolvidos;
- **M1:** recall leve/assistido;
- **M2–M3:** Q→A, perguntas sem pista, C/E/MCQ, distinções, mini casos, voz curta;
- **M3–M4:** transferência, item/caso inédito, issue spotting e microprodução;
- **M4–M5:** discursiva `átomos → esqueleto → parágrafo → resposta completa → tempo/linhas`;
- **M5–M6:** prática `instrumento/ato → estrutura → elementos → execução`;
- **M5–M7:** oral formal `estrutura → precisão → tempo → reperguntas → mudança de premissa`.

**Voz/microfone pode ser usada desde M1/M2 como interface de recall. Isso não equivale a M7.**

É proibido usar discursiva fria, peça fria ou oral de banca como rotina de avaliação de conteúdo ainda não aprendido. Diagnóstico frio, quando útil, não penaliza mastery inicial.

### Dificuldade produtiva
Tarefa aproximadamente um degrau cognitivo acima do desempenho demonstrado.

Falha repetida provoca regressão de suporte:
`problema completo → caso guiado → contraste → recall do núcleo → releitura localizada`.

Depois o sistema volta a subir. Não prender o candidato por dias no mesmo formato para `forçar` aprendizagem.

---

# Correção autoral de 10/09 — objetiva permanente
A progressão M0–M7 **não é uma sequência de fases que substituem as anteriores**.

Novo contrato canônico:
`architecture/CONTINUOUS_ASSESSMENT_BRAID.md`.

Regra:
**subir de mastery adiciona capacidade; não apaga capacidade anterior.**

Logo:
- objetiva é trilha permanente enquanto houver ENAC/concursos estaduais atuais ou futuros;
- retrieval/recall é permanente;
- lei seca guiada retorna conforme valor, fragilidade e freshness;
- discursiva, prática e oral são adicionadas progressivamente;
- um nó M5–M7 continua recebendo objetiva inédita, mista, adversarial e sob tempo em frequência compatível com sua estabilidade;
- quando surgir novo concurso estadual, o National Core é preservado, entra overlay estadual + Bank Style Model + revalidação de freshness;
- aprovação em um concurso não zera o conhecimento: nós fortes entram em `maintenance mode`.

`workflows/DAILY_STUDY_LOOP.md` foi atualizado para quatro faixas adaptativas:
1. `REACTIVATE`;
2. `ACQUIRE`;
3. `OBJECTIVE`;
4. `OUTPUT`.

Nem toda sessão contém as quatro. OUTPUT não pode consumir o avanço curricular quando o candidato ainda está majoritariamente em aquisição.

Questões não têm meta bruta ornamental. O sistema busca **máxima informação por questão**: aumenta volume enquanto novas questões revelam distratores, erros, baixa velocidade, baixa retenção ou estilo de banca; reduz repetição quando o ganho marginal cai.

Separar:
- `Learn item` = usado para aprender/consolidar;
- `Measure item` = reservado para medir generalização/held-out.

---

# Sufficiency Gate
A pergunta autorreferente `com esse material dá para resolver qualquer questão?` **não é evidência** quando respondida pela própria IA.

O padrão exige:
1. `Coverage Matrix` — edital/nós/proposições/fontes/depth/output;
2. `Proposition Coverage` — regras e discriminadores necessários;
3. `Held-out Resolution Test` — questões/casos não usados para escrever aquela versão;
4. `Adversarial Variants` — inversão de exceção, competência, prazo, fato decisivo, instituto confundível e snapshot.

Falhas:
- `CONTENT_GAP`;
- `DISCRIMINATION_GAP`;
- `TRANSFER_GAP`;
- `FRESHNESS_GAP`;
- `QUESTION_DEFECT`;
- `OUT_OF_SCOPE`;
- `LEARNER_GAP`.

Os quatro primeiros corrigem material. `LEARNER_GAP` só pode ser atribuído quando o corpus canônico realmente sustentava a solução no nível esperado.

Linguagem permitida: `sem lacuna conhecida para o escopo validado até esta data`.

Linguagem proibida: `resolve qualquer questão`, `100% garantido`, `completo para toda questão futura`.

## Quatro provas de confiabilidade
Para um nó/material:
1. **Scope proof:** está no edital/currículo ou é pré-requisito justificável?
2. **Source proof:** proposição correta e rastreada a autoridade adequada/snapshot?
3. **Exam proof:** existe evidência de como isso vira questão/saída ou razão real de transferência?
4. **Learner proof:** candidato recupera, discrimina e aplica depois de intervalo?

Nenhuma isoladamente prova prontidão.

---

# Varredura Q→A e flashcards
Cada unidade coerente deve gerar uma revisão tipo pergunta-resposta que percorra o capítulo sem releitura integral.

Q→A prioriza:
- conceitos;
- requisitos;
- competência;
- prazo/lista;
- exceção;
- efeito;
- `confunde com`;
- literalidade decisiva;
- precedentes answer-changing;
- erros pessoais progressivamente.

Flashcards/objetos:
- `Atomic Card` — prazo, competência, requisito, definição curta, exceção literal;
- `Contrast Card` — A × B, regra × exceção, palavra decisiva;
- `Reconstruction Card` — estrutura, procedimento, mapa, resposta oral curta, esqueleto discursivo/prático.

Ciclo:
`active → merged → downgraded → retired → reactivated`.

Objetivo: fila mais inteligente e potencialmente menor com o domínio, não pilha infinita.

---

# Lei seca guiada + Freshness Firewall
Lei seca permanece obrigatória quando redação muda resposta:
- requisitos;
- prazos;
- competências;
- legitimidade;
- vedações;
- exceções;
- listas;
- ordem procedimental;
- palavras limitadoras/ampliativas;
- alterações recentes;
- dispositivos com evidência de cobrança.

Freshness Firewall:
- snapshot histórico ≠ lei atual;
- questão original preservada;
- adaptação atual separada;
- source version / checked_at / target cutoff rastreáveis.

---

# Currículo e corpus preservados
Currículo:
- ENAC: 11/11 matérias;
- temas de alto nível: 181/181;
- subitens oficiais N/R: 138/138;
- Dual Spine preservada;
- relações operacionais prioritárias: `requires` e `confusable_with`;
- mastery M0–M7;
- retention/stability separado.

N/R continua entrando desde o primeiro ciclo. O piloto em Constitucional abaixo é **calibração metodológica auditável**, não mudança permanente da prioridade curricular.

Corpus ENAC histórico, Passagem 1:
- 2025.1: 100/100;
- 2025.2: 100/100;
- 2026.1: 100/100 canônicas;
- total lógico: 300/300;
- 6 anuladas preservadas.

`300/300` = indexação/classificação, não reconstrução integral.

Manter separados:
- `Domain Incidence Model` — o que o domínio cobra em corpus multibanca;
- `Bank Style Model` — como banca/período/família/fase cobra.

Sem pseudo-probabilidades microtemáticas com amostra pequena.

---

# Work Order B — EM EXECUÇÃO

## B0 — piloto de calibração em domínio auditável
Arquivo de contrato:
`workflows/WORK_ORDER_B_CALIBRATION_PILOT.md`.

Tema escolhido:
**Direito Constitucional → Poder Constituinte (GXN-49)**.

Motivo:
- é tema expresso da matriz ENAC 2026.2;
- Constitucional possui peso objetivo maior que Penal no ENAC atual;
- o candidato tem conhecimento residual suficiente para auditar plausibilidade, omissões, excesso e nível;
- existe evidência objetiva, discursiva de concurso de Notário e oral de outorga sobre o núcleo;
- permite testar o princípio `mesmo conhecimento, múltiplas saídas` sem obrigar produção fria.

**Isso não significa abandonar N/R.** Depois da calibração, o padrão é transferido ao primeiro cluster N/R, onde a segurança substantiva dependerá ainda mais de fonte primária + corpus + held-out + adversarial + freshness.

## Proposition Map v0.1 — CRIADO
Arquivo:
`research/PILOT_POWER_CONSTITUENT_PROPOSITION_MAP.md`.

Estado: evidence map, **não MASTER ainda**.

Famílias provisórias cobertas:
- função/fundação do poder constituinte;
- originário: posição jurídica, características e titularidade/exercício;
- derivado/reformador: natureza e limites;
- cláusulas pétreas no nível necessário ao nó;
- emenda controlável × norma constitucional originária;
- poder decorrente estadual;
- institucionalização/revisão estadual;
- Municípios como ponto de oral a validar com rigor;
- DF somente se corpus justificar;
- revisão do ADCT art. 3º com remissão;
- concepções fática/jurídica cobradas pela FGV;
- mutação somente como `confunde com` se necessário.

Regra anti-inchaço já aplicada: `Poder Constituinte`, `Emendas Constitucionais`, `Reforma/Revisão` e `Controle de Constitucionalidade` são temas distintos do currículo. O piloto ensina as pontes necessárias, mas não duplica os capítulos vizinhos.

## Evidência inicial já coletada
- Constituição Federal vigente: arts. 25, 29, 32, 60 e ADCT arts. 3º/11 conforme pertinência;
- STF: limites do poder reformador, controle de emenda, ausência de hierarquia que permita invalidar norma originária contra outra originária e limites do poder decorrente;
- objetiva FGV em famílias originário/derivado/decorrente, limites e natureza;
- discursiva FGV/TJ-RJ/Notário/2022 sobre poder constituinte decorrente;
- oral oficial CEBRASPE/TJ-MT/Outorga/2017 com poder originário/supremacia e questão municipal.

Proveniência de banca/fase é preservada. Exemplo CEBRASPE não vira automaticamente `estilo FGV`.

## Split anti-autoengano do B0
Antes do MASTER final:
- `BUILD SET` — itens/proposições usados para descobrir o conteúdo;
- `VALIDATION SET` — itens não usados para escrever a versão;
- `CHALLENGE SET` — banca/fase adjacente + variações adversariais.

O modelo não pode usar conhecimento externo escondido para declarar que o material resolveu um held-out. A resolução deve ser sustentada pelo corpus canônico no nível esperado.

## Próximo passo HOT
**Não voltar a brainstorm de método.**

Executar no B0:
`QUESTION CORPUS → refino do PROPOSITION MAP → DEPTH BUDGET → MASTER v0.1 → Q→A → OBJECTIVE TRAINING → OUTPUT objects preparados mas liberados por mastery → VALIDATION/CHALLENGE → USER AUDIT → correções`.

A auditoria do candidato deve responder:
- faltou algo que ele sabe ser importante?;
- entrou doutrina inútil?;
- está claro o que compreender versus memorizar?;
- questões parecem consequência do material?;
- alguma solução exigiu algo que o MASTER não ensinou?;
- Q→A reconstrói o capítulo sem releitura integral?;
- a carga permite avançar?

Depois de calibrado:
`TRANSFER TO N/R` e primeiro piloto N/R ponta a ponta.

## Work orders seguintes preservados
### C. Oral + written corpus layer
Registry com fonte/banca/ano/fase, prompt, espelho, átomos, difficulty, snapshot, adaptação atual e reperguntas.

### D. Lei seca protocol
Formalização operacional completa.

### E. Review-load control
Fila por `exam value × forgetting risk × learner gap × transfer × freshness`, com merge/retire.

### F. Minimum Viable Tutor gate
`choose node → orient → teach coherent chunk → retrieval compatível → item/case → diagnose → register M0–M7 + retention → schedule → next action`.

## Regra anti-procrastinação arquitetural
Editorial Standard v1.0 permanece congelado durante o piloto.

Só reabrir estrutura se o piloto demonstrar falha observável que prejudique aprendizagem, aumente carga executiva, ameace freshness/segurança jurídica, impeça evidência de domínio ou reduza preparação para fase real.
