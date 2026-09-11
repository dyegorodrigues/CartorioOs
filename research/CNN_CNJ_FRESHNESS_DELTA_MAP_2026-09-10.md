# GX Cartório OS — CNN/CNJ Freshness Delta Map

Snapshot: 2026-09-10
Status: infraestrutura do Freshness Firewall; NÃO é material de estudo.

## Fonte-base
- Provimento CNJ 149/2023 — Código Nacional de Normas do Foro Extrajudicial, texto compilado oficial.
- Resolução CNJ 696/2026 — regime atual dos concursos de outorga.

## Por que este mapa existe
O CNN/CNJ-Extra recebe alterações frequentes. Questões históricas continuam úteis como forma cognitiva, mas nenhuma proposição pode ser promovida ao MASTER atual sem revalidação contra o texto compilado e atos modificadores posteriores.

## Deltas relevantes observados em 2026

| Ato | Data | Tema | Impacto no Atlas |
|---|---|---|---|
| Prov. 217 | 09/03/2026 | adequação registral/indisponibilidade | revalidar nós de RI e ordens de indisponibilidade |
| Prov. 218 | 13/03/2026 | Justiça Aberta | afeta regime administrativo/dados de serventias |
| Prov. 219 | 20/03/2026 | gestão/publicidade da relação geral de vacâncias | afeta vacância/interinidade/concurso |
| Prov. 224 | 12/05/2026 | Constrijud / Serp-Jud / constrições imobiliárias | afeta RI, prenotação, qualificação, ordens judiciais |
| Prov. 225 | 20/05/2026 | publicidade de protestos / monitoramento de ordens | afeta Protesto e cumprimento de decisões |
| Prov. 227 | 09/06/2026 | solvência trabalhista dos delegatários | afeta deveres/fiscalização/regime da delegação |
| Prov. 228 | 16/06/2026 | extratos eletrônicos no RI | afeta títulos eletrônicos/registro/averbação |
| Prov. 229 | 16/06/2026 | SERP / interoperabilidade / Meu Registro | afeta arquitetura nacional dos registros eletrônicos |
| Prov. 237 | 13/07/2026 | CNS/acervo/certidões + reprodução assistida | afeta publicidade, acervo e RCPN |
| Prov. 242 | 21/07/2026 | base nacional RTDPJ / identificadores / governança de dados | afeta RTD/PJ e interoperabilidade |
| Prov. 253 | 18/08/2026 | certidões e consultas na CENPROT após sustação | afeta Protesto e publicidade atual do registro |

## Regra de versionamento por proposição
Toda proposição derivada de CNN/CNJ deve registrar:
1. artigo atual;
2. snapshot de consulta;
3. ato modificador conhecido;
4. tema/especialidade;
5. status `stable / volatile / recently_changed`;
6. data-gatilho para nova validação;
7. questões históricas que ficaram juridicamente incompatíveis ou parcialmente obsoletas.

## Regra de uso de questão antiga
Classificar em uma destas categorias:
- `VALID_CURRENT`: conteúdo e gabarito seguem atuais;
- `FORM_ONLY`: forma/distrator útil, regra material alterada;
- `PARTIAL`: parte da questão permanece válida;
- `RETIRED`: não usar pedagogicamente salvo para história normativa.

## Consequência para o GX
A contagem de incidência não basta. Toda frequência precisa carregar uma dimensão de validade temporal. Um item muito cobrado no passado pode ter baixo valor pedagógico atual se a norma mudou; um ato de 2026 com pouca frequência histórica pode ter alta prioridade por centralidade e recência.

## Próxima expansão
1. mapear artigos do CNN/CNJ alterados por cada provimento de 2026;
2. ligar cada artigo aos nós do Curriculum Graph;
3. cruzar com ENAC 2025.1/2025.2/2026.1 e concursos estaduais;
4. sinalizar questões que exigem re-gabarito ou aposentadoria;
5. incorporar o status temporal ao Depth Budget.