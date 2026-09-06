---
title: "tei-mcp v0.3: codificar em TEI sem reescrever a fonte"
subtitle: A composição por intervalos bloqueados torna impossíveis, por construção, as alucinações no corpo do texto

summary: >
  A nova versão do tei-mcp introduz a composição por intervalos bloqueados
  (span-locked composition), um sistema concebido para impedir a classe mais
  nociva de alucinação na codificação TEI assistida por IA: as reescritas
  silenciosas do texto-fonte. O modelo nunca escreve texto de corpo; regista
  etiquetas como posições sobre a fonte, e o compositor recusa-se a devolver
  qualquer TEI cujo conteúdo textual plano difira do original num único byte.

date: "2026-05-05T00:00:00Z"
lastmod: "2026-05-05T00:00:00Z"

draft: false
featured: true
machine_translated: true

authors:
- clement

tags:
- Humanidades digitais
- TEI
- MCP
- IA

categories:
- Humanidades digitais
---

Quando [escrevi pela primeira vez sobre o tei-mcp](/post/tei-mcp/), o objetivo
era impedir os assistentes de IA de alucinar marcação TEI. A ancoragem no
esquema resolveu parte do problema: com acesso direto, por ferramentas, à
especificação P5, o modelo já não tem de adivinhar o que um elemento significa
nem que atributos aceita. O resultado valida.

Mas a alucinação tem duas faces na codificação TEI, e o esquema só apanha uma
delas. Validar contra a especificação diz-nos que a *marcação* está bem
formada. Nada diz sobre o *texto* que essa marcação envolve. E é aí – no
próprio texto – que vivem as alucinações mais nocivas. A composição por
intervalos bloqueados, a grande novidade da v0.3, foi concebida especificamente
para as impedir.

{{< toc >}}

## A alucinação que o esquema não apanha

Peça-se a um modelo que codifique uma carta francesa do século XVI e
receber-se-á muitas vezes um documento TEI de aspeto impecável. O cabeçalho
está preenchido, as etiquetas `<persName>` estão bem colocadas, o `<dateline>`
está bem formado. Passe-se pelo `validate_document` e ele passa.

Compare-se depois o corpo com a fonte.

`mesme` passou a `même`. Uma vírgula mudou de sítio. `luy` foi silenciosamente
modernizado em `lui`. Uma oração de leitura difícil no manuscrito foi
«corrigida» para algo mais limpo. Nenhuma destas alterações foi pedida. Nenhuma
é assinalada. O documento é válido segundo o esquema e está discretamente
errado.

Para um fluxo de trabalho de arquivo – em que o texto codificado se torna o
registo permanente de que dependem leitores, índices de pesquisa e citações –
é este o modo de falha que mais importa. Uma etiqueta malformada é um incómodo.
Uma grafia modernizada de que ninguém dá conta durante cinco anos é uma
corrupção.

## A composição por intervalos bloqueados

A nova versão (v0.3) traz um mecanismo de prevenção de alucinações apontado
diretamente a este modo de falha. O objetivo de design é tornar as alucinações
no corpo do texto impossíveis por construção, e não apenas improváveis.

A ideia é simples: **o modelo nunca escreve texto de corpo**.

Em vez disso, o fluxo de trabalho é o seguinte:

1. O modelo chama `get_source("letter_001")` e recebe o texto simples da fonte
   como cadeia imutável.
2. Para cada etiqueta que queira aplicar, chama
   `tag_span("letter_001", start, end, element_path, attrs)` – registando um
   elemento TEI sobre um intervalo de caracteres da fonte.
3. Quando termina, chama `compose("letter_001")`. O servidor intercala as
   etiquetas registadas com o texto simples original, gera o TEI final e
   verifica depois, *byte a byte*, que o conteúdo textual plano do documento
   gerado é igual à fonte.

Se os bytes coincidem, o documento é devolvido. Se não coincidem – se as
etiquetas do modelo implicarem de algum modo um corpo que difere da fonte num
único caráter que seja –, `compose()` lança uma exceção em vez de devolver um
documento corrompido.

Não há caminho, neste fluxo de trabalho, em que o modelo produza um documento
TEI cujo corpo difira da fonte. O invariante é mecânico, não comportamental.
Não é preciso confiar que o modelo não alucina; basta confiar numa comparação
`==` entre duas cadeias de bytes.

## O que isto é, e o que não é

A composição por intervalos bloqueados é **complementar** da ancoragem no
esquema; não a substitui. As ferramentas de ancoragem no esquema
(`validate_document`, `lookup_element`, `valid_children` e as restantes das
dezasseis originais) ajudam o modelo a produzir TEI *válida*. A composição por
intervalos bloqueados garante que o corpo do texto dentro dessa TEI é *fiel* à
fonte. Um fluxo de codificação que se possa pôr em produção tem de satisfazer
os dois eixos, e agora ambos ficam cobertos por um único servidor.

Também não é uma varinha mágica para tudo. `compose()` ainda não verifica se as
etiquetas registadas são admissíveis segundo uma personalização ODD carregada –
fica para uma próxima versão. As etiquetas registadas vivem na memória do
processo e não sobrevivem a um reinício. E os ficheiros-fonte têm de ser
legíveis a partir de onde quer que o servidor corra. Tudo isto tem solução;
nada disto abala o invariante central.

## Porque é que isto importa para lá da TEI

O padrão generaliza-se. Sempre que se pede a um modelo que anote, transforme ou
envolva um pedaço de texto – e sempre que a integridade do texto subjacente
importa mais do que a capacidade do modelo para o «melhorar» –, aplica-se a
mesma forma de solução. Não peça ao modelo que reescreva o texto. Peça-lhe que
produza instruções sobre o texto, e deixe que um compositor determinista as
aplique sob um invariante de igualdade.

Para as edições digitais em particular, isto muda o que se pode pedir a um
modelo com responsabilidade. A codificação torna-se de repente uma tarefa
delegável sem ter de comparar à mão cada resultado com a fonte. A máquina faz
o caminho enfadonho; o editor revê a marcação, não a ortografia.

## Obter a atualização

Se já tem o tei-mcp instalado:

```bash
uvx tei-mcp@latest
```

Ou de raiz:

```bash
pip install tei-mcp
```

Para usar a composição por intervalos bloqueados, aponte o servidor para uma
diretoria de ficheiros-fonte em texto simples:

```bash
export TEI_MCP_SPAN_SOURCE_ROOT=/path/to/sources
uvx tei-mcp
```

O radical do nome de cada ficheiro passa a ser o seu identificador de documento
(`letter_001.txt` → `letter_001`).

Código-fonte, documentação completa e notas de design do invariante:
[github.com/Pantagrueliste/tei-mcp](https://github.com/Pantagrueliste/tei-mcp)
