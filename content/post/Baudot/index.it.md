---
title: "Insegnare il binario con l’emulatore del telegrafo ITA2"
subtitle: "Un approccio pratico per capire le origini della comunicazione digitale"
summary: Una dimostrazione interattiva del codice telegrafico ITA2 (Baudot-Murray) che aiuta gli studenti a cogliere i concetti fondamentali della codifica binaria e delle macchine a stati
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
## Rendere tangibili i concetti astratti
Questo emulatore ITA2 è un sussidio didattico pratico. Rendendo visibili e interattivi i concetti astratti della codifica, introduce gli studenti a un’idea cardine dell’informatica e delle telecomunicazioni: la rappresentazione binaria, ossia il modo in cui un testo si trasforma in sequenze di uno e di zero.
Di solito la insegniamo in modo astratto; vedere i fori comparire davvero sul nastro aiuta invece gli studenti a capire come un sistema fisico possa rappresentare informazione digitale.
{{< Baudot >}}
## Contesto storico: dal telegrafo all’informatica
Il codice ITA2 (International Telegraph Alphabet No. 2), noto anche come codice Baudot-Murray, fu messo a punto negli anni Venti del Novecento come perfezionamento del codice telegrafico originale di Émile Baudot, risalente agli anni Settanta dell’Ottocento. Questi primi sistemi di telecomunicazione hanno influenzato direttamente gli sviluppi successivi dell’informatica:
- lo schema di codifica a 5 bit fu uno dei primi esempi di codifica dei caratteri;
- i limiti del set di caratteri (con 5 bit sono possibili solo 32 combinazioni) portarono all’ingegnoso meccanismo di commutazione LETTERE/CIFRE;
- il sistema rimase in uso nelle telescriventi fino a Novecento inoltrato.
## Imparare le macchine a stati giocando
Il meccanismo di commutazione LETTERE/CIFRE introduce in modo naturale le macchine a stati. Sperimentando, gli studenti scoprono che la stessa sequenza può rappresentare caratteri diversi a seconda della modalità corrente. Questa esperienza diretta con una codifica dipendente dallo stato li prepara a concetti informatici più complessi.
Per esempio, la sequenza di bit `00011` rappresenta:
- la lettera «A» in modalità LETTERE;
- il numero «1» in modalità CIFRE.
Questa doppia interpretazione, che dipende dallo stato, è alla base del modo in cui i computer trattano i dati.
## Attività per la classe
Ecco alcuni modi per integrare l’emulatore ITA2 nella didattica:
1. **Sfida di decrittazione**: far decodificare agli studenti messaggi cifrati in sequenze ITA2
2. **Codifica efficiente**: discutere perché il meccanismo di commutazione fosse importante per risparmiare banda
3. **Evoluzione della codifica**: confrontare il codice a 5 bit dell’ITA2 con ASCII (7 bit) e Unicode
4. **Physical computing**: collegare questo sistema storico ai microcontrollori moderni come Arduino
## Vantaggi per l’accessibilità
Al di là dell’interesse storico, questo approccio aiuta studenti con stili di apprendimento diversi:
- chi apprende visivamente vede le sequenze;
- chi apprende con il corpo interagisce direttamente con il processo di codifica;
- chi ha un’inclinazione concettuale può esplorare gli aspetti matematici della teoria dell’informazione.
## Dettagli di implementazione
L’emulatore è scritto in JavaScript e può essere integrato facilmente in qualsiasi piattaforma didattica basata sul web. Il codice è modulare e personalizzabile per contesti di insegnamento diversi.
Il codice sorgente è disponibile, e l’emulatore si può provare, qui: [Repository GitHub](https://github.com/Pantagrueliste/BaudotMurray_Emulator)
