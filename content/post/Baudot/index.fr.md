---
title: "Enseigner le binaire avec l’émulateur de télégraphe ITA2"
subtitle: "Une approche pratique pour comprendre les débuts de la communication numérique"
summary: Une démonstration interactive du code télégraphique ITA2 (Baudot-Murray) qui aide les étudiants à saisir les concepts fondamentaux du codage binaire et des machines à états
date: "2025-02-13T00:00:00Z"
lastmod: "2025-02-13T00:00:00Z"
draft: false
featured: false
machine_translated: true
image:
  caption: 'Bande de télégraphe ITA2 montrant un message codé'
  focal_point: ""
  placement: 2
  preview_only: false
authors:
- admin
tags:
- Histoire numérique
- Programmation
- Enseignement
- Histoire de l'informatique
categories:
- Humanités numériques
- Outils pédagogiques
---
## Rendre tangibles les concepts abstraits
Cet émulateur ITA2 est un support pédagogique concret. En rendant visibles et interactifs des concepts abstraits de codage, il initie les étudiants à une notion clé de l’informatique et des télécommunications : la représentation binaire, c’est-à-dire la manière dont un texte devient une suite de uns et de zéros.
Nous enseignons souvent cette notion de façon abstraite ; voir les trous apparaître réellement aide les étudiants à comprendre comment des systèmes physiques peuvent représenter de l’information numérique.
{{< Baudot >}}
## Contexte historique : du télégraphe à l’informatique
Le code ITA2 (International Telegraph Alphabet No. 2), aussi appelé code Baudot-Murray, a été mis au point dans les années 1920 comme un perfectionnement du code télégraphique original d’Émile Baudot, datant des années 1870. Ces premiers systèmes de télécommunication ont directement influencé les développements ultérieurs de l’informatique :
- Le codage sur 5 bits est un exemple précoce de codage de caractères
- Les limites du jeu de caractères (seulement 32 combinaisons possibles avec 5 bits) ont conduit à l’ingénieux mécanisme de bascule LETTRES/CHIFFRES (LETTERS/FIGURES)
- Ce système a été utilisé jusque tard dans le XX^e^ siècle pour les téléscripteurs
## Apprendre les machines à états en jouant
Le mécanisme de bascule LETTRES/CHIFFRES introduit naturellement la notion de machine à états. Les étudiants découvrent par l’expérimentation qu’un même motif peut représenter des caractères différents selon le mode en cours. Cette expérience concrète d’un codage dépendant de l’état les prépare à des concepts informatiques plus complexes.
Par exemple, le motif de bits `00011` représente :
- La lettre « A » en mode LETTRES
- Le chiffre « 1 » en mode CHIFFRES
Cette double interprétation selon l’état est fondamentale dans la manière dont les ordinateurs traitent les données.
## Activités en classe
Voici quelques façons d’intégrer l’émulateur ITA2 à l’enseignement :
1. **Défi de décryptage** : faire décoder aux étudiants des messages encodés en motifs ITA2
2. **Codage efficace** : discuter de l’importance du mécanisme de bascule pour économiser la bande passante
3. **Évolution des codages** : comparer le code ITA2 sur 5 bits à l’ASCII (7 bits) et à Unicode
4. **Informatique physique** : relier ce système historique aux microcontrôleurs modernes comme Arduino
## Atouts en matière d’accessibilité
Au-delà de son intérêt historique, cette approche aide des étudiants aux styles d’apprentissage variés :
- Les apprenants visuels voient les motifs
- Les apprenants kinesthésiques interagissent directement avec le processus de codage
- Les esprits conceptuels peuvent explorer les aspects mathématiques de la théorie de l’information
## Détails d’implémentation
L’émulateur est implémenté en JavaScript et peut être facilement intégré à n’importe quelle plateforme d’apprentissage en ligne. Le code est modulaire et personnalisable selon les contextes d’enseignement.
Vous trouverez le code source et pourrez essayer l’émulateur vous-même ici : [Dépôt GitHub](https://github.com/Pantagrueliste/BaudotMurray_Emulator)
