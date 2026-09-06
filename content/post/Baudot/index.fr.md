---
title: "Le binaire à portée de main : un émulateur de télégraphe ITA2"
subtitle: "Comprendre les débuts de la communication numérique en manipulant la machine"
summary: Une démonstration interactive du code télégraphique ITA2 (Baudot-Murray), pour donner aux étudiants une intuition du codage binaire et des machines à états
date: "2025-02-13T00:00:00Z"
lastmod: "2025-02-13T00:00:00Z"
draft: false
featured: false
machine_translated: true
image:
  caption: 'Bande de télégraphe ITA2 portant un message codé'
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
## Donner corps à l’abstraction
Cet émulateur ITA2 est d’abord un outil de classe. Il rend visible, et manipulable, une notion qui est au cœur de l’informatique comme des télécommunications : la représentation binaire, c’est-à-dire la façon dont un texte se change en une suite de uns et de zéros.
On l’enseigne d’ordinaire au tableau, abstraitement ; or il suffit de voir les trous se percer un à un dans la bande pour comprendre qu’un dispositif matériel peut porter de l’information numérique.
{{< Baudot >}}
## Un peu d’histoire : du télégraphe à l’ordinateur
Le code ITA2 (International Telegraph Alphabet No. 2), dit aussi code Baudot-Murray, fut mis au point dans les années 1920 ; il perfectionnait le code télégraphique conçu par Émile Baudot dès les années 1870. Ces premiers systèmes de télécommunication ont pesé directement sur l’informatique qui allait suivre :
- le codage sur 5 bits est l’un des premiers exemples de codage de caractères ;
- l’étroitesse du jeu de caractères (5 bits ne donnent que 32 combinaisons) a suscité l’ingénieuse bascule LETTRES/CHIFFRES (LETTERS/FIGURES) ;
- les téléscripteurs ont continué de s’en servir jusque fort avant dans le XX^e^ siècle.
## Les machines à états, en jouant
La bascule LETTRES/CHIFFRES introduit sans qu’on y prenne garde la notion de machine à états. À force d’essais, les étudiants s’aperçoivent qu’un même motif désigne des caractères différents selon le mode en vigueur ; cette expérience concrète d’un codage qui dépend de l’état leur ouvre la voie vers des notions informatiques plus ardues.
Ainsi, le motif `00011` représente :
- la lettre « A » en mode LETTRES ;
- le chiffre « 1 » en mode CHIFFRES.
Cette double lecture, commandée par l’état, est au fondement même de la manière dont les ordinateurs traitent les données.
## En classe
Quelques manières d’intégrer l’émulateur ITA2 à un cours :
1. **Déchiffrement** : donner aux étudiants des messages codés en ITA2 à décoder
2. **Économie du codage** : expliquer pourquoi la bascule était précieuse pour ménager la bande passante
3. **Généalogie des codages** : comparer les 5 bits de l’ITA2 aux 7 bits de l’ASCII, puis à Unicode
4. **Informatique physique** : rapprocher ce système ancien des microcontrôleurs d’aujourd’hui, Arduino par exemple
## Un outil pour tous les profils
Au-delà de son intérêt historique, l’émulateur convient à des étudiants dont les manières d’apprendre diffèrent :
- les visuels voient les motifs ;
- les manuels agissent directement sur le codage ;
- les esprits théoriciens peuvent pousser jusqu’aux mathématiques de la théorie de l’information.
## Sous le capot
L’émulateur est écrit en JavaScript et s’intègre sans peine à toute plateforme pédagogique en ligne ; son code, modulaire, s’adapte à des contextes d’enseignement variés.
Le code source est disponible, et l’émulateur peut s’essayer, ici : [dépôt GitHub](https://github.com/Pantagrueliste/BaudotMurray_Emulator)
