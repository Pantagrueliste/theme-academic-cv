---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Eine Wahrnehmungsgeographie der Levante"
subtitle: "Womit wurde die Levante im Florenz des 16. Jahrhunderts assoziiert?"
summary: "Die Levante ist ein schwer fassbares Toponym, da sie üblicherweise in Bezug auf – oder in Abgrenzung von – ein anderes Gebiet definiert wird. Was war also die Levante der Toskana im 16. Jahrhundert? Die Daten, die ich aus der MIA-Datenbank zusammengetragen habe, geben eine unerwartete Antwort."
authors: [clement]
tags: [MAP, Avviso]
categories: [Notizen]
date: 2022-10-29T10:02:52-05:00
lastmod: 2022-10-29T10:02:52-05:00
featured: true
machine_translated: true
draft: false


# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: "Dichtekarte der in ASFi MdP 4277 zwischen 1543 und 1566 erwähnten Toponyme"
  focal_point: ""
  preview_only: true

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: ["MAP"]
---

# Einleitung
Die *Levante* ist ein schwer fassbarer Ort. Üblicherweise in Bezug auf – oder in Abgrenzung von – ein anderes Gebiet definiert, war ihre Bedeutung selten stabil und rief je nach Ort und Zeit, in denen der Begriff verwendet wurde, unterschiedliche Geographien hervor. Doch auch wenn sich eine objektive und genaue Definition des Begriffs kaum formulieren lässt, kann man immer noch hoffen, eine subjektive Karte dieser Region zu zeichnen, und zwar auf der Grundlage der Korrelationen, die innerhalb eines bestimmten Textkorpus bestehen. Mit anderen Worten: Welchen Raum konnte die *Levante* für eine bestimmte Gruppe von Lesern evozieren?  
In diesem Beitrag zeige ich Ihnen, wie Sie Daten aus der [MIA-Datenbank](https://mia.medici.org/) des Medici Archive Project verwenden können, 
um die konkreten Orte zu visualisieren, mit denen das Toponym verknüpft war.  

# Die MIA-Datenbank
Die MIA-Datenbank ist eine kollaborative Plattform für Forschende, die ihre eigenen Fotografien von Archivmaterial aus dem [Staatsarchiv Florenz](https://archiviodistatofirenze.cultura.gov.it/asfi/home) hochladen und teilen möchten. Im Laufe des vergangenen Jahres hat unser Team unter der Schirmherrschaft des [National Endowment for the Humanities](https://www.neh.gov) Tausende von Dokumenten aus der *avvisi*-Abteilung des Archivs *Mediceo del Principato* in Florenz fotografiert, transkribiert, zusammengefasst und klassifiziert. Obwohl unsere Datenbank nicht in erster Linie für statistische Analysen gedacht war, lassen sich die von uns bereitgestellten Metadaten dennoch herunterladen und als Datensätze verwenden. 

# Der Datensatz
In diesem Fall umfasst der von mir erstellte Datensatz alle Nachrichten aus der *Levante* von 1543 bis 1566, das heißt vom ersten in den Archiven verzeichneten Avviso bis zum Todesjahr des Sultans [Süleyman I.](https://en.wikipedia.org/wiki/Suleiman_the_Magnificent). Hier ein Ausschnitt der Daten, die ich vom Server extrahiert habe. Die Daten bestehen aus drei Spalten: einer eindeutigen Dokumentnummer, einem Ortsnamen und einem Datum. 

```csv
57386 Malta / Europe / World / Top of the TGN hierarchy 1565-1-3
57386 Modon / Messinias, Nomos / Peloponnisos / Ellas 1565-1-3
57386 Al-Iskandariyah / Muhafazat al Iskandariyah / Egypt / Africa  1565-1-3
57386 Evvoia / Evvoias, Nomos / Sterea Ellas-Evvoia / Ellas 1565-1-3
57386 Venetian Republic / Italia / Europe / World 1565-1-3
57386 Arsenale / Istanbul / Istanbul / Marmara  1565-1-3
57386 Black Sea / Asia / World / Top of the TGN hierarchy 1565-1-3
57389 Otranto / Lecce / Puglia / Italia 1565-1-3
57389 Nisoi Aiyaiou / Ellas / Europe / World  1565-1-3
57389 Malta / Europe / World / Top of the TGN hierarchy 1565-1-3
57389 Buda / Budapest / Budapest / Magyarorszag 1565-1-3
57389 Al-Iskandariyah / Muhafazat al Iskandariyah / Egypt / Africa  1565-1-3
57389 Kipros / Asia / World / Top of the TGN hierarchy  1565-1-3
57389 Rodhos / Rodos, Nisos / Sporadhes / Nisoi Aiyaiou 1565-1-3
57389 Arsenale / Istanbul / Istanbul / Marmara  1565-1-3
57389 Çorlu / Thraki / Ellas / Europe 1565-1-3
```

## Bereinigung der Daten
Um diese Daten zu visualisieren, müssen wir sie als CSV-Datensatz (comma separated values) lesbar machen. Außerdem müssen wir die hier enthaltenen geografischen Angaben in ein „maschinenfreundlicheres“ Format umwandeln: GPS-Koordinaten. Da der Datensatz Hunderte von Einträgen enthält, wollen wir diesen Vorgang lieber automatisieren. Das lässt sich recht schnell und ziemlich genau mit vortrainierten Sprachmodellen wie [GPT-3](https://wwww.openai.org), [Bloom](https://huggingface.co/bigscience/bloom) oder [AI-21](https://www.ai21.com) erreichen, um nur einige zu nennen. Dieser Vorgang muss allerdings eng überwacht werden, da vortrainierte Sprachmodelle eine leichte Neigung zum Halluzinieren haben.


```csv
documentId,latitude,longitude,documentDate
57386,35.899167,14.514167,1565-1-3
57386,37.05,22.116667,1565-1-3
57386,31.200028,29.918719,1565-1-3
57386,38.366667,23.666667,1565-1-3
57386,45.438333,12.331333,1565-1-3
57386,41.018611,28.984444,1565-1-3
57386,42.7,18.8,1565-1-3
57389,40.216667,18.166667,1565-1-3
57389,37.966667,23.716667,1565-1-3
57389,35.899167,14.514167,1565-1-3
57389,47.4925,19.051389,1565-1-3
57389,31.200028,29.918719,1565-1-3
57389,34.916667,33.616667,1565-1-3
57389,36.405419,28.227778,1565-1-3
57389,41.018611,28.984444,1565-1-3
57389,41.133333,27.416667,1565-1-3
```

# Die Dichtekarte
Eine Dichtekarte ist eine Art der Visualisierung, die hervorhebt, wie häufig ein Ort in einem bestimmten Datensatz erwähnt wird. Das ist besonders nützlich, um nicht nur die geografische Reichweite der eigenen Daten zu verstehen, sondern auch ihre Schwerpunkte. Welche Orte auf der Karte werden häufiger erwähnt? Und welche eher episodisch? Wo liegen die Zentren, und wie weit entfernt ist die Peripherie? Worauf richtet sich die Aufmerksamkeit eines Lesers auf der Karte am wahrscheinlichsten? 

<iframe width='100%' height='600px' src="https://api.mapbox.com/styles/v1/clemclem/cl9q7c77p004y14mqytjrfnex.html?title=false&access_token=pk.eyJ1IjoiY2xlbWNsZW0iLCJhIjoiY2lmbGpvbjMwZjh3NnJ5bHg4ZzkzeWZzeCJ9.IgOF4fphVbsWAIKyzAV-DQ&zoomwheel=false#3.83/43.29/33.61" title="Levante" style="border:none;"></iframe>

Für dieses Experiment – und weil ich es eilig hatte – habe ich eine der APIs von [Mapbox](https://www.mapbox.com) verwendet. Viele Visualisierungsbibliotheken und Geoinformationssysteme erlauben es jedoch, dieselbe Art von Dichtekarte zu erstellen. 

# Einige Beobachtungen
Das Ergebnis ist eher ein impressionistisches Tableau als die genaue Darstellung eines klar definierbaren Konzepts, und genau das gefällt mir an diesem Experiment. Denn {{< hl >}}auch wenn die Datenwissenschaft ein mächtiger Verbündeter der Geisteswissenschaften sein kann, müssen wir uns nicht unbedingt an ihre Regeln halten.{{< /hl >}}

Ein weiterer interessanter Aspekt dieses Experiments ist, dass die Karte eine *Levante* zeigt, die vollständig in das übrige Europa und den Mittelmeerraum integriert ist. Sie unterstreicht außerdem die zentrale Stellung von Edirne in der politischen Geographie des Osmanischen Reiches. Darüber hinaus ist die wichtigste Stadt Spaniens auf der Karte weder Madrid noch der Escorial, sondern Neapel. Und nicht zuletzt scheinen Inseln und kleine Stadtstaaten wie Ragusa eine wichtige Vermittlerrolle zwischen den verschiedenen Mächten der Region gespielt zu haben.  


# Wie man Daten von MIA anfordert
Obwohl MIA ein hervorragendes kollaboratives Werkzeug für Forschende ist, sind die auf seinen Servern gespeicherten Daten nicht leicht zugänglich. Sein Back-End ist zum Beispiel nicht in öffentlichen Repositorien veröffentlicht. Sie können die Daten dennoch erhalten, indem Sie sich bei MIA registrieren und mit Python Anfragen an den Server stellen.

### Anfrage
```python
url = "https://mia.medici.org/Mia/json/de/advancedsearch/advancedSearchResults/0/90/docYear/asc/?isNewsFeedSearch=False" 
payload = [{"searchSection":"archivalLocationSearch","type":"archivalLocationAdvancedSearch","isActiveFilter":True,"repository":None,"collection":"Mediceo del Principato","series":None,"volume":"2863","insert":None},{"searchSection":"categoryAndTypologySearch","type":"categoryAndTypologyAdvancedSearch","isActiveFilter":True,"category":"News","typology":None},{"searchSection":"transcriptionSearch","type":"transcriptionAdvancedSearch","isActiveFilter":False,"transcription":""},{"isActiveFilter":False,"searchSection":"synopsisSearch","type":"synopsisAdvancedSearch","synopsis":""},{"searchSection":"placesSearch","type":"placesAdvancedSearch","isActiveFilter":False,"places":[]},{"searchSection":"peopleSearch","type":"peopleAdvancedSearch","isActiveFilter":False,"people":[]},{"searchSection":"topicsSearch","type":"topicsAdvancedSearch","isActiveFilter":True,"topics":[{"topicTitle":"Place Index","topicId":"51","placeAllId":""}]},{"searchSection":"dateSearch","type":"dateAdvancedSearch","isActiveFilter":False,"dateFilterType":"","dateYear":"","dateMonth":"","dateDay":"","dateBYear":"","dateBMonth":"","dateBDay":""},{"searchSection":"documentOwnerSearch","type":"documentOwnerAdvancedSearch","isActiveFilter":False,"editType":"owner","account":""},{"searchSection":"languagesSearch","type":"languagesAdvancedSearch","isActiveFilter":False,"languages":[]}]
headers = {'Content-type': 'application/json', 'Accept': '*/*'}
r = requests.post(url, data=json.dumps(payload), headers=headers, auth=('LOGIN','PASSWORD'))
```
Achten Sie darauf, LOGIN und PASSWORD durch Ihre eigenen Zugangsdaten zu ersetzen.

### Antwort in eine Datei schreiben
```python
with open('response.json', 'wb') as fd:
    for chunk in r.iter_content(chunk_size=128):
        fd.write(chunk)
```
### JSON öffnen
```python
f = open('response.json', encoding="utf8")
```
### JSON-Objekt als Dictionary zurückgeben
```python
json_complete = json.load(f)
```
### Daten aus dem JSON auswählen und im CSV-Format ausgeben
```python
with open('results.csv', 'w', newline='') as csvfile:
    fieldnames = ['documentId', 'placeCited', 'documentDate']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for i in json_complete['data']:
        if i['topics'] != None:
            for x in i['topics']:
                documentId=x['documentId']
                placeCited=x['topicPlaceName']
                year=i['date']['docYear']
                month=i['date']['docMonth']
                day=i['date']['docDay']
                documentDate=str(year)+ "-" + str(month)+"-" + str(day)
                writer.writerow({'documentId': documentId, 'placeCited': placeCited, 'documentDate': documentDate})
```

Sobald Sie die Datei `results.csv` heruntergeladen haben, können Sie die Daten wie oben beschrieben bereinigen. 
