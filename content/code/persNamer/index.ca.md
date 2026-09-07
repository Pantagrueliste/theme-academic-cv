---
title: persNamer
summary: Una eina en Python que converteix identificadors VIAF en entrades de persona i etiquetes d’anotació TEI XML, i simplifica així el control d’autoritats en les edicions acadèmiques digitals.
tags:
  - XML
  - TEI
  - Humanitats digitals
  - Python
  - VIAF
  - Dades enllaçades

date: "2025-03-28T00:00:00Z"

# Optional external URL for project (replaces project detail page)
external_link: ""

image:
  caption: ''
  focal_point: Smart

links:
  - type: code
    icon: brands/github
    label: Codi
    url: https://github.com/Pantagrueliste/persNamer
url_code: ""
url_pdf: ""
url_slides: ""
url_video: ""

# Slides (optional).
#   Associate this project with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides = "example-slides"` references `content/slides/example-slides.md`.
#   Otherwise, set `slides = ""`.
slides: ""
machine_translated: true
---

## persNamer: connectar la TEI amb el Virtual International Authority File

[![DOI](https://zenodo.org/badge/933156851.svg)](https://doi.org/10.5281/zenodo.14875030)

persNamer és una eina especialitzada en Python que facilita la integració en documents TEI XML de dades d’autoritat sobre persones procedents del VIAF (Virtual International Authority File). En convertir els identificadors VIAF en marcatge TEI a punt per fer servir, persNamer redueix notablement la feina manual que comporta crear entrades de persona estructurades per a les edicions acadèmiques digitals.

## El repte del control d’autoritats en TEI

Les edicions acadèmiques digitals sovint exigeixen identificar amb precisió els personatges històrics, incloent-hi els seus noms normalitzats i les dates de naixement i mort. Mantenir un control d’autoritats coherent en tot un projecte requereix:

1. Identificar les persones en els textos històrics
2. Trobar-ne dades d’autoritat
3. Crear entrades TEI correctament formatades
4. Garantir referències coherents al llarg de tot el projecte

Aquests passos solen ser manuals, lents i propensos a la incoherència.

## Com funciona persNamer

persNamer automatitza aquest flux de treball:

1. **Obté les dades del VIAF**: a partir d’un identificador VIAF, l’eina recupera les dades RDF mitjançant negociació de contingut HTTP
2. **N’extreu la informació clau**: analitza l’RDF per extreure’n el nom preferit, la data de naixement i la data de mort
3. **Genera el marcatge TEI**: crea dos fragments XML essencials:
   - Una **entrada de fitxer d’autoritats** (element `<person>` amb un `xml:id` generat, `<persName>`, `<birth>`, `<death>` i `<idno type="VIAF">`)
   - Una **etiqueta d’anotació** a part (`<persName>` amb un atribut `ref` que apunta a l’entrada d’autoritat)

Aquesta doble sortida permet als editors mantenir un fitxer d’autoritats centralitzat i, alhora, inserir fàcilment etiquetes d’anotació en els seus textos TEI.

## Característiques principals

- **Generació d’identificadors normalitzats**: crea identificadors XML coherents amb el format `pers-[familyname]-[givenname initial]` (p. ex., `pers-deteligny-c`)
- **Anàlisi d’RDF**: fa servir `rdflib` per extreure informació de diverses propietats RDF (p. ex., `rdfs:label`, `schema:name`, `viaf:mainHead`)
- **Interfície de línia d’ordres**: s’executa amb un número VIAF com a únic argument obligatori
- **Sortida detallada**: proporciona informació detallada del processament juntament amb l’XML final

## Exemple d’ús

```bash
python persNamer.py 314802260
```

Aquesta ordre produeix:

```xml
<person xml:id="pers-deteligny-c">
  <persName>Charles deTéligny</persName>
  <birth>1535</birth>
  <death>1572-08-24</death>
  <idno type="VIAF">314802260</idno>
</person>

<persName ref="#pers-deteligny-c">Charles deTéligny</persName>
```

## Aplicacions en humanitats digitals

persNamer és especialment útil per a:

- Edicions acadèmiques digitals que requereixen control d’autoritats
- Projectes de codificació TEI que treballen amb personatges històrics
- Iniciatives de dades enllaçades que connecten documents amb registres d’autoritat
- Garantir la coherència en grans corpus TEI
- Ensenyar els conceptes del control d’autoritats en cursos d’humanitats digitals

## Implementació

persNamer està escrit en Python i depèn de:
- `requests` per a les peticions HTTP
- `rdflib` per a l’anàlisi d’RDF
- `lxml` per a la gestió de l’XML

El codi font i la documentació són al [repositori de GitHub](https://github.com/Pantagrueliste/persNamer).