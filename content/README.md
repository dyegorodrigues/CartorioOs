# Conteúdo modular do Tutor OS

Estado: estrutura editorial implementada; sete capítulos planejados de DP-01, ainda sem novo texto ou perguntas aprovadas.

`catalog.json` é o índice. Cada entrada aponta para um `module.json` separado. O módulo registra tópicos, fontes, pré-requisitos e o caminho do texto editável e das perguntas. `sources.json` guarda metadados públicos; os arquivos originais ficam no Drive. `research_candidates.json` organiza Brainscape/Passo por módulo. `law_registry.json` receberá dispositivos versionados.

O índice não contém o texto inteiro. O pacote de saída preserva um arquivo por módulo, permitindo carregamento sob demanda. Um módulo pode se dividir quando for editorialmente necessário, mantendo IDs dos tópicos e remissões. Não criar uma página para cada frase nem cortar a explicação apenas para reduzir o tamanho do arquivo.

## Operação

```bash
python scripts/validate_modular.py
python -m unittest discover -s tests -p 'test_modular.py'
python scripts/build_modular.py --output dist/modular
```

O build gera `manifest.json` e arquivos por módulo. Texto HTML, quando produzido, fica separado e é copiado ao pacote. Questões estão em JSONL por módulo e são ligadas pelos IDs dos tópicos. Não há interface de estudo, exportador PDF ou progresso persistente implementados nesta rodada. A arquitetura prevê essas apresentações sobre a mesma fonte editorial.

## Editar um capítulo

1. Completar a matriz de tópicos e associar fontes/páginas. Candidatos ainda não auditados não são cobertura certificada.
2. Escrever `reading.html` no diretório do módulo e informar `reading_file`. Usar parágrafos, títulos, listas e tabelas sem scripts próprios; apresentação compartilhada virá na camada de leitura/impressão.
3. Registrar perguntas conforme `QUESTION_CONTRACT.md`; adicionar dispositivos literais conferidos ao registro de lei.
4. Conferir o conteúdo jurídico e pedagógico. Só então informar a data e promover o estado editorial. A validação estrutural não faz essa promoção.
5. Reexecutar validação e build. Mudança na base de uma pergunta revisada exige atualizar a revisão ou marcar `needs_review`.

O PDF poderá ser gerado por capítulo e por apostila montada na ordem do catálogo. Não manter cópias divergentes de uma mesma explicação em HTML, DOCX e banco de perguntas. O DOCX é exportação opcional.

## Dados pessoais

Não adicionar PDFs originais, links privados do Drive, credenciais, notas pessoais ou desempenho individual nesta árvore pública. A fila de estudo e os eventos de aprendizagem pertencem a uma camada privada futura, ligada pelos mesmos IDs.
