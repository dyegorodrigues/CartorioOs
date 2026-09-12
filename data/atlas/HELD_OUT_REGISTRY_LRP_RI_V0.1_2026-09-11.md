# GX Cartório OS — Held-Out Registry RI v0.1

Snapshot: 2026-09-11
Status: ACTIVE VALIDATION REGISTRY. NÃO usar conteúdo reservado no BUILD.

## Regra
Identidade e recorte precisam ser registrados antes de abrir questões. Se busca/snippet expuser o conteúdo, a questão deixa de ser held-out independente.

## RI-H1 — IESES/TJPA 2026 Provimento
Fonte oficial pública: concurso TJPA/IESES, prova 6015 Tipo 1 e gabarito oficial.

Contaminação já conhecida por pesquisa BUILD:
- Q40–Q46 foram exibidas parcial ou integralmente em resultados de busca; não usar como validação independente.

### Recorte limpo selado
- modalidade: PROVIMENTO;
- questões: **Q47–Q60**;
- finalidade: procurar itens legítimos de Registro de Imóveis/Regime Registral não usados no BUILD;
- questões de outras disciplinas/especialidades serão OUT_OF_SCOPE;
- não abrir Q61+ nesta rodada.

Resultado após freeze `3de8a57648f75303797b0caa24b33fbcd6d174de`:
- Q47–Q60 = outras disciplinas, nenhum item do núcleo procedimental RI;
- classificação: `OUT_OF_SCOPE`;
- não conta como PASS nem como falha de material.

Status: `CONSUMED / OUT_OF_SCOPE`.

## RI-H2 — IESES/TJPA 2026 Remoção
Fonte oficial pública: prova 6104 Tipo 1 e gabarito.

Contaminação já conhecida:
- Q6–Q10 apareceram em snippet de pesquisa e não podem ser usadas como held-out.

### Recorte limpo selado
- modalidade: REMOÇÃO;
- questões: **Q11–Q25**;
- finalidade: validação multiforma do primeiro material RI;
- comparar duplicidade com provimento antes de contar independência.

Resultado após freeze `3de8a57648f75303797b0caa24b33fbcd6d174de`:
- Q11 = RCPN/emolumentos;
- Q12 = incorporação imobiliária material, fora do núcleo procedimental congelado;
- Q13–Q25 = RCPN/Notas/CNN e outros nós;
- classificação do recorte para este piloto: `OUT_OF_SCOPE`;
- não conta como PASS nem como falha.

Status: `CONSUMED / OUT_OF_SCOPE`.

## RI-H3 — Vunesp/TJSP 13º Concurso
Página oficial confirmada: TJSP2305, 212 vagas.
Provas/gabaritos exigem Área do Candidato na interface pública atual.

Nenhum PDF será usado como held-out sem cabeçalho/concurso/prova verificáveis.
Status: `PENDING_VERIFIED_LOCATOR`.

## RI-H4 — FGV/TJES 2025 Provimento — objetiva
Fonte oficial FGV confirmada antes de abrir conteúdo:
- página do concurso: `https://conhecimento.fgv.br/concursos/tjesnotarial25`;
- caderno: `atividade-notarial-e-de-registro-ingresso-por-provimentocar-002-tipo-1-copia.pdf`;
- gabarito oficial definitivo: `gabarito-definitivo-tjes-notarial.pdf`.

### Recorte limpo selado
- modalidade: PROVIMENTO;
- questões: **Q1–Q25**;
- finalidade: localizar itens do núcleo `apresentação → prenotação → prioridade → qualificação → exigência/dúvida → saída`, usucapião, retificação e indisponibilidade;
- itens de outras especialidades/matérias serão `OUT_OF_SCOPE`;
- não abrir Q26+ nesta rodada;
- caderno ainda não aberto quando esta metadata foi persistida.

Resultado:
- Q15 = `IN_SCOPE`, gabarito definitivo E;
- revelou `MATERIAL_GAP + STRUCTURE_GAP` sobre art.188 §2º e identificação positiva do título registrável;
- demais itens relevantes no recorte pertencem a especialidades/nós adjacentes;
- v0.1 falhou S2; Q15 foi consumida e não pode validar o patch.

