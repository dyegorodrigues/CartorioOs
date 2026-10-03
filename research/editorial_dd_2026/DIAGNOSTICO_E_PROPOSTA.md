# Diagnóstico das amostras DD 2026 G e proposta de material integrado

Data: 02/10/2026. Referência principal: Dedicação Delta. Preferência visual complementar: Gran PDF Sintético. Uso pessoal, impressão e preparação para várias carreiras. As páginas abaixo são as páginas do arquivo PDF, não necessariamente o número impresso no rodapé.

## Resultado e escopo real

Foi confirmado acesso às duas conexões do Drive. A pasta **Dedicação Delta 2026 G**, na conta Fentanes, contém nesta fotografia **39 PDFs e seis subpastas**: teoria (9), DD Legis (7), DD Juris (7), DD Súmulas (4), revisão final PR (7), Gran (2), além de três PDFs na raiz. Todas essas pastas foram listadas. Isso não significa leitura de 39 apostilas ou completude do curso.

Pela conta Russgod foram abertas as pastas compartilhadas **Dedicação Delta - Extensivo 2025** e **Mapa da Lei Seca - Delegado de Polícia - Dedicação 2025**, incluindo os arquivos antigos de Penal utilizados na comparação. As 30 pastas da trilha antiga foram localizadas; os respectivos conteúdos não foram todos lidos. A árvore SEMANAS do Mapa retornou 15 pastas nesta consulta; não assumir que isso represente o curso integral.

| Material | Extensão | Trabalho realizado nesta rodada |
|---|---:|---|
| DD teoria: Noções iniciais e princípios de Penal | 58 páginas | Leitura editorial integral do conteúdo; inspeção visual de páginas selecionadas |
| Gran: Princípios | 11 páginas | Leitura integral; inspeção visual selecionada |
| Gran: Direito Penal, Criminologia e Política Criminal | 23 páginas | Leitura integral; inspeção visual selecionada |
| DD Juris: Insignificância | 15 páginas | Leitura integral; conferência pontual de fonte oficial e visual |
| DD Súmulas: Penal | 13 páginas | Leitura de todo o conteúdo das páginas 3-13; sem validação jurídica integral |
| Orientações gerais e metas da semana 1 | 6 + 2 páginas | Leitura do funcionamento proposto pelo curso |
| DD Legis: Código Penal novo | 282 páginas | Extração integral; leitura das páginas 1-8, com cotejo completo do bloco do art. 1º, páginas 3-4 |
| Teoria antiga / CP antigo / Mapa semana 1 | 57 / 265 / 155 páginas | Comparação amostral: teoria 11-15, CP 3-4, Mapa 4-9; restante apenas extraído |

Inventário, IDs, hashes e páginas efetivamente lidas estão nos arquivos `INVENTORY.json` e `READING_LEDGER.json`. Textos e PDFs originais permanecem fora do repositório. A biblioteca completa de questões do DD e suas funcionalidades autenticadas não foram inspecionadas. Outros materiais soltos, Memorex/Iuris, o original do Notion e a versão exata do verticalizado do CÉREBRO do Magistrar não receberam nova leitura nesta rodada.

Uma deduplicação útil: o texto das 58 páginas da nova cópia de teoria coincide com a amostra DD já disponível localmente, após normalizar espaços e o rodapé individual. Os arquivos binários são diferentes. A leitura anterior tinha sido amostral; nesta rodada o conteúdo foi percorrido integralmente. A apostila antiga de 57 páginas do Extensivo 2025 é outro documento.

## O que a comparação mostrou

**O DD oferece o desenvolvimento; o Gran oferece soluções visuais aproveitáveis.** Isso é uma conclusão sobre estas amostras, não uma classificação geral dos cursos.

