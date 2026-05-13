# Lịch sử sửa đổi

Chế độ xem lịch sử sửa đổi hiển thị tất cả các chỉnh sửa đã được thực hiện đối với cây gia đình.

Chế độ xem danh sách hiển thị các chỉnh sửa được nhóm theo "giao dịch". Một giao dịch là một nhóm gồm một hoặc nhiều bổ sung, xóa bỏ hoặc thay đổi đối tượng Gramps. Ví dụ, việc thêm một gia đình mới với hai người hiện có là cha và mẹ sẽ tạo ra một giao dịch với một đối tượng gia đình được thêm vào và hai đối tượng người được sửa đổi (bởi vì chúng chứa liên kết đến đối tượng gia đình mới).

Nhấp vào một giao dịch sẽ mở chế độ xem chi tiết giao dịch. Nó chứa danh sách các bổ sung, xóa bỏ và cập nhật riêng lẻ theo đối tượng Gramps.

Chọn một thay đổi cá nhân sẽ mở chế độ xem của đại diện JSON thô của đối tượng Gramps với các bổ sung và xóa bỏ được đánh dấu bằng màu xanh lá cây và đỏ, tương ứng.

## Hoàn tác một sửa đổi

Trên trang chi tiết giao dịch, một nút **Hoàn tác** cho phép bạn đảo ngược giao dịch đó. Nhấp vào nó sẽ kiểm tra xem việc hoàn tác có thể được thực hiện một cách sạch sẽ hay không.

**Hoàn tác sạch** – nếu không có đối tượng nào bị ảnh hưởng bởi giao dịch đã được sửa đổi kể từ đó, việc hoàn tác có thể tiến hành mà không có rủi ro. Một hộp thoại xác nhận sẽ hiển thị và nhấp vào **Hoàn tác** sẽ đảo ngược giao dịch.

**Cần ép buộc** – nếu một hoặc nhiều đối tượng bị ảnh hưởng đã được sửa đổi bởi một giao dịch sau đó, việc hoàn tác sạch sẽ không khả thi. Hộp thoại cảnh báo rằng việc ép buộc hoàn tác có thể dẫn đến sự không nhất quán dữ liệu, vì những thay đổi sau này phụ thuộc vào các đối tượng liên quan sẽ được giữ nguyên như cũ mặc dù các đối tượng cơ bản đang được đảo ngược. Bạn có thể hủy bỏ hoặc nhấp vào **Ép buộc hoàn tác** để tiếp tục.

Trong cả hai trường hợp, việc hoàn tác sẽ chạy như một tác vụ nền và một chỉ báo tiến độ sẽ được hiển thị.
