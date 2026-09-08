# GX Cartório OS — Estado Atual

Atualizado em 08/09/2026.

## Branch HOT
`chatgpt/gx-cartorio-v0.1`

## Já consolidado
- arquitetura ChatGPT + Notion + GitHub;
- bancos operacionais no Notion;
- Material Mestre separado da telemetria;
- baseline regulatório da Resolução CNJ 696/2026;
- pesos atuais do ENAC 2026.2;
- modelo National Core + State Overlay;
- taxonomia multibanca para engenharia reversa de questões;
- protocolo editorial do material;
- workflow adaptativo diário;
- radar normativo automático;
- registro de corpus oficial no Notion;
- matriz ENAC 2026.2 completa no nível **Tema**: 11 matérias + 181 temas oficiais de alto nível;
- **138/138 subitens expressos de Direito Notarial e Registral (1.1–11.2) materializados como Subtemas no Curriculum Graph**;
- primeira revisão de integridade da matriz, incluindo confirmação de `CIV 19 — Contratos imobiliários (Lei 4.380/1964)`;
- protocolo pedagógico `pedagogy/ADVANCE_ORGANIZER_PROTOCOL.md`;
- página Notion `GX Cartório — Mapa da Floresta & Advance Organizer v0.1`;
- regra anti-tree-bias formalizada: árvore do edital = navegação; motor = grafo multidimensional;
- arquitetura `architecture/ZERO_TO_OUTORGA_SYSTEM.md`: uma base jurídica com saídas objetiva, discursiva, prática e oral;
- página Notion `GX Cartório — Zero à Outorga & Anti-Tree-Bias v0.1`;
- ENAC 2025.1 Tipo 1: **100/100** classificados na passagem 1;
- ENAC 2025.2 Tipo 1: **100/100** classificados na passagem 1;
- ENAC 2026.1 Tipo 1: **100/100** classificados na passagem 1;
- corpus oficial ENAC histórico atingiu o gate **300/300**;
- anulações preservadas: 2025.1 Q54/Q88/Q94; 2025.2 Q24; 2026.1 Q87/Q95;
- quatro registros antigos de bootstrap do 2026.1 permanecem excluídos das métricas;
- matrix drift histórico confirmado e normalização por oportunidade definida como obrigatória;
- `research/ENAC_2025_1_CLASSIFICATION.md`, `research/ENAC_2025_2_CLASSIFICATION.md` e `research/ENAC_2026_1_CLASSIFICATION.md` versionados;
- gate de meta-análise criado em `research/ENAC_300_CORPUS_GATE.md`;
- corpus multibanca v0.2 com classes L4/L3/L2/L1 e regra anti-contaminação;
- Question Intelligence Lab registra complexidade jurídica, família da fonte, snapshots histórico/atual e mecanismos de distrator;
- protocolo temporal de banca em `research/BANK_DNA_PROTOCOL.md`;
- auditoria inicial de materiais/cursos: VFK, Estratégia, G7, PreparaEnac, QConcursos e obras especializadas;
- Freshness Firewall ativo e Legal Source Registry ampliado;
- atos CNJ 224/2026, 229/2026, 246/2026 e 253/2026 semeados como fontes HOT.

## Progresso verificável
- Matérias do ENAC 2026.2: **11/11**.
- Temas oficiais de alto nível: **181/181**.
- Subtemas oficiais N/R: **138/138**.
- Questões ENAC históricas classificadas na passagem 1: **300/300**.
- ENAC 2025.1: **100/100**, 3 anuladas.
- ENAC 2025.2: **100/100**, 1 anulada.
- ENAC 2026.1: **100/100**, 2 anuladas.
- Total de anuladas históricas identificadas: **6/300**.

## Matrix drift
As três edições históricas 2025.1, 2025.2 e 2026.1 usam: 60 N/R + 14 Civil + 9 Constitucional + 4 Administrativo + 4 Tributário + 4 Empresarial + 2 Processo Civil + 1 Penal + 1 Processo Penal + 1 Conhecimentos Gerais.

A matriz atual ENAC 2026.2 usa: 60 N/R + 14 Civil + 8 Constitucional + 4 Administrativo + 4 Tributário + 4 Empresarial + 2 Processo Civil + 1 Penal + 1 Processo Penal + 1 Trabalho + 1 Processo do Trabalho.

