# ENAC 300 — Corpus Gate

Atualizado em 09/09/2026.

## Marco correto
A passagem 1 das três edições oficiais já aplicadas do ENAC está completa no `Question Intelligence Lab` como **indexação/classificação histórica**, não como corpus integralmente reconstruído:

- ENAC 2025.1: 100/100;
- ENAC 2025.2: 100/100;
- ENAC 2026.1: 100/100 canônicas;
- total lógico: **300/300 questões indexadas/classificadas na Passagem 1**.

Existem quatro registros antigos de bootstrap do ENAC 2026.1 preservados no Notion e marcados `Excluir das métricas = true`. Portanto a camada física pode conter 304 linhas, mas o corpus lógico é 300. Qualquer verificador futuro deve testar explicitamente essa reconciliação.

## O que existe hoje por item
A Passagem 1 captura, em graus variáveis:
- edição/questão;
- disciplina formal;
- banca/proveniência;
- gabarito definitivo/anulação;
- tema curto/nota de engenharia;
- família de fonte;
- mecanismos de distrator em parte substancial do corpus;
- snapshots preliminares e relações curriculares quando seguras.

## O que ainda NÃO existe de forma integral
Não chamar o estado atual de banco plenamente resolvido. Ainda faltam, em escala de 300/300:
- enunciado e alternativas em representação operacional estruturada/acessível;
- fundamento jurídico reconstruído;
- rationale oficial de recursos por item quando disponível;
- alternativa por alternativa;
- Tema/Subtema/Microtema fino;
- snapshot histórico e atual totalmente revalidados;
- demanda cognitiva e mecanismos normalizados por item;
- difficulty empírica do candidato.

O artefato oficial/PDF e a URL permanecem fonte T0. A representação textual operacional pode viver em data plane controlado; o repositório público não precisa republicar integralmente cadernos protegidos.

## Anulações oficiais conhecidas
- 2025.1: Q54, Q88, Q94;
- 2025.2: Q24;
- 2026.1: Q87, Q95.

Total: **6 questões anuladas em 300 itens históricos**. Elas permanecem para análise de tema, redação, ambiguidade e QA da banca, mas não entram como resposta jurídica válida nem acerto/erro ordinário.

## Matrix drift
As três edições históricas 2025.1, 2025.2 e 2026.1 apresentam a macrodistribuição observada:
- 60 Notarial e Registral;
- 14 Civil;
- 9 Constitucional;
- 4 Administrativo;
- 4 Tributário;
- 4 Empresarial;
- 2 Processo Civil;
- 1 Penal;
- 1 Processo Penal;
- 1 Conhecimentos Gerais.

A matriz-alvo atual ENAC 2026.2 muda para 60 N/R, 14 Civil, 8 Constitucional, 4 Administrativo, 4 Tributário, 4 Empresarial, 2 Processo Civil, 1 Penal, 1 Processo Penal, 1 Trabalho e 1 Processo do Trabalho.

Consequência: análise histórica exige normalização por oportunidade; Conhecimentos Gerais é histórico e Trabalho/Processo do Trabalho ainda carecem de histórico ENAC próprio.

## QA contra circularidade
A macrodistribuição histórica é altamente plausível e coerente com os cadernos, mas não deve ser usada como substituto da classificação.

Adicionar ao QA:
1. amostra aleatória de questões;
2. reclassificação cega a partir do artefato oficial;
3. comparação com rótulo existente;
4. registrar concordância e causas de divergência.

O objetivo não é provar o óbvio, mas testar se o pipeline realmente lê a questão em vez de reproduzir uma matriz presumida.

## Limite estatístico do ENAC 300
O corpus é muito valioso para reconstrução jurídica e atributos agregados. Ele é pequeno para inferência fina em centenas de células.

Exemplo: 180 itens N/R distribuídos sobre 138 subitens oficiais produzem em média ~1,3 item por subitem. Logo:
- ranking fino de microtema é instável;
- recorrência microtemática entre apenas três edições é esparsa;
- três edições não sustentam uma série temporal robusta de estilo;
- porcentagens agregadas de fonte, caso/literalidade, mecanismo de distrator e anulação são muito mais defensáveis que porcentagens por microtema.

Não tentar consertar baixa amostra com falsa precisão.

## O que a passagem 1 permite afirmar
Com grau adequado de segurança e sempre respeitando seu nível de anotação:
1. disciplina formal e gabarito/anulação;
2. assunto geral observado;
3. sinais qualitativos de interdisciplinaridade;
4. hipóteses de família de conhecimento e de mecanismos de distrator;
5. itens que merecem revalidação normativa prioritária.

## O que AINDA NÃO pode ser promovido
Sem QA + Passagem 2 + expansão adequada, não promover como canônico:
- ranking fino de incidência por microtema;
- `chance de cair` por microtema;
- tendência temporal quantitativa forte;
- fonte/dispositivo preciso de todos os itens;
- prioridade pedagógica individual;
- afirmação de que resposta histórica continua correta hoje.

## Nova função da Passagem 2
A Passagem 2 deixa de ser um projeto de estatística impossível e passa a ter como produto principal **Reconstruction Cards juridicamente úteis**.

Para cada item relevante, progressivamente:
- comando e fatos decisivos;
- Tema/Subtema/Microtema;
- norma/dispositivo decisivo;
- jurisprudência/ato CNJ quando decisivo;
- rationale de recurso oficial quando disponível;
- fundamento da correta;
- fundamento dos distratores;
- mecanismo de erro;
- snapshot histórico;
- snapshot atual;
- transferência para objetiva/discursiva/prática/oral.

Não é obrigatório reconstruir as 300 antes de o candidato começar a estudar. A reconstrução pode ser priorizada pelos nós que entram na trilha e, ao mesmo tempo, alimentar a meta-análise.

## Dois estimadores diferentes
### Domain Incidence Model
Pergunta: `o que concursos de cartório cobram?`

Usa ENAC + concursos estaduais multibanca com proveniência/pesos. É a fonte adequada para aumentar poder de cobertura temática.

### Bank Style Model
Pergunta: `como a banca X constrói avaliação?`

Usa apenas corpus da banca/janela/família/fase pertinentes e mede atributos agregados de estilo. Não usa outras bancas para aumentar artificialmente amostra de FGV.

## Priors adicionais quando frequência é esparsa
A prioridade de estudo não depende apenas de frequência histórica. Considerar:
- peso oficial da matriz;
- superfície explícita do edital;
- centralidade/dependência;
- transferência entre fases;
- incidência de domínio em corpus ampliado;
- target-bank style evidence;
- volatilidade normativa, sem assumir que `norma nova = cairá`;
- dificuldade e esquecimento individuais.

## Freshness gate
Nenhum item histórico migra automaticamente para MASTER. Fluxo:
`artefato/gabarito histórico → fundamento histórico → fonte atual → alteração → snapshot atual → material`.

## Próximo marco
1. aplicar QA de amostra cega;
2. iniciar Reconstruction Cards junto dos primeiros nós de estudo;
3. formar corpus operacional com enunciado/alternativas acessíveis sem republicação desnecessária;
4. ampliar corpus estadual/multibanca para incidência de domínio;
5. publicar meta-análises com nível de confiança explícito e sem pseudo-precisão.
