---
title: "tei-mcp v0.3 : encoder en TEI sans réécrire la source"
subtitle: La composition à empans verrouillés rend les hallucinations dans le corps du texte impossibles par construction

summary: >
  La nouvelle version de tei-mcp introduit la composition à empans verrouillés,
  un dispositif conçu pour prévenir la classe d’hallucination la plus dommageable
  dans l’encodage TEI assisté par IA : la réécriture silencieuse du texte source.
  Le modèle ne saisit jamais le corps du texte ; il enregistre des balises sous
  forme de positions dans la source, et le compositeur refuse de renvoyer tout
  document TEI dont le contenu textuel plat diffère de l’original ne serait-ce
  que d’un octet.

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

Quand j’ai [écrit pour la première fois sur tei-mcp](/post/tei-mcp/), l’objectif
était d’empêcher les assistants IA d’halluciner du balisage TEI. L’ancrage dans
le schéma a résolu une partie du problème : avec un accès direct, par des outils,
à la spécification P5, le modèle n’a plus à deviner ce que signifie un élément ni
quels attributs il accepte. La sortie est valide.

Mais l’hallucination a deux visages dans l’encodage TEI, et le schéma n’en attrape
qu’un. Valider par rapport à la spécification vous dit que le *balisage* est bien
formé. Cela ne dit rien du *texte* que ce balisage enveloppe. Et c’est là – dans
le texte lui-même – que se logent les hallucinations les plus dommageables.
La composition à empans verrouillés (*span-locked composition*), fonctionnalité
phare de la v0.3, est conçue précisément pour les empêcher.

{{< toc >}}

## L’hallucination que le schéma ne peut pas attraper

Demandez à un modèle d’encoder une lettre française du XVI^e^ siècle et vous
obtiendrez souvent en retour un document TEI d’apparence impeccable. L’en-tête est
rempli, les balises `<persName>` sont correctement placées, la `<dateline>` est
bien formée. Passez-le dans `validate_document` et il est validé.

Puis comparez le corps du texte à la source.

`mesme` est devenu `même`. Une virgule a migré. `luy` a été silencieusement
modernisé en `lui`. Une proposition difficile à lire dans le manuscrit a été
« corrigée » en quelque chose de plus propre. Aucun de ces changements n’a été
demandé. Aucun n’est signalé. Le document est valide par rapport au schéma, et
discrètement faux.

Pour un flux de travail archivistique – où le texte encodé devient l’enregistrement
permanent sur lequel s’appuient, en aval, les lecteurs, les index de recherche et
les citations – c’est le mode de défaillance qui compte le plus. Une balise mal
formée est agaçante. Une graphie modernisée que personne ne remarque pendant cinq
ans est une corruption.

## La composition à empans verrouillés

La nouvelle version (v0.3) embarque un mécanisme de prévention des hallucinations
qui vise précisément ce mode de défaillance. L’objectif de conception est de rendre
les hallucinations dans le corps du texte impossibles par construction, et pas
seulement improbables.

L’idée est simple : **le modèle ne saisit jamais le corps du texte**.

À la place, le flux de travail se déroule ainsi :

1. Le modèle appelle `get_source("letter_001")` et reçoit le texte brut de la
   source sous forme de chaîne immuable.
2. Pour chaque balise qu’il veut appliquer, il appelle
   `tag_span("letter_001", start, end, element_path, attrs)`, ce qui enregistre
   un élément TEI sur un intervalle de caractères de la source.
3. Quand il a terminé, il appelle `compose("letter_001")`. Le serveur entrelace
   les balises enregistrées avec le texte brut original, produit le TEI final,
   puis vérifie *octet par octet* que le contenu textuel plat du document produit
   est égal à la source.

Si les octets correspondent, le document est renvoyé. Sinon – si les balises du
modèle impliquent d’une manière ou d’une autre un corps qui diffère de la source
ne serait-ce que d’un caractère – `compose()` lève une erreur plutôt que de
renvoyer un document corrompu.

Il n’existe aucun chemin, dans ce flux de travail, par lequel le modèle produirait
un document TEI dont le corps du texte diffère de la source. L’invariant est
mécanique, non comportemental. Vous n’avez pas à faire confiance au modèle pour ne
pas halluciner ; vous avez à faire confiance à une comparaison `==` entre deux
chaînes d’octets.

## Ce que c’est, et ce que ce n’est pas

La composition à empans verrouillés est **complémentaire** de l’ancrage dans le
schéma, elle ne le remplace pas. Les outils d’ancrage dans le schéma
(`validate_document`, `lookup_element`, `valid_children` et le reste des seize
outils d’origine) aident le modèle à produire du TEI *valide*. La composition à
empans verrouillés garantit que le corps du texte à l’intérieur de ce TEI est
*fidèle* à la source. Un flux de travail d’encodage déployable doit satisfaire
ces deux axes, et les deux sont désormais couverts par un seul serveur.

Ce n’est pas non plus un remède miracle. `compose()` ne vérifie pas encore que
les balises enregistrées sont admissibles selon une personnalisation ODD chargée –
c’est prévu pour une prochaine étape. Les balises enregistrées vivent dans la
mémoire du processus et ne survivent pas à un redémarrage. Et les fichiers sources
doivent être lisibles depuis l’endroit où le serveur s’exécute. Tout cela peut
être traité ; rien de tout cela ne remet en cause l’invariant central.

## Pourquoi c’est important au-delà de la TEI

Le principe se généralise. Chaque fois que l’on demande à un modèle d’annoter, de
transformer ou d’envelopper un morceau de texte – et chaque fois que l’intégrité
du texte sous-jacent importe plus que la capacité du modèle à l’« améliorer » –
la même forme de solution s’applique. Ne demandez pas au modèle de retaper le
texte. Demandez-lui de produire des instructions sur le texte, et laissez un
compositeur déterministe les appliquer sous un invariant d’égalité.

Pour les éditions numériques en particulier, cela change ce que l’on peut
raisonnablement demander à un modèle. L’encodage devient soudain une tâche que
l’on peut déléguer sans avoir à comparer manuellement chaque sortie à la source.
La machine prend le chemin ennuyeux ; l’éditeur relit le balisage, pas
l’orthographe.

## Obtenir la mise à jour

Si tei-mcp est déjà installé :

```bash
uvx tei-mcp@latest
```

Ou pour une installation neuve :

```bash
pip install tei-mcp
```

Pour utiliser la composition à empans verrouillés, pointez le serveur vers un
répertoire de fichiers sources en texte brut :

```bash
export TEI_MCP_SPAN_SOURCE_ROOT=/path/to/sources
uvx tei-mcp
```

Le radical du nom de chaque fichier devient son identifiant de document
(`letter_001.txt` → `letter_001`).

Code source, documentation complète et notes de conception de l’invariant :
[github.com/Pantagrueliste/tei-mcp](https://github.com/Pantagrueliste/tei-mcp)
