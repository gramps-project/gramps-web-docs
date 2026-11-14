# Nhập tệp phương tiện

Nếu bạn đã [nhập một cây gia đình](import.md) và cần tải lên các tệp phương tiện tương ứng, hãy sử dụng **Nhập tệp phương tiện** trong phần Dữ liệu của [cài đặt Quản trị](settings.md). Nó yêu cầu một tệp ZIP chứa các tệp phương tiện còn thiếu. Các tệp được khớp với các đối tượng phương tiện trong cây của bạn theo một trong hai cách:

- **Theo checksum.** Đối với các đối tượng phương tiện có checksum – như trường hợp với các cây được nhập từ Gramps Desktop – tệp có checksum khớp sẽ được sử dụng, bất kể tên của nó hoặc cấu trúc thư mục trong tệp ZIP. Điều này chỉ hoạt động nếu các checksum trong cơ sở dữ liệu Gramps là chính xác, điều mà việc chạy công cụ kiểm tra và sửa chữa đảm bảo.
- **Theo đường dẫn.** Các đối tượng phương tiện không có checksum – như thường thấy sau khi nhập GEDCOM – được khớp theo đường dẫn của chúng: tệp ZIP phải chứa tệp dưới đúng đường dẫn tương đối được lưu trữ trong đối tượng phương tiện.

Nếu các đường dẫn được lưu trữ trong tệp GEDCOM của bạn là tuyệt đối (ví dụ `C:\Users\...\photo.jpg`), việc khớp theo đường dẫn sẽ không hoạt động. Trong trường hợp này, được khuyến nghị là trước tiên hãy nhập mọi thứ vào Gramps Desktop, nơi có nhiều tùy chọn hơn để liên kết các tệp phương tiện hiện có với một cây đã nhập, và sau đó chuyển sang Gramps Web như được mô tả trong [Đến từ Gramps Desktop](import.md#coming-from-gramps-desktop).

## Tình trạng tệp phương tiện

Phần **Dữ liệu** của [cài đặt Quản trị](settings.md) hiển thị:

- Tổng số đối tượng phương tiện trong cây và liệu có đối tượng nào thiếu checksum
- Số lượng đối tượng phương tiện mà tệp liên quan bị thiếu trên máy chủ

Một dấu kiểm màu xanh lá cây cho biết mọi thứ đều ổn. Nếu phát hiện vấn đề, các liên kết đến các đối tượng bị ảnh hưởng sẽ được hiển thị. Các checksum bị thiếu thường xảy ra khi dữ liệu được nhập từ một định dạng như GEDCOM mà bao gồm các tham chiếu phương tiện nhưng không có các tệp thực tế. Các tệp bị thiếu có thể được tải lên như đã mô tả ở trên.
