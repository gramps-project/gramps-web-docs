# Xác thực OIDC

Gramps Web hỗ trợ xác thực OpenID Connect (OIDC), cho phép người dùng đăng nhập bằng cách sử dụng các nhà cung cấp danh tính bên ngoài. Điều này bao gồm cả các nhà cung cấp phổ biến như Google, Microsoft và GitHub, cũng như các nhà cung cấp OIDC tùy chỉnh như Keycloak, Authentik và những người khác.

## Tổng quan

Xác thực OIDC cho phép bạn:

- Sử dụng các nhà cung cấp danh tính bên ngoài cho xác thực người dùng
- Hỗ trợ nhiều nhà cung cấp xác thực đồng thời
- Ánh xạ các nhóm/nhân vai OIDC đến các vai trò người dùng Gramps Web
- Triển khai Đăng nhập Một lần (SSO) và Đăng xuất Một lần
- Tùy chọn vô hiệu hóa xác thực tên người dùng/mật khẩu cục bộ

## Cấu hình

Để kích hoạt xác thực OIDC, bạn cần cấu hình các thiết lập phù hợp trong tệp cấu hình Gramps Web hoặc biến môi trường của bạn. Xem trang [Cấu hình máy chủ](configuration.md#settings-for-oidc-authentication) để có danh sách đầy đủ các thiết lập OIDC có sẵn.

!!! info
    Khi sử dụng biến môi trường, hãy nhớ thêm tiền tố cho mỗi tên thiết lập với `GRAMPSWEB_` (ví dụ: `GRAMPSWEB_OIDC_ENABLED`). Xem [Tệp cấu hình so với biến môi trường](configuration.md#configuration-file-vs-environment-variables) để biết thêm chi tiết.

### Các nhà cung cấp tích hợp sẵn

Gramps Web có hỗ trợ tích hợp sẵn cho các nhà cung cấp danh tính phổ biến. Để sử dụng chúng, bạn chỉ cần cung cấp ID khách hàng và bí mật khách hàng:

- **Google**: `OIDC_GOOGLE_CLIENT_ID` và `OIDC_GOOGLE_CLIENT_SECRET`
- **Microsoft**: `OIDC_MICROSOFT_CLIENT_ID` và `OIDC_MICROSOFT_CLIENT_SECRET`
- **GitHub**: `OIDC_GITHUB_CLIENT_ID` và `OIDC_GITHUB_CLIENT_SECRET`

Bạn có thể cấu hình nhiều nhà cung cấp đồng thời. Hệ thống sẽ tự động phát hiện các nhà cung cấp nào có sẵn dựa trên các giá trị cấu hình.

### Các nhà cung cấp OIDC tùy chỉnh

Đối với các nhà cung cấp OIDC tùy chỉnh (như Keycloak, Authentik hoặc bất kỳ nhà cung cấp nào tuân thủ OIDC tiêu chuẩn), hãy sử dụng các thiết lập sau:

Key | Mô tả
----|-------------
`OIDC_ENABLED` | Boolean, có kích hoạt xác thực OIDC hay không. Đặt thành `True`.
`OIDC_ISSUER` | URL nhà cung cấp của bạn
`OIDC_CLIENT_ID` | ID khách hàng cho nhà cung cấp OIDC của bạn
`OIDC_CLIENT_SECRET` | Bí mật khách hàng cho nhà cung cấp OIDC của bạn
`OIDC_NAME` | Tên hiển thị tùy chỉnh (tùy chọn, mặc định là "OIDC")
`OIDC_SCOPES` | Các phạm vi OAuth (tùy chọn, mặc định là "openid email profile")

## Các URI chuyển hướng yêu cầu

Khi cấu hình nhà cung cấp OIDC của bạn, bạn phải đăng ký URI chuyển hướng sau:

**Đối với các nhà cung cấp OIDC hỗ trợ ký tự đại diện: (ví dụ: Authentik)**

- `https://your-gramps-backend.com/api/oidc/callback/*`

Trong đó `*` là ký tự đại diện regex. Tùy thuộc vào trình biên dịch regex của nhà cung cấp của bạn, điều này cũng có thể là `.*` hoặc tương tự.
Đảm bảo rằng regex được kích hoạt nếu nhà cung cấp của bạn yêu cầu (ví dụ: Authentik).

**Đối với các nhà cung cấp OIDC không hỗ trợ ký tự đại diện: (ví dụ: Authelia)**

- `https://your-gramps-backend.com/api/oidc/callback/custom`

## Ánh xạ vai trò

Gramps Web có thể tự động ánh xạ các nhóm hoặc vai trò OIDC từ nhà cung cấp danh tính của bạn đến các vai trò người dùng Gramps Web. Điều này cho phép bạn quản lý quyền người dùng một cách trung tâm trong nhà cung cấp danh tính của bạn.

### Cấu hình

Sử dụng các thiết lập này để cấu hình ánh xạ vai trò:

Key | Mô tả
----|-------------
`OIDC_ROLE_CLAIM` | Tên yêu cầu trong token OIDC chứa các nhóm/vai trò của người dùng. Mặc định là "groups"
`OIDC_GROUP_ADMIN` | Tên nhóm/vai trò từ nhà cung cấp OIDC của bạn ánh xạ đến vai trò "Quản trị viên" của Gramps
`OIDC_GROUP_OWNER` | Tên nhóm/vai trò từ nhà cung cấp OIDC của bạn ánh xạ đến vai trò "Chủ sở hữu" của Gramps
`OIDC_GROUP_EDITOR` | Tên nhóm/vai trò từ nhà cung cấp OIDC của bạn ánh xạ đến vai trò "Biên tập viên" của Gramps
`OIDC_GROUP_CONTRIBUTOR` | Tên nhóm/vai trò từ nhà cung cấp OIDC của bạn ánh xạ đến vai trò "Người đóng góp" của Gramps
`OIDC_GROUP_MEMBER` | Tên nhóm/vai trò từ nhà cung cấp OIDC của bạn ánh xạ đến vai trò "Thành viên" của Gramps
`OIDC_GROUP_GUEST` | Tên nhóm/vai trò từ nhà cung cấp OIDC của bạn ánh xạ đến vai trò "Khách" của Gramps

### Hành vi ánh xạ vai trò

- Nếu không có ánh xạ vai trò nào được cấu hình (không có biến `OIDC_GROUP_*` nào được thiết lập), các vai trò người dùng hiện có sẽ được giữ nguyên
- Người dùng sẽ được gán vai trò cao nhất mà họ đủ điều kiện dựa trên tư cách thành viên nhóm của họ
- Ánh xạ vai trò phân biệt chữ hoa chữ thường theo mặc định (phụ thuộc vào nhà cung cấp OIDC của bạn)

## Đăng xuất OIDC

Gramps Web hỗ trợ Đăng xuất Một lần (SSO logout) cho các nhà cung cấp OIDC. Khi một người dùng đăng xuất khỏi Gramps Web sau khi xác thực qua OIDC, họ sẽ được tự động chuyển hướng đến trang đăng xuất của nhà cung cấp danh tính nếu nhà cung cấp hỗ trợ `end_session_endpoint`.

### Đăng xuất Backchannel

Gramps Web triển khai đặc tả Đăng xuất Back-Channel của OpenID Connect. Điều này cho phép các nhà cung cấp danh tính thông báo cho Gramps Web khi một người dùng đăng xuất từ một ứng dụng khác hoặc từ chính nhà cung cấp danh tính.

#### Cấu hình

Để cấu hình đăng xuất backchannel với nhà cung cấp danh tính của bạn:

1. **Đăng ký điểm cuối đăng xuất backchannel** trong cấu hình khách hàng của nhà cung cấp danh tính của bạn:
   ```
   https://your-gramps-backend.com/api/oidc/backchannel-logout/
   ```

2. **Cấu hình nhà cung cấp của bạn** để gửi thông báo đăng xuất. Các bước cụ thể phụ thuộc vào nhà cung cấp của bạn:

   **Keycloak:**

   - Trong cấu hình khách hàng của bạn, điều hướng đến "Cài đặt"
   - Đặt "URL Đăng xuất Backchannel" thành `https://your-gramps-backend.com/api/oidc/backchannel-logout/`
   - Kích hoạt "Yêu cầu Phiên Đăng xuất Backchannel" nếu bạn muốn đăng xuất dựa trên phiên

   **Authentik:**

   - Trong cấu hình nhà cung cấp của bạn, thêm URL đăng xuất backchannel
   - Đảm bảo nhà cung cấp được cấu hình để gửi token đăng xuất

!!! warning "Hết hạn Token"
    Do tính chất không trạng thái của các token JWT, đăng xuất backchannel hiện tại ghi lại sự kiện đăng xuất nhưng không thể ngay lập tức thu hồi các token JWT đã được phát hành. Các token sẽ vẫn hợp lệ cho đến khi hết hạn (mặc định: 15 phút cho các token truy cập).

    Để tăng cường bảo mật, hãy xem xét:

    - Giảm thời gian hết hạn token JWT (`JWT_ACCESS_TOKEN_EXPIRES`)
    - Giáo dục người dùng để đăng xuất thủ công khỏi Gramps Web khi đăng xuất khỏi nhà cung cấp danh tính của bạn

!!! tip "Cách hoạt động"
    Khi một người dùng đăng xuất khỏi nhà cung cấp danh tính của bạn hoặc một ứng dụng khác:

    1. Nhà cung cấp gửi một `logout_token` JWT đến điểm cuối đăng xuất backchannel của Gramps Web
    2. Gramps Web xác thực token và ghi lại sự kiện đăng xuất
    3. JTI của token đăng xuất được thêm vào danh sách chặn để ngăn chặn các cuộc tấn công phát lại
    4. Bất kỳ yêu cầu API mới nào với JWT của người dùng sẽ bị từ chối khi các token hết hạn

## Ví dụ Cấu hình

### Nhà cung cấp OIDC Tùy chỉnh (Keycloak)

```python
TREE="Cây Gia Đình Của Tôi"
BASE_URL="https://mytree.example.com"
SECRET_KEY="..."  # khóa bí mật của bạn
USER_DB_URI="sqlite:////path/to/users.sqlite"

# Cấu hình OIDC Tùy chỉnh
OIDC_ENABLED=True
OIDC_ISSUER="https://auth.example.com/realms/myrealm"
OIDC_CLIENT_ID="gramps-web"
OIDC_CLIENT_SECRET="your-client-secret"
OIDC_NAME="SSO Gia Đình"
OIDC_SCOPES="openid email profile"
OIDC_AUTO_REDIRECT=True  # Tùy chọn: tự động chuyển hướng đến đăng nhập SSO
OIDC_DISABLE_LOCAL_AUTH=True  # Tùy chọn: vô hiệu hóa đăng nhập tên người dùng/mật khẩu

# Tùy chọn: Ánh xạ vai trò từ các nhóm OIDC đến các vai trò Gramps
OIDC_ROLE_CLAIM="groups"  # hoặc "roles" tùy thuộc vào nhà cung cấp của bạn
OIDC_GROUP_ADMIN="gramps-admins"
OIDC_GROUP_EDITOR="gramps-editors"
OIDC_GROUP_MEMBER="gramps-members"

EMAIL_HOST="mail.example.com"
EMAIL_PORT=465
EMAIL_USE_TLS=True
EMAIL_HOST_USER="gramps@example.com"
EMAIL_HOST_PASSWORD="..." # mật khẩu SMTP của bạn
DEFAULT_FROM_EMAIL="gramps@example.com"
```

### Nhà cung cấp Tích hợp Sẵn (Google)

```python
TREE="Cây Gia Đình Của Tôi"
BASE_URL="https://mytree.example.com"
SECRET_KEY="..."  # khóa bí mật của bạn
USER_DB_URI="sqlite:////path/to/users.sqlite"

# Google OAuth
OIDC_GOOGLE_CLIENT_ID="your-google-client-id"
OIDC_GOOGLE_CLIENT_SECRET="your-google-client-secret"
```

### Nhiều Nhà cung cấp

Bạn có thể kích hoạt nhiều nhà cung cấp OIDC đồng thời:

```python
TREE="Cây Gia Đình Của Tôi"
BASE_URL="https://mytree.example.com"
SECRET_KEY="..."  # khóa bí mật của bạn
USER_DB_URI="sqlite:////path/to/users.sqlite"

# Nhà cung cấp tùy chỉnh
OIDC_ENABLED=True
OIDC_ISSUER="https://auth.example.com/realms/myrealm"
OIDC_CLIENT_ID="gramps-web"
OIDC_CLIENT_SECRET="your-client-secret"
OIDC_NAME="SSO Công Ty"

# Google OAuth
OIDC_GOOGLE_CLIENT_ID="your-google-client-id"
OIDC_GOOGLE_CLIENT_SECRET="your-google-client-secret"

# GitHub OAuth
OIDC_GITHUB_CLIENT_ID="your-github-client-id"
OIDC_GITHUB_CLIENT_SECRET="your-github-client-secret"
```

### Authelia

Một hướng dẫn thiết lập OIDC do cộng đồng thực hiện cho Gramps Web có sẵn trên [trang tài liệu chính thức của Authelia](https://www.authelia.com/integration/openid-connect/clients/gramps/).

### Keycloak

Hầu hết các cấu hình cho Keycloak có thể để ở mặc định của nó (*Khách hàng → Tạo khách hàng → Xác thực khách hàng BẬT*).
Có một vài ngoại lệ:

1. **Phạm vi OpenID** – Phạm vi `openid` không được bao gồm theo mặc định trong tất cả các phiên bản Keycloak. Để tránh các vấn đề, hãy thêm nó một cách thủ công: *Khách hàng → [Khách hàng Gramps] → Phạm vi khách hàng → Thêm phạm vi → Tên: `openid` → Đặt làm mặc định.*
2. **Vai trò** – Vai trò có thể được gán ở cấp độ khách hàng hoặc toàn cầu theo miền.

    * Nếu bạn đang sử dụng vai trò khách hàng, hãy đặt tùy chọn cấu hình `OIDC_ROLE_CLAIM` thành: `resource_access.[gramps-client-name].roles`
    * Để làm cho các vai trò có thể nhìn thấy đối với Gramps, hãy điều hướng đến *Phạm vi Khách hàng* (phần cấp cao nhất, không phải dưới khách hàng cụ thể), sau đó: *Vai trò → Mapper → vai trò khách hàng → Thêm vào thông tin người dùng → BẬT.*
