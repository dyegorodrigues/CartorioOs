# Arquitetura de Aprendizagem — GX Cartório OS

## Estado inicial assumido
O sistema não presume base jurídica recente. Deve funcionar para candidato enferrujado, com dificuldade de iniciação e baixa confiança metacognitiva.

## Objetivo pedagógico
Construir conhecimento em quatro camadas simultâneas:
1. **Compreensão** — entender conceitos, estrutura e fundamento.
2. **Recuperação** — produzir a resposta sem pistas.
3. **Discriminação** — separar institutos semelhantes e resistir a distratores.
4. **Aplicação** — resolver caso, discursiva, peça e oral.

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

## Estados de domínio
- `0 Não visto`
- `1 Reconheço`
- `2 Compreendo com apoio`
- `3 Recupero sem apoio`
- `4 Aplico em questão nova`
- `5 Transfiro para discursiva/oral/peça`
- `6 Domínio estável` após evidência tardia

Não elevar estado apenas por leitura ou acerto isolado.

## Sequenciamento
A ordem de ensino é derivada de quatro sinais:
1. pré-requisitos conceituais;
2. centralidade no Direito Notarial/Registral e conexões;
3. peso/incidência de prova;
4. estado individual do candidato.

Exemplo: um tópico de Registro de Imóveis pode exigir recuperar previamente negócio jurídico, direitos reais, forma, publicidade e princípios registrais. O sistema deve ensinar o mínimo necessário desses fundamentos antes de exigir aplicação complexa.

## Ciclo de uma unidade
1. **Mapa de 2 minutos** — onde o tema mora e por que existe.
2. **Fundamentos** — conceitos elementares necessários.
3. **Teoria mestre** — regra, requisitos, efeitos, exceções e procedimento.
4. **Exemplos corretos e contraexemplos**.
5. **Lei seca guiada**.
6. **Recuperação livre curta**.
7. **Questões reais selecionadas**.
8. **Feedback causal do erro**.
9. **Questão de transferência**.
10. **Microdiscursiva/oral**, quando o nó permitir.
11. **Agendamento adaptativo de revisão**.

## Motor de revisão
Não usar calendário fixo 24h/7d/30d como regra permanente.

Bootstrap possível: revisão precoce após primeiro contato. Depois os intervalos dependem de:
- correção;
- confiança;
- latência;
- necessidade de pista;
- recorrência de erro;
- dificuldade;
- importância do nó;
- intervalo desde a última evidência.

### Evidência forte
Resposta correta, relativamente rápida, sem pista, com justificativa e depois de intervalo significativo.

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
- aplicação inadequada ao caso.

Cada causa pede intervenção diferente. Releitura não é tratamento universal.

## Métricas
- cobertura do edital;
- mastery por nó;
- retenção tardia;
- acurácia;
- calibração confiança × acerto;
- latência;
- taxa de transferência para questão inédita;
- recorrência de erro;
- discriminação entre institutos;
- desempenho em discursiva;
- desempenho em peça;
- desempenho oral;
- consistência semanal.

## Regra anti-TDAH operacional
O sistema deve minimizar decisões antes da primeira ação. O comando padrão do candidato pode ser apenas `Começar`.

Resposta do orquestrador:
- uma primeira tarefa pequena e definida;
- sem lista excessiva de opções;
- continuidade automática após cada bloco;
- registro feito pelo sistema ao final.

## Horizonte temporal
Não prometer domínio em prazo arbitrário. O ritmo é recalculado semanalmente a partir de:
- horas líquidas realmente executadas;
- velocidade de aquisição;
- retenção;
- volume de revisões vencidas;
- desempenho em simulados;
- data do alvo real.

Qualidade de domínio tem precedência sobre completar páginas, mas a cobertura integral do edital continua obrigatória ao longo do ciclo.