Consequência: Conhecimentos Gerais é histórico, não currículo atual; Trabalho e Processo do Trabalho precisam de corpus lateral porque ainda não têm histórico ENAC próprio; frequência histórica será normalizada pela oportunidade de cobrança.

## Limitação operacional temporária
- O recurso estruturado `Query Data Source` do Notion atingiu a cota do workspace durante a auditoria final do 2025.2.
- Todas as operações de criação usadas para completar 2025.2 e 2025.1 retornaram sucesso.
- A recontagem SQL final 300/300 e os agregados quantitativos serão rodados quando a consulta voltar a ficar disponível.
- Não inferir falha ou perda de dados a partir dessa limitação de leitura.

## O que NÃO está concluído
- QA estruturado final 300/300 no Notion após liberação da consulta;
- passagem 2 das 300 questões: Tema/Subtema/Microtema fino, fundamento, alternativa por alternativa e snapshots atuais;
- criação de Microtemas úteis abaixo dos subtemas oficiais e temas das demais disciplinas;
- meta-análise quantitativa/qualitativa/temporal/semântica final das 300;
- expansão sistemática do corpus FGV L4/L3 e cartório multibanca;
- sequência pedagógica final calibrada pelo corpus + dependências;
- diagnóstico individual do candidato;
- corpus completo de discursivas, peças e orais estaduais;
- auditoria especializada por matéria/obra e por fase estadual;
- Material Mestre completo.

## Próximo bloco obrigatório antes de promover prioridades
### A. QA + Meta-análise 300
1. recontar 300/300 por edição/disciplina/anulação;
2. detectar duplicados/bootstraps e lacunas de relação;
3. normalizar matrix drift;
4. fazer passagem 2 semântica;
5. clusterizar microtemas e habilidades que atravessam disciplinas;
6. calcular incidência, recorrência, família de fonte, mecanismo de distrator e sinais temporais;
7. publicar `research/ENAC_300_META_ANALYSIS.md` com níveis de confiança separados para fato, padrão e hipótese preditiva.

### B. Curriculum Graph
1. usar os 138 subtemas N/R oficiais como espinha canônica;
2. criar Microtemas apenas quando questão, regra, pré-requisito, jurisprudência ou distinção justificar granularidade separada;
3. decompor as demais matérias na mesma lógica;
4. ligar questão → micro/subtema → fonte → habilidade → material;
5. marcar pré-requisitos e conexões interdisciplinares;
6. separar profundidade ENAC de aprofundamento estadual/discursivo/oral.

### C. Corpus expandido
1. FGV cartório além do ENAC;
2. FGV L4/L3 de mesmo microtema: ENAM, magistratura e carreiras jurídicas comparáveis;
3. cartório Cebraspe/Vunesp/outras bancas;
4. outras carreiras/bancas para transferência;
5. Trabalho/Processo do Trabalho lateralmente até existir histórico ENAC;
6. triangulação oficial → fonte primária → comentário qualificado.

### D. Pedagogia e material
1. produzir L0 Career Map, L1 Discipline Maps, L2 Theme Maps e L3 previews;
2. manter `MAP → MASTER → REVIEW → RECALL → EXAM → REFERENCE`;
3. reconstruir base just in time para candidato enferrujado;
4. flashcards apenas para conhecimento atomicamente recuperável;
5. casos, discursiva, peça e oral para relações/transferência;
6. objetiva, discursiva, prática e oral são saídas da mesma unidade jurídica.

### E. Freshness
1. manter radar CNJ/legislação/jurisprudência;
2. propagar mudanças para nós e materiais derivados;
3. bloquear questões sintéticas baseadas em fonte Revalidar/Histórico;
4. manter direito vigente na prova histórica, direito atual e cutoff do alvo separados.

### F. Concursos estaduais
1. formar corpus de editais/provas recentes;
2. separar regime anterior e posterior à Resolução 696/2026;
3. mapear discursivas, peças e oral;
4. identificar National Core e deltas locais;
5. atualizar overlays quando surgir concurso-alvo.

## Regra de qualidade
Nenhum número de `incidência`, `chance de cair` ou prioridade preditiva é canônico sem origem documentada, QA do corpus e normalização. A matriz garante cobertura; as provas fornecem evidência de cobrança; o grafo pedagógico define ordem; o desempenho individual define adaptação; o Freshness Firewall valida o direito atual. Perfis de banca são versionados por período, e mudança de estilo não autoriza inferir uso de IA sem evidência externa.
