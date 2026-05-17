# Cài đặt Quản trị

Trang **Cài đặt > Quản trị** có thể truy cập thông qua biểu tượng người dùng ở thanh ứng dụng trên cùng. Nó chỉ có sẵn cho người dùng có vai trò Chủ sở hữu hoặc Quản trị viên và cung cấp các công cụ để quản lý cơ sở dữ liệu cây gia đình.

Trang được tổ chức thành các phần có thể thu gọn. Nhấp vào tiêu đề phần để mở rộng nó.

## Dữ liệu

Bao gồm hạn mức sử dụng, nhập dữ liệu và quản lý tệp phương tiện.

### Hạn mức sử dụng

Phần đầu của mục hiển thị mức sử dụng hiện tại so với bất kỳ giới hạn nào đã cấu hình:

- **Người** – số lượng đối tượng người trong cây so với tối đa đã cấu hình (∞ nếu không giới hạn)
- **Lưu trữ phương tiện** – tổng kích thước của các tệp phương tiện đã tải lên so với hạn mức lưu trữ đã cấu hình (∞ nếu không giới hạn)

Hạn mức được thiết lập bởi quản trị viên máy chủ; xem [Cấu hình máy chủ](../install_setup/configuration.md) để biết chi tiết.

### Nhập dữ liệu

Phần nhập cho phép bạn tải lên một tệp cây gia đình hoặc một kho lưu trữ phương tiện. Xem [Nhập dữ liệu](import.md) để biết hướng dẫn đầy đủ.

### Tình trạng tệp phương tiện

Phần này hiển thị:

- Tổng số đối tượng phương tiện trong cây và liệu có đối tượng nào thiếu mã kiểm tra
- Số lượng đối tượng phương tiện mà tệp liên quan bị thiếu trên máy chủ

Một dấu kiểm màu xanh lá cây cho biết mọi thứ đều ổn. Nếu phát hiện vấn đề, các liên kết đến các đối tượng bị ảnh hưởng sẽ được hiển thị. Các mã kiểm tra bị thiếu thường xảy ra khi dữ liệu được nhập từ định dạng như GEDCOM mà bao gồm tham chiếu phương tiện nhưng không có các tệp thực tế. Các tệp bị thiếu có thể được tải lên thông qua tính năng nhập kho lưu trữ phương tiện.

### Nhập kho lưu trữ phương tiện

Cho phép tải lên một tệp ZIP của các tệp phương tiện để bổ sung các tệp bị thiếu. Xem [Nhập dữ liệu](import.md) để biết hướng dẫn đầy đủ.

## Chỉ mục tìm kiếm

### Quản lý chỉ mục tìm kiếm

Gramps Web duy trì một chỉ mục tìm kiếm toàn văn mà thường được cập nhật tự động mỗi khi dữ liệu thay đổi. Chỉ báo trạng thái cho biết có bao nhiêu đối tượng hiện đang được lập chỉ mục so với tổng số đối tượng.

Nhấp vào **Cập nhật chỉ mục tìm kiếm** để kích hoạt việc xây dựng lại toàn bộ. Một chỉ báo tiến trình sẽ được hiển thị trong khi tác vụ chạy ở chế độ nền. Điều này thường chỉ cần thiết sau khi nâng cấp máy chủ.

### Chỉ mục tìm kiếm ngữ nghĩa

Nếu máy chủ đã [bật tìm kiếm ngữ nghĩa (sử dụng AI)](../install_setup/configuration.md), một phần bổ sung sẽ xuất hiện với hai hành động:

- **Tái tạo chỉ mục tìm kiếm ngữ nghĩa** – xây dựng lại toàn bộ chỉ mục ngữ nghĩa từ đầu. Điều này tốn kém về tính toán và có thể mất nhiều thời gian.
- **Cập nhật chỉ mục tìm kiếm ngữ nghĩa** – thực hiện một cập nhật gia tăng, chỉ thêm các đối tượng chưa được lập chỉ mục. Nhanh hơn so với việc xây dựng lại toàn bộ.

## Cài đặt cây

### Tên Cây Gia Đình

!!! note
    Việc đổi tên cây chỉ hoạt động trong một [cài đặt nhiều cây](../install_setup/multi-tree.md) hoặc khi `TREE_ID` được thiết lập rõ ràng trong [cấu hình máy chủ](../install_setup/configuration.md). Trên một cài đặt mặc định với một cây duy nhất mà không có `TREE_ID` được thiết lập, điều này sẽ gây ra lỗi.

Điều này cho phép thay đổi tên của cơ sở dữ liệu cây gia đình Gramps bên dưới. Nhập một tên mới và nhấp vào **Đổi tên** để áp dụng.

