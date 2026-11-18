# Nhập dữ liệu

Bạn có thể đưa một cây gia đình hiện có vào Gramps Web bằng cách tải lên một tệp được xuất từ một chương trình gia phả khác, từ một dịch vụ trực tuyến, hoặc từ Gramps Desktop.

Việc nhập dữ liệu có trang riêng, có sẵn cho chủ sở hữu cây và quản trị viên. Mở nó bằng **Nhập Cây Gia Đình** trong phần **Dữ liệu** của [cài đặt Quản trị](settings.md) (biểu tượng người dùng ở thanh ứng dụng trên cùng ▸ Quản trị). Khi cây vẫn còn trống, nút **Nhập Cây Gia Đình** của thẻ "Bắt đầu" trên trang chính, trong cây gia đình, và trong danh sách cũng dẫn đến đó.

## Tệp nào để sử dụng

| Nguồn gốc | Xuất cây của bạn dưới dạng | Đuôi tệp |
|---|---|---|
| Một chương trình gia phả khác hoặc dịch vụ trực tuyến | GEDCOM | `.ged` |
| Gramps Desktop | Gramps XML | `.gramps` |
| GeneWeb | GeneWeb | `.gw` |
| Pro-Gen | Pro-Gen | `.def` |
| Một bảng tính | Gramps CSV | `.csv` |
| Một danh bạ | vCard | `.vcf` |

