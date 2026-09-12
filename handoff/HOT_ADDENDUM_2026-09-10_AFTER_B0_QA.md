# GX Cartório OS — HOT Addendum — 10/09/2026 — pós B0 QA

## Motivo
Durante a primeira missão piloto, o candidato detectou dois riscos reais:
1. questões sintéticas didáticas estavam sendo apresentadas com aparência de treino objetivo válido;
2. microbloco de 20–35 min podia ser interpretado como carga diária e produzir throughput incompatível com o horizonte 2027.

Também reforçou requisito autoral antigo: materiais jurídicos precisam possuir progressão lógica/modular forte para organizar teorias, classificações, autores e variantes de nomenclatura sem virar coleção de notas desconexas.

## Correções canônicas incorporadas
### 1. Assessment QA
Criado:
`research/B0_MISSION_01_QA_FAILURE_2026_09_10.md`

Achado:
- os gabaritos técnicos dos quatro itens iniciais eram juridicamente defensáveis;
- os itens eram ruins como medição de concurso por distratores óbvios, eco lexical e baixa discriminação;
- classificação: `QUESTION_DEFECT / ASSESSMENT_QUALITY_GAP`;
- não registrar mastery a partir desses itens.

`material/pilots/B0A_CONSTITUTIONAL_BOOTSTRAP_MISSION_01.md` foi corrigido. Node Check válido fica pendente de corpus/QA.

### 2. Throughput
Criado:
`architecture/THROUGHPUT_AND_COVERAGE_CONTROL.md`

Regra:
**tempo da missão != tempo diário de estudo**.

Um dia pode conter várias missões. O sistema usa coverage burn-down ponderado, velocidade real, retenção e backlog para garantir que a preparação atravesse o edital em ciclos e não fique meses lapidando um único tema.

Estratégia de ciclos:
- PASS 1: coverage/comprehension;
- PASS 2: discrimination/transfer;
- PASS 3: exam robustness;
- OUTPUT cycles seletivos;
- TARGET cycles por edital/banca/estado.

### 3. Estrutura curricular modular
Criado:
`architecture/CURRICULUM_MODULE_SYSTEM.md`

Experiência visível:
`Disciplina → Macrobloco → Módulo → Unidade → Proposição`.

Para temas com doutrina/classificações:
`problema → conceito-base → eixo de divergência → teoria A/B/C → autor/rótulo → consequência probatória → confusões`.

Inclui `Terminology Registry` para sinônimos de banca/doutrina, aliases e colisões terminológicas.

Nova falha estrutural reconhecida:
`STRUCTURE_GAP` = conteúdo pode até estar presente, mas está organizado de modo que não forma árvore mental recuperável.

## Estado do piloto
Continuar B0 em Constitucional/Poder Constituinte, mas não exigir que o candidato valide profundidade jurídica por memória residual.

Próximos passos:
1. completar question corpus real/reconstruído;
2. separar BUILD / VALIDATION / CHALLENGE;
3. refinar Proposition Map;
4. construir mapa modular do tema;
5. definir Depth Budget;
6. produzir MASTER v0.1;
7. derivar REVIEW + Q→A;
8. aplicar Node Check com itens que passaram QA;
9. medir compreensão, carga e throughput reais;
10. só então transferir padrão para N/R.

## Regra autoral preservada
O candidato não deve ser transformado em gerente do sistema. Ele recebe missões executáveis; o GX controla sequência, cobertura, revisão, questões, freshness e mudança de foco por fase do concurso.