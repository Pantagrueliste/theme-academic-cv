---
title: Tự động hóa đánh dấu trong ấn bản học thuật kỹ thuật số
subtitle: Mô hình ngôn ngữ tiền huấn luyện có thể nâng năng suất biên tập lên đáng kể không?

# Summary for listings and search engines
summary: Mô hình ngôn ngữ tiền huấn luyện có thể giúp học giả tự động hóa một số công việc biên tập tẻ nhạt và tốn sức nhất. Dựa trên bộ chú giải đã được chọn lọc của *Secrets of Craft and Nature in Renaissance France*, tôi đánh giá xem một mô hình như GPT-3 có thể được huấn luyện nhanh chóng đến đâu để chú giải các bản thảo kỹ thuật thế kỷ XVI.

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
- Nhân văn số
- Học máy
- Ấn bản phê bình kỹ thuật số
- Nghiên cứu hiện tại

categories:
- Biên tập hiệu quả
---
# Mở đầu
Làm sao xây dựng ấn bản học thuật kỹ thuật số mà không phải dốc cạn ngân quỹ? Trong bài này, bài đầu tiên của loạt bài về biên tập hiệu quả, tôi đánh giá xem các mô hình ngôn ngữ tiền huấn luyện có thể đóng vai trò gì trong việc tự động hóa các công việc biên tập, chẳng hạn như đánh dấu ngữ nghĩa.

{{< toc >}}

