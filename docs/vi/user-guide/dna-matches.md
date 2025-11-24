# Làm việc với các kết quả DNA

Các kết quả DNA là các đoạn DNA mà hai cá nhân có sự đồng nhất, được xác định bởi sự hiện diện của các dấu hiệu, gọi là SNP (viết tắt của biến thể nucleotide đơn, phát âm là “snips”).

Để có được dữ liệu này, bạn cần truy cập vào một bài kiểm tra DNA đã được tải lên cơ sở dữ liệu đối sánh cho phép xem dữ liệu đối sánh đoạn DNA (ví dụ: MyHeritage, Gedmatch, FamilytreeDNA). Gramps Web không thực hiện việc đối sánh mà chỉ có quyền truy cập vào dữ liệu bạn tải lên.

## Nhập dữ liệu đối sánh DNA

Để nhập dữ liệu đối sánh DNA, bạn cần [quyền chỉnh sửa](../install_setup/users.md) vì dữ liệu được lưu trữ dưới dạng ghi chú trong cơ sở dữ liệu Gramps. Chế độ xem DNA, có thể truy cập từ menu chính, cung cấp một cách thuận tiện để nhập dữ liệu này theo định dạng đúng.

Để nhập một kết quả mới, hãy nhấp vào nút + ở góc dưới bên phải. Trong hộp thoại mở ra, chọn hai cá nhân. Lưu ý rằng “Người đầu tiên” và “Người thứ hai” được xử lý khác nhau: kết quả được lưu trữ như một mối liên hệ từ người đầu tiên đến người thứ hai. Chỉ người đầu tiên sẽ được chọn cho chế độ xem đối sánh DNA và trình duyệt nhiễm sắc thể. Thông thường, người đầu tiên là người có bài kiểm tra DNA mà bạn có quyền truy cập và người thứ hai là một người họ hàng xa hơn.

Nếu người thứ hai không có trong cơ sở dữ liệu, bạn cần tạo nó trước bằng cách sử dụng nút “Tạo người” ở góc trên bên phải của giao diện người dùng. Khi bạn đã tạo người đó, bạn có thể quay lại chế độ xem đối sánh DNA và chọn người mới được tạo.

Tiếp theo, dán dữ liệu thô vào trường văn bản. Dữ liệu nên là một bảng đối sánh được phân tách bằng dấu phẩy hoặc tab, thường chứa số nhiễm sắc thể, vị trí bắt đầu và kết thúc của kết quả, số lượng SNP trong kết quả và độ dài của kết quả tính bằng centimorgans (cM). Bạn cũng có thể kéo và thả một tệp chứa dữ liệu đối sánh vào trường văn bản.

Một ví dụ tối thiểu của một bảng như vậy là:

```csv
Chromosome,Start Location,End Location,Centimorgans,SNPs
6,6358001,18115715,19.6,7424
7,150135758,154205894,10.9,2816
```

Nếu định dạng hợp lệ, một bản xem trước sẽ được hiển thị bên dưới trường văn bản dưới dạng bảng.

Cuối cùng, nhấp vào nút “Lưu” để lưu kết quả vào cơ sở dữ liệu.

## Xem dữ liệu đối sánh DNA

Chế độ xem đối sánh DNA có một menu thả xuống cho phép chọn từng người trong cơ sở dữ liệu có một kết quả DNA liên quan. Khi một người được chọn, dữ liệu đối sánh DNA sẽ được hiển thị trong một bảng bên dưới menu thả xuống. Nó hiển thị tên của người mà kết quả liên quan, mối quan hệ với người được chọn trong menu thả xuống (được xác định tự động từ cơ sở dữ liệu Gramps), tổng độ dài DNA chia sẻ tính bằng centimorgans (cM), số lượng đoạn chia sẻ, và độ dài của đoạn lớn nhất trong số các đoạn này.

Khi bạn nhấp vào một kết quả cá nhân, nó sẽ mở một trang chi tiết hiển thị tất cả các đoạn và liệu kết quả đó thuộc về bên mẹ hay bên cha. Thông tin này có thể được nhập thủ công (bằng cách cung cấp một `P` cho bên cha hoặc `M` cho bên mẹ trong một cột có tên `Side` trong dữ liệu thô) hoặc được Gramps xác định tự động dựa trên tổ tiên chung gần nhất.

## Chỉnh sửa một kết quả

Bạn có thể chỉnh sửa một kết quả bằng cách nhấp vào nút bút chì ở góc dưới bên phải trong chế độ xem chi tiết kết quả. Điều này mở ra một hộp thoại tương tự như khi tạo một kết quả mới, nhưng với dữ liệu đã được điền sẵn. Lưu ý rằng bạn có thể thay đổi dữ liệu thô, nhưng không thể thay đổi các cá nhân liên quan đến kết quả – bạn cần xóa kết quả và tạo một cái mới nếu bạn muốn thay đổi các cá nhân.

## Làm việc với dữ liệu đối sánh trong Gramps Desktop

Dữ liệu đối sánh DNA được lưu trữ dưới dạng ghi chú trong cơ sở dữ liệu Gramps. Định dạng này tương thích với 
[DNA Segment Map Addon](https://gramps-project.org/wiki/index.php/Addon:DNASegmentMapGramplet)
có sẵn cho Gramps Desktop. Trang wiki của nó chứa thêm chi tiết về cách lấy dữ liệu, cách diễn giải nó và cách nhập dữ liệu vào Gramps.

!!! info
    Gramps Web API v2.8.0 đã giới thiệu một số thay đổi để chấp nhận một loạt dữ liệu đối sánh DNA thô rộng hơn, điều này chưa có sẵn trong Gramps Desktop Addon. Gramps Desktop Addon sẽ được cập nhật trong tương lai để hỗ trợ các định dạng tương tự.
