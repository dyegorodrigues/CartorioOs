# Registro de Imóveis — da exigência ao desfecho da dúvida

**BUILD / NÃO VALIDADO / NÃO INICIAR ESTUDO.**

Conferência legal delimitada: 2026-09-12. CURRENT_LAW; elegibilidade para edital específico não avaliada.

Gerado por `scripts/compile_material.py` a partir de `data/material/pilot_recortes_v0.1.json`. Edite a fonte editorial e regenere; não edite esta derivação.

Fingerprint semântico da fonte: `1ac3739af6600f3c96dc58d9e6465f999a85475062cb31d714e77418128acb94`.

**Proveniência:** Consolida correções dos patches RI v0.2 e v0.3. TJES/FGV 2025 Provimento Tipo 1 Q15 foi consumida e revelou a lacuna do art. 188 §2º. Arts. 200–204 e 207 foram detalhados pela leitura da lei. Nenhuma dessas ampliações representa um novo acerto em prova independente.

**Limites:** Não certifica dúvida inversa, procedimentos de averbação, normas estaduais, recursos em situações especiais, cômputo de datas concretas, retificação, usucapião, indisponibilidade ou jurisprudência. CNN/CNJ integral permanece pendente. Os prazos são apresentados com seu evento e destinatário, sem simular calendário.

## 1. MAP

Procedimento legal da dúvida a partir da exigência: iniciativa, atos do registrador, impugnação, decisão, recurso e cumprimento. Interfaces pontuais com pagamento, sanções por prazos e citação registrável. Não substitui o módulo completo de RI.

P0 = pré-requisito; P1 = cobertura; P2 = discriminativo; P3 = produção avançada; P4 = referência. Os itens deste recorte estão em P1, sem score de frequência inventado.

