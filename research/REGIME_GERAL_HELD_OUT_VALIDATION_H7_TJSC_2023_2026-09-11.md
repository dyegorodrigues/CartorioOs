# GX Cartório OS — Held-Out Validation H7
## TJSC/Cebraspe 2023 — Regime Geral

Data: 2026-09-11
Status: **VALIDATION CONSUMED — SPECIMEN v0.1 FALHOU S2**

## Objetivo
Testar o material congelado:
`material/specimens/REGIME_GERAL_INTERNAL_FREEZE_V0.1_2026-09-11.md`

contra questões objetivas oficiais que não foram usadas no BUILD.

## Proveniência
- concurso: TJSC — Atividade Notarial e de Registro — Edital 015/2022;
- banca: Cebraspe;
- modalidade: provimento;
- prova objetiva aplicada em 18/06/2023;
- caderno oficial: `719_TJSCPROVIMENTO_001_01.PDF`;
- gabarito definitivo oficial: `GAB_DEFINITIVO_719_TJSCPROVIMENTO_001_01.PDF`;
- recorte H7 foi selado ANTES de localizar/abrir o caderno: Q1–Q20.

## Gabarito definitivo do recorte
Q1 X, Q2 C, Q3 E, Q4 E, Q5 A, Q6 B, Q7 C, Q8 E, Q9 A, Q10 D, Q11 E, Q12 A, Q13 E, Q14 D, Q15 E, Q16 B, Q17 B, Q18 C, Q19 X, Q20 B.

## Scope classification

| Questão | Família | In-scope Regime Geral? | Resultado |
|---|---|---:|---|
| Q1 | RPJ / prenotação | não | OUT_OF_SCOPE |
| Q2 | Lei 8.935 — circunscrição territorial | **sim** | MATERIAL_GAP |
| Q3 | Lei 8.935 — art.36 / afastamento preventivo / interventor / renda | **sim** | MATERIAL_GAP + DEPTH_GAP |
| Q4 | Lei 8.935 — previdência / contagem recíproca | **sim** | MATERIAL_GAP |
| Q5 | Protesto | não | OUT_OF_SCOPE |
| Q6 | obrigação fiscal/declaração acessória da serventia | não para este módulo | OUT_OF_SCOPE |
| Q7 | Registro Torrens | não | OUT_OF_SCOPE |
| Q8 | inventário extrajudicial | não | OUT_OF_SCOPE |
| Q9 | Estatuto da Terra | não | OUT_OF_SCOPE |
| Q10 | normas locais de automação/selos SC | não | OUT_OF_SCOPE / STATE OVERLAY |
| Q11–Q20 | Constitucional e outros núcleos gerais | não para Regime Geral N/R | OUT_OF_SCOPE |

## Falha H7-Q2 — circunscrição territorial

### O que a questão exigia
Identificar quais agentes, pela Lei 8.935, estão explicitamente sujeitos às normas que definem circunscrições geográficas.

### Fonte legal
Art.12 da Lei 8.935: oficiais de registro de imóveis e oficiais de registro civil das pessoas naturais ficam sujeitos às normas que definirem as circunscrições geográficas.

A mesma arquitetura exige não confundir:
- tabelião de notas: escolha livre pelo usuário, mas o tabelião não pode praticar atos fora do Município para o qual recebeu delegação;
- RI/RCPN: circunscrição territorial expressamente tratada no art.12;
- protesto: territorialidade segue regras próprias da especialidade.

### Material v0.1
Não ensinava arts.8–13 nem qualquer mapa de atribuição/circunscrição.

### Diagnóstico
`MATERIAL_GAP`.

### Patch
Criar **RG0B — Atribuições e territorialidade básica** em P1, compacto, sem transformar o módulo em estudo das especialidades.

## Falha H7-Q3 — art.36 / afastamento preventivo

### O que a questão exigia
Providências possíveis durante apuração disciplinar e efeitos patrimoniais durante afastamento/intervenção.

### Fonte legal atual
Lei 8.935, art.36:
- afastamento preventivo do titular por até 90 dias, prorrogável por mais 30;
- designação de interventor quando o substituto também estiver acusado ou quando conveniente à apuração;
- durante a intervenção, o titular recebe metade da renda líquida da serventia;
- a outra metade fica em conta especial;
- absolvição → saldo ao titular;
- condenação → saldo ao interventor, conforme regime legal.

### Material v0.1
Ensinava o boundary `90 + 30`, perda e proporcionalidade, mas não ensinava:
- lógica de afastamento preventivo;
- quando surge interventor;
- fluxo 50%/50% da renda.

### Diagnóstico
`MATERIAL_GAP + DEPTH_GAP`.

### Patch
Subir o **microfluxo do art.36** para P1 por três razões:
1. regra curta;
2. alto poder discriminatório;
3. prova oficial estadual direta.

## Falha H7-Q4 — previdência e contagem recíproca

### O que a questão exigia
Reconhecer que tempo anterior de serviço em sistemas previdenciários diversos pode ser contado reciprocamente no regime legal da atividade notarial/registral.

### Fonte legal
Lei 8.935, art.40:
- notários, registradores, escreventes e auxiliares são vinculados à previdência social federal;
- é assegurada contagem recíproca de tempo de serviço em sistemas diversos.

### Material v0.1
Nada ensinava sobre arts.39–40 / previdência.

### Diagnóstico
`MATERIAL_GAP`.

### Patch
Criar **RG8 — Extinção/Previdência/Disposições finais úteis**, extremamente curto em P1:
- extinção da delegação apenas como mapa;
- previdência federal;
- contagem recíproca.

Não expandir para tratado previdenciário.

## Resultado de validação
O frozen specimen v0.1 **NÃO atingiu S2**.

Dos três itens in-scope encontrados em um recorte held-out limpo:
- 3/3 revelaram informação não ensinada ou ensinada insuficientemente.

Isso NÃO significa que todo o material esteja errado. Significa que o escopo P1 ainda estava estreito demais para Regime Geral estadual multibanca.

## Valor da falha
A falha confirma a utilidade da arquitetura:
- não culpar o aluno;
- não declarar “suficiente” por impressão;
- não esconder erro do material;
- patch orientado por questão legítima;
- reteste deve usar corpus ainda não consumido.

## Regras para o patch
1. não inflar o módulo inteiro;
2. subir apenas regras de baixo custo e alto valor probatório;
3. manter especialidades fora do Regime Geral;
4. transformar Q2/Q3/Q4 em evidência de BUILD futuro, nunca reutilizá-las para validar v0.2;
5. retestar v0.2 com novo held-out limpo.

## Próximo estado
- Depth Budget Regime Geral → v0.3;
- internal specimen → v0.2;
- H7 = CONSUMED/FAILED;
- abrir novo held-out somente depois do novo freeze.
