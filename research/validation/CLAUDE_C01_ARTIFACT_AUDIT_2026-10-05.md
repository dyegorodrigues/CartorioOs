# Auditoria comparativa — material Claude × MASTER C01
**Data:** 05/10/2026
**Status:** decisão editorial
**Base analisada:** PDF de 32 páginas + CSV de 86 pares pergunta/resposta + fonte editável HTML/CSS/Python fornecidos pelo usuário.

## Veredito executivo

O material Claude está **mais próximo do produto didático desejado** do que o MASTER candidato V1 produzido pelo Tutor OS.

Isso não significa que seu conteúdo jurídico esteja integralmente correto ou suficiente. Significa que sua **gramática de estudo** é superior para o usuário:
- fluxo por tópico;
- quadro “Em 1 minuto”;
- explicação suficiente antes da síntese;
- tabelas que carregam teoria;
- destaques visuais;
- callouts “Atenção / Não confunda / Complemento / Delegado+”;
- perguntas imediatamente após o tópico;
- fechamento com revisão-mãe, questões comentadas e C/E;
- pipeline fonte editável → PDF + CSV.

O MASTER V1 do Tutor OS falhou principalmente por **compressão precoce e exposição da arquitetura interna ao aluno**.

## O que o Claude acertou

### 1. Sequência editorial
Cada tópico segue aproximadamente:
1. Em 1 minuto;
2. explicação;
3. tabela/quadro;
4. aprofundamento/pegadinha;
5. perguntas do tópico.

Isso reduz carga de navegação.

### 2. Tabelas como corpo do conteúdo
As tabelas não aparecem apenas como “resumo final”; elas carregam explicação.
É exatamente a lógica das tabelas estratégicas de alta densidade do usuário.

### 3. Recuperação ativa logo após aprender
As 75 perguntas tópicas acompanham a matéria. O CSV contém 86 pares:
- 75 perguntas progressivas;
- 11 perguntas-mãe de revisão.

A mediana das respostas tópicas é ~172 caracteres; as respostas-mãe são muito mais densas (~579 caracteres de mediana). Há, portanto, duas granularidades reais.

### 4. Camadas de revisão
- pergunta curta durante o tópico;
- questionário Passo-like ao fim;
- questões reais;
- C/E autoral;
- resumo em 12 frases.

A ideia de várias velocidades é boa.

### 5. Rendering/pipeline
A fonte editável possui CSS reutilizável com componentes:
- `min1`
- `cmp`
- `atc`
- `comp`
- `dlg`
- `dica`
- `nc`
- `caiu`
- `lembra`
- `cards`

O build numera cartões automaticamente, gera o CSV e renderiza PDF A4 com Playwright.
Isso é aproveitável como protótipo de renderer.

## O que o Claude ainda errou ou simplificou demais

### A. Terza Scuola
O quadro afirma responsabilidade moral associada a “livre-arbítrio”.
A auditoria independente já mostrou que, na formulação de Carnevale, há responsabilidade moral **sem fundá-la no livre-arbítrio clássico**, com determinismo psicológico.

**Ação:** corrigir tabela, perguntas e revisão final.

### B. Função promocional
O material apresenta de forma linear “instrumento de transformação social”.
A PC-RS/Delegado 2025 considerou incorreta formulação expansiva dessa natureza quando colocada como missão que supera proteção de bens jurídicos.

**Ação:** manter como formulação doutrinária controvertida, com alerta de prova.

### C. Terceira via
O texto trata “reparação = 3ª via” de modo quase classificatório e cita arrependimento posterior/composição civil como exemplos brasileiros.
A ideia é roxiniana/doutrinária e sua presença normativa brasileira é fragmentária; não deve parecer terceira espécie legal consolidada de sanção.

### D. Ius puniendi
A classificação diz que o Direito Penal subjetivo “nasce quando a lei penal é violada”.
Mais preciso:
- ius puniendi em abstrato existe com a norma incriminadora;
- com o fato punível surge a pretensão punitiva concreta.

### E. Natureza constitutiva
“Protege interesses que nenhum outro ramo regula” é uma simplificação perigosa.
Prova recente rejeitou a ideia de criação autônoma e irrestrita de novos bens jurídicos.

