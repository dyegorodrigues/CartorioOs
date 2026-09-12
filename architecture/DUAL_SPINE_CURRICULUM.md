# GX Cartório OS — Dual Spine Curriculum

Atualizado em 09/09/2026.

## Missão
O GX existe para maximizar a probabilidade de aprovação em todas as fases dos concursos de outorga de delegações e orientar preparação de teto, inclusive tentativa real de gabarito, sem transformar o estudo em enciclopédia indiscriminada.

A regra é **cobertura integral do escopo + profundidade desigual e justificável**. Ver `architecture/COVERAGE_DEPTH_POLICY.md`.

A profundidade jurídica é instrumental: entra quando aumenta acerto, discriminação entre alternativas, velocidade, fundamentação, transferência para caso novo, produção discursiva/prática/oral ou reduz risco de erro recorrente.

## Problema que esta arquitetura resolve
O conhecimento jurídico real é um grafo: Civil alimenta Registro de Imóveis, Família e Sucessões alimentam Notas/RCPN, Administrativo e Constitucional atravessam delegação, responsabilidade e fiscalização, Tributário aparece dentro de atos imobiliários etc.

A prova, porém, continua organizada por disciplinas e o candidato precisa saber:
- qual matéria está estudando;
- onde está no edital;
- o que já cobriu;
- o que domina;
- o que esqueceu;
- quanto falta;
- como aquela matéria funciona como sistema coerente por si mesma.

Portanto, o GX mantém duas espinhas simultâneas.

## Spine A — Official Exam Spine (visível ao candidato)
É a árvore oficial do edital.

`Disciplina → Tema → Subtema → Microtema útil`

Funções:
1. orientação espacial;
2. cobertura integral do edital;
3. progressão compreensível dentro de cada disciplina;
4. dashboard de domínio por matéria;
5. reprodução da segmentação da prova;
6. prevenção de lacunas invisíveis.

A Spine A nunca é substituída pelo grafo.

### Estado visível por disciplina
Cada matéria deve mostrar, no mínimo:
- cobertura do edital (%);
- domínio atual (%);
- retenção após intervalo;
- acurácia em questões oficiais/inéditas;
- velocidade/latência;
- principais erros;
- itens vencidos para revisão;
- profundidade já alcançada: objetiva / discursiva / prática / oral;
- freshness: estável / HOT / revalidar.

O candidato deve conseguir perguntar `onde estou?` e receber uma resposta imediata e concreta.

## Spine B — Knowledge & Transfer Graph (motor interno)
É a rede de relações entre conceitos, regras, fontes, habilidades, questões e aplicações.

Exemplos:
- capacidade civil → escritura pública → testamento → RCPN;
- promessa de compra e venda → adjudicação compulsória → Registro de Imóveis;
- responsabilidade civil → delegatário → responsabilidade estatal;
- ITBI → transmissão imobiliária → qualificação registral;
- protesto → títulos de crédito → falência;
- união estável → sucessões → inventário extrajudicial.

Funções:
1. identificar pré-requisitos;
2. evitar reaprender a mesma regra em cinco apostilas;
3. construir transferência;
4. gerar revisão inteligente;
5. detectar clusters de erro;
6. conectar objetiva, discursiva, prática e oral;
7. selecionar exemplos cartorializados para matérias gerais.

No grafo operacional inicial, priorizar relações que mudam decisão real, especialmente `requires` e `confusable_with`. Não construir ontologia ornamental.

A Spine B fica majoritariamente invisível durante o estudo inicial. Ela aparece quando ajuda.

## Quatro views canônicas

### 1. Edital View
Mostra a matéria isolada e a arquitetura oficial.

Objetivo: localização e completude.

### 2. Learning View
Reordena microtemas por pré-requisitos e eficiência pedagógica sem destruir o mapa oficial.

Objetivo: aprender na ordem mais fácil/robusta, não necessariamente na ordem impressa do edital.

Toda unidade mantém um campo `posição no edital`, mesmo quando ensinada em outra ordem.

### 3. Exam View
Simula exatamente o formato do exame-alvo.

Regras:
- blocos por disciplina quando a prova os segmenta;
- peso e quantidade reais da matriz;
- distribuição temporal semelhante à prova;
- treino progressivo até caderno integral.

O interleaving pedagógico nunca autoriza transformar o simulado em formato diferente do exame real.

### 4. Connection View
Mostra conexões entre disciplinas somente quando o candidato já possui âncoras suficientes para não se perder.

Objetivo: integração, transferência e consolidação.

## Regra anti-embaralhamento
Interleaving não significa misturar tudo desde o primeiro dia.

