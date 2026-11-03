# Danh sách

Mỗi loại đối tượng trong Gramps Web đều có chế độ xem danh sách: Người, Gia đình, Sự kiện, Địa điểm, Nguồn, Trích dẫn, Kho lưu trữ, Ghi chú và Phương tiện. Tất cả đều hoạt động theo cùng một cách và chia sẻ các công cụ giống nhau để sắp xếp, lọc và chỉnh sửa hàng loạt.

## Sắp xếp và phân trang

Nhấp vào tiêu đề cột để sắp xếp theo cột đó; nhấp lại để đảo ngược thứ tự. Việc sắp xếp được thực hiện bởi máy chủ, vì vậy nó áp dụng cho toàn bộ danh sách, không chỉ riêng trang bạn đang xem.

Các danh sách dài được chia thành các trang. Sử dụng các điều khiển phân trang ở dưới cùng để di chuyển giữa chúng.

Trên các màn hình hẹp, bảng tự động chuyển sang chế độ bố trí gọn gàng, vì vậy chế độ xem danh sách vẫn có thể sử dụng trên điện thoại.

## Chọn cột

Nhấp vào biểu tượng bánh răng ở trên cùng danh sách để mở hộp thoại **Cột**. Đánh dấu hoặc bỏ đánh dấu một cột để hiển thị hoặc ẩn nó. **Đặt lại** khôi phục lựa chọn mặc định cho danh sách đó.

Ít nhất một cột phải vẫn hiển thị, vì vậy cột cuối cùng còn lại không thể bị bỏ đánh dấu.

Lựa chọn cột của bạn được ghi nhớ theo từng loại đối tượng và theo từng cây gia đình. Nó được lưu trữ trong trình duyệt của bạn, vì vậy nó không hiển thị cho người dùng khác - nhưng nó cũng không theo bạn đến trình duyệt hoặc thiết bị khác.

## Lọc

Nhấp vào nút **lọc** để mở bảng điều khiển lọc. Nó cung cấp ba cách để lọc, có thể kết hợp:

