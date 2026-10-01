---
title: "Skyrails, ricostruito dalle schermate"
subtitle: Archeologia digitale, intelligenza artificiale e obsolescenza del software

summary: >
  Skyrails, lo straordinario esploratore di reti in 3D di Yose Widjaja, è sparito dal web anni fa. Partendo da una manciata di schermate,
  Claude lo ha ricostruito in una notte. Poi l’originale è riemerso su GitHub, e abbiamo potuto misurare quanto la ricostruzione gli si fosse avvicinata.

date: "2026-10-01T00:00:00Z"
lastmod: "2026-10-01T00:00:00Z"

draft: false
featured: true
machine_translated: true

image:
  caption: 'I personaggi dei *Miserabili* nello Skyrails ricostruito, con Cosette in primo piano'
  focal_point: "Center"
  placement: 2
  preview_only: false

authors:
- clement

tags:
- Sostenibilità
- IA
- Visualizzazione dei dati

categories:
- Note
---

Intorno al 2007 Yose Widjaja, allora studente alla University of New South Wales, creò Skyrails, uno straordinario programma per esplorare le reti in tre dimensioni. Si viaggiava dentro la rete stessa, da un nodo all’altro lungo binari luminosi, come se ci si trovasse all’interno dei dati. Sembrava un videogioco, in anni in cui gli strumenti di ricerca erano quasi tutti piatti e grigi. E dietro la grafica c’era vera sostanza: Skyrails aveva un suo linguaggio di scripting per dare stile ai grafi e analizzarli, e menu scritti in quello stesso linguaggio, perché potesse usarlo anche chi non sapeva programmare. Tutto questo era opera di un solo studente. Anni fa ne vidi una demo su YouTube, e non l’ho più dimenticata.


## Un programma scomparso

