# Sử dụng quản lý tác vụ tích hợp sẵn

Gramps Web chứa một công cụ quản lý tác vụ genealogi tích hợp sẵn. Nó nhằm mục đích cho phép các nhà nghiên cứu lập kế hoạch và ưu tiên, nhưng cũng tài liệu hóa các tác vụ của họ. Đó là lý do tại sao các tác vụ được đại diện như các nguồn trong cơ sở dữ liệu Gramps. Sau khi hoàn thành một tác vụ, nội dung liên quan có thể phục vụ như một nguồn tài liệu hóa quy trình nghiên cứu.

## Cơ bản về tác vụ

Các tác vụ có các thuộc tính sau:

- Trạng thái. Có thể là "Mở", "Đang tiến hành", "Bị chặn", hoặc "Hoàn thành"
- Độ ưu tiên. Có thể là "Thấp", "Trung bình", hoặc "Cao"
- Thẻ. Các nhãn là thẻ Gramps bình thường của nguồn cơ sở. (Lưu ý rằng tất cả các tác vụ đều có nhãn `ToDo` để xác định chúng là tác vụ, nhưng nhãn này bị ẩn trong danh sách tác vụ để tránh rối mắt.)
- Tiêu đề. Hiển thị trong danh sách tác vụ
- Mô tả. Một trường văn bản phong phú có thể được sử dụng để mô tả vấn đề, nhưng cũng tài liệu hóa bất kỳ tiến trình nào đã đạt được
- Phương tiện. Bất kỳ tệp phương tiện nào đính kèm với tác vụ

## Tạo một tác vụ

Vì các tác vụ là các đối tượng Gramps bình thường, chúng có thể được chỉnh sửa hoặc tạo bởi cùng một nhóm người dùng có thể chỉnh sửa hoặc tạo các đối tượng khác (như người hoặc sự kiện).

Để tạo một tác vụ, hãy nhấp vào nút + trên trang danh sách tác vụ. Nhập ít nhất một tiêu đề, và tùy chọn một độ ưu tiên, một mô tả, các tệp đính kèm, và thẻ. Trạng thái sẽ luôn là "Mở" khi tạo.

## Danh sách tác vụ

Danh sách tác vụ được sắp xếp theo trạng thái – các tác vụ đã hoàn thành ở cuối – và trong mỗi trạng thái theo độ ưu tiên, từ cao xuống thấp.

Nhấp vào một tác vụ để mở nó. Người dùng có quyền chỉnh sửa cũng có thể nhấp vào biểu tượng trạng thái của một tác vụ để thay đổi trạng thái của nó trực tiếp trong danh sách, ví dụ để đánh dấu nó là đã hoàn thành.

Nút **lọc** ở trên danh sách lọc các tác vụ theo thẻ, với một biểu thức [GOQL](goql.md), hoặc với [bộ lọc nâng cao](lists.md#advanced-filter).

## Chỉnh sửa một tác vụ

Trang tác vụ không có "chế độ chỉnh sửa" riêng biệt như các đối tượng Gramps khác:

- Nhấp vào tiêu đề để chỉnh sửa. Nhấn Enter, nhấp ✓, hoặc nhấp vào nơi khác để lưu; nhấn Escape hoặc nhấp ✕ để hủy.
- Các thay đổi về trạng thái và độ ưu tiên được áp dụng ngay lập tức.
- Để chỉnh sửa mô tả hoặc các tệp đính kèm, nhấp vào nút chỉnh sửa bên cạnh tiêu đề của phần. Mô tả được lưu với nút "lưu" bên dưới; việc chỉnh sửa các tệp đính kèm kết thúc với **Hoàn tất**.
- Nút khóa xác định xem tác vụ có riêng tư hay không. Mô tả của tác vụ có cùng mức độ riêng tư.

Người dùng không có quyền chỉnh sửa sẽ thấy trạng thái và độ ưu tiên dưới dạng văn bản, và các phần không có nội dung sẽ bị ẩn.

Dưới tiêu đề, các biên tập viên thấy hai nút nữa: **Chỉnh sửa Nguồn** mở nguồn đại diện cho tác vụ, nơi các ghi chú, trích dẫn, và thuộc tính khác có thể được chỉnh sửa. **Xóa** xóa tác vụ sau khi xác nhận và trở về danh sách tác vụ; thông điệp xuất hiện có nút hoàn tác để khôi phục tác vụ.

## Thay đổi hàng loạt thuộc tính tác vụ

Người dùng có quyền chỉnh sửa thấy một ô chọn trên mỗi hàng của danh sách tác vụ. Chọn các tác vụ và sử dụng **Đặt Độ ưu tiên** hoặc **Đặt Trạng thái** ở trên danh sách để thay đổi tất cả các tác vụ đã chọn cùng một lúc.

## Tác vụ trong Gramps Desktop

Khi thêm tác vụ qua Gramps Web, cả nguồn và ghi chú sẽ có thẻ `ToDo` gắn liền với chúng, vì vậy các tác vụ sẽ xuất hiện trong [To Do Notes Gramplet](https://gramps-project.org/wiki/index.php/Addon:ToDoNotesGramplet) trên desktop cũng như trong [Báo cáo To Do](https://gramps-project.org/wiki/index.php/Addon:ToDoReport).

Để thêm hoặc chỉnh sửa một tác vụ trong Gramps Desktop, hãy sử dụng các hướng dẫn sau

- Thêm một nguồn với thẻ `ToDo` và tiêu đề tác vụ làm tiêu đề
- Tùy chọn, thêm một ghi chú vào nguồn với thẻ `ToDo`, gõ "To Do", và mô tả dưới dạng văn bản
- Thêm một thuộc tính "Trạng thái" và đặt nó thành "Mở", "Đang tiến hành", "Bị chặn", hoặc "Hoàn thành"
- Thêm một thuộc tính "Độ ưu tiên" và đặt nó thành 9 cho thấp, 5 cho trung bình, hoặc 1 cho cao (các giá trị không trực quan này được lấy từ đặc tả iCalendar)
