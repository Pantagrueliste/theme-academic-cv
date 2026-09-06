---
title: persNamer
summary: Una herramienta en Python que convierte identificadores VIAF en entradas de persona y etiquetas de anotación en XML TEI, agilizando el control de autoridades en las ediciones críticas digitales.
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
    label: Code
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

persNamer es una herramienta especializada en Python que agiliza la integración de datos de autoridad sobre personas procedentes de VIAF (Virtual International Authority File) en documentos XML TEI. Al convertir los identificadores VIAF en marcado TEI listo para usar, persNamer reduce considerablemente el trabajo manual que supone crear entradas de persona estructuradas para las ediciones críticas digitales.

## El reto del control de autoridades en TEI

Las ediciones críticas digitales suelen requerir una identificación precisa de los personajes históricos, incluidos sus nombres normalizados y sus fechas de nacimiento y muerte. Mantener un control de autoridades coherente en todo un proyecto exige:

1. Identificar a las personas en los textos históricos
2. Encontrar datos de autoridad sobre ellas
3. Crear entradas TEI correctamente formateadas
4. Garantizar referencias coherentes a lo largo de todo el proyecto

Estos pasos suelen ser manuales, laboriosos y propensos a la incoherencia.

## Cómo funciona persNamer

persNamer automatiza este flujo de trabajo:

1. **Obteniendo los datos de VIAF**: dado un identificador VIAF, la herramienta recupera los datos RDF mediante negociación de contenido HTTP
2. **Extrayendo la información clave**: analiza el RDF para extraer el nombre preferido, la fecha de nacimiento y la fecha de muerte
3. **Generando el marcado TEI**: crea dos fragmentos XML esenciales:
   - Una **entrada del fichero de autoridades** (elemento `<person>` con un `xml:id` generado, `<persName>`, `<birth>`, `<death>` e `<idno type="VIAF">`)
   - Una **etiqueta de anotación** independiente (`<persName>` con un atributo `ref` que remite a la entrada de autoridad)

Esta doble salida permite a los editores mantener un fichero de autoridades centralizado e insertar fácilmente etiquetas de anotación en sus textos TEI.

## Características principales

- **Generación normalizada de identificadores**: crea identificadores XML coherentes con el formato `pers-[apellido]-[inicial del nombre]` (p. ej., `pers-deteligny-c`)
- **Análisis de RDF**: utiliza `rdflib` para extraer información de distintas propiedades RDF (p. ej., `rdfs:label`, `schema:name`, `viaf:mainHead`)
- **Interfaz de línea de comandos**: ejecución sencilla con un número VIAF como único argumento obligatorio
- **Salida detallada**: proporciona información pormenorizada del procesamiento junto con la salida XML final

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

## Aplicación en las humanidades digitales

persNamer resulta especialmente valioso para:

- Ediciones críticas digitales que requieren control de autoridades
- Proyectos de codificación TEI que trabajan con personajes históricos
- Iniciativas de datos enlazados que conectan documentos con registros de autoridad
- Garantizar la coherencia en grandes corpus TEI
- Enseñar los conceptos del control de autoridades en cursos de humanidades digitales

## Implementación

persNamer está implementado en Python y depende de:
- `requests` para las peticiones HTTP
- `rdflib` para el análisis de RDF
- `lxml` para el manejo de XML

Encontrará el código fuente y la documentación en el [repositorio de GitHub](https://github.com/Pantagrueliste/persNamer).