!!! tip
    Nếu bạn chỉ muốn thay đổi tên hiển thị trong thanh ứng dụng mà không đổi tên cơ sở dữ liệu, hãy sử dụng cài đặt [Tiêu đề ứng dụng](#app-title) thay thế.

### Thông tin Nhà nghiên cứu

Thiết lập tên, địa chỉ và thông tin liên lạc của nhà nghiên cứu chính. Thông tin này được nhúng trong các xuất khẩu (ví dụ: tệp GEDCOM).

## Tùy chỉnh

### Màu sắc chủ đề

Thiết lập một **màu chính** và **màu nhấn** tùy chỉnh cho giao diện Gramps Web. Những màu này được áp dụng cho tất cả người dùng của cây này và có hiệu lực ngay lập tức sau khi lưu.

Sử dụng bộ chọn màu để chọn màu, sau đó nhấp vào **Lưu**. Nhấp vào **Đặt lại** để quay lại mặc định.

### Tiêu đề ứng dụng

Thiết lập một tiêu đề tùy chỉnh cho ứng dụng. Nếu được thiết lập, điều này sẽ ghi đè tên cây gia đình trong thanh tiêu đề trình duyệt và thanh ứng dụng trên cùng.

Nhập một tiêu đề và nhấp vào **Lưu**. Để trống để sử dụng mặc định (tên cây gia đình).

### Ghi chú trang chính

Chọn một đối tượng **Ghi chú** của Gramps để hiển thị trên trang chính của bảng điều khiển. Nội dung ghi chú được hiển thị bên dưới các cột chính của bảng điều khiển và có thể nhìn thấy bởi tất cả người dùng có quyền truy cập vào cây.

Sử dụng bộ chọn đối tượng để tìm kiếm và chọn một ghi chú, sau đó lưu. Nhấp vào **Xóa** để xóa ghi chú trang chính hiện tại.

### Hình ảnh trang chính

Chọn một đối tượng **Phương tiện** của Gramps để hiển thị dưới dạng hình ảnh trên trang chính của bảng điều khiển. Khi kết hợp với một ghi chú trang chính, hình ảnh sẽ xuất hiện bên cạnh văn bản ghi chú. Nếu không có ghi chú, chỉ hình ảnh sẽ được hiển thị.

Sử dụng bộ chọn đối tượng để tìm kiếm và chọn một đối tượng phương tiện, sau đó lưu. Nhấp vào **Xóa** để xóa hình ảnh trang chính hiện tại.

### Cài đặt Xuất/Nhập

Các cài đặt cấp cây (tiêu đề ứng dụng, màu sắc chủ đề, ghi chú/hình ảnh trang chính, v.v.) có thể được xuất dưới dạng tệp JSON để sao lưu hoặc sao chép sang một phiên bản Gramps Web khác.

- Nhấp vào **Xuất cài đặt** để tải xuống các cài đặt hiện tại dưới dạng tệp JSON.
- Nhấp vào **Nhập cài đặt cây** để tải lên một tệp JSON đã xuất trước đó và áp dụng các cài đặt.

## Xử lý Cây Gia Đình

### Kiểm tra và Sửa chữa Cơ sở dữ liệu

Công cụ này kiểm tra cơ sở dữ liệu Gramps để tìm các bất thường nội bộ và sửa chữa những bất thường mà nó có thể – tương tự như công cụ [Kiểm tra và Sửa chữa Cơ sở dữ liệu](https://www.gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Tools#Check_and_Repair_Database) trong Gramps Desktop.

Nhấp vào **Kiểm tra và Sửa chữa** và chờ chỉ báo tiến trình hoàn tất. Kết quả sẽ được hiển thị bên dưới nút:

- Nếu không tìm thấy lỗi, một thông báo xác nhận sẽ được hiển thị.
- Nếu tìm thấy lỗi, một tóm tắt về các sửa chữa đã áp dụng sẽ được hiển thị.

Chạy công cụ này nếu bạn gặp phải các lỗi hoặc hành vi không mong muốn có thể do các bất thường trong cơ sở dữ liệu, chẳng hạn như các mối quan hệ giữa các đối tượng bị thiếu.

## Khu vực Nguy hiểm

!!! danger
    Các hành động trong Khu vực Nguy hiểm là **không thể đảo ngược**. Hãy sao lưu trước khi tiếp tục.

### Xóa tất cả đối tượng

Xóa các đối tượng khỏi cây gia đình. Nhấp vào **Xóa** sẽ mở một hộp thoại nơi bạn có thể chọn để xóa:

- **Tất cả đối tượng** – xóa hoàn toàn cây
- **Các loại đối tượng cụ thể** – ví dụ, chỉ các sự kiện hoặc chỉ các đối tượng phương tiện

Bạn sẽ được yêu cầu xác thực lại (đăng nhập lại) để xác nhận hành động. Việc xóa sẽ chạy như một tác vụ nền và một chỉ báo tiến trình sẽ được hiển thị.

!!! warning
    Việc xóa chỉ một tập hợp con của các loại đối tượng (thay vì tất cả đối tượng cùng một lúc) có thể mất rất nhiều thời gian cho các cây lớn, vì máy chủ phải kiểm tra và cập nhật tất cả các mối quan hệ giữa các đối tượng.

!!! tip
    Sử dụng điều này để bắt đầu lại trước khi nhập một cây mới, hoặc để xóa các loại đối tượng cụ thể đã được nhập không chính xác.
