# ENAC 300 — QA estruturado do Question Intelligence Lab

> **Governança 28/09/2026:** este arquivo preserva o checkpoint histórico da Passagem 1. Para completude relacional/taxonômica atual, usar `research/ENAC_300_META_ANALYSIS.md` e `research/ENAC_LINK_REPAIR_AND_BLIND_QA_2026-09-28.md`. Não executar como pendência atual os próximos passos antigos abaixo.

Data: 14/09/2026  
Status: **VERIFIED DATABASE QA / NÃO É AINDA META-ANÁLISE 300 COMPLETA**

## 1. Objetivo

Auditar diretamente o data source `GX Cartório — Question Intelligence Lab` antes de publicar estatísticas agregadas da frente “Esquema do Edital ENAC”.

Esta checagem mede **estado do banco e anotações existentes**. Ela não substitui reconstrução jurídica de cada item nem revisão cega da classificação.

## 2. Recontagem canônica

Consulta ao data source com:

- `Origem do corpus = ENAC oficial`;
- `Excluir das métricas != true`.

Resultado:

| Edição | Registros canônicos |
|---|---:|
| ENAC 2025.1 | 100 |
| ENAC 2025.2 | 100 |
| ENAC 2026.1 | 100 |
| **Total** | **300** |

Todos os 300 estão com `Validação = Oficial`.

Resultado histórico:

- 294 = `Não feita`;
- 6 = `Anulada`.

Isto é correto para o estado do projeto: o usuário ainda não iniciou estudo nem respondeu esse corpus. Não interpretar `Não feita` como desempenho.

## 3. Distribuição disciplinar confirmada no banco

| Disciplina | n |
|---|---:|
| Notarial e Registral | 180 |
| Civil | 42 |
| Constitucional | 27 |
| Administrativo | 12 |
| Tributário | 12 |
| Empresarial | 12 |
| Processo Civil | 6 |
| Penal | 3 |
| Processo Penal | 3 |
| Conhecimentos Gerais | 3 |
| Trabalho | 0 |
| Processo do Trabalho | 0 |
| **Total** | **300** |

Essa distribuição corresponde às três matrizes históricas. Trabalho e Processo do Trabalho só entram na matriz-alvo 2026.2.

## 4. Gap crítico de ligação curricular

### Relação `Nós do currículo`

| Edição | COM_LINK | SEM_LINK |
|---|---:|---:|
| ENAC 2025.1 | 0 | **100** |
| ENAC 2025.2 | 72 | **28** |
| ENAC 2026.1 | 99 | **1** |
| **Total** | **171** | **129** |

Logo:

- **57,0%** do corpus está ligado a pelo menos um nó;
- **43,0%** ainda está órfão na árvore curricular;
- qualquer heatmap por nó que ignore isso é materialmente enviesado.

Prioridade de reparo: ENAC 2025.1 inteiro, depois 28 itens de 2025.2 e o item restante de 2026.1.

## 5. Gap crítico de família da fonte

### `Família da fonte`

| Família | n em 300 |
|---|---:|
| Constituição/lei/código | 77 |
| Mista | 43 |
| CNJ/Corregedoria | 33 |
| STF/STJ/TJ | 31 |
| Regulação operacional | 13 |
| Doutrina | 3 |
| **Vazio** | **100** |

A quebra por edição mostra que os **100 vazios são exatamente o ENAC 2026.1**.

Entre os 200 itens anotados de 2025.1 + 2025.2, a distribuição descritiva é:

- Constituição/lei/código: 77/200 = **38,5%**;
- Mista: 43/200 = **21,5%**;
- CNJ/Corregedoria: 33/200 = **16,5%**;
- STF/STJ/TJ: 31/200 = **15,5%**;
- Regulação operacional: 13/200 = **6,5%**;
- Doutrina: 3/200 = **1,5%**.

