---
hide:
  - toc
---

# Hướng dẫn người dùng

Phần này tài liệu các tính năng có sẵn cho người dùng của Gramps Web.

!!! note "Không thấy tất cả các tính năng?"
    Gramps Web sử dụng hệ thống phân quyền dựa trên vai trò. Một số tính năng – chẳng hạn như chỉnh sửa dữ liệu, quản lý thẻ, hoặc xem hồ sơ riêng tư – chỉ có sẵn cho những người dùng có quyền truy cập đủ. Bạn có thể kiểm tra vai trò hiện tại của mình trong [Cài đặt người dùng](settings.md). Nếu bạn cần quyền truy cập nhiều hơn, hãy liên hệ với chủ cây của bạn hoặc quản trị viên. Xem [Hệ thống người dùng](../install_setup/users.md) để biết mô tả về tất cả các vai trò.

## Điều hướng giao diện

### Điều hướng chính

Thanh bên (hoặc menu hamburger trên di động) là cách chính để di chuyển giữa các phần:

- **Trang chủ** – bảng điều khiển (xem bên dưới)
- **Blog** – các câu chuyện về lịch sử gia đình được viết dưới dạng bài đăng blog
- **Cây gia đình** – biểu đồ cây tương tác
- **Dòng thời gian** – chế độ xem theo thời gian của các sự kiện trong cây (cần phiên bản API Gramps Web đủ gần đây)
- **Bản đồ** – chế độ xem địa lý của các địa điểm trong cây
- **DNA** – công cụ phân tích kết quả DNA
- **Danh sách** – duyệt tất cả các đối tượng của mỗi loại: Người, Gia đình, Sự kiện, Địa điểm, Nguồn, Trích dẫn, Kho lưu trữ, Ghi chú
- **Media** – duyệt tất cả các tệp phương tiện (hình ảnh, tài liệu, v.v.)
- **Trợ lý** – trợ lý trò chuyện AI (nếu được quản trị viên bật)
- **Lịch sử** – các đối tượng đã thay đổi gần đây
- **Đánh dấu** – các đánh dấu đã lưu của bạn
- **Nhiệm vụ** – các nhiệm vụ nghiên cứu
- **Báo cáo** – tạo báo cáo
- **Xuất** – xuất cây gia đình
- **Phiên bản** – lịch sử giao dịch đầy đủ (hiển thị cho các thành viên và cao hơn)
- **Thông báo** – thông báo trong quá khứ

!!! note
    Các thẻ không còn được quản lý từ thanh bên – quản lý thẻ đã chuyển sang [Cài đặt quản trị](../administration/settings.md#tags) (Chủ/Quản trị viên chỉ). Xem [Thẻ](tags.md) để biết cách sử dụng thẻ.

### Thanh ứng dụng trên cùng

Thanh ở đầu mỗi trang chứa:

- **Thêm** (biểu tượng cộng, hiển thị cho những người đóng góp và cao hơn) – mở menu để tạo một đối tượng mới: Người, Gia đình, Sự kiện, Địa điểm, Nguồn, Trích dẫn, Kho lưu trữ, Ghi chú, Đối tượng phương tiện, hoặc Nhiệm vụ
- **Tìm kiếm** (kính lúp) – mở trang tìm kiếm
- **Biểu tượng người dùng** – mở menu cài đặt: Cài đặt người dùng, Quản trị (chỉ dành cho chủ), Quản lý người dùng (chỉ dành cho chủ), Thông tin hệ thống

## Trang chủ (bảng điều khiển)

Bảng điều khiển được hiển thị khi bạn lần đầu đăng nhập. Nó có hai cột:

**Cột bên trái:**

- **Thẻ người nhà** – hiển thị tên, ảnh (nếu có) và các thông tin chính của người nhà mà bạn đã chọn, với liên kết đến hồ sơ đầy đủ của họ và điều hướng nhanh đến cây gia đình. Nhấn nút **Đặt người nhà** trên thẻ để tìm kiếm và chọn một người khác.
- **Ngày kỷ niệm** – các sinh nhật và kỷ niệm sắp tới từ cây, dựa trên ngày hôm nay.
- **Đã thay đổi gần đây** – danh sách ngắn các đối tượng đã được sửa đổi gần đây, hữu ích cho việc theo dõi các chỉnh sửa hợp tác.

**Cột bên phải:**

- **Bài đăng blog gần đây** – các mục mới nhất từ [blog](blog.md), nếu có.
- **Thống kê** – tóm tắt số lượng đối tượng trong cây (số người, gia đình, sự kiện, v.v.).

Nếu quản trị viên cây đã cấu hình một **ghi chú trang chủ** và/hoặc một **hình ảnh trang chủ**, chúng sẽ được hiển thị nổi bật ở trên cùng các cột chính. Hình ảnh xuất hiện bên cạnh văn bản ghi chú khi cả hai đều được thiết lập. Xem [Cài đặt quản trị](../administration/settings.md#customization) để biết cách cấu hình những điều này.

!!! tip
    Nếu cây trống và bạn có quyền chỉnh sửa, bảng điều khiển sẽ hiển thị một thông báo "Bắt đầu" với các nút để thêm người đầu tiên của bạn hoặc nhập tệp cây gia đình.
