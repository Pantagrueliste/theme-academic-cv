---
title: Het archief in één oogopslag
subtitle: Hoe interactieve datavisualisaties het archiefonderzoek vooruithelpen

# Summary for listings and search engines
summary: Dashboard-webapplicaties vergroten het overzicht in het archief, en maken dat archief zo toegankelijker en de onderzoekers productiever

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
- Digital humanities
- Datavisualisatie
- Archiefonderzoek
- Lopend onderzoek

categories:
- Notities
---

# Het probleem
Historische archieven kunnen ontmoedigend rommelig zijn. Het *Mediceo del Principato* in het [Staatsarchief van Florence](https://www.archiviodistato.firenze.it/asfi/home) is daar een schoolvoorbeeld van. Slechts een klein deel ervan is geïnventariseerd, en veel documenten liggen zonder aanwijsbare reden verspreid over meer dan 6.500 delen. Om het nog ingewikkelder te maken, mag je in het archief maar een beperkt aantal delen (of *filze*, bundels, zoals ze daar heten) raadplegen. In normale tijden ligt de grens op 4 *filze* per dag. In tijden van pandemie is dat aantal echter gezakt tot 4 per twee weken. Bij gebrek aan gedetailleerde inventarissen dwingt de enorme omvang van het archief onderzoekers om strategieën te bedenken waarmee ze de gezochte documenten snel kunnen vinden.

# De oplossing
Sommigen vertrouwen liever op het toeval, anderen proberen daarnaast onderbouwde gissingen te doen op basis van chronologie, geadresseerden, auteurs, herkomst van het archieffonds, taal enzovoort. Wie al die variabelen tegelijk *bekijkt*, kan echter onverwachte patronen in de structuur van het archief ontdekken en zijn vermoedens aanscherpen. Mijn ervaring leert dat de metadata die onderzoekers doorgaans in een spreadsheet verzamelen, eenmaal in grafiekvorm, het overzicht in het archief aanzienlijk vergroten.

# Het experiment
Mijn huidige onderzoek richt zich op de correspondentie van een zestiende-eeuwse spion. Zijn brieven liggen verspreid over honderden *filze*. Ze zijn geschreven onder verschillende identiteiten, aan verschillende en soms onverwachte geadresseerden, vanuit verschillende plaatsen, enzovoort. Om de *filze* op te sporen waarin de gezochte brieven het waarschijnlijkst zitten, heb ik een dashboard opgezet: een interactieve webapplicatie voor datavisualisatie ([Plotly Dash](https://plotly.com/dash/)) die allerlei gegevens, waaronder geografische en chronologische informatie, koppelt aan een hiërarchisch diagram ([sunburst](https://datavizproject.com/data-type/sunburst-diagram/)) van het archieffonds. Het dashboard toont me in één oogopslag wat er al gevonden is, hoeveel dat voorstelt, en geeft me een ruw idee van waar ik nog nieuwe brieven zou kunnen zoeken. Klik ik bovendien op specifieke variabelen, dan worden alle diagrammen bijgewerkt en tonen ze specifieke correlaties.

# Volgende stappen
Belangrijker misschien nog: dit dashboard kan worden omgebouwd tot een visuele index. Wanneer de kritische editie van deze brieven online verschijnt, zal het dashboard dienen als alternatieve ingang, van waaruit lezers door de gegevens kunnen bladeren. Om redenen van vertrouwelijkheid kan ik op dit moment alleen een schermafbeelding tonen waarop delen zijn weggelakt, maar volgend jaar geef ik het volledige dashboard vrij. Intussen komt er binnenkort een prototype beschikbaar. Wordt vervolgd!