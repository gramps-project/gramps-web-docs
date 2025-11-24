# Cài đặt / Thiết lập Gramps Web

Phần này đề cập đến việc cài đặt và thiết lập Gramps Web, cũng như các tùy chọn khác để bắt đầu.

## Bắt đầu với Gramps Web

Gramps Web là một ứng dụng web chạy trên máy chủ và được truy cập qua trình duyệt web. Nó được thiết kế để có thể truy cập cho người dùng đã xác thực qua internet.

Nếu bạn muốn sử dụng Gramps Web cho dữ liệu nghiên cứu gia phả của mình, bạn phải chọn một trong các tùy chọn sau:

1. Tự lưu trữ trên phần cứng của riêng bạn
2. Tự lưu trữ trên đám mây
3. Đăng ký một phiên bản được lưu trữ

Trong khi tùy chọn đầu tiên mang lại cho bạn sự linh hoạt và kiểm soát tối đa, nó cũng có thể gặp khó khăn về mặt kỹ thuật.

!!! mẹo
    Một trong những nguyên tắc chính của Gramps Web là đặt người dùng vào vị trí kiểm soát dữ liệu của chính họ bất kỳ lúc nào, vì vậy việc di chuyển dữ liệu từ một phiên bản này sang phiên bản khác là đơn giản. Đừng lo lắng về việc bị khóa sau khi đã chọn một trong các tùy chọn!

## Tự lưu trữ trên phần cứng của riêng bạn

Cách tiện lợi nhất để tự lưu trữ Gramps Web là thông qua Docker Compose. Chúng tôi cũng cung cấp hình ảnh Docker cho kiến trúc ARM, vì vậy bạn có thể chạy Gramps Web trên Raspberry Pi trong tầng hầm của bạn.

Xem [Triển khai với Docker](deployment.md) để biết hướng dẫn thiết lập.

## Tự lưu trữ trên đám mây

Cài đặt Gramps Web có thể khó khăn hơn so với các ứng dụng web đơn giản khác và không tương thích với các nhà cung cấp "hosting chia sẻ" thông thường. Bạn có thể đăng ký một máy chủ ảo và cài đặt Gramps Web [thủ công](deployment.md).

Một tùy chọn đơn giản hơn là sử dụng hình ảnh đám mây đã được cài đặt sẵn. Một ví dụ là [ứng dụng 1-click của DigitalOcean](digital_ocean.md).

## Đăng ký một phiên bản được lưu trữ

Gramps Web được lưu trữ là cách dễ nhất để bắt đầu với Gramps Web, vì không cần cài đặt hoặc cấu hình.

Dưới đây là danh sách các nhà cung cấp hosting chuyên dụng cho Gramps Web (cộng đồng mã nguồn mở Gramps không chịu trách nhiệm về dịch vụ của họ):

- Grampshub ([www.grampshub.com](https://www.grampshub.com)), được cung cấp bởi một trong những người đóng góp chính của Gramps Web

Nếu bạn sử dụng tùy chọn lưu trữ cho Gramps Web, bạn có thể bỏ qua phần còn lại của phần này và chuyển ngay đến phần [Quản trị](../administration/admin.md).
