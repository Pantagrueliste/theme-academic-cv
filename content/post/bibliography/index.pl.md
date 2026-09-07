---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Masowe parsowanie bibliografii za pomocą wstępnie wytrenowanych modeli językowych"
subtitle: "Jak szybko zamienić tysiące odsyłaczy bibliograficznych w bazę BibTeX"
summary: "GPT-3 pomaga w krótkim czasie przekształcić obszerną bibliografię w bazę danych"
authors: [clement]
tags: [Humanistyka cyfrowa, GPT-3, Bibliografia, Automatyzacja]
categories: [Wydajne edytorstwo]
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

Automatyzacja to klucz do obniżenia kosztów projektów z zakresu humanistyki cyfrowej. Do dziś powtarzalne i żmudne zadania związane z pracą edytorską w środowisku akademickim wykonywali albo – wielkim kosztem – przeciążeni badacze, albo „zlecano” je studentom. W tym [cyklu wpisów](https://www.clementgodbarge.com/category/efficient-editing/) dowodzę, że większość tych niewdzięcznych zadań nie tylko *można*, ale i *należy* zautomatyzować. Automatyzacja pracy edytorskiej obniża całkowity koszt projektów humanistyki cyfrowej. Co najważniejsze, pozwala badaczom z uboższych regionów świata szybko i tanio publikować cenne dokumenty.

W [poprzednim wpisie](https://www.clementgodbarge.com/post/gpt3/) pokazałem na przykład, jak wstępnie wytrenowane modele językowe mogą wykonać większość pracy związanej ze znakowaniem XML w edycji cyfrowej. 

W tym wpisie przedstawiam drugi przykład, tym razem dotyczący bibliografii.


## Problem
Zbudowanie bazy bibliograficznej z odsyłaczy przywołanych w jednym artykule naukowym to zadanie dość proste. Można szybko przeszukać katalog taki jak [WorldCat](https://www.worldcat.org), pobrać opis w wybranym formacie albo zaimportować go automatycznie z lokalnej bazy. Przy jednym czy dwóch artykułach to działa bez zarzutu.
Powyżej pewnej liczby odsyłaczy zadanie staje się jednak odstręczające i czasochłonne. Żeby temu zaradzić, można sięgnąć po algorytmy parsujące, takie jak [anystyle.io](https://anystyle.io). Trudno je jednak skalować.
Kiedy użyłem anystyle do przetworzenia ponad 150 esejów naukowych zamieszczonych w naszej [edycji krytycznej Ms Fr 640](https://edition640.makingandknowing.org/#/), liczba nagromadzonych błędów okazała się po prostu nie do opanowania. Program nie rozpoznał wielu naszych źródeł, biorąc na przykład długie tytuły wczesnonowożytnych książek za coś zupełnie innego, i nie radził sobie z mniej typowymi dokumentami, takimi jak konkretne strony internetowe, filmy online itd. Parsery działają dobrze pod warunkiem, że autor skrupulatnie trzyma się reguł znanej konwencji – Chicago, Turabian czy MLA. Każde odstępstwo od normy kończy się błędem.

## Rozwiązanie
Tu właśnie mogą pomóc {{< hl >}}wstępnie wytrenowane modele językowe{{< /hl >}}: {{< hl >}}błyskawicznie chwytają one schemat dowolnego stylu bibliograficznego{{< /hl >}}, nawet własnego wynalazku, i potrzebują zaledwie kilku przykładów, by poprawnie przekształcić obszerną, sformatowaną bibliografię w [bazę BibTeX](http://www.bibtex.org/Format/). 

Na początku 2021 r. miałem szczęście uzyskać wczesny dostęp do [GPT-3 Codex](https://openai.com/blog/openai-codex/) firmy OpenAI. Codex to model, który pozwala tłumaczyć język naturalny na kod i odwrotnie. OpenAI twierdzi, że biegle włada kilkunastoma językami programowania, i choć jego API jest w chwili pisania tego wpisu dostępne jeszcze w wersji beta, napędza już popularne aplikacje, takie jak [Copilot](https://github.com/features/copilot/) GitHuba.

Pobawiwszy się tym API, zorientowałem się, że równie dobrze radzi sobie z prostszym kodem, takim jak `BibTeX`. 

I rzeczywiście: wystarczyły cztery przykłady w prompcie wejściowym, żeby działało niezawodnie. 

### Prompt wejściowy

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

### Wyniki
{{< hl >}}[Wyniki](https://github.com/Pantagrueliste/m-k-manuscript-data/blob/master/bibliographies/essays/EssaysBibliography.bib) są uderzające: ponad 2000 odsyłaczy bibliograficznych przekonwertowanych w ciągu kilku dni.{{< /hl >}} Podejście to nie tylko wiernie odtworzyło schemat z mojego promptu, ale też poprawnie dodało typy wpisów i pól, których w prompcie w ogóle nie było. Innymi słowy, `GPT-3` włada `BibTeX`-em doskonale. Co może bardziej zaskakujące w modelu trenowanym głównie na angielszczyźnie, rozpoznał on wszystkie języki (rosyjski, francuski, włoski, łacinę, grekę, niemiecki, hiszpański itd.), za każdym razem dodając właściwe pole `langid`.

> [!NOTE]
> GPT-3 ma obecnie ograniczony rozmiar wejścia i wyjścia: przetwarza maksymalnie 2048 tokenów. Gdy tylko to ograniczenie zniknie, to samo zadanie zajmie zapewne godzinę lub mniej.

Nieco nieoczekiwanie GPT-3 dodał także informacje, których nie było w pierwotnych odsyłaczach. 
>Baillot, Anne, and Anna Busch. “Editing for Man and Machine.” In _Users of Scholarly Editions: Editorial Anticipations of Reading, Studying and Consulting_, Vol. 13. Variants (Journal of the European Society for Textual Scholarship). Leicester, 2015. 

W tym odsyłaczu, na przykład, GPT-3 dodał trwały link do repozytorium otwartego dostępu ([HAL](https://hal.archives-ouvertes.fr)), w którym można przeczytać artykuł, wraz z polami `HAL_ID` i `HAL_VERSION`, stworzonymi ad hoc przez repozytorium HAL: 
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

Te dodatki wskazują, że {{< hl >}}GPT-3 nie tylko parsuje odsyłacz bibliograficzny, ale też uzupełnia go na podstawie tego, czego nauczył się wcześniej.{{< /hl >}} Ciekawie byłoby w tym kontekście sprawdzić, czy zachowa się podobnie wobec odsyłaczy późniejszych niż jego dane treningowe...

## Ograniczenia
GPT-3 nie jest jednak doskonały. Wymaga nadzoru człowieka. Jednym z jego znanych ograniczeń jest [halucynowanie](https://arxiv.org/abs/2005.00661): czasem wymyśla rzeczy i przyjmuje nieprawdopodobne założenia. 

W moim eksperymencie napady niespójności GPT-3 ujawniły się, gdy samorzutnie zmienił nazwisko autora z „Ruscelli” na „Ruscello”. Technicznie rzecz biorąc, nie jest to błąd, bo wczesnonowożytnych włoskich nazwisk używano w liczbie mnogiej i pojedynczej bez różnicy. Dzisiejsza konwencja każe jednak zostawić nazwisko w takiej formie, w jakiej występuje. Nikt dziś nie nazwałby Machiavellego „Machiavello”, tak jak od nas oczekuje się formy Rossello, a nie Rosselli. Czy GPT-3 zignorował tę konwencję z braku świadomości chronologicznej? A może kierował się sąsiednimi nazwiskami, które w tej części bibliografii akurat wszystkie mają formę liczby pojedynczej (Bariletto, Cesano, Rossello)?
Kto to wie.

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

## Wnioski
Ponad 150 esejów [zamieszczonych w naszej edycji cyfrowej](https://edition640.makingandknowing.org/#/essays), napisanych w ciągu czterech lat intensywnej współpracy, nie tylko dostarcza kluczowych informacji o rękopisie, który wydaliśmy i przetłumaczyliśmy, ale zawiera też cenne dane bibliograficzne.

Zebranie tych odsyłaczy w bazie pozwala wydawcom zmieniać formatowanie bibliografii w mgnieniu oka, dając im więcej swobody w prezentowaniu tych informacji. Baza ta mówi też wiele o samej edycji i o projekcie, który ją umożliwił, otwierając przed badaczami nowe perspektywy analityczne. Taką bazę można sporządzić z dużą dokładnością i w rekordowym czasie.

Owszem, jakieś błędy mogą się wkraść, zwłaszcza z powodu skłonności GPT-3 do halucynowania. Przyszłe iteracje wstępnie wytrenowanych modeli językowych złagodzą jednak ten problem.
