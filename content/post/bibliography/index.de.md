---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Bibliographien im großen Stil parsen – mit vortrainierten Sprachmodellen"
subtitle: "Wie man Tausende von Literaturangaben in kürzester Zeit in eine BibTeX-Datenbank verwandelt"
summary: "Mit GPT-3 lassen sich umfangreiche Bibliographien binnen kurzem in eine Datenbank überführen"
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

Wer die Kosten von Projekten der Digital Humanities senken will, kommt an der Automatisierung nicht vorbei. Bis heute werden die eintönigen, mühseligen Arbeiten, die das Edieren im akademischen Betrieb mit sich bringt, entweder von überlasteten Forschenden zu hohen Kosten selbst erledigt oder an Studierende „ausgelagert“. In dieser [Reihe von Blogbeiträgen](https://www.clementgodbarge.com/category/efficient-editing/) vertrete ich die Auffassung, dass sich die meisten dieser undankbaren Aufgaben nicht nur automatisieren *lassen*, sondern dass man sie automatisieren *sollte*. Das senkt die Gesamtkosten von Projekten in den Digital Humanities – und, was entscheidend ist, es erlaubt Forschenden aus einkommensschwachen Weltregionen, wertvolle Dokumente rasch und erschwinglich zu publizieren.

Im [vorigen Beitrag](https://www.clementgodbarge.com/post/gpt3/) habe ich beispielsweise gezeigt, dass vortrainierte Sprachmodelle den Großteil der XML-Auszeichnung einer digitalen Edition übernehmen können. 

Diesmal geht es um ein zweites Beispiel: die Bibliographie.


## Das Problem
Aus den Literaturangaben eines einzelnen wissenschaftlichen Aufsatzes eine bibliographische Datenbank zu machen, ist keine Kunst: Man sucht kurz in einem Katalog wie [WorldCat](https://www.worldcat.org), lädt den Nachweis im gewünschten Format herunter oder importiert ihn gleich aus einer lokalen Datenbank. Bei ein, zwei Aufsätzen geht das gut.
Ab einer gewissen Zahl von Nachweisen wird die Sache jedoch spröde und zeitraubend. Abhilfe versprechen Parser wie [anystyle.io](https://anystyle.io); nur lassen sich diese Algorithmen schlecht auf große Mengen übertragen.
Als ich anystyle auf die über 150 wissenschaftlichen Essays unserer [kritischen Edition von Ms. Fr. 640](https://edition640.makingandknowing.org/#/) losließ, häuften sich die Fehler, bis nichts mehr zu bewältigen war. Viele unserer Quellen wurden schlicht nicht erkannt: Die langen Titel frühneuzeitlicher Bücher hielt der Parser für etwas anderes, und mit weniger gängigen Dokumenten – bestimmten Webseiten, Online-Videos und dergleichen – konnte er gar nichts anfangen. Parser leisten gute Arbeit, solange sich die Autorin oder der Autor buchstabengetreu an eine bekannte Konvention wie Chicago, Turabian oder MLA hält; jede Abweichung von der Norm bezahlt man mit Fehlern.

## Die Lösung
Genau hier helfen {{< hl >}}vortrainierte Sprachmodelle{{< /hl >}}, denn sie {{< hl >}}erfassen im Nu die Muster eines jeden bibliographischen Stils{{< /hl >}} – auch eines selbst ausgedachten – und brauchen nur eine Handvoll Beispiele, um große Mengen formatierter Literaturangaben sauber in eine [BibTeX-Datenbank](http://www.bibtex.org/Format/) zu überführen. 

Anfang 2021 hatte ich das Glück, früh Zugang zu OpenAIs [GPT-3 Codex](https://openai.com/blog/openai-codex/) zu bekommen. Codex übersetzt natürliche Sprache in Code und umgekehrt. Nach Angaben von OpenAI beherrscht es mehr als ein Dutzend Programmiersprachen, und obwohl seine API, während ich dies schreibe, noch im Betastadium ist, treibt es bereits so verbreitete Anwendungen wie GitHubs [Copilot](https://github.com/features/copilot/) an.

Nach einigem Herumprobieren mit dieser API wurde mir klar, dass sie auch mit schlichterem Code wie `BibTeX` bestens zurechtkommt. 

Tatsächlich genügten vier Beispiele im Eingabeprompt, damit die Sache zuverlässig lief. 

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
Die {{< hl >}}[Ergebnisse](https://github.com/Pantagrueliste/m-k-manuscript-data/blob/master/bibliographies/essays/EssaysBibliography.bib) sind verblüffend: Über 2.000 Literaturangaben waren in wenigen Tagen konvertiert.{{< /hl >}} Das Modell hat das Muster meines Prompts nicht bloß getreu nachgebildet, sondern obendrein Eintrags- und Feldtypen korrekt ergänzt, die im Prompt gar nicht vorkamen. `GPT-3` spricht, mit anderen Worten, fließend `BibTeX`. Und was bei einem im Wesentlichen auf Englisch trainierten Modell vielleicht noch mehr überrascht: Es erkannte sämtliche Sprachen (Russisch, Französisch, Italienisch, Latein, Griechisch, Deutsch, Spanisch usw.) und setzte jedes Mal das richtige Feld `langid`.

> [!NOTE]
> Ein- und Ausgabe von GPT-3 sind derzeit begrenzt: Es verarbeitet höchstens 2048 sprachliche Tokens. Fällt diese Beschränkung, dürfte dieselbe Aufgabe in einer Stunde oder weniger erledigt sein.

Einigermaßen unerwartet fügte GPT-3 auch Angaben hinzu, die in den ursprünglichen Nachweisen gar nicht standen. 
>Baillot, Anne, and Anna Busch. “Editing for Man and Machine.” In _Users of Scholarly Editions: Editorial Anticipations of Reading, Studying and Consulting_, Vol. 13. Variants (Journal of the European Society for Textual Scholarship). Leicester, 2015. 

Bei diesem Nachweis etwa ergänzte GPT-3 den permanenten Link zum Open-Access-Repositorium ([HAL](https://hal.archives-ouvertes.fr)), in dem der Aufsatz zu lesen ist – samt der Felder `HAL_ID` und `HAL_VERSION`, die HAL eigens für sich eingeführt hat: 
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

Solche Ergänzungen zeigen, dass {{< hl >}}GPT-3 einen Literaturnachweis nicht nur zerlegt, sondern ihn aus dem, was es einst gelernt hat, auch vervollständigt.{{< /hl >}} Spannend wäre in dieser Hinsicht zu sehen, ob es sich bei Titeln, die nach seinem Training erschienen sind, genauso verhält …

## Grenzen
Vollkommen ist GPT-3 freilich nicht; ein Mensch muss ihm über die Schulter schauen. Eine seiner bekannten Schwächen ist die [Halluzination](https://arxiv.org/abs/2005.00661): Hin und wieder erfindet es etwas oder stellt unwahrscheinliche Vermutungen an. 

In meinem Versuch trat diese Neigung zutage, als GPT-3 den Familiennamen eines Autors kurzerhand von „Ruscelli“ in „Ruscello“ änderte. Streng genommen ist das kein Fehler, denn frühneuzeitliche italienische Familiennamen ließen sich unterschiedslos im Plural wie im Singular gebrauchen. Heute gilt allerdings die Regel, einen Namen so zu belassen, wie er steht, ob Plural oder Singular: Niemand würde Machiavelli heute Machiavello nennen, so wie von uns umgekehrt Rossello statt Rosselli erwartet wird. Hat GPT-3 diese Konvention aus Mangel an historischem Bewusstsein übergangen? Oder hat es sich von den Nachbarnamen leiten lassen, die in diesem Teil der Bibliographie zufällig alle im Singular stehen (Bariletto, Cesano, Rossello)?
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
Die über 150 Essays, die in vier Jahren intensiver Zusammenarbeit entstanden und [in unserer digitalen Edition enthalten sind](https://edition640.makingandknowing.org/#/essays), liefern nicht nur unentbehrliche Informationen zu der Handschrift, die wir ediert und übersetzt haben; sie bergen auch einen wertvollen bibliographischen Schatz.

Führt man diese Literaturangaben in einer Datenbank zusammen, können die Herausgeber das bibliographische Format im Handumdrehen wechseln und die Angaben darstellen, wie es ihnen beliebt. Zugleich verrät eine solche Datenbank viel über die Edition und das Projekt, aus dem sie hervorgegangen ist, und eröffnet der Forschung neue analytische Zugänge. Und sie lässt sich mit hoher Genauigkeit in Rekordzeit anlegen.

Zugegeben: Der eine oder andere Fehler kann sich einschleichen, vor allem wegen der Neigung von GPT-3 zum Halluzinieren. Doch die nächsten Generationen vortrainierter Sprachmodelle werden dieses Problem entschärfen.
