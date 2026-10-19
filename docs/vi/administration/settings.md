# Cài đặt Quản trị

Trang **Cài đặt > Quản trị** có thể truy cập qua biểu tượng người dùng ở thanh công cụ trên cùng. Nó chỉ có sẵn cho người dùng có vai trò Chủ sở hữu hoặc Quản trị viên và cung cấp các công cụ để quản lý cơ sở dữ liệu cây gia đình.

Trang này được tổ chức thành các phần có thể thu gọn. Nhấn vào tiêu đề phần để mở rộng nó.

## Dữ liệu

Bao gồm hạn mức sử dụng, nhập dữ liệu và quản lý tệp phương tiện.

### Hạn mức sử dụng

Phần đầu của mục này hiển thị mức sử dụng hiện tại so với bất kỳ giới hạn nào đã được cấu hình:

- **Người** – số lượng đối tượng cá nhân trong cây so với giới hạn tối đa đã cấu hình (∞ nếu không giới hạn)
- **Lưu trữ phương tiện** – tổng kích thước của các tệp phương tiện đã tải lên so với hạn mức lưu trữ đã cấu hình (∞ nếu không giới hạn)

Hạn mức được thiết lập bởi quản trị viên máy chủ; xem [Cấu hình máy chủ](../install_setup/configuration.md) để biết thêm chi tiết.

### Nhập dữ liệu

Phần nhập cho phép bạn tải lên một tệp cây gia đình hoặc một kho lưu trữ phương tiện. Xem [Nhập dữ liệu](import.md) để biết hướng dẫn đầy đủ.

### Tình trạng tệp phương tiện

Phần này hiển thị:

- Tổng số đối tượng phương tiện trong cây và liệu có đối tượng nào thiếu mã kiểm tra
- Số lượng đối tượng phương tiện mà tệp liên quan bị thiếu trên máy chủ

Một dấu kiểm màu xanh lá cây cho biết mọi thứ đều ổn. Nếu phát hiện vấn đề, các liên kết đến các đối tượng bị ảnh hưởng sẽ được hiển thị. Các mã kiểm tra bị thiếu thường xảy ra khi dữ liệu được nhập từ một định dạng như GEDCOM bao gồm các tham chiếu phương tiện nhưng không có các tệp thực tế. Các tệp bị thiếu có thể được tải lên thông qua tính năng nhập kho lưu trữ phương tiện.

### Nhập kho lưu trữ phương tiện

Cho phép tải lên một tệp ZIP chứa các tệp phương tiện để bổ sung các tệp bị thiếu. Xem [Nhập dữ liệu](import.md) để biết hướng dẫn đầy đủ.

## Chỉ mục tìm kiếm

### Quản lý chỉ mục tìm kiếm

Gramps Web duy trì một chỉ mục tìm kiếm toàn văn mà thường được cập nhật tự động mỗi khi dữ liệu thay đổi. Chỉ báo trạng thái cho biết có bao nhiêu đối tượng hiện đang được lập chỉ mục so với tổng số đối tượng.

Nhấn **Cập nhật chỉ mục tìm kiếm** để kích hoạt việc xây dựng lại toàn bộ. Một chỉ báo tiến trình sẽ được hiển thị trong khi tác vụ chạy ở chế độ nền. Điều này thường chỉ cần thiết sau khi nâng cấp máy chủ.

### Chỉ mục tìm kiếm ngữ nghĩa

!!! warning "Đã ngừng sử dụng"
    Tìm kiếm ngữ nghĩa đã bị ngừng sử dụng và sẽ bị xóa trong Gramps Web API 3.25, cùng với phần này. AI chat không cần nó vì Gramps Web API 3.24.

