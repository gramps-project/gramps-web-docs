## Chuẩn bị cơ sở dữ liệu Gramps của bạn

Nếu bạn đang sử dụng Gramps Desktop, có hai bước để chuẩn bị cơ sở dữ liệu của bạn để đảm bảo mọi thứ sẽ hoạt động trơn tru trong các bước tiếp theo. Nếu bạn đang chuyển từ một chương trình gia phả khác, bạn có thể bỏ qua bước này.

1. Kiểm tra và sửa chữa cơ sở dữ liệu
    - Tùy chọn: tạo một bản sao lưu cơ sở dữ liệu bằng cách xuất sang Gramps XML
    - Chạy công cụ [Kiểm tra và sửa chữa cơ sở dữ liệu](https://gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Tools#Check_and_Repair_Database). Điều này sửa chữa một số sự không nhất quán nội bộ có thể dẫn đến vấn đề trong Gramps Web.
2. Chuyển đổi đường dẫn media sang tương đối
    - Sử dụng Trình quản lý Media Gramps để [chuyển đổi tất cả các đường dẫn media từ tuyệt đối sang tương đối](https://gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Tools#Convert_paths_from_relative_to_absolute). Lưu ý rằng ngay cả với các đường dẫn tương đối, bất kỳ tệp media nào bên ngoài thư mục media của Gramps sẽ không hoạt động đúng khi đồng bộ hóa với Gramps Web.

## Nhập dữ liệu gia phả

Để nhập một cây gia đình hiện có, hãy sử dụng trang "Nhập" và tải lên một tệp ở bất kỳ định dạng tệp nào được Gramps hỗ trợ &ndash; xem [Nhập từ một chương trình gia phả khác](https://www.gramps-project.org/wiki/index.php/Import_from_another_genealogy_program) trong Gramps Wiki.

Nếu bạn đã sử dụng Gramps Desktop, rất được khuyến nghị sử dụng định dạng Gramps XML (`.gramps`) để đảm bảo rằng các cây trực tuyến và ngoại tuyến của bạn sử dụng cùng một định danh và có thể được [đồng bộ hóa](sync.md).

## Tại sao không hỗ trợ gói Gramps XML?

Mặc dù Gramps XML (`.gramps`) là định dạng ưa thích để nhập dữ liệu, gói Gramps XML (`.gpkg`) không được Gramps Web hỗ trợ. Điều này là do các quy trình nhập và xuất cho các tệp media không phù hợp để sử dụng trên máy chủ web.

Để nhập các tệp media thuộc về tệp `.gramps` đã nhập, hãy xem phần tiếp theo.

## Nhập các tệp media

Nếu bạn đã tải lên một cây gia đình và cần tải lên các tệp media tương ứng, bạn có thể sử dụng nút "nhập kho media" trên trang "Nhập".

Nó mong đợi một tệp ZIP với các tệp media còn thiếu bên trong. Cấu trúc thư mục trong tệp ZIP không cần phải giống như cấu trúc thư mục bên trong thư mục media của Gramps vì các tệp được khớp với các đối tượng media bằng kiểm tra tổng hợp của chúng.

Lưu ý rằng tính năng này chỉ hoạt động cho các tệp có kiểm tra tổng hợp đúng trong cơ sở dữ liệu Gramps (điều này nên được đảm bảo bằng cách chạy công cụ kiểm tra và sửa chữa trong bước đầu tiên).

Khi chuyển sang Gramps Web từ một chương trình gia phả khác bao gồm các tệp media, được khuyến nghị trước tiên nhập mọi thứ vào Gramps Desktop, nơi có nhiều tùy chọn hơn để liên kết các tệp media hiện có với một cây đã nhập.
