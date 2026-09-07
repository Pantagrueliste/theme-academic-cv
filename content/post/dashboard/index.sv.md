---
title: Arkivet i ett ögonkast
subtitle: Hur interaktiva datavisualiseringar underlättar arkivforskningen

# Summary for listings and search engines
summary: Webbaserade instrumentpaneler skärper överblicken i arkivet och gör det i förlängningen mer tillgängligt och forskaren mer produktiv

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
- Digital humaniora
- Datavisualisering
- Arkivforskning
- Pågående forskning

categories:
- Anteckningar
---

# Problemet
Historiska arkiv kan vara skrämmande röriga. *Mediceo del Principato* i [Statsarkivet i Florens](https://www.archiviodistato.firenze.it/asfi/home) är ett typexempel. Bara en liten del av beståndet är inventerad, och många dokument ligger utspridda över mer än 6 500 volymer utan synbar anledning. Till råga på allt får man bara beställa fram ett begränsat antal volymer (eller *filze*, buntar, som de kallas där). I normala tider är gränsen 4 *filze* per dag. Under pandemin har den sjunkit till 4 varannan vecka. I brist på detaljerade inventarier tvingar arkivets väldiga omfång forskaren att hitta på strategier för att snabbt lokalisera de dokument hen söker.

# Lösningen
Somliga litar till slumpen, andra försöker göra kvalificerade gissningar utifrån kronologi, mottagare, avsändare, arkivbeståndets ursprung, språk osv. Att *se* alla dessa variabler på en gång kan dock avslöja oväntade mönster i arkivets struktur och vässa våra gissningar. Min erfarenhet är att de metadata forskare brukar samla i ett kalkylark avsevärt skärper överblicken i arkivet, bara man ritar upp dem i diagram.

# Experimentet
Min nuvarande forskning gäller korrespondensen från en spion på 1500-talet. Hans brev är utspridda över hundratals *filze*. De är skrivna under olika identiteter, till olika och ibland oväntade adressater, från olika platser osv. För att hitta de *filze* som med störst sannolikhet innehåller de brev jag väntar mig har jag byggt en instrumentpanel, en interaktiv webbapplikation för datavisualisering ([Plotly Dash](https://plotly.com/dash/)) som kopplar samman alla slags data, däribland geografisk och kronologisk information, med ett hierarkiskt diagram ([sunburst](https://datavizproject.com/data-type/sunburst-diagram/)) över arkivbeståndet. Panelen visar mig i ett ögonkast vad som redan hittats och hur mycket det motsvarar, och ger mig en ungefärlig bild av var jag skulle kunna leta efter nya brev. Klickar jag dessutom på enskilda variabler uppdateras alla diagram och visar specifika samband.

# Nästa steg
Kanske viktigare är att panelen kan återanvändas som ett visuellt register. När den kritiska utgåvan av breven publiceras på nätet kommer panelen att fungera som en alternativ ingång, där läsarna kan bläddra i materialet. Av sekretesskäl kan jag för närvarande bara visa en maskad skärmbild, men den fullständiga panelen släpper jag nästa år. Under tiden kommer en prototyp snart att finnas tillgänglig. Håll utkik!
