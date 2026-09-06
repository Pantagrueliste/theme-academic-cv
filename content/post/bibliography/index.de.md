---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Bibliographisches Parsing im großen Maßstab mit vortrainierten Sprachmodellen"
subtitle: "Wie man Tausende bibliographischer Referenzen rasch in eine BibTeX-Datenbank umwandelt"
summary: "GPT-3 hilft dabei, große Mengen an Bibliographie in kurzer Zeit in eine Datenbank zu überführen"
authors: [clement]
tags: [Digital Humanities, GPT-3, Bibliographie, Automatisierung]
categories: [Effizientes Edieren]
date: 2022-07-07T19:04:14+02:00
lastmod: 2022-07-07T19:04:14+02:00
featured: false
machine_translated: true
draft: false

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ""
  focal_point: ""
  preview_only: false

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: [Efficient Editing]
---

Automatisierung ist der Schlüssel, um die Kosten von Projekten der Digital Humanities zu senken. Bis heute wurden die repetitiven und mühsamen Aufgaben, die mit editorischer Arbeit im akademischen Umfeld verbunden sind, entweder zu hohen Kosten von überlasteten Forschenden erledigt oder an Studierende „ausgelagert“. In dieser [Reihe von Blogbeiträgen](https://www.clementgodbarge.com/category/efficient-editing/) argumentiere ich, dass die meisten dieser undankbaren Aufgaben nicht nur automatisiert werden *können*, sondern auch *sollten*. Die Automatisierung editorischer Aufgaben senkt die Gesamtkosten von Projekten in den Digital Humanities. Entscheidend ist, dass sie Forschenden aus einkommensschwachen Regionen ermöglicht, wertvolle Dokumente rasch und kostengünstig zu veröffentlichen.

Im [vorherigen Beitrag](https://www.clementgodbarge.com/post/gpt3/) habe ich beispielsweise gezeigt, wie vortrainierte Sprachmodelle den Großteil der XML-Auszeichnungsarbeit einer digitalen Edition übernehmen können. 

In diesem Beitrag stelle ich ein zweites Beispiel vor, diesmal anhand von Bibliographien.


## Das Problem
Aus den in einem wissenschaftlichen Aufsatz genannten Literaturangaben eine bibliographische Datenbank zu erstellen, ist recht unkompliziert. Man kann entweder eine schnelle Suche in einem Katalog wie [WorldCat](https://www.worldcat.org) durchführen, die Referenz in einem bestimmten Format herunterladen oder sie automatisch aus einer lokalen Datenbank importieren. Bei ein oder zwei Aufsätzen funktioniert das gut.
Jenseits einer bestimmten Anzahl von Referenzen wird die Aufgabe jedoch widerspenstig und zeitraubend. Um dem abzuhelfen, kann man Parsing-Algorithmen wie [anystyle.io](https://anystyle.io) verwenden. Doch diese Algorithmen lassen sich nur schwer skalieren.
Als ich anystyle einsetzte, um die mehr als 150 wissenschaftlichen Essays unserer [kritischen Edition von Ms. Fr. 640](https://edition640.makingandknowing.org/#/) zu konvertieren, war die Menge der angehäuften Fehler schlicht nicht mehr zu bewältigen. Viele unserer Quellen wurden nicht richtig erkannt; so wurden etwa die langen Titel frühneuzeitlicher Bücher mit etwas anderem verwechselt, und weniger typische Dokumente wie bestimmte Webseiten, Online-Videos usw. wurden gar nicht erkannt. Parser funktionieren gut, sofern sich die Autorin oder der Autor strikt an die Regeln einer bekannten Konvention wie Chicago, Turabian oder MLA hält. Jede Abweichung von der Norm führt zu Fehlern.

## Die Lösung
Hier können {{< hl >}}vortrainierte Sprachmodelle{{< /hl >}} helfen, denn sie {{< hl >}}verstehen rasch die Muster jedes bibliographischen Stils{{< /hl >}}, sogar eines selbst erfundenen, und benötigen nur wenige Beispiele, um große Mengen formatierter Bibliographie korrekt in eine [BibTeX-Datenbank](http://www.bibtex.org/Format/) zu konvertieren. 

Anfang 2021 hatte ich das Glück, frühen Zugang zu OpenAIs [GPT-3 Codex](https://openai.com/blog/openai-codex/) zu erhalten. Codex ist ein Modell, das es ermöglicht, natürliche Sprache in Code zu übersetzen und umgekehrt. OpenAI gibt an, dass es mehr als ein Dutzend Programmiersprachen beherrscht, und obwohl seine API zu dem Zeitpunkt, da ich diesen Beitrag schreibe, noch als Betaversion zugänglich ist, treibt es bereits beliebte Anwendungen wie GitHubs [Copilot](https://github.com/features/copilot/) an.

Nachdem ich mit dieser API herumexperimentiert hatte, stellte ich fest, dass sie auch mit einfacherem Code wie `BibTeX` sehr gut funktioniert. 

Und tatsächlich brauchte ich nur vier Beispiele im Eingabeprompt, damit das zuverlässig funktionierte. 

### Eingabeprompt

References:
Bayle, Ariane. “Patients exemplaires: la correspondance médicale de Fioravanti.” In *Vulgariser la médecine. Du style médical en France et en Italie*, edited by Andrea Carlino and Michel Jeanneret, 181–212. Geneva: Droz, 2009.  

Berns, Andrew D. *The Bible and Natural Philosophy in Renaissance Italy: Jewish and Christian Physicians in Search of Truth*. Cambridge: Cambridge University Press, 2015.  

Gabler, Hans Walter. “Theorizing the Digital Scholarly Edition.” *Literature Compass* 7, no. 2 (2010): 43–56. https://doi.org/10.1111/j.1741-4113.2009.00675.x.  

Findlen, Paula. *Possessing Nature: Museums, Collecting, and Scientific Culture in Early Modern Italy*. Berkeley: University of California Press, 1994.

```BibTeX
@incollection{bayle2009,
  author = {Bayle, Ariane},
  booktitle = {Vulgariser la médecine. Du style médical en France et en Italie},
  title = {Patients exemplaires: la correspondance médicale de Fioravanti},
  editor = {Carlino, Andrea and Michel Jeanneret},
  year = {2009},
  address = {Geneva},
  publisher = {Droz},
  langid = {french}
}
@book{berns2015,
  title = {The Bible and Natural Philosophy in Renaissance Italy: Jewish and Christian Physicians in Search of Truth},
  author = {Berns, Andrew D.},
  address = {Cambridge},
  publisher = {Cambridge University Press},
  langid = {english},
  date = {2015}
}
@article{gabler2010,
  author = {Gabler, Hans Walter},
  title = {Theorizing the Digital Scholarly Edition},
  journal = {Literature Compass},
  volume = {7},
  number = {2},
  pages = {43-56},
  doi = {10.1111/j.1741-4113.2009.00675.x},
  langid = {english},
  year = {2010}
}
@book{findlen1994,
  title = {Possessing Nature: Museums, Collecting, and Scientific Culture in Early Modern Italy},
  author = {Findlen, Paula},
  address = {Berkeley},
  publisher = {University of California Press},
  langid = {english},
  date = {1994}
}
```

### Ergebnisse
Die {{< hl >}}[Ergebnisse](https://github.com/Pantagrueliste/m-k-manuscript-data/blob/master/bibliographies/essays/EssaysBibliography.bib) sind verblüffend: Mehr als 2.000 bibliographische Referenzen wurden innerhalb weniger Tage konvertiert.{{< /hl >}} Dieser Ansatz reproduzierte nicht nur exakt das in meinem Eingabeprompt vorgegebene Muster, sondern fügte auch korrekt Eintrags- und Feldtypen hinzu, die im Eingabeprompt nicht enthalten waren. `GPT-3` beherrscht `BibTeX`, mit anderen Worten, fließend. Vielleicht noch überraschender für ein im Wesentlichen auf Englisch trainiertes Modell: Es erkannte alle Sprachen (Russisch, Französisch, Italienisch, Latein, Griechisch, Deutsch, Spanisch usw.) und fügte jedes Mal das richtige Feld `langid` hinzu.

> [!NOTE]
> GPT-3 hat derzeit begrenzte Ein- und Ausgabegrößen, da es maximal 2048 sprachliche Tokens verarbeiten kann. Sobald diese Beschränkung aufgehoben wird, dürfte dieselbe Aufgabe wahrscheinlich eine Stunde oder weniger dauern.

Etwas unerwartet fügte GPT-3 auch Informationen hinzu, die in den ursprünglichen Referenzen nicht enthalten waren. 
>Baillot, Anne, and Anna Busch. “Editing for Man and Machine.” In _Users of Scholarly Editions: Editorial Anticipations of Reading, Studying and Consulting_, Vol. 13. Variants (Journal of the European Society for Textual Scholarship). Leicester, 2015. 

Bei dieser bibliographischen Referenz beispielsweise fügte GPT-3 den permanenten Link zum Open-Access-Repositorium ([HAL](https://hal.archives-ouvertes.fr)) hinzu, in dem der Aufsatz gelesen werden kann, einschließlich der vom HAL-Repositorium eingeführten Ad-hoc-Felder `HAL_ID` und `HAL_VERSION`: 
```BibTeX
@inproceedings{baillot2015, 
  title = {Editing for Man and Machine},
  author = {Baillot, Anne and Busch, Anna},
  year = 2015,
  booktitle = {Users of Scholarly Editions: Editorial Anticipations of Reading, Studying and Consulting},
  address = {Leicester},
  series = {Variants (Journal of the European Society for Textual Scholarship)},
  volume = 13,
  editor = {Bruhn, Siglinde and Schreiber, Manfred},
  langid = {english},
  hal_id = {halshs-01233380},
  hal_version = {v1}
}
```

Diese Ergänzungen zeigen, dass {{< hl >}}GPT-3 die bibliographische Referenz nicht nur parst, sondern sie auf der Grundlage dessen, was es ursprünglich gelernt hat, auch vervollständigt.{{< /hl >}} Interessant wäre in dieser Hinsicht zu sehen, ob es sich bei Referenzen, die nach dem Training von GPT-3 datieren, ähnlich verhält …

## Grenzen
GPT-3 ist jedoch nicht perfekt. Es muss von einem Menschen überwacht werden. Eine seiner bekannten Schwächen ist die [Halluzination](https://arxiv.org/abs/2005.00661): Manchmal erfindet es Dinge und trifft unwahrscheinliche Annahmen. 

In meinem Experiment zeigten sich die Inkohärenzanfälle von GPT-3, als es spontan den Familiennamen eines Autors von „Ruscelli“ zu „Ruscello“ änderte. Das ist streng genommen kein Fehler, denn frühneuzeitliche italienische Familiennamen konnten unterschiedslos im Plural oder im Singular verwendet werden. Heute gilt jedoch die Konvention, dass ein Familienname, ob im Plural oder im Singular, so belassen wird, wie er ist. Niemand würde heute Machiavelli Machiavello nennen, so wie von uns erwartet wird, den Namen Rossello statt Rosselli zu verwenden. Hat GPT-3 diese Konvention aus Mangel an chronologischem Bewusstsein ignoriert? Oder hat GPT-3 eine Annahme auf der Grundlage benachbarter Familiennamen getroffen, die in diesem Teil der Bibliographie zufällig alle im Singular stehen (Bariletto, Cesano, Rossello)?
Wer weiß.

```Bibtex
@book{rossello1565,
  title = {Della summa de’ secreti universali},
  author = {Rossello, Timoteo},
  address = {Venice},
  publisher = {Giovanni Bariletto},
  langid = {italian},
  date = {1565}
}
@book{ruscello1559, 
  title = {La seconda parte de’ secreti del Reverendo Donno Alessio Piemontese},
  author = {Ruscello, Girolamo},
  address = {Pesaro}, 
  publisher = {Bartolomeo Cesano}, 
  langid = {italian}, 
  date = {1559}
}
```

## Fazit
Die über vier Jahre intensiver Zusammenarbeit entstandenen mehr als 150 Essays, [die in unserer digitalen Edition enthalten sind](https://edition640.makingandknowing.org/#/essays), liefern nicht nur wesentliche Informationen über die von uns edierte und übersetzte Handschrift, sondern enthalten auch wertvolle bibliographische Angaben.

Diese bibliographischen Referenzen in einer Datenbank zusammenzuführen, ermöglicht es den Herausgebern, die bibliographische Formatierung im Handumdrehen zu ändern, und gibt ihnen mehr Flexibilität, diese Informationen nach Belieben darzustellen. Die Datenbank liefert zudem wertvolle Informationen über die Edition und das Projekt, das sie möglich gemacht hat, und eröffnet Forschenden neue analytische Perspektiven. Eine solche Datenbank lässt sich mit hoher Genauigkeit und in Rekordzeit fertigstellen.

Zugegeben, einige Fehler können sich einschleichen, insbesondere wegen der Neigung von GPT-3 zum Halluzinieren. Doch künftige Generationen vortrainierter Sprachmodelle werden dieses Problem abmildern.