| Conhecimento | Relação | Conexão útil |
|---|---|---|
| [Exigência escrita e iniciativa do interessado](RI_DUVIDA_V0.1.md#lrp-ri-nota-018) | requer | [Título, qualificação e exigência](RI_DUVIDA_V0.1.md#ri-base-titulo) |
| [Atos do registrador e momento da remessa](RI_DUVIDA_V0.1.md#lrp-ri-duvida-014) | requer | [Exigência escrita e iniciativa do interessado](RI_DUVIDA_V0.1.md#lrp-ri-nota-018) |
| [Procedente e improcedente: consequências](RI_DUVIDA_V0.1.md#lrp-ri-duvida-014-saida) | requer | [Prenotação e decisão final](RI_DUVIDA_V0.1.md#ri-base-protocolo) |
| [Procedente e improcedente: consequências](RI_DUVIDA_V0.1.md#lrp-ri-duvida-014-saida) | requer | [Falta de impugnação](RI_DUVIDA_V0.1.md#lrp-ri-duvida-014-silencio) |
| [Recurso previsto na LRP](RI_DUVIDA_V0.1.md#lrp-ri-duvida-014-recurso) | comparar para não confundir | [Natureza da decisão e custas da dúvida](RI_DUVIDA_V0.1.md#lrp-ri-duvida-014-natureza) |
| [Sanções por descumprimento do prazo](RI_DUVIDA_V0.1.md#lrp-ri-prazo-sancao-016) | requer | [Suspensão como pena](RG_AFASTAMENTO_INTERVENCAO_V0.1.md#rg-pen-032iii) |

## 2. MASTER

### Base necessária

<a id="ri-base-titulo"></a>

#### Título, qualificação e exigência

Título é o documento apresentado para a prática do ato. Qualificar é examinar sua aptidão jurídica para ingressar no registro. Se existir exigência a satisfazer, o apresentante precisa compreender o obstáculo e decidir sua resposta. A dúvida tratada aqui é o procedimento legal para levar ao juízo a exigência com a qual o interessado não concorda ou que não consegue cumprir.

<a id="ri-base-protocolo"></a>

#### Prenotação e decisão final

A prenotação corresponde ao ingresso do título no Protocolo e não se confunde com o registro pretendido. Neste recorte, acompanhe o que a lei manda anotar ou cancelar no Protocolo. Trânsito em julgado indica que a decisão já não está sujeita a recurso; o art. 203 usa esse marco para as providências finais.

<a id="lrp-ri-nota-018"></a>

### Exigência escrita e iniciativa do interessado

`LRP-RI-NOTA-018` · P1

A exigência deve ser indicada por escrito, de uma só vez, de forma articulada, clara e objetiva, com data, identificação e assinatura do oficial ou preposto responsável, no prazo do art. 188. O interessado pode cumpri-la ou requerer a remessa do título e da dúvida ao juízo se não concordar ou não puder satisfazê-la.

O obstáculo precisa ser comunicável e identificável, não apenas uma recusa oral vaga. A iniciativa prevista no art. 198 VI depende do requerimento do interessado na hipótese descrita. O prazo geral do art. 188 é de 10 dias a partir do protocolo para registrar ou emitir nota, com as exceções que o próprio dispositivo indica. Não use esse número isoladamente para todos os títulos.

[LRP](https://www.planalto.gov.br/ccivil_03/leis/l6015compilada.htm) — Art. 198, caput e V–VI; art. 188, caput.

<a id="lrp-ri-duvida-014"></a>

### Atos do registrador e momento da remessa

`LRP-RI-DUVIDA-014` · P1

Anotada a dúvida no Protocolo e certificadas a prenotação e a suscitação no título, com rubrica das folhas, o oficial dá ciência dos termos ao apresentante, fornece cópia e o notifica para impugnar perante o juízo em 15 dias. Certificado o cumprimento da ciência e notificação, remete eletronicamente título e razões ao juízo. A remessa não aguarda a impugnação nem o término desses 15 dias.

O evento que autoriza a remessa é a certificação da providência do inciso III. A lei não manda aguardar uma impugnação nem esgotar seus 15 dias antes de remeter. Separe as trilhas: o oficial certifica e remete; o apresentante, se impugnar, dirige sua resposta ao juízo. A versão antiga do fluxo invertia essa relação e criava uma espera indevida.

[LRP](https://www.planalto.gov.br/ccivil_03/leis/l6015compilada.htm) — Art. 198, §1º, I–IV.

<a id="lrp-ri-duvida-014-silencio"></a>

### Falta de impugnação

`LRP-RI-DUVIDA-014-SILENCIO` · P1

Mesmo sem impugnação no prazo legal, a dúvida será julgada por sentença.

O silêncio não substitui o julgamento. Uma alternativa que mande cancelar automaticamente a prenotação porque o interessado não impugnou acrescenta um efeito que o art. 199 não estabelece. Ainda é necessário obter a decisão e identificar seu resultado antes de aplicar as saídas do art. 203.

[LRP](https://www.planalto.gov.br/ccivil_03/leis/l6015compilada.htm) — Art. 199.

<a id="lrp-ri-duvida-014-juizo"></a>

### Ministério Público e decisão

`LRP-RI-DUVIDA-014-JUIZO` · P1

Impugnada a dúvida com os documentos apresentados pelo interessado, o Ministério Público será ouvido em 10 dias. Se não forem requeridas diligências, o juiz decidirá em 15 dias, com base nos elementos dos autos.

Há destinatários e condições diferentes: 10 dias dizem respeito à manifestação do Ministério Público na hipótese do art. 200; 15 dias, à decisão na hipótese do art. 201. Não some esses números com os 15 dias de impugnação para fabricar um prazo total invariável. Os dispositivos descrevem etapas e condições, não um calendário único para qualquer caso.

[LRP](https://www.planalto.gov.br/ccivil_03/leis/l6015compilada.htm) — Arts. 200–201.

<a id="lrp-ri-duvida-014-recurso"></a>

### Recurso previsto na LRP

`LRP-RI-DUVIDA-014-RECURSO` · P1

Da sentença podem apelar o interessado, o Ministério Público e o terceiro prejudicado, com efeitos devolutivo e suspensivo.

Recupere juntos os três legitimados enumerados e os dois efeitos. O recorte reproduz o elenco legal: não decide situações especiais de legitimidade por jurisprudência. O art. 202 também não fornece, em seu texto, um número de dias para apelar; esse prazo exigiria uma análise processual adicional, que não foi incluída nesta unidade.

[LRP](https://www.planalto.gov.br/ccivil_03/leis/l6015compilada.htm) — Art. 202.

<a id="lrp-ri-duvida-014-saida"></a>

### Procedente e improcedente: consequências

`LRP-RI-DUVIDA-014-SAIDA` · P1

Depois do trânsito em julgado, a dúvida procedente leva à restituição dos documentos à parte, independentemente de traslado, e à ciência ao oficial para anotar a decisão no Protocolo e cancelar a prenotação. Na improcedente, o interessado reapresenta os documentos com mandado ou certidão da sentença, que ficam arquivados; o registro é feito desde logo, com anotação do fato no Protocolo.

Procedente qualifica a dúvida, não o desejo do apresentante de registrar. Por isso, a saída é cancelamento da prenotação. Improcedente conduz ao registro, mas o cumprimento legal envolve trânsito em julgado e reapresentação acompanhada do documento judicial. Não transforme a simples notícia de uma sentença favorável ao interessado em ordem automática para registrar sem esses passos.

[LRP](https://www.planalto.gov.br/ccivil_03/leis/l6015compilada.htm) — Art. 203, caput e I–II.

<a id="lrp-ri-duvida-014-natureza"></a>

### Natureza da decisão e custas da dúvida

`LRP-RI-DUVIDA-014-NATUREZA` · P1

A decisão da dúvida tem natureza administrativa e não impede o processo contencioso competente. No processo de dúvida, o interessado paga custas somente quando a dúvida for julgada procedente.

O fato de o juízo decidir não altera a natureza que a LRP atribui ao procedimento. A regra de custas é específica da dúvida: ela não significa gratuidade universal dos atos registrais nem elimina emolumentos de operações distintas. Mantenha separados o efeito da decisão e o custo do procedimento.

[LRP](https://www.planalto.gov.br/ccivil_03/leis/l6015compilada.htm) — Arts. 204 e 207.

<a id="lrp-ri-pagamento-015"></a>

### Pagamento e prazo de registro

`LRP-RI-PAGAMENTO-015` · P1

Na opção de pagar inicialmente a prenotação, o restante é depositado em 5 dias da análise que conclua pela aptidão do título; os efeitos da prenotação são mantidos nesse período. O intervalo de pagamento do art. 206-A não integra o prazo de registro do art. 188; após o depósito, seguem os procedimentos de registro e expedição da certidão.

São relógios com objetos diferentes. Um deles permite ao usuário completar o pagamento após a análise de aptidão; outro rege a atuação registral. O §7º impede consumir o prazo de registro com aquele intervalo de pagamento. Esta unidade não calcula uma data final nem generaliza a manutenção da prenotação para hipóteses de inadimplemento, reingresso ou procedimentos especiais.

[LRP](https://www.planalto.gov.br/ccivil_03/leis/l6015compilada.htm) — Art. 206-A, caput, II, §§1º–2º e 7º.

<a id="lrp-ri-prazo-sancao-016"></a>

### Sanções por descumprimento do prazo

`LRP-RI-PRAZO-SANCAO-016` · P1

A inobservância do art. 188 enseja a aplicação das penas do art. 32 da Lei 8.935, nos termos estabelecidos pela Corregedoria Nacional de Justiça. O elenco inclui repreensão, multa, suspensão e perda da delegação, assegurado amplo direito de defesa. A remissão ao elenco não impõe automaticamente a perda da delegação por qualquer atraso.

O §2º usa ensejará, não poderá: não apresenta a submissão ao regime sancionatório como mera opção. Outra pergunta é qual pena poderá resultar da apuração. A perda está no elenco, mas a remissão não a escolhe automaticamente nem elimina a defesa. Na Q15/TJES, a possibilidade mencionada na alternativa E diz respeito à perda da delegação. A explicação anterior confundia essa formulação da questão com o verbo do dispositivo legal.

[LRP](https://www.planalto.gov.br/ccivil_03/leis/l6015compilada.htm); [L8935](https://www.planalto.gov.br/ccivil_03/leis/l8935.htm) — LRP, art. 188 §2º; Lei 8.935, art. 32.

<a id="lrp-ri-citacao-017"></a>

### Interface: citação sujeita a registro

`LRP-RI-CITACAO-017` · P1

A citação de ação real ou pessoal reipersecutória relativa a imóvel está prevista entre os atos de registro do art. 167, I, 21.

O ponto de discriminação aqui é registro, na hipótese específica descrita. Não transforme a regra em afirmação sobre toda citação judicial nem confunda a citação com outros atos processuais que possam ter ingresso registral próprio. Esta interface ajuda a ler os distratores da Q15 já consumida; não foi necessária como uma segunda premissa para reconhecer a alternativa sobre sanções.

[LRP](https://www.planalto.gov.br/ccivil_03/leis/l6015compilada.htm) — Art. 167, I, 21.

## 3. LEI SECA GUIADA

A síntese é autoral. Abra o texto oficial e localize os elementos pedidos; este roteiro não substitui a redação legal.

**Exigência escrita e iniciativa do interessado** — [LRP](https://www.planalto.gov.br/ccivil_03/leis/l6015compilada.htm) — Art. 198, caput e V–VI; art. 188, caput.

Foco da leitura: Como a exigência deve ser comunicada e o que o interessado pode requerer se discordar ou não conseguir cumpri-la?

**Atos do registrador e momento da remessa** — [LRP](https://www.planalto.gov.br/ccivil_03/leis/l6015compilada.htm) — Art. 198, §1º, I–IV.

Foco da leitura: Qual sequência cabe ao oficial e é necessário esperar a impugnação ou seus 15 dias para remeter?

**Falta de impugnação** — [LRP](https://www.planalto.gov.br/ccivil_03/leis/l6015compilada.htm) — Art. 199.

Foco da leitura: A falta de impugnação dispensa a sentença?

**Ministério Público e decisão** — [LRP](https://www.planalto.gov.br/ccivil_03/leis/l6015compilada.htm) — Arts. 200–201.

Foco da leitura: A que atos e condições se ligam os prazos dos arts. 200 e 201?

**Recurso previsto na LRP** — [LRP](https://www.planalto.gov.br/ccivil_03/leis/l6015compilada.htm) — Art. 202.

Foco da leitura: Quem o art. 202 enumera para apelar e com quais efeitos?

**Procedente e improcedente: consequências** — [LRP](https://www.planalto.gov.br/ccivil_03/leis/l6015compilada.htm) — Art. 203, caput e I–II.

Foco da leitura: Após qual marco se cumprem as duas saídas e quais documentos e providências cada uma exige?

**Natureza da decisão e custas da dúvida** — [LRP](https://www.planalto.gov.br/ccivil_03/leis/l6015compilada.htm) — Arts. 204 e 207.

Foco da leitura: Qual é a natureza da decisão, o que ela não impede e quando há custas para o interessado na dúvida?

**Pagamento e prazo de registro** — [LRP](https://www.planalto.gov.br/ccivil_03/leis/l6015compilada.htm) — Art. 206-A, caput, II, §§1º–2º e 7º.

Foco da leitura: Na opção do art. 206-A II, quando se paga o restante e esse intervalo consome o prazo do art. 188?

**Sanções por descumprimento do prazo** — [LRP](https://www.planalto.gov.br/ccivil_03/leis/l6015compilada.htm); [L8935](https://www.planalto.gov.br/ccivil_03/leis/l8935.htm) — LRP, art. 188 §2º; Lei 8.935, art. 32.

Foco da leitura: Para qual elenco de penas remete o art. 188 §2º e isso significa perda automática?

**Interface: citação sujeita a registro** — [LRP](https://www.planalto.gov.br/ccivil_03/leis/l6015compilada.htm) — Art. 167, I, 21.

Foco da leitura: No art. 167 I 21, qual citação está prevista e a modalidade é registro ou averbação?

## 4. REVIEW

Versão compacta: somente as regras canônicas, sem as explicações e os exemplos do MASTER.

**Exigência escrita e iniciativa do interessado** (`LRP-RI-NOTA-018`): A exigência deve ser indicada por escrito, de uma só vez, de forma articulada, clara e objetiva, com data, identificação e assinatura do oficial ou preposto responsável, no prazo do art. 188. O interessado pode cumpri-la ou requerer a remessa do título e da dúvida ao juízo se não concordar ou não puder satisfazê-la. [LRP](https://www.planalto.gov.br/ccivil_03/leis/l6015compilada.htm) — Art. 198, caput e V–VI; art. 188, caput.

**Atos do registrador e momento da remessa** (`LRP-RI-DUVIDA-014`): Anotada a dúvida no Protocolo e certificadas a prenotação e a suscitação no título, com rubrica das folhas, o oficial dá ciência dos termos ao apresentante, fornece cópia e o notifica para impugnar perante o juízo em 15 dias. Certificado o cumprimento da ciência e notificação, remete eletronicamente título e razões ao juízo. A remessa não aguarda a impugnação nem o término desses 15 dias. [LRP](https://www.planalto.gov.br/ccivil_03/leis/l6015compilada.htm) — Art. 198, §1º, I–IV.

**Falta de impugnação** (`LRP-RI-DUVIDA-014-SILENCIO`): Mesmo sem impugnação no prazo legal, a dúvida será julgada por sentença. [LRP](https://www.planalto.gov.br/ccivil_03/leis/l6015compilada.htm) — Art. 199.

**Ministério Público e decisão** (`LRP-RI-DUVIDA-014-JUIZO`): Impugnada a dúvida com os documentos apresentados pelo interessado, o Ministério Público será ouvido em 10 dias. Se não forem requeridas diligências, o juiz decidirá em 15 dias, com base nos elementos dos autos. [LRP](https://www.planalto.gov.br/ccivil_03/leis/l6015compilada.htm) — Arts. 200–201.

**Recurso previsto na LRP** (`LRP-RI-DUVIDA-014-RECURSO`): Da sentença podem apelar o interessado, o Ministério Público e o terceiro prejudicado, com efeitos devolutivo e suspensivo. [LRP](https://www.planalto.gov.br/ccivil_03/leis/l6015compilada.htm) — Art. 202.

**Procedente e improcedente: consequências** (`LRP-RI-DUVIDA-014-SAIDA`): Depois do trânsito em julgado, a dúvida procedente leva à restituição dos documentos à parte, independentemente de traslado, e à ciência ao oficial para anotar a decisão no Protocolo e cancelar a prenotação. Na improcedente, o interessado reapresenta os documentos com mandado ou certidão da sentença, que ficam arquivados; o registro é feito desde logo, com anotação do fato no Protocolo. [LRP](https://www.planalto.gov.br/ccivil_03/leis/l6015compilada.htm) — Art. 203, caput e I–II.

**Natureza da decisão e custas da dúvida** (`LRP-RI-DUVIDA-014-NATUREZA`): A decisão da dúvida tem natureza administrativa e não impede o processo contencioso competente. No processo de dúvida, o interessado paga custas somente quando a dúvida for julgada procedente. [LRP](https://www.planalto.gov.br/ccivil_03/leis/l6015compilada.htm) — Arts. 204 e 207.

**Pagamento e prazo de registro** (`LRP-RI-PAGAMENTO-015`): Na opção de pagar inicialmente a prenotação, o restante é depositado em 5 dias da análise que conclua pela aptidão do título; os efeitos da prenotação são mantidos nesse período. O intervalo de pagamento do art. 206-A não integra o prazo de registro do art. 188; após o depósito, seguem os procedimentos de registro e expedição da certidão. [LRP](https://www.planalto.gov.br/ccivil_03/leis/l6015compilada.htm) — Art. 206-A, caput, II, §§1º–2º e 7º.

**Sanções por descumprimento do prazo** (`LRP-RI-PRAZO-SANCAO-016`): A inobservância do art. 188 enseja a aplicação das penas do art. 32 da Lei 8.935, nos termos estabelecidos pela Corregedoria Nacional de Justiça. O elenco inclui repreensão, multa, suspensão e perda da delegação, assegurado amplo direito de defesa. A remissão ao elenco não impõe automaticamente a perda da delegação por qualquer atraso. [LRP](https://www.planalto.gov.br/ccivil_03/leis/l6015compilada.htm); [L8935](https://www.planalto.gov.br/ccivil_03/leis/l8935.htm) — LRP, art. 188 §2º; Lei 8.935, art. 32.

**Interface: citação sujeita a registro** (`LRP-RI-CITACAO-017`): A citação de ação real ou pessoal reipersecutória relativa a imóvel está prevista entre os atos de registro do art. 167, I, 21. [LRP](https://www.planalto.gov.br/ccivil_03/leis/l6015compilada.htm) — Art. 167, I, 21.

## 5. Q→A

Perguntas de recuperação para revisar o material internamente. As respostas abaixo são geradas das mesmas regras do MASTER.

### Como a exigência deve ser comunicada e o que o interessado pode requerer se discordar ou não conseguir cumpri-la?

A exigência deve ser indicada por escrito, de uma só vez, de forma articulada, clara e objetiva, com data, identificação e assinatura do oficial ou preposto responsável, no prazo do art. 188. O interessado pode cumpri-la ou requerer a remessa do título e da dúvida ao juízo se não concordar ou não puder satisfazê-la. [LRP](https://www.planalto.gov.br/ccivil_03/leis/l6015compilada.htm) — Art. 198, caput e V–VI; art. 188, caput.

Referência: `LRP-RI-NOTA-018`.

### Qual sequência cabe ao oficial e é necessário esperar a impugnação ou seus 15 dias para remeter?

Anotada a dúvida no Protocolo e certificadas a prenotação e a suscitação no título, com rubrica das folhas, o oficial dá ciência dos termos ao apresentante, fornece cópia e o notifica para impugnar perante o juízo em 15 dias. Certificado o cumprimento da ciência e notificação, remete eletronicamente título e razões ao juízo. A remessa não aguarda a impugnação nem o término desses 15 dias. [LRP](https://www.planalto.gov.br/ccivil_03/leis/l6015compilada.htm) — Art. 198, §1º, I–IV.

Referência: `LRP-RI-DUVIDA-014`.

### A falta de impugnação dispensa a sentença?

Mesmo sem impugnação no prazo legal, a dúvida será julgada por sentença. [LRP](https://www.planalto.gov.br/ccivil_03/leis/l6015compilada.htm) — Art. 199.

Referência: `LRP-RI-DUVIDA-014-SILENCIO`.

### A que atos e condições se ligam os prazos dos arts. 200 e 201?

Impugnada a dúvida com os documentos apresentados pelo interessado, o Ministério Público será ouvido em 10 dias. Se não forem requeridas diligências, o juiz decidirá em 15 dias, com base nos elementos dos autos. [LRP](https://www.planalto.gov.br/ccivil_03/leis/l6015compilada.htm) — Arts. 200–201.

Referência: `LRP-RI-DUVIDA-014-JUIZO`.

### Quem o art. 202 enumera para apelar e com quais efeitos?

Da sentença podem apelar o interessado, o Ministério Público e o terceiro prejudicado, com efeitos devolutivo e suspensivo. [LRP](https://www.planalto.gov.br/ccivil_03/leis/l6015compilada.htm) — Art. 202.

Referência: `LRP-RI-DUVIDA-014-RECURSO`.

### Após qual marco se cumprem as duas saídas e quais documentos e providências cada uma exige?

Depois do trânsito em julgado, a dúvida procedente leva à restituição dos documentos à parte, independentemente de traslado, e à ciência ao oficial para anotar a decisão no Protocolo e cancelar a prenotação. Na improcedente, o interessado reapresenta os documentos com mandado ou certidão da sentença, que ficam arquivados; o registro é feito desde logo, com anotação do fato no Protocolo. [LRP](https://www.planalto.gov.br/ccivil_03/leis/l6015compilada.htm) — Art. 203, caput e I–II.

Referência: `LRP-RI-DUVIDA-014-SAIDA`.

### Qual é a natureza da decisão, o que ela não impede e quando há custas para o interessado na dúvida?

A decisão da dúvida tem natureza administrativa e não impede o processo contencioso competente. No processo de dúvida, o interessado paga custas somente quando a dúvida for julgada procedente. [LRP](https://www.planalto.gov.br/ccivil_03/leis/l6015compilada.htm) — Arts. 204 e 207.

Referência: `LRP-RI-DUVIDA-014-NATUREZA`.

### Na opção do art. 206-A II, quando se paga o restante e esse intervalo consome o prazo do art. 188?

Na opção de pagar inicialmente a prenotação, o restante é depositado em 5 dias da análise que conclua pela aptidão do título; os efeitos da prenotação são mantidos nesse período. O intervalo de pagamento do art. 206-A não integra o prazo de registro do art. 188; após o depósito, seguem os procedimentos de registro e expedição da certidão. [LRP](https://www.planalto.gov.br/ccivil_03/leis/l6015compilada.htm) — Art. 206-A, caput, II, §§1º–2º e 7º.

Referência: `LRP-RI-PAGAMENTO-015`.

### Para qual elenco de penas remete o art. 188 §2º e isso significa perda automática?

A inobservância do art. 188 enseja a aplicação das penas do art. 32 da Lei 8.935, nos termos estabelecidos pela Corregedoria Nacional de Justiça. O elenco inclui repreensão, multa, suspensão e perda da delegação, assegurado amplo direito de defesa. A remissão ao elenco não impõe automaticamente a perda da delegação por qualquer atraso. [LRP](https://www.planalto.gov.br/ccivil_03/leis/l6015compilada.htm); [L8935](https://www.planalto.gov.br/ccivil_03/leis/l8935.htm) — LRP, art. 188 §2º; Lei 8.935, art. 32.

Referência: `LRP-RI-PRAZO-SANCAO-016`.

### No art. 167 I 21, qual citação está prevista e a modalidade é registro ou averbação?

A citação de ação real ou pessoal reipersecutória relativa a imóvel está prevista entre os atos de registro do art. 167, I, 21. [LRP](https://www.planalto.gov.br/ccivil_03/leis/l6015compilada.htm) — Art. 167, I, 21.

Referência: `LRP-RI-CITACAO-017`.

## 6. EXAM / OUTPUT

Casos **GX sintéticos / BUILD**. Não são questões oficiais, itens reservados, notas do candidato ou prova de suficiência. A justificativa aplica regras já ensinadas; a base normativa é inserida automaticamente pelos IDs.

### GX-RI-01

O oficial cumpriu e certificou a ciência e a notificação previstas no art. 198 §1º III. O apresentante ainda não impugnou e os 15 dias não terminaram. A lei exige aguardar esse prazo para remeter o título e as razões ao juízo?

**Resposta comentada: Não.** A condição de remessa do inciso IV já foi satisfeita. A impugnação perante o juízo não é um requisito prévio que retenha o título no cartório.

**Base para conferir a resposta:**

- `LRP-RI-DUVIDA-014`: Anotada a dúvida no Protocolo e certificadas a prenotação e a suscitação no título, com rubrica das folhas, o oficial dá ciência dos termos ao apresentante, fornece cópia e o notifica para impugnar perante o juízo em 15 dias. Certificado o cumprimento da ciência e notificação, remete eletronicamente título e razões ao juízo. A remessa não aguarda a impugnação nem o término desses 15 dias. [LRP](https://www.planalto.gov.br/ccivil_03/leis/l6015compilada.htm) — Art. 198, §1º, I–IV.

### GX-RI-02

O apresentante deixou transcorrer o prazo de impugnação. Pode-se encerrar a dúvida sem sentença e cancelar automaticamente a prenotação apenas por esse silêncio?

**Resposta comentada: Não.** A omissão do apresentante não dispensa o julgamento. A saída de cancelamento precisa ser ligada ao resultado e ao marco previstos no art. 203, não presumida a partir do silêncio.

**Base para conferir a resposta:**

- `LRP-RI-DUVIDA-014-SILENCIO`: Mesmo sem impugnação no prazo legal, a dúvida será julgada por sentença. [LRP](https://www.planalto.gov.br/ccivil_03/leis/l6015compilada.htm) — Art. 199.

- `LRP-RI-DUVIDA-014-SAIDA`: Depois do trânsito em julgado, a dúvida procedente leva à restituição dos documentos à parte, independentemente de traslado, e à ciência ao oficial para anotar a decisão no Protocolo e cancelar a prenotação. Na improcedente, o interessado reapresenta os documentos com mandado ou certidão da sentença, que ficam arquivados; o registro é feito desde logo, com anotação do fato no Protocolo. [LRP](https://www.planalto.gov.br/ccivil_03/leis/l6015compilada.htm) — Art. 203, caput e I–II.

### GX-RI-03

A dúvida foi julgada improcedente, houve trânsito em julgado e o interessado reapresentou os documentos com certidão da sentença. A providência indicada pelo art. 203 II é realizar o registro desde logo e anotar o fato no Protocolo?

**Resposta comentada: Sim.** O caso forneceu os pressupostos documentais e temporais da saída favorável ao registro. A certidão ou o mandado acompanha a reapresentação e é arquivado conforme o dispositivo.

**Base para conferir a resposta:**

- `LRP-RI-DUVIDA-014-SAIDA`: Depois do trânsito em julgado, a dúvida procedente leva à restituição dos documentos à parte, independentemente de traslado, e à ciência ao oficial para anotar a decisão no Protocolo e cancelar a prenotação. Na improcedente, o interessado reapresenta os documentos com mandado ou certidão da sentença, que ficam arquivados; o registro é feito desde logo, com anotação do fato no Protocolo. [LRP](https://www.planalto.gov.br/ccivil_03/leis/l6015compilada.htm) — Art. 203, caput e I–II.

### GX-RI-04

Na opção do art. 206-A II, o usuário completa o depósito dentro do intervalo legal após a análise de aptidão. Esse intervalo deve consumir parte do prazo de registro do art. 188?

**Resposta comentada: Não.** O erro seria tratar como um só relógio o pagamento do usuário e o prazo registral. A exclusão vem de regra expressa, não de uma preferência de organização do cartório.

**Base para conferir a resposta:**

- `LRP-RI-PAGAMENTO-015`: Na opção de pagar inicialmente a prenotação, o restante é depositado em 5 dias da análise que conclua pela aptidão do título; os efeitos da prenotação são mantidos nesse período. O intervalo de pagamento do art. 206-A não integra o prazo de registro do art. 188; após o depósito, seguem os procedimentos de registro e expedição da certidão. [LRP](https://www.planalto.gov.br/ccivil_03/leis/l6015compilada.htm) — Art. 206-A, caput, II, §§1º–2º e 7º.

### GX-RI-05

Um comentário afirma que atrasar o prazo do art. 188 nunca pode levar às penas da Lei 8.935, porque a LRP não faz remissão a elas. O comentário está correto?

**Resposta comentada: Não.** A remissão existe. Reconhecer o elenco de consequências possíveis não autoriza escolher automaticamente a mais grave para qualquer atraso.

**Base para conferir a resposta:**

- `LRP-RI-PRAZO-SANCAO-016`: A inobservância do art. 188 enseja a aplicação das penas do art. 32 da Lei 8.935, nos termos estabelecidos pela Corregedoria Nacional de Justiça. O elenco inclui repreensão, multa, suspensão e perda da delegação, assegurado amplo direito de defesa. A remissão ao elenco não impõe automaticamente a perda da delegação por qualquer atraso. [LRP](https://www.planalto.gov.br/ccivil_03/leis/l6015compilada.htm); [L8935](https://www.planalto.gov.br/ccivil_03/leis/l8935.htm) — LRP, art. 188 §2º; Lei 8.935, art. 32.

### GX-RI-06

A dúvida foi julgada procedente. Uma resposta diz que, por isso, o interessado conseguiu o registro e não paga custas da dúvida. Essa leitura das duas consequências está correta?

**Resposta comentada: Não.** A palavra procedente se refere à dúvida. Confira separadamente a saída registral após o trânsito e a regra específica de custas, evitando inverter o beneficiário da decisão.

**Base para conferir a resposta:**

- `LRP-RI-DUVIDA-014-SAIDA`: Depois do trânsito em julgado, a dúvida procedente leva à restituição dos documentos à parte, independentemente de traslado, e à ciência ao oficial para anotar a decisão no Protocolo e cancelar a prenotação. Na improcedente, o interessado reapresenta os documentos com mandado ou certidão da sentença, que ficam arquivados; o registro é feito desde logo, com anotação do fato no Protocolo. [LRP](https://www.planalto.gov.br/ccivil_03/leis/l6015compilada.htm) — Art. 203, caput e I–II.

- `LRP-RI-DUVIDA-014-NATUREZA`: A decisão da dúvida tem natureza administrativa e não impede o processo contencioso competente. No processo de dúvida, o interessado paga custas somente quando a dúvida for julgada procedente. [LRP](https://www.planalto.gov.br/ccivil_03/leis/l6015compilada.htm) — Arts. 204 e 207.

### Critério de revisão da produção

Em cada caso, conferir: identificação da hipótese; conclusão; presença dos elementos das proposições indicadas; ausência de condição ou efeito inventado. É uma rubrica editorial para este recorte, sem pontuação de mastery e sem validação da capacidade de resolver uma prova completa.
