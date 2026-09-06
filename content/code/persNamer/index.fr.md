---
title: persNamer
summary: Un outil Python qui convertit les identifiants VIAF en entrées de personnes et en balises d’annotation TEI XML, simplifiant le contrôle d’autorité dans les éditions savantes numériques.
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

persNamer est un outil Python spécialisé qui simplifie l’intégration de données d’autorité sur les personnes provenant du VIAF (Virtual International Authority File, ou Fichier d’autorité international virtuel) dans des documents TEI XML. En convertissant les identifiants VIAF en balisage TEI prêt à l’emploi, persNamer réduit considérablement le travail manuel nécessaire à la création d’entrées de personnes structurées pour les éditions savantes numériques.

## Le défi du contrôle d’autorité en TEI

Les éditions savantes numériques exigent souvent une identification précise des personnages historiques, y compris leurs noms normalisés et leurs dates de vie. Maintenir un contrôle d’autorité cohérent dans un projet suppose de :

1. Identifier les personnes dans les textes historiques
2. Trouver des données d’autorité à leur sujet
3. Créer des entrées TEI correctement formatées
4. Garantir la cohérence des références dans tout le projet

Ces étapes sont généralement manuelles, chronophages et sujettes aux incohérences.

## Comment fonctionne persNamer

persNamer automatise ce flux de travail en :

1. **Récupérant les données VIAF** : à partir d’un identifiant VIAF, l’outil récupère les données RDF par négociation de contenu HTTP
2. **Extrayant les informations clés** : il analyse le RDF pour en extraire le nom privilégié, la date de naissance et la date de décès
3. **Générant le balisage TEI** : il crée deux fragments XML essentiels :
   - une **entrée de fichier d’autorité** (élément `<person>` avec un `xml:id` généré, `<persName>`, `<birth>`, `<death>` et `<idno type="VIAF">`)
   - une **balise d’annotation** distincte (`<persName>` avec un attribut `ref` renvoyant à l’entrée d’autorité)

Cette double sortie permet aux éditeurs de maintenir un fichier d’autorité centralisé tout en insérant facilement des balises d’annotation dans leurs textes TEI.

## Fonctionnalités principales

- **Génération d’identifiants normalisés** : crée des identifiants XML cohérents au format `pers-[familyname]-[givenname initial]` (p. ex. `pers-deteligny-c`)
- **Analyse RDF** : utilise `rdflib` pour extraire les informations de diverses propriétés RDF (p. ex. `rdfs:label`, `schema:name`, `viaf:mainHead`)
- **Interface en ligne de commande** : exécution simple, avec un numéro VIAF comme seul argument obligatoire
- **Sortie détaillée** : fournit des informations détaillées sur le traitement en plus de la sortie XML finale

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

## Applications en humanités numériques

persNamer est particulièrement utile pour :

- Les éditions savantes numériques nécessitant un contrôle d’autorité
- Les projets d’encodage TEI portant sur des personnages historiques
- Les initiatives de données liées reliant des documents à des notices d’autorité
- Garantir la cohérence de grands corpus TEI
- Enseigner les concepts du contrôle d’autorité dans les cours d’humanités numériques

## Implémentation

persNamer est implémenté en Python et dépend de :
- `requests` pour les requêtes HTTP
- `rdflib` pour l’analyse RDF
- `lxml` pour la manipulation XML

Le code source et la documentation sont disponibles sur le [dépôt GitHub](https://github.com/Pantagrueliste/persNamer).
