# Quản lý Người dùng

Giao diện quản lý người dùng có thể truy cập qua **Cài đặt > Quản lý Người dùng** (biểu tượng người dùng trong thanh công cụ trên cùng). Nó chỉ khả dụng cho những người dùng có vai trò Chủ sở hữu hoặc Quản trị viên.

## Vai trò người dùng

Xem [Hệ thống người dùng](../install_setup/users.md) để biết mô tả đầy đủ về các vai trò người dùng có sẵn và quyền hạn của chúng.

## Xem và lọc người dùng

Trang quản lý người dùng hiển thị một bảng tất cả các tài khoản người dùng đã đăng ký với các cột sau:

- **Tên người dùng** – tên đăng nhập
- **Họ và tên** – tên hiển thị
- **E-mail** – địa chỉ e-mail của người dùng
- **Vai trò** – vai trò được chỉ định (Khách, Thành viên, Người đóng góp, Biên tập viên, Chủ sở hữu, hoặc Quản trị viên)
- **Nguồn tài khoản** – hoặc là "Mật khẩu" (tài khoản cục bộ) hoặc tên của một nhà cung cấp danh tính bên ngoài (ví dụ: khi sử dụng OIDC)

Sử dụng trường tìm kiếm và menu thả xuống vai trò ở đầu bảng để lọc danh sách. Nhấn nút xóa bộ lọc để đặt lại tất cả các bộ lọc.

## Chỉnh sửa một người dùng

Nhấn vào biểu tượng chỉnh sửa (bút chì) trên bất kỳ hàng nào để mở hộp thoại chỉnh sửa. Bạn có thể thay đổi:

- Họ và tên
- Địa chỉ e-mail
- Vai trò

Đây là cách chính để **kích hoạt một người dùng mới tự đăng ký**: thay đổi vai trò của họ từ *vô hiệu hóa* sang bất kỳ vai trò hoạt động nào (ví dụ: Thành viên hoặc Biên tập viên).

## Thêm người dùng thủ công

Nhấn vào biểu tượng **thêm người dùng** (thêm người) ở trên cùng bảng để tạo một tài khoản người dùng mới trực tiếp mà không cần yêu cầu tự đăng ký. Điền vào tên người dùng, họ và tên, địa chỉ e-mail, mật khẩu và vai trò trong hộp thoại và nhấn **Lưu**.

## Xóa một người dùng

Nhấn vào biểu tượng xóa (thùng rác) trên bất kỳ hàng nào và xác nhận trong hộp thoại. Hành động này không thể hoàn tác.

## Xuất và nhập tài khoản người dùng

Các nút này hữu ích khi [di chuyển đến một phiên bản Gramps Web khác](export.md).

- **Xuất chi tiết người dùng** (biểu tượng tải xuống) – tải xuống một tệp JSON chứa tất cả tài khoản người dùng (không có mật khẩu, vì mật khẩu được lưu trữ ở dạng mã hóa).
- **Nhập tài khoản người dùng** (biểu tượng nhóm-thêm) – tải lên một tệp JSON đã xuất trước đó để tạo tài khoản người dùng hàng loạt. Tất cả người dùng đã nhập sẽ cần đặt một mật khẩu mới qua liên kết "Quên mật khẩu", vì mật khẩu không thể được chuyển giao.

## Liên kết đăng ký (chỉ cấu hình đa cây)

Trong cấu hình đa cây, liên kết đăng ký cho người dùng mới được hiển thị ở đầu trang quản lý người dùng. Bạn có thể sao chép liên kết này và chia sẻ nó với những người bạn muốn mời đăng ký tài khoản trên cây của bạn.

!!! note
    Trong cấu hình đơn cây, có một liên kết "Đăng ký" chung trên trang đăng nhập; liên kết đăng ký theo cây chỉ cần thiết trong các cài đặt đa cây.

## Quyền truy cập trò chuyện AI

Nếu trò chuyện AI đã được kích hoạt trên máy chủ, một menu thả xuống ở đầu trang cho phép bạn kiểm soát các vai trò người dùng nào được phép sử dụng tính năng trò chuyện:

- Mọi người (bao gồm cả khách)
- Thành viên và cao hơn
- Người đóng góp và cao hơn
- Biên tập viên và cao hơn
- Chỉ Chủ sở hữu và quản trị viên
- Không ai (vô hiệu hóa trò chuyện cho tất cả người dùng)
