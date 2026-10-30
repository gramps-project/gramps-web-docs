# Thiết lập TrueNAS

Hướng dẫn này giải thích cách thiết lập Gramps Web trên TrueNAS Community Edition 25.04.

!!! warning
    Hướng dẫn này dành cho TrueNAS Community Edition 25.04 hoặc phiên bản mới hơn, đã giới thiệu một hệ thống ứng dụng dựa trên Docker Compose mới. Nó không áp dụng cho các phiên bản trước của TrueNAS.

## Các yêu cầu trước

- TrueNAS Community Edition 25.04 hoặc phiên bản mới hơn
- Kiến thức cơ bản về giao diện web của TrueNAS
- Một dataset để lưu trữ dữ liệu Gramps Web

## Tổng quan

TrueNAS Community Edition 25.04 đã giới thiệu một hệ thống ứng dụng dựa trên Docker Compose mới thay thế cho phương pháp dựa trên Helm chart trước đó. Hướng dẫn này sẽ hướng dẫn bạn tạo một ứng dụng tùy chỉnh cho Gramps Web bằng cách sử dụng Docker Compose.

## Bước 1: Chuẩn bị Lưu trữ

1. Điều hướng đến **Datasets** trong giao diện web của TrueNAS
2. Tạo một dataset mới cho Gramps Web (ví dụ, `grampsweb`). Ghi lại đường dẫn đầy đủ đến dataset này, ví dụ, `/mnt/storage/grampsweb`, vì bạn sẽ cần nó sau này.

Tạo các thư mục con cho các thành phần khác nhau:
- `users` - Cơ sở dữ liệu người dùng
- `database` - Tập tin cơ sở dữ liệu Gramps
- `media` - Tập tin phương tiện

## Bước 2: Tạo Ứng dụng Docker Compose

1. Điều hướng đến **Apps** trong giao diện web của TrueNAS
2. Nhấp vào **Discover Apps**
3. Tìm kiếm "Gramps Web" và nhấp vào nó
4. Nhấp "Install"

Điều này sẽ đưa bạn đến trang cấu hình ứng dụng.

## Bước 3: Cấu hình Ứng dụng

### Cấu hình Gramps Web

- **Múi giờ:** Đặt thành múi giờ địa phương của bạn (ví dụ, `Europe/Berlin`)
- **Mật khẩu Redis:** Đặt một mật khẩu cho Redis. Mật khẩu này chỉ được sử dụng nội bộ bởi ứng dụng.
- **Tắt telemetry:** vui lòng để ô này không được chọn – xem [tại đây để biết chi tiết](telemetry.md).
- **Khóa bí mật:** rất quan trọng để bạn đặt giá trị này thành một giá trị mạnh và duy nhất. Xem [cấu hình máy chủ](configuration.md#existing-configuration-settings) để biết hướng dẫn cách tạo một khóa ngẫu nhiên.
- **Biến Môi trường Bổ sung:** Bạn sẽ cần đặt tất cả các [tùy chọn cấu hình](configuration.md) bổ sung dưới dạng biến môi trường có tiền tố `GRAMPSWEB_`. Vui lòng kiểm tra tài liệu [cấu hình](configuration.md) một cách chi tiết – ví dụ như thực tế rằng các giá trị boolean cần được đặt là `true` hoặc `false` (tất cả chữ thường) trong trường hợp các biến môi trường, một cạm bẫy phổ biến.

Vui lòng **ít nhất** đặt `GRAMPSWEB_BASE_URL` thành URL mà phiên bản Gramps Web của bạn sẽ có thể truy cập – điều này là cần thiết cho hoạt động đúng.

Bạn cũng có thể muốn thiết lập cấu hình email ở giai đoạn này, điều này là cần thiết ví dụ cho việc đặt lại mật khẩu. Các biến môi trường liên quan là:

- `GRAMPSWEB_EMAIL_HOST`
- `GRAMPSWEB_EMAIL_HOST_USER`
- `GRAMPSWEB_EMAIL_HOST_PASSWORD`
- `GRAMPSWEB_DEFAULT_FROM_EMAIL`

Tất cả các cài đặt cấu hình có thể được thay đổi sau bằng cách nhấp "Edit" trong giao diện Ứng dụng TrueNAS.

### Cấu hình Lưu trữ

- **Lưu trữ Người dùng:** Chọn đường dẫn đến thư mục `users` mà bạn đã tạo trước đó.
- **Lưu trữ Chỉ mục:** Bạn có thể để cài đặt mặc định "ixVolume (Dataset được tạo tự động bởi hệ thống)"
- **Lưu trữ Bộ nhớ Cache Hình thu nhỏ:** Bạn có thể để cài đặt mặc định "ixVolume (Dataset được tạo tự động bởi hệ thống)"
- **Lưu trữ Cache:** Bạn có thể để cài đặt mặc định "ixVolume (Dataset được tạo tự động bởi hệ thống)"
- **Lưu trữ Phương tiện:** Chọn đường dẫn đến thư mục `media` mà bạn đã tạo trước đó.
- **Lưu trữ Cơ sở dữ liệu Gramps:** Chọn đường dẫn đến thư mục `database` mà bạn đã tạo trước đó.

### Cấu hình Tài nguyên

Chúng tôi khuyên bạn nên phân bổ ít nhất 2 CPU và 4096 MB RAM để đảm bảo hoạt động mượt mà.

## Bước 4: Truy cập Gramps Web

Khi ứng dụng đã được triển khai, bạn có thể truy cập Gramps Web bằng cách nhấp vào nút "Web UI" trong giao diện Ứng dụng TrueNAS. Bạn sẽ thấy wizard hướng dẫn "Chào mừng đến với Gramps Web".

Nếu bạn muốn cho phép người dùng truy cập giao diện Gramps Web của bạn, **không** phơi bày ứng dụng trực tiếp ra internet, mà hãy tiến hành đến bước tiếp theo.

## Bước 5: Thiết lập Proxy Ngược

Để phơi bày phiên bản Gramps Web của bạn một cách an toàn cho người dùng, nên thiết lập một proxy ngược. Điều này cho phép bạn quản lý chứng chỉ SSL/TLS và kiểm soát quyền truy cập.

Tùy chọn dễ nhất là sử dụng ứng dụng Nginx Proxy Manager chính thức của TrueNAS. Tìm kiếm ứng dụng trong giao diện Ứng dụng TrueNAS và cài đặt nó. Bạn có thể để tất cả các cài đặt ở mặc định, nhưng chúng tôi khuyên bạn nên đặt một biến môi trường bổ sung: `DISABLE_IPV6` với giá trị `true` để tránh các vấn đề liên quan đến IPv6 tiềm ẩn.

Khi đã triển khai, hãy mở giao diện web của Nginx Proxy Manager và tạo một máy chủ proxy mới với các cài đặt sau:

- Scheme: `http`
- Forward Hostname / IP: tên máy chủ của máy chủ TrueNAS của bạn (ví dụ: `truenas`)
- Forward Port: cổng được gán cho ứng dụng Gramps Web của bạn (kiểm tra giao diện Ứng dụng TrueNAS để biết cổng chính xác)
- Trong tab "SSL", kiểm tra "Force SSL"
- Dưới "SSL Certificates", chọn "Add SSL Certificate" > "Let's Encrypt" để tạo một chứng chỉ Let's Encrypt mới cho miền của bạn.

Vui lòng xem tài liệu [Nginx Proxy Manager](https://nginxproxymanager.com/guide/) để biết thêm chi tiết về cách cấu hình bộ định tuyến của bạn và nhận chứng chỉ SSL.
