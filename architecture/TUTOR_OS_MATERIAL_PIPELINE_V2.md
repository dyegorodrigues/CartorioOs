# Tutor OS — Material Pipeline V2

Status: **direção arquitetural vigente para a camada de materiais de estudo**.

Data: 2026-10-04.

Esta decisão refina, sem apagar, a direção registrada em `governance/GRAN_MODULAR_DIRECTION_2026-10-03.md`. Onde houver conflito na granularidade de atualização, prevalece este documento.

## 1. Objetivo

Construir um material jurídico de estudo que seja simultaneamente:

- rápido de ler e visualmente esquemático, inspirado nas virtudes de organização do PDF Sintético;
- profundo o suficiente para concursos de Delegado e carreiras jurídicas;
- atualizável sem reescrever apostilas inteiras;
- auditável por fonte e por data;
- utilizável como teoria, lei seca, revisão ativa, banco de questões e preparação oral/discursiva;
- capaz de gerar HTML, PDF e outras visões sem manter cópias divergentes do mesmo conteúdo.

A regra central é:

`fonte original -> mapa curricular -> proposições canônicas -> objetos de estudo -> renderizações`

PDF e HTML finais são produtos. Não são a base canônica.

## 2. Quatro camadas

### 2.1. Cofre de fontes — Google Drive

O Drive preserva PDFs e demais fontes recebidas **imutáveis por edição**.

Não sobrescrever DD 2025 com DD 2026. Não editar PDF comercial para "atualizá-lo". Cada edição permanece como evidência histórica independente.

O repositório público guarda apenas identificadores, metadados e localizadores suficientes para auditoria. Não guardar links privados, marcas d'água, dados pessoais nem transcrições extensas de material protegido.

### 2.2. Cérebro canônico — GitHub

O GitHub guarda conteúdo autoral do Tutor OS, contratos, mapas de cobertura, proveniência, código, validações e histórico.

Hierarquia:

`Subject -> Booklet -> Module -> Topic -> Claim`

- **Subject**: disciplina.
- **Booklet**: unidade editorial maior.
- **Module**: capítulo coerente de leitura/carregamento.
- **Topic**: assunto curricular estável.
- **Claim**: proposição, distinção, exceção ou regra que pode mudar/revisar independentemente.

O `Claim` é a unidade mínima de atualização jurídica e pedagógica.

### 2.3. Produtos gerados

Da camada canônica podem ser gerados:

- leitura web;
- PDF sintético por capítulo;
- apostila completa;
- visão de véspera;
- lei seca guiada;
- perguntas e respostas;
- flashcards;
- treino C/E;
- simulados;
- roteiro oral/discursivo.

Nenhum produto gerado deve exigir edição manual para permanecer sincronizado.

### 2.4. Estado privado do aluno

Desempenho, erros pessoais, agenda de revisão, confiança e latência não entram no repositório público.

Eles podem usar os mesmos IDs canônicos, mas pertencem a uma camada privada futura.

## 3. Por que Claim, e não apenas Topic

O modelo atual liga perguntas a tópicos e calcula a revisão usando o texto inteiro do módulo. Isso é seguro, porém excessivamente grosseiro: editar um parágrafo não relacionado pode invalidar todas as perguntas revisadas do capítulo.

No V2, uma pergunta deve depender apenas de:

- `claim_ids` que efetivamente fundamentam sua resposta;
- `law_ids` relevantes;
- metadados da própria questão oficial/adaptada.

Quando uma lei, precedente ou proposição muda, somente a cadeia dependente é marcada para revisão.

Exemplo conceitual:

`CP art. X v2 -> CLAIM-PEN-...-17 -> Q-PEN-...-41 -> render/revisão`

Não:

`qualquer edição em reading.md -> todas as questões do capítulo desatualizadas`.

## 4. Tipos de Claim

Tipos mínimos:

