# Sử dụng Gramps Web để phân tích Y-DNA

!!! note "Lưu ý"
    Tính năng này yêu cầu Gramps Web API phiên bản 3.3.0 trở lên và phiên bản giao diện Gramps Web 25.9.0 trở lên.

Chế độ xem Y-DNA trong Gramps Web có thể sử dụng dữ liệu SNP đơn nucleotide (SNP) trên nhiễm sắc thể Y thô để xác định nhóm haplogroup Y-DNA có khả năng nhất của một người và hiển thị tổ tiên đã được suy diễn trong cây nhiễm sắc thể Y của con người cùng với ước lượng thời gian.

## Cách thu thập và lưu trữ dữ liệu SNP Y-DNA

Để thu thập dữ liệu SNP Y-DNA, bạn cần thực hiện một bài kiểm tra Y-DNA thông qua một dịch vụ xét nghiệm di truyền. Kết quả được biểu diễn dưới dạng một tập hợp các đột biến (SNP), mỗi đột biến được xác định bằng một chuỗi (ví dụ: `R-BY44535`) và một dấu `+` hoặc `-` cho biết liệu đột biến đó có mặt hay không. Gramps Web mong đợi chuỗi của tất cả các SNP đã được kiểm tra theo định dạng `SNP1+, SNP2-, SNP3+,...` được lưu trữ trong thuộc tính của người có kiểu tùy chỉnh `Y-DNA` (phân biệt chữ hoa chữ thường). Bạn có thể tạo thuộc tính này thủ công trong Gramps Web hoặc Gramps Desktop, hoặc điều hướng đến chế độ xem Y-DNA trong Gramps Web và nhấp vào nút "Thêm" màu xanh, chọn người để thêm dữ liệu vào, và dán chuỗi SNP. Trong mọi trường hợp, dữ liệu sẽ được lưu trữ dưới dạng thuộc tính của người trong cơ sở dữ liệu Gramps của bạn.

[Xem bên dưới](#instructions-for-obtaining-snp-data-from-testing-services) để biết hướng dẫn cách thu thập dữ liệu SNP từ các dịch vụ xét nghiệm khác nhau.

## Cách thức hoạt động

Khi một người có thuộc tính `Y-DNA` chứa dữ liệu SNP, Gramps Web sẽ sử dụng thư viện Python mã nguồn mở [yclade](https://github.com/DavidMStraub/yclade) để xác định vị trí có khả năng nhất của người đó trên cây nhiễm sắc thể Y của con người. Cây này đã được tạo ra bởi dự án [YFull](https://www.yfull.com/) dựa trên hàng chục nghìn bài kiểm tra Y-DNA. Lưu ý rằng Gramps Web sử dụng một bản sao cục bộ của cây YFull, vì vậy không có dữ liệu nào được gửi đến bên thứ ba.

Cây được duyệt từ gốc đến lá, và tại mỗi nút, các SNP liên quan đến nút đó được so sánh với các SNP đã được kiểm tra dương tính và âm tính của người đó, và nhánh phù hợp được theo dõi.

Kết quả cuối cùng là một chuỗi các nhánh từ gốc của cây (theo [Adam nhiễm sắc thể Y](https://en.wikipedia.org/wiki/Y-chromosomal_Adam)) đến nhánh có nguồn gốc nhất phù hợp với dữ liệu SNP của người đó. Mỗi nhánh có một độ tuổi ước tính dựa trên độ tuổi của các mẫu trong cơ sở dữ liệu YFull thuộc về nhánh đó.

Vì nhiễm sắc thể Y được di truyền từ cha sang con trai, chuỗi này tương ứng với một đoạn của tổ tiên theo dòng cha của người đó.

## Cách diễn giải kết quả

Thông tin quan trọng nhất là nhóm haplogroup có khả năng nhất của người đó, được hiển thị ở đầu trang. Tên này được liên kết với trang tương ứng trên trang web [YFull](https://www.yfull.com/), nơi chứa thêm thông tin, chẳng hạn như quốc gia xuất xứ của các mẫu đã được kiểm tra thuộc về nhóm haplogroup đó.

Trong cây tổ tiên theo dòng cha được hiển thị trong Gramps Web, ô ngay phía trên người đã được kiểm tra là tổ tiên chung gần nhất (MRCA) của tất cả các mẫu đã được kiểm tra thuộc về nhóm haplogroup của người đó. Ngày được hiển thị cho tổ tiên này là ngày sinh ước tính của ông. Tổ tiên phía trên ông là tổ tiên nơi đột biến xác định nhóm haplogroup này lần đầu tiên xuất hiện.

Do tỷ lệ đột biến chậm của nhiễm sắc thể Y, MRCA có thể là hàng trăm năm trước. Đối với các nhóm haplogroup hiếm (tức là các nhóm haplogroup mà ít người đã được kiểm tra cho đến nay), nó thậm chí có thể là hàng ngàn năm.

Giữa MRCA và người đã được kiểm tra, biểu đồ hiển thị dòng cha cho đến mức được tài liệu hóa trong cây của bạn: cha, ông của ông, và cứ thế, từ người lớn tuổi nhất trở đi. Đường chấm trên tổ tiên đã được tài liệu hóa lớn tuổi nhất đại diện cho các thế hệ không được tài liệu hóa, với ước tính số lượng của chúng. Chỉ có cha sinh học mới được theo dõi – dòng dừng lại ở cha nuôi hoặc cha kế, vì họ không truyền lại nhiễm sắc thể Y. Nhấp vào một người trong dòng để mở trang của họ.

Biểu tượng trên mỗi ô nhánh mở nhánh đó trên trang web YFull.

## Dữ liệu Y-DNA riêng tư

Các hộp thoại để thêm và chỉnh sửa dữ liệu Y-DNA có công tắc **Riêng tư**. Dữ liệu Y-DNA riêng tư bị ẩn khỏi những người không thể xem hồ sơ riêng tư. Xem [Hồ sơ riêng tư](privacy.md).

## Hướng dẫn thu thập dữ liệu SNP từ các dịch vụ xét nghiệm

### [YSEQ](https://www.yseq.net/)

Sau khi đăng nhập vào "Tài khoản của tôi", hãy đi đến "Kết quả của tôi / Xem các Allele của tôi" và điều hướng đến cuối trang. Trường văn bản "Danh sách Allele gọn" đã được thêm vào đặc biệt cho Gramps Web và ở đúng định dạng để dán vào thuộc tính `Y-DNA`.