- **Bộ lọc có sẵn** trong các phần có thể thu gọn phụ thuộc vào loại đối tượng. Đối với người, chẳng hạn, bạn có thể lọc theo năm sinh, năm mất, các thuộc tính của người, số lượng mối quan hệ, thẻ, và liệu một đối tượng là riêng tư hay công khai.
- **Bộ lọc nâng cao** - một trình tạo điều kiện cho các bộ lọc mà các bộ lọc có sẵn không thể diễn đạt, được mô tả [dưới đây](#advanced-filter).
- **GQL** - một trường văn bản cho một truy vấn trong [Ngôn ngữ Truy vấn Gramps](gql.md). Nhập truy vấn và nhấn Enter hoặc nhấp vào **Áp dụng**. Nếu truy vấn không hợp lệ, khung của trường sẽ chuyển sang màu đỏ. Một truy vấn áp dụng trên các bộ lọc khác.

Các bộ lọc đang hoạt động được hiển thị dưới dạng chip ở trên danh sách. Xóa một bộ lọc đơn bằng cách nhấp vào nút xóa của chip, hoặc sử dụng **Xóa tất cả bộ lọc** để xóa tất cả cùng một lúc.

### Bộ lọc nâng cao

Nhấp vào **Bộ lọc nâng cao** ở dưới cùng của bảng điều khiển lọc để mở trình tạo điều kiện. Các điều kiện của nó là các quy tắc lọc được biết đến từ Gramps Desktop, chẳng hạn như "Người có &lt;tên&gt;" hoặc "Tổ tiên của &lt;người&gt;".

- Nhấp vào **Thêm điều kiện** để chọn một quy tắc. Các quy tắc được nhóm thành các danh mục và có thể tìm kiếm theo tên hoặc mô tả.
- Điền vào các tham số của quy tắc. Mỗi tham số có một đầu vào tương ứng, ví dụ như trường ngày, bộ chọn thẻ, hoặc bộ chọn đối tượng cho một người hoặc địa điểm.
- Chọn cách các điều kiện của một nhóm được kết hợp: **Tất cả các điều kiện**, **Bất kỳ điều kiện nào**, hoặc - thông qua menu bên cạnh chúng - **Chính xác một điều kiện**.
- Nhấp vào **Thêm nhóm** để thêm một nhóm điều kiện bên trong một nhóm khác, với cách kết hợp riêng của nó.
- Chọn **Không** trên một điều kiện hoặc nhóm để đảo ngược nó.

Nhấp vào **Áp dụng** để lọc danh sách.

Các bộ lọc có sẵn đang hoạt động khi bạn mở trình tạo xuất hiện ở đó dưới dạng các điều kiện. Nếu bộ lọc bạn xây dựng có thể được diễn đạt bằng các bộ lọc có sẵn, nó sẽ được hiển thị cùng với chúng sau khi áp dụng. Nếu không, nó sẽ được hiển thị dưới dạng một chip **Bộ lọc nâng cao** duy nhất, và bảng điều khiển lọc cung cấp một nút **Chỉnh sửa** để mở lại trình tạo.

!!! note
    Các quy tắc tham chiếu đến các bộ lọc tùy chỉnh được lưu trong Gramps Desktop không có sẵn trong trình tạo. Các quy tắc được hiển thị bằng ngôn ngữ của bạn với Gramps Web API 3.24 hoặc mới hơn.

## Chọn đối tượng và thực hiện hành động hàng loạt

Người dùng có quyền chỉnh sửa sẽ thấy nút **Chọn** bên cạnh nút lọc. Nhấp vào nó để vào chế độ chọn, điều này thêm một hộp kiểm vào mỗi hàng.

Đánh dấu các đối tượng bạn muốn, và một thanh công cụ xuất hiện cho biết có bao nhiêu đối tượng được chọn, cùng với một menu thả xuống **Hành động** và một nút **Áp dụng**.

Hộp kiểm trong tiêu đề bảng chọn tất cả các đối tượng trên trang hiện tại. Nếu có nhiều đối tượng phù hợp với các bộ lọc hiện tại, thanh công cụ sau đó cung cấp **Chọn Tất cả (N)**, chọn tất cả N đối tượng phù hợp trên tất cả các trang. Bỏ đánh dấu một hàng, thay đổi trang hoặc các bộ lọc, hoặc rời khỏi chế độ chọn sẽ kết thúc việc chọn này.

### Xóa

Chọn một hoặc nhiều đối tượng, chọn **Xóa**, và nhấp vào **Áp dụng**. Một hộp thoại xác nhận yêu cầu bạn xác nhận, cảnh báo rằng hành động này không thể hoàn tác.

Xóa hơn mười đối tượng sẽ chạy như một tác vụ nền. Tiến trình của nó được hiển thị bên cạnh nút **Áp dụng** và trong [Thông báo](notifications.md), và danh sách sẽ tải lại khi hoàn tất.

!!! tip
    Các lần xóa được ghi lại trong [lịch sử sửa đổi](revisions.md) như bất kỳ thay đổi nào khác, vì vậy một lần xóa hàng loạt sai có thể được đảo ngược bằng cách hoàn tác giao dịch tương ứng.

### Gộp

Chọn **chính xác hai** đối tượng, chọn **Gộp**, và nhấp vào **Áp dụng**. Một hộp thoại hỏi đối tượng nào trong hai đối tượng nên cung cấp dữ liệu chính cho đối tượng đã gộp; nhấp vào đối tượng bạn muốn giữ làm chính. Dữ liệu của đối tượng còn lại sẽ được gộp vào và các tham chiếu sẽ được cập nhật.

Việc gộp có sẵn cho người, gia đình, sự kiện, địa điểm, nguồn và trích dẫn. Nó không có sẵn cho kho lưu trữ, ghi chú và đối tượng phương tiện.

Trong chế độ xem phương tiện, việc chọn hoạt động cả trong chế độ xem thư viện và chế độ xem danh sách: trong chế độ chọn, nhấp vào một ô hoặc hàng sẽ chuyển đổi trạng thái của nó. **Xóa** là hành động duy nhất có sẵn cho phương tiện.

Nếu bạn chọn một hành động mà không có lựa chọn hợp lệ - ví dụ như gộp với chỉ một đối tượng được chọn - một hộp thoại sẽ giải thích những gì cần thiết.
