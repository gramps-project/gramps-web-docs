## Sao lưu cây gia đình của bạn

Để tạo một bản sao lưu cho cây gia đình của bạn, hãy mở trang Xuất trong Gramps Web và chọn định dạng Gramps XML.

Nhấn vào "xuất" sẽ tạo ra tệp và bắt đầu tải xuống khi nó sẵn sàng.

Lưu ý rằng nếu người dùng Gramps Web của bạn không có quyền xem các hồ sơ riêng tư, việc xuất sẽ không phải là một bản sao lưu đầy đủ, vì nó sẽ không chứa bất kỳ hồ sơ riêng tư nào.

## Chia sẻ cây gia đình của bạn với người dùng của các chương trình gia phả khác

Khi việc chia sẻ dữ liệu gia phả dưới dạng Gramps XML không phải là một lựa chọn, bạn cũng có thể xuất một tệp GEDCOM. Lưu ý rằng điều này không phù hợp như một bản sao lưu cho cây Gramps Web của bạn.

## Sao lưu các tệp phương tiện của bạn

Để sao lưu các tệp phương tiện của bạn, bạn có thể tạo và tải xuống một tệp ZIP chứa tất cả các tệp phương tiện trên trang Xuất.

Lưu ý rằng, đặc biệt đối với các cây lớn, điều này có thể là một thao tác tốn kém cho máy chủ và chỉ nên thực hiện nếu thực sự cần thiết.

Một lựa chọn tốt hơn để sao lưu các tệp phương tiện của bạn một cách thường xuyên là sử dụng [tiện ích mở rộng Gramps Web Sync](sync.md) (mà chính nó không phải là một giải pháp sao lưu) và tạo các bản sao lưu gia tăng trên máy tính cục bộ của bạn.

Trong cả hai trường hợp, nếu người dùng Gramps Web của bạn không có quyền xem các hồ sơ riêng tư, việc xuất sẽ không chứa các tệp của các đối tượng phương tiện riêng tư.

## Di chuyển đến một phiên bản Gramps Web khác

Gramps Web không khóa bạn với một nhà cung cấp cụ thể và bạn có thể luôn di chuyển đến một phiên bản Gramps Web khác mà không mất dữ liệu, và không cần truy cập trực tiếp vào bất kỳ máy chủ nào.

Để thực hiện một cuộc di cư đầy đủ, hãy làm theo các bước sau (giả sử bạn có quyền sở hữu cây):

1. Đi đến trang Xuất và xuất cây của bạn dưới dạng tệp Gramps XML (`.gramps`). Nếu bạn sử dụng [tiện ích mở rộng Sync](sync.md), bạn cũng có thể tạo xuất trong Gramps desktop.
2. Trên trang Xuất, tạo và tải xuống một tệp lưu trữ phương tiện. Nếu bạn sử dụng [tiện ích mở rộng Sync](sync.md), bạn cũng có thể đơn giản nén thư mục phương tiện Gramps cục bộ của bạn thành tệp ZIP.
3. Đi đến Cài đặt > Quản trị > Quản lý người dùng và nhấn nút "Xuất chi tiết người dùng". Nó sẽ tải xuống một tệp JSON.
4. Trong phiên bản Gramps Web mới, mở trang Nhập. Nhập tệp `.gramps` đã xuất ở bước 1.
5. Trên trang Nhập của phiên bản Gramps Web mới, tải lên tệp lưu trữ phương tiện (ZIP).
6. Đi đến Cài đặt > Quản trị > Quản lý người dùng của phiên bản Gramps Web mới. Nhấn nút "Nhập tài khoản người dùng" và tải lên tệp JSON đã tải xuống ở bước 3.

Lưu ý rằng, trong khi tài khoản người dùng của bạn sẽ được di chuyển, tất cả người dùng của bạn sẽ cần đặt lại mật khẩu mới bằng cách sử dụng liên kết "quên mật khẩu", vì mật khẩu được lưu trữ ở dạng mã hóa và không thể xuất ra.
