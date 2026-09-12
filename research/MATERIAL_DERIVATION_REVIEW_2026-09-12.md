# Dois recortes didáticos e uma geração verificável

Data: 12/09/2026. Estado: **BUILD / revisão no mesmo contexto / estudo bloqueado**.

O avanço desta passagem é concreto: as correções dos pilotos agora alimentam dois workbooks internos, com explicação, revisão, recuperação e aplicação. A produção foi conferida contra os dispositivos legais delimitados e recebeu testes de integridade. Isso não conclui Regime Geral ou RI inteiros, não constitui teste externo de suficiência e não cumpre automaticamente as Macro-rodadas 1, 2 ou 3.

## Entregas

| Recorte | Regras/grupos | Bases conceituais | Casos sintéticos | Relações |
|---|---:|---:|---:|---:|
| [Afastamento e intervenção](../material/working/RG_AFASTAMENTO_INTERVENCAO_V0.1.md) | 6 | 2 | 5 | 5 |
| [Exigência e dúvida registral](../material/working/RI_DUVIDA_V0.1.md) | 10 | 2 | 6 | 6 |
| Total | 16 | 4 | 11 | 11 |

Cada workbook contém MAP, MASTER, LEI SECA GUIADA, REVIEW, Q→A e EXAM/OUTPUT. Há 16 perguntas de recuperação, uma por regra/grupo. Esses números descrevem conteúdo editorial: não são 16 átomos estatisticamente independentes, 11 provas respondidas ou novos registros do Question Lab.

Fonte editorial: [pilot_recortes_v0.1.json](../data/material/pilot_recortes_v0.1.json). Gerador: [compile_material.py](../scripts/compile_material.py). As regras completas são redigidas uma vez na fonte; MASTER, REVIEW, respostas de recuperação e fundamentos dos casos usam esse mesmo campo. As explicações e aplicações também ficam nessa fonte, com suas referências explícitas.

Dentro deste recorte, a fonte estruturada e seu MASTER gerado constituem a versão de trabalho consolidada. Os ledgers continuam como índices. As bases congeladas e os patches históricos preservam a história dos erros e das correções, sem se tornarem versões concorrentes a editar. Fora dos recortes delimitados, o estado anterior dos pilotos continua valendo.

## Conferência jurídica realizada