Skyrails non è mai stato mantenuto. Girava su Windows, la sua pagina sul sito dell’università è sparita, e tutti i link che seguivo andavano a vuoto. Ne restano soltanto delle tracce: un [album di schermate su Flickr](https://www.flickr.com/photos/14933315@N05/albums/72157602730584157/) e una manciata di post del 2007, su [FlowingData](https://flowingdata.com/?p=947), sul [*Deltoid*](https://scienceblogs.com/deltoid/2007/10/22/skyrails-graph-visualizations) di Tim Lambert e sull’[InfoVis Wiki](https://infovis-wiki.net/wiki/2007-10-27:_Skyrails:_Social_Network_Visualisation_System).

Le schermate dicono più di quanto ci si aspetterebbe. Mostrano un cielo blu notte striato di nuvole, archi disegnati come chevron animati, nodi a forma di icona o di grafico a torta, e un menu radiale che si apre attorno a un nodo quando si tiene premuto il tasto destro del mouse. Mostrano i nomi degli script che guidavano ciascuna dimostrazione (`labs.van`, `macaque.van`, `worldtrade.van`), i menu che quegli script creavano e quattro temi, chiamati *normal*, *desert*, *valley* e *openspace*. Una di esse conserva perfino una riga del linguaggio di scripting, digitata nella console in cima allo schermo:

```
with all nodes do nodeplane x 1 -1 end
```


## Ricostruire dagli indizi

Partendo da questi indizi, Claude ha ricostruito Skyrails in una notte. La nuova versione gira in un browser web grazie a [Three.js](https://threejs.org/) e dovrebbe, in linea di principio, funzionare in un visore per la realtà virtuale. Riprende il cielo, i binari a chevron, i nodi luminosi con le loro icone, i grafici a torta e gli anelli, la grande etichetta del nodo sotto il puntatore, il menu radiale e i quattro temi. Ha anche un piccolo linguaggio di scripting, costruito attorno all’unica riga che le schermate ci hanno conservato: sono istruzioni `with … do … end` a dare stile al grafo e a definire i menu.

Per metterla alla prova ho caricato tre dataset classici: la rete delle famiglie fiorentine di John Padgett, con i loro legami matrimoniali e d’affari; il club di karate di Wayne Zachary; e la rete dei personaggi dei *Miserabili* di Donald Knuth, in cui due personaggi sono collegati se compaiono nello stesso capitolo. Il video qui sotto percorre quest’ultima, da Valjean a Javert, Fantine, Cosette e Marius. Ogni binario si accende man mano che la telecamera lo segue.

<video controls playsinline preload="metadata" poster="/post/skyrails/poster.jpg" style="width:100%; height:auto; border-radius:4px;">
  <source src="/post/skyrails/skyrails-les-miserables.mp4" type="video/mp4">
  Il tuo browser non riesce a riprodurre questo video. In alternativa, puoi <a href="/post/skyrails/skyrails-les-miserables.mp4">scaricarlo</a>.
</video>

Il risultato era così vicino alle schermate che ho subito sospettato che il modello avesse assorbito, durante l’addestramento, qualche traccia del codice originale.


## Riemerge l’originale

Poi, il colpo di scena. A ricostruzione finita, ho trovato il programma originale su GitHub. Un ricercatore lo aveva condiviso nel 2015, con il permesso di Yose Widjaja, insieme al codice di un intervento sulla visualizzazione dei dati alla ShmooCon, una conferenza sulla sicurezza informatica ([RITHoneynet/DataVisualization](https://github.com/RITHoneynet/DataVisualization), copiato anche in [Light0617/3D_UIUX](https://github.com/Light0617/3D_UIUX/tree/master/skyrails/skyrailsdist)). Contiene gli eseguibili per Windows, i dati, gli shader e gli script originali, ma non il codice sorgente del motore principale.

Abbiamo così potuto mettere a confronto i due. Nell’aspetto e nell’esperienza d’uso la ricostruzione si avvicinava all’originale, ma il suo linguaggio di scripting e i suoi shader sono tutt’altra cosa. Gli script originali si presentano così:

```
with all edges do (
   if(#marriage == 1) then (
      linkorigin <- marriage -> linktarget;
   ) end;
) end;
```

Definiscono le subroutine con `sub`, i menu con `menudef` e `menulink`, i colori con `rgb: 130 0 0` e i tipi di collegamento con delle frecce. Niente di tutto questo compare nella ricostruzione, che ne condivide soltanto la forma `with … do … end` visibile nella schermata. Nemmeno gli shader originali, con nomi come `BloomFX` e `RetinalBurnFX`, hanno qualcosa in comune con quelli nuovi.

Questo non chiude la questione della memorizzazione. Gli script originali sono pubblici dal 2015 e potrebbero benissimo aver fatto parte dei dati di addestramento del modello; e nessuno, modello compreso, può dire con certezza che cosa abbia visto. Ma se il modello avesse memorizzato Skyrails, mi aspetterei che ne avesse riprodotto almeno il linguaggio. Le differenze fanno pensare che Claude abbia lavorato sugli indizi offerti dalle schermate.


## Archeologia digitale e sostenibilità del software

Vedo in questo esperimento una forma di archeologia digitale: ricostruire un oggetto perduto dalle tracce che ha lasciato, poi ritrovare l’originale e misurare quanto ci si è andati vicino. Come ogni ricostruzione, il nuovo Skyrails è un’interpretazione. Il suo aspetto e il suo comportamento poggiano sugli indizi; tutto ciò che sta sotto è nuovo.

È anche una questione di sostenibilità. Il software diventa obsoleto molto più in fretta dei dati che è stato costruito per leggere. Quando un programma muore, i file, gli script e le visualizzazioni prodotti con esso diventano difficili da aprire, anche quando sopravvivono. Buona parte del software degli anni Duemila esiste ormai solo sotto forma di schermate, video e vecchi binari che sempre meno macchine sono in grado di eseguire. Lo Skyrails originale potrebbe ancora avviarsi su un computer Windows, o in un emulatore, ma non può più essere mantenuto, adattato o portato su altre piattaforme, perché il suo codice sorgente è andato perduto.

Come avevo previsto qualche anno fa, l’IA sta diventando un rimedio concreto contro questo genere di obsolescenza. Può ricostruire uno strumento perduto a partire dalle sue tracce, e può ricostruire i programmi di lettura che permettono di continuare a usare i vecchi dati. Il passo successivo, per questo progetto, è evidente: insegnare al nuovo motore a leggere gli script `.van` e i file di dati originali, perché le dimostrazioni che Yose Widjaja scrisse nel 2007 possano girare di nuovo. Chiunque abbia a cuore la sostenibilità dei dati, nella ricerca, negli archivi o nell’umanistica digitale, è una cosa che merita attenzione.

Skyrails era in anticipo sui tempi, e a quasi vent’anni di distanza continua a impressionare. Il merito dell’idea e del design spetta interamente a Yose Widjaja: spero che queste righe gli arrivino.
