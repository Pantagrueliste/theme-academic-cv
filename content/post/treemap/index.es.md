---
title: Un navegador visual para el archivo
subtitle: Un enfoque accesible a los documentos de archivo digitalizados

# Summary for listings and search engines
summary: Las visualizaciones interactivas ofrecen a los lectores una entrada sensorial alternativa para navegar por documentos de archivo complejos.

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
Las ediciones digitales adolecen de una paradoja: aunque ponen documentos recónditos al alcance de un público más amplio, la pérdida de entrada sensorial que resulta de su desmaterialización tiende a desorientar a los lectores e incluso a disuadirlos de adentrarse en sus contenidos. Hacen que la navegación por vastos repositorios documentales resulte bastante engorrosa e intimidante. Esto no solo es cierto para los usuarios sin experiencia en la investigación archivística, sino también para los lectores afectados por deficiencias cognitivas.

# La solución
Aquí es donde los metadatos archivísticos pueden ayudarnos. En efecto, estos datos nos permiten crear abstracciones visuales interactivas que ofrecen a los lectores una entrada sensorial alternativa, aumentando así tanto la ergonomía como la accesibilidad. Para hacer el archivo visualmente navegable, un *treemap* (mapa de árbol), o cualquier diagrama que desglose eficazmente datos jerárquicos, puede servir. 

# El experimento
Mi primer experimento adapta el [código del Zoomable Treemap](https://observablehq.com/@d3/zoomable-treemap) para `D3.js`, añadiéndole hipervínculos. Representa el manuscrito BnF Ms. Fr. 640, sus folios y las entradas de cada folio. Los colores representan la categoría dominante. Al pasar el cursor por cada entrada se muestran más datos, incluido el hipervínculo al manuscrito.   
De este modo, el treemap se convierte en un índice visual interactivo, que ofrece a los lectores una visión general muy rápida y ágil, no solo del contenido del manuscrito, sino también de las dimensiones de cada folio y de cada entrada.  
~~En los próximos meses seguiré experimentando con esta idea, probando otros diagramas y otras jerarquías... ¡Permanezcan atentos!~~ Para ver una nueva versión del treemap, haga clic [aquí]({{< relref "/post/treemap2" >}}).  
> [!NOTE]
> Para una mejor experiencia de visualización, asegúrese de que la configuración de la página web esté en modo claro (haga clic en el icono de la luna, arriba a la derecha).

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
