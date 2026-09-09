# GX Cartório OS — Free Tooling Stack

Atualizado em 08/09/2026.

## Regra de produto
O GX deve funcionar sem exigir assinatura adicional do usuário.

Nenhuma função pedagógica central pode depender de recurso pago do Notion, Airtable, Anki, banco de dados comercial ou serviço premium externo.

Se um recurso pago ficar disponível temporariamente, ele é tratado como aceleração opcional, nunca como dependência arquitetural.

## Stack canônica gratuita

### 1. GitHub — Source of Truth versionado
Função: governança, protocolos, matrizes, pesquisas, regras do sistema e artefatos estruturais.

Guardar no GitHub:
- STATUS e ponteiro HOT;
- matriz canônica do edital;
- taxonomias;
- protocolos de classificação/QA;
- meta-análises;
- arquitetura pedagógica;
- políticas de freshness;
- schemas de dados;
- regras de cálculo e priorização;
- snapshots/reconstruções que precisam de histórico auditável.

O GitHub vence conflitos de arquitetura e regras versionadas.

### 2. Google Sheets — Operational Data Plane
Função: dados estruturados de alto volume, métricas e filas operacionais.

Motivo: o Google Sheets suporta até 10 milhões de células por arquivo, escala suficiente para dezenas de milhares de questões e eventos de estudo no estágio atual do GX.

Arquivo operacional preferencial: `GX Cartório — Data Plane`.

Tabs previstas:
1. `Curriculum`
2. `Questions`
3. `Question_Alternatives`
4. `Sources`
5. `Mastery`
6. `Review_Queue`
7. `Sessions`
8. `Errors`
9. `Production`
10. `Dashboard`
11. `Config`

### 3. Notion Free — Human Knowledge Portal
Função: leitura confortável, mapas, Command Center e Material Mestre.

Usar para:
- Command Center;
- mapas de matéria;
- páginas didáticas MASTER/REVIEW;
- páginas de decisão;
- guias navegáveis;
- resumos de estado.

Não usar como banco operacional crítico quando a automação exigir consultas estruturadas pagas.

O plano Free individual continua útil para páginas e bases visuais. O limite da integração avançada não deve bloquear o sistema.

### 4. Google Drive — Corpus e arquivos pesados
Função:
- provas oficiais;
- PDFs e espelhos;
- materiais adquiridos/legalmente disponíveis;
- exportações;
- arquivos maiores que não devem viver dentro do Notion.

Sempre preservar a URL/fonte e metadados de autoridade/data.

## O que não adotar como núcleo agora

### Airtable Free
Não adotar como data plane principal.

Razões atuais:
- 1.000 registros por base;
- 1.000 chamadas de API por workspace/mês.

Isso é pequeno para Question Intelligence + alternativas + sessões + revisões + erros + produção.

### Obsidian
Bom para conhecimento pessoal, mas adicionaria outra interface e não oferece vantagem suficiente sobre GitHub + Notion + Drive no workflow atual.

### Supabase/Postgres
Pode ser excelente no futuro quando o GX virar aplicação própria, mas introduzir backend agora aumenta engenharia antes de necessidade real.

### Anki como dependência
Não será obrigatório. A lógica de spaced retrieval pertence ao GX.

Exportar para Anki pode virar saída opcional futura, sobretudo no Android, mas o candidato não deve administrar decks para o sistema funcionar.

## Separação de responsabilidades

| Tipo de informação | Canônico |
|---|---|
| regra de arquitetura | GitHub |
| estado HOT | GitHub |
| dado operacional tabular | Google Sheets |
| página didática navegável | Notion |
| arquivo/PDF/corpus | Google Drive |
| conversa diária | ChatGPT, com persistência dos efeitos nas camadas acima |

## Chat Is Not Memory
O chat é o cockpit.

Ao final de uma sessão relevante, o sistema deve persistir automaticamente:
- novos erros;
- mastery atualizado;
- próxima revisão;
- questões resolvidas;
- evidências de retenção;
- decisões pedagógicas;
- mudanças de arquitetura, quando existirem.

A conversa pode desaparecer sem destruir o estado do candidato.

## Política para o limite do Notion
Não assumir que o acesso avançado de consulta estruturada reinicia diariamente.

Estado operacional seguro:
- tratar Query Data Source avançado como indisponível no plano gratuito;
- usar se estiver disponível, mas nunca depender dele;
- migrar agregações e telemetria para Sheets;
- manter Notion como visualização e conteúdo humano.

## Migração sem drift
A migração Notion → Sheets deve ser incremental e auditada.

1. congelar schema alvo;
2. exportar/reconstruir registros em lotes verificáveis;
3. preservar IDs/URLs originais;
4. conferir contagens por prova/matéria;
5. conferir anuladas/excluídas;
6. comparar amostras linha a linha;
7. somente depois declarar Sheets como data plane canônico;
8. manter Notion como front-end, sem apagar o histórico durante estabilização.

Não criar uma segunda verdade silenciosa.

## Critério de sucesso
O usuário deve poder usar apenas o ChatGPT para estudar e, no máximo, abrir o Notion/Sheets quando quiser visualizar o estado.

Ele não precisa:
- cadastrar flashcards;
- atualizar cronograma;
- escolher próxima matéria;
- organizar questões;
- recalcular revisão;
- mover linhas entre bancos;
- administrar taxonomia.

Esse trabalho pertence ao sistema.

## Fontes públicas verificadas em 08/09/2026
- Notion Free: https://www.notion.com/pricing
- Airtable Free: https://support.airtable.com/docs/airtable-plans-overview
- Google Drive/Sheets limits: https://support.google.com/drive/answer/37603
