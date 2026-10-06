# HANDOFF CRÍTICO — NOVA CONVERSA — 2026-10-06
**Projeto:** IA Educacional Tutor OS / Legal Tutor OS  
**Branch ativa:** `chatgpt/legal-tutor-os-integrated-2026-10-05`  
**IMPORTANTE:** `dyegorodrigues/delegado-os` é READ-ONLY para este projeto. Não criar commits/PRs nele.

---

## 0. INSTRUÇÃO PARA A PRÓXIMA CONVERSA
Retomar daqui sem reexplicar toda a arquitetura.

Primeira tarefa da próxima conversa:
**responder integralmente a dúvida do usuário sobre integrar Lei Seca + jurisprudência + súmulas + questões por artigo/alternativa ao mesmo banco de questões, sem criar overengineering, preservando todo o fio anterior.**

Depois:
1. formalizar a camada de “Lei Seca Ativa / Normative Graph”;
2. mapear DD LEGIS e materiais correlatos do Drive Russgod;
3. continuar C01 V2 sem mexer em `delegado-os`;
4. aprofundar mineração card-a-card de Brainscape/Passo/MRC;
5. construir banco de questões e corpus oral/discursivo.

---

# 1. ÚLTIMA DÚVIDA DO USUÁRIO, AINDA A RESPONDER COMPLETAMENTE

O usuário lembrou dos ecossistemas:
- Decorando Lei Seca;
- Estudo Lei Seca;
- possível concorrente “ALS Estudo Lei Seca” (nome ainda não confirmado);
- DD LEGIS / Mapa da Lei Seca / cadernos de lei seca no Google Drive.

Ele perguntou se é inteligente, durante a mineração de questões:
- registrar o artigo de lei relacionado à questão;
- se possível, registrar artigo/inciso/parágrafo por **alternativa**;
- também ligar súmulas, julgados, temas, jurisprudência e informativos;
- permitir um modo de estudo “lei seca ativa”, parecido com Decorando Lei Seca:
  - abrir artigo;
  - resolver C/E ou questões diretamente ligadas ao dispositivo;
  - começar por questões fáceis e evoluir;
  - ver fundamento legal/jurisprudencial;
  - cruzar por banca/carreira/dificuldade;
  - revisar literalidade, exceções, prazos, competências e pegadinhas.

A preocupação dele:
**isso é brilhante e útil ou vai criar engenharia demais e travar tudo?**

Resposta já amadurecida internamente:
**é útil e NÃO precisa virar overengineering se for uma camada relacional do mesmo corpus, não um banco paralelo.**
Detalhes no item 8 deste handoff.

---

# 2. ESTADO DO PROJETO PRINCIPAL

## Repositório de trabalho
`dyegorodrigues/CartorioOs`

## Branch ativa
`chatgpt/legal-tutor-os-integrated-2026-10-05`

## Arquivos centrais
- `START_HERE_LEGAL_TUTOR_OS.md`
- `governance/CURRENT_SESSION_POINTER.json`
- `architecture/MODULE_FACTORY_V1.md`
- `governance/VERSIONING_FRESHNESS_POLICY_V1.md`
- `architecture/STUDENT_MATERIAL_FORMAT_V2.md`
- `architecture/BRAINSCAPE_PASSO_INTEGRATION_V2.md`
- `architecture/COGNITIVE_RECONNECTIONS_V1.md`
- `governance/EXTERNAL_COMPARATOR_DELEGADO_OS.md`

## Estado editorial C01
O MASTER V1 do Tutor OS foi **rejeitado como material principal de aluno**.
Motivos:
- conciso demais;
- parecia documentação de engenharia;
- perguntas estavam fora da experiência;
- tabelas insuficientemente densas;
- aliases e palavras-chave mal apresentados;
- usuário e colegas disseram que não conseguiriam aprender por ele.

O backend continua válido:
- Claims;
- auditorias;
- source map;
- correções jurídicas;
- corpus de prova.

---

# 3. REPOSITÓRIO DO CLAUDE / COMPARADOR EXTERNO

## Repo
`dyegorodrigues/delegado-os`

## Política
**READ-ONLY.**
O usuário explicitamente pediu para NÃO modificar.

Pode:
- ler;
- comparar;
- extrair ideias;
- clonar mentalmente arquitetura;
- reproduzir soluções no Tutor OS.

