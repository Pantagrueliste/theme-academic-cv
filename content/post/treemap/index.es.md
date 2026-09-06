---
title: Un navegador visual para el archivo
subtitle: Un modo más amable de acercarse a los documentos de archivo digitalizados

# Summary for listings and search engines
summary: Las visualizaciones interactivas ofrecen al lector una entrada sensorial alternativa para orientarse en documentos de archivo complejos.

# Link this post with a project
projects: [Making & Knowing Project]

# Date published
date: "2021-06-20T16:00:00Z"

# Date updated
lastmod: "2021-06-20T17:00:00Z"

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
  placement: 1
  preview_only: true

authors:
- clement

tags:
- Humanidades digitales
- Visualización de datos
- Investigación archivística

categories:
- Notas
---
# El problema
Las ediciones digitales viven en una paradoja: ponen documentos recónditos al alcance de un público más amplio, pero la pérdida de estímulos sensoriales que acarrea su desmaterialización tiende a desorientar al lector, cuando no a disuadirlo de adentrarse en su contenido. Moverse por vastos repositorios documentales resulta engorroso e intimidante, y no solo para quien carece de experiencia en la investigación de archivo: también para los lectores con deficiencias cognitivas.

# La solución
Aquí es donde los metadatos archivísticos pueden sernos útiles. Con ellos se construyen abstracciones visuales interactivas que ofrecen al lector una entrada sensorial alternativa y mejoran, de paso, la ergonomía y la accesibilidad. Para que el archivo pueda recorrerse con la vista, un *treemap* (mapa de árbol), o cualquier diagrama que desglose con eficacia datos jerárquicos, puede servir. 

# El experimento
Mi primer experimento adapta el [código del Zoomable Treemap](https://observablehq.com/@d3/zoomable-treemap) para `D3.js` y le añade hipervínculos. Representa el manuscrito BnF Ms. Fr. 640, sus folios y las entradas de cada folio; los colores indican la categoría dominante, y al pasar el cursor por una entrada aparecen más datos, incluido el enlace al manuscrito.   
El treemap se convierte así en un índice visual interactivo que ofrece al lector una visión de conjunto, rápida y ágil, no solo del contenido del manuscrito, sino también de las dimensiones de cada folio y de cada entrada.  
~~En los próximos meses seguiré dándole vueltas a esta idea con otros diagramas y otras jerarquías... ¡No se lo pierdan!~~ Para una nueva versión del treemap, pulse [aquí]({{< relref "/post/treemap2" >}}).  
> [!NOTE]
> Para verlo mejor, asegúrese de que la página está en modo claro (pulse el icono de la luna, arriba a la derecha).

  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title></title>
    <link rel="preconnect" href="https://fonts.gstatic.com" />
    <link
      href="https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;700&display=swap"
      rel="stylesheet" />
    <link rel="stylesheet" href="css/index.css" />
    <link rel="stylesheet" href="css/vis-treemap.css" />
    <link rel="stylesheet" href="css/vis-tooltip.css" />
  </head>
  <body>
    <p>Click any cell to zoom in, or the top to zoom out.</p>
    <div id="treemap"></div>
    <script src="https://cdn.jsdelivr.net/npm/d3@7.9.0/dist/d3.min.js" integrity="sha384-CjloA8y00+1SDAUkjs099PVfnY2KmDC2BZnws9kh8D/lX1s46w6EPhpXdqMfjK6i" crossorigin="anonymous" referrerpolicy="no-referrer"></script>
    <script src="js/vis-treemap.js"></script>
    <script src="js/vis-tooltip.js"></script>
    <script src="js/index.js"></script>
  </body>
