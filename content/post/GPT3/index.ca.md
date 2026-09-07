---
title: Automatitzar el marcatge en les edicions acadèmiques digitals
subtitle: Els models de llengua preentrenats poden augmentar significativament la productivitat editorial?

# Summary for listings and search engines
summary: Els models de llengua preentrenats poden ajudar els estudiosos a automatitzar algunes de les tasques més tedioses i laborioses de l’edició. A partir de les anotacions curades de Secrets of Craft and Nature in Renaissance France, avaluo fins a quin punt un model com GPT-3 es pot entrenar ràpidament per anotar manuscrits tècnics del segle XVI.

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
- Humanitats digitals
- Aprenentatge automàtic
- Edicions crítiques digitals
- Recerca actual

categories:
- Edició eficient
---
# Introducció
Com es poden produir edicions acadèmiques digitals sense arruïnar-se? En aquesta entrada, la primera d’una sèrie dedicada a l’edició eficient, avaluo el paper que els models de llengua preentrenats poden tenir en l’automatització de tasques editorials com ara el marcatge semàntic.

{{< toc >}}

# El problema
## Una obra d’amor
En qüestions d’amor no es miren els diners... o això diu el proverbi. I és especialment cert en el cas de les edicions acadèmiques digitals: la transcripció, la traducció i l’anotació que exigeix desenvolupar-les representen milers d’hores de feina, dutes a terme, com en el cas de [*Secrets of Craft and Nature in Renaissance France*](https://edition640.makingandknowing.org), per centenars de col·laboradors altament qualificats.

En cert sentit, que els projectes d’humanitats digitals de gran visibilitat puguin obtenir les enormes quantitats de finançament que necessiten per funcionar és una benedicció. Ara bé, dependre tant de la generositat de fundacions riques, universitats i agències governamentals, i necessitar durant tant de temps uns recursos humans tan importants, no és un model econòmic viable de cara al futur.

De fet, si volem animar els estudiosos d’arreu del món a fer accessibles els documents històrics a un públic més ampli, {{< hl >}}el cost de les edicions crítiques digitals hauria de baixar en diversos ordres de magnitud{{< /hl >}}. 

## Un llindar alt
Paradoxalment, {{< hl >}}la solució pot venir de projectes tan laboriosos com [*Secrets of Craft and Nature in Renaissance France*](https://edition640.makingandknowing.org), perquè constitueixen un valuós conjunt d’entrenament{{< /hl >}} per automatitzar algunes de les tasques més ingrates i repetitives de l’edició digital, com ara el marcatge.

No és que el marcatge no sigui important. Ben al contrari: {{< hl >}}el marcatge ha esdevingut el component indispensable de qualsevol projecte acadèmic digital seriós.{{< /hl >}} Normalitzat per la [Text Encoding Initiative](https://tei-c.org), ens permet registrar tants aspectes com sigui possible del document i del text que aquest transmet: estructura, anotacions marginals, supressions, variants, tipus de paper, taques, cal·ligrafia... El que es vulgui.

Extret de [*Secrets of Craft and Nature in Renaissance France*](https://edition640.makingandknowing.org), l’exemple següent mostra com el marcatge enriqueix el text amb informació addicional (categoria, estructura, camps semàntics, supressions, etc.) i dona així a les edicions digitals un avantatge considerable sobre els seus avantpassats materials.

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

Aquesta informació no només és valuosa amb finalitats d’arxiu, sinó també, com he mostrat en altres ocasions, amb finalitats sintètiques i analítiques. Tanmateix, aquest tipus d’anotació pot consumir moltíssim temps, perquè sovint el mateix text ha d’estar disponible en diverses variants: com a traducció, com a transcripció, com a modernització, etc. 

# La solució
## Els transformers: el camí més senzill cap a l’automatització?
El 2020, [OpenAI](https://www.openai.com) va presentar amb gran pompa la seva darrera família de grans models de llengua d’ús general, anomenada GPT-3, sigla de «Generative Pre-trained Transformer 3». Els transformers són un avenç força recent en intel·ligència artificial. Aprenen tasques noves amb una rapidesa impressionant, simplement llegint una indicació (*prompt*) i mirant un nombre molt limitat d’exemples. També poden rebre un entrenament addicional amb un conjunt de dades ad hoc (ajust fi o *fine-tuning*), cosa que en millora la latència i la precisió. Per això diem que GPT-3 i els transformers comparables són [aprenents amb pocs exemples](https://arxiv.org/abs/2005.14165) (*few-shot learners*). 

OpenAI afirma que GPT-3 conté una xifra rècord de 175.000 milions de paràmetres i que s’ha entrenat amb més de 570 GB de text, majoritàriament documents en anglès presumiblement extrets [d’internet](https://skylion007.github.io/OpenWebTextCorpus/). Per la seva mida descomunal, GPT-3 ha establert un nou estàndard en aquest camp: executa d’entrada tasques molt diverses amb un realisme inquietant. Escriu [articles d’opinió](https://www.theguardian.com/commentisfree/2020/sep/08/robot-wrote-this-article-gpt-3) plausibles, [conversa amb humans](https://www.quickchat.ai/emerson) en sales de xat, [respon correus electrònics](https://www.jarvis.ai/?fpr=serpbattle), [resumeix textos](https://medium.com/geekculture/a-paper-summarizer-with-python-and-gpt-3-2c718bc3bc88), tradueix documents, explica argot, etc.

Amb accés anticipat a l’API d’OpenAI des del maig de 2021, he pogut experimentar amb la capacitat del model per resoldre diverses tasques reputadament difícils, com ara traduir poesia francesa i textos neollatins a l’anglès, explicar analogies i fins i tot simplificar el llibre 4 de la *Fonamentació de la metafísica dels costums* de Kant per a un nen de set anys (bé que sense gaire convicció).

### Codex
Un dels darrers desenvolupaments de GPT-3 se centra en els llenguatges de programació. Anomenat *Codex*, aquest model tradueix el llenguatge natural a llenguatge de programació i viceversa. Per exemple, si busco una expressió regular que em permeti «trobar només les paraules que comencen amb majúscula», GPT-3 ho tradueix a l’instant en una expressió regular funcional: ```[A-Z]+\w+```.

OpenAI afirma que *Codex* pot treballar amb una dotzena de llenguatges de programació, entre els quals Python, JavaScript, Go, Perl, PHP, Ruby i Swift. En convertir el pseudocodi en codi sense fissures, *Codex* permet que la gent se centri no en la sintaxi fastigosa d’un llenguatge de programació, sinó en els passos lògics i les estratègies que permeten a les aplicacions resoldre problemes.

### Més enllà d’OpenAI
OpenAI, és clar, no és l’únic actor en joc. Com ja he dit, la Beijing Academy for Artificial Intelligence va anunciar el 2021 un model encara més gran i més capaç, conegut com a *Wu Dao 2*. Nvidia i Microsoft van unir forces per produir el model *Megatron-Turing NLG 530B*, de nom ben trobat. Empreses emergents més petites com [AI21 Labs](https://www.ai21.com) i [Cohere](https://cohere.ai) també ofereixen API al públic. Cal esmentar també iniciatives de codi obert com ara [EuletherAI](https://www.eleuther.ai). L’escena de la IA, és clar, evoluciona molt de pressa; per seguir les noves iniciatives del camp, val la pena consultar [Hugging Face](https://huggingface.co/transformers/master/index.html).

# Els experiments

> [!NOTE]
> L’objectiu d’aquests experiments és trobar el camí més econòmic cap a una automatització fiable de les tasques editorials. Es podria objectar que algunes també es podrien automatitzar amb algorismes d’aprenentatge supervisat. Explorarem aquesta hipòtesi en una entrada futura.

Un transformer com GPT-3 pot aprendre a anotar, per exemple, un manuscrit tècnic i científic del segle XVI?

## Experiment 1 – Categorització de textos.
Comencem per una cosa relativament senzilla. Com a «aprenent amb pocs exemples», GPT-3 hauria de poder entendre ràpidament com el nostre equip editorial ha classificat les entrades del Ms Fr 640.

### Enginyeria de la indicació
Per entrenar-lo, vaig fer servir una indicació mínima i vaig seleccionar com a exemples quatre entrades breus en text pla, entre les quals una sobre «medicina», «armes i armadures» i «pintura». 

### Prova
Després vaig copiar un altre passatge que no era a la seqüència inicial: 

```text
Working neatly
Never put down, if you can, two colors one on top of the other.   
But next, having made your design carefully, keep the place of shadows for them alone,
& also separately that of lights & highlights, without layering one color all over & then highlighting or else shading on it.  
And in this way, you further your work, economize your colors & work neatly.  
Which is the reason that, the colors not being muddled nor mixed together, they do not die & you soften the colors better, since they are not so thick.
```
El resultat és perfectament coherent amb el contingut: 

```xml
<categories="painting">
```

Si ho provem amb una entrada que pertany a una categoria que ni tan sols era inclosa en la selecció inicial de textos triats per entrenar GPT-3, el resultat és sorprenent. 

```xml
<categories="jewelry">
```

### Resultat
La categoria «jewelry» (joieria) no existeix en la nostra edició del Ms. Fr. 640. L’equip editorial [prefereix](https://edition640.makingandknowing.org/#/content/resources) la categoria més àmplia de «Stones» (pedres). La intuïció de GPT-3, però, és bona, i indica que amb una mica més d’entrenament pot aprendre a categoritzar qualsevol entrada del Ms. Fr. 640, i potser fins i tot les de textos tècnics similars del segle XVI.   

## Experiment 2 – Marcatge semàntic
Pugem una mica el llistó. Si transformers com GPT-3 poden aprendre a categoritzar textos segons criteris editorials específics, poden també identificar part del marcatge del text?  

> [!NOTE]
> *Secrets of Craft and Nature* ofereix una [combinació](https://edition640.makingandknowing.org/#/content/resources/principles) d’etiquetes semàntiques i estructurals. Malauradament, GPT-3 no processa imatges, a diferència d’altres projectes com ara [Wu Dao 2](https://towardsdatascience.com/gpt-3-scared-you-meet-wu-dao-2-0-a-monster-of-1-75-trillion-parameters-832cd83db484). És probable que les futures iteracions de GPT incorporin aquesta capacitat, necessària per reconèixer la majoria dels aspectes estructurals i materials d’un document. Deixarem de banda aquestes etiquetes concretes i ens centrarem en el marcatge que no requereix reconeixement d’imatges.

### Enginyeria de la indicació
Les etiquetes semàntiques inclouen referències a animals, plantes, topònims, percepcions sensorials, etc. Per a la indicació d’entrenament vaig seleccionar uns quants exemples de l’edició:
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
### Prova
Provem unes quantes paraules fàcils amb el model `Davinci-codex`, com ara *Apothecary*, *smoke*, *glassmakers*, *latten* i *snake*. Els resultats són immediats i impecables:

```xml
<!--Output-->
Apothecary: <pro>Apothecary</pro>
smoke: <m>smoke<m>
glassmakers: <pro>glassmakers</pro>
latten: <m>latten</m>
snake: <al>snake</al>
```

Una prova més difícil implica l’ús de paraules compostes, com ara *copper plates*, *walnut oil* i *wood block*. L’objectiu d’aquesta prova és veure si GPT-3 gestiona correctament les etiquetes imbricades. 

```xml
<!--Output-->
copper plates: <m>copper plates</m>
walnut oil: <m><pa>walnut</pa> oil</m>
wood block: <m>wood block</m>
```

Els resultats, però, són desiguals: `Davinci-codex` només ha etiquetat correctament *walnut oil*, i no ha detectat les etiquetes imbricades `tl` i `m` a *copper plates* i *wood block*. Tanmateix, com mostra la prova següent, aquests errors es poden mitigar amb una indicació d’entrenament millor. Després d’afegir-hi cinc exemples més d’etiquetes imbricades, `Davinci-codex` ha retornat un resultat gairebé impecable, amb un únic error (*oil paintbrushes*):

```xml
<!--Output-->
cannon powder: <m><wp>cannon</wp> powder</m>
arquebus powder: <m><wp>arquebus</wp> powder</m>
oil paintbrushes: <m><al>oil</al> paintbrushes</m>
sheep footbones: <m><al>sheep</al> footbones</m>
bronze mortar: <tl><m>bronze</m> mortar</tl>
```

# Conclusió
Cal recordar que aquestes proves s’han fet amb fragments de text breus. Sospito que, si es donés més context en els exemples i en la indicació, els models GPT-3 donarien resultats encara millors. A més, l’ajust fi del model amb conjunts de dades d’entrenament ad hoc milloraria sens dubte encara més la precisió de l’etiquetatge.  
Si bé aquests experiments encara s’haurien de fer a més gran escala per demostrar la fiabilitat dels models de llengua preentrenats, podem concloure tanmateix que {{< hl >}}aquest enfocament permet als editors automatitzar diverses tasques d’anotació en pocs passos senzills, amb un estalvi potencial enorme de temps i de diners.{{< /hl >}}