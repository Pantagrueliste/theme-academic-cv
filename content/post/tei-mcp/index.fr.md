---
title: "tei-mcp : la TEI P5 pour les agents IA"
subtitle: Un serveur MCP qui aide les assistants IA à comprendre les Guidelines de la TEI

summary: >
  tei-mcp est un serveur MCP open source qui donne aux assistants de programmation IA
  un accès direct à la spécification TEI P5 – consultation des éléments, résolution
  des attributs, validation de l’imbrication, validation de documents et
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

Si vous avez déjà utilisé un assistant de programmation IA pour écrire du XML TEI, 
vous avez probablement remarqué qu’il se trompe. Des éléments apparaissent là où 
ils ne devraient pas. Des attributs sont inventés. Les règles d’imbrication sont 
ignorées. Le modèle a une idée approximative de ce à quoi ressemble la TEI, mais 
aucune connaissance fiable de la spécification.

tei-mcp résout ce problème en donnant aux agents IA un accès direct, sous forme 
d’outils, aux Guidelines de la TEI P5.

{{< toc >}}

## Qu’est-ce que MCP ?

Le [Model Context Protocol](https://modelcontextprotocol.io) (MCP) est un standard 
ouvert qui permet aux applications d’IA de se connecter à des sources de données et 
à des outils externes. Voyez-le comme un port USB pour l’IA : un protocole unique 
qui permet à n’importe quel client compatible – Claude, Cursor, Windsurf et 
d’autres – de se brancher sur des services spécialisés.

Un serveur MCP expose des *outils* que l’IA peut appeler au cours d’une conversation. 
Au lieu de se fier à des données d’entraînement mémorisées, le modèle peut interroger 
une source vivante et faisant autorité.

## Ce que fait tei-mcp

tei-mcp analyse la spécification ODD de la TEI P5 et expose 16 outils qui couvrent 
les questions les plus courantes qu’un éditeur ou un encodeur peut se poser :

- **Qu’est-ce que cet élément ?** Recherchez n’importe quel élément, classe, macro 
  ou module par son nom, avec une correspondance insensible à la casse et des 
  suggestions en cas de faute de frappe.
- **Quels attributs accepte-t-il ?** Résolvez les attributs à travers toute la 
  hiérarchie de classes – les attributs locaux d’abord, puis les attributs hérités, 
  dans l’ordre.
- **Que peut-il contenir ?** Développez les modèles de contenu en arbres structurés, 
  ou obtenez une liste plate des enfants valides.
- **Cet élément peut-il aller ici ?** Vérifiez l’imbrication parent-enfant, ou 
  tracez l’accessibilité à travers toute la hiérarchie des éléments.
- **Mon document est-il valide ?** Validez un fichier XML TEI par rapport à la 
  spécification : modèles de contenu, valeurs d’attributs, listes de valeurs 
  fermées, intégrité des références et avertissements d’obsolescence.
- **Et mon schéma de projet ?** Chargez un fichier de personnalisation ODD pour 
  restreindre tout ce qui précède au sous-ensemble de la TEI propre à votre projet.

## Pourquoi c’est important

L’encodage TEI exige de se référer constamment aux Guidelines. Les encodeurs 
expérimentés intériorisent les schémas les plus courants, mais même eux doivent 
consulter la spécification pour les éléments moins familiers ou les modèles de 
contenu complexes. Pour les assistants IA, qui n’ont pas cette connaissance 
intériorisée, le problème est pire : ils hallucinent un balisage d’apparence 
plausible mais incorrect.

Avec tei-mcp, l’IA n’a plus à deviner. Elle peut chercher la réponse dans la 
spécification avant d’écrire le moindre chevron. Le résultat est un balisage 
conforme à la TEI P5 – ou à la personnalisation ODD de votre projet.

## Pour commencer

Installez depuis PyPI :

```bash
pip install tei-mcp
```

Puis ajoutez-le à la configuration de votre client MCP :

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

Le serveur télécharge la spécification TEI au premier lancement et fonctionne avec 
n’importe quel client compatible MCP.

Code source et documentation complète : 
[github.com/Pantagrueliste/tei-mcp](https://github.com/Pantagrueliste/tei-mcp)
