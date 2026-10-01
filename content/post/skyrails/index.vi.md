---
title: "Skyrails, dựng lại từ ảnh chụp màn hình"
subtitle: Khảo cổ học số, trí tuệ nhân tạo và sự lỗi thời của phần mềm

summary: >
  Skyrails, trình khám phá mạng lưới 3D đặc sắc của Yose Widjaja, đã biến mất khỏi web từ nhiều năm trước. Chỉ từ một nhúm ảnh chụp màn hình,
  Claude dựng lại nó trong một đêm. Rồi bản gốc xuất hiện trên GitHub, và chúng tôi có thể đo xem bản dựng lại đã đến gần nó tới đâu.

date: "2026-10-01T00:00:00Z"
lastmod: "2026-10-01T00:00:00Z"

draft: false
featured: true
machine_translated: true

image:
  caption: 'Các nhân vật của *Những người khốn khổ* trong Skyrails dựng lại, với Cosette ở tâm điểm'
  focal_point: "Center"
  placement: 2
  preview_only: false

authors:
- clement

tags:
- Tính bền vững
- AI
- Trực quan hóa dữ liệu

categories:
- Ghi chép
---

Khoảng năm 2007, Yose Widjaja, khi ấy là sinh viên Đại học New South Wales, đã tạo ra Skyrails, một chương trình đặc sắc để khám phá mạng lưới trong không gian ba chiều. Người dùng du hành ngay bên trong mạng lưới, từ nút này sang nút khác dọc theo những đường ray phát sáng, như thể đang ở giữa lòng dữ liệu. Vào thời mà phần lớn công cụ nghiên cứu còn phẳng lì và xám xịt, nó trông như một trò chơi điện tử. Đằng sau vẻ ngoài ấy là một chiều sâu thực sự: Skyrails có ngôn ngữ kịch bản riêng để tùy chỉnh cách hiển thị và phân tích đồ thị, cùng những menu viết bằng chính ngôn ngữ ấy, để cả người không biết lập trình vẫn dùng được. Tất cả đều do một mình một sinh viên làm nên. Nhiều năm trước, tôi đã xem một bản demo trên YouTube và chưa bao giờ quên được.


## Một chương trình biến mất

