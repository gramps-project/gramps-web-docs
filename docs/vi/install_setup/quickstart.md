Để thử nghiệm Gramps Web trên máy tính cục bộ của bạn (Linux, Mac hoặc Windows) mà không làm ảnh hưởng đến cài đặt Gramps Desktop của bạn, bạn có thể sử dụng Docker với lệnh sau:

```bash
docker run -p "5055:5000" -e TREE=new ghcr.io/gramps-project/grampsweb:latest
```

Điều này sẽ tạo ra một phiên bản Gramps Web mới, trống rỗng có thể truy cập tại [http://localhost:5055](http://localhost:5055), nơi bạn có thể tạo một người dùng quản trị và nhập một tệp XML Gramps.

!!! info
    Vì thiết lập đơn giản này không cho phép chạy các tác vụ dài trong một quy trình riêng biệt, việc nhập một tệp XML Gramps lớn có thể thất bại do thời gian chờ trong trợ lý lần đầu chạy.


Để sử dụng các tệp phương tiện từ máy tính của bạn, bạn có thể gắn thư mục phương tiện Gramps vào container với

```bash
docker run -p "5055:5000" -e TREE=new \
  -v /path/to/my/gramps_media_folder:/app/media \
  ghcr.io/gramps-project/grampsweb:latest
```

Lưu ý rằng điều này sẽ không lưu lại các thay đổi bạn thực hiện đối với cơ sở dữ liệu khi bạn khởi động lại container. Để thiết lập Gramps Web một cách chính xác, hãy tiếp tục đọc về [Triển khai](deployment.md).
