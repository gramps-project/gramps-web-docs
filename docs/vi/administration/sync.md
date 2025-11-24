# Đồng bộ hóa Gramps Web và Gramps Desktop

*Gramps Web Sync* là một addon cho Gramps cho phép đồng bộ hóa cơ sở dữ liệu Gramps của bạn trên máy tính để bàn với Gramps Web, bao gồm cả các tệp phương tiện.

!!! warning
    Giống như bất kỳ công cụ đồng bộ hóa nào, xin đừng coi đây là công cụ sao lưu. Việc xóa ngẫu nhiên ở một bên sẽ được lan truyền sang bên kia. Hãy chắc chắn tạo các bản sao lưu định kỳ (ở định dạng Gramps XML) của cây gia đình của bạn.

!!! info
    Tài liệu này đề cập đến phiên bản mới nhất của Gramps Web Sync Addon. Vui lòng sử dụng trình quản lý addon Gramps để cập nhật addon lên phiên bản mới nhất nếu cần.

## Cài đặt

Addon yêu cầu Gramps 6.0 chạy trên Python 3.10 hoặc mới hơn.
Nó có sẵn trong Gramps Desktop và có thể được cài đặt [theo cách thông thường](https://www.gramps-project.org/wiki/index.php/5.2_Addons#Installing_Addons_in_Gramps).

!!! warn
    Vui lòng đảm bảo sử dụng cùng một phiên bản Gramps trên máy tính để bàn với phiên bản đang chạy trên máy chủ của bạn. Xem phần [Get Help](../help/help.md) để biết cách tìm ra phiên bản Gramps mà máy chủ của bạn đang chạy. Phiên bản Gramps có dạng `MAJOR.MINOR.PATCH`, và `MAJOR` và `MINOR` phải giống nhau trên web và desktop.

Bước tùy chọn:

??? note inline end "Lỗi Gnome keyring"
    Hiện tại có một [lỗi trong python keyring](https://github.com/jaraco/keyring/issues/496) ảnh hưởng đến nhiều cấu hình desktop Gnome. Bạn có thể cần tạo tệp cấu hình `~/.config/python_keyring/keyringrc.cfg` và chỉnh sửa nó để trông như sau:

        [backend]
        default-keyring=keyring.backends.SecretService.Keyring

- Cài đặt `keyring` (ví dụ: `sudo apt install python3-keyring` hoặc `sudo dnf install python3-keyring`) để cho phép lưu trữ mật khẩu API một cách an toàn trong trình quản lý mật khẩu của hệ thống bạn.

## Sử dụng

Sau khi cài đặt, addon có sẵn trong Gramps dưới *Tools > Family Tree Processing > Gramps&nbsp;Web&nbsp;Sync*. Khi bắt đầu, và sau khi xác nhận hộp thoại rằng lịch sử hoàn tác sẽ bị bỏ qua, một wizard sẽ hướng dẫn bạn qua các bước đồng bộ hóa. Lưu ý rằng không có thay đổi nào sẽ được áp dụng cho cây địa phương của bạn hoặc cho máy chủ cho đến khi bạn xác nhận chúng một cách rõ ràng.

### Bước 1: nhập thông tin xác thực máy chủ

Công cụ sẽ yêu cầu bạn nhập URL cơ sở (ví dụ: `https://mygrampsweb.com/`) của phiên bản Gramps Web của bạn, tên người dùng và mật khẩu. Bạn cần một tài khoản với ít nhất quyền biên tập để đồng bộ hóa các thay đổi trở lại cơ sở dữ liệu từ xa của bạn. Tên người dùng và URL sẽ được lưu trữ dưới dạng văn bản thuần túy trong thư mục người dùng Gramps của bạn, mật khẩu chỉ được lưu trữ nếu `keyring` được cài đặt (xem trên).

### Bước 2: xem xét các thay đổi

Sau khi xác nhận thông tin xác thực của bạn, công cụ sẽ so sánh cơ sở dữ liệu cục bộ và từ xa và đánh giá xem có bất kỳ sự khác biệt nào không. Nếu có, nó sẽ hiển thị danh sách các thay đổi đối tượng (nơi một đối tượng có thể là một người, gia đình, sự kiện, địa điểm, v.v.) thuộc một trong các loại sau:

- được thêm vào cục bộ
- bị xóa cục bộ
- được sửa đổi cục bộ
- được thêm vào từ xa
- bị xóa từ xa
- được sửa đổi từ xa
- được sửa đổi đồng thời (tức là, ở cả hai bên)

Công cụ sử dụng dấu thời gian để đánh giá bên nào mới hơn cho mỗi đối tượng (xem "Nền tảng" bên dưới nếu bạn quan tâm đến chi tiết).

Nếu các thay đổi trông như mong đợi, bạn có thể nhấp vào "Áp dụng" để áp dụng các thay đổi cần thiết cho cơ sở dữ liệu cục bộ và từ xa.

!!! tip "Nâng cao: Chế độ đồng bộ hóa"
    Dưới danh sách các thay đổi, bạn có thể chọn một chế độ đồng bộ hóa.
    
    Mặc định, **đồng bộ hóa hai chiều**, có nghĩa là nó sẽ áp dụng các thay đổi cho cả hai bên (cục bộ và từ xa) bằng cách sao chép các thay đổi đã phát hiện (các đối tượng được thêm vào cục bộ sẽ được thêm vào bên từ xa, v.v.). Các đối tượng được sửa đổi ở cả hai bên sẽ được hợp nhất và cập nhật ở cả hai bên.

    Tùy chọn **đặt lại từ xa về cục bộ** sẽ đảm bảo cơ sở dữ liệu Gramps từ xa trông giống hệt như cơ sở dữ liệu cục bộ. Bất kỳ đối tượng nào được phát hiện là "được thêm vào từ xa" sẽ bị xóa lại, các đối tượng được phát hiện là "bị xóa từ xa" sẽ được thêm lại, v.v. *Không có thay đổi nào sẽ được áp dụng cho cơ sở dữ liệu Gramps cục bộ.*

    Tùy chọn **đặt lại cục bộ về từ xa** hoạt động theo cách ngược lại và đặt trạng thái cục bộ giống như của cơ sở dữ liệu từ xa. *Không có thay đổi nào sẽ được áp dụng cho cơ sở dữ liệu từ xa.*

    Cuối cùng, tùy chọn **hợp nhất** tương tự như đồng bộ hóa hai chiều ở chỗ nó sửa đổi cả hai cơ sở dữ liệu, nhưng *không xóa bất kỳ đối tượng nào*, mà thay vào đó khôi phục tất cả các đối tượng bị xóa chỉ ở một bên.

### Bước 3: đồng bộ hóa các tệp phương tiện

*Sau khi* các cơ sở dữ liệu đã được đồng bộ hóa, công cụ kiểm tra bất kỳ tệp phương tiện mới hoặc đã cập nhật nào. Nếu nó tìm thấy bất kỳ tệp nào, nó sẽ hiển thị danh sách và yêu cầu xác nhận để tải lên/tải xuống các tệp cần thiết.

Lưu ý các hạn chế sau của việc đồng bộ hóa tệp phương tiện:

- Nếu một tệp cục bộ có checksum khác với tệp được lưu trữ trong cơ sở dữ liệu Gramps (điều này có thể xảy ra ví dụ như đối với các tệp Word khi được chỉnh sửa sau khi được thêm vào Gramps), việc tải lên sẽ thất bại với một thông báo lỗi.
- Công cụ không kiểm tra tính toàn vẹn của tất cả các tệp cục bộ, vì vậy nếu một tệp cục bộ tồn tại dưới đường dẫn được lưu trữ cho đối tượng phương tiện, nhưng tệp đó khác với tệp trên máy chủ, công cụ sẽ không phát hiện ra. Sử dụng Addon Xác minh Phương tiện để phát hiện các tệp có checksum không chính xác.

## Khắc phục sự cố

### Ghi nhật ký gỡ lỗi

Nếu bạn gặp sự cố với Addon Đồng bộ hóa, vui lòng khởi động Gramps với ghi nhật ký gỡ lỗi được bật bằng cách [khởi động Gramps từ dòng lệnh](https://gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Command_Line) với tùy chọn sau:

```bash
gramps --debug grampswebsync
```

Điều này sẽ in nhiều câu lệnh ghi nhật ký hữu ích ra dòng lệnh giúp bạn xác định nguyên nhân của sự cố.

### Thông tin xác thực máy chủ

Nếu bước đầu tiên đã thất bại, vui lòng kiểm tra lại URL máy chủ, tên người dùng và mật khẩu của bạn.

### Vấn đề về quyền

Nếu bạn gặp một lỗi liên quan đến quyền, vui lòng kiểm tra vai trò người dùng của tài khoản người dùng Gramps Web của bạn. Bạn chỉ có thể áp dụng các thay đổi cho cơ sở dữ liệu từ xa nếu bạn là người dùng có vai trò biên tập, chủ sở hữu hoặc quản trị viên.

### Thay đổi cơ sở dữ liệu không mong đợi

Nếu công cụ đồng bộ phát hiện các thay đổi mà bạn nghĩ là không xảy ra, có thể có sự không nhất quán trong một trong các cơ sở dữ liệu khiến Gramps phát hiện sự khác biệt, hoặc thời gian không đồng bộ giữa máy tính cục bộ của bạn và máy chủ của bạn.

Vui lòng kiểm tra xem đồng hồ trên cả hai máy có được đặt đúng không (lưu ý, múi giờ không quan trọng vì công cụ sử dụng dấu thời gian Unix, không phụ thuộc vào múi giờ).

Bạn cũng có thể chạy công cụ kiểm tra & sửa chữa trên cơ sở dữ liệu cục bộ của bạn và xem điều này có giúp ích không.

Một phương pháp thô nhưng hiệu quả để đảm bảo sự không nhất quán trong cơ sở dữ liệu cục bộ của bạn không gây ra các kết quả dương tính giả là xuất cơ sở dữ liệu của bạn sang Gramps XML và nhập lại vào một cơ sở dữ liệu mới, trống. Đây là một thao tác không mất dữ liệu nhưng đảm bảo tất cả dữ liệu được nhập một cách nhất quán.

### Lỗi timeout

Nếu bạn gặp lỗi timeout (ví dụ: được chỉ định bởi mã trạng thái HTTP 408 hoặc một thông báo lỗi khác bao gồm từ "timeout"), có thể do số lượng lớn các thay đổi cần được đồng bộ hóa sang bên từ xa kết hợp với cấu hình máy chủ của bạn.

Đối với các phiên bản của addon đồng bộ trước phiên bản v1.2.0 và các phiên bản của Gramps Web API trước phiên bản v2.7.0 (xem tab thông tin phiên bản trong Gramps Web), việc đồng bộ hóa sang phía máy chủ được xử lý trong một yêu cầu duy nhất có thể hết thời gian, tùy thuộc vào cấu hình máy chủ, sau một đến tối đa vài phút. Đối với các đồng bộ lớn (chẳng hạn như sau khi nhập hàng nghìn đối tượng vào cơ sở dữ liệu cục bộ hoặc cố gắng đồng bộ hóa một cơ sở dữ liệu cục bộ đầy đủ sang một cơ sở dữ liệu máy chủ trống), thời gian này có thể quá ngắn.

Nếu bạn đang sử dụng addon đồng bộ phiên bản v1.2.0 trở lên và Gramps Web API phiên bản v2.7.0 trở lên, việc đồng bộ hóa phía máy chủ được xử lý bởi một tác nhân nền và có thể chạy rất lâu (một thanh tiến trình sẽ được hiển thị) và lỗi timeout sẽ không xảy ra.

### Lỗi tệp phương tiện không mong đợi

Nếu việc tải lên một tệp phương tiện thất bại, thường là do sự không khớp trong checksum của tệp thực tế trên đĩa và checksum trong cơ sở dữ liệu Gramps cục bộ. Điều này thường xảy ra với các tệp có thể chỉnh sửa, như tài liệu văn phòng, được chỉnh sửa bên ngoài Gramps. Vui lòng sử dụng Addon Xác minh Phương tiện Gramps để sửa chữa các checksum của tất cả các tệp phương tiện.

### Hỏi để được giúp đỡ

Nếu tất cả những điều trên không giúp ích, bạn có thể hỏi cộng đồng để được giúp đỡ bằng cách đăng bài trong [chuyên mục Gramps Web của diễn đàn Gramps](https://gramps.discourse.group/c/gramps-web/28). Vui lòng đảm bảo cung cấp:

- phiên bản của Gramps Web Sync addon (và vui lòng sử dụng phiên bản phát hành mới nhất)
- phiên bản Gramps desktop mà bạn đang sử dụng
- đầu ra của ghi nhật ký gỡ lỗi Gramps, được bật như đã mô tả ở trên
- thông tin phiên bản của Gramps Web (bạn có thể tìm thấy nó dưới Cài đặt/Thông tin phiên bản)
- bất kỳ chi tiết nào bạn có thể cung cấp về cài đặt Gramps Web của bạn (tự lưu trữ, Grampshub, ...)
- đầu ra của nhật ký máy chủ Gramps Web của bạn, nếu bạn có quyền truy cập vào chúng (khi sử dụng docker: `docker compose logs --tail 100 grampsweb` và `docker compose logs --tail 100 grampsweb-celery`)

## Nền tảng: cách addon hoạt động

Nếu bạn tò mò về cách addon thực sự hoạt động, bạn có thể tìm thấy một số chi tiết hơn trong phần này.

Addon được thiết kế để giữ cho một cơ sở dữ liệu Gramps cục bộ đồng bộ với một cơ sở dữ liệu Gramps Web từ xa, cho phép cả thay đổi cục bộ và từ xa (chỉnh sửa hợp tác).

Nó **không phù hợp**

- Để đồng bộ hóa với một cơ sở dữ liệu không phải là biến thể trực tiếp (bắt đầu từ một bản sao cơ sở dữ liệu hoặc xuất/nhập Gramps XML) của cơ sở dữ liệu cục bộ
- Để hợp nhất hai cơ sở dữ liệu với một số lượng lớn các thay đổi ở cả hai bên cần sự chú ý thủ công để hợp nhất. Sử dụng [Công cụ Nhập Hợp nhất](https://www.gramps-project.org/wiki/index.php/Import_Merge_Tool) xuất sắc cho mục đích này.

Các nguyên tắc hoạt động của công cụ rất đơn giản:

- Nó so sánh cơ sở dữ liệu cục bộ và từ xa
- Nếu có bất kỳ sự khác biệt nào, nó kiểm tra dấu thời gian của đối tượng giống hệt cuối cùng, hãy gọi nó là **t**
- Nếu một đối tượng thay đổi gần đây hơn **t** tồn tại trong một cơ sở dữ liệu nhưng không tồn tại trong cơ sở dữ liệu kia, nó sẽ được đồng bộ hóa đến cả hai (giả sử đối tượng mới)
- Nếu một đối tượng thay đổi lần cuối trước **t** vắng mặt trong một cơ sở dữ liệu, nó sẽ bị xóa ở cả hai (giả sử đối tượng đã bị xóa)
- Nếu một đối tượng khác nhau nhưng thay đổi sau **t** chỉ trong một cơ sở dữ liệu, đồng bộ hóa đến cơ sở dữ liệu kia (giả sử đối tượng đã sửa đổi)
- Nếu một đối tượng khác nhau nhưng thay đổi sau **t** trong cả hai cơ sở dữ liệu, hợp nhất chúng (giả sử sửa đổi xung đột)

Thuật toán này đơn giản và mạnh mẽ vì nó không yêu cầu theo dõi lịch sử đồng bộ hóa. Tuy nhiên, nó hoạt động tốt nhất khi bạn *đồng bộ hóa thường xuyên*.
