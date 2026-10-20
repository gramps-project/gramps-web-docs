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

- tiền tố mỗi tên cài đặt với `GRAMPSWEB_` để có được tên của biến môi trường
- Sử dụng dấu gạch dưới đôi cho các cài đặt từ điển lồng nhau, ví dụ `GRAMPSWEB_THUMBNAIL_CACHE_CONFIG__CACHE_DEFAULT_TIMEOUT` sẽ thiết lập giá trị cho tùy chọn cấu hình `THUMBNAIL_CACHE_CONFIG['CACHE_DEFAULT_TIMEOUT']`

Lưu ý rằng các tùy chọn cấu hình được thiết lập qua môi trường có ưu tiên hơn so với các tùy chọn trong tệp cấu hình. Nếu cả hai đều có mặt, biến môi trường "thắng".

!!! warning "Các biến môi trường không có tiền tố đã lỗi thời"
    Vì lý do lịch sử, một số cài đặt – `TREE`, `SECRET_KEY`, `USER_DB_URI`, `POSTGRES_USER`, `POSTGRES_PASSWORD`, `MEDIA_BASE_DIR`, `SEARCH_INDEX_DIR`, `EMAIL_HOST`, `EMAIL_PORT`, `EMAIL_HOST_USER`, `EMAIL_HOST_PASSWORD`, `DEFAULT_FROM_EMAIL`, `BASE_URL`, và `STATIC_PATH` – vẫn có thể được thiết lập qua một biến môi trường *không có* tiền tố `GRAMPSWEB_`. Điều này đã lỗi thời, ghi lại một cảnh báo khi khởi động, và sẽ ngừng hoạt động trong một phiên bản tương lai. Luôn sử dụng dạng có tiền tố, ví dụ `GRAMPSWEB_TREE` thay vì `TREE`.

    Lưu ý rằng điều này chỉ liên quan đến các biến môi trường. Trong một tệp cấu hình, các tên cài đặt luôn được sử dụng mà không có tiền tố.

!!! tip "Kiểm tra các tùy chọn đã lỗi thời"
    Các tùy chọn cấu hình đã lỗi thời mà máy chủ của bạn vẫn phụ thuộc vào – chẳng hạn như biến môi trường không có tiền tố, `SEARCH_INDEX_DIR`, hoặc `EMAIL_USE_TLS` – được ghi lại như các cảnh báo khi khởi động. Kể từ Gramps Web API 3.22, chúng cũng được liệt kê, cùng với sự thay thế của chúng và phiên bản mà hỗ trợ sẽ bị loại bỏ, ở đầu trang **Thông tin Hệ thống** (có thể truy cập qua biểu tượng người dùng trong thanh ứng dụng trên cùng) khi bạn đăng nhập với tư cách là quản trị viên.

## Các cài đặt cấu hình hiện có
Các tùy chọn cấu hình sau đây tồn tại.

### Cài đặt bắt buộc

Khóa | Mô tả
----|-------------
`TREE` | Tên của cơ sở dữ liệu cây gia đình để sử dụng. Hiển thị các cây có sẵn với `gramps -l`. Nếu một cây với tên này không tồn tại, một cây mới rỗng sẽ được tạo ra.
`SECRET_KEY` | Khóa bí mật cho flask. Khóa bí mật không được chia sẻ công khai. Thay đổi nó sẽ làm vô hiệu tất cả các mã thông báo truy cập.
`USER_DB_URI` | URL cơ sở dữ liệu của cơ sở dữ liệu người dùng. Bất kỳ URL nào tương thích với SQLAlchemy đều được phép.

!!! info
    Bạn có thể tạo một khóa bí mật an toàn ví dụ như với lệnh

    ```
    python3 -c "import secrets;print(secrets.token_urlsafe(32))"
    ```

### Cài đặt tùy chọn

