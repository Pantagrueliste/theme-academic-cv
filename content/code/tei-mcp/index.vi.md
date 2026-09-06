---
title: tei-mcp
summary: Máy chủ MCP giúp tác tử AI đọc và viết TEI XML hợp lệ, với 16 công cụ bao quát tra cứu phần tử, phân giải thuộc tính, khai triển mô hình nội dung, kiểm tra lồng ghép, kiểm định tài liệu và tùy biến ODD.
tags:
  - XML
  - TEI
  - Nhân văn số
  - Python
  - MCP
  - AI

date: "2026-03-15T00:00:00Z"

external_link: ""

image:
  caption: Biểu ngữ khởi động của tei-mcp
  focal_point: Smart

links:
  - type: code
    icon: brands/github
    label: Mã nguồn
    url: https://github.com/Pantagrueliste/tei-mcp
  - type: site
    icon: brands/python
    label: PyPI
    url: https://pypi.org/project/tei-mcp/
url_code: ""
url_pdf: ""
url_slides: ""
url_video: ""

slides: ""
machine_translated: true
---

## tei-mcp: TEI P5 cho tác tử AI

tei-mcp là một máy chủ [MCP](https://modelcontextprotocol.io) mã nguồn mở, cho phép các trợ lý lập trình AI truy cập trực tiếp vào đặc tả [TEI P5](https://tei-c.org/guidelines/). Thay vì dựa vào dữ liệu huấn luyện đã ghi nhớ – thứ thường sinh ra thẻ đánh dấu trông hợp lý mà sai – AI có thể tra cứu đặc tả theo thời gian thực.

## Tính năng

Máy chủ phân tích ODD của TEI P5 và cung cấp 16 công cụ:

- **Tra cứu** bất kỳ phần tử, lớp, macro hay mô-đun nào theo tên, không phân biệt hoa thường, kèm gợi ý khi gõ nhầm
- **Phân giải thuộc tính** xuyên suốt toàn bộ hệ phân cấp lớp TEI (cục bộ + kế thừa)
- **Khai triển mô hình nội dung** thành cây có cấu trúc, với phân giải lớp và macro
- **Kiểm tra lồng ghép** – quan hệ cha–con trực tiếp hoặc khả năng đạt tới đệ quy, có theo dõi đường dẫn
- **Kiểm định tài liệu** theo TEI P5: mô hình nội dung, thuộc tính, danh sách giá trị đóng, tính toàn vẹn của tham chiếu và cảnh báo lỗi thời
- **Kiểm định từng phần tử** cho quy trình biên tập từng bước
- **Nạp tùy biến ODD** để giới hạn lược đồ vào tập con riêng của dự án
- **Tìm kiếm** trên mọi loại thực thể bằng biểu thức chính quy

## Cài đặt

```bash
pip install tei-mcp
```

Hoặc chạy trực tiếp bằng:

```bash
uvx tei-mcp
```

## Sử dụng

Thêm vào bất kỳ ứng dụng khách tương thích MCP nào (Claude, Cursor, Windsurf, v.v.):

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

Mã nguồn và tài liệu có tại [kho GitHub](https://github.com/Pantagrueliste/tei-mcp).
