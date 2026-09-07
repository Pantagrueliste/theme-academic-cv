---
title: "Nauka kodu dwójkowego z emulatorem telegrafu ITA2"
subtitle: "Wczesna komunikacja cyfrowa, której można dotknąć"
summary: Interaktywna prezentacja kodu telegraficznego ITA2 (Baudota-Murraya), która pomaga studentom uchwycić podstawy kodowania binarnego i działania automatów skończonych
date: "2025-02-13T00:00:00Z"
lastmod: "2025-02-13T00:00:00Z"
draft: false
featured: false
machine_translated: true
image:
  caption: 'Pięciobitowe kody telegraficzne w zestawieniu: ITA2, jego warianty narodowe i niełacińskie oraz odpowiadające im wzory perforacji na taśmie'
  focal_point: "Top"
  placement: 2
  preview_only: false
authors:
- clement
tags:
- Historia cyfrowa
- Programowanie
- Dydaktyka
- Historia informatyki
categories:
- Humanistyka cyfrowa
- Narzędzia dydaktyczne
---
## Abstrakcja, którą można wziąć do ręki
Ten emulator ITA2 to praktyczna pomoc dydaktyczna. Unaoczniając abstrakcyjne pojęcia z zakresu kodowania i pozwalając się nimi bawić, wprowadza studentów w jedno z kluczowych zagadnień informatyki i telekomunikacji – reprezentację binarną, czyli to, jak tekst zamienia się w ciągi jedynek i zer.
Często uczymy tego na sucho; tymczasem widok dziurek pojawiających się na taśmie pomaga studentom pojąć, w jaki sposób fizyczne układy mogą przechowywać informację cyfrową.
{{< Baudot >}}
## Kontekst historyczny: od telegrafu do komputera
Kod ITA2 (Międzynarodowy Alfabet Telegraficzny nr 2), znany też jako kod Baudota-Murraya, opracowano w latach dwudziestych XX wieku jako udoskonalenie pierwotnego kodu telegraficznego Émile'a Baudota z lat siedemdziesiątych XIX wieku. Te wczesne systemy telekomunikacyjne wywarły bezpośredni wpływ na późniejszy rozwój informatyki:
- pięciobitowy schemat kodowania był jednym z pierwszych przykładów kodowania znaków;
- ograniczony zestaw znaków (pięć bitów daje zaledwie 32 kombinacje) wymusił pomysłowy mechanizm przełączania rejestrów LETTERS/FIGURES (litery/cyfry);
- system ten służył dalekopisom jeszcze przez dobrą część XX wieku.
## Automaty skończone przez zabawę
Mechanizm przełączania LETTERS/FIGURES wprowadza pojęcie automatu skończonego w sposób zupełnie naturalny. Studenci sami, eksperymentując, odkrywają, że ten sam wzór może oznaczać różne znaki w zależności od bieżącego trybu. To doświadczenie z kodowaniem zależnym od stanu przygotowuje ich do bardziej złożonych zagadnień informatycznych.
Na przykład ciąg bitów `00011` oznacza:
- literę „A” w trybie LETTERS,
- cyfrę „1” w trybie FIGURES.
Taka podwójna interpretacja zależna od stanu leży u podstaw tego, jak komputery obchodzą się z danymi.
## Ćwiczenia na zajęcia
Oto kilka sposobów wykorzystania emulatora ITA2 w dydaktyce:
1. **Łamanie szyfru**: studenci dekodują wiadomości zapisane jako wzory ITA2.
2. **Oszczędne kodowanie**: dyskusja o tym, dlaczego mechanizm przełączania rejestrów był tak ważny dla oszczędzania pasma.
3. **Ewolucja kodowania**: porównanie pięciobitowego kodu ITA2 z ASCII (7 bitów) i Unicode.
4. **Fizyczna informatyka**: powiązanie tego historycznego systemu ze współczesnymi mikrokontrolerami, takimi jak Arduino.
## Korzyści w zakresie dostępności
Poza walorem historycznym podejście to pomaga studentom o różnych stylach uczenia się:
- wzrokowcy widzą wzory,
- kinestetycy wchodzą w bezpośrednią interakcję z procesem kodowania,
- umysły teoretyczne mogą zgłębiać matematyczną stronę teorii informacji.
## Szczegóły implementacji
Emulator napisano w JavaScripcie i można go łatwo osadzić na dowolnej internetowej platformie edukacyjnej. Kod jest modułowy i daje się dostosować do różnych kontekstów dydaktycznych.
Kod źródłowy oraz działający emulator można znaleźć tu: [Repozytorium GitHub](https://github.com/Pantagrueliste/BaudotMurray_Emulator)
