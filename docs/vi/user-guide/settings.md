# Cài đặt người dùng

Cài đặt người dùng có thể truy cập thông qua biểu tượng người dùng ở thanh ứng dụng trên cùng, sau đó chọn **Cài đặt người dùng**. Trang này được tổ chức thành các phần có thể thu gọn. Các thay đổi có hiệu lực ngay lập tức trừ khi có ghi chú khác.

!!! note
    Các thay đổi trong Cài đặt người dùng chỉ ảnh hưởng đến tài khoản của bạn. Các cài đặt ảnh hưởng đến tất cả người dùng của cây được quản lý trong [Cài đặt quản trị](../administration/settings.md).

## Tài khoản

Bao gồm thông tin hồ sơ của bạn, thông tin xác thực và bảo mật tài khoản.

### Thông tin người dùng

Hiển thị **tên người dùng** và **vai trò người dùng** hiện tại (ví dụ: Khách, Thành viên, Biên tập viên). Đây là thông tin chỉ đọc.

### Thay đổi e-mail

Nhập địa chỉ e-mail mới và nhấp vào **Gửi** để cập nhật địa chỉ liên kết với tài khoản của bạn. Địa chỉ e-mail được sử dụng để đặt lại mật khẩu và (nếu được cấu hình) thông báo.

### Thay đổi mật khẩu

Nhập mật khẩu hiện tại và một mật khẩu mới, sau đó nhấp vào **Gửi**. Nếu bạn quên mật khẩu hiện tại, hãy sử dụng liên kết **Quên mật khẩu** trên trang đăng nhập.

## Giao diện

Điều khiển các tùy chọn hiển thị được lưu trên thiết bị của bạn.

### Ngôn ngữ

Chọn ngôn ngữ cho giao diện Gramps Web. Cài đặt ngôn ngữ được lưu trong bộ nhớ cục bộ của trình duyệt và chỉ áp dụng cho thiết bị hiện tại.

### Chủ đề

Chọn giữa:

- **Hệ thống** – theo sở thích sáng/tối của hệ điều hành (mặc định)
- **Sáng** – luôn sử dụng chủ đề sáng
- **Tối** – luôn sử dụng chủ đề tối

Cài đặt chủ đề được lưu trong bộ nhớ cục bộ của trình duyệt.

### Tùy chọn cây gia đình

#### Chế độ xem cây gia đình mặc định

Đặt loại biểu đồ nào sẽ mở theo mặc định khi bạn điều hướng đến trang [Cây gia đình](tree.md). Các tùy chọn là Cây tổ tiên, Cây con cháu, Biểu đồ đồng hồ cát, Biểu đồ mối quan hệ và Biểu đồ quạt.

Tùy chọn này được lưu trong bộ nhớ cục bộ của trình duyệt.

## Công cụ phát triển

### Mã thông báo API

Sao chép mã thông báo phiên hiện tại của bạn vào clipboard. Mã thông báo có thể được sử dụng để xác thực trực tiếp với REST API, ví dụ trong giao diện Swagger tương tác được phục vụ bởi phiên bản Gramps Web của bạn tại `/api/swagger-ui`.

Nhấp vào **Khởi động Swagger** để mở giao diện Swagger trong một tab mới với phiên của bạn đã có sẵn.

!!! note
    Mã thông báo phiên có thời gian sống ngắn. Sao chép nó ngay lập tức trước khi sử dụng trong Swagger, vì nó có thể hết hạn.
