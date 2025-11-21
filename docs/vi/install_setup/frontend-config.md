# Tùy chỉnh giao diện frontend

Giao diện frontend của Gramps Web là một ứng dụng Javascript được triển khai dưới dạng một tập hợp các tệp HTML, CSS và Javascript tĩnh. Thông thường, không cần cấu hình đặc biệt cho giao diện frontend. Tuy nhiên, một số hành vi có thể được thay đổi bằng cách thiết lập các tùy chọn thích hợp trong tệp `config.js` tại thư mục gốc của bản phân phối.

Tệp này nên có cấu trúc như sau:

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
`leafletTileUrl` | string | URL ô tùy chỉnh cho bản đồ Leaflet
`leafletTileSize` | number | Kích thước ô tùy chỉnh cho bản đồ Leaflet
`leafletZoomOffset` | number | Độ lệch thu phóng tùy chỉnh cho bản đồ Leaflet
`leafletTileAttribution` | string | Ghi nhận tùy chỉnh cho bản đồ Leaflet
