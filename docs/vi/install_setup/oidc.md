# Xác thực OIDC

Gramps Web hỗ trợ xác thực OpenID Connect (OIDC), cho phép người dùng đăng nhập bằng cách sử dụng các nhà cung cấp danh tính bên ngoài. Điều này bao gồm các nhà cung cấp tích hợp sẵn như Google và Microsoft, cũng như các nhà cung cấp OIDC tùy chỉnh như Keycloak, Authentik và Authelia.

!!! warning "GitHub không còn được hỗ trợ như một nhà cung cấp OIDC"
    Nếu bạn đã thiết lập `OIDC_GITHUB_CLIENT_ID` / `OIDC_GITHUB_CLIENT_SECRET` từ phiên bản trước, hãy xóa chúng – chúng hiện đã bị bỏ qua, và người dùng đã đăng nhập qua GitHub trước đây không thể đăng nhập theo cách đó nữa. GitHub là một nhà cung cấp OAuth 2.0, không phải là nhà cung cấp OpenID Connect, và chưa bao giờ trả về yêu cầu mà Gramps Web dựa vào để xác định danh tính, vì vậy nó chưa bao giờ hoàn toàn đáng tin cậy.

## Tổng quan

Xác thực OIDC cho phép bạn:

- Sử dụng các nhà cung cấp danh tính bên ngoài cho xác thực người dùng
- Hỗ trợ nhiều nhà cung cấp xác thực đồng thời
- Ánh xạ các nhóm/nhân vai OIDC tới các vai trò người dùng Gramps Web
- Thực hiện Đăng nhập Một lần (SSO) và Đăng xuất Một lần
- Tùy chọn vô hiệu hóa xác thực tên người dùng/mật khẩu cục bộ

## Cấu hình

