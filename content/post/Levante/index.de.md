---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Eine Wahrnehmungsgeographie der Levante"
subtitle: "Woran dachte man im Florenz des 16. Jahrhunderts bei der Levante?"
summary: "Die Levante ist ein schwer fassbares Toponym: Sie wird gewöhnlich im Verhältnis zu – oder in Abgrenzung von – einem anderen Gebiet bestimmt. Wo lag also die Levante der Toskana im 16. Jahrhundert? Die Daten, die ich aus der MIA-Datenbank gezogen habe, geben eine unerwartete Antwort."
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
  caption: "Dichtekarte der in ASFi MdP 4277 zwischen 1543 und 1566 genannten Toponyme"
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
Die *Levante* ist ein Ort, der sich entzieht. Gewöhnlich im Verhältnis zu – oder in Abgrenzung von – einem anderen Gebiet bestimmt, hat der Begriff selten eine feste Bedeutung gehabt; je nachdem, wo und wann man ihn gebrauchte, rief er eine andere Geographie auf. Doch wenn sich eine objektive, exakte Definition schon kaum formulieren lässt, so darf man doch hoffen, eine subjektive Karte dieser Region zu zeichnen – auf der Grundlage der Zusammenhänge, die sich innerhalb eines bestimmten Textkorpus zeigen. Anders gefragt: Welchen Raum konnte die *Levante* einer bestimmten Gruppe von Lesern vor Augen stellen?  
In diesem Beitrag zeige ich Ihnen, wie Sie mit Daten aus der [MIA-Datenbank](https://mia.medici.org/) des Medici Archive Project 
sichtbar machen, mit welchen konkreten Orten dieses Toponym verbunden war.  

# Die MIA-Datenbank
MIA ist eine kollaborative Plattform, auf der Forschende ihre eigenen Aufnahmen von Archivalien aus dem [Staatsarchiv Florenz](https://archiviodistatofirenze.cultura.gov.it/asfi/home) hochladen und miteinander teilen. Im vergangenen Jahr hat unser Team mit Unterstützung des [National Endowment for the Humanities](https://www.neh.gov) Tausende von Dokumenten aus der *avvisi*-Serie des *Mediceo del Principato* in Florenz fotografiert, transkribiert, regestiert und klassifiziert. Für statistische Auswertungen war die Datenbank zwar nicht in erster Linie gedacht; die Metadaten, die wir bereitstellen, lassen sich aber gleichwohl herunterladen und als Datensätze nutzen. 

# Der Datensatz
Der Datensatz, den ich hier angelegt habe, umfasst sämtliche Nachrichten aus der *Levante* von 1543 bis 1566 – vom ersten im Archiv verzeichneten Avviso bis zum Todesjahr Sultan [Süleymans I.](https://en.wikipedia.org/wiki/Suleiman_the_Magnificent). Hier ein Ausschnitt dessen, was ich vom Server geholt habe: drei Spalten mit einer eindeutigen Dokumentnummer, einem Ortsnamen und einem Datum. 

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

## Die Daten bereinigen
Bevor sich diese Daten visualisieren lassen, müssen sie als CSV-Datensatz (comma separated values) lesbar sein; außerdem wollen die geografischen Angaben in ein „maschinenfreundlicheres“ Format gebracht werden, nämlich in GPS-Koordinaten. Bei Hunderten von Einträgen macht man das lieber nicht von Hand. Vortrainierte Sprachmodelle wie [GPT-3](https://wwww.openai.org), [Bloom](https://huggingface.co/bigscience/bloom) oder [AI-21](https://www.ai21.com), um nur einige zu nennen, erledigen es ziemlich schnell und ziemlich genau – allerdings nur unter strenger Aufsicht, denn zum Halluzinieren neigen sie alle ein wenig.


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
Eine Dichtekarte zeigt, wie oft ein Ort in einem Datensatz genannt wird. Das hilft, nicht nur die geografische Reichweite der Daten zu erfassen, sondern auch ihre Brennpunkte: Welche Orte tauchen immer wieder auf, welche nur gelegentlich? Wo liegen die Zentren, wie weit reicht die Peripherie? Und wohin auf der Karte richtet sich die Aufmerksamkeit eines Lesers am ehesten? 

<iframe width='100%' height='600px' src="https://api.mapbox.com/styles/v1/clemclem/cl9q7c77p004y14mqytjrfnex.html?title=false&access_token=pk.eyJ1IjoiY2xlbWNsZW0iLCJhIjoiY2lmbGpvbjMwZjh3NnJ5bHg4ZzkzeWZzeCJ9.IgOF4fphVbsWAIKyzAV-DQ&zoomwheel=false#3.83/43.29/33.61" title="Levante" style="border:none;"></iframe>

Für dieses Experiment – und weil es schnell gehen musste – habe ich auf eine der APIs von [Mapbox](https://www.mapbox.com) zurückgegriffen. Dieselbe Art von Dichtekarte lässt sich aber mit vielen Visualisierungsbibliotheken und Geoinformationssystemen erzeugen. 

# Einige Beobachtungen
Herausgekommen ist eher ein impressionistisches Tableau als die exakte Darstellung eines sauber definierbaren Begriffs – und genau das gefällt mir an diesem Versuch. Denn {{< hl >}}die Datenwissenschaft mag den Geisteswissenschaften eine mächtige Verbündete sein; an ihre Regeln halten müssen wir uns deshalb noch lange nicht.{{< /hl >}}

Bemerkenswert ist außerdem, dass die Karte eine *Levante* zeigt, die mit dem übrigen Europa und dem Mittelmeerraum aufs Engste verflochten ist. Sie hebt zudem hervor, wie zentral Edirne in der politischen Geographie des Osmanischen Reiches stand. Die wichtigste Stadt Spaniens ist auf dieser Karte überdies weder Madrid noch der Escorial, sondern Neapel. Und nicht zuletzt scheinen Inseln und kleine Stadtstaaten wie Ragusa zwischen den Mächten der Region eine wichtige Mittlerrolle gespielt zu haben.  


# Wie man Daten bei MIA abfragt
So hervorragend MIA als kollaboratives Werkzeug für die Forschung auch ist – an die Daten auf seinen Servern kommt man nicht ohne Weiteres heran. Das Back-End etwa ist in keinem öffentlichen Repositorium veröffentlicht. Wer sich bei MIA registriert, kann die Daten aber dennoch beziehen, indem er den Server mit Python abfragt.

### Anfrage
```python
url = "https://mia.medici.org/Mia/json/de/advancedsearch/advancedSearchResults/0/90/docYear/asc/?isNewsFeedSearch=False" 
payload = [{"searchSection":"archivalLocationSearch","type":"archivalLocationAdvancedSearch","isActiveFilter":True,"repository":None,"collection":"Mediceo del Principato","series":None,"volume":"2863","insert":None},{"searchSection":"categoryAndTypologySearch","type":"categoryAndTypologyAdvancedSearch","isActiveFilter":True,"category":"News","typology":None},{"searchSection":"transcriptionSearch","type":"transcriptionAdvancedSearch","isActiveFilter":False,"transcription":""},{"isActiveFilter":False,"searchSection":"synopsisSearch","type":"synopsisAdvancedSearch","synopsis":""},{"searchSection":"placesSearch","type":"placesAdvancedSearch","isActiveFilter":False,"places":[]},{"searchSection":"peopleSearch","type":"peopleAdvancedSearch","isActiveFilter":False,"people":[]},{"searchSection":"topicsSearch","type":"topicsAdvancedSearch","isActiveFilter":True,"topics":[{"topicTitle":"Place Index","topicId":"51","placeAllId":""}]},{"searchSection":"dateSearch","type":"dateAdvancedSearch","isActiveFilter":False,"dateFilterType":"","dateYear":"","dateMonth":"","dateDay":"","dateBYear":"","dateBMonth":"","dateBDay":""},{"searchSection":"documentOwnerSearch","type":"documentOwnerAdvancedSearch","isActiveFilter":False,"editType":"owner","account":""},{"searchSection":"languagesSearch","type":"languagesAdvancedSearch","isActiveFilter":False,"languages":[]}]
headers = {'Content-type': 'application/json', 'Accept': '*/*'}
r = requests.post(url, data=json.dumps(payload), headers=headers, auth=('LOGIN','PASSWORD'))
```
Ersetzen Sie LOGIN und PASSWORD durch Ihre eigenen Zugangsdaten.

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
### Daten aus dem JSON auswählen und als CSV ausgeben
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
