# Nhập tệp phương tiện

Nếu bạn đã [nhập một cây gia đình](import.md) và cần tải lên các tệp phương tiện tương ứng, hãy sử dụng **Nhập Tệp Phương Tiện** trên trang [Nhập](import.md), bên dưới phần nhập cây gia đình. Nó yêu cầu một tệp ZIP chứa các tệp phương tiện còn thiếu. Việc tải lên chỉ có thể thực hiện khi cây có các đối tượng phương tiện, vì các tệp được ghép nối với các đối tượng phương tiện hiện có – một tệp cây gia đình chỉ tham chiếu đến các tệp phương tiện của nó, vì vậy hãy nhập nó trước.

Các tệp được ghép nối với các đối tượng phương tiện trong cây của bạn theo một trong hai cách:

- **Theo checksum.** Đối với các đối tượng phương tiện có checksum – như trường hợp của các cây được nhập từ Gramps Desktop – tệp có checksum khớp sẽ được sử dụng, bất kể tên của nó hoặc cấu trúc thư mục trong tệp ZIP. Điều này chỉ hoạt động nếu các checksum trong cơ sở dữ liệu Gramps là chính xác, điều này được đảm bảo khi chạy công cụ kiểm tra và sửa chữa.
- **Theo đường dẫn hoặc tên tệp.** Các đối tượng phương tiện không có checksum – như thường thấy sau khi nhập GEDCOM – được ghép nối theo đường dẫn tương đối được lưu trữ trong đối tượng phương tiện. Nếu không có tệp nào trong tệp ZIP có đường dẫn đó, chúng sẽ được ghép nối chỉ bằng tên tệp, bỏ qua chữ hoa và chữ thường (kể từ Gramps Web API 3.26). Điều này cũng hoạt động cho các đường dẫn tuyệt đối từ các chương trình khác, chẳng hạn như `C:\Users\...\Family\grandpa.jpg`, vì vậy bạn có thể đơn giản đưa tất cả các tệp vào tệp ZIP. Một tên tệp chỉ được sử dụng nếu nó là duy nhất, cả trong tệp ZIP và giữa các đối tượng phương tiện vẫn chưa có tệp.

Sau khi tải lên, kết quả cho biết có bao nhiêu đối tượng phương tiện đã tìm thấy tệp, và liệt kê những đối tượng mà tệp ZIP không có tệp, với ID Gramps và đường dẫn đã lưu của chúng. Sử dụng danh sách này để tìm các tệp còn thiếu, sau đó tải lên một tệp ZIP khác chỉ với những tệp này – các tệp đã có trên máy chủ sẽ không bị ảnh hưởng.

Nếu nhiều đối tượng phương tiện có cùng tên tệp trong các thư mục khác nhau, việc ghép nối theo tên tệp sẽ không hoạt động cho chúng. Hoặc là tái tạo cấu trúc thư mục từ các đường dẫn đã lưu trong tệp ZIP, hoặc nhập tất cả vào Gramps Desktop trước, cái có nhiều tùy chọn hơn để liên kết các tệp phương tiện hiện có với một cây đã nhập, và sau đó chuyển sang Gramps Web như đã mô tả trong [Đến từ Gramps Desktop](import.md#coming-from-gramps-desktop).

## Tình trạng tệp phương tiện

Phần **Dữ liệu** của [Cài đặt Quản trị](settings.md) hiển thị:

- Tổng số đối tượng phương tiện trong cây và liệu có đối tượng nào thiếu checksum
- Số lượng đối tượng phương tiện mà tệp liên quan bị thiếu trên máy chủ

Một dấu kiểm màu xanh lá cây cho biết mọi thứ đều ổn. Nếu phát hiện vấn đề, các liên kết đến các đối tượng bị ảnh hưởng sẽ được hiển thị. Các checksum bị thiếu thường xảy ra khi dữ liệu được nhập từ một định dạng như GEDCOM mà bao gồm các tham chiếu phương tiện nhưng không có các tệp thực tế. Các tệp còn thiếu có thể được tải lên như đã mô tả ở trên.
