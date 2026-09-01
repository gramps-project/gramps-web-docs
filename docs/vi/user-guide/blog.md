# Sử dụng blog tích hợp sẵn

Blog được thiết kế để trình bày các câu chuyện về nghiên cứu lịch sử gia đình của bạn.

Trong cơ sở dữ liệu Gramps, các bài viết trên blog được đại diện dưới dạng nguồn với một ghi chú đính kèm, chứa văn bản của blog và tùy chọn, các tệp phương tiện cho hình ảnh của bài viết trên blog. Gramps Web coi mọi nguồn có thẻ `Blog` là bài viết trên blog.

## Thêm một bài viết trên blog

Cách nhanh nhất để viết một bài viết là sử dụng biểu mẫu **Bài viết Blog Mới** trong Gramps Web. Mở nó từ nút **+** màu xanh trên trang Blog, hoặc từ menu **Thêm** (biểu tượng dấu cộng) trên thanh ứng dụng ở trên cùng bằng cách chọn **Bài viết Blog**.

Biểu mẫu có các trường cho:

- **Tiêu đề** – tiêu đề của bài viết (bắt buộc)
- **Tác giả** – người đã viết
- **Nội dung** – một trình soạn thảo văn bản phong phú cho chính bài viết
- **Phương tiện** – một hoặc nhiều đối tượng phương tiện. Tệp đầu tiên sẽ trở thành hình ảnh xem trước hiển thị trên văn bản; tất cả chúng sẽ xuất hiện dưới dạng một bộ sưu tập bên dưới.
- **Thẻ** và một công tắc **riêng tư**, như đối với bất kỳ đối tượng nào khác

Lưu biểu mẫu sẽ tạo ra nguồn cơ bản, ghi chú và thẻ `Blog` cho bạn, như đã mô tả [dưới đây](#relation-between-blog-and-sources).

### Thêm một bài viết bằng tay

Bạn cũng có thể tạo một bài viết bằng cách xây dựng các đối tượng cơ bản tự mình. Đây là cách duy nhất để thực hiện điều này trong Gramps Desktop ([đồng bộ hóa](../administration/sync.md) với Gramps Web), và các bước là giống nhau trong cả hai ứng dụng:

- Thêm một nguồn mới. Tiêu đề của nguồn sẽ là tiêu đề của bài viết trên blog của bạn, tác giả của nguồn sẽ là tác giả của bài viết.
- Tùy chọn, liên kết nguồn với một kho tương ứng với blog Gramps Web của bạn
- Thêm một ghi chú mới vào nguồn. Viết bài viết trên blog của bạn và sao chép văn bản vào ghi chú.
- Tùy chọn, thêm một hoặc nhiều tệp phương tiện vào nguồn của bạn. Tệp phương tiện đầu tiên sẽ được lấy làm hình ảnh xem trước của bài viết hiển thị trên văn bản. Tất cả các tệp phương tiện sẽ được hiển thị bên dưới văn bản dưới dạng một bộ sưu tập.
- Thêm nhãn `Blog` vào nguồn (tạo nó nếu nó không tồn tại)

## Mối quan hệ giữa blog và nguồn

Vì các bài viết trên blog chỉ là các nguồn, tất cả các bài viết trên blog cũng xuất hiện trong danh sách các nguồn và hiển thị dưới dạng nguồn trong các tìm kiếm. Trong chế độ xem nguồn, có một nút "hiển thị trong blog" sẽ đưa bạn đến chế độ xem blog cho bài viết đó. URL của bài viết trên blog cũng chứa ID Gramps của nguồn tương ứng, vì vậy một bài viết tại `yourdomain.com/blog/S0123` tương ứng với nguồn tại `yourdomain.com/source/S0123`.

Ở cuối mỗi bài viết trên blog, có một nút "chi tiết" sẽ đưa bạn đến chế độ xem nguồn.
