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
- protocolo pedagógico `pedagogy/ADVANCE_ORGANIZER_PROTOCOL.md`: mapa da floresta / schema-first / pre-training / progressive disclosure;
- página Notion `GX Cartório — Mapa da Floresta & Advance Organizer v0.1`;
- **regra anti-tree-bias formalizada**: a árvore do edital é interface de navegação; o motor real é grafo multidimensional;
- arquitetura `architecture/ZERO_TO_OUTORGA_SYSTEM.md`: uma base jurídica canônica com renderização objetiva, discursiva, prática e oral;
- página Notion `GX Cartório — Zero à Outorga & Anti-Tree-Bias v0.1`;
- ENAC 2026.1 Tipo 1: **100/100** classificados na passagem 1 do Question Intelligence Lab;
- ENAC 2025.2 Tipo 1: **100/100** classificados na passagem 1;
- Q24 do ENAC 2025.2 registrada como anulada conforme gabarito definitivo;
- QA do banco: quatro registros antigos de bootstrap do 2026.1 preservados, mas excluídos das métricas;
- Q87 e Q95 do ENAC 2026.1 registradas como anuladas conforme gabarito definitivo;
- matrix drift histórico confirmado: 2025.2 e 2026.1 usam 60 N/R + 14 Civil + 9 Constitucional + 4 Administrativo + 4 Tributário + 4 Empresarial + 2 Processo Civil + 1 Penal + 1 Processo Penal + 1 Conhecimentos Gerais; a matriz 2026.2 muda para 8 Constitucional, remove Conhecimentos Gerais e adiciona Trabalho + Processo do Trabalho;
- análise intraprova 2026.1 versionada em `research/ENAC_2026_1_CLASSIFICATION.md`;
- análise intraprova 2025.2 passagem 1 fechada em `research/ENAC_2025_2_CLASSIFICATION.md`;
- corpus multibanca atualizado para v0.2 com classes de complexidade jurídica L4/L3/L2/L1 e regra anti-contaminação;
- Question Intelligence Lab ampliado com `Complexidade jurídica`, `Família da fonte`, `Snapshot histórico`, `Snapshot atual` e `Mecanismo do distrator`;
- protocolo de perfil temporal de banca em `research/BANK_DNA_PROTOCOL.md`;
- auditoria inicial de materiais/cursos: VFK, Estratégia, G7, PreparaEnac, QConcursos e obras especializadas;
- política `Freshness Firewall` versionada;
- Legal Source Registry ampliado com freshness, vigência, revalidação e impacto sobre materiais;
- atos CNJ 224/2026, 229/2026, 246/2026 e 253/2026 semeados como fontes HOT para propagação de impacto.

## Progresso verificável
- Matérias do ENAC 2026.2: **11/11**.
- Temas oficiais de alto nível: **181/181**.
- Subtemas oficiais N/R: **138/138**.
- Questões ENAC históricas classificadas na passagem 1: **200/300**.
- ENAC 2026.1: **100/100**.
- ENAC 2025.2: **100/100**.
- ENAC 2025.2 anuladas: **1 (Q24)**.
- ENAC 2026.1 anuladas: **2 (Q87 e Q95)**.
- Prova ENAC restante para passagem 1: **2025.1 Q1–Q100**.

## Limitação operacional temporária
- O recurso de consulta estruturada (`Query Data Source`) do Notion atingiu a cota do workspace durante a auditoria final do 2025.2.
- As gravações Q61–Q100 retornaram sucesso e o fechamento foi versionado; a recontagem SQL final será feita quando a consulta voltar a ficar disponível.
- Não inferir falha de dados por essa limitação de leitura.

## O que NÃO está concluído
- recontagem estruturada final do ENAC 2025.2 no Notion após liberação da cota de consulta;
- passagem 2 das questões 2026.1 e 2025.2 para relacionar cada item ao Subtema/Microtema fino e revalidar snapshots atuais;
- criação de Microtemas úteis abaixo dos 138 subitens N/R e abaixo dos temas das demais matérias;
- classificação do ENAC 2025.1;
- expansão sistemática do corpus same-topic/same-bank em FGV L4/L3 e cartório multibanca;
- estatísticas históricas de incidência próprias do GX;
- sequência pedagógica final por pré-requisitos;
- diagnóstico individual do candidato;
- corpus completo de discursivas, peças e orais estaduais;
- auditoria especializada por matéria/obra e por fase estadual.

## Próximo bloco obrigatório antes de promover prioridades
### A. Corpus ENAC
1. classificar **ENAC 2025.1 — 100/100**;
2. rodar QA 300/300;
3. normalizar resultados pela matriz de cada edição;
4. registrar anuladas/alteradas e contexto temporal;
5. comparar persistência, recência e mudanças de estilo;
6. só após 300/300 calcular incidência, recorrência e sinais temporais da FGV com pretensão preditiva calibrada.

### B. Curriculum Graph
1. usar os **138 subtemas N/R oficiais** como espinha canônica;
2. criar Microtemas apenas quando questão, regra, pré-requisito, jurisprudência ou distinção justificar granularidade separada;
3. decompor as demais matérias na mesma lógica, sem gerar nós decorativos;
4. ligar questão → micro/subtema → fonte → habilidade → material;
5. marcar pré-requisitos e conexões interdisciplinares;
6. separar profundidade ENAC de aprofundamento estadual/discursivo/oral.

### C. Corpus expandido / bancos
1. FGV cartório além do ENAC;
2. FGV L4/L3 de mesma matéria/microtema (ENAM, magistratura e outras carreiras jurídicas comparáveis);
3. cartório Cebraspe/Vunesp/outras bancas;
4. questões de outras carreiras/bancas para transferência;
5. L1/L2 apenas como drill de fundamento, sem inferir DNA de banca avançada;
6. triangulação oficial → fonte primária → comentário qualificado.

### D. Pedagogia e material
1. produzir L0 Career Map, L1 Discipline Maps, L2 Theme Maps e L3 previews;
2. manter arquitetura `MAP → MASTER → REVIEW → RECALL → EXAM → REFERENCE`;
3. reconstruir base just in time para candidato enferrujado;
4. flashcards só para conhecimento atomicamente recuperável;
5. casos, discursiva, peça e oral para relações/transferência;
6. tratar objetiva, discursiva, prática e oral como **saídas diferentes da mesma unidade jurídica**, não cursos separados.

### E. Freshness
1. manter radar de CNJ/legislação/jurisprudência;
2. propagar mudanças para nós e materiais derivados;
3. bloquear questões sintéticas apoiadas em fonte `Revalidar`/histórica;
4. manter snapshots separados: direito atual, marco da prova-alvo e direito vigente na prova histórica.

### F. Concursos estaduais
1. formar corpus de editais/provas recentes;
2. separar regime anterior e posterior à Resolução 696/2026;
3. mapear discursivas, peças práticas e oral;
4. identificar conteúdo nacional uniforme e deltas locais;
5. atualizar overlays quando surgir concurso-alvo.

## Regra de qualidade
Nenhum número de “incidência”, “chance de cair” ou “prioridade preditiva” é canônico antes de a origem dos dados estar documentada e o corpus correspondente estar classificado. A matriz do edital garante **cobertura**; as provas dão evidência de **cobrança**; o grafo pedagógico define **ordem de aprendizagem**; o desempenho individual define **adaptação**; o Freshness Firewall garante que a proposição jurídica ainda é válida. Perfis de banca são versionados por período; mudança observável de estilo não autoriza inferir uso de IA sem evidência externa.
