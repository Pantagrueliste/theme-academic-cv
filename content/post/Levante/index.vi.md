---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Địa lý cảm nhận về vùng Levante"
subtitle: "Ở Firenze thế kỷ XVI, người ta liên tưởng Levante với những gì?"
summary: "Levante là một địa danh khó nắm bắt, bởi nó thường được định nghĩa trong tương quan – hay đối lập – với một lãnh thổ khác. Vậy Levante của người Toscana thế kỷ XVI là gì? Dữ liệu tôi thu thập từ cơ sở dữ liệu MIA đưa ra một câu trả lời bất ngờ."
authors: [clement]
tags: [MAP, Avviso]
categories: [Ghi chép]
date: 2022-10-29T10:02:52-05:00
lastmod: 2022-10-29T10:02:52-05:00
featured: true
machine_translated: true
draft: false


# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: "Bản đồ mật độ các địa danh được nhắc đến trong ASFi MdP 4277, từ 1543 đến 1566"
  focal_point: ""
  preview_only: true

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: ["MAP"]
---

# Mở đầu
*Levante* là một nơi chốn khó nắm bắt. Thường được định nghĩa trong tương quan – hay đối lập – với một lãnh thổ khác, nghĩa của nó hiếm khi ổn định, gợi lên những địa lý khác nhau tùy nơi và tùy thời người ta dùng từ ấy. Song nếu khó lòng đưa ra một định nghĩa khách quan và chính xác, ta vẫn có thể hy vọng vẽ nên một tấm bản đồ chủ quan của vùng đất này, dựa trên những tương quan tồn tại bên trong một kho ngữ liệu nhất định. Nói cách khác: với một nhóm độc giả cụ thể, *Levante* gợi lên không gian nào?  
Trong bài này, tôi sẽ chỉ cho bạn cách dùng dữ liệu từ [cơ sở dữ liệu MIA](https://mia.medici.org/) của Medici Archive Project 
để trực quan hóa những địa điểm cụ thể mà địa danh ấy gắn liền.  

# Cơ sở dữ liệu MIA
Cơ sở dữ liệu MIA là một nền tảng cộng tác dành cho những học giả muốn tải lên và chia sẻ ảnh chụp tư liệu lưu trữ của mình từ [Lưu trữ Quốc gia Florence](https://archiviodistatofirenze.cultura.gov.it/asfi/home). Trong năm qua, dưới sự bảo trợ của [National Endowment for the Humanities](https://www.neh.gov), nhóm chúng tôi đã chụp, chuyển tự, tóm tắt và phân loại hàng nghìn tài liệu thuộc phần *avvisi* của phông *Mediceo del Principato* tại Firenze. Cơ sở dữ liệu này vốn không được xây dựng cho mục đích phân tích thống kê, nhưng siêu dữ liệu chúng tôi công bố vẫn có thể tải về và dùng làm tập dữ liệu. 

# Tập dữ liệu
Trong trường hợp này, tập dữ liệu tôi tạo ra bao quát mọi tin tức từ *Levante* trong khoảng 1543–1566, tức là từ bản avviso đầu tiên được ghi nhận trong kho lưu trữ đến năm Sultan [Suleyman I](https://en.wikipedia.org/wiki/Suleiman_the_Magnificent) băng hà. Dưới đây là một mẫu dữ liệu tôi trích từ máy chủ. Dữ liệu gồm ba cột: số hiệu tài liệu duy nhất, một địa danh, và một ngày tháng. 

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

## Làm sạch dữ liệu
Để trực quan hóa, ta cần làm cho dữ liệu này đọc được dưới dạng csv (giá trị phân cách bằng dấu phẩy). Ta cũng cần chuyển thông tin địa lý ở đây sang một định dạng "thân thiện với máy" hơn: tọa độ GPS. Vì tập dữ liệu chứa hàng trăm dòng, tốt hơn là tự động hóa việc này. Có thể làm khá nhanh và khá chính xác bằng các mô hình ngôn ngữ tiền huấn luyện như [GPT-3](https://wwww.openai.org), [Bloom](https://huggingface.co/bigscience/bloom) hay [AI-21](https://www.ai21.com), chỉ kể vài cái tên. Song thao tác này cần được giám sát chặt, bởi mô hình ngôn ngữ tiền huấn luyện có đôi chút thói quen bịa chuyện.


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

# Bản đồ mật độ.
Bản đồ mật độ là kiểu trực quan hóa làm nổi bật tần suất một địa điểm được nhắc đến trong một tập dữ liệu. Nó đặc biệt hữu ích không chỉ để hiểu phạm vi địa lý của dữ liệu, mà còn để thấy các tiêu điểm của nó. Nơi nào trên bản đồ được nhắc đến nhiều hơn? Nơi nào chỉ thoáng qua? Trung tâm ở đâu, và ngoại vi xa đến đâu? Sự chú ý của người đọc nhiều khả năng dồn vào chỗ nào trên bản đồ? 

<iframe width='100%' height='600px' src="https://api.mapbox.com/styles/v1/clemclem/cl9q7c77p004y14mqytjrfnex.html?title=false&access_token=pk.eyJ1IjoiY2xlbWNsZW0iLCJhIjoiY2lmbGpvbjMwZjh3NnJ5bHg4ZzkzeWZzeCJ9.IgOF4fphVbsWAIKyzAV-DQ&zoomwheel=false#3.83/43.29/33.61" title="Levante" style="border:none;"></iframe>

Cho thử nghiệm này – và vì đang vội – tôi dùng một trong các API của [Map Box](https://www.mapbox.com). Nhưng nhiều thư viện trực quan hóa và hệ thống thông tin địa lý cũng cho phép bạn tạo ra cùng loại bản đồ mật độ này. 

# Vài nhận xét
Kết quả giống một bức tranh ấn tượng hơn là sự thể hiện chính xác của một khái niệm có thể định nghĩa rõ ràng, và đó chính là điều tôi thích ở thử nghiệm này. Thật vậy, {{< hl >}}khoa học dữ liệu có thể là đồng minh đắc lực của các ngành nhân văn, nhưng ta không nhất thiết phải tuân theo luật chơi của nó.{{< /hl >}}

Một khía cạnh thú vị khác: tấm bản đồ cho thấy một *Levante* hòa nhập hoàn toàn với phần còn lại của châu Âu và Địa Trung Hải. Nó cũng làm nổi bật vị trí trung tâm của Edirne trong địa lý chính trị của Đế quốc Ottoman. Hơn nữa, thành phố Tây Ban Nha quan trọng nhất trên bản đồ chẳng phải Madrid hay Escorial, mà là Napoli. Sau cùng nhưng không kém phần quan trọng, các đảo và những thành bang nhỏ như Ragusa dường như giữ vai trò trung gian đáng kể giữa các thế lực trong vùng.  


# Cách yêu cầu dữ liệu từ MIA
MIA là một công cụ cộng tác xuất sắc cho giới nghiên cứu, nhưng dữ liệu nó lưu trên máy chủ không dễ tiếp cận. Chẳng hạn, phần back-end của nó không được công bố trong kho công khai nào. Dù vậy, bạn vẫn có thể lấy dữ liệu bằng cách đăng ký tài khoản MIA rồi gửi yêu cầu tới máy chủ bằng Python.

### Yêu cầu
```python
url = "https://mia.medici.org/Mia/json/de/advancedsearch/advancedSearchResults/0/90/docYear/asc/?isNewsFeedSearch=False" 
payload = [{"searchSection":"archivalLocationSearch","type":"archivalLocationAdvancedSearch","isActiveFilter":True,"repository":None,"collection":"Mediceo del Principato","series":None,"volume":"2863","insert":None},{"searchSection":"categoryAndTypologySearch","type":"categoryAndTypologyAdvancedSearch","isActiveFilter":True,"category":"News","typology":None},{"searchSection":"transcriptionSearch","type":"transcriptionAdvancedSearch","isActiveFilter":False,"transcription":""},{"isActiveFilter":False,"searchSection":"synopsisSearch","type":"synopsisAdvancedSearch","synopsis":""},{"searchSection":"placesSearch","type":"placesAdvancedSearch","isActiveFilter":False,"places":[]},{"searchSection":"peopleSearch","type":"peopleAdvancedSearch","isActiveFilter":False,"people":[]},{"searchSection":"topicsSearch","type":"topicsAdvancedSearch","isActiveFilter":True,"topics":[{"topicTitle":"Place Index","topicId":"51","placeAllId":""}]},{"searchSection":"dateSearch","type":"dateAdvancedSearch","isActiveFilter":False,"dateFilterType":"","dateYear":"","dateMonth":"","dateDay":"","dateBYear":"","dateBMonth":"","dateBDay":""},{"searchSection":"documentOwnerSearch","type":"documentOwnerAdvancedSearch","isActiveFilter":False,"editType":"owner","account":""},{"searchSection":"languagesSearch","type":"languagesAdvancedSearch","isActiveFilter":False,"languages":[]}]
headers = {'Content-type': 'application/json', 'Accept': '*/*'}
r = requests.post(url, data=json.dumps(payload), headers=headers, auth=('LOGIN','PASSWORD'))
```
Nhớ thay LOGIN và PASSWORD bằng thông tin đăng nhập của bạn.

### Ghi phản hồi ra tệp
```python
with open('response.json', 'wb') as fd:
    for chunk in r.iter_content(chunk_size=128):
        fd.write(chunk)
```
### Mở JSON
```python
f = open('response.json', encoding="utf8")
```
### Trả về đối tượng JSON dưới dạng từ điển
```python
json_complete = json.load(f)
```
### Chọn dữ liệu từ JSON và in ra ở định dạng CSV
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

Sau khi tải về tệp `results.csv`, bạn có thể tiến hành làm sạch dữ liệu như đã giải thích ở trên. 