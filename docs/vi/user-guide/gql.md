# Lọc bằng Ngôn ngữ Truy vấn Gramps

Các chế độ xem danh sách đối tượng (người, gia đình, sự kiện, ...) có chế độ lọc nâng cao tùy chọn dựa trên [Ngôn ngữ Truy vấn Gramps](https://github.com/DavidMStraub/gramps-ql) (GQL).

Để sử dụng, hãy nhập một truy vấn theo cú pháp GQL và nhấn enter (hoặc nhấn nút "áp dụng"). Chế độ xem sẽ được lọc theo truy vấn. Nếu truy vấn không hợp lệ, khung của trường nhập sẽ chuyển sang màu đỏ.

Cú pháp GQL được mô tả bên dưới, sao chép từ tài liệu GQL.

## Cú pháp

Một truy vấn GQL là một chuỗi được tạo thành từ các câu lệnh có dạng `property operator value`, có thể kết hợp tùy chọn với các từ khóa `and` và `or` cũng như dấu ngoặc đơn.

### Thuộc tính

#### `class`

Lọc theo lớp đối tượng Gramps và có thể là một trong các giá trị `person`, `family`, `event`, `place`, `citation`, `source`, `repository`, `media`, hoặc `note`.

#### Thuộc tính đối tượng

GQL hỗ trợ truy vấn các thuộc tính lồng nhau của các đối tượng Gramps, ví dụ: `primary_name.date.calendar`. Xem bên dưới để biết danh sách đầy đủ các thuộc tính – xem thêm [Mô hình Dữ liệu Gramps](https://gramps-project.org/wiki/index.php/Gramps_Data_Model).

#### Các phần tử danh sách theo chỉ số

Các phần tử riêng lẻ trong các thuộc tính giống như danh sách có thể được truy cập bằng chỉ số vị trí trong dấu ngoặc vuông. Điều này có thể được kết hợp với các thuộc tính lồng nhau, ví dụ: `primary_name.surname_list[0].surname`.

#### `length`

Đây là một thuộc tính đặc biệt trả về độ dài của một thuộc tính Gramps giống như mảng, ví dụ: `media_list.length > 0` để lấy các đối tượng có tham chiếu phương tiện.

#### `all`, `any`

Hai thuộc tính đặc biệt khác cho các thuộc tính Gramps giống như mảng. `all` yêu cầu một điều kiện áp dụng cho tất cả các mục trong danh sách, `any` yêu cầu điều đó áp dụng cho ít nhất một mục. Cả hai thuộc tính có thể được kết hợp với các thuộc tính khác trước và sau. Ví dụ: `media_list.any.citation_list.length > 0` để trả về các đối tượng có tham chiếu phương tiện có trích dẫn; `media_list.all.citation_list.length = 0` để trả về các đối tượng mà tất cả các đối tượng phương tiện không có trích dẫn.

#### Chỉ số mảng

Một chỉ số mảng số có thể được sử dụng để truy cập các phần tử cụ thể của một danh sách, ví dụ: `child_ref_list[0]` cho đứa trẻ đầu tiên.

#### `get_person`, v.v.

Trong khi tất cả các thuộc tính trước đó đều tham chiếu đến một đối tượng Gramps duy nhất, cũng có thể lọc theo các đối tượng khác được tham chiếu bởi đối tượng ban đầu. Ví dụ, một sự kiện có một tay cầm địa điểm trong thuộc tính `place`. Sử dụng thuộc tính giả `get_place`, GQL chuyển sang các thuộc tính của đối tượng đó. Ví dụ, có thể tìm kiếm `class = event and place.get_place.name.value ~ York`. Điều này cũng có thể được kết hợp với `any` hoặc `all`, ví dụ: `class = person and event_ref_list.any.ref.get_event.description ~ farmer`.

### Toán tử

#### `=`, `!=`

Công bằng hoặc không công bằng. Ví dụ: `class = person`, `class != family`

#### `>`, `>=`, `<`, `<=`

So sánh. Hoạt động cho cả chuỗi và số. Ví dụ: `confidence <= 1`, `change > 1712477760 `, `gramps_id > "I2015"`

#### `~`, `!~`

Chứa hoặc không chứa. Hoạt động cho danh sách cũng như chuỗi. Ví dụ: `gramps_id !~ F00`, `author ~ David`, `family_list ~ "3a16680f7d226e3ac3eefc8b57a"`

#### Không có toán tử/giá trị

Nếu không có toán tử và giá trị nào được cung cấp, giá trị sẽ được hiểu là một boolean (true hoặc false). Điều này hoạt động cho tất cả các loại thuộc tính và các quy tắc Python cho việc chuyển đổi thành true/false được áp dụng. Ví dụ, truy vấn `private` trả về các đối tượng riêng tư; `confidence` trả về các đối tượng mà độ tin cậy lớn hơn 0; `media_list` trả về các đối tượng có ít nhất một tham chiếu phương tiện.

### Giá trị

Giá trị có thể là số hoặc chuỗi. Nếu số nên được hiểu là chuỗi hoặc các ký tự đặc biệt như = được liên quan, hãy đặt giá trị trong chuỗi. Ví dụ: `gramps_id = F0001`, nhưng `gramps_id = "0001"`.

## Ví dụ có chú thích

```sql
class = note and private and text.string ~ David
```

Tất cả các ghi chú riêng tư chứa chuỗi "David" trong văn bản của chúng


```sql
media_list.length >= 10
```

Tất cả các đối tượng (của bất kỳ lớp nào) có 10 hoặc nhiều tham chiếu phương tiện

```sql
class != person and media_list.any.rect
```

Tất cả các đối tượng *không* phải là người nhưng có một tham chiếu phương tiện là một phần của hình ảnh. Ở đây, `media_list.any.rect` có nghĩa là đối với mỗi mục trong danh sách phương tiện, nó được kiểm tra xem thuộc tính `rect` (hình chữ nhật) có giá trị đúng hay không, có nghĩa là nó là một danh sách không rỗng. (`media_list.any.rect.length > 0` sẽ có cùng hiệu ứng.)

```sql
class = family and child_ref_list.length > 10
```

Các gia đình có hơn 10 đứa trẻ.

```sql
class = event and date.modifier = 0 and date.dateval[2] > 2020
```

Các sự kiện mà ngày là một ngày bình thường (không phải là một khoảng thời gian, v.v.) và năm sau 2020.

```sql
note_list.any.get_note.text.string ~ "David"
```

Tất cả các đối tượng có ít nhất một ghi chú chứa chuỗi "David" trong văn bản của chúng.


```sql
class = family and child_ref_list.all.ref.get_person.gender = 0 and child_ref_list.length = 3
```

Tất cả các gia đình có ba con gái.


## Danh sách đầy đủ các Thuộc tính Gramps

Để biết danh sách đầy đủ các thuộc tính Gramps, xem [tài liệu GQL](https://github.com/DavidMStraub/gramps-ql#full-list-of-gramps-properties).
