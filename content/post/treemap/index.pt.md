---
title: Um navegador visual para o arquivo
subtitle: Uma abordagem amigável aos documentos de arquivo digitalizados

# Summary for listings and search engines
summary: As visualizações interativas dão aos leitores um estímulo sensorial alternativo para navegar em documentos de arquivo complexos.

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
- Humanidades digitais
- Visualização de dados
- Investigação em arquivo

categories:
- Notas
---
# O problema
As edições digitais sofrem de um paradoxo: se tornam documentos recônditos acessíveis a um público mais vasto, a perda de estímulos sensoriais que a sua desmaterialização acarreta tende a desorientar os leitores e até a desencorajá-los de se envolverem com o conteúdo. Tornam a navegação em vastos repositórios documentais bastante pesada e intimidante. Isto vale não apenas para os utilizadores sem experiência de investigação em arquivo, mas também para os leitores com dificuldades cognitivas.

# A solução
É aqui que os metadados de arquivo nos podem ajudar. Com efeito, esses dados permitem criar abstrações visuais interativas que dão aos leitores um estímulo sensorial alternativo, melhorando assim a ergonomia e a acessibilidade. Para tornar o arquivo visualmente navegável, um treemap, ou qualquer diagrama que decomponha eficazmente dados hierárquicos, serve perfeitamente. 

# A experiência
A minha primeira experiência adapta o [código do Zoomable Treemap](https://observablehq.com/@d3/zoomable-treemap) para `D3.js`, acrescentando-lhe hiperligações. Representa o manuscrito BnF Ms Fr 640, os seus fólios e as entradas dentro de cada fólio. As cores representam a categoria dominante. Ao passar o rato sobre cada entrada, obtêm-se mais dados, incluindo a hiperligação para o manuscrito.   
Deste modo, o treemap torna-se um índice visual interativo, dando aos leitores uma panorâmica muito rápida e reativa, não apenas do conteúdo do manuscrito, mas também das dimensões de cada fólio e de cada entrada.  
~~Nos próximos meses continuarei a explorar esta ideia, experimentando outros diagramas e outras hierarquias... Fiquem atentos!~~ Para uma nova versão do treemap, clique [aqui]({{< relref "/post/treemap2" >}}).  
> [!NOTE]
> Para uma melhor experiência de visualização, certifique-se de que a página está em modo claro (clique no ícone da lua, no canto superior direito).

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