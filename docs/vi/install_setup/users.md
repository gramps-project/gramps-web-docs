# Hệ thống người dùng

Gramps Web không được thiết kế để công khai trên internet cho người dùng công cộng, mà chỉ dành cho người dùng đã xác thực. Tài khoản người dùng có thể được tạo bởi chủ sở hữu trang web thông qua dòng lệnh hoặc giao diện web, hoặc bằng cách tự đăng ký và được phê duyệt sau đó bởi chủ sở hữu trang web.

## Vai trò người dùng

Các vai trò người dùng sau đây hiện đang được định nghĩa.

Vai trò | ID vai trò | Quyền hạn
--------|------------|------------
Khách   | 0          | Xem các đối tượng không riêng tư
Thành viên | 1      | Khách + xem các đối tượng riêng tư
Người đóng góp* | 2 | Thành viên + thêm đối tượng
Biên tập viên | 3   | Người đóng góp + chỉnh sửa và xóa đối tượng
Chủ sở hữu | 4     | Biên tập viên + quản lý người dùng
Quản trị viên | 5   | Chủ sở hữu + chỉnh sửa các cây khác trong thiết lập đa cây

\* Lưu ý rằng vai trò "Người đóng góp" hiện chỉ được hỗ trợ một phần; ví dụ, các đối tượng gia đình không thể được thêm vào vì chúng ngụ ý việc sửa đổi các đối tượng người Gramps cơ bản của các thành viên trong gia đình. Nên sử dụng các vai trò khác khi có thể.

## Cấu hình ai có thể sử dụng trò chuyện AI

Nếu bạn đã [cấu hình trò chuyện AI](chat.md), bạn sẽ thấy một tùy chọn ở đây để chọn nhóm người dùng nào được phép sử dụng tính năng trò chuyện.

## Quản lý người dùng

Có hai cách để quản lý người dùng:

- Với quyền sở hữu thông qua giao diện web
- Trên dòng lệnh trên máy chủ

Tài khoản chủ sở hữu cần thiết để truy cập lần đầu vào ứng dụng web có thể được thêm vào trong trình hướng dẫn onboarding được tự động khởi động khi truy cập Gramps Web với cơ sở dữ liệu người dùng trống.

### Quản lý người dùng trên dòng lệnh

Khi sử dụng [Docker Compose](deployment.md), lệnh cơ bản là

```bash
docker compose run grampsweb python3 -m gramps_webapi user COMMAND [ARGS]
```

`COMMAND` có thể là `add` hoặc `delete`. Sử dụng `--help` cho `[ARGS]` để hiển thị cú pháp và các tùy chọn cấu hình có thể.

### Phê duyệt người dùng tự đăng ký

Khi một người dùng tự đăng ký, họ sẽ không được cấp quyền truy cập ngay lập tức. Một email sẽ được gửi đến chủ sở hữu cây về việc đăng ký người dùng mới và người dùng sẽ nhận được một email yêu cầu xác nhận địa chỉ email của họ. Việc xác nhận địa chỉ email thành công sẽ thay đổi vai trò của họ từ `unconfirmed` thành `disabled`. Trong khi tài khoản người dùng ở một trong hai vai trò đó, người dùng không thể đăng nhập. Chủ sở hữu cây phải xem xét yêu cầu của người dùng và gán cho người dùng một vai trò phù hợp trước khi họ được phép đăng nhập.
