# Sử dụng trò chuyện AI

!!! info
    Trò chuyện AI yêu cầu Gramps Web API phiên bản 2.5.0 hoặc cao hơn và Gramps Web phiên bản 24.10.0 hoặc cao hơn.

Chế độ xem trò chuyện trong Gramps Web (nếu có trong cài đặt của bạn) cung cấp quyền truy cập vào một trợ lý AI có thể trả lời các câu hỏi về cây gia đình của bạn.

!!! warning
    Vì đây vẫn là một tính năng mới và đang phát triển, một số loại câu hỏi hoạt động tốt trong khi những loại khác thì không. Ngoài ra, như với bất kỳ trợ lý AI nào, nó có thể đưa ra các câu trả lời không chính xác về mặt thực tế, vì vậy hãy luôn kiểm tra lại.

## Cách hoạt động

Để hiểu loại câu hỏi nào mà trợ lý có thể trả lời, điều quan trọng là hiểu cách nó hoạt động bên dưới:

1. Người dùng đặt câu hỏi.
2. Gramps Web xác định một số (ví dụ, mười) đối tượng Gramps có khả năng chứa thông tin trả lời câu hỏi. Để làm điều này, nó sử dụng một kỹ thuật gọi là "tìm kiếm ngữ nghĩa". Ví dụ, nếu bạn hỏi "Tên của con cái của John Doe là gì?", nếu có một gia đình tồn tại với John Doe là cha, nó có khả năng nằm trong số các kết quả hàng đầu.
3. Gramps Web cung cấp câu hỏi của người dùng cùng với thông tin ngữ cảnh đã thu thập cho một mô hình ngôn ngữ lớn ("chatbot") và yêu cầu nó trích xuất câu trả lời đúng.
4. Câu trả lời được hiển thị cho người dùng.

## Cách đặt câu hỏi

Do cách thức hoạt động của trò chuyện, hiện tại không thể cho trợ lý AI trả lời các câu hỏi về các mối quan hệ cụ thể khác ngoài cha mẹ hoặc con cái, trừ khi thông tin này được chứa dưới dạng văn bản trong một ghi chú.

Vì mỗi câu trả lời dựa trên một số lượng kết quả tìm kiếm ngữ nghĩa hàng đầu có giới hạn, nó cũng không thể trả lời các câu hỏi về thống kê ("có bao nhiêu người trong cơ sở dữ liệu của tôi ...").

Để tránh sự mơ hồ và hiểu lầm, điều hữu ích là diễn đạt câu hỏi một cách chi tiết nhất có thể.

Lưu ý rằng các mô hình ngôn ngữ lớn là đa ngôn ngữ, vì vậy bạn có thể nói chuyện với nó bằng ngôn ngữ của riêng bạn và nó sẽ trả lời bằng cùng một ngôn ngữ.

!!! tip
    Vui lòng chia sẻ kinh nghiệm của bạn về những điều hoạt động và không hoạt động với cộng đồng.
