# Thông báo

Biểu tượng chuông ở thanh ứng dụng trên cùng mở ra thông báo. Một biểu tượng cho biết số lượng thông báo chưa đọc. Menu liệt kê các tác vụ đang chạy và các thông báo mới nhất; **Hiện tất cả** mở toàn bộ nhật ký thông báo. Trên các màn hình nhỏ, chuông sẽ mở nhật ký trực tiếp.

Thông báo liên quan đến:

- **Thay đổi bởi người dùng khác.** Khi người dùng khác thay đổi cây trong khi bạn đang sử dụng Gramps Web, một thông báo sẽ cho biết ai đã thay đổi cái gì, ví dụ: "Chỉnh sửa Người" hoặc "12 thay đổi". Nhấp vào nó để mở thay đổi trong [lịch sử sửa đổi](revisions.md). Những thay đổi không có người dùng Gramps Web, chẳng hạn như những thay đổi được thực hiện trực tiếp trên cơ sở dữ liệu chia sẻ với Gramps Desktop, sẽ được hiển thị mà không có tên. Điều này chỉ có sẵn cho những người dùng có thể xem lịch sử sửa đổi (thành viên và cao hơn).
- **Tác vụ nền** – chẳng hạn như nhập và xuất, tạo báo cáo, nhận diện văn bản OCR, nâng cấp cơ sở dữ liệu, xóa hoặc chỉnh sửa nhiều đối tượng, và xây dựng lại chỉ mục tìm kiếm – hiển thị trạng thái của chúng (ví dụ: đang chờ, đã bắt đầu, đang tiến hành) và thông báo cho bạn khi chúng hoàn thành hoặc thất bại.
- **Lỗi** đã xảy ra trong phiên của bạn – yêu cầu API thất bại, lỗi tác vụ nền, lỗi lưu, hoặc lỗi cấp trình duyệt.

Các xuất khẩu đã hoàn thành và lưu trữ phương tiện có thể được tải xuống từ thông báo của chúng, ngay cả sau khi bạn đã rời khỏi [Trang Xuất](../administration/export.md).

Một số thông báo bao gồm chi tiết có cấu trúc, chẳng hạn như thông báo lỗi của một tác vụ thất bại. Nhấp vào một mục như vậy trong nhật ký thông báo sẽ mở một hộp thoại với phân tích dữ liệu lỗi và một nút **Sao chép JSON**. Điều này hữu ích khi báo cáo một lỗi, vì JSON chứa thông tin lỗi chính xác từ máy chủ.

Sử dụng **Xóa tất cả** trong nhật ký thông báo để xóa tất cả thông báo.

Các tác vụ thay đổi toàn bộ cây, chẳng hạn như nhập, khôi phục, xóa tất cả đối tượng, hoặc xây dựng lại chỉ mục tìm kiếm, không thể chạy cùng một lúc. Nếu bạn bắt đầu một tác vụ trong khi một tác vụ khác đang chạy, một thông báo sẽ cho biết rằng một tác vụ khác đã đang chạy trên cây này, và tác vụ đang chạy sẽ được hiển thị với tiến trình của nó.

!!! note
    Các thông báo chỉ được lưu trữ trong bộ nhớ và sẽ bị xóa khi bạn tải lại trang. Gramps Web chỉ kiểm tra các thay đổi của người dùng khác khi nó đang mở, vì vậy các thay đổi được thực hiện trong khi bạn vắng mặt sẽ không được báo cáo; xem [Lịch sử sửa đổi](revisions.md) cho những thay đổi đó.
