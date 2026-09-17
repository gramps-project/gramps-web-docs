# Sử dụng cơ sở dữ liệu PostgreSQL

Theo mặc định, Gramps Web lưu trữ mỗi cây gia đình trong tệp cơ sở dữ liệu SQLite riêng. Điều này không cần dịch vụ bổ sung, sao lưu đơn giản như việc sao chép tệp, và hoạt động tốt cho hầu hết các cài đặt, bao gồm cả những cài đặt [hosting nhiều cây](multi-tree.md).

Ngoài ra, các cây gia đình có thể được lưu trữ trên máy chủ PostgreSQL bằng cách sử dụng addon SharedPostgreSQL, giữ tất cả các cây trong một cơ sở dữ liệu duy nhất. Điều này có thể hợp lý nếu bạn đã chạy một máy chủ PostgreSQL và muốn quản lý sao lưu và giám sát ở đó, hoặc nếu bạn mong đợi nhiều người dùng chỉnh sửa cùng một lúc. PostgreSQL cũng có thể lưu trữ [cơ sở dữ liệu người dùng](#using-a-postgresql-database-for-the-user-database) và [chỉ mục tìm kiếm](#using-a-postgresql-database-for-the-search-index), độc lập với nơi lưu trữ các cây gia đình.

!!! warning "Addon PostgreSQL đã lỗi thời"
    Addon PostgreSQL cũ hơn, lưu trữ một cây gia đình duy nhất trên mỗi cơ sở dữ liệu, đã lỗi thời và sẽ không còn được hỗ trợ trong phiên bản tương lai của Gramps Web API. Nếu bạn đang sử dụng nó, hãy xem [Chuyển một cây từ addon PostgreSQL sang SharedPostgreSQL](#moving-a-tree-from-the-postgresql-addon-to-sharedpostgresql).

## Thiết lập máy chủ PostgreSQL

Tùy chọn dễ nhất là chạy máy chủ PostgreSQL trong một container trên cùng một máy chủ Docker với Gramps Web, sử dụng Docker Compose.

Gramps cần các ngôn ngữ địa phương được cài đặt trên máy chủ PostgreSQL để sắp xếp các đối tượng đúng cách trong các ngôn ngữ khác nhau, và các hình ảnh PostgreSQL mặc định không bao gồm bất kỳ ngôn ngữ nào. Hình ảnh [`gramps-postgres`](https://github.com/DavidMStraub/gramps-postgres-docker/) thêm chúng vào. Để sử dụng nó, hãy thêm phần sau vào tệp `docker-compose.yml` của bạn:
```yaml
  postgres_gramps:
    image: ghcr.io/davidmstraub/gramps-postgres:latest
    restart: unless-stopped
    environment:
      POSTGRES_PASSWORD: postgres_password_admin
      POSTGRES_PASSWORD_GRAMPS: postgres_password_gramps
      POSTGRES_PASSWORD_GRAMPS_USER: postgres_password_gramps_user
    volumes:
      - postgres_data:/var/lib/postgresql/data
```
và cũng thêm `postgres_data:` như một khóa dưới phần `volumes:` của tệp YAML này. Hình ảnh chứa hai cơ sở dữ liệu, mỗi cơ sở dữ liệu có người dùng và mật khẩu riêng: `gramps` cho dữ liệu gia phả và `grampswebuser` cho cơ sở dữ liệu người dùng Gramps Web.

Nếu bạn sử dụng máy chủ PostgreSQL của riêng mình, hãy tạo một cơ sở dữ liệu có tên `gramps` mà người dùng đã cấu hình có thể tạo bảng trong đó, và đảm bảo rằng các ngôn ngữ địa phương mà người dùng của bạn cần đã được cài đặt.

## Cấu hình Gramps Web

Các cây gia đình mới được tạo trong cơ sở dữ liệu SharedPostgreSQL khi Gramps Web chạy ở chế độ [multi-tree](multi-tree.md) và tùy chọn cấu hình `NEW_DB_BACKEND` được đặt thành `sharedpostgresql`. Với thiết lập Docker Compose ở trên, hãy thêm các mục sau dưới khóa `environment:` của dịch vụ `grampsweb` trong `docker-compose.yml`:

```yaml
      # kích hoạt chế độ multi-tree
      GRAMPSWEB_TREE: "*"
      GRAMPSWEB_MEDIA_PREFIX_TREE: true
      # tạo cây mới trong cơ sở dữ liệu SharedPostgreSQL
      GRAMPSWEB_NEW_DB_BACKEND: sharedpostgresql
      # Máy chủ và cổng của máy chủ PostgreSQL. 
      # máy chủ là tên của dịch vụ PostgreSQL ở trên
      GRAMPSWEB_POSTGRES_HOST: postgres_gramps
      GRAMPSWEB_POSTGRES_PORT: 5432
      # Thông tin xác thực phải khớp với những cái được sử dụng cho
      # container PostgreSQL
      GRAMPSWEB_POSTGRES_USER: gramps
      GRAMPSWEB_POSTGRES_PASSWORD: postgres_password_gramps
```

Xem [Cấu hình](configuration.md) để biết mô tả về tất cả các tùy chọn này. Lưu ý rằng máy chủ và cổng được lưu cùng với mỗi cây khi nó được tạo, vì vậy việc thay đổi chúng sau đó chỉ ảnh hưởng đến các cây mới.

## Tạo một cây và nhập dữ liệu

Để tạo một cây mới, gửi yêu cầu POST đến điểm cuối `/trees/` như đã mô tả trong [Thiết lập để lưu trữ nhiều cây](multi-tree.md#create-a-new-tree). Phản hồi chứa ID của cây mới, mà bạn cần để [tạo tài khoản chủ cây](../administration/owner.md#multi-tree-setup-create-tree-owner-account).

Khi chủ cây đã đăng nhập, họ có thể [nhập](../administration/import.md) một cây gia đình hiện có, ví dụ: một tệp XML Gramps được xuất từ Gramps Desktop, qua giao diện web.

## Sử dụng cơ sở dữ liệu PostgreSQL cho cơ sở dữ liệu người dùng

Cơ sở dữ liệu người dùng thường là một tệp SQLite, bất kể nơi lưu trữ các cây gia đình. Để sử dụng PostgreSQL thay thế, hãy đặt tùy chọn cấu hình `USER_DB_URI` thành URL cơ sở dữ liệu PostgreSQL. Với hình ảnh `gramps-postgres` ở trên, hãy sử dụng cơ sở dữ liệu `grampswebuser` của nó:
```
postgresql://grampswebuser:postgres_password_gramps_user@postgres_gramps:5432/grampswebuser
```

## Sử dụng cơ sở dữ liệu PostgreSQL cho chỉ mục tìm kiếm

Chỉ mục tìm kiếm cũng được lưu trữ trong SQLite theo mặc định. Để sử dụng PostgreSQL thay thế, hãy đặt tùy chọn cấu hình `SEARCH_INDEX_DB_URI` thành URL cơ sở dữ liệu PostgreSQL. Với hình ảnh `gramps-postgres` ở trên, bạn có thể sử dụng cơ sở dữ liệu `gramps` của nó, bất kể các cây gia đình của bạn có được lưu trữ ở đó hay không:
```
postgresql://gramps:postgres_password_gramps@postgres_gramps:5432/gramps
```

## Chuyển một cây từ addon PostgreSQL sang SharedPostgreSQL

Các cài đặt cũ hơn có thể lưu trữ cây gia đình của họ bằng addon PostgreSQL, lưu trữ một cây duy nhất trên mỗi cơ sở dữ liệu và đã lỗi thời. Để tìm hiểu addon nào mà một cây đang sử dụng, hãy xem tệp `database.txt` trong thư mục con của cây trong thư mục cơ sở dữ liệu Gramps: nó chứa `postgresql` cho addon PostgreSQL đã lỗi thời và `sharedpostgresql` cho SharedPostgreSQL.

Để chuyển một cây từ addon PostgreSQL sang SharedPostgreSQL trong cùng một cài đặt, giữ lại tài khoản người dùng và tệp phương tiện của bạn:

1. [Sao lưu cây gia đình của bạn](../administration/export.md#back-up-your-family-tree) dưới dạng tệp XML Gramps (`.gramps`), sử dụng một tài khoản có thể xem các hồ sơ riêng tư.
2. Thay đổi cấu hình của bạn như đã mô tả trong [Cấu hình Gramps Web](#configuring-gramps-web). Bạn có thể tiếp tục sử dụng container `gramps-postgres` hiện tại của mình.
3. [Tạo một cây mới](multi-tree.md#create-a-new-tree) và ghi nhớ ID cây của nó.
4. Gán các tài khoản người dùng hiện có của bạn cho cây mới, như đã mô tả trong [Di chuyển cơ sở dữ liệu người dùng hiện có](multi-tree.md#migrate-existing-user-database).
5. Di chuyển các tệp phương tiện của bạn đến vị trí mong đợi cho cây mới, như đã mô tả trong [Di chuyển các tệp phương tiện hiện có](multi-tree.md#migrate-existing-media-files).
6. Đăng nhập và [nhập](../administration/import.md) tệp XML Gramps vào cây mới.

Giữ tệp XML Gramps cho đến khi bạn đã kiểm tra rằng cây mới hoàn chỉnh.

Nếu bạn đang chuyển đến một cài đặt Gramps Web riêng biệt, hãy làm theo các bước trong [Chuyển đến một phiên bản Gramps Web khác](../administration/export.md#move-to-a-different-gramps-web-instance).

## Vấn đề

Trong trường hợp có vấn đề, vui lòng theo dõi đầu ra nhật ký của Gramps Web và máy chủ PostgreSQL. Trong trường hợp docker, điều này được thực hiện bằng

```
docker compose logs grampsweb
docker compose logs postgres_gramps
```

Nếu bạn nghi ngờ có vấn đề với Gramps Web (hoặc tài liệu), vui lòng báo cáo một vấn đề [trên Github](https://github.com/gramps-project/gramps-web-api/issues).
