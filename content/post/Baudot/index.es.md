---
title: "Enseñar el sistema binario con el emulador de telégrafo ITA2"
subtitle: "Una manera práctica de entender los comienzos de la comunicación digital"
summary: Una demostración interactiva del código telegráfico ITA2 (Baudot-Murray) con la que los estudiantes captan las nociones básicas de la codificación binaria y de las máquinas de estados
date: "2025-02-13T00:00:00Z"
lastmod: "2025-02-13T00:00:00Z"
draft: false
featured: false
machine_translated: true
image:
  caption: 'Cinta de telégrafo ITA2 con un mensaje codificado'
  focal_point: ""
  placement: 2
  preview_only: false
authors:
- admin
tags:
- Historia digital
- Programación
- Docencia
- Historia de la informática
categories:
- Humanidades digitales
- Herramientas didácticas
---
## Dar cuerpo a lo abstracto
Este emulador de ITA2 es, ante todo, un recurso para el aula. Al volver visibles y manipulables las nociones abstractas de la codificación, introduce a los estudiantes en una idea central de la informática y de las telecomunicaciones: la representación binaria, esto es, el modo en que un texto se convierte en una secuencia de unos y ceros.
Solemos explicar todo esto en abstracto; ver cómo van apareciendo los agujeros en la cinta ayuda, en cambio, a comprender que un sistema físico puede contener información digital.
{{< Baudot >}}
## Contexto histórico: del telégrafo al ordenador
El código ITA2 (Alfabeto Telegráfico Internacional n.º 2), llamado también código Baudot-Murray, se desarrolló en los años veinte del siglo pasado como perfeccionamiento del código telegráfico que Émile Baudot había ideado en la década de 1870. Aquellos primeros sistemas de telecomunicación dejaron una huella directa en la informática posterior:
- Su esquema de cinco bits fue una de las primeras codificaciones de caracteres
- Las limitaciones del repertorio (con cinco bits solo caben 32 combinaciones) obligaron a idear el ingenioso mecanismo de cambio LETRAS/CIFRAS
- Los teletipos siguieron usando este sistema hasta bien entrado el siglo XX
## Aprender las máquinas de estados jugando
El mecanismo de cambio LETRAS/CIFRAS es la puerta natural a las máquinas de estados. A fuerza de probar, los estudiantes descubren que un mismo patrón puede representar caracteres distintos según el modo en que se encuentre la máquina; y esa experiencia directa de una codificación dependiente del estado los prepara para nociones informáticas más complejas.
Así, el patrón de bits `00011` representa:
- la letra «A» en modo LETRAS
- la cifra «1» en modo CIFRAS
Esta doble lectura según el estado está en la raíz misma de cómo los ordenadores manejan los datos.
## Actividades para el aula
Algunas maneras de sacar partido al emulador en clase:
1. **Reto de descifrado**: dar a los estudiantes mensajes codificados en ITA2 para que los descifren
2. **Codificación eficiente**: discutir por qué el mecanismo de cambio importaba tanto para ahorrar ancho de banda
3. **Evolución de las codificaciones**: comparar los cinco bits del ITA2 con los siete de ASCII y con Unicode
4. **Computación física**: tender un puente entre este sistema histórico y microcontroladores actuales como Arduino
## Ventajas para la accesibilidad
Más allá de su interés histórico, el enfoque se adapta a distintos estilos de aprendizaje:
- Quien aprende con los ojos ve los patrones
- Quien aprende con las manos interviene directamente en el proceso de codificación
- Quien prefiere los conceptos puede explorar la vertiente matemática de la teoría de la información
## Detalles de implementación
El emulador está escrito en JavaScript y se integra sin dificultad en cualquier plataforma docente basada en la web. El código es modular y puede adaptarse a contextos de enseñanza muy distintos.
El código fuente está disponible, y el emulador puede probarse, en el [repositorio de GitHub](https://github.com/Pantagrueliste/BaudotMurray_Emulator)
