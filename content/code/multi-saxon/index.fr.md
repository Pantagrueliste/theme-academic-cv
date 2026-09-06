---
title: Multi-Saxon
summary: Un outil haute performance pour les transformations XSLT 2.0/3.0 parallèles de grands corpus XML TEI, capable de traiter des transformations que LXML ne peut pas exécuter.
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
  caption: Multi-Saxon en action
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

## Multi-Saxon : traitement XSLT parallèle pour les grands corpus TEI

Multi-Saxon comble une lacune critique des outils de traitement XML en permettant l’exécution parallèle de transformations XSLT 2.0 et 3.0 que LXML (une bibliothèque XML Python très répandue) ne peut pas prendre en charge. Conçu spécifiquement pour les grandes collections de documents XML TEI, Multi-Saxon accélère sensiblement le temps de traitement grâce à une exécution parallèle efficace.

## Fonctionnalités principales

- **Prise en charge avancée de XSLT** : traite les transformations XSLT 2.0 et 3.0, au-delà des capacités de LXML
- **Traitement parallèle** : réduit considérablement le temps de transformation des grandes collections de documents grâce à la parallélisation
- **Optimisé pour la TEI** : spécialement conçu pour les documents XML de la Text Encoding Initiative (TEI)
- **Performance évolutive** : traite efficacement des corpus allant de quelques centaines à plusieurs milliers de documents
- **Multiplateforme** : fonctionne sur différents systèmes d’exploitation et environnements

## Le problème que Multi-Saxon résout

Les chercheurs en humanités numériques qui travaillent avec la TEI se heurtent souvent à deux difficultés majeures :

1. LXML (une bibliothèque Python courante de traitement XML) ne prend en charge que XSLT 1.0, ce qui rend impossible l’utilisation des fonctionnalités plus avancées de XSLT 2.0/3.0
2. Le traitement séquentiel de grands corpus de documents TEI peut prendre un temps prohibitif

Multi-Saxon répond à ces deux problèmes en tirant parti des capacités XSLT avancées de Saxon tout en répartissant le traitement sur plusieurs cœurs, pour des gains de performance significatifs.

## Implémentation

Multi-Saxon combine Python et le processeur Java Saxon pour créer une chaîne de transformation haute performance :

- Utilise la bibliothèque Java Saxon pour un traitement XSLT 2.0/3.0 robuste
- Met en œuvre le multitraitement pour répartir les transformations sur les cœurs de processeur disponibles
- Gère efficacement les pools de processeurs pour maximiser le débit
- Offre une interface simple pour le traitement par lots de documents TEI

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

## Impact pour les humanités numériques

Pour les projets d’humanités numériques qui manipulent de grandes collections de documents TEI, Multi-Saxon permet :

- Des transformations complexes à l’échelle du corpus, impossibles avec LXML
- Des temps de traitement considérablement réduits (souvent d’un facteur 5 à 10 sur les systèmes multicœurs)
- Des analyses plus sophistiquées grâce aux fonctionnalités avancées de XSLT 2.0/3.0
- Un flux de travail simplifié pour le traitement de collections entières de documents

Le code source et la documentation sont disponibles sur le [dépôt GitHub](https://github.com/Pantagrueliste/multi-saxon).
