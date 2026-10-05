# Reconciliação de branches — Legal Tutor OS — 05/10/2026

## Problema encontrado
Havia três linhas úteis e divergentes:
- `chatgpt/legal-tutor-os-core-2026-09-30`
- `chatgpt/legal-tutor-os-pen-dp01-pilot-2026-10-04`
- `chatgpt/tutor-os-material-pipeline-v2-2026-10-04`

Elas não “bugam” umas às outras por existirem: Git isola branches. O risco era humano/operacional: continuar em uma linha sem perceber que outra continha pesquisa ou infraestrutura superior.

## Branch integrada vigente
`chatgpt/legal-tutor-os-integrated-2026-10-05`

Base: branch core mais recente.

## O que foi trazido da branch pilot
- laboratório de arquitetura de perguntas;
- diff DD 2025→2026;
- crosswalk Gran;
- corpus inicial de questões oficiais;
- candidatos Brainscape.

## O que foi trazido da pipeline v2
- arquitetura de pipeline material V2;
- contrato de Claim;
- contrato de perguntas;
- source_map do C01;
- validador de Claims;
- workflow com validação de Claims.

## Bug corrigido
O C01 estava com `status: mapped`, mas o validador V1 só aceitava `planned|draft|reviewed`.

Correção:
- `status = draft` → estado editorial compatível;
- `pipeline_status = mapped` → estado de pipeline V2.

Assim, “mapped” deixa de competir com o estado editorial.

## Pastas/arquivos antigos
Arquivos de cartório, ENAC, atlas e pesquisas antigas permanecem no repositório como histórico. Eles **não entram no build modular** salvo se forem referenciados em `content/catalog.json`.

O validador percorre:
- módulos listados no catálogo;
- arquivos explicitamente ligados pelo descritor;
- registries de fontes/leis/questões.

Portanto, uma pasta velha em `research/` ou `data/` não altera o material do aluno por mera existência.

## Regra de isolamento
1. não apagar legado;
2. não importar automaticamente conteúdo legado;
3. usar `catalog.json` como fronteira do runtime;
4. usar branch integrada como única linha ativa;
5. branches anteriores ficam congeladas como fonte de comparação;
6. qualquer migração futura deve ser registrada neste ledger.

## Pendência
Ainda é necessário rodar/observar o CI da branch integrada após as próximas alterações de conteúdo. Ausência de status no commit não equivale a aprovação.
