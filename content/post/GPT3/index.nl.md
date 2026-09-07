---
title: Markup automatiseren in digitale wetenschappelijke edities
subtitle: Kunnen voorgetrainde taalmodellen de productiviteit van editeurs aanzienlijk verhogen?

# Summary for listings and search engines
summary: Voorgetrainde taalmodellen kunnen editeurs helpen om enkele van de saaiste en meest arbeidsintensieve taken van het editeren te automatiseren. Op basis van de zorgvuldig samengestelde annotaties van Secrets of Craft and Nature in Renaissance France ga ik na in hoeverre een model als GPT-3 snel kan worden getraind om technische handschriften uit de zestiende eeuw te annoteren.

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
- Digital humanities
- Machine learning
- Digitale kritische edities
- Lopend onderzoek

categories:
- Efficiënt editeren
---
# Inleiding
Hoe maak je digitale wetenschappelijke edities zonder je te ruïneren? In dit bericht, het eerste van een reeks over efficiënt editeren, ga ik na welke rol voorgetrainde taalmodellen kunnen spelen bij het automatiseren van editoriale taken zoals semantische markup.

{{< toc >}}

# Het probleem
## Een werk van liefde
Op liefde staat geen prijs... zo luidt althans het spreekwoord. Voor digitale wetenschappelijke edities gaat dat zeker op: de transcriptie, vertaling en annotatie die bij hun totstandkoming komen kijken, vergen duizenden uren werk, verricht – zoals in het geval van [*Secrets of Craft and Nature in Renaissance France*](https://edition640.makingandknowing.org) – door honderden hooggekwalificeerde medewerkers.

In zekere zin is het een zegen dat prestigieuze projecten in de digital humanities de enorme bedragen kunnen binnenhalen die ze nodig hebben om te draaien. Toch is een model dat zo zwaar leunt op de vrijgevigheid van rijke stichtingen, universiteiten en overheidsinstanties, en dat jarenlang veel menskracht vergt, economisch niet houdbaar op de lange termijn.

Sterker nog: willen we onderzoekers van over de hele wereld aanmoedigen om historische documenten voor een breder publiek toegankelijk te maken, dan {{< hl >}}moeten de kosten van digitale kritische edities met enkele ordes van grootte omlaag{{< /hl >}}. 

## Een hoge drempel
Paradoxaal genoeg {{< hl >}}komt de oplossing misschien juist van arbeidsintensieve projecten als [*Secrets of Craft and Nature in Renaissance France*](https://edition640.makingandknowing.org): ze vormen een waardevolle trainingsset{{< /hl >}} waarmee enkele van de meest afstompende en repetitieve taken van het digitaal editeren, zoals markup, kunnen worden geautomatiseerd.

Niet dat markup onbelangrijk zou zijn. Integendeel: {{< hl >}}markup is het onmisbare bestanddeel van elk serieus digitaal wetenschappelijk project geworden.{{< /hl >}} Gestandaardiseerd door het [Text Encoding Initiative](https://tei-c.org) stelt het ons in staat zoveel mogelijk aspecten van het document en van de tekst die het overlevert vast te leggen: structuur, kanttekeningen, doorhalingen, varianten, papiersoort, vlekken, handschrift... noem maar op.

Het volgende voorbeeld, ontleend aan [*Secrets of Craft and Nature in Renaissance France*](https://edition640.makingandknowing.org), laat zien hoe markup de tekst verrijkt met extra informatie (categorie, structuur, semantische velden, doorhalingen enzovoort), waardoor digitale edities uiteindelijk een flinke voorsprong nemen op hun papieren voorouders.

<table>
<tr>
<th> Plain Text </th>
<th> XML Markup</th>
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

Deze informatie is niet alleen waardevol voor archivering, maar ook – zoals ik bij eerdere gelegenheden heb laten zien – voor synthese en analyse. Dit soort annotatie kan echter buitengewoon tijdrovend zijn, omdat dezelfde tekst vaak in verschillende gedaanten beschikbaar moet zijn: als vertaling, als transcriptie, als gemoderniseerde versie enzovoort. 

# De oplossing
## Transformers: de kortste weg naar automatisering?
In 2020 bracht [OpenAI](https://www.openai.com) met veel tamtam zijn nieuwste familie van grootschalige, algemeen inzetbare taalmodellen uit: GPT-3, wat staat voor “Generative Pre-trained Transformer 3”. Transformers zijn een vrij recente doorbraak in de kunstmatige intelligentie. Ze leren nieuwe taken verbluffend snel, gewoon door een prompt te lezen en naar een zeer beperkt aantal voorbeelden te kijken. Ze kunnen ook worden bijgetraind met een dataset op maat (fine-tuning), wat de responstijd en de nauwkeurigheid verbetert. Daarom noemt men GPT-3 en vergelijkbare transformers [few-shot learners](https://arxiv.org/abs/2005.14165). 

Volgens OpenAI telt GPT-3 een recordaantal van 175 miljard parameters en is het getraind op meer dan 570 GB tekst, grotendeels Engelstalige documenten die vermoedelijk van [het internet](https://skylion007.github.io/OpenWebTextCorpus/) zijn geplukt. Door zijn enorme omvang heeft GPT-3 een nieuwe maatstaf gezet: zonder verdere voorbereiding voert het de meest uiteenlopende taken uit met een realisme dat verontrust. Het schrijft geloofwaardige [opiniestukken](https://www.theguardian.com/commentisfree/2020/sep/08/robot-wrote-this-article-gpt-3), het [praat met mensen](https://www.quickchat.ai/emerson) in chatrooms, [beantwoordt e-mails](https://www.jarvis.ai/?fpr=serpbattle), [vat teksten samen](https://medium.com/geekculture/a-paper-summarizer-with-python-and-gpt-3-2c718bc3bc88), vertaalt documenten, legt jargon uit, enzovoort.

Sinds mei 2021 heb ik vroegtijdig toegang tot de API van OpenAI, en zo heb ik kunnen uitproberen hoe het model een aantal notoir lastige taken aanpakt: Franse poëzie en Neolatijnse teksten in het Engels vertalen, analogieën uitleggen, en zelfs boek 4 van Kants *Fundering voor de metafysica van de zeden* uitleggen aan een kind van zeven (al was dat weinig overtuigend).

### Codex
Een van de jongste loten aan de GPT-3-stam richt zich op programmeertalen. Dit model, *Codex* gedoopt, vertaalt natuurlijke taal naar computertaal en omgekeerd. Zoek ik bijvoorbeeld een reguliere expressie om “alleen woorden te vinden die met een hoofdletter beginnen”, dan vertaalt GPT-3 dat meteen in een werkende reguliere expressie: ```[A-Z]+\w+```.

Volgens OpenAI kan *Codex* overweg met een dozijn programmeertalen, waaronder Python, JavaScript, Go, Perl, PHP, Ruby en Swift. Doordat het pseudocode naadloos in code omzet, hoeft men zich niet langer te bekommeren om de pietluttige syntaxis van een programmeertaal, maar kan men zich concentreren op de logische stappen en strategieën waarmee een toepassing problemen oplost.

### Voorbij OpenAI
OpenAI is natuurlijk niet de enige speler op het veld. Zoals gezegd kondigde de Beijing Academy for Artificial Intelligence in 2021 een nog groter en krachtiger model aan, *Wu Dao 2*. Nvidia en Microsoft bundelden hun krachten voor het toepasselijk genaamde *Megatron-Turing NLG 530B*. Kleinere start-ups als [AI21 Labs](https://www.ai21.com) en [Cohere](https://cohere.ai) bieden het publiek eveneens API's aan. Ook opensource-initiatieven zoals [EuletherAI](https://www.eleuther.ai) verdienen vermelding. De AI-wereld verandert uiteraard razendsnel; wie de nieuwe initiatieven in het veld wil volgen, kijkt bij [Hugging Face](https://huggingface.co/transformers/master/index.html).

# De experimenten

> [!NOTE]
> Het doel van deze experimenten is de zuinigste weg naar een betrouwbare automatisering van editoriale taken te vinden. Men kan tegenwerpen dat sommige van die taken ook met algoritmen voor supervised learning te automatiseren zijn. Die hypothese onderzoeken we in een volgend bericht.

Kan een transformer als GPT-3 leren om bijvoorbeeld een technisch en wetenschappelijk handschrift uit de zestiende eeuw te annoteren?

## Experiment 1 – Tekstcategorisering.
Laten we beginnen met iets betrekkelijk eenvoudigs. Als “few-shot learner” zou GPT-3 snel moeten doorhebben hoe onze redactie de items in Ms Fr 640 heeft ingedeeld.

### Prompt engineering
Om het te trainen gebruikte ik een zeer minimale prompt en koos ik vier korte items in platte tekst als voorbeeld, waaronder één over “geneeskunde”, één over “wapens en wapenrustingen” en één over “schilderkunst”. 

### Test
Daarna plakte ik een andere passage die niet in de oorspronkelijke reeks zat: 

```text
Working neatly
Never put down, if you can, two colors one on top of the other.   
But next, having made your design carefully, keep the place of shadows for them alone,
& also separately that of lights & highlights, without layering one color all over & then highlighting or else shading on it.  
And in this way, you further your work, economize your colors & work neatly.  
Which is the reason that, the colors not being muddled nor mixed together, they do not die & you soften the colors better, since they are not so thick.
```
De uitvoer sluit perfect aan bij de inhoud: 

```xml
<categories="painting">
```

Proberen we het met een item uit een categorie die niet eens voorkwam in de teksten waarmee GPT-3 was getraind, dan is het resultaat verrassend. 

```xml
<categories="jewelry">
```

### Resultaat
De categorie “jewelry” bestaat niet in onze editie van Ms. Fr. 640. De redactie [geeft de voorkeur](https://edition640.makingandknowing.org/#/content/resources) aan de bredere categorie “Stones”. De intuïtie van GPT-3 is echter goed en wijst erop dat het met wat extra training elk item van Ms. Fr. 640 kan leren indelen, en misschien zelfs dat van vergelijkbare technische teksten uit de zestiende eeuw.   

## Experiment 2 – Semantische markup
Leggen we de lat wat hoger. Als transformers als GPT-3 kunnen leren teksten volgens specifieke editoriale criteria in te delen, kunnen ze dan ook een deel van de markup van de tekst herkennen?  

> [!NOTE]
> *Secrets of Craft and Nature* biedt een [combinatie](https://edition640.makingandknowing.org/#/content/resources/principles) van semantische en structurele labels. Helaas verwerkt GPT-3 geen afbeeldingen, in tegenstelling tot andere projecten zoals [Wu Dao 2](https://towardsdatascience.com/gpt-3-scared-you-meet-wu-dao-2-0-a-monster-of-1-75-trillion-parameters-832cd83db484). Waarschijnlijk krijgen toekomstige versies van GPT die mogelijkheid wel; ze is nodig om de meeste structurele en materiële aspecten van een document te herkennen. Die tags slaan we hier over; we richten ons op markup waarvoor geen beeldherkenning nodig is.

### Prompt engineering
Semantische tags verwijzen onder meer naar dieren, planten, plaatsnamen, zintuiglijke waarnemingen enzovoort. Voor de trainingsprompt koos ik een paar voorbeelden uit de editie:
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
Laten we een paar makkelijke woorden proberen met het model `Davinci-codex`: *Apothecary*, *smoke*, *glassmakers*, *latten* en *snake*. De resultaten komen meteen en zijn foutloos:

```xml
<!--Output-->
Apothecary: <pro>Apothecary</pro>
smoke: <m>smoke<m>
glassmakers: <pro>glassmakers</pro>
latten: <m>latten</m>
snake: <al>snake</al>
```

Een pittiger test werkt met samengestelde woorden als *copper plates*, *walnut oil* en *wood block*. Daarmee willen we nagaan of GPT-3 geneste tags correct verwerkt. 

```xml
<!--Output-->
copper plates: <m>copper plates</m>
walnut oil: <m><pa>walnut</pa> oil</m>
wood block: <m>wood block</m>
```

De resultaten zijn echter gemengd: `Davinci-codex` labelde alleen *walnut oil* correct en zag de geneste tags `tl` en `m` in *copper plates* en *wood block* over het hoofd. Zoals de volgende test laat zien, zijn die fouten wel te ondervangen met een betere trainingsprompt. Na toevoeging van vijf extra voorbeelden van geneste tags gaf `Davinci-codex` een vrijwel foutloos resultaat terug, met één enkele misser (*oil paintbrushes*):

```xml
<!--Output-->
cannon powder: <m><wp>cannon</wp> powder</m>
arquebus powder: <m><wp>arquebus</wp> powder</m>
oil paintbrushes: <m><al>oil</al> paintbrushes</m>
sheep footbones: <m><al>sheep</al> footbones</m>
bronze mortar: <tl><m>bronze</m> mortar</tl>
```

# Conclusie
Vergeet niet dat deze tests met korte tekstfragmenten zijn uitgevoerd. Ik vermoed dat GPT-3-modellen nog betere resultaten zouden geven als de voorbeelden en de prompt meer context boden. Bovendien zou fine-tuning van het model met datasets op maat de nauwkeurigheid van de labels ongetwijfeld verder verbeteren.  
Deze experimenten moeten weliswaar nog op grotere schaal worden herhaald om de betrouwbaarheid van voorgetrainde taalmodellen aan te tonen, maar we kunnen nu al concluderen dat {{< hl >}}editeurs met deze aanpak verschillende annotatietaken in een paar eenvoudige stappen kunnen automatiseren, wat potentieel enorm veel tijd en geld bespaart.{{< /hl >}}