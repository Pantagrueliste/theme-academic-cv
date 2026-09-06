---
title: Máy mô phỏng điện báo ITA2
summary: Một trình diễn tương tác về mã điện báo ITA2 (Baudot-Murray), giúp sinh viên nắm bắt những khái niệm nền tảng của mã hóa nhị phân và máy trạng thái.
tags:
  - JavaScript
  - Tương tác
  - Giảng dạy

date: "2025-02-13T00:00:00Z"

# Optional external URL for project (replaces project detail page)
external_link: ""

image:
  caption: Băng điện báo ITA2 với một thông điệp đã mã hóa
  focal_point: Smart

links:
  - type: code
    icon: brands/github
    label: Mã nguồn
    url: https://github.com/Pantagrueliste/BaudotMurray_Emulator
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

Máy mô phỏng ITA2 này là một công cụ giảng dạy đúng nghĩa: nó làm cho những khái niệm mã hóa vốn trừu tượng trở nên hữu hình và có thể thao tác. Khi sinh viên gõ chữ và thấy ngay lập tức chúng biến thành các mẫu lỗ đục, các em đang học cùng lúc nhiều khái niệm then chốt của ngành điện toán và viễn thông.

## Lợi ích sư phạm

Trước hết, máy minh họa biểu diễn nhị phân – làm sao chữ viết biến thành những chuỗi số 1 và số 0. Chúng ta thường dạy điều này trên giấy; nhưng khi tận mắt thấy các lỗ đục hiện ra, sinh viên hiểu ngay rằng một hệ thống vật lý cũng có thể mang thông tin số.

{{< Baudot >}}

Cơ chế chuyển đổi LETTERS/FIGURES đưa khái niệm máy trạng thái vào bài học một cách tự nhiên. Tự tay thử nghiệm, sinh viên phát hiện rằng cùng một chuỗi bit có thể biểu thị những ký tự khác nhau, tùy vào chế độ hiện hành. Trải nghiệm trực tiếp với mã hóa dựa trên trạng thái này chuẩn bị cho các em bước tới những khái niệm điện toán phức tạp hơn.

## Chi tiết triển khai

Máy mô phỏng được viết bằng JavaScript và HTML/CSS, nên dễ dàng nhúng vào bất kỳ trang web nào. Mã nguồn được tổ chức theo mô-đun và có thể điều chỉnh cho những bối cảnh giáo dục khác nhau.

Bạn có thể xem mã nguồn và tự mình thử máy mô phỏng tại [kho GitHub](https://github.com/Pantagrueliste/BaudotMurray_Emulator).