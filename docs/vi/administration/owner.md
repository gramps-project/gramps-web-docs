# Tạo tài khoản cho chủ sở hữu cây

Trước khi bạn có thể bắt đầu sử dụng Gramps Web, bạn cần tạo một tài khoản cho chủ sở hữu cây. Nếu không có tài khoản người dùng nào tồn tại cho một cây nhất định, một mẫu sẽ được hiển thị để tạo tài khoản. Mẫu này phụ thuộc vào cấu hình máy chủ là cho một cây đơn hay cho nhiều cây.

## Cấu hình một cây: tạo tài khoản quản trị viên

Trên một máy chủ có cấu hình một cây, khi chưa có tài khoản người dùng nào tồn tại, việc mở Gramps Web sẽ hiển thị một mẫu để tạo tài khoản quản trị viên. Người dùng quản trị viên sẽ là chủ sở hữu của cây (đơn) và là quản trị viên của cài đặt. Mẫu cũng cho phép thiết lập cấu hình email cần thiết cho thông báo qua email (ví dụ: đặt lại mật khẩu người dùng). Nếu cấu hình email đã được thêm qua tệp cấu hình hoặc biến môi trường trên máy chủ, phần này của mẫu có thể để trống.

## Cấu hình nhiều cây: tạo tài khoản quản trị viên

Trong cấu hình nhiều cây, cùng một mẫu để tạo tài khoản quản trị viên sẽ được hiển thị nếu không có người dùng nào tồn tại *trong bất kỳ cây nào*, tức là khi máy chủ vừa mới được tạo.

## Cấu hình nhiều cây: tạo tài khoản chủ sở hữu cây

Trong cấu hình nhiều cây, mỗi người dùng được gắn với một cây duy nhất. Ngay cả khi người dùng đã tồn tại trong các cây khác, một chủ sở hữu cây có thể được tạo trong giao diện web nếu chưa có chủ sở hữu *cho cây này*.

Tuy nhiên, mẫu tạo chủ sở hữu sẽ không được hiển thị tự động trên trang chính của Gramps Web, điều này giống nhau cho tất cả các cây. Thay vào đó, nó có thể được truy cập tại `https://my-gramps-instance/firstrun/my-tree-id`, trong đó `https://my-gramps-instance` là địa chỉ cơ sở của cài đặt Gramps Web của bạn, và `my-tree-id` là ID của cây của bạn.

Một quy trình khả thi cho một quản trị viên trang web để tạo một cây mới là

- Tạo một cây thông qua REST API, lấy ID cây của cây mới
- Chia sẻ liên kết đến mẫu tạo chủ sở hữu với ID cây phù hợp cho chủ sở hữu cây tiềm năng

Mẫu tạo chủ sở hữu cây tương tự như mẫu tạo quản trị viên được mô tả ở trên, ngoại trừ việc nó không cho phép thay đổi cấu hình email (điều này chỉ được phép cho quản trị viên).
