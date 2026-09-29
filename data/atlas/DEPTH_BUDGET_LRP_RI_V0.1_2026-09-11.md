# GX Cartório OS — Depth Budget v0.1
## Lei 6.015 / Registro de Imóveis — núcleo procedimental

Snapshot: 2026-09-11
Status: PRIMEIRO BUDGET FORMAL DE RI; pré-material e pré-held-out específico. NÃO estudar ainda.

## Objetivo
Definir profundidade e ordem pedagógica do primeiro núcleo operacional de Registro de Imóveis sem transformar a LRP em leitura linear enciclopédica.

Tronco:
`APRESENTAÇÃO → PRENOTAÇÃO/PRIORIDADE → QUALIFICAÇÃO → EXIGÊNCIA/NOTA DEVOLUTIVA → DÚVIDA → REGISTRO/SAÍDA`

Procedimentos acoplados neste budget:
`INDISPONIBILIDADE`, `USUCAPIÃO EXTRAJUDICIAL`, `RETIFICAÇÃO`.

## Escala
- P1 = primeira passagem / modelo mental + sobrevivência objetiva.
- P2 = exam depth / exceções / integrações / cases.
- P3+ = execução avançada / banca-alvo / robustez.

## Budget

| Cluster | Tipo de nó | P1 | P2 | P3+ | Memory | Questions | Output | Freshness | Conf. |
|---|---|---|---|---|---|---|---|---|---|
| RI0 Apresentação/Protocolo | RULE/PROCEDURE | finalidade do protocolo, número de ordem, prioridade | conflitos entre títulos e hipóteses especiais | casuística rara | H | H | M | M | A |
| RI1 Prenotação/Prioridade | RULE/PROCEDURE | prioridade; vigência; timeline básica; art.205 = 20 dias em hipótese legal | prorrogações, pagamento/emolumentos, bloqueios e restrições supervenientes | exceções altamente específicas | VH | VH | H | H | A |
| RI2 Prazo de qualificação | RULE NODE | art.188: 10 dias; hipóteses de 5 dias; vínculo com nota devolutiva | exceções dos arts.189–192 e interfaces eletrônicas | detalhes pouco recorrentes | VH | H | M | H | A |
| RI3 Qualificação | PROCEDURE NODE | finalidade, controle de legalidade, decisões possíveis | qualificação material/formal, autonomia e limites | doutrina sofisticada quando corpus exigir | H | VH | VH | H | A |
| RI4 Nota devolutiva/exigência | ACT/RULE | exigência por escrito, de uma só vez, clara/objetiva, dentro do prazo | formulação adequada, exigência sanável x insanável, reentrada | redação integral de nota devolutiva | H | VH | H/VH | M | A |
| RI5 Dúvida registral | PROCEDURE | cabimento, natureza administrativa, fluxo mínimo, efeito sobre prenotação | atores, decisão, recurso/saída, efeitos de procedência/improcedência | drafting/argumentação em banca-alvo | H | VH | H | M | A |
| RI6 Indisponibilidade | SYSTEM + RULE | conceito e prioridade da prenotação frente a restrição superveniente | CNIB/Constrijud, comunicação, tipos de ordem, snapshot vigente | minúcias operacionais pós-2026 | M/H | VH | H | VH | A/B |
| RI7 Usucapião extrajudicial | PROCEDURE | competência, representação, documentos nucleares, ata, fluxo macro, registro/rejeição | notificações, anuências, diligências, justificação, impugnação justificada/injustificada, múltiplos imóveis, unidade autônoma | execução completa de ata/requerimento/qualificação | H | VH | VH | H | A |
| RI8 Ata de usucapião | ACT | função da ata e elementos essenciais | conteúdo probatório, qualificação e diligência | peça completa com fading/skeleton | M/H | H | VH | M | A |
| RI9 Retificação | PROCEDURE | finalidade, arts.212–213, administrativo x judicial | hipóteses, confrontantes, georreferenciamento, limites patrimoniais | casos complexos/saneamento SIG-RI | M/H | H/VH | H | H | A/B |

