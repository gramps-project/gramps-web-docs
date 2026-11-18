# Danh sách

Mỗi loại đối tượng trong Gramps Web đều có chế độ xem danh sách: Người, Gia đình, Sự kiện, Địa điểm, Nguồn, Trích dẫn, Kho lưu trữ, Ghi chú và Phương tiện. Tất cả chúng đều hoạt động theo cùng một cách và chia sẻ các công cụ giống nhau để sắp xếp, lọc và chỉnh sửa hàng loạt.

## Sắp xếp và phân trang

Nhấp vào tiêu đề cột để sắp xếp theo cột đó; nhấp lại để đảo ngược thứ tự. Việc sắp xếp được thực hiện bởi máy chủ, vì vậy nó áp dụng cho toàn bộ danh sách, không chỉ cho trang bạn đang xem.

Các danh sách dài được chia thành các trang. Sử dụng các điều khiển phân trang ở dưới cùng để di chuyển giữa chúng.

Trên các màn hình hẹp, bảng tự động chuyển sang bố cục gọn gàng, vì vậy các chế độ xem danh sách vẫn có thể sử dụng trên điện thoại.

## Chọn cột

Nhấp vào biểu tượng bánh răng ở cuối bên phải của thanh công cụ phía trên danh sách để mở hộp thoại **Cột**. Đánh dấu hoặc bỏ đánh dấu một cột để hiển thị hoặc ẩn nó. **Đặt lại** khôi phục lựa chọn mặc định cho danh sách đó.

Ít nhất một cột phải vẫn hiển thị, vì vậy cột còn lại cuối cùng không thể bị bỏ đánh dấu.

Ngoài các cột mặc định, mỗi danh sách cung cấp một cột **Thẻ** và, đối với những người dùng có thể xem các hồ sơ riêng tư, một cột **Riêng tư** hiển thị một biểu tượng khóa cho mỗi đối tượng riêng tư. Nếu bạn đã thay đổi lựa chọn cột của một danh sách trước đó, các cột mới như **Thẻ** sẽ không được thêm tự động; hãy đánh dấu chúng trong hộp thoại.

Lựa chọn cột của bạn được ghi nhớ theo loại đối tượng và theo cây gia đình. Nó được lưu trữ trong trình duyệt của bạn, vì vậy nó không hiển thị cho những người dùng khác – nhưng nó cũng không theo bạn đến một trình duyệt hoặc thiết bị khác.

## Lọc

Nhấp vào nút **lọc** để mở bảng điều khiển lọc. Nó cung cấp ba cách để lọc, có thể kết hợp:

