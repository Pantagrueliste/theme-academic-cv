---
title: Multi-Saxon
summary: Una herramienta de alto rendimiento para transformaciones XSLT 2.0/3.0 en paralelo de grandes corpus XML TEI, capaz de ejecutar transformaciones que LXML no puede procesar.
tags:
  - XSLT
  - XML
  - TEI
  - Humanidades digitales
  - Python
  - Java
  - Rendimiento

date: "2025-03-28T00:00:00Z"

# Optional external URL for project (replaces project detail page)
external_link: ""

image:
  caption: Multi-Saxon en acción
  focal_point: Smart

links:
  - type: code
    icon: brands/github
    label: Code
    url: https://github.com/Pantagrueliste/multi-saxon
url_code: ""
url_pdf: ""
url_slides: ""
url_video: ""

# Slides (optional).
#   Associate this project with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides = "example-slides"` references `content/slides/example-slides.md`.
#   Otherwise, set `slides = ""`.
slides: ""
machine_translated: true
---

## Multi-Saxon: procesamiento XSLT en paralelo para grandes corpus TEI

Multi-Saxon cubre una laguna importante entre las herramientas de procesamiento XML al permitir la ejecución en paralelo de transformaciones XSLT 2.0 y 3.0 que LXML (una biblioteca XML muy utilizada en Python) no puede manejar. Diseñado específicamente para grandes colecciones de documentos XML TEI, Multi-Saxon acelera considerablemente el tiempo de procesamiento mediante una ejecución paralela eficiente.

## Características principales

- **Compatibilidad avanzada con XSLT**: procesa transformaciones XSLT 2.0 y 3.0, más allá de las capacidades de LXML
- **Procesamiento en paralelo**: reduce drásticamente el tiempo de transformación de grandes colecciones de documentos mediante la paralelización
- **Optimizado para TEI**: diseñado específicamente para documentos XML de la Text Encoding Initiative (TEI)
- **Rendimiento escalable**: maneja con eficacia corpus que van de cientos a miles de documentos
- **Multiplataforma**: funciona en distintos sistemas operativos y entornos

## El problema que resuelve Multi-Saxon

Los investigadores en humanidades digitales que trabajan con TEI suelen enfrentarse a dos retos importantes:

1. LXML (una biblioteca habitual de procesamiento XML en Python) solo admite XSLT 1.0, lo que impide utilizar las funciones más avanzadas de XSLT 2.0/3.0
2. Procesar secuencialmente grandes corpus de documentos TEI puede llevar un tiempo prohibitivo

Multi-Saxon aborda ambos problemas aprovechando las capacidades XSLT avanzadas de Saxon y distribuyendo el procesamiento entre varios núcleos, con ganancias de rendimiento significativas.

## Implementación

Multi-Saxon combina Python con el procesador Saxon de Java para crear una cadena de transformación de alto rendimiento:

- Utiliza la biblioteca Saxon de Java para un procesamiento XSLT 2.0/3.0 robusto
- Implementa el multiprocesamiento para distribuir las transformaciones entre los núcleos de CPU disponibles
- Gestiona con eficiencia los grupos de procesadores para maximizar el rendimiento
- Ofrece una interfaz sencilla para el procesamiento por lotes de documentos TEI

## Ejemplo de uso

```python
from multi_saxon import MultiSaxon

# Initialize with your XSLT stylesheet
transformer = MultiSaxon("transform.xsl")

# Transform a single document
transformer.transform("input.xml", "output.xml")

# Transform an entire directory in parallel
transformer.transform_directory("input_dir", "output_dir")
```

## Impacto para las humanidades digitales

Para los proyectos de humanidades digitales que manejan grandes colecciones de documentos TEI, Multi-Saxon hace posible:

- Transformaciones complejas a escala de corpus que serían imposibles con LXML
- Tiempos de procesamiento drásticamente reducidos (a menudo por un factor de 5 a 10 en sistemas multinúcleo)
- Análisis más sofisticados gracias a las funciones avanzadas de XSLT 2.0/3.0
- Un flujo de trabajo simplificado para procesar colecciones enteras de documentos

Encontrará el código fuente y la documentación en el [repositorio de GitHub](https://github.com/Pantagrueliste/multi-saxon).
