---
title: Een visuele browser voor het archief
subtitle: Een gebruiksvriendelijke benadering van gedigitaliseerde archiefstukken

# Summary for listings and search engines
summary: Interactieve visualisaties bieden lezers een alternatieve zintuiglijke ingang om door complexe archiefstukken te navigeren.

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
- Digital humanities
- Datavisualisatie
- Archiefonderzoek

categories:
- Notities
---
# Het probleem
Digitale edities lijden aan een paradox: ze maken obscure documenten weliswaar voor een breder publiek beschikbaar, maar het verlies aan zintuiglijke prikkels dat met hun dematerialisering gepaard gaat, werkt desoriënterend en schrikt lezers zelfs af om zich in de inhoud te verdiepen. Ze maken het navigeren door omvangrijke documentverzamelingen nogal omslachtig en intimiderend. Dat geldt niet alleen voor gebruikers zonder ervaring met archiefonderzoek, maar ook voor lezers met een cognitieve beperking.

# De oplossing
Hier kunnen archiefmetadata ons helpen. Met zulke gegevens kunnen we namelijk interactieve visuele abstracties maken die lezers een alternatieve zintuiglijke ingang bieden, en zo zowel de ergonomie als de toegankelijkheid vergroten. Om het archief visueel navigeerbaar te maken, volstaat een treemap, of om het even welk diagram dat hiërarchische gegevens efficiënt ontleedt. 

# Het experiment
Mijn eerste experiment bewerkt de [Zoomable Treemap-code](https://observablehq.com/@d3/zoomable-treemap) voor `D3.js` en voegt er hyperlinks aan toe. De treemap stelt het handschrift BnF Ms Fr 640 voor, met zijn folio's en de items op elk folio. De kleuren geven de overheersende categorie aan. Wie met de muis over een item gaat, krijgt meer gegevens te zien, waaronder de hyperlink naar het handschrift.   
Zo wordt de treemap een interactieve visuele index die lezers een razendsnel en responsief overzicht geeft, niet alleen van de inhoud van het handschrift, maar ook van de omvang van elk folio en elk item.  
~~De komende maanden experimenteer ik verder met dit idee en probeer ik andere diagrammen en andere hiërarchieën uit... Wordt vervolgd!~~ Voor een nieuwe versie van de treemap klik je [hier]({{< relref "/post/treemap2" >}}).  
> [!NOTE]
> Voor een betere weergave zorg je ervoor dat de webpagina in de lichte modus staat (klik op het maanpictogram rechtsboven).

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