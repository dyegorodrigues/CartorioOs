# GX Cartório OS — RI Procedure Rubrics v0.1

Snapshot: 2026-09-11
Status: BUILD interno. NÃO estudar ainda.

## Objetivo
Converter Registro de Imóveis em operações treináveis e avaliáveis. O candidato precisa identificar etapa, decidir providência, fundamentar, executar e revisar.

## Rubric universal
`TÍTULO/REQUERIMENTO → COMPETÊNCIA → PROTOCOLO/PRENOTAÇÃO → PRIORIDADE → QUALIFICAÇÃO → DECISÃO → FUNDAMENTO → PRAZO/COMUNICAÇÃO → QA`.

### R1 Prenotação/prioridade
P1: número de ordem, prioridade, art. 188, art. 205 e efeitos temporais.
Assessment: dois títulos conflitantes + restrição superveniente; reconstruir timeline e consequência.
Erros fatais: substituir prioridade pela data do negócio; tratar prenotação como eterna; decorar prazo sem a hipótese legal.

### R2 Qualificação
Perguntas fixas: qual ato é pretendido? título é formalmente idôneo? há continuidade/disponibilidade/especialidade/legitimidade? há restrição? problema é sanável? qual providência correta?
Saídas: registrar/averbar, exigir, suscitar dúvida ou aplicar procedimento especial.

### R3 Nota devolutiva
Art. 198 LRP: exigência escrita, dentro do prazo legal, de uma só vez, articulada, clara e objetiva, com data, identificação e assinatura.
Skeleton: protocolo → ato → exigência individualizada → fundamento → modo de saneamento → direito de dúvida → identificação.
QA: legality, relevance, specificity, actionability, completeness, tone.

### R4 Dúvida registral
Fluxo: `nota devolutiva → discordância/impossibilidade → pedido → anotação na prenotação → ciência → impugnação → remessa → decisão → saída`.
Pontos centrais: impugnação em 15 dias; ausência de impugnação não impede julgamento; procedência cancela prenotação; improcedência permite registro após reapresentação; decisão é administrativa e não impede contencioso.

### R5 Usucapião extrajudicial
Mapa: `advogado + requerimento → RI competente → ata + planta/memorial + documentos → qualificação → notificações/poder público → diligências → impugnação qualificada → registro ou rejeição/remessa`.
Boundaries: rejeição extrajudicial não impede ação judicial; impugnação justificada e injustificada não têm a mesma consequência; unidade autônoma tem regra especial; ata instrui o procedimento e não reconhece sozinha a propriedade.
Output ladder: reconhecer → ordenar → mini-caso → skeleton → ato completo.

### R6 Retificação
Art. 212/213: saneamento de registro omisso/impreciso/inverídico, com via administrativa sem excluir judicial.
Assessment: separar correção simples, retificação técnica e conflito material que não cabe como mera retificação.

### R7 Indisponibilidade/sistemas
P1: conexão com prenotação/prioridade.
P2 HOT: CNIB/Constrijud/SERP e alterações 2026, sempre com Freshness Firewall.

## Output rubric RI
Pontuar separadamente: ISSUE, ROLE, ACT, ATOMS, SEQUENCE, BOUNDARIES, FRESHNESS, FORM e QA.
Manter duas métricas: `LEGAL_ATOM_HIT_RATE` e `PACKAGING_COMPLIANCE`.

## Gate
Usar este documento para construir MASTER/Objective Lab/Output Lab e red-team; não liberar estudo antes de held-out próprio de RI.