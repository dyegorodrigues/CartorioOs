# ENAC 2026.2 — Revalidação do baseline oficial

Data da revalidação: 28/09/2026  
Status: **OFFICIAL BASELINE REVERIFIED / NÃO É MATERIAL DE ESTUDO**

## 1. Fontes oficiais verificadas

### FGV — página do 4º ENAC 2026.2
https://conhecimento.fgv.br/exames/enac/4exame

Estado observado em 28/09/2026:
- exame listado como **Em Andamento**;
- Edital de Abertura nº 2/2026 publicado em 28/08/2026;
- ENAC 2026.2 permanece a edição-alvo corrente do projeto.

### FGV/CNJ — Edital de Abertura nº 2/2026
https://conhecimento.fgv.br/sites/default/files/concursos/minuta-edital-enac-2026.2-27.08.26-versao-final.pdf

Pontos reconfirmados no PDF oficial:
- 100 questões objetivas;
- 5 alternativas e uma resposta correta;
- matriz:
  - Notarial e Registral 60;
  - Constitucional 8;
  - Administrativo 4;
  - Tributário 4;
  - Processo Civil 2;
  - Civil 14;
  - Empresarial 4;
  - Penal 1;
  - Processo Penal 1;
  - Trabalho 1;
  - Processo do Trabalho 1.
- regra de freshness do item 8.8.1: preceitos cuja vigência tenha se iniciado menos de 90 dias antes da prova não serão objeto do exame; preceitos revogados dentro desse período poderão ser cobrados;
- Anexo I manda considerar, em todas as matérias, súmulas, recursos repetitivos e entendimento jurisprudencial dominante dos Tribunais Superiores;
- Direito do Trabalho e Direito Processual do Trabalho constam expressamente do Anexo I;
- em Trabalho, o edital destaca a figura do Notário/Registrador como empregador e reflexos da Lei 8.935/1994.

### CNJ — Resolução nº 696/2026
https://atos.cnj.jus.br/atos/detalhar/7011

Estado observado em 28/09/2026:
- Resolução nº 696, de 26/08/2026;
- situação oficial: **Vigente**;
- disciplina normas gerais dos concursos de outorga e revoga a Resolução nº 81/2009.

## 2. Reconciliation check com o GX

O baseline oficial permanece compatível com:
- `curriculum/ENAC_2026_2_CANONICAL_MATRIX.md`;
- `research/ENAC_EDITAL_MEGA_TREE_META_ANALYSIS_2026-09-14.md`;
- `research/ENAC_300_META_ANALYSIS.md`.

Foi detectado e corrigido um drift documental: a matriz canônica antiga ainda dizia que os subitens N/R aguardavam conversão. O `Curriculum & Mastery Graph` já contém:
- 11 Matérias: Node ID 1–11;
- 181 Temas: Node ID 12–192;
- 138 Subtemas N/R: Node ID 193–330.

Total estrutural: **330 nós**.

A camada ainda aberta é Microtema/Proposição e decomposição seletiva de listas internas das demais disciplinas.

## 3. Consequências operacionais

1. Não alterar a matriz-alvo usando as três edições históricas.
2. Tratar Trabalho e Processo do Trabalho como `ZERO DIRECT ENAC HISTORY`, não como irrelevantes.
3. Tratar Conhecimentos Gerais histórico como `MATRIX_DRIFT`, sem criar nó jurídico artificial.
4. Aplicar freshness por snapshot:
   - EXAM_SNAPSHOT_LAW;
   - CURRENT_LAW;
   - IMPLEMENT_BY quando houver implantação operacional.
5. Não promover norma nova para a prova apenas por ser recente: o item 8.8.1 cria uma janela expressa de 90 dias.
6. Jurisprudência superior é regra transversal expressa do Anexo I; não pode ser tratada como apêndice opcional.

## 4. Gate

Baseline oficial revalidado em fonte primária. Próxima revalidação necessária se ocorrer:
- retificação do Edital 2/2026;
- alteração da Resolução 696/2026;
- mudança relevante em ato normativo do conteúdo programático;
- novo edital/edição que substitua 2026.2 como alvo corrente.
