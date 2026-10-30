# Cài đặt người dùng

Cài đặt người dùng có thể truy cập thông qua biểu tượng người dùng ở thanh công cụ trên cùng, sau đó chọn **Cài đặt người dùng**. Trang này được tổ chức thành các phần có thể thu gọn. Các thay đổi có hiệu lực ngay lập tức trừ khi có ghi chú khác.

!!! note
    Các thay đổi trong Cài đặt người dùng chỉ ảnh hưởng đến tài khoản của bạn. Các cài đặt ảnh hưởng đến tất cả người dùng của cây được quản lý trong [Cài đặt quản trị](../administration/settings.md).

## Tài khoản

Bao gồm thông tin hồ sơ của bạn, thông tin xác thực và bảo mật tài khoản.

### Thông tin người dùng

Hiển thị **tên người dùng** và **vai trò người dùng** hiện tại của bạn (ví dụ: Khách, Thành viên, Biên tập viên). Đây là thông tin chỉ đọc.

### Thay đổi e-mail

Nhập địa chỉ e-mail mới và nhấp vào **Gửi** để cập nhật địa chỉ liên kết với tài khoản của bạn. Địa chỉ e-mail được sử dụng để đặt lại mật khẩu và (nếu được cấu hình) thông báo.

### Thay đổi mật khẩu

Nhập mật khẩu hiện tại của bạn và một mật khẩu mới, sau đó nhấp vào **Gửi**. Nếu bạn quên mật khẩu hiện tại, hãy sử dụng liên kết **Quên mật khẩu** trên trang đăng nhập.

### Phương thức đăng nhập liên kết

Nếu máy chủ của bạn cung cấp đăng nhập một lần (xem [xác thực OIDC](../install_setup/oidc.md)), bạn có thể liên kết một tài khoản từ nhà cung cấp, chẳng hạn như Google hoặc đăng nhập của tổ chức bạn, với tài khoản Gramps Web của bạn. Bạn có thể đăng nhập bằng nhà cung cấp đó và truy cập vào tài khoản hiện có của bạn, với vai trò và các chỉnh sửa của bạn. Phần này chỉ xuất hiện khi đăng nhập một lần được kích hoạt và máy chủ hỗ trợ liên kết (Gramps Web API 3.24 và các phiên bản sau).

Để liên kết một tài khoản, nhấp vào **Liên kết với** và tên nhà cung cấp, đăng nhập tại nhà cung cấp, và bạn sẽ được đưa trở lại cài đặt của mình. Nếu bạn chưa đăng nhập gần đây, bạn sẽ được yêu cầu đăng nhập lại trước.

Một tài khoản nhà cung cấp chỉ có thể được liên kết với một tài khoản Gramps Web. Nếu bạn thấy "Đăng nhập này đã được liên kết với một tài khoản khác", nó đã được liên kết ở nơi khác, chẳng hạn như với một tài khoản được tạo khi bạn lần đầu tiên đăng nhập với nhà cung cấp đó. Một quản trị viên có thể xóa tài khoản khác đó, sau đó bạn có thể liên kết nó với tài khoản của mình.

Để hủy liên kết một tài khoản, nhấp vào **Hủy liên kết**. Nếu đây là phương thức đăng nhập liên kết cuối cùng của bạn, bạn cũng cần nhập mật khẩu của mình, để bạn vẫn có thể đăng nhập sau đó. Nếu tài khoản của bạn được tạo thông qua đăng nhập một lần và bạn chưa bao giờ đặt mật khẩu, hãy sử dụng **Quên mật khẩu** trên trang đăng nhập để đặt một cái trước (điều này cần máy chủ gửi e-mail). Nếu máy chủ chỉ cho phép đăng nhập thông qua nhà cung cấp, tài khoản liên kết cuối cùng không thể bị hủy liên kết.

## Giao diện

Kiểm soát các tùy chọn hiển thị được lưu trên thiết bị của bạn.

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

Đặt loại biểu đồ nào sẽ mở theo mặc định khi bạn điều hướng đến trang [Cây gia đình](tree.md). Các tùy chọn là Cây tổ tiên, Cây hậu duệ, Biểu đồ đồng hồ cát, Biểu đồ mối quan hệ và Biểu đồ quạt.

Tùy chọn này được lưu trong bộ nhớ cục bộ của trình duyệt.

## Công cụ phát triển

### Mã thông báo API

Sao chép mã thông báo phiên hiện tại của bạn vào clipboard. Mã thông báo có thể được sử dụng để xác thực trực tiếp với REST API, chẳng hạn như trong Swagger UI tương tác được phục vụ bởi phiên bản Gramps Web của bạn tại `/api/swagger-ui`.

Nhấp vào **Mở Swagger** để mở Swagger UI trong một tab mới với phiên của bạn đã có sẵn.

!!! note
    Mã thông báo phiên có thời gian sống ngắn. Sao chép nó ngay lập tức trước khi sử dụng trong Swagger, vì nó có thể hết hạn.
