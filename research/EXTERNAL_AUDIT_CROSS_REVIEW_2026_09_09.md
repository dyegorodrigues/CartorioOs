# GX Cartório OS — Cross-review da auditoria externa

Atualizado em 09/09/2026.

Status: **decisão arquitetural**. Este documento não aceita a nota externa como autoridade; classifica cada achado em `ADOTAR`, `ADOTAR COM AJUSTE`, `REJEITAR` ou `VERIFICAR`.

## Horizonte real do candidato

- 2026: início da preparação e construção mínima do tutor; **não prestar ENAC 2026.2** por decisão autoral.
- primeira edição do ENAC em 2027: primeiro alvo operacional de habilitação, salvo mudança autoral futura.
- fim de 2027: alvo desejado de prontidão competitiva ampla para ENAC e concursos estaduais.
- 2028: buffer máximo para aprovação/outorga competitiva; o sistema não deve planejar como se três anos fossem necessários por padrão.
- estado inicial: bacharel em Direito, porém conhecimento competitivo operacional considerado **enferrujado / próximo de zero até evidência em contrário**, e Direito Notarial/Registral tratado como domínio majoritariamente novo.

Não existem dois currículos independentes. Existe um National Core único, com profundidade e modalidades de saída que crescem conforme o domínio e o concurso-alvo.

## Verificação jurídica independente

### ENAC
A Resolução CNJ 696/2026 está vigente. O ENAC é habilitatório, eliminatório e não classificatório. O CNJ informa realização de pelo menos duas edições por ano e certificado válido por seis anos. Para ampla concorrência, a aprovação exige ao menos 60% de acertos totais; não há, no ENAC atual, corte autônomo de 50% em Notarial/Registral.

### Concurso estadual
Quando houver prova objetiva estadual, a Resolução 696/2026 exige cumulativamente, para ampla concorrência:
- pelo menos 50% em Direito Notarial e Registral;
- pelo menos 60% no total;
- colocação dentro de até 12 candidatos por vaga, ressalvadas as regras próprias aplicáveis.

O edital estadual pode substituir a objetiva pelo ENAC quando assim previsto. Portanto, objetiva permanece uma competência estratégica da carreira, mesmo com peso final zero.

A fase discursiva inclui, no mínimo, dissertação + peça prática + três questões discursivas. O modelo classificatório nacional atribui 70% à discursiva, 25% à oral e 5% aos títulos.

## Matriz de decisão sobre a auditoria

### ADOTAR — 1. Passagem 1 não é corpus integral

O marco `300/300` continua válido, mas deve ser nomeado com precisão: **300/300 indexadas/classificadas na passagem 1**.

Verificação direta no Question Intelligence Lab mostrou que os registros possuem metadados úteis, porém ainda não armazenam o enunciado/alternativas como conteúdo estruturado e muitos fundamentos continuam pendentes. Logo:
- a passagem 1 é índice analítico + classificação histórica;
- passagem 2 é reconstrução jurídica e semântica;
- nunca chamar o estado atual de corpus integralmente resolvido.

### ADOTAR COM AJUSTE — 2. Texto integral das questões

O sistema precisa ter acesso operacional ao enunciado e às alternativas para reteste, semântica e autópsia de distratores.

Mas não é obrigatório replicar integralmente texto protegido em repositório Git público ou em cada linha do Notion. Arquitetura preferida:
- artefato oficial/PDF preservado em Drive ou URL oficial;
- identificador estável de questão;
- texto normalizado em data plane controlado quando necessário e juridicamente apropriado;
- repositório público guarda metadados, reconstruções próprias e referências, não uma republicação desnecessária do caderno.

### ADOTAR — 3. Unificar mastery

Há drift real entre a escala 0–6 do `LEARNING_SYSTEM.md` e a escala M0–M7 do `ZERO_TO_OUTORGA_SYSTEM.md`.

Escala canônica passa a ser M0–M7:
- M0 não visto;
- M1 reconhece com apoio;
- M2 recupera regra nuclear sem apoio;
- M3 discrimina institutos/distratores próximos;
- M4 resolve item/caso objetivo inédito;
- M5 produz resposta discursiva juridicamente completa;
- M6 executa saída prática/procedimental quando aplicável;
- M7 sustenta resposta oral e reperguntas sob tempo.

`Estabilidade/retention` é eixo separado, não um nono nível. Um M4 pode ser frágil ou estável.

### ADOTAR COM AJUSTE — 4. Grafo operacional mínimo

A Dual Spine é preservada. O problema apontado é de instanciação, não de conceito.

Para v0.1, duas relações transversais ganham prioridade operacional:
- `requires` — pré-requisito que altera a prontidão do nó;
- `confusable_with` — par útil para treino discriminativo.

Normas, jurisprudência, questões, fase e freshness podem permanecer inicialmente como relações/atributos documentais sem exigir uma ontologia hipercomplexa. Novos tipos de aresta só entram se mudarem uma decisão do tutor ou uma consulta real.

### ADOTAR COM AJUSTE — 5. FSRS / motor de retenção

