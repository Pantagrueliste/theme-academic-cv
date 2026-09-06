---
title: El archivo de un vistazo
subtitle: Cómo la visualización interactiva de datos mejora la investigación en archivos

# Summary for listings and search engines
summary: Las aplicaciones web de tipo panel (dashboard) aumentan la conciencia situacional en el archivo y, a la postre, mejoran su accesibilidad y la productividad de los investigadores

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
Los archivos históricos pueden ser de un desorden desalentador. El *Mediceo del Principato* del [Archivio di Stato di Firenze](https://www.archiviodistato.firenze.it/asfi/home) es un buen ejemplo: solo una pequeña parte está inventariada, y muchos de sus documentos andan dispersos, sin razón aparente, por más de 6500 volúmenes. Para colmo, el archivo solo permite consultar un número limitado de volúmenes —o *filze*, como los llaman allí—: cuatro *filze* al día en tiempos normales; en tiempos de pandemia, cuatro cada dos semanas. A falta de inventarios detallados, las dimensiones del archivo obligan al investigador a idear estrategias para dar pronto con los documentos que busca.

# La solución
Unos se fían del azar; otros hacen además conjeturas fundadas a partir de la cronología, los destinatarios, los autores, el origen del fondo, la lengua, etc. Ahora bien, *mirar* todas esas variables a la vez puede sacar a la luz pautas insospechadas en la estructura del archivo y afinar nuestras conjeturas. Mi experiencia dice que los metadatos que los investigadores suelen acumular en una hoja de cálculo, una vez representados gráficamente, aumentan de forma notable la conciencia situacional en el archivo.

# El experimento
Mi investigación actual gira en torno a la correspondencia de un espía del siglo XVI. Sus cartas están repartidas por cientos de *filze*: escritas bajo identidades distintas, a destinatarios distintos y a veces inesperados, desde lugares distintos, etc. Para localizar las *filze* con más probabilidades de contener las cartas que busco, he montado un panel (*dashboard*), una aplicación web de visualización interactiva ([Plotly Dash](https://plotly.com/dash/)) que conecta datos de toda índole —geográficos y cronológicos, entre otros— con un diagrama jerárquico ([sunburst](https://datavizproject.com/data-type/sunburst-diagram/)) del fondo. El panel me dice de un vistazo qué se ha encontrado ya, cuánto representa y dónde podría, a grandes rasgos, buscar nuevas cartas. Y al pulsar sobre una variable concreta, todos los diagramas se actualizan para mostrar correlaciones específicas.

# Próximos pasos
Más importante aún: el panel puede reconvertirse en índice visual. Cuando la edición crítica de estas cartas se publique en línea, servirá de punto de entrada alternativo desde el que los lectores podrán recorrer los datos. Por razones de confidencialidad, de momento solo puedo mostrar una captura de pantalla con partes tapadas, pero el año que viene publicaré el panel completo. Mientras tanto, pronto habrá un prototipo disponible. ¡No se lo pierdan!