Khóa | Mô tả
----|-------------
`MEDIA_BASE_DIR` | Đường dẫn để sử dụng làm thư mục gốc cho các tệp phương tiện, ghi đè thư mục gốc phương tiện được thiết lập trong Gramps. Khi sử dụng [S3](s3.md), phải có dạng `s3://<bucket_name>`
`TREE_ID` | Tên thư mục của cơ sở dữ liệu cây gia đình để sử dụng trong chế độ một cây (khi `TREE` không được đặt thành `*`). Khi được thiết lập, máy chủ xác định cây theo tên thư mục của nó thay vì tên hiển thị của nó, điều này bền vững hơn với việc đổi tên. Bắt buộc nếu bạn muốn đổi tên cây qua API. Tên thư mục có thể được tìm thấy qua `GET /api/trees/-` (trường `id`).
`SEARCH_INDEX_DB_URI` | URL cơ sở dữ liệu cho chỉ mục tìm kiếm. Chỉ `sqlite` hoặc `postgresql` được phép làm backend. Mặc định là `sqlite:///indexdir/search_index.db`, tạo một tệp SQLite trong thư mục `indexdir` tương đối với đường dẫn nơi kịch bản được chạy
`SEARCH_INDEX_DIR` | **Đã lỗi thời** (sử dụng `SEARCH_INDEX_DB_URI` thay thế). Thư mục chứa chỉ mục tìm kiếm. Nếu được thiết lập trong khi `SEARCH_INDEX_DB_URI` chưa được thiết lập, URL chỉ mục tìm kiếm được suy ra là `sqlite:///<SEARCH_INDEX_DIR>/search_index.db`.
`STATIC_PATH` | Đường dẫn để phục vụ các tệp tĩnh từ (ví dụ: một giao diện web tĩnh)
`BASE_URL` | URL gốc nơi API có thể được truy cập (ví dụ: `https://mygramps.mydomain.com/`). Điều này là cần thiết ví dụ để xây dựng các liên kết đặt lại mật khẩu chính xác. Web Push cũng yêu cầu một URL HTTPS có thể truy cập công khai; mặc định `http://localhost/` vô hiệu hóa Web Push. Khi cấu hình cài đặt này thông qua môi trường, sử dụng `GRAMPSWEB_BASE_URL`.
`CORS_ORIGINS` | Các nguồn mà yêu cầu CORS được phép từ. Mặc định, tất cả đều bị từ chối. Sử dụng `"*"` để cho phép yêu cầu từ bất kỳ miền nào.
`EMAIL_HOST` | Máy chủ SMTP (ví dụ: để gửi email đặt lại mật khẩu)
`EMAIL_PORT` | Cổng máy chủ SMTP. mặc định là 465
`EMAIL_HOST_USER` | Tên người dùng máy chủ SMTP
`EMAIL_HOST_PASSWORD` | Mật khẩu máy chủ SMTP
`EMAIL_USE_TLS` | **Đã lỗi thời** (sử dụng `EMAIL_USE_SSL` hoặc `EMAIL_USE_STARTTLS` thay thế). Boolean, có sử dụng TLS để gửi email hay không. Mặc định là `True`. Khi sử dụng STARTTLS, đặt giá trị này thành `False` và sử dụng cổng khác với 25.
`EMAIL_USE_SSL` | Boolean, có sử dụng SSL/TLS ẩn cho SMTP (v3.6.0+). Mặc định là `True` nếu `EMAIL_USE_TLS` không được thiết lập rõ ràng. Thường được sử dụng với cổng 465.
`EMAIL_USE_STARTTLS` | Boolean, có sử dụng STARTTLS rõ ràng cho SMTP (v3.6.0+). Mặc định là `False`. Thường được sử dụng với cổng 587 hoặc 25.
`DEFAULT_FROM_EMAIL` | Địa chỉ "Từ" cho các email tự động
`THUMBNAIL_CACHE_CONFIG` | Từ điển với các cài đặt cho bộ nhớ cache hình thu nhỏ. Xem [Flask-Caching](https://flask-caching.readthedocs.io/en/latest/) để biết các cài đặt có thể.
`REQUEST_CACHE_CONFIG` | Từ điển với các cài đặt cho bộ nhớ cache yêu cầu. Xem [Flask-Caching](https://flask-caching.readthedocs.io/en/latest/) để biết các cài đặt có thể.
`PERSISTENT_CACHE_CONFIG` | Từ điển với các cài đặt cho bộ nhớ cache bền vững, được sử dụng ví dụ cho telemetry. Xem [Flask-Caching](https://flask-caching.readthedocs.io/en/latest/) để biết các cài đặt có thể.
`CELERY_CONFIG` | Các cài đặt cho hàng đợi tác vụ nền Celery. Xem [Celery](https://docs.celeryq.dev/en/stable/userguide/configuration.html) để biết các cài đặt có thể.
`REPORT_DIR` | Thư mục tạm thời nơi đầu ra của các báo cáo Gramps sẽ được lưu trữ
`EXPORT_DIR` | Thư mục tạm thời nơi đầu ra của việc xuất cơ sở dữ liệu Gramps sẽ được lưu trữ
`BACKUP_DIR` | Thư mục nơi [sao lưu](../administration/settings.md#backups) được lưu trữ, trong một thư mục con theo cây (v3.24.0+). Nếu không được thiết lập (mặc định), các bản sao lưu không thể được lưu trữ trên máy chủ, nhưng vẫn có thể được khôi phục từ một tệp đã tải lên. Sử dụng một vị trí bền vững, ví dụ như một volume Docker, và tốt nhất là một vị trí cũng được sao lưu hoặc đồng bộ hóa ở nơi khác.
`BACKUP_KEEP` | Số lượng sao lưu được lưu giữ cho mỗi cây; các bản sao lưu cũ hơn sẽ bị xóa khi một bản sao lưu mới được tạo (v3.24.0+). Mặc định là `5`
`RATE_LIMIT_BACKUP` | Giới hạn tỷ lệ cho việc tạo sao lưu, cho mỗi cây (v3.24.0+). Mặc định là `"10 mỗi ngày"`
`RATE_LIMIT_MEDIA_ARCHIVE` | Giới hạn tỷ lệ cho việc tạo các kho lưu trữ phương tiện trên trang Xuất. Mặc định là `"1 mỗi giờ"`
`REGISTRATION_DISABLED` | Nếu `True`, không cho phép đăng ký người dùng mới (mặc định `False`)
`DISABLE_TELEMETRY` | Nếu `True`, vô hiệu hóa telemetry thống kê (mặc định `False`). Xem [telemetry](telemetry.md) để biết chi tiết.
`PILLOW_MAX_IMAGE_PIXELS` | Thiết lập tham số PIL.Image.MAX_IMAGE_PIXELS, chỉ ra số pixel mà hình ảnh đã xử lý có thể chứa. Xem [docs](https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.MAX_IMAGE_PIXELS) để biết chi tiết.
`MAX_THUMBNAIL_FILE_BYTES` | Thiết lập kích thước tệp tối đa cứng cho hình thu nhỏ. Mặc định là `50 * 1024 * 1024` (50 MB). Tăng kích thước này có thể làm tăng đáng kể mức sử dụng bộ nhớ và có thể dẫn đến sự cố hết bộ nhớ hoặc mất dữ liệu nếu các tệp lớn được giải nén trong bộ nhớ.


!!! info
    Khi sử dụng biến môi trường cho cấu hình, các tùy chọn boolean như `EMAIL_USE_SSL` phải là chuỗi `true` hoặc `false` (phân biệt chữ hoa chữ thường!).


### Cài đặt cho cơ sở dữ liệu PostgreSQL

Các cài đặt này là bắt buộc nếu các cây gia đình của bạn được lưu trữ trong một [cơ sở dữ liệu PostgreSQL](postgres.md) sử dụng addon SharedPostgreSQL.

Khóa | Mô tả
----|-------------
`POSTGRES_USER` | Tên người dùng cho kết nối cơ sở dữ liệu
`POSTGRES_PASSWORD` | Mật khẩu cho người dùng cơ sở dữ liệu


### Cài đặt liên quan đến việc lưu trữ nhiều cây

Các cài đặt sau đây liên quan khi [lưu trữ nhiều cây](multi-tree.md).


Khóa | Mô tả
----|-------------
`MEDIA_PREFIX_TREE` | Boolean, có sử dụng một thư mục con riêng cho các tệp phương tiện của mỗi cây hay không. Mặc định là `False`, nhưng rất khuyến nghị sử dụng `True` trong một cài đặt nhiều cây
`NEW_DB_BACKEND` | Backend cơ sở dữ liệu để sử dụng cho các cây gia đình mới được tạo. Phải là một trong `sqlite` hoặc `sharedpostgresql`. Mặc định là `sqlite`. Giá trị `postgresql` vẫn được chấp nhận nhưng đã lỗi thời, vì backend PostgreSQL sẽ bị loại bỏ trong Gramps Web API 4.0.
`POSTGRES_HOST` | Tên máy chủ của máy chủ PostgreSQL được sử dụng để tạo các cây mới khi sử dụng cài đặt nhiều cây với backend SharedPostgreSQL
`POSTGRES_PORT` | Cổng của máy chủ PostgreSQL được sử dụng để tạo các cây mới khi sử dụng cài đặt nhiều cây với backend SharedPostgreSQL


### Cài đặt cho xác thực OIDC

Các cài đặt này cần thiết nếu bạn muốn sử dụng xác thực OpenID Connect (OIDC) với các nhà cung cấp bên ngoài. Để biết hướng dẫn thiết lập chi tiết và ví dụ, xem [Xác thực OIDC](oidc.md).

Khóa | Mô tả
----|-------------
`OIDC_ENABLED` | Boolean, có kích hoạt xác thực OIDC hay không. Mặc định là `False`.
`OIDC_ISSUER` | URL nhà cung cấp OIDC (đối với các nhà cung cấp OIDC tùy chỉnh)
`OIDC_CLIENT_ID` | ID khách hàng OAuth (đối với các nhà cung cấp OIDC tùy chỉnh)
`OIDC_CLIENT_SECRET` | Mật khẩu khách hàng OAuth (đối với các nhà cung cấp OIDC tùy chỉnh)
`OIDC_NAME` | Tên hiển thị tùy chỉnh cho nhà cung cấp. Mặc định là "OIDC"
`OIDC_SCOPES` | Các phạm vi OAuth. Mặc định là "openid email profile"
`OIDC_USERNAME_CLAIM` | Khẳng định để sử dụng cho tên người dùng. Mặc định là "preferred_username"
`OIDC_OPENID_CONFIG_URL` | Tùy chọn: URL đến điểm cuối cấu hình OpenID Connect (nếu không sử dụng tiêu chuẩn `/.well-known/openid-configuration`)
`OIDC_PKCE` | Boolean, có sử dụng PKCE hay không. Nếu không được thiết lập, PKCE sẽ được sử dụng khi tài liệu khám phá của nhà cung cấp liệt kê `S256`. Xem [PKCE](oidc.md#pkce)
`OIDC_DISABLE_LOCAL_AUTH` | Boolean, có vô hiệu hóa xác thực tên người dùng/mật khẩu cục bộ hay không. Mặc định là `False`
`OIDC_AUTO_REDIRECT` | Boolean, có tự động chuyển hướng đến OIDC khi chỉ có một nhà cung cấp được cấu hình hay không. Mặc định là `False`

#### Các nhà cung cấp OIDC tích hợp sẵn

Đối với các nhà cung cấp tích hợp sẵn (Google, Microsoft), sử dụng các cài đặt sau:

Khóa | Mô tả
----|-------------
`OIDC_GOOGLE_CLIENT_ID` | ID khách hàng cho Google OAuth
`OIDC_GOOGLE_CLIENT_SECRET` | Mật khẩu khách hàng cho Google OAuth
`OIDC_MICROSOFT_CLIENT_ID` | ID khách hàng cho Microsoft OAuth
`OIDC_MICROSOFT_CLIENT_SECRET` | Mật khẩu khách hàng cho Microsoft OAuth
`OIDC_GOOGLE_PKCE` | Boolean, cài đặt PKCE cho Google, xem [PKCE](oidc.md#pkce)
`OIDC_MICROSOFT_PKCE` | Boolean, cài đặt PKCE cho Microsoft, xem [PKCE](oidc.md#pkce)

#### Phân quyền OIDC

Các cài đặt này cho phép bạn ánh xạ các nhóm/nhóm OIDC từ nhà cung cấp danh tính của bạn đến các vai trò người dùng Gramps Web:

Khóa | Mô tả
----|-------------
`OIDC_ROLE_CLAIM` | Tên khẳng định trong mã thông báo OIDC chứa các nhóm/nhóm của người dùng. Mặc định là "groups"
`OIDC_GROUP_ADMIN` | Tên nhóm/nhóm từ nhà cung cấp OIDC của bạn ánh xạ đến vai trò "Quản trị viên" của Gramps
`OIDC_GROUP_OWNER` | Tên nhóm/nhóm từ nhà cung cấp OIDC của bạn ánh xạ đến vai trò "Chủ sở hữu" của Gramps
`OIDC_GROUP_EDITOR` | Tên nhóm/nhóm từ nhà cung cấp OIDC của bạn ánh xạ đến vai trò "Biên tập viên" của Gramps
`OIDC_GROUP_CONTRIBUTOR` | Tên nhóm/nhóm từ nhà cung cấp OIDC của bạn ánh xạ đến vai trò "Người đóng góp" của Gramps
`OIDC_GROUP_MEMBER` | Tên nhóm/nhóm từ nhà cung cấp OIDC của bạn ánh xạ đến vai trò "Thành viên" của Gramps
`OIDC_GROUP_GUEST` | Tên nhóm/nhóm từ nhà cung cấp OIDC của bạn ánh xạ đến vai trò "Khách" của Gramps

### Cài đặt chỉ dành cho các tính năng AI

Các cài đặt này cần thiết nếu bạn muốn sử dụng các tính năng được hỗ trợ bởi AI như trò chuyện hoặc tìm kiếm ngữ nghĩa. Xem [Thiết lập trò chuyện AI](chat.md) để biết chi tiết.

!!! warning "Tìm kiếm ngữ nghĩa đã lỗi thời"
    Tìm kiếm ngữ nghĩa, và với nó là các cài đặt `VECTOR_EMBEDDING_*`, đã lỗi thời và sẽ bị loại bỏ trong Gramps Web API 3.25. Sau đó, `VECTOR_EMBEDDING_MODEL` vẫn được chấp nhận nhưng sẽ bị bỏ qua. Kể từ Gramps Web API 3.24, trò chuyện AI chỉ cần `LLM_MODEL`.

Khóa | Mô tả
----|-------------
`LLM_BASE_URL` | URL gốc cho API trò chuyện tương thích với OpenAI. Mặc định là `None`, sử dụng API OpenAI.
`LLM_MODEL` | Mô hình để sử dụng cho API trò chuyện tương thích với OpenAI. Nếu không được thiết lập (mặc định), trò chuyện sẽ bị vô hiệu hóa. Từ v3.6.0, trợ lý AI sử dụng Pydantic AI với khả năng gọi công cụ.
`VECTOR_EMBEDDING_MODEL` | **Đã lỗi thời**, sẽ bị loại bỏ trong 3.25. Mô hình để sử dụng cho các nhúng vector tìm kiếm ngữ nghĩa. Khi sử dụng một mô hình cục bộ, điều này phải là tên mô hình [Sentence Transformers](https://sbert.net/). Khi sử dụng một API từ xa (xem `VECTOR_EMBEDDING_BASE_URL`), đây là tên mô hình được truyền cho nhà cung cấp từ xa. Nếu không được thiết lập (mặc định), tìm kiếm ngữ nghĩa sẽ bị vô hiệu hóa. Trước Gramps Web API 3.24, trò chuyện cũng bị vô hiệu hóa.
`VECTOR_EMBEDDING_BASE_URL` | **Đã lỗi thời**, sẽ bị loại bỏ trong 3.25. URL gốc cho một API nhúng tương thích với OpenAI từ xa (ví dụ: Ollama, OpenAI, LiteLLM). Nếu không được thiết lập (mặc định), một mô hình Sentence Transformers cục bộ được sử dụng. Xem [Sử dụng API nhúng từ xa](chat.md#using-a-remote-embedding-api) để biết chi tiết.
`VECTOR_EMBEDDING_API_KEY` | **Đã lỗi thời**, sẽ bị loại bỏ trong 3.25. Khóa API cho các nhà cung cấp nhúng từ xa đã xác thực. Chỉ cần thiết khi `VECTOR_EMBEDDING_BASE_URL` được thiết lập và nhà cung cấp yêu cầu xác thực.
`LLM_MAX_CONTEXT_LENGTH` | Giới hạn ký tự cho ngữ cảnh cây gia đình được cung cấp cho LLM. Mặc định là 50000.
`LLM_SYSTEM_PROMPT` | Lời nhắc hệ thống tùy chỉnh cho trợ lý trò chuyện LLM (v3.6.0+). Nếu không được thiết lập, sử dụng lời nhắc tối ưu hóa genealology mặc định.


## Ví dụ về tệp cấu hình

Một tệp cấu hình tối thiểu cho sản xuất có thể trông như thế này:
```python
TREE="My Family Tree"
BASE_URL="https://mytree.example.com"
SECRET_KEY="..."  # khóa bí mật của bạn
USER_DB_URI="sqlite:////path/to/users.sqlite"
EMAIL_HOST="mail.example.com"
EMAIL_PORT=465
EMAIL_USE_SSL=True  # Sử dụng SSL ẩn cho cổng 465
EMAIL_HOST_USER="gramps@example.com"
EMAIL_HOST_PASSWORD="..." # mật khẩu SMTP của bạn
DEFAULT_FROM_EMAIL="gramps@example.com"