FSRS é candidato forte para **itens atômicos de recuperação** porque é aberto, auditável e sustentado por corpus muito grande de revisões.

Não será promovido a cérebro completo do GX. Limites:
- benchmarks de SRS são majoritariamente de flashcards;
- mastery jurídico também inclui discriminação, caso novo, escrita, peça e oral;
- algoritmos mais complexos podem superar FSRS em previsão, mas não se justificam com dados esparsos de um único candidato no início.

Arquitetura: retention scheduler especializado para recalls atômicos + mastery gates por modalidade + decisão pedagógica do orquestrador. Começar simples e recalibrar com dados reais.

### ADOTAR — 6. Dois estimadores para não contaminar banca

Separar explicitamente:

**Domain Incidence Model**
- pergunta: `o que concursos de cartório cobram?`
- pode agregar FGV, Cebraspe, Vunesp e outras bancas de cartório com pesos/proveniência;
- serve cobertura, profundidade e recorrência de domínio.

**Bank Style Model**
- pergunta: `como esta banca transforma conhecimento em avaliação?`
- permanece específico por banca + janela temporal + família de concurso + fase;
- mede atributos agregados de enunciado, comando, fonte, demanda cognitiva, distrator, anulação etc.

Não usar corpus multibanca para atribuir estilo à FGV.

### ADOTAR — 7. Limite estatístico das 300 ENAC

300 itens são excelentes para reconstrução jurídica, perfil agregado e hipóteses. São insuficientes para frequências finas confiáveis em 138 subtemas de N/R e para uma série temporal robusta com somente três edições.

Consequência:
- não perseguir pseudo-precisão de `chance de cair por microtema`;
- frequência ENAC é um sinal, não o único prior;
- expandir corpus por cartório multibanca para incidência de domínio;
- usar estrutura do edital, centralidade jurídica, transferência de fase, volatilidade normativa e dificuldade individual como sinais adicionais;
- tendências temporais com três edições permanecem exploratórias.

### ADOTAR COM AJUSTE — 8. Freshness como sinal de prioridade

Volatilidade normativa pode elevar prioridade de revisão/análise porque altera risco de erro e pode coincidir com temas novos de prova.

Não canonizar a tese `norma nova = maior chance de cair` sem dados. Usar `normative_change` como prior explicável, com peso aprendido posteriormente.

### ADOTAR — 9. Começar N/R cedo

N/R deve entrar nas primeiras sessões, não apenas depois de um bloco longo de Constitucional/Civil.

Motivo:
- 60% da matriz atual;
- domínio majoritariamente novo para o candidato;
- grande transferência para fases estaduais;
- exige mais ciclos de retenção ao longo do calendário.

Civil, Constitucional, Administrativo e demais fundações entram em espiral e `foundation just in time`, sem cursos completos prévios.

### ADOTAR COM AJUSTE — 10. Material: seis interfaces, menos fontes canônicas

Preservar a experiência `MAP → MASTER → REVIEW → RECALL → EXAM → REFERENCE` para o candidato.

Mas reduzir duplicação editorial:
- `MASTER/Knowledge Unit` = conteúdo canônico semântico;
- `EXAM/Items` = aplicações e avaliações;
- `REFERENCE/Sources` = fontes e profundidade longa;
- MAP, REVIEW e RECALL são preferencialmente projeções/derivações do conteúdo canônico, não cópias manuais independentes.

Isso mantém UX rica com menor dívida de freshness.

### ADOTAR — 11. Espelhos oficiais e produção

Priorizar corpus de:
- discursivas;
- dissertações;
- peças práticas;
- espelhos oficiais;
- respostas a recursos;
- provas/orais ou roteiros oficiais quando disponíveis.

A produção não espera a habilitação para começar. Em 2026/2027 entra em microdoses crescentes; após M4 nos nós relevantes, M5–M7 ganham peso progressivo.

### ADOTAR — 12. Dado do aprendiz é ativo crítico

O sistema não consegue ser realmente adaptativo sem tentativas do candidato. A partir do início das sessões, coletar somente sinais com valor decisório:
- resposta;
- resultado;
- confiança pré-resposta;
- latência aproximada quando útil;
- necessidade de pista;
- causa do erro;
- modalidade de saída;
- intervalo desde última evidência.

Evitar telemetria decorativa.

### ADOTAR COM AJUSTE — 13. Baseline

Não queimar obrigatoriamente um caderno oficial inteiro de cinco horas no estado quase-zero como primeiro ato. Isso pode produzir efeito-chão e consumir um dos poucos cadernos totalmente inéditos.

Plano preferido:
1. diagnóstico curto estratificado de reentrada, com confiança;
2. primeiras semanas de reconstrução;
3. simulado parcial e depois completo quando o resultado puder discriminar níveis reais;
4. preservar ao menos um caderno oficial integral como holdout por um período útil.

O diagnóstico serve o sistema; não vira ritual de sofrimento.

### ADOTAR COM AJUSTE — 14. Limite de engenharia

O risco `construir o tutor em vez de estudar` é real, mas o limite rígido 1:4 não é adequado durante o bootstrap inicial em que a infraestrutura ainda está sendo criada autonomamente pela IA.