Fontes primárias consultadas em 12/09: [Lei 8.935/1994 compilada](https://www.planalto.gov.br/ccivil_03/leis/l8935.htm) e [Lei 6.015/1973 compilada](https://www.planalto.gov.br/ccivil_03/leis/l6015compilada.htm). Leitura do texto vigente dos dispositivos indicados; não certificação de toda a legislação, de jurisprudência, do CNN ou da elegibilidade para um edital específico.

| Núcleo | Elementos conferidos e incorporados |
|---|---|
| Lei 8.935, arts. 32 III, 35 §1º, 36 caput | Finalidade e hipótese antes do prazo: pena, afastamento para apuração e hipótese ligada à perda da delegação. Art. 35 §1º usa decisão final; a comparação é textual e não resolve controvérsias concretas de duração. |
| Art. 36 §§1º–3º | Alternatividade dos critérios para intervenção; conveniência para os serviços; renda líquida; conta especial; correção monetária; destinatário do saldo em cada resultado. |
| Arts. 7º V e 11 III | Autenticação de cópias e recebimento de títulos protocolizados com quitação. A comparação não generaliza a impossibilidade de notas receber valores em outras operações. |
| LRP, art. 198 | Forma da nota e iniciativa; anotação, certificação, ciência, cópia e notificação; remessa após certificação do inciso III. A conclusão de que não se aguarda impugnação decorre da sequência dos incisos III–IV. |
| Arts. 199–202 | Sentença mesmo sem impugnação; condições dos prazos de MP e juízo; legitimados e efeitos da apelação previstos na LRP. Não foi inventado um prazo recursal a partir do art. 202. |
| Arts. 203–204 e 207 | Trânsito em julgado e providências documentais de cada saída; natureza administrativa; acesso contencioso; custas específicas da dúvida. |
| Art. 206-A II, §§1º–2º e 7º | Evento inicial do pagamento, conservação dos efeitos da prenotação no intervalo e exclusão desse período do prazo de registro. Não foi simulado calendário. |
| Arts. 188 §2º e 167 I 21 | Remissão às penas da Lei 8.935 sem perda automática; modalidade registral da citação na hipótese legal específica. |

Os prazos gerais do art. 188 aparecem como interface, com ressalva das exceções. A unidade não promete resolver todos os títulos, hipóteses especiais, calendários ou normas estaduais. Fonte atual não equivale a snapshot de prova: `CURRENT_LAW` permanece separado de `exam_snapshot: NOT_ASSESSED`.

## Conferência dos casos

Os 11 casos foram redigidos e revistos nesta mesma passagem. São exemplos de elaboração GX, sem cinco alternativas FGV e sem amostragem representativa da banca. A conferência abaixo examina a coerência entre hipótese, conclusão e fonte ensinada; não mede desempenho do candidato.

| Caso | Conclusão conferida | Discriminador |
|---|---|---|
| GX-RG-01 | Sim | Prorrogação prevista, sem automatismo |
| GX-RG-02 | Sim | Segundo critério alternativo para intervenção |
| GX-RG-03 | Não | Base líquida, depósito e destino final separados |
| GX-RG-04 | Não | Não universalizar prazo entre hipóteses distintas |
| GX-RG-05 | Não | Atribuições de notas e protesto invertidas |
| GX-RI-01 | Não | Impugnação não condiciona remessa |
| GX-RI-02 | Não | Silêncio não dispensa sentença |
| GX-RI-03 | Sim | Improcedência com trânsito e reapresentação documentada |
| GX-RI-04 | Não | Pagamento não consome prazo registral |
| GX-RI-05 | Não | Remissão sancionatória existe, sem automatismo |
| GX-RI-06 | Não | Procedência da dúvida e custas não se invertem |

Cada caso tem registro `SAME_CONTEXT_EDITORIAL` ligado por fingerprint ao enunciado, conclusão, justificativa, fundamentos, fontes e contexto do recorte. Mudar esses elementos exige nova conferência antes de regenerar. O registro demonstra qual versão foi revista; não transforma a revisão em independente e não detecta sozinho uma lei alterada no site oficial.

Esse mecanismo resolve uma limitação importante: copiar automaticamente o novo fundamento não garante que uma antiga conclusão continue correta. A geração passa a recusar a revisão editorial vencida. Não existe comando de aprovação em massa nem promoção automática de suficiência.

## Integridade e resultado dos testes

Comandos na raiz do repositório:

```bash
python3 -B scripts/compile_material.py
python3 -B scripts/compile_material.py --check
python3 -B -m unittest discover -s tests -v
python3 -B scripts/audit_checks.py
git diff --check
```

Resultado: **29 testes passaram**, sendo 16 anteriores e 13 do gerador. As duas derivações correspondem à fonte. Os cinco registros da auditoria anterior continuam consistentes e seus três documentos congelados preservam os hashes.

Os novos testes verificam propagação de uma correção; referência de caso a conteúdo efetivamente ensinado; fontes ausentes; links entre unidades; ciclos de pré-requisitos; colisões de IDs/arquivos; tentativa de promoção a S2; edição de caso ou fonte após revisão; detecção de derivação antiga sem reescrevê-la no modo `--check`; e confinamento dos arquivos gerados ao diretório de trabalho. Não provam a verdade jurídica das explicações nem sua eficácia pedagógica.

Uma relação entre unidades já funciona: `LRP-RI-PRAZO-SANCAO-016 requires RG-PEN-032III`. O nó de suspensão disciplinar conserva seu ID preexistente. Os detalhamentos da dúvida permanecem ligados ao agrupador 014; não multiplicam frequência empírica. As relações geradas ainda são locais ao GitHub, não uma migração de nós ou mastery para o Notion.

## Estado e continuidade

Nenhum corpus reservado foi aberto. Q20/Q22 do TJES Remoção e Q15 do Provimento continuam consumidas: demonstram lacunas anteriores, não novos acertos. Não houve recontagem dos 300 ENAC/304 registros, preenchimento da Passagem 2 integral, atualização do Contest History ou fechamento do CNN/Freshness nesta passagem.

O próximo trabalho deve usar estes arquivos como entrada verificável para a revisão externa prevista no roadmap e completar as evidências mínimas ainda pendentes dos pilotos, dentro da regra de contenção. Qualquer correção deve voltar à fonte editorial, passar pela revisão dos casos afetados e ser regenerada. Não reabrir arquitetura, não tratar os testes mecânicos como gate pedagógico cumprido e não iniciar aula sem o marco autoral previsto no projeto.
