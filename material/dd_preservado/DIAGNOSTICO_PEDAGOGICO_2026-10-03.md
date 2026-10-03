# Correção de método após o retorno sobre a v2

Retorno do usuário: 03/10/2026, 10h02 BRT. A aparência melhorou parcialmente, mas o material continua confuso, fragmentado e inferior à apostila como instrumento de aprendizagem. Isso não é aprovação da v2 como padrão de conteúdo. Nesta rodada foi feita comparação diagnóstica; não foi produzida uma nova versão dos HTML/PDF.

## O que foi efetivamente comparado

- Conteúdo atual do HTML na versão 1 do arquivo persistente, correspondente à edição editorial v2.
- Apostila teórica DD: sumário e relação inicial de normas/súmulas, PDF pp. 3–5; capítulo 1, pp. 5–13, até o início de Enciclopédia das Ciências Penais.
- Apostila antiga: pp. 5–7, nos assuntos correspondentes.
- DD Legis CP: pp. 3–4 e 6–8, com inspeção visual da p. 3.
- Gran Ciências Penais: pp. 4–9; inspeção visual da p. 7. Gran Princípios: inspeção visual da p. 6.
- Passo Estratégico: trechos indexados de amostras oficiais de Direito Penal PF e PC-SP e página oficial da aula demonstrativa PC-PR 2026. O download integral da amostra atual retornou bloqueio para acesso automatizado; não foi lido integralmente. A amostra indexada mostra perguntas de definição, distinção, fundamento e aplicação e explica o uso da autoexplicação para conectar pontos. Não se afirma que todas as perguntas do produto sejam longas ou agrupadas.

## Falhas demonstradas

| Falha | Evidência | Correção de método |
|---|---|---|
| Recorte incompleto usado como unidade didática | O capítulo 1 contém conceito, características, objeto, evolução, funções e classificações. A v2 contém apenas os três primeiros e uma passagem posterior de princípios | A unidade de edição deve partir do capítulo inteiro e de seus pré-requisitos; assuntos retirados da sequência precisam de destino explícito |
| Perda de conexão explicativa | O bloco dd-04 explica que os quatro autores trazem definições formais centradas na lei e na sanção. Foi tratado como introdução editorial removível | Restaurar essa explicação na reconstrução. A referência bibliográfica pode ficar discreta; a relação conceitual deve permanecer no texto |
| Verificação circular | O verificador confere apenas `display_passages`, uma lista gerada pelo próprio editor. dd-04 tinha lista vazia e passava no teste | O resultado passa a dizer apenas que os trechos declarados estão presentes. Não certifica preservação semântica, completude ou clareza |
| Hierarquia que promete mais do que explica | “Direito Penal e Direito Criminal” recebeu subtítulo próprio, mas contém apenas nota de preferência terminológica e CF 22, I, tal como a nota curta da origem | Desenvolver uma distinção só quando há conteúdo e necessidade; não transformar toda dica em um assunto autônomo |
| Comparação quebrada em perguntas isoladas | R07–R10 fragmentam autores; R11–R13 separam aspectos que devem ser contrastados | Organizar revisão por núcleos de compreensão, com pergunta principal, desdobramentos relacionados e resposta explicada |
| Critérios exibidos como palavras avulsas | “Elementos essenciais: princípios · regras · crime...” não explica relações nem como avaliar a resposta | A resposta de revisão deve ser uma explicação legível. Eventuais critérios de correção ficam em linguagem completa e fora da leitura principal |
| Integração insuficiente com Legis | CP 32/96 e CF 22, I foram inseridos; a relação de normas/súmulas das pp. 4–5 e os esquemas pertinentes do Legis não receberam cotejo completo | Mapear norma, explicação, exceção e questão ao assunto correspondente; proximidade no arquivo não basta para integrar |
| Destaque automático sem leitura semântica | `construir.py` utiliza uma lista global de termos e expressão regular | Marcar por passagem o que exerce papel de conceito, critério, distinção, exceção, autor, corrente, marco histórico e fundamento legal |
| Ampliação de perguntas sem demonstração de utilidade | A v2 aumentou de 18 para 30 perguntas sem validação pedagógica ou de prova | Quantidade de perguntas, tabelas, páginas ou blocos é inventário, não evidência de aprendizagem |

