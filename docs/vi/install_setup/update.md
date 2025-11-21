# Cập nhật Gramps Web

Nếu bạn đang sử dụng một trong các phương pháp cài đặt dựa trên Docker Compose, việc cập nhật Gramps Web lên phiên bản mới nhất là rất đơn giản. Trong thư mục nơi tệp `docker-compose.yml` của bạn nằm, hãy chạy các lệnh sau

```bash
docker compose pull
docker compose up -d
```

Đối với các lần nhảy phiên bản nhỏ của [Gramps Web API](https://github.com/gramps-project/gramps-web-api), đây là tất cả những gì cần thiết. Tuy nhiên, hãy theo dõi [ghi chú phát hành của Gramps Web API](https://github.com/gramps-project/gramps-web-api/releases), vì có thể có những thay đổi quan trọng cần chú ý hoặc thay đổi cấu hình.

Lưu ý rằng hình ảnh docker mặc định `grampsweb:latest` luôn kết hợp phiên bản mới nhất của API với phiên bản mới nhất của frontend. Nếu bạn muốn nâng cấp hai thành phần này riêng biệt - điều này là khả thi - một thiết lập phức tạp hơn so với mô tả ở đây là cần thiết.
