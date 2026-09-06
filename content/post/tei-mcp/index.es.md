---
title: "tei-mcp: TEI P5 para agentes de IA"
subtitle: Un servidor MCP para que los asistentes de IA entiendan las directrices de la TEI

summary: >
  tei-mcp es un servidor MCP de código abierto que da a los asistentes de
  programación con IA acceso directo a la especificación TEI P5: consulta de
  elementos, resolución de atributos, validación del anidamiento, validación de
  documentos y personalización mediante ODD.

date: "2026-03-15T00:00:00Z"
lastmod: "2026-03-15T00:00:00Z"

draft: false
featured: true
machine_translated: true

authors:
- clement

tags:
- Humanidades digitales
- TEI
- MCP
- IA

categories:
- Humanidades digitales
---

Quien haya usado un asistente de programación con IA para escribir XML TEI habrá notado, seguramente, que se equivoca: aparecen elementos donde no deben, se inventan atributos, se ignoran las reglas de anidamiento. El modelo tiene una idea aproximada de qué aspecto tiene la TEI, pero ningún conocimiento fiable de la especificación.

tei-mcp resuelve el problema dando a los agentes de IA acceso directo, mediante herramientas, a las directrices TEI P5.

{{< toc >}}

## ¿Qué es MCP?

El [Model Context Protocol](https://modelcontextprotocol.io) (MCP) es un estándar abierto que permite a las aplicaciones de IA conectarse con fuentes de datos y herramientas externas. Piénsese en él como en un puerto USB para la IA: un único protocolo con el que cualquier cliente compatible —Claude, Cursor, Windsurf y otros— puede enchufarse a servicios especializados.

Un servidor MCP expone *herramientas* que la IA puede invocar en mitad de una conversación. En vez de fiarse de lo que memorizó durante el entrenamiento, el modelo consulta una fuente viva y autorizada.

## Qué hace tei-mcp

tei-mcp analiza la especificación ODD de TEI P5 y expone 16 herramientas que responden a las preguntas más frecuentes de un editor o codificador:

- **¿Qué es este elemento?** Consulta de cualquier elemento, clase, macro o módulo por su nombre, sin distinguir mayúsculas de minúsculas y con sugerencias en caso de errata.
- **¿Qué atributos admite?** Resolución de los atributos a lo largo de toda la jerarquía de clases: primero los locales, después los heredados, por orden.
- **¿Qué puede contener?** Expansión de los modelos de contenido en árboles estructurados, o lista plana de los hijos válidos.
- **¿Puede ir aquí este elemento?** Comprobación del anidamiento padre-hijo, o rastreo de la alcanzabilidad a través de toda la jerarquía de elementos.
- **¿Es válido mi documento?** Validación de un archivo XML TEI contra la especificación: modelos de contenido, valores de atributos, listas cerradas de valores, integridad de las referencias y avisos de obsolescencia.
- **¿Y el esquema de mi proyecto?** Carga de un archivo de personalización ODD que restringe todo lo anterior al subconjunto de la TEI propio de su proyecto.

## Por qué importa

Codificar en TEI obliga a consultar las directrices sin descanso. Los codificadores experimentados interiorizan los patrones más comunes, pero hasta ellos tienen que mirar la especificación ante un elemento poco familiar o un modelo de contenido complejo. Para los asistentes de IA, que carecen de ese saber interiorizado, el problema es peor: alucinan un marcado de aspecto plausible pero incorrecto.

Con tei-mcp la IA no tiene que adivinar: puede buscar la respuesta en la especificación antes de escribir un solo paréntesis angular. El resultado es un marcado conforme a TEI P5, o a la personalización ODD de su proyecto.

## Primeros pasos

Instálelo desde PyPI:

```bash
pip install tei-mcp
```

Añádalo después a la configuración de su cliente MCP:

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

El servidor descarga la especificación TEI la primera vez que se ejecuta y funciona con cualquier cliente compatible con MCP.

Código fuente y documentación completa: [github.com/Pantagrueliste/tei-mcp](https://github.com/Pantagrueliste/tei-mcp)
