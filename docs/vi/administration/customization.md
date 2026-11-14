# Tùy chỉnh cây

Chủ sở hữu và quản trị viên cây có thể điều chỉnh tên và giao diện của cây, cũng như trang chính của nó, cho tất cả người dùng. Các cài đặt này nằm trong phần **Cài đặt cây** và **Tùy chỉnh** của [Cài đặt quản trị](settings.md).

## Tên cây gia đình

!!! note
    Việc đổi tên cây chỉ hoạt động trong một [cài đặt nhiều cây](../install_setup/multi-tree.md) hoặc khi `TREE_ID` được thiết lập rõ ràng trong [cấu hình máy chủ](../install_setup/configuration.md). Trong một cài đặt mặc định với một cây duy nhất mà không có `TREE_ID` được thiết lập, điều này sẽ gây ra lỗi.

Điều này cho phép thay đổi tên của cơ sở dữ liệu cây gia đình Gramps bên dưới. Nhập một tên mới và nhấp vào **Đổi tên** để áp dụng.

!!! tip
    Nếu bạn chỉ muốn thay đổi tên hiển thị trong thanh ứng dụng mà không đổi tên cơ sở dữ liệu, hãy sử dụng cài đặt [Tiêu đề ứng dụng](#app-title) thay thế.

## Thông tin nhà nghiên cứu

Đặt tên, địa chỉ và thông tin liên lạc của nhà nghiên cứu chính. Thông tin này được nhúng trong các tệp xuất (ví dụ: tệp GEDCOM).

## Màu chủ đề

Đặt một **màu chính** và **màu nhấn** tùy chỉnh cho giao diện Gramps Web. Những màu này được áp dụng cho tất cả người dùng của cây này và có hiệu lực ngay lập tức sau khi lưu.

Sử dụng bộ chọn màu để chọn màu, sau đó nhấp vào **Lưu**. Nhấp vào **Đặt lại** để quay lại các mặc định.

## Tiêu đề ứng dụng

Đặt một tiêu đề tùy chỉnh cho ứng dụng. Nếu được thiết lập, điều này sẽ ghi đè tên cây gia đình trong thanh tiêu đề trình duyệt và thanh ứng dụng ở trên cùng.

Nhập một tiêu đề và nhấp vào **Lưu**. Để trống để sử dụng mặc định (tên cây gia đình).

## Ghi chú trang chính

Chọn một đối tượng **Ghi chú** của Gramps để hiển thị trên trang chính bảng điều khiển. Nội dung ghi chú được hiển thị bên dưới các cột chính của bảng điều khiển và có thể nhìn thấy bởi tất cả người dùng có quyền truy cập vào cây.

Sử dụng bộ chọn đối tượng để tìm kiếm và chọn một ghi chú, sau đó lưu. Nhấp vào **Xóa** để xóa ghi chú trang chính hiện tại.

## Hình ảnh trang chính

Chọn một đối tượng **Media** của Gramps để hiển thị dưới dạng hình ảnh trên trang chính bảng điều khiển. Khi kết hợp với một ghi chú trang chính, hình ảnh xuất hiện bên cạnh văn bản ghi chú. Nếu không có ghi chú, chỉ hình ảnh được hiển thị.

Sử dụng bộ chọn đối tượng để tìm kiếm và chọn một đối tượng media, sau đó lưu. Nhấp vào **Xóa** để xóa hình ảnh trang chính hiện tại.

## Cài đặt Xuất/Nhập

Các cài đặt cấp cây (tiêu đề ứng dụng, màu chủ đề, ghi chú/hình ảnh trang chính, v.v.) có thể được xuất dưới dạng tệp JSON để sao lưu hoặc sao chép sang một phiên bản Gramps Web khác.

- Nhấp vào **Xuất cài đặt** để tải xuống các cài đặt hiện tại dưới dạng tệp JSON.
- Nhấp vào **Nhập cài đặt cây** để tải lên một tệp JSON đã xuất trước đó và áp dụng các cài đặt.
