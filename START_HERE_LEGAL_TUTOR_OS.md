# Legal Tutor OS — START HERE

## Missão

Construir materiais jurídicos de alta performance para concursos, começando por Direito Penal com foco prioritário em Delegado estadual e federal, sem reduzir o conteúdo a um "resumo bonito". O sistema deve permitir aprender do zero, revisar, recuperar ativamente, resolver questões e sustentar respostas discursivas/orais.

## Papéis dos sistemas

- **Google Drive** = cofre de fontes e artefatos binários. PDFs originais permanecem imutáveis e versionados por edição/ano.
- **GitHub** = cérebro operacional público-safe: arquitetura, contratos editoriais, IDs estáveis, conteúdo autoral/derivado permitido, código, validações e histórico de mudanças. Não incluir PDFs comerciais, transcrições pessoais ou links privados do Drive.
- **Notion** = painel humano: navegação, status, decisões, auditorias, registro de feedback e leitura editorial. Não é a única fonte canônica.
- **PDF/HTML/DOCX** = produtos gerados. Nunca são a única fonte editável/canônica.

## Ordem de reancoragem para qualquer nova conversa/IA

1. Ler este arquivo.
2. Ler `governance/CURRENT_SESSION_POINTER.json`.
3. Ler `governance/GOVERNANCE_V3_2026-10-04.md`.
4. Ler o `module.json` do módulo indicado no ponteiro.
5. Consultar no Notion o **DOSSIÊ PILOTO 01 — Introdução ao Direito Penal** e o checkpoint mais recente.
6. Consultar no Drive apenas as fontes necessárias ao slice atual.
7. Só então pesquisar web/fontes oficiais ou editar conteúdo.

Se houver conflito, prevalece: instrução expressa mais recente do usuário > governança V3 > ponteiro atual > documentos antigos.

## Branch ativa

`chatgpt/legal-tutor-os-integrated-2026-10-05`

Branches anteriores ficam preservadas como histórico e fonte de comparação. A linha integrada é a única linha ativa para novas mudanças.

## Estado editorial atual

- **Matéria:** Direito Penal.
- **Apostila:** PEN-DP01 — Noções iniciais e princípios.
- **Módulo em foco:** PEN-DP01-C01 — Conceito, características, objeto, evolução, funções e divisões.
- **Situação:** recalibração após rejeição do protótipo Claude V3.
- **Próximo objetivo:** construir o primeiro slice vertical realmente ensinável e auditável, antes de escalar.

## Feedback do usuário que passa a ser requisito

O protótipo anterior foi rejeitado porque:
- comprimiu demais e ficou vago;
- explicações eram insuficientes para aprender e até para revisar;
- perguntas foram criadas sem boa engenharia e algumas eram inadequadas;
- respostas eram imprecisas, telegráficas ou pouco organizadas;
- o visual tinha bons insights, mas a densidade e a sequência pedagógica falharam.

Consequência: **nenhum material é promovido por estar bonito, curto ou organizado**. Precisa ensinar, preservar nomenclatura de prova e sobreviver ao teste com questões reais.

## Contrato pedagógico resumido

1. **DD = currículo e profundidade.**
2. **Gran PDF Sintético = gramática didática/visual e base editorial a aperfeiçoar.**
3. **Passo Estratégico + bons decks Brainscape = referências para engenharia de perguntas, nunca autoridades jurídicas.**
4. **Lei seca + STF/STJ + fontes oficiais = atualização e verificação.**
5. **Questões reais = auditoria do material e inteligência de banca.**
6. **Decorando/Estudo Lei Seca = referência funcional para camada artigo → destaque → verdadeiro/falso → explicação.**

## Regras editoriais não negociáveis

- Preservar terminologia, sinônimos, classificações e nomenclaturas efetivamente cobradas.
- Linguagem pode ser agradável e didática; **não substituir o termo técnico por paráfrase inventada**.
- Tabela é ferramenta de relação/comparação, não licença para amputar explicações.
- Texto corrido só entra quando explica melhor que um quadro.
- Sintético = alta densidade útil + baixa fricção cognitiva, não "poucas palavras".
- Pergunta só entra se tiver função, nó curricular e resposta suficiente.
- Progressão preferida: **visão panorâmica → comparação/discriminação → precisão → aplicação → produção**.
- Questões oficiais preservam banca, ano, cargo, gabarito histórico e eventual mudança jurídica posterior.
- Se uma questão cobra algo não ensinado, abrir **bug curricular**.
- Não escalar para toda a matéria antes de o piloto passar pelos gates editoriais.

## Gates antes de marcar um módulo como pronto

- Cobertura curricular mapeada.
- Terminologia e sinônimos auditados.
- Atualização legal/jurisprudencial sensível ao tempo verificada.
- Perguntas ligadas a nós reais e revisadas.
- Questões reais usadas como teste de suficiência.
- Leitura digital aprovada.
- Exportação/impressão aprovada.
- Feedback humano incorporado.


## Execução vigente
- Checklist operacional: `governance/EXECUTION_CHECKLIST_C01_2026-10-05.md`
- Princípios de produto: `governance/PRODUCT_PRINCIPLES_2026-10-05.md`
- Estado exato: `governance/CURRENT_SESSION_POINTER.json`


## Escala e manutenção
- Fábrica reutilizável de módulos: `architecture/MODULE_FACTORY_V1.md`
- Política de versionamento/freshness: `governance/VERSIONING_FRESHNESS_POLICY_V1.md`
- Template de pesquisa: `templates/MODULE_RESEARCH_TEMPLATE.md`
