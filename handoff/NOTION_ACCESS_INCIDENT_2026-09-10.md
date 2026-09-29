# GX Cartório OS — Incidente de acesso ao Notion — 2026-09-10

## Estado verificado
O conector Notion disponível ao ChatGPT está autenticado em:
- workspace: `Dyego Fentanes's Notion`
- workspace id: `8a3003d8-9b76-4d96-9dd9-4a865e3774ea`
- usuário proprietário/conectado: `Dyego Fentanes`
- e-mail: `fentanespcsc@gmail.com`
- user id: `21574a29-6bc6-4324-adac-e2fa95c216d1`

A busca atual de usuários do workspace não encontrou `dyegorfbarros@gmail.com` nem outro usuário chamado Diego. Portanto links criados nesse workspace podem retornar solicitação de convite quando abertos no app Notion autenticado em outra conta.

## Página afetada
- título: `SPECIMEN A v0.2 — PEN 1 · Aplicação da Lei Penal — INSPEÇÃO`
- page id: `3d742424-cdbc-817f-9f1d-da75b8a8f08d`
- URL: `https://app.notion.com/p/3d742424cdbc817f9f1dda75b8a8f08d?pvs=204`
- parent: `GX Cartório — Material Mestre`
- estado: existente e legível pelo conector; NÃO sumiu.

## Regra operacional de prevenção
1. Não apagar nem recriar a página por causa do erro de permissão.
2. Até decisão explícita de migração, considerar `Dyego Fentanes's Notion / fentanespcsc@gmail.com` como workspace Notion canônico do GX acessível ao conector.
3. Antes de criar novo material learner-facing, verificar a identidade do workspace com `Notion.fetch(self)`.
4. Se o usuário quiser usar outra conta como principal, primeiro resolver compartilhamento/migração na raiz `GX Cartório OS — Command Center` ou reconectar o Notion no ChatGPT à conta/workspace desejados; não espalhar cópias independentes.
5. GitHub permanece Source of Truth para arquitetura, handoffs e incidentes de acesso.

## Limitação da integração
As ferramentas Notion disponíveis nesta sessão permitem ler/criar/editar/mover páginas e consultar usuários, mas não expõem uma ação de convite/compartilhamento de membro. Portanto não é possível, via ChatGPT nesta sessão, adicionar `dyegorfbarros@gmail.com` ao workspace ou alterar as permissões de compartilhamento da página.
