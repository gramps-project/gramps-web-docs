# Đồng bộ hóa Gramps Web và Gramps Desktop

*Gramps Web Sync* là một addon cho Gramps giúp đồng bộ hóa cơ sở dữ liệu Gramps trên máy tính để bàn của bạn với Gramps Web, bao gồm cả các tệp phương tiện. Những thay đổi được thực hiện ở bất kỳ bên nào sẽ được chuyển sang bên kia, vì vậy bạn có thể làm việc cả ở chế độ cục bộ và trên web với cùng một cây gia đình.

Giống như bất kỳ công cụ đồng bộ hóa nào, đây không phải là một bản sao lưu: nếu bạn xóa một cái gì đó ở một bên, nó cũng sẽ bị xóa ở bên kia. Hãy giữ bản sao lưu thường xuyên cho cây gia đình của bạn ở định dạng Gramps XML.

## Cài đặt

Addon yêu cầu Gramps 6.0 chạy trên Python 3.10 hoặc phiên bản mới hơn. Nó có sẵn trong Gramps Desktop và có thể được cài đặt [theo cách thông thường](https://www.gramps-project.org/wiki/index.php/5.2_Addons#Installing_Addons_in_Gramps). Tài liệu này mô tả phiên bản mới nhất của addon; hãy sử dụng trình quản lý addon Gramps để cập nhật nếu cần.

Máy tính để bàn của bạn và máy chủ của bạn phải chạy cùng một phiên bản Gramps. Phiên bản có dạng `MAJOR.MINOR.PATCH`, và `MAJOR` và `MINOR` phải khớp nhau. Xem [Nhận trợ giúp](../help/help.md) để biết cách tìm ra phiên bản Gramps mà máy chủ của bạn đang chạy.

### Yêu cầu máy chủ

Addon kiểm tra hai điều về máy chủ của bạn ngay khi nó kết nối, trước khi bất kỳ điều gì được tải xuống, và dừng lại với một thông báo nếu bất kỳ điều nào không được đáp ứng:

- **Phiên bản Gramps Web API 3.x.** Phiên bản này của addon, dành cho Gramps 6.0, hoạt động với Gramps Web API 3. Một máy chủ cũ cần được cập nhật; một máy chủ chạy phiên bản API chính *mới hơn* cần một phiên bản Gramps mới hơn, không phải một addon mới hơn, vì mỗi dòng phát hành Gramps được ghép cặp với một phiên bản API. Bạn có thể tìm phiên bản của máy chủ của mình dưới *Cài đặt ▸ Thông tin phiên bản* trong Gramps Web.
- **Một hàng đợi tác vụ nền.** Các thay đổi được áp dụng trên máy chủ như một tác vụ nền. Nếu không có hàng đợi tác vụ, điều này sẽ chạy đồng bộ và hết thời gian trên bất kỳ cây gia đình thực nào.

Để áp dụng các thay đổi vào cơ sở dữ liệu từ xa, bạn cần một tài khoản với vai trò biên tập viên, chủ sở hữu hoặc quản trị viên.

### Lưu mật khẩu của bạn (tùy chọn)

Cài đặt `keyring` (ví dụ: `sudo apt install python3-keyring` hoặc `sudo dnf install python3-keyring`) để lưu mật khẩu API trong trình quản lý mật khẩu của hệ thống bạn. Nếu không thể sử dụng keyring, addon sẽ thông báo và tiếp tục mà không có nó – bạn sẽ đơn giản được yêu cầu nhập mật khẩu mỗi lần.

Trên gói **Snap** của Gramps, keyring hệ thống bị chặn bởi confinement cho đến khi bạn kết nối giao diện một lần. Addon hiển thị lệnh này khi nó phát hiện tình huống:

```bash
snap connect gramps:password-manager-service
```

Trên nhiều cấu hình desktop Gnome, một [lỗi trong python keyring](https://github.com/jaraco/keyring/issues/496) có nghĩa là bạn phải tạo tệp cấu hình `~/.config/python_keyring/keyringrc.cfg` với nội dung sau:

```ini
[backend]
default-keyring=keyring.backends.SecretService.Keyring
```

## Sử dụng

Addon có sẵn trong Gramps dưới *Công cụ ▸ Xử lý Cây Gia Đình ▸ Gramps&nbsp;Web&nbsp;Sync*. Sau khi xác nhận hộp thoại cảnh báo rằng lịch sử hoàn tác sẽ bị bỏ qua, cửa sổ đồng bộ hóa sẽ mở. Không có thay đổi nào được áp dụng cho cây cục bộ của bạn hoặc cho máy chủ cho đến khi bạn xác nhận chúng một cách rõ ràng.

Một dải ở phía trên của cửa sổ cho biết tên cây gia đình mà bạn đang đồng bộ hóa, tài khoản và địa chỉ mà nó thuộc về, và khi nào nó được đồng bộ hóa lần cuối. Ở dưới cùng, phiên bản của addon và của Web API của máy chủ được hiển thị, điều này hữu ích khi báo cáo một vấn đề.

### Kết nối

Nếu bạn đã đồng bộ hóa cây gia đình này trước đó và mật khẩu của bạn đã được lưu, addon sẽ kết nối ngay khi nó mở và đi thẳng đến so sánh. Nếu không, nó sẽ yêu cầu URL cơ sở của phiên bản Gramps Web của bạn (ví dụ: `https://mygrampsweb.com/`), tên người dùng của bạn và mật khẩu của bạn.

URL và tên người dùng được lưu dưới dạng văn bản thuần túy trong thư mục người dùng Gramps của bạn. Mật khẩu chỉ được lưu trong trình quản lý mật khẩu của hệ thống nếu bạn để **Nhớ mật khẩu** được đánh dấu; bỏ đánh dấu nó sẽ xóa bất kỳ mật khẩu nào đã được lưu cho máy chủ đó. Nếu bạn nhập một địa chỉ bắt đầu bằng `http://` thay vì `https://`, addon sẽ cảnh báo bạn khi bạn gõ, vì mật khẩu của bạn sẽ được gửi dưới dạng văn bản rõ ràng.

Mỗi máy chủ mà bạn đồng bộ hóa được lưu riêng biệt, cùng với bản ghi của riêng nó về khi nó được đồng bộ hóa lần cuối, vì vậy bạn có thể chuyển đổi giữa hai máy chủ mà không làm gián đoạn bất kỳ máy chủ nào. Mỗi mục cũng ghi lại cây gia đình cục bộ nào mà nó đã được đồng bộ hóa lần cuối. Addon chỉ kết nối tự động khi điều đó khớp với cây mà bạn đang mở; nếu không, nó sẽ hiển thị chi tiết kết nối và chờ bạn nhấn *Kết nối*.

Hai hành động có sẵn trong khi không có gì được ghi:

- **Thay đổi máy chủ…**, trên dải trên cùng, quay lại chi tiết kết nối để bạn có thể chỉ định cây này đến một máy chủ khác. Nó sẽ ngắt quãng một so sánh đang diễn ra thay vì khiến bạn phải chờ nó hoàn thành.
- **Quên máy chủ này**, trên bảng kết nối, xóa địa chỉ, tên người dùng và mật khẩu đã lưu, cùng với bản ghi về khi cây này được đồng bộ hóa lần cuối. Đồng bộ hóa tiếp theo sẽ so sánh hai cây từ đầu.

### Xem xét các thay đổi

Addon so sánh cơ sở dữ liệu cục bộ và từ xa và hiển thị các hành động mà nó đề xuất thực hiện, được nhóm theo cơ sở dữ liệu nào mà chúng thay đổi:

```
▾ Sẽ thay đổi trên máy tính này (7 đối tượng)
    ▾ Thêm 3 đối tượng
        Người   John Smith        I0123
    ▾ Cập nhật 4 đối tượng
        …
▾ Sẽ thay đổi trên máy chủ (5 đối tượng)
    …
```

Mỗi hàng tên đối tượng, vì vậy bạn có thể biết ai hoặc cái gì bị ảnh hưởng thay vì chỉ thấy một ID Gramps. Nếu bất kỳ điều gì sẽ bị xóa, một ghi chú ở trên cùng danh sách cho biết có bao nhiêu đối tượng và ở bên nào.

Nhấn **Áp dụng** để thực hiện những gì danh sách mô tả.

Cửa sổ đồng bộ hóa không chặn phần còn lại của Gramps, vì vậy bạn có thể tiếp tục làm việc trong khi danh sách đang mở. Nếu bạn chỉnh sửa một đối tượng bị ảnh hưởng trong thời gian đó, addon sẽ nhận thấy khi bạn nhấn Áp dụng, dừng lại mà không thay đổi gì và yêu cầu bạn so sánh lại.

#### Chế độ đồng bộ hóa

Chế độ đồng bộ hóa được chọn ở trên danh sách các thay đổi. Thay đổi nó sẽ xây dựng lại danh sách, vì chế độ quyết định mỗi sự khác biệt trở thành gì.

- **Đồng bộ hóa hai chiều** (mặc định) – các thay đổi từ cả hai bên được kết hợp. Các đối tượng được chỉnh sửa ở cả hai nơi sẽ được hợp nhất.
- **Đặt lại máy chủ để khớp với máy tính này** – máy chủ sẽ được làm cho khớp với máy tính này. Bất kỳ điều gì chỉ thay đổi trên máy chủ sẽ bị bỏ qua.
- **Đặt lại máy tính này để khớp với máy chủ** – máy tính này sẽ được làm cho khớp với máy chủ. Bất kỳ điều gì chỉ thay đổi ở đây sẽ bị bỏ qua.

Chế độ **hợp nhất** có sẵn trong các phiên bản trước 1.5 đã bị xóa. Nó khác với đồng bộ hóa hai chiều chỉ ở việc khôi phục các đối tượng bị xóa ở một bên thay vì phát tán việc xóa. Nếu bạn đã dựa vào nó, hãy sử dụng đồng bộ hóa hai chiều và khôi phục bất kỳ điều gì bạn muốn giữ từ một bản sao lưu.

### Tệp phương tiện

Các tệp phương tiện được xử lý như một phần của cùng một xác nhận, không phải là một bước riêng biệt. Nếu bất kỳ tệp nào cần chuyển, một hộp kiểm bên dưới danh sách đề nghị di chuyển chúng:

```
[x] Cũng chuyển 12 tệp phương tiện (4 để tải xuống, 8 để tải lên)
```

Bỏ chọn nó để đồng bộ hóa các thay đổi đối tượng mà không chạm vào các tệp.

Các tệp bị thiếu ở *cả hai* bên được liệt kê riêng biệt, vì không thể làm gì về chúng:

```
2 tệp phương tiện bị thiếu ở cả hai bên và không thể được chuyển.
```

Việc đồng bộ hóa tệp phương tiện có hai hạn chế:

- Nếu một tệp cục bộ có một checksum khác với tệp được lưu trong cơ sở dữ liệu Gramps (điều này có thể xảy ra ví dụ như đối với các tệp Word được chỉnh sửa sau khi được thêm vào Gramps), việc tải lên sẽ thất bại với một thông báo lỗi.
- Công cụ không xác minh tính toàn vẹn của tất cả các tệp cục bộ. Nếu một tệp tồn tại dưới đường dẫn được lưu cho đối tượng phương tiện nhưng khác với tệp trên máy chủ, công cụ sẽ không phát hiện ra điều đó. Sử dụng Addon Xác minh Phương tiện để tìm các tệp có checksum không chính xác.

### Nếu một lần đồng bộ hóa thất bại

Nếu một lần đồng bộ hóa thất bại giữa chừng – chẳng hạn như một kết nối bị mất – addon sẽ báo cáo những gì nó đã áp dụng và cung cấp **Thử lại**, điều này sẽ tiếp tục từ bước đã thất bại thay vì bắt đầu lại. Bản sao tải xuống của cây từ xa sẽ được giữ lại, vì vậy việc thử lại sẽ không tải xuống và so sánh nó lần thứ hai.

Chi tiết kỹ thuật của sự cố có sẵn trong một phần mở rộng *Chi tiết*, với một nút để sao chép chúng cho một báo cáo lỗi.

## Khắc phục sự cố

**Những thay đổi bất ngờ.** Nếu addon đề xuất một số lượng lớn các xóa đáng báo động, hãy kiểm tra dải trên cùng trước: nó cho biết cây gia đình trên máy chủ mà bạn sắp ghi vào. Đồng bộ hóa một cây với một máy chủ chứa một cây *khác* sẽ tạo ra chính triệu chứng này.

Nếu không, những sự khác biệt mà bạn không mong đợi có thể đến từ sự không nhất quán trong một trong các cơ sở dữ liệu, hoặc từ đồng hồ không đồng bộ giữa máy tính của bạn và máy chủ của bạn. Kiểm tra xem cả hai đồng hồ có được đặt đúng không (múi giờ không quan trọng, vì công cụ sử dụng dấu thời gian Unix) và chạy công cụ kiểm tra & sửa chữa trên cơ sở dữ liệu cục bộ của bạn. Như một biện pháp cuối cùng, xuất cơ sở dữ liệu cục bộ của bạn sang Gramps XML và nhập lại vào một cơ sở dữ liệu mới, trống. Đây là một thao tác không mất dữ liệu, nhưng đảm bảo tất cả dữ liệu được lưu trữ một cách nhất quán.

**Lỗi tệp phương tiện.** Một lần tải lên thất bại thường do sự không khớp giữa checksum của tệp trên đĩa và checksum trong cơ sở dữ liệu Gramps cục bộ, điều này xảy ra với các tệp có thể chỉnh sửa như tài liệu văn phòng được chỉnh sửa bên ngoài Gramps. Sử dụng Addon Xác minh Phương tiện của Gramps để sửa chữa các checksum.

**Lỗi quyền.** Kiểm tra vai trò của tài khoản người dùng Gramps Web của bạn: chỉ có biên tập viên, chủ sở hữu và quản trị viên mới có thể áp dụng các thay đổi vào cơ sở dữ liệu từ xa.

### Yêu cầu trợ giúp

Nếu không có gì ở trên giúp ích, hãy hỏi cộng đồng bằng cách đăng bài trong [danh mục Gramps Web của diễn đàn Gramps](https://gramps.discourse.group/c/gramps-web/28). Vui lòng cung cấp:

- phiên bản của addon Gramps Web Sync, được hiển thị ở dưới cùng của cửa sổ đồng bộ hóa bên cạnh phiên bản Web API của máy chủ (và vui lòng sử dụng phiên bản phát hành mới nhất)
- phiên bản Gramps desktop mà bạn đang sử dụng
- thông tin phiên bản của Gramps Web, tìm thấy dưới *Cài đặt ▸ Thông tin phiên bản*
- bất kỳ chi tiết nào về cài đặt Gramps Web của bạn (tự lưu trữ, Grampshub, ...)
- đầu ra của nhật ký máy chủ Gramps Web của bạn, nếu bạn có quyền truy cập vào chúng (khi sử dụng Docker: `docker compose logs --tail 100 grampsweb` và `docker compose logs --tail 100 grampsweb-celery`)

Nếu bạn được yêu cầu cung cấp nhật ký gỡ lỗi, hãy khởi động Gramps [từ dòng lệnh](https://gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Command_Line) với ghi nhật ký gỡ lỗi được bật và tái tạo vấn đề:

```bash
gramps --debug grampswebsync
```

## Bối cảnh: cách addon hoạt động

Addon được thiết kế để giữ cho cơ sở dữ liệu Gramps cục bộ đồng bộ với cơ sở dữ liệu Gramps Web từ xa, cho phép cả thay đổi cục bộ và từ xa (chỉnh sửa hợp tác).

Nó **không phù hợp**

- để đồng bộ hóa với một cơ sở dữ liệu không phải là một biến thể trực tiếp (bắt đầu từ một bản sao cơ sở dữ liệu hoặc xuất/nhập Gramps XML) của cơ sở dữ liệu cục bộ,
- để hợp nhất hai cơ sở dữ liệu với một số lượng lớn các thay đổi ở cả hai bên cần sự chú ý thủ công để hợp nhất. Sử dụng [Công cụ Nhập Hợp Nhất](https://www.gramps-project.org/wiki/index.php/Import_Merge_Tool) tuyệt vời cho mục đích này.

Các nguyên tắc hoạt động rất đơn giản:

- Nó so sánh cơ sở dữ liệu cục bộ và từ xa.
- Nếu có bất kỳ sự khác biệt nào, nó kiểm tra dấu thời gian của đối tượng giống hệt cuối cùng, hãy gọi nó là **t**.
- Nếu một đối tượng thay đổi gần đây hơn **t** tồn tại trong một cơ sở dữ liệu nhưng không có trong cơ sở dữ liệu kia, nó sẽ được đồng bộ hóa đến cả hai (giả sử là đối tượng mới).
- Nếu một đối tượng thay đổi lần cuối trước **t** vắng mặt trong một cơ sở dữ liệu, nó sẽ bị xóa trong cả hai (giả sử là đối tượng đã bị xóa).
- Nếu một đối tượng khác nhau nhưng chỉ thay đổi sau **t** trong một cơ sở dữ liệu, hãy đồng bộ hóa nó với cơ sở dữ liệu kia (giả sử là đối tượng đã chỉnh sửa).
- Nếu một đối tượng khác nhau nhưng thay đổi sau **t** trong cả hai cơ sở dữ liệu, hãy hợp nhất chúng (giả sử là sửa đổi xung đột).

Thời gian của lần đồng bộ hóa thành công cuối cùng cũng được ghi lại, riêng biệt cho mỗi máy chủ, và được sử dụng làm **t** khi nó gần đây hơn đối tượng giống hệt mới nhất.

Thuật toán này đơn giản và mạnh mẽ vì nó không yêu cầu theo dõi lịch sử đồng bộ hóa. Tuy nhiên, nó hoạt động tốt nhất khi bạn *đồng bộ hóa thường xuyên*.
