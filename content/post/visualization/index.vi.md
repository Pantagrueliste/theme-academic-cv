---
title: Trực quan hóa đánh dấu ngữ nghĩa trong BnF Ms. Fr. 640
subtitle: Tạo nhanh các hình trực quan cho một ấn bản học thuật kỹ thuật số bằng Python  

# Summary for listings and search engines
summary: Một cách nhanh gọn để tìm tương quan trong thẻ đánh dấu của các ấn bản kỹ thuật số có chú giải như *Secrets of Craft and Nature in Renaissance France* bằng Python

# Link this post with a project
projects: ["M&K"]

# Date published
date: "2020-12-20T18:15:00Z"

# Date updated
lastmod: "2021-01-28T20:34:00Z"

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
- Nhân văn số
- Trực quan hóa dữ liệu
- BnF Ms. Fr. 640
- Nghiên cứu hiện tại

categories:
- Ghi chép
---

# Tổng quan 
Những ấn bản học thuật giàu dữ liệu chứa các chú giải biên tập quý giá mà ta có thể trích xuất, phân tích và trực quan hóa cho đủ loại mục đích nghiên cứu. Đó là trường hợp của [*Secrets of Craft and Nature in Renaissance France*](https://edition640.makingandknowing.org), ra mắt năm 2020, với tệp siêu dữ liệu có thể tải về từ kho GitHub của dự án. Trong bài này, tôi chỉ cách gom tất cả các biến ấy vào một ma trận tương quan và trực quan hóa chúng theo nhiều cách khác nhau.

# Dữ liệu
Making and Knowing Project tạo ra một bảng tính chứa thông tin cập nhật về nội dung bản thảo: ```entry_metadata.csv```. Tệp này lấy được từ [kho GitHub](https://github.com/cu-mkp/m-k-manuscript-data/blob/master/metadata/entry_metadata.csv) của Making & Knowing. Ngoài ra, ta có thể tự tạo các tệp .csv theo ý mình, với nhiều thẻ đánh dấu hơn, nhờ [manuscript-object](https://github.com/cu-mkp/manuscript-object) xuất sắc của Matthew Kumar – một phiên bản Python của BnF Ms. Fr. 640.

## Thiết lập Python 
Ta sẽ dùng Pandas để xử lý dữ liệu, Matplotlib và seaborn cho bản đồ nhiệt, và cuối cùng là NetworkX để tạo mạng lưới dựa trên tương quan.  
Với loại biến này, ta tránh phương pháp Pearson và dùng phương pháp 𝜙𝐾 thay thế. Hãy chắc rằng bạn đã [đọc về](https://phik.readthedocs.io/en/latest/index.html) phương pháp tương quan này và `PhiK`, thư viện tương ứng của nó.

```python
#install packages
pip install phik

# import modules
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import networkx as nx
```

## Chuẩn bị dữ liệu
Trước hết, tải tệp siêu dữ liệu mới nhất của ấn bản từ [kho GitHub](https://github.com/cu-mkp/m-k-manuscript-data) của họ, trong thư mục metadata.
Ta chỉ chọn những cột cần thiết. Cho phần trình diễn này, tôi chọn tất cả thẻ ngữ nghĩa của bản dịch tiếng Anh `tl`, nhưng bạn cũng có thể chọn thẻ của bản chuyển tự tiếng Pháp `tc`, hoặc bản chuẩn hóa `tcn`. 
Dữ liệu ở dạng giá trị phân cách bằng dấu chấm phẩy, và ta cần Python đếm hộ. Ta sẽ dùng phương pháp stack-unstack với biểu thức chính quy `[^;\s][^\;]*[^;\s]*`.
Để ma trận dễ đọc hơn, ta đổi tên từng cột. Nếu vội, bạn có thể bỏ qua bước này; chỉ cần nhớ rằng dataframe của ta ở giai đoạn này mang tên `tagsrn`.

```python
# load the edition's metadata
df = pd.read_csv('entry_metadata.csv')

# select the tags you want to correlate
dftags = df[['al_tl', 'bp_tl', 'cn_tl', 'df_tl', 'env_tl', 'm_tl', 'md_tl', 'ms_tl', 'mu_tl', 'pa_tl', 'pl_tl', 'pn_tl', 'pro_tl', 'sn_tl', 'tl_tl', 'tmp_tl', 'wp_tl', 'de_tl', 'el_tl', 'it_tl', 'la_tl', 'oc_tl', 'po_tl']]

# count comma separated values
tagcount = dftags.stack(dropna=False).str.count(r'[^;\s][^\;]*[^;\s]*').unstack()

# rename columns
tagsrn = tagcount.rename(columns={'al_tl': 'animals', 'bp_tl': 'body parts', 'cn_tl': 'currency', 'df_tl': 'definitions', 'env_tl': 'environment', 'm_tl': 'material', 'md_tl': 'medical', 'ms_tl': 'measurement', 'mu_tl': 'music', 'pa_tl': 'plant', 'pl_tl': 'toponym', 'pn_tl': 'person', 'pro_tl': 'profession', 'sn_tl': 'sensory', 'tl_tl': 'tool', 'tmp_tl': 'temporal', 'wp_tl': 'weapons', 'de_tl': 'German', 'el_tl': 'Greek', 'it_tl': 'Italian', 'la_tl': 'Italian', 'oc_tl': 'Occitan', 'po_tl': 'Poitevin'})
```

# Tính tương quan

Khi dataframe đã sạch, ta chuyển sang tính hệ số tương quan giữa các biến. Ở bước này, điều cốt yếu là hiểu dữ liệu của mình và chọn đúng phương pháp tương quan thích hợp nhất. Gói `pandas-profiling` đặc biệt hữu ích cho việc đó. 

```python
# calculate correlation coefficient with the phi k method
cortag = tagsrn.phik_matrix()
```
`cortag` là ma trận tương quan của ta. Giờ có thể thử nhiều kiểu trực quan hóa khác nhau.

# Trực quan hóa
Thứ đầu tiên đáng thử là hiển thị nó như một ma trận mã hóa bằng màu, dùng [mô-đun heatmap](https://seaborn.pydata.org/generated/seaborn.heatmap.html) của `seaborn`. 

### Bản đồ nhiệt tương quan
```python
f, ax = plt.subplots(figsize=(16, 14))
ax = sns.heatmap(cortag, linewidths=.03, vmin=0, cmap="Oranges", square=True)
```
![Bản đồ nhiệt tương quan của BnF Ms. Fr. 640](heatmap.png)

Nếu quen văn bản, bạn sẽ thấy ngay bản đồ nhiệt này rất có lý. Chẳng hạn, tên người tương quan mạnh với tiếng Latinh, vì thời ấy – nhất là trong giới nhân văn chủ nghĩa thế kỷ XVI – người ta có thói quen Latinh hóa tên.  

Có người sẽ bảo bản đồ nhiệt này chỉ nói lên điều hiển nhiên. Họ không hoàn toàn sai, và thoạt nhìn, các thẻ y học có vẻ là ví dụ điển hình: chúng tương quan, đúng như dự đoán, với bộ phận cơ thể, đơn vị đo lường và thực vật.

Nhưng đọc bản đồ nhiệt kỹ hơn, từng dòng một, ta có thể phát hiện những tương quan thú vị và bất ngờ. Việc các thẻ y học tương quan với từ tiếng Ý và tiếng Latinh, chẳng hạn, cho ta manh mối về nguồn gốc các bài thuốc trong Ms. Fr. 640. Tương tự, tương quan giữa nghề nghiệp, định nghĩa và đơn vị đo lường cho thấy căn tính nghề nghiệp định hình diễn ngôn kỹ thuật thế kỷ XVI đến mức nào. 

### Bản đồ cụm tương quan

Bản đồ nhiệt hữu ích trong bối cảnh "khám phá", nhưng với người xem, chúng có thể hơi rối, nhất là khi bạn đang bàn về – hay vẫn đang tìm – những cụm ngữ nghĩa cụ thể trong bản thảo. Mô-đun `clustermap` của Seaborn có thể cho kết quả đáng chú ý.

```python
clustermap = sns.clustermap(cortag, figsize=(12, 13), dendrogram_ratio=(.1, .2), vmin=0, cmap="Oranges", cbar_pos=(-.06, .12, .03, .68))
```
![Bản đồ cụm tương quan của BnF Ms. Fr. 640](clustermap.png)

Ngoài chuyện trông như một con côn trùng bị vỡ điểm ảnh (pixelated – vâng, từ này có trong OED), bản đồ cụm phân biệt rõ các thẻ đứng lẻ (phía trên và bên trái) với những thẻ liên kết chặt chẽ hơn. Ta cũng nhận ra các cụm biệt lập, như âm nhạc và tiếng Poitevin (ai mà ngờ!), so với những cụm trung tâm hơn như đo lường, vật liệu, định nghĩa và vũ khí. Nghề nghiệp liên kết nhiều hơn, nhưng ít nhất trong ma trận tương quan cụ thể này, chúng không thuộc về một cụm riêng nào.

### Mạng lưới tương quan

Nếu muốn cô đọng hơn nữa các tương quan trong ma trận, đồ thị mạng lưới là một giải pháp thanh nhã. Điều này đặc biệt đúng khi ta muốn truyền đạt về nội dung bản thảo.  
Để làm vậy, ta cần biến ma trận thành danh sách các cạnh và nút, rồi định một ngưỡng để loại các tương quan yếu khỏi đồ thị.

```python
# transform the data
links = cortag.stack().reset_index()
links.columns = ['var1', 'var2','value']

# threshold 
links_filtered = links.loc[(links['value'] > .6) & (links['var1'] != links['var2'])]
links_filtered

# create edges
G = nx.from_pandas_edgelist(links_filtered, 'var1', 'var2')

# draw network using Kamada & Kawai's algorithm 
plt.figure(3,figsize = (12,12)) 
nx.draw_kamada_kawai(G, with_labels = True, node_color = 'red', node_size = 400, edge_color = 'black', linewidths = 1, font_size = 14)
```
![Đồ thị tương quan của BnF Ms. Fr. 640](graph.png)

Nếu có quá nhiều cạnh và nút, bạn vẫn có thể đổi ngưỡng để được kết quả gọn hơn. Hoặc xuất đồ thị ra để nghịch trong `Gephi`, bằng hàm `.write_gexf()`.

```python 
nx.write_gexf(G, 'graph.gexf')
``` 
Bạn có thể xem kết quả ở đầu bài viết này.


### Cập nhật: Mạng lưới có trọng số dạng vòng

Tôi đang tìm cách hiển thị ma trận tương quan dưới dạng mạng lưới có trọng số thì gặp cách tiếp cận thú vị này [do Julian West chia sẻ](https://julian-west.github.io/blog/visualising-asset-price-correlations/#remove-edges-below-a-threshold), và tôi phỏng theo nó cho tập dữ liệu của chúng ta ở đây.

```python
# create graph weighted by correlation coefficients (unfiltered)
Gx = nx.from_pandas_edgelist(links, 'var1', 'var2', edge_attr=['value'])

# determine a threshold to remove some edges
threshold = 0.4

# list to store edges to remove
remove = []

# loop through edges in Gx and find correlations which are below the threshold
for var1, var2 in Gx.edges():
    corr = Gx[var1][var2]['value']
    #add to remove node list if abs(corr) < threshold
    if abs(corr) < threshold:
        remove.append((var1, var2))

# remove edges contained in the remove list
Gx.remove_edges_from(remove)

print(str(len(remove)) + ' edges removed')
```
Sau khi bỏ bớt vài cạnh, ta có thể định màu sắc và độ dày cho chúng.

```python
# determine the colors of edges
def assign_colour(correlation):
    if correlation <= 0.8:
        return '#ff872c'  # orange
    else:
        return '#f11d28'  # red


def assign_thickness(correlation, benchmark_thickness=3, scaling_factor=3):
    return benchmark_thickness * abs(correlation)**scaling_factor


def assign_node_size(degree, scaling_factor=50):
    return degree * scaling_factor
```

Ta cũng cho các nút một kích thước tỷ lệ với số kết nối của chúng. 

```python
# assign node size depending on number of connections (degree)
node_size = []
for key, value in dict(Gx.degree).items():
    node_size.append(assign_node_size(value))
```
Kết quả là một đồ thị có trọng số chấp nhận nhiều nút hơn và nhiều cạnh hơn hẳn, mà vẫn dễ đọc và giàu thông tin. 

![Đồ thị tương quan có trọng số của BnF Ms. Fr. 640](weightedgraph.png) 