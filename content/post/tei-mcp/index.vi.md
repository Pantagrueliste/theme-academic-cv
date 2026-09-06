---
title: "tei-mcp: TEI P5 cho tác tử AI"
subtitle: Một máy chủ MCP giúp trợ lý AI hiểu Hướng dẫn TEI

summary: >
  tei-mcp là một máy chủ MCP mã nguồn mở, cho phép các trợ lý lập trình AI truy cập
  trực tiếp vào đặc tả TEI P5 – tra cứu phần tử, phân giải thuộc tính, kiểm tra
  lồng ghép, kiểm định tài liệu và tùy biến ODD.

date: "2026-03-15T00:00:00Z"
lastmod: "2026-03-15T00:00:00Z"

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

Nếu đã từng nhờ một trợ lý lập trình AI viết TEI XML, hẳn bạn nhận ra nó hay
sai. Phần tử mọc ở chỗ không được phép. Thuộc tính thì bịa ra. Quy tắc lồng ghép
bị bỏ qua. Mô hình chỉ có một ý niệm đại khái về hình dáng của TEI, chứ không nắm
chắc đặc tả.

tei-mcp giải quyết chuyện này bằng cách cho tác tử AI truy cập trực tiếp, qua
công cụ, vào Hướng dẫn TEI P5.

{{< toc >}}

## MCP là gì?

[Model Context Protocol](https://modelcontextprotocol.io) (MCP) là một chuẩn mở
cho phép các ứng dụng AI kết nối với nguồn dữ liệu và công cụ bên ngoài. Hãy hình
dung nó như cổng USB của AI: một giao thức duy nhất để bất kỳ ứng dụng khách tương
thích nào – Claude, Cursor, Windsurf và những cái khác – cắm vào các dịch vụ chuyên
biệt.

Một máy chủ MCP cung cấp những *công cụ* mà AI có thể gọi ngay trong lúc trò chuyện.
Thay vì dựa vào dữ liệu huấn luyện đã ghi nhớ, mô hình có thể tra hỏi một nguồn
sống, có thẩm quyền.

## tei-mcp làm gì

tei-mcp phân tích đặc tả ODD của TEI P5 và cung cấp 16 công cụ, bao quát những câu
hỏi thường gặp nhất của người biên tập hay người mã hóa:

- **Phần tử này là gì?** Tra cứu bất kỳ phần tử, lớp, macro hay mô-đun nào theo tên,
  không phân biệt hoa thường, kèm gợi ý khi gõ nhầm.
- **Nó nhận những thuộc tính nào?** Phân giải thuộc tính xuyên suốt toàn bộ hệ
  phân cấp lớp – thuộc tính cục bộ trước, rồi đến thuộc tính kế thừa theo thứ tự.
- **Bên trong nó chứa được gì?** Khai triển mô hình nội dung thành cây có cấu trúc,
  hoặc lấy danh sách phẳng các phần tử con hợp lệ.
- **Phần tử này đặt ở đây được không?** Kiểm tra quan hệ cha–con, hoặc lần theo
  khả năng đạt tới qua toàn bộ hệ phân cấp phần tử.
- **Tài liệu của tôi có hợp lệ không?** Kiểm định một tệp TEI XML theo đặc tả: mô
  hình nội dung, giá trị thuộc tính, danh sách giá trị đóng, tính toàn vẹn của tham
  chiếu, và cảnh báo về phần tử đã lỗi thời.
- **Còn lược đồ riêng của dự án tôi thì sao?** Nạp một tệp tùy biến ODD để giới hạn
  tất cả những gì kể trên vào tập con TEI riêng của dự án bạn.

## Vì sao điều này quan trọng

Mã hóa TEI đòi hỏi tra cứu Hướng dẫn không ngừng. Người mã hóa lão luyện thuộc lòng
những mẫu thông dụng nhất, nhưng ngay cả họ cũng phải giở đặc tả khi gặp phần tử ít
quen hay mô hình nội dung phức tạp. Với trợ lý AI, vốn chẳng có chút hiểu biết
thuộc lòng nào như thế, vấn đề còn tệ hơn: chúng bịa ra thứ đánh dấu trông có vẻ
hợp lý mà thực ra sai.

Có tei-mcp, AI không còn phải đoán. Nó có thể tra câu trả lời trong đặc tả trước
khi viết ra dù chỉ một dấu ngoặc nhọn. Kết quả là thứ đánh dấu tuân thủ TEI P5 –
hoặc tuân thủ bản tùy biến ODD của dự án bạn.

## Bắt đầu

Cài từ PyPI:

```bash
pip install tei-mcp
```

Rồi thêm vào cấu hình của ứng dụng khách MCP:

```json
{
  "mcpServers": {
    "tei": {
      "command": "uvx",
      "args": ["tei-mcp"]
    }
  }
}
```

Máy chủ tải đặc tả TEI về trong lần chạy đầu tiên và hoạt động với mọi ứng dụng
khách tương thích MCP.

Mã nguồn và tài liệu đầy đủ: 
[github.com/Pantagrueliste/tei-mcp](https://github.com/Pantagrueliste/tei-mcp)
