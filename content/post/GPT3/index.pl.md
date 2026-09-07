---
title: Automatyzacja znakowania w cyfrowych edycjach naukowych
subtitle: Czy wstępnie wytrenowane modele językowe mogą znacząco zwiększyć wydajność pracy edytorskiej?

# Summary for listings and search engines
summary: Wstępnie wytrenowane modele językowe mogą pomóc badaczom zautomatyzować niektóre z najżmudniejszych i najbardziej pracochłonnych zadań edytorskich. Na podstawie starannie opracowanych adnotacji z edycji Secrets of Craft and Nature in Renaissance France sprawdzam, w jakim stopniu model taki jak GPT-3 daje się szybko wytrenować do znakowania szesnastowiecznych rękopisów technicznych.

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
- Humanistyka cyfrowa
- Uczenie maszynowe
- Cyfrowe edycje krytyczne
- Bieżące badania

categories:
- Wydajne edytorstwo
---
# Wprowadzenie
Jak wydawać cyfrowe edycje naukowe, nie rujnując przy tym budżetu? W tym wpisie, pierwszym z cyklu poświęconego wydajnemu edytorstwu, oceniam, jaką rolę mogą odegrać wstępnie wytrenowane modele językowe w automatyzacji zadań edytorskich, takich jak znakowanie semantyczne.

{{< toc >}}

