# Sử dụng cơ sở dữ liệu PostgreSQL

Theo mặc định, Gramps sử dụng cơ sở dữ liệu SQLite dựa trên tệp để lưu trữ cây gia đình. Điều này hoạt động hoàn hảo cho Gramps Web và được khuyến nghị cho hầu hết người dùng. Tuy nhiên, bắt đầu từ phiên bản 0.3.0 của Gramps Web API, cũng hỗ trợ máy chủ PostgreSQL với một cây gia đình duy nhất trên mỗi cơ sở dữ liệu, được cung cấp bởi [Gramps PostgreSQL Addon](https://gramps-project.org/wiki/index.php/Addon:PostgreSQL). Kể từ [phiên bản 1.0.0](https://github.com/gramps-project/gramps-web-api/releases/tag/v1.0.0), cũng hỗ trợ Addon SharedPostgreSQL, cho phép lưu trữ nhiều cây gia đình trong một cơ sở dữ liệu duy nhất, điều này đặc biệt hữu ích khi sử dụng cùng với [hỗ trợ đa cây](multi-tree.md) của Gramps Web API.

## Thiết lập máy chủ PostgreSQL

Nếu bạn muốn thiết lập một cơ sở dữ liệu mới để sử dụng với PostgreSQLAddon, bạn có thể làm theo [hướng dẫn trong Gramps Wiki](https://gramps-project.org/wiki/index.php/Addon:PostgreSQL) để thiết lập máy chủ.

Ngoài ra, bạn cũng có thể sử dụng Docker Compose để chạy máy chủ PostgreSQL trong một container trên cùng một máy chủ docker với Gramps Web.

Việc sử dụng PostgreSQL được docker hóa với Gramps chỉ phức tạp bởi thực tế là các hình ảnh PostgreSQL mặc định không có bất kỳ ngôn ngữ địa phương nào được cài đặt, điều này tuy nhiên cần thiết cho Gramps để phân loại đối tượng theo ngôn ngữ địa phương. Tùy chọn dễ nhất là sử dụng hình ảnh `gramps-postgres` được phát hành trong [kho lưu trữ này](https://github.com/DavidMStraub/gramps-postgres-docker/). Để sử dụng nó, thêm phần sau vào tệp `docker-compose.yml` của bạn:
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
và cũng thêm `postgres_data:` như một khóa dưới phần `volumes:` của tệp YAML này. Hình ảnh này chứa một cơ sở dữ liệu riêng cho dữ liệu gia phả của Gramps và cho cơ sở dữ liệu người dùng Gramps; mỗi cái có thể có mật khẩu riêng biệt.

## Nhập một cây gia đình Gramps

Một lần nữa, nếu bạn đã thiết lập máy chủ PostgreSQL của riêng mình, bạn có thể làm theo [hướng dẫn trong Gramps Wiki](https://gramps-project.org/wiki/index.php/Addon:PostgreSQL) để nhập một cây gia đình vào cơ sở dữ liệu.

Ngoài ra, nếu bạn đã làm theo hướng dẫn Docker Compose ở trên, bạn có thể sử dụng lệnh sau để nhập một tệp XML Gramps nằm trên máy chủ docker của bạn:

```bash
docker compose run --entrypoint "" grampsweb \
    gramps -C postgres \
    -i /root/.gramps/grampsdb/my_tree.gramps \
    --config=database.path:/root/.gramps/grampsdb \
    --config=database.backend:postgresql \
    --config=database.host:postgres_gramps \
    --config=database.port:5432 \
    --username=gramps --password=postgres_password_gramps
```

## Cấu hình Web API để sử dụng với cơ sở dữ liệu

Để cấu hình Web API để sử dụng với cơ sở dữ liệu PostgreSQL, thêm phần sau dưới khóa `environment:` của dịch vụ `grampsweb` trong `docker-compose.yml`:

```yaml
      # addon PostgreSQL giả định rằng tên cây là
      # bằng với tên cơ sở dữ liệu và ở đây tên cơ sở dữ liệu
      # mặc định của hình ảnh PostgreSQL được sử dụng
      TREE: postgres
      # Thông tin xác thực phải đồng ý với những thông tin được sử dụng cho
      # container PostgreSQL
      POSTGRES_USER: gramps
      POSTGRES_PASSWORD: postgres_password_gramps
```

## Sử dụng cơ sở dữ liệu PostgreSQL chia sẻ trong cài đặt đa cây

Khi sử dụng [cài đặt đa cây](multi-tree.md), addon SharedPostgreSQL là một tùy chọn tiện lợi để lưu trữ tất cả các cây, bao gồm cả những cây mới được tạo qua API, trong một cơ sở dữ liệu PostgreSQL duy nhất mà không làm ảnh hưởng đến quyền riêng tư hoặc bảo mật.

Để đạt được điều này, thiết lập một container dựa trên hình ảnh `gramps-postgres` như đã mô tả ở trên và đơn giản chỉ cần đặt tùy chọn cấu hình `NEW_DB_BACKEND` thành `sharedpostgresql`, ví dụ thông qua biến môi trường `GRAMPSWEB_NEW_DB_BACKEND`.

## Sử dụng cơ sở dữ liệu PostgreSQL cho cơ sở dữ liệu người dùng

Không phụ thuộc vào backend cơ sở dữ liệu nào được sử dụng cho dữ liệu gia phả, cơ sở dữ liệu người dùng có thể được lưu trữ trong một cơ sở dữ liệu PostgreSQL bằng cách cung cấp một URL cơ sở dữ liệu thích hợp. Hình ảnh docker `gramps-postgres` đã đề cập ở trên chứa một cơ sở dữ liệu riêng `grampswebuser` có thể được sử dụng cho mục đích này. Trong trường hợp đó, giá trị thích hợp cho tùy chọn cấu hình `USER_DB_URI` sẽ là
```
postgresql://grampswebuser:postgres_password_gramps_user@postgres_gramps:5432/grampswebuser
```

## Sử dụng cơ sở dữ liệu PostgreSQL cho chỉ mục tìm kiếm

Kể từ phiên bản 2.4.0 của Gramps Web API, chỉ mục tìm kiếm được lưu trữ trong một cơ sở dữ liệu SQLite (mặc định) hoặc một cơ sở dữ liệu PostgreSQL. Cũng cho mục đích này, hình ảnh `gramps-postgres` có thể được sử dụng. Đối với chỉ mục tìm kiếm, chúng ta có thể sử dụng cơ sở dữ liệu `gramps` được cung cấp bởi hình ảnh, bất kể chúng ta có lưu trữ dữ liệu gia phả của mình trong PostgreSQL hay không (chỉ mục tìm kiếm và dữ liệu gia phả có thể đồng tồn tại trong cùng một cơ sở dữ liệu). Điều này có thể đạt được, trong ví dụ trên, bằng cách đặt tùy chọn cấu hình `SEARCH_INDEX_DB_URI` thành
```
postgresql://gramps:postgres_password_gramps@postgres_gramps:5432/gramps
```

## Vấn đề

Trong trường hợp có vấn đề, vui lòng theo dõi đầu ra nhật ký của Gramps Web và máy chủ PostgreSQL. Trong trường hợp docker, điều này được thực hiện bằng

```
docker compose logs grampsweb
docker compose logs postgres_grampsweb
```

Nếu bạn nghi ngờ có vấn đề với Gramps Web (hoặc tài liệu), vui lòng báo cáo một vấn đề [trên Github](https://github.com/gramps-project/gramps-web-api/issues).
