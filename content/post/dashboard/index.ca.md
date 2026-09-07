---
title: L’arxiu d’un cop d’ull
subtitle: Com les visualitzacions interactives de dades milloren la recerca d’arxiu

# Summary for listings and search engines
summary: Les aplicacions web de tipus tauler de control (dashboard) augmenten la consciència situacional a l’arxiu i, al capdavall, en milloren l’accessibilitat i la productivitat dels investigadors

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
- Humanitats digitals
- Visualització de dades
- Recerca d'arxiu
- Recerca actual

categories:
- Notes
---

# El problema
Els arxius històrics poden ser d’un desordre aclaparador. El *Mediceo del Principato* de l’[Arxiu d’Estat de Florència](https://www.archiviodistato.firenze.it/asfi/home) n’és un bon exemple. Només una petita part està inventariada, i molts dels seus documents es troben escampats per més de 6.500 volums sense cap raó aparent. Per acabar-ho d’adobar, l’arxiu només permet consultar un nombre limitat de volums (o *filze*, com en diuen allà: lligalls). En temps normals, el límit és de 4 *filze* al dia. En temps de pandèmia, però, la xifra ha baixat a 4 cada dues setmanes. Sense inventaris detallats, la mida considerable de l’arxiu obliga els investigadors a idear estratègies per trobar de pressa els documents que busquen.

# La solució
Hi ha qui confia en l’atzar; d’altres proven també de fer conjectures fonamentades a partir de la cronologia, els destinataris, els autors, l’origen del fons arxivístic, la llengua, etc. Ara bé, *mirar* totes aquestes variables alhora pot revelar patrons inesperats en l’estructura de l’arxiu i afinar les nostres conjectures. La meva experiència demostra que, un cop representades gràficament, les metadades que els investigadors solen recollir en un full de càlcul poden augmentar notablement la consciència situacional a l’arxiu.

# L’experiment
La meva recerca actual gira entorn de la correspondència d’un espia del segle XVI. Les seves cartes estan escampades per centenars de *filze*. Les va escriure amb identitats diferents, a destinataris diversos i de vegades inesperats, des de llocs diferents, etc. Per localitzar les *filze* amb més probabilitats de contenir les cartes que busco, he muntat un tauler de control, una aplicació web de visualització interactiva de dades ([Plotly Dash](https://plotly.com/dash/)) que relaciona tota mena d’informació, geogràfica i cronològica inclosa, amb un diagrama jeràrquic ([sunburst](https://datavizproject.com/data-type/sunburst-diagram/)) del fons arxivístic. El tauler em diu d’un cop d’ull què s’ha trobat ja, quant representa, i em dona una idea aproximada d’on podria buscar cartes noves. A més, en clicar sobre variables concretes, tots els diagrames s’actualitzen per mostrar correlacions específiques.

# Propers passos
Potser més important encara, aquest tauler es pot reconvertir en un índex visual. Quan l’edició crítica d’aquestes cartes es publiqui en línia, el tauler farà de porta d’entrada alternativa des d’on els lectors podran navegar per les dades. Per raons de confidencialitat, de moment només en puc mostrar una captura de pantalla parcialment emmascarada, però l’any que ve publicaré el tauler complet. Mentrestant, aviat n’hi haurà disponible un prototip. Continuarà!