O DD teoria começa com artigos e súmulas relacionados (p. 4), desenvolve conceitos, distingue correntes, usa quadros e exemplos, e intercala apontamentos de prova. Há questões completas com alternativas nas páginas 35, 50 e 56; uma discursiva com padrão de resposta nas páginas 33-34; e referência à prova oral na página 17. Muitas outras inserções já revelam a resposta no próprio bloco. A busca textual encontrou 41 ocorrências de “caiu”, número que **não equivale a 41 questões completas, independentes ou auditadas**.

Portanto, seria incorreto dizer que a apostila não tem questões. A lacuna é outra: falta, para o objetivo do usuário, uma sequência suficiente de exercícios independentes, comentários de todas as alternativas relevantes e critérios de resposta oral/discursiva. As Orientações gerais, p. 3, encaminham o treinamento diário para o banco externo. Os dois PDFs do Gran também terminam encaminhando o aluno à plataforma de questões (Princípios, p. 10; Ciências, p. 20). Os arquivos recebidos não substituem automaticamente esses bancos.

O DD Legis não é apenas lei seca: junto do art. 1º há doutrina, quadros comparativos e perguntas, nas páginas 3-4. Esses elementos se sobrepõem à teoria, p. 24-25 e 50-51. O Mapa antigo também faz essa integração, p. 6-9. A solução deve reaproveitar essa lógica e reduzir a necessidade de procurar a mesma explicação em arquivos distintos.

O DD Juris distingue aplicação, rejeição e divergências. Sua p. 5 reproduz a mesma referência equivocada presente na teoria, p. 36. Essa repetição mostra por que duas apostilas concordantes não são duas confirmações independentes. É necessário conferir a origem comum.

O Gran explicita a convenção de cores na apresentação: azul para afirmações importantes, vermelho para exceções/restrições e marca-texto para destaques. Nas páginas 6-10 de Princípios, quadros curtos facilitam a localização. Em Ciências, há tabela comparativa (p. 7), blocos de retomada e prosa desenvolvida. Nem todo conteúdo fica melhor dentro de tabelas: passagens argumentativas precisam de texto contínuo. Os nomes dos arquivos indicam fevereiro e agosto de 2024; isso não certifica atualização até 2026.

## Correções e pontos de atenção encontrados

| ID | Onde | Achado | Tratamento |
|---|---|---|---|
| E01 | DD teoria p. 36 e DD Juris p. 5 | A tese sobre restituição do bem furtado é vinculada ao RMS 68.504/SC e ao Tema 1208 | **Erro de referência confirmado.** Vincular ao Tema 1205, REsp 2.062.375/AL e 2.062.095/AL, rel. Sebastião Reis Júnior. O RMS citado trata de credenciamento de leiloeiros |
| E02 | DD CP novo p. 4; CP antigo p. 4; Mapa antigo p. 9 | O exemplo de ato obsceno remete ao art. 233 do CPP | **Erro de diploma confirmado.** O dispositivo pertinente é o art. 233 do Código Penal. Reaparece em fontes antigas e novas |
| E03 | Gran Princípios p. 10 | Contrabando é apresentado na lista de não aplicação, com ressalva para medicamentos, sem a hipótese de cigarros do Tema 1143 | **Lacuna de atualização confirmada no recorte.** Acrescentar o precedente, seus requisitos, exceção por reiteração e alcance temporal; não transformar a regra em automatismo |
| E04 | DD teoria p. 20-21 | Primeiro afirma ausência de autor específico para quarta/quinta velocidades; depois atribui a quarta a Daniel Pastor | Inconsistência interna de atribuição. Cotejar fonte doutrinária antes de reescrever como conhecimento consolidado |
| E05 | DD teoria p. 50-51 | Anuncia dois fundamentos da reserva legal e enumera três | Ajuste editorial de contagem; manter distinção jurídico/político/democrático |
| E06 | DD teoria p. 32-34 | Conflito aparente de normas é desenvolvido dentro de subsidiariedade/intervenção mínima | Reorganização proposta: distinguir os dois usos de “subsidiariedade”; introduzir a ponte e desenvolver conflito de normas em bloco próprio |
| E07 | Gran Ciências p. 12 | Comentário sobre decisões do STF e “interesses de toda a sociedade” aparece em destaque | Evitar converter avaliação editorial ampla em regra jurídica ou critério de gabarito |

