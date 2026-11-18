# Làm việc với các kết quả DNA

Các kết quả DNA là các đoạn DNA mà hai cá nhân có sự đồng nhất, được xác định bởi sự hiện diện của các dấu hiệu, được gọi là SNP (viết tắt của biến thể nucleotide đơn, phát âm là “snips”).

Để có được dữ liệu này, bạn cần truy cập vào một bài kiểm tra DNA đã được tải lên cơ sở dữ liệu đối sánh cho phép xem dữ liệu đối sánh đoạn DNA (ví dụ: MyHeritage, Gedmatch, FamilytreeDNA). Gramps Web không thực hiện việc đối sánh, vì nó chỉ có quyền truy cập vào dữ liệu mà bạn tải lên.

## Nhập dữ liệu đối sánh DNA

Để nhập dữ liệu đối sánh DNA, bạn cần [quyền chỉnh sửa](../install_setup/users.md) vì dữ liệu được lưu trữ dưới dạng ghi chú trong cơ sở dữ liệu Gramps. Chế độ xem DNA, có thể truy cập từ menu chính, cung cấp cách thuận tiện để nhập dữ liệu này theo định dạng đúng.

Để nhập một kết quả mới, nhấp vào nút + ở góc dưới bên phải. Trong hộp thoại mở ra, chọn hai cá nhân. Lưu ý rằng “Người đầu tiên” và “Người thứ hai” được xử lý khác nhau: kết quả được lưu trữ như một liên kết từ người đầu tiên đến người thứ hai. Chỉ người đầu tiên sẽ có thể được chọn cho chế độ xem đối sánh DNA và trình duyệt nhiễm sắc thể. Thông thường, người đầu tiên là người có bài kiểm tra DNA mà bạn có quyền truy cập và người thứ hai là một người họ hàng xa hơn.

Nếu người thứ hai không có trong cơ sở dữ liệu, bạn cần tạo nó trước bằng cách sử dụng nút “Tạo người” ở góc trên bên phải của giao diện người dùng. Khi bạn đã tạo người đó, bạn có thể quay lại chế độ xem đối sánh DNA và chọn người mới tạo.

Tiếp theo, dán dữ liệu thô vào trường văn bản. Dữ liệu nên là một bảng đối sánh được phân tách bằng dấu phẩy hoặc tab, thường chứa số nhiễm sắc thể, vị trí bắt đầu và kết thúc của đối sánh, số lượng SNP trong đối sánh và độ dài của đối sánh tính bằng đơn vị centimorgan (cM). Bạn cũng có thể kéo và thả một tệp chứa dữ liệu đối sánh vào trường văn bản.

Một ví dụ tối thiểu của một bảng như vậy là:

```csv
Chromosome,Start Location,End Location,Centimorgans,SNPs
6,6358001,18115715,19.6,7424
7,150135758,154205894,10.9,2816
```

Nếu định dạng hợp lệ, một bản xem trước sẽ được hiển thị bên dưới trường văn bản dưới dạng bảng.

Cuối cùng, nhấp vào nút “Lưu” để lưu kết quả vào cơ sở dữ liệu.

## Xem dữ liệu đối sánh DNA

Chế độ xem đối sánh DNA có một menu thả xuống cho phép chọn mỗi người trong cơ sở dữ liệu có một kết quả DNA liên quan. Khi một người được chọn, các kết quả của họ sẽ được liệt kê trong một bảng: tên của kết quả, mối quan hệ của họ với người được chọn, tổng độ dài DNA chia sẻ tính bằng centimorgan (cM), số lượng đoạn chia sẻ, và độ dài của đoạn lớn nhất trong số các đoạn này.

Đối với các kết quả đã được đặt trong cây, cột mối quan hệ hiển thị mối quan hệ được ghi lại trong cây (được xác định tự động từ cơ sở dữ liệu Gramps). Đối với các kết quả không có mối quan hệ với người được chọn trong cây, nó hiển thị mối quan hệ ước tính từ DNA chia sẻ, được đánh dấu bằng "≈".

