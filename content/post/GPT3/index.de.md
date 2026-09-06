---
title: Automatisierte Auszeichnung in digitalen wissenschaftlichen Editionen
subtitle: Können vortrainierte Sprachmodelle die editorische Produktivität deutlich steigern?

# Summary for listings and search engines
summary: Vortrainierte Sprachmodelle können Forschenden helfen, einige der mühsamsten und arbeitsintensivsten Aufgaben des Edierens zu automatisieren. Auf der Grundlage der kuratierten Annotationen von *Secrets of Craft and Nature in Renaissance France* prüfe ich, inwieweit ein Modell wie GPT-3 rasch darauf trainiert werden kann, technische Handschriften des 16. Jahrhunderts zu annotieren.

# Link this post with a project
projects: [Efficient Editing]

# Date published
date: "2021-11-22T18:15:00Z"

# Date updated
lastmod: "2021-11-22T20:34:00Z"

# Is this an unpublished draft?
draft: false

# Show this page in the Featured widget?
featured: true
machine_translated: true

# Featured image
# Place an image named `featured.jpg/png` in this page's folder and customize its options here.
image:
  caption: ""
  focal_point: ""
  placement: 1
  preview_only: false

authors:
- clement

tags:
- Digital Humanities
- Maschinelles Lernen
- Digitale kritische Editionen
- Aktuelle Forschung

categories:
- Effizientes Edieren
---
# Einleitung
Wie lassen sich digitale wissenschaftliche Editionen herstellen, ohne das Budget zu sprengen? In diesem Beitrag, dem ersten einer Reihe zum effizienten Edieren, bewerte ich die Rolle, die vortrainierte Sprachmodelle bei der Automatisierung editorischer Aufgaben wie der semantischen Auszeichnung spielen können.

{{< toc >}}

