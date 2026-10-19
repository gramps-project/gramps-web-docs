# Tìm kiếm

Trang tìm kiếm có thể truy cập bằng cách nhấp vào biểu tượng kính lúp ở thanh công cụ trên cùng, hoặc bằng cách nhấn phím `s` [phím tắt](shortcuts.md).

## Tìm kiếm toàn văn

Nhập bất kỳ truy vấn nào vào trường tìm kiếm và nhấn Enter (hoặc nhấp vào nút tìm kiếm). Gramps Web tìm kiếm trên tất cả các loại đối tượng – người, gia đình, sự kiện, địa điểm, nguồn, trích dẫn, kho lưu trữ, ghi chú và phương tiện – và trả về các kết quả phù hợp được xếp hạng theo mức độ liên quan.

Kết quả hiển thị loại đối tượng, tên và một tóm tắt ngắn. Nhấp vào bất kỳ kết quả nào để mở trang chi tiết tương ứng.

Một dấu `*` ở cuối có thể được sử dụng như một ký tự đại diện, ví dụ `Mey*` sẽ khớp với "Meyer", "Meyers", "Meyerhofer", v.v.

## Lọc theo loại đối tượng

Dưới trường tìm kiếm, các nút chuyển đổi cho từng loại đối tượng (Người, Gia đình, Sự kiện, Địa điểm, ...) cho phép bạn thu hẹp kết quả về một hoặc nhiều loại cụ thể. Theo mặc định, tất cả các loại đều được tìm kiếm. Kích hoạt một hoặc nhiều nút chuyển đổi sẽ hạn chế kết quả chỉ ở những loại đó.

## Tìm kiếm ngữ nghĩa

!!! warning "Đã ngừng sử dụng"
    Tìm kiếm ngữ nghĩa đã ngừng sử dụng và sẽ bị xóa trong Gramps Web API 3.25. Tìm kiếm toàn văn được mô tả ở trên không bị ảnh hưởng.

Nếu quản trị viên máy chủ đã bật [tìm kiếm ngữ nghĩa (sử dụng AI)](../install_setup/chat.md#semantic-search-deprecated), một nút chuyển đổi chế độ sẽ xuất hiện ở góc trên bên phải của trang tìm kiếm với hai tùy chọn:

- **Tìm kiếm** – tìm kiếm toàn văn tiêu chuẩn (mặc định)
- **Ngữ nghĩa** – tìm kiếm sử dụng AI hiểu nghĩa của truy vấn của bạn thay vì khớp với các từ chính xác

Tìm kiếm ngữ nghĩa hữu ích cho các truy vấn bằng ngôn ngữ tự nhiên như "nông dân ở Bavaria vào thế kỷ 19". Nó yêu cầu chỉ mục tìm kiếm ngữ nghĩa phải được cập nhật; xem [Cài đặt quản trị](../administration/settings.md) để biết cách xây dựng hoặc cập nhật chỉ mục.
