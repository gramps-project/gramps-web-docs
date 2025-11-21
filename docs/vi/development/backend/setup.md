# Cài đặt phát triển Backend

Trang này liệt kê các bước cần thiết để bắt đầu phát triển [Gramps Web API](https://github.com/gramps-project/gramps-web-api/), thành phần backend (máy chủ) của Gramps Web.


## Điều kiện tiên quyết

Cài đặt phát triển được khuyến nghị sử dụng Visual Studio Code với devcontainers. Cách tiếp cận này sẽ tạo ra một môi trường phát triển được cấu hình sẵn với tất cả các công cụ bạn cần. Để bắt đầu, bạn sẽ cần các thành phần sau:

- [Docker](https://docs.docker.com/get-docker/)
- [Visual Studio Code](https://code.visualstudio.com/) với [tiện ích mở rộng Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) đã được cài đặt
- [Git](https://git-scm.com)

Bạn có thể sử dụng Linux, macOS hoặc Windows làm hệ điều hành của mình.


## Bắt đầu

1. Mở [kho lưu trữ Gramps Web API](https://github.com/gramps-project/gramps-web-api) và nhấp vào "fork"
2. Sao chép kho lưu trữ đã fork về máy tính của bạn bằng Git
3. Mở kho lưu trữ đã sao chép trong Visual Studio Code. Khi được nhắc, chọn "Reopen in Container" hoặc mở bảng lệnh (Ctrl+Shift+P hoặc Cmd+Shift+P) và chọn "Dev Containers: Rebuild and Reopen in Container".
4. Chờ cho dev container được xây dựng và khởi động. Điều này có thể mất vài phút, đặc biệt là lần đầu tiên.


## Nhiệm vụ

Nếu bạn chỉ đang sửa đổi mã backend, bạn không nhất thiết phải khởi động một máy chủ web - các bài kiểm tra đơn vị sử dụng một khách hàng kiểm tra Flask cho phép mô phỏng các yêu cầu đến API mà không cần một máy chủ đang chạy.

Tuy nhiên, việc chạy một máy chủ là hữu ích nếu bạn

- muốn thử nghiệm các thay đổi của bạn với các yêu cầu HTTP thực (xem [truy vấn thủ công](queries.md)), 
- muốn xem trước tác động của các thay đổi trên toàn bộ ứng dụng Gramps Web, hoặc
- cũng muốn thực hiện các thay đổi đồng thời trên frontend (xem [cài đặt phát triển frontend](../frontend/setup.md)).

Việc chạy máy chủ được đơn giản hóa trong dev container bằng các nhiệm vụ được định nghĩa trước. Bạn có thể chạy các nhiệm vụ này từ bảng lệnh (Ctrl+Shift+P hoặc Cmd+Shift+P) bằng cách chọn "Tasks: Run Task" và sau đó chọn một trong các tùy chọn sau:
- "Serve Web API" - khởi động máy chủ phát triển Flask trên cổng 5555 với ghi nhật ký gỡ lỗi được bật
- "Start Celery worker" - khởi động một worker Celery để xử lý các tác vụ nền.


## Gỡ lỗi

Gỡ lỗi đôi khi có thể khó khăn, đặc biệt là khi cố gắng theo dõi hành vi phức tạp hoặc xác định các vấn đề tinh vi. Để làm điều này dễ dàng hơn, bạn có thể gỡ lỗi cả một phiên bản API đang chạy và các trường hợp kiểm tra riêng lẻ trực tiếp trong Visual Studio Code.

### Gỡ lỗi Gramps Web API

Để gỡ lỗi API đang chạy:

1. Mở Visual Studio Code và đi đến chế độ xem **Chạy và Gỡ lỗi**.  
2. Chọn cấu hình **"Web API"** từ menu thả xuống.  
3. Bắt đầu gỡ lỗi.  
4. Khi bạn gửi yêu cầu đến backend (có thể là thủ công hoặc thông qua GUI Gramps Web), quá trình thực thi sẽ tạm dừng tại bất kỳ điểm dừng nào bạn đã đặt trong mã.  
   Điều này cho phép bạn kiểm tra các biến, luồng điều khiển và các chi tiết thời gian thực khác.

### Gỡ lỗi Các Trường Hợp Kiểm Tra

Để gỡ lỗi một trường hợp kiểm tra cụ thể:

1. Mở tệp kiểm tra mà bạn muốn gỡ lỗi (ví dụ, `test_people.py`).  
2. Trong Visual Studio Code, mở chế độ xem **Chạy và Gỡ lỗi**.  
3. Chọn cấu hình **"Current Test File"**.  
4. Bắt đầu gỡ lỗi — quá trình thực thi sẽ dừng lại tại bất kỳ điểm dừng nào được đặt trong tệp kiểm tra đó.  

Cài đặt này cho phép bạn bước qua logic kiểm tra, kiểm tra giá trị biến và hiểu rõ hơn về các lỗi kiểm tra hoặc kết quả không mong muốn.
