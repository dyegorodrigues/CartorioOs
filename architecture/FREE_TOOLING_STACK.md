# GX Cartório OS — Free Tooling Stack

Atualizado em 08/09/2026.

## Regra de produto
O GX deve funcionar sem exigir assinatura adicional do usuário.

Nenhuma função pedagógica central pode depender de recurso pago do Notion, Airtable, Anki, banco de dados comercial ou serviço premium externo.

Se um recurso pago ficar disponível temporariamente, ele é tratado como aceleração opcional, nunca como dependência arquitetural.

## Decisão arquitetural atual
**Não criar nem promover um Google Sheets de produção neste momento.**

O corpus 300/300 e o estado atual permanecem onde já estão até que o schema operacional esteja congelado e exista necessidade concreta de analytics/telemetria que justifique um novo data plane.

Motivo: o risco real não é escala de células nem contexto do modelo. O risco é criar duas fontes de verdade, duplicar registros e introduzir drift. A adoção de Sheets será uma migração controlada, não um reflexo automático à limitação do Notion Free.

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

### 2. Notion Free — Human Knowledge Portal + estado visual atual
Função: leitura confortável, mapas, Command Center, Material Mestre e bancos já existentes enquanto forem suficientes.

Usar para:
- Command Center;
- mapas de matéria;
- páginas didáticas MASTER/REVIEW;
- páginas de decisão;
- guias navegáveis;
- resumos de estado;
- Curriculum/Question Lab/Errors/Sessions já existentes, sem depender de consultas avançadas pagas.

O plano Free individual continua útil para páginas e bases visuais. A limitação da integração avançada não deve bloquear o sistema.

### 3. Google Sheets — Candidate Operational Data Plane, ainda não promovido
Função futura potencial: dados estruturados de alto volume, métricas e filas operacionais.

Capacidade técnica não é preocupação imediata: Google Sheets suporta até 10 milhões de células por arquivo, escala suficiente para dezenas de milhares de questões e eventos de estudo no estágio atual do GX.

**Mas capacidade não é critério de adoção.** Sheets só será criado quando:
1. o schema operacional estiver congelado;
2. houver necessidade concreta de consulta/agregação/analytics que o Notion Free não resolva;
3. IDs e regras de reconciliação estiverem definidos;
4. a migração puder ser feita em lotes auditáveis;
5. houver ganho claro de confiabilidade ou eficiência.

Arquivo futuro preferencial, se promovido: `GX Cartório — Data Plane`.

Tabs candidatas:
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

### 4. Google Drive — Corpus e arquivos pesados
Função:
- provas oficiais;
- PDFs e espelhos;
- materiais adquiridos/legalmente disponíveis;
- exportações;
- imagens/mapas/diagramas gerados;
- arquivos maiores que não devem viver dentro do Notion.

Sempre preservar a URL/fonte e metadados de autoridade/data.

## Regra de contexto
Mesmo se Sheets for adotado no futuro, **o tutor nunca carregará a planilha inteira para o contexto**.

O runtime deve ler somente:
- o nó curricular atual;
- revisões vencidas;
- erros relevantes;
- poucas questões candidatas;
- métricas agregadas necessárias à decisão atual.

Dados volumosos permanecem fora da janela de conversa e são consultados por faixa/registro quando necessário.

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

## Separação de responsabilidades atual

| Tipo de informação | Canônico atual |
|---|---|
| regra de arquitetura | GitHub |
| estado HOT | GitHub |
| página didática navegável | Notion |
| bancos operacionais já existentes | Notion, provisoriamente |
| arquivo/PDF/corpus pesado | Google Drive |
| conversa diária | ChatGPT, com persistência dos efeitos nas camadas acima |
| data plane analítico futuro | Google Sheets, somente após promotion gate |

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
- tratar a consulta avançada paga como indisponível para arquitetura;
- usar recursos gratuitos disponíveis quando suficientes;
- manter Notion como visualização e conteúdo humano;
- não migrar apenas porque uma consulta específica ficou indisponível;
- introduzir Sheets somente quando o promotion gate for satisfeito.

## Promotion gate para Google Sheets
1. congelar schema alvo no GitHub;
2. definir chave primária/IDs estáveis;
3. especificar fonte de verdade por entidade;
4. criar uma planilha SANDBOX pequena, nunca o corpus inteiro de saída;
5. migrar amostra de 20–30 registros;
6. testar leitura/escrita e contexto por range;
7. reconciliar linha a linha;
8. só então decidir se o ganho justifica produção;
9. se aprovado, migrar em lotes e recontar;
10. se não aprovado, descartar sandbox sem tocar no corpus atual.

Não criar uma segunda verdade silenciosa.

## Critério de sucesso
O usuário deve poder usar apenas o ChatGPT para estudar e, no máximo, abrir o Notion/Drive quando quiser visualizar material e estado.

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
