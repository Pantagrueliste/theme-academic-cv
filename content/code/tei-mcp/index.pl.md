---
title: tei-mcp
summary: Serwer MCP, który pomaga agentom AI czytać i pisać poprawny TEI XML; jego 16 narzędzi obejmuje wyszukiwanie elementów, rozwiązywanie atrybutów, rozwijanie modeli zawartości, sprawdzanie zagnieżdżeń, walidację dokumentów i dostosowania ODD.
tags:
  - XML
  - TEI
  - Humanistyka cyfrowa
  - Python
  - MCP
  - AI

date: "2026-03-15T00:00:00Z"

external_link: ""

image:
  caption: baner startowy tei-mcp
  focal_point: Smart

links:
  - type: code
    icon: brands/github
    label: Kod
    url: https://github.com/Pantagrueliste/tei-mcp
  - type: site
    icon: brands/python
    label: PyPI
    url: https://pypi.org/project/tei-mcp/
url_code: ""
url_pdf: ""
url_slides: ""
url_video: ""

slides: ""
machine_translated: true
---

## tei-mcp: TEI P5 dla agentów AI

tei-mcp to serwer [MCP](https://modelcontextprotocol.io) open source, który daje asystentom AI do kodowania bezpośredni dostęp do specyfikacji [TEI P5](https://tei-c.org/guidelines/). Zamiast polegać na zapamiętanych danych treningowych – co często daje znakowanie wiarygodne z pozoru, lecz błędne – AI może odpytywać specyfikację w czasie rzeczywistym.

## Funkcje

Serwer parsuje ODD TEI P5 i udostępnia 16 narzędzi:

- **Wyszukiwanie** dowolnego elementu, klasy, makra lub modułu po nazwie, bez rozróżniania wielkości liter i z podpowiedziami przy literówkach
- **Rozwiązywanie atrybutów** w całej hierarchii klas TEI (lokalne + dziedziczone)
- **Rozwijanie modeli zawartości** w ustrukturyzowane drzewa, z rozwiązywaniem klas i makr
- **Sprawdzanie zagnieżdżeń** – bezpośrednia relacja rodzic–dziecko lub rekurencyjna osiągalność ze śledzeniem ścieżki
- **Walidacja dokumentów** względem TEI P5: modele zawartości, atrybuty, zamknięte listy wartości, spójność odwołań i ostrzeżenia o elementach przestarzałych
- **Walidacja pojedynczych elementów** na potrzeby przyrostowej edycji
- **Wczytywanie dostosowań ODD**, by zawęzić schemat do podzbioru właściwego dla projektu
- **Przeszukiwanie** wszystkich typów encji wyrażeniami regularnymi

## Instalacja

```bash
pip install tei-mcp
```

Albo uruchom bezpośrednio:

```bash
uvx tei-mcp
```

## Użycie

Dodaj do dowolnego klienta zgodnego z MCP (Claude, Cursor, Windsurf itd.):

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

Kod źródłowy i dokumentację znajdziesz w [repozytorium GitHub](https://github.com/Pantagrueliste/tei-mcp).
