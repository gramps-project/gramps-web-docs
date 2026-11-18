# Hồ sơ riêng tư

Bất kỳ hồ sơ nào trong cây có thể được đánh dấu là riêng tư. Cùng với [vai trò người dùng](../install_setup/users.md#user-roles), điều này quyết định ai thấy cái gì.

## Ai có thể thấy cái gì

Gramps Web không bao giờ mở cho công chúng: chỉ có người dùng có tài khoản mới có thể thấy bất kỳ điều gì. "Công khai" trong Gramps đơn giản có nghĩa là "không riêng tư", tức là có thể nhìn thấy bởi mọi người dùng đã đăng nhập vào cây.

| Vai trò | Hồ sơ công khai | Hồ sơ riêng tư |
|---|---|---|
| Khách | xem | – |
| Thành viên | xem | xem |
| Người đóng góp | xem, thêm | xem, thêm |
| Biên tập viên, Chủ sở hữu, Quản trị viên | xem, thêm, chỉnh sửa, xóa | xem, thêm, chỉnh sửa, xóa |

Đối với khách, hồ sơ riêng tư không tồn tại: chúng bị loại khỏi các trang, danh sách, kết quả tìm kiếm, biểu đồ, báo cáo, xuất khẩu và câu trả lời của trợ lý AI. Điều này được thực thi khi máy chủ đọc cơ sở dữ liệu, không phải bằng cách ẩn những thứ trong ứng dụng, vì vậy một khách không thể truy cập vào dữ liệu riêng tư bằng bất kỳ cách nào khác.

Các tài khoản chưa được phê duyệt (sau khi [đăng ký tự động](registration.md)) không thể đăng nhập.

Vì vậy, nếu người thân hoặc những người khác có tài khoản khách không nên thấy thông tin nhất định, hãy đánh dấu nó là riêng tư. Nếu tất cả người dùng của một cây có thể thấy mọi thứ, hãy cho họ vai trò thành viên (hoặc cao hơn) và không cần phải đánh dấu bất kỳ điều gì là riêng tư.

## Người sống không tự động trở thành riêng tư

Không có gì được đánh dấu là riêng tư tự động – ngay cả những người vẫn còn sống. Dữ liệu của những người sống có thể nhìn thấy bởi khách cho đến khi bạn đánh dấu nó là riêng tư. Điều này cũng áp dụng cho các cây được nhập khẩu.

Để làm cho những người có khả năng còn sống trở thành riêng tư trong Gramps Web:

1. Trong danh sách người, mở [bộ lọc nâng cao](lists.md#advanced-filter) và thêm điều kiện "Người có khả năng còn sống" (để trống ngày cho hôm nay). Áp dụng bộ lọc.
2. Nhấp vào **Chọn**, đánh dấu ô kiểm trong tiêu đề, và chọn **Chọn tất cả**.
3. Chọn hành động **Riêng tư** và đánh dấu các hồ sơ là riêng tư.

"Khả năng còn sống" được ước tính từ các ngày tháng của người đó và của các người thân của họ. Những người không có bất kỳ ngày tháng nào có thể sử dụng được được coi là còn sống. Kiểm tra kết quả, và hãy nhớ rằng ước tính có thể thay đổi khi bạn thêm dữ liệu.

Đánh dấu một người là riêng tư sẽ ẩn người đó, nhưng không ẩn các sự kiện, ghi chú, phương tiện hoặc gia đình của họ – xem bên dưới. Gramps Desktop có nhiều công cụ hơn để thiết lập quyền riêng tư cho nhiều hồ sơ liên quan cùng một lúc, mà bạn có thể sử dụng với [Tiện ích đồng bộ](../administration/sync.md).

Những người chết sau đó cũng không tự động trở thành công khai. Việc bạn có muốn điều đó hay không là tùy thuộc vào bạn – nhiều nhà nghiên cứu thích giữ thông tin đã thu thập riêng tư trong một thời gian.

## Đọc biểu tượng khóa

Người dùng có thể xem dữ liệu riêng tư sẽ thấy một biểu tượng khóa bên cạnh các mục riêng tư. Có hai loại:

- **Khóa đầy** – hồ sơ đó là riêng tư. Trên trang của một người, ví dụ, một khóa đầy bên cạnh một sự kiện có nghĩa là sự kiện đó là riêng tư, và bên cạnh một đứa trẻ có nghĩa là đứa trẻ đó là riêng tư.
- **Khóa phác thảo** – chỉ có *liên kết* là riêng tư, không phải hồ sơ mà nó dẫn đến. Ví dụ, liên kết của một người đến một sự kiện có thể là riêng tư trong khi sự kiện đó thì công khai. Sự kiện sau đó sẽ bị ẩn khỏi trang của người đó nhưng vẫn có thể nhìn thấy ở nơi khác, chẳng hạn như trên các trang của những người tham gia khác hoặc trong danh sách sự kiện.

Nếu cả hồ sơ và liên kết của nó đều riêng tư, khóa đầy sẽ được hiển thị.

Sự phân biệt tương tự áp dụng cho trẻ em (đứa trẻ hoặc liên kết của đứa trẻ đến gia đình), các hiệp hội, liên kết kho của một nguồn, và phương tiện trong một bộ sưu tập. Tên, thuộc tính, địa chỉ và URL thuộc về hồ sơ của chúng và chỉ có khóa đầy.

## Làm cho một cái gì đó trở thành riêng tư

Bạn cần quyền chỉnh sửa để thay đổi quyền riêng tư.

- **Một hồ sơ hoàn chỉnh**: mở trang của nó, vào chế độ chỉnh sửa, và nhấp vào nút khóa trên thanh công cụ.
- **Một phần của hồ sơ** – một tên thay thế, thuộc tính, địa chỉ, URL, hiệp hội, liên kết trẻ, hoặc liên kết kho: mở hộp thoại chỉnh sửa của mục đó và bật công tắc **Riêng tư**. Tên chính không có công tắc, vì người đó sẽ hiển thị là "Riêng tư".
- **Một sự kiện từ trang của một người hoặc gia đình**: hộp thoại chỉnh sửa của sự kiện có một công tắc quyền riêng tư cho chính sự kiện đó. Nếu sự kiện được chia sẻ với những người khác, nó chỉ trở nên có thể chỉnh sửa sau khi **Chỉnh sửa cho mọi người**, vì nó là riêng tư đối với tất cả họ.
- **Liên kết của một người đến một sự kiện**: trên trang sự kiện, mở hàng của người tham gia trong chế độ chỉnh sửa. Công tắc quyền riêng tư ở đó chỉ áp dụng cho liên kết của người tham gia đó, vì vậy sự kiện vẫn hiển thị cho các người tham gia khác.
- **Một đối tượng phương tiện trong một bộ sưu tập**: trong chế độ chỉnh sửa, nhấp vào khóa ở góc của ô.
- **Nhiều hồ sơ cùng một lúc**: chọn chúng trong danh sách và sử dụng hành động **Riêng tư**, xem [Danh sách](lists.md#tags-and-privacy).

Để kiểm tra các hồ sơ nào trong danh sách là riêng tư, hãy bật cột **Riêng tư** trong trình chọn cột của danh sách.

## Những điều cần nhớ

- Việc làm cho một hồ sơ trở thành riêng tư không làm cho các hồ sơ mà nó liên kết đến trở thành riêng tư. Nếu một người là riêng tư, các sự kiện của họ, các gia đình mà họ thuộc về, và các ghi chú đính kèm vẫn có thể nhìn thấy trừ khi chúng cũng là riêng tư. Sử dụng bộ lọc nâng cao hoặc cột **Riêng tư** để kiểm tra các hồ sơ liên quan.
- Việc làm cho một gia đình hoặc sự kiện trở thành riêng tư sẽ ẩn nó, nhưng không ẩn những người trong đó.
- [Các kết quả DNA và dữ liệu Y-DNA](dna-matches.md#private-matches) có công tắc **Riêng tư** riêng trong các hộp thoại của chúng.
- Các xuất khẩu và kho phương tiện được thực hiện bởi một người dùng không thể xem dữ liệu riêng tư sẽ không chứa hồ sơ hoặc tệp riêng tư.
- Quyền riêng tư là một tính năng của Gramps, vì vậy các hồ sơ được đánh dấu là riêng tư trong Gramps Desktop cũng sẽ là riêng tư trong Gramps Web, và ngược lại.