Não pode:
- commit;
- PR;
- editar;
- sincronizar automaticamente.

## Estado observado
- `main` contém PR #1 mergeado;
- DP-01 Cap. 1 v1.1;
- ~49 páginas;
- 113 perguntas progressivas;
- 12 perguntas de revisão;
- 6 questões oficiais comentadas;
- 17 itens C/E autorais;
- renderer HTML/CSS/Python;
- CSV/banco;
- regras editoriais e workflow.

## Veredito
A v1.1 está **à frente visualmente e pedagogicamente** do nosso protótipo.
Pontos fortes:
- “Em 1 minuto”;
- tabelas que carregam teoria;
- destaques;
- callouts;
- perguntas integradas;
- fechamento multicamada;
- renderer reaproveitável como referência.

Mas NÃO é autoridade jurídica/canônica.
Problemas detectados:
- risco de crescimento enciclopédico;
- “todo DD entra” pode sobrecarregar a superfície;
- 113 perguntas podem ser demais se usadas como revisão;
- Brainscape ainda analisado mais por pack do que card-a-card;
- corpus de questões ainda pequeno para inferir incidência robusta;
- oral/discursiva ainda praticamente não analisadas;
- alguns pontos precisam auditoria/rebaixamento.

Auditoria:
`research/validation/DELEGADO_OS_V11_AUDIT_2026-10-06.md`

---

# 4. NOVA DIREÇÃO PEDAGÓGICA

## Não é:
“apostila resumida + flashcards”.

## É:
**DD como coverage/depth floor + Gran/Claude como gramática visual + Brainscape/Passo como engenharia de recuperação + MRC/Trutas/OAB como C/E/aplicação + provas reais como QA + fontes oficiais como autoridade.**

## Superfície de estudo desejada
Por tópico:
1. EM 1 MINUTO
2. explicação suficiente
3. tabela estratégica de alta densidade
4. ATENÇÃO / NÃO CONFUNDA / CAIU / RECONEXÃO
5. perguntas progressivas
6. resposta explicativa
7. resposta-relâmpago quando útil

Fechamento:
1. mapa ultrarrápido
2. perguntas-mãe estilo Passo
3. EXAM Lab
4. C/E
5. oral/discursiva
6. revisão adaptativa futura

---

# 5. ÂNCORAS DE RECONEXÃO

Arquivo:
`architecture/COGNITIVE_RECONNECTIONS_V1.md`

Técnica:
parênteses/travessões/microbox para retomar:
- conceito;
- teoria;
- artigo;
- autor;
- exceção;
- exemplo;
- tema futuro.

Exemplo mental:
“bem jurídico” é ensinado numa home pedagógica e reaparece em:
- Roxin;
- fragmentariedade;
- ofensividade;
- tipicidade material;
- teoria do crime.

Não reensinar tudo; reconectar.

---

# 6. BRAINSCAPE / PASSO / MRC

## Brainscape
Packs fortes já catalogados:
- Mateus Carvalho
- Júlio Carlos
- Jônatas Romero
- Sérgio Henrique Santana
- Trutas 2025
- OAB/JurisCards
- outros

### Funções diferentes
- Mateus/Jônatas: sequência conceitual;
- Sérgio: profundidade vertical;
- Júlio: quick-answer/turbo;
- Trutas/OAB: C/E, literalidade, aplicação;
- outros: microconfusões e cobertura.

### Regra
Não escolher “o melhor deck”.
Mineração deve ser card-a-card:
`card → microtópico → Claim → qualidade da pergunta → qualidade da resposta → prova real → duplicidade → decisão`

Estados:
- KEEP_CORE
- KEEP_ADVANCED
- MERGE_OR_CHILD
- REWRITE_AUDIT
- DEFER_OTHER_NODE
- PENDING_EVIDENCE
- REJECT

Arquivo:
`architecture/BRAINSCAPE_PASSO_INTEGRATION_V2.md`

## MRC
“MRC” = decks .apkg anexados pelo usuário:
- Direito Penal
- Constitucional
- Administrativo

Não são autoridade.
Úteis sobretudo para:
- C/E;
- comentários curtos;
- discriminação;
- aplicação.

## Trutas
Sim, Trutas é Brainscape.

---

# 7. BANCO DE QUESTÕES

