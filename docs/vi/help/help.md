---
hide:
  - navigation
---

Nếu bạn gặp vấn đề hoặc cần trợ giúp với Gramps Web, vui lòng chọn một trong các tùy chọn sau.

[Diễn đàn :material-forum:](https://gramps.discourse.group/c/gramps-web/){ .md-button }
[Vấn đề Backend :material-github:](https://github.com/gramps-project/gramps-web-api/issues){ .md-button }
[Vấn đề Frontend :material-github:](https://github.com/gramps-project/gramps-web/issues){ .md-button }

Xem bên dưới để có một số hướng dẫn về nơi bạn nên bắt đầu.

## Đặt câu hỏi

Diễn đàn Gramps Discourse chính thức có một [danh mục riêng cho Gramps Web](https://gramps.discourse.group/c/gramps-web/). Vui lòng sử dụng nó để đặt bất kỳ câu hỏi nào bạn có thể có về Gramps Web, chẳng hạn như

- Câu hỏi về cách sử dụng Gramps Web
- Câu hỏi về cấu hình Gramps Web
- Khắc phục sự cố khi triển khai Gramps Web
- Ý tưởng về cải tiến Gramps Web
- ...

## Báo cáo vấn đề

Nếu bạn gặp một vấn đề mà bạn tin rằng là một lỗi trong Gramps Web, vui lòng hỗ trợ nó qua Github.

Có hai kho Github riêng biệt cho mã được sử dụng trong Gramps Web, một cho giao diện người dùng (“frontend”) và một cho mã máy chủ (“backend”):

- [Vấn đề Frontend](https://github.com/gramps-project/gramps-web/issues)
- [Vấn đề Backend](https://github.com/gramps-project/gramps-web-api/issues)

Nếu bạn không chắc chắn nơi nào để nộp một vấn đề, đừng lo lắng và chỉ cần chọn một trong hai – các quản trị viên sẽ có thể chuyển vấn đề nếu cần thiết.

Trong mọi trường hợp, vui lòng luôn bao gồm thông tin sau trong báo cáo của bạn:

- Chi tiết về thiết lập của bạn (ví dụ: một tệp docker-compose với các giá trị nhạy cảm đã được che giấu, hoặc bạn đang sử dụng phiên bản lưu trữ, chẳng hạn như Grampshub, hoặc một hình ảnh đã được cấu hình sẵn, chẳng hạn như DigitalOcean)
- Thông tin phiên bản. Để lấy thông tin này, hãy đi đến tab "Thông tin hệ thống" trên trang Cài đặt trong Gramps Web và sao chép/dán các giá trị trong hộp, mà sẽ trông giống như thế này:

```
Gramps 5.1.6
Gramps Web API 1.5.1
Gramps.js 24.1.0
locale: en
multi-tree: false
task queue: true
```

## Đề xuất cải tiến

Đối với các ý tưởng và thảo luận chung về các cải tiến trong tương lai, hãy thoải mái mở một cuộc thảo luận trong [diễn đàn](https://gramps.discourse.group/c/gramps-web/). Bạn cũng có thể muốn kiểm tra các trang vấn đề (xem các liên kết ở trên) để xem liệu một tính năng cụ thể đã được lên kế hoạch hoặc đang được làm việc hay chưa.

Đối với các cải tiến cụ thể với phạm vi hạn chế, hãy thoải mái mở một vấn đề trực tiếp với yêu cầu tính năng trong kho Github frontend hoặc backend thích hợp.
