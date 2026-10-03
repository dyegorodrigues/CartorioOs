# DD organizado — conceito, características e bens jurídicos

Edição v2, 03/10/2026. Corrige a mistura de numerações, a ausência de títulos visíveis e as referências editoriais repetidas apontadas pelo usuário. Ainda não foi avaliada por ele. A amostra anterior `material/penal_inicio` permanece rejeitada.

## Conteúdo e organização

O recorte conserva a substância de 60 blocos da amostra teórica DD: seções a–c, PDF pp. 5–7; antiga seção 7.1.1, pp. 26–29. Não cobre toda a apostila de 58 páginas. A fonte normalizada, com 2.478 palavras, permanece intacta em `fonte.json`.

`apresentacao.json` estabelece três assuntos e 18 unidades com uma única hierarquia. A antiga 7.1.1 foi incorporada a 3.3, depois das definições e dos limites constitucionais. As letras a/b/c e a numeração interna da origem deixaram de competir com os títulos. `destinos_editoriais.json` registra o destino dos 60 blocos, os trechos substantivos exibidos e cada prefixo editorial removido ou deslocado. Não se afirma preservação literal de cabeçalhos e metatexto: as explicações foram mantidas e organizadas; títulos, referências e comandos foram tratados como elementos de apresentação.

Sete tabelas apresentam autores, aspectos formal/material/sociológico, características, resultado jurídico/ofensividade, objeto jurídico/material, bens individuais/coletivos e coletivos reais/aparentes. Lei seca, dicas e notas de precisão têm papéis e cores distintos. As páginas de origem aparecem discretamente nos títulos; as referências ficam recolhíveis no fim.

As fontes de conteúdo são a amostra teórica DD, o cotejo dos arts. 32 e 96 com DD Legis CP e legislação oficial, CF 22, I, e as autoridades identificadas nas notas. As pp. 38 e 81 do DD Legis foram lidas para localizar os artigos; sua jurisprudência adjacente não foi incorporada em bloco. Gran serviu como referência visual. Notion não foi importado para este recorte, nem se afirma fusão completa de teoria/Legis/Juris ou revisão integral das apostilas antigas.

## Prática

`banco_questoes.json` separa três itens reais do texto de estudo: PF 2025, Delegado, itens 52/53/54, gabaritos definitivos E/C/E, confrontados com o caderno e o gabarito oficiais. Já constavam do DD; não são três questões novas acrescentadas ao material. A referência AM/2022 permanece abreviada e não entra na contagem de questões completas conferidas.

`recuperacao.json` reúne 30 perguntas autorais mais delimitadas, com resposta esperada, elementos essenciais e retorno ao subtópico. São treino de recuperação, inclusive em voz alta; não são questões oficiais de prova oral nem instrumento validado de prontidão. As dificuldades são estimativas pedagógicas. A expansão do banco por banca/ano, o cotejo de alternativas e a preparação para todas as fases continuam pendentes.

## Formatos e conferência

HTML autônomo: capítulos e lei seca recolhíveis; respostas ocultas; três itens C/E com correção; retorno ao trecho pertinente; impressão abre temporariamente o conteúdo e restaura o estado anterior. PDF estático: 11 páginas, sete tabelas e 29 marcadores de navegação. Os dois formatos derivam do mesmo modelo.

`verificar.py` conferiu o destino de todos os 60 blocos, a presença dos trechos substantivos nos dois formatos, a hierarquia, 75 vínculos internos, os três gabaritos e os limites do texto no PDF. Todas as páginas do PDF foram renderizadas e inspecionadas; tabelas, bens jurídicos, questões e recuperação também foram vistos em tamanho maior. Os controles JavaScript foram exercitados em ambiente simulado: abrir/fechar, retorno ao assunto, ausência/acerto/erro da resposta e abertura/restauração para impressão. Não houve validação visual do HTML em navegador real.

O cotejo dos sumários e a fila de revisão estão em `MAPA_SUMARIO_E_COTEJO_2026-10-03.md`. A revisão jurídica integral e a suficiência para concursos não foram estabelecidas. As provas reservadas de avaliação não foram abertas.

## Reprodução e histórico

Executar, em ordem, `organizar.py`, `revisar_perguntas.py`, `construir.py` e `verificar.py`. A construção não depende dos PDFs originais porque parte de `fonte.json`; `preparar.py` reproduz essa seleção quando eles estão disponíveis. HTML/PDF são gerados em `output/pdf/`, no workspace que contém o repositório.

`historico/` conserva o construtor, as perguntas e a verificação da v1. A hipótese do usuário continua sendo a regra: se a redação funciona, melhorar organização e apresentação sem reescrever por novidade. Alterações de conteúdo precisam de um motivo identificável e conferência da fonte.
