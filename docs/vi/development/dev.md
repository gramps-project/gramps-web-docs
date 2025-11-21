---
hide:
  - toc
---

# Phát triển Gramps Web: tổng quan

Gramps Web là một ứng dụng web bao gồm hai thành phần được phát triển riêng biệt:

- **Gramps Web API** là một API RESTful được viết bằng Python và dựa trên Flask. Mã nguồn được lưu trữ tại [github.com/gramps-project/gramps-web-api](https://github.com/gramps-project/gramps-web-api/). Nó quản lý quyền truy cập cơ sở dữ liệu và các chức năng gia phả bằng cách trực tiếp sử dụng thư viện Gramps Python. Nó đóng vai trò là backend của Gramps Web. Để biết tài liệu phát triển, xem [Backend](backend/index.md).
- **Gramps Web Frontend** là một ứng dụng web Javascript đóng vai trò là frontend cho Gramps Web. Mã nguồn được lưu trữ tại [github.com/gramps-project/gramps-web](https://github.com/gramps-project/gramps-web/). Để biết tài liệu phát triển, xem [Frontend](frontend/index.md).

Một lưu ý về phiên bản: Gramps Web API và Gramps Web frontend được phiên bản độc lập. Hiện tại, "Gramps Web" &ndash; ứng dụng kết hợp &ndash; không có số phiên bản riêng biệt. Cả hai dự án tuân theo [SemVer](https://semver.org/).

Nếu bạn không phải là nhà phát triển Python hoặc Javascript nhưng vẫn muốn đóng góp cho Gramps Web, hãy xem [Contribute](../contribute/contribute.md).
