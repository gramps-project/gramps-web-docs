# Sử dụng Trợ lý AI

Chế độ **Trợ lý** trong Gramps Web (nếu được kích hoạt trong cài đặt của bạn) cung cấp quyền truy cập vào một trợ lý AI có thể trả lời các câu hỏi về cây gia đình của bạn.

!!! warning
    Giống như bất kỳ trợ lý AI nào, các câu trả lời có thể sai. Sử dụng các liên kết trong câu trả lời để kiểm tra các hồ sơ mà nó dựa vào.

## Cách hoạt động

Trợ lý không biết cây của bạn trước. Để trả lời một câu hỏi, một mô hình ngôn ngữ lớn sẽ tìm kiếm các hồ sơ cần thiết, giống như bạn tự làm:

- nó tìm kiếm cây với [tìm kiếm toàn văn](search.md),
- nó lọc người, sự kiện và gia đình theo các tiêu chí như tên, ngày tháng, địa điểm hoặc số lượng trẻ em,
- nó tìm tổ tiên, con cháu và các họ hàng khác của một người, cùng với mối quan hệ của họ,
- nó đọc các hồ sơ đầy đủ của người, gia đình, sự kiện, địa điểm và ghi chú.

Sau đó, nó trả lời dựa trên các hồ sơ mà nó đã tìm thấy, kèm theo các liên kết đến chúng. Trong khi nó đang làm việc, các công cụ mà nó đang sử dụng sẽ được hiển thị, vì vậy bạn có thể theo dõi. Các câu hỏi mất nhiều thời gian hơn sẽ chạy ở chế độ nền – bạn có thể điều hướng đi và quay lại.

Trợ lý chỉ trả lời từ cây của bạn, không từ kiến thức chung của mô hình ngôn ngữ – ngay cả về những người nổi tiếng. Nếu cây không ghi lại điều gì đó, nó sẽ nói như vậy, đề cập đến thông tin liên quan mà nó đã tìm thấy, chẳng hạn như trong một ghi chú. Nó chỉ thấy những gì bạn được phép thấy: các liên kết đến hồ sơ riêng tư sẽ được hiển thị dưới dạng văn bản thuần cho những người không thể xem chúng.

Các câu hỏi tiếp theo giữ nguyên bối cảnh của các câu hỏi trước đó trong cùng một cuộc trò chuyện, vì vậy bạn có thể hỏi "Và khi nào ông ấy qua đời?" sau khi hỏi về một người.

## Những gì bạn có thể hỏi

- **Sự kiện về người**: "Mary Smith sinh khi nào?" hoặc "Tên của các con của John Doe là gì?"
- **Họ hàng**: "Ông bà của Jane Smith là ai?" hoặc "Những con cháu nào của Johann Meyer đã di cư đến Mỹ?"
- **Tìm kiếm theo tiêu chí**: "Ai sinh ra ở London sau năm 1850?", "Liệt kê các cuộc hôn nhân giữa năm 1920 và 1950", hoặc "Cặp đôi nào có năm hoặc nhiều trẻ em hơn?"
- **Địa điểm**: "Những sự kiện nào đã xảy ra ở Paris?" hoặc "Ai sinh ra ở Đan Mạch?" – các địa điểm nằm trong một địa điểm lớn hơn cũng được bao gồm.
- **Ghi chú**: "Ghi chú nói gì về trang trại của gia đình Meyer?"

Các câu hỏi cần toàn bộ cây một lần, chẳng hạn như "Tên đầu tiên phổ biến nhất là gì?", hoạt động kém hơn, vì trợ lý chỉ thấy một số lượng hồ sơ hạn chế mỗi lần tìm kiếm.

## Hỏi về hình ảnh

Nếu quản trị viên máy chủ đã kích hoạt, nhắc nhở sẽ có một nút để đính kèm hình ảnh. Bạn cũng có thể dán một hình ảnh hoặc thả các tệp hình ảnh vào nhắc nhở. Tối đa bốn hình ảnh có thể được đính kèm vào một câu hỏi, chẳng hạn như một bản quét của một hồ sơ nhà thờ để hỏi "Ai được đề cập trong mục này, và họ có trong cây của tôi không?"

Các hình ảnh chỉ được gửi cùng với câu hỏi mà chúng được đính kèm. Các câu hỏi tiếp theo có thể tham khảo những gì trợ lý đã nói về chúng, nhưng không thể tham chiếu đến chính các hình ảnh, vì vậy hãy đính kèm chúng lại nếu cần. Nếu cây của bạn có giới hạn về việc sử dụng AI, mỗi hình ảnh sẽ được tính như một câu hỏi bổ sung.

## Cho phép trợ lý thay đổi cây của bạn

Nếu quản trị viên máy chủ đã kích hoạt, các biên tập viên, chủ sở hữu và quản trị viên có thể yêu cầu trợ lý thay đổi cây, chẳng hạn như "Thêm một lễ rửa tội vào ngày 3 tháng 5 năm 1802 tại St. Mary's cho Johann Meyer" hoặc "Sửa năm sinh của Anna Smith, nó nên là 1871".

Trợ lý không bao giờ tự thay đổi bất cứ điều gì. Nó trả lời bằng một thẻ **Thay đổi đề xuất** liệt kê mọi hồ sơ mà nó sẽ thêm, chỉnh sửa hoặc xóa, với các giá trị cũ bị gạch chéo và các giá trị mới được làm nổi bật. Không có gì xảy ra cho đến khi bạn nhấp vào **Áp dụng**. Các thay đổi sau đó sẽ được thực hiện trong một bước, mà bạn có thể hoàn tác như bất kỳ chỉnh sửa nào khác, từ thông điệp xuất hiện hoặc trong [lịch sử sửa đổi](revisions.md).

Kiểm tra một đề xuất cẩn thận trước khi áp dụng – đặc biệt là đảm bảo rằng trợ lý đã chọn đúng người, và rằng nó không thêm một hồ sơ mới (chẳng hạn như một địa điểm hoặc nguồn) đã tồn tại trong cây của bạn dưới một tên hơi khác. Nếu một đề xuất không hoàn toàn đúng, hãy nói rõ điều gì cần thay đổi, và trợ lý sẽ đề xuất lại.

Khi một đề xuất đã được áp dụng, các đề xuất cũ hơn trong cùng một cuộc trò chuyện không còn có thể được áp dụng, vì chúng đã được thực hiện cho cây như nó đã trước đó. Điều tương tự cũng xảy ra nếu một trong các hồ sơ bị ảnh hưởng đã được thay đổi trong thời gian đó.

## Mẹo để đặt câu hỏi

- **Gọi tên người.** Trợ lý không biết bạn là ai hoặc người nhà của bạn là ai, vì vậy thay vì "bà ngoại của tôi", hãy hỏi về "bà ngoại của Anna Smith (sinh năm 1950)". Bạn cũng có thể sử dụng ID Gramps, ví dụ "các con của I0042".
- **Cụ thể** khi tên phổ biến: "Khi nào John Smith sinh năm 1850 ở Boston kết hôn?" thì tốt hơn là "Khi nào John Smith kết hôn?"
- **Sử dụng ngôn ngữ của bạn.** Bạn có thể hỏi bằng ngôn ngữ của mình và nhận câu trả lời bằng cùng một ngôn ngữ.
- **Hỏi lại theo cách khác** nếu một câu trả lời có vẻ không đầy đủ – chẳng hạn bằng cách nêu tên địa điểm hoặc thời gian mà bạn quan tâm.

!!! tip
    Vui lòng chia sẻ kinh nghiệm của bạn về những điều hoạt động và không hoạt động với cộng đồng.