A fonte normalizada do capítulo 1 contém aproximadamente 3.423 palavras: 575 em conceito, 227 em características, 212 em objeto, 821 em evolução, 1.147 em funções e 441 em classificações. São contagens de extração, não uma métrica de qualidade. Elas evidenciam o tamanho do conteúdo do próprio capítulo que ficou fora da entrega; o aprofundamento das pp. 26–29 não substitui essas partes.

## Resposta precisa à dúvida sobre cortes

A v2 não resumiu sistematicamente as definições dos trechos a–c: várias foram transpostas integralmente. Houve, porém, seleção restrita do conteúdo, redução nas respostas de revisão e pelo menos uma supressão de conexão conceitual demonstrada (dd-04). Portanto, a afirmação ampla de que a substância estava preservada foi mais forte que a verificação disponível. A auditoria mecânica anterior não autoriza negar a percepção de incompletude do usuário.

“Sanção penal” como gênero, com penas e medidas de segurança como espécies, consta das duas referências fornecidas. A pergunta não é necessariamente incorreta no conteúdo; é insuficiente como bloco de ensino quando exige uma classificação sem explicar seus termos e relações. Não transformar objeção pedagógica em falsa correção jurídica.

## Modelo de revisão agrupada: exemplo autoral

### Núcleo — três perspectivas do Direito Penal

**Pergunta:** Como o Direito Penal é compreendido nos aspectos formal, material e sociológico? Explique o que cada perspectiva observa e por que elas se complementam.

**Resposta explicada:**

- **Aspecto formal ou estático:** observa o Direito Penal como conjunto de normas. Essas normas qualificam comportamentos como infrações penais, definem seus agentes e estabelecem as sanções aplicáveis. O foco recai sobre a estrutura normativa: infração, sujeito e consequência jurídica.
- **Aspecto material:** considera o conteúdo daquilo que é criminalizado. Refere-se a comportamentos altamente reprováveis ou danosos que atingem bens jurídicos indispensáveis à conservação e ao desenvolvimento da sociedade. O foco recai sobre a relevância do interesse protegido e a gravidade da ofensa.
- **Aspecto sociológico ou dinâmico:** considera a atuação do Direito Penal na sociedade. Ele integra os instrumentos de controle social dos comportamentos desviados, buscando preservar a disciplina necessária à convivência. O foco recai sobre a função social desse conjunto de normas.

As perspectivas se complementam porque examinam o mesmo objeto por ângulos diferentes: a estrutura das normas, o conteúdo que justifica a tutela penal e a função exercida na convivência social.

**Desdobramento de revisão:** Ao ler uma definição, identifique se ela enfatiza a norma e a sanção, os bens jurídicos atingidos ou o controle social. Explique o motivo da classificação; reconhecer apenas a palavra do título não encerra a resposta.

Este exemplo é autoral, baseado nas passagens fornecidas; não é transcrição do Passo Estratégico nem substitui a exposição teórica do capítulo. A quantidade final de núcleos depende dos assuntos e relações, e não de uma meta de cartões.

## Direção da reconstrução

Apostila teórica completa como base de trabalho; exposição contínua e suficiente para aprender; tabelas para relações comparáveis; dispositivos e entendimentos no assunto pertinente; perguntas agrupadas após a exposição; questões oficiais com comentário ligado à explicação. Retomadas curtas entre parênteses explicam um termo necessário no ponto de uso, sem frases artificiais de comando.

A próxima edição precisa conferir conteúdo, sequência e compreensão, além da montagem dos arquivos. Trabalhar por capítulo delimitado não exige fechar o curso inteiro antes de editar, mas entregar um recorte não pode ser apresentado como cobertura do capítulo. Atualização jurídica e análise de questões continuam necessárias e não foram concluídas por este diagnóstico.

## Fontes externas de formato

- Página oficial com aula demonstrativa: https://www.estrategiaconcursos.com.br/curso/pc-pr-agente-de-policia-judiciaria-passo-estrategico-de-direito-penal-2026-pos-edital/
- Amostras oficiais indexadas: PF, Eduardo Alberi, curso 316555, aula 00; PC-SP, Telma Vieira, curso 327408, aula 00. Uso limitado ao trecho de questionário retornado pela pesquisa; não copiar conteúdo integral nem declarar leitura integral.
