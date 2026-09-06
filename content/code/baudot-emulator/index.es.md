---
title: Emulador de telégrafo ITA2
summary: Una demostración interactiva del código telegráfico ITA2 (Baudot-Murray) que ayuda al alumnado a comprender conceptos fundamentales de la codificación binaria y de las máquinas de estados.
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
    label: Code
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

Este emulador de ITA2 sirve como recurso didáctico práctico al hacer visibles e interactivos los conceptos abstractos de la codificación. Cuando los estudiantes escriben un texto y ven su conversión inmediata en patrones de agujeros, están aprendiendo varios conceptos clave de la informática y las telecomunicaciones.

## Ventajas pedagógicas

En primer lugar, demuestra la representación binaria, es decir, cómo el texto se convierte en secuencias de unos y ceros. Aunque solemos enseñar esto de forma abstracta, ver aparecer los agujeros reales ayuda a los estudiantes a comprender cómo los sistemas físicos pueden representar información digital.

{{< Baudot >}}

El mecanismo de cambio LETRAS/CIFRAS introduce de forma natural las máquinas de estados. Los estudiantes descubren experimentando que un mismo patrón puede representar caracteres distintos según el modo activo. Esta experiencia práctica con la codificación basada en estados los prepara para conceptos informáticos más complejos.

## Detalles de implementación

El emulador está implementado en JavaScript y HTML/CSS, lo que permite integrarlo fácilmente en cualquier página web. El código es modular y puede adaptarse a distintos contextos educativos.

Puede encontrar el código fuente y probar el emulador en el [repositorio de GitHub](https://github.com/Pantagrueliste/BaudotMurray_Emulator).
