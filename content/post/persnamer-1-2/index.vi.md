---
title: "persNamer 1.2: Một số VIAF, chín tệp thẩm quyền"
subtitle: Công cụ danh mục nhân vật nhỏ bé nay gộp thẳng vào tệp TEI sẵn có của bạn và mang theo mã định danh của các danh mục lớn

summary: >
  persNamer nhận một số VIAF và trả về một mục nhân danh TEI. Phiên bản 1.2
  làm cho mục ấy đáng để có: các biến thể tên, ngày tháng chuẩn hóa, mã định
  danh của chín tệp thẩm quyền quốc gia và quốc tế, cùng một chế độ gộp làm
  giàu danh mục nhân vật sẵn có thay vì in ra từng mẩu.

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

[persNamer](/code/persnamer/) khởi đầu như một tiện ích nhỏ: đưa nó một số VIAF, nhận về một mục `<person>` TEI và thẻ `<persName>` để chú giải văn bản của bạn. Nó chỉ làm đúng một việc, và mục nó tạo ra khá mỏng – một cái tên, hai mốc ngày, một mã định danh. Phiên bản 1.2, phát hành hôm nay, vẫn giữ một việc ấy nhưng làm cho mục nhân danh đáng để giữ lại.

## Một mục nhân danh giờ chứa những gì

Bắt đầu từ cái tên. Một cụm VIAF mang một tên cho mỗi thư viện đóng góp, và persNamer cũ đơn giản lấy nhãn đầu tiên nó gặp. Hỏi nó về Voltaire, nó sẽ trả lời « فولتير، » – dạng tiếng Ả Rập, kèm luôn dấu phẩy thừa ở đuôi – và để cho trọn bộ, thêm một `xml:id` trống. Phiên bản 1.2 đếm các dạng tên trong toàn cụm và giữ lại dạng mà các hồ sơ nguồn đồng thuận; những dạng còn lại đi kèm dưới dạng `<persName type="variant">`, phổ biến nhất xếp trước. Ngày tháng được chuẩn hóa (`1572-08-00` thành `1572-08`) và xuất ra hai lần, vừa là văn bản vừa là thuộc tính `@when` – thứ mà bất kỳ bước xử lý nào hiểu được ngày tháng trên tệp thực sự sẽ đọc. Giới tính và mô tả xuất hiện khi VIAF cung cấp.

Phần tôi mong nhất: mọi mã định danh mà VIAF liên kết tới, qua `schema:sameAs` và qua các mã nguồn của chính nó, đều được ghi ra thành một `<idno>` – BnF, GND, Thư viện Quốc hội Mỹ, SUDOC, Wikidata, ISNI, BNE, LIBRIS, NDL. Một số đi vào, chín danh mục đi ra. Với một danh mục nhân vật (personography), đó là khác biệt giữa một bảng liệt kê tên và một nút trong mạng lưới dữ liệu có thẩm quyền.

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

In XML ra terminal thì ổn với một người. Ấn bản có hàng trăm người. persNamer nay nhận nhiều số VIAF cùng lúc, lịch sự nghỉ một nhịp giữa các yêu cầu, lưu đệm những gì đã tải, và – với `--merge` – chèn thẳng các mục mới vào `<listPerson>` của một tệp TEI sẵn có. Hồ sơ đã có sẵn được nhận ra qua số VIAF và `xml:id` của chúng được dùng lại; mã mới được đối chiếu với tệp và thêm hậu tố (`-2`, `-3`) nếu có nguy cơ trùng; tệp được thụt lề lại, và trước đó một bản sao `.bak` được ghi ra.

```bash
persnamer --merge edition.xml 314802260 36925746
```

Một thay đổi cần biết: tiểu từ đứng trước họ nay mặc định bị bỏ khỏi mã định danh, nên Charles de Téligny là `pers-teligny-c` chứ không phải `pers-deteligny-c`. Nếu dự án của bạn đã thống nhất dùng dạng cũ, `--keep-particle` khôi phục nó; còn nếu bạn thà không phụ thuộc vào tên chút nào, `--id-format viaf` cho bạn `pers-viaf-314802260`.

## Dọn dẹp

Script nay là một gói với lệnh `persnamer`, cài được bằng một dòng với `uv tool install` hoặc `pipx` (hoặc chạy một lần, không cần cài, với `uvx`). Hai mươi sáu bài kiểm thử chạy trên các phản hồi VIAF đã ghi sẵn, nên bộ kiểm thử không cần mạng; CI chạy chúng trên Python từ 3.9 đến 3.13, và đầu ra được kiểm định theo TEI P5. Giấy phép Apache 2.0, như trước.

Điều nó vẫn chưa làm được là cho bạn biết ai đó sinh ở đâu hay làm nghề gì: RDF cụm của VIAF không mang địa danh, cũng chẳng mang nghề nghiệp. Các hồ sơ BnF và GND được liên kết thì có, và giờ bạn đã có số của chúng.

Mã nguồn và tài liệu trên [GitHub](https://github.com/Pantagrueliste/persNamer).
