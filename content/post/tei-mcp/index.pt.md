---
title: "tei-mcp: a TEI P5 ao alcance dos agentes de IA"
subtitle: Um servidor MCP que ajuda os assistentes de IA a compreender as Guidelines da TEI

summary: >
  O tei-mcp é um servidor MCP de código aberto que dá aos assistentes de programação
  por IA acesso direto à especificação TEI P5 – consulta de elementos, resolução de
  atributos, validação do aninhamento, validação de documentos e personalização ODD.

date: "2026-03-15T00:00:00Z"
lastmod: "2026-03-15T00:00:00Z"

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

Quem já tenha usado um assistente de programação por IA para escrever XML TEI 
terá reparado que ele se engana. Aparecem elementos onde não deviam. 
Inventam-se atributos. Ignoram-se as regras de aninhamento. O modelo tem uma 
ideia vaga do aspeto da TEI, mas nenhum conhecimento fiável da especificação.

O tei-mcp resolve o problema dando aos agentes de IA acesso direto, por meio de 
ferramentas, às Guidelines da TEI P5.

{{< toc >}}

## O que é o MCP?

O [Model Context Protocol](https://modelcontextprotocol.io) (MCP) é uma norma 
aberta que permite às aplicações de IA ligar-se a fontes de dados e ferramentas 
externas. Pense-se nele como uma porta USB para a IA: um protocolo único que 
permite a qualquer cliente compatível – Claude, Cursor, Windsurf e outros – 
ligar-se a serviços especializados.

Um servidor MCP expõe *ferramentas* que a IA pode invocar durante uma conversa. 
Em vez de se fiar em dados de treino memorizados, o modelo pode consultar uma 
fonte viva e autorizada.

## O que faz o tei-mcp

O tei-mcp analisa a especificação ODD da TEI P5 e expõe 16 ferramentas que 
cobrem as perguntas mais frequentes de um editor ou codificador:

- **O que é este elemento?** Consultar qualquer elemento, classe, macro ou 
  módulo pelo nome, sem distinção de maiúsculas e com sugestões em caso de gralha.
- **Que atributos aceita?** Resolver os atributos ao longo de toda a hierarquia 
  de classes – primeiro os locais, depois os herdados, por ordem.
- **O que pode conter?** Expandir os modelos de conteúdo em árvores 
  estruturadas, ou obter uma lista simples dos filhos válidos.
- **Este elemento pode ir aqui?** Verificar o aninhamento pai-filho, ou seguir 
  a acessibilidade através de toda a hierarquia de elementos.
- **O meu documento é válido?** Validar um ficheiro XML TEI contra a 
  especificação: modelos de conteúdo, valores de atributos, listas fechadas de 
  valores, integridade das referências e avisos de depreciação.
- **E o esquema do meu projeto?** Carregar um ficheiro de personalização ODD 
  para restringir tudo o que precede ao subconjunto de TEI próprio do seu projeto.

## Porque é que isto importa

Codificar em TEI exige consultar as Guidelines a toda a hora. Os codificadores 
experientes interiorizam os padrões mais comuns, mas até eles têm de verificar 
a especificação quando se trata de elementos menos familiares ou de modelos de 
conteúdo complexos. Para os assistentes de IA, que não têm esse conhecimento 
interiorizado, o problema é pior: alucinam marcação de aspeto plausível, mas 
incorreta.

Com o tei-mcp, a IA não tem de adivinhar. Pode procurar a resposta na 
especificação antes de escrever um único parêntese angular. O resultado é 
marcação conforme à TEI P5 – ou à personalização ODD do seu projeto.

## Primeiros passos

Instale a partir do PyPI:

```bash
pip install tei-mcp
```

Depois, acrescente-o à configuração do seu cliente MCP:

```json
{
  "mcpServers": {
    "tei": {
      "command": "uvx",
      "args": ["tei-mcp"]
    }
  }
}
```

O servidor descarrega a especificação TEI na primeira execução e funciona com 
qualquer cliente compatível com MCP.

Código-fonte e documentação completa: 
[github.com/Pantagrueliste/tei-mcp](https://github.com/Pantagrueliste/tei-mcp)
