# Gramps Web DigitalOcean 1-Click App

Thay vì [thiết lập Gramps Web tự mình](deployment.md), bạn cũng có thể sử dụng [Gramps Web DigitalOcean 1-Click App](https://marketplace.digitalocean.com/apps/gramps-web?refcode=b1d13ebe86ac&action=deploy). Digital Ocean lưu trữ phiên bản Demo của Gramps Web.

<a href="https://www.digitalocean.com/?refcode=b1d13ebe86ac&utm_campaign=Referral_Invite&utm_medium=Referral_Program&utm_source=badge"><img src="https://web-platforms.sfo2.cdn.digitaloceanspaces.com/WWW/Badge%202.svg" alt="DigitalOcean Referral Badge" /></a>

Trong quá trình thiết lập, bạn sẽ phải đăng ký một tài khoản với DigitalOcean và chọn một gói trả phí cho "droplet" (máy ảo) để sử dụng.

Có thể nói, đây hiện là cách đơn giản nhất để triển khai một phiên bản Gramps Web tự lưu trữ của riêng bạn, được bảo mật bằng SSL, mà không cần sử dụng phần cứng của riêng bạn.

!!! info
    Lưu ý rằng bạn sẽ phải trả tiền cho DigitalOcean cho các dịch vụ lưu trữ. Dự án mã nguồn mở Gramps không cung cấp hỗ trợ trả phí.

## Bước 1: Tạo tài khoản DigitalOcean

Tạo một tài khoản tại [DigitalOcean](https://www.digitalocean.com/) nếu bạn chưa có.

## Bước 2: Tạo droplet

- Truy cập [Gramps Web 1-Click App](https://marketplace.digitalocean.com/apps/gramps-web?refcode=b1d13ebe86ac&action=deploy) và nhấp vào "Create Gramps Web Droplet".
- Chọn một gói có ít nhất 2 GB RAM.
- Thiết lập xác thực cho droplet của bạn
- Nhấp vào "Create Droplet"

!!! info
    Bạn có thể cần chờ tối đa mười phút để 1-Click App cài đặt phiên bản `docker-compose` mới nhất.
    Sử dụng phiên bản mới nhất của `docker-compose` có thể giảm thiểu lỗi tham chiếu đến `firstlogin.sh`. 

## Bước 3: Thiết lập tên miền

Bạn sẽ cần một tên miền (hoặc tên miền phụ). Nếu bạn sở hữu một tên miền, hãy trỏ nó đến địa chỉ IP của droplet của bạn. Nếu không, bạn có thể sử dụng một dịch vụ miễn phí như [DuckDNS](https://www.duckdns.org/).

## Bước 4: Đăng nhập vào droplet của bạn

SSH vào droplet của bạn. Bạn sẽ thấy thông điệp "Welcome to the Gramps Web DigitalOcean 1-click app setup!". Nếu không phải như vậy, hãy chờ vài phút và thử lại (quá trình cài đặt chưa hoàn tất).

Kịch bản thiết lập sẽ yêu cầu bạn nhập tên miền (ví dụ: `mygrampswebinstance.duckdns.org`) và một địa chỉ email (cần thiết cho chứng chỉ Let's Encrypt).

Khi điều này hoàn tất, hãy chờ cho quá trình thiết lập hoàn tất trong nền.

## Bước 5: Khởi động Gramps Web

Phiên bản Gramps Web của bạn giờ đây nên có thể truy cập tại gốc của tên miền của bạn, với chứng chỉ SSL hợp lệ, và nó nên hiển thị trợ lý lần đầu chạy.