Sequência padrão:
1. **blocked foundation** — aprender um bloco coerente dentro da matéria;
2. **local discrimination** — misturar institutos próximos/confundíveis da mesma matéria;
3. **cross-topic transfer** — misturar temas diferentes da mesma matéria;
4. **cross-discipline transfer** — introduzir conexões com outras matérias;
5. **exam simulation** — voltar ao formato real da prova.

O grafo escolhe quando misturar. O candidato nunca recebe aleatoriedade sem finalidade diagnóstica ou pedagógica.

## Coverage Floor
Nenhum conteúdo expressamente examinável é descartado por baixa incidência histórica.

A incidência altera:
- orçamento de tempo;
- quantidade de questões;
- frequência de revisão;
- profundidade;
- mastery-alvo.

Ela não altera a existência do nó no currículo.

Para preparação objetiva madura, conteúdo expresso deve atingir normalmente pelo menos M2–M3, subindo a M4 quando a aplicação em caso/questão inédita for relevante.

## Depth Budget — quanto estudar de cada coisa
Todo nó recebe uma classe de profundidade, sem confundir profundidade com inclusão/exclusão.

### P0 — Pré-requisito mínimo
Base esquecida ou nunca aprendida necessária para entender conteúdo pontuável.

Ensinar apenas o suficiente para destravar o próximo nó. Mastery típico M1–M2, salvo dependência recorrente.

### P1 — Cobertura examinável
Conteúdo expresso ou plausivelmente examinável que precisa de piso seguro.

Exige localizar, recuperar núcleo e discriminar o normal. Mastery típico M2–M4 conforme formato observado.

### P2 — High-yield / discriminativo
Regra, exceção, procedimento, jurisprudência ou distinção com alta recorrência, centralidade ou poder de separar candidato preparado de candidato mediano.

Exige recuperação rápida, discriminação e aplicação. Mastery típico M3–M4 na objetiva.

### P3 — Produção avançada
Conteúdo que precisa sustentar discursiva, peça prática ou oral.

Exige fundamentação, estrutura de resposta e transferência. Mastery típico M5–M7 conforme fase.

### P4 — Reference
Doutrina, controvérsia ou detalhe de baixa utilidade imediata.

Fica disponível para consulta e sobe de prioridade por evidência de edital, banca, erro, fase estadual, mudança normativa ou dependência.

## Regra de utilidade
Nenhum conteúdo recebe alta densidade de repetição apenas porque é juridicamente interessante.

Ele precisa justificar pelo menos uma função:
- pré-requisito;
- cobertura expressa do edital;
- incidência histórica relevante;
- dificuldade/discriminação de banca;
- dependência de tema importante;
- erro real do candidato;
- exigência de discursiva/peça/oral;
- atualização normativa crítica.

Mas conteúdo examinável de baixa incidência continua coberto pelo Coverage Floor.

## Progressão por matéria
Cada disciplina deve possuir uma progressão legível:

`Mapa → Fundamentos mínimos → Core → Procedimentos/distinções → Questões → Consolidação → Produção → Simulação`

A progressão é independente da porcentagem de peso. Uma matéria de 1 questão ainda precisa de coerência; ela apenas recebe menor orçamento de tempo/profundidade se não for dependência de outros blocos.

## Caso especial: Direito Notarial e Registral
Na matriz ENAC 2026.2, N/R responde por 60 das 100 questões. Também é domínio praticamente novo para o candidato e ponto central de integração prática.

Por isso N/R entra desde o primeiro ciclo, em espiral com fundações just in time.

Isso não significa estudar 60% do tempo mecanicamente. O orçamento considera:
- peso de prova;
- tamanho real do conteúdo;
- dependências;
- domínio individual;
- taxa de esquecimento;
- transferência para demais fases;
- recência normativa;
- incidência documentada;
- risco da cauda ainda não dominada.

## Mastery canônico
A escala única do GX é M0–M7:
- M0 — não visto;
- M1 — reconhece com apoio;
- M2 — recupera núcleo sem apoio;
- M3 — discrimina de alternativas/institutos próximos;
- M4 — aplica em item/caso inédito;
- M5 — produz resposta escrita juridicamente suficiente;
- M6 — executa saída prática/procedimental quando aplicável;
- M7 — explica e sustenta oralmente sob reperguntas.

`Retention/stability` é eixo separado. Um nó pode ter alta capacidade atual e baixa estabilidade futura.

A exigência de nível varia com o Depth Budget e a fase.

## Orientação permanente
Toda sessão deve poder responder quatro perguntas:
1. Onde estou no edital?
2. Por que estou estudando isto agora?
3. O que preciso conseguir fazer ao final?
4. Quando e como este conhecimento será testado novamente?

E para o candidato com tendência a hiperprofundidade, uma quinta:
5. **Qual detalhe eu não preciso memorizar agora e por quê?**

Se o GX não consegue responder às cinco, a sessão não está bem arquitetada.