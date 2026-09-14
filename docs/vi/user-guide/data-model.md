# Cách Gramps tổ chức dữ liệu

Gramps Web lưu trữ một cây gia đình không phải dưới dạng biểu đồ, mà là các đối tượng riêng biệt – người, gia đình, sự kiện, địa điểm, nguồn, và nhiều thứ khác – được liên kết với nhau. Khi bạn biết cách các đối tượng này kết hợp với nhau, việc nhập dữ liệu trở nên dễ đoán: bất cứ thứ gì bạn muốn liên kết phải tồn tại trước.

Gramps Web sử dụng cùng một mô hình dữ liệu như Gramps Desktop, vì vậy mọi thứ trên trang này đều áp dụng cho cả hai.

## Các khối xây dựng

| Đối tượng | Đại diện cho điều gì | Ví dụ |
|---|---|---|
| Người | Một cá nhân | Bạn, bà của bạn |
| Gia đình | Một cặp đôi, con cái của họ, hoặc cả hai | Cha mẹ của bạn và con cái của họ |
| Sự kiện | Một điều gì đó đã xảy ra, với một ngày và một địa điểm | Sinh, kết hôn, điều tra dân số, di cư |
| Địa điểm | Một vị trí địa lý | Một ngôi làng, một giáo xứ, một quốc gia |
| Nguồn | Một tài liệu hoặc bộ thông tin | Một sổ đăng ký giáo xứ, một cuộc điều tra dân số, một cuốn sách |
| Trích dẫn | Một tham chiếu cụ thể trong một nguồn | Trang 12, mục 3 của sổ đăng ký giáo xứ |
| Kho lưu trữ | Nơi một nguồn được lưu giữ | Một kho lưu trữ, một thư viện, một trang web |
| Ghi chú | Văn bản tự do | Một bản sao, nhận xét nghiên cứu |
| Đối tượng truyền thông | Một tệp | Một bức ảnh, một chứng chỉ quét |

Mỗi loại đối tượng có danh sách riêng trong Gramps Web, xem [Danh sách](lists.md).

## Người và gia đình

Cha mẹ và con cái không được liên kết với nhau trực tiếp, mà thông qua một **gia đình**. Một gia đình có tối đa hai đối tác và bất kỳ số lượng con cái nào:

- Cha mẹ của bạn và bạn được liên kết thông qua gia đình mà bạn là một đứa trẻ.
- Anh chị em của bạn là những đứa trẻ khác trong cùng một gia đình.
- Bạn và vợ/chồng của bạn tạo thành một gia đình khác, trong đó bạn là một đối tác, cùng với các con của bạn.

Một người có thể là một đứa trẻ trong một gia đình và là một đối tác trong nhiều gia đình. Mỗi đứa trẻ có một mối quan hệ với mỗi cha mẹ, chẳng hạn như sinh, nhận nuôi, hoặc con riêng, và mỗi gia đình có một loại mối quan hệ, chẳng hạn như đã kết hôn hoặc liên minh dân sự.

Đó là lý do tại sao "thêm cha mẹ" cho một người có nghĩa là thêm người đó như một đứa trẻ vào một gia đình – điều mà [biểu đồ cây](tree-edit.md) thực hiện cho bạn trong một bước.

## Sự kiện

Một sự kiện sinh, chết, hoặc kết hôn không phải là một trường của một người, mà là một **sự kiện** riêng, với một loại, một ngày, một địa điểm, và một mô tả. Con người được liên kết với một sự kiện bằng một **vai trò**: người có sự kiện sinh ra có vai trò "Chính", trong khi người khác có thể được liên kết với cùng một sự kiện với vai trò là nhân chứng.

Các sự kiện liên quan đến một cặp đôi, chẳng hạn như một cuộc hôn nhân, thuộc về gia đình hơn là thuộc về một trong hai đối tác. Một sự kiện cũng có thể được chia sẻ bởi nhiều người – ví dụ như một bản ghi điều tra dân số liệt kê toàn bộ hộ gia đình – thay vì được nhập một lần cho mỗi người.

## Các đối tượng chia sẻ: địa điểm và nguồn

Địa điểm, nguồn, trích dẫn, kho lưu trữ, ghi chú, và đối tượng truyền thông tồn tại độc lập, và bất kỳ số lượng đối tượng nào khác có thể tham chiếu đến cùng một đối tượng. Điều này có một vài hệ quả:

- **Tạo một lần, chọn nhiều lần.** Ngôi làng nơi mười tổ tiên của bạn sinh ra là một địa điểm, được chọn trong mười sự kiện sinh. Nếu bạn sửa tên hoặc tọa độ của nó, sự sửa chữa sẽ áp dụng ở mọi nơi.
- **Tạo nó trước khi bạn chọn nó.** Các biểu mẫu trong Gramps Web chọn các địa điểm và nguồn đã tồn tại. Tạo một địa điểm hoặc nguồn mới trước bằng cách sử dụng nút **+** (Thêm) trong thanh ứng dụng trên cùng.
- **Các địa điểm được lồng ghép.** Một địa điểm có thể được bao quanh bởi một địa điểm lớn hơn – một ngôi làng bởi một quận, quận bởi một quốc gia – vì vậy bạn không cần phải lặp lại toàn bộ hệ thống phân cấp cho mỗi ngôi làng.
- **Nguồn và trích dẫn là riêng biệt.** Một nguồn là sổ đăng ký giáo xứ nói chung; một trích dẫn là mục cụ thể hỗ trợ một sự thật, với trang, ngày, và mức độ tin cậy của bạn. Nhiều trích dẫn có thể chỉ đến cùng một nguồn.

