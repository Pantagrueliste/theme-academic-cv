---
title: "Old Habits, New Tools"
subtitle: A Programming Historian lesson on publishing a critical edition as you encode it

summary: >
  We have had computers for half a century and still make digital editions as if they were printed books.
  My new lesson for Programming Historian en français, the first of two parts, sets out the building blocks
  of an edition published at the pace of its encoding.

date: "2026-10-02T00:00:00Z"
lastmod: "2026-10-02T00:00:00Z"

draft: false
featured: true

image:
  caption: 'A weaver at a Jacquard loom, with the chain of punched cards that programmes the pattern. Photograph via [*IEEE Spectrum*](https://spectrum.ieee.org/the-jacquard-loom-a-driver-of-the-industrial-revolution)'
  focal_point: "Center"
  placement: 2
  preview_only: false

authors:
- clement

tags:
- Digital Humanities
- Digital Editions
- Scholarly Editing
- TEI

categories:
- Digital Humanities

projects: [DCE]
---

The early modern humanists who adopted the printing press gave the edition the form it has kept ever since: the text is established, set in type, published once, and corrected, if at all, in a second edition years later. We have had computers for half a century, and we still make digital editions as if they were printed books. We finish the text, publish it in one go, and leave the errata for later. The tools are new, but the habits are old.

My new lesson for *Programming Historian en français*, [‘L’édition critique en continu : publier au rythme de l’encodage (Partie 1)’](https://programminghistorian.org/fr/lecons/edition-critique-continu-pt1), takes the new tools at their word. If TEI encoding is code, and it is, then it can be versioned, validated and transformed like code. Software developers long ago stopped waiting for a finished product: every change is checked automatically and released once it passes. Nothing prevents a critical edition from working the same way, publishing each letter as soon as it is encoded and reviewed, and correcting it in the open whenever a better reading turns up.


## Part 1: the building blocks

This first part sets out the pieces that free the editor from the inherited workflow, all of them open-source:

- an **ODD**, the single document that specifies the project’s encoding;
- a **RELAX NG schema** generated from it, which enforces the structure;
- **Schematron rules**, which add the editorial constraints a schema cannot express;
- a **validation script**, which checks the whole corpus in one command and produces readable outputs through XSLT.

The examples come from the correspondence of Filippo Cavriana, the edition I am [building along these lines](/post/cavriana-edition/). Part 2 will add the chain that ties these pieces together, so that every change to the corpus is validated and published as it is made. The lesson belongs to my [Efficient Editing](/project/dce/) project, which looks for ways to bring the cost of scholarly editions down; automating publication, so that the editor is no longer waiting on a specialist at the end of the chain, is one of the largest savings available.


## Outcry, denial, or superficial adoption

The reception of artificial intelligence follows the same pattern: outcry, denial, or superficial adoption. This is one reason I like the digital humanities: few fields show the paradox so plainly. New tools should be an invitation to rethink how we can work better, not a new coat of paint on old routines. This lesson takes up the invitation for scholarly editing. Stay tuned for Part 2.

My thanks go to my editors, Daphné Mathelier and Matthias Gille Levenson, to my reviewers, Jasmin Macarios and Elsa Van Kote, and to Anisa Hawes.

The lesson is in open access: [programminghistorian.org/fr/lecons/edition-critique-continu-pt1](https://programminghistorian.org/fr/lecons/edition-critique-continu-pt1) (DOI: [10.46430/phfr0044](https://doi.org/10.46430/phfr0044)).
