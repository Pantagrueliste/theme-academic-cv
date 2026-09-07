---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Grootschalig bibliografisch parsen met voorgetrainde taalmodellen"
subtitle: "Hoe je duizenden literatuurverwijzingen in een handomdraai omzet in een BibTeX-database"
summary: "GPT-3 helpt om in korte tijd grote hoeveelheden bibliografie om te zetten in een database"
authors: [clement]
tags: [Digital humanities, GPT-3, Bibliografie, Automatisering]
categories: [Efficiënt editeren]
date: 2022-07-07T19:04:14+02:00
lastmod: 2022-07-07T19:04:14+02:00
featured: false
draft: false
machine_translated: true

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

Automatisering is de sleutel om de kosten van projecten in de digital humanities te drukken. Tot op heden werden de repetitieve en saaie klussen die bij editoriaal werk in academische kringen komen kijken, ofwel tegen hoge kosten verricht door overbelaste onderzoekers, ofwel “uitbesteed” aan studenten. In deze [reeks blogberichten](https://www.clementgodbarge.com/category/efficient-editing/) betoog ik dat de meeste van die ondankbare taken niet alleen *kunnen*, maar ook *moeten* worden geautomatiseerd. Automatisering van editoriale taken drukt de totale kosten van projecten in de digital humanities. En wat vooral telt: ze stelt onderzoekers uit armere regio's in staat om waardevolle documenten snel en betaalbaar te publiceren.

In [het vorige bericht](https://www.clementgodbarge.com/post/gpt3/) heb ik bijvoorbeeld laten zien hoe voorgetrainde taalmodellen het grootste deel van het XML-labelwerk van een digitale editie voor hun rekening kunnen nemen. 

In dit bericht geef ik een tweede voorbeeld, ditmaal met bibliografie.


## Het probleem
Een bibliografische database aanleggen op basis van de verwijzingen in een wetenschappelijk artikel is vrij eenvoudig. Je zoekt even in een catalogus als [WorldCat](https://www.worldcat.org), downloadt de verwijzing in een bepaald formaat, of importeert ze automatisch uit een lokale database. Met een of twee artikelen werkt dat prima.
Boven een bepaald aantal verwijzingen wordt de klus echter afstompend en tijdrovend. Om daar iets aan te doen kun je parsingalgoritmen als [anystyle.io](https://anystyle.io) gebruiken. Maar zulke algoritmes laten zich moeilijk opschalen.
Toen ik anystyle inzette om de meer dan 150 wetenschappelijke essays van onze [kritische editie van Ms Fr 640](https://edition640.makingandknowing.org/#/) om te zetten, stapelden de fouten zich op tot een onbeheersbare berg. Het herkende veel van onze bronnen niet goed – zo zag het de lange titels van vroegmoderne boeken voor iets anders aan – en het struikelde over minder gangbare documenten, zoals specifieke webpagina's, onlinevideo's enzovoort. Parsers werken goed, mits de auteur zich strikt houdt aan de regels van een bekende conventie als Chicago, Turabian of MLA. Elke afwijking van de norm levert fouten op.

## De oplossing
Hier kunnen {{< hl >}}voorgetrainde taalmodellen{{< /hl >}} uitkomst bieden: ze {{< hl >}}doorgronden razendsnel de patronen van welke bibliografische stijl dan ook{{< /hl >}}, zelfs een die je zelf hebt bedacht, en hebben maar een handvol voorbeelden nodig om grote hoeveelheden opgemaakte bibliografie correct om te zetten in een [BibTeX-database](http://www.bibtex.org/Format/). 

Begin 2021 had ik het geluk vroegtijdig toegang te krijgen tot [GPT-3 Codex](https://openai.com/blog/openai-codex/) van OpenAI. Codex is een model waarmee je natuurlijke taal naar code vertaalt en omgekeerd. Volgens OpenAI beheerst het meer dan een dozijn programmeertalen, en hoewel de API op het moment dat ik dit schrijf nog als bètaversie beschikbaar is, draait er al populaire software op, zoals GitHubs [Copilot](https://github.com/features/copilot/).

Na wat experimenteren met deze API merkte ik dat ze ook uitstekend overweg kan met eenvoudiger code zoals `BibTeX`. 

Sterker nog: vier voorbeelden in de invoerprompt volstonden om het betrouwbaar te laten werken. 

### Invoerprompt

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

### Resultaten
De {{< hl >}}[resultaten](https://github.com/Pantagrueliste/m-k-manuscript-data/blob/master/bibliographies/essays/EssaysBibliography.bib) zijn opzienbarend: meer dan 2.000 literatuurverwijzingen werden in een paar dagen omgezet.{{< /hl >}} Deze aanpak reproduceerde niet alleen getrouw het patroon uit mijn invoerprompt, maar voegde ook correct entry- en veldtypes toe die daar niet in voorkwamen. `GPT-3` spreekt met andere woorden vloeiend `BibTeX`. Verrassender nog voor een model dat hoofdzakelijk in het Engels is getraind: het herkende alle talen (Russisch, Frans, Italiaans, Latijn, Grieks, Duits, Spaans enzovoort) en voegde telkens het juiste `langid`-veld toe.

> [!NOTE]
> GPT-3 kent momenteel beperkingen op de omvang van invoer en uitvoer: het verwerkt maximaal 2048 taaltokens. Zodra die beperking wegvalt, zou dezelfde klus waarschijnlijk een uur of minder vergen.

Enigszins onverwacht voegde GPT-3 ook informatie toe die niet in de oorspronkelijke verwijzingen stond. 
>Baillot, Anne, and Anna Busch. “Editing for Man and Machine.” In _Users of Scholarly Editions: Editorial Anticipations of Reading, Studying and Consulting_, Vol. 13. Variants (Journal of the European Society for Textual Scholarship). Leicester, 2015. 

In deze verwijzing bijvoorbeeld voegde GPT-3 de permanente link toe naar het open-accessarchief ([HAL](https://hal.archives-ouvertes.fr)) waar het artikel te lezen is, inclusief de speciale velden `HAL_ID` en `HAL_VERSION` die HAL zelf heeft bedacht: 
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

Uit die toevoegingen blijkt dat {{< hl >}}GPT-3 een literatuurverwijzing niet alleen parseert, maar ze ook aanvult op grond van wat het eerder heeft geleerd.{{< /hl >}} Het zou in dat opzicht interessant zijn om te zien of het zich net zo gedraagt bij verwijzingen van na zijn trainingsperiode...

## Beperkingen
GPT-3 is echter niet volmaakt. Het heeft menselijk toezicht nodig. Een van zijn bekende zwakke plekken is [hallucinatie](https://arxiv.org/abs/2005.00661): soms verzint het dingen en doet het onwaarschijnlijke aannames. 

In mijn experiment kwam de warrigheid van GPT-3 aan het licht toen het uit eigen beweging de familienaam van een auteur veranderde van “Ruscelli” in “Ruscello”. Strikt genomen is dat geen fout: vroegmoderne Italiaanse familienamen konden zonder onderscheid in het meervoud of het enkelvoud worden gebruikt. Tegenwoordig is de conventie echter dat je een naam laat zoals hij is, of hij nu in het meervoud of in het enkelvoud staat. Niemand zou Machiavelli vandaag nog Machiavello noemen, net zoals we geacht worden Rossello te schrijven en niet Rosselli. Heeft GPT-3 die conventie genegeerd bij gebrek aan chronologisch besef? Of heeft het een aanname gedaan op grond van de omringende namen, die in dit deel van de bibliografie toevallig allemaal in het enkelvoud staan (Bariletto, Cesano, Rossello)?
Wie zal het zeggen.

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

## Conclusie
De ruim 150 essays [in onze digitale editie](https://edition640.makingandknowing.org/#/essays), geschreven tijdens vier jaar van intensieve samenwerking, bevatten niet alleen cruciale informatie over het handschrift dat we hebben geëditeerd en vertaald, maar ook waardevolle bibliografische gegevens.

Door die literatuurverwijzingen in een database samen te brengen, kunnen editeurs de bibliografische opmaak in een oogwenk veranderen en hebben ze meer vrijheid om die informatie naar eigen inzicht te tonen. Zo'n database vertelt bovendien veel over de editie en het project dat haar mogelijk maakte, en opent nieuwe analytische perspectieven voor onderzoekers. En ze kan met grote nauwkeurigheid en in recordtijd worden aangelegd.

Er kunnen weliswaar fouten insluipen, met name door de neiging van GPT-3 om te hallucineren. Maar toekomstige generaties voorgetrainde taalmodellen zullen dat probleem verkleinen.
