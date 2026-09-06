---
title: "tei-mcp v0.3 : encoder en TEI sans toucher à la source"
subtitle: Avec la composition à empans verrouillés, l’hallucination dans le corps du texte devient impossible par construction

summary: >
  La nouvelle version de tei-mcp introduit la composition à empans verrouillés,
  un dispositif qui prévient l’hallucination la plus dommageable de l’encodage TEI
  assisté par IA : la réécriture silencieuse du texte source. Le modèle ne tape
  jamais le corps du texte ; il enregistre ses balises comme des positions dans la
  source, et le compositeur refuse de rendre tout document TEI dont le texte nu
  s’écarte de l’original, fût-ce d’un seul octet.

date: "2026-05-05T00:00:00Z"
lastmod: "2026-05-05T00:00:00Z"

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

Quand j’ai [présenté tei-mcp pour la première fois](/post/tei-mcp/), il
s’agissait d’empêcher les assistants IA d’halluciner du balisage TEI. L’ancrage
dans le schéma a réglé une partie du problème : dès lors qu’il accède, par des
outils, à la spécification P5, le modèle n’a plus à deviner ce que signifie un
élément ni quels attributs il admet. Ce qu’il produit est valide.

Mais l’hallucination, en TEI, a deux visages, et le schéma n’en démasque qu’un.
Valider contre la spécification vous assure que le *balisage* est bien formé ;
cela ne dit rien du *texte* que ce balisage enveloppe. Or c’est là, dans le texte
même, que nichent les hallucinations les plus dommageables. La composition à
empans verrouillés (*span-locked composition*), pièce maîtresse de la v0.3, a
été conçue tout exprès pour les rendre impossibles.

{{< toc >}}

## L’hallucination qui échappe au schéma

Demandez à un modèle d’encoder une lettre française du XVI^e^ siècle : vous
recevrez souvent un document TEI d’allure impeccable. L’en-tête est rempli, les
`<persName>` sont à leur place, la `<dateline>` est bien formée. Passez-le à
`validate_document` : il est reçu.

Comparez maintenant le corps du texte à la source.

`mesme` est devenu `même`. Une virgule a changé de place. `luy` a été modernisé
en `lui` sans un mot. Une proposition malaisée à lire dans le manuscrit a été
« corrigée » en quelque chose de plus net. Aucune de ces retouches n’a été
demandée ; aucune n’est signalée. Le document est valide au regard du schéma,
et faux en douce.

Dans un flux de travail archivistique, où le texte encodé devient la version de
référence dont dépendront les lecteurs, les index de recherche et les citations,
c’est la faute qui compte le plus. Une balise mal formée agace ; une graphie
modernisée que personne ne remarque pendant cinq ans est une corruption.

## La composition à empans verrouillés

La nouvelle version (v0.3) embarque un mécanisme de prévention des hallucinations
qui vise exactement cette faute-là. Le principe qui a guidé sa conception :
rendre l’hallucination dans le corps du texte impossible par construction, et non
pas seulement improbable.

L’idée est simple : **le modèle ne tape jamais le corps du texte**.

Le travail se déroule ainsi :

1. Le modèle appelle `get_source("letter_001")` et reçoit le texte brut de la
   source sous forme de chaîne immuable.
2. Pour chaque balise qu’il veut poser, il appelle
   `tag_span("letter_001", start, end, element_path, attrs)`, qui enregistre
   un élément TEI sur un intervalle de caractères de la source.
3. Quand il a fini, il appelle `compose("letter_001")`. Le serveur entrelace
   les balises enregistrées et le texte brut d’origine, produit le TEI final,
   puis vérifie *octet par octet* que le texte nu du document produit est
   identique à la source.

Si les octets concordent, le document est rendu. Sinon – si les balises du
modèle impliquent, d’une manière ou d’une autre, un corps qui s’écarte de la
source ne serait-ce que d’un caractère – `compose()` lève une erreur au lieu de
rendre un document corrompu.

Il n’existe dans ce flux de travail aucun chemin par lequel le modèle puisse
produire un document TEI dont le corps diffère de la source. L’invariant est
mécanique, non comportemental : vous n’avez pas à faire confiance au modèle pour
qu’il n’hallucine pas ; vous n’avez à faire confiance qu’à un `==` entre deux
chaînes d’octets.

## Ce que c’est, et ce que ce n’est pas

La composition à empans verrouillés **complète** l’ancrage dans le schéma ; elle
ne le remplace pas. Les outils d’ancrage (`validate_document`,
`lookup_element`, `valid_children` et le reste des seize outils d’origine)
aident le modèle à produire du TEI *valide* ; la composition à empans verrouillés
garantit que le corps du texte à l’intérieur de ce TEI est *fidèle* à la source.
Un flux d’encodage digne d’être mis en production doit satisfaire à ces deux
exigences, et un seul serveur y pourvoit désormais.

Ce n’est pas non plus un remède universel. `compose()` ne vérifie pas encore
que les balises enregistrées sont admises par la personnalisation ODD chargée –
ce sera l’objet d’une prochaine étape. Les balises enregistrées vivent dans la
mémoire du processus et ne survivent pas à un redémarrage. Et les fichiers
sources doivent être lisibles depuis l’endroit où tourne le serveur. Tout cela
se corrige ; rien de tout cela n’entame l’invariant central.

## Au-delà de la TEI

Le procédé se généralise. Chaque fois qu’on demande à un modèle d’annoter, de
transformer ou d’envelopper un texte, et chaque fois que l’intégrité de ce texte
importe plus que le talent du modèle à l’« améliorer », la même forme de solution
s’applique. Ne demandez pas au modèle de retaper le texte ; demandez-lui des
instructions sur le texte, et laissez un compositeur déterministe les appliquer
sous un invariant d’égalité.

Pour les éditions numériques en particulier, cela change ce que l’on peut
raisonnablement confier à un modèle. L’encodage devient d’un coup une tâche que
l’on peut déléguer sans avoir à comparer à la main chaque sortie avec la source.
La machine se charge de la besogne ; l’éditeur relit le balisage, non
l’orthographe.

## Obtenir la mise à jour

Si tei-mcp est déjà installé :

```bash
uvx tei-mcp@latest
```

Ou, pour une installation neuve :

```bash
pip install tei-mcp
```

Pour utiliser la composition à empans verrouillés, indiquez au serveur un
répertoire de fichiers sources en texte brut :

```bash
export TEI_MCP_SPAN_SOURCE_ROOT=/path/to/sources
uvx tei-mcp
```

Le nom de chaque fichier, sans son extension, devient l’identifiant du document
(`letter_001.txt` → `letter_001`).

Code source, documentation complète et notes de conception de l’invariant :
[github.com/Pantagrueliste/tei-mcp](https://github.com/Pantagrueliste/tei-mcp)
