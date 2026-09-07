---
title: "tei-mcp v0.3: kodowanie TEI bez przepisywania źródła"
subtitle: Kompozycja z blokadą zakresów sprawia, że halucynacje w tekście głównym są niemożliwe z samej konstrukcji

summary: >
  tei-mcp v0.3 wprowadza kompozycję z blokadą zakresów, która uniemożliwia najgroźniejszą
  halucynację w kodowaniu TEI wspomaganym przez AI – ciche przepisywanie źródła.
  Model nigdy nie wpisuje tekstu głównego: rejestruje znaczniki jako przesunięcia,
  a kompozycja kończy się błędem, jeśli zmienił się choć jeden bajt.

date: "2026-05-05T00:00:00Z"
lastmod: "2026-05-05T00:00:00Z"

draft: false
featured: true
machine_translated: true

authors:
- clement

tags:
- Humanistyka cyfrowa
- TEI
- MCP
- AI

categories:
- Humanistyka cyfrowa
---

Kiedy [pisałem o tei-mcp po raz pierwszy](/post/tei-mcp/), celem było
powstrzymanie asystentów AI przed halucynowaniem znakowania TEI. Osadzenie
w schemacie rozwiązało część problemu: mając bezpośredni, oparty na narzędziach
dostęp do specyfikacji P5, model nie musi już zgadywać, co znaczy dany element
ani jakie atrybuty przyjmuje. Wynik przechodzi walidację.

Ale halucynacja w kodowaniu TEI ma dwa oblicza, a schemat wyłapuje tylko jedno
z nich. Walidacja względem specyfikacji mówi, że *znakowanie* jest poprawne.
Nie mówi nic o *tekście*, który to znakowanie obejmuje. A właśnie tam –
w samym tekście – gnieżdżą się groźniejsze halucynacje. Kompozycja z blokadą
zakresów (span-locked composition), główna nowość w v0.3, została
zaprojektowana właśnie po to, by im zapobiegać.

{{< toc >}}

## Halucynacja, której schemat nie wyłapie

Poproś model o zakodowanie szesnastowiecznego francuskiego listu, a często
dostaniesz z powrotem dokument TEI, który wygląda nienagannie. Nagłówek
wypełniony, znaczniki `<persName>` na swoich miejscach, `<dateline>` poprawnie
zbudowany. Przepuść go przez `validate_document` – przejdzie.

Potem porównaj tekst główny ze źródłem.

`mesme` stało się `même`. Przecinek się przesunął. `luy` po cichu
zmodernizowano na `lui`. Zdanie trudne do odczytania w rękopisie zostało
„poprawione” na coś gładszego. Żadnej z tych zmian nikt nie zlecił. Żadna nie
została oznaczona. Dokument jest zgodny ze schematem i po cichu błędny.

W pracy archiwalnej – gdzie zakodowany tekst staje się trwałym zapisem, na
którym polegają czytelnicy, indeksy wyszukiwania i cytowania – to właśnie ten
rodzaj awarii liczy się najbardziej. Zniekształcony znacznik irytuje.
Zmodernizowana pisownia, której nikt nie zauważy przez pięć lat, to skażenie
tekstu.

## Kompozycja z blokadą zakresów

Nowe wydanie (v0.3) zawiera mechanizm zapobiegania halucynacjom wycelowany
dokładnie w ten rodzaj awarii. Cel projektowy: sprawić, by halucynacje
w tekście głównym były niemożliwe z samej konstrukcji, a nie tylko mało
prawdopodobne.

Pomysł jest prosty: **model nigdy nie wpisuje tekstu głównego**.

Zamiast tego przebieg pracy wygląda tak:

1. Model wywołuje `get_source("letter_001")` i otrzymuje źródłowy czysty tekst
   jako niezmienny ciąg znaków.
2. Dla każdego znacznika, który chce zastosować, wywołuje
   `tag_span("letter_001", start, end, element_path, attrs)` – rejestrując
   element TEI na zakresie znaków w źródle.
