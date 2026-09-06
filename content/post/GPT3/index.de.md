---
title: Auszeichnung automatisieren in digitalen wissenschaftlichen Editionen
subtitle: Lässt sich die Produktivität beim Edieren mit vortrainierten Sprachmodellen spürbar steigern?

# Summary for listings and search engines
summary: Vortrainierte Sprachmodelle können Forschenden einige der mühsamsten und arbeitsintensivsten Schritte des Edierens abnehmen. Anhand der kuratierten Annotationen von *Secrets of Craft and Nature in Renaissance France* prüfe ich, wie weit sich ein Modell wie GPT-3 in kurzer Zeit darauf trainieren lässt, technische Handschriften des 16. Jahrhunderts zu annotieren.

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
Wie bringt man eine digitale wissenschaftliche Edition zustande, ohne sich zu ruinieren? Dieser Beitrag eröffnet eine Reihe zum effizienten Edieren; ich prüfe darin, was vortrainierte Sprachmodelle leisten können, wenn es darum geht, editorische Routinearbeiten wie die semantische Auszeichnung zu automatisieren.

{{< toc >}}

# Das Problem
## Ein Werk der Liebe
Wo die Liebe hinfällt, fragt niemand nach dem Preis – so jedenfalls will es das alte Sprichwort. Auf digitale wissenschaftliche Editionen trifft das in besonderem Maße zu: Transkription, Übersetzung und Annotation verschlingen Tausende von Arbeitsstunden, die – wie bei [*Secrets of Craft and Nature in Renaissance France*](https://edition640.makingandknowing.org) – von Hunderten hochqualifizierter Mitarbeiterinnen und Mitarbeiter geleistet werden.

In gewisser Weise ist es ein Segen, dass Vorzeigeprojekte der Digital Humanities die gewaltigen Summen einwerben können, die ihr Betrieb verlangt. Doch wer sich derart auf die Großzügigkeit reicher Stiftungen, Universitäten und Behörden verlässt und über Jahre hinweg viel Personal binden muss, hat kein Wirtschaftsmodell, das die Zukunft trägt.

Wollen wir Forschende in aller Welt ermutigen, historische Dokumente einem breiteren Publikum zu erschließen, dann {{< hl >}}müssen die Kosten digitaler kritischer Editionen um Größenordnungen sinken{{< /hl >}}. 

## Eine hohe Schwelle
Paradoxerweise {{< hl >}}könnte die Lösung ausgerechnet von arbeitsintensiven Unternehmungen wie [*Secrets of Craft and Nature in Renaissance France*](https://edition640.makingandknowing.org) kommen, denn sie liefern einen wertvollen Trainingsdatensatz{{< /hl >}}, mit dem sich einige der sprödesten und eintönigsten Arbeiten des digitalen Edierens automatisieren lassen – etwa die Auszeichnung.

Nicht, dass die Auszeichnung nebensächlich wäre; im Gegenteil: {{< hl >}}Markup ist heute der unverzichtbare Bestandteil jedes ernstzunehmenden digitalen Editionsvorhabens.{{< /hl >}} Normiert durch die [Text Encoding Initiative](https://tei-c.org), erlaubt es, möglichst viele Eigenschaften des Dokuments und des Textes, den es überliefert, festzuhalten – Struktur, Marginalien, Streichungen, Varianten, Papiersorte, Flecken, Schriftbild … ganz nach Belieben.

Das folgende Beispiel aus [*Secrets of Craft and Nature in Renaissance France*](https://edition640.makingandknowing.org) zeigt, wie die Auszeichnung den Text mit Zusatzinformation anreichert (Kategorie, Struktur, semantische Felder, Streichungen usw.) – und der digitalen Edition damit einen handfesten Vorsprung vor ihren gedruckten Vorfahren verschafft.

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

Wertvoll ist diese Information für die Archivierung, aber ebenso – wie ich andernorts gezeigt habe – für Synthese und Analyse. Nur ist eine solche Annotation eben ungeheuer zeitraubend, zumal derselbe Text häufig in mehreren Gestalten vorliegen muss: als Übersetzung, als Transkription, als modernisierte Fassung und so fort. 

# Die Lösung
## Transformer: der kürzeste Weg zur Automatisierung?
2020 stellte [OpenAI](https://www.openai.com) mit großem Getöse seine neueste Familie universell einsetzbarer großer Sprachmodelle vor: GPT-3, ausgeschrieben „Generative Pre-trained Transformer 3“. Transformer sind ein noch recht junger Durchbruch der Künstlichen Intelligenz. Sie lernen neue Aufgaben verblüffend schnell – es genügt, ihnen eine Anweisung (den Prompt) und eine Handvoll Beispiele vorzulegen. Zudem lassen sie sich mit einem eigens zusammengestellten Datensatz nachtrainieren (Fine-Tuning), was Antwortzeit und Treffsicherheit verbessert. Deshalb spricht man bei GPT-3 und verwandten Transformern von [Few-Shot-Learnern](https://arxiv.org/abs/2005.14165). 

Nach Angaben von OpenAI umfasst GPT-3 die Rekordzahl von 175 Milliarden Parametern und wurde mit über 570 GB Text trainiert, überwiegend englischsprachigen Dokumenten, die vermutlich aus [dem Internet](https://skylion007.github.io/OpenWebTextCorpus/) stammen. Allein kraft seiner Größe hat GPT-3 in diesem Feld neue Maßstäbe gesetzt: Es erledigt ohne jede Anpassung die verschiedensten Aufgaben mit einem Realismus, der einen beunruhigen kann. Es schreibt glaubwürdige [Meinungsbeiträge](https://www.theguardian.com/commentisfree/2020/sep/08/robot-wrote-this-article-gpt-3), [plaudert mit Menschen](https://www.quickchat.ai/emerson) in Chatrooms, [beantwortet E-Mails](https://www.jarvis.ai/?fpr=serpbattle), [fasst Texte zusammen](https://medium.com/geekculture/a-paper-summarizer-with-python-and-gpt-3-2c718bc3bc88), übersetzt Dokumente, erklärt Fachjargon und dergleichen mehr.

Seit Mai 2021 habe ich frühen Zugang zur API von OpenAI und konnte seither ausprobieren, wie das Modell mit Aufgaben zurechtkommt, die als notorisch schwierig gelten: französische Lyrik und neulateinische Texte ins Englische übersetzen, Analogien erläutern, ja sogar den vierten Abschnitt von Kants *Grundlegung zur Metaphysik der Sitten* für ein siebenjähriges Kind herunterbrechen (wenn auch wenig überzeugend).

### Codex
Eine der jüngsten Ausprägungen von GPT-3 hat es auf Programmiersprachen abgesehen. Das Modell heißt *Codex* und übersetzt natürliche Sprache in Programmcode und umgekehrt. Suche ich etwa einen regulären Ausdruck, der „nur Wörter findet, die mit einem Großbuchstaben beginnen“, so liefert GPT-3 prompt einen funktionierenden: ```[A-Z]+\w+```.

Laut OpenAI beherrscht *Codex* ein Dutzend Programmiersprachen, darunter Python, JavaScript, Go, Perl, PHP, Ruby und Swift. Weil es Pseudocode reibungslos in Code verwandelt, kann man sich statt auf die pedantische Syntax einer Programmiersprache auf das konzentrieren, worauf es ankommt: die logischen Schritte und Strategien, mit denen ein Programm ein Problem löst.

### Jenseits von OpenAI
OpenAI ist freilich nicht der einzige Mitspieler. Wie erwähnt, kündigte die Beijing Academy of Artificial Intelligence 2021 mit *Wu Dao 2* ein noch größeres und leistungsfähigeres Modell an. Nvidia und Microsoft taten sich für das treffend benannte *Megatron-Turing NLG 530B* zusammen. Kleinere Start-ups wie [AI21 Labs](https://www.ai21.com) und [Cohere](https://cohere.ai) bieten der Öffentlichkeit ebenfalls APIs an, und auch Open-Source-Initiativen wie [EleutherAI](https://www.eleuther.ai) verdienen Erwähnung. Die KI-Szene ist natürlich in rasender Bewegung; wer auf dem Laufenden bleiben will, sollte einen Blick auf [Hugging Face](https://huggingface.co/transformers/master/index.html) werfen.

# Die Experimente

> [!NOTE]
> Ziel dieser Experimente ist es, den sparsamsten Weg zu einer verlässlichen Automatisierung editorischer Aufgaben zu finden. Man könnte einwenden, dass sich manche davon auch mit Verfahren des überwachten Lernens automatisieren ließen. Dieser Hypothese gehen wir in einem späteren Beitrag nach.

Kann ein Transformer wie GPT-3 lernen, etwa eine technisch-naturwissenschaftliche Handschrift des 16. Jahrhunderts zu annotieren?

## Experiment 1 – Textkategorisierung
Beginnen wir mit etwas vergleichsweise Einfachem. Als „Few-Shot-Learner“ sollte GPT-3 rasch durchschauen, nach welchem Schema unser Herausgeberteam die Einträge von Ms. Fr. 640 klassifiziert hat.

### Prompt-Engineering
Zum Anlernen begnügte ich mich mit einem denkbar knappen Prompt und vier kurzen Einträgen im Reintext als Beispielen, darunter je einer zu „Medizin“, „Waffen und Rüstungen“ und „Malerei“. 

### Test
Anschließend kopierte ich eine weitere Passage hinein, die in der ursprünglichen Folge nicht enthalten war: 

```text
Working neatly
Never put down, if you can, two colors one on top of the other.   
But next, having made your design carefully, keep the place of shadows for them alone,
& also separately that of lights & highlights, without layering one color all over & then highlighting or else shading on it.  
And in this way, you further your work, economize your colors & work neatly.  
Which is the reason that, the colors not being muddled nor mixed together, they do not die & you soften the colors better, since they are not so thick.
```
Die Ausgabe passt vollkommen zum Inhalt: 

```xml
<categories="painting">
```

Nimmt man einen Eintrag aus einer Kategorie, die in der Auswahl der Trainingstexte gar nicht vorkam, überrascht das Ergebnis. 

```xml
<categories="jewelry">
```

### Ergebnis
Eine Kategorie „jewelry“ (Schmuck) gibt es in unserer Edition von Ms. Fr. 640 nicht; das Herausgeberteam [bevorzugt](https://edition640.makingandknowing.org/#/content/resources) die weiter gefasste Rubrik „Stones“ (Steine). Der Instinkt von GPT-3 ist gleichwohl richtig, und das lässt erwarten, dass es mit ein wenig mehr Training jeden Eintrag von Ms. Fr. 640 einordnen könnte – womöglich sogar Einträge vergleichbarer technischer Texte des 16. Jahrhunderts.   

## Experiment 2 – Semantische Auszeichnung
Legen wir die Latte etwas höher. Wenn Transformer wie GPT-3 lernen können, Texte nach bestimmten editorischen Kriterien zu klassifizieren – erkennen sie dann auch einen Teil der Auszeichnung im Text?  

> [!NOTE]
> *Secrets of Craft and Nature* verwendet eine [Kombination](https://edition640.makingandknowing.org/#/content/resources/principles) aus semantischen und strukturellen Labels. Leider verarbeitet GPT-3 keine Bilder, anders als etwa [Wu Dao 2](https://towardsdatascience.com/gpt-3-scared-you-meet-wu-dao-2-0-a-monster-of-1-75-trillion-parameters-832cd83db484). Künftige Versionen von GPT werden diese Fähigkeit wahrscheinlich mitbringen; ohne sie lassen sich die meisten strukturellen und materiellen Merkmale eines Dokuments nicht erkennen. Wir übergehen diese Tags daher und wenden uns der Auszeichnung zu, die ohne Bilderkennung auskommt.

### Prompt-Engineering
Semantische Tags erfassen unter anderem Tiere, Pflanzen, Ortsnamen und Sinneseindrücke. Für den Trainingsprompt griff ich einige Beispiele aus der Edition heraus:
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
Versuchen wir es mit dem Modell `Davinci-codex` und ein paar leichten Wörtern: *Apothecary* (Apotheker), *smoke* (Rauch), *glassmakers* (Glasmacher), *latten* (Messingblech) und *snake* (Schlange). Die Antwort kommt sofort, und sie ist fehlerfrei:

```xml
<!--Output-->
Apothecary: <pro>Apothecary</pro>
smoke: <m>smoke<m>
glassmakers: <pro>glassmakers</pro>
latten: <m>latten</m>
snake: <al>snake</al>
```

Schwieriger wird es mit zusammengesetzten Ausdrücken wie *copper plates* (Kupferplatten), *walnut oil* (Walnussöl) und *wood block* (Holzblock). Hier soll sich zeigen, ob GPT-3 mit verschachtelten Tags zurechtkommt. 

```xml
<!--Output-->
copper plates: <m>copper plates</m>
walnut oil: <m><pa>walnut</pa> oil</m>
wood block: <m>wood block</m>
```

Das Ergebnis ist durchwachsen: `Davinci-codex` hat nur *walnut oil* korrekt ausgezeichnet und die verschachtelten Tags `tl` und `m` in *copper plates* und *wood block* übersehen. Wie der nächste Test zeigt, lassen sich solche Fehler indes mit einem besseren Trainingsprompt eindämmen. Nachdem ich fünf weitere Beispiele für verschachtelte Tags ergänzt hatte, lieferte `Davinci-codex` ein nahezu makelloses Ergebnis mit einem einzigen Fehler (*oil paintbrushes*):

```xml
<!--Output-->
cannon powder: <m><wp>cannon</wp> powder</m>
arquebus powder: <m><wp>arquebus</wp> powder</m>
oil paintbrushes: <m><al>oil</al> paintbrushes</m>
sheep footbones: <m><al>sheep</al> footbones</m>
bronze mortar: <tl><m>bronze</m> mortar</tl>
```

# Fazit
Vergessen wir nicht, dass diese Tests mit kleinen Textstücken gemacht wurden. Ich vermute, dass GPT-3-Modelle noch besser abschneiden, wenn Beispiele und Prompt mehr Kontext bieten; und ein Fine-Tuning mit eigens angelegten Trainingsdaten würde die Treffsicherheit der Auszeichnung zweifellos weiter erhöhen.  
Gewiss müssten diese Versuche in größerem Maßstab wiederholt werden, um die Verlässlichkeit vortrainierter Sprachmodelle nachzuweisen. Festhalten lässt sich aber schon jetzt, dass {{< hl >}}dieser Ansatz Editorinnen und Editoren erlaubt, mehrere Annotationsaufgaben in wenigen einfachen Schritten zu automatisieren – und dabei womöglich enorm viel Zeit und Geld zu sparen.{{< /hl >}}
