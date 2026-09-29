# ENAC 300 — Auditoria de granularidade das relações curriculares

Data: 28/09/2026  
Status: **PRE-REPAIR SNAPSHOT / GOVERNANCE GATE**

## 1. Problema encontrado

A auditoria 300/300 confirmou que cobertura relacional e granularidade relacional eram duas coisas diferentes.

O corpus estava praticamente todo relacionado:
- ENAC 2025.1: 100/100 com vínculo;
- ENAC 2025.2: 99/100, com Q100 Conhecimentos Gerais intencionalmente sem vínculo;
- ENAC 2026.1: 100/100 com vínculo.

Porém a profundidade dos vínculos não era homogênea.

## 2. Granularidade por edição antes do reparo

### ENAC 2025.1
- N/R: **60/60** chegam a Subtema;
- matérias gerais: em regra chegam a Tema; alguns itens também carregam Subtema N/R transversal.

### ENAC 2025.2
- N/R: **56/60** chegam a Subtema;
- 4/60 permanecem apenas em Tema/tema externo;
- matérias gerais: em regra chegam a Tema;
- Q100 Conhecimentos Gerais: intentional unmapped / matrix drift.

### ENAC 2026.1
- N/R: **60/60 estavam apenas em Tema**, sem Subtema N/R;
- Constitucional: 9/9 apenas em Matéria;
- Administrativo: 4/4 apenas em Matéria;
- Tributário: 4/4 apenas em Matéria;
- Processo Civil: 2/2 apenas em Matéria;
- Civil: 14/14 apenas em Matéria;
- Empresarial: 4/4 apenas em Matéria;
- Penal: 1/1 apenas em Matéria;
- Processo Penal: 1/1 apenas em Matéria;
- Conhecimentos Gerais Q100 possuía vínculo derivado que requer auditoria separada.

Logo, publicar um heatmap fino por Subtema antes de normalizar 2026.1 produziria viés sistemático contra a edição mais recente.

## 3. Causa

A passagem de reparo anterior priorizou retirar órfãos e garantir localização mínima, mas 2026.1 foi ligado majoritariamente na camada pai:
- N/R → Tema;
- demais disciplinas → Matéria.

Isso é suficiente para navegação, não para incidência fina.

## 4. Regra de reparo

- preservar toda relação correta já existente;
- **adicionar** o nó oficial mais específico demonstrável;
- N/R: descer de Tema para Subtema quando houver correspondência segura com o subitem expresso do edital;
- demais disciplinas: descer de Matéria para Tema, que é a camada oficial canônica atualmente materializada;
- não criar Microtema apenas para aumentar resolução estatística;
- não forçar Conhecimentos Gerais histórico para o currículo atual;
- itens multidisciplinares podem manter mais de um vínculo, mas cada relação precisa representar conteúdo materialmente examinado;
- anuladas podem ser relacionadas para conteúdo/QA, nunca para inferir resposta jurídica correta.

## 5. Consequência estatística

Antes do reparo:
- 300 questões canônicas;
- 299 com ao menos um vínculo;
- 406 atribuições questão→nó;
- 159 nós tocados;
- mas a distribuição por nível era assimétrica por edição.

Portanto:
- **coverage completeness = PASS**;
- **granularity comparability = FAIL pré-reparo**;
- heatmap fino 3-edition = BLOCKED até normalização.

## 6. Próximo gate

1. granularizar 2026.1 N/R para Subtema;
2. granularizar 2026.1 matérias gerais para Tema;
3. resolver os 4 N/R coarse de 2025.2 quando houver subtema aplicável;
4. recontar níveis;
5. só então gerar o heatmap de nó/subtema v0.1.

