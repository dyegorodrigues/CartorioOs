# ENAC 300 — Repair checkpoint + blind QA sample

Data: 28/09/2026  
Branch HOT: `chatgpt/gx-cartorio-v0.1`  
Status: **REPARO RELACIONAL QUASE FECHADO / ANOTAÇÕES 300/300 COMPLETAS / QA CEGO AMOSTRAL INICIADO**

## 1. Estado relacional verificado

Recontagem direta no `GX Cartório — Question Intelligence Lab` após os reparos:

| Edição | Total | sem vínculo curricular |
|---|---:|---:|
| ENAC 2025.1 | 100 | **0** |
| ENAC 2025.2 | 100 | **1** |
| ENAC 2026.1 | 100 | **0** |

O único item sem vínculo é **ENAC 2025.2 Q100 — Debate público sobre medicamentos para obesidade**. Isto é **intencional**, não falha de classificação: trata-se de Conhecimentos Gerais, bloco histórico que não integra a matriz-alvo ENAC 2026.2. Não forçar vínculo artificial a um nó jurídico apenas para produzir “0 órfãs”.

Assim, para o currículo jurídico atual:
- 299/300 itens possuem vínculo;
- 299/299 itens juridicamente mapeáveis neste corpus possuem vínculo;
- 1/300 permanece `INTENTIONAL_UNMAPPED / MATRIX_DRIFT`.

## 2. Campos analíticos

Recontagem estruturada confirmada antes do limite de consultas do workspace:

| Edição | Família da fonte vazia | Distrator vazio | Validação oficial | Anuladas |
|---|---:|---:|---:|---:|
| 2025.1 | 0 | 0 | 100 | 3 |
| 2025.2 | 0 | 0 | 100 | 1 |
| 2026.1 | 0 | 0 | 100 | 2 |

Portanto:
- `Família da fonte`: **300/300 preenchida**;
- `Mecanismo do distrator`: **300/300 preenchido**;
- `Validação`: **300/300 Oficial**;
- anuladas: **6/300**, preservadas no corpus sem serem tratadas como resposta jurídica canônica.

O limite de `Query Data Source` do workspace foi atingido logo depois, antes da recomputação dos novos agregados 300/300 por família e mecanismo. Não inventar esses percentuais até a recontagem voltar a estar disponível.

## 3. Reparos finais de 2025.2

Foram relacionados aos nós atuais, entre outros:

- Q41 incompatibilidades/impedimentos → Lei 8.935/1994;
- Q43 perda da delegação/processo disciplinar → responsabilidade disciplinar + fiscalização;
- Q44 condomínio edilício → CIV 22;
- Q52 responsabilidade do notário por ato de substituto → NTR 1.2 + CIV 11;
- Q53 sanção disciplinar → NTR 1.2;
- Q62 APP/reserva legal/alteração normativa → direitos coletivos + processo legislativo;
- Q74 ITBI → TRIB 9;
- Q75 ITCMD/partilha → TRIB 11 + CIV 14;
- Q76 benefício fiscal/anterioridade → TRIB 4 + TRIB 1;
- Q77 IPTU/prescrição → TRIB 12 + TRIB 6;
- Q78 título executivo extrajudicial → PCIV 7;
- Q79 coisa julgada/questão prejudicial/prova → PCIV 6 + PCIV 5;
- Q81 Minha Casa, Minha Vida/contrato → CIV 20 + CIV 12;
- Q84 cessão hereditária → CIV 14;
- Q86 ausência/sucessão definitiva → CIV 14 + NTR 7.21;
- Q87 Súmula 308/alienação fiduciária/incorporação → CIV 15 + CIV 18 + CIV 22;
- Q88 vícios formais em testamento → CIV 14 + NTR 4.10;
- Q90 emancipação/capacidade/contrato → CIV 2 + CIV 12;
- Q92 testamentos sucessivos/testamenteiro → CIV 14 + NTR 4.10;
- Q99 flagrante/prisão especial → PPEN 4.

## 4. Blind QA estratificado contra cadernos oficiais FGV

A amostra foi relida diretamente nos PDFs oficiais da FGV e visualmente conferida nas páginas dos cadernos, sem depender apenas dos títulos do banco.

### 2025.1
Conferidos, entre outros:
- Q47 — usucapião extrajudicial;
- Q63 — ADPF;
- Q94 — recuperação judicial e alienação fiduciária de recebíveis (**anulada**, usada apenas para QA de tema/ambiguidade, não como resposta canônica).

### 2025.2
Conferidos:
- Q43 — perda da delegação / Lei 8.935/1994;
- Q44 — síndico / Lei 4.591/1964;
- Q76 — revogação de benefício de ICMS e anterioridade;
- Q77 — IPTU, parcelamento e prescrição;
- Q78 — título executivo extrajudicial no CPC;
- Q79 — coisa julgada sobre questão prejudicial;
- Q84 — cessão de bem singular da herança;
- Q86 — ausência e sucessão definitiva;
- Q87 — Súmula 308/STJ + alienação fiduciária;
- Q88 — preservação da vontade do testador;
- Q90 — capacidade/emancipação em contrato.

### 2026.1
Conferidos, entre outros:
- Q30 — execução extrajudicial de hipoteca;
- Q34 — usucapião extrajudicial com impugnação;
- Q42 — responsabilidade civil do notário/registrador;
- Q48 — impedimentos para designação de interino.

Resultado do recorte estratificado: **nenhum drift de tema material encontrado** entre os enunciados oficiais vistos e os vínculos/taxonomias correspondentes.

Isto é QA amostral estratificado, não certificação 300/300 do conteúdo jurídico.

## 5. Próximo batch correto

1. quando `Query Data Source` voltar, recalcular agregados 300/300 de família de fonte e mecanismos de distrator;
2. registrar Q100 como `INTENTIONAL_UNMAPPED / MATRIX_DRIFT` no relatório canônico, sem inventar nó;
3. ampliar QA cego de forma estratificada entre 2025.1, 2025.2 e 2026.1;
4. somente depois gerar heatmap quantitativo por nó/subtema;
5. cruzar separadamente:
   - **Domain Incidence Model** = ENAC + cartório multibanca;
   - **FGV Bank Style Model** = ENAC + FGV cartório + FGV comparável com peso menor;
6. preservar estudo real bloqueado e não atribuir mastery.

## 6. Regra anti-drift

`INDEXED != LEGALLY RECONSTRUCTED`

`LINKED != MASTERED`

`SAMPLE_QA != FULL_CERTIFICATION`

O banco agora está estruturalmente apto para a primeira análise quantitativa fina, mas os percentuais 300/300 de fonte/distrator ainda precisam de uma última recontagem após o limite do Notion liberar.
