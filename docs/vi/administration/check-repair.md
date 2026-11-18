# Kiểm tra và xác minh dữ liệu

Phần **Xử lý Cây Gia Đình** trong [Cài đặt Quản trị](settings.md) chứa hai công cụ kiểm tra cây gia đình: một cho các vấn đề kỹ thuật trong cơ sở dữ liệu và một cho dữ liệu không hợp lý.

## Kiểm tra và Sửa chữa Cơ sở Dữ liệu

Công cụ này kiểm tra cơ sở dữ liệu Gramps để phát hiện các sự không nhất quán nội bộ và sửa chữa những vấn đề mà nó có thể – tương tự như công cụ [Kiểm tra và Sửa chữa Cơ sở Dữ liệu](https://www.gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Tools#Check_and_Repair_Database) trong Gramps Desktop.

Nhấn **Kiểm tra và Sửa chữa** và chờ cho chỉ báo tiến trình hoàn thành. Kết quả sẽ được hiển thị bên dưới nút:

- Nếu không tìm thấy lỗi, một thông báo xác nhận sẽ được hiển thị.
- Nếu tìm thấy lỗi, một tóm tắt các sửa chữa đã áp dụng sẽ được hiển thị.

Chạy công cụ này nếu bạn gặp phải các lỗi hoặc hành vi bất ngờ có thể do sự không nhất quán trong cơ sở dữ liệu, chẳng hạn như các mối quan hệ bị thiếu giữa các đối tượng.

## Xác minh Dữ liệu

Trong khi [Kiểm tra và Sửa chữa Cơ sở Dữ liệu](#check-and-repair-database) tìm kiếm các sự không nhất quán *kỹ thuật*, công cụ này tìm kiếm dữ liệu *không hợp lý* – tương tự như công cụ [Xác minh Dữ liệu](https://gramps-project.org/wiki/index.php/Gramps_5.0_Wiki_Manual_-_Tools#Verify_the_Data) trong Gramps Desktop. Nó báo cáo những điều không phải là không thể nhưng đủ không có khả năng để đáng để xem xét lại, chẳng hạn như một người mẹ 12 tuổi hoặc một người sống đến 130 tuổi.

Dưới **Tùy chọn**, bạn có thể điều chỉnh các ngưỡng mà các bài kiểm tra sử dụng – độ tuổi tối đa, độ tuổi tối thiểu và tối đa để kết hôn hoặc có con, số lượng con tối đa, và nhiều hơn nữa – cũng như việc ước lượng các ngày tháng bị thiếu hoặc không chính xác và việc báo cáo các ngày không hợp lệ như 31 tháng 2. Các tùy chọn bạn thay đổi sẽ được ghi nhớ trong trình duyệt của bạn cho lần chạy tiếp theo; **Đặt lại** sẽ khôi phục về mặc định.

Nhấn **Xác minh Dữ liệu** để bắt đầu. Kiểm tra sẽ chạy như một tác vụ nền, và các phát hiện sau đó sẽ được liệt kê dưới **Kết quả Xác minh Dữ liệu**. Công cụ này không thay đổi gì: nó chỉ báo cáo những gì nó tìm thấy.

!!! note
    Một phát hiện không phải là bằng chứng của một lỗi. Những cuộc sống dài và khoảng cách tuổi tác lớn thực sự xảy ra, vì vậy hãy coi kết quả như một danh sách những điều cần kiểm tra hơn là một danh sách những điều cần sửa chữa.
