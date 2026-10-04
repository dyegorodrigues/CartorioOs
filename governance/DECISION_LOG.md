# Decision Log — Legal Tutor OS

## 2026-10-04 — GOV-001 · Separação de responsabilidades
**Decisão:** Drive = fontes/binários; GitHub = cérebro operacional público-safe; Notion = painel humano; PDF/HTML/DOCX = produtos gerados.  
**Motivo:** evitar duplicação, perda de rastreabilidade e dependência de conversa.

## 2026-10-04 — GOV-002 · Fontes comerciais imutáveis
**Decisão:** DD, Gran e demais PDFs-fonte ficam preservados por edição/ano e não são reescritos in-place.  
**Motivo:** manter prova-fonte, permitir diff e evitar confundir material original com edição própria.

## 2026-10-04 — GOV-003 · Claude V3 rebaixado para histórico
**Decisão:** protótipo Claude V3 não é modelo-base.  
**Motivo:** feedback humano apontou excesso de compressão, explicações insuficientes, perguntas inadequadas e respostas imprecisas.  
**Reuso permitido:** somente componentes isolados que passem por nova validação.

## 2026-10-04 — GOV-004 · Contrato editorial
**Decisão:** DD fornece currículo/profundidade; Gran fornece gramática didática/visual; Passo e Brainscape informam engenharia de perguntas; fontes oficiais e questões reais auditam correção e suficiência.  
**Motivo:** cada fonte resolve um problema diferente.

## 2026-10-04 — GOV-005 · Terminologia de prova é obrigatória
**Decisão:** todo nó deve registrar termos canônicos, aliases/sinônimos cobrados e formulações relevantes de banca.  
**Motivo:** não permitir que simplificação didática substitua nomenclatura efetivamente exigida.

## 2026-10-04 — GOV-006 · Perguntas derivadas de conteúdo validado
**Decisão:** não gerar perguntas antes de mapear e auditar o conteúdo. Progressão: panorama → discriminação → precisão → aplicação → produção.  
**Motivo:** impedir cartões artificiais, redundantes ou sem utilidade de prova.

## 2026-10-04 — GOV-007 · Questões como QA curricular
**Decisão:** questão real que cobra algo não ensinado abre bug curricular; falhas são classificadas em lacuna, didática, recall ou aplicação.  
**Motivo:** usar o corpus de provas para testar o material, não apenas o aluno.

## 2026-10-04 — GOV-008 · Não escalar antes do piloto
**Decisão:** PEN-DP01-C01 será validado antes de expandir em massa para Penal/Constitucional/etc.  
**Gate:** ensinar do zero, permitir recuperação e resolver questões-alvo sem depender das fontes ao lado.

## 2026-10-04 — GOV-009 · Repositório público com conteúdo public-safe
**Decisão:** enquanto o cérebro reside no repositório público `CartorioOs`, não versionar PDFs comerciais, transcrições pessoais nem links privados do Drive.  
**Motivo:** proteção de conteúdo e privacidade. Uma futura migração para repositório privado pode ampliar o que é versionado.