# Das Problem
## Eine Arbeit aus Liebe
Wer liebt, der rechnet nicht … so jedenfalls das alte Sprichwort. Für digitale wissenschaftliche Editionen gilt das in besonderem Maße, denn die Transkription, Übersetzung und Annotation, die ihre Erarbeitung erfordert, bedeuten Tausende von Arbeitsstunden, geleistet – wie im Fall von [*Secrets of Craft and Nature in Renaissance France*](https://edition640.makingandknowing.org) – von Hunderten hochqualifizierter Mitarbeiterinnen und Mitarbeiter.

In gewissem Sinne ist es ein Segen, dass Projekte der Digital Humanities mit hoher Sichtbarkeit die enormen Fördermittel einwerben können, die für ihren Betrieb nötig sind. Doch die starke Abhängigkeit von der Großzügigkeit wohlhabender Stiftungen, Universitäten und staatlicher Einrichtungen sowie der langanhaltende Bedarf an umfangreichen personellen Ressourcen bilden kein tragfähiges Wirtschaftsmodell für die Zukunft.

Wenn wir Forschende aus aller Welt ermutigen wollen, historische Dokumente einem breiteren Publikum zugänglich zu machen, {{< hl >}}müssen die Kosten digitaler kritischer Editionen um Größenordnungen sinken{{< /hl >}}. 

## Eine hohe Schwelle
Etwas paradoxerweise {{< hl >}}könnte die Lösung gerade von arbeitsintensiven Projekten wie [*Secrets of Craft and Nature in Renaissance France*](https://edition640.makingandknowing.org) kommen, denn sie bilden einen wertvollen Trainingsdatensatz{{< /hl >}}, um einige der widerspenstigsten und repetitivsten Aufgaben des digitalen Edierens zu automatisieren, etwa die Auszeichnung (Markup).

Nicht, dass die Auszeichnung unwichtig wäre. Im Gegenteil: {{< hl >}}Markup ist zum unverzichtbaren Bestandteil jedes ernsthaften digitalen Editionsprojekts geworden.{{< /hl >}} Standardisiert durch die [Text Encoding Initiative](https://tei-c.org), erlaubt es uns, möglichst viele Aspekte des Dokuments und des Textes, den es vermittelt, festzuhalten: Struktur, Randbemerkungen, Streichungen, Varianten, Papiersorte, Flecken, Schriftbild … was immer Sie wollen.

Das folgende Beispiel aus [*Secrets of Craft and Nature in Renaissance France*](https://edition640.makingandknowing.org) zeigt, wie die Auszeichnung den Text um zusätzliche Informationen anreichert (Kategorie, Struktur, semantische Felder, Streichungen usw.) und digitalen Editionen damit letztlich einen erheblichen Vorteil gegenüber ihren materiellen Vorfahren verschafft.

<table>
<tr>
<th> Reiner Text </th>
<th> XML-Markup</th>
</tr>
<tr>
<td>

```text
Pour rompre grenades et donner 
violence aux artifices de foeu

Mects parmy la pouldre et la sixiesme
partye dicelle de vif argent
```

</td>
<td>

```xml
<div id="p008r_2" categories="arms and armor">  
<head>Pour rompre <wp>grenades</wp> et donner<lb/> 
violence aux <wp>artifices de foeu</wp></head>
<ab>Mects parmy la <m>pouldre</m>
<del><ms>six fois autant</ms> de 
<m>vif argent</m></del><lb/>
<del>et</del> <ms>la sixiesme partye</ms>
 dicelle de <m>vif argent</m></ab>
</div>

```

</td>
</tr>
</table>

Diese Informationen sind nicht nur für Archivzwecke wertvoll, sondern, wie ich bei früheren Gelegenheiten gezeigt habe, auch für synthetische und analytische Zwecke. Dennoch kann diese Art der Annotation äußerst zeitaufwendig sein, da derselbe Text oft in verschiedenen Fassungen verfügbar sein muss: als Übersetzung, als Transkription, als Modernisierung usw. 

# Die Lösung
## Transformer: der einfachste Weg zur Automatisierung?
2020 veröffentlichte [OpenAI](https://www.openai.com) mit großem Tamtam seine neueste Familie universeller großer Sprachmodelle namens GPT-3, was für „Generative Pre-trained Transformer 3“ steht. Transformer stellen einen recht jungen Durchbruch in der Künstlichen Intelligenz dar. Sie lernen neue Aufgaben mit beeindruckender Geschwindigkeit, indem sie einfach einen Prompt lesen und eine sehr begrenzte Zahl von Beispielen betrachten. Sie können auch mit einem eigens zusammengestellten Datensatz zusätzlich trainiert werden (Fine-Tuning), was Latenz und Genauigkeit verbessert. Aus diesem Grund bezeichnet man GPT-3 und vergleichbare Transformer als [Few-Shot-Learner](https://arxiv.org/abs/2005.14165). 

OpenAI gibt an, dass GPT-3 die Rekordzahl von 175 Milliarden Parametern umfasst und mit mehr als 570 GB Text trainiert wurde, überwiegend englischsprachigen Dokumenten, die vermutlich aus [dem Internet](https://skylion007.github.io/OpenWebTextCorpus/) stammen. Allein durch seine schiere Größe hat GPT-3 in diesem Bereich einen neuen Standard gesetzt und führt ohne weitere Anpassung verschiedenste Aufgaben mit beunruhigendem Realismus aus. Es schreibt plausible [Meinungsbeiträge](https://www.theguardian.com/commentisfree/2020/sep/08/robot-wrote-this-article-gpt-3), es [interagiert mit Menschen](https://www.quickchat.ai/emerson) in Chatrooms, [beantwortet E-Mails](https://www.jarvis.ai/?fpr=serpbattle), [fasst Texte zusammen](https://medium.com/geekculture/a-paper-summarizer-with-python-and-gpt-3-2c718bc3bc88), übersetzt Dokumente, erklärt Fachjargon usw.

Da ich seit Mai 2021 frühen Zugang zur API von OpenAI hatte, konnte ich mit der Fähigkeit des Modells experimentieren, eine Reihe als schwierig geltender Aufgaben zu lösen: französische Lyrik und neulateinische Texte ins Englische zu übersetzen, Analogien zu erklären und sogar Buch 4 von Kants *Grundlegung zur Metaphysik der Sitten* für ein siebenjähriges Kind zu vereinfachen (wenn auch wenig überzeugend).

### Codex
Eine der jüngsten Entwicklungen von GPT-3 konzentriert sich auf Programmiersprachen. Dieses Modell namens *Codex* übersetzt natürliche Sprache in Programmiersprache und umgekehrt. Wenn ich zum Beispiel einen regulären Ausdruck suche, mit dem ich „nur Wörter finden kann, die mit einem Großbuchstaben beginnen“, übersetzt GPT-3 dies prompt in einen funktionierenden regulären Ausdruck: ```[A-Z]+\w+```.

OpenAI gibt an, dass *Codex* mit einem Dutzend Programmiersprachen arbeiten kann, darunter Python, JavaScript, Go, Perl, PHP, Ruby und Swift. Indem es Pseudocode nahtlos in Code umwandelt, erlaubt *Codex* den Nutzenden, sich nicht auf die mühselige Syntax einer Programmiersprache zu konzentrieren, sondern auf die logischen Schritte und Strategien, mit denen Anwendungen Probleme lösen.

### Jenseits von OpenAI
OpenAI ist natürlich nicht der einzige Akteur auf dem Markt. Wie bereits erwähnt, kündigte die Beijing Academy of Artificial Intelligence 2021 ein noch größeres und leistungsfähigeres Modell namens *Wu Dao 2* an. Nvidia und Microsoft haben sich zusammengetan, um das treffend benannte Modell *Megatron-Turing NLG 530B* zu entwickeln. Kleinere Start-ups wie [AI21 Labs](https://www.ai21.com) und [Cohere](https://cohere.ai) bieten der Öffentlichkeit ebenfalls APIs an. Erwähnenswert sind auch Open-Source-Initiativen wie [EleutherAI](https://www.eleuther.ai). Die KI-Szene entwickelt sich natürlich sehr schnell; um neue Initiativen in diesem Bereich zu verfolgen, werfen Sie einen Blick auf [Hugging Face](https://huggingface.co/transformers/master/index.html).

# Die Experimente

> [!NOTE]
> Ziel dieser Experimente ist es, den wirtschaftlichsten Weg zu einer zuverlässigen Automatisierung editorischer Aufgaben zu finden. Man könnte einwenden, dass einige davon auch mit Algorithmen des überwachten Lernens automatisiert werden könnten. Diese Hypothese werden wir in einem künftigen Beitrag untersuchen.

Kann ein Transformer wie GPT-3 lernen, zum Beispiel eine technisch-wissenschaftliche Handschrift des 16. Jahrhunderts zu annotieren?

## Experiment 1 – Textkategorisierung
Beginnen wir mit etwas relativ Einfachem. Als „Few-Shot-Learner“ sollte GPT-3 rasch verstehen können, wie unser Redaktionsteam die Einträge in Ms. Fr. 640 klassifiziert hat.

### Prompt-Engineering
Zum Training verwendete ich einen sehr minimalen Prompt und wählte vier kurze Einträge im Reintext als Beispiele aus, darunter je einen zu „Medizin“, „Waffen und Rüstungen“ und „Malerei“. 

### Test
Dann kopierte ich eine weitere Passage, die nicht in der ursprünglichen Sequenz enthalten war: 

```text
Working neatly
Never put down, if you can, two colors one on top of the other.   
But next, having made your design carefully, keep the place of shadows for them alone,
& also separately that of lights & highlights, without layering one color all over & then highlighting or else shading on it.  
And in this way, you further your work, economize your colors & work neatly.  
Which is the reason that, the colors not being muddled nor mixed together, they do not die & you soften the colors better, since they are not so thick.
```
Die Ausgabe stimmt vollkommen mit dem Inhalt überein: 

```xml
<categories="painting">
```

Versuchen wir es mit einem Eintrag aus einer Kategorie, die in der ursprünglichen Textauswahl zum Training von GPT-3 gar nicht enthalten war, so ist das Ergebnis überraschend. 

```xml
<categories="jewelry">
```

### Ergebnis
Die Kategorie „jewelry“ (Schmuck) existiert in unserer Edition von Ms. Fr. 640 nicht. Das Redaktionsteam [bevorzugt](https://edition640.makingandknowing.org/#/content/resources) die weiter gefasste Kategorie „Stones“ (Steine). Die Intuition von GPT-3 ist jedoch gut und deutet darauf hin, dass es mit etwas mehr Training lernen kann, jeden Eintrag von Ms. Fr. 640 zu kategorisieren – und vielleicht sogar die Einträge ähnlicher technischer Texte des 16. Jahrhunderts.   

## Experiment 2 – Semantische Auszeichnung
Legen wir die Messlatte etwas höher. Wenn Transformer wie GPT-3 lernen können, Texte nach bestimmten editorischen Kriterien zu kategorisieren, können sie dann auch einen Teil der Auszeichnung des Textes erkennen?  

> [!NOTE]
> *Secrets of Craft and Nature* bietet eine [Kombination](https://edition640.makingandknowing.org/#/content/resources/principles) aus semantischen und strukturellen Labels. Leider verarbeitet GPT-3 keine Bilder, im Gegensatz zu anderen Projekten wie [Wu Dao 2](https://towardsdatascience.com/gpt-3-scared-you-meet-wu-dao-2-0-a-monster-of-1-75-trillion-parameters-832cd83db484). Wahrscheinlich werden künftige Versionen von GPT diese Fähigkeit enthalten, die notwendig ist, um die meisten strukturellen und materiellen Aspekte eines Dokuments zu erkennen. Wir lassen diese speziellen Tags beiseite und konzentrieren uns stattdessen auf Auszeichnungen, die keine Bilderkennung erfordern.

### Prompt-Engineering
Semantische Tags umfassen Verweise auf Tiere, Pflanzen, Ortsnamen, Sinneswahrnehmungen usw. Für den Trainingsprompt wählte ich einige Beispiele aus der Edition aus:
```xml
<!--Input prompt-->
The following is a list of words and their corresponding semantic tags

cannons: <wp>cannons</wp>
powder: <m>powder</m>
flasks: <tl>flasks</tl>
wooden: <m>wooden</m>
iron: <m>iron</m>
parchment: <m>parchment</m>
goats: <al>goats</al>
lambs: <al>lambs</al>
leather: <m>leather</m>
earth: <m>earth</m>
fine fatty earth: <m>fine fatty earth</m>
Venice: <pl>Venice</pl>
Flemish: <pl>Flemish</pl>
almond: <pa>almond</pa>
almond oil: <m><pa>almond</pa> oil</m>
walnuts skin: <m><pa>walnuts</pa> skin</m>
molten lead: <m>molten lead</m>
today: <tmp>today</tmp>
In the past: <tmp>In the past</tmp>
Clockmakers: <pro>Clockmakers</pro>
red copper: <m>red copper</m>
crucible: <tl>crucible</tl>
bellows: <tl>bellows</tl>
charcoal: <m>charcoal</m>
founders: <pro>founders</pro>
```
### Test
Versuchen wir es mit dem Modell `Davinci-codex` und ein paar einfachen Wörtern wie *Apothecary* (Apotheker), *smoke* (Rauch), *glassmakers* (Glasmacher), *latten* (Messingblech) und *snake* (Schlange). Die Ergebnisse kommen sofort und sind fehlerfrei:

```xml
<!--Output-->
Apothecary: <pro>Apothecary</pro>
smoke: <m>smoke<m>
glassmakers: <pro>glassmakers</pro>
latten: <m>latten</m>
snake: <al>snake</al>
```

Ein schwierigerer Test beinhaltet zusammengesetzte Begriffe wie *copper plates* (Kupferplatten), *walnut oil* (Walnussöl) und *wood block* (Holzblock). Ziel eines solchen Tests ist es zu sehen, ob GPT-3 verschachtelte Tags richtig handhabt. 

```xml
<!--Output-->
copper plates: <m>copper plates</m>
walnut oil: <m><pa>walnut</pa> oil</m>
wood block: <m>wood block</m>
```

Die Ergebnisse sind jedoch gemischt, da `Davinci-codex` nur *walnut oil* korrekt ausgezeichnet hat und die verschachtelten Tags `tl` und `m` in *copper plates* und *wood block* nicht erkannte. Wie der nächste Test unten zeigt, lassen sich diese Fehler jedoch durch einen besseren Trainingsprompt abmildern. Nachdem ich fünf weitere Beispiele für verschachtelte Tags hinzugefügt hatte, lieferte `Davinci-codex` ein nahezu fehlerfreies Ergebnis mit nur einem Fehler (*oil paintbrushes*):

```xml
<!--Output-->
cannon powder: <m><wp>cannon</wp> powder</m>
arquebus powder: <m><wp>arquebus</wp> powder</m>
oil paintbrushes: <m><al>oil</al> paintbrushes</m>
sheep footbones: <m><al>sheep</al> footbones</m>
bronze mortar: <tl><m>bronze</m> mortar</tl>
```

# Fazit
Man sollte nicht vergessen, dass diese Tests mit kleinen Textfragmenten durchgeführt wurden. Ich vermute, dass GPT-3-Modelle noch bessere Ergebnisse liefern würden, wenn man in den Beispielen und im Prompt mehr Kontext bereitstellte. Darüber hinaus würde ein Fine-Tuning des Modells mit eigens erstellten Trainingsdatensätzen die Genauigkeit der Auszeichnung zweifellos weiter verbessern.  
Auch wenn diese Experimente noch in größerem Maßstab durchgeführt werden müssten, um die Zuverlässigkeit vortrainierter Sprachmodelle nachzuweisen, können wir dennoch festhalten, dass {{< hl >}}dieser Ansatz es Editorinnen und Editoren ermöglicht, mehrere Annotationsaufgaben in wenigen einfachen Schritten zu automatisieren und dabei potenziell enorm viel Zeit und Geld zu sparen.{{< /hl >}}