E01-E03 foram confrontados com fontes primárias listadas ao fim. E04 e outras formulações doutrinárias continuam pendentes; não são corrigidas por intuição. Nenhum dos cursos foi declarado integralmente desatualizado ou incorreto.

## Estrutura proposta para o material

**Um caderno principal por unidade de assunto, suficientemente desenvolvido para aprender, com lei, doutrina, jurisprudência e prática integradas.** A ordem do código continua disponível em um índice de dispositivos. O percurso de aprendizagem pode seguir pré-requisitos. Assim, a mesma informação serve à leitura inicial, à revisão da lei e às perguntas sem manutenção de três versões independentes.

O desenvolvimento deve alternar explicação fluente, dispositivos pertinentes, exemplos, contrastes e perguntas. Não será imposto um formulário de sete caixas a toda página. Os parênteses de retomada serão breves e úteis, explicando a conexão que o aluno precisa recuperar; não apenas remetendo a códigos internos.

Exemplo de integração já mapeado: o bloco de legalidade reúne DD teoria p. 24-25 e 50-52, DD Legis p. 3-4 e o texto oficial do CP. Uma explicação desenvolve os sentidos de lei e as quatro garantias; uma tabela fixa as diferenças; exercícios testam costumes, analogia e temporalidade. O índice por artigo conduz ao mesmo bloco. Para insignificância, combinar teoria p. 34-48, DD Juris p. 4-15 e súmulas pertinentes, distinguindo regra, requisitos, situação fática, tribunal e exceções.

### Treino incorporado

- Recuperação curta: pergunta específica antes da resposta, com explicação suficiente para corrigir a confusão.
- Questão real: banca, carreira, ano, fase, identificação do caderno, fonte e situação do gabarito. Comentar a razão de cada alternativa; destacar a palavra que muda a resposta quando relevante.
- Progressão: identificação simples, distinção próxima, caso de aplicação e integração de assuntos. Dificuldade estimada pelo conteúdo deve ficar distinta da dificuldade observada no desempenho do usuário.
- Discursiva e oral: começar com respostas curtas desde o início; avançar para fundamentação, objeções e síntese. Usar espelho/rubrica oficial quando existente.
- Peça prática: entrar quando os pressupostos materiais e processuais estiverem cobertos; não inserir peça descontextualizada em toda unidade.
- Questões antigas desde 2010: conservar a redação e o gabarito histórico; registrar separadamente o direito atual. Adaptação recebe outra identificação. Anulada/ambígua fica marcada e não compõe medida ingênua de domínio.

Os cartões podem ser extraídos das mesmas perguntas, com contexto suficiente. Não há evidência produzida aqui de que uma sequência exclusivamente por questões seja o melhor método para este usuário. A proposta combina explicação, tentativa, feedback e nova recuperação; o desempenho orientará os ajustes.

### Visual e impressão

O nome da preferência apresentada pelo usuário é **diagramação ou projeto gráfico editorial**; gramatura é a espessura/massa do papel. Proposta inicial: A4, texto em uma coluna, corpo de aproximadamente 10,5-11 pt, entrelinha confortável e tabelas de comparação curtas. Usar azul escuro para estrutura/regra; vinho para ressalvas; amarelo suave para ponto de memória; verde discreto para exemplo. A cor acompanha rótulos, para continuar compreensível em impressão cinza. Evitar fundos de página inteiros, excesso de negrito e tabelas quebradas sem cabeçalho.

Perguntas de treino e respostas terão distância de leitura suficiente no impresso; comentários podem ocupar a página seguinte ou seção final da unidade. A proposta visual anexa é um ensaio, não uma unidade curricular liberada. Sua avaliação de conforto visual permanece necessária antes de aplicar o padrão em centenas de páginas.

