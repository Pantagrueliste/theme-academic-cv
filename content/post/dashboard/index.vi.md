---
title: Kho lưu trữ trong một cái nhìn
subtitle: Trực quan hóa dữ liệu tương tác giúp gì cho nghiên cứu lưu trữ

# Summary for listings and search engines
summary: Ứng dụng web dạng bảng điều khiển giúp nhà nghiên cứu nắm rõ tình hình trong kho lưu trữ, nhờ đó kho lưu trữ dễ tiếp cận hơn và công việc nghiên cứu hiệu quả hơn

# Link this post with a project
projects: [Filippo Cavriana's Secret Correspondence, 1568—1589.]

# Date published
date: "2021-05-24T16:00:00Z"

# Date updated
lastmod: "2021-05-24T16:00:00Z"

# Is this an unpublished draft?
draft: false

# Show this page in the Featured widget?
featured: false
machine_translated: true

# Featured image
# Place an image named `featured.jpg/png` in this page's folder and customize its options here.
image:
  caption: ''
  focal_point: ""
  placement: 2
  preview_only: false

authors:
- clement

tags:
- Nhân văn số
- Trực quan hóa dữ liệu
- Nghiên cứu lưu trữ
- Nghiên cứu hiện tại

categories:
- Ghi chép
---

# Vấn đề
Kho lưu trữ lịch sử có thể hỗn độn đến phát nản. Phông *Mediceo del Principato* tại [Lưu trữ Quốc gia Florence](https://www.archiviodistato.firenze.it/asfi/home) là một ví dụ điển hình. Chỉ một phần nhỏ của phông này được lập mục lục; vô số tài liệu nằm rải rác trong hơn 6.500 tập mà chẳng theo lý do nào rõ rệt. Đã vậy, kho lưu trữ chỉ cho phép mỗi người đọc một số lượng tập hạn chế (ở đây người ta gọi là *filze*). Bình thường, giới hạn là 4 *filze* mỗi ngày. Nhưng trong thời đại dịch, con số ấy tụt xuống còn 4 *filze* mỗi hai tuần. Không có mục lục chi tiết, quy mô đồ sộ của kho lưu trữ buộc nhà nghiên cứu phải nghĩ ra chiến lược để nhanh chóng tìm được thứ mình cần.

# Giải pháp
Có người trông vào may rủi; người khác thì cố đoán cho có căn cứ dựa vào niên đại, người nhận, người gửi, nguồn gốc của phông lưu trữ, ngôn ngữ, v.v. Song nếu *nhìn* tất cả các biến ấy cùng một lúc, ta có thể phát hiện những quy luật bất ngờ trong cấu trúc của kho lưu trữ và đoán trúng hơn. Kinh nghiệm của tôi cho thấy: siêu dữ liệu mà nhà nghiên cứu thường gom vào bảng tính, một khi được vẽ thành đồ thị, giúp người ta nắm tình hình trong kho lưu trữ tốt hơn hẳn.

# Thử nghiệm
Nghiên cứu hiện tại của tôi xoay quanh thư từ của một điệp viên thế kỷ XVI. Thư của ông nằm rải rác trong hàng trăm *filze*. Chúng được viết dưới nhiều danh tính khác nhau, gửi cho nhiều người nhận khác nhau – đôi khi khá bất ngờ – từ nhiều nơi khác nhau, v.v. Để tìm ra những *filze* nhiều khả năng chứa thư cần tìm, tôi đã dựng một bảng điều khiển: một ứng dụng web trực quan hóa dữ liệu tương tác ([Plotly Dash](https://plotly.com/dash/)) kết nối đủ loại dữ liệu, trong đó có thông tin địa lý và niên đại, với một sơ đồ phân cấp ([sunburst](https://datavizproject.com/data-type/sunburst-diagram/)) của phông lưu trữ. Chỉ liếc qua bảng điều khiển, tôi biết ngay những gì đã tìm thấy, chúng chiếm tỷ lệ bao nhiêu, và đại khái nên tìm thư mới ở đâu. Hơn nữa, nhấp vào một biến cụ thể là mọi sơ đồ đều cập nhật để hiển thị các tương quan tương ứng.

# Bước tiếp theo
Có lẽ quan trọng hơn cả: bảng điều khiển này có thể được dùng lại như một mục lục trực quan. Khi ấn bản phê bình của những lá thư này được công bố trực tuyến, bảng điều khiển sẽ là một lối vào khác, từ đó người đọc có thể duyệt qua dữ liệu. Vì lý do bảo mật, hiện tôi chỉ có thể đưa ra một ảnh chụp màn hình đã che bớt, nhưng sang năm tôi sẽ công bố bảng điều khiển hoàn chỉnh. Trong lúc chờ đợi, một bản mẫu sẽ sớm ra mắt. Xin hãy đón xem!
