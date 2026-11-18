# Sử dụng quản lý tác vụ tích hợp sẵn

Gramps Web chứa một công cụ quản lý tác vụ genealogi tích hợp sẵn. Nó được thiết kế để giúp các nhà nghiên cứu lập kế hoạch và ưu tiên, nhưng cũng để tài liệu hóa các tác vụ của họ. Đó là lý do tại sao các tác vụ được đại diện như các nguồn trong cơ sở dữ liệu Gramps. Sau khi hoàn thành một tác vụ, nội dung liên quan có thể phục vụ như một nguồn tài liệu hóa quá trình nghiên cứu.

## Cơ bản về tác vụ

Các tác vụ có các thuộc tính sau:

- Trạng thái. Có thể là "Mở", "Đang tiến hành", "Bị chặn", hoặc "Đã hoàn thành"
- Ưu tiên. Có thể là "Thấp", "Trung bình", hoặc "Cao"
- Thẻ. Các nhãn là thẻ Gramps thông thường của nguồn cơ sở. (Lưu ý rằng tất cả các tác vụ đều có nhãn `ToDo` để xác định chúng là tác vụ, nhưng nhãn này bị ẩn trong danh sách tác vụ để tránh làm rối.)
- Tiêu đề. Hiển thị trong danh sách tác vụ
- Mô tả. Một trường văn bản phong phú có thể được sử dụng để mô tả vấn đề, nhưng cũng để tài liệu hóa bất kỳ tiến bộ nào đã đạt được
- Tài liệu. Bất kỳ tệp phương tiện nào đính kèm với tác vụ

## Tạo một tác vụ

Vì các tác vụ là các đối tượng Gramps thông thường, chúng có thể được chỉnh sửa hoặc tạo bởi cùng một nhóm người dùng có thể chỉnh sửa hoặc tạo các đối tượng khác (như người hoặc sự kiện).

Để tạo một tác vụ, nhấp vào nút + trên trang danh sách tác vụ. Nhập ít nhất một tiêu đề, và tùy chọn một ưu tiên, một mô tả, các tệp đính kèm, và các thẻ. Trạng thái sẽ luôn là "Mở" khi tạo.

## Danh sách tác vụ

Theo mặc định, danh sách tác vụ được sắp xếp theo trạng thái – các tác vụ đã hoàn thành ở cuối – và trong mỗi trạng thái theo ưu tiên, ưu tiên cao nhất trước. Menu sắp xếp trong thanh bộ lọc cũng sắp xếp theo ưu tiên, tiêu đề, hoặc thay đổi cuối cùng (mới nhất trước).

Nhấp vào một tác vụ để mở nó. Người dùng có quyền chỉnh sửa cũng có thể nhấp vào biểu tượng trạng thái của một tác vụ để thay đổi trạng thái của nó trực tiếp trong danh sách, ví dụ để đánh dấu nó là đã hoàn thành.

Nút **lọc** ở trên danh sách lọc các tác vụ theo tiêu đề, trạng thái, ưu tiên, hoặc thẻ, với một biểu thức [GOQL](goql.md), hoặc với [bộ lọc nâng cao](lists.md#advanced-filter). Đánh dấu nhiều trạng thái hoặc ưu tiên sẽ hiển thị các tác vụ với bất kỳ trạng thái nào trong số đó, ví dụ tất cả các tác vụ mở và bị chặn.

## Chỉnh sửa một tác vụ

Trang tác vụ không có chế độ "chỉnh sửa" riêng biệt như các đối tượng Gramps khác:

- Nhấp vào tiêu đề để chỉnh sửa. Nhấn Enter, nhấp ✓, hoặc nhấp vào nơi khác để lưu; nhấn Escape hoặc nhấp ✕ để hủy.
- Các thay đổi về trạng thái và ưu tiên sẽ được áp dụng ngay lập tức.
- Để chỉnh sửa mô tả hoặc các tệp đính kèm, nhấp vào nút chỉnh sửa bên cạnh tiêu đề của phần. Mô tả được lưu với nút "lưu" bên dưới; chỉnh sửa các tệp đính kèm kết thúc với **Hoàn tất**.
- Nút khóa xác định liệu tác vụ có riêng tư hay không. Mô tả của tác vụ sẽ có cùng mức độ riêng tư.

Người dùng không có quyền chỉnh sửa sẽ thấy trạng thái và ưu tiên dưới dạng văn bản, và các phần không có nội dung sẽ bị ẩn.

Dưới tiêu đề, các biên tập viên thấy hai nút nữa: **Chỉnh sửa Nguồn** mở nguồn đại diện cho tác vụ, nơi có thể chỉnh sửa các ghi chú, trích dẫn, và thuộc tính khác của nó. **Xóa** xóa tác vụ sau khi xác nhận và quay lại danh sách tác vụ; thông điệp xuất hiện có nút hoàn tác để khôi phục tác vụ.

## Thay đổi hàng loạt thuộc tính tác vụ

Người dùng có quyền chỉnh sửa sẽ thấy một ô chọn trên mỗi hàng của danh sách tác vụ. Chọn các tác vụ và sử dụng **Đặt Ưu tiên** hoặc **Đặt Trạng thái** ở trên danh sách để thay đổi tất cả các tác vụ đã chọn cùng một lúc.

## Tác vụ trong Gramps Desktop

Khi thêm tác vụ qua Gramps Web, cả nguồn và ghi chú sẽ có thẻ `ToDo` đính kèm, vì vậy các tác vụ sẽ xuất hiện trong [To Do Notes Gramplet](https://gramps-project.org/wiki/index.php/Addon:ToDoNotesGramplet) trên máy tính để bàn cũng như trong [Báo cáo To Do](https://gramps-project.org/wiki/index.php/Addon:ToDoReport).

Để thêm hoặc chỉnh sửa một tác vụ trong Gramps Desktop, hãy sử dụng các hướng dẫn sau

- Thêm một nguồn với thẻ `ToDo` và tiêu đề tác vụ làm tiêu đề
- Tùy chọn, thêm một ghi chú vào nguồn với thẻ `ToDo`, gõ "To Do", và mô tả dưới dạng văn bản
- Thêm một thuộc tính "Trạng thái" và đặt nó thành "Mở", "Đang tiến hành", "Bị chặn", hoặc "Đã hoàn thành"
- Thêm một thuộc tính "Ưu tiên" và đặt nó thành 9 cho thấp, 5 cho trung bình, hoặc 1 cho cao (các giá trị không trực quan này được lấy từ thông số kỹ thuật iCalendar)
