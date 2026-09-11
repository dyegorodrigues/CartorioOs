# GX Cartório OS — Autonomous Execution Protocol

Data: 2026-09-11
Status: HOT

## Mandato autoral
O usuário autorizou execução autônoma, autossuficiente e adaptativa da pesquisa/arquitetura do GX, sem ciclos de confirmação do tipo “posso prosseguir?” ou “qual próximo passo?”.

Isso NÃO autoriza trabalho em background entre mensagens. Significa que, a cada turno de execução, o agente deve consumir o maior lote seguro e útil possível antes de voltar ao usuário.

## Regra principal
**EXECUTE → VERIFY → PERSIST → ADAPT → CONTINUE**, até atingir um verdadeiro ponto de decisão autoral, risco de dano, falta de acesso ou limite material da sessão.

Não interromper para pedir opinião sobre microdecisões reversíveis.

## Quando o agente PODE decidir sozinho
- ordem das pesquisas;
- seleção de provas/fontes para BUILD/CHALLENGE;
- criação de mapas, ledgers, heatmaps e benchmarks;
- refinamento de metodologia;
- classificação P1/P2/P3;
- ajustes de schema/arquitetura reversíveis;
- criação de artefatos internos de pesquisa;
- correção de inconsistências e fatos errados em arquivos internos;
- red-team e QA;
- atualização de handoff/status.

## Quando PARAR e pedir decisão autoral
Somente se houver:
1. mudança irreversível de escopo/missão;
2. decisão de estudar de fato / ativar runtime do aluno;
3. duas arquiteturas materialmente diferentes sem critério objetivo de desempate;
4. necessidade de gasto/assinatura/compra;
5. necessidade de ação externa irreversível;
6. conflito com restrição autoral explícita;
7. escolha estética/pedagógica em que a preferência pessoal do usuário é o dado decisivo.

## Tamanho de lote padrão
Em vez de um passo por mensagem, operar em BATCHES de valor completo. Um batch ideal contém, quando possível:
- pesquisa primária;
- triangulação secundária;
- criação/atualização de artefato;
- verificação/QA;
- persistência GitHub;
- próximo ponteiro HOT.

## Política de pesquisa
Prioridade:
A. fonte oficial atual;
B. prova/gabarito/espelho oficial;
C. banco de questões/livro/material secundário para descoberta;
D. cursinho/material legado como benchmark/red-team.

Nunca promover C/D acima de A/B.

## Política de exploração
O agente pode abrir novas frentes apenas se elas alimentarem uma destas camadas:
- OFFICIAL SCOPE;
- SOURCE REGISTRY;
- EXAM CORPUS;
- PROPOSITION MAP;
- INCIDENCE/CONSEQUENCE;
- DEPTH BUDGET;
- CANONICAL TREE;
- BUILD/VALIDATION/CHALLENGE;
- FRESHNESS;
- LEARNER-FACING COMPILER;
- CONTEST HISTORY / OPPORTUNITY MODEL.

Evitar pesquisas interessantes porém desconectadas.

## Regra de não-ansiedade
Não expandir conteúdo porque “pode cair”.
Toda inclusão profunda precisa de pelo menos um motivo:
- incidência real;
- centralidade/pré-requisito;
- consequência de erro;
- custo baixo/retorno alto;
- exigência de fase;
- alteração normativa relevante;
- lacuna demonstrada em validation/challenge.

## Regra de auto-red-team
Antes de promover qualquer módulo:
1. procurar contraexemplos;
2. testar com outra banca;
3. testar mudança de formulação;
4. conferir atualidade jurídica;
5. verificar se o material ensina a proposição, não apenas a menciona;
6. reservar held-out antes do freeze;
7. registrar falha e patch, sem racionalizar erro.

## Regra de comunicação
Relatórios ao usuário devem ser por MARCOS, não por cliques.

Não reportar:
- “achei um PDF”;
- “agora vou olhar outro”.

Reportar quando houver:
- descoberta que muda arquitetura;
- lote de corpus consolidado;
- Depth Budget novo/alterado;
- material que passou/falhou validation;
- artefato útil pronto;
- decisão autoral necessária.

## Estado atual
Enquanto a restrição `NÃO INICIAR ESTUDO AINDA` estiver ativa:
- não atribuir mastery;
- não emitir Missão 01;
- não transformar espécime em material canônico sem Sufficiency Gate;
- continuar Exam Atlas + Contest History Atlas + Freshness + held-out + red-team.
