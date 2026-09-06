---
title: El archivo de un vistazo
subtitle: Cómo las visualizaciones de datos interactivas mejoran la investigación archivística

# Summary for listings and search engines
summary: Las aplicaciones web de tipo panel de control (dashboard) aumentan la conciencia situacional en el archivo y mejoran, en última instancia, su accesibilidad y la productividad de los investigadores

# Link this post with a project
projects: [Filippo Cavriana's Secret Correspondence, 1568—1589.]

# Date published
date: "2021-05-24T16:00:00Z"

# Date updated
lastmod: "2021-05-24T16:00:00Z"

# Is this an unpublished draft?
draft: false

# Show this page in the Featured widget?
featured: false
machine_translated: true

# Featured image
# Place an image named `featured.jpg/png` in this page's folder and customize its options here.
image:
  caption: ''
  focal_point: ""
  placement: 2
  preview_only: false

authors:
- clement

tags:
- Humanidades digitales
- Visualización de datos
- Investigación archivística
- Investigación en curso

categories:
- Notas
---

# El problema
Los archivos históricos pueden ser desalentadoramente caóticos. El *Mediceo del Principato* del [Archivio di Stato di Firenze](https://www.archiviodistato.firenze.it/asfi/home) es un buen ejemplo. En efecto, solo una pequeña parte está inventariada, y muchos de sus documentos se hallan dispersos en más de 6500 volúmenes sin motivo aparente. Para complicar aún más las cosas, el archivo solo permite consultar un número limitado de volúmenes (o *filze*, como los llaman allí). En tiempos normales, el límite es de 4 *filze* al día. En tiempos de pandemia, sin embargo, esa cifra ha bajado a 4 cada dos semanas. A falta de inventarios detallados, el tamaño considerable del archivo obliga a los investigadores a idear estrategias para encontrar rápidamente los documentos que buscan.

# La solución
Algunos confiarán en el azar; otros intentarán además hacer conjeturas fundadas a partir de la cronología, los destinatarios, los autores, el origen del fondo archivístico, la lengua, etc. *Mirar* todas estas variables simultáneamente, sin embargo, puede revelar patrones inesperados en la estructura del archivo y mejorar nuestras conjeturas. Mi experiencia demuestra que, una vez representados gráficamente, los metadatos que los investigadores suelen reunir en una hoja de cálculo pueden aumentar considerablemente la conciencia situacional en el archivo.

# El experimento
Mi investigación actual se centra en la correspondencia de un espía del siglo XVI. Sus cartas están repartidas entre cientos de *filze*. Están escritas bajo distintas identidades, a destinatarios distintos y a veces inesperados, desde lugares distintos, etc. Para encontrar las *filze* con más probabilidades de contener las cartas buscadas, he montado un panel de control (*dashboard*), una aplicación web de visualización de datos interactiva ([Plotly Dash](https://plotly.com/dash/)) que conecta todo tipo de datos, incluida información geográfica y cronológica, con un diagrama jerárquico ([sunburst](https://datavizproject.com/data-type/sunburst-diagram/)) del fondo archivístico. El panel me indica de un vistazo lo que ya se ha encontrado, cuánto representa, y me da una idea aproximada de dónde podría buscar nuevas cartas. Además, al hacer clic en variables concretas, todos los diagramas se actualizan para mostrar correlaciones específicas.

# Próximos pasos
Quizá más importante aún, este panel puede reutilizarse como índice visual. Cuando la edición crítica de estas cartas se publique en línea, el panel funcionará como punto de entrada alternativo, desde el que los lectores podrán explorar los datos. Por razones de confidencialidad, de momento solo puedo mostrar una captura de pantalla parcialmente censurada, pero publicaré el panel completo el año que viene. Mientras tanto, pronto estará disponible un prototipo. ¡Permanezcan atentos!
