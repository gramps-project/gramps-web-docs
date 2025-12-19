# Thiết lập trò chuyện AI

!!! info
    Trò chuyện AI yêu cầu Gramps Web API phiên bản 2.5.0 hoặc cao hơn. Phiên bản 3.6.0 đã giới thiệu khả năng gọi công cụ để tương tác thông minh hơn.

Gramps Web API hỗ trợ việc đặt câu hỏi về cơ sở dữ liệu gia phả bằng cách sử dụng các mô hình ngôn ngữ lớn (LLM) thông qua một kỹ thuật gọi là tạo ra tăng cường truy xuất (RAG) kết hợp với gọi công cụ.

## Cách hoạt động

Trợ lý AI sử dụng hai phương pháp bổ sung:

**Tạo ra tăng cường truy xuất (RAG)**: Một *mô hình nhúng vector* tạo ra một chỉ mục của tất cả các đối tượng trong cơ sở dữ liệu Gramps dưới dạng các vector số mã hóa ý nghĩa của các đối tượng. Khi người dùng đặt câu hỏi, câu hỏi đó cũng được chuyển đổi thành một vector và so sánh với các đối tượng trong cơ sở dữ liệu. Tìm kiếm *ngữ nghĩa* này trả về các đối tượng có ý nghĩa tương tự nhất với câu hỏi.

**Gọi Công Cụ (v3.6.0+)**: Trợ lý AI hiện có thể sử dụng các công cụ chuyên biệt để truy vấn dữ liệu gia phả của bạn trực tiếp. Những công cụ này cho phép trợ lý tìm kiếm cơ sở dữ liệu, lọc người/sự kiện/gia đình/nơi chốn theo các tiêu chí cụ thể, tính toán mối quan hệ giữa các cá nhân và lấy thông tin chi tiết về đối tượng. Điều này giúp trợ lý có khả năng trả lời các câu hỏi gia phả phức tạp một cách chính xác hơn.

Để kích hoạt điểm cuối trò chuyện trong Gramps Web API, cần thực hiện ba bước:

1. Cài đặt các phụ thuộc cần thiết,
2. Kích hoạt tìm kiếm ngữ nghĩa,
3. Thiết lập nhà cung cấp LLM.

