---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Levantens perceptuelle geografi"
subtitle: "Hvad forbandt man Levanten med i 1500-tallets Firenze?"
summary: "Levanten er et undvigende stednavn, for det defineres som regel i forhold til – eller i modsætning til – et andet område. Hvad var så Toscanas Levante i 1500-tallet? De data, jeg har hentet fra MIA-databasen, giver et uventet svar."
authors: [clement]
tags: [MAP, Avviso]
categories: [Noter]
date: 2022-10-29T10:02:52-05:00
lastmod: 2022-10-29T10:02:52-05:00
featured: true
machine_translated: true
draft: false


# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: "Tæthedskort over stednavne nævnt i ASFi MdP 4277 fra 1543 til 1566"
  focal_point: ""
  preview_only: true

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: ["MAP"]
---

# Indledning
*Levanten* er et sted, der undslipper én. Den defineres som regel i forhold til – eller i modsætning til – et andet område, og dens betydning har sjældent ligget fast; den har fremkaldt forskellige geografier alt efter, hvor og hvornår ordet blev brugt. Men selv om en objektiv og præcis definition er svær at give, kan man stadig håbe på at tegne et subjektivt kort over egnen med udgangspunkt i de sammenhænge, der findes inden for et bestemt tekstkorpus. Med andre ord: hvilket rum kunne *Levanten* fremkalde hos en bestemt gruppe læsere?  
I dette indlæg viser jeg dig, hvordan man kan bruge data fra Medici Archive Projects [MIA-database](https://mia.medici.org/) 
til at visualisere de konkrete steder, som stednavnet blev forbundet med.  

# MIA-databasen
MIA-databasen er en samarbejdsplatform for forskere, der vil uploade og dele deres egne fotografier af arkivmateriale fra [Statsarkivet i Firenze](https://archiviodistatofirenze.cultura.gov.it/asfi/home). I løbet af det seneste år har vores hold, med støtte fra [National Endowment for the Humanities](https://www.neh.gov), fotograferet, transskriberet, resumeret og klassificeret tusindvis af dokumenter fra *avvisi*-afdelingen i arkivet *Mediceo del Principato* i Firenze. Databasen var ganske vist ikke primært tænkt til statistisk analyse, men de metadata, vi har gjort tilgængelige, kan alligevel downloades og bruges som datasæt. 

# Datasættet
I dette tilfælde dækker det datasæt, jeg har lavet, alle nyheder fra *Levanten* i årene 1543 til 1566 – det vil sige fra den første avviso i arkiverne til det år, hvor sultan [Süleyman 1.](https://en.wikipedia.org/wiki/Suleiman_the_Magnificent) dør. Her er en prøve på de data, jeg trak ud fra serveren. De består af tre kolonner: et entydigt dokumentnummer, et stednavn og en dato. 

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

## Rensning af data
For at visualisere disse data skal de kunne læses som et csv-datasæt (kommaseparerede værdier). De geografiske oplysninger skal desuden konverteres til et mere “maskinvenligt” format: GPS-koordinater. Da datasættet rummer hundredvis af poster, vil vi helst automatisere processen. Det kan gøres ret hurtigt og ganske præcist med fortrænede sprogmodeller som [GPT-3](https://wwww.openai.org), [Bloom](https://huggingface.co/bigscience/bloom) eller [AI-21](https://www.ai21.com), for blot at nævne nogle få. Operationen kræver dog tæt opsyn, for fortrænede sprogmodeller har en vis tilbøjelighed til at hallucinere.


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

# Tæthedskortet.
Et tæthedskort er en type visualisering, der fremhæver, hvor hyppigt et sted nævnes i et givet datasæt. Det er særlig nyttigt, hvis man vil forstå ikke blot sine datas geografiske udstrækning, men også deres brændpunkter. Hvilke steder på kortet nævnes oftest? Og hvilke kun sporadisk? Hvor ligger centrene, og hvor langt væk er periferien? Hvor på kortet vil en læsers opmærksomhed mest sandsynligt samle sig? 

<iframe width='100%' height='600px' src="https://api.mapbox.com/styles/v1/clemclem/cl9q7c77p004y14mqytjrfnex.html?title=false&access_token=pk.eyJ1IjoiY2xlbWNsZW0iLCJhIjoiY2lmbGpvbjMwZjh3NnJ5bHg4ZzkzeWZzeCJ9.IgOF4fphVbsWAIKyzAV-DQ&zoomwheel=false#3.83/43.29/33.61" title="Levante" style="border:none;"></iframe>

Til dette eksperiment – og fordi jeg havde travlt – brugte jeg en af [Mapbox'](https://www.mapbox.com) API'er. Men mange visualiseringsbiblioteker og geografiske informationssystemer kan lave samme slags tæthedskort. 

# Nogle iagttagelser
Resultatet er snarere et impressionistisk tableau end en præcis gengivelse af et klart afgrænseligt begreb, og det er netop det, jeg holder af ved eksperimentet. For {{< hl >}}datavidenskaben kan ganske vist være en stærk allieret for humaniora, men vi behøver ikke nødvendigvis at følge dens regler.{{< /hl >}}

Et andet interessant træk ved eksperimentet er, at kortet afslører en *Levante*, som er fuldstændig integreret med resten af Europa og Middelhavet. Det fremhæver også Edirnes centrale plads i Osmannerrigets politiske geografi. Desuden er Spaniens vigtigste by på kortet hverken Madrid eller Escorial, men Napoli. Sidst, men ikke mindst, ser øer og små bystater som Ragusa ud til at have spillet en vigtig rolle som mellemled mellem regionens forskellige magter.  


# Sådan rekvirerer man data fra MIA
MIA er et fremragende samarbejdsredskab for forskere, men de data, der ligger på dens servere, er ikke lette at få fat i. Dens backend er for eksempel ikke offentliggjort i åbne repositorier. Man kan dog stadig få fat i dataene ved at oprette sig som bruger i MIA og sende forespørgsler til serveren med Python.

### Forespørgsel
```python
url = "https://mia.medici.org/Mia/json/de/advancedsearch/advancedSearchResults/0/90/docYear/asc/?isNewsFeedSearch=False" 
payload = [{"searchSection":"archivalLocationSearch","type":"archivalLocationAdvancedSearch","isActiveFilter":True,"repository":None,"collection":"Mediceo del Principato","series":None,"volume":"2863","insert":None},{"searchSection":"categoryAndTypologySearch","type":"categoryAndTypologyAdvancedSearch","isActiveFilter":True,"category":"News","typology":None},{"searchSection":"transcriptionSearch","type":"transcriptionAdvancedSearch","isActiveFilter":False,"transcription":""},{"isActiveFilter":False,"searchSection":"synopsisSearch","type":"synopsisAdvancedSearch","synopsis":""},{"searchSection":"placesSearch","type":"placesAdvancedSearch","isActiveFilter":False,"places":[]},{"searchSection":"peopleSearch","type":"peopleAdvancedSearch","isActiveFilter":False,"people":[]},{"searchSection":"topicsSearch","type":"topicsAdvancedSearch","isActiveFilter":True,"topics":[{"topicTitle":"Place Index","topicId":"51","placeAllId":""}]},{"searchSection":"dateSearch","type":"dateAdvancedSearch","isActiveFilter":False,"dateFilterType":"","dateYear":"","dateMonth":"","dateDay":"","dateBYear":"","dateBMonth":"","dateBDay":""},{"searchSection":"documentOwnerSearch","type":"documentOwnerAdvancedSearch","isActiveFilter":False,"editType":"owner","account":""},{"searchSection":"languagesSearch","type":"languagesAdvancedSearch","isActiveFilter":False,"languages":[]}]
headers = {'Content-type': 'application/json', 'Accept': '*/*'}
r = requests.post(url, data=json.dumps(payload), headers=headers, auth=('LOGIN','PASSWORD'))
```
Husk at erstatte LOGIN og PASSWORD med dine egne loginoplysninger.

### Skriv svaret til en fil
```python
with open('response.json', 'wb') as fd:
    for chunk in r.iter_content(chunk_size=128):
        fd.write(chunk)
```
### Åbn JSON
```python
f = open('response.json', encoding="utf8")
```
### Returnér JSON-objektet som en dictionary
```python
json_complete = json.load(f)
```
### Udvælg data fra JSON og skriv dem ud i CSV-format
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

Når du har hentet filen `results.csv`, kan du gå videre med at rense data som beskrevet ovenfor. 