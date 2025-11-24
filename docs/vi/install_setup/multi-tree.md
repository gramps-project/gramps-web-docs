# Cài đặt để lưu trữ nhiều cây

Theo mặc định, Gramps Web chỉ cho phép truy cập vào một cơ sở dữ liệu cây gia đình duy nhất (“cây”), được chỉ định trong tệp cấu hình.

Tuy nhiên, bắt đầu từ phiên bản 0.7.0 của backend Gramps Web API, cũng có thể phục vụ nhiều cây từ một cài đặt duy nhất. Tuy nhiên, mỗi người dùng (hiện tại) bị ràng buộc với một cây duy nhất, vì vậy cài đặt này không phù hợp để chia sẻ cây giữa các người dùng, mà để lưu trữ nhiều phiên bản Gramps Web tách biệt.

## Bật hỗ trợ nhiều cây

Để bật hỗ trợ nhiều cây, tùy chọn cấu hình `TREE` phải được đặt thành một dấu hoa thị duy nhất `*`, ví dụ trong một tệp cấu hình:

```python
TREE = "*"
```

Điều này sẽ làm cho tất cả các cây trong thư mục cơ sở dữ liệu Gramps của máy chủ có thể truy cập được (với quyền truy cập người dùng đủ). ID của cây là tên của thư mục con. Bạn có thể liệt kê các cây hiện có (tên và ID) với lệnh

```bash
python -m gramps_webapi --config /app/config/config.cfg tree list
```

Ngoài ra, bạn nên đặt tùy chọn cấu hình `MEDIA_PREFIX_TREE` thành `True` để đảm bảo các tệp phương tiện được lưu trữ trong các thư mục con riêng biệt. Nếu không, người dùng có thể truy cập các tệp phương tiện thuộc về một cây mà họ không có quyền truy cập!

## Thêm tài khoản người dùng vào một cây cụ thể

Để thêm một người dùng vào một cây cụ thể, chỉ cần thêm tùy chọn dòng lệnh `--tree TREEID` vào lệnh thêm người dùng. Bạn cũng có thể POST đến điểm cuối `/users/` với thuộc tính `tree` được thiết lập trong tải trọng JSON.

Tên người dùng và địa chỉ email phải là duy nhất trên *tất cả* các cây.

## Tạo một cây mới

Để tạo một cây mới, nên POST đến điểm cuối `/trees/` thay vì sử dụng Gramps CLI. Điều này sẽ sử dụng UUIDv4 làm ID cây, điều này dẫn đến bảo mật bổ sung vì tên không thể đoán được. Hiện tại, chỉ SQLite được hỗ trợ cho các cây mới được tạo.

## Ủy quyền

Để ủy quyền (lấy mã thông báo), chỉ cần tên người dùng và mật khẩu là cần thiết, giống như trong chế độ một cây, vì ID cây đã biết cho mỗi người dùng, vì vậy không cần cung cấp nó.

## Di chuyển các tệp phương tiện hiện có

Nếu bạn muốn di chuyển một phiên bản Gramps Web hiện có sang hỗ trợ nhiều cây và đang sử dụng các tệp phương tiện cục bộ, bạn có thể đơn giản di chuyển chúng vào một thư mục con của vị trí gốc với ID cây làm tên.

Nếu bạn đang sử dụng các tệp phương tiện được lưu trữ trên S3, bạn có thể sử dụng kịch bản được cung cấp trong thư mục `scripts` của kho `gramps-web-api`:

```bash
python scripts/s3_rename.py BUCKET_NAME TREE_ID
```

Điều này giả định rằng các khóa truy cập liên quan đã được thiết lập dưới dạng biến môi trường.

## Di chuyển cơ sở dữ liệu người dùng hiện có

Nếu bạn muốn bật hỗ trợ nhiều cây và tái sử dụng người dùng hiện có, bạn cần gán họ cho một cây cụ thể. Bạn có thể sử dụng lệnh sau được cung cấp cho mục đích này,

```bash
python -m gramps_webapi --config /app/config/config.cfg user fill-tree TREE_ID
```

## Tùy chỉnh giao diện frontend

Trang đăng ký có thể truy cập từ trang đăng nhập không hoạt động trong cài đặt nhiều cây, vì một cây cần được chỉ định cho việc đăng ký. Do đó, nên đặt `hideRegisterLink` thành `true` trong [cấu hình frontend](frontend-config.md).
