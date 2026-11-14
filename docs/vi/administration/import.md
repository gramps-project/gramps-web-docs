# Nhập dữ liệu

Bạn có thể đưa một cây gia đình hiện có vào Gramps Web bằng cách tải lên một tệp được xuất từ một chương trình gia phả khác, từ một dịch vụ trực tuyến, hoặc từ Gramps Desktop.

Chức năng nhập dữ liệu nằm trong phần **Dữ liệu** của [cài đặt quản trị](settings.md) (biểu tượng người dùng trên thanh công cụ ứng dụng ▸ Quản trị), có sẵn cho các chủ sở hữu cây và quản trị viên. Khi cây vẫn còn trống, nút **Nhập cây gia đình** trên thẻ "Bắt đầu" của trang chính cũng dẫn đến đó.

## Tệp nào để sử dụng

| Đến từ | Xuất cây của bạn dưới dạng | Đuôi tệp |
|---|---|---|
| Một chương trình gia phả khác hoặc dịch vụ trực tuyến | GEDCOM | `.ged` |
| Gramps Desktop | Gramps XML | `.gramps` |
| GeneWeb | GeneWeb | `.gw` |
| Pro-Gen | Pro-Gen | `.def` |
| Một bảng tính | Gramps CSV | `.csv` |
| Một danh bạ | vCard | `.vcf` |

