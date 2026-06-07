# Thông báo

**Thông báo** là một mục trong thanh bên với biểu tượng chuông. Khi có lỗi xảy ra hoặc các tác vụ nền đang chạy, một biểu tượng cho biết số lượng thông báo chưa đọc. Nhấp vào nó để mở nhật ký thông báo.

Nhật ký thông báo phục vụ hai mục đích:

- Nó là một bản ghi các lỗi đã xảy ra trong phiên của bạn – các yêu cầu API thất bại, lỗi tác vụ nền, lỗi lưu, hoặc lỗi cấp độ trình duyệt.
- Nó theo dõi tiến trình của các tác vụ nền chạy lâu – chẳng hạn như nhập và xuất, tạo báo cáo, nhận diện văn bản OCR, nâng cấp cơ sở dữ liệu, và xây dựng lại chỉ mục tìm kiếm/ ngữ nghĩa – hiển thị trạng thái của chúng (ví dụ: đang chờ, đã bắt đầu, đang tiến hành) và thông báo cho bạn khi chúng hoàn thành hoặc thất bại.

Mỗi mục hiển thị một thông điệp ngắn, nguồn (Mạng, Tác vụ, Lưu, hoặc Trình duyệt), và một dấu thời gian.

Một số thông báo bao gồm chi tiết có cấu trúc. Nhấp vào một mục như vậy sẽ mở một hộp thoại với phân tích dữ liệu lỗi và một nút **Sao chép JSON**. Điều này hữu ích khi báo cáo một lỗi, vì JSON chứa thông tin lỗi chính xác từ máy chủ.

Sử dụng **Xóa tất cả** để xóa tất cả thông báo.

!!! note
    Các thông báo chỉ được lưu trữ trong bộ nhớ và sẽ bị xóa khi bạn tải lại trang.