Nếu bạn đã vô tình tạo cùng một địa điểm hoặc nguồn hai lần, bạn có thể [gộp các bản sao](lists.md#merge).

## Người chính

Người chính là người mà các biểu đồ cây gia đình bắt đầu từ và là điểm khởi đầu mặc định cho các báo cáo. Xem [Đăng nhập lần đầu](first-login.md) để biết cách thiết lập.

!!! note "Khác với Gramps Desktop"
    Trong Gramps Desktop, Người chính được lưu trữ trong cơ sở dữ liệu cây gia đình, vì vậy nó giống nhau cho tất cả mọi người mở cơ sở dữ liệu đó. Gramps Web không sử dụng nó. Thay vào đó, Người chính được lưu trữ trong trình duyệt của bạn, riêng biệt cho mỗi cây: nó không được chia sẻ với người dùng khác, và nó không theo bạn đến trình duyệt hoặc thiết bị khác. Sau khi nhập một cây từ Gramps Desktop, hoặc khi bạn sử dụng Gramps Web trên một thiết bị khác, bạn phải thiết lập lại.

## Một thứ tự được khuyến nghị

Khi nhập một gia đình mới bằng tay, thứ tự này tránh việc nhảy qua lại giữa các biểu mẫu:

1. **Địa điểm và nguồn.** Tạo các địa điểm bạn cần và, nếu bạn ghi lại nguồn, nguồn mà bạn đang làm việc từ.
2. **Người.** Thêm những người với ngày sinh và ngày chết cùng địa điểm của họ. Điều này nhanh nhất trong chế độ chỉnh sửa của biểu đồ Cây Gia Đình, cái mà tạo ra các gia đình cho bạn – xem [Bắt đầu một cây mới](start-tree.md) và [Chỉnh sửa cây gia đình](tree-edit.md).
3. **Các sự kiện khác.** Mở một gia đình (ví dụ từ tab Quan hệ của một người) để thêm cuộc hôn nhân, và trang của một người để thêm các sự kiện khác.
4. **Trích dẫn.** Trên tab Trích dẫn Nguồn của người, sự kiện, hoặc đối tượng khác mà một nguồn hỗ trợ, thêm một trích dẫn mới, chọn nguồn, và nhập trang.
5. **Ghi chú và truyền thông.** Đính kèm các bản sao, ảnh, và quét – xem [Thêm tệp truyền thông](media.md).

## Nhập ngày tháng

Một ngày được nhập dưới dạng các trường năm, tháng, và ngày riêng biệt, mà cũng có thể được điền bằng cách sử dụng trình chọn ngày. Bỏ qua các phần bạn không biết: chỉ một năm cũng là một ngày hợp lệ.

Thay vì đoán một ngày chính xác, hãy mô tả những gì bạn thực sự biết với **Loại** của ngày:

| Những gì bạn biết | Loại | Ví dụ |
|---|---|---|
| Ngày chính xác, hoặc một phần của nó | Thông thường | 12 tháng 3 năm 1850, hoặc chỉ 1850 |
| Một ngày gần đúng | khoảng | khoảng năm 1850 |
| Một giới hạn | trước, sau | trước năm 1900 |
| Ngày nằm trong một khoảng thời gian | Khoảng | giữa năm 1850 và 1855 |
| Một cái gì đó kéo dài trong một khoảng thời gian | Khoảng thời gian | từ năm 1850 đến 1855 |
| Chỉ bắt đầu hoặc kết thúc của một khoảng thời gian | từ, đến | từ năm 1850 |

Trường **Chất lượng** ghi lại cách bạn đến được một ngày: "Ước lượng" cho một phỏng đoán có cơ sở, "Tính toán" cho một ngày được suy ra từ thông tin khác, chẳng hạn như năm sinh được tính từ độ tuổi khi chết.

!!! warning "Ngày khoảng và ước lượng bao gồm 50 năm theo cả hai hướng"
    Khi Gramps so sánh các ngày, nó coi một ngày thuộc loại "khoảng" – và bất kỳ ngày nào có chất lượng "Ước lượng" – như một khoảng thời gian kéo dài từ 50 năm trước đến 50 năm sau ngày đã cho. Ví dụ, lọc danh sách Người cho những người sinh ra giữa năm 1840 và 1860 cũng tìm thấy một người sinh ra "khoảng năm 1880", vì ngày đó được coi là bao gồm từ năm 1830 đến 1930. Theo cách tương tự, "trước" và "sau" được coi là kéo dài lên đến 50 năm trước hoặc sau ngày.

    Điều này có thể dẫn đến những kết quả bất ngờ, vì vậy hãy sử dụng "khoảng" và "Ước lượng" chỉ khi bạn không thể thu hẹp ngày. Nếu bạn biết một khoảng thời gian ngắn hơn, một Khoảng như "giữa năm 1878 và 1882" là chính xác hơn.

Trường **Lịch** cho phép bạn nhập một ngày trong lịch được sử dụng trong bản ghi gốc, chẳng hạn như lịch Julian, thay vì tự chuyển đổi nó.
