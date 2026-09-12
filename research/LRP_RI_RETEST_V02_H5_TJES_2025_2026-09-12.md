# GX Cartório OS — RI retest v0.2 / H5 TJES 2025

Data: 2026-09-12
Base testada: v0.1 + `LRP_RI_PROCEDURAL_PATCH_V0.2_2026-09-12.md`
Status auditado em 12/09: **NO IN-SCOPE ITEM PARA O RECORTE RI; S2 não atingido**.

## Integridade
O relato anterior registra reserva antes da abertura. Não há resolução cega documentada; esta revisão é de cobertura, com prova e gabarito conhecidos. Fonte: [caderno oficial, Tipo 1](https://conhecimento.fgv.br/sites/default/files/concursos/atividade-notarial-e-de-registro-ingresso-por-remocaocar-001-tipo-1-copia.pdf) e [gabarito definitivo, p.1](https://conhecimento.fgv.br/sites/default/files/concursos/gabarito-definitivo-tjes-notarial.pdf).

## Resultado
O recorte não fornece teste do núcleo previamente delimitado. A exclusão não decorre simplesmente de ausência no texto do specimen:

| Itens | Família identificada | Por que não testa este núcleo RI |
|---|---|---|
| 1 | RTD/locação | outra especialidade |
| 2 | superfície/alienação fiduciária | direito material especial |
| 3–4, 6–7, 12, 24 | títulos de crédito/financiamento | regime cedular especial |
| 5, 13 | proteção de dados/desburocratização | nós transversais distintos |
| 8, 10 | colonização/aquisição rural por estrangeiro | legislação material especial |
| 9, 11, 16, 21, 23 | condomínio/loteamento/CDRU/incorporação/SFI | regimes materiais próprios |
| 14 | averbação de correção de valores no SFH, Lei 4.380 | não é retificação de assento dos arts.212–213 da LRP; reconhecer a proximidade sem fundir os nós |
| 15, 25 | união estável/livros do RCPN | outra especialidade |
| 17–19 | servidor/organização judiciária/corregedoria estadual | overlay local |
| 20, 22 | atribuições/afastamento na Lei 8.935 | Regime Geral, não núcleo RI |

Esta classificação preserva o escopo estreito do piloto; **não** certifica cobertura de Registro de Imóveis inteiro.

Classificação: `OUT_OF_SCOPE` para o piloto RI. Não conta como PASS nem como falha.

## Cross-node útil, sem promoção indevida
**Errata:** Q22 não sustenta o `CHALLENGE_PASS` anteriormente registrado. O RG v0.2 menciona “prazo legal” na cautelar, omite correção monetária e não explicita o destino final do saldo. Os números 90+30 constam apenas da pena de suspensão, instituto que o próprio texto manda distinguir. Resultado correto: `COVERAGE_GAP / OPPORTUNISTIC`, gabarito B, sem evidência independente S2.

A auditoria também identificou Q20 (gabarito C): autenticação exclusiva de cópias por notas versus recebimento/quitação privativos do protesto. O bloco territorial RG0B não ensinava esses discriminadores. Outro `COVERAGE_GAP`, não nova prova independente. Ambos alimentam `REGIME_GERAL_AUDIT_PATCH_V0.3_2026-09-12.md`.

## Veredito
O recorte não valida nem refuta o patch RI v0.2. A auditoria legal posterior encontrou outros problemas no RI, corrigidos pelo patch v0.3. Ausência de item adequado não equivale a robustez. Estado: `S1 PATCHED / S2 PENDING`; sem promoção automática e sem abertura de novo pool neste ciclo.
