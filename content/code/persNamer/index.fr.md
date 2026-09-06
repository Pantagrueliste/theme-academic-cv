---
title: persNamer
summary: Un outil Python qui change les identifiants VIAF en notices de personnes et en balises d’annotation TEI XML, et allège ainsi le contrôle d’autorité dans les éditions savantes numériques.
tags:
  - XML
  - TEI
  - Humanités numériques
  - Python
  - VIAF
  - Données liées

date: "2025-03-28T00:00:00Z"

# Optional external URL for project (replaces project detail page)
external_link: ""

image:
  caption: Démonstration de persNamer
  focal_point: Smart

links:
  - type: code
    icon: brands/github
    label: Code
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

## persNamer : relier la TEI au Virtual International Authority File

[![DOI](https://zenodo.org/badge/933156851.svg)](https://doi.org/10.5281/zenodo.14875030)

persNamer est un petit outil Python qui facilite l’intégration, dans des documents TEI XML, des données d’autorité sur les personnes que fournit le VIAF (Virtual International Authority File, ou Fichier d’autorité international virtuel). En changeant les identifiants VIAF en balisage TEI prêt à l’emploi, il épargne à l’éditeur une bonne part du travail manuel qu’exige la création de notices de personnes structurées dans une édition savante numérique.

## Le contrôle d’autorité en TEI : une corvée

Les éditions savantes numériques exigent souvent d’identifier avec précision les personnages historiques, formes normalisées des noms et dates de vie comprises. Tenir un contrôle d’autorité cohérent sur l’ensemble d’un projet suppose de :

1. repérer les personnes dans les textes historiques ;
2. trouver à leur sujet des données faisant autorité ;
3. rédiger des notices TEI correctement formées ;
4. garantir l’uniformité des renvois dans tout le projet.

Autant d’étapes qui se font d’ordinaire à la main, qui prennent du temps et où se glissent des incohérences.

## Comment persNamer procède

persNamer automatise cette chaîne de travail en :

1. **allant chercher les données VIAF** : à partir d’un identifiant VIAF, l’outil récupère les données RDF par négociation de contenu HTTP ;
2. **en extrayant l’essentiel** : il lit le RDF pour en tirer la forme retenue du nom, la date de naissance et la date de décès ;
3. **produisant le balisage TEI** : il crée deux fragments XML essentiels :
   - une **notice de fichier d’autorité** (élément `<person>` muni d’un `xml:id` généré, `<persName>`, `<birth>`, `<death>` et `<idno type="VIAF">`) ;
   - une **balise d’annotation** distincte (`<persName>` dont l’attribut `ref` renvoie à la notice d’autorité).

Grâce à cette double sortie, l’éditeur tient un fichier d’autorité centralisé tout en insérant sans effort les balises d’annotation dans ses textes TEI.

## Principales fonctions

- **Identifiants normalisés** : produit des identifiants XML uniformes, de la forme `pers-[familyname]-[givenname initial]` (par ex. `pers-deteligny-c`)
- **Lecture du RDF** : s’appuie sur `rdflib` pour extraire l’information de diverses propriétés RDF (par ex. `rdfs:label`, `schema:name`, `viaf:mainHead`)
- **Interface en ligne de commande** : s’exécute simplement, le numéro VIAF étant le seul argument obligatoire
- **Sortie détaillée** : rend compte du traitement en détail, en plus du XML final

## Exemple d’utilisation

```bash
python persNamer.py 314802260
```

Cette commande produit :

```xml
<person xml:id="pers-deteligny-c">
  <persName>Charles deTéligny</persName>
  <birth>1535</birth>
  <death>1572-08-24</death>
  <idno type="VIAF">314802260</idno>
</person>

<persName ref="#pers-deteligny-c">Charles deTéligny</persName>
```

## Usages en humanités numériques

persNamer rend particulièrement service pour :

- les éditions savantes numériques qui exigent un contrôle d’autorité ;
- les projets d’encodage TEI qui mettent en scène des personnages historiques ;
- les initiatives de données liées qui rattachent des documents à des notices d’autorité ;
- l’uniformité des grands corpus TEI ;
- l’enseignement du contrôle d’autorité dans les cours d’humanités numériques.

## Mise en œuvre

persNamer est écrit en Python et dépend de :
- `requests` pour les requêtes HTTP
- `rdflib` pour la lecture du RDF
- `lxml` pour la manipulation du XML

Le code source et la documentation sont sur le [dépôt GitHub](https://github.com/Pantagrueliste/persNamer).
