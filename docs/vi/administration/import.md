# Nhập dữ liệu

Bạn có thể đưa một cây gia đình hiện có vào Gramps Web bằng cách tải lên một tệp được xuất từ một chương trình gia phả khác, từ một dịch vụ trực tuyến, hoặc từ Gramps Desktop.

Chức năng nhập dữ liệu nằm trong phần **Dữ liệu** của [cài đặt Quản trị](settings.md) (biểu tượng người dùng ở thanh công cụ trên cùng ▸ Quản trị), có sẵn cho các chủ sở hữu cây và quản trị viên. Khi cây vẫn còn trống, nút **Nhập Cây Gia Đình** trên thẻ "Bắt đầu" của trang chính cũng dẫn đến đó.

## Tệp nào để sử dụng

| Nguồn gốc | Xuất cây của bạn dưới dạng | Đuôi tệp |
|---|---|---|
| Một chương trình gia phả khác hoặc dịch vụ trực tuyến | GEDCOM | `.ged` |
| Gramps Desktop | Gramps XML | `.gramps` |
| GeneWeb | GeneWeb | `.gw` |
| Pro-Gen | Pro-Gen | `.def` |
| Một bảng tính | Gramps CSV | `.csv` |
| Một danh bạ | vCard | `.vcf` |

GEDCOM là định dạng trao đổi phổ biến mà hầu hết mọi chương trình gia phả và dịch vụ trực tuyến đều có thể xuất. Tìm tùy chọn "Xuất" hoặc "Tải xuống" trong chương trình của bạn hoặc trên trang web, và chọn GEDCOM nếu bạn được cung cấp nhiều định dạng. Trang Wiki của Gramps [Nhập từ một chương trình gia phả khác](https://www.gramps-project.org/wiki/index.php/Import_from_another_genealogy_program) có ghi chú về các chương trình cụ thể.

Nếu bạn sử dụng Gramps Desktop, hãy chọn Gramps XML (`.gramps`) thay vì GEDCOM. Nó mang tất cả dữ liệu Gramps mà không bị mất, và các cây trực tuyến và ngoại tuyến của bạn giữ nguyên các định danh giống nhau, để có thể [đồng bộ hóa](sync.md). Xem [Đến từ Gramps Desktop](#coming-from-gramps-desktop) bên dưới.

## Nhập tệp cây gia đình

1. Mở phần **Dữ liệu** của cài đặt Quản trị.
2. Dưới "Nhập Cây Gia Đình", chọn tệp của bạn và nhấp vào **Nhập**.
3. Tệp sẽ được phân tích trước, và một hộp thoại "Xác nhận Nhập" sẽ hiển thị số lượng đối tượng mà nó chứa (người, gia đình, sự kiện, địa điểm, v.v.). Chưa có gì được thêm vào cây của bạn. Kiểm tra xem các số liệu có hợp lý không, sau đó nhấp vào **Nhập** để tiếp tục, hoặc **Hủy** để thoát mà không thay đổi gì.
4. Quá trình nhập diễn ra ở chế độ nền và một chỉ báo tiến trình sẽ được hiển thị. Khi dữ liệu đã được nhập, chỉ mục tìm kiếm sẽ được cập nhật, điều này có thể mất một thời gian đối với một cây lớn.

Khi quá trình nhập hoàn tất, hãy kiểm tra kết quả: so sánh số lượng người trong bảng **Thống kê** trên trang chính với số lượng trong chương trình cũ của bạn, và mở một gia đình mà bạn biết rõ để xem rằng cha mẹ, con cái, ngày tháng và địa điểm đã được chuyển qua như mong đợi.

!!! warning
    Một lần nhập thông thường hoàn toàn là bổ sung: nó luôn tạo ra các đối tượng mới và không bao giờ cập nhật hoặc xóa các đối tượng hiện có, ngay cả đối với các đối tượng đã tồn tại trong cây của bạn dưới cùng một ID Gramps hoặc tay cầm. Nhập cùng một tệp hai lần – hoặc nhập một tệp chồng chéo với dữ liệu đã có trong cây – sẽ nhân đôi mọi đối tượng khớp thay vì hợp nhất hoặc bỏ qua nó.

    Nếu bạn cần đưa vào các thay đổi được thực hiện ở nơi khác vào một cây đã được nhập, hãy sử dụng [Khôi phục từ Sao lưu](settings.md#restore-from-backup) thay vào đó, điều này thay thế cây để khớp với tệp đã tải lên thay vì thêm vào nó. Điều này yêu cầu một tệp Gramps XML hoặc một bản sao lưu Gramps Web.

Nếu một giới hạn về số lượng người đã được đặt cho cây của bạn (xem [Hạn mức sử dụng](settings.md#usage-quotas)), một lần nhập sẽ vượt quá giới hạn đó sẽ bị từ chối hoàn toàn.

## Tệp GEDCOM

Cả tệp GEDCOM 5.5.1 và GEDCOM 7 đều có thể được nhập. Có một vài điều cần lưu ý.

### Mã hóa ký tự

Một tệp GEDCOM 5.5.1 khai báo mã hóa ký tự của nó trong tiêu đề. Các mã hóa UTF-8, UTF-16, ANSEL và Windows (ANSI) được hỗ trợ. Nếu các tên có dấu hoặc các ký tự đặc biệt khác trông bị rối sau khi nhập (ví dụ `MÃ¼ller` thay vì `Müller`), tệp có thể đã được xuất với một mã hóa khác so với mã hóa mà nó khai báo. Xuất lại tệp từ chương trình cũ của bạn, chọn UTF-8 nếu có tùy chọn, và [bắt đầu lại](#starting-over).

Các tệp GEDCOM 7 phải luôn được mã hóa dưới dạng UTF-8; các tệp khác sẽ bị từ chối với lỗi "Tệp GEDCOM không hợp lệ".

### Dữ liệu cụ thể của chương trình

Nhiều chương trình thêm các phần mở rộng riêng của họ vào GEDCOM mà các chương trình khác không hiểu. Gramps không âm thầm bỏ qua dữ liệu như vậy: các dòng mà nó không thể diễn giải sẽ được thu thập trong một ghi chú loại "nhập GEDCOM", gắn liền với người, gia đình, hoặc đối tượng khác mà chúng thuộc về. Xem lại các ghi chú này để xem có điều gì quan trọng không được chuyển qua.

### Tệp phương tiện

Một tệp GEDCOM chứa các tham chiếu đến các tệp phương tiện (như ảnh hoặc tài liệu quét), nhưng không chứa chính các tệp đó. Sau khi nhập, các đối tượng phương tiện tồn tại trong cây của bạn, nhưng các tệp của chúng bị thiếu, điều này được hiển thị dưới [Trạng thái tệp phương tiện](settings.md#media-file-status). Để thêm các tệp, hãy xem [Nhập tệp phương tiện](#import-media-files) bên dưới.

## Đến từ Gramps Desktop

Nếu bạn đang sử dụng Gramps Desktop, có hai bước để chuẩn bị cơ sở dữ liệu của bạn để đảm bảo mọi thứ sẽ hoạt động trơn tru trong các bước tiếp theo.

1. Kiểm tra và sửa chữa cơ sở dữ liệu
    - Tùy chọn: tạo một bản sao lưu cơ sở dữ liệu bằng cách xuất sang Gramps XML
    - Chạy [Công cụ Kiểm tra và Sửa chữa Cơ sở Dữ liệu](https://gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Tools#Check_and_Repair_Database). Điều này sửa chữa một số bất thường nội bộ có thể dẫn đến vấn đề trong Gramps Web.
2. Chuyển đổi đường dẫn phương tiện thành tương đối
    - Sử dụng Trình quản lý Phương tiện Gramps để [chuyển đổi tất cả các đường dẫn phương tiện từ tuyệt đối sang tương đối](https://gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Tools#Convert_paths_from_relative_to_absolute). Lưu ý rằng ngay cả với các đường dẫn tương đối, bất kỳ tệp phương tiện nào bên ngoài thư mục phương tiện Gramps của bạn sẽ không hoạt động đúng khi đồng bộ hóa với Gramps Web.

Sau đó, xuất cây của bạn sang Gramps XML (`.gramps`), nhập nó như đã mô tả ở trên, và tải lên các tệp phương tiện của bạn như đã mô tả trong phần tiếp theo. Để tiếp tục làm việc trên cùng một cây trên máy tính của bạn và trên web, hãy sử dụng [Tiện ích mở rộng Đồng bộ Gramps Web](sync.md).

### Tại sao không hỗ trợ gói Gramps XML?

Trong khi Gramps XML (`.gramps`) là định dạng ưa thích để nhập dữ liệu, gói Gramps XML (`.gpkg`) không được Gramps Web hỗ trợ. Điều này là do các quy trình nhập và xuất cho các tệp phương tiện không phù hợp để sử dụng trên máy chủ web.

## Nhập tệp phương tiện

Nếu bạn đã nhập một cây gia đình và cần tải lên các tệp phương tiện tương ứng, hãy sử dụng **Nhập Tệp Phương Tiện** trong phần Dữ liệu của cài đặt Quản trị. Nó yêu cầu một tệp ZIP chứa các tệp phương tiện bị thiếu. Các tệp sẽ được khớp với các đối tượng phương tiện trong cây của bạn theo một trong hai cách:

- **Theo kiểm tra.** Đối với các đối tượng phương tiện có kiểm tra – như trường hợp của các cây được nhập từ Gramps Desktop – tệp có kiểm tra khớp sẽ được sử dụng, bất kể tên của nó hoặc cấu trúc thư mục trong tệp ZIP. Điều này chỉ hoạt động nếu các kiểm tra trong cơ sở dữ liệu Gramps là chính xác, điều này được đảm bảo khi chạy công cụ kiểm tra và sửa chữa.
- **Theo đường dẫn.** Các đối tượng phương tiện không có kiểm tra – như thường thấy sau khi nhập GEDCOM – được khớp theo đường dẫn của chúng: tệp ZIP phải chứa tệp dưới đúng đường dẫn tương đối được lưu trữ trong đối tượng phương tiện.

Nếu các đường dẫn được lưu trữ trong tệp GEDCOM của bạn là tuyệt đối (ví dụ `C:\Users\...\photo.jpg`), việc khớp theo đường dẫn sẽ không hoạt động. Trong trường hợp này, nên nhập tất cả vào Gramps Desktop trước, nơi có nhiều tùy chọn hơn để liên kết các tệp phương tiện hiện có với một cây đã nhập, và sau đó chuyển sang Gramps Web như đã mô tả trong [Đến từ Gramps Desktop](#coming-from-gramps-desktop).

## Các vấn đề phổ biến

**"Định dạng không được hỗ trợ".** Chỉ các đuôi tệp được liệt kê [ở trên](#which-file-to-use) mới có thể được nhập. Nếu chương trình hoặc dịch vụ trực tuyến của bạn đã cung cấp cho bạn một tệp ZIP, hãy giải nén nó và tải lên tệp `.ged` bên trong.

**Mọi thứ xuất hiện hai lần.** Cùng một tệp đã được nhập hai lần. Vì các lần nhập không bao giờ hợp nhất, hãy [bắt đầu lại](#starting-over).

**Ký tự đặc biệt bị rối.** Xem [Mã hóa ký tự](#character-encoding).

**Ảnh bị thiếu.** Xem [Nhập tệp phương tiện](#import-media-files).

### Bắt đầu lại

Nếu một lần nhập bị sai, hoặc bạn muốn sửa chữa điều gì đó trong chương trình cũ của mình và nhập lại, trước tiên hãy làm trống cây bằng cách sử dụng [Xóa tất cả đối tượng](settings.md#delete-all-objects) trong Khu vực Nguy hiểm của cài đặt Quản trị, sau đó nhập tệp đã được sửa chữa. Lưu ý rằng điều này cũng sẽ xóa bất kỳ thay đổi nào bạn đã thực hiện trong Gramps Web kể từ khi nhập.
