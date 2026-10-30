# Ứng dụng Gramps Web DigitalOcean 1-Click

Thay vì [thiết lập Gramps Web tự mình](deployment.md), bạn cũng có thể sử dụng [Ứng dụng Gramps Web DigitalOcean 1-Click](https://marketplace.digitalocean.com/apps/gramps-web?refcode=b1d13ebe86ac&action=deploy). Digital Ocean lưu trữ phiên bản Demo của Gramps Web.

<a href="https://www.digitalocean.com/?refcode=b1d13ebe86ac&utm_campaign=Referral_Invite&utm_medium=Referral_Program&utm_source=badge"><img src="https://web-platforms.sfo2.cdn.digitaloceanspaces.com/WWW/Badge%202.svg" alt="DigitalOcean Referral Badge" /></a>

Trong quá trình thiết lập, bạn sẽ phải đăng ký một tài khoản với DigitalOcean và chọn một gói trả phí cho "droplet" (máy ảo) để sử dụng.

Có thể nói, đây hiện là cách đơn giản nhất để triển khai một phiên bản Gramps Web tự lưu trữ của riêng bạn, được bảo mật bằng SSL, mà không cần sử dụng phần cứng của riêng bạn.

!!! info
    Lưu ý rằng bạn sẽ phải trả tiền cho DigitalOcean cho các dịch vụ lưu trữ. Dự án mã nguồn mở Gramps không cung cấp hỗ trợ trả phí.

## Bước 1: Tạo tài khoản DigitalOcean

Tạo một tài khoản tại [DigitalOcean](https://www.digitalocean.com/) nếu bạn chưa có.

## Bước 2: Tạo droplet

- Truy cập [Ứng dụng Gramps Web 1-Click](https://marketplace.digitalocean.com/apps/gramps-web?refcode=b1d13ebe86ac&action=deploy) và nhấp vào "Tạo Droplet Gramps Web".
- Chọn một gói có ít nhất 2 GB RAM.
- Thiết lập xác thực cho droplet của bạn
- Nhấp vào "Tạo Droplet"

## Bước 3: Thiết lập tên miền

Bạn sẽ cần một tên miền (hoặc tên miền phụ). Nếu bạn sở hữu một tên miền, hãy trỏ nó đến địa chỉ IP của droplet của bạn. Nếu không, bạn có thể sử dụng dịch vụ miễn phí như [DuckDNS](https://www.duckdns.org/).

## Bước 4: Đăng nhập vào droplet của bạn

SSH vào droplet của bạn. Bạn sẽ thấy thông điệp "Chào mừng đến với thiết lập ứng dụng Gramps Web DigitalOcean 1-click!". Nếu không phải như vậy, hãy đợi vài phút và thử lại (cài đặt vẫn chưa hoàn tất).

Kịch bản thiết lập sẽ yêu cầu bạn nhập tên miền (ví dụ: `mygrampswebinstance.duckdns.org`) và một địa chỉ e-mail (cần thiết cho chứng chỉ Let's Encrypt). Tùy chọn, nó cũng sẽ yêu cầu thông tin cấu hình SMTP mà Gramps Web sử dụng để gửi e-mail, ví dụ: cho việc đặt lại mật khẩu; để trống thông tin máy chủ SMTP để bỏ qua bước này.

Khi điều này hoàn tất, hãy đợi cho quá trình thiết lập hoàn tất ở chế độ nền.

## Bước 5: Khởi động Gramps Web

Phiên bản Gramps Web của bạn giờ đây nên có thể truy cập tại gốc của tên miền của bạn, với chứng chỉ SSL hợp lệ, và nó sẽ hiển thị trợ lý lần đầu chạy.

## Thay đổi cấu hình sau này

Kịch bản thiết lập lưu trữ URL cơ sở và các cài đặt e-mail trong tệp `/root/letsencrypt.env` dưới dạng [các tùy chọn cấu hình](configuration.md) được tiền tố bằng `GRAMPSWEB_`, ví dụ:

```
GRAMPSWEB_EMAIL_HOST=smtp.example.com
GRAMPSWEB_EMAIL_PORT=587
GRAMPSWEB_EMAIL_USE_STARTTLS=true
```

Để thêm hoặc thay đổi cài đặt, hãy chỉnh sửa tệp này trên droplet và áp dụng thay đổi với

```bash
cd /opt/grampsweb && docker compose up -d
