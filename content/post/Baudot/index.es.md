---
title: "Enseñar el sistema binario con el emulador de telégrafo ITA2"
subtitle: "Un enfoque práctico para comprender los inicios de la comunicación digital"
summary: Una demostración interactiva del código telegráfico ITA2 (Baudot-Murray) que ayuda al alumnado a comprender conceptos fundamentales de la codificación binaria y de las máquinas de estados
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
## Hacer tangibles los conceptos abstractos
Este emulador de ITA2 es un recurso didáctico práctico. Al hacer visibles e interactivos los conceptos abstractos de la codificación, introduce al alumnado en una noción clave de la informática y las telecomunicaciones: la representación binaria, es decir, cómo el texto se convierte en secuencias de unos y ceros.
Aunque solemos enseñar esto de forma abstracta, ver aparecer los agujeros reales ayuda a los estudiantes a comprender cómo los sistemas físicos pueden representar información digital.
{{< Baudot >}}
## Contexto histórico: del telégrafo a la informática
El código ITA2 (Alfabeto Telegráfico Internacional n.º 2), también conocido como código Baudot-Murray, se desarrolló en la década de 1920 como un perfeccionamiento del código telegráfico original de Émile Baudot, de la década de 1870. Estos primeros sistemas de telecomunicación influyeron directamente en el desarrollo posterior de la informática:
- El esquema de codificación de 5 bits fue un ejemplo temprano de codificación de caracteres
- Las limitaciones del juego de caracteres (solo 32 combinaciones posibles con 5 bits) dieron lugar al ingenioso mecanismo de cambio LETRAS/CIFRAS
- Este sistema se utilizó en los teletipos hasta bien entrado el siglo XX
## Aprender las máquinas de estados jugando
El mecanismo de cambio LETRAS/CIFRAS introduce de forma natural las máquinas de estados. Los estudiantes descubren experimentando que un mismo patrón puede representar caracteres distintos según el modo activo. Esta experiencia práctica con la codificación basada en estados los prepara para conceptos informáticos más complejos.
Por ejemplo, el patrón de bits `00011` representa:
- La letra «A» en modo LETRAS
- El número «1» en modo CIFRAS
Esta doble interpretación en función del estado es fundamental para entender cómo los ordenadores trabajan con los datos.
## Actividades para el aula
He aquí algunas formas de incorporar el emulador de ITA2 a la enseñanza:
1. **Reto de descifrado**: pedir a los estudiantes que decodifiquen mensajes codificados como patrones ITA2
2. **Codificación eficiente**: debatir por qué el mecanismo de cambio era importante para ahorrar ancho de banda
3. **Evolución de la codificación**: comparar el código de 5 bits del ITA2 con ASCII (7 bits) y Unicode
4. **Computación física**: relacionar este sistema histórico con microcontroladores modernos como Arduino
## Ventajas en materia de accesibilidad
Más allá de su interés histórico, este enfoque ayuda a estudiantes con distintos estilos de aprendizaje:
- Los aprendices visuales ven los patrones
- Los aprendices cinestésicos interactúan directamente con el proceso de codificación
- Los pensadores conceptuales pueden explorar los aspectos matemáticos de la teoría de la información
## Detalles de implementación
El emulador está implementado en JavaScript y puede integrarse fácilmente en cualquier plataforma de aprendizaje basada en la web. El código es modular y puede personalizarse para distintos contextos docentes.
Puede encontrar el código fuente y probar el emulador en el [repositorio de GitHub](https://github.com/Pantagrueliste/BaudotMurray_Emulator)
