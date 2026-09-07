---
title: Archiwum na jeden rzut oka
subtitle: Jak interaktywne wizualizacje danych wspomagają badania archiwalne

# Summary for listings and search engines
summary: Aplikacje typu dashboard poprawiają orientację w archiwum, a tym samym jego dostępność i wydajność pracy badaczy

# Link this post with a project
projects: [Filippo Cavriana's Secret Correspondence, 1568—1589.]

# Date published
date: "2021-05-24T16:00:00Z"

# Date updated
lastmod: "2021-05-24T16:00:00Z"

# Is this an unpublished draft?
draft: false

# Show this page in the Featured widget?
featured: false
machine_translated: true

# Featured image
# Place an image named `featured.jpg/png` in this page's folder and customize its options here.
image:
  caption: ''
  focal_point: ""
  placement: 2
  preview_only: false

authors:
- clement

tags:
- Humanistyka cyfrowa
- Wizualizacja danych
- Badania archiwalne
- Bieżące badania

categories:
- Notatki
---

# Problem
Archiwa historyczne bywają przerażająco chaotyczne. Zespół *Mediceo del Principato* w [Archiwum Państwowym we Florencji](https://www.archiviodistato.firenze.it/asfi/home) jest tego najlepszym przykładem. Zinwentaryzowano ledwie niewielką jego część, a wiele dokumentów rozproszono, bez widocznej przyczyny, po ponad 6500 tomach. Na domiar złego archiwum pozwala zamawiać tylko ograniczoną liczbę tomów (czyli *filze* – poszytów, jak się je tam nazywa). W normalnych czasach limit wynosi 4 *filze* dziennie; w czasach pandemii spadł jednak do 4 na dwa tygodnie. Wobec braku szczegółowych inwentarzy ogrom archiwum zmusza badaczy do obmyślania strategii, które pozwolą szybko trafić na poszukiwane dokumenty.

# Rozwiązanie
Jedni zdadzą się na szczęśliwy traf, inni spróbują też stawiać uzasadnione hipotezy na podstawie chronologii, adresatów, autorów, pochodzenia zespołu archiwalnego, języka itd. Kiedy jednak *spojrzeć* na wszystkie te zmienne naraz, mogą się ujawnić nieoczekiwane prawidłowości w strukturze archiwum, a nasze domysły zyskują na trafności. Z mojego doświadczenia wynika, że metadane, które badacze zwykle gromadzą w arkuszu kalkulacyjnym, po przedstawieniu w formie wykresów potrafią znacząco poprawić orientację w archiwum.

# Eksperyment
Moje obecne badania dotyczą korespondencji szesnastowiecznego szpiega. Jego listy rozsiane są po setkach poszytów (*filze*). Pisane pod różnymi tożsamościami, do różnych, czasem zaskakujących adresatów, z różnych miejsc itd. Aby wytypować *filze*, w których z największym prawdopodobieństwem kryją się poszukiwane listy, zbudowałem dashboard – interaktywną aplikację internetową do wizualizacji danych ([Plotly Dash](https://plotly.com/dash/)), która łączy najrozmaitsze dane, w tym informacje geograficzne i chronologiczne, z hierarchicznym diagramem ([sunburst](https://datavizproject.com/data-type/sunburst-diagram/)) zespołu archiwalnego. Dashboard mówi mi na jeden rzut oka, co już znalazłem, ile to stanowi, i podsuwa z grubsza, gdzie mógłbym szukać kolejnych listów. Co więcej, po kliknięciu wybranej zmiennej wszystkie diagramy aktualizują się, ukazując konkretne korelacje.

# Kolejne kroki
Co być może ważniejsze, ten dashboard da się przekształcić w indeks wizualny. Kiedy edycja krytyczna tych listów ukaże się w sieci, dashboard posłuży za alternatywne wejście, z którego czytelnicy będą mogli przeglądać dane. Ze względów poufności mogę na razie pokazać tylko zamazany zrzut ekranu, ale pełny dashboard udostępnię w przyszłym roku. Tymczasem wkrótce pojawi się prototyp. Ciąg dalszy nastąpi!