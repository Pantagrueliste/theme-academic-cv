---
title: Một trình duyệt trực quan cho kho lưu trữ
subtitle: Cách tiếp cận thân thiện với người dùng đối với tài liệu lưu trữ số hóa

# Summary for listings and search engines
summary: Trực quan hóa tương tác đem lại cho người đọc một kênh cảm nhận khác để định hướng trong những tài liệu lưu trữ phức tạp.

# Link this post with a project
projects: [Making & Knowing Project]

# Date published
date: "2021-06-20T16:00:00Z"

# Date updated
lastmod: "2021-06-20T17:00:00Z"

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
  placement: 1
  preview_only: true

authors:
- clement

tags:
- Nhân văn số
- Trực quan hóa dữ liệu
- Nghiên cứu lưu trữ

categories:
- Ghi chép
---
# Vấn đề
Ấn bản kỹ thuật số mang trong mình một nghịch lý: chúng đưa những tài liệu ít người biết đến tới công chúng rộng rãi, nhưng khi tài liệu bị phi vật chất hóa, người đọc mất đi các kênh cảm nhận quen thuộc, dễ mất phương hướng, thậm chí nản lòng trước nội dung. Duyệt qua những kho tài liệu đồ sộ vì thế trở nên nặng nề và đáng ngại. Điều này không chỉ đúng với người chưa quen nghiên cứu lưu trữ, mà cả với những độc giả gặp khó khăn về nhận thức.

# Giải pháp
Đây là chỗ siêu dữ liệu lưu trữ phát huy tác dụng. Từ những dữ liệu ấy, ta có thể tạo ra các hình ảnh trừu tượng tương tác, đem lại cho người đọc một kênh cảm nhận khác, vừa tiện dụng hơn vừa dễ tiếp cận hơn. Để kho lưu trữ có thể duyệt bằng mắt, một sơ đồ cây (treemap) – hay bất kỳ sơ đồ nào phân tách hiệu quả dữ liệu phân cấp – là đủ. 

# Thử nghiệm
Thử nghiệm đầu tiên của tôi phỏng theo mã [Zoomable Treemap](https://observablehq.com/@d3/zoomable-treemap) của `D3.js`, có bổ sung siêu liên kết. Sơ đồ biểu diễn bản thảo BnF Ms Fr 640, các tờ của nó, và các mục trong từng tờ. Màu sắc thể hiện hạng mục chiếm ưu thế. Rê chuột lên mỗi mục sẽ hiện thêm dữ liệu, kể cả siêu liên kết dẫn tới bản thảo.   
Nhờ vậy, sơ đồ cây trở thành một mục lục trực quan tương tác, cho người đọc một cái nhìn tổng quan rất nhanh và linh hoạt, không chỉ về nội dung bản thảo mà còn về kích thước của từng tờ, từng mục.  
~~Trong những tháng tới, tôi sẽ tiếp tục thử nghiệm ý tưởng này với các sơ đồ và hệ phân cấp khác... Xin hãy đón xem!~~ Để xem phiên bản mới của sơ đồ cây, nhấp vào [đây]({{< relref "/post/treemap2" >}}).  
> [!NOTE]
> Để xem tốt nhất, hãy chắc rằng trang web đang ở chế độ Sáng (nhấp vào biểu tượng mặt trăng ở góc trên bên phải).

  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title></title>
    <link rel="preconnect" href="https://fonts.gstatic.com" />
    <link
      href="https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;700&display=swap"
      rel="stylesheet" />
    <link rel="stylesheet" href="css/index.css" />
    <link rel="stylesheet" href="css/vis-treemap.css" />
    <link rel="stylesheet" href="css/vis-tooltip.css" />
  </head>
  <body>
    <p>Click any cell to zoom in, or the top to zoom out.</p>
    <div id="treemap"></div>
    <script src="https://cdn.jsdelivr.net/npm/d3@7.9.0/dist/d3.min.js" integrity="sha384-CjloA8y00+1SDAUkjs099PVfnY2KmDC2BZnws9kh8D/lX1s46w6EPhpXdqMfjK6i" crossorigin="anonymous" referrerpolicy="no-referrer"></script>
    <script src="js/vis-treemap.js"></script>
    <script src="js/vis-tooltip.js"></script>
    <script src="js/index.js"></script>
  </body>