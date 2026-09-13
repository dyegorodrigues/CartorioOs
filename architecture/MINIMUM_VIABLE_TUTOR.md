# GX Cartório OS — Tutor mínimo

Atualizado em 13/09/2026. Contrato simplificado; versão anterior preservada no histórico Git.

## Resultado para o candidato

Abrir o ChatGPT no projeto e dizer **“Continuar”**, opcionalmente com o tempo disponível. Receber uma tarefa por vez, responder por texto ou ditado disponível na interface e receber correção. O tutor prepara material, escolhe sequência, registra tentativas e organiza revisões.

O candidato não mantém resumos, decks, planilhas, cronogramas ou bancos no Notion. GitHub e Notion são bastidores. Nenhuma assinatura adicional é requisito. Não há promessa de superar todo cursinho, de aprovação ou de memória perfeita entre chats.

**Estado atual: preparação, estudo real ainda não iniciado.** Simplificar não revoga essa restrição nem registra respostas fictícias como desempenho do candidato.

## Um ciclo, três tarefas úteis

1. **Aprender:** explicação curta autossuficiente, fundamento, exemplo e contraste necessário.
2. **Recuperar:** responder sem ver o gabarito; flashcard, contraste ou reconstrução breve.
3. **Aplicar:** questão/caso, feedback e, progressivamente, produção escrita/prática/oral.

Não executar seis leituras obrigatórias do mesmo conteúdo. MAP, MASTER, REVIEW e demais superfícies são modos de acessar uma base; aparecem quando ajudam naquela tarefa. O mapa visível localiza disciplina e objetivo. O grafo interno começa por pré-requisitos e conceitos confundíveis; uma conexão só entra se mudar a explicação, a ordem ou o exercício.

Primeiro percurso preservado: mapa das especialidades → art.236/delegação → regime geral → operações extrajudiciais simples. Base competitiva enferrujada; Notarial/Registral parte sem exposição prévia relevante. Fundamentos gerais entram quando necessários. Os recortes de afastamento e dúvida são ensaios da fábrica, não a primeira aula automática de um iniciante.

## Rotina diária

- Retomar uma tarefa interrompida antes de abrir outra, rechecando o conteúdo.
- Sem interrupção: selecionar uma dose de revisão vencida e um bloco novo estudável; ajustar ao tempo disponível. Sem duração combinada, 20 minutos é hipótese inicial de sessão curta, não preferência comprovada.
- Se revisão ocupar repetidamente todo o tempo, reduzir entrada de novos cards, retirar duplicatas e investigar itens que falham; preservar avanço curricular. Não perseguir 100% de retenção por ansiedade.
- Pergunta primeiro, resposta e feedback depois da tentativa. Consulta/pista fica separada de recuperação independente.
- Ensinar conteúdo desconhecido antes de avaliar. Falha repetida pede mais suporte ou menor complexidade, além de verificar lacuna do material.
- Ao parar, deixar registro conferido e primeira ação de retomada. Não exigir formulário de fechamento.

## Quem decide o quê

| Decisão | Mecanismo mínimo |
|---|---|
| O que aprender | edital, pré-requisitos, cobertura, questões verificadas e material liberado |
| Quando rever um card | FSRS executado por código, com histórico observado |
| Como explicar | clareza e resultado das tentativas; hipóteses pessoais revisáveis |
| Quando aumentar dificuldade | desempenho no formato correspondente e em casos novos |
| O que mostrar hoje | tempo disponível, tarefa pendente e fila curta |

FSRS não produz prioridade de prova nem mastery. Frequência em outras carreiras continua separada de ENAC/FGV Cartório; poucos itens não sustentam previsão precisa. Cadernos equivalentes, alternativas e proposições dependentes não são observações independentes. Anuladas e alterações de matriz exigem denominadores explícitos. Etiquetar o grafo não cria uma probabilidade de cair.

## Revisão e telemetria

Ensaio: `fsrs==6.3.2`, parâmetros padrão e alvo 0,90. Configuração genérica a avaliar, não 90% de retenção pessoal medida. Sem ajustes manuais de pesos ou otimização antes de histórico suficiente. Fuzz desativado apenas para reprodução do ensaio; decidir configuração do piloto antes de ativá-lo.

Anki usa Again/Hard/Good/Easy. Para reduzir decisões, começar com **não recuperou → Again; recuperou → Good**. Hard significa acerto difícil, não esquecimento. O candidato pode apenas responder; o tutor avalia os elementos essenciais. Ambiguidade pede esclarecimento ou tentativa não pontuável. Falha do material exige corrigir/suspender o item antes de diagnosticar dificuldade pessoal.

Histórico de recall pertence ao item/formato estável, não a toda proposição. Acerto por alternativas, eliminação ou chute fica no desempenho de questões; não vira automaticamente Good em um card de recuperação livre. Variações de aplicação treinam transferência sem fingir ser a mesma observação de memória.