Arquitetura já definida:
- EXAM CORPUS
- LEARNING PROMPT CORPUS
- ANSWER PATTERN CORPUS

Cada questão oficial deve ter:
- banca;
- órgão/cargo;
- carreira;
- ano/data;
- fase;
- número;
- dificuldade;
- tema/tópico/subtópico/microtópico;
- Claim(s);
- mecanismo de cobrança;
- mecanismo de distrator;
- gabarito preliminar/definitivo/anulação;
- snapshot histórico;
- estado jurídico atual;
- comentário Tutor OS;
- comentários de terceiros separados.

## Censo Delegado
Objetivo:
todas as provas localizáveis de Delegado, estadual e PF, em todas as fases disponíveis.

Não limitar a 2023–2026.
Recentes primeiro, histórico depois.

Arquivo:
`research/exams/DELEGADO_EXAM_CENSUS_PROTOCOL_2026-10-05.md`

## Oral/discursiva
Ainda precisa crescer muito.
Nova arquitetura desejada:
- pergunta real;
- concurso/UF;
- banca/comissão;
- ano/fase;
- literalidade ou grau de reconstrução;
- follow-ups;
- resposta oral natural;
- resposta 30s/90s;
- rubrica;
- erros comuns;
- microtópico/Claims.

Não inventar “questão oral real”.

---

# 8. NOVA CAMADA A CRIAR: LEI SECA ATIVA / NORMATIVE GRAPH

## Resposta à última dúvida
**Sim, é uma ótima ideia.**
Não precisa complicar o sistema se for modelada como RELAÇÕES do mesmo banco.

### NÃO criar:
- um banco separado de “questões de lei seca”;
- cópias duplicadas da questão;
- outro conteúdo canônico paralelo.

### Criar:
um grafo normativo:

`question/item/alternative → Claim → provision → precedent/súmula/theme/informativo`

## Estrutura recomendada

### Provision
- instrument_id
- article
- paragraph
- item/inciso
- alínea
- text_snapshot
- version_from / version_to
- official_source
- checked_at

### Precedent/Jurisprudence
- tribunal
- case/theme/súmula
- thesis
- date
- status
- official_source

### Question link
No nível da questão:
- provision_ids
- precedent_ids
- jurisprudence_ids

No nível da alternativa:
- option_id
- claim_ids
- provision_ids
- precedent_ids
- error_mechanism

**Alternativa por alternativa é útil**, principalmente em múltipla escolha, porque cada alternativa pode testar dispositivo/entendimento diferente.

## Porém, para não travar:
não exigir mapeamento profundo de TODA alternativa na ingestão inicial.

Pipeline:
1. ingestão da questão;
2. mapeamento obrigatório do tema/microtópico;
3. mapeamento normativo da questão quando evidente;
4. alternativa-level somente:
   - questão-chave;
   - prova prioritária;
   - alternativa com norma/jurisprudência diferente;
   - item usado no material;
   - item com bug/controvérsia.

Isso dá 80% do valor sem 500% do custo.

## Produto derivado
Com essas relações, gerar modo:

### LEI SECA ATIVA
Abra:
**CP, art. X**

Veja:
- texto vigente;
- alterações;
- palavras/expressões cobradas;
- questões fáceis → médias → difíceis;
- C/E;
- bancos/cargos;
- pegadinhas;
- jurisprudência/súmulas vinculadas;
- taxa de erro pessoal;
- última revisão.

É o equivalente próprio ao Vade Mecum de Questões.

## Pesquisa web feita em 06/10/2026
Decorando Lei Seca confirma publicamente:
- questões diretamente ligadas a artigo/parágrafo/inciso;
- questões reais e inéditas;
- gabarito com fundamento no artigo destacado;
- jurisprudência/súmulas;
- Raio-X por banca;
- prioridade de artigos.

Estudo Lei Seca anuncia:
- +500 legislações;
- +35 mil questões;
- +1.100 julgados;
- +3.000 súmulas;
- leitura de lei + jurisprudência + questões na mesma tela.

“ALS Estudo Lei Seca” ainda NÃO foi localizado com segurança pelo nome informado. Não inventar.

## Importante
Esse modo se torna MUITO mais relevante:
- aplicação da lei penal;
- teoria do crime com artigos;
- parte especial;
- legislação especial;
- Constitucional/Administrativo etc.

