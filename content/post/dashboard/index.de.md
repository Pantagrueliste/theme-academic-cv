---
title: Das Archiv auf einen Blick
subtitle: Wie interaktive Datenvisualisierungen die Archivforschung bereichern

# Summary for listings and search engines
summary: Dashboard-Webanwendungen erhöhen das Situationsbewusstsein im Archiv und verbessern damit letztlich dessen Zugänglichkeit und die Produktivität der Forschenden

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
Historische Archive können entmutigend unübersichtlich sein. Das *Mediceo del Principato* im [Staatsarchiv Florenz](https://www.archiviodistato.firenze.it/asfi/home) ist ein Paradebeispiel. Nur ein kleiner Teil davon ist inventarisiert, und viele seiner Dokumente sind ohne erkennbaren Grund über mehr als 6.500 Bände verstreut. Erschwerend kommt hinzu, dass das Archiv nur eine begrenzte Zahl von Bänden (oder *filze*, wie man sie dort nennt) zur Einsicht freigibt. In normalen Zeiten liegt die Grenze bei 4 *filze* pro Tag. In Pandemiezeiten ist diese Zahl jedoch auf 4 alle zwei Wochen gesunken. Da detaillierte Inventare fehlen, zwingt der beträchtliche Umfang des Archivs Forschende dazu, Strategien zu entwickeln, um die gesuchten Dokumente rasch zu finden.

# Die Lösung
Manche setzen auf den Zufall, andere versuchen zudem, auf der Grundlage von Chronologie, Empfängern, Verfassern, Herkunft des Archivbestands, Sprache usw. begründete Vermutungen anzustellen. All diese Variablen gleichzeitig zu *betrachten*, kann jedoch unerwartete Muster in der Struktur des Archivs offenbaren und unsere Vermutungen verbessern. Meine Erfahrung zeigt, dass die Metadaten, die Forschende üblicherweise in einer Tabelle sammeln, in grafischer Form das Situationsbewusstsein im Archiv erheblich steigern können.

# Das Experiment
Meine aktuelle Forschung konzentriert sich auf die Korrespondenz eines Spions des 16. Jahrhunderts. Seine Briefe sind über Hunderte von *filze* verstreut. Sie sind unter verschiedenen Identitäten geschrieben, an verschiedene und manchmal unerwartete Adressaten, von verschiedenen Orten aus usw. Um *filze* zu finden, die die gesuchten Briefe mit höherer Wahrscheinlichkeit enthalten, habe ich ein Dashboard eingerichtet, eine interaktive Webanwendung zur Datenvisualisierung ([Plotly Dash](https://plotly.com/dash/)), die alle möglichen Daten, darunter geografische und chronologische Informationen, mit einem hierarchischen Diagramm ([Sunburst](https://datavizproject.com/data-type/sunburst-diagram/)) des Archivbestands verknüpft. Das Dashboard zeigt mir auf einen Blick, was bereits gefunden wurde, wie viel das ausmacht, und gibt mir eine ungefähre Vorstellung davon, wo ich nach neuen Briefen suchen könnte. Durch Anklicken bestimmter Variablen werden zudem alle Diagramme aktualisiert, um spezifische Korrelationen anzuzeigen.

# Nächste Schritte
Vielleicht noch wichtiger ist, dass sich dieses Dashboard als visueller Index umfunktionieren lässt. Wenn die kritische Edition dieser Briefe online veröffentlicht wird, dient das Dashboard als alternativer Einstiegspunkt, von dem aus Leserinnen und Leser die Daten durchstöbern können. Aus Gründen der Vertraulichkeit kann ich im Moment nur einen geschwärzten Screenshot zeigen, aber ich werde das vollständige Dashboard nächstes Jahr freigeben. In der Zwischenzeit wird bald ein Prototyp verfügbar sein. Bleiben Sie dran!
