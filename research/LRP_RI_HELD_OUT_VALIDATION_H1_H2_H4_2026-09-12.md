# GX Cartório OS — RI held-out validation H1/H2/H4

Data: 2026-09-12
Freeze local originalmente indicado: `3de8a57648f75303797b0caa24b33fbcd6d174de`.
Status após auditoria de 12/09: **COBERTURA INSUFICIENTE DEMONSTRADA; S2 NÃO DEMONSTRADO**.

## Fontes oficiais
- IESES/TJPA 2026, cadernos 6015 Tipo 1 e 6104 Tipo 1 + gabaritos oficiais, publicados na página oficial do concurso.
- FGV/TJES 2025, caderno de Provimento Tipo 1 + gabarito oficial definitivo, publicados em `conhecimento.fgv.br/concursos/tjesnotarial25`.

## Integridade
O relato da execução registra reserva e freeze locais antes do consumo. Porém, no GitHub, esses eventos foram publicados juntos no commit `a502b45245d014ac080ed161a8653868026f7330`; o SHA local acima não constitui, sozinho, trilha remota sequencial verificável. Hashes dos documentos preservados estão no relatório de auditoria.

Não há resposta selada antes do gabarito com acesso restrito ao material demonstrada nesta passagem. A leitura de prova/gabarito sustenta **auditoria de cobertura**, não taxa de acerto nem teste cego. “Não usado” também não significa “não exposto”: retornos ampliados alcançaram itens vizinhos; o registry registra a quarentena. Nenhum desses recortes será reaproveitado como held-out limpo.

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
`MATERIAL_GAP` decisivo: art.188 §2º. O átomo do art.167 I 21 é complemento de discriminação útil; a auditoria retira a alegação de que esse segundo átomo fosse condição necessária para afirmar a alternativa E. Não converter toda ausência de explicação de distrator em novo gap estrutural obrigatório.

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
