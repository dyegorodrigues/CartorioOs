# ENAC 2026.1 — Repair de taxonomia do Question Intelligence Lab

Data: 14/09/2026  
Status: **BATCH CONCLUÍDO / RECONTAGEM SQL GLOBAL PENDENTE POR COTA DO NOTION**

## Objetivo

Reparar as lacunas identificadas no QA estruturado do corpus ENAC:

- `Família da fonte` vazia em 100/100 itens do ENAC 2026.1;
- `Mecanismo do distrator` vazio em 100/100 itens do ENAC 2026.1;
- 1 item de 2026.1 sem relação curricular (Q100).

O batch foi executado contra o caderno oficial Tipo 1 do 3º ENAC 2026.1, com leitura visual das páginas do PDF oficial da FGV e preservação dos registros existentes.

## Resultado operacional

### Relação curricular

A Q100 — `Nepotismo na Carta de Pero Vaz de Caminha` — foi ligada a:

- `ADM 7 — Princípios constitucionais da Administração Pública`;
- `NTR 3.8 — Decisões e atos normativos no âmbito do CNJ`.

Após essa gravação, consulta estruturada ainda disponível naquele momento confirmou:

- ENAC 2026.1 `curriculo_vazio = 0`.

Portanto, **2026.1 está 100/100 ligado a pelo menos um nó curricular**.

### Família da fonte + mecanismos do distrator

Foram revisadas e gravadas individualmente as Q1–Q100 do ENAC 2026.1, atribuindo:

- uma `Família da fonte` predominante;
- um ou mais `Mecanismo do distrator` conforme a taxonomia existente.

A classificação foi feita por conteúdo oficial, não por preenchimento automático ou extrapolação de matriz.

Famílias possíveis preservadas:

- Constituição/lei/código;
- CNJ/Corregedoria;
- STF/STJ/TJ;
- Doutrina;
- Regulação operacional;
- Mista.

Mecanismos possíveis preservados:

- Competência;
- Requisito;
- Prazo/momento;
- Efeito jurídico;
- Legitimidade;
- Exceção;
- Judicialização;
- Responsabilidade;
- Literalidade/lista;
- Conceito próximo.

## QA de gravação

A gravação não foi inferida por batch opaco: cada atualização retornou sucesso individual.

Foram também relidos registros de extremos/blocos distintos após a escrita, inclusive:

- Q61, Constitucional: `Família da fonte = Mista`; mecanismos `Competência`, `Conceito próximo`, `Efeito jurídico`; relação curricular preservada;
- Q99, Processo Penal: `Família da fonte = Mista`; mecanismos `Requisito`, `Exceção`, `Conceito próximo`; relação curricular preservada;
- Q100 foi relida após o reparo e preservou os dois vínculos curriculares + taxonomia nova.

## Limite de verificação

Após as gravações, o recurso `Query Data Source` do workspace Notion atingiu a cota de uso do plano atual. Por isso **não foi possível executar a recontagem SQL final 300/300 nesta mesma sessão**.

Não interpretar isso como falha das gravações: as ações individuais retornaram sucesso e amostras foram relidas. Mas, metodologicamente, o selo `300/300 aggregated recount` permanece pendente até que a consulta estruturada volte a estar disponível.

Regra: não recalcular percentuais globais de fonte/distrator por memória ou soma manual enquanto essa recontagem não for executada.

## Fonte oficial usada

- FGV — 3º ENAC 2026.1, página do exame;
- FGV — caderno oficial Tipo 1;
- gabarito definitivo já preservado no Question Intelligence Lab.

PDF oficial:
`https://conhecimento.fgv.br/sites/default/files/concursos/enac-2026-1-enac-2026-1-tipo-1-2.pdf`

## Estado após o batch

### Fechado

- 2026.1: 100/100 relações curriculares;
- 2026.1: repair individual de 100/100 famílias de fonte executado;
- 2026.1: repair individual de 100/100 mecanismos de distrator executado;
- Q100 histórica de Conhecimentos Gerais mantida como histórica, sem forçar sua disciplina removida para a matriz 2026.2.

### Ainda pendente

1. recontagem estruturada final das anotações 300/300 quando a cota do Notion permitir;
2. 100 relações curriculares faltantes do ENAC 2025.1;
3. 28 relações curriculares faltantes do ENAC 2025.2;
4. QA cego amostral direto contra cadernos oficiais;
5. depois disso, primeiro heatmap quantitativo por nó/cluster com denominador completo;
6. Reconstruction Cards priorizados por conectividade, não em ordem numérica compulsiva.

## Consequência

A maior assimetria interna do corpus foi removida: o ENAC 2026.1 não deve mais ser tratado como edição sem taxonomia de fonte/distrator.

O próximo gargalo passa a ser **questão → nó curricular nas duas edições mais antigas**, especialmente 2025.1.