Nhấp vào một kết quả mở trang của nó, với một tóm tắt về DNA chia sẻ, [ước tính mối quan hệ](#relationship-estimate), một biểu đồ về mối quan hệ trong cây, và danh sách các đoạn. Mỗi đoạn cho biết nó thuộc về bên cha hay bên mẹ. Bên có thể được nhập thủ công (bằng cách cung cấp một `P` cho bên cha hoặc `M` cho bên mẹ trong một cột có tên `Side` trong dữ liệu thô) hoặc được xác định tự động từ tổ tiên chung gần nhất. Nút tải xuống bên cạnh các đoạn lưu chúng dưới dạng tệp CSV theo định dạng mà hộp thoại đối sánh chấp nhận.

## Ước tính mối quan hệ

DNA chia sẻ không phải là bằng chứng của một mối quan hệ cụ thể: lượng DNA mà hai người họ hàng chia sẻ thay đổi rất nhiều, và các mối quan hệ khác nhau có thể chồng chéo lên nhau. Do đó, Gramps Web hiển thị một loạt các mối quan hệ có thể với xác suất của chúng, được tính toán từ số lượng và độ dài của các đoạn chia sẻ (cần Gramps Web API 3.26 hoặc mới hơn).

Các mối quan hệ được nhóm theo *bậc* của chúng:

- **Cha hoặc con** và **Anh chị em ruột** được hiển thị riêng.
- **Người họ hàng bậc 2** bao gồm anh chị em cùng cha mẹ, ông bà và cháu, và cô, dì, cháu trai và cháu gái.
- **Người họ hàng bậc 3** bao gồm anh chị em họ, cụ, cô dì chú bác, và cô dì chú bác cùng cha mẹ.
- Mỗi bậc tiếp theo cách nhau khoảng một thế hệ, ví dụ, anh chị em họ một lần loại bỏ là bậc 4 và anh chị em họ hai là bậc 5. Bậc 9 và cao hơn được nhóm lại thành "9+".

Các mối quan hệ có cùng bậc chia sẻ khoảng cùng một lượng DNA trung bình, vì vậy DNA một mình không thể phân biệt chúng. Sử dụng độ tuổi của những người để quyết định giữa chúng – một người họ hàng bậc 2 30 tuổi của một người 60 tuổi có khả năng là cháu gái hơn là ông bà.

Ước tính này đáng tin cậy nhất cho những người họ hàng gần. Đối với các mối quan hệ xa, các kết quả chỉ chia sẻ một vài đoạn, và xác suất phân tán qua nhiều bậc.

### Kiểm tra cây với DNA

Nếu kết quả được đặt trong cây, Gramps Web kiểm tra xem DNA chia sẻ có phù hợp với mối quan hệ được ghi lại ở đó không. Nếu DNA rất khó xảy ra cho mối quan hệ đó, một biểu tượng cảnh báo sẽ được hiển thị trong bảng kết quả và một cảnh báo trên trang kết quả. Số trong ngoặc, ví dụ "1 : 500", so sánh khả năng DNA cho mối quan hệ đã ghi với khả năng cho mối quan hệ có khả năng nhất.

Một cảnh báo là lý do để xem xét kỹ lưỡng hơn, không phải là bằng chứng của một lỗi. Các nguyên nhân phổ biến là:

- một sai sót trong cây, chẳng hạn như một bậc phụ sai,
- một mối quan hệ cha mẹ không rõ, ví dụ như một sự nhận nuôi không rõ hoặc một người cha sinh học khác,
- dữ liệu đối sánh không đầy đủ, chẳng hạn như nếu chỉ có các đoạn trên một ngưỡng cao được sao chép từ dịch vụ kiểm tra,
- các mối quan hệ qua nhiều dòng, ví dụ như những người có mối quan hệ qua cả mẹ và cha ("sụp đổ phả hệ"), chia sẻ nhiều DNA hơn mong đợi.

Các mối quan hệ không phải do sinh ra, chẳng hạn như qua một sự nhận nuôi, không được kiểm tra.

## Chỉnh sửa một kết quả

Để chỉnh sửa một kết quả, mở trang của nó và nhấp vào nút chỉnh sửa, hoặc nhấn `e`. Lưu ý rằng bạn có thể thay đổi dữ liệu thô, nhưng không thể thay đổi các cá nhân liên quan đến kết quả – bạn cần xóa kết quả và tạo một cái mới nếu bạn muốn thay đổi các cá nhân.

## Kết quả riêng tư

Các hộp thoại để thêm và chỉnh sửa một kết quả có một công tắc **Riêng tư**. Một kết quả riêng tư, bao gồm các đoạn của nó, bị ẩn khỏi những người không thể xem các hồ sơ riêng tư. Các kết quả riêng tư được đánh dấu bằng một ổ khóa cho mọi người khác. Xem [Hồ sơ riêng tư](privacy.md) để biết thêm về quyền riêng tư.

## Làm việc với dữ liệu đối sánh trong Gramps Desktop

Dữ liệu đối sánh DNA được lưu trữ dưới dạng ghi chú trong cơ sở dữ liệu Gramps. Định dạng này tương thích với 
[DNA Segment Map Addon](https://gramps-project.org/wiki/index.php/Addon:DNASegmentMapGramplet)
có sẵn cho Gramps Desktop. Trang wiki của nó chứa thêm thông tin về cách lấy dữ liệu, cách diễn giải nó, và cách nhập dữ liệu vào Gramps.

!!! info
    Gramps Web API v2.8.0 đã giới thiệu một số thay đổi để chấp nhận một loạt dữ liệu đối sánh DNA thô rộng hơn, điều này vẫn chưa có sẵn trong Gramps Desktop Addon. Gramps Desktop Addon sẽ được cập nhật trong tương lai để hỗ trợ các định dạng tương tự như vậy.
