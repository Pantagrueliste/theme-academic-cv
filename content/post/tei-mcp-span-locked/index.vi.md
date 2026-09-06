---
title: "tei-mcp v0.3: Mã hóa TEI mà không viết lại văn bản gốc"
subtitle: Ghép khóa theo đoạn (span-locked composition) khiến việc bịa đặt phần thân văn bản trở thành bất khả ngay từ cấu trúc

summary: >
  Bản phát hành mới của tei-mcp giới thiệu cơ chế ghép khóa theo đoạn, một hệ
  thống được thiết kế để ngăn chặn loại bịa đặt tai hại nhất trong mã hóa TEI
  có AI hỗ trợ: âm thầm viết lại văn bản gốc. Mô hình không bao giờ gõ phần
  thân văn bản; nó chỉ đăng ký các thẻ dưới dạng vị trí ký tự trên văn bản gốc,
  và bộ ghép từ chối trả về bất kỳ tài liệu TEI nào có nội dung văn bản phẳng
  khác với bản gốc dù chỉ một byte.

date: "2026-05-05T00:00:00Z"
lastmod: "2026-05-05T00:00:00Z"

draft: false
featured: true
machine_translated: true

authors:
- clement

tags:
- Nhân văn số
- TEI
- MCP
- AI

categories:
- Nhân văn số
---

Khi [lần đầu viết về tei-mcp](/post/tei-mcp/), mục tiêu của tôi là chặn các trợ
lý AI bịa ra thẻ đánh dấu TEI. Neo vào lược đồ đã giải quyết được một phần vấn
đề: có trong tay quyền truy cập trực tiếp, qua công cụ, vào đặc tả P5, mô hình
không còn phải đoán một phần tử nghĩa là gì hay nhận những thuộc tính nào. Đầu
ra vượt qua kiểm định.

Thế nhưng trong mã hóa TEI, bịa đặt có hai bộ mặt, và lược đồ chỉ bắt được một.
Kiểm định theo đặc tả cho bạn biết *thẻ đánh dấu* có đúng dạng hay không. Nó
chẳng nói gì về *văn bản* mà thẻ ấy bao bọc. Mà chính ở đó – ở bản thân văn bản
– mới là nơi trú ngụ của những bịa đặt tai hại hơn. Ghép khóa theo đoạn, tính
năng chủ đạo của v0.3, được thiết kế riêng để ngăn chặn chúng.

{{< toc >}}

## Thứ bịa đặt mà lược đồ không bắt được

Hãy yêu cầu một mô hình mã hóa một lá thư tiếng Pháp thế kỷ XVI: bạn thường sẽ
nhận về một tài liệu TEI trông hoàn hảo. Phần đầu được điền đầy đủ, các thẻ
`<persName>` đặt đúng chỗ, `<dateline>` đúng dạng. Chạy qua `validate_document`
– đạt.

Rồi đem so phần thân với văn bản gốc.

`mesme` đã biến thành `même`. Một dấu phẩy đã đổi chỗ. `luy` bị lặng lẽ hiện đại
hóa thành `lui`. Một mệnh đề khó đọc trong bản thảo được "sửa" thành thứ gì đó
gọn gàng hơn. Không thay đổi nào trong số này được yêu cầu. Không thay đổi nào
được báo. Tài liệu hợp lệ theo lược đồ, và sai một cách lặng lẽ.

Với quy trình lưu trữ – nơi văn bản đã mã hóa trở thành bản ghi vĩnh viễn mà
người đọc, chỉ mục tìm kiếm và trích dẫn sau này đều dựa vào – đây chính là kiểu
thất bại đáng lo nhất. Một thẻ sai dạng thì gây bực mình. Một chính tả bị hiện
đại hóa mà năm năm sau chẳng ai nhận ra thì là văn bản đã bị làm hỏng.

## Ghép khóa theo đoạn

Bản phát hành mới (v0.3) đi kèm một cơ chế chống bịa đặt nhắm thẳng vào kiểu thất
bại này. Mục tiêu thiết kế là làm cho việc bịa đặt phần thân văn bản trở thành
bất khả ngay từ cấu trúc, chứ không chỉ là khó xảy ra.

Ý tưởng rất đơn giản: **mô hình không bao giờ gõ phần thân văn bản**.

Thay vào đó, quy trình diễn ra như sau:

1. Mô hình gọi `get_source("letter_001")` và nhận về văn bản gốc thuần dưới
   dạng một chuỗi bất biến.
