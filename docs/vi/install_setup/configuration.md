# Cấu hình máy chủ

Khi sử dụng image Docker mặc định, bạn có thể thực hiện mọi cấu hình cần thiết từ trình duyệt. Tuy nhiên, tùy thuộc vào cách triển khai, bạn có thể cần tùy chỉnh cấu hình máy chủ.

Trang này liệt kê tất cả các phương thức thay đổi cấu hình và tất cả các tùy chọn cấu hình hiện có.


## Tệp cấu hình và biến môi trường

Đối với các thiết lập, bạn có thể sử dụng tệp cấu hình hoặc các biến môi trường.

Khi bạn sử dụng [thiết lập dựa trên Docker Compose](deployment.md), bạn có thể thêm tệp cấu hình bằng cách thêm mục danh sách sau bên dưới khóa `volumes:` trong khối `grampsweb:`:

```yaml
      - /path/to/config.cfg:/app/config/config.cfg
```
trong đó `/path/to/config.cfg` là đường dẫn đến tệp cấu hình trong hệ thống tệp của máy chủ (vế bên phải là đường dẫn trong container và không được thay đổi).

Khi sử dụng các biến môi trường,

- thêm tiền tố `GRAMPSWEB_` vào trước mỗi tên thiết lập để lấy tên của biến môi trường
- Sử dụng hai dấu gạch dưới cho các thiết lập từ điển lồng nhau, ví dụ: `GRAMPSWEB_THUMBNAIL_CACHE_CONFIG__CACHE_DEFAULT_TIMEOUT` sẽ đặt giá trị của tùy chọn cấu hình `THUMBNAIL_CACHE_CONFIG['CACHE_DEFAULT_TIMEOUT']`

Lưu ý rằng các tùy chọn cấu hình được thiết lập thông qua môi trường sẽ được ưu tiên hơn các tùy chọn trong tệp cấu hình. Nếu cả hai đều tồn tại, biến môi trường sẽ được ưu tiên.

!!! warning "Các biến môi trường không có tiền tố đã lỗi thời"
    Vì lý do lịch sử, một số ít thiết lập – `TREE`, `SECRET_KEY`, `USER_DB_URI`, `POSTGRES_USER`, `POSTGRES_PASSWORD`, `MEDIA_BASE_DIR`, `SEARCH_INDEX_DIR`, `EMAIL_HOST`, `EMAIL_PORT`, `EMAIL_HOST_USER`, `EMAIL_HOST_PASSWORD`, `DEFAULT_FROM_EMAIL`, `BASE_URL` và `STATIC_PATH` – vẫn có thể được đặt thông qua biến môi trường *không có* tiền tố `GRAMPSWEB_`. Cách này đã lỗi thời, sẽ ghi cảnh báo khi khởi động và sẽ ngừng hoạt động trong một bản phát hành tương lai. Luôn sử dụng dạng có tiền tố, ví dụ: `GRAMPSWEB_TREE` thay vì `TREE`.

    Lưu ý rằng điều này chỉ liên quan đến các biến môi trường. Trong tệp cấu hình, tên các thiết lập luôn được sử dụng mà không có tiền tố.

!!! tip "Kiểm tra các tùy chọn đã lỗi thời"
    Các tùy chọn cấu hình đã lỗi thời mà máy chủ của bạn vẫn phụ thuộc vào – chẳng hạn như các biến môi trường không có tiền tố, `SEARCH_INDEX_DIR` hoặc `EMAIL_USE_TLS` – sẽ được ghi dưới dạng cảnh báo khi khởi động. Kể từ Gramps Web API 3.22, chúng cũng được liệt kê, cùng với tùy chọn thay thế và phiên bản sẽ xóa hỗ trợ, ở đầu trang **Thông tin hệ thống** (có thể truy cập thông qua biểu tượng người dùng trên thanh ứng dụng phía trên) khi bạn đăng nhập với tư cách quản trị viên.

    Các thiết lập e-mail và URL cơ sở mà trình hướng dẫn thiết lập lần đầu của các phiên bản cũ hơn đã lưu trong cơ sở dữ liệu cũng được liệt kê ở đó. Hãy đặt chúng trong cấu hình của bạn thành các giá trị đã lưu; cảnh báo sẽ biến mất khi chúng khớp nhau.

