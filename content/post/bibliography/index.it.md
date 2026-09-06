---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Analisi bibliografica su larga scala con i modelli linguistici pre-addestrati"
subtitle: "Come convertire rapidamente migliaia di riferimenti bibliografici in una banca dati BibTeX"
summary: "GPT-3 aiuta a convertire grandi quantità di bibliografia in una banca dati in poco tempo"
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

L’automazione è la chiave per ridurre il costo dei progetti di umanistica digitale. Fino a oggi, le operazioni ripetitive e tediose legate al lavoro editoriale in ambito accademico sono state svolte a caro prezzo da studiosi oberati, oppure «esternalizzate» agli studenti. In questa [serie di post](https://www.clementgodbarge.com/category/efficient-editing/) sostengo che la maggior parte di queste operazioni ingrate non solo *può*, ma *deve* essere automatizzata. L’automazione delle operazioni editoriali riduce il costo complessivo dei progetti di umanistica digitale. Soprattutto, permette agli studiosi delle regioni a basso reddito di pubblicare documenti preziosi in modo rapido ed economico.

Nel [post precedente](https://www.clementgodbarge.com/post/gpt3/) ho mostrato per esempio come i modelli linguistici pre-addestrati possano farsi carico della maggior parte del lavoro di etichettatura XML di un’edizione digitale. 

In questo post presento un secondo esempio, questa volta con la bibliografia.


## Il problema
Creare una banca dati bibliografica a partire dai riferimenti citati in un articolo scientifico è piuttosto semplice. Si può fare una rapida ricerca in un catalogo come [WorldCat](https://www.worldcat.org), scaricare il riferimento in un formato particolare, oppure importarlo automaticamente da una banca dati locale. Con uno o due articoli funziona bene.
Oltre un certo numero di riferimenti, però, il compito diventa ingrato e dispendioso in termini di tempo. Per ovviare si possono usare algoritmi di analisi come [anystyle.io](https://anystyle.io), ma questi algoritmi sono difficili da scalare.
Quando ho usato anystyle per convertire gli oltre 150 saggi inclusi nella nostra [edizione critica del Ms. Fr. 640](https://edition640.makingandknowing.org/#/), la quantità di errori accumulati era semplicemente ingestibile. Non riusciva a riconoscere correttamente molte delle nostre fonti, scambiando per esempio i lunghi titoli dei libri della prima età moderna per qualcos’altro, e non riconosceva i documenti meno tipici, come pagine web specifiche, video online ecc. Gli analizzatori funzionano bene, a condizione che l’autore segua religiosamente le regole di una convenzione nota come Chicago, Turabian o MLA. Ogni scarto dalla norma produce errori.

## La soluzione
È qui che i {{< hl >}}modelli linguistici pre-addestrati{{< /hl >}} possono aiutare, perché {{< hl >}}capiscono rapidamente gli schemi di qualsiasi stile bibliografico{{< /hl >}}, anche di uno inventato da voi, e bastano pochi esempi perché convertano correttamente grandi quantità di bibliografia formattata in una [banca dati BibTeX](http://www.bibtex.org/Format/). 

All’inizio del 2021 ho avuto la fortuna di ottenere l’accesso anticipato a [GPT-3 Codex](https://openai.com/blog/openai-codex/) di OpenAI. Codex è un modello che permette di tradurre il linguaggio naturale in codice e viceversa. OpenAI sostiene che padroneggi più di una dozzina di linguaggi di programmazione e, sebbene la sua API sia ancora, mentre scrivo questo post, accessibile in versione beta, alimenta già applicazioni popolari come [Copilot](https://github.com/features/copilot/) di GitHub.

Dopo aver fatto qualche prova con questa API, mi sono reso conto che poteva funzionare molto bene anche con un codice più semplice come `BibTeX`. 

E in effetti mi sono bastati quattro esempi nel prompt di input perché funzionasse in modo affidabile. 

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
I {{< hl >}}[risultati](https://github.com/Pantagrueliste/m-k-manuscript-data/blob/master/bibliographies/essays/EssaysBibliography.bib) sono sorprendenti: più di 2.000 riferimenti bibliografici convertiti nel giro di pochi giorni.{{< /hl >}} Questo approccio non solo ha riprodotto fedelmente lo schema esposto nel mio prompt di input, ma ha anche aggiunto correttamente tipi di voce e di campo che nel prompt non comparivano. `GPT-3`, in altre parole, parla `BibTeX` alla perfezione. Cosa forse più sorprendente per un modello addestrato essenzialmente in inglese, ha riconosciuto tutte le lingue (russo, francese, italiano, latino, greco, tedesco, spagnolo ecc.) aggiungendo ogni volta il campo `langid` corretto.

> [!NOTE]
> GPT-3 ha al momento dimensioni limitate di input e di output, perché può elaborare al massimo 2048 token linguistici. Non appena questa limitazione sarà rimossa, lo stesso compito richiederà probabilmente un’ora o meno.

In modo un po’ inatteso, GPT-3 ha anche aggiunto informazioni che non erano presenti nei riferimenti originali. 
>Baillot, Anne, and Anna Busch. “Editing for Man and Machine.” In _Users of Scholarly Editions: Editorial Anticipations of Reading, Studying and Consulting_, Vol. 13. Variants (Journal of the European Society for Textual Scholarship). Leicester, 2015. 

In questo riferimento bibliografico, per esempio, GPT-3 ha aggiunto il link permanente al repository ad accesso aperto ([HAL](https://hal.archives-ouvertes.fr)) dove l’articolo può essere letto, compresi i campi ad hoc `HAL_ID` e `HAL_VERSION` creati dal repository HAL: 
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

Queste aggiunte indicano che {{< hl >}}GPT-3 non si limita ad analizzare il riferimento bibliografico, ma lo completa sulla base di ciò che ha appreso in origine.{{< /hl >}} Sarebbe interessante, a questo proposito, vedere se si comporta allo stesso modo con riferimenti posteriori all’addestramento di GPT-3…

## Limiti
GPT-3 non è però perfetto. Ha bisogno di essere supervisionato da un essere umano. Uno dei suoi limiti noti è l’[allucinazione](https://arxiv.org/abs/2005.00661): a volte inventa cose e fa supposizioni improbabili. 

Nel mio esperimento, gli accessi di incoerenza di GPT-3 si sono manifestati quando ha cambiato spontaneamente il patronimico di un autore da «Ruscelli» a «Ruscello». Tecnicamente non è un errore, perché nell’Italia della prima età moderna i patronimici potevano essere usati indifferentemente al plurale o al singolare. La convenzione odierna, però, è che un patronimico al plurale o al singolare vada lasciato così com’è. Oggi nessuno chiamerebbe Machiavelli «Machiavello», così come ci si aspetta che si usi il nome Rossello e non Rosselli. GPT-3 ha ignorato questa convenzione per mancanza di coscienza cronologica? Oppure ha fatto una supposizione sulla base dei patronimici vicini, che in questa parte della bibliografia sono per caso tutti flessi al singolare (Bariletto, Cesano, Rossello)?
Chissà.

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
Scritti nel corso di quattro anni di intensa collaborazione, gli oltre 150 saggi [inclusi nella nostra edizione digitale](https://edition640.makingandknowing.org/#/essays) non solo forniscono informazioni essenziali sul manoscritto che abbiamo curato e tradotto, ma contengono anche preziose informazioni bibliografiche.

Aggregare questi riferimenti bibliografici in una banca dati permette agli editori di cambiare la formattazione bibliografica in un batter d’occhio, dando loro più flessibilità nel presentare queste informazioni come preferiscono. Questa banca dati fornisce inoltre informazioni preziose sull’edizione e sul progetto che l’ha resa possibile, aprendo nuove prospettive analitiche agli studiosi. Una simile banca dati può essere completata con grande precisione e in tempi record.

Qualche errore può insinuarsi, certo, soprattutto a causa della tendenza di GPT-3 ad avere allucinazioni. Ma le prossime iterazioni dei modelli linguistici pre-addestrati attenueranno questo problema.
