# Ứng dụng Gramps Web 1-Click trên DigitalOcean

Thay vì [tự thiết lập Gramps Web](deployment.md), bạn cũng có thể sử dụng [Ứng dụng Gramps Web 1-Click trên DigitalOcean](https://marketplace.digitalocean.com/apps/gramps-web?refcode=b1d13ebe86ac&action=deploy). DigitalOcean lưu trữ phiên bản Demo của Gramps Web.

<a href="https://www.digitalocean.com/?refcode=b1d13ebe86ac&utm_campaign=Referral_Invite&utm_medium=Referral_Program&utm_source=badge"><img src="https://web-platforms.sfo2.cdn.digitaloceanspaces.com/WWW/Badge%202.svg" alt="Huy hiệu giới thiệu DigitalOcean" /></a>

Trong quá trình thiết lập, bạn sẽ phải đăng ký tài khoản DigitalOcean và chọn một gói trả phí cho "droplet" (máy ảo) để sử dụng.

Có thể nói đây hiện là cách đơn giản nhất để triển khai phiên bản Gramps Web tự lưu trữ của riêng bạn, được bảo mật bằng SSL, mà không cần sử dụng phần cứng của riêng bạn.

!!! info
    Lưu ý rằng bạn sẽ phải trả phí dịch vụ lưu trữ cho DigitalOcean. Dự án mã nguồn mở Gramps không cung cấp dịch vụ hỗ trợ trả phí.

## Bước 1: Tạo tài khoản DigitalOcean

Tạo tài khoản tại [DigitalOcean](https://www.digitalocean.com/) nếu bạn chưa có.

## Bước 2: Tạo droplet

- Truy cập [Ứng dụng Gramps Web 1-Click](https://marketplace.digitalocean.com/apps/gramps-web?refcode=b1d13ebe86ac&action=deploy) và nhấp vào "Tạo Gramps Web Droplet".
- Chọn gói có ít nhất 2 GB RAM.
- Thiết lập phương thức xác thực cho droplet của bạn
- Nhấp vào "Tạo Droplet"

## Bước 3: Thiết lập tên miền

Bạn sẽ cần một tên miền (hoặc tên miền phụ). Nếu sở hữu một tên miền, hãy trỏ tên miền đó đến địa chỉ IP của droplet. Nếu không, bạn có thể sử dụng một dịch vụ miễn phí như [DuckDNS](https://www.duckdns.org/).

## Bước 4: Đăng nhập vào droplet

SSH vào droplet của bạn. Bạn sẽ thấy thông báo "Chào mừng bạn đến với quá trình thiết lập ứng dụng Gramps Web 1-click trên DigitalOcean!". Nếu không thấy thông báo này, hãy đợi vài phút rồi thử lại (quá trình cài đặt vẫn chưa hoàn tất).

Tập lệnh thiết lập sẽ yêu cầu bạn nhập tên miền (ví dụ: `mygrampswebinstance.duckdns.org`) và địa chỉ e-mail (cần thiết cho chứng chỉ Let's Encrypt). Ngoài ra, tập lệnh cũng sẽ hỏi các thiết lập SMTP mà Gramps Web sử dụng để gửi e-mail, chẳng hạn như e-mail đặt lại mật khẩu; hãy để trống máy chủ SMTP để bỏ qua bước này.

Khi hoàn tất, hãy chờ quá trình thiết lập hoàn tất trong nền

## Bước 5: Khởi chạy Gramps Web

Giờ đây, phiên bản Gramps Web của bạn sẽ có thể truy cập tại thư mục gốc của tên miền, với chứng chỉ SSL hợp lệ và sẽ hiển thị trình hướng dẫn chạy lần đầu.

## Thay đổi cấu hình sau này

Tập lệnh thiết lập lưu URL cơ sở và các thiết lập e-mail trong tệp `/root/letsencrypt.env` dưới dạng [tùy chọn cấu hình](configuration.md) có tiền tố `GRAMPSWEB_`, ví dụ:

```
GRAMPSWEB_EMAIL_HOST=smtp.example.com
GRAMPSWEB_EMAIL_PORT=587
GRAMPSWEB_EMAIL_USE_STARTTLS=true
```

Để thêm hoặc thay đổi các thiết lập, hãy chỉnh sửa tệp này trên droplet và áp dụng thay đổi bằng lệnh

```bash
cd /opt/grampsweb && docker compose up -d
```
