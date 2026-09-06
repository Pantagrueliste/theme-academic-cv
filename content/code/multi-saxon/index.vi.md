---
title: Multi-Saxon
summary: Công cụ hiệu năng cao để chạy song song các phép biến đổi XSLT 2.0/3.0 trên những kho ngữ liệu XML TEI lớn, xử lý được những biến đổi mà LXML không kham nổi.
tags:
  - XSLT
  - XML
  - TEI
  - Nhân văn số
  - Python
  - Java
  - Hiệu năng

date: "2025-03-28T00:00:00Z"

# Optional external URL for project (replaces project detail page)
external_link: ""

image:
  caption: Multi-Saxon đang vận hành
  focal_point: Smart

links:
  - type: code
    icon: brands/github
    label: Mã nguồn
    url: https://github.com/Pantagrueliste/multi-saxon
url_code: ""
url_pdf: ""
url_slides: ""
url_video: ""

# Slides (optional).
#   Associate this project with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides = "example-slides"` references `content/slides/example-slides.md`.
#   Otherwise, set `slides = ""`.
slides: ""
machine_translated: true
---

## Multi-Saxon: Xử lý XSLT song song cho kho ngữ liệu TEI lớn

Multi-Saxon lấp một khoảng trống đáng kể trong bộ công cụ xử lý XML: nó cho phép chạy song song các phép biến đổi XSLT 2.0 và 3.0 mà LXML (thư viện XML phổ biến của Python) không xử lý được. Được thiết kế riêng cho những bộ sưu tập tài liệu XML TEI lớn, Multi-Saxon rút ngắn đáng kể thời gian xử lý nhờ thực thi song song hiệu quả.

## Tính năng chính

- **Hỗ trợ XSLT nâng cao**: Xử lý các phép biến đổi XSLT 2.0 và 3.0, vượt ngoài khả năng của LXML
- **Xử lý song song**: Giảm mạnh thời gian biến đổi trên các bộ sưu tập tài liệu lớn nhờ song song hóa
- **Tối ưu cho TEI**: Được thiết kế riêng cho tài liệu XML theo chuẩn Text Encoding Initiative (TEI)
- **Hiệu năng mở rộng được**: Xử lý hiệu quả những kho ngữ liệu từ vài trăm đến hàng nghìn tài liệu
- **Đa nền tảng**: Chạy được trên nhiều hệ điều hành và môi trường khác nhau

## Vấn đề mà Multi-Saxon giải quyết

Học giả nhân văn số làm việc với TEI thường vấp phải hai trở ngại lớn:

1. LXML (thư viện xử lý XML thông dụng của Python) chỉ hỗ trợ XSLT 1.0, nên không thể dùng các tính năng nâng cao của XSLT 2.0/3.0
2. Xử lý tuần tự những kho ngữ liệu TEI lớn có thể tốn thời gian đến mức không chấp nhận được

Multi-Saxon giải quyết cả hai bằng cách tận dụng năng lực XSLT nâng cao của Saxon, đồng thời phân phối việc xử lý trên nhiều lõi để đạt mức tăng hiệu năng đáng kể.

## Triển khai

Multi-Saxon kết hợp Python với bộ xử lý Saxon của Java để tạo nên một đường ống biến đổi hiệu năng cao:

- Dùng thư viện Saxon của Java để xử lý XSLT 2.0/3.0 một cách vững chắc
- Dùng cơ chế đa tiến trình để phân phối các phép biến đổi trên những lõi CPU sẵn có
- Quản lý hiệu quả các nhóm bộ xử lý nhằm tối đa hóa thông lượng
- Cung cấp giao diện đơn giản để xử lý hàng loạt tài liệu TEI

## Ví dụ sử dụng

```python
from multi_saxon import MultiSaxon

# Initialize with your XSLT stylesheet
transformer = MultiSaxon("transform.xsl")

# Transform a single document
transformer.transform("input.xml", "output.xml")

# Transform an entire directory in parallel
transformer.transform_directory("input_dir", "output_dir")
```

## Tác động đối với nhân văn số

Với những dự án nhân văn số phải xử lý các bộ sưu tập tài liệu TEI lớn, Multi-Saxon cho phép:

- Thực hiện những phép biến đổi phức tạp trên toàn bộ kho ngữ liệu, điều bất khả với LXML
- Rút ngắn mạnh thời gian xử lý (thường gấp 5–10 lần trên hệ thống đa lõi)
- Phân tích tinh vi hơn nhờ các tính năng nâng cao của XSLT 2.0/3.0
- Đơn giản hóa quy trình xử lý trọn bộ sưu tập tài liệu

Mã nguồn và tài liệu có tại [kho GitHub](https://github.com/Pantagrueliste/multi-saxon).
