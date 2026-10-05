# Xác thực OIDC

Gramps Web hỗ trợ xác thực OpenID Connect (OIDC), cho phép người dùng đăng nhập bằng cách sử dụng các nhà cung cấp danh tính bên ngoài. Điều này bao gồm các nhà cung cấp tích hợp sẵn như Google và Microsoft, cũng như các nhà cung cấp OIDC tùy chỉnh như Keycloak, Authentik và Authelia.

!!! warning "GitHub không còn được hỗ trợ như một nhà cung cấp OIDC"
    Nếu bạn đã thiết lập `OIDC_GITHUB_CLIENT_ID` / `OIDC_GITHUB_CLIENT_SECRET` từ phiên bản trước, hãy xóa chúng – chúng hiện đã bị bỏ qua, và người dùng đã đăng nhập trước đó qua GitHub không thể đăng nhập theo cách đó nữa. GitHub là một nhà cung cấp OAuth 2.0, không phải là nhà cung cấp OpenID Connect, và chưa bao giờ trả về yêu cầu mà Gramps Web dựa vào để xác định danh tính, vì vậy nó chưa bao giờ hoàn toàn đáng tin cậy.

## Tổng quan

Xác thực OIDC cho phép bạn:

- Sử dụng các nhà cung cấp danh tính bên ngoài cho xác thực người dùng
- Hỗ trợ nhiều nhà cung cấp xác thực đồng thời
- Ánh xạ các nhóm/nhân vai OIDC tới các vai trò người dùng Gramps Web
- Triển khai Đăng nhập một lần (SSO) và Đăng xuất một lần
- Tùy chọn vô hiệu hóa xác thực tên người dùng/mật khẩu cục bộ

## Cấu hình

