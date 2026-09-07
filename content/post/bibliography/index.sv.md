---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Bibliografisk parsning i stor skala med förtränade språkmodeller"
subtitle: "Hur man snabbt förvandlar tusentals litteraturhänvisningar till en BibTeX-databas"
summary: "GPT-3 hjälper till att på kort tid omvandla stora mängder bibliografi till en databas"
authors: [clement]
tags: [Digital humaniora, GPT-3, Bibliografi, Automatisering]
categories: [Effektiv utgivning]
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

Automatisering är nyckeln till lägre kostnader för projekt inom digital humaniora. Hittills har de repetitiva och enformiga sysslorna i akademiskt utgivningsarbete antingen utförts till hög kostnad av överbelastade forskare eller ”lagts ut” på studenter. I den här [serien av blogginlägg](https://www.clementgodbarge.com/category/efficient-editing/) hävdar jag att de flesta av dessa otacksamma sysslor inte bara *kan* utan också *bör* automatiseras. Automatiserade redaktionella uppgifter sänker totalkostnaden för projekt inom digital humaniora. Framför allt gör de det möjligt för forskare i låginkomstregioner att snabbt och billigt ge ut värdefulla dokument.

I [förra inlägget](https://www.clementgodbarge.com/post/gpt3/) visade jag t.ex. hur förtränade språkmodeller kan sköta merparten av XML-uppmärkningen i en digital utgåva. 

I det här inlägget ger jag ett andra exempel, denna gång med bibliografi.


## Problemet
Att bygga en bibliografisk databas av de referenser som nämns i en vetenskaplig artikel är ganska enkelt. Man kan söka snabbt i en katalog som [WorldCat](https://www.worldcat.org), ladda ner referensen i ett visst format eller importera den automatiskt från en lokal databas. Det fungerar bra med en eller två artiklar.
Bortom ett visst antal referenser blir uppgiften dock avskräckande och tidsödande. För att råda bot på det kan man använda parsningsalgoritmer som [anystyle.io](https://anystyle.io). Men sådana algoritmer kan vara svåra att skala upp.
När jag använde anystyle för att konvertera de över 150 vetenskapliga essäer som ingår i vår [kritiska utgåva av Ms Fr 640](https://edition640.makingandknowing.org/#/) blev mängden ackumulerade fel helt enkelt ohanterlig. Programmet kände inte igen många av våra källor – det tog t.ex. de långa titlarna på tidigmoderna böcker för något annat – och missade mindre typiska dokument som enskilda webbsidor, videor på nätet osv. Parsrar fungerar bra, förutsatt att författaren slaviskt följer reglerna i en välkänd konvention som Chicago, Turabian eller MLA. Varje avsteg från normen ger fel.

## Lösningen
Här kan {{< hl >}}förtränade språkmodeller{{< /hl >}} hjälpa till, eftersom de {{< hl >}}snabbt uppfattar mönstren i vilken bibliografisk stil som helst{{< /hl >}}, även en du hittat på själv, och bara behöver några få exempel för att korrekt omvandla stora mängder formaterad bibliografi till en [BibTeX-databas](http://www.bibtex.org/Format/). 

I början av 2021 hade jag turen att få tidig tillgång till OpenAI:s [GPT-3 Codex](https://openai.com/blog/openai-codex/). Codex är en modell som låter användaren översätta naturligt språk till kod och tvärtom. OpenAI uppger att den behärskar över ett dussin programspråk, och även om dess API i skrivande stund fortfarande bara är tillgängligt som betaversion driver det redan populära applikationer som GitHubs [Copilot](https://github.com/features/copilot/).

Efter att ha lekt en stund med API:et insåg jag att det också fungerade utmärkt med enklare kod som `BibTeX`. 

Och faktum är att det räckte med fyra exempel i prompten för att det skulle fungera tillförlitligt. 

### Prompt

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

### Resultat
{{< hl >}}[Resultatet](https://github.com/Pantagrueliste/m-k-manuscript-data/blob/master/bibliographies/essays/EssaysBibliography.bib) är slående: över 2 000 litteraturhänvisningar konverterade på några dagar.{{< /hl >}} Metoden återgav inte bara troget mönstret i min prompt, den lade också korrekt till post- och fälttyper som inte fanns med där. `GPT-3` talar med andra ord flytande `BibTeX`. Kanske än mer förvånande, för en modell som i huvudsak tränats på engelska: den kände igen alla språk (ryska, franska, italienska, latin, grekiska, tyska, spanska osv.) och lade varje gång till rätt `langid`-fält.

> [!NOTE]
> GPT-3 har för närvarande begränsad in- och utmatningsstorlek: modellen kan behandla högst 2 048 språkliga token. När den begränsningen väl hävs skulle samma uppgift troligen ta en timme eller mindre.

Något oväntat lade GPT-3 också till uppgifter som inte fanns i originalreferenserna. 
>Baillot, Anne, and Anna Busch. “Editing for Man and Machine.” In _Users of Scholarly Editions: Editorial Anticipations of Reading, Studying and Consulting_, Vol. 13. Variants (Journal of the European Society for Textual Scholarship). Leicester, 2015. 

I den här referensen lade GPT-3 t.ex. till den permanenta länken till det öppna arkivet ([HAL](https://hal.archives-ouvertes.fr)) där uppsatsen kan läsas, inklusive de särskilda fälten `HAL_ID` och `HAL_VERSION` som HAL-arkivet skapat: 
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

Dessa tillägg visar att {{< hl >}}GPT-3 inte bara parsar litteraturhänvisningen utan också kompletterar den utifrån vad modellen ursprungligen lärt sig.{{< /hl >}} Det vore i det sammanhanget intressant att se om den beter sig likadant med referenser som är yngre än GPT-3:s träningsdata …

## Begränsningar
GPT-3 är dock inte perfekt. Modellen behöver övervakas av en människa. En av dess kända svagheter är [hallucination](https://arxiv.org/abs/2005.00661): ibland hittar den på saker och gör osannolika antaganden. 

I mitt experiment blev GPT-3:s anfall av osammanhang tydliga när modellen på eget bevåg ändrade en författares släktnamn från ”Ruscelli” till ”Ruscello”. Tekniskt sett är det inget fel, eftersom tidigmoderna italienska släktnamn kunde användas i plural och singular utan åtskillnad. Men dagens konvention är att ett släktnamn behålls som det är, vare sig det står i plural eller singular. I dag skulle ingen kalla Machiavelli för Machiavello, precis som vi förväntas skriva Rossello och inte Rosselli. Har GPT-3 struntat i konventionen för att modellen saknar kronologiskt medvetande? Eller gjorde den ett antagande utifrån släktnamnen i närheten, som i just den här delen av bibliografin råkar stå i singular allihop (Bariletto, Cesano, Rossello)?
Vem vet.

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

## Slutsats
De över 150 essäer som [ingår i vår digitala utgåva](https://edition640.makingandknowing.org/#/essays), skrivna under fyra år av intensivt samarbete, ger inte bara avgörande information om den handskrift vi gett ut och översatt utan rymmer också värdefulla bibliografiska uppgifter.

Samlar man dessa referenser i en databas kan utgivaren byta bibliografiskt format på ett ögonblick och får större frihet att visa informationen som hen vill. Databasen säger också något värdefullt om utgåvan och om det projekt som gjort den möjlig, och öppnar därmed nya analytiska perspektiv för forskare. En sådan databas kan färdigställas med hög precision och på rekordtid.

Visst kan en del fel smyga sig in, särskilt på grund av GPT-3:s benägenhet att hallucinera. Men kommande generationer av förtränade språkmodeller kommer att mildra det problemet.
