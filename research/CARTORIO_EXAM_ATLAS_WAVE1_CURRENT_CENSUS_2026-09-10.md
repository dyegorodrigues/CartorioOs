# GX Cartório OS — Cartório Exam Atlas — Wave 1 Current Census

Data do snapshot: 2026-09-10
Status: CENSO INICIAL VERIFICADO / não exaustivo histórico
Objetivo: mapear o cenário contemporâneo de concursos de outorga e as bancas efetivamente ativas para orientar coleta de provas, perfis de cobrança e priorização de corpus.

## Regra de proveniência
- A = CNJ / TJ / banca oficial
- B = associação institucional / entidade oficial correlata
- C = plataforma secundária confiável o suficiente para descoberta
- D = material comercial / marketing

Este arquivo usa A sempre que disponível.

## Baseline nacional
Fonte A: Resolução CNJ 696/2026, vigente em 10/09/2026.
https://atos.cnj.jus.br/atos/detalhar/7011

Consequências estruturais:
- concurso estadual: objetiva eliminatória e sem peso final, substituível pela habilitação no ENAC nos termos da Resolução;
- discursiva = 70% da nota final;
- oral = 25%;
- títulos = 5%;
- a preparação não pode pressupor que todo concurso estadual manterá objetiva própria quando o ENAC puder substituí-la.

## Fonte nacional de inventário
Painel CNJ de acompanhamento de concursos cartorários:
https://concursos-serventias.cloud.cnj.jus.br/concursos

O painel, no snapshot de 10/09/2026, lista concursos novos, inscrições abertas, em andamento, suspensos e concluídos em uma base nacional única.

## Onda contemporânea verificada — 2024–2026

| UF | Concurso / edital-base | Banca | Estado em 10/09/2026 | Evidência principal | Uso no Atlas |
|---|---|---|---|---|---|
| RS | IV concurso / 2026 | FGV | inscrições reabertas / em andamento | FGV + CNJ | C1 atual, futura objetiva/escrita/oral |
| MS | VI concurso / Ed. 01/2025 | FGV | em andamento; objetiva e escrita/prática já realizadas | FGV + CNJ | C1 ouro: objetiva + espelho escrita/prática |
| RN | concurso notarial 2025 | FGV | em andamento; escrita/prática realizada; oral em 2026 | FGV + CNJ | C1 ouro cross-phase |
| ES | concurso notarial 2025 | FGV | em andamento / fases avançadas | TJES/FGV + CNJ | C1 cross-phase |
| BA | concurso 2025 | Cebraspe | em andamento; escrita/prática realizada | TJBA/Cebraspe + CNJ | C1 ouro para discursiva/peça |
| MT | concurso 2025 | Cebraspe | em andamento | Cebraspe + CNJ | C1 atual |
| RO | VII concurso 2025 | Cebraspe | em andamento; oral já realizada/resultado provisório | TJRO/Cebraspe + CNJ | C1 ouro cross-phase |
| RR | II concurso 2025 | Cebraspe | em andamento; escrita/prática realizada | Cebraspe + CNJ | C1 atual |
| CE | concurso 2025 | Cebraspe | suspenso | TJCE/Cebraspe + CNJ | C1 estrutural, cuidado com status |
| PA | II concurso / Ed. 001/2025 | IESES | em andamento com escrita/prática suspensa | IESES + CNJ | C1 multibanca; objetiva disponível |
| PB | II concurso / Ed. 01/2024 | Consulplan | concurso contemporâneo | TJPB + CNJ | C1/C2 recente Consulplan |
| MG | Ed. 1/2024 | Consulplan | nulidade parcial/suspensão em 2026 | CNJ/TJMG/Consulplan | C1 estrutural; corpus com cautela processual |
| SP | 13º concurso | Vunesp | concluído | Vunesp + CNJ | C2 recente Vunesp |

## Contagem preliminar por banca no conjunto acima
Não é ranking histórico. É apenas a onda contemporânea selecionada.

- Cebraspe: BA, MT, RO, RR, CE = 5
- FGV: RS, MS, RN, ES = 4
- Consulplan: PB, MG = 2
- IESES: PA = 1
- Vunesp: SP = 1

