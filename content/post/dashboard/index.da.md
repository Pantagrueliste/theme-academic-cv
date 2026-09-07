---
title: Arkivet i ét blik
subtitle: Hvordan interaktive datavisualiseringer styrker arkivforskningen

# Summary for listings and search engines
summary: Dashboard-webapplikationer øger situationsfornemmelsen i arkivet og forbedrer i sidste ende både arkivets tilgængelighed og forskernes produktivitet

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
- Digital humaniora
- Datavisualisering
- Arkivforskning
- Aktuel forskning

categories:
- Noter
---

# Problemet
Historiske arkiver kan være skræmmende rodede. *Mediceo del Principato* i [Statsarkivet i Firenze](https://www.archiviodistato.firenze.it/asfi/home) er et skoleeksempel. Kun en lille del af det er registreret, og mange af dokumenterne ligger spredt over mere end 6.500 bind uden nogen synlig grund. For at gøre det hele endnu mere indviklet må man kun bestille et begrænset antal bind ad gangen (eller *filze*, som de kalder dem – læg eller bundter). Under normale forhold er grænsen 4 *filze* om dagen. Under pandemien er tallet imidlertid faldet til 4 hver anden uge. Uden detaljerede registranter tvinger arkivets enorme omfang forskerne til at udtænke strategier for hurtigt at finde de dokumenter, de leder efter.

# Løsningen
Nogle sætter deres lid til tilfældet, andre forsøger sig desuden med kvalificerede gæt ud fra kronologi, modtagere, afsendere, arkivfondens oprindelse, sprog osv. Men *ser* man på alle disse variabler på én gang, kan der vise sig uventede mønstre i arkivets struktur, som gør gætteriet mere kvalificeret. Min erfaring er, at de metadata, forskere plejer at samle i et regneark, kan øge situationsfornemmelsen i arkivet betydeligt, når de bliver sat på graf.

# Eksperimentet
Min nuværende forskning drejer sig om en spions korrespondance fra 1500-tallet. Hans breve ligger spredt over hundredvis af *filze*. De er skrevet under forskellige identiteter, til forskellige og undertiden uventede modtagere, fra forskellige steder osv. For at finde de *filze*, der med størst sandsynlighed rummer de eftersøgte breve, har jeg sat et dashboard op, en interaktiv webapplikation til datavisualisering ([Plotly Dash](https://plotly.com/dash/)), som kobler alle mulige data sammen – heriblandt geografiske og kronologiske oplysninger – med et hierarkisk diagram ([sunburst](https://datavizproject.com/data-type/sunburst-diagram/)) over arkivfonden. Dashboardet fortæller mig i ét blik, hvad der allerede er fundet, og hvor meget det udgør, og det giver mig en omtrentlig idé om, hvor jeg kunne lede efter nye breve. Klikker man på bestemte variabler, opdateres alle diagrammerne desuden, så de viser de konkrete sammenhænge.

# Næste skridt
Vigtigere er måske, at dashboardet kan genbruges som visuelt register. Når den kritiske udgave af brevene engang udkommer online, vil dashboardet fungere som en alternativ indgang, hvorfra læserne kan bladre i dataene. Af fortrolighedshensyn kan jeg for øjeblikket kun vise et sløret skærmbillede, men jeg frigiver det komplette dashboard næste år. I mellemtiden kommer der snart en prototype. Følg med!
