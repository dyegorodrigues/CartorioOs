# C01 Alternativo — piloto integral de experiência de estudo

> Branch experimental. `dyegorodrigues/delegado-os` permanece **READ-ONLY**.
>
> Objetivo: reconstruir **todo o Capítulo 1 do DP-01** com o mesmo patrimônio de pesquisa disponível no Claude, mas usando uma regra editorial diferente: **sequência de aprendizagem primeiro; banco e cobertura nos bastidores**.

## 1. Problema que este piloto tenta resolver

A v1.1 do Claude ficou mais agradável do que o antigo MASTER, mas cresceu para 49 páginas e passou a conter 113 perguntas progressivas, além de fechamento, questões e C/E. O corpus cresceu ainda mais: 307 questões, 5.801 cartões externos e 69 microtópicos no DP-01.

O problema não é falta de conteúdo. É **seleção e sequência**.

Uma informação pode:
- pertencer ao assunto;
- estar no DD;
- existir em dezenas de cards;
- ter aparecido numa prova de outra carreira;

e ainda assim **não merecer uma pergunta autônoma na primeira passagem de um candidato a Delegado**.

## 2. Nova regra editorial

A unidade do aluno não é construída a partir de cards.

Ela é construída nesta ordem:

**linha de raciocínio → explicação → tabela quando relacional → recuperação progressiva → questão real → produção oral/discursiva quando justificada**

O corpus é consultado **depois** para verificar:
1. se falta cobrança relevante;
2. se a banca usa uma distinção específica;
3. se algum detalhe merece subir de prioridade.

### O que fica invisível para o aluno

O backend pode guardar:
- microtópicos;
- incidência;
- carreira;
- banca;
- ano;
- status da fonte;
- dificuldade;
- distrator;
- autor;
- jurisprudência;
- relações com lei;
- milhares de cards.

Isso **não precisa aparecer como etiquetas o tempo todo**.

## 3. Quatro destinos possíveis para uma informação

### A. ENTENDER
Precisa estar na explicação para a matéria fazer sentido.

### B. RECUPERAR
Precisa ser lembrada sem consulta. Ganha pergunta própria.

### C. RECONHECER
Não precisa ser recitada espontaneamente, mas o aluno deve identificar quando aparecer numa alternativa. Fica em quadro/tabela/questão real.

### D. PRODUZIR
Precisa poder ser articulada em oral/discursiva. Ganha pergunta de resposta ampla.

Uma mesma informação pode ocupar mais de um destino.

---

# Estrutura proposta do Capítulo 1 inteiro

## Tópico 1 — Conceito de Direito Penal

### Linha de raciocínio
1. O que é Direito Penal?
2. Por que a definição fala em infração penal?
3. Quais sanções pertencem ao sistema penal?
4. Por que é ramo do Direito Público?
5. Quais são os três aspectos do conceito?
6. Como isso se conecta com controle social e limites ao poder punitivo?

### Explicação principal
Deve ser contínua, curta e autossuficiente.

### Tabela
**Formal/Estático × Material × Sociológico/Dinâmico**

Aliases aparecem no mesmo rótulo.

### Perguntas de recuperação
1. Conceitue Direito Penal em uma frase.
2. Por que se fala em infração penal e não apenas em crime?
3. Quais são as espécies de sanção penal?
4. Pena e medida de segurança podem ser cumuladas ao semi-imputável?
5. Por que o Direito Penal é ramo do Direito Público?
6. Diferencie os aspectos formal/estático, material e sociológico/dinâmico.
7. Qual o papel limitador do Direito Penal diante do poder punitivo?

### Conteúdo que NÃO ganha pergunta autônoma na primeira passagem
- quatro definições individuais de Liszt, Mezger, Welzel e Cirino;
- Direito Penal × Direito Criminal como detalhe isolado;
- três vias de Roxin, salvo se a prova-alvo justificar;
- nomenclaturas que podem ser reconhecidas no quadro sem virar memorização independente.

Esses itens permanecem no backend e podem aparecer em tabela, nota ou questão real.

---

## Tópico 2 — Características do Direito Penal

### Linha de raciocínio
A pergunta pedagógica central é: **que tipo de ciência é o Direito Penal e como ele atua?**

