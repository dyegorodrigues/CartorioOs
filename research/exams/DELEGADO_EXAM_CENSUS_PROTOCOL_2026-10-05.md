# DELEGADO EXAM CENSUS — Protocolo de Cobertura
**Data:** 05/10/2026
**Status:** vigente
**Objetivo:** construir um inventário tão completo quanto tecnicamente possível das provas de Delegado de Polícia, sem reduzir a pesquisa aos certames recentes já citados.

## 1. Escopo obrigatório

### Carreira primária
- Delegado de Polícia Federal.
- Delegados das Polícias Civis de todos os Estados e do DF.

### Fases
Sempre que publicamente acessíveis:
- objetiva;
- discursiva;
- peça/prático-profissional;
- oral;
- padrões/espelhos de resposta;
- recursos/anulações relevantes.

### Janela temporal
**Sem corte rígido de exclusão.**
Ordem de ingestão:
1. 2026 → trás, pelos certames mais recentes;
2. completar ciclos 2015–2026;
3. retroceder 2010–2014;
4. backfill histórico anterior a 2010 quando houver prova digital utilizável.

Motivo: recência importa para vigência e estilo, mas provas antigas ainda revelam doutrina, nomenclaturas, origem de cobranças e padrões históricos.

## 2. Fontes em ordem de autoridade

### Tier 0 — oficial
- página da banca;
- página do órgão;
- caderno oficial;
- gabarito definitivo;
- espelho/padrão oficial;
- decisão de recurso/anulação.

### Tier 1 — arquivo de prova confiável
- PCI Concursos e repositórios equivalentes para descoberta/recuperação histórica.

### Tier 2 — bancos de questões
- TEC Concursos;
- QConcursos;
- Gran Questões;
- outros bancos relevantes.

Uso:
- localizar itens;
- taxonomia;
- comentários;
- incidência;
- filtros por banca/cargo/ano.

Não substituem o oficial quando o documento oficial existe.

### Tier 3 — materiais comentados
- cursinhos;
- PDFs de questões comentadas;
- blogs/professores;
- comentários de usuários.

Uso:
- descobrir raciocínio;
- identificar controvérsia;
- encontrar fonte;
- comparar explicações.

Nunca promover automaticamente para verdade jurídica.

## 3. Registro por certame

Cada prova/ciclo recebe:
- exam_id;
- órgão/UF;
- cargo;
- banca;
- ano;
- data;
- fase;
- caderno/tipo;
- URL oficial;
- fonte alternativa;
- gabarito preliminar;
- gabarito definitivo;
- anulações;
- número de questões;
- número de questões penais;
- número de itens mapeados ao C01;
- status de ingestão;
- status de auditoria;
- snapshot jurídico;
- observações.

## 4. Registro por questão

Cada item recebe:
- question_id;
- exam_id;
- número;
- disciplina;
- matéria;
- tema;
- tópico;
- subtópico;
- microtópico;
- Claim(s);
- artigo(s);
- jurisprudência;
- doutrina/autoria quando exigida;
- gabarito;
- status do gabarito;
- dificuldade;
- tipo cognitivo;
- mecanismo de cobrança;
- mecanismo de distrator;
- comentário oficial;
- comentário editorial Tutor OS;
- comentário de terceiros como candidato separado;
- validade histórica × atual;
- bugs curriculares detectados.

## 5. Todas as questões de Delegado, não só as que “parecem introdutórias”

A ingestão da prova é integral.

Depois o sistema classifica:
- C01 direto;
- C01 indireto/ponte;
- outro módulo;
- legislação especial;
- criminologia;
- processo etc.

Isso evita perder uma cobrança de C01 escondida dentro de caso prático ou questão de outro rótulo.

## 6. Bancos de questões como detector de cobertura

Exemplo de uso:
- TEC pode mostrar grande universo filtrado por Delegado.
- QConcursos pode oferecer comentários de professor/usuário e classificações alternativas.
- Gran Questões pode ajudar a localizar questões vinculadas a materiais Gran.

A contagem de cada plataforma é tratada como **índice do próprio banco**, não como verdade absoluta sobre “quantas questões existem”.

## 7. Outras carreiras continuam entrando

Depois do Censo Delegado:
- ENAM;
- ENAC;
- Magistratura;
- Ministério Público;
- Defensoria;
- Procuradorias;
- demais carreiras jurídicas de alta exigência.

Função: transferência de microconhecimento, banca e fase.
Nunca contam artificialmente como incidência de Delegado.

## 8. Critério de completude

Não declarar “100% de todas as questões da internet”.

Declarar, quando alcançado:
- “certame X integralmente ingerido”;
- “fonte Y integralmente varrida até data Z”;
- “C01 coberto em N provas oficiais e M bancos”.

O ledger mantém lacunas conhecidas.

## 9. Primeira fila ampliada

### 2025–2026 / atuais ou recentíssimos
- PF 2025
- PC-DF 2026
- PC-PI 2025/2026
- PC-PR 2026
- PC-CE 2025
- PC-MG 2024/2025
- PC-SC 2023/2024
- PC-RS 2025/2026
- PC-PE 2023/2024
- demais ciclos identificados no universo-alvo

### Backfill já evidenciado em arquivos públicos
- PC-RJ 2022
- PC-AM 2022
- PC-MS 2021
- PC-PR 2021
- PC-RS 2018
- PC-MT 2017
- PC-GO 2017 / 2013
- PC-BA 2016
- PC-SC 2014
- PC-ES 2010
- além de provas anteriores localizadas em arquivos históricos.

Esta lista é fila inicial, não universo fechado.
