---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Bibliografisk parsing i stor skala med fortrænede sprogmodeller"
subtitle: "Sådan konverterer man hurtigt tusindvis af litteraturhenvisninger til en BibTeX-database"
summary: "GPT-3 hjælper med at omdanne store mængder bibliografi til en database på kort tid"
authors: [clement]
tags: [Digital humaniora, GPT-3, Bibliografi, Automatisering]
categories: [Effektiv udgivelse]
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

Automatisering er nøglen til at få omkostningerne ved projekter i digital humaniora ned. Indtil nu er de gentagne og ensformige opgaver i det redaktionelle arbejde ved universiteterne enten blevet udført for dyre penge af overbebyrdede forskere eller “udliciteret” til studerende. I denne [serie af blogindlæg](https://www.clementgodbarge.com/category/efficient-editing/) argumenterer jeg for, at de fleste af disse utaknemmelige opgaver ikke blot *kan*, men også *bør* automatiseres. Automatisering af redaktionelle opgaver nedbringer de samlede omkostninger ved projekter i digital humaniora. Og hvad der er afgørende: den giver forskere i lavindkomstregioner mulighed for hurtigt og billigt at udgive værdifulde dokumenter.

I [det forrige indlæg](https://www.clementgodbarge.com/post/gpt3/) viste jeg for eksempel, hvordan fortrænede sprogmodeller kan klare størstedelen af XML-opmærkningen i en digital udgave. 

I dette indlæg fremlægger jeg et andet eksempel, denne gang med bibliografi.


## Problemet
At lave en bibliografisk database ud fra henvisningerne i en videnskabelig artikel er ret ligetil. Man kan enten slå hurtigt op i en katalog som [worldcat](https://www.worldcat.org), hente henvisningen i et bestemt format eller importere den automatisk fra en lokal database. Det fungerer fint med en eller to artikler.
Ud over et vist antal henvisninger bliver opgaven dog afskrækkende og tidkrævende. For at råde bod på det kan man bruge parsingalgoritmer som [anystyle.io](https://anystyle.io) Men den slags algoritmer kan være svære at skalere op.
Da jeg brugte anystyle til at konvertere de over 150 videnskabelige essays i vores [kritiske udgave af Ms Fr 640](https://edition640.makingandknowing.org/#/), hobede fejlene sig op i et omfang, der simpelthen ikke var til at håndtere. Den kunne ikke genkende mange af vores kilder ordentligt – den forvekslede for eksempel de lange titler på bøger fra tidlig moderne tid med noget andet – og den fejlede over for mindre typiske dokumenter som bestemte websider, onlinevideoer osv. Parsere fungerer godt, forudsat at forfatteren slavisk følger reglerne i en velkendt konvention som Chicago, Turabian eller MLA. Enhver afvigelse fra normen giver fejl.

## Løsningen
Her kan {{< hl >}}fortrænede sprogmodeller{{< /hl >}} hjælpe, for de {{< hl >}}gennemskuer hurtigt mønstrene i enhver bibliografisk stil{{< /hl >}} – selv en, du selv har fundet på – og behøver kun nogle få eksempler for at konvertere store mængder formateret bibliografi korrekt til en [BibTeX-database](http://www.bibtex.org/Format/). 

I begyndelsen af 2021 var jeg så heldig at få tidlig adgang til OpenAI's [GPT-3 Codex](https://openai.com/blog/openai-codex/). Codex er en model, der lader brugeren oversætte naturligt sprog til kode og omvendt. Ifølge OpenAI behersker den mere end et dusin programmeringssprog, og selv om dens API i skrivende stund stadig kun er tilgængelig som betaversion, driver den allerede populære programmer som GitHubs [Copilot](https://github.com/features/copilot/).

Efter at have leget lidt med denne API gik det op for mig, at den også fungerede glimrende med enklere kode som `BibTeX`. 

Og faktisk skulle jeg kun bruge fire eksempler i inputprompten, før det virkede pålideligt. 

### Inputprompt

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

### Resultater
{{< hl >}}[Resultaterne](https://github.com/Pantagrueliste/m-k-manuscript-data/blob/master/bibliographies/essays/EssaysBibliography.bib) er slående: mere end 2.000 litteraturhenvisninger konverteret på få dage.{{< /hl >}} Denne tilgang gengav ikke blot mønstret fra min inputprompt nøjagtigt, den tilføjede også korrekt post- og felttyper, som slet ikke indgik i prompten. `GPT-3` taler med andre ord flydende `BibTeX`. Mere overraskende er det måske, at en model, der i det væsentlige er trænet på engelsk, genkendte alle sprogene (russisk, fransk, italiensk, latin, græsk, tysk, spansk osv.) og hver gang tilføjede det korrekte `langid`-felt.

> [!NOTE]
> GPT-3 har i øjeblikket begrænsede input- og outputstørrelser, da den højst kan behandle 2048 sproglige tokens. Så snart den begrænsning ophæves, vil samme opgave formentlig tage en time eller mindre.

Noget uventet tilføjede GPT-3 også oplysninger, som ikke stod i de oprindelige henvisninger. 
>Baillot, Anne, and Anna Busch. “Editing for Man and Machine.” In _Users of Scholarly Editions: Editorial Anticipations of Reading, Studying and Consulting_, Vol. 13. Variants (Journal of the European Society for Textual Scholarship). Leicester, 2015. 

I denne henvisning tilføjede GPT-3 for eksempel det permanente link til det open access-arkiv ([HAL](https://hal.archives-ouvertes.fr)), hvor artiklen kan læses, inklusive de særlige felter `HAL_ID` og `HAL_VERSION`, som HAL-arkivet har indført: 
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

Disse tilføjelser viser, at {{< hl >}}GPT-3 ikke blot parser den bibliografiske henvisning, men også fuldstændiggør den på grundlag af, hvad den oprindelig har lært.{{< /hl >}} Det ville i den forbindelse være interessant at se, om den opfører sig på samme måde med henvisninger, der er yngre end GPT-3's træning …

## Begrænsninger
GPT-3 er dog ikke fejlfri. Den skal overvåges af et menneske. En af dens kendte svagheder er [hallucination](https://arxiv.org/abs/2005.00661): af og til finder den på ting og drager usandsynlige slutninger. 

I mit eksperiment kom GPT-3's anfald af usammenhæng tydeligst til udtryk, da den af sig selv ændrede en forfatters slægtsnavn fra “Ruscelli” til “Ruscello”. Teknisk set er det ikke en fejl, for italienske slægtsnavne fra tidlig moderne tid kunne bruges i flertal eller ental i flæng. Nutidens konvention er dog, at et slægtsnavn beholdes i den form, ental eller flertal, det nu engang har. I dag ville ingen kalde Machiavelli for Machiavello, ligesom vi forventes at skrive Rossello og ikke Rosselli. Har GPT-3 ignoreret konventionen af mangel på kronologisk bevidsthed? Eller har den draget en slutning ud fra nabonavnene i bibliografien, som i netop dette afsnit alle tilfældigvis står i ental (Bariletto, Cesano, Rossello)?
Hvem ved.

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

## Konklusion
De over 150 essays, der [indgår i vores digitale udgave](https://edition640.makingandknowing.org/#/essays), er skrevet i løbet af fire års intenst samarbejde og rummer ikke blot vigtige oplysninger om det håndskrift, vi har udgivet og oversat, men også værdifuld bibliografisk information.

Samles disse henvisninger i en database, kan redaktørerne skifte bibliografisk format på et øjeblik og får dermed friere hænder til at vise oplysningerne, som de vil. Databasen rummer også værdifulde oplysninger om udgaven og det projekt, der gjorde den mulig, og åbner nye analytiske perspektiver for forskerne. En sådan database kan færdiggøres med høj præcision og på rekordtid.

Der kan ganske vist snige sig fejl ind, ikke mindst på grund af GPT-3's hang til at hallucinere. Men kommende generationer af fortrænede sprogmodeller vil afhjælpe det problem.
