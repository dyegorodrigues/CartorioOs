# GX Cartório OS — RI held-out validation H1/H2/H4

Data: 2026-09-12
Freeze testado: `3de8a57648f75303797b0caa24b33fbcd6d174de`
Status: **v0.1 FALHOU S2; patch necessário**

## Fontes oficiais
- IESES/TJPA 2026, cadernos 6015 Tipo 1 e 6104 Tipo 1 + gabaritos oficiais, publicados na página oficial do concurso.
- FGV/TJES 2025, caderno de Provimento Tipo 1 + gabarito oficial definitivo, publicados em `conhecimento.fgv.br/concursos/tjesnotarial25`.

## Integridade
Os recortes foram identificados e persistidos no registry antes da abertura. O specimen RI v0.1 foi congelado e commitado antes do consumo. Questões fora do recorte não foram usadas nesta validação.

## H1 — IESES/TJPA Provimento Q47–Q60
Todo o recorte trata de outras disciplinas. Resultado: `OUT_OF_SCOPE`.

## H2 — IESES/TJPA Remoção Q11–Q25
- Q12: incorporação imobiliária material;
- demais: RCPN, Notas, CNN e outros nós.

Nenhuma questão testa o núcleo procedimental congelado. Resultado: `OUT_OF_SCOPE`.

## H4 — FGV/TJES Provimento Q1–Q25

### Item in-scope: Q15
Microcaso: apresentação, ao RI, de citação em ação pessoal reipersecutória relativa a imóvel em loteamento urbano.

Operações exigidas:
1. reconhecer que o protocolo não equivale ao registro;
2. rejeitar prazo de 15 dias e aplicar o prazo-base do art. 188;
3. distinguir registro de averbação/RTD;
4. reconhecer a consequência da inobservância do art. 188 §2º, que remete às penas do art. 32 da Lei 8.935.

Gabarito definitivo Tipo 1: **E**.

### Cobertura do specimen v0.1
- `PASS`: protocolo ≠ registro;
- `PASS`: prazo-base de 10 dias ≠ 15 dias;
- `PARTIAL`: competência/saída registral foi ensinada como método, sem o átomo específico do título;
- `FAIL`: consequência disciplinar do art. 188 §2º não foi ensinada.

### Gap
`MATERIAL_GAP + STRUCTURE_GAP`.

O candidato conseguiria eliminar distratores, mas o material não permite afirmar a alternativa correta por conhecimento positivo e rastreável. Eliminação probabilística não satisfaz o gate.

### Descobertas cross-node não contadas
- Q18 toca gratuidade/tributos em regularização fundiária: alimentar Emolumentos/Reurb, não o score deste piloto;
- Q24 trata loteamento material: fora do núcleo congelado;
- Q8/Q11 tratam alienação fiduciária: nó material/procedimental futuro, não este tronco.

## Veredito
O specimen v0.1 **não atinge S2**. H1/H2 não fornecem evidência in-scope; H4 encontra uma questão in-scope e ela revela lacuna real. O patch deve ser estreito:
- explicitar art. 188 §2º e sua conexão disciplinar;
- criar boundary mínimo `título registrável/ato pretendido`, sem importar listas extensas para P1;
- retestar com pool independente, sem reutilizar Q15.