## P1 MUST-KNOW
- número de ordem/protocolo se conecta à prioridade;
- art.188: em regra 10 dias para registro ou nota devolutiva; hipóteses do §1º em 5 dias;
- art.205: prenotação não é “eterna”; regra atual de 20 dias na hipótese de omissão do interessado;
- exigência deve ser escrita, única, articulada, clara e objetiva;
- decisão da dúvida é administrativa e não impede processo contencioso;
- usucapião extrajudicial tramita no RI competente e exige representação profissional + documentação nuclear, inclusive ata notarial;
- impugnação na usucapião precisa ser qualificada, não gera automaticamente a mesma consequência;
- rejeição extrajudicial da usucapião não impede ação judicial;
- retificação administrativa corrige/saneia registro, não é atalho universal para adquirir domínio.

## P1 MUST-UNDERSTAND
- diferença entre `apresentação`, `prenotação`, `qualificação`, `registro` e `averbação`;
- por que a prioridade depende do protocolo e não da data do negócio isoladamente;
- como nota devolutiva e dúvida se conectam;
- por que indisponibilidade superveniente exige análise de prioridade;
- diferença funcional entre `ata notarial` e `registro final` na usucapião;
- diferença entre sanar descrição registral e resolver conflito substancial de propriedade.

## P2 UNLOCKS JÁ JUSTIFICADOS
- ENAC 2026.1: prioridade x indisponibilidade superveniente;
- ENAC 2026.1: impugnação de usucapião;
- ENAC 2026.1: rejeição de usucapião;
- ENAC 2026.1: retificação em conflito com área pública;
- ENAC 2025.2: procedimento de dúvida;
- ENAC 2025.2: requisitos/documentos da usucapião;
- Cebraspe/TJPE e TJRO: execução de ata notarial de usucapião;
- CNN/Prov.149: diligências, justificação e impugnação;
- Prov.195/2025: saneamento/SIG-RI;
- Prov.224/2026: Constrijud;
- Prov.229/2026: SERP/interoperabilidade.

## P3+/REFERENCE
Não entram na primeira passagem sem banca/edital/erro que justifique:
- listas integrais de todos os documentos de procedimentos especiais;
- detalhes tecnológicos internos de cada operador/sistema;
- todos os subartigos de saneamento territorial;
- casuística estadual sem edital-alvo;
- doutrina histórica extensa sobre princípios registrais.

## Formatos pedagógicos por nó
### RULE NODE
Lei seca guiada + boundary + Q→A + MCQ.

### PROCEDURE NODE
Flowchart textual + decision points + mini-casos + sequência embaralhada.

### ACT NODE
Model sheet textual + skeleton + completion/fading + microexecução.

### SYSTEM NODE
Mapa de atores/entradas/saídas + freshness + caso operacional.

## Assessment design
### Encoding checks
- identificar etapa seguinte;
- escolher providência do registrador;
- completar fluxo curto.

### Assessment real
- caso com fatos fora de ordem;
- conflito entre duas regras;
- mudança temporal no meio da prenotação;
- impugnação com conteúdo ambíguo;
- nota devolutiva parcialmente correta.

### OUTPUT
Só depois de conhecimento mínimo:
`identificar ato → skeleton → preencher átomos → revisar formalidade → peça/nota/ata inteira`.

## Gate antes de material learner-facing
- ledger RI expandido por procedure;
- pelo menos FGV + Cebraspe + outra banca/estadual representados;
- held-out RI separado ANTES do freeze;
- CNN current snapshot aplicado;
- mini-rubrics de `nota devolutiva`, `dúvida`, `usucapião` e `retificação`;
- challenge sem vazamento do held-out.

## Estado
Confiança global: **B+ / A- no tronco procedural**.

Aprovado para BUILD interno. Ainda NÃO liberar estudo.