### Tabela-carreadora da teoria
| Característica | Significado | Não confundir |
|---|---|---|
| Cultural | ciência do dever-ser | Criminologia = ser |
| Normativa | trabalha com normas | não significa apenas “lei escrita” |
| Valorativa | seleciona e hierarquiza valores | não é valoração livre do julgador |
| Finalista | possui finalidade prática | ≠ finalismo de Welzel |
| Predominantemente sancionatória | reforça proteção de bens já reconhecidos | pode haver aspecto constitutivo |
| Fragmentária | protege apenas parcela dos bens/ataques | conecta-se à intervenção mínima |

### Perguntas de recuperação
1. Quais são as características centrais?
2. Por que Direito Penal é dever-ser e Criminologia é ser?
3. O que significa ser normativo?
4. O que significa ser valorativo?
5. Por que “finalista” aqui não é Welzel?
6. Por que se diz predominantemente sancionatório?
7. Explique fragmentariedade com um exemplo.

Sem mini-card separado para cada formulação secundária se a tabela já resolve.

---

## Tópico 3 — Objeto de proteção: bem jurídico

### Linha de raciocínio
1. O que o Direito Penal protege?
2. Quem escolhe?
3. Qual é o papel da Constituição?
4. Todo valor constitucional merece tutela penal?
5. Para que serve a teoria do bem jurídico?
6. Por que Birnbaum aparece?
7. Como reconhecer bens coletivos legítimos e bens aparentes?

### Perguntas de recuperação
1. O que é bem jurídico?
2. Quem escolhe os bens protegidos e quais são os limites?
3. Qual a dupla função da Constituição nessa seleção?
4. Todo valor constitucional exige tutela penal?
5. O que é função crítica/limitadora do bem jurídico?
6. Qual associação histórica com Birnbaum merece memória e por quê?
7. O que são bens jurídicos aparentes?
8. O que é espiritualização/desmaterialização dos bens jurídicos?

### RECONHECER, não necessariamente RECUPERAR
Binding, Liszt, concepção metodológica, Honig e demais etapas históricas entram em **uma tabela evolutiva**, não em uma sequência de cinco cards isolados.

### Aprofundamento acionado por prova
Se a prova-alvo exigir, abrir:
- Birnbaum × concepção metodológica;
- bem jurídico e funcionalismo;
- harm principle;
- funções adicionais do bem jurídico.

---

## Tópico 4 — Evolução histórica e escolas

Este é o tópico em que a evidência de Delegado justifica maior densidade.

### Linha de raciocínio
1. Fases históricas da reação penal.
2. Humanização iluminista e Beccaria.
3. Escola Clássica.
4. Escola Positiva.
5. Terza Scuola.
6. Outras escolas, apenas no nível cobrado.
7. Evolução brasileira.

### Tabela principal
**Clássica × Positiva × Terza Scuola**

Dimensões:
- livre-arbítrio/determinismo;
- conceito de crime;
- foco;
- método;
- fundamento da responsabilidade;
- função da pena;
- representantes;
- pegadinhas recorrentes.

### Perguntas de recuperação
1. Qual a sequência geral das fases históricas?
2. Por que o talião representou limitação?
3. O que muda no Período Humanitário?
4. Quais ideias de Beccaria são efetivamente relevantes para prova?
5. Compare Clássica e Positiva.
6. Quais autores centrais identificam a Escola Positiva e o que cada fase enfatiza?
7. O que a Terza Scuola tenta conciliar?
8. Qual a pegadinha sobre livre-arbítrio na Terza Scuola?
9. Qual o núcleo da Escola Moderna Alemã de Liszt?
10. Como reconhecer técnico-jurídica, Correcionalista e Defesa Social em alternativa?
11. Quais diplomas realmente estruturam a história penal brasileira?
12. Quais detalhes históricos já foram cobrados diretamente em Delegado?

### Regra especial
Escolas menores **não** recebem uma bateria de cards cada. Ganham uma tabela de reconhecimento + questões reais.

---

## Tópico 5 — Funções do Direito Penal

### Linha de raciocínio
1. Missões mediatas.
2. Missão imediata.
3. Roxin × Jakobs.
4. Demais funções.
5. Formulações controversas e armadilhas de banca.

### Tabela principal
**Roxin × Jakobs**

- bem jurídico × vigência da norma;
- funcionalismo moderado/teleológico × radical/sistêmico;
- prevenção;
- conexão com teoria do delito;
- linguagem típica de prova.

### Perguntas de recuperação
1. Como se divide a missão do Direito Penal?
2. Quais são as missões mediatas?
3. Para Roxin, qual é a missão imediata?
4. Para Jakobs, qual é a missão?
5. Qual a diferença estrutural entre os funcionalismos?
6. O que é função simbólica e por que é problemática?
7. Como tratar a função promocional sem cair na formulação expansiva rejeitada em prova?
8. Qual o sentido da ideia de Direito Penal como garantia/limite?