Status: `CONSUMED / FAIL`.

## RI-H5 — FGV/TJES 2025 Remoção — objetiva
Fonte oficial FGV confirmada antes de abrir conteúdo:
- caderno: `atividade-notarial-e-de-registro-ingresso-por-remocaocar-001-tipo-1-copia.pdf`;
- mesmo gabarito oficial definitivo do concurso.

### Recorte limpo selado
- modalidade: REMOÇÃO;
- questões: **Q1–Q25**;
- finalidade: retestar o patch v0.2 no mesmo núcleo procedimental;
- verificar duplicidade com Provimento antes de contar independência;
- itens de outros nós serão `OUT_OF_SCOPE`;
- caderno ainda não aberto quando esta metadata foi persistida.

Resultado:
- nenhum item testou diretamente o núcleo procedimental RI;
- Q1–Q25 = `OUT_OF_SCOPE` para o piloto;
- Q22 gerou challenge oportunístico de Regime Geral, sem contaminar score RI e sem virar held-out retroativo de outro piloto.

Status: `CONSUMED / OUT_OF_SCOPE`.

## Errata de integridade — auditoria 12/09/2026

Os relatos acima preservam a execução histórica; prevalecem estas qualificações:

- H4-Q15 demonstra lacuna de cobertura no art.188 §2º, não uma taxa de resolução cega. Seu segundo rótulo `STRUCTURE_GAP` foi rebaixado a complemento de discriminação.
- H5-Q22 foi erroneamente marcado como confirmação de RG; na verdade revelou `COVERAGE_GAP`, assim como H5-Q20. Ver relatório H5 corrigido.
- Não há resposta pré-gabarito selada demonstrada para H1/H2/H4/H5. Uso futuro desses recortes: **BUILD/CHALLENGE_ONLY**, nunca novo held-out.
- Retornos ampliados da execução anterior expuseram, ao menos parcialmente, Q46 e Q61–62/TJPA Provimento, Q26/TJPA Remoção, Q26–30/TJES Provimento e Q26–31/TJES Remoção. Esses vizinhos ficam em quarentena; não confundir “fora do score” com “não visto”.
- Gabaritos ampliados também foram expostos. Limpeza dos demais itens não está certificada; é necessária auditoria de exposição antes de reservar qualquer restante desses cadernos. Não foi aberto pool novo nesta revisão.
- O freeze local foi publicado remotamente junto com os resultados no commit `a502b45245d014ac080ed161a8653868026f7330`. Preservar os hashes das bases, sem atribuir a essa publicação cronologia remota independente que ela não documenta.

## Atualização de exposição — reconstrução de 12/09

Foram lidas as páginas integrais dos gabaritos Tipo 1 de TJES Provimento e Remoção para conferir Q15/E, Q20/C e Q22/B, além de páginas dos cadernos e retornos ampliados com vizinhos. Prevalece o estado **BUILD/CHALLENGE_ONLY_ENTIRE_BOOK** para os dois cadernos TJES, sem exceção por número de questão. O mesmo item reapresentado em outro tipo não recupera independência. A regra não afirma análise integral das 200 questões.

Índice de proveniência e análise: `data/atlas/FGV_TJES_RECONSTRUCTION_INDEX_2026-09-12.json` e `research/FGV_TJES_THREE_QUESTIONS_RECONSTRUCTED_2026-09-12.md`. Nenhum novo pool reservado foi aberto e nenhum resultado do registro histórico foi convertido em novo PASS.

## Critério de falha
MATERIAL_GAP / STRUCTURE_GAP / DEPTH_GAP / FRESHNESS_GAP / TRANSFER_GAP / OUT_OF_SCOPE / BAD_QUESTION / PROVENANCE_ERROR / DUPLICATE_NOT_INDEPENDENT.

## Gate S2 RI
Exige múltiplos itens IN_SCOPE limpos, pelo menos duas formas/bancas quando possível e nenhuma dependência de fonte secundária para identidade/gabarito.