GEDCOM là định dạng trao đổi phổ biến mà hầu hết mọi chương trình gia phả và dịch vụ trực tuyến đều có thể xuất. Tìm tùy chọn "Xuất" hoặc "Tải xuống" trong chương trình của bạn hoặc trên trang web, và chọn GEDCOM nếu bạn được cung cấp nhiều định dạng. Trang Wiki của Gramps [Nhập từ một chương trình gia phả khác](https://www.gramps-project.org/wiki/index.php/Import_from_another_genealogy_program) có ghi chú về các chương trình cụ thể.

Nếu bạn sử dụng Gramps Desktop, hãy chọn Gramps XML (`.gramps`) thay vì GEDCOM. Nó mang tất cả dữ liệu Gramps mà không bị mất mát, và các cây trực tuyến và ngoại tuyến của bạn giữ nguyên các định danh giống nhau, vì vậy chúng có thể được [đồng bộ hóa](sync.md). Xem [Đến từ Gramps Desktop](#coming-from-gramps-desktop) bên dưới.

## Nhập tệp cây gia đình

1. Mở phần **Dữ liệu** của cài đặt quản trị.
2. Dưới "Nhập cây gia đình", chọn tệp của bạn và nhấp vào **Nhập**.
3. Tệp sẽ được phân tích trước, và một hộp thoại "Xác nhận Nhập" sẽ hiển thị số lượng đối tượng mà nó chứa (người, gia đình, sự kiện, địa điểm, v.v.). Chưa có gì được thêm vào cây của bạn. Kiểm tra xem các số liệu có hợp lý không, sau đó nhấp vào **Nhập** để tiếp tục, hoặc **Hủy** để hủy bỏ mà không thay đổi gì.
4. Quá trình nhập diễn ra trong nền và một chỉ báo tiến độ sẽ được hiển thị. Khi dữ liệu được nhập, chỉ mục tìm kiếm sẽ được cập nhật, điều này có thể mất một thời gian đối với một cây lớn. Nếu quá trình nhập thất bại, lý do sẽ được hiển thị.

Khi quá trình nhập hoàn tất, hãy kiểm tra kết quả: so sánh số lượng người trong bảng **Thống kê** trên trang chính với số lượng trong chương trình cũ của bạn, và mở một gia đình mà bạn biết rõ để xem rằng cha mẹ, con cái, ngày tháng và địa điểm đã được chuyển giao như mong đợi.

!!! warning
    Một lần nhập thông thường hoàn toàn là bổ sung: nó luôn tạo ra các đối tượng mới và không bao giờ cập nhật hoặc xóa các đối tượng hiện có, ngay cả đối với các đối tượng đã tồn tại trong cây của bạn dưới cùng một ID Gramps hoặc tay cầm. Nhập cùng một tệp hai lần – hoặc nhập một tệp chồng chéo với dữ liệu đã có trong cây – sẽ nhân đôi mọi đối tượng khớp thay vì hợp nhất hoặc bỏ qua nó.

    Nếu bạn cần đưa vào các thay đổi được thực hiện ở nơi khác cho một cây đã được nhập, hãy sử dụng [Khôi phục từ Sao lưu](backups.md#restore-from-backup) thay thế, điều này sẽ thay thế cây để phù hợp với tệp đã tải lên thay vì bổ sung vào nó. Điều này yêu cầu một tệp Gramps XML hoặc một bản sao lưu Gramps Web.

## Hạn mức sử dụng

Quản trị viên máy chủ có thể đặt giới hạn cho cây của bạn (xem [Cấu hình máy chủ](../install_setup/configuration.md)). Đỉnh của phần **Dữ liệu** hiển thị mức sử dụng hiện tại so với các giới hạn này:

- **Người** – số lượng đối tượng người trong cây so với giới hạn tối đa được cấu hình (∞ nếu không giới hạn)
- **Lưu trữ phương tiện** – kích thước tổng của các tệp phương tiện đã tải lên so với hạn mức lưu trữ được cấu hình (∞ nếu không giới hạn)

Một lần nhập sẽ bị từ chối hoàn toàn nếu nó vượt quá giới hạn về số lượng người.

## Tệp GEDCOM

Cả tệp GEDCOM 5.5.1 và GEDCOM 7 đều có thể được nhập. Có một vài điều cần lưu ý.

### Mã hóa ký tự

Một tệp GEDCOM 5.5.1 khai báo mã hóa ký tự của nó trong tiêu đề. Các mã hóa UTF-8, UTF-16, ANSEL và Windows (ANSI) được hỗ trợ. Nếu các tên có dấu hoặc các ký tự đặc biệt khác trông bị rối sau khi nhập (ví dụ `MÃ¼ller` thay vì `Müller`), tệp có thể đã được xuất với một mã hóa khác so với mã hóa mà nó khai báo. Xuất tệp lại từ chương trình cũ của bạn, chọn UTF-8 nếu có tùy chọn, và [bắt đầu lại](#starting-over).

Các tệp GEDCOM 7 phải luôn được mã hóa dưới dạng UTF-8; các tệp khác sẽ bị từ chối với lỗi "Tệp GEDCOM không hợp lệ".

### Dữ liệu cụ thể của chương trình

Nhiều chương trình thêm các phần mở rộng riêng của họ vào GEDCOM mà các chương trình khác không hiểu. Gramps không âm thầm bỏ qua các dữ liệu như vậy: các dòng mà nó không thể diễn giải sẽ được thu thập trong một ghi chú thuộc loại "Nhập GEDCOM", gắn liền với người, gia đình hoặc đối tượng khác mà chúng thuộc về. Xem xét các ghi chú này để xem có điều gì quan trọng không được chuyển giao.

### Tệp phương tiện

Một tệp GEDCOM chứa các tham chiếu đến các tệp phương tiện (chẳng hạn như ảnh hoặc tài liệu quét), nhưng không chứa các tệp đó. Sau khi nhập, các đối tượng phương tiện tồn tại trong cây của bạn, nhưng các tệp của chúng bị thiếu, điều này được hiển thị dưới [Tình trạng tệp phương tiện](import-media.md#media-file-status). Để thêm các tệp, hãy xem [Nhập tệp phương tiện](import-media.md).

## Đến từ Gramps Desktop

Nếu bạn đang sử dụng Gramps Desktop, có hai bước để chuẩn bị cơ sở dữ liệu của bạn để đảm bảo mọi thứ sẽ hoạt động trơn tru trong các bước tiếp theo.

1. Kiểm tra và sửa chữa cơ sở dữ liệu
    - Tùy chọn: tạo một bản sao lưu cơ sở dữ liệu bằng cách xuất sang Gramps XML
    - Chạy [Công cụ Kiểm tra và sửa chữa cơ sở dữ liệu](https://gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Tools#Check_and_Repair_Database). Điều này sửa chữa một số bất thường nội bộ có thể dẫn đến vấn đề trong Gramps Web.
2. Chuyển đổi đường dẫn phương tiện thành tương đối
    - Sử dụng Trình quản lý Phương tiện Gramps để [chuyển đổi tất cả các đường dẫn phương tiện từ tuyệt đối sang tương đối](https://gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Tools#Convert_paths_from_relative_to_absolute). Lưu ý rằng ngay cả với các đường dẫn tương đối, bất kỳ tệp phương tiện nào bên ngoài thư mục phương tiện Gramps của bạn sẽ không hoạt động đúng khi đồng bộ hóa với Gramps Web.

Sau đó, xuất cây của bạn sang Gramps XML (`.gramps`), nhập nó như đã mô tả ở trên, và [tải lên các tệp phương tiện của bạn](import-media.md). Để tiếp tục làm việc trên cùng một cây trên máy tính và trên web, hãy sử dụng [tiện ích mở rộng Đồng bộ hóa Gramps Web](sync.md).

### Tại sao không hỗ trợ gói Gramps XML?

Trong khi Gramps XML (`.gramps`) là định dạng ưa thích để nhập dữ liệu, gói Gramps XML (`.gpkg`) không được Gramps Web hỗ trợ. Điều này là do các quy trình nhập và xuất cho các tệp phương tiện không phù hợp để sử dụng trên một máy chủ web.

## Các vấn đề phổ biến

**"Định dạng không được hỗ trợ".** Chỉ các đuôi tệp được liệt kê [ở trên](#which-file-to-use) mới có thể được nhập. Nếu chương trình hoặc dịch vụ trực tuyến của bạn đã cung cấp cho bạn một tệp ZIP, hãy giải nén nó và tải lên tệp `.ged` bên trong.

**Mọi thứ xuất hiện hai lần.** Cùng một tệp đã được nhập hai lần. Vì các lần nhập không bao giờ hợp nhất, hãy [bắt đầu lại](#starting-over).

**Ký tự đặc biệt bị rối.** Xem [Mã hóa ký tự](#character-encoding).

**Ảnh bị thiếu.** Xem [Nhập tệp phương tiện](import-media.md).

### Bắt đầu lại

Nếu một lần nhập bị sai, hoặc bạn muốn sửa chữa điều gì đó trong chương trình cũ của mình và nhập lại, trước tiên hãy làm trống cây bằng cách sử dụng [Xóa tất cả đối tượng](#delete-all-objects), sau đó nhập tệp đã được sửa chữa. Lưu ý rằng điều này cũng sẽ xóa bất kỳ thay đổi nào bạn đã thực hiện trong Gramps Web kể từ lần nhập.

### Xóa tất cả đối tượng

!!! danger
    Việc xóa đối tượng là **không thể đảo ngược**. Hãy tạo một [bản sao lưu](backups.md) trước khi tiếp tục.

**Xóa tất cả đối tượng** nằm trong phần **Khu vực Nguy hiểm** của [cài đặt quản trị](settings.md). Nhấp vào **Xóa** sẽ mở ra một hộp thoại nơi bạn có thể chọn xóa:

- **Tất cả đối tượng** – hoàn toàn xóa sạch cây
- **Các loại đối tượng cụ thể** – ví dụ, chỉ sự kiện hoặc chỉ đối tượng phương tiện

Bạn sẽ được yêu cầu xác thực lại (đăng nhập lại) để xác nhận hành động. Việc xóa sẽ chạy như một tác vụ nền và một chỉ báo tiến độ sẽ được hiển thị.

!!! warning
    Việc xóa chỉ một tập hợp con của các loại đối tượng (thay vì tất cả đối tượng cùng một lúc) có thể mất rất nhiều thời gian đối với các cây lớn, vì máy chủ phải kiểm tra và cập nhật tất cả các mối quan hệ giữa các đối tượng.
