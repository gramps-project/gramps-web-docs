# Danh sách

Mỗi loại đối tượng trong Gramps Web đều có chế độ xem danh sách: Người, Gia đình, Sự kiện, Địa điểm, Nguồn, Trích dẫn, Kho lưu trữ, Ghi chú và Phương tiện. Tất cả đều hoạt động theo cùng một cách và chia sẻ các công cụ giống nhau để sắp xếp, lọc và chỉnh sửa hàng loạt.

## Sắp xếp và phân trang

Nhấp vào tiêu đề cột để sắp xếp theo cột đó; nhấp lại để đảo ngược thứ tự. Việc sắp xếp được thực hiện bởi máy chủ, vì vậy nó áp dụng cho toàn bộ danh sách, không chỉ riêng trang bạn đang xem.

Các danh sách dài được chia thành các trang. Sử dụng các điều khiển phân trang ở dưới cùng để di chuyển giữa chúng.

Trên các màn hình hẹp, bảng tự động chuyển sang bố cục gọn gàng, vì vậy chế độ xem danh sách vẫn có thể sử dụng trên điện thoại.

## Chọn cột

Nhấp vào biểu tượng bánh răng ở trên cùng danh sách để mở hộp thoại **Cột**. Đánh dấu hoặc bỏ đánh dấu một cột để hiển thị hoặc ẩn nó. **Đặt lại** khôi phục lựa chọn mặc định cho danh sách đó.

Ít nhất một cột phải vẫn hiển thị, vì vậy cột cuối cùng còn lại không thể bị bỏ đánh dấu.

Lựa chọn cột của bạn được ghi nhớ theo từng loại đối tượng và theo từng cây gia đình. Nó được lưu trữ trong trình duyệt của bạn, vì vậy nó không hiển thị cho người dùng khác – nhưng nó cũng không theo bạn đến trình duyệt hoặc thiết bị khác.

## Lọc

Nhấp vào nút **lọc** để mở bảng lọc. Một nút chuyển đổi ở đầu bảng chuyển đổi giữa hai chế độ:

- **đơn giản** – một bộ lọc đã được chuẩn bị sẵn phụ thuộc vào loại đối tượng. Đối với người, ví dụ, bạn có thể lọc theo năm sinh, năm mất, các thuộc tính của người, số lượng mối quan hệ, thẻ, và xem một đối tượng là riêng tư hay công khai.
- **GQL** – một trường văn bản duy nhất cho một truy vấn nâng cao trong [Ngôn ngữ truy vấn Gramps](gql.md). Gõ truy vấn và nhấn Enter hoặc nhấp vào **Áp dụng**. Nếu truy vấn không hợp lệ, khung của trường sẽ chuyển sang màu đỏ.

Các bộ lọc đang hoạt động được hiển thị dưới dạng chip ở trên danh sách. Xóa một bộ lọc đơn lẻ bằng cách nhấp vào nút xóa của chip, hoặc sử dụng **Xóa tất cả bộ lọc** để xóa tất cả cùng một lúc.

!!! note
    Hai chế độ là các lựa chọn thay thế, không phải là bổ sung: một truy vấn GQL thay thế các bộ lọc đơn giản, và việc chuyển lại chế độ đơn giản sẽ bỏ truy vấn.

## Chọn đối tượng và thực hiện hành động hàng loạt

Người dùng có quyền chỉnh sửa sẽ thấy nút **Chọn** bên cạnh nút lọc. Nhấp vào nó để vào chế độ chọn, điều này sẽ thêm một ô kiểm vào mỗi hàng.

Đánh dấu các đối tượng bạn muốn, và một thanh công cụ sẽ xuất hiện cho biết có bao nhiêu đối tượng được chọn, cùng với một menu thả xuống **Hành động** và một nút **Áp dụng**.

### Xóa

Chọn một hoặc nhiều đối tượng, chọn **Xóa**, và nhấp **Áp dụng**. Một hộp thoại xác nhận sẽ yêu cầu bạn xác nhận, cảnh báo rằng hành động này không thể hoàn tác.

!!! tip
    Việc xóa được ghi lại trong [lịch sử sửa đổi](revisions.md) như bất kỳ thay đổi nào khác, vì vậy một lần xóa hàng loạt sai lầm có thể được đảo ngược bằng cách hoàn tác giao dịch tương ứng.

### Gộp

Chọn **chính xác hai** đối tượng, chọn **Gộp**, và nhấp **Áp dụng**. Một hộp thoại sẽ hỏi đối tượng nào trong hai đối tượng nên cung cấp dữ liệu chính cho đối tượng đã gộp; nhấp vào đối tượng bạn muốn giữ làm chính. Dữ liệu của đối tượng còn lại sẽ được gộp vào và các tham chiếu sẽ được cập nhật.

Việc gộp có sẵn cho người, gia đình, sự kiện, địa điểm, nguồn và trích dẫn. Nó không có sẵn cho kho lưu trữ, ghi chú và đối tượng phương tiện.

Nếu bạn chọn một hành động mà không có lựa chọn hợp lệ – ví dụ như gộp với chỉ một đối tượng được chọn – một hộp thoại sẽ giải thích những gì cần thiết.
