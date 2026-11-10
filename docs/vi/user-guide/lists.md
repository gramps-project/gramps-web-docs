# Danh sách

Mỗi loại đối tượng trong Gramps Web đều có chế độ xem danh sách: Người, Gia đình, Sự kiện, Địa điểm, Nguồn, Trích dẫn, Kho lưu trữ, Ghi chú và Phương tiện. Tất cả đều hoạt động theo cách giống nhau và chia sẻ các công cụ giống nhau để sắp xếp, lọc và chỉnh sửa hàng loạt.

## Sắp xếp và phân trang

Nhấp vào tiêu đề cột để sắp xếp theo cột đó; nhấp lại để đảo ngược thứ tự. Việc sắp xếp được thực hiện bởi máy chủ, vì vậy nó áp dụng cho toàn bộ danh sách, không chỉ cho trang bạn đang xem.

Các danh sách dài được chia thành các trang. Sử dụng các điều khiển phân trang ở dưới cùng để di chuyển giữa chúng.

Trên các màn hình hẹp, bảng tự động chuyển sang bố cục gọn gàng, vì vậy chế độ xem danh sách vẫn có thể sử dụng trên điện thoại.

## Chọn cột

Nhấp vào biểu tượng bánh răng ở cuối bên phải của thanh công cụ trên danh sách để mở hộp thoại **Cột**. Đánh dấu hoặc bỏ đánh dấu một cột để hiển thị hoặc ẩn nó. **Đặt lại** khôi phục lựa chọn mặc định cho danh sách đó.

Ít nhất một cột phải luôn hiển thị, vì vậy cột còn lại cuối cùng không thể bị bỏ đánh dấu.

Lựa chọn cột của bạn được ghi nhớ theo từng loại đối tượng và theo từng cây gia đình. Nó được lưu trữ trong trình duyệt của bạn, vì vậy nó không hiển thị cho người dùng khác – nhưng nó cũng không theo bạn đến trình duyệt hoặc thiết bị khác.

## Lọc

Nhấp vào nút **lọc** để mở bảng lọc. Nó cung cấp ba cách để lọc, có thể kết hợp:

