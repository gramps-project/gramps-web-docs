# Triển khai Gramps Web với Docker

Tùy chọn thuận tiện nhất để lưu trữ Gramps Web trên máy chủ của bạn (hoặc máy chủ ảo) là sử dụng Docker Compose.

Chúng tôi giả định rằng Docker và Docker Compose đã được cài đặt trên hệ thống của bạn. Bạn có thể sử dụng Windows, Mac OS hoặc Linux làm hệ thống máy chủ. Các kiến trúc được hỗ trợ không chỉ bao gồm x86-64 (hệ thống máy tính để bàn), mà còn cả các hệ thống ARM như Raspberry Pi, có thể hoạt động như một máy chủ web chi phí thấp nhưng đủ mạnh.

!!! note
    Bạn không cần cài đặt Gramps trên máy chủ vì nó đã được chứa trong hình ảnh docker.


## Bước 1: Cấu hình Docker

Tạo một tệp mới trên máy chủ có tên `docker-compose.yml` và chèn nội dung sau: [docker-compose.yml](https://raw.githubusercontent.com/gramps-project/gramps-web-docs/main/examples/docker-compose-base/docker-compose.yml).



Điều này sẽ tạo ra sáu volume có tên để đảm bảo rằng tất cả dữ liệu liên quan sẽ được lưu giữ khi khởi động lại container.

!!! warning
    Điều trên sẽ làm cho API có sẵn trên cổng 80 của máy chủ **không có bảo vệ SSL/TLS**. Bạn có thể sử dụng điều này cho việc kiểm tra cục bộ, nhưng đừng để nó trực tiếp trên internet, điều này hoàn toàn không an toàn!

## Bước 2: Bảo mật truy cập với SSL/TLS

API web **phải** được phục vụ cho internet công cộng qua HTTPS. Có một số tùy chọn, ví dụ:

- Sử dụng dịch vụ lưu trữ docker bao gồm SSL/TLS tự động
- Sử dụng Nginx Reverse Proxy với chứng chỉ Let's Encrypt

Xem [Docker với Let's Encrypt](lets_encrypt.md) để biết cách thiết lập tùy chọn đầu tiên.

Nếu bạn dự định chỉ sử dụng Gramps Web trên mạng cục bộ của mình, bạn có thể bỏ qua bước này.

## Bước 3: Khởi động máy chủ

Chạy

```
docker compose up -d
```

Khi chạy lần đầu tiên, ứng dụng sẽ hiển thị một wizard khởi động lần đầu cho phép bạn

- Tạo một tài khoản cho người dùng chủ sở hữu (quản trị viên)
- Đặt một số tùy chọn cấu hình cần thiết
- Nhập một cây gia đình ở định dạng Gramps XML (`.gramps`)

## Bước 4: Tải lên tệp phương tiện

Có một số tùy chọn để tải lên tệp phương tiện.

- Khi sử dụng các tệp được lưu trữ trên cùng một máy chủ với Gramps Web, bạn có thể gắn một thư mục vào container Docker thay vì sử dụng một volume có tên, tức là `/home/server_user/gramps_media/:/app/media` thay vì `gramps_media:/app/media`, và tải lên các tệp phương tiện của bạn ở đó.
- Khi sử dụng các tệp phương tiện [được lưu trữ trên S3](s3.md), bạn có thể sử dụng tiện ích mở rộng S3 Media Uploader
- Tùy chọn có lẽ thuận tiện nhất là sử dụng [Gramps Web Sync](../administration/sync.md).
