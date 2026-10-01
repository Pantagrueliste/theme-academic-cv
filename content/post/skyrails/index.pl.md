---
title: "Skyrails odbudowany ze zrzutów ekranu"
subtitle: Archeologia cyfrowa, sztuczna inteligencja i starzenie się oprogramowania

summary: >
  Skyrails, niezwykły program do trójwymiarowej eksploracji sieci, którego autorem jest Yose Widjaja, przed laty zniknął z internetu.
  Na podstawie garści zrzutów ekranu Claude odbudował go w ciągu jednej nocy. Potem oryginał odnalazł się na GitHubie i mogliśmy zmierzyć, jak bardzo zbliżyła się do niego rekonstrukcja.

date: "2026-10-01T00:00:00Z"
lastmod: "2026-10-01T00:00:00Z"

draft: false
featured: true
machine_translated: true

image:
  caption: 'Postaci *Nędzników* w odbudowanym Skyrails, z Kozetą na pierwszym planie'
  focal_point: "Center"
  placement: 2
  preview_only: false

authors:
- clement

tags:
- Trwałość
- AI
- Wizualizacja danych

categories:
- Notatki
---

Około 2007 roku Yose Widjaja, wówczas student University of New South Wales, stworzył Skyrails – niezwykły program do eksplorowania sieci w trzech wymiarach. Podróżowało się po samej sieci, od węzła do węzła, wzdłuż świetlistych szyn, jak gdyby było się wewnątrz danych. Program wyglądał jak gra wideo w czasach, gdy większość narzędzi badawczych była płaska i szara. Za efektowną oprawą kryła się prawdziwa głębia: Skyrails miał własny język skryptowy do stylizowania i analizy grafów, a w tym języku napisano menu, dzięki którym mogli z niego korzystać także ci, którzy nie umieli programować. Wszystko to było dziełem jednego studenta. Przed laty zobaczyłem na YouTubie jego demonstrację i nigdy jej nie zapomniałem.


## Program, który przepadł

