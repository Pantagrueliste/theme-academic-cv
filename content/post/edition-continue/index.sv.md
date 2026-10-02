---
title: "Gamla vanor, nya verktyg"
subtitle: En lektion i Programming Historian om att publicera en textkritisk utgåva i takt med kodningen

summary: >
  Vi har haft datorer i ett halvsekel och gör ändå digitala utgåvor som om de vore tryckta böcker.
  Min nya lektion för Programming Historian en français, den första av två delar, går igenom byggstenarna
  i en utgåva som publiceras i samma takt som den kodas.

date: "2026-10-02T00:00:00Z"
lastmod: "2026-10-02T00:00:00Z"

draft: false
featured: true
machine_translated: true

image:
  caption: 'En vävare vid en jacquardvävstol, med den kedja av hålkort som programmerar mönstret. Foto: [*IEEE Spectrum*](https://spectrum.ieee.org/the-jacquard-loom-a-driver-of-the-industrial-revolution)'
  focal_point: "Center"
  placement: 2
  preview_only: false

authors:
- clement

tags:
- Digital humaniora
- Digitala utgåvor
- Textutgivning
- TEI

categories:
- Digital humaniora

projects: [DCE]
---

De tidigmoderna humanister som tog boktryckarkonsten i bruk gav utgåvan den form den har behållit sedan dess: texten fastställs, sätts, ges ut en gång och rättas, om alls, i en andra upplaga många år senare. Vi har haft datorer i ett halvsekel och gör fortfarande digitala utgåvor som om de vore tryckta böcker. Vi gör texten färdig, publicerar den i ett svep och skjuter rättelserna på framtiden. Verktygen är nya, vanorna gamla.

Min nya lektion för *Programming Historian en français*, [”L’édition critique en continu : publier au rythme de l’encodage (Partie 1)”](https://programminghistorian.org/fr/lecons/edition-critique-continu-pt1), tar de nya verktygen på orden. Om TEI-kodning är kod – och det är den – kan den versionshanteras, valideras och transformeras precis som kod. Programutvecklare slutade för länge sedan vänta på en färdig produkt: varje ändring kontrolleras automatiskt och släpps så snart den klarar kontrollen. Ingenting hindrar en textkritisk utgåva från att arbeta på samma sätt – att publicera varje brev så snart det är kodat och granskat, och att rätta det öppet så fort en bättre läsart dyker upp.


## Första delen: byggstenarna

Den här första delen går igenom de komponenter som befriar utgivaren från det nedärvda arbetsflödet, samtliga med öppen källkod:

- en **ODD**, det enda dokument som specificerar projektets kodning;
- ett **RELAX NG-schema** som genereras ur den och upprätthåller strukturen;
- **Schematron-regler**, som lägger till de redaktionella villkor som ett schema inte kan uttrycka;
- ett **valideringsskript**, som kontrollerar hela korpusen med ett enda kommando och ger läsbara utdata via XSLT.

Exemplen är hämtade ur Filippo Cavrianas korrespondens, den utgåva jag [bygger upp efter dessa principer](/post/cavriana-edition/). Del 2 lägger till den kedja som binder samman komponenterna, så att varje ändring i korpusen valideras och publiceras i samma stund som den görs. Lektionen ingår i mitt projekt [Effektiv utgivning](/project/dce/), som söker vägar att pressa kostnaderna för vetenskapliga utgåvor; att automatisera publiceringen, så att utgivaren inte längre står och väntar på en specialist i slutet av kedjan, är en av de största besparingar som går att göra.


## Ramaskri, förnekelse eller fasadputs

Den artificiella intelligensen tas emot efter samma mönster: ramaskri, förnekelse eller ytligt anammande. Det är ett av skälen till att jag tycker om digital humaniora: få fält visar paradoxen så ogenerat. Nya verktyg borde vara en inbjudan att tänka om kring hur vi kan arbeta bättre, inte ett nytt lager färg på gamla rutiner. Den här lektionen antar inbjudan för textutgivningens räkning. Håll utkik efter del 2.

Jag vill tacka mina redaktörer, Daphné Mathelier och Matthias Gille Levenson, mina granskare, Jasmin Macarios och Elsa Van Kote, samt Anisa Hawes.

Lektionen är fritt tillgänglig: [programminghistorian.org/fr/lecons/edition-critique-continu-pt1](https://programminghistorian.org/fr/lecons/edition-critique-continu-pt1) (DOI: [10.46430/phfr0044](https://doi.org/10.46430/phfr0044)).
