---
title: L’archivio a colpo d’occhio
subtitle: Come le visualizzazioni interattive dei dati aiutano la ricerca d’archivio

# Summary for listings and search engines
summary: Le dashboard aiutano a orientarsi in archivio, e alla lunga migliorano tanto l’accessibilità dell’archivio quanto la produttività di chi vi lavora

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
Gli archivi storici possono essere di un disordine che scoraggia. Il *Mediceo del Principato* dell’[Archivio di Stato di Firenze](https://www.archiviodistato.firenze.it/asfi/home) ne è l’esempio perfetto: solo una piccola parte del fondo è inventariata, e molti documenti sono sparsi senza ragione apparente in più di 6.500 volumi. Come se non bastasse, l’archivio consente di consultare soltanto un numero limitato di volumi – o *filze*, come si dice a Firenze. In tempi normali il limite è di 4 *filze* al giorno; in tempo di pandemia è sceso a 4 ogni due settimane. In mancanza di inventari dettagliati, la mole dell’archivio obbliga chi vi fa ricerca a escogitare strategie per arrivare in fretta ai documenti che cerca.

# La soluzione
C’è chi si affida al caso, e chi prova a fare congetture ragionate su cronologia, destinatari, autori, provenienza del fondo, lingua e via dicendo. Ma *guardare* tutte queste variabili insieme può far emergere regolarità inattese nella struttura dell’archivio e affinare le congetture. La mia esperienza dice che i metadati che i ricercatori raccolgono di solito in un foglio di calcolo, una volta messi in grafico, aiutano sensibilmente a orientarsi in archivio: si sa dove si è, e che cosa si sta cercando.

# L’esperimento
La mia ricerca attuale verte sulla corrispondenza di una spia del Cinquecento. Le sue lettere sono disperse in centinaia di *filze*: scritte sotto identità diverse, a destinatari diversi e talvolta inaspettati, da luoghi diversi, e così via. Per individuare le *filze* in cui è più probabile trovarle, ho messo in piedi una dashboard, cioè un’applicazione web di visualizzazione interattiva dei dati ([Plotly Dash](https://plotly.com/dash/)) che collega informazioni di ogni genere – geografiche, cronologiche – a un diagramma gerarchico ([sunburst](https://datavizproject.com/data-type/sunburst-diagram/)) del fondo archivistico. A colpo d’occhio la dashboard mi dice che cosa è già stato trovato, quanto pesa sul totale, e mi dà un’idea approssimativa di dove potrei cercare lettere nuove. Cliccando su una variabile, poi, tutti i diagrammi si aggiornano e mostrano le correlazioni corrispondenti.

# Prossimi passi
Ma forse la cosa più importante è che la dashboard può trasformarsi in un indice visivo. Quando l’edizione critica delle lettere sarà online, farà da porta d’ingresso alternativa, da cui i lettori potranno esplorare i dati. Per ragioni di riservatezza al momento posso mostrare soltanto una schermata parzialmente oscurata, ma l’anno prossimo pubblicherò la dashboard completa; nel frattempo sarà presto disponibile un prototipo. A presto!