**Não generalizar ainda para ENAC 300.** Esses números descrevem somente as duas edições com o campo preenchido e refletem a taxonomia Passagem 1, não necessariamente todas as fontes relevantes de cada questão.

## 6. Gap de mecanismos de distrator

### Cobertura do campo

| Edição | COM_TAG | SEM_TAG |
|---|---:|---:|
| ENAC 2025.1 | 100 | 0 |
| ENAC 2025.2 | 100 | 0 |
| ENAC 2026.1 | 0 | **100** |

Portanto nenhuma porcentagem de distratores deve ser rotulada `ENAC 300` antes de anotar 2026.1 e fazer QA da consistência dos rótulos.

### Distribuição preliminar em 2025.1 + 2025.2

O campo é multi-select: uma questão pode receber mais de um mecanismo. Denominador para `% de questões` = 200.

| Mecanismo | Questões com tag | % das 200 |
|---|---:|---:|
| Requisito | 155 | 77,5% |
| Efeito jurídico | 133 | 66,5% |
| Competência | 63 | 31,5% |
| Exceção | 57 | 28,5% |
| Conceito próximo | 56 | 28,0% |
| Literalidade/lista | 51 | 25,5% |
| Prazo/momento | 33 | 16,5% |
| Judicialização | 19 | 9,5% |
| Responsabilidade | 19 | 9,5% |
| Legitimidade | 10 | 5,0% |

Esses percentuais não somam 100%, pois as tags não são mutuamente exclusivas.

### Estabilidade entre as duas edições anotadas

2025.1:
- requisito 82;
- efeito jurídico 74;
- competência 34;
- exceção 29;
- conceito próximo 24;
- literalidade/lista 20;
- prazo/momento 14;
- judicialização 12;
- responsabilidade 6;
- legitimidade 4.

2025.2:
- requisito 73;
- efeito jurídico 59;
- conceito próximo 32;
- literalidade/lista 31;
- competência 29;
- exceção 28;
- prazo/momento 19;
- responsabilidade 13;
- judicialização 7;
- legitimidade 6.

Leitura permitida: **requisito** e **efeito jurídico** aparecem como os dois mecanismos mais difundidos em ambas as edições anotadas. Competência/exceção/conceito próximo/literalidade formam um segundo grupo relevante. Isso é um sinal consistente de duas provas, não ainda uma estatística final do DNA FGV.

## 7. Consequência para a meta-análise

A meta-análise antiga estava correta em segurar percentuais agregados. Agora sabemos exatamente por quê:

1. 129/300 itens ainda sem ligação curricular;
2. 100/300 sem família de fonte;
3. 100/300 sem mecanismo de distrator;
4. Passagem 1 ainda não contém reconstrução alternativa por alternativa em escala 300/300.

Por outro lado, já é legítimo promover como fatos:

- 300 registros canônicos reconciliados;
- distribuição disciplinar;
- 6 anulações;
- estado de completude de cada campo;
- distribuições **parciais explicitamente denominadas 200/200**;
- estabilidade qualitativa de `requisito` e `efeito jurídico` nas duas edições já anotadas.

## 8. Reparação objetiva, sem reabrir arquitetura

Ordem:

1. preencher `Nós do currículo` dos 129 órfãos;
2. preencher `Família da fonte` em ENAC 2026.1;
3. preencher `Mecanismo do distrator` em ENAC 2026.1;
4. executar amostra cega de classificação contra cadernos oficiais;
5. só então recalcular os agregados 300/300;
6. iniciar Reconstruction Cards prioritários, não reconstrução compulsiva em ordem numérica.

## 9. Regra de publicação

Todo número futuro deve declarar o denominador e o nível de completude do campo. Exemplos:

- correto: `Requisito aparece em 155/200 itens com distratores anotados nas edições 2025.1–2025.2`;
- incorreto: `77,5% das questões ENAC usam requisito`.

Essa diferença impede que o dashboard transforme ausência de anotação em ausência de fenômeno.
