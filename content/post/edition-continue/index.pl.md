---
title: "Stare nawyki, nowe narzędzia"
subtitle: Lekcja dla Programming Historian o publikowaniu edycji krytycznej w rytmie kodowania

summary: >
  Od pół wieku mamy komputery, a edycje cyfrowe wciąż przygotowujemy tak, jakby były drukowanymi książkami.
  Moja nowa lekcja dla Programming Historian en français, pierwsza z dwóch części, przedstawia elementy składowe
  edycji publikowanej w rytmie jej kodowania.

date: "2026-10-02T00:00:00Z"
lastmod: "2026-10-02T00:00:00Z"

draft: false
featured: true
machine_translated: true

image:
  caption: 'Tkacz przy krośnie żakardowym, z łańcuchem kart perforowanych, który programuje wzór. Fot.: [*IEEE Spectrum*](https://spectrum.ieee.org/the-jacquard-loom-a-driver-of-the-industrial-revolution)'
  focal_point: "Center"
  placement: 2
  preview_only: false

authors:
- clement

tags:
- Humanistyka cyfrowa
- Edycje cyfrowe
- Edytorstwo naukowe
- TEI

categories:
- Humanistyka cyfrowa

projects: [DCE]
---

Wczesnonowożytni humaniści, którzy przyswoili sobie druk, nadali edycji kształt zachowany do dziś: tekst się ustala, składa, publikuje raz i poprawia – jeśli w ogóle – w drugim wydaniu wiele lat później. Komputery mamy od pół wieku, a edycje cyfrowe wciąż robimy tak, jakby były drukowanymi książkami. Kończymy tekst, publikujemy go za jednym zamachem, a erratę odkładamy na później. Narzędzia są nowe, nawyki – stare.

Moja nowa lekcja dla *Programming Historian en français*, [„L’édition critique en continu : publier au rythme de l’encodage (Partie 1)”](https://programminghistorian.org/fr/lecons/edition-critique-continu-pt1), łapie nowe narzędzia za słowo. Jeśli kodowanie TEI jest kodem – a jest – to można je wersjonować, walidować i przekształcać jak każdy kod. Programiści dawno przestali czekać na gotowy produkt: każda zmiana jest automatycznie sprawdzana i wydawana, gdy tylko przejdzie testy. Nic nie stoi na przeszkodzie, by edycja krytyczna działała tak samo: publikowała każdy list, gdy tylko zostanie zakodowany i sprawdzony, i poprawiała go jawnie, ilekroć pojawi się lepsze odczytanie.


## Część pierwsza: cegiełki

Pierwsza część przedstawia elementy, które uwalniają edytora od odziedziczonego sposobu pracy, wszystkie otwartoźródłowe:

- plik **ODD**, jedyny dokument, w którym zapisano reguły kodowania w projekcie;
- wygenerowany z niego **schemat RELAX NG**, który egzekwuje strukturę;
- **reguły Schematron**, które dokładają ograniczenia edytorskie niewyrażalne w samym schemacie;
- **skrypt walidacyjny**, który jednym poleceniem sprawdza cały korpus i za pomocą XSLT generuje czytelne wyniki.

Przykłady pochodzą z korespondencji Filippa Cavriany, której edycję [buduję właśnie według tych zasad](/post/cavriana-edition/). Część druga doda łańcuch spinający te elementy, tak by każda zmiana w korpusie była walidowana i publikowana na bieżąco. Lekcja powstała w ramach mojego projektu [Wydajne edytorstwo](/project/dce/), który szuka sposobów na obniżenie kosztów edycji naukowych; automatyzacja publikacji – dzięki której edytor nie musi już czekać na specjalistę na końcu łańcucha – to jedna z największych oszczędności, jakie da się osiągnąć.


## Oburzenie, wyparcie albo kosmetyka

Sztuczną inteligencję przyjmuje się według tego samego schematu: oburzenie, wyparcie albo powierzchowne przyswojenie. To jeden z powodów, dla których lubię humanistykę cyfrową: mało która dziedzina obnaża ten paradoks tak dobitnie. Nowe narzędzia powinny być zaproszeniem do przemyślenia na nowo, jak pracować lepiej, a nie świeżą warstwą farby na starych nawykach. Ta lekcja przyjmuje to zaproszenie w imieniu edytorstwa naukowego. Ciąg dalszy nastąpi w części drugiej.

Dziękuję wszystkim, bez których ta lekcja by nie powstała. Redakcja: Daphné Mathelier i Matthias Gille Levenson. Recenzje: Jasmin Macarios i Elsa Van Kote. Nieoceniona pomoc: Anisa Hawes.

Lekcja ukazała się w otwartym dostępie: [programminghistorian.org/fr/lecons/edition-critique-continu-pt1](https://programminghistorian.org/fr/lecons/edition-critique-continu-pt1) (DOI: [10.46430/phfr0044](https://doi.org/10.46430/phfr0044)).
