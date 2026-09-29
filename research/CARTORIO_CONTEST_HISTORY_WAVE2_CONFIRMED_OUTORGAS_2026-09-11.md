# GX Cartório OS — Contest History Atlas — Wave 2
## Outorgas, classificados e cortes auditáveis

Snapshot: 2026-09-11
Status: pesquisa em andamento; NÃO é material de estudo.

## Objetivo
Separar rigorosamente:
1. vagas anunciadas;
2. candidatos habilitados/classificados;
3. candidatos convocados para escolha;
4. serventias efetivamente escolhidas/outorgadas;
5. corte normativo;
6. corte empírico de cada lista/fase.

Nenhum desses campos deve ser inferido a partir dos demais.

## Taxonomia de corte
O Atlas usa pelo menos quatro medidas:
- `CUT_RULE`: mínimo normativo do edital;
- `CUT_OBJ_EMPIRICAL`: nota do último convocado para a fase seguinte na objetiva, por modalidade/lista;
- `CUT_FINAL_APPROVED`: menor nota final de candidato aprovado na classificação válida;
- `CUT_CHOICE_EFFECTIVE`: classificação/nota do último candidato que efetivamente conseguiu escolher uma serventia naquela audiência/lista.

Essas quatro medidas respondem perguntas diferentes e não devem ser colapsadas.

## Achados confirmados nesta onda

### Santa Catarina — Edital 015/2022 — Cebraspe
Fontes oficiais:
- https://www.tjsc.jus.br/web/concursos/notarial-e-registral/edital-015-2022
- https://www.tjsc.jus.br/web/imprensa/-/escolha-de-22-serventias-extrajudiciais-mobiliza-115-classificados-do-concurso-tjsc
- https://cdn.cebraspe.org.br/concursos/tj_sc_22_notarios/arquivos/ED_15_2022_TJSC_NOTRIOS_ABERTURA.PDF
- https://cdn.cebraspe.org.br/concursos/tj_sc_22_notarios/arquivos/EDITAL_N._55_2023___RESULTADO_DEFINITIVO_DA_PROVA_OBJETIVA_E_CONVOCAO_PARA_PROVA_ESCRITA_E_PRTICA.PDF

Confirmado:
- desenho original: 23 vagas, 16 provimento + 7 remoção;
- subitem 9.10.1: ampla concorrência convocada à escrita na proporção de 8 candidatos por serventia, empatados no limite incluídos;
- `CUT_OBJ_EMPIRICAL` ampla/provimento = **73 pontos**: 16×8 = 128 posições e a fronteira caiu no grupo de nota 73; os empatados em 73 foram incluídos;
- `CUT_OBJ_EMPIRICAL` ampla/remoção = **33 pontos**: teto teórico 7×8 = 56 e o conjunto habilitado/convocado ficou abaixo desse teto, chegando ao candidato de 33 pontos;
- concurso concluído/homologado em 2025;
- lista final de escolha: 22 serventias, 15 provimento + 7 remoção;
- 115 classificados foram chamados para a audiência pública de escolha;
- todas as 22 serventias foram selecionadas ao final da audiência;
- edital considerava aprovado no concurso final quem alcançasse média final >= 5,00, o que NÃO é o corte empírico da objetiva.

Consequência:
- `CUT_OBJ_EMPIRICAL` passa a ser calculado por modalidade/lista;
- não comparar 73/33 cruamente com outra banca sem normalizar vagas, escala, regra de barreira, cotas e pool de candidatos.

### Acre — Edital 01/2023 — Consulplan
Fontes oficiais:
- https://webdev.tjac.jus.br/adm/processos-seletivos/notario/
- https://www.tjac.jus.br/2025/01/tjac-realiza-a-investidura-de-17-delegatarios/
- https://www.tjac.jus.br/2024/12/escolha-das-delegacoes-e-realizada-durante-sessao-publica/

Confirmado:
- 20 serventias vacantes eram objeto do ciclo do concurso;
- resultado final divulgado em 06/12/2024 e homologado em 16/12/2024;
- sessão de escolha em 20/12/2024;
- solenidade de 22/01/2025 investiu 17 delegatários;
- houve outorga posterior específica para Assis Brasil em 24/02/2025, indicando que `17` não deve ser confundido automaticamente com número final absoluto de todas as unidades titularizadas pelo concurso.

Consequência:
- registrar `17 investidos na solenidade coletiva`;
- manter `outorgas finais = em consolidação`, porque houve ato posterior e movimentos de remoção/vacância derivados do próprio concurso.

### Amazonas — concurso regido pelo Edital 001/2023 — IESES
Fonte oficial:
- https://www.tjam.jus.br/index.php/menu/sala-de-imprensa/13140-tjam-realiza-audiencia-publica-para-escolha-de-serventias-extrajudiciais-por-aprovados-em-concurso-publico

