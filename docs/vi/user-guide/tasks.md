# Sử dụng quản lý tác vụ tích hợp sẵn

Gramps Web chứa một công cụ quản lý tác vụ genealogi tích hợp sẵn. Nó nhằm mục đích giúp các nhà nghiên cứu lập kế hoạch và ưu tiên, nhưng cũng ghi lại các tác vụ của họ. Đó là lý do tại sao các tác vụ được đại diện như các nguồn trong cơ sở dữ liệu Gramps. Sau khi hoàn thành một tác vụ, nội dung liên quan có thể phục vụ như một nguồn tài liệu ghi lại quá trình nghiên cứu.

## Cơ bản về tác vụ

Các tác vụ có các thuộc tính sau:

- Trạng thái. Có thể là "Mở", "Đang tiến hành", "Bị chặn", hoặc "Hoàn thành"
- Độ ưu tiên. Có thể là "Thấp", "Trung bình", hoặc "Cao"
- Thẻ. Các nhãn là thẻ Gramps bình thường của nguồn cơ sở dữ liệu. (Lưu ý rằng tất cả các tác vụ đều có nhãn `ToDo` để xác định chúng là tác vụ, nhưng nhãn này bị ẩn trong danh sách tác vụ để tránh làm rối.)
- Tiêu đề. Hiển thị trong danh sách tác vụ
- Mô tả. Một trường văn bản phong phú có thể được sử dụng để mô tả vấn đề, nhưng cũng ghi lại bất kỳ tiến bộ nào đã đạt được
- Phương tiện. Bất kỳ tệp phương tiện nào được đính kèm với tác vụ

## Tạo một tác vụ

Vì các tác vụ là các đối tượng Gramps bình thường, chúng có thể được chỉnh sửa hoặc tạo bởi cùng một nhóm người dùng có thể chỉnh sửa hoặc tạo các đối tượng khác (như người hoặc sự kiện).

Để tạo một tác vụ, nhấp vào nút + trên trang danh sách tác vụ. Nhập ít nhất một tiêu đề. Trạng thái sẽ luôn là "Mở" khi tạo.

## Chỉnh sửa một tác vụ

Để chỉnh sửa bất kỳ chi tiết nào của tác vụ, nhấp vào nó trong danh sách tác vụ.

Trang chi tiết tác vụ không có chế độ "chỉnh sửa" riêng biệt như các đối tượng Gramps khác. Các thay đổi đối với tiêu đề, trạng thái và độ ưu tiên sẽ được áp dụng ngay lập tức. Các thay đổi đối với mô tả văn bản phong phú yêu cầu nhấp vào nút "lưu" bên dưới nó.

## Thay đổi hàng loạt thuộc tính tác vụ

Độ ưu tiên và trạng thái của các tác vụ có thể được thay đổi hàng loạt bằng cách sử dụng các ô kiểm trong danh sách tác vụ để chọn và các nút thích hợp ở trên danh sách tác vụ.

## Các tác vụ trong Gramps Desktop

Khi thêm tác vụ qua Gramps Web, cả nguồn và ghi chú sẽ có thẻ `ToDo` đính kèm, vì vậy các tác vụ sẽ xuất hiện trong [To Do Notes Gramplet](https://gramps-project.org/wiki/index.php/Addon:ToDoNotesGramplet) trên desktop cũng như trong [To Do Report](https://gramps-project.org/wiki/index.php/Addon:ToDoReport).

Để thêm hoặc chỉnh sửa một tác vụ trong Gramps Desktop, hãy sử dụng các hướng dẫn sau:

- Thêm một nguồn với thẻ `ToDo` và tiêu đề tác vụ làm tiêu đề
- Tùy chọn, thêm một ghi chú vào nguồn với thẻ `ToDo`, loại "To Do", và mô tả làm văn bản
- Thêm một thuộc tính "Trạng thái" và đặt nó thành "Mở", "Đang tiến hành", "Bị chặn", hoặc "Hoàn thành"
- Thêm một thuộc tính "Độ ưu tiên" và đặt nó thành 9 cho thấp, 5 cho trung bình, hoặc 1 cho cao (các giá trị ngược lại này được lấy từ thông số kỹ thuật iCalendar)