No C01 conceitual ele existe, mas tem poucos anchors:
- DL 3.914/41 art. 1º
- CP arts. 97-98
- CF art. 22

---

# 9. DD LEGIS / DRIVE

O Tutor OS TEM acesso à conta Russgod e ao “Compartilhados comigo”.

Busca confirmada em 06/10/2026:
- pasta **DD LEGIS**
- **D_CP Comentado completo (atualizado até 08.12.25)**
- **Código Penal (CP)**
- **MAPA DA LEI SECA - DEDICAÇÃO DELTA**
- **Caderno de Lei Seca**
- **EXTENSIVA DELTA E MP - CADERNO DE LEI SECA**
- IURIS Penal
- DD 2025/2026
- outros materiais.

Isso é vantagem real sobre o Claude, que disse não ter acesso equivalente à Russgod/compartilhados.

## Papel do DD LEGIS
Não será tratado como autoridade final.
Função:
- detectar artigos destacados;
- marcações pedagógicas;
- incidência presumida;
- comentários;
- conexões;
- estrutura de leitura.

Fonte final:
Planalto / legislação oficial / STF / STJ etc.

---

# 10. NOTION

Usuário mencionou backup e tabelas ultra densas.
Claude encontrou:
- Biblioteca Mestre de Penal;
- Bloco 01 ~2.200 linhas;
- matriz de microtópicos;
- lacuna com Direito Romano, Germânico e Canônico.

Tutor OS deve usar Notion como:
- fonte histórica de ideias;
- referência de tabela/organização;
- detector de lacunas.

Não assumir que tudo ali é correto ou atual.

---

# 11. QUESTÃO CENTRAL DE PRODUTO

Usuário quer UM MATERIAL apenas:
- gostoso;
- fluido;
- visual;
- eficiente;
- suficiente para reaprender;
- capaz de resolver objetiva fácil→muito difícil;
- com lei seca;
- jurisprudência;
- questões;
- revisão;
- oral;
- discursiva;
- sem virar enciclopédia.

A regra crítica:
**coverage floor ≠ attention priority.**

Tudo relevante precisa ser decidido/rastreável.
Nem tudo merece o mesmo peso na primeira passagem.

---

# 12. PRÓXIMOS PASSOS RECOMENDADOS

1. Criar `architecture/NORMATIVE_GRAPH_AND_ACTIVE_LAW_V1.md`.
2. Estender schema de question/option com vínculos normativos.
3. Criar registry de provisions/jurisprudence com versionamento.
4. Mapear DD LEGIS Penal como fonte secundária.
5. Construir piloto de Lei Seca Ativa em um artigo simples.
6. Continuar mineração Brainscape card-a-card.
7. Continuar Censo Delegado.
8. Construir corpus oral/discursivo.
9. Criar matriz de decisão C01:
   `MANTER | CORRIGIR | REBAIXAR | MOVER | EXPANDIR | TESTAR`
   sobre v1.1 Claude + nosso backend.
10. Só depois reconstruir/renderizar C01 completo.

---

# 13. NÃO FAZER

- não modificar `delegado-os`;
- não fundir repos sem autorização;
- não copiar decks comerciais integralmente para repo;
- não assumir que DD é 100% completo/atual;
- não assumir que Gran é suficiente;
- não transformar tudo em card;
- não obrigar mapeamento alternativa-level para milhões de questões logo no primeiro passe;
- não deixar lei seca/jurisprudência como apêndice separado;
- não usar autor raro como enfeite;
- não declarar corpus “completo da internet”.

---

# 14. PROMPT CURTO PARA COLAR NO NOVO CHAT

“Retome o Legal Tutor OS a partir do handoff `governance/HANDOFF_NEXT_CHAT_2026-10-06.md` na branch `chatgpt/legal-tutor-os-integrated-2026-10-05` do repo `dyegorodrigues/CartorioOs`. O repo `dyegorodrigues/delegado-os` é READ-ONLY. Primeiro responda integralmente minha última dúvida sobre integrar Decorando Lei Seca / Estudo Lei Seca / DD Legis ao banco de questões com artigo/inciso/parágrafo por questão e, quando útil, por alternativa, além de súmulas/jurisprudência, sem criar overengineering. Depois continue exatamente os próximos passos registrados no handoff, sem reinventar a arquitetura.”
