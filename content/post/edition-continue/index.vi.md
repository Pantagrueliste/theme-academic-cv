---
title: "Công cụ mới, thói quen cũ"
subtitle: Một bài học trên Programming Historian về việc xuất bản ấn bản phê bình ngay trong lúc mã hóa

summary: >
  Máy tính đã có mặt nửa thế kỷ, vậy mà ta vẫn làm ấn bản kỹ thuật số như thể làm sách in. Bài học mới
  của tôi cho Programming Historian en français, phần đầu trong hai phần, trình bày những viên gạch nền móng
  cho một ấn bản được xuất bản theo nhịp mã hóa.

date: "2026-10-02T00:00:00Z"
lastmod: "2026-10-02T00:00:00Z"

draft: false
featured: true
machine_translated: true

image:
  caption: 'Người thợ dệt bên khung cửi Jacquard, cùng chuỗi bìa đục lỗ lập trình nên hoa văn. Ảnh: [*IEEE Spectrum*](https://spectrum.ieee.org/the-jacquard-loom-a-driver-of-the-industrial-revolution)'
  focal_point: "Center"
  placement: 2
  preview_only: false

authors:
- clement

tags:
- Nhân văn số
- Ấn bản kỹ thuật số
- Hiệu đính văn bản
- TEI

categories:
- Nhân văn số

projects: [DCE]
---

Khi đón nhận máy in, các nhà nhân văn chủ nghĩa đầu thời cận đại đã trao cho ấn bản cái hình hài mà nó giữ mãi đến nay: văn bản được xác lập, sắp chữ, xuất bản một lần, và nếu có sửa thì cũng phải đợi lần tái bản nhiều năm sau. Máy tính đã có mặt nửa thế kỷ, vậy mà chúng ta vẫn làm ấn bản kỹ thuật số như thể làm sách in: hoàn tất văn bản, công bố một lượt, còn đính chính thì để sau. Bình thì mới, rượu vẫn cũ.

Bài học mới của tôi trên *Programming Historian en français*, [“L’édition critique en continu : publier au rythme de l’encodage (Partie 1)”](https://programminghistorian.org/fr/lecons/edition-critique-continu-pt1), thử coi lời hứa của các công cụ mới là thật. Nếu mã hóa TEI là một dạng mã – mà đúng là thế – thì có thể quản lý phiên bản, kiểm tra hợp lệ và chuyển đổi nó như mọi đoạn mã khác. Giới lập trình từ lâu đã thôi chờ đợi một sản phẩm hoàn chỉnh: mọi thay đổi đều được kiểm tra tự động và phát hành ngay khi đạt yêu cầu. Chẳng có gì ngăn một ấn bản phê bình vận hành theo cách ấy: mỗi lá thư được công bố ngay khi mã hóa và thẩm định xong, rồi được sửa công khai mỗi khi xuất hiện một cách đọc tốt hơn.


## Phần 1: những viên gạch nền móng

Phần đầu này giới thiệu các thành phần giúp người biên tập thoát khỏi quy trình làm việc thừa hưởng từ quá khứ, tất cả đều là mã nguồn mở:

- một tệp **ODD**, tài liệu duy nhất đặc tả cách mã hóa của dự án;
- một **lược đồ RELAX NG** sinh ra từ tệp ấy, buộc văn bản tuân thủ cấu trúc;
- các **quy tắc Schematron**, bổ sung những ràng buộc biên tập mà lược đồ không diễn đạt được;
- một **script kiểm tra hợp lệ**, rà soát toàn bộ kho văn bản chỉ bằng một lệnh và xuất ra kết quả dễ đọc nhờ XSLT.

Các ví dụ được lấy từ thư từ của Filippo Cavriana, ấn bản mà tôi đang [xây dựng theo hướng này](/post/cavriana-edition/). Phần 2 sẽ bổ sung đường ống xử lý (pipeline) nối các thành phần ấy lại với nhau, để mọi thay đổi trong kho văn bản đều được kiểm tra và xuất bản ngay khi vừa thực hiện. Bài học thuộc dự án [Biên tập hiệu quả](/project/dce/) của tôi, vốn tìm cách hạ giá thành các ấn bản học thuật; tự động hóa khâu xuất bản, để người biên tập không còn phải ngồi chờ một chuyên gia ở cuối dây chuyền, là một trong những khoản tiết kiệm lớn nhất có thể có.


## Phản đối, phủ nhận, hay áp dụng hời hợt

Trí tuệ nhân tạo cũng đang được đón nhận theo đúng kịch bản ấy: phản đối ầm ĩ, phủ nhận, hoặc áp dụng hời hợt. Đó là một lý do khiến tôi thích nhân văn số: hiếm lĩnh vực nào phơi bày nghịch lý này rõ đến thế. Công cụ mới lẽ ra phải là lời mời ta nghĩ lại cách làm việc cho tốt hơn, chứ đâu phải lớp sơn mới phủ lên những lề thói cũ. Bài học này đáp lại lời mời ấy trong lĩnh vực hiệu đính văn bản. Hãy đón chờ Phần 2.

Tôi xin cảm ơn các biên tập viên Daphné Mathelier và Matthias Gille Levenson, các người phản biện Jasmin Macarios và Elsa Van Kote, cùng Anisa Hawes.

Bài học được truy cập mở tại: [programminghistorian.org/fr/lecons/edition-critique-continu-pt1](https://programminghistorian.org/fr/lecons/edition-critique-continu-pt1) (DOI: [10.46430/phfr0044](https://doi.org/10.46430/phfr0044)).
