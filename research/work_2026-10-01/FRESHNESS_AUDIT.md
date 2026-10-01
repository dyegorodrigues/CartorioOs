# Duas passagens de frescor — 01/10/2026

Janela principal: provas/fases aplicadas entre01/01/2023 e01/10/2026. Varredura recente conservadora:02/08/2026–01/10/2026, limitada aos documentos disponíveis no horário da coleta. Data de publicação, aplicação, edital e resultado são campos diferentes.

## Passagem1 — descoberta

Busca multicarreira2026, recuo2025/2024/2023 e leitura das páginas oficiais FGV. Foram capturadas a listagem principal e13 páginas subsequentes; de80 páginas candidatas, o lote priorizou as atuais e as necessárias à reserva/contraprova. Também foram consultados índices FCC, Cebraspe e instituições. Consultas e retornos estão em `discovery/search_round_*` e `discovery/search_backfill_*`.

## Passagem2 — adversarial

A pergunta mudou de “o que encontro sobre o piloto?” para “quais carreiras, bancas, fases e provas recentes estão faltando?”. Buscas com recência de60 dias e consultas específicas a provas, discursivas, orais e cronogramas foram confrontadas com catálogos oficiais. Foram inspecionados também os arquivos públicos da API Cebraspe, descoberta no JavaScript público da própria página, sem sessão de candidato.

Registros: `discovery/adversarial_freshness_1.json`, `adversarial_freshness_2.json`, `universe_gaps_*.json`; `CEBRASPE_API_INDEX` e páginas detalhadas nos snapshots. O catálogo apresenta **223 publicações** na janela recente: publicações não equivalem a223 provas novas.

| Contraprova | Resultado |
|---|---|
| PGE-AL2026 | Objetiva aplicada05/09; caderno e preliminar publicados25/09; escritas de06/09 com padrões públicos. Faltava no universo legado. |
| PGE-RN2026 | Objetiva de21/06 e padrão escrito definitivo publicado01/09. Faltava no universo legado. |
| PGM Porto Velho2026 | Objetiva21/06, escritas26/07 e padrões definitivos deagosto. Faltava no universo legado. |
| PCDF | Edital11 de30/09 altera estado conhecido: oral futura10–11/10; não é questão oral já aplicada. |
| TJPE | Caderno fresco publicado29/09 contém questões relevantes mesmo sem os rótulos usados na triagem anterior. |
| MPES25promotor | Atos de oral/setembro localizados; sorteio de ponto não comprova texto da pergunta feita. |
| DPE-MA e DPE-BA | Fases avançadas2026 e divulgação viaFCC; ponte pública leva ao Portal do Candidato em parte dos arquivos. Não presumir que arquivo restrito esteja disponível. |
| MPMS e MPSC | Fontes institucionais2026, com caderno/chave MPMS e padrão escrito MPSC. MPSC45 usa Vunesp na organização; não classificar tudo como FGV. |
| PF | Oral real sub judice de19/07/2026 localizada no ciclo2025 e decomposta. Demonstra por que filtrar apenas “edital2026” perderia prova atual. |
| MPF31 | Objetiva2025 e oral2026 identificadas na fonte institucional; caderno objetivo adquirido. Não declarar revisão semântica integral ainda. |

## Resultado da segunda passagem

**Executada, mas sem saturação demonstrada.** Surgiram novas provas relevantes; portanto ela refuta a suficiência do inventário anterior e não autoriza fechar o universo. Há candidatos secundários ainda sem validação oficial completa, por exemplo PGM Foz do Iguaçu, Câmara de Joinville, PGE-RJ19 e concursos próprios estaduais. Isso está em fila, não foi convertido em evidência de conteúdo.

Notícias de nomeação, prorrogação de validade, pessoal de apoio e concursos futuros foram separadas de provas novas. Fontes com anos conflitantes, páginas dinâmicas e indisponibilidade permanecem lacunas explícitas. O gráfico de cobertura não usa ausência de resultado de busca como “não houve concurso”.
