---
title: persNamer
summary: Una herramienta en Python que convierte identificadores VIAF en entradas de persona y etiquetas de anotación en XML TEI, y agiliza así el control de autoridades en las ediciones críticas digitales.
tags:
  - XML
  - TEI
  - Humanidades digitales
  - Python
  - VIAF
  - Datos enlazados

date: "2025-03-28T00:00:00Z"

# Optional external URL for project (replaces project detail page)
external_link: ""

image:
  caption: Demostración de persNamer
  focal_point: Smart

links:
  - type: code
    icon: brands/github
    label: Código
    url: https://github.com/Pantagrueliste/persNamer
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

## persNamer: conectar la TEI con el Virtual International Authority File

[![DOI](https://zenodo.org/badge/933156851.svg)](https://doi.org/10.5281/zenodo.14875030)

persNamer es una herramienta especializada en Python que agiliza la integración en documentos XML TEI de los datos de autoridad sobre personas de VIAF (Virtual International Authority File). Al convertir los identificadores VIAF en marcado TEI listo para usar, persNamer reduce en buena medida el trabajo manual que supone crear entradas de persona estructuradas para una edición crítica digital.

## El reto del control de autoridades en TEI

Las ediciones críticas digitales suelen exigir una identificación precisa de los personajes históricos, con sus nombres normalizados y sus fechas de nacimiento y muerte. Mantener un control de autoridades coherente en todo un proyecto exige:

1. Identificar a las personas en los textos históricos
2. Encontrar datos de autoridad sobre ellas
3. Crear entradas TEI con el formato correcto
4. Garantizar que las referencias sean coherentes en todo el proyecto

Todo ello suele hacerse a mano, lleva tiempo y se presta a incoherencias.

## Cómo funciona persNamer

persNamer automatiza este flujo de trabajo en tres pasos:

1. **Obtiene los datos de VIAF**: a partir de un identificador VIAF, recupera los datos RDF mediante negociación de contenido HTTP
2. **Extrae la información clave**: analiza el RDF para extraer el nombre preferente y las fechas de nacimiento y muerte
3. **Genera el marcado TEI**: crea dos fragmentos XML esenciales:
   - Una **entrada del fichero de autoridades** (elemento `<person>` con un `xml:id` generado, `<persName>`, `<birth>`, `<death>` e `<idno type="VIAF">`)
   - Una **etiqueta de anotación** independiente (`<persName>` con un atributo `ref` que remite a la entrada de autoridad)

Esta doble salida permite al editor mantener un fichero de autoridades centralizado y, a la vez, insertar sin esfuerzo etiquetas de anotación en sus textos TEI.

## Características principales

- **Identificadores normalizados**: genera identificadores XML coherentes con el formato `pers-[apellido]-[inicial del nombre]` (p. ej., `pers-deteligny-c`)
- **Análisis de RDF**: usa `rdflib` para extraer información de distintas propiedades RDF (p. ej., `rdfs:label`, `schema:name`, `viaf:mainHead`)
- **Interfaz de línea de comandos**: se ejecuta con un número VIAF como único argumento obligatorio
- **Salida detallada**: informa con detalle del procesamiento junto a la salida XML final

## Ejemplo de uso

```bash
python persNamer.py 314802260
```

Este comando produce:

```xml
<person xml:id="pers-deteligny-c">
  <persName>Charles deTéligny</persName>
  <birth>1535</birth>
  <death>1572-08-24</death>
  <idno type="VIAF">314802260</idno>
</person>

<persName ref="#pers-deteligny-c">Charles deTéligny</persName>
```

## Aplicaciones en humanidades digitales

persNamer resulta especialmente útil para:

- Ediciones críticas digitales que necesitan control de autoridades
- Proyectos de codificación TEI que trabajan con personajes históricos
- Iniciativas de datos enlazados que conectan documentos con registros de autoridad
- Garantizar la coherencia en grandes corpus TEI
- Enseñar el control de autoridades en cursos de humanidades digitales

## Implementación

persNamer está escrito en Python y depende de:
- `requests` para las peticiones HTTP
- `rdflib` para el análisis de RDF
- `lxml` para el manejo de XML

El código fuente y la documentación están en el [repositorio de GitHub](https://github.com/Pantagrueliste/persNamer).
