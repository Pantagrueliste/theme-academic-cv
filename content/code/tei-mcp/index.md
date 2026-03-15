---
title: tei-mcp
summary: An MCP server that helps AI agents read and write valid TEI XML, with 16 tools covering element lookup, attribute resolution, content model expansion, nesting validation, document validation, and ODD customisation.
tags:
  - XML
  - TEI
  - Digital Humanities
  - Python
  - MCP
  - AI

date: "2026-03-15T00:00:00Z"

external_link: ""

image:
  caption: tei-mcp startup banner
  focal_point: Smart

links:
  - icon: github
    icon_pack: fab
    name: Code
    url: https://github.com/Pantagrueliste/tei-mcp
  - icon: python
    icon_pack: fab
    name: PyPI
    url: https://pypi.org/project/tei-mcp/
url_code: ""
url_pdf: ""
url_slides: ""
url_video: ""

slides: ""
---

## tei-mcp: TEI P5 for AI Agents

tei-mcp is an open-source [MCP](https://modelcontextprotocol.io) server that gives AI coding assistants direct access to the [TEI P5](https://tei-c.org/guidelines/) specification. Instead of relying on memorised training data — which often produces plausible but incorrect markup — the AI can query the specification in real time.

## Features

The server parses the TEI P5 ODD and exposes 16 tools:

- **Lookup** any element, class, macro, or module by name with case-insensitive matching and typo suggestions
- **Resolve attributes** across the full TEI class hierarchy (local + inherited)
- **Expand content models** into structured trees with class and macro resolution
- **Validate nesting** — direct parent-child or recursive reachability with path tracking
- **Validate documents** against TEI P5: content models, attributes, closed value lists, reference integrity, and deprecation warnings
- **Validate single elements** for incremental editing workflows
- **Load ODD customisations** to constrain the schema to a project-specific subset
- **Search** across all entity types with regex patterns

## Installation

```bash
pip install tei-mcp
```

Or run directly with:

```bash
uvx tei-mcp
```

## Usage

Add to any MCP-compatible client (Claude, Cursor, Windsurf, etc.):

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

Find the source code and documentation at the [GitHub repository](https://github.com/Pantagrueliste/tei-mcp).
