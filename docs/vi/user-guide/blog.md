# Sử dụng blog tích hợp sẵn

Blog được thiết kế để trình bày các câu chuyện về nghiên cứu lịch sử gia đình của bạn.

Trong cơ sở dữ liệu Gramps, các bài viết trên blog được đại diện dưới dạng nguồn với một ghi chú đính kèm, chứa văn bản của blog và tùy chọn, các tệp phương tiện cho hình ảnh của bài viết trên blog. Gramps Web coi mọi nguồn có thẻ `Blog` là bài viết trên blog.

## Thêm một bài viết trên blog

Để thêm một bài viết trên blog, bạn có thể sử dụng Gramps Web hoặc Gramps Desktop ([đồng bộ hóa](../administration/sync.md) với Gramps Web), các bước là giống nhau trong cả hai trường hợp:

- Thêm một nguồn mới. Tiêu đề của nguồn sẽ là tiêu đề của bài viết trên blog của bạn, tác giả của nguồn sẽ là tác giả của bài viết.
- Tùy chọn, liên kết nguồn với một kho tương ứng với blog Gramps Web của bạn
- Thêm một ghi chú mới vào nguồn. Viết bài viết trên blog của bạn và sao chép văn bản vào ghi chú.
- Tùy chọn, thêm một hoặc nhiều tệp phương tiện vào nguồn của bạn. Tệp phương tiện đầu tiên sẽ được lấy làm hình ảnh xem trước của bài viết hiển thị trên văn bản. Tất cả các tệp phương tiện sẽ được hiển thị dưới văn bản như một bộ sưu tập.
- Thêm nhãn `Blog` vào nguồn (tạo nó nếu chưa tồn tại)

## Mối quan hệ giữa blog và nguồn

Vì các bài viết trên blog chỉ là nguồn, tất cả các bài viết trên blog cũng xuất hiện trong danh sách các nguồn và hiện ra như các nguồn trong tìm kiếm. Trong chế độ xem nguồn, có một nút "hiển thị trong blog" sẽ đưa bạn đến chế độ xem blog cho bài viết đó. URL của bài viết trên blog cũng chứa ID Gramps của nguồn tương ứng, vì vậy một bài viết tại `yourdomain.com/blog/S0123` tương ứng với nguồn tại `yourdomain.com/source/S0123`.

Ở cuối mỗi bài viết trên blog, có một nút "chi tiết" sẽ đưa bạn đến chế độ xem nguồn.
