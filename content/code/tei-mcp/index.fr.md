---
title: tei-mcp
summary: Un serveur MCP qui aide les agents IA à lire et à écrire du XML TEI valide, avec 16 outils couvrant la consultation des éléments, la résolution des attributs, le développement des modèles de contenu, la validation de l’imbrication, la validation de documents et la personnalisation ODD.
tags:
  - XML
  - TEI
  - Humanités numériques
  - Python
  - MCP
  - IA

date: "2026-03-15T00:00:00Z"

external_link: ""

image:
  caption: Bannière de démarrage de tei-mcp
  focal_point: Smart

links:
  - type: code
    icon: brands/github
    label: Code
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

## tei-mcp : la TEI P5 pour les agents IA

tei-mcp est un serveur [MCP](https://modelcontextprotocol.io) open source qui donne aux assistants de programmation IA un accès direct à la spécification [TEI P5](https://tei-c.org/guidelines/). Au lieu de se fier à des données d’entraînement mémorisées – ce qui produit souvent un balisage plausible mais incorrect – l’IA peut interroger la spécification en temps réel.

## Fonctionnalités

Le serveur analyse l’ODD de la TEI P5 et expose 16 outils :

- **Rechercher** n’importe quel élément, classe, macro ou module par son nom, avec correspondance insensible à la casse et suggestions en cas de faute de frappe
- **Résoudre les attributs** à travers toute la hiérarchie de classes de la TEI (locaux + hérités)
- **Développer les modèles de contenu** en arbres structurés, avec résolution des classes et des macros
- **Valider l’imbrication** – relation parent-enfant directe ou accessibilité récursive, avec suivi du chemin
- **Valider des documents** par rapport à la TEI P5 : modèles de contenu, attributs, listes de valeurs fermées, intégrité des références et avertissements d’obsolescence
- **Valider des éléments isolés** pour les flux de travail d’édition incrémentale
- **Charger des personnalisations ODD** pour restreindre le schéma à un sous-ensemble propre au projet
- **Chercher** parmi tous les types d’entités avec des expressions régulières

## Installation

```bash
pip install tei-mcp
```

Ou exécutez-le directement avec :

```bash
uvx tei-mcp
```

## Utilisation

Ajoutez-le à n’importe quel client compatible MCP (Claude, Cursor, Windsurf, etc.) :

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

Le code source et la documentation sont disponibles sur le [dépôt GitHub](https://github.com/Pantagrueliste/tei-mcp).
