# Tìm kiếm

Trang tìm kiếm có thể truy cập bằng cách nhấp vào biểu tượng kính lúp ở thanh công cụ trên cùng, hoặc bằng cách nhấn phím `s` [phím tắt](shortcuts.md).

## Tìm kiếm toàn văn

Nhập bất kỳ truy vấn nào vào ô tìm kiếm và nhấn Enter (hoặc nhấp vào nút tìm kiếm). Gramps Web tìm kiếm trên tất cả các loại đối tượng – người, gia đình, sự kiện, địa điểm, nguồn, trích dẫn, kho lưu trữ, ghi chú và phương tiện – và trả về các kết quả phù hợp được xếp hạng theo mức độ liên quan.

Kết quả hiển thị loại đối tượng, tên và một tóm tắt ngắn. Nhấp vào bất kỳ kết quả nào để mở trang chi tiết tương ứng.

## Cú pháp tìm kiếm

- **Tất cả các từ phải khớp.** `Müller Berlin` tìm các đối tượng chứa cả hai từ.
- **`or`** tìm các đối tượng chứa một trong hai từ, ví dụ `Meyer or Maier`. `and` cũng có thể được gõ giữa các từ, nhưng không có sự khác biệt.
- `or` áp dụng cho các từ ngay bên cạnh nó: `Meyer or Maier Berlin` có nghĩa là "(Meyer hoặc Maier) và Berlin". Dấu ngoặc không được hỗ trợ.
- **Dấu ngoặc kép** khớp với một cụm từ, tức là các từ theo thứ tự này: `"Johann Georg"`.
- **Ký tự đại diện:** một dấu `*` ở cuối khớp với bất kỳ kết thúc nào, ví dụ `Mey*` khớp với "Meyer", "Meyers", "Meyerhofer", v.v. Điều này cũng hoạt động cho các cụm từ: `"Johann Georg"*`.
- `or` và `and` được nhận diện trong bất kỳ trường hợp nào. Để tìm kiếm một trong những từ này, hãy đặt nó trong dấu ngoặc kép.
- Các từ không thể bị loại trừ; không có "không".

## Những gì tìm kiếm tìm thấy

- Các dấu nhấn không cần phải khớp: "Müller" cũng tìm thấy "Muller", và "muller" tìm thấy "Müller".
- Gia đình và sự kiện cũng được tìm thấy qua tên của những người trong đó, ví dụ "Müller" tìm thấy gia đình và sự kiện của mọi người mang tên Müller. Những kết quả này được xếp hạng dưới các kết quả khớp trực tiếp.
- Các loại tiêu chuẩn được tìm thấy qua tên của chúng trong ngôn ngữ giao diện của bạn, ví dụ "Taufe" tìm thấy các lễ rửa tội trong giao diện tiếng Đức.
- Dấu gạch dưới phân tách các từ, vì vậy "microfilm" tìm thấy một tệp phương tiện có tên `scanned_microfilm.png`.
- Người dùng không thể xem các hồ sơ riêng tư sẽ không tìm thấy các đối tượng thông qua thông tin riêng tư, chẳng hạn như một gia đình thông qua tên của một thành viên riêng tư.

## Lọc theo loại đối tượng

Dưới ô tìm kiếm, các nút chuyển đổi cho mỗi loại đối tượng (Người, Gia đình, Sự kiện, Địa điểm, …) cho phép bạn thu hẹp kết quả về một hoặc nhiều loại cụ thể. Mặc định, tất cả các loại đều được tìm kiếm. Kích hoạt một hoặc nhiều nút chuyển đổi sẽ hạn chế kết quả chỉ cho các loại đó.
