# Giới hạn việc sử dụng CPU và bộ nhớ

Trong cấu hình dựa trên docker được khuyến nghị, Gramps Web sử dụng [Gunicorn](https://gunicorn.org/) để phục vụ backend và [Celery](https://docs.celeryq.dev) cho các tác vụ nền. Trong cả hai trường hợp, nhiều tiến trình worker có thể chạy song song, điều này làm cho ứng dụng phản hồi tốt hơn từ góc độ người dùng. Tuy nhiên, việc tăng số lượng worker cũng làm tăng lượng RAM được sử dụng (ngay cả khi ứng dụng không hoạt động) và cho phép các yêu cầu được xử lý song song có thể dẫn đến việc sử dụng CPU cao (đặc biệt khi nhiều người dùng đang sử dụng ứng dụng cùng một lúc). Cả Gunicorn và Celery đều cho phép giới hạn số lượng worker song song.

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

Cách dễ nhất để đặt số lượng worker của Gunicorn khi sử dụng hình ảnh docker Gramps Web mặc định là thiết lập biến môi trường `GUNICORN_NUM_WORKERS`, ví dụ, bằng cách khai báo nó trong tệp `docker-compose.yml`, dưới phần "environment".

```yaml
services:
  grampsweb:
    environment:
      GUNICORN_NUM_WORKERS: 2
```

Xem [tài liệu của Gunicorn](https://docs.gunicorn.org/en/stable/design.html#how-many-workers) để quyết định
về số lượng worker lý tưởng.



## Giới hạn số lượng worker của Celery

Để đặt số lượng worker của Celery, điều chỉnh cài đặt `concurrency` trong tệp Docker compose:

```yaml
  grampsweb_celery:
    command: celery -A gramps_webapi.celery worker --loglevel=INFO --concurrency=2
```

Xem [tài liệu của Celery](https://docs.celeryq.dev/en/stable/userguide/workers.html#concurrency) để quyết định
về số lượng worker lý tưởng.

!!! info
    Nếu cờ `concurrency` bị bỏ qua (điều này đã xảy ra trong tài liệu Gramps Web cho đến v2.5.0), nó
    sẽ mặc định là số lõi CPU có sẵn trên hệ thống, điều này có thể tiêu tốn một lượng lớn bộ nhớ.
