# Tùy chỉnh giao diện người dùng

Giao diện người dùng Gramps Web là một ứng dụng Javascript được triển khai dưới dạng một tập hợp các tệp HTML, CSS và Javascript tĩnh. Thông thường, không cần cấu hình đặc biệt cho giao diện người dùng. Tuy nhiên, một số hành vi có thể được thay đổi bằng cách thiết lập các tùy chọn phù hợp trong tệp `config.js` ở thư mục gốc của bản phân phối.

Tệp nên có cấu trúc sau:

```javascript
window.grampsjsConfig = {
    option: value
}
```

Các khóa tùy chọn sau đây tồn tại.

Key |Type | Mô tả 
----|-----|-----------
`hideDNALink` | boolean | Nếu đúng, ẩn liên kết DNA trên thanh điều hướng.
`hideRegisterLink` | boolean | Nếu đúng, ẩn liên kết đăng ký trên trang đăng nhập. Điều này nên được sử dụng cho các triển khai đa cây.
`loginRedirect` | string | URL để chuyển hướng đến khi chưa đăng nhập và điều hướng đến bất kỳ trang nào khác ngoài "đăng nhập" hoặc "đăng ký"
`mapBaseStyleLight` | string | URL kiểu MapLibre cho bản đồ cơ sở trong chủ đề sáng (mặc định: `https://tiles.openfreemap.org/styles/liberty`)
`mapBaseStyleDark` | string | URL kiểu MapLibre cho bản đồ cơ sở trong chủ đề tối (mặc định: `https://tiles.openfreemap.org/styles/dark`)
`mapOhmStyle` | string | URL kiểu MapLibre cho lớp phủ OpenHistoricalMap (mặc định: `https://www.openhistoricalmap.org/map-styles/main/main.json`)
