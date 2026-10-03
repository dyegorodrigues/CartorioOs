# DD preservado - conceito, características e bens jurídicos

Edição de trabalho em 03/10/2026. O usuário ainda não avaliou este resultado. A amostra anterior `material/penal_inicio` continua rejeitada.

## Trabalho efetivamente executado

- Seleção literal da amostra DD fornecida: seções a-c, páginas 5-7; seção 7.1.1, páginas 26-29. São 60 blocos e 2.478 palavras da fonte. Espaços, quebras de linha e travessões da extração foram normalizados; nenhum bloco selecionado foi eliminado ou reescrito.
- Passagens sobre bens jurídicos reunidas na mesma seção. Conservam-se as repetições nesta primeira edição para verificar a preservação antes de qualquer eventual redução.
- Tabela original reconstruída sem eliminar células, autores e definições mantidos; enunciados e comentários do DD deslocados para exercícios sem perda de texto.
- CP 32/96 e CF 22, I incorporados nos pontos pertinentes e conferidos na redação oficial. Não há súmula ou precedente colocado nesta introdução apenas para ilustrar integração.
- PF 2025 itens 52, 53 e 54 já existentes no DD, confrontados com o caderno oficial 106_PF_001_01 e o gabarito definitivo de Cargo 1, Delegado. Não são questões novas acrescidas ao DD. Referência AM/2022 continua abreviada e não é contada como questão completa conferida.
- 18 perguntas autorais de recuperação, com dificuldade pedagógica estimada e vínculo com blocos de conteúdo.
- HTML autônomo: leitura contínua, assuntos recolhíveis, respostas ocultas, retorno às explicações, impressão com abertura temporária de todo o conteúdo. PDF de 10 páginas: 7 de conteúdo/questões e 3 de recuperação/fontes. PDF e HTML derivam do mesmo modelo.

## Revisão e limites

As notas sobre terceira via, penas diferentes de prisão, sentido de “finalista” e atribuição doutrinária estão separadas do texto-base. A precisão de leitura do item 52 registra a simplificação histórica do comentário do DD, sem substituir esse comentário silenciosamente. A conferência doutrinária integral permanece pendente; não se afirma atualização integral da apostila, cobertura suficiente de concursos ou conclusão do banco de questões. Provas reservadas de avaliação não foram abertas.

`verificar.py` conferiu os 60 blocos literalmente no HTML (com recolocação do gabarito) e todos os trechos no PDF; conferiu 65 links internos e ausência de dados pessoais extraídos da marca d'água. O PDF foi renderizado e todas as páginas foram inspecionadas. Não houve teste visual do HTML em navegador real; a sintaxe do JavaScript e a estrutura do documento foram verificadas.

## Reprodução

`fonte.json` contém a seleção de texto fornecida pelo usuário e sua origem. `recuperacao.json` contém apenas perguntas autorais. `construir.py` gera os dois formatos em `output/pdf/` no workspace que contém o repositório. `verificar.py` confere o resultado.

`preparar.py` reproduz a seleção a partir de `dd_review_2026/dd_penal.json` e `dd_penal.pdf`, quando os originais estiverem disponíveis. A construção cotidiana não depende desses PDFs, pois usa `fonte.json`.

A hipótese expressa do usuário governa a continuação: se uma apostila estivesse perfeita, a redação poderia permanecer inteira, com mudanças exclusivamente de organização e apresentação. Não reescrever para novidade. Alterações futuras precisam de motivo identificável e conferência do destino de todos os elementos úteis.
