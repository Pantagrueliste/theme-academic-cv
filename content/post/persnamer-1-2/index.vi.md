---
title: "persNamer 1.2: Một số VIAF, chín tệp thẩm quyền"
subtitle: Công cụ danh mục nhân vật nhỏ bé nay biết tự gộp vào tệp TEI sẵn có của bạn, lại mang về cả mã định danh của các danh mục lớn

summary: >
  Đưa persNamer một số VIAF, nó trả lại một mục nhân danh TEI. Với phiên bản
  1.2, mục ấy rốt cuộc có da có thịt: các biến thể tên, ngày tháng chuẩn hóa,
  mã định danh của chín tệp thẩm quyền quốc gia và quốc tế, cùng một chế độ
  gộp làm giàu danh mục nhân vật sẵn có thay vì in ra từng mẩu XML.

date: "2026-09-07T00:00:00Z"
lastmod: "2026-09-07T00:00:00Z"

draft: false
featured: false
machine_translated: true

image:
  caption: ''
  focal_point: "Center"
  placement: 2
  preview_only: false

authors:
- clement

tags:
- TEI
- VIAF
- Dữ liệu liên kết
- Nhân văn số
- Python

categories:
- Nhân văn số
---

Thuở đầu, [persNamer](/code/persnamer/) chỉ là một tiện ích nhỏ: đưa vào một số VIAF, nhận về một mục `<person>` TEI kèm thẻ `<persName>` để chú giải văn bản. Chỉ một việc, không hơn – mà mục nhân danh làm ra cũng khá mỏng: một cái tên, hai mốc ngày, một mã định danh. Phiên bản 1.2 ra mắt hôm nay vẫn chỉ làm đúng một việc ấy, nhưng lần này mục nhân danh đã đáng để giữ lại.

## Một mục nhân danh giờ chứa những gì

Trước hết là cái tên. Trong một cụm VIAF, mỗi thư viện đóng góp mang đến một dạng tên riêng, và persNamer cũ cứ gặp nhãn nào đầu tiên là lấy nhãn ấy. Hỏi nó về Voltaire, nó đáp « فولتير، » – dạng chữ Ả Rập, dấu phẩy thừa ở đuôi cũng mang theo luôn – rồi tặng kèm một `xml:id` trống cho đủ bộ. Nay công cụ đếm các dạng tên trong toàn cụm, giữ lại dạng được các hồ sơ nguồn đồng thuận; những dạng còn lại xếp theo sau dưới dạng `<persName type="variant">`, dạng nào phổ biến hơn đứng trước. Ngày tháng được chuẩn hóa (`1572-08-00` thành `1572-08`) và ghi hai lần: một lần thành văn bản, một lần trong thuộc tính `@when` – mà thực ra, bất kỳ bước xử lý nào hiểu ngày tháng cũng chỉ đọc chỗ ấy. Giới tính và mô tả có mặt khi VIAF cung cấp.

Còn đây là phần tôi mong nhất. Mọi mã định danh mà VIAF nối tới nhân vật – qua `schema:sameAs` lẫn qua mã định danh của chính các nguồn trong VIAF – nay đều được ghi thành một `<idno>` riêng: BnF, GND, Thư viện Quốc hội Mỹ, SUDOC, Wikidata, ISNI, BNE, LIBRIS, NDL. Một số vào, chín danh mục ra. Với một danh mục nhân vật (personography), đó là cả một khoảng cách: giữa một bảng kê tên suông và một nút trong mạng lưới dữ liệu thẩm quyền.

```xml
<person xml:id="pers-teligny-c">
  <persName>Charles de Téligny</persName>
  <birth when="1535">1535</birth>
  <death when="1572-08-24">1572-08-24</death>
  <sex value="M">M</sex>
  <idno type="VIAF">314802260</idno>
  <idno type="BNF">16133360</idno>
  <idno type="Wikidata">Q1868249</idno>
  <idno type="ISNI">0000000071126808</idno>
</person>
```

## Từ những mẩu lẻ đến một danh mục nhân vật

In XML ra terminal, với một người thì được; nhưng một ấn bản có tới hàng trăm người. Vì thế persNamer nay nhận nhiều số VIAF một lượt, lịch sự nghỉ một nhịp giữa hai lần hỏi VIAF, giữ lại trong bộ đệm những gì đã tải để khỏi hỏi lại, và – khi có `--merge` – chèn thẳng các mục mới vào `<listPerson>` của tệp TEI sẵn có. Ai đã có trong tệp thì được nhận ra qua số VIAF và giữ nguyên `xml:id` cũ; mã mới được đối chiếu với tệp, hễ trùng là thêm hậu tố (`-2`, `-3`); cuối cùng cả tệp được thụt lề lại – dĩ nhiên, sau khi một bản sao `.bak` đã được cất sẵn.

```bash
persnamer --merge edition.xml 314802260 36925746
```

Có một thay đổi nên biết: tiểu từ đứng trước họ nay mặc định không còn nằm trong mã định danh nữa, nên Charles de Téligny thành `pers-teligny-c` thay vì `pers-deteligny-c` như trước. Dự án nào đã quen dạng cũ thì `--keep-particle` trả lại y nguyên; còn ai không muốn mã định danh phụ thuộc vào tên người chút nào thì `--id-format viaf` cho ra `pers-viaf-314802260`.

## Dọn dẹp

Script nay đã thành một gói đàng hoàng, có lệnh `persnamer` riêng: một dòng `uv tool install` hoặc `pipx` là cài xong, hoặc muốn chạy thử một lần mà không cài thì có `uvx`. Hai mươi sáu bài kiểm thử chạy trên các phản hồi VIAF đã ghi sẵn, nên bộ kiểm thử không cần đến mạng; CI chạy lại chúng trên Python từ 3.9 đến 3.13, và đầu ra được kiểm định theo TEI P5. Giấy phép vẫn là Apache 2.0.

Điều nó vẫn chưa làm được là cho bạn biết một người sinh ở đâu, sống bằng nghề gì: RDF cụm của VIAF không có địa danh mà cũng chẳng có nghề nghiệp. Nhưng các hồ sơ BnF và GND liên kết với nó thì có – và giờ số của chúng đã nằm trong tay bạn.

Mã nguồn và tài liệu trên [GitHub](https://github.com/Pantagrueliste/persNamer).
