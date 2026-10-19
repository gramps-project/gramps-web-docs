# Sử dụng Trợ lý AI

!!! info
    Trợ lý AI yêu cầu Gramps Web API phiên bản 2.5.0 hoặc cao hơn và Gramps Web phiên bản 24.10.0 hoặc cao hơn. Gramps Web API phiên bản 3.6.0 đã giới thiệu khả năng gọi công cụ để tương tác thông minh hơn.

Chế độ **Trợ lý** trong Gramps Web (nếu có trong cài đặt của bạn, được gán nhãn "Chat" trong các phiên bản cũ hơn) cung cấp quyền truy cập vào một trợ lý AI có thể trả lời các câu hỏi về cây gia đình của bạn.

!!! warning
    Vì đây vẫn là một tính năng mới và đang phát triển, một số loại câu hỏi hoạt động tốt trong khi những loại khác thì không. Ngoài ra, như với bất kỳ trợ lý AI nào, nó có thể đưa ra câu trả lời không chính xác về mặt thực tế, vì vậy hãy luôn kiểm tra lại.

## Cách hoạt động

Để hiểu loại câu hỏi nào mà trợ lý có thể trả lời, điều quan trọng là hiểu cách nó hoạt động bên trong:

1. Người dùng đặt câu hỏi.
2. Trợ lý truy vấn cơ sở dữ liệu của bạn trực tiếp bằng cách sử dụng các công cụ chuyên dụng: nó tìm kiếm cây với [tìm kiếm toàn văn](search.md), lọc người/dự kiện/gia đình/nơi chốn theo các tiêu chí cụ thể, tính toán mối quan hệ giữa các cá nhân và tra cứu các hồ sơ hoàn chỉnh, bao gồm cả ghi chú của chúng.
3. Một mô hình ngôn ngữ lớn hình thành câu trả lời dựa trên các hồ sơ mà nó đã tìm thấy.
4. Câu trả lời được hiển thị cho bạn, với các liên kết đến các hồ sơ mà nó dựa vào.

Trên các máy chủ chạy Gramps Web API phiên bản cũ hơn 3.24, trợ lý cũng dựa vào tìm kiếm ngữ nghĩa, tính năng này đang được loại bỏ.

Trong khi trợ lý đang làm việc, các chỉ báo cho thấy các công cụ mà nó đang sử dụng (ví dụ: tìm kiếm người, tra cứu mối quan hệ) để bạn có thể theo dõi khi nó xây dựng câu trả lời. Các câu hỏi kéo dài hơn được xử lý như các tác vụ nền – bạn có thể điều hướng đi và quay lại, và tiến trình cũng được phản ánh trong [Thông báo](notifications.md). Các câu trả lời được định dạng bằng Markdown (danh sách, nhấn mạnh, liên kết, v.v.) để dễ đọc hơn.

## Những gì bạn có thể hỏi

Với khả năng gọi công cụ được giới thiệu trong Gramps Web API phiên bản 3.6.0, trợ lý AI hiện có thể xử lý các câu hỏi phức tạp hơn:

- **Mối quan hệ gia đình**: "Ông bà của Jane Smith là ai?" hoặc "John Doe có quan hệ như thế nào với Mary Johnson?"
- **Tìm kiếm có lọc**: "Cho tôi xem tất cả những người sinh ra ở London sau năm 1850" hoặc "Những sự kiện nào đã xảy ra ở Paris?"
- **Câu hỏi dựa trên thời gian**: "Ai đã chết trước năm 1900?" hoặc "Liệt kê các cuộc hôn nhân đã diễn ra giữa năm 1920 và 1950"
- **Thông tin về địa điểm**: "Có những địa điểm nào ở Pháp?" hoặc "Hãy cho tôi biết về Nhà thờ St. Mary's"
- **Câu hỏi chung**: "Tên của các con của John Doe là gì?" hoặc "Mary Smith sinh khi nào?"

## Mẹo để đặt câu hỏi

Để có được kết quả tốt nhất từ trợ lý AI:

- **Cụ thể**: Hãy đặt câu hỏi của bạn với càng nhiều chi tiết càng tốt để tránh sự mơ hồ. Ví dụ, "Khi nào John Smith sinh năm 1850 ở Boston kết hôn?" thì tốt hơn là "Khi nào John Smith kết hôn?"
- **Sử dụng tên riêng**: Đề cập đến các tên, địa điểm và ngày tháng cụ thể khi có liên quan.
- **Hỏi một điều tại một thời điểm**: Phân chia các câu hỏi phức tạp thành các phần đơn giản hơn để có kết quả tốt hơn.
- **Sử dụng ngôn ngữ của bạn**: Các mô hình ngôn ngữ lớn là đa ngôn ngữ, vì vậy bạn có thể đặt câu hỏi bằng ngôn ngữ của mình và nhận câu trả lời bằng cùng một ngôn ngữ.

!!! tip
    Vui lòng chia sẻ trải nghiệm của bạn về những điều hoạt động và không hoạt động với cộng đồng.
