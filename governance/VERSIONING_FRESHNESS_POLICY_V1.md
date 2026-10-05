# VERSIONING & FRESHNESS POLICY V1
**Data:** 05/10/2026

## 1. Regra-mãe
Material antigo nunca é presumido inútil e nunca é presumido atual.

Cada proposição relevante deve ser classificada conforme sua natureza:
- doutrina estável;
- legislação;
- jurisprudência;
- edital/prova;
- estatística de incidência;
- técnica pedagógica.

## 2. Edições
Exemplo:
- DD 2025 fica congelado;
- DD 2026 fica congelado;
- DD 2027 será nova fonte.

Não sobrescrever 2025 com “versão atualizada”.

## 3. Diff semântico
Comparar conteúdo por significado, não apenas por texto.

Categorias:
- novo;
- removido;
- alterado;
- movido;
- aprofundado;
- simplificado;
- corrigido;
- superado;
- ainda válido;
- incerto.

## 4. Fonte histórica × estado atual
Questão de 2018 pode estar correta em 2018 e errada hoje.

Guardar:
- `legal_state_at_exam`;
- `current_legal_state`;
- `changed_since_exam`;
- motivo;
- fonte oficial.

## 5. Lei
Registrar:
- diploma;
- dispositivo;
- redação/versionamento;
- vigência;
- fonte oficial;
- data de conferência;
- dispositivos relacionados.

## 6. Jurisprudência
Registrar:
- tribunal;
- classe/número;
- tema/súmula/informativo;
- tese;
- data;
- situação;
- impacto nos Claims;
- data de conferência.

## 7. Materiais preparatórios
DD, Gran, IURIS, Estratégia, Legis etc.:
- são fontes secundárias;
- podem revelar atualização;
- não são prova final de vigência;
- divergência entre materiais abre auditoria.

## 8. Atualização incremental
Não reler todo o acervo a cada mudança.

Quando um evento chega:
1. identificar Claims atingidos;
2. marcar `needs_review`;
3. conferir fonte oficial;
4. atualizar Claim;
5. atualizar perguntas afetadas;
6. atualizar comentários de questões;
7. regenerar outputs.

## 9. Obsolescência
Conteúdo obsoleto pode ser:
- preservado como histórico;
- ocultado do modo de estudo atual;
- usado para explicar evolução;
- ligado a questão histórica.

Nunca deletar silenciosamente se houver valor de auditoria.

## 10. Revisão periódica
Prioridade maior para:
- legislação recente;
- jurisprudência volátil;
- súmulas/temas novos;
- edital novo;
- área com alta incidência;
- Claims que já geraram bugs.

Doutrina estável recebe revisão menos frequente.
