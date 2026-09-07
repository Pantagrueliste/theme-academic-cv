---
title: "Ensenyar el sistema binari amb l’emulador de telègraf ITA2"
subtitle: "Una manera pràctica d’entendre els inicis de la comunicació digital"
summary: Una demostració interactiva del codi telegràfic ITA2 (Baudot-Murray) que ajuda els estudiants a copsar les nocions fonamentals de la codificació binària i de les màquines d’estats
date: "2025-02-13T00:00:00Z"
lastmod: "2025-02-13T00:00:00Z"
draft: false
featured: false
machine_translated: true
image:
  caption: 'Codis telegràfics de cinc bits comparats: l’ITA2, les seves variants nacionals i no llatines, i els patrons de perforació de la cinta'
  focal_point: "Top"
  placement: 2
  preview_only: false
authors:
- clement
tags:
- Història digital
- Programació
- Docència
- Història de la informàtica
categories:
- Humanitats digitals
- Eines docents
---
## Fer tangibles els conceptes abstractes
Aquest emulador de l’ITA2 és una eina docent pràctica. En fer visibles i interactius uns conceptes de codificació que d’entrada són abstractes, introdueix els estudiants a una noció clau de la informàtica i de les telecomunicacions: la representació binària, és a dir, com un text es converteix en seqüències d’uns i de zeros.
Sovint ho ensenyem de manera abstracta; veure aparèixer els forats de debò ajuda els estudiants a entendre com un sistema físic pot representar informació digital.
{{< Baudot >}}
## Context històric: del telègraf a la informàtica
El codi ITA2 (Alfabet Telegràfic Internacional núm. 2), conegut també com a codi Baudot-Murray, es va desenvolupar als anys vint del segle XX com un refinament del codi telegràfic original que Émile Baudot havia ideat als anys setanta del segle XIX. Aquests primers sistemes de telecomunicació van influir directament en l’evolució posterior de la informàtica:
- L’esquema de codificació de 5 bits va ser un dels primers exemples de codificació de caràcters
- Les limitacions del joc de caràcters (només 32 combinacions possibles amb 5 bits) van donar lloc a l’enginyós mecanisme de canvi LLETRES/XIFRES
- El sistema es va fer servir en els teletips fins ben entrat el segle XX
## Aprendre les màquines d’estats jugant
El mecanisme de canvi LLETRES/XIFRES introdueix les màquines d’estats de manera natural. Tot experimentant, els estudiants descobreixen que un mateix patró pot representar caràcters diferents segons el mode actiu. Aquesta experiència directa amb la codificació basada en estats els prepara per a conceptes informàtics més complexos.
Per exemple, el patró de bits `00011` representa:
- La lletra «A» en mode LLETRES
- El número «1» en mode XIFRES
Aquesta doble interpretació segons l’estat és un principi fonamental de com els ordinadors treballen amb les dades.
## Activitats per a l’aula
Algunes maneres d’incorporar l’emulador de l’ITA2 a la docència:
1. **Repte de desxifratge**: fer que els estudiants descodifiquin missatges codificats en patrons ITA2
2. **Codificació eficient**: discutir per què el mecanisme de canvi era important per estalviar amplada de banda
3. **Evolució de la codificació**: comparar el codi de 5 bits de l’ITA2 amb l’ASCII (7 bits) i amb Unicode
4. **Informàtica física**: relacionar aquest sistema històric amb microcontroladors moderns com Arduino
## Avantatges per a l’accessibilitat
Més enllà de l’interès històric, aquest enfocament ajuda estudiants amb estils d’aprenentatge diferents:
- Els aprenents visuals veuen els patrons
- Els aprenents cinestèsics interactuen directament amb el procés de codificació
- Els pensadors conceptuals poden explorar els aspectes matemàtics de la teoria de la informació
## Detalls d’implementació
L’emulador està escrit en JavaScript i s’integra fàcilment en qualsevol plataforma d’aprenentatge en línia. El codi és modular i es pot adaptar a contextos docents diversos.
Pots consultar el codi font i provar l’emulador tu mateix a: [Repositori de GitHub](https://github.com/Pantagrueliste/BaudotMurray_Emulator)
