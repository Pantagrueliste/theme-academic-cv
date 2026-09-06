---
title: tei-mcp
summary: Un servidor MCP que ayuda a los agentes de IA a leer y escribir XML TEI válido, con 16 herramientas para consultar elementos, resolver atributos, expandir modelos de contenido, validar el anidamiento, validar documentos y personalizar el esquema mediante ODD.
tags:
  - XML
  - TEI
  - Humanidades digitales
  - Python
  - MCP
  - IA

date: "2026-03-15T00:00:00Z"

external_link: ""

image:
  caption: Pantalla de inicio de tei-mcp
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

## tei-mcp: TEI P5 para agentes de IA

tei-mcp es un servidor [MCP](https://modelcontextprotocol.io) de código abierto que da a los asistentes de programación con IA acceso directo a la especificación [TEI P5](https://tei-c.org/guidelines/). En lugar de fiarse de lo que memorizó durante el entrenamiento —fuente frecuente de marcado plausible pero incorrecto—, la IA puede consultar la especificación en tiempo real.

## Funciones

El servidor analiza el ODD de TEI P5 y expone 16 herramientas:

- **Consultar** cualquier elemento, clase, macro o módulo por su nombre, sin distinguir mayúsculas de minúsculas y con sugerencias en caso de errata
- **Resolver atributos** a lo largo de toda la jerarquía de clases de la TEI (locales y heredados)
- **Expandir modelos de contenido** en árboles estructurados, con resolución de clases y macros
- **Validar el anidamiento**: relación directa padre-hijo o alcanzabilidad recursiva, con seguimiento de la ruta
- **Validar documentos** contra TEI P5: modelos de contenido, atributos, listas cerradas de valores, integridad de las referencias y avisos de obsolescencia
- **Validar elementos sueltos** para flujos de edición incremental
- **Cargar personalizaciones ODD** que restringen el esquema al subconjunto propio de un proyecto
- **Buscar** en todos los tipos de entidades con expresiones regulares

## Instalación

```bash
pip install tei-mcp
```

O ejecútelo directamente con:

```bash
uvx tei-mcp
```

## Uso

Añádalo a cualquier cliente compatible con MCP (Claude, Cursor, Windsurf, etc.):

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

El código fuente y la documentación están en el [repositorio de GitHub](https://github.com/Pantagrueliste/tei-mcp).
