---
title: L’archivio a colpo d’occhio
subtitle: Come le visualizzazioni interattive dei dati potenziano la ricerca d’archivio

# Summary for listings and search engines
summary: Le applicazioni web di tipo dashboard aumentano la consapevolezza situazionale in archivio, migliorando in definitiva l’accessibilità di quest’ultimo e la produttività dei ricercatori

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
- Umanistica digitale
- Visualizzazione dei dati
- Ricerca d'archivio
- Ricerca in corso

categories:
- Note
---

# Il problema
Gli archivi storici possono essere di un disordine scoraggiante. Il *Mediceo del Principato* all’[Archivio di Stato di Firenze](https://www.archiviodistato.firenze.it/asfi/home) ne è un esempio lampante. Solo una piccola parte del fondo è inventariata, e molti dei suoi documenti sono dispersi in più di 6.500 volumi senza una ragione apparente. A complicare ulteriormente le cose, l’archivio permette di consultare soltanto un numero limitato di volumi (o *filze*, come le chiamano lì). In tempi normali il limite è fissato a 4 *filze* al giorno. In tempo di pandemia, però, quel numero è sceso a 4 ogni due settimane. In assenza di inventari dettagliati, le dimensioni considerevoli dell’archivio costringono i ricercatori a escogitare strategie per trovare rapidamente i documenti che cercano.

# La soluzione
Alcuni privilegeranno il caso, altri cercheranno di fare ipotesi ragionate sulla base della cronologia, dei destinatari, degli autori, dell’origine del fondo archivistico, della lingua ecc. *Guardare* tutte queste variabili contemporaneamente, però, può rivelare schemi inattesi nella struttura dell’archivio e migliorare le nostre congetture. La mia esperienza mostra che, una volta rappresentati graficamente, i metadati che i ricercatori raccolgono di solito in un foglio di calcolo possono aumentare in modo significativo la consapevolezza situazionale in archivio.

# L’esperimento
La mia ricerca attuale verte sulla corrispondenza di una spia del Cinquecento. Le sue lettere sono disperse in centinaia di *filze*. Sono scritte sotto identità diverse, a destinatari diversi e talvolta inattesi, da luoghi diversi, e così via. Per individuare le *filze* che hanno più probabilità di contenere le lettere cercate, ho messo a punto una dashboard, un’applicazione web di visualizzazione interattiva dei dati ([Plotly Dash](https://plotly.com/dash/)) che collega dati di ogni tipo, comprese informazioni geografiche e cronologiche, a un diagramma gerarchico ([sunburst](https://datavizproject.com/data-type/sunburst-diagram/)) del fondo archivistico. La dashboard mi dice a colpo d’occhio che cosa è già stato trovato, quanto rappresenta, e mi dà un’idea approssimativa di dove potrei cercare nuove lettere. Cliccando su variabili specifiche, inoltre, tutti i diagrammi si aggiornano per mostrare correlazioni specifiche.

# Prossimi passi
Cosa forse più importante, questa dashboard può essere riconvertita in indice visivo. Quando l’edizione critica di queste lettere sarà pubblicata online, la dashboard fungerà da punto di accesso alternativo, da cui i lettori potranno esplorare i dati. Per ragioni di riservatezza, al momento posso mostrare solo una schermata parzialmente oscurata, ma pubblicherò la dashboard completa l’anno prossimo. Nel frattempo, un prototipo sarà presto disponibile. Restate sintonizzati!
