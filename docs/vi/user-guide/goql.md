# Lọc bằng Ngôn ngữ Truy vấn Đối tượng Gramps

Các [khung danh sách đối tượng](lists.md) (người, gia đình, sự kiện, ...) và [danh sách nhiệm vụ](tasks.md) có một trường lọc cho các biểu thức trong [Ngôn ngữ Truy vấn Đối tượng Gramps](https://github.com/DavidMStraub/gramps-object-query-language) (GOQL).

Để sử dụng, mở bảng điều khiển lọc, gõ một biểu thức vào trường **GOQL** và nhấn Enter (hoặc nhấp vào **Áp dụng**). Danh sách sẽ được lọc theo biểu thức, trên bất kỳ bộ lọc nào khác đang hoạt động. Nếu biểu thức không hợp lệ, trường sẽ được đánh dấu là lỗi.

Biểu thức luôn áp dụng cho các đối tượng trong danh sách mà bạn đang ở: trong danh sách Người, `surname == 'Smith'` tìm những người có họ là Smith.

!!! note
    Trường GOQL cần Gramps Web API 3.24 hoặc mới hơn.

## Cú pháp

Một biểu thức GOQL trông giống như một điều kiện trong ngôn ngữ lập trình Python. Bạn không cần phải biết Python để sử dụng – các ví dụ dưới đây bao gồm hầu hết các nhu cầu.

### So sánh

Một phép so sánh có dạng `trường toán tử giá trị`, ví dụ `surname == 'Smith'`.

Toán tử | Ý nghĩa
---------|--------
`==` | bằng
`!=` | không bằng
`<`, `<=` | nhỏ hơn, nhỏ hơn hoặc bằng (trước, nhỏ hơn)
`>`, `>=` | lớn hơn, lớn hơn hoặc bằng (sau, lớn hơn)
`in [ ... ]` | là một trong các giá trị được liệt kê, ví dụ `surname in ['Meyer', 'Maier']`
`not in [ ... ]` | không phải là bất kỳ giá trị nào trong danh sách
`'text' in field` | trường chứa văn bản, ví dụ `'mill' in surname`
`is None` | trường trống hoặc không tồn tại, ví dụ `death.date.sortval is None`

Văn bản được đặt trong dấu nháy đơn hoặc đôi (`'Smith'`), số thì không (`1850`). Các phép so sánh có thể được nối tiếp, ví dụ `Date('1850') <= birth.date.sortval < Date('1900')`.

### Kết hợp điều kiện

Các điều kiện có thể được kết hợp với `and` và `or`, và đảo ngược với `not`. `and` có ưu tiên hơn `or`; sử dụng dấu ngoặc để nhóm các điều kiện:

```python
(gender == Person.MALE and surname == 'Smith') or given_name == 'Mary'
```

### Mẫu văn bản

- `like(field, 'pattern')` khớp với một mẫu trong đó `%` đại diện cho bất kỳ văn bản nào và `_` cho một ký tự đơn, ví dụ `like(given_name, 'J%')` cho tất cả các tên gọi bắt đầu bằng "J".
- `regex(field, 'pattern')` khớp với một [biểu thức chính quy](https://en.wikipedia.org/wiki/Regular_expression), ví dụ `regex(surname, '^M[ae][iy]er$')`.

`like` và `'text' in field` không phân biệt chữ hoa và chữ thường (trên SQLite, điều này chỉ áp dụng cho các chữ cái A–Z không có dấu). `regex` thì phân biệt chữ hoa và chữ thường.

### Trường

Một trường là tên của một thuộc tính của đối tượng, như `gender` hoặc `gramps_id`, hoặc một đường dẫn đến một thuộc tính lồng nhau, như `primary_name.first_name` hoặc `primary_name.surname_list[0].surname`. Các dấu ngoặc vuông chọn một phần tử của danh sách theo vị trí của nó, bắt đầu từ 0. Các thuộc tính có sẵn là các thuộc tính của [mô hình dữ liệu Gramps](https://gramps-project.org/wiki/index.php/Gramps_Data_Model). Nếu một trường không tồn tại, thông báo lỗi sẽ liệt kê các trường tồn tại.

Một vài phím tắt có sẵn:

- Người có `given_name` và `surname`, tên gọi và họ của tên chính.
- Người có `birth` và `death`, các sự kiện sinh và chết của họ, ví dụ `birth.date.sortval` hoặc `death.place.name.value`.
- Gia đình có `father` và `mother`, ví dụ `father.surname == 'Smith'`.
- Sự kiện có `place`, trích dẫn có `source`, và địa điểm có `enclosed_by`, địa điểm bao quanh.

Những điều này có thể được nối tiếp, ví dụ `father.birth.place.name.value` trong danh sách Gia đình. Hai trường cũng có thể được so sánh với nhau, ví dụ `father.surname == mother.surname`.

### Danh sách các đối tượng liên quan

`any(collection, condition)` khớp nếu ít nhất một mục trong một bộ sưu tập đáp ứng điều kiện, và `len(collection)` đếm số mục. Nếu không có điều kiện, `any(collection)` khớp nếu bộ sưu tập không trống. Các bộ sưu tập là:

- trên hầu hết mọi đối tượng: `notes`, `citations`, `media`, và `tags`
- trên người: `events`, `families` (như một đối tác), `parent_families` (như một đứa trẻ), và `associations`
- trên gia đình: `children`
- trên tất cả các đối tượng: `backlinks`, các đối tượng tham chiếu đến nó, có thể được kiểm tra loại của chúng với `_class`, ví dụ `any(backlinks, _class == 'Person')`

`any` và `len` cũng hoạt động cho các danh sách được lưu trữ trong chính đối tượng, chẳng hạn như `alternate_names` hoặc `primary_name.surname_list`.

### Hằng số và loại

Các giá trị cố định của Gramps có sẵn dưới dạng hằng số, chẳng hạn như `Person.MALE`, `Person.FEMALE`, `Person.UNKNOWN`, hoặc các mức độ tin cậy `Citation.CONF_VERY_LOW` đến `Citation.CONF_VERY_HIGH`. Các loại được so sánh theo `value` của chúng với các hằng số như `EventType.BIRTH`, `FamilyRelType.MARRIED`, `NameType.BIRTH`, `PlaceType.VILLAGE`, hoặc `RepositoryType.ARCHIVE`:

```python
type.value == EventType.BAPTISM
```

Các loại tùy chỉnh mà bạn đã nhập không có hằng số riêng của chúng.

### Ngày tháng

`Date('...')` chuyển một ngày được viết dưới dạng văn bản thành một giá trị có thể so sánh với `sortval` của một ngày, ví dụ `birth.date.sortval < Date('1800')`.

`sortval` là một điểm thời gian duy nhất và bỏ qua loại và chất lượng của một ngày: "trước năm 1800", "khoảng năm 1800" và "năm 1800" đều có cùng một `sortval`, và đối với một khoảng hoặc khoảng thời gian, nó là bắt đầu. Để tính đến những điều này, hãy so sánh `modifier` hoặc `quality` của ngày với các hằng số như `Date.MOD_ABOUT`, `Date.MOD_BEFORE`, `Date.MOD_AFTER`, `Date.MOD_RANGE`, `Date.MOD_SPAN`, hoặc `Date.QUAL_ESTIMATED`:

```python
date.modifier == Date.MOD_ABOUT
```

## Ví dụ có chú thích

Danh sách Người:

```python
gender == Person.FEMALE and like(given_name, 'Mar%')
```

Phụ nữ có tên gọi bắt đầu bằng "Mar".

```python
Date('1850') <= birth.date.sortval < Date('1900')
```

Người sinh từ năm 1850 đến 1899.

```python
birth.place.name.value == death.place.name.value
```

Người đã sinh và chết ở một nơi có cùng tên.

```python
not any(notes)
```

Người không có ghi chú.

```python
any(events, type.value == EventType.BURIAL)
```

Người có một sự kiện chôn cất.

```python
any(alternate_names, surname_list[0].surname == 'Meyer')
```

Người có một tên gọi thay thế với họ Meyer.

Danh sách Gia đình:

```python
len(children) > 10
```

Gia đình có hơn 10 đứa trẻ.

```python
len(children, gender == Person.FEMALE) == 3
```

Gia đình có ba cô con gái.

```python
mother.death.date.sortval < father.death.date.sortval
```

Gia đình mà mẹ chết trước cha.

Danh sách Sự kiện:

```python
type.value == EventType.BAPTISM and place.name.value == 'Berlin'
```

Lễ rửa tội ở một nơi có tên là Berlin.

Danh sách Trích dẫn:

```python
confidence >= Citation.CONF_HIGH
```

Trích dẫn có độ tin cậy cao hoặc rất cao.

Danh sách Ghi chú:

```python
'David' in text.string and private == True
```

Ghi chú riêng tư chứa "David".

```python
not any(backlinks)
```

Ghi chú không được gắn với bất kỳ đối tượng nào.

## Tham khảo đầy đủ

Để tham khảo đầy đủ về ngôn ngữ, xem [tài liệu GOQL](https://github.com/DavidMStraub/gramps-object-query-language/blob/main/docs/where_expr.md).