- **Bộ lọc có sẵn** trong các phần có thể thu gọn phụ thuộc vào loại đối tượng. Ví dụ, đối với người, bạn có thể lọc theo tên, năm sinh, năm mất, các thuộc tính của người, số lượng mối quan hệ, thẻ, và liệu một đối tượng có phải là riêng tư hay công khai. Gia đình có thể được lọc theo tên của cha, mẹ hoặc một đứa trẻ, nguồn theo tác giả, và địa điểm cũng như kho lưu trữ theo loại của chúng.
- **Lọc nâng cao** – một trình tạo điều kiện cho các bộ lọc mà các bộ lọc có sẵn không thể diễn đạt, được mô tả [dưới đây](#advanced-filter).
- **GOQL** – một trường văn bản cho một biểu thức trong [Ngôn ngữ truy vấn đối tượng Gramps](goql.md), với đánh dấu cú pháp. Nhập biểu thức và nhấn Enter hoặc nhấp vào **Áp dụng**. Nếu biểu thức không hợp lệ, trường sẽ được đánh dấu là lỗi. Một biểu thức áp dụng trên các bộ lọc khác.

Các bộ lọc đang hoạt động được hiển thị dưới dạng chip trong một hàng bên dưới thanh công cụ. Xóa một bộ lọc đơn bằng cách nhấp vào nút xóa của chip, hoặc sử dụng **Xóa tất cả bộ lọc** để xóa tất cả cùng một lúc.

### Lọc nâng cao

Nhấp vào **Lọc nâng cao** ở dưới cùng của bảng lọc để mở trình tạo điều kiện. Các điều kiện của nó là các quy tắc lọc được biết đến từ Gramps Desktop, chẳng hạn như "Người với &lt;tên&gt;" hoặc "Tổ tiên của &lt;người&gt;".

- Nhấp vào **Thêm điều kiện** để chọn một quy tắc. Các quy tắc được nhóm thành các danh mục và có thể được tìm kiếm theo tên hoặc mô tả.
- Điền vào các tham số của quy tắc. Mỗi tham số có một đầu vào tương ứng, ví dụ như một trường ngày, một bộ chọn thẻ, hoặc một bộ chọn đối tượng cho một người hoặc địa điểm.
- Chọn cách các điều kiện của một nhóm được kết hợp: **Tất cả các điều kiện**, **Bất kỳ điều kiện nào**, hoặc – thông qua menu bên cạnh chúng – **Chính xác một điều kiện**.
- Nhấp vào **Thêm nhóm** để thêm một nhóm điều kiện bên trong một nhóm khác, với cách kết hợp riêng của nó.
- Chọn **Không** trên một điều kiện hoặc nhóm để đảo ngược nó.

Nhấp vào **Áp dụng** để lọc danh sách.

Các bộ lọc có sẵn và biểu thức GOQL đang hoạt động khi bạn mở trình tạo xuất hiện ở đó như các điều kiện. Một biểu thức GOQL cũng có thể được thêm như một điều kiện riêng, chẳng hạn như để kết hợp nhiều biểu thức với **Bất kỳ điều kiện nào**. Nếu bộ lọc bạn xây dựng có thể được diễn đạt bằng các bộ lọc có sẵn, nó sẽ được hiển thị cùng với chúng sau khi áp dụng. Nếu không, nó sẽ được hiển thị dưới dạng một chip **Lọc nâng cao** duy nhất, và bảng lọc cung cấp một nút **Chỉnh sửa** để mở lại trình tạo.

!!! note
    Các quy tắc tham chiếu đến các bộ lọc tùy chỉnh được lưu trong Gramps Desktop không có sẵn trong trình tạo. Các quy tắc được hiển thị bằng ngôn ngữ của bạn với Gramps Web API 3.24 hoặc mới hơn.

## Chọn đối tượng và thực hiện hành động hàng loạt

Người dùng có quyền chỉnh sửa sẽ thấy nút **Chọn** bên cạnh nút lọc. Nhấp vào nó để vào chế độ chọn, điều này sẽ thêm một ô kiểm vào mỗi hàng.

Đánh dấu các đối tượng bạn muốn, và một thanh công cụ xuất hiện hiển thị số lượng đã chọn, cùng với một menu thả xuống **Hành động** và một nút **Áp dụng**.

Ô kiểm trong tiêu đề bảng chọn tất cả các đối tượng trên trang hiện tại. Nếu có nhiều đối tượng phù hợp với các bộ lọc hiện tại, thanh công cụ sau đó cung cấp **Chọn tất cả (N)**, chọn tất cả N đối tượng phù hợp trên tất cả các trang. Bỏ đánh dấu một hàng, thay đổi trang hoặc các bộ lọc, hoặc rời khỏi chế độ chọn sẽ kết thúc việc chọn này.

### Xóa

Chọn một hoặc nhiều đối tượng, chọn **Xóa**, và nhấp vào **Áp dụng**. Một hộp thoại xác nhận yêu cầu bạn xác nhận, cảnh báo rằng hành động này không thể hoàn tác.

Việc xóa hơn mười đối tượng sẽ chạy như một tác vụ nền. Tiến trình của nó được hiển thị bên cạnh nút **Áp dụng** và trong [Thông báo](notifications.md), và danh sách sẽ được tải lại khi hoàn tất.

!!! tip
    Việc xóa được ghi lại trong [lịch sử sửa đổi](revisions.md) như bất kỳ thay đổi nào khác, vì vậy một lần xóa hàng loạt nhầm có thể được đảo ngược bằng cách hoàn tác giao dịch tương ứng.

### Gộp

Chọn **chính xác hai** đối tượng, chọn **Gộp**, và nhấp vào **Áp dụng**. Một hộp thoại hỏi đối tượng nào trong hai đối tượng nên cung cấp dữ liệu chính cho đối tượng đã gộp; nhấp vào đối tượng mà bạn muốn giữ làm chính. Dữ liệu của đối tượng còn lại sẽ được gộp vào nó và các tham chiếu sẽ được cập nhật.

Việc gộp có sẵn cho người, gia đình, sự kiện, địa điểm, nguồn và trích dẫn. Nó không có sẵn cho kho lưu trữ, ghi chú và đối tượng phương tiện.

Trong chế độ xem phương tiện, việc chọn hoạt động trong cả chế độ xem thư viện và chế độ xem danh sách: trong chế độ chọn, nhấp vào một ô hoặc hàng sẽ chuyển đổi trạng thái của nó. **Xóa** là hành động duy nhất có sẵn cho phương tiện.

Nếu bạn chọn một hành động mà không có lựa chọn hợp lệ – chẳng hạn như gộp với chỉ một đối tượng được chọn – một hộp thoại sẽ giải thích những gì cần thiết.
