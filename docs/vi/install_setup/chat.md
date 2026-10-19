# Thiết lập trò chuyện AI

!!! info
    Trò chuyện AI yêu cầu Gramps Web API phiên bản 2.5.0 trở lên. Phiên bản 3.6.0 đã giới thiệu khả năng gọi công cụ để tương tác thông minh hơn.

Gramps Web API hỗ trợ việc đặt câu hỏi về cơ sở dữ liệu gia phả bằng cách sử dụng các mô hình ngôn ngữ lớn (LLM) với khả năng gọi công cụ.

## Cách hoạt động

Trợ lý AI sử dụng các công cụ chuyên biệt để truy vấn dữ liệu gia phả của bạn trực tiếp. Những công cụ này cho phép trợ lý tìm kiếm cơ sở dữ liệu bằng tìm kiếm toàn văn, lọc người/sự kiện/gia đình/nơi chốn theo các tiêu chí cụ thể, tính toán mối quan hệ giữa các cá nhân và truy xuất các hồ sơ đầy đủ, bao gồm cả ghi chú. Trợ lý sau đó trả lời dựa trên các hồ sơ mà nó đã tra cứu và liên kết đến chúng trong câu trả lời của nó.

Kể từ Gramps Web API 3.24, trò chuyện AI không còn yêu cầu một mô hình nhúng vector. Các phiên bản trước đó cũng đã sử dụng *tìm kiếm ngữ nghĩa* (tạo ra thông tin bổ sung, RAG), so sánh ý nghĩa của một câu hỏi với một chỉ mục các vector số được tính toán cho tất cả các đối tượng trong cơ sở dữ liệu. Tìm kiếm ngữ nghĩa đã bị ngừng hỗ trợ và sẽ bị loại bỏ trong Gramps Web API 3.25, xem [Tìm kiếm ngữ nghĩa (đã ngừng hỗ trợ)](#semantic-search-deprecated) bên dưới.

Để kích hoạt điểm cuối trò chuyện trong Gramps Web API, cần thực hiện hai bước:

1. Cài đặt các phụ thuộc cần thiết,
2. Thiết lập nhà cung cấp LLM.

Hai bước này được mô tả dưới đây. Cuối cùng, một chủ sở hữu hoặc quản trị viên phải [cấu hình ai có thể truy cập tính năng trò chuyện](users.md#configuring-who-can-use-ai-chat) trong cài đặt Quản lý Người dùng.

## Cài đặt các phụ thuộc cần thiết

Các hình ảnh docker tiêu chuẩn cho Gramps Web đã có sẵn tất cả các phụ thuộc cần thiết cho trò chuyện AI được cài đặt sẵn.

Khi cài đặt Gramps Web API qua `pip` (điều này không cần thiết khi sử dụng các hình ảnh Docker), các phụ thuộc cần thiết được cài đặt bằng

```bash
pip install gramps_webapi[ai]
```

## Tìm kiếm ngữ nghĩa (đã ngừng hỗ trợ)

!!! warning "Tìm kiếm ngữ nghĩa đã ngừng hỗ trợ"
    Tìm kiếm ngữ nghĩa đã ngừng hỗ trợ kể từ Gramps Web API 3.24 và sẽ bị loại bỏ trong phiên bản 3.25. Trò chuyện AI và [tìm kiếm toàn văn](../user-guide/search.md) không cần nó. Sau khi loại bỏ, cài đặt `VECTOR_EMBEDDING_MODEL` vẫn được chấp nhận nhưng sẽ bị bỏ qua. Nếu bạn chỉ đặt nó để kích hoạt trò chuyện AI, bạn có thể xóa nó ngay bây giờ, cùng với các cài đặt `VECTOR_EMBEDDING_*` khác, điều này cũng tiết kiệm bộ nhớ mà mô hình nhúng cần.

Phần còn lại của mục này mô tả tìm kiếm ngữ nghĩa cho các máy chủ vẫn sử dụng nó với Gramps Web API 3.24.

Nếu các phụ thuộc cần thiết đã được cài đặt, việc kích hoạt tìm kiếm ngữ nghĩa có thể đơn giản như việc thiết lập tùy chọn cấu hình `VECTOR_EMBEDDING_MODEL` (ví dụ: bằng cách thiết lập biến môi trường `GRAMPSWEB_VECTOR_EMBEDDING_MODEL`), xem [Cấu hình Máy chủ](configuration.md). Đây có thể là bất kỳ chuỗi nào của một mô hình được hỗ trợ bởi thư viện [Sentence Transformers](https://sbert.net/). Xem tài liệu của dự án này để biết chi tiết và các mô hình có sẵn.

!!! warning
    Lưu ý rằng các hình ảnh docker mặc định không bao gồm phiên bản PyTorch có hỗ trợ GPU. Nếu bạn có quyền truy cập vào GPU (sẽ tăng tốc độ lập chỉ mục ngữ nghĩa đáng kể), vui lòng cài đặt phiên bản PyTorch có hỗ trợ GPU.

Có một số điều cần xem xét khi chọn mô hình.

- Khi bạn thay đổi mô hình, bạn phải tự tay tái tạo chỉ mục tìm kiếm ngữ nghĩa cho cây của bạn (hoặc tất cả các cây trong một thiết lập đa cây), nếu không bạn sẽ gặp lỗi hoặc kết quả vô nghĩa. Gramps Web phát hiện khi mô hình nhúng đã cấu hình không còn phù hợp với chỉ mục hiện có và hiển thị một thông báo liên tục cho các quản trị viên nhắc họ kích hoạt một lần lập chỉ mục lại hoàn toàn từ [Cài đặt Quản trị](../administration/settings.md#semantic-search-index).
- Các mô hình là một sự đánh đổi giữa độ chính xác/tính tổng quát ở một bên và thời gian tính toán/kho lưu trữ ở bên kia. Nếu bạn không chạy Gramps Web API trên một hệ thống có quyền truy cập vào một GPU mạnh mẽ, các mô hình lớn thường quá chậm trong thực tế.
- Trừ khi toàn bộ cơ sở dữ liệu của bạn bằng tiếng Anh và tất cả người dùng của bạn chỉ được mong đợi đặt câu hỏi trò chuyện bằng tiếng Anh, bạn sẽ cần một mô hình nhúng đa ngôn ngữ, mà hiếm hơn so với các mô hình tiếng Anh thuần túy.

Nếu mô hình không có trong bộ nhớ cache cục bộ, nó sẽ được tải xuống khi Gramps Web API được khởi động lần đầu tiên với cấu hình mới. Mô hình `sentence-transformers/distiluse-base-multilingual-cased-v2` đã có sẵn cục bộ khi sử dụng các hình ảnh docker tiêu chuẩn. Mô hình này là một điểm khởi đầu tốt và hỗ trợ đầu vào đa ngôn ngữ.

Vui lòng chia sẻ những hiểu biết về các mô hình khác nhau với cộng đồng!

!!! info
    Thư viện sentence transformers tiêu tốn một lượng lớn bộ nhớ, điều này có thể khiến các quy trình worker bị giết. Như một quy tắc chung, với tìm kiếm ngữ nghĩa được kích hoạt, mỗi worker Gunicorn tiêu tốn khoảng 200 MB bộ nhớ và mỗi worker celery khoảng 500 MB bộ nhớ ngay cả khi không hoạt động, và lên tới 1 GB khi tính toán các nhúng. Xem [Giới hạn việc sử dụng CPU và bộ nhớ](cpu-limited.md) để biết các cài đặt giới hạn việc sử dụng bộ nhớ. Ngoài ra, nên cung cấp một phân vùng hoán đổi đủ lớn để ngăn ngừa lỗi OOM do các đỉnh sử dụng bộ nhớ tạm thời.

### Sử dụng API nhúng từ xa

Như một sự thay thế cho việc chạy một mô hình Sentence Transformers cục bộ, bạn có thể sử dụng một API nhúng tương thích với OpenAI từ xa cho tìm kiếm ngữ nghĩa. Điều này hữu ích nếu bạn muốn chuyển giao việc tính toán nhúng cho một dịch vụ riêng biệt (ví dụ: [Ollama](https://ollama.com/)), sử dụng nhà cung cấp nhúng đám mây (ví dụ: OpenAI), hoặc tránh việc tải thư viện Sentence Transformers và PyTorch vào bộ nhớ.

API từ xa phải tương thích với [điểm cuối nhúng OpenAI](https://platform.openai.com/docs/api-reference/embeddings) (`/v1/embeddings`).

Để sử dụng API nhúng từ xa, hãy thiết lập các tùy chọn cấu hình sau (xem [Cấu hình Máy chủ](configuration.md)):

Key | Mô tả
----|-------------
`VECTOR_EMBEDDING_MODEL` | Tên mô hình để truyền cho nhà cung cấp từ xa
`VECTOR_EMBEDDING_BASE_URL` | URL cơ sở của API từ xa
`VECTOR_EMBEDDING_API_KEY` | Khóa API (chỉ cần nếu nhà cung cấp yêu cầu xác thực)

#### Sử dụng Ollama cho nhúng

Khi triển khai Gramps Web với Docker Compose, bạn có thể thêm một dịch vụ Ollama và sử dụng nó cho cả nhúng và (tùy chọn) LLM:

```yaml
services:
  grampsweb: &grampsweb
    # ... cấu hình hiện tại ...
    environment:
      GRAMPSWEB_VECTOR_EMBEDDING_MODEL: nomic-embed-text
      GRAMPSWEB_VECTOR_EMBEDDING_BASE_URL: http://ollama:11434

  grampsweb_celery: &grampsweb_celery
    # ... cấu hình hiện tại ...
    environment:
      GRAMPSWEB_VECTOR_EMBEDDING_MODEL: nomic-embed-text
      GRAMPSWEB_VECTOR_EMBEDDING_BASE_URL: http://ollama:11434

  ollama:
    image: ollama/ollama
    container_name: ollama
    ports:
      - "11434:11434"
    volumes:
      - ollama_data:/root/.ollama

volumes:
  ollama_data:
```

Sau khi khởi động các dịch vụ, kéo mô hình nhúng vào Ollama:

```bash
docker compose exec ollama ollama pull nomic-embed-text
```

!!! info
    Khi sử dụng Ollama cho nhúng, thư viện Sentence Transformers và PyTorch không cần thiết, điều này giảm đáng kể việc sử dụng bộ nhớ của các worker Gramps Web API.

#### Sử dụng OpenAI cho nhúng

Để sử dụng API nhúng OpenAI, hãy thiết lập URL cơ sở đến API OpenAI và cung cấp khóa API của bạn:

```yaml
environment:
  GRAMPSWEB_VECTOR_EMBEDDING_MODEL: text-embedding-3-small
  GRAMPSWEB_VECTOR_EMBEDDING_BASE_URL: https://api.openai.com
  GRAMPSWEB_VECTOR_EMBEDDING_API_KEY: sk-...
```

!!! warning
    Thay đổi mô hình nhúng yêu cầu tái lập chỉ mục tất cả các hồ sơ cho cây của bạn (hoặc tất cả các cây trong một thiết lập đa cây), vì các mô hình khác nhau tạo ra các vector với các kích thước khác nhau.

## Thiết lập nhà cung cấp LLM

Giao tiếp với LLM sử dụng khung AI Pydantic, hỗ trợ các API tương thích với OpenAI. Điều này cho phép sử dụng một LLM được triển khai cục bộ qua Ollama (xem [Tính tương thích OpenAI của Ollama](https://ollama.com/blog/openai-compatibility)) hoặc các API được lưu trữ như OpenAI, Anthropic hoặc Hugging Face TGI (Dự đoán Tạo văn bản). LLM được cấu hình qua các tham số cấu hình `LLM_MODEL` và `LLM_BASE_URL`.

### Sử dụng LLM được lưu trữ qua API OpenAI

Khi sử dụng API OpenAI, `LLM_BASE_URL` có thể để trống, trong khi `LLM_MODEL` phải được thiết lập thành một trong các mô hình OpenAI, ví dụ: `gpt-4o-mini`. LLM sử dụng khả năng gọi công cụ để trả lời câu hỏi: nó truy vấn cơ sở dữ liệu trực tiếp bằng cách sử dụng các công cụ chuyên biệt và trả lời dựa trên các hồ sơ mà nó tìm thấy. Nó không yêu cầu kiến thức sâu về gia phả hoặc lịch sử. Do đó, bạn có thể thử xem một mô hình nhỏ/rẻ có đủ không.

Bạn cũng sẽ cần đăng ký một tài khoản, lấy một khóa API và lưu nó trong biến môi trường `OPENAI_API_KEY`.

!!! info
    `LLM_MODEL` là một tham số cấu hình; nếu bạn muốn thiết lập nó qua một biến môi trường, hãy sử dụng `GRAMPSWEB_LLM_MODEL` (xem [Cấu hình](configuration.md)). `OPENAI_API_KEY` không phải là một tham số cấu hình mà là một biến môi trường được thư viện Pydantic AI sử dụng trực tiếp, vì vậy nó không nên có tiền tố.

### Sử dụng Mistral AI

Để sử dụng các mô hình được lưu trữ của Mistral AI, hãy thêm tiền tố `mistral:` vào tên mô hình khi thiết lập `LLM_MODEL`.

Bạn sẽ cần đăng ký một tài khoản Mistral AI, lấy một khóa API và lưu nó trong biến môi trường `MISTRAL_API_KEY`. Không cần thiết lập `LLM_BASE_URL` vì Pydantic AI sẽ tự động sử dụng điểm cuối API Mistral chính xác.

Ví dụ cấu hình khi sử dụng docker compose với các biến môi trường:
```yaml
environment:
  GRAMPSWEB_LLM_MODEL: mistral:mistral-large-latest
  MISTRAL_API_KEY: your-mistral-api-key-here
```

### Sử dụng LLM cục bộ qua Ollama

[Ollama](https://ollama.com/) là một cách thuận tiện để chạy LLM cục bộ. Vui lòng tham khảo tài liệu của Ollama để biết chi tiết. Lưu ý rằng LLM yêu cầu tài nguyên tính toán đáng kể và tất cả các mô hình lớn hơn sẽ có thể quá chậm nếu không có hỗ trợ GPU. Vì trợ lý dựa vào khả năng gọi công cụ, hãy chọn một mô hình hỗ trợ công cụ, chẳng hạn như [`qwen2.5`](https://ollama.com/library/qwen2.5). Bắt đầu với một biến thể nhỏ như `qwen2.5:7b` và thử một cái lớn hơn nếu các câu trả lời không đủ tốt. Vui lòng chia sẻ bất kỳ kinh nghiệm nào với cộng đồng!

Khi triển khai Gramps Web với Docker Compose, bạn có thể thêm một dịch vụ Ollama và chỉ định Gramps Web đến nó:

```yaml
services:
  grampsweb: &grampsweb
    # ... cấu hình hiện tại ...
    environment:
      GRAMPSWEB_LLM_MODEL: ollama:qwen2.5:7b
      GRAMPSWEB_LLM_BASE_URL: http://ollama:11434/v1/

  grampsweb_celery: &grampsweb_celery
    # ... cấu hình hiện tại ...
    environment:
      GRAMPSWEB_LLM_MODEL: ollama:qwen2.5:7b
      GRAMPSWEB_LLM_BASE_URL: http://ollama:11434/v1/

  ollama:
    image: ollama/ollama
    container_name: ollama
    ports:
      - "11434:11434"
    volumes:
      - ollama_data:/root/.ollama

volumes:
  ollama_data:
```

Sau khi khởi động các dịch vụ, kéo mô hình vào Ollama:

```bash
docker compose exec ollama ollama pull qwen2.5:7b
```

Một vài điều cần lưu ý:

- Đặt `LLM_MODEL` thành tên mô hình Ollama, bao gồm cả thẻ của nó (phần sau dấu hai chấm, ví dụ: `7b`), được tiền tố bằng `ollama:`. Tiền tố này khiến Pydantic AI sử dụng các cài đặt riêng cho mô hình Ollama, đây là cấu hình được khuyến nghị.
- `LLM_BASE_URL` phải kết thúc bằng `/v1/`, ví dụ: `http://ollama:11434/v1/`.
- Với tiền tố `ollama:`, không cần thiết phải có `OPENAI_API_KEY` hay biến môi trường `OLLAMA_BASE_URL`. Nếu `LLM_BASE_URL` không được thiết lập, Gramps Web sẽ quay lại `OLLAMA_BASE_URL`.
- Ngoài ra, bạn có thể bỏ qua tiền tố (ví dụ: `LLM_MODEL: qwen2.5:7b`) và sử dụng Ollama thông qua API tương thích với OpenAI của nó. Trong trường hợp này, bạn cũng phải thiết lập biến môi trường `OPENAI_API_KEY` thành `ollama` (bất kỳ giá trị không rỗng nào cũng hoạt động).

Để khắc phục sự cố với Ollama, bạn có thể bật ghi nhật ký gỡ lỗi bằng cách thiết lập biến môi trường `OLLAMA_DEBUG=1` trong môi trường dịch vụ Ollama.

!!! info
    Nếu bạn đang sử dụng Ollama cho trò chuyện AI của Gramps Web, vui lòng hỗ trợ cộng đồng bằng cách hoàn thiện tài liệu này với bất kỳ chi tiết nào còn thiếu.

### Sử dụng các nhà cung cấp khác

Xin vui lòng gửi tài liệu cho các nhà cung cấp khác và chia sẻ kinh nghiệm của bạn với cộng đồng!
