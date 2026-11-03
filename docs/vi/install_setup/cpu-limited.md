# Giới hạn mức sử dụng CPU và bộ nhớ

Trong cấu hình dựa trên Docker được khuyến nghị, Gramps Web sử dụng [Gunicorn](https://gunicorn.org/) để phục vụ
backend và [Celery](https://docs.celeryq.dev) cho các tác vụ nền. Trong cả hai trường hợp, có thể chạy nhiều tiến trình worker song song, điều này làm cho ứng dụng phản hồi nhanh hơn từ góc độ người dùng. Tuy nhiên, việc tăng số lượng worker cũng làm tăng lượng RAM được sử dụng (ngay cả khi ứng dụng không hoạt động) và cho phép các yêu cầu được xử lý song song có thể dẫn đến mức sử dụng CPU cao (đặc biệt khi nhiều người dùng đang sử dụng ứng dụng cùng một lúc). Cả Gunicorn và Celery đều cho phép giới hạn số lượng worker song song.

## Lấy thông tin về hệ thống của bạn

Trên Linux, bạn có thể kiểm tra số lõi có sẵn trên hệ thống của mình bằng lệnh sau:

```bash
lscpu | grep CPU
```

Để xem bạn có bao nhiêu bộ nhớ và không gian swap có sẵn, hãy sử dụng

```bash
free -h
```

## Giới hạn số lượng worker của Gunicorn

Cách dễ nhất để thiết lập số lượng worker của Gunicorn khi sử dụng hình ảnh Docker mặc định của Gramps Web là thiết lập biến môi trường `GUNICORN_NUM_WORKERS`, ví dụ bằng cách khai báo nó trong tệp `docker-compose.yml`,
dưới phần "environment".

```yaml
services:
  grampsweb:
    environment:
      GUNICORN_NUM_WORKERS: 2
```

Xem [tài liệu của Gunicorn](https://docs.gunicorn.org/en/stable/design.html#how-many-workers) để quyết định
về số lượng worker lý tưởng.

!!! info
    Hình ảnh Docker khởi động Gunicorn với tùy chọn `--preload`, vì vậy các worker chia sẻ bộ nhớ của ứng dụng đã được tải và mỗi worker bổ sung cần ít bộ nhớ hơn. Nếu bạn ghi đè lệnh Gunicorn, hãy giữ `--preload` để hưởng lợi từ điều này.

## Giới hạn số lượng worker của Celery

Để thiết lập số lượng worker của Celery, hãy điều chỉnh cài đặt `concurrency` trong tệp Docker compose:

```yaml
  grampsweb_celery:
    command: celery -A gramps_webapi.celery worker --loglevel=INFO --concurrency=2
```

Xem [tài liệu của Celery](https://docs.celeryq.dev/en/stable/userguide/workers.html#concurrency) để quyết định
về số lượng worker lý tưởng.

!!! info
    Nếu cờ `concurrency` bị bỏ qua (điều này đã xảy ra trong tài liệu Gramps Web cho đến v2.5.0), nó
    sẽ mặc định là số lõi CPU có sẵn trên hệ thống, điều này có thể tiêu tốn một lượng bộ nhớ đáng kể.
