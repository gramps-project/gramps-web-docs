# Cài đặt phát triển frontend

Trang này mô tả các bước cần thiết để bắt đầu với phát triển frontend.

## Các yêu cầu trước

Cài đặt phát triển được khuyến nghị sử dụng Visual Studio Code với devcontainers. Cách tiếp cận này sẽ tạo ra một môi trường phát triển được cấu hình sẵn với tất cả các công cụ bạn cần.

Xem [Cài đặt phát triển backend](../backend/setup.md#prerequisites) để biết các yêu cầu cần thiết.

## Bắt đầu

1. Mở [kho mã nguồn frontend Gramps Web](https://github.com/gramps-project/gramps-web) và nhấp vào "fork"
2. Sao chép kho mã nguồn đã fork về máy tính của bạn bằng Git
3. Mở kho mã nguồn đã sao chép trong Visual Studio Code. Khi được nhắc, chọn "Reopen in Container" hoặc mở bảng lệnh (Ctrl+Shift+P hoặc Cmd+Shift+P) và chọn "Dev Containers: Rebuild and Reopen in Container".
4. Chờ cho dev container được xây dựng và khởi động. Điều này có thể mất vài phút, đặc biệt là lần đầu tiên.

## Chạy máy chủ phát triển frontend

Để chạy máy chủ phát triển frontend và xem trước tác động của các thay đổi của bạn trong trình duyệt, bạn có thể sử dụng các tác vụ được định nghĩa sẵn trong dev container.

Để điều này hoạt động, trước tiên bạn cần khởi động một phiên bản của [Gramps Web API backend](../backend/setup.md#tasks). Cách dễ nhất để làm điều này là sử dụng dev container backend và [chạy tác vụ "Serve Web API"](../backend/setup.md#tasks) trong một cửa sổ VS Code riêng biệt.

Khi backend đang chạy, bạn có thể chạy máy chủ phát triển frontend bằng cách chọn "Tasks: Run Task" từ bảng lệnh (Ctrl+Shift+P hoặc Cmd+Shift+P) và sau đó chọn "Serve Gramps Web frontend".

Điều này sẽ khởi động máy chủ phát triển frontend trên cổng 8001, mà bạn có thể truy cập trong trình duyệt của mình tại `http://localhost:8001`. Trình duyệt sẽ tự động tải lại khi bạn thực hiện các thay đổi đối với mã nguồn frontend, cho phép bạn thấy ngay tác động của các thay đổi của mình.