Để kích hoạt xác thực OIDC, bạn cần cấu hình các thiết lập phù hợp trong tệp cấu hình Gramps Web của bạn hoặc các biến môi trường. Xem trang [Cấu hình Máy chủ](configuration.md#settings-for-oidc-authentication) để biết danh sách đầy đủ các thiết lập OIDC có sẵn.

!!! info
    Khi sử dụng các biến môi trường, hãy nhớ thêm tiền tố `GRAMPSWEB_` vào mỗi tên thiết lập (ví dụ: `GRAMPSWEB_OIDC_ENABLED`). Xem [Tệp cấu hình vs. biến môi trường](configuration.md#configuration-file-vs-environment-variables) để biết thêm chi tiết.

### Các Nhà Cung Cấp Tích Hợp Sẵn

Gramps Web có hỗ trợ tích hợp sẵn cho các nhà cung cấp danh tính phổ biến. Để sử dụng chúng, bạn chỉ cần cung cấp ID khách hàng và bí mật khách hàng:

- **Google**: `OIDC_GOOGLE_CLIENT_ID` và `OIDC_GOOGLE_CLIENT_SECRET`
- **Microsoft**: `OIDC_MICROSOFT_CLIENT_ID` và `OIDC_MICROSOFT_CLIENT_SECRET`

Bạn có thể cấu hình nhiều nhà cung cấp đồng thời. Hệ thống sẽ tự động phát hiện các nhà cung cấp nào có sẵn dựa trên các giá trị cấu hình.

!!! tip "Microsoft: triển khai một thuê bao"
    Nhà cung cấp Microsoft tích hợp sẵn sử dụng điểm cuối đa thuê bao `/common` và chấp nhận đăng nhập từ bất kỳ tài khoản Microsoft nào theo thiết kế. Nếu bạn chỉ muốn cho phép người dùng từ thuê bao của riêng mình, hãy sử dụng [nhà cung cấp OIDC tùy chỉnh](#custom-oidc-providers) với URL phát hành cụ thể cho thuê bao của bạn, điều này giữ cho việc xác thực phát hành hoạt động và hạn chế đăng nhập vào thuê bao đó.

### Các Nhà Cung Cấp OIDC Tùy Chỉnh

Đối với các nhà cung cấp OIDC tùy chỉnh (như Keycloak, Authentik, Authelia, hoặc một thuê bao Microsoft Entra đơn), hãy sử dụng các thiết lập sau:

Key | Mô tả
----|-------------
`OIDC_ENABLED` | Boolean, có kích hoạt xác thực OIDC hay không. Đặt thành `True`.
`OIDC_ISSUER` | URL phát hành của nhà cung cấp của bạn. Khám phá được lấy từ `<issuer>/.well-known/openid-configuration`.
`OIDC_CLIENT_ID` | ID khách hàng cho nhà cung cấp OIDC của bạn
`OIDC_CLIENT_SECRET` | Bí mật khách hàng cho nhà cung cấp OIDC của bạn
`OIDC_NAME` | Tên hiển thị tùy chỉnh (tùy chọn, mặc định là "OIDC")
`OIDC_SCOPES` | Phạm vi OAuth (tùy chọn, mặc định là "openid email profile")
`OIDC_USERNAME_CLAIM` | Yêu cầu được sử dụng để tạo tên người dùng (tùy chọn, mặc định là "preferred_username")
`OIDC_PKCE` | Có sử dụng PKCE hay không, xem [PKCE](#pkce) (tùy chọn, tự động kích hoạt nếu nhà cung cấp hỗ trợ)

### PKCE

Kể từ Gramps Web API 3.23, Gramps Web hỗ trợ [PKCE](https://datatracker.ietf.org/doc/html/rfc7636) (Chìa khóa chứng minh cho mã trao đổi, phương pháp `S256`) cho luồng mã ủy quyền. Một số nhà cung cấp danh tính, chẳng hạn như Pocket ID, có thể được cấu hình để *yêu cầu* PKCE cho một khách hàng, và từ chối các đăng nhập không sử dụng nó. Các phiên bản cũ hơn của Gramps Web API không bao giờ sử dụng PKCE, vì vậy các đăng nhập với một khách hàng như vậy sẽ thất bại.

Việc sử dụng PKCE được quyết định khi đăng nhập như sau:

- Nếu `OIDC_PKCE` được đặt thành `True`, PKCE được sử dụng.
- Nếu `OIDC_PKCE` được đặt thành `False`, PKCE không được sử dụng, ngay cả khi nhà cung cấp hỗ trợ nó.
- Nếu `OIDC_PKCE` không được đặt, hoặc được đặt nhưng trống, PKCE sẽ được sử dụng nếu tài liệu khám phá của nhà cung cấp (`/.well-known/openid-configuration`) liệt kê `S256` trong `code_challenge_methods_supported`, và không được sử dụng trong trường hợp khác.

Đối với hầu hết các thiết lập, bạn không cần phải đặt gì cả. Đặt `OIDC_PKCE` thành `True` nếu nhà cung cấp của bạn yêu cầu PKCE nhưng không quảng cáo `S256` trong tài liệu khám phá của nó, và đặt thành `False` nếu nhà cung cấp của bạn quảng cáo `S256` nhưng xử lý sai. Là các biến môi trường, các giá trị boolean phải viết thường (`GRAMPSWEB_OIDC_PKCE=true`), xem [Cấu hình](configuration.md).

Đối với các nhà cung cấp tích hợp sẵn, các tùy chọn tương ứng là `OIDC_GOOGLE_PKCE` và `OIDC_MICROSOFT_PKCE`.

Bộ xác minh mã PKCE được giữ trong phiên của người dùng giữa việc chuyển hướng đến nhà cung cấp và callback, vì vậy điều này không yêu cầu thay đổi gì đối với các URI chuyển hướng.

### Cài Đặt Đa Cây

Trên một máy chủ đa cây, một người dùng đăng nhập với một danh tính đã được liên kết với một tài khoản Gramps Web sẽ được đăng nhập vào cây của tài khoản đó, vì vậy trang đăng nhập đơn giản hoạt động cho họ.

Để tạo một tài khoản *mới* với một danh tính OIDC, Gramps Web cần biết cây mà nó nên thuộc về. Do đó, người dùng mới phải bắt đầu từ liên kết đăng ký của cây (`/register/<tree_id>`, xem [Liên kết đăng ký](../administration/users.md#registration-link-multi-tree-setup-only)), hoặc từ trang đăng nhập của cây (`/login/<tree_id>`). Cả hai đều cung cấp các nhà cung cấp đã được cấu hình. Đăng nhập với một danh tính không xác định từ trang đăng nhập đơn giản sẽ bị từ chối với một thông điệp chỉ đến liên kết đăng ký. Điều này yêu cầu Gramps Web API 3.25.3 và Gramps Web 26.11.2 hoặc mới hơn.

Ở phía sau, việc đăng nhập bắt đầu với:

```
GET /api/oidc/login/?provider=<id>&tree=<tree_id>
```

nơi `tree` là tùy chọn trừ khi một tài khoản mới được tạo. Việc truyền ID của một cây không tồn tại sẽ khiến việc đăng nhập thất bại. Trên một máy chủ đơn cây, `tree` là tùy chọn, nhưng nếu được cung cấp thì nó phải khớp với `TREE` đã được cấu hình.

Một danh tính OIDC được ràng buộc với chính xác một tài khoản Gramps Web, mà lại thuộc về chính xác một cây – việc đăng nhập vào một cây khác sẽ thất bại thay vì di chuyển tài khoản. Không có cách nào để liên kết một danh tính duy nhất tại nhà cung cấp với các tài khoản trong nhiều cây; người dùng cần truy cập vào nhiều cây cần có các danh tính riêng biệt tại nhà cung cấp (ví dụ: tên người dùng hoặc tài khoản khác nhau).

!!! warning
    Một tài khoản quản trị viên trang web không có cây liên kết nào (xem [tạo tài khoản quản trị viên](../administration/owner.md)) không thể được tạo qua OIDC, vì một tài khoản được tạo bởi một đăng nhập OIDC luôn thuộc về một cây. Tạo các tài khoản như vậy với tên người dùng và mật khẩu cục bộ.

### Ứng Dụng Gốc

Các ứng dụng gốc, chẳng hạn như ứng dụng di động cho Gramps Web, có thể cho phép người dùng đăng nhập trong trình duyệt hệ thống và nhận kết quả tại một liên kết `https` của ứng dụng. Kể từ Gramps Web API 3.26, điều này hoạt động nếu liên kết được liệt kê trong `OIDC_ALLOWED_REDIRECT_URIS`, ví dụ:

```
GRAMPSWEB_OIDC_ALLOWED_REDIRECT_URIS='["https://app.example.com/oidc-callback"]'
```

Tài liệu của ứng dụng sẽ cho bạn biết liên kết nào cần thêm. Các URI chuyển hướng đã đăng ký tại nhà cung cấp danh tính vẫn giữ nguyên.

## Các URI Chuyển Hướng Bắt Buộc

Khi cấu hình nhà cung cấp OIDC của bạn, bạn phải đăng ký URI chuyển hướng sau:

**Đối với các nhà cung cấp OIDC hỗ trợ ký tự đại diện: (ví dụ: Authentik)**

- `https://your-gramps-backend.com/api/oidc/callback/*`

Nơi `*` là một ký tự đại diện regex. Tùy thuộc vào trình thông dịch regex của nhà cung cấp của bạn, điều này cũng có thể là `.*` hoặc tương tự.
Đảm bảo rằng regex được kích hoạt nếu nhà cung cấp của bạn yêu cầu điều đó (ví dụ: Authentik).

**Đối với các nhà cung cấp OIDC không hỗ trợ ký tự đại diện: (ví dụ: Authelia)**

- `https://your-gramps-backend.com/api/oidc/callback/custom`

Cây không bao giờ là một phần của URI chuyển hướng, ngay cả trên các máy chủ đa cây – nó di chuyển riêng biệt trong phiên, vì các nhà cung cấp yêu cầu URI chuyển hướng phải khớp chính xác với URI đã đăng ký.

## Ánh Xạ Vai Trò

Gramps Web có thể tự động ánh xạ các nhóm hoặc vai trò OIDC từ nhà cung cấp danh tính của bạn tới các vai trò người dùng Gramps Web. Điều này cho phép bạn quản lý quyền người dùng một cách tập trung trong nhà cung cấp danh tính của bạn. Việc ánh xạ vai trò hoạt động giống nhau cho tất cả các nhà cung cấp, tích hợp sẵn hoặc tùy chỉnh.

### Cấu hình

Sử dụng các thiết lập sau để cấu hình ánh xạ vai trò:

Key | Mô tả
----|-------------
`OIDC_ROLE_CLAIM` | Tên yêu cầu trong mã thông báo OIDC chứa các nhóm/vai trò của người dùng. Mặc định là "groups". Các đường dẫn có dấu chấm được hỗ trợ, ví dụ: `realm_access.roles`.
`OIDC_GROUP_ADMIN` | Tên nhóm/vai trò từ nhà cung cấp OIDC của bạn ánh xạ tới vai trò "Quản trị viên" của Gramps
`OIDC_GROUP_OWNER` | Tên nhóm/vai trò từ nhà cung cấp OIDC của bạn ánh xạ tới vai trò "Chủ sở hữu" của Gramps
`OIDC_GROUP_EDITOR` | Tên nhóm/vai trò từ nhà cung cấp OIDC của bạn ánh xạ tới vai trò "Biên tập viên" của Gramps
`OIDC_GROUP_CONTRIBUTOR` | Tên nhóm/vai trò từ nhà cung cấp OIDC của bạn ánh xạ tới vai trò "Người đóng góp" của Gramps
`OIDC_GROUP_MEMBER` | Tên nhóm/vai trò từ nhà cung cấp OIDC của bạn ánh xạ tới vai trò "Thành viên" của Gramps
`OIDC_GROUP_GUEST` | Tên nhóm/vai trò từ nhà cung cấp OIDC của bạn ánh xạ tới vai trò "Khách" của Gramps

### Hành Vi Ánh Xạ Vai Trò

Nếu không có thiết lập `OIDC_GROUP_*` nào được cấu hình, việc ánh xạ vai trò sẽ tắt và các vai trò sẽ được quản lý thủ công trong Gramps Web; các tài khoản OIDC mới sau đó sẽ được tạo ra ở trạng thái bị vô hiệu hóa và cần được phê duyệt bởi một chủ sở hữu hoặc quản trị viên hiện có (xem [Đăng Nhập Đầu Tiên và Khởi Tạo](#first-login-and-bootstrapping) bên dưới).

Khi ánh xạ vai trò được cấu hình, trong mỗi lần đăng nhập:

- Nếu yêu cầu vai trò có mặt và người dùng thuộc về một nhóm đã được ánh xạ, họ sẽ nhận được vai trò tương ứng.
- Nếu yêu cầu vai trò có mặt nhưng người dùng không thuộc về nhóm nào đã được ánh xạ, vai trò của họ sẽ được đặt thành bị vô hiệu hóa. Đây là mặc định fail-closed, không phải là lỗi – Gramps Web không thể suy ra một vai trò cho một nhóm mà nó không nhận ra.
- Nếu yêu cầu vai trò hoàn toàn vắng mặt trong mã thông báo, vai trò hiện có sẽ không thay đổi; một tài khoản mới vẫn mặc định là bị vô hiệu hóa.

!!! warning "Google không gửi yêu cầu nhóm"
    Các mã thông báo của Google không bao giờ bao gồm yêu cầu `groups`, vì vậy với việc ánh xạ vai trò được kích hoạt, các đăng nhập Google rơi vào trường hợp "yêu cầu vắng mặt" ở trên: người dùng hiện có giữ vai trò của họ, nhưng người dùng Google mới được tạo ra ở trạng thái bị vô hiệu hóa và cần phê duyệt thủ công. Hãy ghi nhớ điều này trước khi kích hoạt ánh xạ vai trò chỉ cho một nhà cung cấp khác – nó không, tự nó, vô hiệu hóa người dùng Google hiện có.

Microsoft Entra trả về vai trò ứng dụng và thành viên nhóm chỉ trong mã thông báo ID, không từ điểm cuối thông tin người dùng. Gramps Web hợp nhất các yêu cầu của mã thông báo ID vào phản hồi thông tin người dùng để `OIDC_ROLE_CLAIM` hoạt động giống như đối với các nhà cung cấp khác; nơi cả hai đều chứa một yêu cầu, giá trị thông tin người dùng sẽ được ưu tiên.

## Đăng Nhập Đầu Tiên và Khởi Tạo

Các tài khoản mới được tạo thông qua OIDC bắt đầu ở trạng thái bị vô hiệu hóa trừ khi ánh xạ vai trò gán cho chúng một vai trò (xem ở trên). Trên một phiên bản hoàn toàn mới, không ai có thể phê duyệt một tài khoản bị vô hiệu hóa, và nếu `OIDC_DISABLE_LOCAL_AUTH` cũng được kích hoạt thì không có đăng nhập bằng mật khẩu để quay lại.

!!! warning "Cấu hình một nhóm chủ sở hữu/quản trị viên trước khi đăng nhập đầu tiên"
    Trước khi bất kỳ ai đăng nhập qua OIDC lần đầu tiên, hãy đặt `OIDC_GROUP_OWNER` (hoặc `OIDC_GROUP_ADMIN`) và đảm bảo rằng người dùng đầu tiên thuộc về nhóm đó tại nhà cung cấp. Nếu không, phiên bản không thể được khởi tạo qua OIDC.

## Tài Khoản và Tên Người Dùng

Các tài khoản được tạo thông qua OIDC nhận được một tên người dùng được tạo tự động, được gán một lần tại thời điểm tạo tài khoản và không bao giờ thay đổi trong các lần đăng nhập sau:

- Các nhà cung cấp tích hợp sẵn: `<provider>_<claim value>`, ví dụ: `microsoft_alice@contoso.com`
- Nhà cung cấp tùy chỉnh: giá trị yêu cầu thuần túy, ví dụ: `alice`

Một hậu tố số sẽ được thêm vào khi có sự trùng lặp. Không có cách nào để đổi tên người dùng của tài khoản được tạo bởi OIDC sau này; ngược lại, tên đầy đủ và địa chỉ e-mail sẽ được làm mới trong mỗi lần đăng nhập.

Một đăng nhập OIDC không bao giờ gắn liền với một tài khoản cục bộ hiện có mà tình cờ chia sẻ địa chỉ e-mail của nó – điều này là cố ý, vì việc liên kết các tài khoản bằng e-mail là một vector chiếm đoạt tài khoản. Một người dùng đã có một tài khoản cục bộ sẽ nhận được một tài khoản thứ hai, riêng biệt lần đầu tiên họ đăng nhập qua OIDC, trừ khi họ trước đó liên kết nhà cung cấp với tài khoản của họ.

Kể từ Gramps Web API 3.24, người dùng có thể liên kết các danh tính OIDC với tài khoản hiện có của họ, và liệt kê và hủy liên kết chúng, dưới [Cài Đặt Người Dùng > Các phương thức đăng nhập liên kết](../user-guide/settings.md#linked-sign-in-methods). Việc liên kết yêu cầu một lần đăng nhập gần đây và được xác nhận bằng mã thông báo của chính người dùng, vì vậy nó cũng hoạt động khi frontend ở một nguồn khác với API. Một danh tính chỉ có thể thuộc về một tài khoản; để liên kết một danh tính đã có tài khoản riêng của nó, một quản trị viên trước tiên phải xóa tài khoản đó (các chỉnh sửa của nó vẫn còn, nhưng lịch sử sửa đổi không còn hiển thị tên của nó). Danh tính được liên kết cuối cùng chỉ có thể bị hủy liên kết với mật khẩu hiện tại của tài khoản, và không thể hủy liên kết nếu `OIDC_DISABLE_LOCAL_AUTH` được thiết lập.

Địa chỉ e-mail từ nhà cung cấp chỉ được lưu trữ nếu nhà cung cấp đánh dấu chúng là đã xác minh (hoặc hoàn toàn bỏ qua yêu cầu `email_verified`); nếu không, đăng nhập sẽ tiếp tục mà không lưu trữ địa chỉ e-mail. Vì địa chỉ e-mail không cần phải duy nhất (kể từ Gramps Web API 3.22), một địa chỉ sẽ được lưu trữ ngay cả khi một tài khoản khác đã sử dụng nó.

## Đăng Xuất OIDC

Gramps Web hỗ trợ Đăng xuất Một lần (SSO logout) cho các nhà cung cấp OIDC. `GET /api/oidc/logout/` tìm kiếm `end_session_endpoint` của nhà cung cấp và trả về nó dưới dạng `logout_url` trong phản hồi; chính frontend của Gramps Web sẽ điều hướng trình duyệt đến đó để thực sự kết thúc phiên tại nhà cung cấp danh tính. `logout_url` là `null` khi nhà cung cấp không có `end_session_endpoint`.

!!! warning "Các mã thông báo không bị thu hồi khi đăng xuất"
    Đăng xuất chỉ kết thúc phiên trình duyệt; hiện tại không có cách nào để thu hồi một mã thông báo Gramps Web đã được cấp. Các mã thông báo vẫn hợp lệ cho đến khi chúng hết hạn (`JWT_ACCESS_TOKEN_EXPIRES`, mặc định 15 phút cho các mã thông báo truy cập), bất kể người dùng đã đăng xuất tại Gramps Web hay tại nhà cung cấp danh tính.

## Khắc Phục Sự Cố

Bắt đầu từ điểm mà đăng nhập dừng lại và theo dõi nhánh. Gramps Web ghi lại lý do cho một callback thất bại (tìm `OIDC callback error for provider` trong nhật ký máy chủ), điều này thường cụ thể hơn so với thông điệp hiển thị trong trình duyệt.

**1. Nút đăng nhập có bị thiếu không?**

- Kiểm tra `<BASE_URL>/api/oidc/config/`. Nếu `enabled` là `false` hoặc `providers` trống, OIDC không được cấu hình: `OIDC_ENABLED` phải là `True`, và một nhà cung cấp tùy chỉnh cần cả `OIDC_ISSUER` và `OIDC_CLIENT_ID`.
- Một nhà cung cấp tích hợp sẵn (Google, Microsoft) chỉ được đăng ký nếu cả ID khách hàng và bí mật khách hàng của nó đều được thiết lập.
- Tìm trong nhật ký máy chủ khi khởi động cho `Could not load discovery document`. Điều này có nghĩa là máy chủ không thể truy cập `<issuer>/.well-known/openid-configuration` (hoặc `OIDC_OPENID_CONFIG_URL`). Nó sẽ thử lại khi sử dụng lần đầu, nhưng container Gramps Web phải có khả năng giải quyết và truy cập URL phát hành, không chỉ trình duyệt của bạn.

**2. Trình duyệt có nhận được lỗi ngay sau khi được gửi đến nhà cung cấp không?**

Lỗi được hiển thị bởi nhà cung cấp danh tính, trước khi bạn đăng nhập.

- *"mismatch URI chuyển hướng"* (hoặc tương tự): URI chuyển hướng đã đăng ký tại nhà cung cấp phải khớp chính xác, bao gồm cả giao thức, máy chủ, cổng và ID nhà cung cấp. Xem [Các URI Chuyển Hướng Bắt Buộc](#required-redirect-uris). Lưu ý rằng nó được xây dựng từ `BASE_URL`, vì vậy một `BASE_URL` sai sẽ tạo ra một URI chuyển hướng sai.
- *Một lỗi PKCE* (ví dụ `invalid_request`, "cần mã thách thức", hoặc thiếu tham số `code_challenge`): nhà cung cấp yêu cầu PKCE nhưng Gramps Web không gửi nó. Đi tới [nhánh PKCE](#pkce-branch) bên dưới.

**3. Nhà cung cấp có chấp nhận đăng nhập nhưng Gramps Web sau đó hiển thị lỗi?**

- *`mismatching_state`, hoặc lỗi đề cập đến phiên hoặc trạng thái*: trình duyệt không gửi lại cookie phiên mà Gramps Web đã thiết lập khi bắt đầu đăng nhập. Cookie này cũng mang theo bộ xác minh mã PKCE. Đảm bảo rằng địa chỉ trong trình duyệt khớp với `BASE_URL` (cùng giao thức và máy chủ), rằng một proxy ngược truyền cookie và máy chủ gốc qua, và rằng việc đăng nhập được bắt đầu và hoàn thành trong cùng một tab hoặc cửa sổ trình duyệt.
- *`OIDC authentication failed for <provider>` (HTTP 401)*: kiểm tra nhật ký máy chủ để biết lý do cơ bản. Các nguyên nhân phổ biến là bí mật khách hàng sai, một URL phát hành không khớp với yêu cầu `iss` của các mã thông báo, và nhà cung cấp trả về lỗi cho callback (ví dụ PKCE, xem bên dưới).
- *Quá nhiều nỗ lực*: các điểm cuối đăng nhập và callback bị giới hạn tỷ lệ (5 yêu cầu mỗi phút). Chờ một phút và thử lại.

**4. Đăng nhập thành công nhưng bạn thấy "Tài khoản đang được xem xét", hoặc không thể làm gì?**

Các tài khoản mới được tạo ra ở trạng thái bị vô hiệu hóa trừ khi ánh xạ vai trò gán cho chúng một vai trò. Xem [Đăng Nhập Đầu Tiên và Khởi Tạo](#first-login-and-bootstrapping) và [Hành Vi Ánh Xạ Vai Trò](#role-mapping-behavior). Một quản trị viên cũng có thể kích hoạt tài khoản dưới Cài đặt > Quản trị > Quản lý người dùng.

### Nhánh PKCE

Gramps Web quyết định có sử dụng PKCE khi một đăng nhập bắt đầu (xem [PKCE](#pkce)). Để tìm hiểu điều gì đã xảy ra cho thiết lập của bạn, hãy làm theo các câu hỏi này theo thứ tự:

1. **`OIDC_PKCE` có được thiết lập không?** (Đối với các nhà cung cấp tích hợp sẵn, `OIDC_GOOGLE_PKCE` hoặc `OIDC_MICROSOFT_PKCE`.)
    - `True`: PKCE được sử dụng. Bỏ qua câu hỏi 3.
    - `False`: PKCE cố ý tắt, và tài liệu khám phá của nhà cung cấp bị bỏ qua. Nếu nhà cung cấp của bạn yêu cầu PKCE, hãy xóa thiết lập hoặc đặt nó thành `True`.
    - Không được thiết lập, hoặc trống: tiếp tục với câu hỏi 2.
2. **Tài liệu khám phá có liệt kê `S256` không?** Mở `<issuer>/.well-known/openid-configuration` và tìm `S256` trong `code_challenge_methods_supported`.
    - Có: PKCE được sử dụng tự động. Tiếp tục với câu hỏi 3.
    - Không, hoặc trường bị thiếu: PKCE **không** được sử dụng. Đặt `OIDC_PKCE` thành `True` nếu nhà cung cấp của bạn yêu cầu điều đó. Cũng kiểm tra nhật ký máy chủ cho `Could not check the provider for PKCE support`, điều này có nghĩa là tài liệu khám phá không thể được lấy và PKCE do đó đã bị tắt.
3. **PKCE có thực sự được gửi không?** Bắt đầu một đăng nhập và nhìn vào địa chỉ của trang đăng nhập của nhà cung cấp (hoặc lần chuyển hướng đầu tiên trong tab mạng của trình duyệt bạn). Nó nên chứa `code_challenge=` và `code_challenge_method=S256`.
    - Có mặt, nhưng đăng nhập vẫn thất bại tại callback: nhà cung cấp đã từ chối bộ xác minh mã. Cookie phiên có thể đã bị mất giữa chuyển hướng và callback (xem nhánh 3 ở trên), hoặc nhà cung cấp không hỗ trợ `S256`, trong trường hợp đó hãy đặt `OIDC_PKCE` thành `False` nếu nhà cung cấp không yêu cầu PKCE.
    - Vắng mặt: các thiết lập ở trên không được áp dụng. Kiểm tra rằng biến môi trường có tiền tố đúng và giá trị viết thường (ví dụ `GRAMPSWEB_OIDC_PKCE=true` trong Docker; `True` không được đọc là boolean), khởi động lại máy chủ và xem lại cấu hình.

!!! note
    Với PKCE được kích hoạt tại nhà cung cấp là *tùy chọn*, hoặc không được kích hoạt, các đăng nhập hoạt động bất kể Gramps Web có gửi một thách thức hay không. Chỉ các nhà cung cấp (hoặc khách hàng) được cấu hình để *yêu cầu* PKCE mới làm cho thiết lập này có ý nghĩa.

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
OIDC_DISABLE_LOCAL_AUTH=True  # Tùy chọn: vô hiệu hóa đăng nhập bằng tên người dùng/mật khẩu

# Tùy chọn: Ánh xạ vai trò từ các nhóm OIDC tới các vai trò Gramps
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

# Microsoft OAuth
OIDC_MICROSOFT_CLIENT_ID="your-microsoft-client-id"
OIDC_MICROSOFT_CLIENT_SECRET="your-microsoft-client-secret"
```

### Pocket ID

Tạo một khách hàng OIDC trong Pocket ID với URI chuyển hướng `<BASE_URL>/api/oidc/callback/custom` (xem [Các URI Chuyển Hướng Bắt Buộc](#required-redirect-uris)). Nếu bạn kích hoạt "Yêu cầu PKCE" cho khách hàng, không cần cấu hình Gramps Web bổ sung, vì Pocket ID quảng cáo hỗ trợ PKCE trong tài liệu khám phá của nó. Sau đó cấu hình:

```
GRAMPSWEB_OIDC_ENABLED=True
GRAMPSWEB_OIDC_ISSUER=https://id.example.com
GRAMPSWEB_OIDC_CLIENT_ID=<client id>
GRAMPSWEB_OIDC_CLIENT_SECRET=<client secret>
GRAMPSWEB_OIDC_NAME=Pocket ID
```

### Authelia

Một hướng dẫn thiết lập OIDC do cộng đồng thực hiện cho Gramps Web có sẵn trên [trang tài liệu chính thức của Authelia](https://www.authelia.com/integration/openid-connect/clients/gramps/).

### Keycloak

Hầu hết các cấu hình cho Keycloak có thể để ở mặc định của nó (*Khách hàng → Tạo khách hàng → Bật xác thực khách hàng*).
Có một vài ngoại lệ:

1. **Phạm vi OpenID** – Phạm vi `openid` không được bao gồm theo mặc định trong tất cả các phiên bản Keycloak. Để tránh sự cố, hãy thêm nó bằng tay: *Khách hàng → [Khách hàng Gramps] → Phạm vi khách hàng → Thêm phạm vi → Tên: `openid` → Đặt làm mặc định.*
2. **Vai trò** – Vai trò có thể được gán ở cấp độ khách hàng hoặc toàn cầu theo miền.

    * Nếu bạn đang sử dụng vai trò khách hàng, hãy đặt tùy chọn cấu hình `OIDC_ROLE_CLAIM` thành: `resource_access.[gramps-client-name].roles`
    * Để làm cho các vai trò có thể nhìn thấy đối với Gramps, hãy điều hướng đến *Phạm vi Khách hàng* (phần cấp cao nhất, không phải dưới khách hàng cụ thể), sau đó: *Vai trò → Bộ ánh xạ → vai trò khách hàng → Thêm vào thông tin người dùng → BẬT.*
