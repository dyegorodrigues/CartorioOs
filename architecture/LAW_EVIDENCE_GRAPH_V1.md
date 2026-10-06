# LAW / JURISPRUDENCE EVIDENCE GRAPH V1
**Data:** 06/10/2026
**Status:** arquitetura vigente para lei seca ativa, questões e jurisprudência

## 1. Objetivo
Permitir que cada questão, alternativa, artigo, súmula, precedente e comentário se conectem sem duplicação desnecessária.

O sistema deve responder nos dois sentidos:
- **questão → qual artigo/julgado resolve?**
- **artigo/julgado → quais questões já cobraram isso e como?**

## 2. Não é uma “mega tabela única”
São objetos ligados por IDs.

### QUESTION
- question_id
- prova/banca/cargo/ano/fase
- enunciado
- gabarito
- dificuldade
- microtópicos
- claim_ids
- snapshot jurídico
- source oficial

### OPTION
Uma linha por alternativa/assertiva:
- option_id
- question_id
- texto
- correta/incorreta
- mechanism
- legal_basis_ids
- case_law_ids
- claim_ids
- distractor_type
- commentary

### LEGAL_PROVISION
- provision_id
- diploma
- artigo
- parágrafo
- inciso
- alínea
- texto oficial
- vigência
- valid_from / valid_to quando histórico
- official_url
- aliases
- claim_ids

### CASE_LAW
- case_law_id
- tribunal
- tipo: súmula/tema/repetitivo/informativo/acórdão
- número
- tese
- data
- status
- dispositivo(s) relacionados
- official_url
- claim_ids

### DOCTRINE
Só quando necessária:
- author/theory
- statement
- source
- confidence
- exam relevance

## 3. Link no nível da alternativa
**Sim, quando houver fundamento jurídico identificável.**

Exemplo:
Q123 alternativa B
→ CP art. 7º, II, b
→ princípio da nacionalidade ativa
→ microtópico extraterritorialidade condicionada
→ distractor: troca por nacionalidade passiva

Não forçar um artigo para alternativa puramente doutrinária.

## 4. Evidência primária × enriquecimento
Cada alternativa pode ter:
- **primary_basis**: dispositivo/tese que resolve a alternativa;
- **supporting_basis**: outros artigos/julgados que ajudam;
- **commentary_basis**: doutrina/explicação.

Isso evita ligar vinte artigos a tudo.

## 5. Lei seca ativa
A partir do grafo, o sistema gera por artigo:

### Exemplo de tela/bloco
**CP, art. 7º, II, b**
1. texto oficial;
2. palavras-chave destacadas;
3. microexplicação;
4. nomenclaturas/aliases;
5. jurisprudência relacionada;
6. questões reais por dificuldade;
7. C/E autoral;
8. distratores recorrentes;
9. taxa de acerto futura do usuário;
10. próxima revisão.

## 6. Escada de dificuldade por artigo/julgado
- **L0 literal**: completar/reconhecer palavra;
- **L1 C/E direto**;
- **L2 diferença/condição/exceção**;
- **L3 múltipla escolha com distrator**;
- **L4 caso prático**;
- **L5 integração com outro artigo/jurisprudência**;
- **L6 discursiva/oral**.

Assim o mesmo artigo pode aquecer e depois aprofundar.

## 7. Fontes de inspiração, não para copiar
- Decorando a Lei Seca: questão diretamente ligada a artigo/parágrafo/inciso; fundamento destacado; jurisprudência/súmulas.
- Estudo Lei Seca (ELS): legislação + jurisprudência + questões na mesma tela.
- LeiJuris: artigo/julgado → múltipla escolha, C/E, discursiva, oral e reversa, sempre ancorado na fonte.
- PROLegis: mapa de incidência por artigo/banca/carreira.
- DD LEGIS / Mapa da Lei Seca: literalidade + destaques + comentários + jurisprudência + mapa de incidência.

## 8. DD LEGIS encontrado no Drive Russgod
Fontes já localizadas:
- pasta **DD LEGIS**;
- **D_CP Comentado completo**, atualizado até 08/12/2025;
- **Caderno de Lei Seca**;
- **Mapa da Lei Seca — Delegado de Polícia**;
- cadernos extensivos DD/MP.

O DD LEGIS já usa:
- incidência por dispositivo;
- destaque de palavras;
- comentários doutrinários;
- súmulas/jurisprudência;
- “não confunda”;
- exemplos;
- conexão direta artigo → explicação.

Isso é forte referência para nosso modo lei seca.

## 9. Regra de ingestão
Não enriquecer tudo de uma vez.

### Passo A
Ingerir questão com metadados básicos.

### Passo B
Classificar microtópico/Claim.

### Passo C
Vincular **primary_basis** da questão/alternativa quando evidente.

### Passo D
Adicionar jurisprudência/súmula apenas quando realmente necessária.

### Passo E
Enriquecer alternativas relevantes e distratores.

Dessa forma a mineração flui e o grafo cresce incrementalmente.

## 10. Histórico jurídico
Questões antigas preservam:
- fundamento na data da prova;
- gabarito histórico;
- estado jurídico atual;
- flag `changed_since_exam`.

O sistema pode ensinar:
“à época era X; hoje é Y”.

## 11. O que fica invisível ao aluno
Toda complexidade relacional fica no backend.

Na superfície o aluno vê apenas:
- artigo;
- grifo;
- explicação;
- questão;
- gabarito/fundamento;
- jurisprudência quando necessária;
- próxima revisão.

## 12. Benefício
Esta estrutura não aumenta a bagunça. Ela evita bagunça porque cria **um único grafo de evidência** para:
- teoria;
- lei seca;
- jurisprudência;
- objetiva;
- C/E;
- discursiva;
- oral;
- revisão adaptativa.

A complexidade fica na máquina; a experiência fica simples.
