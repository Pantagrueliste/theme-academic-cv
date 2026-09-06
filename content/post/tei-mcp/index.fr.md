---
title: "tei-mcp : la TEI P5 à la portée des agents IA"
subtitle: Un serveur MCP qui met les Guidelines de la TEI sous les yeux des assistants IA

summary: >
  tei-mcp est un serveur MCP libre qui ouvre aux assistants de programmation
  un accès direct à la spécification TEI P5 – consultation des éléments, résolution
  des attributs, contrôle de l’imbrication, validation des documents et
  personnalisation ODD.

date: "2026-03-15T00:00:00Z"
lastmod: "2026-03-15T00:00:00Z"

draft: false
featured: true
machine_translated: true

authors:
- clement

tags:
- Humanités numériques
- TEI
- MCP
- IA

categories:
- Humanités numériques
---

Quiconque a demandé à un assistant IA d’écrire du XML TEI l’a constaté : 
il se trompe. Des éléments surgissent là où ils n’ont rien à faire, des attributs 
sont inventés de toutes pièces, les règles d’imbrication sont foulées aux pieds. 
Le modèle a une vague idée de ce à quoi ressemble la TEI ; de la spécification 
elle-même, il n’a aucune connaissance sûre.

tei-mcp y remédie en donnant aux agents IA un accès direct, par des outils, 
aux Guidelines de la TEI P5.

{{< toc >}}

## Qu’est-ce que MCP ?

Le [Model Context Protocol](https://modelcontextprotocol.io) (MCP) est une norme 
ouverte qui permet aux applications d’IA de se relier à des sources de données et 
à des outils extérieurs. C’est, si l’on veut, le port USB de l’IA : un protocole 
unique grâce auquel n’importe quel client compatible – Claude, Cursor, Windsurf 
et d’autres – se branche sur des services spécialisés.

Un serveur MCP expose des *outils* que l’IA peut appeler au fil de la conversation ; 
au lieu de puiser dans le souvenir de ses données d’entraînement, le modèle 
interroge une source vivante, qui fait autorité.

## Ce que fait tei-mcp

tei-mcp lit la spécification ODD de la TEI P5 et expose seize outils, qui répondent 
aux questions que se posent le plus souvent un éditeur ou un encodeur :

- **Qu’est-ce que cet élément ?** Recherche de tout élément, classe, macro ou 
  module par son nom, sans distinction de casse et avec suggestions en cas de 
  coquille.
- **Quels attributs admet-il ?** Résolution des attributs à travers toute la 
  hiérarchie des classes – d’abord les attributs locaux, puis les attributs 
  hérités, dans l’ordre.
- **Que peut-il contenir ?** Développement des modèles de contenu en arbres 
  structurés, ou simple liste des enfants admis.
- **Cet élément a-t-il sa place ici ?** Contrôle de l’imbrication parent-enfant, 
  ou recherche d’un chemin à travers toute la hiérarchie des éléments.
- **Mon document est-il valide ?** Validation d’un fichier XML TEI contre la 
  spécification : modèles de contenu, valeurs d’attributs, listes de valeurs 
  fermées, intégrité des renvois et avertissements d’obsolescence.
- **Et le schéma de mon projet ?** Chargement d’un fichier de personnalisation ODD, 
  qui restreint tout ce qui précède au sous-ensemble de la TEI propre à votre projet.

## Pourquoi cela compte

Encoder en TEI, c’est avoir sans cesse les Guidelines sous la main. Les encodeurs 
chevronnés ont intériorisé les tournures les plus courantes, mais eux-mêmes doivent 
retourner à la spécification pour les éléments moins familiers ou les modèles de 
contenu complexes. Pour les assistants IA, qui n’ont rien intériorisé du tout, le 
mal est pire : ils hallucinent un balisage d’aspect plausible, et faux.

Avec tei-mcp, l’IA n’a plus à deviner. Elle va chercher la réponse dans la 
spécification avant d’écrire le moindre chevron, et le balisage qui en sort est 
conforme à la TEI P5 – ou à la personnalisation ODD de votre projet.

## Premiers pas

Installation depuis PyPI :

```bash
pip install tei-mcp
```

Puis ajoutez le serveur à la configuration de votre client MCP :

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

Au premier lancement, le serveur télécharge la spécification TEI ; il fonctionne 
avec tout client compatible MCP.

Code source et documentation complète : 
[github.com/Pantagrueliste/tei-mcp](https://github.com/Pantagrueliste/tei-mcp)
