# GX Cartório OS — Oral Corpus Seed
## Resolução CNJ 696/2026 + provas públicas históricas

Snapshot: 2026-09-10
Status: RESEARCH SEED / não é treino do candidato

## 1. Novo baseline oral nacional
Fonte oficial: Resolução CNJ 696/2026.
Fonte indexada complementar: https://farolnormativo.com.br/ato/180914

### Peso e natureza
- oral = 25% da nota final;
- exclusivamente classificatória no novo regime;
- 25 pontos.

### Composição da nota
Art. 54:
- 90% conteúdo jurídico conforme padrão esperado;
- 10% articulação técnica: postura, adequação da linguagem, articulação e capacidade de argumentação;
- critérios devem ser objetivos; vedado carisma/aparência/sotaque como critério.

### Forma de aplicação
Art. 55:
- pontos sorteados com antecedência mínima de 72h;
- perguntas previamente formuladas pela instituição organizadora;
- pergunta entregue POR ESCRITO ao candidato na arguição;
- diretrizes predefinidas para reperguntas;
- candidatos do mesmo turno respondem às mesmas perguntas;
- turnos distintos recebem perguntas diferentes de dificuldade semelhante;
- edital informa duração máxima, disciplinas e conteúdos.

### Transparência e padrão
Resolução também determina gravação integral e padrão de resposta no fluxo do concurso.

## Consequência estrutural muito importante
O futuro treino oral do GX não deve ser improvisação teatral do tipo “examinador aleatório pergunta qualquer coisa”.

A nova arquitetura nacional favorece treino reproduzível:
`PERGUNTA ESCRITA → ATOMS ESPERADOS → RESPOSTA ORAL → REPERGUNTA GUIADA → RUBRIC`.

Isso permite aproveitar o mesmo proposition graph de objetiva/discursiva sem treinar discurso vazio.

## 2. Oral atual FGV — evidência de editais 2025/2026
### TJES / FGV
Edital atual da prova oral informa avaliação de:
- domínio do conhecimento jurídico;
- adequação da linguagem;
- articulação do raciocínio;
- capacidade de argumentação;
- uso correto do vernáculo;
- possibilidade de consulta a textos de lei disponibilizados pela banca.

O concurso teve prova oral em janeiro/fevereiro de 2026, mas a página pública consultada não disponibiliza um banco integral identificável de perguntas e padrões por candidato. Portanto não inventar corpus oral FGV atual onde ele não está público.

### TJRN / FGV
Página oficial registra convocação, banca e ordem de arguição em agosto de 2026. No snapshot de 10/09/2026, o certame ainda está em andamento. Não promover supostas perguntas de candidatos de redes sociais a evidence A sem documento oficial.

## 3. Corpus oral histórico público Cebraspe — valor e limite
O Cebraspe publicou, em concursos anteriores de Cartório, malotes/pontos com questão e padrão de resposta. Esses arquivos são excelentes para entender `question atomization`, MAS precisam REGIME TAG porque o conteúdo/disciplinas possíveis podem ter mudado sob Res. 696.

### Exemplo — TJSC / Cebraspe, concurso anterior
Ponto de Direito Notarial e Registral pergunta sobre possibilidade de escritura pública autônoma para nomeação de inventariante e exige fundamentação. O padrão fornece regra objetiva, caráter facultativo e relação temporal com inventário/partilha.

### Exemplo — TJSC / Cebraspe, Civil
Pergunta pede ação de petição de herança, prazo/termo inicial e relação com ação rescisória; padrão articula CC, Súmula STF e Tema repetitivo STJ.

### Exemplo — TJSC / Cebraspe, Processo Penal
Há malote histórico com pergunta de ação penal. Sob Res. 696/2026 esse tipo de conteúdo é útil somente como FORM EXAMPLE, não como prioridade oral atual, pois Processo Penal hoje é objective-only no baseline nacional.

## 4. Oral item schema
Cada item do Oral Corpus deve registrar:
- oral_item_id;
- TJ/banca/ano;
- REGIME_TAG;
- disciplina;
- ponto sorteado;
- pergunta escrita;
- reperguntas oficiais, se houver;
- pattern/rubric oficial;
- proposition_ids;
- número de atoms;
- tempo disponível;
- consulta permitida;
- content_validity;
- phase_validity;
- current-source validation;
- dificuldade;
- `BUILD / VALIDATION / HELD-OUT / CHALLENGE`.

## 5. Progressão oral futura GX
Não aplicar agora. Quando runtime for ativado:

### O0 — Q→A spoken recall
20–40 s, sem banca. Serve recuperação.

### O1 — atom answer
Pergunta jurídica curta, lista de 2–4 atoms, feedback imediato.

### O2 — structured answer
Pergunta escrita + abertura → tese → fundamento → ressalva → conclusão.

### O3 — guided follow-up
Repergunta prevista para corrigir/estender resposta.

### O4 — bank/edital packaging
Tempo e rubrica da banca-alvo.

### O5 — adversarial oral
Mudança de premissa, distinção, exceção, jurisprudência concorrente.

Objetiva continua em manutenção durante O1–O5.

## 6. Métrica oral
Separar:
- atom coverage;
- legal correctness;
- precision/terminology;
- answer latency;
- organization;
- handling of follow-up;
- articulation score (somente quando o estágio formal justificar).

Não confundir fluência verbal com domínio jurídico.

## 7. Regra de eficiência
Pergunta oral não precisa gerar uma aula nova. Ela puxa proposition_ids do mesmo corpus.

Se o aluno falhar por conteúdo ausente no MASTER, `MATERIAL GAP`.
Se o conteúdo estava disponível mas não foi recuperado, `LEARNER GAP`.
Se a pergunta depende de regra superada, `FRESHNESS GAP`.

## 8. Próxima coleta
- buscar malotes/padrões de oral Cebraspe de Cartório com maior proximidade temporal;
- acompanhar publicação oficial de padrões sob Res. 696 quando surgirem;
- FGV: usar somente documentos oficiais ou, secundariamente, relatos claramente rotulados como D/C para hipótese, nunca para canon;
- construir oral mini-corpus primeiro em N/R, Civil, Constitucional, Administrativo, Tributário, Empresarial e CPC, respeitando exclusão de Penal/PP/Trabalho/PTrab do oral atual.