Để kích hoạt xác thực OIDC, bạn cần cấu hình các thiết lập phù hợp trong tệp cấu hình Gramps Web của bạn hoặc biến môi trường. Xem trang [Cấu hình máy chủ](configuration.md#settings-for-oidc-authentication) để có danh sách đầy đủ các thiết lập OIDC có sẵn.

!!! info
    Khi sử dụng biến môi trường, hãy nhớ thêm tiền tố `GRAMPSWEB_` vào mỗi tên thiết lập (ví dụ: `GRAMPSWEB_OIDC_ENABLED`). Xem [Tệp cấu hình vs. biến môi trường](configuration.md#configuration-file-vs-environment-variables) để biết thêm chi tiết.

### Các nhà cung cấp tích hợp sẵn

Gramps Web có hỗ trợ tích hợp cho các nhà cung cấp danh tính phổ biến. Để sử dụng chúng, bạn chỉ cần cung cấp ID khách hàng và bí mật khách hàng:

- **Google**: `OIDC_GOOGLE_CLIENT_ID` và `OIDC_GOOGLE_CLIENT_SECRET`
- **Microsoft**: `OIDC_MICROSOFT_CLIENT_ID` và `OIDC_MICROSOFT_CLIENT_SECRET`

Bạn có thể cấu hình nhiều nhà cung cấp đồng thời. Hệ thống sẽ tự động phát hiện các nhà cung cấp nào có sẵn dựa trên các giá trị cấu hình.

!!! tip "Microsoft: triển khai đơn thuê"
    Nhà cung cấp Microsoft tích hợp sẵn sử dụng điểm cuối đa thuê `/common` và chấp nhận đăng nhập từ bất kỳ tài khoản Microsoft nào theo thiết kế. Nếu bạn chỉ muốn cho phép người dùng từ thuê của riêng mình, hãy sử dụng [nhà cung cấp OIDC tùy chỉnh](#custom-oidc-providers) với URL phát hành cụ thể cho thuê của bạn, điều này giữ cho việc xác thực phát hành hoạt động và hạn chế đăng nhập vào thuê đó.

### Các nhà cung cấp OIDC tùy chỉnh

Đối với các nhà cung cấp OIDC tùy chỉnh (như Keycloak, Authentik, Authelia, hoặc một thuê Microsoft Entra đơn), hãy sử dụng các thiết lập sau:

Key | Mô tả
----|-------------
`OIDC_ENABLED` | Boolean, xác định xem có kích hoạt xác thực OIDC hay không. Đặt thành `True`.
`OIDC_ISSUER` | URL phát hành của nhà cung cấp của bạn. Thông tin khám phá được lấy từ `<issuer>/.well-known/openid-configuration`.
`OIDC_CLIENT_ID` | ID khách hàng cho nhà cung cấp OIDC của bạn
`OIDC_CLIENT_SECRET` | Bí mật khách hàng cho nhà cung cấp OIDC của bạn
`OIDC_NAME` | Tên hiển thị tùy chỉnh (tùy chọn, mặc định là "OIDC")
`OIDC_SCOPES` | Phạm vi OAuth (tùy chọn, mặc định là "openid email profile")
`OIDC_USERNAME_CLAIM` | Yêu cầu được sử dụng để tạo tên người dùng (tùy chọn, mặc định là "preferred_username")
`OIDC_PKCE` | Xác định xem có sử dụng PKCE hay không, xem [PKCE](#pkce) (tùy chọn, tự động kích hoạt nếu nhà cung cấp hỗ trợ)

### PKCE

Kể từ API Gramps Web 3.23, Gramps Web hỗ trợ [PKCE](https://datatracker.ietf.org/doc/html/rfc7636) (Chìa khóa chứng minh cho trao đổi mã, phương thức `S256`) cho quy trình mã ủy quyền. Một số nhà cung cấp danh tính, chẳng hạn như Pocket ID, có thể được cấu hình để *yêu cầu* PKCE cho một khách hàng, và từ chối các đăng nhập không sử dụng nó. Các phiên bản cũ hơn của API Gramps Web không bao giờ sử dụng PKCE, vì vậy các đăng nhập với một khách hàng như vậy sẽ thất bại.

Việc sử dụng PKCE được quyết định khi đăng nhập như sau:

- Nếu `OIDC_PKCE` được đặt thành `True`, PKCE sẽ được sử dụng.
- Nếu `OIDC_PKCE` được đặt thành `False`, PKCE sẽ không được sử dụng, ngay cả khi nhà cung cấp hỗ trợ nó.
- Nếu `OIDC_PKCE` không được đặt, hoặc được đặt nhưng trống, PKCE sẽ được sử dụng nếu tài liệu khám phá của nhà cung cấp (`/.well-known/openid-configuration`) liệt kê `S256` trong `code_challenge_methods_supported`, và không được sử dụng trong trường hợp khác.

Đối với hầu hết các thiết lập, bạn không cần phải đặt gì cả. Đặt `OIDC_PKCE` thành `True` nếu nhà cung cấp của bạn yêu cầu PKCE nhưng không quảng cáo `S256` trong tài liệu khám phá của nó, và đặt thành `False` nếu nhà cung cấp của bạn quảng cáo `S256` nhưng xử lý sai. Là biến môi trường, các giá trị boolean phải được viết thường (`GRAMPSWEB_OIDC_PKCE=true`), xem [Cấu hình](configuration.md).

Đối với các nhà cung cấp tích hợp sẵn, các tùy chọn tương ứng là `OIDC_GOOGLE_PKCE` và `OIDC_MICROSOFT_PKCE`.

Bộ xác thực mã PKCE được giữ trong phiên của người dùng giữa việc chuyển hướng đến nhà cung cấp và callback, vì vậy điều này không yêu cầu thay đổi gì đối với các URI chuyển hướng.

### Cài đặt đa cây

Trên một máy chủ đa cây, cây mà người dùng đang đăng nhập phải được biết trước khi Gramps Web chuyển hướng đến nhà cung cấp danh tính, vì vậy quá trình đăng nhập bắt đầu bằng:

```
GET /api/oidc/login/?provider=<id>&tree=<tree_id>
```

`tree` là bắt buộc trong các thiết lập đa cây; nếu bỏ qua nó, hoặc truyền ID của một cây không tồn tại, sẽ thất bại trong việc đăng nhập. Trên một máy chủ đơn cây, `tree` là tùy chọn, nhưng nếu được cung cấp, nó phải khớp với `TREE` đã được cấu hình.

Một danh tính OIDC được ràng buộc với chính xác một tài khoản Gramps Web, mà lại thuộc về chính xác một cây – việc đăng nhập vào một cây khác sẽ thất bại thay vì di chuyển tài khoản. Không có cách nào để liên kết một danh tính duy nhất tại nhà cung cấp với các tài khoản trong nhiều cây; những người dùng cần truy cập vào nhiều cây cần có các danh tính riêng biệt tại nhà cung cấp (ví dụ: tên người dùng hoặc tài khoản khác nhau).

!!! warning
    Một tài khoản quản trị viên trang web không có cây liên kết (xem [tạo tài khoản quản trị viên](../administration/owner.md)) không thể đăng nhập qua OIDC, vì việc đăng nhập OIDC luôn yêu cầu một cây. Những tài khoản như vậy phải được tạo và xác thực bằng tên người dùng/mật khẩu cục bộ thay thế.

## URI chuyển hướng cần thiết

Khi cấu hình nhà cung cấp OIDC của bạn, bạn phải đăng ký URI chuyển hướng sau:

**Đối với các nhà cung cấp OIDC hỗ trợ ký tự đại diện: (ví dụ: Authentik)**

- `https://your-gramps-backend.com/api/oidc/callback/*`

Trong đó `*` là một ký tự đại diện regex. Tùy thuộc vào trình biên dịch regex của nhà cung cấp của bạn, điều này cũng có thể là `.*` hoặc tương tự.
Đảm bảo rằng regex được kích hoạt nếu nhà cung cấp của bạn yêu cầu (ví dụ: Authentik).

**Đối với các nhà cung cấp OIDC không hỗ trợ ký tự đại diện: (ví dụ: Authelia)**

- `https://your-gramps-backend.com/api/oidc/callback/custom`

Cây không bao giờ là một phần của URI chuyển hướng, ngay cả trên các máy chủ đa cây – nó được truyền riêng biệt trong phiên, vì các nhà cung cấp yêu cầu URI chuyển hướng phải khớp chính xác với URI đã đăng ký.

## Ánh xạ vai trò

Gramps Web có thể tự động ánh xạ các nhóm hoặc vai trò OIDC từ nhà cung cấp danh tính của bạn tới các vai trò người dùng Gramps Web. Điều này cho phép bạn quản lý quyền người dùng một cách tập trung trong nhà cung cấp danh tính của bạn. Việc ánh xạ vai trò hoạt động giống nhau cho tất cả các nhà cung cấp, cả tích hợp sẵn và tùy chỉnh.

### Cấu hình

Sử dụng các thiết lập sau để cấu hình ánh xạ vai trò:

Key | Mô tả
----|-------------
`OIDC_ROLE_CLAIM` | Tên yêu cầu trong token OIDC chứa các nhóm/vai trò của người dùng. Mặc định là "groups". Hỗ trợ các đường dẫn có dấu chấm, ví dụ: `realm_access.roles`.
`OIDC_GROUP_ADMIN` | Tên nhóm/vai trò từ nhà cung cấp OIDC của bạn ánh xạ tới vai trò "Quản trị viên" của Gramps
`OIDC_GROUP_OWNER` | Tên nhóm/vai trò từ nhà cung cấp OIDC của bạn ánh xạ tới vai trò "Chủ sở hữu" của Gramps
`OIDC_GROUP_EDITOR` | Tên nhóm/vai trò từ nhà cung cấp OIDC của bạn ánh xạ tới vai trò "Biên tập viên" của Gramps
`OIDC_GROUP_CONTRIBUTOR` | Tên nhóm/vai trò từ nhà cung cấp OIDC của bạn ánh xạ tới vai trò "Người đóng góp" của Gramps
`OIDC_GROUP_MEMBER` | Tên nhóm/vai trò từ nhà cung cấp OIDC của bạn ánh xạ tới vai trò "Thành viên" của Gramps
`OIDC_GROUP_GUEST` | Tên nhóm/vai trò từ nhà cung cấp OIDC của bạn ánh xạ tới vai trò "Khách" của Gramps

### Hành vi ánh xạ vai trò

Nếu không có thiết lập `OIDC_GROUP_*` nào được cấu hình, việc ánh xạ vai trò sẽ tắt và các vai trò sẽ được quản lý thủ công trong Gramps Web; các tài khoản OIDC mới sau đó sẽ được tạo ở trạng thái vô hiệu hóa và cần được phê duyệt bởi một chủ sở hữu hoặc quản trị viên hiện có (xem [Đăng nhập lần đầu và Khởi tạo](#first-login-and-bootstrapping) bên dưới).

Khi ánh xạ vai trò đã được cấu hình, trong mỗi lần đăng nhập:

- Nếu yêu cầu vai trò có mặt và người dùng thuộc về một nhóm đã được ánh xạ, họ sẽ nhận được vai trò tương ứng.
- Nếu yêu cầu vai trò có mặt nhưng người dùng không thuộc về nhóm nào đã được ánh xạ, vai trò của họ sẽ được đặt thành vô hiệu hóa. Đây là mặc định fail-closed, không phải là lỗi – Gramps Web không thể suy ra vai trò cho một nhóm mà nó không nhận ra.
- Nếu yêu cầu vai trò hoàn toàn vắng mặt trong token, vai trò hiện có sẽ không thay đổi; một tài khoản mới vẫn mặc định là vô hiệu hóa.

!!! warning "Google không gửi yêu cầu nhóm"
    Các token của Google không bao giờ bao gồm yêu cầu `groups`, vì vậy với việc ánh xạ vai trò được kích hoạt, các đăng nhập Google rơi vào trường hợp "yêu cầu vắng mặt" ở trên: người dùng hiện có giữ vai trò của họ, nhưng người dùng Google mới được tạo ra ở trạng thái vô hiệu hóa và cần phê duyệt thủ công. Hãy ghi nhớ điều này trước khi chỉ kích hoạt ánh xạ vai trò cho một nhà cung cấp khác – điều này không tự động vô hiệu hóa người dùng Google hiện có.

Microsoft Entra trả về vai trò ứng dụng và thành viên nhóm chỉ trong token ID, không từ điểm cuối thông tin người dùng. Gramps Web hợp nhất các yêu cầu của token ID vào phản hồi thông tin người dùng để `OIDC_ROLE_CLAIM` hoạt động giống như đối với các nhà cung cấp khác; nơi cả hai đều chứa một yêu cầu, giá trị thông tin người dùng sẽ được ưu tiên.

## Đăng nhập lần đầu và Khởi tạo

Các tài khoản mới được tạo thông qua OIDC bắt đầu ở trạng thái vô hiệu hóa trừ khi ánh xạ vai trò gán cho chúng một vai trò (xem trên). Trên một phiên bản hoàn toàn mới, không ai có thể phê duyệt một tài khoản vô hiệu hóa, và nếu `OIDC_DISABLE_LOCAL_AUTH` cũng được kích hoạt thì cũng không có đăng nhập bằng mật khẩu để quay lại.

!!! warning "Cấu hình một nhóm chủ sở hữu/quản trị viên trước lần đăng nhập đầu tiên"
    Trước khi bất kỳ ai đăng nhập qua OIDC lần đầu tiên, hãy đặt `OIDC_GROUP_OWNER` (hoặc `OIDC_GROUP_ADMIN`) và đảm bảo người dùng đầu tiên thuộc về nhóm đó tại nhà cung cấp. Nếu không, phiên bản không thể được khởi tạo thông qua OIDC.

## Tài khoản và Tên người dùng

Các tài khoản được tạo thông qua OIDC nhận được một tên người dùng được tạo ra, được gán một lần tại thời điểm tạo tài khoản và không bao giờ thay đổi trong các lần đăng nhập sau:

- Các nhà cung cấp tích hợp sẵn: `<provider>_<claim value>`, ví dụ: `microsoft_alice@contoso.com`
- Nhà cung cấp tùy chỉnh: giá trị yêu cầu thuần túy, ví dụ: `alice`

Một hậu tố số sẽ được thêm vào khi có sự trùng lặp. Không có cách nào để đổi tên người dùng của một tài khoản được tạo qua OIDC sau đó; ngược lại, tên đầy đủ và địa chỉ email sẽ được làm mới trong mỗi lần đăng nhập.

Một lần đăng nhập OIDC không bao giờ gắn liền với một tài khoản cục bộ hiện có mà tình cờ chia sẻ địa chỉ email của nó – điều này là có chủ đích, vì việc liên kết các tài khoản bằng email là một vector chiếm đoạt tài khoản. Một người dùng đã có tài khoản cục bộ sẽ nhận được một tài khoản thứ hai, riêng biệt lần đầu tiên họ đăng nhập qua OIDC.

Địa chỉ email từ nhà cung cấp chỉ được lưu trữ nếu nhà cung cấp đánh dấu chúng là đã xác minh (hoặc bỏ qua hoàn toàn yêu cầu `email_verified`); nếu không, đăng nhập sẽ tiếp tục mà không lưu trữ địa chỉ email. Vì địa chỉ email không cần phải duy nhất (kể từ API Gramps Web 3.22), một địa chỉ sẽ được lưu trữ ngay cả khi một tài khoản khác đã sử dụng nó.

## Đăng xuất OIDC

Gramps Web hỗ trợ Đăng xuất một lần (SSO logout) cho các nhà cung cấp OIDC. `GET /api/oidc/logout/` tìm kiếm `end_session_endpoint` của nhà cung cấp và trả về nó dưới dạng `logout_url` trong phản hồi; chính giao diện Gramps Web sẽ điều hướng trình duyệt đến đó để thực sự kết thúc phiên tại nhà cung cấp danh tính. `logout_url` là `null` khi nhà cung cấp không có `end_session_endpoint`.

!!! warning "Các token không bị thu hồi khi đăng xuất"
    Đăng xuất chỉ kết thúc phiên trình duyệt; hiện tại không có cách nào để thu hồi một token Gramps Web đã được phát hành. Các token vẫn hợp lệ cho đến khi chúng hết hạn (`JWT_ACCESS_TOKEN_EXPIRES`, mặc định 15 phút cho các token truy cập), bất kể người dùng đã đăng xuất tại Gramps Web hoặc tại nhà cung cấp danh tính hay chưa.

## Khắc phục sự cố

Bắt đầu từ điểm mà đăng nhập dừng lại và theo dõi nhánh. Gramps Web ghi lại lý do cho một callback thất bại (tìm kiếm `OIDC callback error for provider` trong nhật ký máy chủ), điều này thường cụ thể hơn so với thông điệp hiển thị trong trình duyệt.

**1. Nút đăng nhập có bị thiếu không?**

- Kiểm tra `<BASE_URL>/api/oidc/config/`. Nếu `enabled` là `false` hoặc `providers` là trống, OIDC không được cấu hình: `OIDC_ENABLED` phải là `True`, và một nhà cung cấp tùy chỉnh cần cả `OIDC_ISSUER` và `OIDC_CLIENT_ID`.
- Một nhà cung cấp tích hợp sẵn (Google, Microsoft) chỉ được đăng ký nếu cả ID khách hàng và bí mật khách hàng của nó đều được thiết lập.
- Tìm trong nhật ký máy chủ khi khởi động cho `Could not load discovery document`. Điều này có nghĩa là máy chủ không thể truy cập `<issuer>/.well-known/openid-configuration` (hoặc `OIDC_OPENID_CONFIG_URL`). Nó sẽ thử lại khi sử dụng lần đầu, nhưng container Gramps Web phải có khả năng giải quyết và truy cập URL phát hành, không chỉ trình duyệt của bạn.

**2. Trình duyệt có nhận được lỗi ngay sau khi được gửi đến nhà cung cấp không?**

Lỗi được hiển thị bởi nhà cung cấp danh tính, trước khi bạn đăng nhập.

- *"mismatch URI chuyển hướng"* (hoặc tương tự): URI chuyển hướng đã đăng ký tại nhà cung cấp phải khớp chính xác, bao gồm cả giao thức, máy chủ, cổng và ID nhà cung cấp. Xem [URI chuyển hướng cần thiết](#required-redirect-uris). Lưu ý rằng nó được xây dựng từ `BASE_URL`, vì vậy một `BASE_URL` sai sẽ dẫn đến một URI chuyển hướng sai.
- *Một lỗi PKCE* (ví dụ `invalid_request`, "yêu cầu mã thách thức", hoặc thiếu tham số `code_challenge`): nhà cung cấp yêu cầu PKCE nhưng Gramps Web không gửi nó. Đi tới [nhánh PKCE](#pkce-branch) bên dưới.

**3. Nhà cung cấp có chấp nhận đăng nhập nhưng Gramps Web sau đó hiển thị lỗi?**

- *`mismatching_state`, hoặc lỗi đề cập đến phiên hoặc trạng thái*: trình duyệt không gửi lại cookie phiên mà Gramps Web đã thiết lập khi bắt đầu đăng nhập. Cookie này cũng mang theo bộ xác thực mã PKCE. Đảm bảo rằng địa chỉ trong trình duyệt khớp với `BASE_URL` (cùng giao thức và máy chủ), rằng một proxy đảo ngược truyền cookie và máy chủ gốc qua, và rằng đăng nhập được bắt đầu và hoàn thành trong cùng một tab hoặc cửa sổ trình duyệt.
- *`OIDC authentication failed for <provider>` (HTTP 401)*: kiểm tra nhật ký máy chủ để biết lý do cơ bản. Nguyên nhân phổ biến là bí mật khách hàng sai, URL phát hành không khớp với yêu cầu `iss` của các token, và nhà cung cấp trả về lỗi cho callback (ví dụ PKCE, xem bên dưới).
- *Quá nhiều nỗ lực*: các điểm cuối đăng nhập và callback bị giới hạn tỷ lệ (5 yêu cầu mỗi phút). Chờ một phút và thử lại.

**4. Đăng nhập thành công nhưng bạn thấy "Tài khoản đang xem xét", hoặc không thể làm gì?**

Các tài khoản mới được tạo ở trạng thái vô hiệu hóa trừ khi ánh xạ vai trò gán cho chúng một vai trò. Xem [Đăng nhập lần đầu và Khởi tạo](#first-login-and-bootstrapping) và [Hành vi ánh xạ vai trò](#role-mapping-behavior). Một quản trị viên cũng có thể kích hoạt tài khoản trong Cài đặt > Quản trị > Quản lý người dùng.

### Nhánh PKCE

Gramps Web quyết định có sử dụng PKCE khi một đăng nhập bắt đầu (xem [PKCE](#pkce)). Để tìm hiểu điều gì đã xảy ra cho thiết lập của bạn, hãy làm theo các câu hỏi này theo thứ tự:

1. **`OIDC_PKCE` có được thiết lập không?** (Đối với các nhà cung cấp tích hợp sẵn, `OIDC_GOOGLE_PKCE` hoặc `OIDC_MICROSOFT_PKCE`.)
    - `True`: PKCE được sử dụng. Bỏ qua câu hỏi 3.
    - `False`: PKCE được tắt có chủ đích, và tài liệu khám phá của nhà cung cấp bị bỏ qua. Nếu nhà cung cấp của bạn yêu cầu PKCE, hãy xóa thiết lập hoặc đặt nó thành `True`.
    - Không được đặt, hoặc trống: tiếp tục với câu hỏi 2.
2. **Tài liệu khám phá có liệt kê `S256` không?** Mở `<issuer>/.well-known/openid-configuration` và tìm `S256` trong `code_challenge_methods_supported`.
    - Có: PKCE được sử dụng tự động. Tiếp tục với câu hỏi 3.
    - Không, hoặc trường bị thiếu: PKCE **không** được sử dụng. Đặt `OIDC_PKCE` thành `True` nếu nhà cung cấp của bạn yêu cầu. Cũng kiểm tra nhật ký máy chủ cho `Could not check the provider for PKCE support`, điều này có nghĩa là tài liệu khám phá không thể được lấy và PKCE do đó đã bị tắt.
3. **PKCE có thực sự được gửi không?** Bắt đầu một đăng nhập và nhìn vào địa chỉ của trang đăng nhập của nhà cung cấp (hoặc lần chuyển hướng đầu tiên trong tab mạng của trình duyệt của bạn). Nó nên chứa `code_challenge=` và `code_challenge_method=S256`.
    - Có mặt, nhưng đăng nhập vẫn thất bại tại callback: nhà cung cấp đã từ chối bộ xác thực mã. Cookie phiên có thể đã bị mất giữa chuyển hướng và callback (xem nhánh 3 ở trên), hoặc nhà cung cấp không hỗ trợ `S256`, trong trường hợp đó hãy đặt `OIDC_PKCE` thành `False` nếu nhà cung cấp không yêu cầu PKCE.
    - Vắng mặt: các thiết lập ở trên không được áp dụng. Kiểm tra rằng biến môi trường có tiền tố đúng và giá trị viết thường (ví dụ `GRAMPSWEB_OIDC_PKCE=true` trong Docker; `True` không được đọc là boolean), khởi động lại máy chủ và kiểm tra cấu hình một lần nữa.

!!! note
    Với PKCE được kích hoạt tại nhà cung cấp như *tùy chọn*, hoặc không được kích hoạt, các đăng nhập hoạt động bất kể Gramps Web có gửi một thách thức hay không. Chỉ những nhà cung cấp (hoặc khách hàng) được cấu hình để *yêu cầu* PKCE mới làm cho thiết lập này trở nên quan trọng.

## Ví dụ về Cấu hình

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

### Nhà cung cấp Tích hợp sẵn (Google)

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

# Microsoft OAuth
OIDC_MICROSOFT_CLIENT_ID="your-microsoft-client-id"
OIDC_MICROSOFT_CLIENT_SECRET="your-microsoft-client-secret"
```

### Pocket ID

Tạo một khách hàng OIDC trong Pocket ID với URI chuyển hướng `<BASE_URL>/api/oidc/callback/custom` (xem [URI chuyển hướng cần thiết](#required-redirect-uris)). Nếu bạn kích hoạt "Yêu cầu PKCE" cho khách hàng, không cần cấu hình Gramps Web bổ sung, vì Pocket ID quảng cáo hỗ trợ PKCE trong tài liệu khám phá của nó. Sau đó cấu hình:

```
GRAMPSWEB_OIDC_ENABLED=True
GRAMPSWEB_OIDC_ISSUER=https://id.example.com
GRAMPSWEB_OIDC_CLIENT_ID=<client id>
GRAMPSWEB_OIDC_CLIENT_SECRET=<client secret>
GRAMPSWEB_OIDC_NAME=Pocket ID
```

### Authelia

Một hướng dẫn thiết lập OIDC do cộng đồng tạo cho Gramps Web có sẵn trên [trang tài liệu chính thức của Authelia](https://www.authelia.com/integration/openid-connect/clients/gramps/).

### Keycloak

Hầu hết các cấu hình cho Keycloak có thể để ở mặc định của nó (*Khách hàng → Tạo khách hàng → Kích hoạt xác thực khách hàng*).
Có một vài ngoại lệ:

1. **Phạm vi OpenID** – Phạm vi `openid` không được bao gồm theo mặc định trong tất cả các phiên bản Keycloak. Để tránh sự cố, hãy thêm nó một cách thủ công: *Khách hàng → [Khách hàng Gramps] → Phạm vi khách hàng → Thêm phạm vi → Tên: `openid` → Đặt làm mặc định.*
2. **Vai trò** – Vai trò có thể được gán ở cấp độ khách hàng hoặc toàn cầu theo miền.

    * Nếu bạn đang sử dụng vai trò khách hàng, hãy đặt tùy chọn cấu hình `OIDC_ROLE_CLAIM` thành: `resource_access.[gramps-client-name].roles`
    * Để làm cho các vai trò có thể nhìn thấy với Gramps, hãy điều hướng đến *Phạm vi Khách hàng* (phần cấp cao nhất, không phải dưới khách hàng cụ thể), sau đó: *Vai trò → Mapper → vai trò khách hàng → Thêm vào thông tin người dùng → BẬT.*
