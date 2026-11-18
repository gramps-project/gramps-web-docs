# Xuất dữ liệu

Trang Xuất cho phép bạn tải xuống dữ liệu cây gia đình ở nhiều định dạng khác nhau, cũng như một kho lưu trữ tất cả các tệp phương tiện.

## Xuất cây gia đình dưới dạng Gramps XML

Để có một bản sao của dữ liệu cây gia đình, hãy mở trang Xuất trong Gramps Web và chọn định dạng Gramps XML. Nhấp vào **Tạo** để tạo tệp, và **Tải xuống** khi nó đã sẵn sàng. Đối với một cây lớn, việc tạo tệp có thể mất một thời gian; bạn có thể rời khỏi trang trong khi chờ đợi và tải xuống tệp sau từ mục của nó trong [thông báo](../user-guide/notifications.md).

Lưu ý rằng nếu người dùng Gramps Web của bạn không có quyền xem các hồ sơ riêng tư, thì xuất sẽ không chứa bất kỳ hồ sơ riêng tư nào.

## Sao lưu cây gia đình của bạn

Để sao lưu hoàn toàn cây – bao gồm cả cài đặt và người dùng của nó – xem [Sao lưu và khôi phục](backups.md). Một xuất Gramps XML có thể được sử dụng như một bản sao lưu của dữ liệu cây gia đình và có thể được khôi phục thông qua [Khôi phục từ Bản sao lưu](backups.md#restore-from-backup).

## Chia sẻ cây gia đình của bạn với người dùng của các chương trình phả hệ khác

Khi chia sẻ dữ liệu phả hệ dưới dạng Gramps XML không phải là một lựa chọn, bạn cũng có thể xuất một tệp GEDCOM. Lưu ý rằng điều này không phù hợp như một bản sao lưu cho cây Gramps Web của bạn.

## Sao lưu các tệp phương tiện của bạn

Để sao lưu các tệp phương tiện của bạn, bạn có thể tạo và tải xuống một kho lưu trữ ZIP của tất cả các tệp phương tiện trên trang Xuất.

Lưu ý rằng, đặc biệt đối với các cây lớn, điều này có thể là một thao tác tốn kém cho máy chủ và chỉ nên thực hiện nếu thật sự cần thiết. Vì lý do này, số lượng kho lưu trữ phương tiện có thể được tạo ra là có giới hạn (mặc định là một mỗi giờ). Nếu bạn đạt giới hạn, thông báo lỗi sẽ hiển thị điều đó.

Một lựa chọn tốt hơn để sao lưu các tệp phương tiện của bạn thường xuyên là sử dụng [tiện ích mở rộng Gramps Web Sync](sync.md) (mà chính nó không phải là một giải pháp sao lưu) và tạo các bản sao lưu gia tăng trên máy tính cục bộ của bạn.

Trong cả hai trường hợp, nếu người dùng Gramps Web của bạn không có quyền xem các hồ sơ riêng tư, thì xuất sẽ không chứa các tệp của các đối tượng phương tiện riêng tư.

## Chuyển đến một phiên bản Gramps Web khác

Gramps Web không khóa bạn với một nhà cung cấp cụ thể và bạn luôn có thể chuyển đến một phiên bản Gramps Web khác mà không mất dữ liệu, và không cần truy cập trực tiếp vào bất kỳ máy chủ nào.

Để thực hiện một cuộc di cư hoàn toàn, hãy làm theo các bước sau (giả sử bạn có quyền sở hữu cây):

1. Đi đến trang Xuất và xuất cây của bạn dưới dạng tệp Gramps XML (`.gramps`). Nếu bạn sử dụng [tiện ích mở rộng Sync](sync.md), bạn cũng có thể tạo xuất trong Gramps desktop.
2. Trên trang Xuất, tạo và tải xuống một kho lưu trữ phương tiện. Nếu bạn sử dụng [tiện ích mở rộng Sync](sync.md), bạn cũng có thể đơn giản ZIP thư mục phương tiện Gramps cục bộ của bạn.
3. Đi đến Cài đặt > Quản trị > Quản lý người dùng và nhấp vào nút "Xuất chi tiết người dùng". Nó sẽ tải xuống một tệp JSON.
4. Trong phiên bản Gramps Web mới, mở trang [Nhập](import.md). Nhập tệp `.gramps` đã xuất ở bước 1.
5. Trên trang Nhập của phiên bản Gramps Web mới, tải lên kho lưu trữ phương tiện (ZIP) dưới [Nhập Tệp Phương tiện](import-media.md).
6. Đi đến Cài đặt > Quản trị > Quản lý người dùng của phiên bản Gramps Web mới. Nhấp vào nút "Nhập tài khoản người dùng" và tải lên tệp JSON đã tải xuống ở bước 3.

Lưu ý rằng, trong khi tài khoản người dùng của bạn sẽ được di chuyển, tất cả người dùng của bạn sẽ cần đặt lại mật khẩu mới bằng cách sử dụng liên kết "quên mật khẩu", vì mật khẩu được lưu trữ dưới dạng mã hóa và không thể xuất.
