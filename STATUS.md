# GX Cartório OS — Estado Atual

Atualizado em 08/09/2026.

## Branch HOT
`chatgpt/gx-cartorio-v0.1`

## Já consolidado
- arquitetura ChatGPT + Notion + GitHub;
- Material Mestre separado da telemetria;
- baseline regulatório da Resolução CNJ 696/2026;
- pesos atuais do ENAC 2026.2;
- modelo National Core + State Overlay;
- taxonomia multibanca para engenharia reversa de questões;
- protocolo editorial do material;
- workflow adaptativo diário;
- radar normativo automático;
- matriz ENAC 2026.2 completa no nível **Tema**: 11 matérias + 181 temas oficiais de alto nível;
- **138/138 subitens expressos de Direito Notarial e Registral (1.1–11.2)** materializados como Subtemas;
- protocolo pedagógico `pedagogy/ADVANCE_ORGANIZER_PROTOCOL.md`;
- arquitetura `architecture/ZERO_TO_OUTORGA_SYSTEM.md`: uma base jurídica com saídas objetiva, discursiva, prática e oral;
- **Dual Spine** formalizada em `architecture/DUAL_SPINE_CURRICULUM.md`: edital visível e segmentado por matéria + grafo multidimensional como motor interno;
- regra anti-embaralhamento: blocked foundation → discriminação local → transferência → simulação no formato real da prova;
- Depth Budget P0–P4 para impedir estudo enciclopédico sem utilidade para aprovação;
- runtime pedagógico `pedagogy/CHAT_TUTOR_RUNTIME.md`: `Começar estudo` → ensinar → recuperar → testar → diagnosticar → revisar → registrar → recalibrar;
- stack gratuita formalizada em `architecture/FREE_TOOLING_STACK.md`;
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

## Objetivo canônico do candidato
**Aprovação em todas as etapas.**

O GX não otimiza para erudição máxima nem para formação profissional completa antes da prova. Fundamentos, teoria, doutrina e prática entram na profundidade necessária para:
- entender;
- lembrar;
- acertar;
- discriminar alternativas;
- resolver caso novo;
- fundamentar discursiva/peça;
- responder oralmente;
- executar sob tempo e pressão.

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

## Stack gratuita canônica
### GitHub
Source of Truth versionado para arquitetura, estado HOT, protocolos, matrizes e meta-análises.

### Google Sheets
Novo destino planejado para o **Operational Data Plane**: questões, alternativas, mastery, revisões, sessões, erros, produção e dashboard. Migração será auditada e incremental para não criar duas verdades.

### Notion Free
Permanece como **Human Knowledge Portal**: Command Center, mapas, páginas didáticas e Material Mestre. Nenhuma função central dependerá de consulta avançada paga.

### Google Drive
Corpus de PDFs, provas, espelhos, arquivos e materiais pesados.

## Restrição do Notion Free
A consulta estruturada avançada disponível pela integração aparece como recurso dependente de plano pago no workspace atual.

Portanto:
- não assumir reset diário como fundamento arquitetural;
- não assinar plano pago;
- usar a consulta avançada quando eventualmente disponível apenas como bônus;
- mover telemetria/agregações para Google Sheets;
- manter Notion para navegação e conteúdo humano.

## O que NÃO está concluído
- QA agregado final 300/300 por uma camada estruturada independente do Notion pago;
- migração auditada do Operational Data Plane para Google Sheets;
- passagem 2 das 300 questões: Tema/Subtema/Microtema fino, fundamento, alternativa por alternativa e snapshots atuais;
- criação de Microtemas úteis abaixo dos subtemas oficiais e temas das demais disciplinas;
- meta-análise quantitativa/qualitativa/temporal/semântica final das 300;
- expansão sistemática do corpus FGV L4/L3 e cartório multibanca;
- Discipline Maps e progressões pedagógicas completas das 11 matérias;
- diagnóstico individual do candidato;
- calibração individual do espaçamento/retrieval;
- corpus completo de discursivas, peças e orais estaduais;
- auditoria especializada por matéria/obra e por fase estadual;
- Material Mestre completo.

## Próximo bloco obrigatório antes de promover prioridades
### A. Data Plane gratuito + QA 300
1. congelar schema operacional para Google Sheets;
2. migrar/reconstruir o corpus em lotes verificáveis;
3. preservar IDs/URLs históricas;
4. recontar 300/300 por edição/disciplina/anulação;
5. detectar duplicados/bootstraps e lacunas;
6. declarar Sheets canônico apenas após reconciliação.

### B. Meta-análise 300
1. normalizar matrix drift;
2. fazer passagem 2 semântica;
3. clusterizar microtemas e habilidades que atravessam disciplinas;
4. calcular incidência, recorrência, família de fonte, mecanismo de distrator e sinais temporais;
5. publicar `research/ENAC_300_META_ANALYSIS.md` com níveis de confiança separados para fato, padrão e hipótese preditiva.

### C. Curriculum / Dual Spine
1. preservar a árvore oficial para orientação e cobertura;
2. criar Discipline Maps independentes e coerentes;
3. usar o grafo apenas para pré-requisitos, transferência e revisão;
4. criar Microtemas somente quando houver valor probatório/pedagógico;
5. ligar questão → micro/subtema → fonte → habilidade → material;
6. manter Exam View idêntica à segmentação real da prova.

### D. Corpus expandido
1. FGV cartório além do ENAC;
2. FGV L4/L3 de mesmo microtema: ENAM, magistratura e carreiras jurídicas comparáveis;
3. cartório Cebraspe/Vunesp/outras bancas;
4. outras carreiras/bancas para transferência;
5. Trabalho/Processo do Trabalho lateralmente até existir histórico ENAC;
6. triangulação oficial → fonte primária → comentário qualificado.

### E. Pedagogia e material
1. produzir L0 Career Map, L1 Discipline Maps, L2 Theme Maps e L3 previews;
2. manter `MAP → MASTER → REVIEW → RECALL → EXAM → REFERENCE`;
3. reconstruir base just in time;
4. aplicar retrieval durante o ensino, não apenas ao final;
5. ajustar intervalos de revisão pelo desempenho individual;
6. objetiva, discursiva, prática e oral são saídas da mesma unidade jurídica.

### F. Freshness
1. manter radar CNJ/legislação/jurisprudência;
2. propagar mudanças para nós e materiais derivados;
3. bloquear questões sintéticas baseadas em fonte Revalidar/Histórico;
4. manter direito vigente na prova histórica, direito atual e cutoff do alvo separados.

### G. Concursos estaduais
1. formar corpus de editais/provas recentes;
2. separar regime anterior e posterior à Resolução 696/2026;
3. mapear discursivas, peças e oral;
4. identificar National Core e deltas locais;
5. atualizar overlays quando surgir concurso-alvo.

## Regra de qualidade
Nenhum número de `incidência`, `chance de cair` ou prioridade preditiva é canônico sem origem documentada, QA do corpus e normalização. A matriz garante cobertura; as provas fornecem evidência de cobrança; a Dual Spine preserva orientação e conexões; o desempenho individual define adaptação; o Freshness Firewall valida o direito atual. Perfis de banca são versionados por período, e mudança de estilo não autoriza inferir uso de IA sem evidência externa.