Correção importante ao inventário inicial:
- banca = IESES, não `comissão própria`;
- havia 10 vagas por provimento no desenho citado pela notícia, além das vagas por remoção/listas reservadas;
- Portaria classificatória homologada: 74 aprovados para vagas regulares de provimento, 8 por remoção, 10 para vagas de negros e 11 para PcD;
- na audiência de 09/12/2024, 15 aprovados fizeram opção por serventias;
- uma serventia (Lábrea) ficou fora da lista por decisão liminar.

Consequência:
- distinguir `aprovados/classificados` de `optantes na audiência`;
- registrar 15 escolhas na primeira audiência, sem ainda inferir que isso foi o número final de outorgas, pois houve reescolha posterior em 2025.

### Sergipe — Edital 01/2023 — FGV
Fontes oficiais:
- https://conhecimento.fgv.br/concursos/tjsenotarial23
- https://conhecimento.fgv.br/sites/default/files/concursos/577_tjse-resultado-definitivo-prova-objetiva-26-01-atualizado.pdf
- https://conhecimento.fgv.br/sites/default/files/concursos/tjse-notarios-convocacao-provas-escritas-por-categoria.pdf
- https://conhecimento.fgv.br/sites/default/files/concursos/diario-n.-6471-de-25-de-marco-de-2025.pdf
- https://agencia.tjse.jus.br/noticias/item/16030-tjse-convoca-candidatos-para-sessao-de-reescolha-em-concurso-de-cartorios-no-estado

#### CUT_OBJ_EMPIRICAL para convocação à escrita/prática
- provimento / ampla concorrência: **57**;
- provimento / candidatos negros: **24**;
- provimento / PcD: **28**;
- remoção / ampla concorrência: **19**;
- remoção / PcD: **34**.

Esses valores vêm da lista oficial de convocação por categoria. São cortes empíricos daquela fase/lista, NÃO mínimos normativos universais e NÃO notas finais do concurso.

#### Resultado final
- 54 aprovados na lista geral de provimento e 6 na lista geral de remoção, além das listas de cotas com sobreposição de candidatos;
- menor nota final observada na lista geral de provimento: **4,62**;
- menor nota final observada na lista geral de remoção: **4,88**;
- sessão de escolha/outorga em 30/04/2025;
- após primeira escolha houve desistências/renúncias/não investidura e o TJSE convocou reescolha em setembro de 2025, com três unidades explicitamente remanescentes na notícia.

Consequência:
- prova real de que `CUT_OBJ_EMPIRICAL ≠ CUT_FINAL_APPROVED ≠ vagas ≠ outorgas definitivas`;
- qualquer tabela nacional que tenha apenas uma coluna `nota de corte` perde informação crítica.

### Pernambuco — 2º concurso 2024 — Cebraspe
Fontes oficiais:
- https://portal.tjpe.jus.br/comunicacao/noticias/-/asset_publisher/ubhL04hQXv5n/content/id/8479590
- https://portal.tjpe.jus.br/web/portal/-/concurso-para-cart%C3%B3rios-%C3%A9-homologado-e-data-para-escolha-de-serventias-%C3%A9-divulgada-1

Correção do inventário inicial:
- o TJPE informou 145 vagas no resultado final de dezembro de 2025, não 147;
- resultado homologado em 15/12/2025;
- audiência de escolha marcada para 22/01/2026.

Consequência:
- atualizar planilha para 145;
- outorgas efetivas devem ser extraídas da audiência/atos posteriores, não presumidas pelo total do edital.

## Insight estatístico importante
Não usar `CUT_OBJ_EMPIRICAL` cru como ranking de dificuldade entre bancas/Estados. Ele é função de:
- escala e dificuldade da prova;
- número de serventias naquela modalidade;
- multiplicador de candidatos por vaga;
- empates no limite;
- ações afirmativas/regras de corte específicas;
- composição do pool de candidatos;
- anulações/retificações.

Comparação futura deve criar métricas normalizadas, por exemplo:
- percentil aproximado de avanço;
- candidatos convocados por vaga;
- taxa de sobrevivência por fase;
- z-score dentro da distribuição quando dados permitirem;
- taxa de preenchimento efetivo das serventias.

## Próxima onda
1. extrair `CUT_OBJ_EMPIRICAL` de mais concursos FGV/Cebraspe/Vunesp/IESES;
2. localizar ata/outorga final de PE 2026;
3. consolidar primeira escolha + reescolha de AM e SE;
4. fechar AC com relação final de escolhas + outorgas posteriores;
5. repetir metodologia em PR, GO, RS, SP e PE, que têm massa histórica grande;
6. transformar a planilha nacional em série temporal por Estado, não só `último concurso`;
7. só depois gerar comparativos de `facilidade/oportunidade`, nunca a partir de corte cru.