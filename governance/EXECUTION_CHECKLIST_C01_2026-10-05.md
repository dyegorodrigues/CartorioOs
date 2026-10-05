# EXECUTION CHECKLIST — PEN-DP01-C01
**Data:** 05/10/2026  
**Branch ativa:** `chatgpt/legal-tutor-os-integrated-2026-10-05`  
**Estado:** execução autônoma em andamento

## Regra de produto
O objetivo não é produzir uma enciclopédia jurídica nem um resumo bonito. O objetivo é construir um sistema de aprovação que permita:
**aprender → recuperar → discriminar → transferir → produzir → diagnosticar → retornar.**

A unidade só avança quando o aluno consegue reconhecer o problema, recuperar o conhecimento, aplicar em objetiva e produzir resposta compatível com discursiva/oral quando pertinente.

## Três espinhas simultâneas
1. **Conceitual-pedagógica:** ordem de aprendizagem.
2. **Normativa:** lei, Constituição, súmula, precedente e literalidade conectados ao conceito.
3. **Probatória:** banca, carreira, fase, incidência, distratores e profundidade real.

Essas dimensões pertencem à mesma unidade. Não criar três apostilas paralelas.

---

## G0 — GOVERNANÇA E INFRAESTRUTURA
- [x] Branch integrada criada.
- [x] Branches divergentes reconciliadas sem apagar histórico.
- [x] START_HERE aponta para linha integrada.
- [x] CURRENT_SESSION_POINTER atualizado.
- [x] Artefatos antigos não aprovados marcados como NÃO ESTUDAR / deprecated.
- [x] Runtime isolado pelo catalog/descritores.
- [x] Pipeline status separado de status editorial.
- [x] Claim contract incorporado.
- [x] Question contract incorporado.
- [x] Validação de Claims incorporada ao workflow.
- [x] Política de reuso do legado registrada.
- [ ] Observar/rodar CI com uma alteração completa de conteúdo antes de marcar infraestrutura como congelada.

## G1 — COBERTURA CURRICULAR C01
- [x] Árvore humana v2 criada a partir do DD.
- [x] Diff inicial DD 2025 → 2026 recuperado.
- [x] Crosswalk inicial Gran recuperado.
- [x] Source map técnico reconciliado.
- [ ] Revisar linha por linha DD 2026 do C01.
- [ ] Conferir DD 2025 para conteúdo removido/movido.
- [ ] Cruzar editais Delegado PF/estaduais e carreiras de transferência.
- [ ] Classificar cada microtópico: CORE / ADVANCED / REFERENCE.
- [ ] Resolver fronteiras C01 × C02 e capítulos seguintes.
- [ ] Auditar microlacunas pedagógicas não explicitadas no DD, como pré-requisitos necessários.

## G2 — FONTES DIDÁTICAS
- [x] Gran Sintético catalogado como material-base editorial/didático.
- [x] 33 sintéticos de Penal catalogados no projeto.
- [x] Corpus inicial Passo Estratégico mapeado.
- [x] Brainscape source registry criado.
- [x] Links enviados em 05/10 catalogados por função.
- [x] MRC Penal/Constitucional/Administrativo desmontados e auditados por estrutura.
- [ ] Deep sweep card-a-card dos decks pertinentes ao C01.
- [ ] Marcar duplicidades semânticas entre decks.
- [ ] Classificar resposta: boa para aprender / revisar / C-E / contraste / caso / oral.
- [ ] Registrar falhas técnicas ou respostas juridicamente suspeitas.
- [ ] Construir Calibration Set com conteúdo equivalente e formas diferentes.

## G3 — CORPUS DE PROVAS
- [x] Arquitetura EXAM CORPUS definida.
- [x] Seed index C01 criado.
- [x] Universo-alvo 2023–2026 recuperado do legado.
- [x] Protocolo multibanca recuperado.
- [x] Protocolo oral/discursivo recuperado.
- [ ] Varredura integral por certame prioritário: PF, PCDF, PCPI, PCMG, PCSC, PCPE, PCSP, PCRS e outros relevantes.
- [ ] Incorporar ENAM e ENAC como transferência, sem contaminar incidência Delegado.
- [ ] Incorporar Magistratura, MP, Defensoria e Procuradorias conforme microtópico.
- [ ] Decompor alternativas/distratores das questões-chave.
- [ ] Separar gabarito preliminar/definitivo/anulação.
- [ ] Registrar snapshot jurídico histórico × atual.
- [ ] Construir cobertura por banca, carreira, fase e microtópico.
- [ ] Manter ledger de lacunas de corpus; não alegar completude absoluta da internet.

## G4 — ATUALIZAÇÃO JURÍDICA
- [ ] Conferir legislação em fonte oficial.
- [ ] Conferir súmulas, temas e jurisprudência STF/STJ pertinentes.
- [ ] Marcar freshness por Claim sensível ao tempo.
- [ ] Registrar conflitos: lei × jurisprudência × doutrina × banca.
- [ ] Não corrigir silenciosamente questão histórica.
- [ ] Não promover material de cursinho/deck a autoridade.

## G5 — ENGENHARIA DE PERGUNTAS
- [x] Corpus lógico separado em Exam / Learning Prompt / Answer Pattern.
- [x] Resposta em duas velocidades incorporada ao contrato.
- [ ] Construir árvore de perguntas na mesma progressão da matéria.
- [ ] Perguntas-mãe antes de perguntas-filhas.
- [ ] Pergunta-filho só com justificativa de incidência/confusão/complexidade.
- [ ] Adicionar C/E depois da compreensão.
- [ ] Adicionar aplicação real depois da recuperação.
- [ ] Preparar output oral/discursivo quando pertinente.
- [ ] Validar cada pergunta contra Claim e fonte.

## G6 — MASTER DO ALUNO
**Bloqueado até G1–G5 atingirem amostra suficiente.**
- [ ] Mapa panorâmico.
- [ ] Teoria fluida e autossuficiente.
- [ ] Tabelas estratégicas densas quando agregarem.
- [ ] Destaques de termos técnicos/aliases.
- [ ] Âncoras de reconexão em pontos de alto valor.
- [ ] Lei seca integrada sem misturar comentário à literalidade.
- [ ] Questão-sinal no ponto pedagógico adequado.
- [ ] Perguntas progressivas.
- [ ] Resposta comentada + resposta-relâmpago.
- [ ] EXAM Lab.
- [ ] Oral/discursiva.

## G7 — PROVA DE FOGO
- [ ] Separar conjunto de questões não usado para redigir o MASTER.
- [ ] Testar cobertura em corpus amplo.
- [ ] Classificar falhas: curricular / didática / recall / aplicação / atualização / questão defeituosa.
- [ ] Corrigir o MASTER.
- [ ] Repetir até convergência editorial.
- [ ] Só então marcar `study_ready`.

## G8 — ESCALA
**Proibido escalar antes da prova de fogo.**
Depois de C01 aprovado:
- replicar pipeline para demais capítulos de Penal;
- depois demais matérias;
- manter mesma taxonomia, corpus e governança;
- overlays por carreira mudam prioridade/profundidade, não duplicam conhecimento.
