# ENAC 300 — Corpus Gate

Atualizado em 08/09/2026.

## Marco
A passagem 1 das três edições oficiais já aplicadas do ENAC está completa no `Question Intelligence Lab`:

- ENAC 2025.1: 100/100;
- ENAC 2025.2: 100/100;
- ENAC 2026.1: 100/100;
- total lógico da passagem 1: **300/300**.

## Anulações oficiais conhecidas
- 2025.1: Q54, Q88, Q94;
- 2025.2: Q24;
- 2026.1: Q87, Q95.

Total: **6 questões anuladas em 300 itens históricos**. Elas permanecem no corpus para análise de tema, redação, ambiguidade e QA da banca, mas não entram como resposta jurídica válida nem como acerto/erro ordinário.

## Matrix drift
As três edições históricas 2025.1, 2025.2 e 2026.1 usam a mesma macrodistribuição:

- 60 Notarial e Registral;
- 14 Civil;
- 9 Constitucional;
- 4 Administrativo;
- 4 Tributário;
- 4 Empresarial;
- 2 Processo Civil;
- 1 Penal;
- 1 Processo Penal;
- 1 Conhecimentos Gerais.

A matriz-alvo atual ENAC 2026.2 muda para:

- 60 Notarial e Registral;
- 14 Civil;
- 8 Constitucional;
- 4 Administrativo;
- 4 Tributário;
- 4 Empresarial;
- 2 Processo Civil;
- 1 Penal;
- 1 Processo Penal;
- 1 Trabalho;
- 1 Processo do Trabalho.

Consequência: qualquer análise histórica deve ser **normalizada por oportunidade de exposição**, e Conhecimentos Gerais não pode contaminar o currículo atual. Trabalho e Processo do Trabalho, por outro lado, não possuem histórico ENAC próprio ainda e precisam de corpus lateral FGV/multibanca.

## O que a passagem 1 permite afirmar
Com alto grau de segurança:
1. quais assuntos gerais foram cobrados em cada item;
2. qual era a disciplina formal da banca;
3. qual foi o gabarito definitivo/anulação;
4. quais famílias de conhecimento e mecanismos de distrator parecem dominantes em cada questão;
5. onde há interdisciplinaridade ostensiva;
6. quais questões dependem de revalidação normativa forte antes de alimentar material atual.

## O que AINDA NÃO pode ser promovido
Sem QA 300 + passagem 2, não promover como canônico:
- ranking fino de incidência por microtema;
- porcentagem de cada mecanismo de distrator;
- frequência de artigo/norma/jurisprudência;
- tendência temporal quantitativa;
- `chance de cair`;
- prioridade pedagógica individual;
- afirmação de que uma questão histórica continua correta hoje.

## Meta-análise 300: pipeline obrigatório
### 1. QA estrutural
- recontar por edição;
- validar disciplinas, gabaritos e anuladas;
- detectar duplicados/bootstrap;
- auditar registros sem relação curricular.

### 2. Passage 2 semântica
Para cada item:
- Tema/Subtema/Microtema;
- norma e dispositivo decisivo;
- jurisprudência/ato CNJ decisivo;
- comando cognitivo;
- padrão do enunciado;
- mecanismo de cada distrator relevante;
- interdisciplinaridade;
- snapshot histórico;
- snapshot atual.

### 3. Normalização
Medir frequência relativa à quantidade de oportunidades por edição e à mudança de matriz.

### 4. Clustering semântico
Agrupar questões que testam a mesma habilidade jurídica mesmo quando aparecem sob rótulos de disciplina diferentes.

Exemplos esperados:
- nome/RCPN/Civil;
- garantias/Civil/RI/RTD;
- inventário/Sucessões/Notas/Tributário;
- responsabilidade/Constitucional/Administrativo/Lei 8.935;
- protesto/Empresarial/Tributário/N&R.

### 5. Perfil de banca
Separar:
- caso concreto;
- literalidade/lista;
- jurisprudência;
- norma operacional recente;
- doutrina;
- questão integrativa;
- tamanho/complexidade do enunciado;
- arquitetura dos distratores.

### 6. Eixo temporal
Comparar 2025.1 → 2025.2 → 2026.1 sem confundir mudança normativa com mudança estilística.

### 7. Predição calibrada
Somente depois das etapas anteriores. A saída deve ser probabilidade/prioridade com intervalo de confiança qualitativo, nunca profecia.

## Primeiros sinais qualitativos a testar quantitativamente
Hipóteses, não conclusões finais:
- N/R é fortemente interdisciplinar e frequentemente exige Civil embutido;
- competência, requisito e efeito jurídico parecem mecanismos de distrator recorrentes;
- normas CNJ/centrais eletrônicas/sistemas nacionais aparecem com frequência relevante;
- a FGV alterna caso concreto com questões mais literais/doutrinárias, portanto não existe um único molde;
- matérias externas são frequentemente contextualizadas em problemas próximos da atividade extrajudicial;
- garantias, desjudicialização, RCPN, RI, protesto e família/sucessões parecem formar clusters de alta conectividade.

## Freshness gate
Nenhum item histórico migra automaticamente para MASTER. Primeiro passa por:
`gabarito histórico → fundamento histórico → fonte atual → verificação de alteração → snapshot atual → material`.

## Próximo marco
Após QA e passagem 2, produzir `research/ENAC_300_META_ANALYSIS.md` e usar seus resultados como um dos insumos do grafo de prioridade, junto com edital atual, dependências pedagógicas e estado do candidato.
