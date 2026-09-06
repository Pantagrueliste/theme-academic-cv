---
title: Multi-Saxon
summary: Un outil de haute performance pour appliquer en parallèle des transformations XSLT 2.0/3.0 à de grands corpus XML TEI, là où LXML déclare forfait.
tags:
  - XSLT
  - XML
  - TEI
  - Humanités numériques
  - Python
  - Java
  - Performance

date: "2025-03-28T00:00:00Z"

# Optional external URL for project (replaces project detail page)
external_link: ""

image:
  caption: Multi-Saxon à l’œuvre
  focal_point: Smart

links:
  - type: code
    icon: brands/github
    label: Code
    url: https://github.com/Pantagrueliste/multi-saxon
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

## Multi-Saxon : du XSLT en parallèle pour les grands corpus TEI

Multi-Saxon comble une lacune sérieuse de l’outillage XML : il exécute en parallèle des transformations XSLT 2.0 et 3.0 que LXML, la bibliothèque XML la plus répandue en Python, ne sait pas traiter. Conçu tout exprès pour les grandes collections de documents XML TEI, il en abrège sensiblement le traitement par une parallélisation efficace.

## Principales fonctions

- **XSLT de dernière génération** : traite les transformations XSLT 2.0 et 3.0, hors de portée de LXML
- **Traitement parallèle** : la parallélisation abrège considérablement la transformation des grandes collections de documents
- **Taillé pour la TEI** : conçu spécialement pour les documents XML de la Text Encoding Initiative (TEI)
- **Montée en charge** : traite avec la même aisance des corpus de quelques centaines ou de plusieurs milliers de documents
- **Multiplateforme** : fonctionne sur les divers systèmes d’exploitation et environnements

## Le problème que Multi-Saxon résout

Les chercheurs en humanités numériques qui travaillent en TEI butent souvent sur deux obstacles :

1. LXML (bibliothèque Python courante pour le traitement XML) ne connaît que XSLT 1.0, ce qui interdit les fonctions plus avancées de XSLT 2.0/3.0
2. Traiter un grand corpus de documents TEI l’un après l’autre peut prendre un temps rédhibitoire

Multi-Saxon répond aux deux à la fois : il s’appuie sur les capacités XSLT avancées de Saxon, et répartit le traitement sur plusieurs cœurs, d’où des gains de performance considérables.

## Mise en œuvre

Multi-Saxon associe Python au processeur Java Saxon pour former une chaîne de transformation à haute performance :

- il s’appuie sur la bibliothèque Java Saxon pour un traitement XSLT 2.0/3.0 robuste ;
- il recourt au multitraitement pour distribuer les transformations sur les cœurs disponibles ;
- il gère les réserves de processus de façon à maximiser le débit ;
- il offre une interface simple pour traiter les documents TEI par lots.

## Exemple d’utilisation

```python
from multi_saxon import MultiSaxon

# Initialize with your XSLT stylesheet
transformer = MultiSaxon("transform.xsl")

# Transform a single document
transformer.transform("input.xml", "output.xml")

# Transform an entire directory in parallel
transformer.transform_directory("input_dir", "output_dir")
```

## Ce que cela change pour les humanités numériques

Pour les projets qui manipulent de grandes collections de documents TEI, Multi-Saxon rend possibles :

- des transformations complexes à l’échelle du corpus, impossibles avec LXML ;
- des temps de traitement considérablement réduits (souvent d’un facteur 5 à 10 sur les machines multicœurs) ;
- des analyses plus fines, grâce aux fonctions avancées de XSLT 2.0/3.0 ;
- une chaîne de travail simplifiée pour traiter des collections entières.

Le code source et la documentation sont sur le [dépôt GitHub](https://github.com/Pantagrueliste/multi-saxon).