# Vấn đề
## Một công trình của tình yêu
Đã yêu thì chẳng ai tính toán thiệt hơn... tục ngữ xưa bảo vậy. Với ấn bản học thuật kỹ thuật số, điều ấy càng đúng: chuyển tự, dịch thuật và chú giải trong quá trình xây dựng chúng ngốn hàng nghìn giờ lao động, và như trường hợp của [*Secrets of Craft and Nature in Renaissance France*](https://edition640.makingandknowing.org), do hàng trăm cộng tác viên trình độ cao đảm nhận.

Xét ở một mặt, việc những dự án nhân văn số có tiếng có thể huy động được khoản tiền khổng lồ cần thiết để vận hành là một điều may. Thế nhưng, dựa dẫm quá nhiều vào sự hào phóng của các quỹ giàu có, các trường đại học và cơ quan chính phủ, cộng với nhu cầu nhân lực lớn kéo dài, không phải là một mô hình kinh tế khả thi cho tương lai.

Thực vậy, nếu muốn khuyến khích học giả khắp nơi trên thế giới đưa tài liệu lịch sử đến với công chúng rộng rãi hơn, thì {{< hl >}}chi phí của ấn bản phê bình kỹ thuật số phải giảm đi nhiều bậc{{< /hl >}}. 

## Một ngưỡng cửa cao
Nghe có vẻ nghịch lý, nhưng {{< hl >}}giải pháp có thể đến từ chính những dự án tốn nhiều công sức như [*Secrets of Craft and Nature in Renaissance France*](https://edition640.makingandknowing.org), bởi chúng là một tập huấn luyện quý giá{{< /hl >}} để tự động hóa một số công việc khó nhằn và lặp đi lặp lại nhất của biên tập kỹ thuật số, chẳng hạn như đánh dấu.

Không phải đánh dấu là chuyện không đáng kể. Trái lại, {{< hl >}}đánh dấu đã trở thành thành phần không thể thiếu của bất kỳ dự án học thuật kỹ thuật số nghiêm túc nào.{{< /hl >}} Được [Text Encoding Initiative](https://tei-c.org) chuẩn hóa, nó cho phép ta ghi lại càng nhiều càng tốt các khía cạnh của tài liệu và của văn bản mà tài liệu ấy chuyển tải: cấu trúc, ghi chú bên lề, đoạn bị xóa, dị bản, loại giấy, vết ố, nét chữ... muốn gì có nấy.

Ví dụ sau đây, trích từ [*Secrets of Craft and Nature in Renaissance France*](https://edition640.makingandknowing.org), cho thấy đánh dấu làm giàu văn bản bằng thông tin bổ sung ra sao (hạng mục, cấu trúc, trường ngữ nghĩa, đoạn bị xóa, v.v.), và rốt cuộc đem lại cho ấn bản kỹ thuật số một lợi thế đáng kể so với tổ tiên bằng giấy của chúng.

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

Thông tin này không chỉ quý cho mục đích lưu trữ, mà như tôi đã chỉ ra trong những dịp trước, còn quý cho mục đích tổng hợp và phân tích. Dẫu vậy, kiểu chú giải này có thể cực kỳ tốn thời gian, vì cùng một văn bản thường phải có mặt dưới nhiều dạng khác nhau: bản dịch, bản chuyển tự, bản hiện đại hóa, v.v. 

# Giải pháp
## Transformer: con đường đơn giản nhất đến tự động hóa?
Năm 2020, [OpenAI](https://www.openai.com) rầm rộ công bố họ mô hình ngôn ngữ đa dụng quy mô lớn mới nhất của mình, gọi là GPT-3, viết tắt của "Generative Pre-trained Transformer 3". Transformer là một đột phá khá gần đây của trí tuệ nhân tạo. Chúng học nhiệm vụ mới với tốc độ ấn tượng, chỉ bằng cách đọc một câu lệnh (prompt) và xem qua một số rất ít ví dụ. Chúng cũng có thể được huấn luyện thêm bằng một tập dữ liệu chuyên biệt (tinh chỉnh – fine-tuning), qua đó cải thiện độ trễ và độ chính xác. Vì lẽ đó, người ta nói GPT-3 và các transformer tương tự là những [few-shot learner](https://arxiv.org/abs/2005.14165) – kẻ học từ vài ví dụ. 

OpenAI tuyên bố GPT-3 chứa con số kỷ lục 175 tỷ tham số, được huấn luyện trên hơn 570 GB văn bản, phần lớn là tài liệu tiếng Anh có lẽ lấy từ [internet](https://skylion007.github.io/OpenWebTextCorpus/). Nhờ kích thước khổng lồ ấy, GPT-3 đã đặt ra chuẩn mực mới trong lĩnh vực này, thực hiện ngay lập tức đủ loại nhiệm vụ với độ chân thực đáng lo ngại. Nó viết [bài bình luận](https://www.theguardian.com/commentisfree/2020/sep/08/robot-wrote-this-article-gpt-3) nghe rất có lý, [trò chuyện với người](https://www.quickchat.ai/emerson) trong phòng chat, [trả lời email](https://www.jarvis.ai/?fpr=serpbattle), [tóm tắt văn bản](https://medium.com/geekculture/a-paper-summarizer-with-python-and-gpt-3-2c718bc3bc88), dịch tài liệu, giải thích thuật ngữ chuyên môn, v.v.

Được tiếp cận sớm API của OpenAI từ tháng 5 năm 2021, tôi đã có dịp thử nghiệm khả năng của mô hình trong một số nhiệm vụ vốn được xem là khó: dịch thơ Pháp và văn bản tân Latinh sang tiếng Anh, giải thích phép loại suy, thậm chí giản lược Quyển 4 của *Groundwork for a Metaphysics of Morals* (Kant) cho một đứa trẻ bảy tuổi (dù chưa thật thuyết phục).

### Codex
Một trong những bước phát triển mới nhất của GPT-3 nhắm vào ngôn ngữ máy tính. Mang tên *Codex*, mô hình này dịch ngôn ngữ tự nhiên sang ngôn ngữ lập trình và ngược lại. Chẳng hạn, nếu tôi cần một biểu thức chính quy để "chỉ tìm những từ bắt đầu bằng chữ in hoa", GPT-3 lập tức dịch nó thành một biểu thức chính quy chạy được: ```[A-Z]+\w+```.

OpenAI tuyên bố *Codex* làm việc được với khoảng chục ngôn ngữ lập trình, trong đó có Python, JavaScript, Go, Perl, PHP, Ruby và Swift. Bằng cách chuyển mã giả thành mã thật một cách liền mạch, *Codex* cho phép người ta tập trung không phải vào cú pháp rườm rà của một ngôn ngữ lập trình, mà vào các bước logic và chiến lược giúp ứng dụng giải quyết vấn đề.

### Ngoài OpenAI
Dĩ nhiên, OpenAI không phải tay chơi duy nhất. Như đã nói, Viện Hàn lâm Trí tuệ Nhân tạo Bắc Kinh năm 2021 đã công bố một mô hình còn lớn hơn và mạnh hơn, gọi là *Wu Dao 2*. Nvidia và Microsoft bắt tay tạo ra mô hình mang cái tên rất hợp cảnh *Megatron-Turing NLG 530B*. Những công ty khởi nghiệp nhỏ hơn như [AI21 Labs](https://www.ai21.com) và [Cohere](https://cohere.ai) cũng cung cấp API cho công chúng. Đáng nhắc đến nữa là các sáng kiến mã nguồn mở như [EuletherAI](https://www.eleuther.ai). Cảnh quan AI dĩ nhiên biến chuyển rất nhanh; để theo dõi các sáng kiến mới trong lĩnh vực, hãy xem [Hugging Face](https://huggingface.co/transformers/master/index.html).

# Các thử nghiệm

> [!NOTE]
> Mục tiêu của các thử nghiệm này là tìm ra con đường tiết kiệm nhất để tự động hóa các công việc biên tập một cách đáng tin cậy. Có thể có người cho rằng một số việc trong đó cũng tự động hóa được bằng thuật toán học có giám sát. Chúng ta sẽ xem xét giả thuyết ấy trong một bài sau.

Một transformer như GPT-3 có thể học cách chú giải, chẳng hạn, một bản thảo kỹ thuật và khoa học thế kỷ XVI không?

## Thử nghiệm 1 – Phân loại văn bản.
Bắt đầu bằng thứ tương đối đơn giản. Là "kẻ học từ vài ví dụ", GPT-3 hẳn phải nhanh chóng hiểu được nhóm biên tập của chúng tôi đã phân loại các mục trong Ms Fr 640 như thế nào.

### Thiết kế câu lệnh
Để huấn luyện, tôi dùng một câu lệnh tối giản và chọn bốn mục ngắn ở dạng văn bản thuần làm ví dụ, gồm một mục về "y học", "vũ khí và áo giáp" và "hội họa". 

### Kiểm tra
Rồi tôi chép vào một đoạn khác, không nằm trong chuỗi ban đầu: 

```text
Working neatly
Never put down, if you can, two colors one on top of the other.   
But next, having made your design carefully, keep the place of shadows for them alone,
& also separately that of lights & highlights, without layering one color all over & then highlighting or else shading on it.  
And in this way, you further your work, economize your colors & work neatly.  
Which is the reason that, the colors not being muddled nor mixed together, they do not die & you soften the colors better, since they are not so thick.
```
Kết quả hoàn toàn khớp với nội dung: 

```xml
<categories="painting">
```

Nếu thử với một mục thuộc hạng mục thậm chí không có trong bộ văn bản ban đầu dùng để huấn luyện GPT-3, kết quả thật bất ngờ. 

```xml
<categories="jewelry">
```

### Kết quả
Hạng mục "jewelry" (nữ trang) không tồn tại trong ấn bản Ms. Fr. 640 của chúng tôi. Nhóm biên tập [ưu tiên](https://edition640.makingandknowing.org/#/content/resources) hạng mục rộng hơn là "Stones" (đá). Dù vậy, trực giác của GPT-3 là tốt, và cho thấy chỉ cần huấn luyện thêm chút nữa, nó có thể học cách phân loại bất kỳ mục nào của Ms. Fr. 640, thậm chí cả các văn bản kỹ thuật thế kỷ XVI tương tự.   

## Thử nghiệm 2 – Đánh dấu ngữ nghĩa
Nâng thanh xà lên cao hơn một chút. Nếu transformer như GPT-3 học được cách phân loại văn bản theo những tiêu chí biên tập cụ thể, liệu chúng có nhận diện được một phần thẻ đánh dấu của văn bản không?  

> [!NOTE]
> *Secrets of Craft and Nature* dùng [kết hợp](https://edition640.makingandknowing.org/#/content/resources/principles) nhãn ngữ nghĩa và nhãn cấu trúc. Tiếc là GPT-3 không xử lý được hình ảnh, khác với các dự án như [Wu Dao 2](https://towardsdatascience.com/gpt-3-scared-you-meet-wu-dao-2-0-a-monster-of-1-75-trillion-parameters-832cd83db484). Nhiều khả năng các phiên bản GPT sau này sẽ có năng lực đó, vốn cần thiết để nhận ra phần lớn các khía cạnh cấu trúc và vật chất của một tài liệu. Ta sẽ bỏ qua những thẻ ấy và tập trung vào loại đánh dấu không đòi hỏi nhận dạng hình ảnh.

### Thiết kế câu lệnh
Thẻ ngữ nghĩa bao gồm tham chiếu đến động vật, thực vật, địa danh, cảm giác, v.v. Trong câu lệnh huấn luyện, tôi chọn vài ví dụ từ ấn bản:
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
### Kiểm tra
Thử vài từ dễ với mô hình `Davinci-codex`, như *Apothecary*, *smoke*, *glassmakers*, *latten* và *snake*. Kết quả tức thì và không một lỗi:

```xml
<!--Output-->
Apothecary: <pro>Apothecary</pro>
smoke: <m>smoke<m>
glassmakers: <pro>glassmakers</pro>
latten: <m>latten</m>
snake: <al>snake</al>
```

Bài kiểm tra khó hơn dùng từ ghép, như *copper plates*, *walnut oil* và *wood block*. Mục đích là xem GPT-3 có xử lý đúng các thẻ lồng nhau hay không. 

```xml
<!--Output-->
copper plates: <m>copper plates</m>
walnut oil: <m><pa>walnut</pa> oil</m>
wood block: <m>wood block</m>
```

Kết quả lần này nửa được nửa không: `Davinci-codex` chỉ gắn nhãn đúng *walnut oil*, còn bỏ sót các thẻ lồng `tl` và `m` trong *copper plates* và *wood block*. Tuy nhiên, như bài kiểm tra tiếp theo dưới đây cho thấy, những lỗi này có thể giảm bớt bằng một câu lệnh huấn luyện tốt hơn. Sau khi thêm năm ví dụ nữa về thẻ lồng nhau, `Davinci-codex` trả về kết quả gần như hoàn hảo, chỉ sai một chỗ (*oil paintbrushes*):

```xml
<!--Output-->
cannon powder: <m><wp>cannon</wp> powder</m>
arquebus powder: <m><wp>arquebus</wp> powder</m>
oil paintbrushes: <m><al>oil</al> paintbrushes</m>
sheep footbones: <m><al>sheep</al> footbones</m>
bronze mortar: <tl><m>bronze</m> mortar</tl>
```

# Kết luận
Cần nhớ rằng các bài kiểm tra này được thực hiện trên những mẩu văn bản ngắn. Tôi ngờ rằng nếu cung cấp nhiều ngữ cảnh hơn trong ví dụ và trong câu lệnh, các mô hình GPT-3 sẽ cho kết quả còn tốt hơn nữa. Hơn thế, tinh chỉnh mô hình bằng những tập huấn luyện chuyên biệt chắc chắn sẽ nâng độ chính xác gắn nhãn lên thêm.  
Dẫu các thử nghiệm này còn cần được tiến hành ở quy mô lớn hơn để chứng minh độ tin cậy của mô hình ngôn ngữ tiền huấn luyện, ta vẫn có thể kết luận rằng {{< hl >}}cách tiếp cận này cho phép người biên tập tự động hóa nhiều công việc chú giải chỉ qua vài bước đơn giản, và qua đó có thể tiết kiệm rất nhiều thời gian lẫn tiền bạc.{{< /hl >}}