# Xác thực OIDC

Gramps Web hỗ trợ xác thực OpenID Connect (OIDC), cho phép người dùng đăng nhập bằng cách sử dụng các nhà cung cấp danh tính bên ngoài. Điều này bao gồm các nhà cung cấp tích hợp sẵn như Google và Microsoft, cũng như các nhà cung cấp OIDC tùy chỉnh như Keycloak, Authentik và Authelia.

!!! warning "GitHub không còn được hỗ trợ như một nhà cung cấp OIDC"
    Nếu bạn đã thiết lập `OIDC_GITHUB_CLIENT_ID` / `OIDC_GITHUB_CLIENT_SECRET` từ phiên bản trước, hãy xóa chúng – chúng hiện đã bị bỏ qua, và người dùng đã đăng nhập trước đó qua GitHub không thể đăng nhập theo cách đó nữa. GitHub là một nhà cung cấp OAuth 2.0, không phải là nhà cung cấp OpenID Connect, và chưa bao giờ trả về yêu cầu mà Gramps Web dựa vào để xác định danh tính, vì vậy nó chưa bao giờ hoàn toàn đáng tin cậy.

## Tổng quan

Xác thực OIDC cho phép bạn:

- Sử dụng các nhà cung cấp danh tính bên ngoài để xác thực người dùng
- Hỗ trợ nhiều nhà cung cấp xác thực cùng một lúc
- Ánh xạ các nhóm/nhân viên OIDC thành các vai trò người dùng Gramps Web
- Triển khai Đăng nhập Một lần (SSO) và Đăng xuất Một lần
- Tùy chọn vô hiệu hóa xác thực tên người dùng/mật khẩu cục bộ

## Cấu hình

