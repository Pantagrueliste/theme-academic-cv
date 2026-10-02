---
title: "Strumenti nuovi, vecchie abitudini"
subtitle: Una lezione di Programming Historian su come pubblicare un’edizione critica man mano che la si codifica

summary: >
  Abbiamo i computer da mezzo secolo e continuiamo a fare edizioni digitali come se fossero libri a stampa.
  La mia nuova lezione per Programming Historian en français, la prima di due, presenta i mattoni
  di un’edizione pubblicata al ritmo della sua codifica.

date: "2026-10-02T00:00:00Z"
lastmod: "2026-10-02T00:00:00Z"

draft: false
featured: true
machine_translated: true

image:
  caption: 'Un tessitore al telaio Jacquard, con la catena di schede perforate che ne programma il disegno. Fotografia: [*IEEE Spectrum*](https://spectrum.ieee.org/the-jacquard-loom-a-driver-of-the-industrial-revolution)'
  focal_point: "Center"
  placement: 2
  preview_only: false

authors:
- clement

tags:
- Umanistica digitale
- Edizioni digitali
- Ecdotica
- TEI

categories:
- Umanistica digitale

projects: [DCE]
---

Gli umanisti che adottarono la stampa diedero all’edizione la forma che ha conservato fino a oggi: si stabilisce il testo, lo si compone, lo si pubblica una volta per tutte e lo si corregge, semmai, in una seconda edizione anni dopo. Abbiamo i computer da mezzo secolo, eppure continuiamo a fare edizioni digitali come se fossero libri a stampa: si finisce il testo, lo si pubblica in blocco, e all’errata corrige si penserà poi. Gli strumenti sono nuovi; le abitudini, vecchie.

La mia nuova lezione per *Programming Historian en français*, [«L’édition critique en continu : publier au rythme de l’encodage (Partie 1)»](https://programminghistorian.org/fr/lecons/edition-critique-continu-pt1), prende in parola gli strumenti nuovi. Se la codifica TEI è codice, e lo è, allora la si può versionare, validare e trasformare come qualsiasi altro codice. Gli sviluppatori hanno smesso da tempo di aspettare il prodotto finito: ogni modifica viene verificata automaticamente e rilasciata non appena supera i controlli. Nulla impedisce a un’edizione critica di funzionare allo stesso modo, pubblicando ogni lettera appena codificata e rivista, e correggendola alla luce del sole ogni volta che salta fuori una lettura migliore.


## Prima parte: i mattoni

Questa prima parte presenta i pezzi, tutti open source, che liberano l’editore dal flusso di lavoro ereditato:

- un **ODD**, il documento unico che specifica la codifica del progetto;
- uno **schema RELAX NG** generato a partire dall’ODD, che ne impone la struttura;
- delle **regole Schematron**, che aggiungono i vincoli editoriali che uno schema non sa esprimere;
- uno **script di validazione**, che controlla l’intero corpus con un solo comando e produce output leggibili tramite XSLT.

Gli esempi vengono dal carteggio di Filippo Cavriana, l’edizione che sto [costruendo secondo questi criteri](/post/cavriana-edition/). La seconda parte aggiungerà la catena che lega insieme questi pezzi, in modo che ogni modifica al corpus venga validata e pubblicata nel momento stesso in cui la si fa. La lezione rientra nel mio progetto [Edizione efficiente](/project/dce/), che cerca il modo di abbattere i costi delle edizioni critiche; e automatizzare la pubblicazione, così che l’editore non debba più aspettare uno specialista in fondo alla catena, è uno dei risparmi più consistenti a portata di mano.


## Scandalo, rifiuto o adozione di facciata

L’intelligenza artificiale viene accolta allo stesso modo: scandalo, rifiuto o adozione di facciata. È uno dei motivi per cui amo l’umanistica digitale: pochi campi mostrano il paradosso con tanta evidenza. Gli strumenti nuovi dovrebbero invitarci a ripensare come lavorare meglio, non dare una mano di vernice fresca a vecchie routine. Questa lezione raccoglie l’invito sul terreno dell’ecdotica. Alla prossima puntata, con la seconda parte.

Ringrazio i miei editor, Daphné Mathelier e Matthias Gille Levenson, i miei revisori, Jasmin Macarios ed Elsa Van Kote, e Anisa Hawes.

La lezione è in accesso aperto: [programminghistorian.org/fr/lecons/edition-critique-continu-pt1](https://programminghistorian.org/fr/lecons/edition-critique-continu-pt1) (DOI: [10.46430/phfr0044](https://doi.org/10.46430/phfr0044)).
