# GX Cartório OS — Free Tooling Stack

Atualizado em 09/09/2026.

## Regra de produto
O GX deve funcionar sem exigir assinatura adicional do usuário.

Nenhuma função pedagógica central pode depender de recurso pago do Notion, Airtable, Anki, banco de dados comercial ou serviço premium externo.

## Decisão arquitetural atual
**Não migrar o data plane de produção agora.**

O risco principal não é capacidade de armazenamento ou contexto do modelo. É criar duas fontes de verdade, duplicar registros e introduzir drift antes de o tutor mínimo começar a produzir dados reais do candidato.

## Stack canônica gratuita atual

### 1. GitHub — Source of Truth versionado
Função:
- STATUS/ponteiro HOT;
- arquitetura e protocolos;
- matriz canônica;
- schemas;
- pesquisas/meta-análises;
- regras de QA/freshness;
- snapshots textuais que precisam de diff/auditoria.

O repositório `dyegorodrigues/CartorioOs` está **público** em 09/09/2026.

### 2. Notion Free — Human Knowledge Portal + estado operacional provisório
Função:
- Command Center;
- Discipline/Theme Maps;
- Material Mestre;
- bancos operacionais já construídos;
- navegação humana.

#### Limite real observado
A consulta SQL avançada da integração é limitada em planos que não possuem a capacidade paga correspondente. Isso **não significa que toda leitura estruturada do Notion deixou de funcionar**.

A integração atual também oferece:
- `rows` mode, para até 100 linhas por consulta com filtros;
- `view` mode, que usa views e não tem a mesma cota específica de SQL.

Portanto:
- nenhuma função central depende de SQL pago;
- usar rows/views para leituras delimitadas quando suficiente;
- Notion continua operacional enquanto a escala real permitir;
- não assinar plano pago como requisito do GX.

### 3. Google Drive — corpus e arquivos pesados
Função:
- provas oficiais/PDFs;
- espelhos;
- materiais adquiridos ou legalmente disponíveis;
- imagens, mapas e diagramas;
- exports e artefatos grandes.

Preservar URL, autoridade, edição/data e freshness.

### 4. Google Sheets — Candidate Operational Data Plane, não promovido
Pode ser excelente para:
- tentativas em grande volume;
- review queue;
- mastery/retention;
- analytics e dashboards;
- queries por ranges.

A integração está conectada. Se adotado, o tutor **nunca carrega a planilha inteira**: lê somente ranges/registros necessários à sessão.

Sheets só entra após promotion gate e quando resolver dor real observada.

## SQLite / JSONL
### SQLite
SQLite é tecnicamente excelente dentro de um aplicativo/local runtime, mas **não é o data plane imediato do GX nesta integração**.

Razões:
- arquivo `.sqlite` é binário e produz diffs pobres no Git;
- o conector GitHub atual versiona conteúdo de arquivo, mas não executa transações SQL persistentes contra um banco hospedado no repositório;
- regravar binário a cada sessão criaria fricção e risco de conflito;
- portanto o ganho teórico de transação não está disponível no runtime atual.

Reavaliar SQLite apenas quando houver aplicação própria/runtime local ou cloud que opere o banco diretamente.

### JSONL/CSV
São boas opções para:
- exports auditáveis;
- snapshots de tentativas;
- datasets de pesquisa;
- interchange entre ferramentas.

Mas atualizar um arquivo Git grande a cada microtentativa também pode ser ineficiente. Usar quando houver contrato claro, não como religião de stack.

## O que não adotar como núcleo agora
### Airtable Free
Pequeno demais para o volume previsto e adiciona fornecedor sem vantagem decisiva.

### Obsidian
Bom produto, mas outra interface sem ganho suficiente no workflow atual.

### Supabase/Postgres
Excelente candidato caso o GX vire aplicação própria. Overengineering agora.

### Anki como dependência
Não obrigatório. Exportação futura é permitida, mas o candidato não administra decks para o sistema funcionar.

## Separação de responsabilidades atual
| Tipo de informação | Canônico atual |
|---|---|
| arquitetura / regra / estado HOT | GitHub |
| páginas didáticas / mapas / portal | Notion |
| bancos atuais | Notion provisoriamente |
| PDFs / espelhos / assets | Google Drive |
| conversa diária | ChatGPT, persistindo efeitos |
| analytics/data plane futuro | decidir por promotion gate |

## Chat Is Not Memory
Ao final de uma sessão relevante, persistir o **efeito** da conversa:
- tentativas;
- mastery/retention;
- próxima revisão;
- erros relevantes;
- evidências discursivas/orais;
- decisões pedagógicas.

O candidato não deve administrar isso manualmente.

## Promotion gate para qualquer novo data plane
1. definir o problema que a ferramenta resolve;
2. congelar schema mínimo;
3. definir IDs/chaves;
4. definir source-of-truth por entidade;
5. criar sandbox pequeno;
6. testar leitura/escrita do runtime real;
7. reconciliar 20–30 registros linha a linha;
8. testar falha/retry/duplicata;
9. só promover se o ganho superar a dívida de migração;
10. manter rollback claro.

## Context budget rule
Independentemente da ferramenta, o tutor consulta somente:
- estado curricular necessário;
- itens vencidos;
- erros relevantes;
- poucas questões candidatas;
- fontes jurídicas do bloco;
- métricas agregadas suficientes para a decisão.

O data plane pode ter milhões de células/linhas sem ocupar a janela de conversa, desde que seja consultado seletivamente.

## Critério de sucesso
O usuário deve conseguir estudar apenas com o comando `Começar estudo` e, opcionalmente, abrir Notion/Drive para consulta visual. Ele não escolhe próxima matéria, não move linhas, não mantém flashcards e não recalcula revisão.