Để kích hoạt xác thực OIDC, bạn cần cấu hình các thiết lập thích hợp trong tệp cấu hình Gramps Web của bạn hoặc biến môi trường. Xem trang [Cấu hình Máy chủ](configuration.md#settings-for-oidc-authentication) để có danh sách đầy đủ các thiết lập OIDC có sẵn.

!!! info
    Khi sử dụng biến môi trường, hãy nhớ thêm tiền tố `GRAMPSWEB_` vào mỗi tên thiết lập (ví dụ: `GRAMPSWEB_OIDC_ENABLED`). Xem [Tệp cấu hình so với biến môi trường](configuration.md#configuration-file-vs-environment-variables) để biết thêm chi tiết.

### Nhà cung cấp tích hợp sẵn

Gramps Web có hỗ trợ tích hợp cho các nhà cung cấp danh tính phổ biến. Để sử dụng chúng, bạn chỉ cần cung cấp ID khách hàng và bí mật khách hàng:

- **Google**: `OIDC_GOOGLE_CLIENT_ID` và `OIDC_GOOGLE_CLIENT_SECRET`
- **Microsoft**: `OIDC_MICROSOFT_CLIENT_ID` và `OIDC_MICROSOFT_CLIENT_SECRET`

Bạn có thể cấu hình nhiều nhà cung cấp cùng một lúc. Hệ thống sẽ tự động phát hiện các nhà cung cấp nào có sẵn dựa trên các giá trị cấu hình.

!!! tip "Microsoft: triển khai đơn thuê"
    Nhà cung cấp Microsoft tích hợp sẵn sử dụng điểm cuối đa thuê `/common` và chấp nhận đăng nhập từ bất kỳ tài khoản Microsoft nào theo thiết kế. Nếu bạn chỉ muốn cho phép người dùng từ thuê của riêng bạn, hãy sử dụng [nhà cung cấp OIDC tùy chỉnh](#custom-oidc-providers) với URL nhà phát hành cụ thể cho thuê của bạn, điều này giữ cho xác thực nhà phát hành hoạt động và hạn chế đăng nhập vào thuê đó.

### Nhà cung cấp OIDC tùy chỉnh

Đối với các nhà cung cấp OIDC tùy chỉnh (như Keycloak, Authentik, Authelia, hoặc một thuê Microsoft Entra đơn), hãy sử dụng các thiết lập sau:

Key | Mô tả
----|-------------
`OIDC_ENABLED` | Boolean, cho biết có kích hoạt xác thực OIDC hay không. Đặt thành `True`.
`OIDC_ISSUER` | URL nhà phát hành của nhà cung cấp của bạn. Khám phá được lấy từ `<issuer>/.well-known/openid-configuration`.
`OIDC_CLIENT_ID` | ID khách hàng cho nhà cung cấp OIDC của bạn
`OIDC_CLIENT_SECRET` | Bí mật khách hàng cho nhà cung cấp OIDC của bạn
`OIDC_NAME` | Tên hiển thị tùy chỉnh (tùy chọn, mặc định là "OIDC")
`OIDC_SCOPES` | Phạm vi OAuth (tùy chọn, mặc định là "openid email profile")
`OIDC_USERNAME_CLAIM` | Yêu cầu được sử dụng để tạo tên người dùng (tùy chọn, mặc định là "preferred_username")

### Cài đặt Đa Cây

Trên một máy chủ đa cây, cây mà người dùng đang đăng nhập phải được biết trước khi Gramps Web chuyển hướng đến nhà cung cấp danh tính, vì vậy việc đăng nhập bắt đầu với:

```
GET /api/oidc/login/?provider=<id>&tree=<tree_id>
```

`tree` là bắt buộc trong các cài đặt đa cây; nếu bỏ qua, hoặc truyền ID của một cây không tồn tại, sẽ thất bại trong việc đăng nhập. Trên một máy chủ đơn cây, `tree` là tùy chọn, nhưng nếu được cung cấp thì phải khớp với `TREE` đã cấu hình.

Một danh tính OIDC được liên kết với đúng một tài khoản Gramps Web, mà lại thuộc về đúng một cây – việc đăng nhập vào một cây khác sẽ thất bại thay vì chuyển tài khoản. Không có cách nào để liên kết một danh tính duy nhất tại nhà cung cấp với các tài khoản trong nhiều cây; người dùng cần truy cập vào nhiều cây cần có các danh tính riêng biệt tại nhà cung cấp (ví dụ: tên người dùng hoặc tài khoản khác nhau).

!!! warning
    Tài khoản quản trị viên của trang web không có cây liên kết nào (xem [tạo tài khoản quản trị viên](../administration/owner.md)) không thể đăng nhập qua OIDC, vì xác thực OIDC luôn yêu cầu một cây. Các tài khoản như vậy phải được tạo và xác thực bằng tên người dùng/mật khẩu cục bộ thay thế.

## URI Chuyển hướng Bắt buộc

Khi cấu hình nhà cung cấp OIDC của bạn, bạn phải đăng ký URI chuyển hướng sau:

**Đối với các nhà cung cấp OIDC hỗ trợ ký tự đại diện: (ví dụ: Authentik)**

- `https://your-gramps-backend.com/api/oidc/callback/*`

Nơi mà `*` là một ký tự đại diện regex. Tùy thuộc vào trình phân tích regex của nhà cung cấp của bạn, điều này cũng có thể là `.*` hoặc tương tự.
Đảm bảo rằng regex được kích hoạt nếu nhà cung cấp của bạn yêu cầu (ví dụ: Authentik).

**Đối với các nhà cung cấp OIDC không hỗ trợ ký tự đại diện: (ví dụ: Authelia)**

- `https://your-gramps-backend.com/api/oidc/callback/custom`

Cây không bao giờ là một phần của URI chuyển hướng, ngay cả trên các máy chủ đa cây – nó di chuyển riêng biệt trong phiên, vì các nhà cung cấp yêu cầu URI chuyển hướng phải khớp chính xác với URI đã đăng ký.

## Ánh xạ Vai trò

Gramps Web có thể tự động ánh xạ các nhóm hoặc vai trò OIDC từ nhà cung cấp danh tính của bạn thành các vai trò người dùng Gramps Web. Điều này cho phép bạn quản lý quyền người dùng một cách tập trung trong nhà cung cấp danh tính của bạn. Việc ánh xạ vai trò hoạt động giống nhau cho tất cả các nhà cung cấp, cả tích hợp sẵn và tùy chỉnh.

### Cấu hình

Sử dụng các thiết lập này để cấu hình ánh xạ vai trò:

Key | Mô tả
----|-------------
`OIDC_ROLE_CLAIM` | Tên yêu cầu trong token OIDC chứa các nhóm/vai trò của người dùng. Mặc định là "groups". Hỗ trợ các đường dẫn có dấu chấm, ví dụ: `realm_access.roles`.
`OIDC_GROUP_ADMIN` | Tên nhóm/vai trò từ nhà cung cấp OIDC của bạn ánh xạ đến vai trò "Quản trị viên" của Gramps
`OIDC_GROUP_OWNER` | Tên nhóm/vai trò từ nhà cung cấp OIDC của bạn ánh xạ đến vai trò "Chủ sở hữu" của Gramps
`OIDC_GROUP_EDITOR` | Tên nhóm/vai trò từ nhà cung cấp OIDC của bạn ánh xạ đến vai trò "Biên tập viên" của Gramps
`OIDC_GROUP_CONTRIBUTOR` | Tên nhóm/vai trò từ nhà cung cấp OIDC của bạn ánh xạ đến vai trò "Người đóng góp" của Gramps
`OIDC_GROUP_MEMBER` | Tên nhóm/vai trò từ nhà cung cấp OIDC của bạn ánh xạ đến vai trò "Thành viên" của Gramps
`OIDC_GROUP_GUEST` | Tên nhóm/vai trò từ nhà cung cấp OIDC của bạn ánh xạ đến vai trò "Khách" của Gramps

### Hành vi Ánh xạ Vai trò

Nếu không có thiết lập `OIDC_GROUP_*` nào được cấu hình, việc ánh xạ vai trò sẽ tắt và các vai trò sẽ được quản lý thủ công trong Gramps Web; các tài khoản OIDC mới sau đó sẽ được tạo ra ở trạng thái vô hiệu hóa và cần được phê duyệt bởi một chủ sở hữu hoặc quản trị viên hiện có (xem [Đăng nhập Đầu tiên và Khởi động](#first-login-and-bootstrapping) bên dưới).

Khi ánh xạ vai trò được cấu hình, trong mỗi lần đăng nhập:

- Nếu yêu cầu vai trò có mặt và người dùng thuộc về một nhóm đã được ánh xạ, họ sẽ nhận được vai trò tương ứng.
- Nếu yêu cầu vai trò có mặt nhưng người dùng không thuộc về nhóm nào đã được ánh xạ, vai trò của họ sẽ được đặt thành vô hiệu hóa. Đây là một mặc định fail-closed, không phải là lỗi – Gramps Web không thể suy ra một vai trò cho một nhóm mà nó không nhận ra.
- Nếu yêu cầu vai trò hoàn toàn vắng mặt trong token, vai trò hiện có sẽ không thay đổi; một tài khoản mới vẫn mặc định là vô hiệu hóa.

!!! warning "Google không gửi yêu cầu nhóm"
    Các token của Google không bao giờ bao gồm yêu cầu `groups`, vì vậy với việc ánh xạ vai trò được kích hoạt, các lần đăng nhập Google rơi vào trường hợp "yêu cầu vắng mặt" ở trên: người dùng hiện có giữ vai trò của họ, nhưng người dùng Google mới được tạo ra ở trạng thái vô hiệu hóa và cần phê duyệt thủ công. Hãy nhớ điều này trước khi kích hoạt ánh xạ vai trò chỉ cho một nhà cung cấp khác – nó không tự động vô hiệu hóa người dùng Google hiện có.

Microsoft Entra trả về các vai trò ứng dụng và tư cách thành viên nhóm chỉ trong token ID, không từ điểm cuối userinfo. Gramps Web hợp nhất các yêu cầu của token ID vào phản hồi userinfo để `OIDC_ROLE_CLAIM` hoạt động giống như đối với các nhà cung cấp khác; nơi cả hai đều chứa một yêu cầu, giá trị userinfo sẽ có ưu tiên.

## Đăng nhập Đầu tiên và Khởi động

Các tài khoản mới được tạo thông qua OIDC bắt đầu ở trạng thái vô hiệu hóa trừ khi ánh xạ vai trò gán cho chúng một vai trò (xem ở trên). Trên một phiên bản hoàn toàn mới, không ai có thể phê duyệt một tài khoản bị vô hiệu hóa, và nếu `OIDC_DISABLE_LOCAL_AUTH` cũng được kích hoạt thì cũng không có đăng nhập bằng mật khẩu để quay lại.

!!! warning "Cấu hình một nhóm chủ sở hữu/quản trị viên trước lần đăng nhập đầu tiên"
    Trước khi bất kỳ ai đăng nhập qua OIDC lần đầu tiên, hãy đặt `OIDC_GROUP_OWNER` (hoặc `OIDC_GROUP_ADMIN`) và đảm bảo rằng người dùng đầu tiên thuộc về nhóm đó tại nhà cung cấp. Nếu không, phiên bản không thể được khởi động thông qua OIDC.

## Tài khoản và Tên người dùng

Các tài khoản được tạo thông qua OIDC nhận được một tên người dùng được tạo tự động, được gán một lần tại thời điểm tạo tài khoản và không bao giờ thay đổi trong các lần đăng nhập sau:

- Nhà cung cấp tích hợp: `<provider>_<giá trị yêu cầu>`, ví dụ: `microsoft_alice@contoso.com`
- Nhà cung cấp tùy chỉnh: giá trị yêu cầu thuần túy, ví dụ: `alice`

Một hậu tố số sẽ được thêm vào khi có sự trùng lặp. Không có cách nào để đổi tên người dùng của tài khoản được tạo bởi OIDC sau đó; ngược lại, tên đầy đủ và địa chỉ email sẽ được làm mới trong mỗi lần đăng nhập.

Một lần đăng nhập OIDC không bao giờ gắn liền với một tài khoản cục bộ hiện có mà tình cờ chia sẻ địa chỉ email của nó – điều này là cố ý, vì việc liên kết tài khoản bằng email là một vector chiếm đoạt tài khoản. Một người dùng đã có tài khoản cục bộ sẽ nhận được một tài khoản thứ hai, riêng biệt lần đầu tiên họ đăng nhập qua OIDC.

Địa chỉ email từ nhà cung cấp chỉ được lưu trữ nếu nhà cung cấp đánh dấu chúng là đã xác minh (hoặc bỏ qua yêu cầu `email_verified` hoàn toàn) và nếu địa chỉ đó chưa được sử dụng bởi một tài khoản khác; nếu không, việc đăng nhập sẽ tiếp tục mà không lưu trữ địa chỉ email.

## Đăng xuất OIDC

Gramps Web hỗ trợ Đăng xuất Một lần (SSO logout) cho các nhà cung cấp OIDC. `GET /api/oidc/logout/` tìm kiếm `end_session_endpoint` của nhà cung cấp và trả về nó dưới dạng `logout_url` trong phản hồi; chính giao diện Gramps Web sẽ điều hướng trình duyệt đến đó để thực sự kết thúc phiên tại nhà cung cấp danh tính. `logout_url` là `null` khi nhà cung cấp không có `end_session_endpoint`.

!!! warning "Các token không bị thu hồi khi đăng xuất"
    Đăng xuất chỉ kết thúc phiên trình duyệt; hiện tại không có cách nào để thu hồi một token Gramps Web đã được phát hành. Các token vẫn hợp lệ cho đến khi hết hạn (`JWT_ACCESS_TOKEN_EXPIRES`, mặc định 15 phút cho các token truy cập), bất kể người dùng đã đăng xuất tại Gramps Web hay tại nhà cung cấp danh tính.

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
OIDC_DISABLE_LOCAL_AUTH=True  # Tùy chọn: vô hiệu hóa đăng nhập bằng tên người dùng/mật khẩu

# Tùy chọn: Ánh xạ vai trò từ các nhóm OIDC đến các vai trò Gramps
OIDC_ROLE_CLAIM="groups"  # hoặc "roles" tùy thuộc vào nhà cung cấp của bạn
OIDC_GROUP_ADMIN="gramps-admins"
OIDC_GROUP_EDITOR="gramps-editors"
OIDC_GROUP_MEMBER="gramps-members"

EMAIL_HOST="mail.example.com"
EMAIL_PORT=465
EMAIL_USE_SSL=True  # Sử dụng SSL ngầm cho cổng 465
EMAIL_HOST_USER="gramps@example.com"
EMAIL_HOST_PASSWORD="..." # mật khẩu SMTP của bạn
DEFAULT_FROM_EMAIL="gramps@example.com"
```

### Nhà cung cấp Tích hợp (Google)

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

Bạn có thể kích hoạt nhiều nhà cung cấp OIDC cùng một lúc:

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

# Microsoft OAuth
OIDC_MICROSOFT_CLIENT_ID="your-microsoft-client-id"
OIDC_MICROSOFT_CLIENT_SECRET="your-microsoft-client-secret"
```

### Authelia

Một hướng dẫn thiết lập OIDC do cộng đồng tạo cho Gramps Web có sẵn trên [trang tài liệu chính thức của Authelia](https://www.authelia.com/integration/openid-connect/clients/gramps/).

### Keycloak

Hầu hết các cấu hình cho Keycloak có thể để ở mặc định của nó (*Client → Tạo client → Bật xác thực client*).
Có một vài ngoại lệ:

1. **Phạm vi OpenID** – Phạm vi `openid` không được bao gồm theo mặc định trong tất cả các phiên bản Keycloak. Để tránh sự cố, hãy thêm nó thủ công: *Client → [client Gramps] → Client scopes → Thêm phạm vi → Tên: `openid` → Đặt làm mặc định.*
2. **Vai trò** – Vai trò có thể được gán ở cấp độ client hoặc toàn cầu cho mỗi realm.

    * Nếu bạn đang sử dụng vai trò client, hãy đặt tùy chọn cấu hình `OIDC_ROLE_CLAIM` thành: `resource_access.[gramps-client-name].roles`
    * Để làm cho vai trò có thể nhìn thấy đối với Gramps, hãy điều hướng đến *Client Scopes* (phần cấp cao nhất, không phải dưới client cụ thể), sau đó: *Roles → Mappers → vai trò client → Thêm vào userinfo → BẬT.*
