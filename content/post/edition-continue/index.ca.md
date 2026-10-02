---
title: "Eines noves, costums vells"
subtitle: Una lliçó de Programming Historian sobre com publicar una edició crítica a mesura que es codifica

summary: >
  Fa mig segle que tenim ordinadors i encara fem les edicions digitals com si fossin llibres impresos.
  La meva nova lliçó per a Programming Historian en français, la primera de dues parts, exposa les peces
  bàsiques d’una edició publicada al ritme de la codificació.

date: "2026-10-02T00:00:00Z"
lastmod: "2026-10-02T00:00:00Z"

draft: false
featured: true
machine_translated: true

image:
  caption: 'Un teixidor davant d’un teler Jacquard, amb la cadena de targetes perforades que en programa el dibuix. Fotografia: [*IEEE Spectrum*](https://spectrum.ieee.org/the-jacquard-loom-a-driver-of-the-industrial-revolution)'
  focal_point: "Center"
  placement: 2
  preview_only: false

authors:
- clement

tags:
- Humanitats digitals
- Edicions digitals
- Edició crítica
- TEI

categories:
- Humanitats digitals

projects: [DCE]
---

Els humanistes que van adoptar la impremta van donar a l’edició la forma que ha conservat fins avui: s’estableix el text, es compon, es publica una sola vegada i es corregeix, si de cas, en una segona edició anys més tard. Fa mig segle que tenim ordinadors i continuem fent les edicions digitals com si fossin llibres impresos: acabem el text, el publiquem d’una tirada i les errates ja les esmenarem més endavant. Les eines són noves; els costums, vells.

La meva nova lliçó per a *Programming Historian en français*, [«L’édition critique en continu : publier au rythme de l’encodage (Partie 1)»](https://programminghistorian.org/fr/lecons/edition-critique-continu-pt1), agafa les eines noves al peu de la lletra. Si la codificació TEI és codi —i ho és—, es pot versionar, validar i transformar com qualsevol altre codi. Fa temps que els desenvolupadors de programari van deixar d’esperar el producte acabat: cada canvi es verifica automàticament i es publica tan bon punt supera les proves. Res no impedeix que una edició crítica funcioni de la mateixa manera: publicar cada carta tan bon punt ha estat codificada i revisada, i corregir-la a la vista de tothom cada vegada que aparegui una lectura millor.


## Primera part: els fonaments

Aquesta primera part presenta les peces, totes de codi obert, que alliberen l’editor del flux de treball heretat:

- un **ODD**, el document únic que especifica la codificació del projecte;
- un **esquema RELAX NG** generat a partir de l’ODD, que imposa l’estructura;
- unes **regles Schematron**, que afegeixen les restriccions editorials que un esquema no sap expressar;
- un **script de validació**, que comprova tot el corpus amb una sola ordre i genera sortides llegibles mitjançant XSLT.

Els exemples provenen de la correspondència de Filippo Cavriana, l’edició que estic [construint amb aquests criteris](/post/cavriana-edition/). La segona part hi afegirà la cadena que enllaça totes aquestes peces, de manera que cada canvi en el corpus es validi i es publiqui en el moment mateix de fer-lo. La lliçó s’inscriu en el meu projecte [Edició eficient](/project/dce/), que busca maneres d’abaratir les edicions crítiques; i automatitzar la publicació, perquè l’editor ja no hagi d’esperar un especialista al final de la cadena, és un dels estalvis més grans que tenim a l’abast.


## Indignació, negació o adopció de cara a la galeria

La intel·ligència artificial s’està rebent de la mateixa manera: indignació, negació o adopció de cara a la galeria. És una de les raons per les quals m’agraden les humanitats digitals: pocs camps mostren la paradoxa amb tanta cruesa. Les eines noves haurien de ser una invitació a repensar com podem treballar millor, no una mà de pintura sobre rutines velles. Aquesta lliçó accepta la invitació en el terreny de l’edició crítica. Continuarà, amb la segona part.

Moltes gràcies als meus editors, Daphné Mathelier i Matthias Gille Levenson, als meus revisors, Jasmin Macarios i Elsa Van Kote, i a Anisa Hawes.

La lliçó és d’accés obert: [programminghistorian.org/fr/lecons/edition-critique-continu-pt1](https://programminghistorian.org/fr/lecons/edition-critique-continu-pt1) (DOI: [10.46430/phfr0044](https://doi.org/10.46430/phfr0044)).
