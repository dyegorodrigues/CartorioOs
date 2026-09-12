# Regime Geral — correção de auditoria v0.3

Data: 2026-09-12. Estado: **BUILD CORRIGIDO / NÃO VALIDADO / NÃO ESTUDAR**.

Base imutável: `REGIME_GERAL_INTERNAL_FREEZE_V0.2_2026-09-11.md`. Este patch substitui os trechos indicados; não transforma a base antiga em um teste aprovado. TJES/FGV 2025 Remoção Tipo 1 Q20 e Q22 são evidência consumida, disponível apenas para BUILD/regressão.

## RG0B — completar a atribuição básica

`RG-ATTR-AUTH-001`: autenticar cópias é atribuição exclusiva dos tabeliães de notas (art. 7º, V). Receber pagamento de títulos protocolizados, dando quitação, é atribuição privativa dos tabeliães de protesto (art. 11, III). A v0.2 ensinava territorialidade, mas não estes dois discriminadores da Q20.

## RG6 — substituir integralmente o bloco 8.1

`RG-DISC-PREV-001`: quando necessário afastar o titular para apurar faltas, a suspensão preventiva pode durar **90 dias, prorrogáveis por 30** (art. 36). Não deduzir esse prazo da pena de suspensão do art. 32: são institutos distintos, embora os números coincidam.

`RG-DISC-INTERVENTOR-002`: o juízo competente designa interventor se o substituto também estiver acusado ou se a medida for conveniente **para os serviços** (§1º). A redação anterior trocava esse segundo critério por conveniência à apuração.

`RG-DISC-RENDA-003`: durante o afastamento, metade da renda **líquida** fica com o titular; a outra metade vai a conta bancária especial, **com correção monetária**. Absolvido, o titular recebe o saldo; condenado, o saldo cabe ao interventor (§§2º–3º).

Fonte: [Lei 8.935, arts. 7º, 11 e 36](https://www.planalto.gov.br/ccivil_03/leis/l8935.htm), conferidos em 12/09/2026. Esta conferência não certifica os demais dispositivos nem os overlays CNJ/STF do módulo.

## Derivações obrigatórias

| Superfície | Correção vinculada aos IDs acima |
|---|---|
| MAP/contraste | Sanção e cautelar têm fundamentos diferentes; prazo coincidente não torna os regimes iguais. |
| Lei seca guiada | Arts. 7º V, 11 III, 36 caput e §§1º–3º; localizar sujeito, prazo, base econômica e destino. |
| Q→A 9–10 | Recuperar o prazo cautelar, critério de intervenção, renda líquida, correção e destino do saldo, não apenas “metade”. |
| OUTPUT art.36 | Necessidade → prazo → juízo/interventor → renda/conta/correção → absolvição ou condenação. |

Regressão editorial: Q20 e Q22 agora encontram os átomos antes ausentes. Isso **não** é novo held-out, resultado de aluno ou selo S2. Não há nova rodada de prova neste patch.
