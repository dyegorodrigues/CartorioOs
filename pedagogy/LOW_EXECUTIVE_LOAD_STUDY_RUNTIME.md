# GX Cartório OS — Low Executive-Load Study Runtime

## Objetivo
Reduzir a carga executiva exigida do candidato. O sistema deve exigir energia para **aprender e responder**, não para planejar, organizar, resumir, agendar ou decidir o próximo passo.

Este protocolo é geral e não codifica diagnóstico médico em repositório público.

## Regra central
O candidato pode iniciar com um comando mínimo: `Começar estudo`.

O tutor decide:
- revisão vencida;
- conteúdo novo;
- sequência;
- dificuldade;
- quantidade de questões;
- necessidade de reparo;
- registro;
- próxima revisão.

## Sessão em blocos curtos
A sessão longa é composta por ciclos curtos e fechados, por exemplo:
1. orientação de 60–120s;
2. ensino de uma unidade pequena;
3. recuperação imediata;
4. questão/caso;
5. feedback e reparo;
6. microfechamento.

O sistema pode encadear vários ciclos, mas evita entregar um bloco enorme de leitura passiva antes da primeira resposta do candidato.

## Externalização
O candidato não precisa manter na cabeça:
- o que estudar amanhã;
- o que revisar;
- onde parou;
- quais erros se repetem;
- qual material é vigente;
- que questão precisa refazer;
- qual fase merece treino.

Esses estados pertencem ao sistema.

## Resumo
O candidato **não deve produzir resumo por transcrição** como tarefa padrão.

O GX gera REVIEW a partir da unidade canônica. O candidato só produz síntese quando a própria produção for pedagogicamente útil, por exemplo:
- reconstruir conceito de memória;
- montar quadro sem consulta;
- responder mini-discursiva;
- explicar oralmente.

## Atenção e engajamento
Preferir:
- interação frequente;
- objetivos visíveis e pequenos;
- feedback rápido;
- alternância controlada entre leitura, recall e questão;
- retomadas explícitas (`onde estamos`, `por que isso importa`, `o que fecha este bloco`);
- progresso granular;
- dificuldade ajustada para evitar monotonia e sobrecarga.

Evitar:
- longas instruções administrativas;
- listas gigantes sem hierarquia;
- múltiplas escolhas de estudo delegadas ao candidato;
- revisão baseada só em releitura;
- calendários rígidos que viram culpa quando quebrados.

## Memória
Revisão usa múltiplos tipos:
- recall de 20–60s;
- flashcard quando atômico;
- questão curta;
- discriminação;
- reconstrução de tabela;
- caso;
- mini-oral.

O scheduler seleciona a modalidade com base no tipo de conhecimento, não apenas no tempo decorrido.

## Retorno depois de ausência
Se houver intervalo sem estudo, o sistema não exige reconstrução manual de cronograma. Executa:
1. diagnóstico curto de retenção;
2. reparo dos nós frágeis mais importantes;
3. retomada do próximo nó elegível;
4. reprogramação automática dos demais.

## Métricas úteis
Guardar apenas o que muda decisão:
- acerto;
- confiança;
- necessidade de pista;
- latência aproximada quando útil;
- tipo de erro;
- modalidade;
- intervalo desde a última evidência;
- desempenho sob maior complexidade.

Não medir produtividade por páginas lidas, horas de vídeo ou quantidade bruta de flashcards.

## Regra de carga
Quando o tempo é curto, reduzir **volume**, não destruir a estrutura da sessão. Uma sessão de 20 minutos ainda deve conter recuperação e feedback.

## Finalidade
O sistema deve funcionar mesmo para um candidato com rotina irregular e alta carga externa. A consistência deve vir da arquitetura, não da exigência de disciplina administrativa perfeita.