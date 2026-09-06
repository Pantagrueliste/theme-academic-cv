---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Levanteの知覚地理"
subtitle: "16世紀のフィレンツェで、Levanteは何と結びつけられていたのか？"
summary: "Levanteはとらえどころのない地名です。通常、別の領域との関係において――あるいは対立において――定義されるからです。では、16世紀のトスカーナにとってのLevanteとは何だったのでしょうか？ MIAデータベースから集めたデータは、予想外の答えを示しています。"
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
*Levante*はとらえどころのない場所です。通常、別の領域との関係において――あるいは対立において――定義されるため、その意味が安定していたことはほとんどなく、この語が使われた場所と時代に応じて異なる地理を呼び起こしてきました。しかし、この語の客観的で正確な定義を言葉にするのが難しいとしても、所与のテキストコーパス内に存在する相関関係を基礎として、その地域の主観的な地図を描くことはなお期待できます。言い換えれば、*Levante*は特定の読者集団にとって、どのような空間を喚起しえたのでしょうか？
本稿では、Medici Archive Projectの[MIAデータベース](https://mia.medici.org/)のデータを使って、この地名が結びつけられていた具体的な場所を可視化する方法をお見せします。

# MIAデータベース
MIAデータベースは、[フィレンツェ国立文書館](https://archiviodistatofirenze.cultura.gov.it/asfi/home)の史料を自ら撮影した写真をアップロードして共有したい研究者のための協働プラットフォームです。この1年間、[全米人文科学基金](https://www.neh.gov)の支援のもと、私たちのチームはフィレンツェの*Mediceo del Principato*文書群の*avvisi*セクションに保存されている数千点の文書を撮影、転写、要約、分類してきました。私たちのデータベースは本来、統計分析を主目的としたものではありませんが、公開したメタデータはダウンロードしてデータセットとして利用することができます。

# データセット
今回私が作成したデータセットは、1543年から1566年まで、すなわち文書館に記録された最初のavvisoから、スルタン[スレイマン1世](https://en.wikipedia.org/wiki/Suleiman_the_Magnificent)が没する年までの、*Levante*発のすべてのニュースを対象としています。以下はサーバーから抽出したデータのサンプルです。3列からなるこのデータは、文書の固有番号、地名、日付で構成されています。

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

## データのクリーニング
このデータを可視化するには、csv（カンマ区切り値）データセットとして読める形にする必要があります。また、ここに含まれる地理情報を、より「機械に優しい」形式、すなわちGPS座標に変換する必要もあります。データセットには数百件の項目が含まれるため、この処理は自動化したいところです。これは、[GPT-3](https://wwww.openai.org)、[Bloom](https://huggingface.co/bigscience/bloom)、[AI-21](https://www.ai21.com)などの事前学習済み言語モデルを使えば、かなり迅速かつ正確に実現できます。ただし、事前学習済み言語モデルにはわずかにハルシネーション（幻覚）を起こす傾向があるため、この操作は綿密に監督する必要があります。


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
密度マップは、所与のデータセット内である場所が言及される頻度を強調する可視化の一種です。これは、データの地理的範囲だけでなく、その焦点を理解するうえで特に有用です。地図上のどの場所がより頻繁に言及されているのか？ どの場所がより散発的なのか？ 中心はどこにあり、周縁はどれほど遠いのか？ 読者の注意は地図上のどこに最も向けられやすいのか？

<iframe width='100%' height='600px' src="https://api.mapbox.com/styles/v1/clemclem/cl9q7c77p004y14mqytjrfnex.html?title=false&access_token=pk.eyJ1IjoiY2xlbWNsZW0iLCJhIjoiY2lmbGpvbjMwZjh3NnJ5bHg4ZzkzeWZzeCJ9.IgOF4fphVbsWAIKyzAV-DQ&zoomwheel=false#3.83/43.29/33.61" title="Levante" style="border:none;"></iframe>

この実験のために――そして急いでいたこともあり――私は[Map Box](https://www.mapbox.com)のAPIの一つを使いました。しかし、多くの可視化ライブラリや地理情報システムで、同じ種類の密度マップを作成することができます。

# いくつかの観察
結果は、明確に定義できる概念の正確な表現というよりも、印象派的な絵画に近いものです。そして、まさにそこがこの実験の気に入っているところです。実際、{{< hl >}}データサイエンスは人文学の強力な味方になりえますが、私たちが必ずしもそのルールに従う必要はないのです。{{< /hl >}}

この実験のもう一つの興味深い側面は、地図が、ヨーロッパの他の地域および地中海と完全に統合された*Levante*を明らかにしていることです。また、オスマン帝国の政治地理におけるエディルネの中心性も浮き彫りになります。さらに、地図上でスペインの最も重要な都市はマドリードでもエスコリアルでもなく、ナポリです。最後に、ラグーザのような島々や小さな都市国家が、この地域のさまざまな勢力の間を仲介する重要な役割を担っていたようです。


# MIAにデータを要求する方法
MIAは研究者にとって卓越した協働ツールですが、そのサーバーに保存されているデータには簡単にはアクセスできません。たとえば、そのバックエンドは公開リポジトリで公開されていません。それでも、MIAに登録し、Pythonを使ってサーバーにリクエストを送ることでデータを入手できます。

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
### JSONオブジェクトを辞書として返す
```python
json_complete = json.load(f)
```
### JSONからデータを選択してCSV形式で出力する
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

`results.csv`ファイルをダウンロードしたら、上で説明したようにデータのクリーニングに進むことができます。