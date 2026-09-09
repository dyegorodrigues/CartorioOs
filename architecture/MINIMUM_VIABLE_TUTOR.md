# GX Cartório OS — Minimum Viable Tutor

Atualizado em 09/09/2026.

## Objetivo
Chegar rapidamente a um tutor que realmente ensina, testa, registra e recalibra o candidato, em vez de adiar estudo enquanto a arquitetura cresce.

O MVT não precisa possuir todo o Material Mestre nem o corpus completo reconstruído. Precisa possuir **um loop confiável e repetível**.

## Contrato mínimo
Quando o candidato disser `Começar estudo`, o sistema deve conseguir:

1. identificar o estado do candidato e o ponto da sequência atual;
2. escolher um nó estudável e justificar a escolha internamente;
3. mostrar onde ele está no mapa sem sobrecarregar;
4. ensinar a fundação mínima + conteúdo examinável;
5. inserir retrieval durante o ensino;
6. aplicar pelo menos uma questão/caso relevante;
7. classificar o erro pela causa quando houver;
8. registrar evidência de mastery e retenção;
9. definir próxima recuperação;
10. deixar o próximo passo pronto.

Se essas dez funções operam, já existe tutor. Todo o restante é melhoria incremental.

## Perfil inicial canônico do candidato
- formado em Direito;
- conhecimento jurídico competitivo atual tratado como enferrujado até evidência em contrário;
- **nenhuma exposição acadêmica/prática prévia relevante a Direito Notarial e Registral/serventias**;
- tendência de tentar compreender e memorizar tudo antes de avançar;
- precisa de forte orientação sistêmica para saber o que é fundamento, o que é examinável, como cai e qual profundidade merece investimento;
- objetivo de desempenho é teto competitivo, não corte mínimo.

Consequência: N/R começa do zero real. Erro inicial em N/R mede principalmente exposição, não capacidade.

## Primeira trilha do MVT
A primeira sequência deve combinar:

### A. Mapa global curto
Explicar:
- o que são serviços notariais e registrais;
- quais especialidades existem;
- como se conectam com Civil, Constitucional, Administrativo, Tributário, Empresarial e Processo;
- o que ENAC e concursos estaduais exigem em linhas gerais.

Não transformar isso em aula histórica longa.

### B. Regime geral / arquitetura constitucional
Primeiro contato com:
- art. 236 da Constituição;
- delegação;
- natureza privada do exercício;
- fiscalização;
- concurso;
- distinção entre delegatário, preposto, interino/substituto quando entrar no nível adequado;
- Lei 8.935/1994 como eixo de regime geral.

### C. Foundation JIT
Recuperar apenas os conceitos gerais necessários para cada passo.

Exemplos:
- serviço público/delegação;
- pessoa natural/jurídica;
- capacidade;
- negócio jurídico;
- forma/publicidade;
- direitos reais;
- obrigações;
- família/sucessões.

### D. Aplicação extrajudicial cedo
O candidato não deve passar semanas em abstração. Cada bloco relevante ganha situação concreta de serventia.

## Formato mínimo de uma unidade
### 1. Você está aqui
Uma frase de localização + objetivo observável.

### 2. Mapa
3–8 elementos centrais, apenas para criar esquema mental.

### 3. Ensino
Blocos curtos:
- ideia em linguagem natural;
- regra;
- fundamento;
- exceção/limite;
- exemplo;
- `confunde com`.

### 4. Retrieval
Pergunta sem alternativa antes de o conteúdo desaparecer da memória de trabalho.

### 5. Questão/caso
Preferência:
- questão oficial reconstruída e validada;
- ou item diagnóstico/sintético explicitamente rotulado e baseado em fonte atual.

### 6. Feedback causal
Não dizer apenas `certo/errado`.

Classificar:
- desconhecimento;
- falha de recuperação;
- confusão;
- exceção;
- competência;
- prazo;
- efeito;
- leitura;
- desatualização;
- excesso de inferência;
- falsa confiança.

### 7. Closure
2–5 recalls + uma frase `o que você deve levar desta sessão`.

## Dados mínimos por tentativa
Registrar somente o que muda decisões:
- item/nó;
- modalidade;
- resposta;
- correta/incorreta;
- confiança antes do feedback;
- necessidade de pista;
- causa do erro;
- latency aproximada quando útil;
- timestamp/intervalo;
- evidência mastery M0–M7.

Evitar telemetria ornamental.

## Mastery inicial do MVT
Usar escala canônica:
- M0 não visto;
- M1 reconhece;
- M2 recupera núcleo;
- M3 discrimina;
- M4 aplica a caso/item inédito;
- M5 produz escrito;
- M6 executa prática;
- M7 sustenta oral/reperguntas.

Retenção é separada.

## Regras para o candidato que quer `saber tudo`
O tutor deve sempre sinalizar implicitamente ou explicitamente:
- `isso é fundação`;
- `isso é regra examinável`;
- `isso é high-yield`;
- `isso é cauda, mas permanece coberto`;
- `isso é referência e não merece memorização agora`.

O candidato não deve precisar decidir isso sozinho.

## Gabarito como orientação, não promessa
O sistema é desenhado para reduzir cada classe de erro até o menor nível praticável.

Não promete 100/100 em prova futura. O alvo pedagógico é **domínio de teto**:
- cobertura integral;
- alta robustez em high-yield;
- manutenção sistemática da cauda;
- forte transferência para questões inéditas;
- precisão sob tempo;
- capacidade escrita/prática/oral.

## Gate para começar estudo real
Não esperar:
- passagem 2 das 300 inteira;
- corpus estadual completo;
- dashboard perfeito;
- Sheets;
- FSRS calibrado;
- todos os capítulos MASTER.

O MVT pode começar quando houver:
1. mapa inicial confiável;
2. primeiro cluster curricular seguro;
3. fontes oficiais atuais;
4. algumas questões/casos validados;
5. mecanismo de registro de tentativa.

## Construir enquanto ensina
Ao estudar um cluster, o GX melhora simultaneamente:
- Reconstruction Cards daquele cluster;
- material MASTER;
- REVIEW/RECALL derivados;
- mapa de dependências;
- dados pessoais do candidato.

Assim, pesquisa e estudo deixam de ser filas separadas.

## Primeira evidência que nenhum cursinho possui
Depois das primeiras sessões, o GX deve começar a aprender:
- quanto tempo o candidato leva para recuperar uma regra;
- se acerto veio de conhecimento ou eliminação;
- que tipos de confusão se repetem;
- quais explicações produzem transferência;
- quanto conteúdo decai após 1, 3, 7, 14+ dias;
- quando reconhecimento vira aplicação;
- quanto de fundamentação escrita/oral surge espontaneamente.

Esse learner model passa a competir em importância com a incidência histórica das provas.

## Próximo gate
MVT v0.1 é considerado operacional após completar uma primeira sessão real e conseguir reabrir o sistema depois dela sabendo:
- o que foi estudado;
- o que foi aprendido;
- o que falhou;
- o que revisar;
- e qual é a próxima ação.