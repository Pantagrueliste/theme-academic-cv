---
title: "tei-mcp: TEI P5 for AI Agents"
subtitle: An MCP server that helps AI assistants understand the TEI Guidelines

summary: >
  tei-mcp is an open-source MCP server that gives AI coding assistants 
  direct access to the TEI P5 specification — element lookup, attribute 
  resolution, nesting validation, document validation, and ODD customisation.

date: "2026-03-15T00:00:00Z"
lastmod: "2026-03-15T00:00:00Z"

draft: false
featured: true

authors:
- clement

tags:
- Digital Humanities
- TEI
- MCP
- AI

categories:
- Digital Humanities
---

If you've ever used an AI coding assistant to write TEI XML, you've probably 
noticed that it gets things wrong. Elements appear where they shouldn't. 
Attributes are invented. Nesting rules are ignored. The model has a rough sense 
of what TEI looks like, but no reliable knowledge of the specification.

tei-mcp solves this by giving AI agents direct, tool-based access to the TEI 
P5 Guidelines.

{{< toc >}}

## What is MCP?

The [Model Context Protocol](https://modelcontextprotocol.io) (MCP) is an open 
standard that allows AI applications to connect to external data sources and 
tools. Think of it as a USB port for AI: a single protocol that lets any 
compatible client — Claude, Cursor, Windsurf, and others — plug into 
specialised services.

An MCP server exposes *tools* that the AI can call during a conversation. 
Instead of relying on memorised training data, the model can query a live, 
authoritative source.

## What tei-mcp does

tei-mcp parses the TEI P5 ODD specification and exposes 16 tools that cover 
the most common questions an editor or encoder would ask:

- **What is this element?** Look up any element, class, macro, or module by 
  name, with case-insensitive matching and typo suggestions.
- **What attributes does it take?** Resolve attributes across the full class 
  hierarchy — local attributes first, then inherited ones in order.
- **What can go inside it?** Expand content models into structured trees, 
  or get a flat list of valid children.
- **Can this element go here?** Check parent-child nesting, or trace 
  reachability through the full element hierarchy.
- **Is my document valid?** Validate a TEI XML file against the spec: content 
  models, attribute values, closed value lists, reference integrity, and 
  deprecation warnings.
- **What about my project schema?** Load an ODD customisation file to 
  constrain all of the above to your project's specific subset of TEI.

## Why it matters

TEI encoding requires constant reference to the Guidelines. Experienced 
encoders internalise the most common patterns, but even they need to check 
the spec for less familiar elements or complex content models. For AI 
assistants, which have no such internalised knowledge, the problem is worse: 
they hallucinate plausible-looking but incorrect markup.

With tei-mcp, the AI doesn't have to guess. It can look up the answer in 
the specification before writing a single angle bracket. The result is markup 
that conforms to TEI P5 — or to your project's ODD customisation.

## Getting started

Install from PyPI:

```bash
pip install tei-mcp
```

Then add it to your MCP client's configuration:

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

The server downloads the TEI specification on first run and works with any 
MCP-compatible client.

Source code and full documentation: 
[github.com/Pantagrueliste/tei-mcp](https://github.com/Pantagrueliste/tei-mcp)