### RECONHECER
- universidade associada a cada autor;
- função motivadora;
- função de redução da violência;
- distinções secundárias.

Só sobem para RECUPERAR se o corpus de Delegado justificar.

---

## Tópico 6 — Classificações do Direito Penal

### Linha de raciocínio
Classificações servem para **não confundir pares**, não para criar dez miniassuntos.

### Tabela única
- fundamental × complementar;
- comum × especial;
- geral × local;
- objetivo × subjetivo;
- substantivo × adjetivo.

### Perguntas de recuperação
1. Diferencie objetivo e subjetivo.
2. O ius puniendi pertence a quem?
3. A ação penal privada transfere o direito de punir ao particular?
4. Diferencie substantivo e adjetivo.
5. O que é Direito de Intervenção de Hassemer e qual problema ele tenta resolver?

Os demais pares podem ser treinados dentro da tabela e em C/E, sem uma pergunta autônoma para cada subdivisão.

---

# Fechamento do capítulo

## Mapa em uma página
Uma página, não 14 frases arbitrárias: relações entre os seis tópicos.

## 6 perguntas-mãe
1. Conceitue Direito Penal e explique seus três aspectos.
2. Explique as características centrais e suas principais confusões.
3. Explique bem jurídico, papel constitucional e função crítica.
4. Compare Clássica, Positiva e Terza Scuola e situe Beccaria.
5. Compare Roxin e Jakobs e explique as demais funções relevantes.
6. Explique as classificações com ênfase em Direito Penal objetivo/subjetivo.

## EXAM Lab
Selecionar um conjunto pequeno e representativo de questões reais:
- uma simples/factual;
- uma questão de comparação;
- uma questão com autor;
- uma questão com meia-verdade;
- uma de bem jurídico PF 2025;
- uma de escolas recente;
- uma de funções;
- uma de história/classificação, se relevante.

O objetivo não é “mostrar muitas questões”. É mostrar **mecanismos de banca diferentes**.

## C/E
Somente itens que treinem confusões de alto valor.

## Oral
No capítulo 1, não fabricar profundidade oral artificial.

Usar:
- perguntas reais quando existirem;
- pergunta-mãe falada para tópicos nucleares;
- follow-ups somente quando houver justificativa.

---

# Orçamento de perguntas

A v1.1 atual tem 113 perguntas progressivas.

Meta do piloto integral:

| Bloco | Faixa |
|---|---:|
| Conceito | 6–7 |
| Características | 6–7 |
| Bem jurídico | 7–9 |
| Evolução/escolas | 10–13 |
| Funções | 7–9 |
| Classificações | 4–6 |
| **Total progressivas** | **40–51** |
| Perguntas-mãe | 6 |
| Questões reais comentadas | 8–10 |
| C/E | 8–12 |
| Oral/discursiva | 2–4, quando justificado |

Não é uma meta de corte mecânico. Se a evidência exigir 55, serão 55. O princípio é: **uma pergunta só existe se recuperar uma unidade cognitiva que vale recuperar.**

---

# Regra para o corpus Brainscape

Os 5.801 cartões permanecem intactos no banco.

Eles não entram no material por votação de frequência.

Cada card pode fornecer:
- formulação;
- decomposição;
- comparação;
- exemplo;
- contraexemplo;
- resposta curta;
- estilo C/E;
- pista de lacuna.

Mas o card nunca decide sozinho que um conteúdo merece ser estudado.

---

# Regra para a prova

Questão oficial tem duas funções:

1. **peso**: ajuda a decidir o que merece memória;
2. **forma**: mostra como a banca transforma conhecimento em distrator.

Uma questão de outra carreira não pesa igual a uma questão de Delegado.

Uma questão oral de Magistratura não transforma automaticamente o conteúdo em obrigação de oral de Delegado.

---

# Critério de sucesso do piloto

O C01 alternativo só vence se o aluno conseguir:

1. ler em sequência sem sensação de fragmentação;
2. explicar os seis blocos sem consultar;
3. reconhecer detalhes secundários quando a banca os apresenta;
4. resolver as questões reais relevantes;
5. saber o que é essencial e o que é mera referência;
6. terminar o capítulo com sensação de progresso, não de catálogo infinito.

O banco pode crescer indefinidamente.

**A superfície de estudo não.**