Conclusão provisória: FGV e Cebraspe merecem prioridade alta na engenharia de banca, mas o GX NÃO deve inferir dominância histórica somente desta onda. Consulplan, IESES e Vunesp precisam permanecer no corpus de robustez.

## Evidência de que a arquitetura de fases está mudando
### BA / Cebraspe 2026
O edital contemporâneo inicia a etapa avaliativa diretamente com prova escrita e prática, já no contexto em que a habilitação nacional pode substituir a objetiva estadual.

Formato da escrita/prática verificado no edital:
- 5 horas;
- dissertação: até 30 linhas, 4,0 pontos;
- peça prática: até 90 linhas, 4,0 pontos;
- 2 questões discursivas: até 15 linhas cada, 1,0 ponto por questão;
- legislação não comentada permitida, conforme regras do edital.

Implicação GX: o runtime deve ter `CONTEST TARGET MODE`. Após ENAC, um edital real pode exigir aumento abrupto de OUTPUT sem uma nova etapa objetiva estadual intermediária.

### MS / FGV 2026
A página oficial da FGV disponibiliza:
- prova objetiva;
- gabaritos e recursos;
- prova escrita e prática;
- espelho de correção;
- resultado da escrita/prática.

Implicação GX: TJMS 2026 é um corpus de altíssimo valor porque permite conectar `proposição objetiva → produção escrita/prática → espelho` dentro da mesma seleção.

### RN / FGV 2026
A página oficial disponibiliza prova escrita/prática e documentação de prova oral. É outro candidato forte para corpus cross-phase.

### RO / Cebraspe 2026
O concurso contemporâneo chegou à prova oral em 2026. Serve para estudar progressão Cebraspe escrita/prática → oral.

## Prioridade de aquisição de corpus — Wave 2
### Tier A — capturar primeiro
1. TJMS/FGV 2026: objetiva + escrita/prática + espelho.
2. TJRN/FGV 2026: escrita/prática + oral; recuperar objetiva/ENAC relation conforme edital.
3. TJBA/Cebraspe 2026: escrita/prática + padrões de correção.
4. TJRO/Cebraspe 2025/26: objetiva + escrita/prática + oral.
5. TJRR/Cebraspe 2025/26: objetiva + escrita/prática.
6. TJPA/IESES 2026: objetiva + gabarito.

### Tier B
7. TJPB/Consulplan 2024/25.
8. TJSP/Vunesp 13º concurso.
9. TJES/FGV 2025.
10. TJMG/Consulplan 2024/26, mantendo metadado de nulidade/suspensão.
11. TJCE/Cebraspe 2025, mantendo metadado de suspensão.
12. TJRS/FGV 2026 à medida que as provas surgirem.

## Estrutura de registro por prova
Cada caderno deve produzir:
- exam_id;
- UF/TJ;
- banca;
- edital-base;
- modalidade: provimento/remoção;
- fase;
- data;
- status jurídico da prova;
- questão;
- gabarito/espelho;
- provenance;
- disciplina;
- nó;
- proposições examinadas;
- fonte normativa/jurisprudencial;
- tipo cognitivo;
- tipo de distrator;
- dificuldade estimada;
- necessidade de memorização;
- nível P1/P2/P3;
- se foi usada em BUILD, VALIDATION, HELD-OUT ou CHALLENGE.

## Anti-contaminação histórica
Concursos antigos continuam valiosos para:
- recorrência;
- aliases;
- formatos;
- jurisprudência histórica;
- DNA de banca.

Mas toda questão antiga deve passar por revalidação jurídica antes de entrar em treino atual. Questão superada pode sobreviver apenas como `FORM/DECOY EXAMPLE`, jamais como regra vigente.

## Próxima ação
Construir Wave 2 com ingestão de cadernos/espelhos oficiais Tier A e começar o primeiro `PROPOSITION LEDGER` real em três eixos:
1. N/R — Regime Geral / Lei 8.935 + CNN/CNJ;
2. Civil — Parte Geral/LINDB como base;
3. Constitucional — núcleo inicial e transversal.

Penal/PEN1 permanece somente como benchmark de pipeline até o Atlas do núcleo prioritário avançar.