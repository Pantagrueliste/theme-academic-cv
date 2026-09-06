---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Spoglio bibliografico su larga scala con i modelli linguistici pre-addestrati"
subtitle: "Come trasformare in poco tempo migliaia di riferimenti bibliografici in una banca dati BibTeX"
summary: "GPT-3 converte in pochi giorni grandi quantità di bibliografia in una banca dati"
authors: [clement]
tags: [Umanistica digitale, GPT-3, Bibliografia, Automazione]
categories: [Edizione efficiente]
date: 2022-07-07T19:04:14+02:00
lastmod: 2022-07-07T19:04:14+02:00
featured: false
machine_translated: true
draft: false

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ""
  focal_point: ""
  preview_only: false

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: [Efficient Editing]
---

L’automazione è la chiave per abbattere i costi dei progetti di umanistica digitale. Finora, le operazioni ripetitive e tediose del lavoro editoriale in ambito accademico sono state svolte a caro prezzo da studiosi già oberati, oppure «appaltate» agli studenti. In questa [serie di post](https://www.clementgodbarge.com/category/efficient-editing/) sostengo che la maggior parte di queste incombenze ingrate non solo *può*, ma *deve* essere automatizzata. Automatizzare le operazioni editoriali riduce il costo complessivo dei progetti; e soprattutto permette agli studiosi delle regioni meno ricche di pubblicare documenti di valore in fretta e con poca spesa.

Nel [post precedente](https://www.clementgodbarge.com/post/gpt3/) ho mostrato, per esempio, come i modelli linguistici pre-addestrati possano sbrigare gran parte dell’etichettatura XML di un’edizione digitale. 

Qui presento un secondo esempio: la bibliografia.


## Il problema
Ricavare una banca dati bibliografica dai riferimenti citati in un articolo scientifico è cosa abbastanza semplice: si cerca in un catalogo come [WorldCat](https://www.worldcat.org), si scarica il riferimento nel formato voluto, oppure lo si importa da una banca dati locale. Con uno o due articoli funziona.
Oltre un certo numero di riferimenti, però, il compito diventa ingrato e divora tempo. Per rimediare esistono algoritmi di analisi come [anystyle.io](https://anystyle.io), ma scalarli non è facile.
Quando ho usato anystyle per convertire gli oltre 150 saggi della nostra [edizione critica del Ms. Fr. 640](https://edition640.makingandknowing.org/#/), gli errori si sono accumulati fino a diventare ingestibili: molte fonti non venivano riconosciute, i lunghi titoli dei libri della prima età moderna venivano scambiati per chissà che, e i documenti meno convenzionali – una pagina web, un video in rete – restavano lettera morta. Gli analizzatori funzionano bene a patto che l’autore osservi religiosamente uno stile noto, Chicago, Turabian o MLA che sia; ogni scarto dalla norma si paga in errori.

## La soluzione
È qui che i {{< hl >}}modelli linguistici pre-addestrati{{< /hl >}} tornano utili: {{< hl >}}colgono in un attimo lo schema di qualunque stile bibliografico{{< /hl >}}, anche di uno inventato da voi, e bastano pochi esempi perché convertano correttamente masse di bibliografia formattata in una [banca dati BibTeX](http://www.bibtex.org/Format/). 

All’inizio del 2021 ho avuto la fortuna di accedere in anteprima a [GPT-3 Codex](https://openai.com/blog/openai-codex/) di OpenAI, un modello che traduce il linguaggio naturale in codice e viceversa. OpenAI gli attribuisce la padronanza di più di una dozzina di linguaggi di programmazione; e sebbene la sua API sia ancora in versione beta mentre scrivo, alimenta già applicazioni popolari come [Copilot](https://github.com/features/copilot/) di GitHub.

Dopo qualche prova con l’API mi sono reso conto che se la cavava benissimo anche con un codice più modesto come `BibTeX`. 

E infatti sono bastati quattro esempi nel prompt di input perché funzionasse in modo affidabile. 

### Prompt di input

References:
Bayle, Ariane. “Patients exemplaires: la correspondance médicale de Fioravanti.” In *Vulgariser la médecine. Du style médical en France et en Italie*, edited by Andrea Carlino and Michel Jeanneret, 181–212. Geneva: Droz, 2009.  

Berns, Andrew D. *The Bible and Natural Philosophy in Renaissance Italy: Jewish and Christian Physicians in Search of Truth*. Cambridge: Cambridge University Press, 2015.  

Gabler, Hans Walter. “Theorizing the Digital Scholarly Edition.” *Literature Compass* 7, no. 2 (2010): 43–56. https://doi.org/10.1111/j.1741-4113.2009.00675.x.  

Findlen, Paula. *Possessing Nature: Museums, Collecting, and Scientific Culture in Early Modern Italy*. Berkeley: University of California Press, 1994.

```BibTeX
@incollection{bayle2009,
  author = {Bayle, Ariane},
  booktitle = {Vulgariser la médecine. Du style médical en France et en Italie},
  title = {Patients exemplaires: la correspondance médicale de Fioravanti},
  editor = {Carlino, Andrea and Michel Jeanneret},
  year = {2009},
  address = {Geneva},
  publisher = {Droz},
  langid = {french}
}
@book{berns2015,
  title = {The Bible and Natural Philosophy in Renaissance Italy: Jewish and Christian Physicians in Search of Truth},
  author = {Berns, Andrew D.},
  address = {Cambridge},
  publisher = {Cambridge University Press},
  langid = {english},
  date = {2015}
}
@article{gabler2010,
  author = {Gabler, Hans Walter},
  title = {Theorizing the Digital Scholarly Edition},
  journal = {Literature Compass},
  volume = {7},
  number = {2},
  pages = {43-56},
  doi = {10.1111/j.1741-4113.2009.00675.x},
  langid = {english},
  year = {2010}
}
@book{findlen1994,
  title = {Possessing Nature: Museums, Collecting, and Scientific Culture in Early Modern Italy},
  author = {Findlen, Paula},
  address = {Berkeley},
  publisher = {University of California Press},
  langid = {english},
  date = {1994}
}
```

### Risultati
I {{< hl >}}[risultati](https://github.com/Pantagrueliste/m-k-manuscript-data/blob/master/bibliographies/essays/EssaysBibliography.bib) sono impressionanti: più di 2.000 riferimenti bibliografici convertiti nel giro di pochi giorni.{{< /hl >}} Non solo il modello ha riprodotto fedelmente lo schema del prompt, ma ha aggiunto, a ragion veduta, tipi di voce e di campo che nel prompt non c’erano: `GPT-3`, insomma, parla `BibTeX` correntemente. E, cosa forse più sorprendente per un modello addestrato per lo più sull’inglese, ha riconosciuto tutte le lingue (russo, francese, italiano, latino, greco, tedesco, spagnolo…) aggiungendo ogni volta il campo `langid` giusto.

> [!NOTE]
> GPT-3 ha per ora dimensioni limitate di input e di output: elabora al massimo 2048 token. Quando questo limite verrà rimosso, lo stesso lavoro richiederà probabilmente un’ora, o meno.

Un po’ a sorpresa, GPT-3 ha aggiunto anche informazioni che nei riferimenti originali non c’erano. 
>Baillot, Anne, and Anna Busch. “Editing for Man and Machine.” In _Users of Scholarly Editions: Editorial Anticipations of Reading, Studying and Consulting_, Vol. 13. Variants (Journal of the European Society for Textual Scholarship). Leicester, 2015. 

In questo riferimento, per esempio, ha inserito il link permanente al repository ad accesso aperto ([HAL](https://hal.archives-ouvertes.fr)) dove l’articolo si può leggere, compresi i campi ad hoc `HAL_ID` e `HAL_VERSION` propri di HAL: 
```BibTeX
@inproceedings{baillot2015, 
  title = {Editing for Man and Machine},
  author = {Baillot, Anne and Busch, Anna},
  year = 2015,
  booktitle = {Users of Scholarly Editions: Editorial Anticipations of Reading, Studying and Consulting},
  address = {Leicester},
  series = {Variants (Journal of the European Society for Textual Scholarship)},
  volume = 13,
  editor = {Bruhn, Siglinde and Schreiber, Manfred},
  langid = {english},
  hal_id = {halshs-01233380},
  hal_version = {v1}
}
```

Aggiunte del genere indicano che {{< hl >}}GPT-3 non si limita ad analizzare il riferimento bibliografico: lo completa con quello che ha imparato in origine.{{< /hl >}} Sarebbe interessante, a questo proposito, vedere se si comporta allo stesso modo con riferimenti posteriori al suo addestramento…

## Limiti
GPT-3 non è però infallibile, e va sorvegliato da un essere umano. Uno dei suoi limiti noti è l’[allucinazione](https://arxiv.org/abs/2005.00661): ogni tanto inventa, e si lascia andare a supposizioni improbabili. 

Nel mio esperimento, l’incoerenza di GPT-3 si è manifestata quando ha cambiato di sua iniziativa il cognome di un autore da «Ruscelli» in «Ruscello». A rigore non è un errore: nell’Italia della prima età moderna i cognomi si usavano indifferentemente al plurale e al singolare. La convenzione odierna, però, vuole che il cognome resti com’è, plurale o singolare che sia: nessuno oggi chiamerebbe Machiavelli «Machiavello», così come si dice Rossello e non Rosselli. GPT-3 ha ignorato la convenzione per difetto di coscienza cronologica? O ha tirato a indovinare sulla scorta dei cognomi vicini, che in questa parte della bibliografia sono per combinazione tutti al singolare (Bariletto, Cesano, Rossello)?
Chi lo sa.

```Bibtex
@book{rossello1565,
  title = {Della summa de’ secreti universali},
  author = {Rossello, Timoteo},
  address = {Venice},
  publisher = {Giovanni Bariletto},
  langid = {italian},
  date = {1565}
}
@book{ruscello1559, 
  title = {La seconda parte de’ secreti del Reverendo Donno Alessio Piemontese},
  author = {Ruscello, Girolamo},
  address = {Pesaro}, 
  publisher = {Bartolomeo Cesano}, 
  langid = {italian}, 
  date = {1559}
}
```

## Conclusione
Scritti nell’arco di quattro anni di intensa collaborazione, gli oltre 150 saggi [compresi nella nostra edizione digitale](https://edition640.makingandknowing.org/#/essays) non solo forniscono informazioni essenziali sul manoscritto che abbiamo curato e tradotto, ma racchiudono anche un patrimonio bibliografico prezioso.

Raccogliere quei riferimenti in una banca dati permette ai curatori di cambiare stile bibliografico in un batter d’occhio, e di presentare l’informazione come meglio credono. La banca dati dice inoltre molto sull’edizione e sul progetto che l’ha resa possibile, e apre agli studiosi nuove prospettive d’analisi. E la si può completare con grande precisione e in tempi record.

Qualche errore, certo, può insinuarsi, soprattutto per la propensione di GPT-3 ad allucinare. Ma le prossime generazioni di modelli linguistici pre-addestrati attenueranno il problema.
