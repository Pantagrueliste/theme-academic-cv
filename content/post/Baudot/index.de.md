---
title: "Binärcode begreifen mit dem ITA2-Telegrafen-Emulator"
subtitle: "Frühe digitale Kommunikation zum Anfassen"
summary: Eine interaktive Vorführung des ITA2-Telegrafencodes (Baudot-Murray-Code), an der Studierende die Grundbegriffe der Binärkodierung und der Zustandsautomaten erfassen
date: "2025-02-13T00:00:00Z"
lastmod: "2025-02-13T00:00:00Z"
draft: false
featured: false
machine_translated: true
image:
  caption: 'ITA2-Lochstreifen mit kodierter Nachricht'
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
## Abstraktes greifbar machen
Dieser ITA2-Emulator ist ein handfestes Lehrmittel: Er macht sichtbar und anfassbar, was sonst abstrakt bleibt, und führt Studierende so an einen Grundbegriff von Informatik und Telekommunikation heran – die Binärdarstellung, also die Frage, wie aus Text ein Muster aus Einsen und Nullen wird.
Oft lehren wir das rein abstrakt. Wer aber zusieht, wie die Löcher tatsächlich im Streifen erscheinen, begreift viel leichter, dass ein physisches System digitale Information tragen kann.
{{< Baudot >}}
## Historischer Hintergrund: Vom Telegrafen zum Computer
Der ITA2-Code (Internationales Telegrafenalphabet Nr. 2), auch Baudot-Murray-Code genannt, entstand in den 1920er Jahren als Weiterentwicklung des Telegrafencodes, den Émile Baudot in den 1870er Jahren entworfen hatte. Diese frühen Fernmeldesysteme haben die spätere Entwicklung des Computers unmittelbar geprägt:
- Das 5-Bit-Schema ist ein frühes Beispiel für Zeichenkodierung
- Weil fünf Bit nur 32 Kombinationen zulassen, brauchte es einen Kunstgriff: die Umschaltung zwischen Buchstaben und Ziffern (LETTERS/FIGURES)
- Fernschreiber arbeiteten mit diesem System bis weit ins 20. Jahrhundert hinein
## Zustandsautomaten im Spiel lernen
Mit der LETTERS/FIGURES-Umschaltung ist der Zustandsautomat wie von selbst im Raum. Beim Ausprobieren entdecken die Studierenden, dass ein und dasselbe Muster je nach Modus ein anderes Zeichen bedeutet – eine handfeste Erfahrung mit zustandsabhängiger Kodierung, die den Boden für anspruchsvollere Begriffe der Informatik bereitet.
Das Bitmuster `00011` etwa steht für:
- den Buchstaben ‚A‘ im LETTERS-Modus
- die Ziffer ‚1‘ im FIGURES-Modus
Dass die Bedeutung vom Zustand abhängt, gehört zum Kern dessen, wie Computer mit Daten umgehen.
## Übungen für den Unterricht
Einige Vorschläge, wie sich der ITA2-Emulator in die Lehre einbauen lässt:
1. **Code knacken**: Lassen Sie Studierende Nachrichten entschlüsseln, die als ITA2-Muster vorliegen
2. **Sparsam kodieren**: Erörtern Sie, warum die Umschaltung wichtig war, um Bandbreite zu sparen
3. **Kodierung im Wandel**: Stellen Sie dem 5-Bit-Code von ITA2 ASCII (7 Bit) und Unicode gegenüber
4. **Physical Computing**: Schlagen Sie die Brücke von diesem historischen System zu heutigen Mikrocontrollern wie dem Arduino
## Ein Gewinn für die Zugänglichkeit
Abgesehen vom historischen Reiz kommt dieser Zugang Studierenden mit ganz unterschiedlichen Lernweisen entgegen:
- Wer visuell lernt, sieht die Muster
- Wer über die Hand lernt, greift unmittelbar in den Kodierungsvorgang ein
- Wer begrifflich denkt, kann die mathematische Seite der Informationstheorie erkunden
## Zur Implementierung
Der Emulator ist in JavaScript geschrieben und lässt sich ohne Umstände in jede webbasierte Lernplattform einbinden. Der Code ist modular aufgebaut und für verschiedene Unterrichtssituationen anpassbar.
Quellcode und Emulator zum Selbstausprobieren finden Sie hier: [GitHub-Repository](https://github.com/Pantagrueliste/BaudotMurray_Emulator)
