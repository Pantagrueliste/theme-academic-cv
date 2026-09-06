---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Phân tích thư mục quy mô lớn bằng mô hình ngôn ngữ tiền huấn luyện"
subtitle: "Cách chuyển nhanh hàng nghìn tài liệu tham khảo thành một cơ sở dữ liệu BibTeX"
summary: "GPT-3 giúp chuyển một khối lượng lớn thư mục thành cơ sở dữ liệu trong thời gian ngắn"
authors: [clement]
tags: [Nhân văn số, GPT-3, Thư mục, Tự động hóa]
categories: [Biên tập hiệu quả]
date: 2022-07-07T19:04:14+02:00
lastmod: 2022-07-07T19:04:14+02:00
featured: false
machine_translated: true
draft: false

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ""
  focal_point: ""
  preview_only: false

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: [Efficient Editing]
---

Tự động hóa là chìa khóa để hạ chi phí của các dự án nhân văn số. Cho đến nay, những công việc lặp đi lặp lại và tẻ nhạt của khâu biên tập trong môi trường học thuật hoặc do các học giả vốn đã quá tải gánh vác với giá đắt, hoặc được "khoán" cho sinh viên. Trong [loạt bài blog này](https://www.clementgodbarge.com/category/efficient-editing/), tôi lập luận rằng phần lớn những việc bạc bẽo ấy không những *có thể* mà còn *nên* được tự động hóa. Tự động hóa khâu biên tập làm giảm tổng chi phí của các dự án nhân văn số. Quan trọng hơn cả, nó cho phép học giả ở những vùng thu nhập thấp công bố tài liệu quý một cách nhanh chóng và vừa túi tiền.

Trong [bài trước](https://www.clementgodbarge.com/post/gpt3/), tôi đã cho thấy, chẳng hạn, mô hình ngôn ngữ tiền huấn luyện có thể đảm nhận phần lớn công việc gắn nhãn XML của một ấn bản kỹ thuật số. 

Trong bài này, tôi trình bày ví dụ thứ hai, lần này với thư mục.


## Vấn đề
Lập một cơ sở dữ liệu thư mục từ các tài liệu tham khảo được nhắc đến trong một bài báo học thuật là chuyện khá đơn giản. Ta có thể tra nhanh trên một mục lục như [worldcat](https://www.worldcat.org), tải tài liệu tham khảo về theo một định dạng nhất định, hoặc nhập tự động từ cơ sở dữ liệu cục bộ. Cách này ổn với một hai bài báo.
Nhưng quá một số lượng tài liệu tham khảo nào đó, công việc trở nên khó nhằn và ngốn thời gian. Để khắc phục, ta có thể dùng các thuật toán phân tích như [anystyle.io](https://anystyle.io). Thế nhưng những thuật toán ấy có thể khó mở rộng quy mô.
Khi tôi dùng anystyle để chuyển đổi hơn 150 tiểu luận học thuật trong [ấn bản phê bình Ms Fr 640](https://edition640.makingandknowing.org/#/) của chúng tôi, số lỗi tích tụ lại đơn giản là không thể kiểm soát nổi. Nó không nhận ra đúng nhiều nguồn của chúng tôi – chẳng hạn nhầm những nhan đề dài dằng dặc của sách đầu thời cận đại thành thứ gì khác – và cũng không nhận ra những tài liệu ít điển hình hơn, như một trang web cụ thể, một video trực tuyến, v.v. Trình phân tích chạy tốt với điều kiện tác giả tuân thủ răm rắp quy tắc của một chuẩn quen thuộc như Chicago, Turabian hay MLA. Hễ chệch khỏi chuẩn là có lỗi.

## Giải pháp
Đây là chỗ {{< hl >}}mô hình ngôn ngữ tiền huấn luyện{{< /hl >}} có thể giúp sức, bởi chúng {{< hl >}}nắm bắt rất nhanh quy luật của bất kỳ kiểu trích dẫn thư mục nào{{< /hl >}}, kể cả kiểu do chính bạn nghĩ ra, và chỉ cần vài ví dụ là chuyển đổi được đúng đắn một khối lượng lớn thư mục đã định dạng thành một [cơ sở dữ liệu BibTeX](http://www.bibtex.org/Format/). 

Đầu năm 2021, tôi may mắn được tiếp cận sớm [GPT-3 Codex](https://openai.com/blog/openai-codex/) của OpenAI. Codex là mô hình cho phép người dùng dịch ngôn ngữ tự nhiên sang mã và ngược lại. OpenAI tuyên bố nó thành thạo hơn chục ngôn ngữ lập trình; và dù API của nó, vào lúc tôi viết bài này, vẫn ở dạng beta, nó đã vận hành những ứng dụng phổ biến như [Copilot](https://github.com/features/copilot/) của GitHub.

Sau khi vọc API này một hồi, tôi nhận ra nó cũng làm việc rất tốt với thứ mã đơn giản hơn như `BibTeX`. 

Và thực tế, tôi chỉ cần dùng bốn ví dụ trong câu lệnh đầu vào là mọi thứ chạy ổn định. 

### Câu lệnh đầu vào

References:
Bayle, Ariane. “Patients exemplaires: la correspondance médicale de Fioravanti.” In *Vulgariser la médecine. Du style médical en France et en Italie*, edited by Andrea Carlino and Michel Jeanneret, 181–212. Geneva: Droz, 2009.  

Berns, Andrew D. *The Bible and Natural Philosophy in Renaissance Italy: Jewish and Christian Physicians in Search of Truth*. Cambridge: Cambridge University Press, 2015.  

Gabler, Hans Walter. “Theorizing the Digital Scholarly Edition.” *Literature Compass* 7, no. 2 (2010): 43–56. https://doi.org/10.1111/j.1741-4113.2009.00675.x.  

Findlen, Paula. *Possessing Nature: Museums, Collecting, and Scientific Culture in Early Modern Italy*. Berkeley: University of California Press, 1994.

```BibTeX
@incollection{bayle2009,
  author = {Bayle, Ariane},
  booktitle = {Vulgariser la médecine. Du style médical en France et en Italie},
  title = {Patients exemplaires: la correspondance médicale de Fioravanti},
  editor = {Carlino, Andrea and Michel Jeanneret},
  year = {2009},
  address = {Geneva},
  publisher = {Droz},
  langid = {french}
}
@book{berns2015,
  title = {The Bible and Natural Philosophy in Renaissance Italy: Jewish and Christian Physicians in Search of Truth},
  author = {Berns, Andrew D.},
  address = {Cambridge},
  publisher = {Cambridge University Press},
  langid = {english},
  date = {2015}
}
@article{gabler2010,
  author = {Gabler, Hans Walter},
  title = {Theorizing the Digital Scholarly Edition},
  journal = {Literature Compass},
  volume = {7},
  number = {2},
  pages = {43-56},
  doi = {10.1111/j.1741-4113.2009.00675.x},
  langid = {english},
  year = {2010}
}
@book{findlen1994,
  title = {Possessing Nature: Museums, Collecting, and Scientific Culture in Early Modern Italy},
  author = {Findlen, Paula},
  address = {Berkeley},
  publisher = {University of California Press},
  langid = {english},
  date = {1994}
}
```

### Kết quả
{{< hl >}}[Kết quả](https://github.com/Pantagrueliste/m-k-manuscript-data/blob/master/bibliographies/essays/EssaysBibliography.bib) thật ấn tượng: hơn 2.000 tài liệu tham khảo được chuyển đổi chỉ trong vài ngày.{{< /hl >}} Cách này không chỉ tái hiện chính xác mẫu hình trong câu lệnh đầu vào của tôi, mà còn thêm đúng những loại mục và loại trường không hề có trong câu lệnh ấy. Nói cách khác, `GPT-3` nói `BibTeX` trôi chảy như tiếng mẹ đẻ. Và có lẽ đáng ngạc nhiên hơn đối với một mô hình chủ yếu được huấn luyện bằng tiếng Anh: nó nhận ra tất cả các ngôn ngữ (Nga, Pháp, Ý, Latinh, Hy Lạp, Đức, Tây Ban Nha, v.v.) và lần nào cũng thêm đúng trường `langid`.

> [!NOTE]
> GPT-3 hiện bị giới hạn về kích thước đầu vào và đầu ra: nó chỉ xử lý được tối đa 2.048 token ngôn ngữ. Một khi giới hạn này được gỡ bỏ, cùng công việc ấy có lẽ chỉ mất một giờ hoặc ít hơn.

Khá bất ngờ, GPT-3 còn bổ sung thông tin không có trong tài liệu tham khảo gốc. 
>Baillot, Anne, and Anna Busch. “Editing for Man and Machine.” In _Users of Scholarly Editions: Editorial Anticipations of Reading, Studying and Consulting_, Vol. 13. Variants (Journal of the European Society for Textual Scholarship). Leicester, 2015. 

Với tài liệu tham khảo này chẳng hạn, GPT-3 đã thêm đường dẫn cố định tới kho truy cập mở ([HAL](https://hal.archives-ouvertes.fr)) nơi có thể đọc bài báo, kể cả các trường đặc thù `HAL_ID` và `HAL_VERSION` do kho HAL đặt ra: 
```BibTeX
@inproceedings{baillot2015, 
  title = {Editing for Man and Machine},
  author = {Baillot, Anne and Busch, Anna},
  year = 2015,
  booktitle = {Users of Scholarly Editions: Editorial Anticipations of Reading, Studying and Consulting},
  address = {Leicester},
  series = {Variants (Journal of the European Society for Textual Scholarship)},
  volume = 13,
  editor = {Bruhn, Siglinde and Schreiber, Manfred},
  langid = {english},
  hal_id = {halshs-01233380},
  hal_version = {v1}
}
```

Những bổ sung này cho thấy {{< hl >}}GPT-3 không chỉ phân tích tài liệu tham khảo, mà còn hoàn thiện nó dựa trên những gì đã học từ trước.{{< /hl >}} Về điểm này, sẽ thú vị nếu xem nó có hành xử tương tự với những tài liệu ra đời sau thời điểm huấn luyện GPT-3 hay không...

## Hạn chế
Tuy nhiên, GPT-3 không hoàn hảo. Nó cần có người giám sát. Một trong những hạn chế đã biết của nó là [bịa đặt](https://arxiv.org/abs/2005.00661) (hallucination): đôi khi nó tự sáng tác và đưa ra những phỏng đoán khó tin. 

Trong thử nghiệm của tôi, cơn lú lẫn của GPT-3 lộ rõ khi nó tự ý đổi họ một tác giả từ "Ruscelli" thành "Ruscello". Về mặt kỹ thuật, đây không hẳn là lỗi, vì họ người Ý đầu thời cận đại có thể dùng ở dạng số nhiều hay số ít không phân biệt. Nhưng quy ước ngày nay là họ ở dạng nào thì giữ nguyên dạng ấy. Ngày nay chẳng ai gọi Machiavelli là Machiavello, cũng như ta phải dùng tên Rossello chứ không phải Rosselli. GPT-3 bỏ qua quy ước này vì thiếu ý thức về niên đại chăng? Hay vì nó phỏng đoán dựa trên những họ lân cận, mà ở phần thư mục này tình cờ đều ở dạng số ít (Bariletto, Cesano, Rossello)?
Ai mà biết được.

```Bibtex
@book{rossello1565,
  title = {Della summa de’ secreti universali},
  author = {Rossello, Timoteo},
  address = {Venice},
  publisher = {Giovanni Bariletto},
  langid = {italian},
  date = {1565}
}
@book{ruscello1559, 
  title = {La seconda parte de’ secreti del Reverendo Donno Alessio Piemontese},
  author = {Ruscello, Girolamo},
  address = {Pesaro}, 
  publisher = {Bartolomeo Cesano}, 
  langid = {italian}, 
  date = {1559}
}
```

## Kết luận
Được viết ra trong bốn năm cộng tác miệt mài, hơn 150 tiểu luận [trong ấn bản kỹ thuật số của chúng tôi](https://edition640.makingandknowing.org/#/essays) không chỉ cung cấp thông tin thiết yếu về bản thảo mà chúng tôi đã biên tập và dịch, mà còn chứa những thông tin thư mục quý giá.

Gom các tài liệu tham khảo ấy vào một cơ sở dữ liệu cho phép người biên tập đổi định dạng thư mục trong nháy mắt, linh hoạt hơn trong cách trình bày thông tin theo ý mình. Cơ sở dữ liệu này còn cho biết nhiều điều về ấn bản và về dự án đã làm nên nó, mở ra những hướng phân tích mới cho giới nghiên cứu. Một cơ sở dữ liệu như thế có thể được hoàn thành với độ chính xác cao và trong thời gian kỷ lục.

Đành rằng vẫn có thể lọt vài lỗi, nhất là do thói bịa đặt của GPT-3. Song các thế hệ mô hình ngôn ngữ tiền huấn luyện sau này sẽ làm dịu bớt vấn đề ấy.
