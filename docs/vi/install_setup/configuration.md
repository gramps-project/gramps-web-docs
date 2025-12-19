# Cấu hình máy chủ

Sử dụng hình ảnh Docker mặc định, tất cả cấu hình cần thiết có thể được thực hiện từ trình duyệt. Tuy nhiên, tùy thuộc vào việc triển khai, có thể cần tùy chỉnh cấu hình máy chủ.

Trang này liệt kê tất cả các phương pháp để thay đổi cấu hình và tất cả các tùy chọn cấu hình hiện có.


## Tệp cấu hình so với biến môi trường

Đối với các cài đặt, bạn có thể sử dụng tệp cấu hình hoặc biến môi trường.

Khi bạn sử dụng [cài đặt dựa trên Docker Compose](deployment.md), bạn có thể bao gồm một tệp cấu hình bằng cách thêm mục danh sách sau dưới khóa `volumes:` trong khối `grampsweb:`:

```yaml
      - /path/to/config.cfg:/app/config/config.cfg
```
trong đó `/path/to/config.cfg` là đường dẫn đến tệp cấu hình trong hệ thống tệp của máy chủ của bạn (phía bên phải tham chiếu đến đường dẫn trong container và không được thay đổi).

Khi sử dụng biến môi trường,

- thêm tiền tố `GRAMPSWEB_` vào mỗi tên cài đặt để có được tên của biến môi trường
- Sử dụng hai dấu gạch dưới cho các cài đặt từ điển lồng nhau, ví dụ `GRAMPSWEB_THUMBNAIL_CACHE_CONFIG__CACHE_DEFAULT_TIMEOUT` sẽ thiết lập giá trị của tùy chọn cấu hình `THUMBNAIL_CACHE_CONFIG['CACHE_DEFAULT_TIMEOUT']`

Lưu ý rằng các tùy chọn cấu hình được thiết lập qua môi trường có ưu tiên hơn so với những tùy chọn trong tệp cấu hình. Nếu cả hai đều có mặt, biến môi trường sẽ "thắng".

## Các cài đặt cấu hình hiện có
Các tùy chọn cấu hình sau đây tồn tại.

### Cài đặt bắt buộc

Chìa khóa | Mô tả
----|-------------
`TREE` | Tên của cơ sở dữ liệu cây gia đình để sử dụng. Hiển thị các cây có sẵn với `gramps -l`. Nếu một cây với tên này không tồn tại, một cây mới trống sẽ được tạo ra.
`SECRET_KEY` | Khóa bí mật cho flask. Khóa bí mật không được chia sẻ công khai. Thay đổi nó sẽ làm vô hiệu hóa tất cả các mã thông báo truy cập.
`USER_DB_URI` | URL cơ sở dữ liệu của cơ sở dữ liệu người dùng. Bất kỳ URL nào tương thích với SQLAlchemy đều được phép.

!!! info
    Bạn có thể tạo một khóa bí mật an toàn ví dụ với lệnh

    ```
    python3 -c "import secrets;print(secrets.token_urlsafe(32))"
    ```

### Cài đặt tùy chọn