3. Gdy skończy, wywołuje `compose("letter_001")`. Serwer przeplata
   zarejestrowane znaczniki z pierwotnym czystym tekstem, renderuje końcowy
   dokument TEI, a następnie sprawdza *bajt po bajcie*, czy płaska zawartość
   tekstowa wyrenderowanego dokumentu jest równa źródłu.

Jeśli bajty się zgadzają, dokument wraca. Jeśli nie – jeśli znaczniki modelu
w jakiś sposób implikują tekst główny różniący się od źródła choćby jednym
znakiem – `compose()` zgłasza wyjątek, zamiast zwracać skażony dokument.

W tym przebiegu nie ma ścieżki, na której model wyprodukowałby dokument TEI
z tekstem głównym różnym od źródła. Ten niezmiennik jest mechaniczny, nie
behawioralny. Nie musisz ufać, że model nie halucynuje; musisz ufać
porównaniu `==` dwóch ciągów bajtów.

## Czym to jest, a czym nie jest

Kompozycja z blokadą zakresów jest **uzupełnieniem** osadzenia w schemacie,
nie jego zamiennikiem. Narzędzia osadzające w schemacie (`validate_document`,
`lookup_element`, `valid_children` i reszta pierwotnej szesnastki) pomagają
modelowi wytwarzać *poprawne* TEI. Kompozycja z blokadą zakresów gwarantuje,
że tekst główny wewnątrz tego TEI jest *wierny* źródłu. Przebieg kodowania
nadający się do wdrożenia musi spełniać oba warunki – i teraz oba pokrywa
jeden serwer.

Nie jest to też magiczne lekarstwo na wszystko. `compose()` nie sprawdza
jeszcze, czy zarejestrowane znaczniki są dopuszczalne wedle wczytanego
dostosowania ODD – to zadanie na później. Zarejestrowane znaczniki żyją
w pamięci procesu i nie przetrwają restartu. A pliki źródłowe muszą być
czytelne z miejsca, w którym działa serwer. Wszystko to da się rozwiązać;
nic z tego nie podważa głównego niezmiennika.

## Dlaczego to ważne poza TEI

Ten wzorzec się uogólnia. Zawsze, gdy model ma adnotować, przekształcać lub
obudowywać fragment tekstu – i zawsze, gdy integralność tekstu bazowego liczy
się bardziej niż zdolność modelu do jego „ulepszania” – stosuje się ten sam
kształt rozwiązania. Nie każ modelowi przepisywać tekstu. Każ mu wytwarzać
instrukcje nad tekstem, a deterministycznemu kompozytorowi pozwól je
zastosować pod niezmiennikiem równości.

Dla edycji cyfrowych w szczególności zmienia to zakres tego, co można
odpowiedzialnie zlecić modelowi. Kodowanie staje się nagle zadaniem, które
można delegować bez ręcznego porównywania każdego wyniku ze źródłem. Maszyna
idzie nudną ścieżką; edytor sprawdza znakowanie, nie pisownię.

## Jak pobrać aktualizację

Jeśli masz już zainstalowany tei-mcp:

```bash
uvx tei-mcp@latest
```

Albo od zera:

```bash
pip install tei-mcp
```

Aby korzystać z kompozycji z blokadą zakresów, wskaż serwerowi katalog
z plikami źródłowymi w postaci czystego tekstu:

```bash
export TEI_MCP_SPAN_SOURCE_ROOT=/path/to/sources
uvx tei-mcp
```

Rdzeń nazwy każdego pliku staje się identyfikatorem dokumentu (`letter_001.txt` →
`letter_001`).

Kod źródłowy, pełna dokumentacja i notatki projektowe dotyczące niezmiennika:
[github.com/Pantagrueliste/tei-mcp](https://github.com/Pantagrueliste/tei-mcp)
