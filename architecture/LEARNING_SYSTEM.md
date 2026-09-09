# Arquitetura de Aprendizagem — GX Cartório OS

Atualizado em 09/09/2026.

## Estado inicial assumido
O sistema não presume base jurídica recente. Deve funcionar para candidato enferrujado, com dificuldade de iniciação e baixa confiança metacognitiva.

O candidato é bacharel em Direito, mas a base competitiva operacional é tratada como **próxima de zero até evidência em contrário**. Direito Notarial e Registral é considerado domínio majoritariamente novo.

## Objetivo pedagógico
Construir conhecimento em quatro dimensões simultâneas:
1. **Compreensão** — entender conceitos, estrutura e fundamento.
2. **Recuperação** — produzir a resposta sem pistas.
3. **Discriminação** — separar institutos semelhantes e resistir a distratores.
4. **Aplicação/produção** — resolver caso e, conforme relevância, escrever, executar peça e sustentar oralmente.

## Grafo de domínio
Unidade mínima: `Learning Node`.

Campos essenciais:
- disciplina;
- tema/subtema/microtema;
- pré-requisitos;
- conceitos-base;
- fontes oficiais;
- questões associadas;
- evidências de domínio;
- erros recorrentes;
- prioridade;
- última prática;
- próxima recuperação.

## Escala canônica de mastery — M0 a M7
Esta é a única escala de mastery válida no GX. `Estabilidade/retention` é eixo separado e não constitui nível adicional.

- `M0 — Não visto`.
- `M1 — Reconhece com apoio`: identifica conceito/regra quando há pista suficiente.
- `M2 — Recupera núcleo sem apoio`: produz regra ou estrutura central sem consultar.
- `M3 — Discrimina`: separa institutos próximos, exceções e distratores plausíveis.
- `M4 — Aplica`: resolve item ou caso objetivo **inédito**, justificando a variável decisiva.
- `M5 — Produz escrito`: entrega resposta discursiva juridicamente suficiente sob restrição adequada.
- `M6 — Executa prática`: identifica e produz solução/ato/peça procedimental quando o tema admitir.
- `M7 — Sustenta oral`: explica e defende o tema sob tempo e reperguntas.

Nem todo nó precisa chegar a M7. O teto exigido depende do edital, da fase e do valor de transferência.

### Estabilidade é ortogonal
Um nó pode estar em M4 e ainda ser frágil. Registrar separadamente:
- estabilidade/força de retenção;
- probabilidade estimada de recuperação;
- intervalo desde última evidência;
- reincidência de erro.

Não elevar mastery apenas por leitura, explicação imediatamente repetida ou acerto isolado.

## Promoção baseada em evidência
A promoção entre níveis deve evoluir para regras observáveis. Enquanto não houver dados suficientes para calibrar thresholds definitivos, usar gates conservadores:
- M1→M2: recall sem pista do núcleo;
- M2→M3: discriminação correta contra pelo menos um par próximo;
- M3→M4: desempenho em caso/item não visto;
- M4→M5: produção escrita avaliada por rubrica/espelho quando disponível;
- M5→M6: execução prática com estrutura e fundamento adequados;
- M6→M7: resposta oral completa + repergunta.

Persistência após intervalo valida **estabilidade**, não substitui a natureza do nível.

## Sequenciamento
A ordem de ensino deriva de:
1. pré-requisitos conceituais;
2. centralidade no Direito Notarial/Registral e conexões;
3. peso estrutural do edital e evidência de prova;
4. estado individual do candidato;
5. tempo até o alvo;
6. freshness e volatilidade normativa.

N/R entra desde o início. Bases de Civil, Constitucional, Administrativo e demais ramos são recuperadas **just in time**, sem exigir uma revisão integral da graduação antes do núcleo extrajudicial.

