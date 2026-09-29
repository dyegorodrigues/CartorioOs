# GX Cartório OS — Regime Geral v0.2 Retest
## H8/H9 — TJPE/Cebraspe 2024

Data: 2026-09-11
Status: VALIDATION PARTIAL; **S2 AINDA NÃO ATINGIDO**

## Material testado
`material/specimens/REGIME_GERAL_INTERNAL_FREEZE_V0.2_2026-09-11.md`

## H8 — Provimento
O recorte original Q1–Q20 foi selado antes da busca. O locator expôs automaticamente Q1–Q6, que foram marcadas contaminadas. O recorte limpo Q7–Q20 foi então selado e aberto.

Resultado:
- Q7 LGPD/dados → cross-system;
- Q8 imóvel rural/CAR/alienação fiduciária → Civil/RI;
- Q9 CNIB → RI/system;
- Q10 princípios registrais → RI;
- Q11–Q15 RCPN;
- Q16 RCPJ;
- Q17 RTD;
- Q18 adjudicação compulsória;
- Q19 condomínio/incorporação;
- Q20 emolumentos/Lei 10.169 → nó adjacente próprio.

Nenhum item limpo desse recorte pertence diretamente ao scope RG0–RG8 do specimen. Resultado: `NO_IN_SCOPE_SIGNAL`.

## H9 — Remoção
Q1–Q6 foram seladas antes da busca do caderno. Fonte e gabarito oficiais Cebraspe foram confirmados.

### Q1 — independência x fiscalização
Pergunta: relação entre independência dos notários/registradores no gerenciamento e fiscalização judicial.
Gabarito definitivo: **C** — fiscalização não implica direção exaustiva da execução dos serviços.

### Cobertura no specimen v0.2
O freeze ensina:
- atividade privada por delegação;
- fiscalização judicial;
- titular como delegatário/gestor;
- independência no exercício de suas atribuições dentro da ordem jurídica.

A resposta correta decorre diretamente da combinação desses átomos. Não exige proposição ausente.

Diagnóstico: `COVERED / TRANSFER EXPECTED / PASS`.

Q2 assinatura eletrônica → OUT_OF_SCOPE.
Q3 norma local sobre reorganização/fusão → STATE_OVERLAY.
Q4–Q6 atos de notas → SPECIALTY OUT_OF_SCOPE.

## Efeito da ferramenta
O retorno expandido usado para localizar Q6 exibiu também Q7–Q29 do caderno de remoção. Esses itens não estavam no recorte H9, mas ficam contaminados para futuro held-out.

## Conclusão
A v0.2 passou no único item Regime Geral limpo/materialmente independente encontrado em H9, mas **uma questão não oferece diversidade suficiente para S2**.

Estado:
- H7: falha real e patch feito;
- H8: sem item in-scope limpo;
- H9: 1 pass in-scope;
- S2: NÃO atingido.

## Decisão metodológica
Não ampliar artificialmente “Regime Geral” para absorver LGPD, emolumentos, RCPN/RTD/RI apenas para aumentar taxa de acerto do module test. O One-Home Rule vale também para validação.

## Próxima validação
Buscar banca/Estado diverso com:
1. caderno oficial verificável;
2. conteúdo não usado no BUILD;
3. questões de Lei 8.935/CF236/regime funcional;
4. gabarito definitivo;
5. recorte registrado antes da abertura.