Skyrails nigdy nie był utrzymywany. Działał pod Windows, jego strona domowa na uniwersytecie zniknęła, a każdy link, w który klikałem, okazywał się martwy. Przetrwały za to ślady: [album zrzutów ekranu na Flickrze](https://www.flickr.com/photos/14933315@N05/albums/72157602730584157/) i garść wpisów blogowych z 2007 roku – na [FlowingData](https://flowingdata.com/?p=947), na blogu Tima Lamberta [*Deltoid*](https://scienceblogs.com/deltoid/2007/10/22/skyrails-graph-visualizations) i na [InfoVis Wiki](https://infovis-wiki.net/wiki/2007-10-27:_Skyrails:_Social_Network_Visualisation_System).

Zrzuty ekranu mówią zaskakująco wiele. Widać na nich nocny błękit nieba poprzecinany smugami chmur, krawędzie rysowane jako animowane szewrony, węzły w postaci ikon lub wykresów kołowych i menu radialne, które rozwija się wokół węzła, gdy przytrzyma się prawy przycisk myszy. Widać nazwy skryptów, które napędzały poszczególne demonstracje (`labs.van`, `macaque.van`, `worldtrade.van`), menu tworzone przez te skrypty i cztery motywy: *normal*, *desert*, *valley* i *openspace*. Jeden ze zrzutów zachował nawet pojedynczą linijkę języka skryptowego, wpisaną do konsoli u góry ekranu:

```
with all nodes do nodeplane x 1 -1 end
```


## Rekonstrukcja z poszlak

Na tej podstawie Claude odbudował Skyrails w ciągu jednej nocy. Nowa wersja, oparta na [Three.js](https://threejs.org/), uruchamia się w przeglądarce i teoretycznie powinna działać także w goglach wirtualnej rzeczywistości. Odwzorowuje niebo, szewronowe szyny, świecące węzły z ich ikonami, wykresami kołowymi i pierścieniami, dużą etykietę węzła pod kursorem, menu radialne i cztery motywy. Ma też niewielki język skryptowy, zbudowany wokół tej jednej linijki, którą zachowały zrzuty, tak że instrukcje `with … do … end` nadają grafowi styl i definiują menu.

Do testów wczytałem trzy klasyczne zbiory danych: sieć florenckich rodów Johna Padgetta, z ich powiązaniami małżeńskimi i handlowymi; klub karate Wayne'a Zachary'ego; wreszcie sieć postaci *Nędzników* Donalda Knutha, w której dwie postaci są połączone, jeśli występują w tym samym rozdziale. Poniższe nagranie przemierza tę ostatnią, od Valjeana do Javerta, Fantyny, Kozety i Mariusza. Każda szyna rozbłyska, gdy sunie wzdłuż niej kamera.

<video controls playsinline preload="metadata" poster="/post/skyrails/poster.jpg" style="width:100%; height:auto; border-radius:4px;">
  <source src="/post/skyrails/skyrails-les-miserables.mp4" type="video/mp4">
  Twoja przeglądarka nie może odtworzyć tego nagrania. Możesz je natomiast <a href="/post/skyrails/skyrails-les-miserables.mp4">pobrać</a>.
</video>

Wynik był tak bliski zrzutom ekranu, że od razu zacząłem podejrzewać, iż model wchłonął w trakcie treningu ślady oryginalnego kodu.


## Odnajduje się oryginał

Wtedy nastąpił zwrot akcji. Już po rekonstrukcji znalazłem oryginalny program na GitHubie. Pewien badacz udostępnił go w 2015 roku, za zgodą Yose Widjai, wraz z kodem do wystąpienia o wizualizacji danych na konferencji poświęconej bezpieczeństwu ShmooCon ([RITHoneynet/DataVisualization](https://github.com/RITHoneynet/DataVisualization), kopia również w [Light0617/3D_UIUX](https://github.com/Light0617/3D_UIUX/tree/master/skyrails/skyrailsdist)). Repozytorium zawiera pliki wykonywalne dla Windows, dane, shadery i oryginalne skrypty, ale nie kod źródłowy głównego silnika.

Mogliśmy więc zestawić obie wersje. Rekonstrukcja zbliżyła się do oryginału wyglądem i charakterem, ale jej język skryptowy i shadery bardzo się od niego różnią. Oryginalne skrypty wyglądają tak:

```
with all edges do (
   if(#marriage == 1) then (
      linkorigin <- marriage -> linktarget;
   ) end;
) end;
```

Podprogramy definiuje się w nich za pomocą `sub`, menu za pomocą `menudef` i `menulink`, kolory zapisem `rgb: 130 0 0`, a typy połączeń – strzałkami. Nic z tego nie pojawia się w rekonstrukcji, która ma z oryginałem wspólną jedynie formę `with … do … end`, widoczną na zrzucie ekranu. Oryginalne shadery, noszące nazwy takie jak `BloomFX` i `RetinalBurnFX`, również nie mają nic wspólnego z nowymi.

Nie rozstrzyga to kwestii zapamiętywania. Oryginalne skrypty są publicznie dostępne od 2015 roku i całkiem możliwe, że trafiły do danych treningowych modelu, a nikt, łącznie z samym modelem, nie potrafi z pewnością powiedzieć, co ten widział. Gdyby jednak model zapamiętał Skyrails, spodziewałbym się, że odtworzyłby przynajmniej język. Różnice sugerują, że Claude oparł się na tym, co dało się wyczytać ze zrzutów ekranu.


## Archeologia cyfrowa i trwałość oprogramowania

Traktuję ten eksperyment jako formę archeologii cyfrowej: odbudowuje się utracony przedmiot ze śladów, które po sobie zostawił, a potem odnajduje oryginał i mierzy, jak blisko udało się podejść. Jak każda rekonstrukcja, nowy Skyrails jest interpretacją. Jego wygląd i zachowanie opierają się na świadectwach, wszystko pod spodem jest natomiast nowe.

To także kwestia trwałości. Oprogramowanie starzeje się znacznie szybciej niż dane, do których odczytywania powstało. Kiedy program umiera, utworzone w nim pliki, skrypty i wizualizacje stają się trudne do otwarcia, nawet jeśli przetrwały. Znaczna część oprogramowania z lat dwutysięcznych istnieje dziś już tylko w postaci zrzutów ekranu, nagrań wideo i starych plików binarnych, które da się uruchomić na coraz mniejszej liczbie maszyn. Oryginalny Skyrails być może wciąż uruchomi się na komputerze z Windows albo w emulatorze, ale nie da się go już utrzymywać, dostosowywać ani przenosić na inne platformy, bo jego kod źródłowy przepadł.

Jak przewidywałem kilka lat temu, AI staje się praktycznym narzędziem w walce z tego rodzaju starzeniem się. Potrafi zrekonstruować utracone narzędzie z jego śladów i odbudować programy do odczytu, dzięki którym stare dane pozostają użyteczne. Oczywistym następnym krokiem w tym projekcie jest nauczenie nowego silnika czytania oryginalnych skryptów `.van` i plików danych, tak by demonstracje, które Yose Widjaja napisał w 2007 roku, mogły znów działać. Dla każdego, komu zależy na trwałości danych – w badaniach naukowych, w archiwach czy w humanistyce cyfrowej – to sprawa warta uwagi.

Skyrails wyprzedzał swoje czasy i prawie dwadzieścia lat później wciąż robi wrażenie. Wszelkie zasługi za pomysł i projekt należą się Yose Widjai i mam nadzieję, że ten tekst do niego dotrze.
