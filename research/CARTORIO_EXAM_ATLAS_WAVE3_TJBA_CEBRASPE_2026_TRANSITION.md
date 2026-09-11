# GX Cartório OS — Exam Atlas Wave 3
## TJBA / Cebraspe 2026 — Written/Practical + Regulatory Transition

Snapshot: 2026-09-10
Status: VERIFIED SOURCE ANALYSIS

## Fontes
Edital/caderno oficial Cebraspe:
https://cdn.cebraspe.org.br/concursos/tj_ba_25_notarios/

Resolução CNJ 696/2026 vigente:
https://atos.cnj.jus.br/atos/detalhar/7011

## 1. Por que esta prova é importante
O TJBA/Cebraspe oferece contraste com TJMS/FGV em:
- banca;
- distribuição de pontos;
- tamanho das respostas;
- forma de explicitar subitens;
- exigência de escrita;
- peça notarial real.

Também captura o perigo de usar prova recente sem considerar o REGIME NORMATIVO do edital.

## 2. Formato oficial da escrita/prática
O edital estabelece:
- 5 horas;
- 10 pontos totais;
- 1 dissertação de até 30 linhas = 4 pontos;
- 1 peça prática de até 90 linhas = 4 pontos;
- 2 questões discursivas de até 15 linhas = 1 ponto cada.

A banca separa conteúdo e língua/estrutura, com pontuação explícita para domínio jurídico, apresentação e modalidade escrita.

## 3. Conteúdo observado
### Dissertação
Desconsideração da personalidade jurídica em cenário de transferência patrimonial para sociedade para frustrar credores.

A banca fornece três deliverables explícitos:
1. conceito + legitimados;
2. pressupostos;
3. desconsideração inversa + aplicação ao caso.

Consequência GX:
- Cebraspe tende, nesta amostra, a transformar a resposta em `rubric-visible prompts`;
- treino pode ensinar decomposição do comando em átomos antes da redação;
- 30 linhas exigem densidade, não tratado.

### Peça prática
Casal procura tabelionato para proteger imóvel familiar contra futuras penhoras. A banca exige a elaboração, na condição de tabelião, do ato que produza os efeitos jurídicos desejados, com base no Código Civil e Lei 8.009/90.

A peça é de até 90 linhas e traz instruções formais detalhadas sobre qualificação, datas, assinaturas e informações dispensadas.

Consequência GX:
- practical training precisa incluir `DOCUMENT GRAMMAR`, não apenas conteúdo substantivo;
- o candidato deve saber identificar o ato correto a partir da intenção do usuário;
- deve dominar estrutura e requisitos formais suficientes para produzir o instrumento.

### Questão discursiva 1
Tema: escreventes e substitutos interinos em serventias extrajudiciais.
Exige texto constitucional + jurisprudência STF sobre:
- natureza como agentes públicos;
- equiparação ou não ao titular;
- teto remuneratório;
- controle prévio da contratação;
- concurso/processo seletivo;
- responsabilidade civil do Estado.

Consequência GX:
Um nó aparentemente de Regime Geral N/R possui satélites em Constitucional/Administrativo/jurisprudência. O `Integrated Case Graph` precisa registrar isso sem duplicar conteúdo.

### Questão discursiva 2
Tema: erro de proibição.
Exige:
- conceito;
- espécies direta e indireta;
- distinção em relação ao erro sobre elementos do tipo.

## 4. ALERTA DE TRANSIÇÃO — Penal na discursiva
A presença de erro de proibição nesta prova NÃO pode ser usada para planejar OUTPUT penal no futuro baseline nacional.

Razão:
- este concurso foi estruturado sob edital anterior à vigência da Resolução CNJ 696/2026;
- art. 48, §2º, da Resolução 696 determina agora que Direito Penal, Processo Penal, Trabalho e Processo do Trabalho serão exigidos exclusivamente no ENAC e na prova objetiva.

### Regra nova do Atlas: REGIME TAG
Toda prova recebe:
- `REGIME_81_PRE_ENAC`;
- `REGIME_81_ENAC_TRANSITION`;
- `REGIME_696`;
- ou tag futura equivalente.

Toda evidência de modalidade recebe validade:
- `CONTENT_VALIDITY`: a proposição jurídica ainda pode ser atual;
- `PHASE_VALIDITY`: a modalidade em que apareceu ainda é permitida no baseline vigente?

Assim, TJBA/2026 Penal pode ser:
- válido como questão jurídica e challenge;
- inválido para aumentar `OUTPUT_PRIORITY_PENAL` sob Res. 696.

## 5. Comparação inicial FGV x Cebraspe
Amostra insuficiente para DNA definitivo, mas já permite hipóteses a testar.

### FGV/TJMS
- peça 80 linhas;
- dissertação 80 linhas;
- quatro discursivas 30 linhas;
- casos muito integrados;
- espelho atomizado em muitos itens de pontuação.

### Cebraspe/TJBA
- peça 90 linhas;
- dissertação 30 linhas;
- duas discursivas 15 linhas;
- comandos explicitam subitens e valores;
- conteúdo + língua/estrutura têm fórmulas de avaliação próprias.

### Hipótese de banca, NÃO CANÔNICA ainda
FGV nesta amostra demanda mais espaço para desenvolvimento de casos complexos; Cebraspe comprime respostas e fornece alvos mais explícitos. Precisa de triangulação com outros concursos das duas bancas antes de virar regra pedagógica.

## 6. Regra de treino derivada
OUTPUT training deve armazenar dois parâmetros separados:
- `KNOWLEDGE_ATOMS` = o que juridicamente precisa estar presente;
- `BANK_PACKAGING` = como aquela banca exige organizar, limitar e escrever.

Isso permite estudar o Direito uma vez e adaptar embalagem por banca depois.

## 7. Consequência para o candidato multiestado
A base de conhecimento deve ser nacional e reutilizável.
Quando edital-alvo aparece, o GX injeta:
- overlay local;
- restrições da banca;
- tamanho de resposta;
- estilo de peça;
- regras de consulta;
- pesos;
- jurisprudência/atos locais relevantes.

O conteúdo nacional não é reconstruído do zero.

## 8. Próximo passo
- triangular FGV com RN/ES;
- triangular Cebraspe com RO/RR;
- iniciar Proposition Ledger N/R no eixo Regime Geral/Lei 8.935 + CNN/CNJ;
- separar `content evidence` de `phase evidence` em todas as linhas do Atlas.