---
title: Automatisk uppmärkning i digitala vetenskapliga utgåvor
subtitle: Kan förtränade språkmodeller ge utgivaren ett rejält produktivitetslyft?

# Summary for listings and search engines
summary: Förtränade språkmodeller kan hjälpa forskare att automatisera några av utgivningsarbetets mest enformiga och arbetskrävande moment. Med utgångspunkt i de redaktionellt granskade annotationerna i Secrets of Craft and Nature in Renaissance France undersöker jag i vilken mån en modell som GPT-3 snabbt kan tränas att märka upp tekniska handskrifter från 1500-talet.

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
- Maskininlärning
- Digitala kritiska utgåvor
- Pågående forskning

categories:
- Effektiv utgivning
---
# Inledning
Hur ger man ut digitala vetenskapliga utgåvor utan att ruinera sig? I det här inlägget, det första i en serie om effektiv utgivning, undersöker jag vilken roll förtränade språkmodeller kan spela när man vill automatisera redaktionella uppgifter som semantisk uppmärkning.

{{< toc >}}

# Problemet
## Ett kärleksverk
När det gäller kärlek räknar man inte kostnaden … så lyder åtminstone det gamla ordspråket. Det gäller i högsta grad digitala vetenskapliga utgåvor: transkription, översättning och annotation kräver tusentals arbetstimmar, som i fallet [*Secrets of Craft and Nature in Renaissance France*](https://edition640.makingandknowing.org) utförs av hundratals högt kvalificerade medarbetare.

På sätt och vis är det en välsignelse att digital humanioras flaggskeppsprojekt kan få de enorma anslag som krävs för att driva dem. Men ett så tungt beroende av rika stiftelsers, universitets och myndigheters frikostighet, och det långvariga behovet av stora personalresurser, är ingen hållbar ekonomisk modell för framtiden.

Vill vi uppmuntra forskare världen över att göra historiska dokument tillgängliga för en bredare allmänhet måste i själva verket {{< hl >}}kostnaden för digitala kritiska utgåvor sjunka med flera storleksordningar{{< /hl >}}. 

## En hög tröskel
Något paradoxalt {{< hl >}}kan lösningen komma från just sådana arbetskrävande projekt som [*Secrets of Craft and Nature in Renaissance France*](https://edition640.makingandknowing.org), eftersom de utgör ett värdefullt träningsmaterial{{< /hl >}} för att automatisera några av den digitala utgivningens mest avskräckande och repetitiva moment, uppmärkningen till exempel.

Inte för att uppmärkningen skulle vara oviktig. Tvärtom: {{< hl >}}uppmärkningen har blivit den oumbärliga beståndsdelen i varje seriöst digitalt utgivningsprojekt.{{< /hl >}} Standardiserad av [Text Encoding Initiative](https://tei-c.org) låter den oss registrera så många aspekter som möjligt av dokumentet och den text det förmedlar: struktur, marginalanteckningar, strykningar, varianter, papperskvalitet, fläckar, handstil … ja, vad du vill.

Följande exempel, hämtat ur [*Secrets of Craft and Nature in Renaissance France*](https://edition640.makingandknowing.org), visar hur uppmärkningen berikar texten med ytterligare information (kategori, struktur, semantiska fält, strykningar osv.) och därmed ger den digitala utgåvan ett rejält försprång framför sina förfäder på papper.

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

Den här informationen är värdefull inte bara för arkivändamål utan också, som jag har visat vid tidigare tillfällen, för syntes och analys. Men annotationen kan vara oerhört tidskrävande, eftersom samma text ofta måste finnas i flera skepnader: som översättning, som transkription, som moderniserad text osv. 

# Lösningen
## Transformers – den enklaste vägen till automatisering?
År 2020 släppte [OpenAI](https://www.openai.com) med buller och bång sin senaste familj av storskaliga språkmodeller för allmänt bruk, GPT-3, vilket står för ”Generative Pre-trained Transformer 3”. Transformermodeller är ett ganska nytt genombrott inom artificiell intelligens. De lär sig nya uppgifter förbluffande snabbt – det räcker att de läser en prompt och får se ett mycket begränsat antal exempel. De kan också vidareutbildas med en särskilt sammanställd datamängd (finjustering), vilket förbättrar både svarstid och träffsäkerhet. Därför säger man att GPT-3 och jämförbara transformermodeller är [few-shot learners](https://arxiv.org/abs/2005.14165), dvs. lär sig av ett fåtal exempel. 

OpenAI uppger att GPT-3 rymmer rekordmånga parametrar, 175 miljarder, och har tränats på mer än 570 GB text, till största delen engelska dokument som förmodligen hämtats från [internet](https://skylion007.github.io/OpenWebTextCorpus/). Tack vare sin blotta storlek har GPT-3 satt en ny standard på området och utför direkt ur lådan de mest skilda uppgifter med oroväckande realism. Den skriver trovärdiga [debattartiklar](https://www.theguardian.com/commentisfree/2020/sep/08/robot-wrote-this-article-gpt-3), den [pratar med människor](https://www.quickchat.ai/emerson) i chattrum, [besvarar e-post](https://www.jarvis.ai/?fpr=serpbattle), [sammanfattar texter](https://medium.com/geekculture/a-paper-summarizer-with-python-and-gpt-3-2c718bc3bc88), översätter dokument, förklarar fackjargong och så vidare.

Eftersom jag haft tidig tillgång till OpenAI:s API sedan maj 2021 har jag kunnat pröva modellens förmåga att lösa en rad uppgifter som anses svåra: att översätta fransk poesi och nylatinska texter till engelska, att förklara analogier, och till och med att förenkla fjärde boken av Kants *Grundläggning av sedernas metafysik* för en sjuåring (om än inte särskilt övertygande).

### Codex
En av GPT-3:s senaste utvecklingsgrenar är inriktad på programspråk. Modellen, som heter *Codex*, översätter naturligt språk till programkod och tvärtom. Om jag t.ex. letar efter ett reguljärt uttryck som låter mig ”hitta ord som bara börjar med stor bokstav”, översätter GPT-3 det raskt till ett fungerande reguljärt uttryck: ```[A-Z]+\w+```.

OpenAI uppger att *Codex* behärskar ett dussintal programspråk, däribland Python, JavaScript, Go, Perl, PHP, Ruby och Swift. Genom att sömlöst förvandla pseudokod till kod låter *Codex* oss koncentrera oss inte på programspråkets petiga syntax utan på de logiska steg och strategier som gör att en applikation kan lösa ett problem.

### Bortom OpenAI
OpenAI är förstås inte ensamt på plan. Som nämnts tillkännagav Pekings akademi för artificiell intelligens 2021 en ännu större och mer kapabel modell, *Wu Dao 2*. Nvidia och Microsoft slog sig samman och tog fram den träffande namngivna modellen *Megatron-Turing NLG 530B*. Mindre uppstartsföretag som [AI21 Labs](https://www.ai21.com) och [Cohere](https://cohere.ai) erbjuder också API:er för allmänheten. Värda att nämna är även initiativ med öppen källkod som [EuletherAI](https://www.eleuther.ai). AI-scenen förändras naturligtvis i rasande takt; vill du följa nya initiativ på fältet, ta en titt på [Hugging Face](https://huggingface.co/transformers/master/index.html).

# Experimenten

> [!NOTE]
> Syftet med experimenten är att hitta den billigaste vägen till tillförlitlig automatisering av redaktionella uppgifter. Man kan invända att några av dem också skulle kunna automatiseras med övervakad inlärning. Den hypotesen återkommer vi till i ett senare inlägg.

Kan en transformer som GPT-3 lära sig att annotera, säg, en teknisk och vetenskaplig handskrift från 1500-talet?

## Experiment 1 – textkategorisering
Vi börjar med något förhållandevis enkelt. Som ”few-shot learner” borde GPT-3 snabbt kunna förstå hur vår redaktion har klassificerat posterna i Ms Fr 640.

### Promptdesign
För att träna modellen använde jag en ytterst minimal prompt och valde ut fyra korta poster i ren text som exempel, bl.a. en om ”medicin”, en om ”vapen och rustningar” och en om ”måleri”. 

### Test
Sedan klistrade jag in ett annat avsnitt som inte ingick i den första sekvensen: 

```text
Working neatly
Never put down, if you can, two colors one on top of the other.   
But next, having made your design carefully, keep the place of shadows for them alone,
& also separately that of lights & highlights, without layering one color all over & then highlighting or else shading on it.  
And in this way, you further your work, economize your colors & work neatly.  
Which is the reason that, the colors not being muddled nor mixed together, they do not die & you soften the colors better, since they are not so thick.
```
Resultatet stämmer helt med innehållet: 

```xml
<categories="painting">
```

Prövar vi med en post ur en kategori som inte ens fanns med i det första urvalet av träningstexter blir resultatet överraskande. 

```xml
<categories="jewelry">
```

### Resultat
Kategorin ”jewelry” (smycken) finns inte i vår utgåva av Ms. Fr. 640. Redaktionen [föredrar](https://edition640.makingandknowing.org/#/content/resources) den bredare kategorin ”Stones” (stenar). GPT-3:s intuition är dock god och tyder på att modellen med lite mer träning kan lära sig att kategorisera vilken post som helst i Ms. Fr. 640, och kanske också i liknande tekniska texter från 1500-talet.   

## Experiment 2 – semantisk uppmärkning
Vi höjer ribban något. Om transformers som GPT-3 kan lära sig att kategorisera texter efter bestämda redaktionella kriterier, kan de då också känna igen en del av textens uppmärkning?  

> [!NOTE]
> *Secrets of Craft and Nature* använder en [kombination](https://edition640.makingandknowing.org/#/content/resources/principles) av semantiska och strukturella etiketter. Tyvärr kan GPT-3 inte bearbeta bilder, till skillnad från andra projekt som [Wu Dao 2](https://towardsdatascience.com/gpt-3-scared-you-meet-wu-dao-2-0-a-monster-of-1-75-trillion-parameters-832cd83db484). Troligen kommer framtida versioner av GPT att få den förmågan, som är nödvändig för att känna igen de flesta av ett dokuments strukturella och materiella drag. Vi hoppar över just de taggarna och koncentrerar oss på uppmärkning som inte kräver bildigenkänning.

### Promptdesign
De semantiska taggarna omfattar hänvisningar till djur, växter, ortnamn, sinnesintryck osv. I träningsprompten valde jag ut några exempel ur utgåvan:
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
Vi prövar några lätta ord med modellen `Davinci-codex`: *Apothecary*, *smoke*, *glassmakers*, *latten* och *snake*. Svaret kommer omedelbart och är felfritt:

```xml
<!--Output-->
Apothecary: <pro>Apothecary</pro>
smoke: <m>smoke<m>
glassmakers: <pro>glassmakers</pro>
latten: <m>latten</m>
snake: <al>snake</al>
```

Ett svårare prov är sammansatta uttryck som *copper plates*, *walnut oil* och *wood block*. Här vill vi se om GPT-3 klarar nästlade taggar. 

```xml
<!--Output-->
copper plates: <m>copper plates</m>
walnut oil: <m><pa>walnut</pa> oil</m>
wood block: <m>wood block</m>
```

Resultatet är dock blandat: `Davinci-codex` märkte bara upp *walnut oil* korrekt och missade de nästlade taggarna `tl` och `m` i *copper plates* och *wood block*. Som nästa test visar kan sådana fel ändå avhjälpas med en bättre träningsprompt. Efter fem ytterligare exempel på nästlade taggar levererade `Davinci-codex` ett nästan felfritt resultat med ett enda misstag (*oil paintbrushes*):

```xml
<!--Output-->
cannon powder: <m><wp>cannon</wp> powder</m>
arquebus powder: <m><wp>arquebus</wp> powder</m>
oil paintbrushes: <m><al>oil</al> paintbrushes</m>
sheep footbones: <m><al>sheep</al> footbones</m>
bronze mortar: <tl><m>bronze</m> mortar</tl>
```

# Slutsats
Det är viktigt att komma ihåg att testerna gjordes med små textfragment. Jag misstänker att GPT-3-modellerna skulle prestera ännu bättre med mer sammanhang i exemplen och i prompten. Och finjusterar man dessutom modellen med särskilt sammanställda träningsdata förbättras träffsäkerheten utan tvekan ytterligare.  
Visserligen skulle experimenten behöva upprepas i större skala för att bevisa de förtränade språkmodellernas tillförlitlighet, men vi kan ändå dra slutsatsen att {{< hl >}}den här metoden låter utgivare automatisera flera annotationsuppgifter i några få enkla steg, och därmed potentiellt spara enorma mängder tid och pengar.{{< /hl >}}