- `concept` — conceito;
- `rule` — regra;
- `exception` — exceção/restrição;
- `distinction` — comparação A × B;
- `classification` — classificação/lista estruturada;
- `doctrine` — posição doutrinária relevante;
- `jurisprudence` — entendimento jurisprudencial;
- `exam_pattern` — padrão recorrente de cobrança;
- `example` — exemplo/contraexemplo de ensino.

Cada Claim deve possuir ID estável, tópico principal, texto autoral/sintético, fontes/localizadores, status editorial e política de freshness.

## 5. Proveniência e DD/Gran

O Tutor OS não escolhe uma única apostila como "verdade".

Para cada microtópico:

1. Gran fornece a espinha de leitura compacta quando houver cobertura adequada.
2. DD fornece profundidade, estrutura curricular, exceções e lacunas.
3. fontes oficiais confirmam texto legal, jurisprudência e mudanças.
4. editais e questões reais medem relevância e linguagem de cobrança.
5. fontes auxiliares entram apenas quando adicionam algo identificável.

Papéis de fonte:

- `primary_study` — espinha de leitura;
- `depth_audit` — cobertura/profundidade;
- `official_authority` — autoridade normativa/jurisprudencial;
- `exam_evidence` — evidência de cobrança;
- `review_pattern` — formato útil para recuperação ativa.

### DD 2025 x 2026

O delta é semântico, não uma edição destrutiva do PDF.

Estados possíveis por Claim:

- `unchanged`;
- `new`;
- `changed`;
- `removed_from_new_edition`;
- `needs_official_check`;
- `superseded`.

Conteúdo ausente no DD 2026 não é automaticamente falso. Conteúdo presente no DD 2025 não é automaticamente atual.

## 6. Freshness Firewall

Cada Claim recebe uma classe de volatilidade:

- `stable_doctrine`;
- `legislation`;
- `jurisprudence`;
- `exam_pattern`;
- `mixed`.

Alterações em fontes disparam uma fila de impacto, não uma reescrita geral.

Regras:

1. texto literal de lei só é promovido após conferência em fonte oficial;
2. jurisprudência temporalmente sensível exige data e origem;
3. gabarito histórico de questão oficial nunca é reescrito para parecer atual;
4. se o direito vigente divergir do contexto histórico, guardar `historical_legal_context` e `current_law_note`;
5. automação pode **marcar revisão**, nunca certificar sozinha correção jurídica.

## 7. Lei seca como objeto de primeira classe

Lei seca não será um apêndice nem um segundo sistema desconectado.

`law_registry` deve evoluir para registrar, por dispositivo:

- instrumento;
- artigo/inciso/parágrafo/alínea;
- versão;
- vigência;
- texto literal;
- URL oficial;
- data da conferência;
- Claims e tópicos relacionados.

Modos derivados do mesmo dispositivo:

- leitura limpa;
- leitura com destaques autorais;
- completar lacuna;
- C/E com alteração mínima;
- identificar exceção;
- comparar artigos próximos;
- artigo -> caso;
- caso -> artigo;
- questões oficiais ligadas ao dispositivo.

Uma alteração legislativa deve atingir apenas os Claims e exercícios dependentes.

## 8. Engenharia de questões

Brainscape, Passo Estratégico e fontes semelhantes são **corpus de candidatos/padrões**, não base canônica automática.

Taxonomia de objetos:

- `learning` — ensina;
- `recall` — recupera sem pista;
- `contrast` — diferencia institutos;
- `law_literal` — cobra literalidade relevante;
- `application` — transfere para caso;
- `official` — questão oficial preservada com contexto;
- `oral`;
- `discursive`.

A sequência preferencial é:

`conceito -> distinção -> fundamento -> exemplo -> exceção -> aplicação -> produção`.

Cada item deve apontar para `topic_ids`, `claim_ids` e, quando houver, `law_ids`.

Duas auditorias passam a ser possíveis:

- Claims importantes sem questão adequada;
- questões cobrando algo que o material ainda não ensina.

Não importar baralhos inteiros por popularidade ou quantidade de cartões.

## 9. Autoria e renderização visual

