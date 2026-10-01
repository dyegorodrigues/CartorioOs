# SOURCE REGISTRY v0.1 — Penal Intro Audit
**Checked through:** 2026-10-01
**Rule:** official source first; secondary banks for discovery/commentary only.

| Source | Type | Career / exam | Status | Use |
|---|---|---|---|---|
| https://conhecimento.fgv.br/concursos/pcpi25/1 | official contest page | PC-PI Delegado 2026 | VERIFIED_OFFICIAL | dates, files, provenance |
| https://conhecimento.fgv.br/sites/default/files/concursos/delegado-de-policia-cns100-tipo-1.pdf | official exam PDF | PC-PI Delegado 2026 | INGESTED_PARTIAL | Q42, Q71, Q72 alternative-level analysis |
| https://conhecimento.fgv.br/sites/default/files/concursos/pcpi-delegado-gabarito-definitivo.pdf | official key PDF | PC-PI Delegado 2026 | INGESTED_PARTIAL | definitive answers; metadata conflict flagged |
| https://cj.estrategia.com/portal/wp-content/uploads/2026/01/26141918/Prova-comentada-PC-PI.pdf | secondary expert commentary | PC-PI Delegado 2026 | VERIFIED_SECONDARY | adversarial commentary; appealability of Q72 |
| https://pc.rs.gov.br/concurso-publico-para-delegado-de-policia-2025 | official contest page | PC-RS Delegado 2025/2026 | VERIFIED_OFFICIAL | confirms contest phases, keys, oral cycle |
| https://www.pc.rs.gov.br/upload/arquivos/202510/13082837-edital-de-abertura-04-2025-admin-f.pdf | official edital | PC-RS Delegado | VERIFIED_OFFICIAL | discursive structure + scoring criteria |
| https://conhecimento.fgv.br/exames/enam/5exame | official exam page | ENAM 2026.1 | VERIFIED_OFFICIAL | current Magistratura core |
| https://www.qconcursos.com/ | secondary question bank | multiple | DISCOVERY_ONLY | locate items/comments; tags not semantic truth |
| https://www.tecconcursos.com.br/ | secondary question bank | multiple | DISCOVERY_ONLY | corpus discovery/incidence hints; requires semantic reclassification |
| https://questoes.grancursosonline.com.br/ | secondary question bank | multiple | DISCOVERY_ONLY | item discovery and cross-checking |

## Source-confidence policy
- OFFICIAL_CURRENT: official statute/tribunal/exam/gabarito.
- OFFICIAL_HISTORICAL: official but tied to historical legal state.
- SECONDARY_EXPERT: prep/commentary; useful for dissent and explanation, not authority.
- SECONDARY_BANK: question-bank reproduction; useful for discovery, not final provenance.
- LEGACY_PREP: supplied course PDFs/Notion; benchmark + preservation source, must be audited.

## Known source anomalies
1. PC-PI official contest page says objective exam 27/01/2026, while official definitive-key PDF header says 25/01/2025; Strategy says 25/01/2026.
2. Question-bank subject tags often place mixed questions under one label; semantic classification is rebuilt internally.
3. PCRS functions item is currently verified as a real item by multiple banks and the official contest exists; exact official question PDF still pending archive.