## Papel das ferramentas

| Superfície | Função proposta |
|---|---|
| PDF | Material principal para estudar, imprimir, anotar e levar offline; versão/data visíveis |
| Google Drive | Originais, referências e futuras edições para consulta; conservar a organização montada pelo usuário |
| GitHub | Fonte editável do projeto, relações entre assuntos, evidências, correções e histórico. PDFs comerciais não entram no repositório |
| Notion | Página simples de entrada para unidade, próximas revisões, dúvidas/erros e links. Evitar exigir que o usuário administre uma base complexa |
| GitHub Actions | Etapa posterior: verificar referências/IDs e gerar arquivos de modo reproduzível. Conferência automática não declara validade jurídica |

Os grafos ficam na estrutura interna: conceito, artigo, precedente, questão, pré-requisito e carreira. A navegação precisa servir à leitura; o usuário não precisa estudar um grafo. Não há decisão de carreira: Delegado estadual/PF, MP estadual/federal, cartórios/ENAC e demais carreiras continuam como recortes sobre a base comum. Uma questão de Delegado não demonstra suficiência para MP ou cartórios.

## Execução e conclusão de cada etapa

1. **Concluído nesta rodada:** acesso confirmado, inventário da pasta nova, leitura editorial principal, comparação amostral com o acervo antigo, três achados confrontados com fontes oficiais e mapa inicial de integração.
2. **Próximo trabalho de conteúdo:** associar as questões já selecionadas às passagens das apostilas; concluir as lacunas recentes de MP/PF e demais famílias previstas no handoff; resolver conflitos e validar as proposições que entrarão na unidade piloto. Não reiniciar uma coleta indiscriminada de PDFs antigos.
3. **Unidade piloto:** só liberar após as etapas de cobertura, leitura semântica, conferência jurídica, reconciliação do mapa e validação reservada exigidas pelo handoff. A unidade deverá permitir aprender, recuperar e aplicar, com teste de leitura/impressão.
4. **Expansão:** repetir o padrão aprovado por unidade; aproveitar cada material antigo por passagem; incorporar futuras adições do DD/Juris pelo inventário e pela versão. Publicar errata/suplemento para evitar reimpressão integral quando possível.

O estado curricular continua `NOT_READY_TO_RENDER`. O diagnóstico editorial está concluído no recorte declarado. Não foram executados novos testes em questões reservadas, nem produzida uma apostila completa validada. A infraestrutura existente continua sendo aproveitada; construir uma nova plataforma inteira não é requisito para começar a obter material utilizável.

## Fontes primárias das conferências

- STJ, [Tema 1205](https://processo.stj.jus.br/repetitivos/temas_repetitivos/pesquisa.jsp?cod_tema_final=1205&cod_tema_inicial=1205&novaConsulta=true&tipo_pesquisa=T), consulta em 02/10/2026: restituição e insignificância; julgados em 24/10/2023.
- STJ, [RMS 68.504/SC, inteiro teor](https://www.stj.jus.br/websecstj/cgi/revista/REJ.cgi/ITA?CodOrgaoJgdr=&SeqCgrmaSessao=&dt=20231016&formato=HTML&nreg=202200744520&salvar=false&seq=2365864&tipo=0): credenciamento de leiloeiros, Primeira Turma, 10/10/2023.
- Presidência da República, [Código Penal, art. 233](https://www.planalto.gov.br/ccivil_03/decreto-lei/del2848compilado.htm): diploma correto do exemplo de ato obsceno.
- STJ, [Tema 1143](https://processo.stj.jus.br/repetitivos/temas_repetitivos/pesquisa.jsp?cod_tema_final=1143&cod_tema_inicial=1143&novaConsulta=true&tipo_pesquisa=T): contrabando de cigarros, julgado em 13/09/2023; tese e modulação registradas na base.

Os endereços dos PDFs privados estão no inventário. O PDF de apresentação não reproduz marcas d'água pessoais nem páginas comerciais completas.
