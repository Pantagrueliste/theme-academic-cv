---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "レヴァンテの知覚地理"
subtitle: "16世紀のフィレンツェで、レヴァンテは何を連想させたのか？"
summary: "レヴァンテはつかみどころのない地名です。たいていは別の領域との関係で――あるいは対立で――定義されるからです。では、16世紀のトスカーナにとってのレヴァンテとは何だったのか。MIAデータベースから集めたデータは、思いがけない答えを返してきました。"
authors: [clement]
tags: [MAP, Avviso]
categories: [ノート]
date: 2022-10-29T10:02:52-05:00
lastmod: 2022-10-29T10:02:52-05:00
featured: true
machine_translated: true
draft: false


# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: "1543年から1566年までにASFi MdP 4277で言及された地名の密度マップ"
  focal_point: ""
  preview_only: true

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: ["MAP"]
---

# はじめに
*Levante*はつかみどころのない場所です。たいていは別の領域との関係で――あるいは対立で――定義されるため、その意味が安定していたためしはなく、語が使われた場所と時代に応じて、呼び起こす地理も変わってきました。とはいえ、客観的で正確な定義を言葉にしにくいからといって、あきらめる必要はありません。あるテキストのコーパスの内部に見られる相関を手がかりに、この地域の主観的な地図を描くことなら望めるはずです。言い換えれば、特定の読者集団にとって、*Levante*はどのような空間を呼び起こしえたのか。
本稿では、Medici Archive Projectの[MIAデータベース](https://mia.medici.org/)のデータを使って、この地名が結びついていた具体的な場所を可視化する手順をお見せします。

# MIAデータベース
MIAデータベースは、[フィレンツェ国立文書館](https://archiviodistatofirenze.cultura.gov.it/asfi/home)の史料を自分で撮影した写真をアップロードし、共有したい研究者のための協働プラットフォームです。この1年、[全米人文科学基金](https://www.neh.gov)の支援を受けて、私たちのチームはフィレンツェの*Mediceo del Principato*文書群のうち*avvisi*の部に収められた数千点の文書を撮影し、転写し、要約し、分類してきました。もともと統計分析のために作ったデータベースではありませんが、公開したメタデータはダウンロードしてデータセットとして使えます。

# データセット
今回作ったデータセットは、1543年から1566年まで、つまり文書館に残る最初のavvisoから、スルタン[スレイマン1世](https://en.wikipedia.org/wiki/Suleiman_the_Magnificent)が没する年までの、*Levante*発のニュースをすべて含んでいます。以下はサーバーから抜き出したデータの一部です。3列からなり、文書の固有番号、地名、日付が並んでいます。

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

## データの整理
このデータを可視化するには、csv（カンマ区切り）のデータセットとして読める形にしなければなりません。また、ここに含まれる地理情報を、もっと「機械に優しい」形式、すなわちGPS座標に変換する必要もあります。項目は数百件ありますから、手作業ではなく自動化したいところです。[GPT-3](https://wwww.openai.org)、[Bloom](https://huggingface.co/bigscience/bloom)、[AI-21](https://www.ai21.com)といった事前学習済み言語モデルを使えば、これはかなり速く、しかもかなり正確にこなせます。ただし目を離してはいけません。事前学習済み言語モデルには、ハルシネーション（幻覚）を起こす癖が少々あるからです。


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

# 密度マップ
密度マップとは、あるデータセットの中で各地がどれくらい頻繁に言及されているかを浮かび上がらせる可視化の一種です。データの地理的な広がりだけでなく、その焦点を知るうえでとりわけ役立ちます。地図上で頻繁に言及されるのはどこか。逆に散発的にしか現れないのはどこか。中心はどこにあり、周縁はどれほど遠いのか。読者の注意は、地図のどこに集まりやすいのか。

<iframe width='100%' height='600px' src="https://api.mapbox.com/styles/v1/clemclem/cl9q7c77p004y14mqytjrfnex.html?title=false&access_token=pk.eyJ1IjoiY2xlbWNsZW0iLCJhIjoiY2lmbGpvbjMwZjh3NnJ5bHg4ZzkzeWZzeCJ9.IgOF4fphVbsWAIKyzAV-DQ&zoomwheel=false#3.83/43.29/33.61" title="Levante" style="border:none;"></iframe>

今回は実験ということで――それに急いでいたので――[Map Box](https://www.mapbox.com)のAPIを使いました。もっとも、同じ種類の密度マップは、多くの可視化ライブラリや地理情報システムでも作れます。

# いくつかの観察
できあがったものは、明確に定義できる概念の正確な表現というより、印象派の絵に近いものです。そして私がこの実験を気に入っているのは、まさにその点です。{{< hl >}}データサイエンスは人文学の強力な味方になりえますが、そのルールにいちいち従う義理はないのです。{{< /hl >}}

この実験のもう一つ面白いところは、地図に浮かび上がる*Levante*が、ヨーロッパの他の地域や地中海と完全に一体化していることです。オスマン帝国の政治地理におけるエディルネの中心性も際立ちます。さらに、地図上でスペインを代表する都市はマドリードでもエスコリアルでもなく、ナポリです。そして最後に、ラグーザのような島々や小さな都市国家が、この地域のさまざまな勢力のあいだを取り持つ重要な役割を担っていたらしいことも見て取れます。


# MIAからデータを取り出す方法
MIAは研究者にとって卓越した協働ツールですが、サーバーに蓄えられたデータに手軽にアクセスできるわけではありません。たとえばバックエンドは公開リポジトリで公開されていません。それでも、MIAに登録し、Pythonでサーバーにリクエストを送れば、データは手に入ります。

### リクエスト
```python
url = "https://mia.medici.org/Mia/json/de/advancedsearch/advancedSearchResults/0/90/docYear/asc/?isNewsFeedSearch=False" 
payload = [{"searchSection":"archivalLocationSearch","type":"archivalLocationAdvancedSearch","isActiveFilter":True,"repository":None,"collection":"Mediceo del Principato","series":None,"volume":"2863","insert":None},{"searchSection":"categoryAndTypologySearch","type":"categoryAndTypologyAdvancedSearch","isActiveFilter":True,"category":"News","typology":None},{"searchSection":"transcriptionSearch","type":"transcriptionAdvancedSearch","isActiveFilter":False,"transcription":""},{"isActiveFilter":False,"searchSection":"synopsisSearch","type":"synopsisAdvancedSearch","synopsis":""},{"searchSection":"placesSearch","type":"placesAdvancedSearch","isActiveFilter":False,"places":[]},{"searchSection":"peopleSearch","type":"peopleAdvancedSearch","isActiveFilter":False,"people":[]},{"searchSection":"topicsSearch","type":"topicsAdvancedSearch","isActiveFilter":True,"topics":[{"topicTitle":"Place Index","topicId":"51","placeAllId":""}]},{"searchSection":"dateSearch","type":"dateAdvancedSearch","isActiveFilter":False,"dateFilterType":"","dateYear":"","dateMonth":"","dateDay":"","dateBYear":"","dateBMonth":"","dateBDay":""},{"searchSection":"documentOwnerSearch","type":"documentOwnerAdvancedSearch","isActiveFilter":False,"editType":"owner","account":""},{"searchSection":"languagesSearch","type":"languagesAdvancedSearch","isActiveFilter":False,"languages":[]}]
headers = {'Content-type': 'application/json', 'Accept': '*/*'}
r = requests.post(url, data=json.dumps(payload), headers=headers, auth=('LOGIN','PASSWORD'))
```
LOGINとPASSWORDは、必ずご自身の認証情報に置き換えてください。

### レスポンスをファイルに書き出す
```python
with open('response.json', 'wb') as fd:
    for chunk in r.iter_content(chunk_size=128):
        fd.write(chunk)
```
### JSONを開く
```python
f = open('response.json', encoding="utf8")
```
### JSONオブジェクトを辞書として読み込む
```python
json_complete = json.load(f)
```
### JSONからデータを選び、CSV形式で書き出す
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

`results.csv`をダウンロードしたら、上で説明した手順でデータの整理に進めます。