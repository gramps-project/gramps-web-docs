# Sao lưu và khôi phục

Chủ sở hữu cây gia đình có thể tạo, tải xuống và khôi phục các bản sao lưu của cây trong phần **Sao lưu** của [Cài đặt quản trị](settings.md).

Một bản sao lưu chứa dữ liệu cây gia đình, bao gồm các hồ sơ riêng tư, cài đặt cây và người dùng của cây. Các tệp phương tiện không được bao gồm; xem [Sao lưu các tệp phương tiện của bạn](export.md#back-up-your-media-files).

## Các bản sao lưu đã lưu

Nếu quản trị viên máy chủ đã thiết lập một thư mục sao lưu (`BACKUP_DIR`, xem [Cấu hình máy chủ](../install_setup/configuration.md)), các bản sao lưu có thể được lưu trữ trên máy chủ. Nếu không, phần này sẽ hiển thị một thông báo rằng việc lưu trữ các bản sao lưu chưa được cấu hình, và chỉ có thể khôi phục từ một tệp đã tải lên.

Nhấp vào **Tạo bản sao lưu...** để tạo một bản sao lưu. Nó được tạo ra như một tác vụ nền và sau đó xuất hiện trong danh sách các bản sao lưu đã lưu, với ngày, số lượng người và kích thước của nó. Máy chủ chỉ giữ lại các bản sao lưu mới nhất (mặc định là năm) và tự động xóa các bản cũ hơn. Số lượng bản sao lưu có thể được tạo mỗi ngày cũng bị giới hạn.

Đối với mỗi bản sao lưu đã lưu, bạn có thể:

- **Tải xuống** nó dưới dạng tệp `.tar`, ví dụ để giữ một bản sao ở nơi khác.
- **Khôi phục** nó, như mô tả bên dưới.
- **Xóa** nó, sau khi xác nhận.

Một bản sao lưu được thực hiện với phiên bản Gramps Web mới hơn phiên bản đang chạy trên máy chủ sẽ được đánh dấu bằng biểu tượng cảnh báo và không thể được khôi phục.

## Khôi phục từ Bản sao lưu

Khôi phục cây từ một bản sao lưu đã lưu hoặc từ một tệp đã tải lên. Để khôi phục một bản sao lưu đã lưu, nhấp vào nút khôi phục bên cạnh nó. Để khôi phục từ một tệp, chọn một bản sao lưu Gramps Web (`.tar`) hoặc một tệp XML Gramps (`.gramps`) và nhấp vào **Khôi phục**.

!!! danger
    Khôi phục dữ liệu là một thay thế phá hủy, không phải là một hợp nhất. Bất kỳ đối tượng nào hiện có không có trong bản sao lưu sẽ bị xóa.

Đối với một bản sao lưu Gramps Web, một hộp thoại sẽ hiển thị khi bản sao lưu được thực hiện, cho cây nào và với phiên bản nào, và cho phép bạn chọn các phần nào để khôi phục:

- **Dữ liệu** – các đối tượng của cây gia đình
- **Cài đặt cây** – các cài đặt của trang Quản trị, chẳng hạn như màu sắc chủ đề, tiêu đề ứng dụng và ghi chú trang chủ
- **Người dùng** – các người dùng của cây

Nhấp vào **Xem trước** để xem những gì sẽ thay đổi khi khôi phục. Một tệp XML Gramps chỉ chứa dữ liệu, vì vậy đối với một tệp như vậy, việc xem trước bắt đầu ngay lập tức. Bạn sẽ được yêu cầu xác thực lại nếu phiên của bạn không đủ mới. Việc xem trước chạy như một tác vụ nền và, khi hoàn tất, mở một hộp thoại tóm tắt các thay đổi theo loại đối tượng (người, gia đình, sự kiện, địa điểm, trích dẫn, nguồn, kho, đối tượng phương tiện, ghi chú, thẻ), và cho các cài đặt cây và người dùng nếu được chọn:

- **Thêm** – các đối tượng có trong bản sao lưu nhưng thiếu trong cây hiện tại
- **Cập nhật** – các đối tượng có trong cả hai nhưng khác nhau
- **Xóa** – các đối tượng trong cây hiện tại mà không có trong bản sao lưu
- **Không thay đổi** – các đối tượng giống hệt nhau trong cả hai

Nếu có bất kỳ đối tượng nào sẽ bị xóa, hộp thoại sẽ cảnh báo số lượng. Xem lại tóm tắt, sau đó nhấp vào **Khôi phục** để áp dụng các thay đổi, hoặc **Hủy** để hủy bỏ.

Sau khi khôi phục, các người dùng được thêm từ bản sao lưu sẽ được liệt kê. Họ nhận được một mật khẩu ngẫu nhiên, vì vậy họ phải đặt lại mật khẩu của mình trước khi có thể đăng nhập. Các người dùng đã tồn tại trên máy chủ sẽ không bao giờ bị thay đổi. Các đối tượng phương tiện mà tệp của chúng bị thiếu trên máy chủ cũng sẽ được liệt kê; tải lên chúng qua [Nhập các tệp phương tiện](import-media.md).

!!! note
    Việc khôi phục dữ liệu chỉ khôi phục dữ liệu đối tượng và tham chiếu phương tiện. Các tệp phương tiện nhị phân và siêu dữ liệu cây (người mặc định, đánh dấu, nhóm tên) không bị ảnh hưởng.

!!! tip
    Sử dụng điều này để quay lại một cây về một bản sao lưu đã biết tốt, chẳng hạn như sau một lần nhập sai hoặc một chỉnh sửa hàng loạt không mong muốn.

## Gramps XML như một bản sao lưu

Nếu việc lưu trữ các bản sao lưu không khả dụng, hoặc bạn chỉ muốn giữ một bản sao của dữ liệu cây gia đình, [xuất](export.md) cây dưới dạng Gramps XML. Một tệp như vậy cũng có thể được khôi phục qua [Khôi phục từ Bản sao lưu](#restore-from-backup).

Lưu ý rằng nếu người dùng Gramps Web của bạn không có quyền xem các hồ sơ riêng tư, việc xuất sẽ không phải là một bản sao lưu đầy đủ, vì nó sẽ không chứa bất kỳ hồ sơ riêng tư nào.