GEDCOM là định dạng trao đổi chung mà hầu hết mọi chương trình gia phả và dịch vụ trực tuyến có thể xuất. Tìm tùy chọn "Xuất" hoặc "Tải xuống" trong chương trình của bạn hoặc trên trang web, và chọn GEDCOM nếu bạn được cung cấp nhiều định dạng. Trang Wiki của Gramps [Nhập từ một chương trình gia phả khác](https://www.gramps-project.org/wiki/index.php/Import_from_another_genealogy_program) có ghi chú về các chương trình cụ thể.

Nếu bạn sử dụng Gramps Desktop, hãy chọn Gramps XML (`.gramps`) thay vì GEDCOM. Nó mang tất cả dữ liệu Gramps mà không bị mất mát, và cây trực tuyến và ngoại tuyến của bạn giữ nguyên các định danh giống nhau, vì vậy chúng có thể được [đồng bộ hóa](sync.md). Xem [Đến từ Gramps Desktop](#coming-from-gramps-desktop) bên dưới.

## Nhập tệp cây gia đình

1. Mở trang Nhập như đã mô tả ở trên.
2. Dưới "Nhập Cây Gia Đình", chọn tệp của bạn và nhấp **Nhập**. Tiến trình tải lên được hiển thị.
3. Tệp được đọc trước tiên, và một hộp thoại "Xác nhận Nhập" hiển thị số lượng đối tượng mà nó chứa (người, gia đình, sự kiện, địa điểm, v.v.), và báo cáo của người nhập [báo cáo](#the-import-report) nếu có. Chưa có gì được thêm vào cây của bạn. Kiểm tra xem các số liệu có hợp lý không, sau đó nhấp **Nhập** để tiếp tục, hoặc **Hủy** để bỏ qua mà không thay đổi gì. Nếu cây của bạn đã chứa người, hộp thoại cảnh báo rằng việc nhập dữ liệu giống nhau một lần nữa sẽ tạo ra các bản sao.
4. Việc nhập diễn ra trong nền và một chỉ báo tiến trình được hiển thị. Khi dữ liệu được nhập, chỉ mục tìm kiếm được cập nhật, điều này có thể mất một thời gian cho một cây lớn. Nếu việc nhập thất bại, lý do sẽ được hiển thị.
5. Nếu cây chưa có người chính, bạn sẽ được mời chọn một.

Khi việc nhập hoàn tất, hãy kiểm tra kết quả: so sánh số lượng người trong bảng **Thống kê** trên trang chính với số lượng trong chương trình cũ của bạn, và mở một gia đình mà bạn biết rõ để xem rằng cha mẹ, con cái, ngày tháng, và địa điểm đã được chuyển giao như mong đợi. Nếu tệp tham chiếu đến ảnh hoặc tệp phương tiện khác, hãy thêm chúng tiếp theo, dưới [Nhập Tệp Phương Tiện](import-media.md) trên cùng một trang.

!!! warning
    Một lần nhập thông thường là hoàn toàn bổ sung: nó luôn tạo ra các đối tượng mới và không bao giờ cập nhật hoặc xóa các đối tượng hiện có, ngay cả đối với các đối tượng đã tồn tại trong cây của bạn dưới cùng một ID Gramps hoặc tay cầm. Nhập cùng một tệp hai lần – hoặc nhập một tệp chồng chéo với dữ liệu đã có trong cây – sẽ tạo ra mỗi đối tượng khớp thay vì hợp nhất hoặc bỏ qua nó.

    Nếu bạn cần đưa vào các thay đổi đã thực hiện ở nơi khác vào một cây đã được nhập, hãy sử dụng [Khôi phục từ Sao lưu](backups.md#restore-from-backup) thay vào đó, điều này thay thế cây để phù hợp với tệp đã tải lên thay vì thêm vào nó. Điều này yêu cầu một tệp Gramps XML hoặc một bản sao lưu Gramps Web.

## Báo cáo nhập

Người nhập báo cáo những gì họ không thể nhập hoàn toàn, ví dụ như các dòng GEDCOM mà họ không hiểu, các tham chiếu đến các bản ghi thiếu trong tệp, hoặc định dạng tệp lỗi thời. Báo cáo được hiển thị dưới **Báo cáo**, cả trong hộp thoại xác nhận và sau khi nhập. Đọc nó trước khi xác nhận: nó thường giải thích các vấn đề mà bạn sẽ chỉ nhận thấy sau này trong cây.

Không phải mọi thông điệp đều là vấn đề – nhiều tệp GEDCOM chứa dữ liệu cụ thể cho chương trình mà được báo cáo nhưng vẫn được giữ lại, xem [Dữ liệu cụ thể cho chương trình](#program-specific-data). Sử dụng các nút bên cạnh báo cáo để sao chép nó hoặc tải xuống dưới dạng tệp văn bản, ví dụ để yêu cầu trợ giúp trong [diễn đàn](../help/help.md).

## Hạn mức sử dụng

Quản trị viên máy chủ có thể đặt giới hạn cho cây của bạn (xem [Cấu hình máy chủ](../install_setup/configuration.md)). Đỉnh của phần **Dữ liệu** hiển thị mức sử dụng hiện tại so với các giới hạn này:

- **Người** – số lượng đối tượng người trong cây so với giới hạn tối đa đã cấu hình (∞ nếu không giới hạn)
- **Lưu trữ phương tiện** – tổng kích thước của các tệp phương tiện đã tải lên so với hạn mức lưu trữ đã cấu hình (∞ nếu không giới hạn)

Một lần nhập sẽ vượt quá giới hạn về số lượng người sẽ bị từ chối hoàn toàn.

## Tệp GEDCOM

Cả tệp GEDCOM 5.5.1 và GEDCOM 7 đều có thể được nhập. Có một vài điều cần lưu ý.

### Mã hóa ký tự

Một tệp GEDCOM 5.5.1 khai báo mã hóa ký tự của nó trong tiêu đề. Các mã hóa UTF-8, UTF-16, ANSEL và Windows (ANSI) được hỗ trợ. Nếu tên có dấu hoặc các ký tự đặc biệt khác trông bị rối sau khi nhập (ví dụ `MÃ¼ller` thay vì `Müller`), tệp có thể đã được xuất với mã hóa khác với mã hóa mà nó khai báo. Xuất lại tệp từ chương trình cũ của bạn, chọn UTF-8 nếu nó cung cấp tùy chọn, và [bắt đầu lại](#starting-over).

Các tệp GEDCOM 7 phải luôn được mã hóa dưới dạng UTF-8; các tệp khác sẽ bị từ chối với lỗi "Tệp GEDCOM không hợp lệ".

### Dữ liệu cụ thể cho chương trình

Nhiều chương trình thêm các phần mở rộng riêng của họ vào GEDCOM mà các chương trình khác không hiểu. Gramps không âm thầm bỏ qua dữ liệu như vậy: các dòng mà nó không thể diễn giải được thu thập trong một ghi chú của loại "nhập GEDCOM", đính kèm vào người, gia đình, hoặc đối tượng khác mà chúng thuộc về. Xem xét các ghi chú này để xem có điều gì quan trọng không được chuyển giao.

### Tệp phương tiện

Một tệp GEDCOM chứa các tham chiếu đến các tệp phương tiện (như ảnh hoặc tài liệu quét), nhưng không chứa các tệp đó. Sau khi nhập, các đối tượng phương tiện tồn tại trong cây của bạn, nhưng các tệp của chúng bị thiếu, điều này được hiển thị dưới [Tình trạng tệp phương tiện](import-media.md#media-file-status). Để thêm các tệp, xem [Nhập tệp phương tiện](import-media.md).

## Đến từ Gramps Desktop

Nếu bạn đang sử dụng Gramps Desktop, có hai bước để chuẩn bị cơ sở dữ liệu của bạn để đảm bảo mọi thứ sẽ hoạt động suôn sẻ trong các bước tiếp theo.

1. Kiểm tra và sửa chữa cơ sở dữ liệu
    - Tùy chọn: tạo một bản sao lưu cơ sở dữ liệu bằng cách xuất sang Gramps XML
    - Chạy [Công cụ Kiểm tra và Sửa chữa cơ sở dữ liệu](https://gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Tools#Check_and_Repair_Database). Điều này sửa chữa một số sự không nhất quán nội bộ có thể dẫn đến vấn đề trong Gramps Web.
2. Chuyển đổi đường dẫn phương tiện thành tương đối
    - Sử dụng Trình quản lý Phương tiện Gramps để [chuyển đổi tất cả các đường dẫn phương tiện từ tuyệt đối sang tương đối](https://gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Tools#Convert_paths_from_relative_to_absolute). Lưu ý rằng ngay cả với các đường dẫn tương đối, bất kỳ tệp phương tiện nào bên ngoài thư mục phương tiện của Gramps của bạn sẽ không hoạt động đúng khi đồng bộ hóa với Gramps Web.

Sau đó xuất cây của bạn sang Gramps XML (`.gramps`), nhập nó như đã mô tả ở trên, và [tải lên các tệp phương tiện của bạn](import-media.md). Để tiếp tục làm việc trên cùng một cây trên máy tính của bạn và trên web, hãy sử dụng [tiện ích mở rộng Đồng bộ hóa Gramps Web](sync.md).

### Tại sao không hỗ trợ gói Gramps XML?

Trong khi Gramps XML (`.gramps`) là định dạng ưa thích để nhập dữ liệu, gói Gramps XML (`.gpkg`) không được Gramps Web hỗ trợ. Điều này là do các quy trình nhập và xuất cho các tệp phương tiện không phù hợp để sử dụng trên máy chủ web.

## Vấn đề thường gặp

**"Định dạng không được hỗ trợ".** Chỉ các đuôi tệp được liệt kê [ở trên](#which-file-to-use) mới có thể được nhập. Nếu chương trình hoặc dịch vụ trực tuyến của bạn đã cung cấp cho bạn một tệp ZIP, hãy giải nén nó và tải lên tệp `.ged` bên trong.

**Mọi thứ xuất hiện hai lần.** Cùng một tệp đã được nhập hai lần. Vì các lần nhập không bao giờ hợp nhất, [bắt đầu lại](#starting-over).

**Ký tự đặc biệt bị rối.** Xem [Mã hóa ký tự](#character-encoding).

**Ảnh bị thiếu.** Xem [Nhập tệp phương tiện](import-media.md).

### Bắt đầu lại

Nếu một lần nhập gặp lỗi, hoặc bạn muốn sửa chữa một cái gì đó trong chương trình cũ của bạn và nhập lại, trước tiên hãy làm trống cây bằng cách sử dụng [Xóa tất cả đối tượng](#delete-all-objects), sau đó nhập tệp đã được sửa chữa. Lưu ý rằng điều này cũng xóa bất kỳ thay đổi nào bạn đã thực hiện trong Gramps Web kể từ lần nhập.

### Xóa tất cả đối tượng

!!! danger
    Việc xóa đối tượng là **không thể khôi phục**. Hãy tạo một [bản sao lưu](backups.md) trước khi tiếp tục.

**Xóa tất cả đối tượng** được tìm thấy trong phần **Khu vực Nguy hiểm** của [cài đặt Quản trị](settings.md). Nhấp vào **Xóa** mở một hộp thoại nơi bạn có thể chọn để xóa:

- **Tất cả đối tượng** – hoàn toàn xóa sạch cây
- **Các loại đối tượng cụ thể** – ví dụ, chỉ sự kiện hoặc chỉ đối tượng phương tiện

Bạn sẽ được yêu cầu xác thực lại (đăng nhập lại) để xác nhận hành động. Việc xóa diễn ra như một tác vụ nền và một chỉ báo tiến trình được hiển thị.

!!! warning
    Việc xóa chỉ một tập hợp con của các loại đối tượng (thay vì tất cả đối tượng cùng một lúc) có thể mất rất nhiều thời gian cho các cây lớn, vì máy chủ phải kiểm tra và cập nhật tất cả các mối quan hệ giữa các đối tượng.