- **Bộ lọc có sẵn** trong các phần có thể thu gọn tùy thuộc vào loại đối tượng. Đối với người, ví dụ, bạn có thể lọc theo tên, năm sinh, năm mất, các thuộc tính của người, số lượng mối quan hệ, thẻ, và liệu một đối tượng là riêng tư hay công khai. Gia đình có thể được lọc theo tên của cha, mẹ hoặc một đứa trẻ, nguồn theo tác giả, và địa điểm cũng như kho lưu trữ theo loại của chúng.
- **Bộ lọc nâng cao** – một trình tạo điều kiện cho các bộ lọc mà các bộ lọc có sẵn không thể diễn đạt, được mô tả [dưới đây](#advanced-filter).
- **GOQL** – một trường văn bản cho một biểu thức trong [Ngôn ngữ truy vấn đối tượng Gramps](goql.md), với định dạng cú pháp. Gõ biểu thức và nhấn Enter hoặc nhấp vào **Áp dụng**. Nếu biểu thức không hợp lệ, trường sẽ được đánh dấu là lỗi. Một biểu thức áp dụng trên các bộ lọc khác.

Các bộ lọc đang hoạt động được hiển thị dưới dạng chip trong một hàng bên dưới thanh công cụ. Xóa một bộ lọc đơn lẻ bằng cách nhấp vào nút xóa của chip, hoặc sử dụng **Xóa tất cả bộ lọc** để xóa tất cả cùng một lúc.

### Bộ lọc nâng cao

Nhấp vào **Bộ lọc nâng cao** ở dưới cùng của bảng điều khiển lọc để mở trình tạo điều kiện. Các điều kiện của nó là các quy tắc lọc được biết đến từ Gramps Desktop, chẳng hạn như "Người với &lt;tên&gt;" hoặc "Tổ tiên của &lt;người&gt;".

- Nhấp vào **Thêm điều kiện** để chọn một quy tắc. Các quy tắc được nhóm thành các danh mục và có thể được tìm kiếm theo tên hoặc mô tả.
- Điền vào các tham số của quy tắc. Mỗi tham số có một đầu vào tương ứng, ví dụ như một trường ngày, một trình chọn thẻ, hoặc một trình chọn đối tượng cho một người hoặc địa điểm.
- Chọn cách mà các điều kiện của một nhóm được kết hợp: **Tất cả các điều kiện**, **Bất kỳ điều kiện nào**, hoặc – qua menu bên cạnh chúng – **Chính xác một điều kiện**.
- Nhấp vào **Thêm nhóm** để thêm một nhóm điều kiện bên trong một nhóm khác, với cách kết hợp riêng của nó.
- Chọn **Không** trên một điều kiện hoặc nhóm để đảo ngược nó.

Nhấp vào **Áp dụng** để lọc danh sách.

Các bộ lọc có sẵn và biểu thức GOQL đang hoạt động khi bạn mở trình tạo xuất hiện ở đó dưới dạng các điều kiện. Một biểu thức GOQL cũng có thể được thêm như một điều kiện riêng, ví dụ để kết hợp nhiều biểu thức với **Bất kỳ điều kiện nào**. Nếu bộ lọc bạn xây dựng có thể được diễn đạt bằng các bộ lọc có sẵn, nó sẽ được hiển thị cùng với chúng sau khi áp dụng. Nếu không, nó sẽ được hiển thị như một chip **Bộ lọc nâng cao** đơn lẻ, và bảng điều khiển lọc cung cấp một nút **Chỉnh sửa** để mở lại trình tạo.

!!! note
    Các quy tắc tham chiếu đến các bộ lọc tùy chỉnh được lưu trong Gramps Desktop không có sẵn trong trình tạo. Các quy tắc được hiển thị bằng ngôn ngữ của bạn với Gramps Web API 3.24 hoặc mới hơn.

#### Bộ lọc đã lưu

Để sử dụng lại một bộ lọc bạn đã xây dựng, nhấp vào **Lưu** trong trình tạo điều kiện và đặt cho nó một tên. Lưu dưới một tên đã tồn tại sẽ thay thế bộ lọc đó. **Bộ lọc đã lưu** trong trình tạo liệt kê các bộ lọc đã lưu cho loại đối tượng hiện tại; chọn một cái sẽ tải nó vào trình tạo, nơi bạn có thể thay đổi trước khi nhấp vào **Áp dụng**.

Các bộ lọc đã lưu được lưu trữ trong trình duyệt của bạn, theo cây gia đình và loại đối tượng, vì vậy chúng không có sẵn cho những người dùng khác hoặc trên các thiết bị khác của bạn.

Một bộ lọc đã lưu có thể ngừng hoạt động khi cây thay đổi, ví dụ nếu nó tham chiếu đến một người đã bị xóa (trình chọn đối tượng sau đó hiển thị "Không tìm thấy"). Một bộ lọc như vậy không thể được áp dụng hoặc lưu cho đến khi điều kiện được sửa chữa.

## Chọn đối tượng và thực hiện hành động hàng loạt

Người dùng có quyền chỉnh sửa sẽ thấy một nút **Chọn** bên cạnh nút lọc. Nhấp vào nó để vào chế độ chọn, điều này sẽ thêm một ô kiểm vào mỗi hàng.

Đánh dấu các đối tượng bạn muốn, và một thanh công cụ sẽ xuất hiện hiển thị số lượng đã chọn, cùng với một menu thả xuống **Hành động** và một nút **Áp dụng**.

Ô kiểm trong tiêu đề bảng chọn tất cả các đối tượng trên trang hiện tại. Nếu có nhiều đối tượng phù hợp với các bộ lọc hiện tại, thanh công cụ sau đó cung cấp **Chọn tất cả (N)**, chọn tất cả N đối tượng phù hợp trên tất cả các trang. Bỏ đánh dấu một hàng, thay đổi trang hoặc các bộ lọc, hoặc rời khỏi chế độ chọn sẽ kết thúc lựa chọn này.

### Xóa

Chọn một hoặc nhiều đối tượng, chọn **Xóa**, và nhấp vào **Áp dụng**. Một hộp thoại xác nhận yêu cầu bạn xác nhận, cảnh báo rằng hành động này không thể hoàn tác.

Xóa hơn mười đối tượng sẽ chạy như một tác vụ nền. Tiến trình của nó sẽ được hiển thị bên cạnh nút **Áp dụng** và trong [Thông báo](notifications.md), và danh sách sẽ được tải lại khi hoàn tất.

!!! tip
    Các lần xóa được ghi lại trong [lịch sử sửa đổi](revisions.md) như bất kỳ thay đổi nào khác, vì vậy một lần xóa hàng loạt nhầm lẫn có thể được đảo ngược bằng cách hoàn tác giao dịch tương ứng.

### Thẻ và quyền riêng tư

Các hành động **Thêm Thẻ**, **Xóa Thẻ**, và **Riêng tư** thay đổi tất cả các đối tượng đã chọn cùng một lúc (cần Gramps Web API 3.26 hoặc mới hơn):

- **Thêm Thẻ** thêm một thẻ hiện có hoặc một thẻ mới mà bạn tạo trong hộp thoại.
- **Xóa Thẻ** xóa một thẻ khỏi các đối tượng đã chọn có thẻ đó.
- **Riêng tư** đánh dấu các đối tượng đã chọn là riêng tư hoặc công khai. Điều này chỉ thay đổi các đối tượng đó, không phải các phần của chúng hoặc các hồ sơ mà chúng liên kết đến – xem [Hồ sơ riêng tư](privacy.md).

Giống như việc xóa, chỉnh sửa hơn mười đối tượng sẽ chạy như một tác vụ nền. Các thay đổi được ghi lại trong [lịch sử sửa đổi](revisions.md) như một giao dịch, vì vậy chúng có thể được hoàn tác cùng nhau.

### Gộp

Chọn **chính xác hai** đối tượng, chọn **Gộp**, và nhấp vào **Áp dụng**. Một hộp thoại hỏi đối tượng nào trong hai đối tượng nên cung cấp dữ liệu chính cho đối tượng được gộp; nhấp vào đối tượng bạn muốn giữ làm chính. Dữ liệu của đối tượng còn lại sẽ được gộp vào nó và các tham chiếu sẽ được cập nhật.

Việc gộp có sẵn cho người, gia đình, sự kiện, địa điểm, nguồn và trích dẫn. Nó không có sẵn cho kho lưu trữ, ghi chú và đối tượng phương tiện.

Trong chế độ xem phương tiện, việc chọn hoạt động cả trong chế độ xem thư viện và chế độ xem danh sách: trong chế độ chọn, nhấp vào một ô hoặc hàng sẽ chuyển đổi nó. Các đối tượng phương tiện không thể được gộp.

Nếu bạn chọn một hành động mà không có lựa chọn hợp lệ – ví dụ như gộp với chỉ một đối tượng được chọn – một hộp thoại sẽ giải thích những gì cần thiết.
