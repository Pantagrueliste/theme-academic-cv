---
title: "Insegnare il binario con l’emulatore del telegrafo ITA2"
subtitle: "Un modo concreto per capire da dove viene la comunicazione digitale"
summary: Una dimostrazione interattiva del codice telegrafico ITA2 (Baudot-Murray) con cui gli studenti toccano con mano i fondamenti della codifica binaria e delle macchine a stati
date: "2025-02-13T00:00:00Z"
lastmod: "2025-02-13T00:00:00Z"
draft: false
featured: false
machine_translated: true
image:
  caption: 'Nastro telegrafico ITA2 con un messaggio codificato'
  focal_point: ""
  placement: 2
  preview_only: false
authors:
- admin
tags:
- Storia digitale
- Programmazione
- Didattica
- Storia dell'informatica
categories:
- Umanistica digitale
- Strumenti didattici
---
## Rendere concreto l’astratto
Questo emulatore ITA2 è, prima di tutto, un sussidio didattico. Rende visibile e manipolabile ciò che di solito resta sulla lavagna, e introduce così gli studenti a un’idea cardine dell’informatica e delle telecomunicazioni: la rappresentazione binaria, cioè il modo in cui un testo diventa una sequenza di uno e di zero.
Se ne parla quasi sempre in astratto; ma vedere i fori comparire uno dopo l’altro sul nastro fa capire, meglio di qualsiasi spiegazione, come un oggetto fisico possa portare informazione digitale.
{{< Baudot >}}
## Un po’ di storia: dal telegrafo al calcolatore
Il codice ITA2 (International Telegraph Alphabet No. 2), detto anche codice Baudot-Murray, fu messo a punto negli anni Venti del Novecento come perfezionamento del codice telegrafico ideato da Émile Baudot negli anni Settanta dell’Ottocento. Da questi primi sistemi di telecomunicazione l’informatica ha ereditato parecchio:
- la codifica a 5 bit è uno dei primi esempi di codifica dei caratteri;
- l’angustia del repertorio (con 5 bit si hanno appena 32 combinazioni) suggerì l’ingegnoso meccanismo di commutazione LETTERS/FIGURES, fra lettere e cifre;
- il sistema rimase in servizio sulle telescriventi fino a Novecento inoltrato.
## Le macchine a stati, giocando
La commutazione LETTERS/FIGURES è il modo più naturale di introdurre le macchine a stati. Provando e riprovando, gli studenti scoprono da soli che la stessa sequenza di fori significa caratteri diversi a seconda della modalità in cui si trova la macchina; e questa esperienza diretta di una codifica che dipende dallo stato li prepara a nozioni informatiche ben più complesse.
La sequenza `00011`, per esempio, vale:
- la lettera «A» in modalità LETTERS;
- la cifra «1» in modalità FIGURES.
Questa doppia lettura, che dipende dallo stato, è alla radice stessa del modo in cui i calcolatori trattano i dati.
## Attività per la classe
Qualche idea per portare l’emulatore ITA2 in aula:
1. **Decifrazione**: far decodificare agli studenti messaggi trasmessi in sequenze ITA2
2. **Codifica efficiente**: discutere perché la commutazione fosse tanto preziosa per risparmiare banda
3. **Evoluzione delle codifiche**: confrontare i 5 bit dell’ITA2 con i 7 di ASCII e con Unicode
4. **Physical computing**: collegare questo sistema d’altri tempi ai microcontrollori di oggi, Arduino in testa
## Un vantaggio per l’accessibilità
Interesse storico a parte, l’approccio viene incontro a studenti che imparano in modi diversi:
- chi apprende con gli occhi vede le sequenze;
- chi apprende con le mani interviene direttamente sul processo di codifica;
- chi ha un’inclinazione teorica può spingersi fino agli aspetti matematici della teoria dell’informazione.
## Note tecniche
L’emulatore è scritto in JavaScript e si integra senza fatica in qualunque piattaforma didattica basata sul web. Il codice è modulare e si lascia adattare a contesti d’insegnamento diversi.
Il codice sorgente, con l’emulatore da provare, è qui: [repository GitHub](https://github.com/Pantagrueliste/BaudotMurray_Emulator)
