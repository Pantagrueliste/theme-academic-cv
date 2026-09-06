---
title: Das Archiv auf einen Blick
subtitle: Wie interaktive Datenvisualisierung die Arbeit im Archiv erleichtert

# Summary for listings and search engines
summary: Dashboards verschaffen im Archiv Überblick – und machen so den Bestand zugänglicher und die Forschenden produktiver

# Link this post with a project
projects: [Filippo Cavriana's Secret Correspondence, 1568—1589.]

# Date published
date: "2021-05-24T16:00:00Z"

# Date updated
lastmod: "2021-05-24T16:00:00Z"

# Is this an unpublished draft?
draft: false

# Show this page in the Featured widget?
featured: false
machine_translated: true

# Featured image
# Place an image named `featured.jpg/png` in this page's folder and customize its options here.
image:
  caption: ''
  focal_point: ""
  placement: 2
  preview_only: false

authors:
- clement

tags:
- Digital Humanities
- Datenvisualisierung
- Archivforschung
- Aktuelle Forschung

categories:
- Notizen
---

# Das Problem
Historische Archive können von entmutigender Unordnung sein. Das *Mediceo del Principato* im [Staatsarchiv Florenz](https://www.archiviodistato.firenze.it/asfi/home) ist dafür ein Musterfall: Nur ein kleiner Teil des Bestands ist erschlossen, und viele Dokumente liegen ohne erkennbaren Grund über mehr als 6.500 Bände verstreut. Hinzu kommt, dass das Archiv nur eine begrenzte Zahl von Bänden – *filze*, wie man sie dort nennt – zur Einsicht ausgibt: in normalen Zeiten 4 *filze* am Tag, in Pandemiezeiten indes 4 alle zwei Wochen. Wo ausführliche Findmittel fehlen, zwingt schon die schiere Größe des Archivs die Forschenden, sich Strategien zurechtzulegen, um die gesuchten Dokumente rasch aufzuspüren.

# Die Lösung
Die einen vertrauen auf den Zufall, die anderen versuchen es zusätzlich mit begründeten Vermutungen – nach Chronologie, Empfängern, Verfassern, Herkunft des Bestands, Sprache und dergleichen. Wer all diese Variablen aber gleichzeitig *vor Augen* hat, entdeckt in der Struktur des Archivs womöglich Muster, mit denen niemand gerechnet hatte, und kann seine Vermutungen entsprechend schärfen. Meine Erfahrung ist: Die Metadaten, die Forschende ohnehin in einer Tabelle sammeln, verschaffen, einmal grafisch aufbereitet, im Archiv einen ganz anderen Überblick.

# Das Experiment
Ich arbeite derzeit über die Korrespondenz eines Spions des 16. Jahrhunderts. Seine Briefe verteilen sich auf Hunderte von *filze*; er schrieb sie unter wechselnden Identitäten, an wechselnde und mitunter überraschende Adressaten, von wechselnden Orten aus. Um jene *filze* zu finden, in denen die erhofften Briefe mit einiger Wahrscheinlichkeit liegen, habe ich mir ein Dashboard gebaut – eine interaktive Webanwendung zur Datenvisualisierung ([Plotly Dash](https://plotly.com/dash/)), die Daten aller Art, darunter geografische und chronologische Angaben, mit einem hierarchischen Diagramm ([Sunburst](https://datavizproject.com/data-type/sunburst-diagram/)) des Bestands verknüpft. Das Dashboard zeigt mir auf einen Blick, was schon gefunden ist, wie viel das ausmacht, und gibt mir eine ungefähre Ahnung, wo weitere Briefe zu vermuten wären. Klicke ich zudem einzelne Variablen an, richten sich alle Diagramme neu aus und lassen bestimmte Zusammenhänge hervortreten.

# Wie es weitergeht
Vielleicht wichtiger noch: Dieses Dashboard lässt sich in ein visuelles Register umwidmen. Sobald die kritische Edition dieser Briefe online erscheint, wird es als zweiter Zugang dienen, von dem aus die Leserinnen und Leser die Daten durchstöbern können. Aus Gründen der Vertraulichkeit kann ich vorerst nur einen geschwärzten Screenshot zeigen; das vollständige Dashboard gebe ich im kommenden Jahr frei. Ein Prototyp wird schon bald verfügbar sein. Bleiben Sie dran!
