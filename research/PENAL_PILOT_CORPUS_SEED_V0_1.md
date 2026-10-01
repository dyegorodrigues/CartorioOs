# CORPUS SEED v0.1 — PILOTO PENAL
**Data:** 2026-09-30
**Uso:** engenharia de prova e validação; não é material de estudo final.

## Âncoras oficiais de escopo

### Delegado PF 2025 — Cebraspe
O edital contém:
- Introdução ao Direito Penal;
- conceito, caracteres e função;
- princípios básicos;
- relações com outros ramos;
- Direito Penal e política criminal;
- depois, Lei Penal;
- depois, Teoria Geral do Crime, incluindo bem jurídico.

A prova de Delegado inclui objetiva, três questões dissertativas + peça e prova oral. Penal integra discursiva e oral.

### ENAM 2026.1 — FGV
O edital contém:
- conceito, características e finalidade;
- princípios gerais;
- (des)criminalização e (des)penalização;
- política criminal;
- criminologia;
- relações com outros ramos;
- Constituição Penal;
- Norma Penal.

### Magistratura TJSC — FGV — Edital 44/2024
O programa penal começa por:
- conceito, funções e caracteres;
- ciências penais e disciplinas auxiliares;
- escolas/tendências;
- evolução epistemológica;
- princípios;
- bem jurídico.
O certame prevê objetiva, provas escritas e prova oral.

## Questões oficiais já localizadas

### PF 2025 — itens 52–54
Bloco específico sobre evolução da teoria do bem jurídico:
- Johann Birnbaum / ratio legis;
- bens jurídicos aparentes;
- relação entre Constituição e tutela penal.
Gabarito definitivo oficial: 52 E; 53 C; 54 E.

**Uso:** construção/validação futura do nó PEN.INT.014–017, não do microbloco 001–003.

### PC-AM Delegado 2021 — FGV
Foram localizados itens úteis para os nós adjacentes:
- garantismo;
- institutos despenalizadores;
- crítica criminológica ao sistema penal;
- história do pensamento criminológico.

**Uso:** corpus FGV de carreira policial; não contar como incidência ENAM.

### ENAM 2026.1 — FGV
A prova oficial foi localizada. As questões penais da edição estão concentradas em aplicação/casos concretos e não fornecem, por si sós, amostra suficiente para afirmar incidência baixa do bloco conceitual inicial.

## Regra estatística
Não inferir importância pela ausência de questão em uma única edição.
Para cada nó:
- coverage_signal: aparece em edital?
- observed_question_count: quantas questões oficiais localizadas?
- sample_size: tamanho do corpus relevante;
- confidence: baixa/média/alta;
- career/bank/window/phase: sempre separados.

## Held-out
O conjunto held-out será definido por microbloco antes da redação do MASTER.
Questões held-out:
- não entram na redação;
- não entram no ajuste de profundidade;
- só são abertas depois do MASTER congelado em versão de teste;
- se revelarem lacuna legítima, gera-se PATCH com registro de causa.

## Fontes oficiais
- PF 2025: https://cdn.cebraspe.org.br/concursos/PF_25/arquivos/Ed_1_PF_25_Abertura.html
- prova PF 2025: https://cdn.cebraspe.org.br/concursos/PF_25/arquivos/106_PF_001_01.pdf
- gabarito PF 2025: fonte Cebraspe oficial
- ENAM 2026.1: https://conhecimento.fgv.br/exames/enam/5exame
- TJSC Magistratura 2024: https://conhecimento.fgv.br/sites/default/files/concursos/sei_8359560_edital.pdf
