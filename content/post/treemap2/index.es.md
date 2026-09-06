---
title: Visualizar manuscritos 2 (actualización)
subtitle: Una herramienta de visualización de manuscritos con múltiples criterios

# Summary for listings and search engines
summary: Nueva versión del treemap interactivo con funciones adicionales. 

# Link this post with a project
projects: [Making & Knowing Project]

# Date published
date: "2021-11-20T16:00:00Z"

# Date updated
lastmod: "2021-11-20T17:00:00Z"

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
- BnF Ms. Fr. 640
- Investigación en curso

categories:
- Notas
---
Como prometí, he aquí una nueva versión del treemap interactivo presentado en una [entrada anterior]({{< relref "/post/treemap" >}}), esta vez con dos modos de visualización.

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
      rel="stylesheet"
    />
    <link rel="stylesheet" href="css/index.css" />
    <link rel="stylesheet" href="css/vis-treemap.css" />
    <link rel="stylesheet" href="css/vis-tooltip.css" />
  </head>
  <body>
    <div class="stacked">
      <div class="switch">
        <input
          type="checkbox"
          name="group-by-category-switch"
          id="group-by-category-switch"
          checked
        />
        <label for="group-by-category-switch"> Group folios by category </label>
      </div>
      <div id="treemap"></div>
    </div>
    <script src="https://cdn.jsdelivr.net/npm/d3@7.9.0/dist/d3.min.js" integrity="sha384-CjloA8y00+1SDAUkjs099PVfnY2KmDC2BZnws9kh8D/lX1s46w6EPhpXdqMfjK6i" crossorigin="anonymous" referrerpolicy="no-referrer"></script>
    <script src="js/vis-treemap.js"></script>
    <script src="js/vis-tooltip.js"></script>
    <script src="js/index.js"></script>
  </body>
