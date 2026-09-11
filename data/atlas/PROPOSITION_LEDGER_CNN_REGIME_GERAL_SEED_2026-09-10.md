# GX Cartório OS — Proposition Ledger Seed
## CNN/CNJ — Regime Geral / Administração da Delegação

Snapshot: 2026-09-10
Status: SEED; NÃO é material de estudo.

## Escopo desta semente
Somente proposições nacionais recentes que dialogam diretamente com Regime Geral e podem alterar o Depth Budget do módulo-base.

## Fontes oficiais
- Prov. 149/2023 compilado.
- Prov. 218/2026 — Justiça Aberta.
- Prov. 219/2026 — relação geral de vacâncias.
- Prov. 220/2026 — incapacidade permanente.
- Prov. 227/2026 — solvência trabalhista.
- Res. 696/2026 — concursos de outorga.

## Ledger

| ID | Proposição examinável | Fonte | Tipo | Volatilidade | P1? | Memory | Question | Output | Observação |
|---|---|---|---|---|---|---|---|---|---|
| CNN-JA-136 | Justiça Aberta é banco público estratégico alimentado com dados decorrentes da atividade N/R para planejamento/políticas | Prov. 218 → CNN art. 136 | conceito/estrutura | recently_changed | SIM, arquitetura | M | M/H | M | não exigir redação literal extensa em P1 |
| CNN-JA-136A | Alimentação/atualização do Justiça Aberta é dever funcional de notários e registradores e deve observar atualidade, fidedignidade, exatidão, integridade, rastreabilidade e coerência | Prov. 218 → CNN art. 136-A | dever funcional | recently_changed | SIM | H seletiva | H | M/H | candidato a questão de consequência disciplinar |
| CNN-VAC-073 | Gestão/atualização/publicidade da relação geral de vacância segue Prov. 219/2026 | CNN art. 73 + Prov. 219 | remissão/norma nacional | recently_changed | SIM, mapa | M | H | H | central para concursos e interinidade |
| CNN-VAC-RGV | RGV nacional registra comarca, CNS, unidade, criação, vacância, motivo, critério de ingresso, forma originária/derivada etc. | Prov. 219, anexo | procedimento/dados | recently_changed | PARCIAL | L/M | M | M | detalhes do anexo provavelmente P2/REFERENCE até corpus |
| CNN-INC-220 | Há procedimento administrativo nacional específico para aferir incapacidade permanente do delegatário para fins do art. 39 III da Lei 8.935 | Prov. 220/2026 | procedimento/extinção | recently_changed | SIM, existência/estrutura | M/H | H | H | detalhamento probatório/processual a calibrar |
| CNN-SOLV-001 | Delegatário deve declarar periodicamente passivos trabalhistas e solvência à Corregedoria | Prov. 227 art. 1 e ss. | dever administrativo | recently_changed | SIM | H | H | H | conecta gestão, fiscalização e disciplina |
| CNN-SOLV-004 | Declaração anual do passivo é apresentada até 31 de março com base em 31 de dezembro anterior | Prov. 227 arts. 3–4 | prazo/boundary | recently_changed | TALVEZ P1/P2 | VH se incidência | H | M | custo de memória baixo; aguardar corpus para peso final |
| CNN-SOLV-008 | Declaração de solvência acompanha a de passivo e deve indicar bens/direitos suficientes para cobertura | Prov. 227 arts. 8–10 | procedimento | recently_changed | P2 candidato | M/H | M/H | M/H | lista de bens excluídos não deve entrar plana em P1 sem prova |
| CNN-SOLV-017 | Descumprimento das obrigações do Prov. 227 caracteriza inobservância normativa, remetendo ao art. 31 I da Lei 8.935 | Prov. 227 art. 17 | ponte disciplinar | recently_changed | SIM | H | H | H | excelente integração CNN ↔ L8935 |
| CNN-SOLV-036 | Em risco grave e iminente de inadimplemento generalizado, pode haver PAD e medida cautelar associada ao art. 36 da Lei 8.935 com interventor | Prov. 227 art. 12 §4 | consequência/cautelar | recently_changed | P2 | M/H | H | H | output e caso integrado mais provável que decoreba isolada |
| CNN-SOLV-019 | Prov. 227 não se aplica às serventias Classe I do Prov. 213 nem às sob interinidade | Prov. 227 art. 19 | exceção | recently_changed | P2 | H se cobrado | H | M | candidato clássico a alternativa de exceção |

## Insights do Compiler

### 1. O Regime Geral de 2026 não cabe apenas na Lei 8.935
A árvore correta precisa ter:
`CF 236 → Lei 8.935 → CNN/CNJ geral → atos autônomos CNJ → STF/STJ`.

### 2. Atualização recente pode criar prioridade sem histórico longo
`CNN-SOLV-004` ainda não tem longa frequência histórica, mas é boundary barato e recente. O Atlas deve usar uma `RECENCY/CHANGE BONUS` moderada, nunca substituir o corpus por novidade.

### 3. Detalhe operacional precisa de poda
No Prov. 227 há listas extensas de bens, documentos contábeis e regras de avaliação. P1 deve ensinar arquitetura e consequências; P2/REFERENCE absorve detalhe salvo incidência objetiva comprovada.

### 4. Ponte normativa vale mais que arquivo isolado
A proposição mais importante pedagogicamente pode ser a aresta:
`dever novo CNN → descumprimento → art. 31 I → sanção/processo → art. 36 em cautelar`.
Isso gera compreensão e resolve múltiplas formulações.

## Próxima expansão
- cruzar estas proposições com ENAC 2026.2 futuro e concursos estaduais pós-696;
- incluir fiscalização, LGPD/TI e emolumentos gerais somente após delimitar One-Home Rule;
- ligar IDs ao ledger Lei 8.935;
- marcar BUILD / VALIDATION / HELD-OUT / CHALLENGE quando corpus suficiente.