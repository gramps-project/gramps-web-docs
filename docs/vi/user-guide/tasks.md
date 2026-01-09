# Sử dụng quản lý nhiệm vụ tích hợp sẵn

Gramps Web chứa một công cụ quản lý nhiệm vụ genealogi tích hợp sẵn. Nó nhằm mục đích cho phép các nhà nghiên cứu lập kế hoạch và ưu tiên, nhưng cũng ghi lại các nhiệm vụ của họ. Đó là lý do tại sao các nhiệm vụ được đại diện như các nguồn trong cơ sở dữ liệu Gramps. Sau khi hoàn thành một nhiệm vụ, nội dung liên quan có thể phục vụ như một nguồn tài liệu ghi lại quá trình nghiên cứu.

## Cơ bản về nhiệm vụ

Các nhiệm vụ có các thuộc tính sau:

- Trạng thái. Có thể là "Mở", "Đang tiến hành", "Bị chặn", hoặc "Hoàn thành"
- Độ ưu tiên. Có thể là "Thấp", "Trung bình", hoặc "Cao"
- Thẻ. Các nhãn là các thẻ Gramps bình thường của nguồn cơ bản. (Lưu ý rằng tất cả các nhiệm vụ đều có nhãn `ToDo` để xác định chúng là nhiệm vụ, nhưng nhãn này bị ẩn trong danh sách nhiệm vụ để tránh làm rối.)
- Tiêu đề. Hiển thị trong danh sách nhiệm vụ
- Mô tả. Một trường văn bản phong phú có thể được sử dụng để mô tả tuyên bố vấn đề, nhưng cũng ghi lại bất kỳ tiến bộ nào đã đạt được
- Phương tiện. Bất kỳ tệp phương tiện nào đính kèm với nhiệm vụ

## Tạo một nhiệm vụ

Vì các nhiệm vụ là các đối tượng Gramps bình thường, chúng có thể được chỉnh sửa hoặc tạo bởi cùng một nhóm người dùng có thể chỉnh sửa hoặc tạo các đối tượng khác (như người hoặc sự kiện).

Để tạo một nhiệm vụ, nhấp vào nút + trên trang danh sách nhiệm vụ. Nhập ít nhất một tiêu đề. Trạng thái sẽ luôn là "Mở" khi tạo.

## Chỉnh sửa một nhiệm vụ

Để chỉnh sửa bất kỳ chi tiết nào của nhiệm vụ, nhấp vào nó trong danh sách nhiệm vụ.

Trang chi tiết nhiệm vụ không có chế độ "chỉnh sửa" riêng biệt như các đối tượng Gramps khác. Các thay đổi về tiêu đề, trạng thái và độ ưu tiên được áp dụng ngay lập tức. Các thay đổi về mô tả văn bản phong phú yêu cầu nhấp vào nút "lưu" bên dưới nó.

## Thay đổi hàng loạt thuộc tính nhiệm vụ

Độ ưu tiên và trạng thái của các nhiệm vụ có thể được thay đổi hàng loạt bằng cách sử dụng các ô kiểm trong danh sách nhiệm vụ để chọn và các nút thích hợp ở trên danh sách nhiệm vụ.

## Nhiệm vụ trong Gramps Desktop

Khi thêm nhiệm vụ qua Gramps Web, cả nguồn và ghi chú sẽ có thẻ `ToDo` đính kèm, vì vậy các nhiệm vụ sẽ xuất hiện trong [To Do Notes Gramplet](https://gramps-project.org/wiki/index.php/Addon:ToDoNotesGramplet) trên máy tính để bàn cũng như trong [To Do Report](https://gramps-project.org/wiki/index.php/Addon:ToDoReport).

Để thêm hoặc chỉnh sửa một nhiệm vụ trong Gramps Desktop, hãy sử dụng các hướng dẫn sau

- Thêm một nguồn với thẻ `ToDo` và tiêu đề nhiệm vụ làm tiêu đề
- Tùy chọn, thêm một ghi chú vào nguồn với thẻ `ToDo`, loại "To Do", và mô tả làm văn bản
- Thêm một thuộc tính "Trạng thái" và đặt nó thành "Mở", "Đang tiến hành", "Bị chặn", hoặc "Hoàn thành"
- Thêm một thuộc tính "Độ ưu tiên" và đặt nó thành 9 cho thấp, 5 cho trung bình, hoặc 1 cho cao (các giá trị ngược lại này được lấy từ đặc tả iCalendar)
