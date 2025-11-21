# Kiến trúc

## Thành phần

Giao diện người dùng được xây dựng từ các thành phần web. Chúng được định nghĩa trong các tệp Javascript trong thư mục `src`.

Thông thường, mỗi tệp định nghĩa một thành phần, bắt đầu với
```javascript
class GrampsjsSomeElement extends LitElement
```
và kết thúc với
```javascript
customElements.define('grampsjs-some-element', GrampsjsSomeElement)`
```
để định nghĩa phần tử HTML mới `grampsjs-some-element` có thể được sử dụng ở nơi khác.

Điểm vào chính, được bao gồm trong `index.html`, là phần tử `gramps-js` được định nghĩa trong `GrampsJs.js`. Điều này chứa định nghĩa của tất cả các trang riêng lẻ (tương ứng đơn giản với các phần tử được hiển thị hoặc ẩn dựa trên đường dẫn/URL), menu và định tuyến.

Các thành phần trong thư mục `src/views` thường tương ứng với các thành phần trang đầy đủ lấy dữ liệu từ backend (ví dụ: chế độ xem danh sách người), trong khi các thành phần trong `src/components` thường là các khối xây dựng nhỏ hơn được sử dụng bên trong các chế độ xem mà nhận dữ liệu từ các thuộc tính được cung cấp bởi phần tử cha của chúng. Tuy nhiên, sự tách biệt này không phải là nghiêm ngặt.

## Luồng dữ liệu

Dữ liệu được trao đổi với Backend/API thông qua các phương thức `apiGet`, `apiPut` và `apiPost` trong `src/api.js`, tự động xử lý việc xác thực.

Dữ liệu được truyền từ các thành phần cha đến các thành phần con thông qua các thuộc tính (xem ví dụ như [tài liệu Lit](https://lit.dev/docs/components/properties/)).

Khi dữ liệu cần được truyền ngược từ một thành phần con đến một thành phần cha, các sự kiện tùy chỉnh được sử dụng có thể được kích hoạt bằng hàm `fireEvent` trong `src/api.js` và lắng nghe bằng cú pháp `@` của Lit [(tài liệu)](https://lit.dev/docs/components/events/).

## Xác thực

Mã thông báo làm mới và mã thông báo xác thực được lưu trữ trong bộ nhớ cục bộ của trình duyệt. Mỗi khi một cuộc gọi API được thực hiện và mã thông báo đã hết hạn, mã thông báo làm mới được lưu trữ sẽ được sử dụng để lấy mã thông báo truy cập mới và cuộc gọi API sẽ được lặp lại.

Phạm vi ủy quyền của người dùng, được lưu trữ trong các tuyên bố của mã thông báo truy cập, được lấy bằng hàm `getPermissions` và được sử dụng trong phần tử `GrampsJs` cấp cao nhất để thiết lập các thuộc tính boolean `canAdd`, `canEdit`, `canManageUsers`, được truyền xuống các phần tử con để thực hiện chức năng cụ thể cho ủy quyền.