O texto de estudo canônico deve ser simples de versionar e difundir. Preferência: Markdown/estrutura textual com marcação semântica, em vez de um HTML gigante editado manualmente.

Papéis visuais semânticos:

- regra/ideia nuclear;
- exceção/proibição;
- atenção/pegadinha;
- comparação;
- jurisprudência;
- lei seca;
- aprofundamento;
- questão.

O renderizador converte esses papéis em cores, caixas e tabelas no HTML/PDF. O estilo pode reproduzir a **função pedagógica** do PDF Sintético, mas não copiar sua identidade editorial.

Design tokens devem ser compartilhados pelos módulos para impedir que cada matéria vire uma colcha de retalhos.

## 10. Unidade editorial e tamanho

Não fragmentar fisicamente PDFs comerciais.

Fragmentar o conhecimento.

A unidade normal de publicação é um capítulo coerente. Um capítulo pode conter dezenas de Claims sem virar dezenas de arquivos visíveis ao aluno.

Dividir módulo somente quando houver ganho real de navegação/carregamento/edição.

## 11. Pipeline de uma apostila

Para cada booklet:

1. inventariar fontes;
2. extrair sumários e localizadores;
3. montar união de microtópicos;
4. mapear cobertura Gran/DD;
5. localizar lacunas;
6. conferir fatos voláteis em fontes oficiais;
7. redigir Claims autorais;
8. montar leitura sintética;
9. ligar lei seca;
10. ligar questões e padrões de revisão;
11. validar cobertura;
12. gerar HTML/PDF;
13. revisar juridicamente;
14. promover estado editorial.

Estados do módulo:

`planned -> mapped -> drafting -> review -> study_ready`.

`study_ready` significa que o capítulo pode ser usado para estudar. Não significa que todo o Direito futuro está congelado.

## 12. Escala para várias matérias

O motor não muda ao sair de Penal:

`subject/booklet/module/topic/claim`

O que muda são fontes, taxonomia específica e sobreposições de edital/banca/cargo.

Overlays futuros:

- Delegado estadual;
- Delegado Federal;
- carreiras jurídicas;
- banca;
- edital/ano.

O conteúdo nuclear não deve ser duplicado por concurso. O overlay seleciona profundidade, prioridade e exercícios.

## 13. Papel do Notion

Notion é opcional como painel de navegação e acompanhamento editorial.

Não é a fonte mestra do conhecimento jurídico. O dado canônico permanece versionável e auditável no GitHub.

## 14. Segurança autoral e privacidade

No repositório público:

- não incluir PDFs comerciais;
- não incluir transcrições extensas de fontes comerciais;
- não incluir dados de marca d'água;
- não incluir links privados do Drive;
- não incluir desempenho individual do aluno;
- não copiar decks completos de terceiros.

Registrar a ideia/conhecimento em redação própria, metadados e localizadores.

## 15. Vertical slice inicial

Antes de escalar para Penal inteiro, fechar `PEN-DP01-C01` ponta a ponta:

**Conceito, características, objeto, evolução, funções e divisões do Direito Penal.**

Entrega mínima:

- mapa de microtópicos;
- cobertura Gran/DD;
- Claims;
- lacunas explícitas;
- lei seca relacionada;
- conjunto progressivo de perguntas;
- questões oficiais pertinentes;
- render de estudo;
- validação de dependências/freshness.

Depois de aprovado o padrão, replicar o compilador para os demais capítulos e matérias.

## 16. Definição de sucesso

A arquitetura está funcionando quando:

- uma mudança de lei invalida só o que depende dela;
- uma nova edição DD pode ser comparada sem destruir a antiga;
- uma pergunta abre exatamente a teoria que a fundamenta;
- um erro do aluno retorna ao Claim correto;
- o mesmo conteúdo gera leitura rápida, revisão, lei seca e treino;
- o aluno consegue estudar um capítulo sem abrir cinco PDFs;
- o repositório informa o que está pronto, pendente e potencialmente desatualizado sem fingir certeza jurídica.