Skyrails chưa bao giờ được bảo trì. Nó chạy trên Windows, trang chủ của nó ở trường đại học đã biến mất, và mọi đường link tôi lần theo đều hỏng. Những gì còn sót lại chỉ là dấu vết: một [album ảnh chụp màn hình trên Flickr](https://www.flickr.com/photos/14933315@N05/albums/72157602730584157/), và dăm bài blog năm 2007, trên [FlowingData](https://flowingdata.com/?p=947), trên [*Deltoid*](https://scienceblogs.com/deltoid/2007/10/22/skyrails-graph-visualizations) của Tim Lambert và trên [InfoVis Wiki](https://infovis-wiki.net/wiki/2007-10-27:_Skyrails:_Social_Network_Visualisation_System).

Những ảnh chụp ấy cho biết nhiều điều đến bất ngờ. Ta thấy một bầu trời xanh đêm vằn mây, các cạnh được vẽ thành những dấu chữ V chuyển động, các nút mang hình biểu tượng hoặc biểu đồ tròn, và một menu hình tròn xòe ra quanh nút khi ta giữ chuột phải. Ta thấy tên các script điều khiển từng bản trình diễn (`labs.van`, `macaque.van`, `worldtrade.van`), những menu mà các script ấy tạo ra, và bốn chủ đề giao diện mang tên *normal*, *desert*, *valley* và *openspace*. Một tấm thậm chí còn giữ lại được đúng một dòng của ngôn ngữ kịch bản, gõ vào cửa sổ lệnh ở đầu màn hình:

```
with all nodes do nodeplane x 1 -1 end
```


## Dựng lại từ chứng cứ

Từ những chứng cứ ấy, Claude dựng lại Skyrails chỉ trong một đêm. Phiên bản mới chạy trong trình duyệt web với [Three.js](https://threejs.org/) và, về nguyên tắc, cũng phải chạy được trên kính thực tế ảo. Nó sao lại bầu trời, những đường ray hình chữ V, các nút phát sáng cùng biểu tượng, biểu đồ tròn và các vành của chúng, nhãn lớn của nút nằm dưới con trỏ, menu hình tròn và bốn chủ đề giao diện. Nó cũng có một ngôn ngữ kịch bản nho nhỏ, xây dựng quanh dòng lệnh duy nhất mà ảnh chụp còn giữ lại, để các câu lệnh `with … do … end` định kiểu cho đồ thị và khai báo menu.

Để thử nghiệm, tôi nạp vào ba bộ dữ liệu kinh điển: mạng lưới các gia tộc Firenze của John Padgett, với những mối quan hệ hôn nhân và làm ăn giữa họ; câu lạc bộ karate của Wayne Zachary; và mạng lưới nhân vật *Những người khốn khổ* của Donald Knuth, trong đó hai nhân vật được nối với nhau khi cùng xuất hiện trong một chương. Đoạn video dưới đây du hành qua mạng lưới cuối cùng này, từ Valjean đến Javert, Fantine, Cosette và Marius. Máy quay men theo đường ray nào, đường ray ấy bừng sáng.

<video controls playsinline preload="metadata" poster="/post/skyrails/poster.jpg" style="width:100%; height:auto; border-radius:4px;">
  <source src="/post/skyrails/skyrails-les-miserables.mp4" type="video/mp4">
  Trình duyệt của bạn không phát được video này. Thay vào đó, bạn có thể <a href="/post/skyrails/skyrails-les-miserables.mp4">tải video về</a>.
</video>

Kết quả giống các ảnh chụp đến mức tôi lập tức ngờ rằng mô hình đã hấp thụ dấu vết của mã gốc trong quá trình huấn luyện.


## Bản gốc lộ diện

Rồi câu chuyện bất ngờ rẽ hướng. Dựng lại xong, tôi tìm thấy chương trình gốc trên GitHub. Năm 2015, được Yose Widjaja cho phép, một nhà nghiên cứu đã chia sẻ nó cùng với mã của một bài thuyết trình về trực quan hóa dữ liệu tại hội nghị bảo mật ShmooCon ([RITHoneynet/DataVisualization](https://github.com/RITHoneynet/DataVisualization), cũng được sao lại trong [Light0617/3D_UIUX](https://github.com/Light0617/3D_UIUX/tree/master/skyrails/skyrailsdist)). Kho này chứa các tệp thực thi cho Windows, dữ liệu, shader và các script gốc, nhưng không có mã nguồn của engine chính.

Vậy là có thể so sánh hai bên. Bản dựng lại đến gần với diện mạo và cảm giác sử dụng của bản gốc, nhưng ngôn ngữ kịch bản và shader của nó thì rất khác. Script gốc trông như thế này:

```
with all edges do (
   if(#marriage == 1) then (
      linkorigin <- marriage -> linktarget;
   ) end;
) end;
```

Chúng định nghĩa chương trình con bằng `sub`, menu bằng `menudef` và `menulink`, màu sắc bằng `rgb: 130 0 0`, và kiểu liên kết bằng các mũi tên. Bản dựng lại không có thứ nào trong số đó; điểm chung duy nhất là dạng `with … do … end` nhìn thấy trong ảnh chụp. Các shader gốc, với những cái tên như `BloomFX` và `RetinalBurnFX`, cũng chẳng có gì chung với các shader mới.

Điều này chưa khép lại được câu hỏi liệu mô hình có học thuộc hay không. Các script gốc đã được công khai từ năm 2015 và rất có thể đã nằm trong dữ liệu huấn luyện của mô hình; không ai, kể cả chính mô hình, có thể nói chắc nó đã từng thấy những gì. Nhưng nếu mô hình đã học thuộc Skyrails, thì tôi cho rằng chí ít nó cũng đã tái hiện được ngôn ngữ kịch bản. Những khác biệt này gợi ý rằng Claude đã làm việc dựa trên chứng cứ trong các ảnh chụp màn hình.


## Khảo cổ học số và tính bền vững của phần mềm

Tôi xem thí nghiệm này như một dạng khảo cổ học số: dựng lại một vật đã mất từ những dấu vết nó để lại, rồi tìm ra bản gốc và đo xem mình đã đến gần tới đâu. Như mọi công trình phục dựng, Skyrails mới là một cách diễn giải. Diện mạo và cách vận hành của nó dựa trên chứng cứ, còn mọi thứ bên dưới đều mới.

Đây cũng là một vấn đề về tính bền vững. Phần mềm lỗi thời nhanh hơn nhiều so với dữ liệu mà nó được viết ra để đọc. Khi một chương trình chết đi, các tệp, script và hình ảnh trực quan hóa tạo ra bằng nó trở nên khó mở, ngay cả khi chúng vẫn còn đó. Rất nhiều phần mềm của thập niên 2000 giờ chỉ còn lại dưới dạng ảnh chụp màn hình, video và những tệp nhị phân cũ mà ngày càng ít máy chạy nổi. Skyrails gốc có thể vẫn khởi động được trên một máy tính Windows, hay trong một trình giả lập, nhưng không thể bảo trì, điều chỉnh hay chuyển nó sang nền tảng khác được nữa, vì mã nguồn của nó đã mất.

Như tôi đã dự đoán từ vài năm trước, AI đang trở thành một công cụ thiết thực để chống lại kiểu lỗi thời này. Nó có thể dựng lại một công cụ đã mất từ những dấu vết còn lại, và dựng lại những trình đọc giúp dữ liệu cũ vẫn dùng được. Bước tiếp theo hiển nhiên của dự án này là dạy engine mới đọc các script `.van` và tệp dữ liệu gốc, để những bản trình diễn mà Yose Widjaja viết năm 2007 có thể chạy lại. Với bất kỳ ai quan tâm đến tính bền vững của dữ liệu, dù trong nghiên cứu, trong ngành lưu trữ hay trong nhân văn số, điều này đáng được lưu tâm.

Skyrails đã đi trước thời đại, và gần hai mươi năm sau vẫn còn gây ấn tượng. Toàn bộ công lao về ý tưởng và thiết kế thuộc về Yose Widjaja, và tôi mong những dòng này sẽ đến được với anh.
