# Telemetry

Bắt đầu từ phiên bản 3.2.0 của Gramps Web API, Gramps Web mặc định gửi dữ liệu telemetry hoàn toàn ẩn danh mỗi 24 giờ đến một điểm cuối phân tích do nhóm Gramps Web kiểm soát. Trang này chứa thông tin về dữ liệu telemetry được thu thập, cách nó được sử dụng và cách tắt nó nếu bạn muốn.

## Dữ liệu nào được thu thập?

Dữ liệu telemetry là một payload JSON nhỏ có dạng như sau:

```json
{
  "server_uuid": "c04325bfa7ae4578bcf134ec8fc046a7",
  "tree_uuid": "abcdef1234567890abcdef1234567890abcdef1234567890abcdef1234567890",
  "timestamp": 1701234567,
}
```

Như bạn có thể kiểm tra [trong mã nguồn](https://github.com/gramps-project/gramps-web-api/blob/master/gramps_webapi/api/telemetry.py#L83-L87), các định danh máy chủ và cây là duy nhất cho máy chủ và cây, nhưng chúng không chứa bất kỳ thông tin cá nhân nào có thể nhận diện. `timestamp` là thời gian hiện tại dưới dạng timestamp Unix.

## Tại sao dữ liệu được thu thập?

Gửi một định danh duy nhất mỗi ngày cho phép nhóm Gramps Web theo dõi có bao nhiêu máy chủ duy nhất đang chạy Gramps Web, và có bao nhiêu cây duy nhất đang được sử dụng.

Điều này rất quan trọng để hiểu tác động lên các dịch vụ bên ngoài mà Gramps Web sử dụng, chẳng hạn như bản đồ.

## Dữ liệu được thu thập như thế nào?

Khi một yêu cầu được gửi đến máy chủ Gramps Web API của bạn, nó kiểm tra xem dữ liệu telemetry đã được gửi trong 24 giờ qua chưa (bằng cách kiểm tra một khóa trong bộ nhớ cache cục bộ). Nếu chưa, payload ở trên sẽ được gửi đến một điểm cuối ghi lại dữ liệu.

Điểm cuối ghi lại được lưu trữ trên Google Cloud Run và được triển khai trực tiếp từ một [kho mã nguồn mở](https://github.com/DavidMStraub/cloud-run-telemetry), vì vậy bạn có thể kiểm tra cách dữ liệu được xử lý.

## Dữ liệu sẽ được sử dụng như thế nào?

Trước hết, không có dữ liệu nào ngoài payload ẩn danh, có thể giả định được thu thập (chẳng hạn như địa chỉ IP của máy chủ), sẽ được nhóm Gramps Web sử dụng.

Các ID ẩn danh và timestamp được thu thập sẽ được tổng hợp để tạo ra các biểu đồ như:

- Số lượng cài đặt Gramps Web đang hoạt động theo thời gian
- Số lượng cây Gramps Web đang hoạt động theo thời gian

Các biểu đồ này sẽ được công bố trên trang tài liệu của Gramps Web.

## Cách tắt telemetry?

Vì dữ liệu thống kê là hữu ích cho nhóm Gramps Web và chúng tôi đã đảm bảo rằng không có dữ liệu cá nhân nào được gửi, **chúng tôi sẽ rất biết ơn nếu bạn không tắt telemetry!**

Tuy nhiên, Gramps Web cho phép người dùng hoàn toàn kiểm soát, vì vậy bạn có thể chọn tắt tính năng này nếu bạn muốn.

Để làm điều đó, chỉ cần đặt tùy chọn cấu hình `DISABLE_TELEMETRY` thành `True` (ví dụ: bằng cách đặt biến môi trường `GRAMPSWEB_DISABLE_TELEMETRY` thành `true` &ndash; xem [tài liệu cấu hình](configuration.md) để biết chi tiết).
