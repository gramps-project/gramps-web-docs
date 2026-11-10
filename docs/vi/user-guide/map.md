# Bản đồ

Trang Bản đồ hiển thị tất cả các địa điểm trong cây gia đình của bạn dưới dạng các đánh dấu tương tác trên một bản đồ địa lý. Nó có thể truy cập từ thanh bên.

## Đánh dấu địa điểm

Chỉ những địa điểm có tọa độ GPS được lưu trữ trong cơ sở dữ liệu Gramps mới được hiển thị trên bản đồ. Những địa điểm không có tọa độ sẽ bị bỏ qua một cách lặng lẽ. Tọa độ GPS có thể được thiết lập trên trang chi tiết địa điểm (chỉnh sửa địa điểm và điền vào các trường vĩ độ và kinh độ).

!!! tip
    Nếu nhiều địa điểm của bạn bị thiếu trên bản đồ, hãy mở trang chi tiết địa điểm và kiểm tra xem vĩ độ và kinh độ đã được thiết lập chưa. Bạn có thể thêm hoặc sửa tọa độ trực tiếp từ chế độ chỉnh sửa của địa điểm.

Mỗi địa điểm có tọa độ được hiển thị dưới dạng một đánh dấu. Nhấp vào một đánh dấu sẽ mở một thẻ tóm tắt hiển thị tên địa điểm và các sự kiện cũng như người liên kết với nó. Nhấp vào tên địa điểm trong thẻ để mở trang chi tiết địa điểm đầy đủ.

## Tìm kiếm

Hộp tìm kiếm ở góc trên bên trái của bản đồ tìm kiếm khi bạn gõ và nhóm các kết quả dưới ba tiêu đề:

- **Địa điểm** – các địa điểm trong cây gia đình của bạn. Chọn một địa điểm sẽ di chuyển bản đồ đến đó và làm nổi bật đánh dấu của nó.
- **Người** – những người trong cây gia đình của bạn. Chọn một người sẽ chuyển bản đồ sang chế độ người được mô tả [dưới đây](#following-a-person-across-the-map).
- **Ngoài** – các địa điểm từ [OpenStreetMap](https://www.openstreetmap.org/), cho bất kỳ đâu trên thế giới. Chọn một địa điểm sẽ chỉ đơn giản là di chuyển và phóng to bản đồ đến vị trí đó; nó không lọc hoặc thay đổi các địa điểm trong cây của bạn.

Các kết quả bên ngoài cũng hữu ích khi thêm tọa độ cho một địa điểm: bạn có thể tra cứu vị trí ở đây để xem nó ở đâu trước khi nhập vĩ độ và kinh độ.

## Theo dõi một người trên bản đồ

Chọn một người – từ hộp tìm kiếm của bản đồ, hoặc với nút **Mở trong bản đồ** trên trang chi tiết của một người – sẽ hiển thị các địa điểm liên kết với các sự kiện của người đó, được nối với nhau bằng các đường theo thứ tự thời gian. Các mũi tên nhỏ dọc theo mỗi đường chỉ ra hướng di chuyển, vì vậy bạn có thể theo dõi cuộc sống của một người từ khi sinh ra đến khi qua đời trên bản đồ.

Các địa điểm trên trang chi tiết địa điểm cũng có nút **Mở trong bản đồ**, mở bản đồ được trung tâm vào địa điểm đó.

## Thanh trượt thời gian

Thanh trượt thời gian ở dưới cùng của trang lọc các đánh dấu địa điểm được hiển thị dựa trên năm của các sự kiện liên quan của chúng:

- Kéo tay cầm để chọn một năm.
- Chỉ các địa điểm liên kết với các sự kiện nằm trong khoảng thời gian đã chọn mới được hiển thị.
- Sử dụng điều này để theo dõi nơi tổ tiên của bạn đã sống tại một thời điểm cụ thể trong lịch sử.

## Các lớp bản đồ

Một nút chuyển đổi lớp (biểu tượng lớp chồng, góc dưới bên trái) cho phép bạn chọn giữa hai bản đồ cơ sở. Dưới chúng, nó liệt kê các lớp bản đồ của riêng bạn dưới "Bản đồ của bạn" (xem [Lớp bản đồ tùy chỉnh](#custom-map-overlays) và [Tệp bản đồ của các địa điểm](#map-files-of-places)) và lớp [Công trình Wikidata](#wikidata-buildings) dưới "Ngoài", mỗi lớp có thể được bật và tắt.

Các nhãn của cả hai bản đồ cơ sở được hiển thị bằng ngôn ngữ mà bạn đã chọn trong Gramps Web, nơi dữ liệu bản đồ có tên trong ngôn ngữ đó, và bằng tên địa phương nếu không có.

### Bản đồ cơ sở

Lớp mặc định, được cung cấp bởi [OpenFreeMap](https://openfreemap.org) (kiểu Liberty cho chế độ sáng, kiểu tối cho chế độ tối). Đây là một bản đồ hiện đại đa mục đích phù hợp cho việc xác định vị trí các địa điểm.

### Bản đồ lịch sử

Chuyển đổi bản đồ cơ sở sang [OpenHistoricalMap](https://www.openhistoricalmap.org) (OHM), một dự án do cộng đồng điều hành mà lập bản đồ thế giới như nó đã tồn tại ở các thời điểm khác nhau – hãy nghĩ về nó như một phiên bản lịch sử của OpenStreetMap.

Khi lớp Bản đồ lịch sử được kích hoạt, thanh trượt thời gian cũng lọc các ô bản đồ: OHM hiển thị bản đồ như nó đã xuất hiện trong năm đã chọn, vì vậy các biên giới lịch sử, tên địa điểm và các đặc điểm được hiển thị thay vì các đặc điểm hiện đại. Điều này cho phép bạn thấy cả vị trí của tổ tiên bạn và bối cảnh địa lý và chính trị đương đại trong một cái nhìn duy nhất.

!!! note
    Phạm vi của OpenHistoricalMap thay đổi theo vùng và thời kỳ. Các khu vực hoặc thời kỳ có đóng góp ít có thể cho thấy chi tiết lịch sử hạn chế. Nếu bạn nhận thấy dữ liệu lịch sử bị thiếu hoặc không chính xác, hãy xem xét [đóng góp cho OpenHistoricalMap](https://www.openhistoricalmap.org) – đây là một dự án cộng đồng mở mà bất kỳ ai cũng có thể chỉnh sửa.

## Lớp bản đồ tùy chỉnh

Ngoài các lớp cơ bản tích hợp sẵn, bạn có thể biến bất kỳ hình ảnh bản đồ lịch sử nào đã quét – được lưu trữ trong Gramps dưới dạng một đối tượng **Media** – thành một lớp phủ tùy chỉnh được định vị trên bản đồ trực tiếp. Điều này hữu ích cho các bản quét của các kế hoạch thành phố cũ, bản đồ giáo xứ hoặc bản đồ tài sản mà bạn muốn so sánh trực tiếp với địa lý hiện đại hoặc lịch sử.

### Địa chính một hình ảnh

1. Mở đối tượng media cho hình ảnh bản đồ đã quét và chuyển sang chế độ chỉnh sửa.
2. Mở tab "Bản đồ" và nhấp vào **Chỉnh sửa tọa độ**. Điều này mở một hộp thoại địa chính với hình ảnh bên cạnh một bản đồ.
3. Nhấp vào **Chọn một điểm trên bản đồ**, sau đó nhấp vào vị trí trên bản đồ mà một điểm trên hình ảnh nên tương ứng. Hình ảnh được đặt trên bản đồ lần đầu tiên ngay khi một điểm được chọn.
4. Sử dụng thanh trượt **Tỷ lệ** để thay đổi kích thước hình ảnh và thanh trượt **Độ mờ** để nhìn thấy bản đồ cơ sở qua nó trong khi định vị.
5. Nhấp vào **Căn chỉnh hình ảnh** và nhấp vào bản đồ một lần nữa để di chuyển hình ảnh sao cho điểm đã ghim khớp chính xác.
6. Lặp lại các bước tỷ lệ, độ mờ và căn chỉnh cho đến khi hình ảnh khớp với địa lý bên dưới, sau đó lưu lại.

Ở phía sau, điều này lưu trữ tọa độ góc của hình ảnh trong thuộc tính `map:bounds` trên đối tượng media.

### Xem lớp phủ trên trang Bản đồ

Khi một đối tượng media đã được địa chính theo cách này, nó tự động trở thành có sẵn như một lớp có thể bật tắt trên trang Bản đồ. Mở công tắc lớp (biểu tượng lớp chồng, góc dưới bên trái) để hiển thị hoặc ẩn từng lớp phủ độc lập với bản đồ cơ sở. Các lớp phủ được liệt kê theo tiêu đề của đối tượng media.

Mỗi lớp phủ có một thanh trượt độ mờ bên dưới tên của nó, vì vậy bạn có thể thấy bản đồ cơ sở qua nó.

## Tệp bản đồ của các địa điểm

Các địa điểm có thể có tệp bản đồ đính kèm dưới dạng đối tượng media – ví dụ như ranh giới của một giáo xứ, một quận, hoặc một khu đất, hoặc một lộ trình. Các tệp được hỗ trợ là KML (`.kml`), GeoJSON (`.geojson`), và GPX (`.gpx`).

Khi bạn chọn một địa điểm trên bản đồ, các tệp bản đồ của nó được vẽ trên bản đồ, sử dụng các màu sắc được lưu trữ trong tệp nơi có chúng. Điều này cũng hoạt động cho các địa điểm không có tọa độ: bản đồ sau đó phóng to vào khu vực được bao phủ bởi các tệp. Trong khi địa điểm được chọn, các tệp của nó được liệt kê trong công tắc lớp dưới "Bản đồ của bạn", nơi bạn có thể tắt từng tệp.

Để thêm một tệp bản đồ vào một địa điểm, hãy thêm nó vào thư viện của địa điểm như bất kỳ [tệp media nào khác](media.md).

## Công trình Wikidata

Lớp "Công trình Wikidata" hiển thị các công trình được ghi nhận trong [Wikidata](https://www.wikidata.org/), chẳng hạn như nhà thờ, trang trại, hoặc nhà phố. Nó tắt theo mặc định và có thể được bật trong công tắc lớp dưới "Ngoài". Các công trình chỉ được hiển thị khi bản đồ được phóng to đủ gần. Khi thanh trượt thời gian được kích hoạt, chỉ các công trình tồn tại tại thời điểm đã chọn mới được hiển thị.

Nhấp vào một công trình để xem chi tiết của nó từ Wikidata, chẳng hạn như khi nào nó được xây dựng hoặc phá hủy, địa chỉ của nó, người cư ngụ và chủ sở hữu.

### Lưu một công trình như một địa điểm

Người dùng có thể thêm đối tượng sẽ thấy nút **Lưu như địa điểm** trong chi tiết của công trình. Nó mở biểu mẫu cho một địa điểm mới, được điền sẵn với tên công trình trong ngôn ngữ của bạn, loại địa điểm (`Farm` cho các trang trại, nếu không thì `Building`), tọa độ của nó, và một liên kết đến mục Wikidata. Hoàn thành biểu mẫu, ví dụ bằng cách chọn địa điểm bao quanh, và lưu lại.

Nếu một địa điểm trong cây của bạn nằm ở cùng một vị trí với công trình, nút sẽ đọc **Mở địa điểm đã lưu** thay vào đó và hiển thị địa điểm đó.

!!! info
    Quản trị viên máy chủ có thể xóa lớp công trình Wikidata với tùy chọn `mapWikidata` của [cấu hình frontend](../install_setup/frontend-config.md).
