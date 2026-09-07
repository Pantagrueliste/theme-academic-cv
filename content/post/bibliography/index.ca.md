---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Anàlisi bibliogràfica a gran escala amb models de llengua preentrenats"
subtitle: "Com convertir ràpidament milers de referències bibliogràfiques en una base de dades BibTeX"
summary: "GPT-3 ajuda a convertir grans quantitats de bibliografia en una base de dades en poc temps"
authors: [clement]
tags: [Humanitats digitals, GPT-3, Bibliografia, Automatització]
categories: [Edició eficient]
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

L’automatització és clau per abaratir els projectes d’humanitats digitals. Fins avui, les tasques repetitives i tedioses de la feina editorial en l’àmbit acadèmic les han fet, a un cost molt alt, uns estudiosos desbordats, o bé s’han «externalitzat» als estudiants. En aquesta [sèrie d’entrades](https://www.clementgodbarge.com/category/efficient-editing/) sostinc que la majoria d’aquestes tasques ingrates no només *es poden* automatitzar, sinó que *s’han* d’automatitzar. L’automatització de les tasques editorials redueix el cost global dels projectes d’humanitats digitals. I, sobretot, permet als estudiosos de les regions amb pocs recursos publicar documents valuosos de manera ràpida i assequible.

A [l’entrada anterior](https://www.clementgodbarge.com/post/gpt3/) he mostrat, per exemple, com els models de llengua preentrenats poden fer la major part de la feina d’etiquetatge XML d’una edició digital. 

En aquesta entrada exposo un segon exemple, aquest cop amb la bibliografia.


## El problema
Crear una base de dades bibliogràfica a partir de les referències esmentades en un article acadèmic és força senzill. Es pot fer una cerca ràpida en un catàleg com [worldcat](https://www.worldcat.org), descarregar la referència en un format concret, o importar-la automàticament des d’una base de dades local. Amb un o dos articles, això funciona bé.
Més enllà d’un cert nombre de referències, però, la tasca es torna ingrata i lenta. Per posar-hi remei es poden fer servir algorismes d’anàlisi com [anystyle.io](https://anystyle.io). Però aquests algorismes poden ser difícils d’escalar.
Quan vaig fer servir anystyle per convertir els més de 150 assaigs acadèmics inclosos en la nostra [edició crítica del Ms Fr 640](https://edition640.makingandknowing.org/#/), la quantitat d’errors acumulats era senzillament impossible de gestionar. No va reconèixer bé moltes de les nostres fonts – va confondre, per exemple, els llargs títols dels llibres de l’inici de l’època moderna amb una altra cosa – i no va saber identificar documents menys típics, com ara pàgines web concretes, vídeos en línia, etc. Els analitzadors funcionen bé sempre que l’autor segueixi religiosament les regles d’una convenció coneguda com Chicago, Turabian o MLA. Qualsevol desviació de la norma es tradueix en errors.

## La solució
És aquí on {{< hl >}}els models de llengua preentrenats{{< /hl >}} poden ajudar, perquè {{< hl >}}entenen ràpidament els patrons de qualsevol estil bibliogràfic{{< /hl >}}, fins i tot d’un que t’hagis inventat, i només necessiten uns quants exemples per convertir correctament grans quantitats de bibliografia formatada en una [base de dades BibTeX](http://www.bibtex.org/Format/). 

A principis de 2021 vaig tenir la sort d’obtenir accés anticipat al [GPT-3 Codex](https://openai.com/blog/openai-codex/) d’OpenAI. Codex és un model que permet als usuaris traduir el llenguatge natural a codi i viceversa. OpenAI afirma que domina més d’una dotzena de llenguatges de programació i, tot i que la seva API encara és, mentre escric aquesta entrada, en fase beta, ja fa funcionar aplicacions populars com ara el [Copilot](https://github.com/features/copilot/) de GitHub.

Després de jugar una mica amb aquesta API, em vaig adonar que també podia funcionar molt bé amb codi més senzill, com ara `BibTeX`. 

I, de fet, només vaig haver de fer servir quatre exemples a la indicació d’entrada perquè funcionés de manera fiable. 

### Indicació d’entrada

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

### Resultats
Els {{< hl >}}[resultats](https://github.com/Pantagrueliste/m-k-manuscript-data/blob/master/bibliographies/essays/EssaysBibliography.bib) són espectaculars: més de 2.000 referències bibliogràfiques convertides en qüestió de dies.{{< /hl >}} Aquest enfocament no només ha reproduït amb exactitud el patró exposat a la meva indicació d’entrada, sinó que també hi ha afegit correctament tipus d’entrada i de camp que no hi figuraven. `GPT-3`, dit d’una altra manera, parla `BibTeX` amb tota fluïdesa. Potser més sorprenent encara, per a un model entrenat essencialment en anglès, ha reconegut totes les llengües (rus, francès, italià, llatí, grec, alemany, castellà, etc.) i ha afegit cada vegada el camp `langid` correcte.

> [!NOTE]
> GPT-3 té actualment una mida d’entrada i de sortida limitada, ja que pot processar un màxim de 2048 tokens lingüístics. Tan bon punt s’aixequi aquesta limitació, la mateixa tasca probablement es farà en una hora o menys.

Una mica inesperadament, GPT-3 també ha afegit informació que no era a les referències originals. 
>Baillot, Anne, and Anna Busch. “Editing for Man and Machine.” In _Users of Scholarly Editions: Editorial Anticipations of Reading, Studying and Consulting_, Vol. 13. Variants (Journal of the European Society for Textual Scholarship). Leicester, 2015. 

En aquesta referència bibliogràfica, per exemple, GPT-3 ha afegit l’enllaç permanent al repositori d’accés obert ([HAL](https://hal.archives-ouvertes.fr)) on es pot llegir l’article, inclosos els camps ad hoc `HAL_ID` i `HAL_VERSION` creats pel repositori HAL: 
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

Aquestes addicions indiquen que {{< hl >}}GPT-3 no només analitza la referència bibliogràfica, sinó que també la completa a partir del que va aprendre inicialment.{{< /hl >}} Seria interessant, en aquest sentit, veure si es comporta igual amb referències posteriors a l’entrenament de GPT-3...

## Limitacions
GPT-3 no és perfecte, però. Cal que un humà el supervisi. Una de les seves limitacions conegudes és l’[al·lucinació](https://arxiv.org/abs/2005.00661): de tant en tant s’inventa coses i fa suposicions improbables. 

En el meu experiment, els rampells d’incoherència de GPT-3 es van fer evidents quan va canviar espontàniament el cognom d’un autor de «Ruscelli» a «Ruscello». Tècnicament no és un error, perquè els cognoms italians de l’inici de l’època moderna es podien fer servir indistintament en plural o en singular. Avui, però, la convenció és que si un cognom és en plural o en singular, s’ha de deixar tal com és. Avui ningú no diria Machiavello per Machiavelli, de la mateixa manera que s’espera que fem servir el nom Rossello i no Rosselli. GPT-3 ha ignorat aquesta convenció per manca de consciència cronològica? O és que ha fet una suposició a partir dels cognoms veïns, que en aquesta part de la bibliografia resulta que estan tots flexionats en singular (Bariletto, Cesano, Rossello)?
Qui ho sap.

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

## Conclusió
Escrits al llarg de quatre anys de col·laboracions intenses, els més de 150 assaigs [inclosos en la nostra edició digital](https://edition640.makingandknowing.org/#/essays) no només aporten informació vital sobre el manuscrit que hem editat i traduït, sinó que també contenen informació bibliogràfica valuosa.

Reunir aquestes referències bibliogràfiques en una base de dades permet als editors canviar el format bibliogràfic en un tres i no res, i els dona més flexibilitat per mostrar aquesta informació com vulguin. La base de dades també aporta informació valuosa sobre l’edició i sobre el projecte que la va fer possible, i obre als estudiosos noves perspectives d’anàlisi. Una base de dades així es pot completar amb gran precisió i en un temps rècord.

Es pot argumentar que s’hi poden esmunyir alguns errors, sobretot per la tendència de GPT-3 a al·lucinar. Però les futures iteracions dels models de llengua preentrenats mitigaran aquest problema.
