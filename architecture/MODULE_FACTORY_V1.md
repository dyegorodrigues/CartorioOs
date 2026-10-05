# MODULE FACTORY V1 — Legal Tutor OS
**Data:** 05/10/2026
**Status:** padrão operacional reutilizável para todas as apostilas e matérias

## Objetivo
Transformar o trabalho artesanal feito em PEN-DP01-C01 numa linha de produção controlada, auditável e repetível.

Um novo módulo NÃO redefine arquitetura. Ele instancia este pipeline.

---

## Entrada mínima de um novo módulo
- matéria;
- apostila/capítulo de referência;
- DD disponível por ano/edição;
- Gran Sintético correspondente, quando houver;
- DD Legis/Juris/IURIS relacionados, quando houver;
- editais-alvo;
- corpus de provas e bancos de questões;
- fontes oficiais aplicáveis.

## Fase 0 — Identificação e congelamento das fontes
1. catalogar arquivo;
2. registrar edição/ano/hash/localização;
3. nunca sobrescrever fonte antiga;
4. distinguir:
   - teoria;
   - lei seca;
   - jurisprudência;
   - questões;
   - resumo/sintético;
   - histórico/protótipo.

Saída: `source_registry`.

## Fase 1 — Diff editorial e jurídico
Comparar versões:
- DD 2025 × DD 2026 × posteriores;
- Gran antigo × Gran recente;
- Legis/Juris antigos × atuais;
- materiais antigos do usuário × padrão vigente.

Classificar alteração:
- `UNCHANGED`
- `NEW`
- `CHANGED`
- `MOVED`
- `REMOVED`
- `SUPERSEDED`
- `OUTDATED`
- `ERROR_FIXED`
- `NEEDS_REVIEW`

Nunca apagar a versão anterior.

Saída: `version_diff`.

## Fase 2 — Árvore curricular
Construir:
`matéria → tema → tópico → subtópico → microtópico → Claim`

Fontes:
1. DD como espinha curricular/de profundidade;
2. editais oficiais;
3. provas reais;
4. Gran/Passo/Brainscape/MRC como detectores de lacuna;
5. fontes oficiais para correção jurídica.

DD é âncora, não teto.

Saída: `curriculum_tree` + `source_map`.

## Fase 3 — Freshness e autoridade
Para cada Claim sensível ao tempo:
- lei vigente;
- revogação;
- alteração legislativa;
- súmula;
- tema;
- precedente relevante;
- informativo;
- mudança doutrinária relevante para prova;
- mudança de gabarito/entendimento de banca.

Hierarquia:
1. fonte normativa oficial;
2. tribunal/fonte jurisprudencial oficial;
3. prova/gabarito/espelho oficial;
4. doutrina;
5. material preparatório.

Saída: `freshness_ledger`.

## Fase 4 — Corpus de provas
Ingestão por carreira/banca/fase.

Para Delegado:
- todas as provas localizáveis;
- objetiva, discursiva, prática e oral;
- recentíssimas primeiro, histórico depois.

Para outras carreiras:
- overlay próprio;
- não contam artificialmente como incidência de Delegado.

Cada questão:
- exam_id;
- microtópicos/Claims;
- banca/cargo/ano/fase;
- gabarito;
- snapshot histórico/atual;
- mecanismo de cobrança;
- mecanismo de distrator;
- fonte oficial;
- comentário editorial;
- bugs curriculares.

Saída: `exam_corpus`.

## Fase 5 — Corpus de aprendizagem
Varrer:
- Passo Estratégico;
- Brainscape;
- MRC/Anki;
- questões comentadas;
- Notion legado;
- materiais de cursinhos;
- outros bancos.

Classificar cada padrão:
- orientação;
- aprendizagem;
- pergunta-mãe;
- precisão;
- contraste;
- C/E;
- lei seca;
- aplicação;
- oral;
- discursiva;
- prática.

Não copiar indiscriminadamente.
Não promover resposta sem auditoria.

Saída: `learning_prompt_corpus`.

## Fase 6 — Calibration Set
Somente depois de amostra suficiente.

Comparar o mesmo conteúdo em:
- Passo-like;
- Brainscape estruturado;
- tabela estratégica;
- resposta comentada + relâmpago;
- C/E comentado;
- caso;
- oral/discursiva.

Objetivo: calibrar experiência do usuário sem sacrificar rigor.

Saída: `editorial_profile`.

## Fase 7 — MASTER
Só começa após F0–F6 atingirem cobertura suficiente.

MASTER integra:
1. mapa panorâmico;
2. teoria progressiva;
3. tabelas estratégicas;
4. nomenclaturas/aliases;
5. âncoras de reconexão;
6. lei seca;
7. jurisprudência;
8. questão-sinal;
9. perguntas progressivas;
10. resposta explicativa;
11. resposta-relâmpago;
12. C/E;
13. EXAM Lab;
14. oral/discursiva/prática quando pertinente.

Saída: conteúdo canônico estruturado.

## Fase 8 — QA / Prova de fogo
Separar conjunto de questões não usado na redação.

Diagnosticar falhas:
- curricular;
- jurídica;
- didática;
- recall;
- discriminação;
- aplicação;
- atualização;
- questão defeituosa.

Corrigir MASTER e repetir.

Saída: `study_ready`.

## Fase 9 — Renderização
Gerar:
- HTML;
- PDF;
- revisão rápida;
- banco de perguntas;
- lei seca;
- app/plataforma;
- futuras exportações.

Nenhum output renderizado é fonte canônica.

## Fase 10 — Manutenção
Evento novo:
- alteração legislativa;
- novo tema/súmula;
- nova questão importante;
- nova edição DD/Gran;
- correção aceita.

Fluxo:
`evento → Claim afetado → diff → revisão → regeneração dos produtos`.

---

## Gates obrigatórios

### G1 Cobertura
Nenhum microtópico relevante órfão sem decisão explícita.

### G2 Correção jurídica
Claims sensíveis auditados.

### G3 Terminologia
Aliases e nomenclaturas de prova preservados.

### G4 Perguntas
Progressão coerente; sem cards artificiais.

### G5 Prova
Material resolve corpus-alvo em nível adequado.

### G6 Experiência
Leitura/revisão fluem no padrão aprovado.

### G7 Atualização
Freshness registrado.

### G8 Continuidade
Pointer/changelog/status atualizados.

---

## Regra de escala
Ao iniciar um novo módulo:
1. copiar o template de módulo;
2. preencher fontes;
3. executar fases;
4. registrar gaps;
5. não reabrir decisões arquiteturais já congeladas salvo evidência nova.

Se uma melhoria estrutural surgir, ela é:
- testada no módulo atual;
- registrada como decisão;
- incorporada ao Factory;
- aplicada aos próximos módulos;
- retroaplicada aos anteriores apenas quando custo/benefício justificar.
