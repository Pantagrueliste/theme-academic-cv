---
title: Multi-Saxon
summary: Una herramienta de alto rendimiento para aplicar en paralelo transformaciones XSLT 2.0/3.0 a grandes corpus XML TEI, incluidas las que LXML no es capaz de procesar.
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
    label: Código
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

## Multi-Saxon: XSLT en paralelo para grandes corpus TEI

Multi-Saxon cubre una laguna importante de las herramientas de procesamiento XML: permite ejecutar en paralelo transformaciones XSLT 2.0 y 3.0 que LXML (una biblioteca XML muy usada en Python) no puede manejar. Pensado para grandes colecciones de documentos XML TEI, Multi-Saxon acorta considerablemente los tiempos de procesamiento gracias a una ejecución paralela eficiente.

## Características principales

- **Compatibilidad avanzada con XSLT**: procesa transformaciones XSLT 2.0 y 3.0, fuera del alcance de LXML
- **Procesamiento en paralelo**: la paralelización reduce drásticamente el tiempo de transformación de grandes colecciones de documentos
- **Optimizado para TEI**: diseñado expresamente para documentos XML de la Text Encoding Initiative (TEI)
- **Rendimiento escalable**: maneja con soltura corpus de cientos o miles de documentos
- **Multiplataforma**: funciona en sistemas operativos y entornos distintos

## El problema que resuelve Multi-Saxon

Quienes trabajan con TEI en humanidades digitales tropiezan a menudo con dos obstáculos:

1. LXML (una biblioteca habitual de procesamiento XML en Python) solo admite XSLT 1.0, lo que deja fuera las funciones más avanzadas de XSLT 2.0/3.0
2. Procesar grandes corpus de documentos TEI uno tras otro puede llevar un tiempo prohibitivo

Multi-Saxon resuelve ambos aprovechando las capacidades XSLT avanzadas de Saxon y repartiendo el trabajo entre varios núcleos, con ganancias de rendimiento notables.

## Implementación

Multi-Saxon combina Python con el procesador Saxon de Java para formar una cadena de transformación de alto rendimiento:

- Usa la biblioteca Saxon de Java para un procesamiento XSLT 2.0/3.0 robusto
- Recurre al multiprocesamiento para distribuir las transformaciones entre los núcleos de CPU disponibles
- Gestiona con eficiencia los grupos de procesos para maximizar el rendimiento
- Ofrece una interfaz sencilla para procesar documentos TEI por lotes

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

## Qué aporta a las humanidades digitales

A los proyectos de humanidades digitales que manejan grandes colecciones de documentos TEI, Multi-Saxon les permite:

- Transformaciones complejas a escala de corpus, imposibles con LXML
- Tiempos de procesamiento drásticamente menores (a menudo entre 5 y 10 veces, en sistemas multinúcleo)
- Análisis más sofisticados gracias a las funciones avanzadas de XSLT 2.0/3.0
- Un flujo de trabajo más simple para procesar colecciones enteras de documentos

El código fuente y la documentación están en el [repositorio de GitHub](https://github.com/Pantagrueliste/multi-saxon).
