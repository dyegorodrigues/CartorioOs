# GX Cartório OS — Roadmap finito até o início do estudo

Data: 2026-09-11
Status: HOT roadmap

## Objetivo
Evitar engenharia infinita. O sistema deve convergir para estudo real do candidato. A partir deste ponto, o projeto terá **5 macro-rodadas** até o início do estudo guiado.

## Macro-rodada 1 — Fechar dois pilotos representativos
Estado atual: EM EXECUÇÃO.

Objetivo:
- Regime Geral / Lei 8.935: consolidar material v0.x, challenge e held-out suficiente;
- Registro de Imóveis / LRP: fechar ledger, depth budget, rubrics, build, challenge e held-out próprio.

Critério de saída:
- um módulo predominantemente RULE/JURISPRUDENCE (Regime Geral);
- um módulo PROCEDURE/ACT/SYSTEM (RI);
- ambos com provenance, freshness e pelo menos validação externa mínima real.

## Macro-rodada 2 — Validar a fábrica, não só o conteúdo
Objetivo:
- verificar se o pipeline produz material compacto, correto e treinável;
- medir se MAP, MASTER, lei seca guiada, REVIEW, Q→A e questões derivam da mesma árvore;
- eliminar redundância e sofisticação sem retorno probatório;
- confirmar que depth budget reduz carga sem criar buracos.

Critério de saída:
- nenhum gap estrutural grave conhecido nos dois pilotos;
- revisão não exige releitura integral;
- questões e outputs têm origem rastreável;
- carga executiva do aluno é baixa.

## Macro-rodada 3 — Auditoria independente Work/Astra
Momento planejado para acionar Work/Astra.

Objetivo:
- red-team global de arquitetura, currículo, fontes, material, questões, freshness, adaptação e carga;
- tentar falsificar a hipótese de que o GX prepara para aprovação com eficiência;
- procurar overengineering, falsa confiança, omissões, métricas inúteis e caminhos sem evidência.

O Work/Astra NÃO deverá reinventar o sistema. Deverá auditá-lo contra a missão de aprovação.

Critério de saída:
- relatório de falhas/risco;
- patches classificados em MUST / SHOULD / REJECT;
- nenhuma mudança entra apenas por parecer sofisticada.

## Macro-rodada 4 — Productização mínima para estudo
Objetivo:
- transformar a arquitetura validada em experiência simples;
- definir rotina diária, seleção automática de tarefas, review queue, questão/erro, freshness e progresso;
- preparar o primeiro conjunto real de módulos para aprender do zero.

Critério de saída:
- candidato não precisa escolher material, ordem, revisão ou profundidade;
- sistema entrega “faça isto agora”;
- todas as superfícies apontam para a mesma árvore;
- telemetria mínima suficiente sem burocracia.

## Macro-rodada 5 — Piloto real de estudo e calibração
Esta é a transição de engenharia para preparação.

Objetivo:
- iniciar estudo real em lote pequeno;
- observar compreensão, retenção, tempo real, fadiga, acertos, erros e capacidade de recuperação;
- adaptar throughput e carga;
- corrigir o sistema com dados do candidato, não apenas teoria.

Critério de saída:
- rotina sustentável;
- revisão funcionando;
- material suficientemente claro;
- questões detectando gaps úteis;
- carga compatível com vida real;
- então escalar para o currículo inteiro.

# Depois da Rodada 5
Não haverá nova fase de “engenharia antes de estudar”.

O sistema entra em **runtime contínuo**:
`STUDY → RETRIEVE → ASSESS → PATCH → REVIEW → ADVANCE`.

Novas melhorias de arquitetura só entram se corrigirem problema observável ou aumentarem:
- velocidade de aprendizagem;
- retenção;
- acerto/discriminação;
- produção objetiva/discursiva/prática/oral;
- atualização;
- redução de carga organizacional.

## Regra de contenção
Nenhum módulo pode receber rodadas infinitas.

Padrão por módulo:
1. BUILD;
2. CHALLENGE;
3. FREEZE;
4. HELD-OUT;
5. PATCH se necessário;
6. no máximo um RETEST limpo antes de promover ou rebaixar.

Se após isso continuar instável, registrar a limitação e avançar o currículo em vez de paralisar toda a preparação.

## Estado atual
Estamos na **Macro-rodada 1 de 5**.

Regime Geral já passou por build, challenge, freeze, falha held-out e patch.
Registro de Imóveis está em fechamento de depth budget/rubrics/build e preparação de held-out próprio.

Próximo marco visível ao usuário: conclusão da Macro-rodada 1 e decisão de entrada na Rodada 2.