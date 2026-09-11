# GX Cartório OS — Contest History Atlas — Wave 3
## Paraná + Goiás: escolha efetiva, reescolha e diferença entre vaga/anúncio/preenchimento

Snapshot: 2026-09-11
Status: pesquisa histórica paralela; NÃO é material de estudo.

## Paraná — 3º Concurso — Edital 01/2018
Fontes oficiais:
- https://www.tjpr.jus.br/widget/noticias/-/asset_publisher/9jZB/content/tjpr-realizara-audiencia-para-aprovados-no-concurso-do-edital-01-2018/18319
- https://portal.tjpr.jus.br/pesquisa_athos/publico/ajax_concursos.do?actionType=detalhesMateria&idMateria=4669298&view=detalheMateria
- Diário/TJPR sobre outorga e investidura de 08/12/2022.

### Números confirmados
- audiência principal: 08/12/2022;
- TJPR anunciou 390 cargos a preencher;
- mais de 1.000 candidatos constavam como aprovados no resultado final;
- 848 candidatos foram efetivamente chamados à escolha até se esgotar a lista disponível;
- PCD/provimento: 36 aprovados; 5 ausentes; 16 renúncias; **15 escolhas**;
- remoção geral: 15 aprovados; 1 ausente; 5 renúncias; **9 escolhas**;
- provimento geral: 986 aprovados; 236 ausentes; 246 renúncias; **365 escolhas**; os candidatos da posição 849 em diante não foram chamados porque a candidata 848 escolheu o último cartório disponível;
- total registrado naquela audiência = **389 escolhas**.

### Por que 389 e não 390
A própria ata informa retirada do 1º Registro de Imóveis de Umuarama da lista de serventias disponíveis por decisão liminar. Logo, a fotografia operacional da audiência ficou com 389 escolhas, apesar de a comunicação prévia falar em 390 cargos.

### Insight de métrica
Este concurso permite calcular depois:
- `CHOICE_REACH = classificação 848` para o último chamado na ampla/provimento;
- taxa de escolhas entre os chamados;
- taxa de ausência/renúncia;
- diferença entre aprovados finais e candidatos que tiveram oportunidade real de escolher.

Não converter `classificação 848` em nota sem localizar a tabela final de notas/classificação e cruzar o candidato limítrofe.

## Goiás — 2º Concurso Unificado
Fontes oficiais:
- https://www.tjgo.jus.br/index.php/agencia-de-noticias/noticias-ccs/20-destaque/29655-audiencia-publica-define-escolha-de-cartorios-de-notas-e-registros-dos-aprovados-no-2-concurso-unificado-do-tjgo
- https://www.tjgo.jus.br/index.php/agencia-de-noticias/noticias-ccs/20-destaque/31140-concluida-audiencia-de-reescolha-de-serventias-investidura-sera-ainda-nesta-quinta-feira-e-cartorios-deverao-ser-assumidos-em-30-dias
- https://www.tjgo.jus.br/index.php/cogex-noticias/254-destaque-extrajudicial-e-tj/34219-investidos-10-notarios-e-registradores-apos-3-audiencia-de-escolha-das-serventias-nesta-quarta-feira-1-homenagens-ao-presidente-do-tjgo-corregedores-e-desembargador-carlos-franca-marcaram-a-solenidade
- https://www.tjgo.jus.br/index.php/juiz-substituto-2

### Números confirmados
- edital disponibilizou **292 serventias**;
- concurso homologado em maio/2024;
- **275 candidatos aprovados**;
- primeira audiência, 14/06/2024: **139 serventias escolhidas**;
- na primeira audiência: 36 ausências e 95 renúncias com ressalva de escolha futura;
- serventias remanescentes puderam ir para nova sessão pública;
- segunda audiência/re-escolha ocorreu em 14/11/2024, com outorga formal pelo Decreto Judiciário 4820/2024; número de escolhas dessa sessão ainda precisa ser extraído da lista anexa/decreto;
- terceira audiência, 01/10/2025: **26 serventias escolhidas**; 10 delegatários foram investidos no ato e 16 prorrogaram a investidura;
- notícia de janeiro/2025 registra que, até então, a gestão da Corregedoria havia colocado 120 notários/registradores investidos em exercício ligados ao ciclo de renovação, mas esse número não deve ser somado mecanicamente às escolhas porque mede momento/status diferente.

### Insight de métrica
Goiás prova que uma coluna `vagas = 292` não informa probabilidade efetiva de ingresso. Precisamos de série por audiência:
`serventias disponíveis → candidatos chamados → escolhas → outorgas → investidura → exercício → remanescentes`.

## Decisão para o Contest History Atlas
Adicionar entidade `CHOICE_ROUND`:
- round_id;
- concurso;
- data;
- serventias oferecidas naquela rodada;
- escolhas efetivas;
- ausências;
- renúncias;
- outorgas emitidas;
- investiduras imediatas/postergadas;
- remanescentes;
- fonte oficial.

Assim evitamos atribuir a um concurso um único número final quando o preenchimento ocorre em ondas.

## Próximos alvos
1. extrair número da 2ª audiência GO pelo decreto/lista;
2. cruzar classificação final PR com o candidato da posição 848 para produzir `CUT_CHOICE_EFFECTIVE` por nota;
3. localizar eventuais sessões subsequentes PR;
4. aplicar `CHOICE_ROUND` em AM, SE, PE e SP;
5. calcular `FILL_RATE_INITIAL` e `FILL_RATE_CUMULATIVE` apenas depois das rodadas estarem consolidadas.