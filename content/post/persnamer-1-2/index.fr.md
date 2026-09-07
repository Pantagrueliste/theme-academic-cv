---
title: "persNamer 1.2 : un numéro VIAF, neuf fichiers d’autorité"
subtitle: Le petit outil de personographie sait maintenant s’insérer dans un fichier TEI existant, et il rapporte au passage les identifiants des grands catalogues

summary: >
  Donnez un numéro VIAF à persNamer, il vous rend une notice TEI. Avec la
  version 1.2, la notice a enfin de la chair : formes variantes du nom, dates
  normalisées, identifiants de neuf fichiers d’autorité, et un mode de fusion
  qui fait grandir une personographie au lieu d’imprimer des bouts de XML.

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

[persNamer](/code/persnamer/) n’était au départ qu’une commodité : un numéro
VIAF en entrée, et en sortie une notice `<person>` en TEI, avec la balise
`<persName>` pour annoter le texte. Rien de plus — et la notice était maigre :
un nom, deux dates, un identifiant. La version 1.2, publiée aujourd’hui, ne
fait toujours qu’une chose, mais elle la fait bien : cette fois, la notice
vaut la peine d’être conservée.

## Ce qu’une notice contient désormais

Commençons par le nom. Dans une grappe VIAF, chaque bibliothèque
contributrice apporte sa forme, et l’ancien persNamer se contentait de la
première venue. Demandez-lui Voltaire : vous obteniez « فولتير، », en arabe,
virgule comprise, et un `xml:id` vide par-dessus le marché. Désormais l’outil
fait le compte des formes et retient celle qui fait consensus parmi les
notices sources ; les autres suivent en `<persName type="variant">`, par
ordre de fréquence. Les dates sont normalisées (`1572-08-00` devient
`1572-08`) et inscrites deux fois : en clair, et dans un attribut `@when` — le
seul que consultera un traitement qui sait lire une date. Le sexe et les
descriptions viennent avec, lorsque VIAF les fournit.

Et puis ce qui me manquait le plus : tous les identifiants que VIAF relie à
la personne, par `schema:sameAs` ou par ses propres identifiants de source,
sont reportés chacun dans un `<idno>` — BnF, GND, Library of Congress, SUDOC,
Wikidata, ISNI, BNE, LIBRIS, NDL. Un numéro entre, neuf catalogues sortent.
Pour une personographie, c’est toute la différence entre une liste de noms et
un nœud dans la toile des données d’autorité.

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

## De bouts de XML à une personographie

Du XML imprimé dans le terminal, cela suffit pour une personne. Une édition
en compte des centaines. persNamer accepte donc plusieurs numéros à la fois,
laisse poliment souffler VIAF entre deux requêtes, garde en cache ce qu’il a
déjà obtenu et, avec `--merge`, insère les nouvelles notices directement dans
le `<listPerson>` d’un fichier TEI existant. Les personnes déjà présentes sont
reconnues à leur numéro VIAF et gardent leur `xml:id` ; les nouveaux
identifiants sont vérifiés contre le fichier et reçoivent un suffixe (`-2`,
`-3`) en cas de doublon ; le tout est réindenté, après qu’une copie `.bak` a
été mise de côté.

```bash
persnamer --merge edition.xml 314802260 36925746
```

Un détail à connaître : par défaut, la particule ne fait plus partie de
l’identifiant — Charles de Téligny devient `pers-teligny-c`, et non plus
`pers-deteligny-c`. Si votre projet a pris ses habitudes avec l’ancienne
forme, `--keep-particle` la rétablit ; et pour qui préfère ne pas dépendre des
noms, `--id-format viaf` donne `pers-viaf-314802260`.

## Intendance

Le script est devenu un paquet en bonne et due forme, avec sa commande
`persnamer` : une ligne suffit pour l’installer (`uv tool install` ou `pipx`),
ou pour l’essayer sans rien installer (`uvx`). Vingt-six tests le vérifient
sur des réponses VIAF enregistrées — pas besoin de réseau — et l’intégration
continue les rejoue de Python 3.9 à 3.13 ; la sortie est validée contre
TEI P5. Licence Apache 2.0, comme avant.

Ce qu’il ne sait toujours pas, c’est où quelqu’un est né ni ce qu’il faisait
dans la vie : le RDF des grappes VIAF ne dit rien des lieux ni des
professions. Les notices de la BnF et de la GND, elles, le savent — et vous
avez maintenant leurs numéros.

Code et documentation sur
[GitHub](https://github.com/Pantagrueliste/persNamer).
