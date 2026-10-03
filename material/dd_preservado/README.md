# Direito Penal — capítulo inicial, v3 em revisão

A autorização dada pelo usuário refere-se à operação no GitHub. **Conteúdo e formato não estão aprovados.** Esta edição substitui a v2 para avaliação; não apaga as críticas nem declara o curso pronto.

## O que foi reconstruído

A sequência agora abrange os seis assuntos do primeiro capítulo da amostra DD: conceito, características, objeto de proteção, evolução, funções e classificações (páginas 5–13). O aprofundamento sobre bens jurídicos das páginas 26–29 permanece depois do capítulo, recolhido inicialmente no HTML. A ligação entre as definições formais dos autores, omitida em dd-04, foi restaurada.

São 34 unidades numeradas e 18 perguntas autorais agrupadas, com respostas explicativas. Os destaques são escolhidos por passagem, não por substituição global de palavras. As tabelas comparam aspectos, autores, características, períodos, correntes e classificações. Normas aparecem nos assuntos correspondentes. Não foi importado conteúdo do Notion.

As três questões completas da PF 2025 já presentes na base permanecem conectadas à teoria. A referência à PC/CE 2025, questão 22, foi conferida no caderno 084_PC_CE_001_01 e no gabarito definitivo: alternativa E. Reproduz-se apenas o excerto já existente no material fornecido, com link para a questão completa. Os excertos SP/2023, RO/2022 e AM/2022 continuam identificados como pendentes de cotejo integral.

## Preservação e correções

- `fonte.json` conserva os 60 blocos originais da seleção anterior.
- `fonte_capitulo_1.json` registra a extração do capítulo inicial; o texto anterior ao título e o capítulo seguinte não entram no recorte.
- `fonte_segmentos_v3.json` divide a porção acrescentada em 40 segmentos contíguos.
- `destinos_editoriais_v3.json` aponta seus destinos; `decisoes_v3.json` justifica correções e identifica pendências.
- `historico/v2` conserva o modelo, a revisão, o construtor e a verificação anteriores.

Correções documentadas incluem a relação gênero/espécie das sanções, a Terza Scuola, a distinção entre descrição do Direito Penal do Inimigo e direito constitucional brasileiro, titularidade versus disponibilidade de bens individuais e uma impropriedade textual sobre legitimidade da criminalização. A nota sobre “modinha” foi substituída por uma descrição limitada às questões efetivamente usadas, sem inventar tendência estatística.

## Produção e conferência

Execute, nesta ordem, a partir da raiz do repositório:

```sh
python3 material/dd_preservado/reconstruir_capitulo.py
python3 material/dd_preservado/revisao_agrupada.py
python3 material/dd_preservado/construir.py
python3 material/dd_preservado/verificar.py
```

O construtor usa ReportLab e DejaVu Sans; a verificação usa PyMuPDF. As saídas HTML e PDF derivam do mesmo modelo. O PDF tem 23 páginas e 54 marcadores. Todas as páginas foram inspecionadas visualmente, com ampliação de páginas representativas. Os controles de abrir/fechar, navegação por âncora, correção C/E e impressão foram exercitados em DOM simulado; **não houve validação visual em navegador**.

Os 213 trechos declarados para exibição estão presentes nas duas saídas. Esse teste verifica integridade de renderização; **não certifica completude semântica nem eficácia pedagógica**. O mapa de origem é o instrumento de cotejo e não substitui leitura crítica.

## O que continua pendente

Revisão doutrinária aprofundada da apresentação do Direito de Intervenção, especialmente a referência a autoridade judicial; cotejo integral dos excertos de provas assinalados; restante da amostra de 58 páginas; comparação página a página com apostilas antigas; ampliação do banco por banca, ano e fase. Não há alegação de análise de todas as questões ou suficiência para gabaritar.

As versões HTML/PDF foram salvas mantendo a identidade dos arquivos existentes, agora na versão 2. Não houve publicação de site, merge ou alteração do Notion nesta rodada.
