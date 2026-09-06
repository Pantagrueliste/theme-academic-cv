---
title: "Binärcode vermitteln mit dem ITA2-Telegrafen-Emulator"
subtitle: "Ein praxisnaher Zugang zum Verständnis früher digitaler Kommunikation"
summary: Eine interaktive Demonstration des ITA2-Telegrafencodes (Baudot-Murray-Code), die Studierenden hilft, grundlegende Konzepte der Binärkodierung und der Zustandsautomaten zu erfassen
date: "2025-02-13T00:00:00Z"
lastmod: "2025-02-13T00:00:00Z"
draft: false
featured: false
machine_translated: true
image:
  caption: 'ITA2-Telegrafenlochstreifen mit kodierter Nachricht'
  focal_point: ""
  placement: 2
  preview_only: false
authors:
- admin
tags:
- Digitale Geschichte
- Programmierung
- Lehre
- Computergeschichte
categories:
- Digital Humanities
- Lehrwerkzeuge
---
## Abstrakte Konzepte greifbar machen
Dieser ITA2-Emulator ist ein praktisches Lehrmittel. Indem er abstrakte Kodierungskonzepte sichtbar und interaktiv macht, führt er Studierende an ein Schlüsselkonzept der Informatik und der Telekommunikation heran: die Binärdarstellung – wie aus Text Muster aus Einsen und Nullen werden.
Wir vermitteln dies oft rein abstrakt; wer aber die tatsächlichen Löcher erscheinen sieht, begreift leichter, wie physische Systeme digitale Information darstellen können.
{{< Baudot >}}
## Historischer Kontext: Vom Telegrafen zum Computer
Der ITA2-Code (Internationales Telegrafenalphabet Nr. 2), auch als Baudot-Murray-Code bekannt, wurde in den 1920er Jahren als Weiterentwicklung von Émile Baudots ursprünglichem Telegrafencode aus den 1870er Jahren entwickelt. Diese frühen Telekommunikationssysteme hatten einen direkten Einfluss auf spätere Entwicklungen der Informatik:
- Das 5-Bit-Kodierungsschema war ein frühes Beispiel für Zeichenkodierung
- Die Beschränkungen des Zeichensatzes (nur 32 mögliche Kombinationen mit 5 Bit) führten zum genialen Umschaltmechanismus zwischen Buchstaben und Ziffern (LETTERS/FIGURES)
- Dieses System wurde bis weit ins 20. Jahrhundert hinein für Fernschreiber verwendet
## Zustandsautomaten spielerisch lernen
Der LETTERS/FIGURES-Umschaltmechanismus führt ganz natürlich in das Konzept der Zustandsautomaten ein. Studierende entdecken durch Experimentieren, dass dasselbe Muster je nach aktuellem Modus unterschiedliche Zeichen darstellen kann. Diese praktische Erfahrung mit zustandsabhängiger Kodierung bereitet sie auf komplexere Konzepte der Informatik vor.
Das Bitmuster `00011` steht zum Beispiel für:
- den Buchstaben ‚A‘ im LETTERS-Modus
- die Ziffer ‚1‘ im FIGURES-Modus
Diese doppelte, vom Zustand abhängige Interpretation ist grundlegend dafür, wie Computer mit Daten arbeiten.
## Aktivitäten für den Unterricht
Hier einige Möglichkeiten, den ITA2-Emulator in die Lehre einzubinden:
1. **Codeknacker-Wettbewerb**: Lassen Sie Studierende als ITA2-Muster kodierte Nachrichten entschlüsseln
2. **Effiziente Kodierung**: Diskutieren Sie, warum der Umschaltmechanismus für die Einsparung von Bandbreite wichtig war
3. **Evolution der Kodierung**: Vergleichen Sie den 5-Bit-Code von ITA2 mit ASCII (7 Bit) und Unicode
4. **Physical Computing**: Verbinden Sie dieses historische System mit modernen Mikrocontrollern wie Arduino
## Vorteile für die Zugänglichkeit
Über das historische Interesse hinaus hilft dieser Ansatz Studierenden mit unterschiedlichen Lernstilen:
- Visuelle Lernende sehen die Muster
- Kinästhetische Lernende interagieren direkt mit dem Kodierungsprozess
- Konzeptuell Denkende können die mathematischen Aspekte der Informationstheorie erkunden
## Details zur Implementierung
Der Emulator ist in JavaScript implementiert und lässt sich leicht in jede webbasierte Lernplattform integrieren. Der Code ist modular aufgebaut und für verschiedene Lehrkontexte anpassbar.
Den Quellcode finden Sie hier, wo Sie den Emulator auch selbst ausprobieren können: [GitHub-Repository](https://github.com/Pantagrueliste/BaudotMurray_Emulator)