Registrar ID da tarefa/tentativa, versão do conteúdo, instante real, resposta/evidência, resultado, pista/consulta, causa de erro demonstrável e próxima ação. Duração, esforço ou confiança só quando disponíveis e úteis. Não usar intervalo entre mensagens como tempo líquido de estudo; não exigir nota subjetiva a cada pergunta.

Separar quatro leituras:

- **Resposta agora:** acerto/erro/assistida/não pontuável.
- **Retenção observada:** recuperação após intervalo, com quantidade de tentativas e período.
- **Previsão FSRS:** estimativa genérica por item; desconhecida antes da primeira revisão; não evidência de calibração pessoal.
- **Mastery M0–M7:** não visto, reconhece, recupera, discrimina, aplica, produz escrito, executa prática e sustenta oral, segundo as rubricas existentes. Um card acertado não promove toda a matéria.

Mostrar apenas o necessário: cobertura percorrida, resultado em revisões tardias e desempenho em questões novas, com denominadores. Deixar campos sem evidência vazios. Nota global de 1 a 5 não é necessária. Diagnósticos iniciais não culpam o candidato por falta de exposição.

## Continuidade entre conversas

Entrada única: `docs/START_HERE.md` na branch `chatgpt/gx-cartorio-v0.1`. O tutor lê estado recente e busca apenas material/registros necessários. Notion permanece como destino operacional provisório; não criar outra base de produção.

Na futura sessão real, salvar efeitos de cada bloco curto e tarefa pendente. Aproveitar Study Sessions para episódios/referências; o formato final e a leitura dirigida ainda exigem integração antes da ativação. Histórico pessoal não vai ao repositório público.

Protocolo: ler estado recente → aplicar eventos com IDs estáveis → escrever → reler/conferir → anunciar salvo. Interrupção após escrita: reconhecer mesmo evento sem recontar tentativa. Falha antes de gravar: informar pendência e preservar lote disponível na conversa. Não garantir recuperação de resposta nunca salva.

Uma sessão ativa por vez no piloto. Revisão local não cria transação/lock no Notion. Conflitos/indisponibilidade precisam ser tratados; o ensaio não prova escrita simultânea segura nem promove backend novo.

Projetos compartilham instruções/fontes; memória é auxílio. Uma conversa nova precisa ter acesso aos conectores e ao ponto de entrada. Não há ferramenta disponível nesta sessão para instalar/inspecionar instruções do projeto ChatGPT. Não afirmar que GitHub é carregado automaticamente. Processo novo + leitura do Notion são evidência parcial; aceitação em nova conversa real permanece pendente.

## Implementação e saída finita

`scripts/review_runtime.py`: exposição, tarefa pendente, resultado binário, FSRS, fila limitada, checkpoint e retry idempotente. Só aceita `SANDBOX`/itens `SYN-`. Não corrige Direito, escolhe currículo novo, atualiza mastery ou trabalha em background.

Transição ao piloto pequeno segue o roadmap existente: conteúdo inicial seguro/fontes/validação externa delimitada; derivações consistentes; revisão independente pendente; registro e retomada conferidos na interface real; decisão de início do candidato. Não exigir completar 300 reconstruções ou todo o edital antes de aprender. Esta entrega não encerra macro-rodadas nem concede S2.

Após validar o ciclo, funcionalidades só entram para corrigir falha observada de conteúdo, retenção, transferência, tempo ou retomada. Não abrir dashboard, ontologia extensa, frota de agentes ou catálogo de métricas como novo requisito.

## Evidências da decisão

- [Manual Anki — FSRS](https://docs.ankiweb.net/deck-options.html#fsrs): histórico e troca entre retenção/carga. [Botões](https://docs.ankiweb.net/studying.html#answer-buttons): opção de usar apenas Again/Good. A política binária deriva dessa opção.
- [Py-FSRS, mantenedores](https://github.com/open-spaced-repetition/py-fsrs): implementação/serialização reutilizadas; versão instalada fixada e conferida em 13/09. Não há sincronização com aplicativo Anki.
- [Karpicke e Blunt, 2011](https://learninglab.psych.purdue.edu/downloads/2011/2011_Karpicke_Blunt_Science.pdf): recuperação favoreceu desempenho posterior, inclusive inferências, nos experimentos com textos científicos. [O’Day e Karpicke, 2021](https://learninglab.psych.purdue.edu/downloads/2021/2021_ODay_Karpicke_JEDP.pdf): mapas antes da recuperação não acrescentaram benefício no desenho estudado, apesar do tempo extra. Apoiam priorizar recuperação; não testam este tutor nem provam inutilidade de mapas ou superioridade em concurso jurídico.
- [OpenAI — projetos](https://learn.chatgpt.com/docs/projects) e [memórias](https://learn.chatgpt.com/docs/customization/memories): contexto compartilhado/memória ajudam continuidade; regras obrigatórias precisam de documentação. Checkpoint e limites são decisões do GX, não garantias atribuídas à plataforma.
