# Thiết lập HTTPS với Let's Encrypt và Docker Compose

Khi được phục vụ trên internet công cộng, Gramps Web **phải** sử dụng mã hóa HTTPS.

Một tùy chọn đặc biệt tiện lợi là sử dụng một proxy ngược Nginx được docker hóa với việc tạo chứng chỉ Let's Encrypt tự động. Điều này được thực hiện với [docker-compose.yml](https://raw.githubusercontent.com/gramps-project/gramps-web-docs/main/examples/docker-compose-letsencrypt/docker-compose.yml).
(Tệp [nginx_proxy.conf](https://raw.githubusercontent.com/gramps-project/gramps-web-docs/main/examples/docker-compose-letsencrypt/nginx_proxy.conf) cần được lưu trữ trong cùng một thư mục để cho phép tải lên các tệp phương tiện lớn vào Gramps Web.)

Vui lòng xem tài liệu [acme-companion](https://github.com/nginx-proxy/acme-companion) để biết cách thiết lập miền của bạn.
