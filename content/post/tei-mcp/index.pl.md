---
title: "tei-mcp: TEI P5 dla agentów AI"
subtitle: Serwer MCP, który pomaga asystentom AI zrozumieć wytyczne TEI

summary: >
  tei-mcp to serwer MCP open source, który daje asystentom AI do kodowania
  bezpośredni dostęp do specyfikacji TEI P5 – wyszukiwanie elementów, rozwiązywanie
  atrybutów, sprawdzanie zagnieżdżeń, walidacja dokumentów i dostosowania ODD.

date: "2026-03-15T00:00:00Z"
lastmod: "2026-03-15T00:00:00Z"

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

Kto choć raz prosił asystenta AI o napisanie TEI XML, ten zapewne zauważył, 
że coś mu nie wychodzi. Elementy pojawiają się tam, gdzie nie powinny. 
Atrybuty są zmyślone. Reguły zagnieżdżania – ignorowane. Model ma z grubsza 
pojęcie, jak wygląda TEI, ale żadnej pewnej wiedzy o specyfikacji.

tei-mcp rozwiązuje ten problem, dając agentom AI bezpośredni, oparty na 
narzędziach dostęp do wytycznych TEI P5.

{{< toc >}}

## Czym jest MCP?

[Model Context Protocol](https://modelcontextprotocol.io) (MCP) to otwarty 
standard, który pozwala aplikacjom AI łączyć się z zewnętrznymi źródłami danych 
i narzędziami. Można o nim myśleć jak o porcie USB dla AI: jeden protokół, dzięki 
któremu każdy zgodny klient – Claude, Cursor, Windsurf i inne – może się 
podłączyć do wyspecjalizowanych usług.

Serwer MCP udostępnia *narzędzia*, które AI może wywoływać w trakcie rozmowy. 
Zamiast polegać na zapamiętanych danych treningowych, model może odpytać żywe, 
miarodajne źródło.

## Co robi tei-mcp

tei-mcp parsuje specyfikację ODD TEI P5 i udostępnia 16 narzędzi, które 
odpowiadają na najczęstsze pytania edytora czy kodera:

- **Co to za element?** Wyszukaj dowolny element, klasę, makro lub moduł po 
  nazwie, bez rozróżniania wielkości liter i z podpowiedziami przy literówkach.
- **Jakie przyjmuje atrybuty?** Rozwiąż atrybuty w całej hierarchii klas – 
  najpierw lokalne, potem po kolei dziedziczone.
- **Co może się w nim znaleźć?** Rozwiń modele zawartości w ustrukturyzowane 
  drzewa albo pobierz płaską listę dopuszczalnych dzieci.
- **Czy ten element może tu stać?** Sprawdź zagnieżdżenie rodzic–dziecko albo 
  prześledź osiągalność w całej hierarchii elementów.
- **Czy mój dokument jest poprawny?** Zwaliduj plik TEI XML względem 
  specyfikacji: modele zawartości, wartości atrybutów, zamknięte listy wartości, 
  spójność odwołań i ostrzeżenia o elementach przestarzałych.
- **A co z moim schematem projektowym?** Wczytaj plik dostosowania ODD, by 
  zawęzić wszystko powyższe do podzbioru TEI właściwego dla twojego projektu.

## Dlaczego to ważne

Kodowanie w TEI wymaga ciągłego zaglądania do wytycznych. Doświadczeni koderzy 
mają najczęstsze wzorce w małym palcu, ale nawet oni muszą sprawdzać w 
specyfikacji mniej znane elementy czy złożone modele zawartości. Dla asystentów 
AI, które takiej przyswojonej wiedzy nie mają, problem jest poważniejszy: 
halucynują znakowanie, które wygląda wiarygodnie, ale jest błędne.

Z tei-mcp AI nie musi zgadywać. Może sprawdzić odpowiedź w specyfikacji, zanim 
napisze choćby jeden nawias ostry. W rezultacie powstaje znakowanie zgodne 
z TEI P5 – albo z dostosowaniem ODD twojego projektu.

## Pierwsze kroki

Zainstaluj z PyPI:

```bash
pip install tei-mcp
```

Następnie dodaj go do konfiguracji swojego klienta MCP:

```json
{
  "mcpServers": {
    "tei": {
      "command": "uvx",
      "args": ["tei-mcp"]
    }
  }
}
```

Serwer pobiera specyfikację TEI przy pierwszym uruchomieniu i współpracuje 
z każdym klientem zgodnym z MCP.

Kod źródłowy i pełna dokumentacja: 
[github.com/Pantagrueliste/tei-mcp](https://github.com/Pantagrueliste/tei-mcp)
