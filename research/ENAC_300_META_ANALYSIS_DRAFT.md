# ENAC 300 — Meta-análise preliminar

Status: **DRAFT / não preditivo**
Atualizado em 08/09/2026.

Este documento cruza os três relatórios intraprova já completos. Ele deliberadamente separa fatos determinísticos de padrões qualitativos repetidos. Percentuais finos aguardam QA agregado do banco e passagem 2.

## 1. Fatos já seguros

### Corpus
- 3 edições oficiais completas analisadas em passagem 1;
- 300 itens históricos;
- 6 questões anuladas no gabarito definitivo;
- 294 itens com resposta definitiva não anulada.

### Matriz histórica comum
2025.1, 2025.2 e 2026.1 tiveram a mesma distribuição macro:
- 60 N/R;
- 14 Civil;
- 9 Constitucional;
- 4 Administrativo;
- 4 Tributário;
- 4 Empresarial;
- 2 Processo Civil;
- 1 Penal;
- 1 Processo Penal;
- 1 Conhecimentos Gerais.

Portanto, no corpus histórico existem 180 questões formalmente N/R e 120 de outras disciplinas.

### Matriz atual
2026.2 mantém 60 N/R e 14 Civil, reduz Constitucional de 9 para 8, remove Conhecimentos Gerais e introduz Trabalho e Processo do Trabalho com 1 cada.

## 2. Padrões qualitativos independentes repetidos nas três edições

Os relatórios das três provas, produzidos separadamente antes desta síntese, convergem em vários pontos.

### 2.1 O rótulo da disciplina não descreve sozinho o conhecimento exigido
N/R contém Civil, garantias, família, sucessões, responsabilidade e normas administrativas. Civil, Administrativo, Tributário e Empresarial frequentemente retornam a cenários ou consequências cartorárias.

**Implicação pedagógica:** currículo e material não podem ser apostilas-silo. A disciplina oficial deve coexistir com relações semânticas e pré-requisitos.

### 2.2 A FGV alterna aplicação e precisão normativa
Há forte presença de casos concretos e decisões operacionais, mas também itens de listas, requisitos, definições, doutrina e jurisprudência.

**Implicação:** não é suficiente treinar apenas caso prático nem apenas lei seca. O scheduler deve alternar formatos conforme microtema.

### 2.3 A variável decisiva costuma ser pequena
Nos três relatórios aparecem repetidamente diferenças de:
- competência;
- requisito;
- prazo/momento;
- efeito jurídico;
- legitimidade;
- exceção;
- via judicial versus extrajudicial;
- responsabilidade;
- conceito próximo.

**Hipótese a quantificar:** boa parte dos distratores plausíveis preserva quase todo o enunciado jurídico e troca uma variável crítica.

### 2.4 Civil funciona como infraestrutura do extrajudicial
Os três exames reforçam direitos reais, obrigações, contratos, capacidade, família e sucessões em problemas notariais/registrais ou diretamente conectados à serventia.

**Implicação:** Civil precisa de alta centralidade no dependency graph apesar de possuir 14% da prova formal.

### 2.5 Atualização normativa é parte do conteúdo
SERP, CNIB, centrais, atos CNJ, desjudicialização, garantias e procedimentos eletrônicos aparecem repetidamente.

**Implicação:** Freshness Firewall é componente curricular, não mero clipping informativo.

### 2.6 A FGV cartorializa matérias externas
Exemplos recorrentes nos relatórios:
- Constitucional: serventias, emolumentos, interinidade, competências;
- Administrativo: responsabilidade por ato notarial, regime de delegação, improbidade;
- Tributário: ITBI/ITCMD/ISS/IR com ligação a imóveis, escrituras ou titular de serventia;
- Empresarial: protesto, garantias, títulos e recuperação;
- Processo Penal/Penal: cenários de serventia ou PLD/FT.

**Implicação:** o MASTER geral pode ensinar a base da disciplina, mas transferência e questões devem voltar ao universo cartorário sempre que houver evidência.

## 3. Clusters de alta conectividade que merecem passagem 2 prioritária

Isto é prioridade de **análise**, não ainda prioridade final de estudo:

1. Registro de Imóveis + direitos reais + garantias;
2. desjudicialização: usucapião, adjudicação, inventário/divórcio;
3. RCPN + família + nome + filiação + atos estrangeiros;
4. Tabelionato de Notas + sucessões + capacidade + escrituras;
5. Protesto + crédito + Empresarial + Tributário;
6. SERP/CNIB/centrais eletrônicas + regulação CNJ;
7. regime da delegação + responsabilidade + interinidade;
8. parcelamento/incorporação/regularização fundiária;
9. proteção de dados/compliance/PLD-FT.

## 4. Anulações como fonte de engenharia de qualidade

As seis anuladas não serão descartadas. Na passagem 2 serão analisadas por:
- ambiguidade semântica;
- mudança normativa;
- conflito de fonte;
- mais de uma alternativa defensável;
- ausência de alternativa correta;
- problema de redação;
- eventual mudança entre preliminar e definitivo.

Objetivo: ensinar o GX a evitar gerar questões sintéticas com as mesmas patologias.

## 5. Fonte de resolução das questões

As páginas oficiais da FGV das três edições disponibilizam:
- caderno oficial;
- gabarito preliminar;
- **respostas aos recursos contra o gabarito preliminar**;
- gabarito definitivo.

Portanto, a reconstrução da questão na passagem 2 terá hierarquia:
1. caderno oficial;
2. gabarito definitivo;
3. resposta oficial da banca aos recursos, quando acessível;
4. fonte jurídica primária histórica;
5. fonte jurídica atual;
6. comentários especializados secundários.

A resposta a recurso da própria banca é especialmente útil para compreender a **rationale da FGV**, mas não substitui a verificação jurídica atual.

## 6. Hipóteses quantitativas que aguardam dados agregados

Não publicar números ainda para:
- distribuição de mecanismos de distrator;
- frequência de CNJ vs lei vs jurisprudência vs doutrina;
- tamanho médio de enunciado;
- quantidade de questões realmente interdisciplinares;
- recorrência por microtema;
- persistência entre três edições;
- taxa de novidade por edição;
- proximidade temporal da norma cobrada;
- concentração de temas em clusters;
- mudança de estilo entre 2025.1 e 2026.1.

## 7. Consequências já autorizadas para o design do Material Mestre

Mesmo antes dos percentuais finos, a convergência das três provas autoriza:
- `MAP` para localizar o instituto;
- `MASTER` com conceito + regra + fundamento + procedimento + efeito + exceção;
- quadro `CONFUNDE COM`;
- `Freshness` visível para temas voláteis;
- caso operacional cedo;
- alternativas comentadas por mecanismo de erro;
- `RECALL` sem alternativas;
- transferência para discursiva/oral em temas de alta relevância estadual;
- links cruzados entre disciplinas em vez de repetição de texto.

## 8. Próximos passos

1. QA agregado 300/300 quando a consulta Notion estiver disponível;
2. passagem 2 começando por N/R + Civil de maior conectividade;
3. incorporar resposta oficial a recursos quando acessível;
4. medir padrões quantitativamente;
5. somente então promover `ENAC_300_META_ANALYSIS.md` de DRAFT para canônico;
6. cruzar com corpus estadual e FGV L4/L3 para reduzir risco de overfit a apenas três ENACs.