Ba bước này được mô tả dưới đây lần lượt. Cuối cùng, một chủ sở hữu hoặc quản trị viên phải [cấu hình người dùng nào có thể truy cập tính năng trò chuyện](users.md#configuring-who-can-use-ai-chat) trong cài đặt Quản lý Người dùng.

## Cài đặt các phụ thuộc cần thiết

Trò chuyện AI yêu cầu các thư viện Sentence Transformers và PyTorch được cài đặt.

Các hình ảnh docker tiêu chuẩn cho Gramps Web đã có sẵn các thư viện này được cài đặt sẵn cho các kiến trúc `amd64` (ví dụ: PC để bàn 64-bit) và `arm64` (ví dụ: Raspberry Pi 64-bit). Thật không may, trò chuyện AI không được hỗ trợ trên kiến trúc `armv7` (ví dụ: Raspberry Pi 32-bit) do thiếu hỗ trợ PyTorch.

Khi cài đặt Gramps Web API qua `pip` (điều này không cần thiết khi sử dụng các hình ảnh Docker), các phụ thuộc cần thiết được cài đặt với

```bash
pip install gramps_webapi[ai]
```

## Kích hoạt tìm kiếm ngữ nghĩa

Nếu các phụ thuộc cần thiết đã được cài đặt, việc kích hoạt tìm kiếm ngữ nghĩa có thể đơn giản như việc thiết lập tùy chọn cấu hình `VECTOR_EMBEDDING_MODEL` (ví dụ: bằng cách thiết lập biến môi trường `GRAMPSWEB_VECTOR_EMBEDDING_MODEL`), xem [Cấu hình Máy chủ](configuration.md). Đây có thể là bất kỳ chuỗi nào của một mô hình được hỗ trợ bởi thư viện [Sentence Transformers](https://sbert.net/). Xem tài liệu của dự án này để biết chi tiết và các mô hình có sẵn.

!!! warning
    Lưu ý rằng các hình ảnh docker mặc định không bao gồm một phiên bản PyTorch có hỗ trợ GPU. Nếu bạn có quyền truy cập vào GPU (điều này sẽ tăng tốc độ lập chỉ mục ngữ nghĩa một cách đáng kể), vui lòng cài đặt phiên bản PyTorch có hỗ trợ GPU.

Có một số điều cần cân nhắc khi chọn mô hình.

- Khi bạn thay đổi mô hình, bạn phải tự tay tái tạo chỉ mục tìm kiếm ngữ nghĩa cho cây của bạn (hoặc tất cả các cây trong một thiết lập đa cây), nếu không bạn sẽ gặp phải lỗi hoặc kết quả vô nghĩa.
- Các mô hình là một sự đánh đổi giữa độ chính xác/tính tổng quát ở một bên và thời gian tính toán/không gian lưu trữ ở bên kia. Nếu bạn không chạy Gramps Web API trên một hệ thống có quyền truy cập vào một GPU mạnh mẽ, các mô hình lớn thường quá chậm trong thực tế.
- Trừ khi toàn bộ cơ sở dữ liệu của bạn là tiếng Anh và tất cả người dùng của bạn chỉ được mong đợi đặt câu hỏi trò chuyện bằng tiếng Anh, bạn sẽ cần một mô hình nhúng đa ngôn ngữ, mà hiếm hơn so với các mô hình tiếng Anh thuần túy.

Nếu mô hình không có trong bộ nhớ cache cục bộ, nó sẽ được tải xuống khi Gramps Web API được khởi động lần đầu tiên với cấu hình mới. Mô hình `sentence-transformers/distiluse-base-multilingual-cased-v2` đã có sẵn cục bộ khi sử dụng các hình ảnh docker tiêu chuẩn. Mô hình này là một điểm khởi đầu tốt và hỗ trợ đầu vào đa ngôn ngữ.

Hãy chia sẻ những hiểu biết về các mô hình khác nhau với cộng đồng!

!!! info
    Thư viện sentence transformers tiêu tốn một lượng lớn bộ nhớ, điều này có thể khiến các quy trình làm việc bị giết. Như một quy tắc chung, với tìm kiếm ngữ nghĩa được kích hoạt, mỗi quy trình Gunicorn tiêu tốn khoảng 200 MB bộ nhớ và mỗi quy trình celery khoảng 500 MB bộ nhớ ngay cả khi không hoạt động, và lên đến 1 GB khi tính toán nhúng. Xem [Giới hạn CPU và sử dụng bộ nhớ](cpu-limited.md) để biết các cài đặt giới hạn sử dụng bộ nhớ. Ngoài ra, nên cung cấp một phân vùng hoán đổi đủ lớn để ngăn ngừa lỗi OOM do các đỉnh sử dụng bộ nhớ tạm thời.

## Thiết lập nhà cung cấp LLM

Giao tiếp với LLM sử dụng khung Pydantic AI, hỗ trợ các API tương thích với OpenAI. Điều này cho phép sử dụng một LLM được triển khai cục bộ qua Ollama (xem [Tính tương thích OpenAI của Ollama](https://ollama.com/blog/openai-compatibility)) hoặc các API được lưu trữ như OpenAI, Anthropic hoặc Hugging Face TGI (Text Generation Inference). LLM được cấu hình qua các tham số cấu hình `LLM_MODEL` và `LLM_BASE_URL`.

### Sử dụng LLM được lưu trữ qua API OpenAI

Khi sử dụng API OpenAI, `LLM_BASE_URL` có thể để trống, trong khi `LLM_MODEL` phải được thiết lập thành một trong các mô hình của OpenAI, ví dụ: `gpt-4o-mini`. LLM sử dụng cả RAG và gọi công cụ để trả lời các câu hỏi: nó chọn thông tin liên quan từ các kết quả tìm kiếm ngữ nghĩa và có thể truy vấn trực tiếp cơ sở dữ liệu bằng cách sử dụng các công cụ chuyên biệt. Nó không yêu cầu kiến thức sâu về gia phả hoặc lịch sử. Do đó, bạn có thể thử xem một mô hình nhỏ/rẻ có đủ không.

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
  GRAMPSWEB_VECTOR_EMBEDDING_MODEL: sentence-transformers/distiluse-base-multilingual-cased-v2
```

### Sử dụng LLM cục bộ qua Ollama

[Ollama](https://ollama.com/) là một cách thuận tiện để chạy LLM cục bộ. Vui lòng tham khảo tài liệu của Ollama để biết chi tiết. Xin lưu ý rằng LLM yêu cầu tài nguyên tính toán đáng kể và tất cả các mô hình lớn hơn sẽ có thể quá chậm nếu không có hỗ trợ GPU. Bạn có thể thử xem [`tinyllama`](https://ollama.com/library/tinyllama) có đáp ứng nhu cầu của bạn không. Nếu không, hãy thử một trong các mô hình lớn hơn. Hãy chia sẻ bất kỳ kinh nghiệm nào với cộng đồng!

Khi triển khai Gramps Web với Docker Compose, bạn có thể thêm một dịch vụ Ollama

```yaml
services:
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

và sau đó thiết lập tham số cấu hình `LLM_BASE_URL` thành `http://ollama:11434/v1`. Thiết lập `LLM_MODEL` thành một mô hình được Ollama hỗ trợ và tải nó xuống trong container của bạn với `ollama pull <model>`. Cuối cùng, thiết lập `OPENAI_API_KEY` thành `ollama`.

Để khắc phục sự cố với Ollama, bạn có thể kích hoạt ghi nhật ký gỡ lỗi bằng cách thiết lập biến môi trường `OLLAMA_DEBUG=1` trong môi trường dịch vụ Ollama.

!!! info
    Nếu bạn đang sử dụng Ollama cho trò chuyện AI Gramps Web, hãy hỗ trợ cộng đồng bằng cách hoàn thiện tài liệu này với bất kỳ chi tiết nào còn thiếu.

### Sử dụng các nhà cung cấp khác

Xin vui lòng gửi tài liệu cho các nhà cung cấp khác và chia sẻ kinh nghiệm của bạn với cộng đồng!
