---
title: Automatisering af opmærkning i digitale videnskabelige udgaver
subtitle: Kan fortrænede sprogmodeller øge redaktørens produktivitet markant?

# Summary for listings and search engines
summary: Fortrænede sprogmodeller kan hjælpe forskere med at automatisere nogle af de mest ensformige og arbejdskrævende opgaver i udgivelsesarbejdet. Med udgangspunkt i de kuraterede annotationer i Secrets of Craft and Nature in Renaissance France undersøger jeg, i hvor høj grad en model som GPT-3 hurtigt kan trænes til at annotere tekniske håndskrifter fra 1500-tallet.

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
- Digital humaniora
- Maskinlæring
- Digitale kritiske udgaver
- Aktuel forskning

categories:
- Effektiv udgivelse
---
# Indledning
Hvordan laver man digitale videnskabelige udgaver uden at sprænge budgettet? I dette indlæg, det første i en serie om effektiv udgivelse, undersøger jeg, hvilken rolle fortrænede sprogmodeller kan spille i automatiseringen af redaktionelle opgaver som semantisk opmærkning.

{{< toc >}}

# Problemet
## Et kærlighedsarbejde
Kærlighed kender ingen regnskab … eller sådan lyder i hvert fald det gamle ord. Det gælder ikke mindst digitale videnskabelige udgaver: transskription, oversættelse og annotation løber op i tusindvis af arbejdstimer, udført – som i tilfældet [*Secrets of Craft and Nature in Renaissance France*](https://edition640.makingandknowing.org) – af hundredvis af højt kvalificerede medarbejdere.

På én måde er det en velsignelse, at de store, synlige projekter i digital humaniora kan skaffe de enorme bevillinger, der skal til for at holde dem kørende. Men en så tung afhængighed af rige fondes, universiteters og statslige styrelsers gavmildhed, kombineret med et langvarigt behov for mange hænder, er ikke nogen holdbar økonomisk model for fremtiden.

Hvis vi vil opmuntre forskere over hele verden til at gøre historiske dokumenter tilgængelige for et bredere publikum, må {{< hl >}}prisen på digitale kritiske udgaver falde med flere størrelsesordener{{< /hl >}}. 

## En høj tærskel
Paradoksalt nok {{< hl >}}kan løsningen meget vel komme fra netop de arbejdstunge projekter som [*Secrets of Craft and Nature in Renaissance France*](https://edition640.makingandknowing.org), for de udgør et værdifuldt træningssæt{{< /hl >}} til at automatisere nogle af de mest afskrækkende og monotone opgaver i digital udgivelse, opmærkningen for eksempel.

Ikke fordi opmærkning er uvæsentlig. Tværtimod: {{< hl >}}opmærkningen er blevet den uundværlige bestanddel af ethvert seriøst digitalt videnskabeligt projekt.{{< /hl >}} Standardiseret af [Text Encoding Initiative](https://tei-c.org) lader den os registrere så mange aspekter som muligt af dokumentet og den tekst, det formidler: struktur, marginalnoter, overstregninger, varianter, papirtype, pletter, håndskrift … og hvad man ellers kan komme i tanke om.

Følgende eksempel, hentet fra [*Secrets of Craft and Nature in Renaissance France*](https://edition640.makingandknowing.org), viser, hvordan opmærkningen beriger teksten med yderligere oplysninger (kategori, struktur, semantiske felter, overstregninger osv.) og dermed i sidste ende giver digitale udgaver et betydeligt forspring i forhold til deres materielle forfædre.

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

Disse oplysninger er ikke blot værdifulde til arkivformål, men også, som jeg tidligere har vist, til syntese og analyse. Alligevel kan denne form for annotation være uhyre tidkrævende, eftersom den samme tekst ofte skal foreligge i flere varianter: som oversættelse, som transskription, som moderniseret tekst osv. 

# Løsningen
## Transformere: den enkleste vej til automatisering?
I 2020 lancerede [OpenAI](https://www.openai.com) med stor ståhej sin seneste familie af store sprogmodeller til generelle formål, GPT-3, hvor forkortelsen står for “Generative Pre-trained Transformer 3”. Transformere er et ret nyt gennembrud inden for kunstig intelligens. De lærer nye opgaver imponerende hurtigt – blot ved at læse en prompt og se på et meget begrænset antal eksempler. De kan desuden efteruddannes med et særligt datasæt (finjustering), hvilket forbedrer både svartid og præcision. Derfor kalder man GPT-3 og lignende transformere for [few-shot learners](https://arxiv.org/abs/2005.14165). 

Ifølge OpenAI rummer GPT-3 rekordmange 175 milliarder parametre og er trænet på over 570 GB tekst, for størstedelens vedkommende engelsksprogede dokumenter, formodentlig hentet fra [internettet](https://skylion007.github.io/OpenWebTextCorpus/). Alene i kraft af sin størrelse har GPT-3 sat en ny standard på området og løser fra første færd vidt forskellige opgaver med en foruroligende realisme. Den skriver plausible [debatindlæg](https://www.theguardian.com/commentisfree/2020/sep/08/robot-wrote-this-article-gpt-3), [taler med mennesker](https://www.quickchat.ai/emerson) i chatrum, [besvarer e-mails](https://www.jarvis.ai/?fpr=serpbattle), [resumerer tekster](https://medium.com/geekculture/a-paper-summarizer-with-python-and-gpt-3-2c718bc3bc88), oversætter dokumenter, forklarer fagjargon osv.

Jeg har haft tidlig adgang til OpenAI's API siden maj 2021 og har kunnet afprøve modellens evne til at løse en række opgaver med ry for at være vanskelige: at oversætte fransk poesi og nylatinske tekster til engelsk, at forklare analogier og endda at forenkle fjerde bog af Kants *Grundlæggelse af sædernes metafysik* for et syvårigt barn (om end ikke overbevisende).

### Codex
En af de seneste udviklinger af GPT-3 retter sig mod programmeringssprog. Modellen, der har fået navnet *Codex*, oversætter naturligt sprog til programkode og omvendt. Leder jeg for eksempel efter et regulært udtryk, der lader mig “kun finde ord, som begynder med stort bogstav”, oversætter GPT-3 det straks til et fungerende regulært udtryk: ```[A-Z]+\w+```.

Ifølge OpenAI behersker *Codex* et dusin programmeringssprog, heriblandt Python, JavaScript, Go, Perl, PHP, Ruby og Swift. Ved gnidningsløst at omsætte pseudokode til kode lader *Codex* folk koncentrere sig ikke om programmeringssprogets pedantiske syntaks, men om de logiske trin og strategier, der gør et program i stand til at løse problemer.

### Ud over OpenAI
OpenAI er naturligvis ikke ene på markedet. Som tidligere nævnt annoncerede Beijing Academy for Artificial Intelligence i 2021 en endnu større og mere kapabel model ved navn *Wu Dao 2*. Nvidia og Microsoft slog sig sammen om den rammende døbte *Megatron-Turing NLG 530B*. Mindre startups som [AI21 Labs](https://www.ai21.com) og [Cohere](https://cohere.ai) tilbyder ligeledes API'er til offentligheden. Open source-initiativer som [EuletherAI](https://www.eleuther.ai) fortjener også at blive nævnt. AI-feltet udvikler sig naturligvis lynhurtigt; vil man følge med i nye initiativer på området, kan man kigge forbi [Hugging Face](https://huggingface.co/transformers/master/index.html).

# Eksperimenterne

> [!NOTE]
> Formålet med disse eksperimenter er at finde den billigste vej til pålidelig automatisering af redaktionelle opgaver. Man kan indvende, at nogle af dem også kunne automatiseres med superviserede læringsalgoritmer. Den hypotese vender vi tilbage til i et senere indlæg.

Kan en transformer som GPT-3 lære at annotere for eksempel et teknisk og videnskabeligt håndskrift fra 1500-tallet?

## Eksperiment 1 – Tekstkategorisering.
Lad os begynde med noget forholdsvis enkelt. Som “few-shot learner” burde GPT-3 hurtigt kunne gennemskue, hvordan vores redaktion har klassificeret indførslerne i Ms Fr 640.

### Promptdesign
Til træningen brugte jeg en meget minimal prompt og udvalgte fire små indførsler i ren tekst som eksempler, blandt andet én om “medicin”, én om “våben og rustninger” og én om “maleri”. 

### Afprøvning
Derefter kopierede jeg en anden passage, som ikke indgik i den oprindelige sekvens: 

```text
Working neatly
Never put down, if you can, two colors one on top of the other.   
But next, having made your design carefully, keep the place of shadows for them alone,
& also separately that of lights & highlights, without layering one color all over & then highlighting or else shading on it.  
And in this way, you further your work, economize your colors & work neatly.  
Which is the reason that, the colors not being muddled nor mixed together, they do not die & you soften the colors better, since they are not so thick.
```
Resultatet stemmer fuldstændig overens med indholdet: 

```xml
<categories="painting">
```

Prøver vi med en indførsel fra en kategori, som slet ikke var med i det oprindelige udvalg af tekster til træningen af GPT-3, bliver resultatet overraskende. 

```xml
<categories="jewelry">
```

### Resultat
Kategorien “jewelry” (smykker) findes ikke i vores udgave af Ms. Fr. 640. Redaktionen [foretrækker](https://edition640.makingandknowing.org/#/content/resources) den bredere kategori “Stones” (sten). GPT-3's intuition er dog god og tyder på, at modellen med lidt mere træning kan lære at kategorisere enhver indførsel i Ms. Fr. 640 – og måske endda indførslerne i lignende tekniske tekster fra 1500-tallet.   

## Eksperiment 2 – Semantisk opmærkning
Lad os lægge overliggeren lidt højere. Hvis transformere som GPT-3 kan lære at kategorisere tekster efter bestemte redaktionelle kriterier, kan de så også identificere dele af tekstens opmærkning?  

> [!NOTE]
> *Secrets of Craft and Nature* bruger en [kombination](https://edition640.makingandknowing.org/#/content/resources/principles) af semantiske og strukturelle mærker. Desværre kan GPT-3 ikke behandle billeder, i modsætning til andre projekter som [Wu Dao 2](https://towardsdatascience.com/gpt-3-scared-you-meet-wu-dao-2-0-a-monster-of-1-75-trillion-parameters-832cd83db484). Kommende versioner af GPT vil sandsynligvis få den evne, som er nødvendig for at genkende de fleste strukturelle og materielle træk ved et dokument. Vi springer disse mærker over og koncentrerer os i stedet om opmærkning, der ikke kræver billedgenkendelse.

### Promptdesign
De semantiske mærker omfatter henvisninger til dyr, planter, stednavne, sanseindtryk osv. I træningsprompten udvalgte jeg nogle få eksempler fra udgaven:
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
### Afprøvning
Lad os prøve et par lette ord med modellen `Davinci-codex`: *Apothecary*, *smoke*, *glassmakers*, *latten* og *snake*. Resultaterne kommer omgående og er fejlfrie:

```xml
<!--Output-->
Apothecary: <pro>Apothecary</pro>
smoke: <m>smoke<m>
glassmakers: <pro>glassmakers</pro>
latten: <m>latten</m>
snake: <al>snake</al>
```

En sværere prøve indebærer sammensatte udtryk som *copper plates*, *walnut oil* og *wood block*. Formålet med den er at se, om GPT-3 håndterer indlejrede mærker korrekt. 

```xml
<!--Output-->
copper plates: <m>copper plates</m>
walnut oil: <m><pa>walnut</pa> oil</m>
wood block: <m>wood block</m>
```

Her er resultaterne dog blandede: `Davinci-codex` mærkede kun *walnut oil* korrekt og overså de indlejrede `tl`- og `m`-mærker i *copper plates* og *wood block*. Som næste prøve viser, kan disse fejl imidlertid afhjælpes med en bedre træningsprompt. Efter at jeg havde tilføjet fem eksempler mere på indlejrede mærker, leverede `Davinci-codex` et næsten fejlfrit resultat med en enkelt fejl (*oil paintbrushes*):

```xml
<!--Output-->
cannon powder: <m><wp>cannon</wp> powder</m>
arquebus powder: <m><wp>arquebus</wp> powder</m>
oil paintbrushes: <m><al>oil</al> paintbrushes</m>
sheep footbones: <m><al>sheep</al> footbones</m>
bronze mortar: <tl><m>bronze</m> mortar</tl>
```

# Konklusion
Man skal huske, at disse prøver blev udført på små tekstfragmenter. Jeg formoder, at GPT-3-modellerne ville give endnu bedre resultater, hvis eksemplerne og prompten rummede mere kontekst. Dertil kommer, at en finjustering af modellen med særligt tilrettelagte træningsdata uden tvivl ville forbedre præcisionen yderligere.  
Ganske vist skal disse eksperimenter gentages i større skala, før de fortrænede sprogmodellers pålidelighed er bevist, men vi kan alligevel konkludere, at {{< hl >}}denne tilgang lader redaktører automatisere flere annotationsopgaver i nogle få enkle trin – og dermed potentielt spare enorme mængder tid og penge.{{< /hl >}}