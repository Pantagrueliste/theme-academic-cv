---
title: tei-mcp
summary: Um servidor MCP que ajuda os agentes de IA a ler e escrever XML TEI válido, com 16 ferramentas que cobrem a consulta de elementos, a resolução de atributos, a expansão de modelos de conteúdo, a validação do aninhamento, a validação de documentos e a personalização ODD.
tags:
  - XML
  - TEI
  - Humanidades digitais
  - Python
  - MCP
  - IA

date: "2026-03-15T00:00:00Z"

external_link: ""

image:
  caption: Ecrã de arranque do tei-mcp
  focal_point: Smart

links:
  - type: code
    icon: brands/github
    label: Código
    url: https://github.com/Pantagrueliste/tei-mcp
  - type: site
    icon: brands/python
    label: PyPI
    url: https://pypi.org/project/tei-mcp/
url_code: ""
url_pdf: ""
url_slides: ""
url_video: ""

slides: ""
machine_translated: true
---

## tei-mcp: a TEI P5 ao alcance dos agentes de IA

O tei-mcp é um servidor [MCP](https://modelcontextprotocol.io) de código aberto que dá aos assistentes de programação por IA acesso direto à especificação [TEI P5](https://tei-c.org/guidelines/). Em vez de se fiar em dados de treino memorizados – o que produz muitas vezes marcação plausível, mas incorreta –, a IA pode consultar a especificação em tempo real.

## Funcionalidades

O servidor analisa a ODD da TEI P5 e expõe 16 ferramentas:

- **Consultar** qualquer elemento, classe, macro ou módulo pelo nome, sem distinção de maiúsculas e com sugestões em caso de gralha
- **Resolver atributos** ao longo de toda a hierarquia de classes da TEI (locais + herdados)
- **Expandir modelos de conteúdo** em árvores estruturadas, com resolução de classes e macros
- **Validar o aninhamento** – relação direta pai-filho ou acessibilidade recursiva, com registo do caminho
- **Validar documentos** contra a TEI P5: modelos de conteúdo, atributos, listas fechadas de valores, integridade das referências e avisos de depreciação
- **Validar elementos isolados** para fluxos de edição incremental
- **Carregar personalizações ODD** para restringir o esquema a um subconjunto específico do projeto
- **Pesquisar** em todos os tipos de entidade com expressões regulares

## Instalação

```bash
pip install tei-mcp
```

Ou executar diretamente com:

```bash
uvx tei-mcp
```

## Utilização

Acrescente-o a qualquer cliente compatível com MCP (Claude, Cursor, Windsurf, etc.):

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

O código-fonte e a documentação estão no [repositório GitHub](https://github.com/Pantagrueliste/tei-mcp).
