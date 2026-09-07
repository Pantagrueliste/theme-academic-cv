---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "En upplevd geografi över Levanten"
subtitle: "Vad förknippades Levanten med i 1500-talets Florens?"
summary: "Levanten är ett undflyende ortnamn: det brukar definieras i förhållande till – eller i motsats till – ett annat territorium. Vad var då Toscanas Levante på 1500-talet? De data jag hämtat ur MIA-databasen ger ett oväntat svar."
authors: [clement]
tags: [MAP, Avviso]
categories: [Anteckningar]
date: 2022-10-29T10:02:52-05:00
lastmod: 2022-10-29T10:02:52-05:00
featured: true
machine_translated: true
draft: false


# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: "Densitetskarta över ortnamn som nämns i ASFi MdP 4277 mellan 1543 och 1566"
  focal_point: ""
  preview_only: true

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: ["MAP"]
---

# Inledning
*Levante* – Levanten – är en undflyende plats. Den definieras vanligen i förhållande till – eller i motsats till – ett annat territorium, och dess innebörd har sällan varit stabil: den har frammanat olika geografier beroende på var och när ordet använts. Men även om en objektiv och exakt definition är svår att formulera kan man ändå hoppas kunna rita en subjektiv karta över regionen, med de samband som finns inom en given textkorpus som underlag. Med andra ord: vilket rum kunde *Levante* frammana hos en bestämd krets av läsare?  
I det här inlägget visar jag hur man med data från Medici Archive Projects [MIA-databas](https://mia.medici.org/) 
kan visualisera vilka platser ortnamnet förknippades med.  

# MIA-databasen
MIA-databasen är en samarbetsplattform för forskare som vill ladda upp och dela sina egna fotografier av arkivmaterial från [Statsarkivet i Florens](https://archiviodistatofirenze.cultura.gov.it/asfi/home). Under det gångna året har vårt team, med stöd av [National Endowment for the Humanities](https://www.neh.gov), fotograferat, transkriberat, sammanfattat och klassificerat tusentals dokument ur *avvisi*-avdelningen i arkivet *Mediceo del Principato* i Florens. Databasen var visserligen inte i första hand tänkt för statistisk analys, men de metadata vi gjort tillgängliga kan ändå laddas ner och användas som datamängder. 

# Datamängden
I det här fallet täcker den datamängd jag skapade alla nyheter från *Levante* mellan 1543 och 1566, dvs. från den första avviso som finns registrerad i arkivet till det år då sultan [Süleyman I](https://en.wikipedia.org/wiki/Suleiman_the_Magnificent) dör. Här är ett utdrag ur de data jag hämtade från servern. De består av tre kolumner: ett unikt dokumentnummer, ett ortnamn och ett datum. 

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

## Att städa data
För att kunna visualisera dessa data måste vi göra dem läsbara som csv (kommaseparerade värden). Den geografiska informationen måste dessutom omvandlas till ett mer ”maskinvänligt” format: GPS-koordinater. Eftersom datamängden rymmer hundratals poster vill vi helst automatisera processen. Det går ganska snabbt och rätt exakt med förtränade språkmodeller som [GPT-3](https://wwww.openai.org), [Bloom](https://huggingface.co/bigscience/bloom) eller [AI-21](https://www.ai21.com), för att bara nämna några. Momentet måste dock övervakas noga, eftersom förtränade språkmodeller har en viss benägenhet att hallucinera.


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

# Densitetskartan
En densitetskarta är en visualisering som lyfter fram hur ofta en plats nämns i en given datamängd. Den är särskilt användbar när man vill förstå inte bara sina datas geografiska räckvidd utan också deras tyngdpunkter. Vilka platser på kartan nämns oftast, och vilka bara sporadiskt? Var ligger centrum, och hur långt bort är periferin? Var på kartan är det troligast att en läsares uppmärksamhet fastnade? 

<iframe width='100%' height='600px' src="https://api.mapbox.com/styles/v1/clemclem/cl9q7c77p004y14mqytjrfnex.html?title=false&access_token=pk.eyJ1IjoiY2xlbWNsZW0iLCJhIjoiY2lmbGpvbjMwZjh3NnJ5bHg4ZzkzeWZzeCJ9.IgOF4fphVbsWAIKyzAV-DQ&zoomwheel=false#3.83/43.29/33.61" title="Levante" style="border:none;"></iframe>

För det här experimentet – och eftersom jag hade bråttom – använde jag ett av [Mapbox](https://www.mapbox.com) API:er. Men många visualiseringsbibliotek och geografiska informationssystem låter dig framställa samma slags densitetskarta. 

# Några iakttagelser
Resultatet är snarare en impressionistisk tavla än en exakt bild av ett klart definierbart begrepp, och det är just det jag tycker om med experimentet. Ty {{< hl >}}datavetenskapen kan visserligen vara en mäktig bundsförvant för humaniora, men vi är inte tvungna att spela efter dess regler.{{< /hl >}}

En annan intressant sida av experimentet är att kartan visar ett *Levante* som är helt integrerat med resten av Europa och Medelhavet. Den framhäver också Edirnes centrala plats i Osmanska rikets politiska geografi. Dessutom är Spaniens viktigaste stad på kartan varken Madrid eller Escorial utan Neapel. Sist men inte minst tycks öar och små stadsstater som Ragusa ha spelat en viktig förmedlande roll mellan regionens makter.  


# Hur man hämtar data från MIA
MIA är ett utmärkt samarbetsverktyg för forskare, men de data som lagras på dess servrar är inte lättåtkomliga. Dess back-end är t.ex. inte publicerad i något öppet kodförråd. Du kan ändå få ut data genom att registrera dig hos MIA och skicka förfrågningar till servern med Python.

### Förfrågan
```python
url = "https://mia.medici.org/Mia/json/de/advancedsearch/advancedSearchResults/0/90/docYear/asc/?isNewsFeedSearch=False" 
payload = [{"searchSection":"archivalLocationSearch","type":"archivalLocationAdvancedSearch","isActiveFilter":True,"repository":None,"collection":"Mediceo del Principato","series":None,"volume":"2863","insert":None},{"searchSection":"categoryAndTypologySearch","type":"categoryAndTypologyAdvancedSearch","isActiveFilter":True,"category":"News","typology":None},{"searchSection":"transcriptionSearch","type":"transcriptionAdvancedSearch","isActiveFilter":False,"transcription":""},{"isActiveFilter":False,"searchSection":"synopsisSearch","type":"synopsisAdvancedSearch","synopsis":""},{"searchSection":"placesSearch","type":"placesAdvancedSearch","isActiveFilter":False,"places":[]},{"searchSection":"peopleSearch","type":"peopleAdvancedSearch","isActiveFilter":False,"people":[]},{"searchSection":"topicsSearch","type":"topicsAdvancedSearch","isActiveFilter":True,"topics":[{"topicTitle":"Place Index","topicId":"51","placeAllId":""}]},{"searchSection":"dateSearch","type":"dateAdvancedSearch","isActiveFilter":False,"dateFilterType":"","dateYear":"","dateMonth":"","dateDay":"","dateBYear":"","dateBMonth":"","dateBDay":""},{"searchSection":"documentOwnerSearch","type":"documentOwnerAdvancedSearch","isActiveFilter":False,"editType":"owner","account":""},{"searchSection":"languagesSearch","type":"languagesAdvancedSearch","isActiveFilter":False,"languages":[]}]
headers = {'Content-type': 'application/json', 'Accept': '*/*'}
r = requests.post(url, data=json.dumps(payload), headers=headers, auth=('LOGIN','PASSWORD'))
```
Byt ut LOGIN och PASSWORD mot dina egna inloggningsuppgifter.

### Skriv svaret till fil
```python
with open('response.json', 'wb') as fd:
    for chunk in r.iter_content(chunk_size=128):
        fd.write(chunk)
```
### Öppna JSON-filen
```python
f = open('response.json', encoding="utf8")
```
### Returnera JSON-objektet som en dictionary
```python
json_complete = json.load(f)
```
### Välj ut data ur JSON-filen och skriv ut dem i CSV-format
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

När du har laddat ner filen `results.csv` kan du städa data enligt anvisningarna ovan. 