## Các thiết lập cấu hình hiện có
Các tùy chọn cấu hình sau đây hiện có.

### Các thiết lập bắt buộc

Key | Description
----|-------------
`TREE` | Tên của cơ sở dữ liệu cây gia đình cần sử dụng. Hiển thị các cây hiện có bằng `gramps -l`. Nếu không tồn tại cây có tên này, một cây mới trống sẽ được tạo.
`SECRET_KEY` | Khóa bí mật cho flask. Không được công khai khóa bí mật. Việc thay đổi khóa này sẽ làm mất hiệu lực của tất cả token truy cập.
`USER_DB_URI` | URL cơ sở dữ liệu của cơ sở dữ liệu người dùng. Cho phép mọi URL tương thích với SQLAlchemy.

!!! info
    Bạn có thể tạo khóa bí mật an toàn, chẳng hạn bằng lệnh

    ```
    python3 -c "import secrets;print(secrets.token_urlsafe(32))"
    ```

### Các thiết lập tùy chọn

Key | Description
----|-------------
`MEDIA_BASE_DIR` | Đường dẫn được sử dụng làm thư mục cơ sở cho các tệp phương tiện, ghi đè thư mục cơ sở phương tiện được thiết lập trong Gramps. Khi sử dụng [S3](s3.md), phải có dạng `s3://<bucket_name>`
`TREE_ID` | Tên thư mục của cơ sở dữ liệu cây gia đình cần sử dụng trong chế độ một cây (khi `TREE` không được đặt thành `*`). Khi được đặt, máy chủ sẽ nhận diện cây theo tên thư mục thay vì tên hiển thị, giúp việc đổi tên đáng tin cậy hơn. Bắt buộc nếu bạn muốn đổi tên cây thông qua API. Có thể tìm tên thư mục thông qua `GET /api/trees/-` (trường `id`).
`SEARCH_INDEX_DB_URI` | URL cơ sở dữ liệu cho chỉ mục tìm kiếm. Chỉ cho phép `sqlite` hoặc `postgresql` làm phần phụ trợ. Mặc định là `sqlite:///indexdir/search_index.db`, tạo một tệp SQLite trong thư mục `indexdir` tương đối với đường dẫn nơi tập lệnh được chạy
`SEARCH_INDEX_DIR` | **Đã lỗi thời** (thay vào đó sử dụng `SEARCH_INDEX_DB_URI`). Thư mục chứa chỉ mục tìm kiếm. Nếu được đặt trong khi `SEARCH_INDEX_DB_URI` chưa được đặt, URL chỉ mục tìm kiếm sẽ được suy ra là `sqlite:///<SEARCH_INDEX_DIR>/search_index.db`.
`STATIC_PATH` | Đường dẫn để cung cấp các tệp tĩnh (ví dụ: giao diện web tĩnh)
`BASE_URL` | URL cơ sở nơi có thể truy cập API (ví dụ: `https://mygramps.mydomain.com/`). URL này cần thiết, chẳng hạn để tạo đúng các liên kết đặt lại mật khẩu. Web Push cũng yêu cầu một URL HTTPS có thể truy cập công khai; `http://localhost/` mặc định sẽ tắt Web Push. Khi cấu hình thiết lập này thông qua môi trường, hãy sử dụng `GRAMPSWEB_BASE_URL`.
`CORS_ORIGINS` | Các origin mà từ đó các yêu cầu CORS được phép. Theo mặc định, tất cả đều bị từ chối. Sử dụng `"*"` để cho phép yêu cầu từ bất kỳ miền nào.
`EMAIL_HOST` | Máy chủ SMTP (ví dụ: để gửi e-mail đặt lại mật khẩu)
`EMAIL_PORT` | Cổng máy chủ SMTP. mặc định là 465
`EMAIL_HOST_USER` | Tên người dùng máy chủ SMTP
`EMAIL_HOST_PASSWORD` | Mật khẩu máy chủ SMTP
`EMAIL_USE_TLS` | **Đã lỗi thời** (thay vào đó sử dụng `EMAIL_USE_SSL` hoặc `EMAIL_USE_STARTTLS`). Giá trị Boolean cho biết có sử dụng TLS để gửi e-mail hay không. Mặc định là `True`. Khi sử dụng STARTTLS, đặt giá trị này thành `False` và sử dụng cổng khác 25.
`EMAIL_USE_SSL` | Giá trị Boolean cho biết có sử dụng SSL/TLS ngầm định cho SMTP hay không (v3.6.0+). Mặc định là `True` nếu `EMAIL_USE_TLS` chưa được đặt rõ ràng. Thường được sử dụng với cổng 465.
`EMAIL_USE_STARTTLS` | Giá trị Boolean cho biết có sử dụng STARTTLS tường minh cho SMTP hay không (v3.6.0+). Mặc định là `False`. Thường được sử dụng với cổng 587 hoặc 25.
`DEFAULT_FROM_EMAIL` | Địa chỉ "From" cho các e-mail tự động
`THUMBNAIL_CACHE_CONFIG` | Từ điển chứa các thiết lập cho bộ nhớ đệm hình thu nhỏ. Xem [Flask-Caching](https://flask-caching.readthedocs.io/en/latest/) để biết các thiết lập có thể sử dụng.
`REQUEST_CACHE_CONFIG` | Từ điển chứa các thiết lập cho bộ nhớ đệm yêu cầu. Xem [Flask-Caching](https://flask-caching.readthedocs.io/en/latest/) để biết các thiết lập có thể sử dụng.
`PERSISTENT_CACHE_CONFIG` | Từ điển chứa các thiết lập cho bộ nhớ đệm liên tục, được sử dụng chẳng hạn cho hoạt động đo từ xa. Xem [Flask-Caching](https://flask-caching.readthedocs.io/en/latest/) để biết các thiết lập có thể sử dụng.
`CELERY_CONFIG` | Các thiết lập cho hàng đợi tác vụ nền Celery. Xem [Celery](https://docs.celeryq.dev/en/stable/userguide/configuration.html) để biết các thiết lập có thể sử dụng.
`REPORT_DIR` | Thư mục tạm thời nơi lưu đầu ra của các báo cáo Gramps được chạy
`EXPORT_DIR` | Thư mục tạm thời nơi lưu đầu ra của việc xuất cơ sở dữ liệu Gramps
`BACKUP_DIR` | Thư mục nơi lưu [bản sao lưu](../administration/backups.md), trong một thư mục con riêng cho mỗi cây (v3.24.0+). Nếu không được đặt (mặc định), không thể lưu bản sao lưu trên máy chủ, nhưng bạn vẫn có thể khôi phục từ một tệp đã tải lên. Hãy sử dụng một vị trí liên tục, chẳng hạn một volume Docker, và tốt nhất là vị trí đó cũng được sao lưu hoặc đồng bộ ở nơi khác.
`BACKUP_KEEP` | Số lượng bản sao lưu được lưu giữ cho mỗi cây; các bản cũ hơn sẽ bị xóa khi tạo bản sao lưu mới (v3.24.0+). Mặc định là `5`
`RATE_LIMIT_BACKUP` | Giới hạn tốc độ tạo bản sao lưu, cho mỗi cây (v3.24.0+). Mặc định là `"10 per day"`
`RATE_LIMIT_MEDIA_ARCHIVE` | Giới hạn tốc độ tạo kho lưu trữ phương tiện trên trang Export. Mặc định là `"1 per hour"`
`REGISTRATION_DISABLED` | Nếu là `True`, không cho phép đăng ký người dùng mới (mặc định là `False`). Kể từ Gramps Web API 3.26, trang đăng nhập cũng sẽ ẩn liên kết đăng ký.
`PROXY_FIX_X_FOR` | Số lượng proxy ngược đáng tin cậy ở phía trước Gramps Web (v3.26.0+). Đặt thành `1` khi ở phía sau một proxy ngược duy nhất để các giới hạn tốc độ được áp dụng cho từng máy khách thay vì áp dụng cho tất cả người dùng cùng nhau. Mặc định là `0`. Chỉ đặt tùy chọn này nếu máy chủ chỉ có thể được truy cập thông qua các proxy đó.
`DISABLE_TELEMETRY` | Nếu là `True`, tắt hoạt động đo từ xa thống kê (mặc định là `False`). Xem [đo từ xa](telemetry.md) để biết chi tiết.
`PILLOW_MAX_IMAGE_PIXELS` | Đặt tham số PIL.Image.MAX_IMAGE_PIXELS, cho biết số pixel mà hình ảnh được xử lý có thể chứa. Xem [tài liệu](https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.MAX_IMAGE_PIXELS) để biết chi tiết.
`MAX_THUMBNAIL_FILE_BYTES` | Đặt kích thước tệp tối đa cứng cho hình thu nhỏ. Mặc định là `50 * 1024 * 1024` (50 MB). Việc tăng giá trị này có thể làm tăng đáng kể mức sử dụng bộ nhớ và dẫn đến lỗi hết bộ nhớ hoặc mất dữ liệu nếu các tệp lớn được giải nén trong bộ nhớ.


!!! info
    Khi sử dụng các biến môi trường để cấu hình, các tùy chọn Boolean như `EMAIL_USE_SSL` phải là chuỗi `true` hoặc `false` (phân biệt chữ hoa chữ thường!).


### Các thiết lập cho cơ sở dữ liệu PostgreSQL

Các thiết lập này là bắt buộc nếu cây gia đình của bạn được lưu trữ trong [cơ sở dữ liệu PostgreSQL](postgres.md) bằng addon SharedPostgreSQL.

Key | Description
----|-------------
`POSTGRES_USER` | Tên người dùng cho kết nối cơ sở dữ liệu
`POSTGRES_PASSWORD` | Mật khẩu của người dùng cơ sở dữ liệu


### Các thiết lập liên quan đến việc lưu trữ nhiều cây

Các thiết lập sau đây liên quan khi [lưu trữ nhiều cây](multi-tree.md).


Key | Description
----|-------------
`MEDIA_PREFIX_TREE` | Giá trị Boolean cho biết có sử dụng thư mục con riêng cho các tệp phương tiện của từng cây hay không. Mặc định là `False`, nhưng bạn nên sử dụng `True` trong thiết lập nhiều cây
`NEW_DB_BACKEND` | Phần phụ trợ cơ sở dữ liệu cần sử dụng cho các cây gia đình mới được tạo. Phải là `sqlite` hoặc `sharedpostgresql`. Mặc định là `sqlite`. Giá trị `postgresql` vẫn được chấp nhận nhưng đã lỗi thời, vì phần phụ trợ PostgreSQL sẽ bị xóa trong Gramps Web API 4.0.
`POSTGRES_HOST` | Tên máy chủ PostgreSQL được sử dụng để tạo cây mới khi sử dụng thiết lập nhiều cây với phần phụ trợ SharedPostgreSQL
`POSTGRES_PORT` | Cổng của máy chủ PostgreSQL được sử dụng để tạo cây mới khi sử dụng thiết lập nhiều cây với phần phụ trợ SharedPostgreSQL


### Các thiết lập cho xác thực OIDC

Các thiết lập này cần thiết nếu bạn muốn sử dụng xác thực OpenID Connect (OIDC) với các nhà cung cấp bên ngoài. Để biết hướng dẫn thiết lập chi tiết và ví dụ, hãy xem [Xác thực OIDC](oidc.md).

Key | Description
----|-------------
`OIDC_ENABLED` | Giá trị Boolean cho biết có bật xác thực OIDC hay không. Mặc định là `False`.
`OIDC_ISSUER` | URL issuer của nhà cung cấp OIDC (đối với các nhà cung cấp OIDC tùy chỉnh)
`OIDC_CLIENT_ID` | ID máy khách OAuth (đối với các nhà cung cấp OIDC tùy chỉnh)
`OIDC_CLIENT_SECRET` | Bí mật máy khách OAuth (đối với các nhà cung cấp OIDC tùy chỉnh)
`OIDC_NAME` | Tên hiển thị tùy chỉnh cho nhà cung cấp. Mặc định là "OIDC"
`OIDC_SCOPES` | Các scope OAuth. Mặc định là "openid email profile"
`OIDC_USERNAME_CLAIM` | Claim được sử dụng cho tên người dùng. Mặc định là "preferred_username"
`OIDC_OPENID_CONFIG_URL` | Tùy chọn: URL đến endpoint cấu hình OpenID Connect (nếu không sử dụng `/.well-known/openid-configuration` tiêu chuẩn)
`OIDC_PKCE` | Giá trị Boolean cho biết có sử dụng PKCE hay không. Nếu không được đặt, PKCE sẽ được sử dụng khi tài liệu discovery của nhà cung cấp liệt kê `S256`. Xem [PKCE](oidc.md#pkce)
`OIDC_DISABLE_LOCAL_AUTH` | Giá trị Boolean cho biết có tắt xác thực tên người dùng/mật khẩu cục bộ hay không. Mặc định là `False`
`OIDC_AUTO_REDIRECT` | Giá trị Boolean cho biết có tự động chuyển hướng đến OIDC khi chỉ cấu hình một nhà cung cấp hay không. Mặc định là `False`
`OIDC_ALLOWED_REDIRECT_URIS` | Danh sách các URI `https` tại đó ứng dụng gốc có thể nhận kết quả đăng nhập (v3.26.0+), được đặt dưới dạng danh sách JSON trong một biến môi trường. Mặc định là rỗng. Chỉ cần thiết nếu tài liệu của ứng dụng gốc yêu cầu. Xem [Ứng dụng gốc](oidc.md#native-apps)

#### Các nhà cung cấp OIDC tích hợp sẵn

Đối với các nhà cung cấp tích hợp sẵn (Google, Microsoft), hãy sử dụng các thiết lập sau:

Key | Description
----|-------------
`OIDC_GOOGLE_CLIENT_ID` | ID máy khách cho Google OAuth
`OIDC_GOOGLE_CLIENT_SECRET` | Bí mật máy khách cho Google OAuth
`OIDC_MICROSOFT_CLIENT_ID` | ID máy khách cho Microsoft OAuth
`OIDC_MICROSOFT_CLIENT_SECRET` | Bí mật máy khách cho Microsoft OAuth
`OIDC_GOOGLE_PKCE` | Giá trị Boolean, thiết lập PKCE cho Google, xem [PKCE](oidc.md#pkce)
`OIDC_MICROSOFT_PKCE` | Giá trị Boolean, thiết lập PKCE cho Microsoft, xem [PKCE](oidc.md#pkce)

#### Ánh xạ vai trò OIDC

Các thiết lập này cho phép bạn ánh xạ nhóm/vai trò OIDC từ nhà cung cấp danh tính của mình sang các vai trò người dùng Gramps Web:

Key | Description
----|-------------
`OIDC_ROLE_CLAIM` | Tên claim trong token OIDC chứa các nhóm/vai trò của người dùng. Mặc định là "groups"
`OIDC_GROUP_ADMIN` | Tên nhóm/vai trò từ nhà cung cấp OIDC của bạn được ánh xạ tới vai trò "Admin" của Gramps
`OIDC_GROUP_OWNER` | Tên nhóm/vai trò từ nhà cung cấp OIDC của bạn được ánh xạ tới vai trò "Owner" của Gramps
`OIDC_GROUP_EDITOR` | Tên nhóm/vai trò từ nhà cung cấp OIDC của bạn được ánh xạ tới vai trò "Editor" của Gramps
`OIDC_GROUP_CONTRIBUTOR` | Tên nhóm/vai trò từ nhà cung cấp OIDC của bạn được ánh xạ tới vai trò "Contributor" của Gramps
`OIDC_GROUP_MEMBER` | Tên nhóm/vai trò từ nhà cung cấp OIDC của bạn được ánh xạ tới vai trò "Member" của Gramps
`OIDC_GROUP_GUEST` | Tên nhóm/vai trò từ nhà cung cấp OIDC của bạn được ánh xạ tới vai trò "Guest" của Gramps

### Các thiết lập chỉ dành cho tính năng AI

Các thiết lập này cần thiết nếu bạn muốn sử dụng trò chuyện AI. Xem [Thiết lập trò chuyện AI](chat.md) để biết chi tiết.

!!! note
    Các thiết lập `VECTOR_EMBEDDING_MODEL`, `VECTOR_EMBEDDING_BASE_URL` và `VECTOR_EMBEDDING_API_KEY` cho tìm kiếm ngữ nghĩa bị bỏ qua kể từ Gramps Web API 3.25, phiên bản đã loại bỏ tìm kiếm ngữ nghĩa. Trò chuyện AI chỉ cần `LLM_MODEL`.

Key | Description
----|-------------
`LLM_BASE_URL` | URL cơ sở cho API trò chuyện tương thích với OpenAI. Mặc định là `None`, giá trị này sử dụng OpenAI API.
`LLM_MODEL` | Mô hình cần sử dụng cho API trò chuyện tương thích với OpenAI. Nếu không được đặt (mặc định), trò chuyện sẽ bị tắt. Kể từ v3.6.0, trợ lý AI sử dụng Pydantic AI với khả năng gọi công cụ.
`LLM_MAX_OUTPUT_TOKENS` | Số token tối đa mà mô hình có thể tạo trong một phản hồi. Theo mặc định không được đặt, để máy chủ mô hình tự quyết định giới hạn. Hữu ích cho các máy chủ mô hình không có giới hạn riêng, nơi phản hồi có thể tiếp tục vô thời hạn.
`LLM_MAX_CONTEXT_LENGTH` | Giới hạn ký tự cho ngữ cảnh cây gia đình được cung cấp cho LLM. Mặc định là 50000.
`LLM_SYSTEM_PROMPT` | System prompt tùy chỉnh cho trợ lý trò chuyện LLM (v3.6.0+). Nếu không được đặt, sẽ sử dụng prompt mặc định được tối ưu hóa cho phả hệ.
`LLM_VISION` | Giá trị Boolean cho biết người dùng có thể đính kèm hình ảnh vào câu hỏi hay không (v3.26.0+). Chỉ bật tùy chọn này nếu mô hình chấp nhận hình ảnh. Mặc định là `False`. Xem [Hình ảnh trong câu hỏi](chat.md#images-in-questions)
`LLM_ALLOW_WRITE_PROPOSALS` | Giá trị Boolean cho biết trợ lý có thể đề xuất thay đổi đối với cây để người dùng xem xét và áp dụng hay không (v3.26.0+). Mặc định là `False`. Xem [Cho phép trợ lý đề xuất thay đổi](chat.md#letting-the-assistant-propose-changes)


## Ví dụ về tệp cấu hình

Một tệp cấu hình tối thiểu cho môi trường production có thể trông như sau:
```python
TREE="My Family Tree"
BASE_URL="https://mytree.example.com"
SECRET_KEY="..."  # your secret key
USER_DB_URI="sqlite:////path/to/users.sqlite"
EMAIL_HOST="mail.example.com"
EMAIL_PORT=465
EMAIL_USE_SSL=True  # Use implicit SSL for port 465
EMAIL_HOST_USER="gramps@example.com"
EMAIL_HOST_PASSWORD="..." # your SMTP password
DEFAULT_FROM_EMAIL="gramps@example.com"
```
