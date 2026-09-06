---
title: "tei-mcp: TEI P5 para agentes de IA"
subtitle: Un servidor MCP que ayuda a los asistentes de IA a entender las directrices de la TEI

summary: >
  tei-mcp es un servidor MCP de código abierto que da a los asistentes de
  programación con IA acceso directo a la especificación TEI P5: consulta de
  elementos, resolución de atributos, validación de anidamiento, validación de
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

Si alguna vez ha utilizado un asistente de programación con IA para escribir 
XML TEI, probablemente habrá notado que se equivoca. Aparecen elementos donde 
no deberían. Se inventan atributos. Se ignoran las reglas de anidamiento. El 
modelo tiene una idea aproximada de qué aspecto tiene la TEI, pero ningún 
conocimiento fiable de la especificación.

tei-mcp resuelve este problema dando a los agentes de IA acceso directo, a través 
de herramientas, a las directrices TEI P5.

{{< toc >}}

## ¿Qué es MCP?

El [Model Context Protocol](https://modelcontextprotocol.io) (MCP) es un 
estándar abierto que permite a las aplicaciones de IA conectarse a fuentes de 
datos y herramientas externas. Piense en él como un puerto USB para la IA: un 
único protocolo que permite a cualquier cliente compatible —Claude, Cursor, 
Windsurf y otros— conectarse a servicios especializados.

Un servidor MCP expone *herramientas* que la IA puede invocar durante una 
conversación. En lugar de depender de los datos de entrenamiento memorizados, 
el modelo puede consultar una fuente viva y autorizada.

## Qué hace tei-mcp

tei-mcp analiza la especificación ODD de TEI P5 y expone 16 herramientas que 
cubren las preguntas más habituales que se haría un editor o codificador:

- **¿Qué es este elemento?** Consulte cualquier elemento, clase, macro o módulo 
  por su nombre, sin distinción entre mayúsculas y minúsculas y con sugerencias 
  en caso de errata.
- **¿Qué atributos admite?** Resuelva los atributos a lo largo de toda la 
  jerarquía de clases: primero los atributos locales, luego los heredados, en orden.
- **¿Qué puede ir dentro?** Expanda los modelos de contenido en árboles 
  estructurados, u obtenga una lista plana de hijos válidos.
- **¿Puede ir aquí este elemento?** Compruebe el anidamiento padre-hijo, o 
  rastree la alcanzabilidad a través de toda la jerarquía de elementos.
- **¿Es válido mi documento?** Valide un archivo XML TEI contra la 
  especificación: modelos de contenido, valores de atributos, listas cerradas de 
  valores, integridad de las referencias y avisos de obsolescencia.
- **¿Y el esquema de mi proyecto?** Cargue un archivo de personalización ODD 
  para restringir todo lo anterior al subconjunto específico de TEI de su proyecto.

## Por qué importa

La codificación TEI exige consultar constantemente las directrices. Los 
codificadores experimentados interiorizan los patrones más comunes, pero incluso 
ellos necesitan comprobar la especificación para los elementos menos familiares 
o los modelos de contenido complejos. Para los asistentes de IA, que carecen de 
ese conocimiento interiorizado, el problema es peor: alucinan un marcado de 
apariencia plausible pero incorrecto.

Con tei-mcp, la IA no tiene que adivinar. Puede buscar la respuesta en la 
especificación antes de escribir un solo paréntesis angular. El resultado es un 
marcado conforme a TEI P5, o a la personalización ODD de su proyecto.

## Primeros pasos

Instálelo desde PyPI:

```bash
pip install tei-mcp
```

A continuación, añádalo a la configuración de su cliente MCP:

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

El servidor descarga la especificación TEI en la primera ejecución y funciona 
con cualquier cliente compatible con MCP.

Código fuente y documentación completa: 
[github.com/Pantagrueliste/tei-mcp](https://github.com/Pantagrueliste/tei-mcp)
