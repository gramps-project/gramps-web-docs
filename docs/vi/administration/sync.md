# Đồng bộ hóa Gramps Web và Gramps Desktop

*Gramps Web Sync* là một addon cho Gramps cho phép đồng bộ hóa cơ sở dữ liệu Gramps của bạn trên máy tính để bàn với Gramps Web, bao gồm cả các tệp phương tiện.

!!! warning
    Giống như bất kỳ công cụ đồng bộ hóa nào, xin đừng coi đây là công cụ sao lưu. Một sự xóa nhầm ở một bên sẽ được truyền sang bên kia. Hãy chắc chắn tạo các bản sao lưu định kỳ (ở định dạng Gramps XML) cho cây gia đình của bạn.

!!! info
    Tài liệu này đề cập đến phiên bản mới nhất của Gramps Web Sync Addon. Vui lòng sử dụng trình quản lý addon Gramps để cập nhật addon lên phiên bản mới nhất nếu cần.

!!! note "Điều gì đã thay đổi trong phiên bản 1.5"
    Giao diện của addon đã được viết lại trong phiên bản 1.5. Wizard từng bước đã biến mất, được thay thế bằng một cửa sổ duy nhất, và các tệp phương tiện giờ đây được xác nhận cùng với các thay đổi đối tượng thay vì trên một trang riêng biệt sau đó. Nếu bạn đang tìm kiếm bộ chọn chế độ đồng bộ, nó hiện nằm **trên** danh sách các thay đổi thay vì bên dưới. Chế độ đồng bộ **hợp nhất** đã bị xóa; xem [Chế độ đồng bộ](#sync-mode) bên dưới.

## Cài đặt

Addon yêu cầu Gramps 6.0 chạy trên Python 3.10 hoặc mới hơn. Nó có sẵn trong Gramps Desktop và có thể được cài đặt [theo cách thông thường](https://www.gramps-project.org/wiki/index.php/5.2_Addons#Installing_Addons_in_Gramps).

!!! warning
    Vui lòng đảm bảo sử dụng cùng một phiên bản Gramps trên máy tính để bàn như phiên bản đang chạy trên máy chủ của bạn. Xem phần [Nhận trợ giúp](../help/help.md) để biết cách tìm ra phiên bản Gramps mà máy chủ của bạn đang chạy. Phiên bản Gramps có dạng `MAJOR.MINOR.PATCH`, và `MAJOR` và `MINOR` phải giống nhau trên web và desktop.

### Yêu cầu máy chủ

Addon kiểm tra hai điều về máy chủ của bạn ngay khi nó kết nối, và từ chối tiếp tục nếu một trong hai điều không được đáp ứng. Cả hai kiểm tra diễn ra trước khi bất kỳ thứ gì được tải xuống.

- **Phiên bản Gramps Web API 3.x.** Phiên bản của addon này, cho Gramps 6.0, hoạt động với Gramps Web API 3. Một máy chủ cũ cần được cập nhật; một máy chủ chạy phiên bản API chính *mới hơn* cần một phiên bản Gramps mới hơn, không phải một addon mới hơn, vì mỗi dòng phát hành Gramps tương ứng với một phiên bản API. Bạn có thể tìm phiên bản của máy chủ của bạn dưới *Cài đặt ▸ Thông tin phiên bản* trong Gramps Web.
- **Một hàng đợi tác vụ nền.** Đồng bộ hóa gửi các thay đổi của nó như một tác vụ nền. Trên một máy chủ không được cấu hình hàng đợi tác vụ, việc áp dụng các thay đổi sẽ chạy đồng bộ và hết thời gian trên bất kỳ cây gia đình thực nào, vì vậy addon từ chối khởi động thay vì thất bại giữa chừng.

Bạn cũng cần một tài khoản với ít nhất quyền chỉnh sửa để áp dụng các thay đổi cho cơ sở dữ liệu từ xa.

Bước tùy chọn:

??? note inline end "Lỗi Gnome keyring"
    Hiện tại có một [lỗi trong python keyring](https://github.com/jaraco/keyring/issues/496) ảnh hưởng đến nhiều cấu hình máy tính để bàn Gnome. Bạn có thể cần tạo tệp cấu hình `~/.config/python_keyring/keyringrc.cfg` và chỉnh sửa nó để trông giống như sau:

        [backend]
        default-keyring=keyring.backends.SecretService.Keyring

- Cài đặt `keyring` (ví dụ: `sudo apt install python3-keyring` hoặc `sudo dnf install python3-keyring`) để cho phép lưu trữ mật khẩu API một cách an toàn trong trình quản lý mật khẩu của hệ thống bạn.

Nếu keyring không thể được sử dụng, addon sẽ thông báo và tiếp tục mà không có nó — bạn sẽ chỉ được yêu cầu nhập mật khẩu của mình mỗi lần. Trên gói Gramps **Snap**, keyring hệ thống bị chặn bởi confinement cho đến khi bạn kết nối giao diện một lần:

```bash
snap connect gramps:password-manager-service
```

Addon sẽ hiển thị chính xác lệnh này khi nó phát hiện tình huống.

## Sử dụng

Khi đã cài đặt, addon có sẵn trong Gramps dưới *Công cụ ▸ Xử lý Cây Gia Đình ▸ Gramps&nbsp;Web&nbsp;Sync*. Sau khi xác nhận hộp thoại cảnh báo rằng lịch sử hoàn tác sẽ bị xóa, cửa sổ đồng bộ sẽ mở ra.

**Không có thay đổi nào được áp dụng cho cây địa phương của bạn hoặc cho máy chủ cho đến khi bạn xác nhận rõ ràng chúng.**

Cửa sổ có một dải ở trên cùng ghi tên cây gia đình mà bạn đang đồng bộ hóa, tài khoản và địa chỉ mà nó thuộc về, và khi nào nó được đồng bộ hóa lần cuối. Ở dưới cùng, phiên bản của addon và của API Web của máy chủ được hiển thị — hữu ích khi báo cáo một vấn đề.

### Kết nối

Nếu bạn đã đồng bộ hóa cây gia đình này trước đó và mật khẩu của bạn đã được lưu trữ, addon sẽ kết nối ngay khi mở và đi thẳng đến so sánh. Nếu không, nó sẽ yêu cầu URL cơ sở của phiên bản Gramps Web của bạn (ví dụ: `https://mygrampsweb.com/`), tên người dùng của bạn và mật khẩu của bạn.

URL và tên người dùng được lưu trữ dưới dạng văn bản thuần túy trong thư mục người dùng Gramps của bạn. Mật khẩu được lưu trữ trong trình quản lý mật khẩu của hệ thống của bạn chỉ nếu bạn để **Nhớ mật khẩu** được đánh dấu; bỏ đánh dấu nó sẽ xóa bất kỳ mật khẩu nào đã được lưu trữ cho máy chủ đó.

!!! tip "Nhiều cây gia đình, nhiều máy chủ"
    Mỗi máy chủ mà bạn đồng bộ hóa được lưu trữ riêng biệt, cùng với bản ghi riêng của nó về khi nó được đồng bộ hóa lần cuối. Việc chuyển đổi giữa hai máy chủ không còn làm phiền cả hai.

    Mỗi mục cũng ghi lại **cây gia đình địa phương nào** mà nó đã được đồng bộ hóa lần cuối. Addon chỉ kết nối tự động khi điều đó khớp với cây mà bạn đang mở; nếu không, nó sẽ hiển thị chi tiết kết nối và chờ bạn nhấn *Kết nối*, với một cảnh báo nếu thông tin xác thực đã lưu thuộc về một cây khác. Điều này quan trọng vì việc đồng bộ hóa một cây với một máy chủ chứa một cây *khác* sẽ đề xuất xóa nội dung của cả hai.

Hai hành động có sẵn trong khi không có gì được ghi:

- **Thay đổi máy chủ…**, trên dải trên cùng, quay lại chi tiết kết nối để bạn có thể chỉ định cây này đến một máy chủ khác. Nó sẽ ngắt quãng một so sánh đang diễn ra thay vì khiến bạn phải chờ nó hoàn thành.
- **Quên máy chủ này**, trên bảng kết nối, xóa địa chỉ, tên người dùng và mật khẩu đã lưu, cùng với bản ghi về khi cây này được đồng bộ hóa lần cuối. Việc đồng bộ hóa tiếp theo sẽ so sánh hai cây từ đầu.

Nếu bạn nhập một địa chỉ bắt đầu bằng `http://` thay vì `https://`, một cảnh báo sẽ xuất hiện khi bạn gõ. Mật khẩu của bạn sẽ được gửi dưới dạng văn bản rõ ràng, vì vậy chỉ sử dụng nó cho thử nghiệm cục bộ.

### Xem xét các thay đổi

Addon so sánh cơ sở dữ liệu địa phương và từ xa và hiển thị những gì nó đề xuất thực hiện. Khác với các phiên bản trước, liệt kê các sự khác biệt thô giữa hai cây, danh sách bây giờ hiển thị các **hành động** sẽ được thực hiện, được nhóm theo cơ sở dữ liệu nào chúng thay đổi:

```
▾ Sẽ thay đổi trên máy tính này (7 đối tượng)
    ▾ Thêm 3 đối tượng
        Người   John Smith        I0123
    ▾ Cập nhật 4 đối tượng
        …
▾ Sẽ thay đổi trên máy chủ (5 đối tượng)
    …
```

Mỗi hàng ghi tên đối tượng, vì vậy bạn có thể biết ai hoặc cái gì bị ảnh hưởng thay vì chỉ thấy một ID Gramps.

Nếu bất kỳ thứ gì sẽ bị xóa, một cảnh báo ở trên danh sách cho biết số lượng đối tượng và bên nào. Điều này xuất hiện bất cứ khi nào có sự xóa liên quan, bao gồm trong một đồng bộ hai chiều thông thường đang truyền một sự xóa mà bạn đã thực hiện.

Nhấn **Áp dụng** để thực hiện những gì danh sách mô tả.

!!! warning "Đừng chỉnh sửa trong khi xem xét"
    Cửa sổ đồng bộ không chặn phần còn lại của Gramps, vì vậy bạn có thể tiếp tục làm việc trong khi danh sách mở. Nếu bạn chỉnh sửa một đối tượng bị ảnh hưởng, addon sẽ phát hiện điều đó khi bạn nhấn Áp dụng, dừng lại mà không thay đổi gì và yêu cầu bạn so sánh lại. Không có gì bị mất, nhưng việc so sánh phải được lặp lại.

#### Chế độ đồng bộ

Chế độ đồng bộ được chọn **trên** danh sách các thay đổi. Thay đổi nó sẽ xây dựng lại danh sách, vì chế độ quyết định mỗi sự khác biệt thực sự trở thành gì.

- **Đồng bộ hai chiều** (mặc định) — các thay đổi từ cả hai bên được kết hợp. Các đối tượng được chỉnh sửa ở cả hai nơi sẽ được hợp nhất.
- **Đặt lại máy chủ để khớp với máy tính này** — máy chủ sẽ được làm cho khớp với máy tính này. Bất kỳ thứ gì chỉ thay đổi trên máy chủ sẽ bị xóa.
- **Đặt lại máy tính này để khớp với máy chủ** — máy tính này sẽ được làm cho khớp với máy chủ. Bất kỳ thứ gì chỉ thay đổi ở đây sẽ bị xóa.

!!! note
    Chế độ **hợp nhất** có sẵn trong các phiên bản trước đã bị xóa. Nó khác với đồng bộ hai chiều chỉ ở việc khôi phục các đối tượng bị xóa ở một bên thay vì truyền sự xóa, điều này không phải là một sự phân biệt mà giao diện có thể giải thích một cách hữu ích. Nếu bạn đã dựa vào nó, hãy sử dụng đồng bộ hai chiều và khôi phục bất kỳ thứ gì bạn muốn giữ từ một bản sao lưu.

### Tệp phương tiện

Các tệp phương tiện được xử lý như một phần của cùng một xác nhận, không phải như một bước riêng biệt. Nếu bất kỳ tệp nào cần được chuyển, một hộp kiểm bên dưới danh sách cung cấp để di chuyển chúng:

```
[x] Cũng chuyển 12 tệp phương tiện (4 để tải xuống, 8 để tải lên)
```

Bỏ đánh dấu nó để đồng bộ hóa các thay đổi đối tượng mà không chạm vào các tệp.

Các tệp bị thiếu ở *cả hai* bên được liệt kê riêng biệt, vì không có gì có thể được thực hiện về chúng:

```
2 tệp phương tiện bị thiếu ở cả hai bên và không thể được chuyển.
```

Lưu ý các hạn chế sau của đồng bộ tệp phương tiện:

- Nếu một tệp địa phương có một checksum khác với tệp được lưu trong cơ sở dữ liệu Gramps (điều này có thể xảy ra ví dụ như đối với các tệp Word khi được chỉnh sửa sau khi được thêm vào Gramps), việc tải lên sẽ thất bại với một thông báo lỗi.
- Công cụ không kiểm tra tính toàn vẹn của tất cả các tệp địa phương, vì vậy nếu một tệp địa phương tồn tại dưới đường dẫn được lưu cho đối tượng phương tiện, nhưng tệp đó khác với tệp trên máy chủ, công cụ sẽ không phát hiện ra điều đó. Sử dụng Addon Xác minh Phương tiện để phát hiện các tệp có checksum không chính xác.

### Khi có điều gì đó sai

Nếu một sự đồng bộ thất bại giữa chừng — một kết nối bị ngắt, chẳng hạn — addon báo cáo những gì nó đã áp dụng và cung cấp **Thử lại**, điều này sẽ tiếp tục từ bước đã thất bại thay vì bắt đầu lại. Bản sao đã tải xuống của cây từ xa sẽ được giữ lại, vì vậy việc thử lại không tải xuống và so sánh nó lần thứ hai.

Chi tiết kỹ thuật của sự thất bại có sẵn trong một phần mở rộng *Chi tiết*, với một nút để sao chép chúng cho một báo cáo lỗi.

## Khắc phục sự cố

### Ghi nhật ký gỡ lỗi

Nếu bạn gặp sự cố với Addon Đồng bộ, vui lòng khởi động Gramps với ghi nhật ký gỡ lỗi được bật bằng cách [khởi động Gramps từ dòng lệnh](https://gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Command_Line) với tùy chọn sau:

```bash
gramps --debug grampswebsync
```

Điều này sẽ in nhiều câu lệnh ghi nhật ký hữu ích ra dòng lệnh giúp bạn xác định nguyên nhân của sự cố.

### Thông tin xác thực máy chủ

Nếu việc kết nối thất bại, vui lòng kiểm tra lại URL máy chủ, tên người dùng và mật khẩu của bạn.

### Addon từ chối kết nối

Nếu addon báo cáo rằng phiên bản Gramps Web API của máy chủ quá cũ hoặc quá mới, hoặc rằng không có hàng đợi tác vụ nền nào được cấu hình, hãy xem [Yêu cầu máy chủ](#server-requirements) ở trên. Những điều này được kiểm tra trước bất kỳ điều gì khác, vì vậy thông điệp sẽ nêu rõ vấn đề trực tiếp.

### Vấn đề về quyền

Nếu bạn gặp lỗi liên quan đến quyền, vui lòng kiểm tra vai trò người dùng của tài khoản Gramps Web của bạn. Bạn chỉ có thể áp dụng các thay đổi cho cơ sở dữ liệu từ xa nếu bạn là người dùng có vai trò biên tập viên, chủ sở hữu hoặc quản trị viên.

### Thay đổi cơ sở dữ liệu không mong muốn

Nếu công cụ đồng bộ phát hiện các thay đổi mà bạn nghĩ là không xảy ra, có thể có sự không nhất quán trong một trong các cơ sở dữ liệu khiến Gramps phát hiện sự khác biệt, hoặc thời gian không đồng bộ giữa máy tính địa phương của bạn và máy chủ của bạn.

Vui lòng kiểm tra rằng đồng hồ trên cả hai máy đều được đặt chính xác (lưu ý, múi giờ không quan trọng vì công cụ sử dụng dấu thời gian Unix, không phụ thuộc vào múi giờ).

Bạn cũng có thể chạy công cụ kiểm tra & sửa chữa trên cơ sở dữ liệu địa phương của bạn và xem liệu điều này có giúp ích không.

Một phương pháp thô nhưng hiệu quả để đảm bảo rằng sự không nhất quán trong cơ sở dữ liệu địa phương của bạn không gây ra các kết quả dương giả là xuất cơ sở dữ liệu của bạn sang Gramps XML và nhập lại vào một cơ sở dữ liệu mới, trống. Đây là một thao tác không mất dữ liệu nhưng đảm bảo tất cả dữ liệu được nhập một cách nhất quán.

!!! tip
    Nếu addon đề xuất một số lượng xóa đáng báo động, hãy kiểm tra dải trên cùng trước: nó ghi tên cây gia đình trên máy chủ mà bạn sắp ghi vào. Đồng bộ hóa với một máy chủ chứa một cây *khác* sẽ tạo ra chính triệu chứng này.

### Lỗi hết thời gian

Việc đồng bộ hóa với máy chủ được xử lý bởi một công nhân nền, vì vậy các đồng bộ hóa kéo dài không nên hết thời gian. Một máy chủ không được cấu hình hàng đợi tác vụ sẽ bị từ chối tại thời điểm kết nối vì lý do này — xem [Yêu cầu máy chủ](#server-requirements).

Các yêu cầu từ addon đến máy chủ sẽ hết thời gian sau 60 giây mà không có phản hồi, vì vậy một máy chủ không thể truy cập sẽ báo cáo lỗi kết nối thay vì treo vô thời hạn.

### Lỗi tệp phương tiện không mong muốn

Nếu việc tải lên một tệp phương tiện thất bại, thường là do sự không khớp trong checksum của tệp thực tế trên đĩa và checksum trong cơ sở dữ liệu Gramps địa phương. Điều này thường xảy ra với các tệp có thể chỉnh sửa, như tài liệu văn phòng, được chỉnh sửa bên ngoài Gramps. Vui lòng sử dụng Addon Xác minh Phương tiện Gramps để sửa chữa các checksum của tất cả các tệp phương tiện.

### Hỏi để được giúp đỡ

Nếu tất cả những điều trên không giúp ích, bạn có thể hỏi cộng đồng để được giúp đỡ bằng cách đăng bài trong [Danh mục Gramps Web của diễn đàn Gramps](https://gramps.discourse.group/c/gramps-web/28). Vui lòng đảm bảo cung cấp:

- phiên bản của addon Gramps Web Sync (và hãy sử dụng phiên bản phát hành mới nhất, vui lòng) — nó được hiển thị ở dưới cùng của cửa sổ đồng bộ, bên cạnh phiên bản Web API của máy chủ
- phiên bản Gramps desktop mà bạn đang sử dụng
- đầu ra của ghi nhật ký gỡ lỗi Gramps, được bật như đã mô tả ở trên
- thông tin phiên bản của Gramps Web (bạn có thể tìm thấy nó dưới Cài đặt/Thông tin phiên bản)
- bất kỳ chi tiết nào bạn có thể cung cấp về cài đặt Gramps Web của bạn (tự lưu trữ, Grampshub, ...)
- đầu ra của nhật ký máy chủ Gramps Web của bạn, nếu bạn có quyền truy cập vào chúng (khi sử dụng docker: `docker compose logs --tail 100 grampsweb` và `docker compose logs --tail 100 grampsweb-celery`)

## Bối cảnh: cách addon hoạt động

Nếu bạn tò mò về cách addon thực sự hoạt động, bạn có thể tìm thấy một số chi tiết hơn trong phần này.

Addon được thiết kế để giữ cho một cơ sở dữ liệu Gramps địa phương đồng bộ với một cơ sở dữ liệu Gramps Web từ xa, cho phép cả thay đổi địa phương và từ xa (chỉnh sửa hợp tác).

Nó **không phù hợp**

- Để đồng bộ hóa với một cơ sở dữ liệu không phải là bản sao trực tiếp (bắt đầu từ một bản sao cơ sở dữ liệu hoặc xuất/nhập Gramps XML) của cơ sở dữ liệu địa phương
- Để hợp nhất hai cơ sở dữ liệu với một số lượng lớn thay đổi ở cả hai bên cần sự chú ý thủ công để hợp nhất. Sử dụng [Công cụ Nhập Hợp nhất](https://www.gramps-project.org/wiki/index.php/Import_Merge_Tool) tuyệt vời cho mục đích này.

Các nguyên tắc hoạt động của công cụ rất đơn giản:

- Nó so sánh cơ sở dữ liệu địa phương và từ xa
- Nếu có bất kỳ sự khác biệt nào, nó kiểm tra dấu thời gian của đối tượng giống hệt cuối cùng, hãy gọi nó là **t**
- Nếu một đối tượng thay đổi gần đây hơn **t** tồn tại trong một cơ sở dữ liệu nhưng không tồn tại trong cơ sở dữ liệu kia, nó sẽ được đồng bộ hóa đến cả hai (giả sử là đối tượng mới)
- Nếu một đối tượng đã thay đổi lần cuối trước **t** không có trong một cơ sở dữ liệu, nó sẽ bị xóa trong cả hai (giả sử là đối tượng đã bị xóa)
- Nếu một đối tượng khác nhau nhưng chỉ thay đổi sau **t** trong một cơ sở dữ liệu, đồng bộ đến cơ sở dữ liệu kia (giả sử là đối tượng đã chỉnh sửa)
- Nếu một đối tượng khác nhau nhưng thay đổi sau **t** trong cả hai cơ sở dữ liệu, hợp nhất chúng (giả sử là sửa đổi xung đột)

Thời gian của lần đồng bộ thành công cuối cùng cũng được ghi lại, riêng biệt cho mỗi máy chủ, và được sử dụng làm **t** khi nó gần đây hơn đối tượng giống hệt mới nhất.

Thuật toán này đơn giản và mạnh mẽ vì nó không yêu cầu theo dõi lịch sử đồng bộ. Tuy nhiên, nó hoạt động tốt nhất khi bạn *đồng bộ thường xuyên*.