### F. Regras × princípios
“Regras rígidas/fechadas; princípios abertos que admitem flexibilização” é didaticamente sedutor, mas tecnicamente esquemático demais e não é necessário para definir Direito Penal neste ponto.
Pode criar um desvio de teoria geral do Direito.

### G. Jakobs
Trechos como “sem direito às garantias” e algumas linhas da tabela moderado/radical, dualista/monista, “quem se adapta a quem” são fórmulas fortes de cursinho.
Devem ser auditadas e contextualizadas como descrição da construção teórica, não prescrição normativa nem consenso.

### H. Direito de Intervenção
A Lei de Improbidade como “exemplo brasileiro” deve ser rotulada como aproximação/analogia doutrinária, não implementação formal da teoria de Hassemer.

### I. Critérios classificatórios variáveis
“Comum × especial” e outros pares variam conforme o autor.
A própria edição reconhece critério alternativo. O material final deve registrar a variação no mesmo quadro, não em rodapé tímido.

## Problemas do MASTER V1 do Tutor OS

1. **Compressão excessiva:** 25 perguntas para todo o C01 ficaram insuficientes para o usuário que prefere aprender/reaprender por Q&A.
2. **Cabeçalhos artificiais:** “árvore mais básica primeiro”, “camada Delegado” etc. soam como documentação de engenharia, não como material de estudo.
3. **Tabela com aliases mal desenhada:** “Formal” e “Estático” devem aparecer na mesma célula/rótulo, não em coluna “também chamado”.
4. **Pouca explicação antes da síntese:** o leitor precisa inferir relações que deveriam ser ensinadas.
5. **Pouca integração de perguntas no corpo:** o Question Tree ficou no JSON, invisível na experiência de estudo.
6. **Destaques visuais fracos:** palavras-chave, qualificadores e exceções não estavam marcados com densidade suficiente.
7. **Modelo ainda parecia resumo:** boa auditoria, má experiência de primeira aprendizagem.

## Decisão

O MASTER V1 deixa de ser candidato principal de experiência do aluno.

Ele continua valioso como:
- fonte de Claims auditados;
- correções jurídicas;
- radar de prova;
- camada advanced;
- source map.

A nova versão deve usar a **gramática didática do Claude como referência de experiência**, mas reconstruída sobre o conteúdo auditado do Tutor OS.

## Nova gramática do aluno

### Por tópico
1. **EM 1 MINUTO**
2. teoria explicada em blocos curtos
3. **TABELA ESTRATÉGICA DE ALTA DENSIDADE** quando houver relação/comparação
4. **NÃO CONFUNDA / ATENÇÃO / CAIU / RECONEXÃO**
5. **PERGUNTAS PROGRESSIVAS DO TÓPICO**
6. opcional: resposta-relâmpago dentro da resposta, não como substituta

### Ao fim do capítulo
1. mapa de revisão
2. 8–15 perguntas-mãe Passo-like
3. EXAM Lab com questões reais comentadas alternativa por alternativa
4. C/E autoral derivado de distratores reais
5. bloco oral/discursivo
6. plano de revisão espaçada futuro

## Política de quantidade de perguntas

Não fixar “25” nem “75”.

Cada pergunta recebe função:
- ensinar;
- recuperar;
- precisão;
- contraste;
- aplicar.

Durante a primeira aprendizagem, podem existir perguntas mais granulares.
Para revisão espaçada, o sistema seleciona subconjunto CORE + erros do aluno + itens de alta incidência.

Assim, abundância de perguntas não vira 900 revisões diárias.

## Regra visual para aliases
Usar:
- **Formal / Estático**
- **Sociológico / Dinâmico**
- **Objetivo / ius poenale**
- **Subjetivo / ius puniendi**

Evitar coluna exclusiva “também chamado” quando o alias cabe no próprio rótulo.

## Renderer
A fonte HTML/CSS/Python do Claude é boa prova de conceito.
O Tutor OS deve absorver:
- componentes de callout;
- numeração automática;
- geração PDF;
- export CSV.

Mas o conteúdo canônico continua separado do renderer.
