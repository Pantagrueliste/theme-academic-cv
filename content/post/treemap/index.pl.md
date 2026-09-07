---
title: Wizualna przeglądarka archiwum
subtitle: Przyjazne podejście do zdigitalizowanych dokumentów archiwalnych

# Summary for listings and search engines
summary: Interaktywne wizualizacje dają czytelnikom alternatywny bodziec zmysłowy, ułatwiając poruszanie się po złożonych dokumentach archiwalnych.

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
- Humanistyka cyfrowa
- Wizualizacja danych
- Badania archiwalne

categories:
- Notatki
---
# Problem
Edycje cyfrowe cierpią na pewien paradoks: udostępniają wprawdzie szerokiej publiczności dokumenty trudno dostępne, ale utrata bodźców zmysłowych, jaka wynika z ich dematerializacji, na ogół dezorientuje czytelników, a nawet zniechęca ich do obcowania z treścią. Poruszanie się po ogromnych zbiorach dokumentów staje się przez to uciążliwe i onieśmielające. Dotyczy to nie tylko użytkowników bez doświadczenia w badaniach archiwalnych, ale i czytelników z zaburzeniami poznawczymi.

# Rozwiązanie
Tu z pomocą przychodzą metadane archiwalne. Pozwalają one bowiem tworzyć interaktywne abstrakcje wizualne, które dostarczają czytelnikom alternatywnego bodźca zmysłowego, poprawiając zarazem ergonomię i dostępność. Aby po archiwum dało się nawigować wzrokiem, wystarczy treemapa (mapa drzewa) albo jakikolwiek inny diagram, który sprawnie rozkłada dane hierarchiczne. 

# Eksperyment
W pierwszym eksperymencie adaptuję [kod Zoomable Treemap](https://observablehq.com/@d3/zoomable-treemap) dla `D3.js`, dodając do niego hiperłącza. Diagram przedstawia rękopis BnF Ms Fr 640, jego karty oraz wpisy na każdej z nich. Kolory oznaczają dominującą kategorię. Po najechaniu kursorem na wpis pojawiają się dodatkowe dane, w tym hiperłącze do rękopisu.   
W ten sposób treemapa staje się interaktywnym indeksem wizualnym, który daje czytelnikom błyskawiczny i responsywny przegląd nie tylko zawartości rękopisu, ale i rozmiarów każdej karty i każdego wpisu.  
~~W nadchodzących miesiącach będę dalej rozwijał ten pomysł, próbując innych diagramów i innych hierarchii... Ciąg dalszy nastąpi!~~ Nową wersję treemapy znajdziesz [tutaj]({{< relref "/post/treemap2" >}}).  
> [!NOTE]
> Dla lepszego efektu upewnij się, że strona wyświetla się w trybie jasnym (kliknij ikonę księżyca w prawym górnym rogu).

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