Regra operacional:
- arquitetura deve alcançar Minimum Viable Tutor rapidamente;
- depois do início do estudo, mudanças de sistema só ganham prioridade se corrigirem falha observada, reduzirem carga executiva ou melhorarem evidência;
- o tempo do candidato deve ser majoritariamente aprendizagem, não administração do sistema;
- trabalho autônomo da IA no repositório não deve ser contabilizado como `tempo de estudo do candidato`.

### REJEITAR — 15. `Cada ponto acima de 60 no ENAC é desperdício`

Falso para a missão de carreira.

É verdadeiro somente para a certificação isolada, pois o ENAC não classifica. O conhecimento excedente:
- cria margem contra variância de prova/esquecimento;
- transfere para objetiva estadual quando existir;
- alimenta discursiva, prática e oral;
- reduz tempo de campanha quando surgir edital.

O GX não otimizará para `60 raspando`; otimizará margem segura e domínio transferível.

### REJEITAR — 16. `Objetiva é secundária porque vale 0%`

Peso final zero não significa baixa importância. Quando mantida pelo edital estadual, a objetiva possui cortes próprios e cláusula classificatória de convocação por vaga. O sistema mantém competência objetiva alta.

### REJEITAR / NÃO APLICAR — 17. Pressão para ENAC 2026.2

O usuário decidiu não prestar a edição de 2026.2. O projeto não reabre essa decisão por inércia do auditor.

Regra futura:
- primeira edição do ENAC em 2027 é o primeiro alvo de habilitação;
- a partir dela, se não houver habilitação, inscrição recorrente nas edições subsequentes é o default recomendado, salvo impedimento real.

A data exata de 2027 ainda não existe oficialmente e não será inventada.

### REJEITAR — 18. SQLite no Git como solução imediata

Boa ideia em aplicações locais, mas inadequada à integração operacional atual:
- arquivo SQLite é binário e não produz diffs úteis;
- o conector GitHub atual opera conteúdo textual e não oferece transações SQL contra um arquivo persistente;
- atualizar um binário a cada sessão aumentaria fricção e risco operacional.

Alternativas permanecem sob promotion gate:
- Notion Free enquanto suficiente, usando leituras por rows/views quando possível;
- JSONL/CSV versionado para snapshots/auditoria quando fizer sentido;
- Google Sheets por ranges, apenas se telemetria exigir e após sandbox/reconciliação;
- backend/SQLite local somente se futuramente houver um runtime próprio do GX.

### REJEITAR — 19. `Notion está totalmente inviável após ~8 queries`

A limitação observada é principalmente da consulta SQL avançada no plano gratuito. A integração atual também oferece `rows` e `view` para consultas delimitadas. Portanto o Notion não é descartado agora.

O princípio correto é: nenhuma função central dependerá de SQL pago; persistência futura será promovida por necessidade observada, não por pânico.

### REJEITAR — 20. Repositório privado

Fato atual: `dyegorodrigues/CartorioOs` está público. Não há ação necessária para `torná-lo público`.

### REJEITAR — 21. Probabilidades do red team

Percentuais como `35% falha por engenharia`, `20% por não habilitar` etc. não possuem modelo empírico para este candidato e não entram no GX. Os riscos qualitativos são úteis; os números são descartados.

## Política temporal 2026–2028

### Bootstrap — setembro/outubro de 2026
Objetivo: Minimum Viable Tutor + início do estudo real.
- corrigir drift de mastery;
- definir corpus operacional de questões;
- criar primeiros Discipline Maps;
- iniciar N/R + foundations JIT;
- coletar tentativas reais;
- produzir primeiro MASTER efetivamente estudável;
- aplicar diagnóstico curto.

### Base competitiva — restante de 2026
- rotina estável;
- N/R presente desde o começo;
- Civil/Constitucional e demais matérias integradas progressivamente;
- questões oficiais desde cedo;
- recalls e revisão adaptativa;
- microdiscursiva/oral sem competir com a reconstrução da base;
- primeiro simulado integral quando houver sinal suficiente para ele ser informativo.

### Habilitação + expansão — 2027
- primeira edição ENAC 2027 como primeiro alvo de habilitação;
- manter preparação única, não curso separado para ENAC;
- aumentar margem objetiva;
- crescer produção M5–M7;
- incorporar concursos estaduais, bancas e overlays conforme editais reais;
- alvo desejado: prontidão competitiva ampla até o fim de 2027.

### Buffer competitivo — 2028
- não é prazo padrão de aprendizagem; é teto de segurança;
- campanhas estaduais específicas;
- aperfeiçoamento de discursiva/peça/oral;
- overlays e banca-alvo;
- objetivo: aprovação com posição competitiva suficiente para escolha de delegação atrativa.

## Regra final

A auditoria externa é uma fonte de hipóteses e testes, não uma autoridade. O GX só muda quando o achado:
1. sobrevive à verificação jurídica/técnica;
2. resolve um risco real;
3. é compatível com as ferramentas efetivamente acessíveis;
4. melhora a probabilidade de aprovação ou reduz carga executiva;
5. não cria mais dívida operacional do que benefício.