## Ciclo de uma unidade
1. **Mapa curto** — onde o tema mora e por que existe.
2. **Fundamentos mínimos** — apenas o que destrava o conteúdo.
3. **Teoria mestre** — regra, requisitos, efeitos, exceções e procedimento.
4. **Exemplos corretos e contraexemplos**.
5. **Lei seca/fonte guiada**.
6. **Recuperação livre curta**.
7. **Questões reais selecionadas**.
8. **Feedback causal do erro**.
9. **Questão de transferência**.
10. **Microdiscursiva/oral**, quando o nó permitir.
11. **Agendamento adaptativo de recuperação**.

## Motor de retenção
Não usar calendário fixo 24h/7d/30d como regra permanente e não delegar ao LLM uma intuição irrestrita sobre esquecimento.

### Bootstrap
Enquanto há pouco histórico individual, intervalos heurísticos podem servir de sementes. Depois, a agenda deve usar evidência real de:
- correção;
- confiança pré-resposta;
- latência;
- necessidade de pista;
- reincidência;
- dificuldade;
- importância do nó;
- intervalo desde a última evidência.

### FSRS e algoritmos especializados
FSRS é candidato preferencial para **recalls atômicos/flashcards e itens de recuperação repetível**, por ser aberto, auditável e amplamente testado em históricos de revisão.

Ele não substitui todo o scheduler jurídico. Mastery de discriminação, item inédito, discursiva, peça e oral exige evidência própria. O desenho é híbrido:
- `retention model` decide quando reativar unidades recuperáveis;
- `mastery gates` medem qual saída jurídica o candidato consegue executar;
- `orchestrator` monta a sessão com peso de prova, prontidão, erros e fase.

Não introduzir DKT/SAKT ou modelos complexos antes de haver volume individual suficiente para justificar ganho real.

### Evidência forte
Resposta correta, relativamente rápida, sem pista, com justificativa e após intervalo significativo.

### Evidência fraca
Reconhecimento por alternativa, chute, acerto inseguro ou resposta correta imediatamente após leitura.

## Diagnóstico de erro
Classificar antes de intervir:
- lacuna conceitual;
- desconhecimento de norma;
- confusão entre institutos;
- atualização normativa;
- jurisprudência;
- leitura/interpretação;
- atenção;
- estratégia de prova;
- incapacidade de recuperação;
- aplicação inadequada ao caso;
- falsa confiança;
- sobre-inferência.

Cada causa pede intervenção diferente. Releitura não é tratamento universal.

## Métricas
Priorizar medidas que mudam decisão:
- acurácia em item inédito;
- mastery M0–M7 por nó;
- estabilidade/retention após intervalo;
- calibração confiança × acerto;
- latência quando relevante;
- taxa de transferência;
- reincidência de erro;
- discriminação entre institutos;
- desempenho em discursiva/peça/oral;
- cobertura ponderada do edital;
- desempenho em simulados representativos.

Horas assistidas, páginas produzidas e quantidade bruta de questões são métricas auxiliares, não domínio.

## Regra operacional de baixa fricção
O sistema deve minimizar decisões antes da primeira ação. O comando padrão do candidato pode ser apenas `Começar`.

Resposta do orquestrador:
- uma primeira tarefa pequena e definida;
- sem lista excessiva de opções;
- continuidade automática após cada bloco;
- registro feito pelo sistema ao final.

## Horizonte temporal atual
- 2026: bootstrap + início do estudo real; ENAC 2026.2 fora do alvo por decisão autoral.
- primeira edição ENAC 2027: primeiro alvo de habilitação.
- fim de 2027: alvo desejado de prontidão competitiva ampla.
- 2028: teto/buffer máximo, não duração padrão prometida.

O ritmo é recalculado semanalmente a partir de execução, velocidade de aquisição, retenção, backlog, simulados e alvo real. Qualidade de domínio tem precedência sobre completar páginas, mas a cobertura integral do edital continua obrigatória ao longo do ciclo.