# Problem
## Dzieło z miłości
Kto kocha, ten nie liczy... tak przynajmniej głosi stare przysłowie. Do cyfrowych edycji naukowych pasuje ono szczególnie: transkrypcja, przekład i adnotacje, jakich wymaga ich opracowanie, to tysiące godzin pracy, wykonywanej – jak w przypadku [*Secrets of Craft and Nature in Renaissance France*](https://edition640.makingandknowing.org) – przez setki wysoko wykwalifikowanych współpracowników.

W pewnym sensie to błogosławieństwo, że głośne projekty humanistyki cyfrowej potrafią zdobyć ogromne fundusze niezbędne do ich prowadzenia. A jednak uzależnienie od hojności bogatych fundacji, uniwersytetów i agencji rządowych, w połączeniu z długotrwałym zapotrzebowaniem na znaczne zasoby ludzkie, nie stanowi na przyszłość realnego modelu ekonomicznego.

W gruncie rzeczy, jeśli chcemy zachęcić badaczy z całego świata do udostępniania dokumentów historycznych szerszej publiczności, {{< hl >}}koszt cyfrowych edycji krytycznych powinien spaść o rzędy wielkości{{< /hl >}}. 

## Wysoki próg
Paradoksalnie, {{< hl >}}rozwiązanie może przyjść właśnie od tak pracochłonnych projektów jak [*Secrets of Craft and Nature in Renaissance France*](https://edition640.makingandknowing.org), stanowią one bowiem cenny zbiór treningowy{{< /hl >}}, pozwalający zautomatyzować niektóre z najbardziej odstręczających i powtarzalnych zadań edytorstwa cyfrowego, takich jak znakowanie.

Nie znaczy to, że znakowanie jest nieważne. Przeciwnie: {{< hl >}}znakowanie stało się nieodzownym składnikiem każdego poważnego projektu cyfrowej edycji naukowej.{{< /hl >}} Ustandaryzowane przez [Text Encoding Initiative](https://tei-c.org), pozwala nam utrwalić możliwie wiele aspektów dokumentu i tekstu, który on przekazuje: strukturę, marginalia, skreślenia, warianty, rodzaj papieru, plamy, kaligrafię... Co tylko dusza zapragnie.

Poniższy przykład, zaczerpnięty z [*Secrets of Craft and Nature in Renaissance France*](https://edition640.makingandknowing.org), pokazuje, jak znakowanie wzbogaca tekst o dodatkowe informacje (kategoria, struktura, pola semantyczne, skreślenia itd.), dając ostatecznie edycjom cyfrowym istotną przewagę nad ich materialnymi przodkami.

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

Te informacje są cenne nie tylko z punktu widzenia archiwizacji, ale też – jak pokazywałem już przy innych okazjach – do celów syntetycznych i analitycznych. Tego typu adnotowanie bywa jednak niezwykle czasochłonne, bo ten sam tekst często musi być dostępny w kilku odmianach: jako przekład, jako transkrypcja, jako wersja zmodernizowana itd. 

# Rozwiązanie
## Transformery: najprostsza droga do automatyzacji?
W 2020 r. [OpenAI](https://www.openai.com) wypuściło z wielką pompą swoją najnowszą rodzinę wielkoskalowych modeli językowych ogólnego przeznaczenia pod nazwą GPT-3, czyli „Generative Pre-trained Transformer 3”. Transformery to dość świeży przełom w sztucznej inteligencji. Uczą się nowych zadań w imponującym tempie, po prostu czytając prompt i przyglądając się bardzo niewielkiej liczbie przykładów. Można je też dotrenować na zbiorze danych przygotowanym ad hoc (fine-tuning), co poprawia czas odpowiedzi i dokładność. Z tego powodu mówimy, że GPT-3 i porównywalne transformery to modele [uczące się na kilku przykładach](https://arxiv.org/abs/2005.14165) (few-shot learners). 

OpenAI twierdzi, że GPT-3 ma rekordowe 175 miliardów parametrów i został wytrenowany na ponad 570 GB tekstu, w większości dokumentów angielskich, zaczerpniętych zapewne z [internetu](https://skylion007.github.io/OpenWebTextCorpus/). Samą swoją skalą GPT-3 wyznaczył nowy standard w tej dziedzinie, wykonując od ręki najróżniejsze zadania z niepokojącym realizmem. Pisze wiarygodne [artykuły publicystyczne](https://www.theguardian.com/commentisfree/2020/sep/08/robot-wrote-this-article-gpt-3), [rozmawia z ludźmi](https://www.quickchat.ai/emerson) na czatach, [odpowiada na e-maile](https://www.jarvis.ai/?fpr=serpbattle), [streszcza teksty](https://medium.com/geekculture/a-paper-summarizer-with-python-and-gpt-3-2c718bc3bc88), tłumaczy dokumenty, objaśnia żargon itd.

Mając od maja 2021 r. wczesny dostęp do API OpenAI, mogłem sprawdzić, jak model radzi sobie z szeregiem zadań uchodzących za trudne: z przekładem francuskiej poezji i tekstów nowołacińskich na angielski, z objaśnianiem analogii, a nawet z uproszczeniem czwartej księgi *Uzasadnienia metafizyki moralności* Kanta dla siedmiolatka (co prawda nieprzekonująco).

### Codex
Jedno z najnowszych rozwinięć GPT-3 dotyczy języków programowania. Model ten, nazwany *Codex*, tłumaczy język naturalny na język komputerowy i odwrotnie. Jeśli na przykład szukam wyrażenia regularnego, które pozwoli mi „znaleźć tylko słowa zaczynające się wielką literą”, GPT-3 natychmiast przekłada to na działające wyrażenie regularne: ```[A-Z]+\w+```.

OpenAI twierdzi, że *Codex* obsługuje kilkanaście języków programowania, w tym Pythona, JavaScript, Go, Perla, PHP, Ruby i Swifta. Płynnie zamieniając pseudokod w kod, *Codex* pozwala skupić się nie na żmudnej składni języka, lecz na logicznych krokach i strategiach, dzięki którym aplikacje rozwiązują problemy.

### Poza OpenAI
OpenAI nie jest oczywiście jedynym graczem na rynku. Jak już wspomniałem, Pekińska Akademia Sztucznej Inteligencji ogłosiła w 2021 r. jeszcze większy i sprawniejszy model, znany jako *Wu Dao 2*. Nvidia i Microsoft połączyły siły, by stworzyć model o wymownej nazwie *Megatron-Turing NLG 530B*. Mniejsze start-upy, takie jak [AI21 Labs](https://www.ai21.com) i [Cohere](https://cohere.ai), również oferują publicznie swoje API. Warto też wspomnieć o inicjatywach open source, takich jak [EuletherAI](https://www.eleuther.ai). Scena AI zmienia się oczywiście bardzo szybko; aby śledzić nowe inicjatywy w tej dziedzinie, warto zajrzeć na [Hugging Face](https://huggingface.co/transformers/master/index.html).

# Eksperymenty

> [!NOTE]
> Celem tych eksperymentów jest znalezienie najoszczędniejszej drogi do niezawodnej automatyzacji zadań edytorskich. Można by argumentować, że niektóre z nich dałoby się zautomatyzować także algorytmami uczenia nadzorowanego. Tę hipotezę zbadamy w jednym z przyszłych wpisów.

Czy transformer taki jak GPT-3 może nauczyć się adnotować, powiedzmy, szesnastowieczny rękopis techniczno-naukowy?

## Eksperyment 1 – kategoryzacja tekstu.
Zacznijmy od czegoś stosunkowo prostego. Jako model „uczący się na kilku przykładach” GPT-3 powinien szybko pojąć, jak nasz zespół redakcyjny sklasyfikował wpisy w Ms Fr 640.

### Konstruowanie promptu
Do treningu użyłem bardzo oszczędnego promptu i wybrałem jako przykłady cztery krótkie wpisy w postaci czystego tekstu, m.in. o „medycynie”, „broni i uzbrojeniu” oraz „malarstwie”. 

### Test
Następnie wkleiłem inny fragment, którego nie było w początkowej sekwencji: 

```text
Working neatly
Never put down, if you can, two colors one on top of the other.   
But next, having made your design carefully, keep the place of shadows for them alone,
& also separately that of lights & highlights, without layering one color all over & then highlighting or else shading on it.  
And in this way, you further your work, economize your colors & work neatly.  
Which is the reason that, the colors not being muddled nor mixed together, they do not die & you soften the colors better, since they are not so thick.
```
Wynik jest w pełni zgodny z treścią: 

```xml
<categories="painting">
```

Jeśli spróbujemy z wpisem należącym do kategorii, której nie było nawet w początkowym zestawie tekstów wybranych do treningu GPT-3, wynik zaskakuje. 

```xml
<categories="jewelry">
```

### Wynik
Kategoria „jewelry” (biżuteria) nie istnieje w naszej edycji Ms. Fr. 640. Zespół redakcyjny [woli](https://edition640.makingandknowing.org/#/content/resources) szerszą kategorię „Stones” (kamienie). Intuicja GPT-3 jest jednak dobra i wskazuje, że przy odrobinie dodatkowego treningu może się on nauczyć kategoryzować każdy wpis Ms. Fr. 640, a być może nawet wpisy podobnych szesnastowiecznych tekstów technicznych.   

## Eksperyment 2 – znakowanie semantyczne
Podnieśmy nieco poprzeczkę. Skoro transformery takie jak GPT-3 potrafią nauczyć się kategoryzować teksty według określonych kryteriów edytorskich, czy potrafią też rozpoznać część znakowania tekstu?  

> [!NOTE]
> *Secrets of Craft and Nature* łączy [etykiety](https://edition640.makingandknowing.org/#/content/resources/principles) semantyczne ze strukturalnymi. Niestety GPT-3, w odróżnieniu od innych projektów, takich jak [Wu Dao 2](https://towardsdatascience.com/gpt-3-scared-you-meet-wu-dao-2-0-a-monster-of-1-75-trillion-parameters-832cd83db484), nie przetwarza obrazów. Przyszłe iteracje GPT prawdopodobnie zyskają tę zdolność, niezbędną do rozpoznawania większości strukturalnych i materialnych aspektów dokumentu. Pominiemy więc te konkretne znaczniki i skupimy się na znakowaniu, które nie wymaga rozpoznawania obrazów.

### Konstruowanie promptu
Znaczniki semantyczne obejmują odniesienia do zwierząt, roślin, toponimów, bodźców zmysłowych itd. W prompcie treningowym wybrałem kilka przykładów z edycji:
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
Wypróbujmy na modelu `Davinci-codex` kilka łatwych słów, takich jak *Apothecary*, *smoke*, *glassmakers*, *latten* i *snake*. Wyniki są natychmiastowe i bezbłędne:

```xml
<!--Output-->
Apothecary: <pro>Apothecary</pro>
smoke: <m>smoke<m>
glassmakers: <pro>glassmakers</pro>
latten: <m>latten</m>
snake: <al>snake</al>
```

Trudniejszy test wymaga użycia wyrażeń złożonych, takich jak *copper plates*, *walnut oil* i *wood block*. Chodzi o sprawdzenie, czy GPT-3 poprawnie obsługuje znaczniki zagnieżdżone. 

```xml
<!--Output-->
copper plates: <m>copper plates</m>
walnut oil: <m><pa>walnut</pa> oil</m>
wood block: <m>wood block</m>
```

Wyniki są jednak mieszane: `Davinci-codex` poprawnie oznaczył tylko *walnut oil*, nie wykrywając zagnieżdżonych znaczników `tl` i `m` w *copper plates* i *wood block*. Jak jednak pokazuje kolejny test, błędy te można ograniczyć lepszym promptem treningowym. Po dodaniu pięciu kolejnych przykładów zagnieżdżonych znaczników `Davinci-codex` zwrócił niemal bezbłędny wynik, z jedną tylko pomyłką (*oil paintbrushes*):

```xml
<!--Output-->
cannon powder: <m><wp>cannon</wp> powder</m>
arquebus powder: <m><wp>arquebus</wp> powder</m>
oil paintbrushes: <m><al>oil</al> paintbrushes</m>
sheep footbones: <m><al>sheep</al> footbones</m>
bronze mortar: <tl><m>bronze</m> mortar</tl>
```

# Wnioski
Trzeba pamiętać, że testy te przeprowadzono na krótkich fragmentach tekstu. Podejrzewam, że gdyby dostarczyć więcej kontekstu w przykładach i w prompcie, modele GPT-3 dałyby jeszcze lepsze wyniki. Co więcej, dotrenowanie modelu na zbiorach danych przygotowanych ad hoc bez wątpienia dodatkowo poprawiłoby dokładność znakowania.  
Choć eksperymenty te trzeba by jeszcze przeprowadzić na większą skalę, by wykazać niezawodność wstępnie wytrenowanych modeli językowych, możemy mimo to stwierdzić, że {{< hl >}}podejście to pozwala wydawcom zautomatyzować szereg zadań adnotacyjnych w kilku prostych krokach, oszczędzając potencjalnie ogromne ilości czasu i pieniędzy.{{< /hl >}}