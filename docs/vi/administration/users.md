# Quản lý Người dùng

Giao diện quản lý người dùng có thể truy cập qua **Cài đặt > Quản lý Người dùng** (biểu tượng người dùng trên thanh ứng dụng ở trên cùng). Nó chỉ có sẵn cho những người dùng có vai trò Chủ sở hữu hoặc Quản trị viên.

## Vai trò người dùng

Xem [Hệ thống người dùng](../install_setup/users.md) để biết mô tả đầy đủ về các vai trò người dùng có sẵn và quyền của họ.

## Xem và lọc người dùng

Trang quản lý người dùng hiển thị bảng tất cả các tài khoản người dùng đã đăng ký với các cột sau:

- **Tên người dùng** – tên đăng nhập
- **Họ và tên** – tên hiển thị
- **E-mail** – địa chỉ e-mail của người dùng
- **Vai trò** – vai trò được chỉ định (Khách, Thành viên, Người đóng góp, Biên tập viên, Chủ sở hữu hoặc Quản trị viên)
- **Nguồn tài khoản** – có thể là "Mật khẩu" (tài khoản cục bộ) hoặc tên của một nhà cung cấp danh tính bên ngoài (ví dụ: khi sử dụng OIDC)

Sử dụng trường tìm kiếm và menu thả xuống vai trò ở đầu bảng để lọc danh sách. Nhấp vào nút xóa bộ lọc để đặt lại tất cả các bộ lọc.

## Chỉnh sửa người dùng

Nhấp vào biểu tượng chỉnh sửa (bút chì) trên bất kỳ hàng nào để mở hộp thoại chỉnh sửa. Bạn có thể thay đổi:

- Họ và tên
- Địa chỉ e-mail
- Vai trò

Đây là cách chính để **kích hoạt một người dùng mới tự đăng ký**: thay đổi vai trò của họ từ *vô hiệu hóa* sang bất kỳ vai trò hoạt động nào (ví dụ: Thành viên hoặc Biên tập viên).

Địa chỉ e-mail không cần phải duy nhất (kể từ Gramps Web API 3.22), vì vậy nhiều tài khoản có thể chia sẻ cùng một địa chỉ.

## Thêm người dùng thủ công

Nhấp vào biểu tượng **thêm người dùng** (thêm người) ở trên bảng để tạo một tài khoản người dùng mới trực tiếp mà không cần yêu cầu tự đăng ký. Điền vào tên người dùng, họ và tên, địa chỉ e-mail, mật khẩu và vai trò trong hộp thoại và nhấp vào **Lưu**.

## Xóa người dùng

Nhấp vào biểu tượng xóa (thùng rác) trên bất kỳ hàng nào và xác nhận trong hộp thoại. Hành động này không thể hoàn tác.

!!! note
    Để ngăn một cây không có ai có thể quản lý nó, bạn không thể hạ vai trò của mình xuống dưới Chủ sở hữu hoặc xóa tài khoản của chính mình nếu bạn là Chủ sở hữu hoặc Quản trị viên duy nhất của cây. Hãy nâng cấp một người dùng khác lên Chủ sở hữu trước. Một quản trị viên vẫn có thể thay đổi hoặc xóa Chủ sở hữu cuối cùng của cây của người dùng khác, vì họ có thể bổ nhiệm một người mới.

## Xuất và nhập tài khoản người dùng

Các nút này hữu ích khi [di chuyển sang một phiên bản Gramps Web khác](export.md).

- **Xuất chi tiết người dùng** (biểu tượng tải xuống) – tải xuống một tệp JSON chứa tất cả các tài khoản người dùng (không có mật khẩu, vì mật khẩu được lưu trữ dưới dạng mã hóa).
- **Nhập tài khoản người dùng** (biểu tượng nhóm-thêm) – tải lên một tệp JSON đã xuất trước đó để tạo tài khoản người dùng hàng loạt. Tất cả người dùng được nhập sẽ cần thiết lập mật khẩu mới qua liên kết "Quên mật khẩu", vì mật khẩu không thể được chuyển giao.

## Liên kết đăng ký (chỉ thiết lập đa cây)

Trong một thiết lập đa cây, liên kết đăng ký cho người dùng mới được hiển thị ở đầu trang quản lý người dùng. Bạn có thể sao chép liên kết này và chia sẻ với những người mà bạn muốn mời đăng ký tài khoản trên cây của bạn.

!!! note
    Trong một thiết lập đơn cây, có một liên kết "Đăng ký" chung trên trang đăng nhập; liên kết đăng ký theo cây chỉ cần thiết trong các cài đặt đa cây.

## Quyền truy cập trò chuyện AI

Nếu trò chuyện AI đã được kích hoạt trên máy chủ, một menu thả xuống ở đầu trang cho phép bạn kiểm soát các vai trò người dùng nào được phép sử dụng tính năng trò chuyện:

- Mọi người (bao gồm cả khách)
- Thành viên và cao hơn
- Người đóng góp và cao hơn
- Biên tập viên và cao hơn
- Chỉ Chủ sở hữu và quản trị viên
- Không ai (vô hiệu hóa trò chuyện cho tất cả người dùng)
