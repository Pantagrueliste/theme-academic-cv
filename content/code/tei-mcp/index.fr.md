---
title: tei-mcp
summary: Un serveur MCP qui aide les agents IA à lire et à écrire du XML TEI valide, grâce à seize outils couvrant la consultation des éléments, la résolution des attributs, le développement des modèles de contenu, le contrôle de l’imbrication, la validation des documents et la personnalisation ODD.
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

## tei-mcp : la TEI P5 à la portée des agents IA

tei-mcp est un serveur [MCP](https://modelcontextprotocol.io) libre qui ouvre aux assistants de programmation un accès direct à la spécification [TEI P5](https://tei-c.org/guidelines/). Au lieu de puiser dans le souvenir de ses données d’entraînement – d’où sort souvent un balisage plausible, mais faux – l’IA interroge la spécification en temps réel.

## Fonctions

Le serveur lit l’ODD de la TEI P5 et expose seize outils :

- **Consulter** tout élément, classe, macro ou module par son nom, sans distinction de casse et avec suggestions en cas de coquille
- **Résoudre les attributs** à travers toute la hiérarchie des classes de la TEI (locaux et hérités)
- **Développer les modèles de contenu** en arbres structurés, avec résolution des classes et des macros
- **Contrôler l’imbrication** – filiation directe ou accessibilité récursive, avec le chemin suivi
- **Valider des documents** contre la TEI P5 : modèles de contenu, attributs, listes de valeurs fermées, intégrité des renvois et avertissements d’obsolescence
- **Valider un élément isolé**, pour l’édition pas à pas
- **Charger des personnalisations ODD**, qui restreignent le schéma au sous-ensemble propre à un projet
- **Chercher** parmi tous les types d’entités au moyen d’expressions régulières

## Installation

```bash
pip install tei-mcp
```

Ou, pour l’exécuter directement :

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

Le code source et la documentation sont sur le [dépôt GitHub](https://github.com/Pantagrueliste/tei-mcp).
