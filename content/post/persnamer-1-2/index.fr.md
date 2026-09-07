---
title: "persNamer 1.2 : un numéro VIAF, neuf fichiers d’autorité"
subtitle: Le petit outil de personographie fusionne désormais ses notices dans votre fichier TEI et y porte les identifiants des grands catalogues

summary: >
  persNamer prend un numéro VIAF et rend une notice de personne TEI. La
  version 1.2 fait de cette notice quelque chose qui vaut la peine : formes
  variantes du nom, dates normalisées, identifiants de neuf fichiers
  d’autorité nationaux et internationaux, et un mode de fusion qui étoffe une
  personographie existante au lieu d’imprimer des bouts de XML.

date: "2026-09-07T00:00:00Z"
lastmod: "2026-09-07T00:00:00Z"

draft: false
featured: false
machine_translated: true

image:
  caption: ''
  focal_point: "Center"
  placement: 2
  preview_only: false

authors:
- clement

tags:
- TEI
- VIAF
- Données liées
- Humanités numériques
- Python

categories:
- Humanités numériques
---

[persNamer](/code/persnamer/) est né d’une petite commodité : on lui donne un
numéro VIAF, il rend une notice `<person>` en TEI et la balise `<persName>`
qui sert à annoter le texte. Il ne faisait qu’une chose, et la notice qu’il
produisait était maigre – un nom, deux dates, un identifiant. La version 1.2,
publiée aujourd’hui, fait toujours cette seule chose, mais la notice,
désormais, vaut la peine d’être gardée.

## Ce que contient désormais une notice de personne

Le nom, d’abord. Une grappe VIAF porte un nom par bibliothèque contributrice,
et l’ancien persNamer prenait tout bonnement la première étiquette venue.
Demandez-lui Voltaire : il répondait « فولتير، » – la forme arabe, virgule
finale comprise – avec, pour faire bonne mesure, un `xml:id` vide. La
version 1.2 compte les formes à travers la grappe et retient celle sur
laquelle les notices sources s’accordent ; les autres suivent en
`<persName type="variant">`, les plus fréquentes en tête. Les dates sont
normalisées (`1572-08-00` devient `1572-08`) et écrites deux fois, en texte et
dans un attribut `@when`, car c’est lui, et non le texte, que lira en réalité
tout traitement du fichier qui tient compte des dates. Sexe et descriptions
apparaissent quand VIAF les expose.

Ce que je voulais le plus : chaque identifiant que VIAF relie, par
`schema:sameAs` et par ses propres identifiants de source, est écrit dans un
`<idno>` – BnF, GND, Library of Congress, SUDOC, Wikidata, ISNI, BNE, LIBRIS,
NDL. Un numéro à l’entrée, neuf catalogues à la sortie. Pour une
personographie, c’est ce qui sépare une liste de noms d’un nœud dans la toile
des données d’autorité.

```xml
<person xml:id="pers-teligny-c">
  <persName>Charles de Téligny</persName>
  <birth when="1535">1535</birth>
  <death when="1572-08-24">1572-08-24</death>
  <sex value="M">M</sex>
  <idno type="VIAF">314802260</idno>
  <idno type="BNF">16133360</idno>
  <idno type="Wikidata">Q1868249</idno>
  <idno type="ISNI">0000000071126808</idno>
</person>
```

## Des bouts de XML à une personographie

Imprimer du XML dans le terminal convient pour une personne. Une édition en
compte des centaines. persNamer accepte désormais plusieurs numéros VIAF d’un
coup, marque une pause polie entre deux requêtes, met en cache ce qu’il
récupère et – avec `--merge` – insère les nouvelles notices directement dans
le `<listPerson>` d’un fichier TEI existant. Les notices déjà présentes sont
reconnues à leur numéro VIAF et leur `xml:id` est réutilisé ; les nouveaux
identifiants sont confrontés au fichier et suffixés (`-2`, `-3`) s’ils
risquaient d’entrer en collision ; le fichier est réindenté, non sans qu’une
copie `.bak` ait d’abord été écrite.

```bash
persnamer --merge edition.xml 314802260 36925746
```

Un changement à connaître : la particule du nom de famille est désormais
retirée de l’identifiant par défaut, de sorte que Charles de Téligny devient
`pers-teligny-c` et non plus `pers-deteligny-c`. Si votre projet s’est fixé
sur l’ancienne forme, `--keep-particle` la rétablit ; et `--id-format viaf`
donne `pers-viaf-314802260` si vous préférez ne pas dépendre des noms du tout.

## Intendance

Le script est devenu un paquet doté d’une commande `persnamer`, installable
en une ligne avec `uv tool install` ou `pipx` (ou exécutable une fois, sans
rien installer, avec `uvx`). Vingt-six tests tournent sur des réponses VIAF
enregistrées, si bien que la suite se passe de réseau ; l’intégration
continue les fait passer de Python 3.9 à 3.13, et la sortie est validée
contre TEI P5. Apache 2.0, comme avant.

Ce qu’il ne sait toujours pas faire, c’est vous dire où quelqu’un est né ni
ce qu’il faisait dans la vie : le RDF des grappes VIAF ne porte ni lieux ni
professions. Les notices BnF et GND qui y sont liées, elles, les portent – et
vous avez maintenant leurs numéros.

Code et documentation sur
[GitHub](https://github.com/Pantagrueliste/persNamer).
