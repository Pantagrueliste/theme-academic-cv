---
title: Emulador de telégrafo ITA2
summary: Una demostración interactiva del código telegráfico ITA2 (Baudot-Murray) con la que los estudiantes captan las nociones básicas de la codificación binaria y de las máquinas de estados.
tags:
  - JavaScript
  - Interactivo
  - Docencia

date: "2025-02-13T00:00:00Z"

# Optional external URL for project (replaces project detail page)
external_link: ""

image:
  caption: Cinta de telégrafo ITA2 con un mensaje codificado
  focal_point: Smart

links:
  - type: code
    icon: brands/github
    label: Código
    url: https://github.com/Pantagrueliste/BaudotMurray_Emulator
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

Este emulador de ITA2 es un recurso para el aula: vuelve visibles y manipulables las nociones abstractas de la codificación. Cuando los estudiantes escriben un texto y lo ven convertirse al instante en patrones de agujeros, están aprendiendo varias ideas clave de la informática y de las telecomunicaciones.

## Ventajas pedagógicas

En primer lugar, muestra la representación binaria: cómo un texto se convierte en una secuencia de unos y ceros. Solemos explicarlo en abstracto; ver cómo van apareciendo los agujeros ayuda, en cambio, a comprender que un sistema físico puede contener información digital.

{{< Baudot >}}

El mecanismo de cambio LETRAS/CIFRAS es la puerta natural a las máquinas de estados. A fuerza de probar, los estudiantes descubren que un mismo patrón puede representar caracteres distintos según el modo en que se encuentre la máquina; y esa experiencia directa de una codificación dependiente del estado los prepara para nociones informáticas más complejas.

## Detalles de implementación

El emulador está escrito en JavaScript y HTML/CSS, de modo que se incrusta sin dificultad en cualquier página web. El código es modular y puede adaptarse a distintos contextos docentes.

El código fuente está disponible, y el emulador puede probarse, en el [repositorio de GitHub](https://github.com/Pantagrueliste/BaudotMurray_Emulator).