Nếu máy chủ đã [bật tìm kiếm ngữ nghĩa (được hỗ trợ bởi AI)](../install_setup/chat.md#semantic-search-deprecated), một phần bổ sung sẽ xuất hiện với hai hành động:

- **Tái tạo chỉ mục tìm kiếm ngữ nghĩa** – xây dựng lại toàn bộ chỉ mục ngữ nghĩa từ đầu. Điều này tốn kém về tính toán và có thể mất nhiều thời gian.
- **Cập nhật chỉ mục tìm kiếm ngữ nghĩa** – thực hiện một cập nhật gia tăng, chỉ thêm các đối tượng chưa được lập chỉ mục. Nhanh hơn so với việc xây dựng lại toàn bộ.

## Cài đặt cây

### Tên Cây Gia Đình

!!! note
    Việc đổi tên cây chỉ hoạt động trong một [cài đặt nhiều cây](../install_setup/multi-tree.md) hoặc khi `TREE_ID` được thiết lập rõ ràng trong [cấu hình máy chủ](../install_setup/configuration.md). Trong một cài đặt mặc định với một cây đơn mà không có `TREE_ID` được thiết lập, điều này sẽ gây ra lỗi.

Điều này cho phép thay đổi tên của cơ sở dữ liệu cây gia đình Gramps. Nhập một tên mới và nhấn **Đổi tên** để áp dụng.

!!! tip
    Nếu bạn chỉ muốn thay đổi tên hiển thị trong thanh công cụ mà không đổi tên cơ sở dữ liệu, hãy sử dụng cài đặt [Tiêu đề ứng dụng](#app-title) thay thế.

### Thông tin Nhà Nghiên Cứu

Thiết lập tên, địa chỉ và thông tin liên lạc của nhà nghiên cứu chính. Thông tin này được nhúng trong các xuất khẩu (ví dụ: tệp GEDCOM).

## Tùy chỉnh

### Màu sắc chủ đề

Thiết lập một **màu chính** và **màu nhấn** tùy chỉnh cho giao diện Gramps Web. Những màu sắc này được áp dụng cho tất cả người dùng của cây này và có hiệu lực ngay lập tức sau khi lưu.

Sử dụng bộ chọn màu để chọn màu, sau đó nhấn **Lưu**. Nhấn **Đặt lại** để quay lại mặc định.

### Tiêu đề ứng dụng

Thiết lập một tiêu đề tùy chỉnh cho ứng dụng. Nếu được thiết lập, điều này sẽ ghi đè tên cây gia đình trong thanh tiêu đề trình duyệt và thanh công cụ trên cùng.

Nhập một tiêu đề và nhấn **Lưu**. Để trống để sử dụng mặc định (tên cây gia đình).

### Ghi chú trang chính

Chọn một đối tượng **Ghi chú** của Gramps để hiển thị trên trang chính của bảng điều khiển. Nội dung ghi chú được hiển thị bên dưới các cột chính của bảng điều khiển và có thể nhìn thấy bởi tất cả người dùng có quyền truy cập vào cây.

Sử dụng bộ chọn đối tượng để tìm kiếm và chọn một ghi chú, sau đó lưu. Nhấn **Xóa** để xóa ghi chú trang chính hiện tại.

### Hình ảnh trang chính

Chọn một đối tượng **Phương tiện** của Gramps để hiển thị dưới dạng hình ảnh trên trang chính của bảng điều khiển. Khi kết hợp với một ghi chú trang chính, hình ảnh sẽ xuất hiện bên cạnh văn bản ghi chú. Nếu không có ghi chú, chỉ hình ảnh sẽ được hiển thị.

Sử dụng bộ chọn đối tượng để tìm kiếm và chọn một đối tượng phương tiện, sau đó lưu. Nhấn **Xóa** để xóa hình ảnh trang chính hiện tại.

### Cài đặt Xuất/Nhập

Các cài đặt cấp cây (tiêu đề ứng dụng, màu sắc chủ đề, ghi chú/hình ảnh trang chính, v.v.) có thể được xuất dưới dạng tệp JSON để sao lưu hoặc sao chép sang một phiên bản Gramps Web khác.

- Nhấn **Xuất cài đặt** để tải xuống các cài đặt hiện tại dưới dạng tệp JSON.
- Nhấn **Nhập cài đặt cây** để tải lên một tệp JSON đã xuất trước đó và áp dụng các cài đặt.

## Xử lý Cây Gia Đình

### Kiểm tra và Sửa chữa Cơ sở Dữ liệu

Công cụ này kiểm tra cơ sở dữ liệu Gramps để tìm các bất thường nội bộ và sửa chữa những bất thường mà nó có thể – tương tự như công cụ [Kiểm tra và Sửa chữa Cơ sở Dữ liệu](https://www.gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Tools#Check_and_Repair_Database) trong Gramps Desktop.

Nhấn **Kiểm tra và Sửa chữa** và chờ cho chỉ báo tiến trình hoàn thành. Kết quả sẽ được hiển thị bên dưới nút:

- Nếu không tìm thấy lỗi, một thông báo xác nhận sẽ được hiển thị.
- Nếu tìm thấy lỗi, một tóm tắt về các sửa chữa đã áp dụng sẽ được hiển thị.

Chạy công cụ này nếu bạn gặp phải lỗi hoặc hành vi bất ngờ có thể do các bất thường trong cơ sở dữ liệu, chẳng hạn như thiếu các mối quan hệ giữa các đối tượng.

### Xác minh Dữ liệu

Trong khi [Kiểm tra và Sửa chữa Cơ sở Dữ liệu](#check-and-repair-database) tìm kiếm các bất thường *kỹ thuật*, công cụ này tìm kiếm dữ liệu *không hợp lý* – tương tự như công cụ [Xác minh Dữ liệu](https://gramps-project.org/wiki/index.php/Gramps_5.0_Wiki_Manual_-_Tools#Verify_the_Data) trong Gramps Desktop. Nó báo cáo những điều không phải là không thể nhưng không đủ khả năng để đáng để xem xét lại, chẳng hạn như một người mẹ 12 tuổi hoặc một người sống đến 130 tuổi.

Dưới **Tùy chọn**, bạn có thể điều chỉnh các ngưỡng mà các bài kiểm tra sử dụng – độ tuổi tối đa, độ tuổi tối thiểu và tối đa để kết hôn hoặc có con, số lượng con tối đa, và nhiều hơn nữa – cũng như liệu có ước lượng các ngày tháng bị thiếu hoặc không chính xác và liệu có báo cáo các ngày tháng không hợp lệ như 31 tháng 2 hay không.

Nhấn **Xác minh Dữ liệu** để bắt đầu. Kiểm tra sẽ chạy như một tác vụ nền, và các phát hiện sau đó sẽ được liệt kê dưới **Kết quả Xác minh Dữ liệu**. Công cụ này không thay đổi gì: nó chỉ báo cáo những gì nó tìm thấy.

!!! note
    Một phát hiện không phải là bằng chứng của một lỗi. Những cuộc sống dài và khoảng cách tuổi tác lớn thực sự xảy ra, vì vậy hãy coi kết quả như một danh sách những điều cần kiểm tra hơn là một danh sách những điều cần sửa chữa.

## Thẻ

### Quản lý thẻ

Tạo, đổi tên, thay đổi màu sắc và xóa [thẻ](../user-guide/tags.md) cho cây gia đình. Các thẻ được lưu trữ trong cơ sở dữ liệu Gramps, chia sẻ giữa tất cả người dùng và hoàn toàn tương thích với Gramps Desktop.

Nhấn **Thẻ Mới** để tạo một thẻ. Sử dụng các điều khiển bên cạnh một thẻ hiện có để đổi tên (biểu tượng bút chì), thay đổi màu sắc (bộ chọn màu), hoặc xóa nó (biểu tượng xóa).

!!! note
    Việc xóa một thẻ sẽ xóa nó khỏi tất cả các đối tượng mà nó đã được áp dụng.

Xem [Thẻ](../user-guide/tags.md) để biết cách các thẻ được sử dụng trong toàn bộ Gramps Web, bao gồm các thẻ đặc biệt `Blog` và `ToDo`.

## Khu vực Nguy hiểm

!!! danger
    Các hành động trong Khu vực Nguy hiểm là **không thể đảo ngược**. Hãy sao lưu trước khi tiếp tục.

### Xóa tất cả đối tượng

Xóa các đối tượng khỏi cây gia đình. Nhấn **Xóa** sẽ mở một hộp thoại nơi bạn có thể chọn xóa:

- **Tất cả đối tượng** – hoàn toàn xóa sạch cây
- **Các loại đối tượng cụ thể** – ví dụ, chỉ sự kiện hoặc chỉ các đối tượng phương tiện

Bạn sẽ được yêu cầu xác thực lại (đăng nhập lại) để xác nhận hành động. Việc xóa sẽ chạy như một tác vụ nền và một chỉ báo tiến trình sẽ được hiển thị.

!!! warning
    Việc xóa chỉ một tập hợp con của các loại đối tượng (thay vì tất cả đối tượng cùng một lúc) có thể mất rất nhiều thời gian đối với các cây lớn, vì máy chủ phải kiểm tra và cập nhật tất cả các mối quan hệ giữa các đối tượng.

!!! tip
    Sử dụng điều này để bắt đầu lại trước khi nhập một cây mới, hoặc để xóa các loại đối tượng cụ thể đã được nhập không chính xác.

### Khôi phục từ Sao lưu

Đặt lại cây để khớp với tệp sao lưu Gramps XML (`.gramps`) đã tải lên, thêm, cập nhật và xóa các đối tượng khi cần thiết để cây cuối cùng giống hệt như sao lưu.

!!! danger
    Đây là một thay thế phá hủy, không phải là một hợp nhất. Bất kỳ đối tượng hiện có nào không có trong sao lưu đã tải lên sẽ bị xóa.

Tải lên một tệp `.gramps`, sau đó nhấn **Xem trước Khôi phục**. Bạn sẽ được yêu cầu xác thực lại nếu phiên của bạn không đủ mới. Một bản xem trước sẽ chạy như một tác vụ nền và, khi hoàn tất, sẽ mở một hộp thoại tóm tắt các thay đổi theo loại đối tượng (người, gia đình, sự kiện, địa điểm, trích dẫn, nguồn, kho, đối tượng phương tiện, ghi chú, thẻ):

- **Thêm** – các đối tượng có trong sao lưu nhưng thiếu trong cây hiện tại
- **Cập nhật** – các đối tượng có trong cả hai nhưng khác nhau
- **Xóa** – các đối tượng trong cây hiện tại mà không có trong sao lưu
- **Không thay đổi** – các đối tượng giống hệt nhau trong cả hai

Nếu có bất kỳ đối tượng nào sẽ bị xóa, hộp thoại sẽ cảnh báo số lượng. Xem xét tóm tắt, sau đó nhấn **Khôi phục** để áp dụng các thay đổi, hoặc **Hủy** để hủy bỏ.

!!! note
    Chỉ dữ liệu đối tượng và các tham chiếu phương tiện được khôi phục. Các tệp phương tiện nhị phân và siêu dữ liệu cây (người mặc định, dấu trang, nhóm tên) không bị ảnh hưởng. Khôi phục các tệp phương tiện bị thiếu riêng biệt thông qua [Nhập kho lưu trữ phương tiện](#import-media-archive) nếu cần.

!!! tip
    Sử dụng điều này để quay lại một cây về một bản sao lưu Gramps XML đã biết tốt, chẳng hạn như sau khi nhập sai hoặc chỉnh sửa hàng loạt không mong muốn.
