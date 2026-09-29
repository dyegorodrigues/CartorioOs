# Tutor mínimo — decisão e ensaio de 13/09/2026

## Decisão

O pedido atual é uma rotina fluida no ChatGPT, usando celular/tablet. O projeto já tinha os componentes conceituais necessários; faltava demonstrar revisão e retomada. Foi simplificado o contrato existente em `architecture/MINIMUM_VIABLE_TUTOR.md`, em vez de desenhar outro sistema.

A interface prevista é **aprender → recuperar → aplicar**, com uma tarefa por vez. O tutor assume planejamento e registros. Grafo e seis superfícies didáticas ficam disponíveis conforme necessidade, sem seis releituras obrigatórias. A mesma regra jurídica tem uma base e várias aplicações.

## Pesquisa incorporada

| Evidência consultada | Decisão e limite |
|---|---|
| [Anki: FSRS](https://docs.ankiweb.net/deck-options.html#fsrs) | Usar cálculo real de revisão; alvo inicial genérico de 0,90, sem prometer retenção pessoal. Retenção maior aumenta carga. |
| [Anki: respostas](https://docs.ankiweb.net/studying.html#answer-buttons) | Começar com Again/Good, opção admitida no manual. Hard é acerto difícil. Não obrigar nota 1–5 em cada tentativa. |
| [Py-FSRS](https://github.com/open-spaced-repetition/py-fsrs) | Reutilizar biblioteca mantida; instalado/fixado pacote 6.3.2. Sem implementar outra curva de esquecimento ou sincronização Anki. |
| [Karpicke e Blunt, 2011](https://learninglab.psych.purdue.edu/downloads/2011/2011_Karpicke_Blunt_Science.pdf) | Recuperação contribuiu para aprendizagem posterior e inferências no experimento com textos científicos; não prova desempenho no ENAC. |
| [O’Day e Karpicke, 2021](https://learninglab.psych.purdue.edu/downloads/2021/2021_ODay_Karpicke_JEDP.pdf) | Mapas antes de recall não acrescentaram benefício no desenho estudado. Evitar impor trabalho adicional de mapas ao aluno; não abolir orientação conceitual útil. |
| [OpenAI: projetos](https://learn.chatgpt.com/docs/projects), [memórias](https://learn.chatgpt.com/docs/customization/memories), [web](https://learn.chatgpt.com/docs/web) | Projeto compartilha fontes/instruções; memória é auxílio. Ambiente web permite trabalho com ferramentas disponíveis. Isso não garante gravação/retomada em qualquer conversa sem os conectores. |

## O que foi executado

- Núcleo `scripts/review_runtime.py`: eventos de exposição/apresentação/resposta/cancelamento, cálculo FSRS, tarefa pendente, fila dentro do orçamento, serialização e verificação de integridade.
- Correção binária recebida pelo núcleo; não há corretor jurídico automático implementado. Assistência e lacuna do material não treinam o FSRS como falha pessoal. Lacuna suspende o item.
- Sem exposição anterior, alteração de versão/conteúdo ou falta de liberação/freshness: não conceder revisão válida silenciosa.
- Retry com mesmo evento não duplica; mesmo ID com conteúdo distinto e estado antigo são recusados. Esta proteção local não equivale a escrita concorrente transacional no Notion.
- `requirements-review.txt` fixa a dependência; sem API, assinatura adicional, site ou novo banco de produção.

## Prova de persistência

Foi criada uma única [página de ensaio no Notion](https://app.notion.com/p/3da42424cdbc81dc9066d20b0eccad0f), separada de Study Sessions. Todos os dados são fictícios.

1. Gerados dois itens `SYN-`, 12 respostas simuladas, exposições/apresentações e uma tarefa pendente: 27 eventos.
2. Escrito o checkpoint no Notion; feito novo fetch; JSON recebido foi validado por hash e comparado campo a campo. O Notion normalizou ordem de propriedades, sem mudança de valores.
3. Um novo processo Python, recebendo o conteúdo relido, recuperou os 27 eventos e exatamente a pergunta pendente, sem incluir gabarito no objeto de apresentação.
4. Reaplicados os 27 eventos sem duplicação ou alteração do checkpoint.
5. Aplicado evento fictício 28, com esquecimento: FSRS calculou revisão em 10 minutos segundo o passo de reaprendizagem padrão. Gravado no Notion e relido; tarefa pendente encerrada e hash conferido.

Hash dos 27 eventos: `6972e685e7c209d597fe4b891eedd71463c22bd6a0454456ea2f47c6b9bf65c5`.

Hash após evento 28: `85311d9ee55768b724d84b7e7c317efd6f3f020406b978c00624367cbdb197f5`.

Essa prova demonstra persistência/reconstituição do ensaio pela integração disponível. **Não é teste com o candidato nem abertura real de outra conversa do projeto.** Não existe transação Notion que assegure dois tutores escrevendo simultaneamente. O piloto deve começar com uma sessão ativa e conferência após escrita.

## Verificação mecânica

41 testes passaram: 29 anteriores e 12 novos, incluindo processo novo, retry dos 27 eventos, mudança de conteúdo, fila/orçamento, ausência de exposição, assistência, lacuna de material, relógio/fuso e modo real recusado. Checagem do material derivado e integridade dos três arquivos congelados continuam sendo gates separados. Testes de software não detectam toda incorreção jurídica nem demonstram retenção do candidato.

## O que permanece por concluir

1. **Conteúdo inicial e validação:** fechar o primeiro percurso para iniciante e as pendências externas/independentes já registradas no roadmap; os dois recortes técnicos não são módulos completos nem primeira aula pronta. Nenhum S2 novo.
2. **Integração real:** reaproveitar Study Sessions e o ponto de entrada único, testar leitura/escrita/retomada numa nova conversa com os mesmos conectores. Não há ferramenta disponível para instalar ou verificar instruções do projeto ChatGPT nesta sessão. Não depender de copiar um novo resumo a cada conversa.
3. **Piloto pequeno:** quando conteúdo e integração passarem, apresentar o primeiro percurso concreto para a decisão de início já prevista. Só então medir duração real, revisão tardia, transferência e sustentabilidade, ajustando o método.

Não é necessário reconstruir previamente todo o corpus, migrar bancos ou construir dashboard. Esta entrega resolve parte mecânica da revisão/retomada sem declarar o tutor completo ou encerrar as macro-rodadas. O único histórico pessoal continua sendo o que efetivamente existir nas bases reais; o ensaio não cria mastery, sessão de estudo, notas ou retenção do candidato.
