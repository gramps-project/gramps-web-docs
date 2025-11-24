# Xác thực OIDC

Gramps Web hỗ trợ xác thực OpenID Connect (OIDC), cho phép người dùng đăng nhập bằng cách sử dụng các nhà cung cấp danh tính bên ngoài. Điều này bao gồm cả các nhà cung cấp phổ biến như Google, Microsoft và GitHub, cũng như các nhà cung cấp OIDC tùy chỉnh như Keycloak, Authentik và những người khác.

## Tổng quan

Xác thực OIDC cho phép bạn:

- Sử dụng các nhà cung cấp danh tính bên ngoài cho xác thực người dùng
- Hỗ trợ nhiều nhà cung cấp xác thực đồng thời
- Ánh xạ các nhóm/nhóm OIDC thành các vai trò người dùng Gramps Web
- Thực hiện Đăng nhập Một lần (SSO) và Đăng xuất Một lần
- Tùy chọn vô hiệu hóa xác thực tên người dùng/mật khẩu cục bộ

## Cấu hình

Để kích hoạt xác thực OIDC, bạn cần cấu hình các thiết lập phù hợp trong tệp cấu hình Gramps Web hoặc biến môi trường của bạn. Xem trang [Cấu hình Máy chủ](configuration.md#settings-for-oidc-authentication) để có danh sách đầy đủ các thiết lập OIDC có sẵn.

!!! info
    Khi sử dụng biến môi trường, hãy nhớ thêm tiền tố cho mỗi tên thiết lập với `GRAMPSWEB_` (ví dụ: `GRAMPSWEB_OIDC_ENABLED`). Xem [Tệp cấu hình so với biến môi trường](configuration.md#configuration-file-vs-environment-variables) để biết thêm chi tiết.

### Các Nhà Cung Cấp Tích Hợp Sẵn

Gramps Web có hỗ trợ tích hợp sẵn cho các nhà cung cấp danh tính phổ biến. Để sử dụng chúng, bạn chỉ cần cung cấp ID khách hàng và bí mật khách hàng:

- **Google**: `OIDC_GOOGLE_CLIENT_ID` và `OIDC_GOOGLE_CLIENT_SECRET`
- **Microsoft**: `OIDC_MICROSOFT_CLIENT_ID` và `OIDC_MICROSOFT_CLIENT_SECRET`
- **GitHub**: `OIDC_GITHUB_CLIENT_ID` và `OIDC_GITHUB_CLIENT_SECRET`

Bạn có thể cấu hình nhiều nhà cung cấp đồng thời. Hệ thống sẽ tự động phát hiện các nhà cung cấp nào có sẵn dựa trên các giá trị cấu hình.

### Các Nhà Cung Cấp OIDC Tùy Chỉnh

Đối với các nhà cung cấp OIDC tùy chỉnh (như Keycloak, Authentik hoặc bất kỳ nhà cung cấp nào tuân thủ OIDC tiêu chuẩn), hãy sử dụng các thiết lập sau:

Key | Mô tả
----|-------------
`OIDC_ENABLED` | Boolean, có cho phép xác thực OIDC hay không. Đặt thành `True`.
`OIDC_ISSUER` | URL nhà cung cấp của bạn
`OIDC_CLIENT_ID` | ID khách hàng cho nhà cung cấp OIDC của bạn
`OIDC_CLIENT_SECRET` | Bí mật khách hàng cho nhà cung cấp OIDC của bạn
`OIDC_NAME` | Tên hiển thị tùy chỉnh (tùy chọn, mặc định là "OIDC")
`OIDC_SCOPES` | Các phạm vi OAuth (tùy chọn, mặc định là "openid email profile")

## Các URI Chuyển Hướng Bắt Buộc

Khi cấu hình nhà cung cấp OIDC của bạn, bạn phải đăng ký URI chuyển hướng sau:

**Đối với các nhà cung cấp OIDC hỗ trợ ký tự đại diện: (ví dụ: Authentik)**

- `https://your-gramps-backend.com/api/oidc/callback/*`

Nơi mà `*` là một ký tự đại diện regex. Tùy thuộc vào trình phân tích cú pháp regex của nhà cung cấp của bạn, điều này cũng có thể là `.*` hoặc tương tự.
Đảm bảo rằng regex được bật nếu nhà cung cấp của bạn yêu cầu (ví dụ: Authentik).

**Đối với các nhà cung cấp OIDC không hỗ trợ ký tự đại diện: (ví dụ: Authelia)**

- `https://your-gramps-backend.com/api/oidc/callback/?provider=custom`

## Ánh Xạ Vai Trò

Gramps Web có thể tự động ánh xạ các nhóm hoặc vai trò OIDC từ nhà cung cấp danh tính của bạn thành các vai trò người dùng Gramps Web. Điều này cho phép bạn quản lý quyền người dùng một cách tập trung trong nhà cung cấp danh tính của bạn.

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

### Hành Vi Ánh Xạ Vai Trò

- Nếu không có ánh xạ vai trò nào được cấu hình (không có biến `OIDC_GROUP_*` nào được thiết lập), các vai trò người dùng hiện có sẽ được bảo tồn
- Người dùng sẽ được gán vai trò cao nhất mà họ đủ điều kiện dựa trên tư cách thành viên nhóm của họ
- Ánh xạ vai trò phân biệt chữ hoa chữ thường theo mặc định (phụ thuộc vào nhà cung cấp OIDC của bạn)

## Đăng Xuất OIDC

Gramps Web hỗ trợ Đăng xuất Một lần (SSO logout) cho các nhà cung cấp OIDC. Khi một người dùng đăng xuất khỏi Gramps Web sau khi xác thực qua OIDC, họ sẽ được tự động chuyển hướng đến trang đăng xuất của nhà cung cấp danh tính nếu nhà cung cấp hỗ trợ `end_session_endpoint`.

### Đăng Xuất Kênh Phụ

Gramps Web thực hiện đặc tả Đăng xuất Kênh Phụ OpenID Connect. Điều này cho phép các nhà cung cấp danh tính thông báo cho Gramps Web khi một người dùng đăng xuất từ một ứng dụng khác hoặc từ chính nhà cung cấp danh tính.

#### Cấu hình

Để cấu hình đăng xuất kênh phụ với nhà cung cấp danh tính của bạn:

1. **Đăng ký điểm cuối đăng xuất kênh phụ** trong cấu hình khách hàng của nhà cung cấp danh tính của bạn:
   ```
   https://your-gramps-backend.com/api/oidc/backchannel-logout/
   ```

2. **Cấu hình nhà cung cấp của bạn** để gửi thông báo đăng xuất. Các bước cụ thể phụ thuộc vào nhà cung cấp của bạn:

   **Keycloak:**

   - Trong cấu hình khách hàng của bạn, điều hướng đến "Cài đặt"
   - Đặt "URL Đăng xuất Kênh Phụ" thành `https://your-gramps-backend.com/api/oidc/backchannel-logout/`
   - Bật "Yêu cầu Phiên Đăng xuất Kênh Phụ" nếu bạn muốn đăng xuất dựa trên phiên

   **Authentik:**

   - Trong cấu hình nhà cung cấp của bạn, thêm URL đăng xuất kênh phụ
   - Đảm bảo nhà cung cấp được cấu hình để gửi token đăng xuất

!!! warning "Hết Hạn Token"
    Do tính chất không trạng thái của các token JWT, đăng xuất kênh phụ hiện tại ghi lại sự kiện đăng xuất nhưng không thể ngay lập tức thu hồi các token JWT đã phát hành. Các token sẽ vẫn hợp lệ cho đến khi hết hạn (mặc định: 15 phút cho các token truy cập).

    Để tăng cường bảo mật, hãy xem xét:

    - Giảm thời gian hết hạn token JWT (`JWT_ACCESS_TOKEN_EXPIRES`)
    - Giáo dục người dùng để đăng xuất thủ công khỏi Gramps Web khi đăng xuất khỏi nhà cung cấp danh tính của bạn

!!! tip "Cách Hoạt Động"
    Khi một người dùng đăng xuất từ nhà cung cấp danh tính của bạn hoặc một ứng dụng khác:

    1. Nhà cung cấp gửi một `logout_token` JWT đến điểm cuối đăng xuất kênh phụ của Gramps Web
    2. Gramps Web xác thực token và ghi lại sự kiện đăng xuất
    3. JTI của token đăng xuất được thêm vào danh sách chặn để ngăn chặn các cuộc tấn công phát lại
    4. Bất kỳ yêu cầu API mới nào với JWT của người dùng sẽ bị từ chối khi các token hết hạn

## Ví Dụ Cấu Hình

### Nhà Cung Cấp OIDC Tùy Chỉnh (Keycloak)

```python
TREE="Cây Gia Đình Của Tôi"
BASE_URL="https://mytree.example.com"
SECRET_KEY="..."  # khóa bí mật của bạn
USER_DB_URI="sqlite:////path/to/users.sqlite"

# Cấu hình OIDC Tùy Chỉnh
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

### Nhà Cung Cấp Tích Hợp Sẵn (Google)

```python
TREE="Cây Gia Đình Của Tôi"
BASE_URL="https://mytree.example.com"
SECRET_KEY="..."  # khóa bí mật của bạn
USER_DB_URI="sqlite:////path/to/users.sqlite"

# Google OAuth
OIDC_GOOGLE_CLIENT_ID="your-google-client-id"
OIDC_GOOGLE_CLIENT_SECRET="your-google-client-secret"
```

### Nhiều Nhà Cung Cấp

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

Một hướng dẫn thiết lập OIDC do cộng đồng tạo cho Gramps Web có sẵn trên [trang tài liệu chính thức của Authelia](https://www.authelia.com/integration/openid-connect/clients/gramps/).
