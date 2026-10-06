# Auditoria comparativa — delegado-os v1.1 × Tutor OS
**Data:** 06/10/2026
**Objeto:** repositório `dyegorodrigues/delegado-os` e PDF `DP-01 Cap 1 - Edicao de estudo v1.1.pdf`

## Estado do repositório delegado-os
- `main` contém o PR #1 já mergeado.
- O projeto possui `CLAUDE.md`, regras editoriais/workflow/perguntas/banco, histórico, fontes, banco de questões e renderer HTML/CSS/Python.
- Cap. 1 v1.1 registrado como 49 páginas, 113 perguntas progressivas, 12 perguntas de revisão, 6 questões oficiais comentadas e 17 C/E autorais.
- A branch `claude/delegado-claude-code-migration-3oumu1` ainda existe, mas as mudanças centrais já estão em `main`.

## Veredito
A v1.1 é claramente superior ao MASTER V1 do Tutor OS como **produto de estudo visual** e, em vários trechos, superior também ao protótipo Topic 1 V2.

O ganho vem de:
- continuidade visual;
- tabelas que carregam teoria;
- destaques palavra a palavra;
- perguntas integradas ao fluxo;
- fechamento multicamada;
- marcação de versão;
- build reproduzível.

Não adotar a v1.1 como conteúdo canônico sem nova auditoria.

## Pontos fortes que devem ser absorvidos
1. Layout e renderer HTML/CSS/Python.
2. `Em 1 minuto` como orientação, não como substituto da teoria.
3. Tabelas de alta densidade como corpo principal quando apropriado.
4. Perguntas no mesmo fluxo visual do tópico.
5. Fechamento com:
   - resumo;
   - perguntas-mãe;
   - questões reais;
   - C/E.
6. Barra visual de versão e changelog.
7. Fontes por tópico.
8. Aliases no próprio rótulo.
9. Reconexões internas (“cap. X”, “tópico Y”) quando úteis.

## Riscos da governança atual do delegado-os

### 1. “Nunca menos conteúdo que o DD”
A regra “toda proposição do DD entra” protege contra lacuna, mas pode produzir crescimento enciclopédico.
Nova regra recomendada:
- toda proposição do DD deve ser **decidida**, não necessariamente ocupar o mesmo peso na superfície;
- estados: CORE, EXPLAIN_INLINE, TABLE, RECONNECTION, ADVANCED, REFERENCE;
- nada importante some, mas o aluno não recebe tudo com o mesmo peso.

### 2. 113 perguntas progressivas
A quantidade pode ser ótima como **banco**, mas perigosa como rotina de revisão.
Separar:
- learning bank;
- review core;
- adaptive errors;
- advanced/oral.

### 3. Incidência ainda não é censo
O audit do Claude usa ~30 itens/pistas no capítulo e algumas provas oficiais.
Isso é bom piloto, não suficiente para inferir incidência robusta em “todas as provas de Delegado”.
Tutor OS mantém censo mais amplo.

### 4. Brainscape ainda é análise por pack, não por card
O documento do delegado-os analisou 7 packs principais e estilos.
Não existe ainda:
- ingestão card a card dos decks úteis;
- crosswalk card → microtópico → Claim → prova;
- deduplicação semântica;
- ranking de formulações.

Portanto, ainda há espaço grande para nossa mineração sistemática.

## Pontos jurídicos/editoriais ainda a revisar na v1.1

### A. Regras × princípios
A fórmula “regras rígidas/fechadas; princípios abertos que admitem flexibilização” é simplificadora demais para o C01 e cria desvio para teoria geral do Direito.
Provável destino: explicação inline curta ou retirada da pergunta autônoma.

### B. Definições de Liszt/Mezger/Welzel/Cirino
Ocupam bloco e card próprios sem forte incidência de Delegado comprovada no corpus atual.
Manter como ADVANCED/REFERENCE, não exigir na primeira rota.

### C. Harm principle
Útil para compreender paternalismo e PF/2025, mas o bloco/card pode estar superdimensionado para este capítulo.
Preferível como reconexão/Delegado+ salvo nova evidência.

### D. Roxin “prevalece”
Uma questão Vunesp não basta para transformar em enunciado geral de prevalência doutrinária.
Reescrever por contexto da banca/prova.

### E. Jakobs
As fórmulas:
- “sem direito às garantias”;
- radical = só reconhece limites próprios;
- monista = independe dos demais ramos;
- sociedade deve se ajustar ao Direito Penal;
precisam de auditoria doutrinária forte antes de entrarem em material canônico.

### F. Ius puniendi
“nasce quando a lei penal é violada” é impreciso.
Separar poder punitivo em abstrato e pretensão punitiva concreta.

### G. Direito de Intervenção
Lei de Improbidade deve aparecer, se mantida, como aproximação/analogia doutrinária, não como implementação formal brasileira.

### H. Conteúdo extra por questão isolada
Escolas raras, nomes/universidades e detalhes históricos devem ser promovidos segundo:
- repetição em provas;
- valor oral/discursivo;
- poder de discriminação;
não apenas porque apareceu uma vez.

## Decisão para nossa V2
Não competir com o Claude escrevendo outro PDF inteiro do zero.

Construir por cima da melhor infraestrutura já visível:
- experiência visual/renderer do delegado-os;
- DD como coverage floor auditado;
- question mining mais profundo;
- banco de provas/censo mais amplo;
- claims/freshness/auditoria do Tutor OS;
- roteamento adaptativo das perguntas.

## Próximo passo antes de nova redação
Incorporar as reclamações do usuário sobre a v1.1 e produzir uma matriz:
`manter | corrigir | rebaixar | mover | expandir | testar`
para cada bloco do capítulo.

Não expandir o C01 inteiro antes dessa matriz.
