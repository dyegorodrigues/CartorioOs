# Comparação Claude V1/V2 — checkpoint

Data: 03/10/2026. Relatório para o usuário: `Comparacao_DD_Claude_V1_V2.md`, Library `libfile_b8d422c50680819185c36803fa06f35b`, versão 0.

## Fontes

- V1: `DP-01 Nocoes Iniciais e Principios.html`, Library `libfile_8c8d72f1ed908191b2021ca9c0753c8b`.
- V2: `DP-01 v2 Nocoes Iniciais e Principios.html`, Library `libfile_64a73c3867548191b7b363d465339238`.
- Screenshot: `Screenshot_20261003-131711.png`, Library `libfile_e55916fcbb608191a79b49d4900d707b`.
- DD teórico 58 páginas, Library `libfile_a7f350fc59808191826c927e0d43d228`.

## Evidência e decisões

1. A edição anterior do Codex v3 (pp. 5–13 e 26–29) é um recorte. Os HTMLs trazidos já organizam o percurso da apostila inteira. O produto pretendido é a apostila inteira, editada por capítulos e com teoria como leitura central.
2. Comparação automática da área teórica: V1 `p-teoria`, V2 `p-apostila`, contra páginas 5–58. Normalização de caixa, acentos, pontuação e remoção de rodapés/cabeçalhos; presença de sequências contíguas de 8 palavras. Correspondência literal ponderada: V1 14,9%, V2 93,7%. Isso NÃO é cobertura semântica; não reproduz nem valida a alegação da screenshot de 1.062/1.085 frases e 23 diferenças resolvidas.
3. Conferência manual: V1 condensa introdução/evolução/escolas; V2 preserva parágrafos. V1 escolas compara base/crime/pena/autores; V2 usa escola/texto da apostila. Restaurar comparação por critérios mantendo explicações.
4. Área teórica: V1/V2 com 69/38 tabelas, 549/833 elementos b/strong. Classes vm/az/h: V1 95/25/36; V2 8/0/0. V2 não perdeu negrito em geral; reduziu variedade de destaques internos. Não considerar quantidade um indicador isolado de qualidade.
5. Arrays de treino Q: 37/46 registros. Revisão P: 50/80 perguntas. V2 reúne ambos ao fim de capítulos via fillRev(). Primeira P é sobre súmulas de insignificância; corrigir progressão global. Revisar perguntas por coerência e cobertura, não por número fixo.
6. Gran: complementos de sujeito passivo imediato/mediato e momentos da individualização aparecem na V1 e não se mantêm como exposições equivalentes na V2. Usuário permite complementação explicativa pertinente; não limitar Gran a cores nem substituir DD por síntese.
7. DD Juris: números de julgados não provam preservação integral das condições e ressalvas. Cotejo semântico completo pendente. DD Súmulas abrange tópicos futuros: não inserir tudo em introdução nem classificar todo trecho ausente como perda.
8. PC/CE 2025 Q22: V2 diz prova completa, mas alternativas reordenadas e uma encurtada; resposta B corresponde ao E oficial. Não é erro de escolha da proposição correta; é falha de fidelidade/proveniência. Prova e gabarito oficiais novamente abertos: https://cdn.cebraspe.org.br/concursos/PC_CE_25_DELEGADO/arquivos/084_PC_CE_001_01.pdf e https://cdn.cebraspe.org.br/concursos/PC_CE_25_DELEGADO/arquivos/Gab_Definitivo_084_PC_CE_001_01.pdf .
9. Ambas sem persistência local/remota de progresso e sem CSS/eventos próprios de impressão. IDs únicos e destinos data-go/P/Q existentes no exame estático. Nenhum navegador disponível para QA visual nesta rodada; não certificar UX ou PDF.
10. Preservar correções documentadas da nossa edição ao reconciliar conteúdo; não reintroduzir erro por copiar a V2. Original dos HTMLs não alterado. Nova edição não gerada. V3 Claude ainda não recebida. GitHub autorizado; conteúdo continua não aprovado.

## Referências de questionário efetivamente lidas

- E-book público oficial: https://gratis.estrategiaconcursos.com.br/wp-content/uploads/2022/04/E-book_questionario_de_revisao_ativa_escrivao.pdf . Seção Penal, PDF p. 37–38 (índices 36–37), resposta com distinções e aprofundamento comparativo.
- Prévia de questionário de noções iniciais: https://pt.scribd.com/document/1071637900/Curso-228971-Aula-00-Somente-Em-PDF-9ad7-Completo . Lido por formato, não como validação de Direito vigente.

## Próxima execução

Inventariar fonte completa; editar teoria por capítulo preservando explicações; recuperar recursos V1 úteis; inserir Legis/Juris no tópico; elaborar revisão progressiva; conferir originais das questões; implementar persistência e saída impressa; testar visualmente. Não aumentar arquitetura ou coletar todo o universo de provas como pré-condição para editar um capítulo. Não declarar integralidade com uma métrica mecânica.