Chìa khóa | Mô tả
----|-------------
`MEDIA_BASE_DIR` | Đường dẫn sử dụng làm thư mục gốc cho các tệp phương tiện, ghi đè thư mục gốc phương tiện đã được thiết lập trong Gramps. Khi sử dụng [S3](s3.md), phải có dạng `s3://<bucket_name>`
`SEARCH_INDEX_DB_URI` | URL cơ sở dữ liệu cho chỉ mục tìm kiếm. Chỉ `sqlite` hoặc `postgresql` được phép làm backend. Mặc định là `sqlite:///indexdir/search_index.db`, tạo một tệp SQLite trong thư mục `indexdir` tương đối với đường dẫn nơi kịch bản được chạy
`STATIC_PATH` | Đường dẫn để phục vụ các tệp tĩnh từ (ví dụ: một giao diện web tĩnh)
`BASE_URL` | URL cơ sở nơi API có thể được truy cập (ví dụ: `https://mygramps.mydomain.com/`). Điều này là cần thiết ví dụ để xây dựng các liên kết đặt lại mật khẩu chính xác
`CORS_ORIGINS` | Các nguồn mà yêu cầu CORS được phép từ. Theo mặc định, tất cả đều bị cấm. Sử dụng `"*"` để cho phép yêu cầu từ bất kỳ miền nào.
`EMAIL_HOST` | Máy chủ SMTP (ví dụ: để gửi email đặt lại mật khẩu)
`EMAIL_PORT` | Cổng máy chủ SMTP. mặc định là 465
`EMAIL_HOST_USER` | Tên người dùng máy chủ SMTP
`EMAIL_HOST_PASSWORD` | Mật khẩu máy chủ SMTP
`EMAIL_USE_TLS` | **Đã ngừng sử dụng** (sử dụng `EMAIL_USE_SSL` hoặc `EMAIL_USE_STARTTLS` thay vào đó). Boolean, có sử dụng TLS để gửi email hay không. Mặc định là `True`. Khi sử dụng STARTTLS, đặt điều này thành `False` và sử dụng cổng khác với 25.
`EMAIL_USE_SSL` | Boolean, có sử dụng SSL/TLS ngầm định cho SMTP (v3.6.0+). Mặc định là `True` nếu `EMAIL_USE_TLS` không được thiết lập rõ ràng. Thường được sử dụng với cổng 465.
`EMAIL_USE_STARTTLS` | Boolean, có sử dụng STARTTLS rõ ràng cho SMTP (v3.6.0+). Mặc định là `False`. Thường được sử dụng với cổng 587 hoặc 25.
`DEFAULT_FROM_EMAIL` | Địa chỉ "Từ" cho email tự động
`THUMBNAIL_CACHE_CONFIG` | Từ điển với các cài đặt cho bộ nhớ đệm hình thu nhỏ. Xem [Flask-Caching](https://flask-caching.readthedocs.io/en/latest/) để biết các cài đặt có thể có.
`REQUEST_CACHE_CONFIG` | Từ điển với các cài đặt cho bộ nhớ đệm yêu cầu. Xem [Flask-Caching](https://flask-caching.readthedocs.io/en/latest/) để biết các cài đặt có thể có.
`PERSISTENT_CACHE_CONFIG` | Từ điển với các cài đặt cho bộ nhớ đệm bền vững, được sử dụng ví dụ cho telemetry. Xem [Flask-Caching](https://flask-caching.readthedocs.io/en/latest/) để biết các cài đặt có thể có.
`CELERY_CONFIG` | Cài đặt cho hàng đợi tác vụ nền Celery. Xem [Celery](https://docs.celeryq.dev/en/stable/userguide/configuration.html) để biết các cài đặt có thể có.
`REPORT_DIR` | Thư mục tạm thời nơi đầu ra của việc chạy báo cáo Gramps sẽ được lưu trữ
`EXPORT_DIR` | Thư mục tạm thời nơi đầu ra của việc xuất cơ sở dữ liệu Gramps sẽ được lưu trữ
`REGISTRATION_DISABLED` | Nếu `True`, không cho phép đăng ký người dùng mới (mặc định `False`)
`DISABLE_TELEMETRY` | Nếu `True`, vô hiệu hóa telemetry thống kê (mặc định `False`). Xem [telemetry](telemetry.md) để biết chi tiết.


!!! info
    Khi sử dụng biến môi trường cho cấu hình, các tùy chọn boolean như `EMAIL_USE_TLS` phải là chuỗi `true` hoặc `false` (phân biệt chữ hoa chữ thường!).


### Cài đặt chỉ dành cho cơ sở dữ liệu backend PostgreSQL

Điều này là cần thiết nếu bạn đã cấu hình cơ sở dữ liệu Gramps của mình để làm việc với [addon PostgreSQL](https://gramps-project.org/wiki/index.php/Addon:PostgreSQL).

Chìa khóa | Mô tả
----|-------------
`POSTGRES_USER` | Tên người dùng cho kết nối cơ sở dữ liệu
`POSTGRES_PASSWORD` | Mật khẩu cho người dùng cơ sở dữ liệu


### Cài đặt liên quan đến việc lưu trữ nhiều cây

Các cài đặt sau đây có liên quan khi [lưu trữ nhiều cây](multi-tree.md).


Chìa khóa | Mô tả
----|-------------
`MEDIA_PREFIX_TREE` | Boolean, có sử dụng một thư mục con riêng cho các tệp phương tiện của mỗi cây hay không. Mặc định là `False`, nhưng rất khuyến nghị sử dụng `True` trong cài đặt nhiều cây
`NEW_DB_BACKEND` | Backend cơ sở dữ liệu để sử dụng cho các cây gia đình mới được tạo. Phải là một trong `sqlite`, `postgresql`, hoặc `sharedpostgresql`. Mặc định là `sqlite`.
`POSTGRES_HOST` | Tên máy chủ của máy chủ PostgreSQL được sử dụng để tạo các cây mới khi sử dụng cài đặt nhiều cây với backend SharedPostgreSQL
`POSTGRES_PORT` | Cổng của máy chủ PostgreSQL được sử dụng để tạo các cây mới khi sử dụng cài đặt nhiều cây với backend SharedPostgreSQL


### Cài đặt cho xác thực OIDC

Các cài đặt này cần thiết nếu bạn muốn sử dụng xác thực OpenID Connect (OIDC) với các nhà cung cấp bên ngoài. Để biết hướng dẫn cài đặt chi tiết và ví dụ, xem [Xác thực OIDC](oidc.md).

Chìa khóa | Mô tả
----|-------------
`OIDC_ENABLED` | Boolean, có bật xác thực OIDC hay không. Mặc định là `False`.
`OIDC_ISSUER` | URL nhà cung cấp OIDC (đối với các nhà cung cấp OIDC tùy chỉnh)
`OIDC_CLIENT_ID` | ID khách hàng OAuth (đối với các nhà cung cấp OIDC tùy chỉnh)
`OIDC_CLIENT_SECRET` | Mật khẩu khách hàng OAuth (đối với các nhà cung cấp OIDC tùy chỉnh)
`OIDC_NAME` | Tên hiển thị tùy chỉnh cho nhà cung cấp. Mặc định là "OIDC"
`OIDC_SCOPES` | Các phạm vi OAuth. Mặc định là "openid email profile"
`OIDC_USERNAME_CLAIM` | Khẳng định được sử dụng cho tên người dùng. Mặc định là "preferred_username"
`OIDC_OPENID_CONFIG_URL` | Tùy chọn: URL đến điểm cấu hình OpenID Connect (nếu không sử dụng chuẩn `/.well-known/openid-configuration`)
`OIDC_DISABLE_LOCAL_AUTH` | Boolean, có vô hiệu hóa xác thực tên người dùng/mật khẩu cục bộ hay không. Mặc định là `False`
`OIDC_AUTO_REDIRECT` | Boolean, có tự động chuyển hướng đến OIDC khi chỉ có một nhà cung cấp được cấu hình hay không. Mặc định là `False`

#### Các nhà cung cấp OIDC tích hợp sẵn

Đối với các nhà cung cấp tích hợp sẵn (Google, Microsoft, GitHub), sử dụng các cài đặt sau:

Chìa khóa | Mô tả
----|-------------
`OIDC_GOOGLE_CLIENT_ID` | ID khách hàng cho Google OAuth
`OIDC_GOOGLE_CLIENT_SECRET` | Mật khẩu khách hàng cho Google OAuth
`OIDC_MICROSOFT_CLIENT_ID` | ID khách hàng cho Microsoft OAuth
`OIDC_MICROSOFT_CLIENT_SECRET` | Mật khẩu khách hàng cho Microsoft OAuth
`OIDC_GITHUB_CLIENT_ID` | ID khách hàng cho GitHub OAuth
`OIDC_GITHUB_CLIENT_SECRET` | Mật khẩu khách hàng cho GitHub OAuth

#### Phân bổ vai trò OIDC

Các cài đặt này cho phép bạn ánh xạ các nhóm/ vai trò OIDC từ nhà cung cấp danh tính của bạn đến các vai trò người dùng Gramps Web:

Chìa khóa | Mô tả
----|-------------
`OIDC_ROLE_CLAIM` | Tên khẳng định trong mã thông báo OIDC chứa các nhóm/ vai trò của người dùng. Mặc định là "groups"
`OIDC_GROUP_ADMIN` | Tên nhóm/ vai trò từ nhà cung cấp OIDC của bạn ánh xạ đến vai trò "Quản trị viên" của Gramps
`OIDC_GROUP_OWNER` | Tên nhóm/ vai trò từ nhà cung cấp OIDC của bạn ánh xạ đến vai trò "Chủ sở hữu" của Gramps
`OIDC_GROUP_EDITOR` | Tên nhóm/ vai trò từ nhà cung cấp OIDC của bạn ánh xạ đến vai trò "Biên tập viên" của Gramps
`OIDC_GROUP_CONTRIBUTOR` | Tên nhóm/ vai trò từ nhà cung cấp OIDC của bạn ánh xạ đến vai trò "Người đóng góp" của Gramps
`OIDC_GROUP_MEMBER` | Tên nhóm/ vai trò từ nhà cung cấp OIDC của bạn ánh xạ đến vai trò "Thành viên" của Gramps
`OIDC_GROUP_GUEST` | Tên nhóm/ vai trò từ nhà cung cấp OIDC của bạn ánh xạ đến vai trò "Khách" của Gramps

### Cài đặt chỉ dành cho các tính năng AI

Các cài đặt này cần thiết nếu bạn muốn sử dụng các tính năng được hỗ trợ bởi AI như trò chuyện hoặc tìm kiếm ngữ nghĩa.

Chìa khóa | Mô tả
----|-------------
`LLM_BASE_URL` | URL cơ sở cho API trò chuyện tương thích với OpenAI. Mặc định là `None`, sử dụng API OpenAI.
`LLM_MODEL` | Mô hình để sử dụng cho API trò chuyện tương thích với OpenAI. Nếu không đặt (mặc định), trò chuyện sẽ bị vô hiệu hóa. Từ phiên bản v3.6.0, trợ lý AI sử dụng Pydantic AI với khả năng gọi công cụ.
`VECTOR_EMBEDDING_MODEL` | Mô hình [Sentence Transformers](https://sbert.net/) để sử dụng cho các nhúng vector tìm kiếm ngữ nghĩa. Nếu không đặt (mặc định), tìm kiếm ngữ nghĩa và trò chuyện sẽ bị vô hiệu hóa.
`LLM_MAX_CONTEXT_LENGTH` | Giới hạn ký tự cho ngữ cảnh cây gia đình được cung cấp cho LLM. Mặc định là 50000.
`LLM_SYSTEM_PROMPT` | Lời nhắc hệ thống tùy chỉnh cho trợ lý trò chuyện LLM (v3.6.0+). Nếu không đặt, sử dụng lời nhắc tối ưu hóa genealology mặc định.


## Ví dụ tệp cấu hình

Một tệp cấu hình tối thiểu cho sản xuất có thể trông như thế này:
```python
TREE="My Family Tree"
BASE_URL="https://mytree.example.com"
SECRET_KEY="..."  # khóa bí mật của bạn
USER_DB_URI="sqlite:////path/to/users.sqlite"
EMAIL_HOST="mail.example.com"
EMAIL_PORT=465
EMAIL_USE_SSL=True  # Sử dụng SSL ngầm định cho cổng 465
EMAIL_HOST_USER="gramps@example.com"
EMAIL_HOST_PASSWORD="..." # mật khẩu SMTP của bạn
DEFAULT_FROM_EMAIL="gramps@example.com"
