---
title: persNamer
summary: Công cụ Python chuyển mã định danh VIAF thành mục nhân danh TEI XML và thẻ chú giải, giúp hợp lý hóa việc kiểm soát thẩm quyền trong ấn bản học thuật kỹ thuật số.
tags:
  - XML
  - TEI
  - Nhân văn số
  - Python
  - VIAF
  - Dữ liệu liên kết

date: "2025-03-28T00:00:00Z"

# Optional external URL for project (replaces project detail page)
external_link: ""

image:
  caption: Trình diễn persNamer
  focal_point: Smart

links:
  - type: code
    icon: brands/github
    label: Mã nguồn
    url: https://github.com/Pantagrueliste/persNamer
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

## persNamer: Nối TEI với Virtual International Authority File

[![DOI](https://zenodo.org/badge/933156851.svg)](https://doi.org/10.5281/zenodo.14875030)

persNamer là một công cụ Python chuyên dụng, giúp đưa dữ liệu nhân danh có thẩm quyền từ VIAF (Virtual International Authority File) vào tài liệu TEI XML một cách trơn tru. Bằng cách chuyển mã định danh VIAF thành thẻ đánh dấu TEI dùng được ngay, persNamer giảm hẳn phần việc thủ công khi tạo các mục nhân danh có cấu trúc cho ấn bản học thuật kỹ thuật số.

## Bài toán kiểm soát thẩm quyền trong TEI

Ấn bản học thuật kỹ thuật số thường đòi hỏi định danh chính xác các nhân vật lịch sử, kể cả tên chuẩn hóa và năm sinh năm mất. Để kiểm soát thẩm quyền nhất quán trong suốt một dự án, người ta phải:

1. Nhận diện nhân vật trong văn bản lịch sử
2. Tìm dữ liệu có thẩm quyền về họ
3. Tạo các mục TEI đúng định dạng
4. Bảo đảm tham chiếu nhất quán trong toàn dự án

Các bước này thường làm bằng tay, tốn thời gian và dễ thiếu nhất quán.

## persNamer vận hành ra sao

persNamer tự động hóa quy trình ấy bằng cách:

1. **Lấy dữ liệu VIAF**: Từ một mã định danh VIAF, công cụ truy xuất dữ liệu RDF qua cơ chế thương lượng nội dung HTTP
2. **Trích xuất thông tin chính**: Phân tích RDF để lấy tên ưu tiên, ngày sinh và ngày mất
3. **Sinh thẻ đánh dấu TEI**: Tạo ra hai đoạn XML thiết yếu:
   - Một **mục trong tệp thẩm quyền** (phần tử `<person>` với `xml:id` được sinh tự động, `<persName>`, `<birth>`, `<death>` và `<idno type="VIAF">`)
   - Một **thẻ chú giải** riêng (`<persName>` với thuộc tính `ref` trỏ về mục thẩm quyền)

Đầu ra kép này cho phép người biên tập duy trì một tệp thẩm quyền tập trung, đồng thời dễ dàng chèn thẻ chú giải vào văn bản TEI của mình.

## Tính năng chính

- **Sinh mã định danh chuẩn hóa**: Tạo XML ID nhất quán theo dạng `pers-[familyname]-[givenname initial]` (ví dụ `pers-deteligny-c`)
- **Phân tích RDF**: Dùng `rdflib` để trích thông tin từ nhiều thuộc tính RDF khác nhau (ví dụ `rdfs:label`, `schema:name`, `viaf:mainHead`)
- **Giao diện dòng lệnh**: Chạy đơn giản, chỉ cần một số VIAF làm đối số bắt buộc duy nhất
- **Đầu ra chi tiết**: Cung cấp thông tin xử lý đầy đủ bên cạnh XML kết quả

## Ví dụ sử dụng

```bash
python persNamer.py 314802260
```

Lệnh này cho ra:

```xml
<person xml:id="pers-deteligny-c">
  <persName>Charles deTéligny</persName>
  <birth>1535</birth>
  <death>1572-08-24</death>
  <idno type="VIAF">314802260</idno>
</person>

<persName ref="#pers-deteligny-c">Charles deTéligny</persName>
```

## Ứng dụng trong nhân văn số

persNamer đặc biệt hữu ích cho:

- Ấn bản học thuật kỹ thuật số cần kiểm soát thẩm quyền
- Dự án mã hóa TEI làm việc với nhân vật lịch sử
- Sáng kiến dữ liệu liên kết nối tài liệu với hồ sơ thẩm quyền
- Bảo đảm tính nhất quán trên những kho ngữ liệu TEI lớn
- Giảng dạy khái niệm kiểm soát thẩm quyền trong các khóa nhân văn số

## Triển khai

persNamer được viết bằng Python và phụ thuộc vào:
- `requests` cho các yêu cầu HTTP
- `rdflib` để phân tích RDF
- `lxml` để xử lý XML

Mã nguồn và tài liệu có tại [kho GitHub](https://github.com/Pantagrueliste/persNamer).