2. Với mỗi thẻ muốn áp dụng, nó gọi
   `tag_span("letter_001", start, end, element_path, attrs)` – đăng ký một
   phần tử TEI tại một khoảng ký tự trên văn bản gốc.
3. Xong việc, nó gọi `compose("letter_001")`. Máy chủ đan các thẻ đã ghi nhận
   vào văn bản gốc, kết xuất tài liệu TEI cuối cùng, rồi kiểm tra *từng byte
   một* rằng nội dung văn bản phẳng của tài liệu vừa kết xuất bằng đúng văn
   bản gốc.

Nếu các byte khớp, tài liệu được trả về. Nếu không – nếu các thẻ của mô hình, vì
lý do nào đó, hàm ý một phần thân khác với bản gốc dù chỉ một ký tự –
`compose()` sẽ báo lỗi thay vì trả về một tài liệu đã bị hỏng.

Không có lối nào trong quy trình này để mô hình tạo ra một tài liệu TEI mà phần
thân khác với văn bản gốc. Bất biến này mang tính cơ học, không phải tính hành
vi. Bạn không cần tin rằng mô hình sẽ không bịa; bạn chỉ cần tin vào một phép
so sánh `==` giữa hai chuỗi byte.

## Nó là gì, và không phải là gì

Ghép khóa theo đoạn **bổ sung** cho việc neo vào lược đồ, chứ không thay thế nó.
Các công cụ neo lược đồ (`validate_document`, `lookup_element`,
`valid_children`, cùng phần còn lại của mười sáu công cụ ban đầu) giúp mô hình
tạo ra TEI *hợp lệ*. Ghép khóa theo đoạn bảo đảm phần thân văn bản bên trong TEI
ấy *trung thành* với bản gốc. Một quy trình mã hóa có thể triển khai thực sự
phải thỏa mãn cả hai trục, và giờ đây cả hai đều được một máy chủ duy nhất đảm
đương.

Nó cũng không phải là liều thuốc tiên chữa bách bệnh. `compose()` chưa kiểm tra
xem các thẻ đã đăng ký có được phép theo một bản tùy biến ODD đã nạp hay không –
đó là việc của bước tiếp theo. Các thẻ đã ghi nhận nằm trong bộ nhớ tiến trình
và không sống sót qua một lần khởi động lại. Và các tệp gốc phải đọc được từ nơi
máy chủ chạy. Tất cả đều có thể khắc phục; không điều nào làm lung lay bất biến
cốt lõi.

## Vì sao điều này quan trọng vượt ra ngoài TEI

Mẫu hình này có thể khái quát hóa. Bất cứ khi nào ta yêu cầu một mô hình chú
giải, biến đổi hay bao bọc một đoạn văn bản – và bất cứ khi nào tính toàn vẹn
của văn bản gốc quan trọng hơn khả năng "cải thiện" nó của mô hình – thì cùng
một dạng giải pháp đều áp dụng được. Đừng bắt mô hình gõ lại văn bản. Hãy bắt nó
đưa ra chỉ dẫn trên văn bản, rồi để một bộ ghép tất định áp dụng các chỉ dẫn ấy
dưới một bất biến về đẳng thức.

Riêng với ấn bản kỹ thuật số, điều này thay đổi những gì bạn có thể giao cho mô
hình một cách có trách nhiệm. Mã hóa bỗng trở thành công việc có thể ủy thác mà
không phải tự tay so từng đầu ra với bản gốc. Máy đi con đường tẻ nhạt; người
biên tập duyệt thẻ đánh dấu, chứ không duyệt chính tả.

## Cập nhật

Nếu bạn đã cài tei-mcp:

```bash
uvx tei-mcp@latest
```

Hoặc cài mới:

```bash
pip install tei-mcp
```

Để dùng ghép khóa theo đoạn, hãy trỏ máy chủ tới một thư mục chứa các tệp văn
bản gốc thuần:

```bash
export TEI_MCP_SPAN_SOURCE_ROOT=/path/to/sources
uvx tei-mcp
```

Phần gốc của tên mỗi tệp trở thành mã tài liệu (`letter_001.txt` →
`letter_001`).

Mã nguồn, tài liệu đầy đủ và ghi chú thiết kế về bất biến:
[github.com/Pantagrueliste/tei-mcp](https://github.com/Pantagrueliste/tei-mcp)
