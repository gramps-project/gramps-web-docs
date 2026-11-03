# Thiết lập trò chuyện AI

!!! info
    Trò chuyện AI yêu cầu Gramps Web API phiên bản 2.5.0 hoặc cao hơn. Phiên bản 3.6.0 đã giới thiệu khả năng gọi công cụ để tương tác thông minh hơn.

Gramps Web API hỗ trợ việc đặt câu hỏi về cơ sở dữ liệu gia phả bằng cách sử dụng các mô hình ngôn ngữ lớn (LLM) với khả năng gọi công cụ.

## Cách hoạt động

Trợ lý AI sử dụng các công cụ chuyên biệt để truy vấn dữ liệu gia phả của bạn trực tiếp. Những công cụ này cho phép trợ lý tìm kiếm cơ sở dữ liệu bằng cách tìm kiếm toàn văn, lọc người/sự kiện/gia đình/nơi chốn theo các tiêu chí cụ thể, tính toán mối quan hệ giữa các cá nhân và truy xuất các hồ sơ đầy đủ, bao gồm cả ghi chú. Sau đó, trợ lý trả lời dựa trên các hồ sơ mà nó đã tra cứu và liên kết đến chúng trong câu trả lời của mình. Nó chỉ trả lời từ cây gia phả, không từ kiến thức chung: nếu cây không ghi lại điều gì, trợ lý sẽ nói như vậy. Các liên kết đến các đối tượng không tồn tại hoặc riêng tư với người dùng sẽ được thay thế bằng văn bản của chúng.

Trò chuyện AI không cần một mô hình nhúng vector. Các phiên bản của Gramps Web API trước 3.24 cũng đã sử dụng *tìm kiếm ngữ nghĩa* (tạo ra thông tin tăng cường, RAG), so sánh ý nghĩa của một câu hỏi với một chỉ mục các vector số được tính toán cho tất cả các đối tượng trong cơ sở dữ liệu. Tìm kiếm ngữ nghĩa đã bị loại bỏ trong Gramps Web API 3.25; các cài đặt `VECTOR_EMBEDDING_MODEL`, `VECTOR_EMBEDDING_BASE_URL` và `VECTOR_EMBEDDING_API_KEY` sẽ bị bỏ qua và có thể được loại bỏ khỏi cấu hình của bạn.

Để kích hoạt điểm cuối trò chuyện trong Gramps Web API, cần thực hiện hai bước:

1. Cài đặt các phụ thuộc cần thiết,
2. Thiết lập nhà cung cấp LLM.

Hai bước này được mô tả dưới đây lần lượt. Cuối cùng, một chủ sở hữu hoặc quản trị viên phải [cấu hình ai có thể truy cập tính năng trò chuyện](users.md#configuring-who-can-use-ai-chat) trong cài đặt Quản lý Người dùng.

## Cài đặt các phụ thuộc cần thiết

Các hình ảnh docker tiêu chuẩn cho Gramps Web đã có sẵn tất cả các phụ thuộc cần thiết cho trò chuyện AI được cài đặt trước.

Khi cài đặt Gramps Web API thông qua `pip` (điều này không cần thiết khi sử dụng các hình ảnh Docker), các phụ thuộc cần thiết được cài đặt bằng

```bash
pip install gramps_webapi[ai]
```

## Thiết lập nhà cung cấp LLM

Giao tiếp với LLM sử dụng framework Pydantic AI, hỗ trợ các API tương thích với OpenAI. Điều này cho phép sử dụng một LLM được triển khai cục bộ qua Ollama (xem [Tính tương thích OpenAI của Ollama](https://ollama.com/blog/openai-compatibility)) hoặc các API được lưu trữ như OpenAI, Anthropic hoặc Hugging Face TGI (Text Generation Inference). LLM được cấu hình thông qua các tham số cấu hình `LLM_MODEL` và `LLM_BASE_URL`.

Ngoài các API tương thích với OpenAI, các tiền tố mô hình cụ thể của nhà cung cấp trong Pydantic AI có thể được sử dụng cho OpenAI, Anthropic, Google, Mistral, Groq, AWS Bedrock và Ollama. Các nhà cung cấp khác, chẳng hạn như Cohere, Hugging Face và xAI, không được cài đặt; các Nhà cung cấp Dự đoán của Hugging Face vẫn có thể được sử dụng thông qua điểm cuối tương thích với OpenAI của họ (`LLM_BASE_URL` được đặt thành `https://router.huggingface.co/v1`).

Nếu máy chủ mô hình của bạn không giới hạn độ dài của một phản hồi, hãy đặt `LLM_MAX_OUTPUT_TOKENS` thành số lượng tối đa các token mà mô hình có thể tạo ra cho mỗi phản hồi (xem [Cấu hình](configuration.md)).

### Sử dụng LLM được lưu trữ qua API OpenAI

Khi sử dụng API OpenAI, `LLM_BASE_URL` có thể để trống, trong khi `LLM_MODEL` phải được đặt thành một trong các mô hình OpenAI, ví dụ: `gpt-4o-mini`. LLM sử dụng khả năng gọi công cụ để trả lời các câu hỏi: nó truy vấn cơ sở dữ liệu trực tiếp bằng cách sử dụng các công cụ chuyên biệt và trả lời dựa trên các hồ sơ mà nó tìm thấy. Nó không yêu cầu kiến thức sâu về gia phả hoặc lịch sử. Do đó, bạn có thể thử xem một mô hình nhỏ/rẻ có đủ không.

Bạn cũng cần đăng ký một tài khoản, lấy một khóa API và lưu nó trong biến môi trường `OPENAI_API_KEY`.

!!! info
    `LLM_MODEL` là một tham số cấu hình; nếu bạn muốn đặt nó qua một biến môi trường, hãy sử dụng `GRAMPSWEB_LLM_MODEL` (xem [Cấu hình](configuration.md)). `OPENAI_API_KEY` không phải là một tham số cấu hình mà là một biến môi trường được thư viện Pydantic AI sử dụng trực tiếp, vì vậy nó không nên có tiền tố.

### Sử dụng Mistral AI

Để sử dụng các mô hình được lưu trữ của Mistral AI, hãy thêm tiền tố `mistral:` vào tên mô hình khi đặt `LLM_MODEL`.

Bạn sẽ cần đăng ký một tài khoản Mistral AI, lấy một khóa API và lưu nó trong biến môi trường `MISTRAL_API_KEY`. Không cần phải đặt `LLM_BASE_URL` vì Pydantic AI sẽ tự động sử dụng điểm cuối API Mistral chính xác.

Ví dụ cấu hình khi sử dụng docker compose với các biến môi trường:
```yaml
environment:
  GRAMPSWEB_LLM_MODEL: mistral:mistral-large-latest
  MISTRAL_API_KEY: your-mistral-api-key-here
```

### Sử dụng LLM cục bộ qua Ollama

[Ollama](https://ollama.com/) là một cách tiện lợi để chạy LLM cục bộ. Vui lòng tham khảo tài liệu của Ollama để biết chi tiết. Xin lưu ý rằng LLM yêu cầu tài nguyên tính toán đáng kể và tất cả các mô hình ngoài những mô hình nhỏ nhất có thể sẽ quá chậm mà không có hỗ trợ GPU. Vì trợ lý phụ thuộc vào khả năng gọi công cụ, hãy chọn một mô hình hỗ trợ công cụ, chẳng hạn như [`qwen2.5`](https://ollama.com/library/qwen2.5). Bắt đầu với một biến thể nhỏ như `qwen2.5:7b` và thử một cái lớn hơn nếu các câu trả lời không đủ tốt. Vui lòng chia sẻ bất kỳ trải nghiệm nào với cộng đồng!

Khi triển khai Gramps Web với Docker Compose, bạn có thể thêm một dịch vụ Ollama và chỉ định Gramps Web đến nó:

```yaml
services:
  grampsweb: &grampsweb
    # ... cấu hình hiện có ...
    environment:
      GRAMPSWEB_LLM_MODEL: ollama:qwen2.5:7b
      GRAMPSWEB_LLM_BASE_URL: http://ollama:11434/v1/

  grampsweb_celery: &grampsweb_celery
    # ... cấu hình hiện có ...
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

Sau khi khởi động các dịch vụ, hãy kéo mô hình vào Ollama:

```bash
docker compose exec ollama ollama pull qwen2.5:7b
```

Một vài điều cần lưu ý:

- Đặt `LLM_MODEL` thành tên mô hình Ollama, bao gồm cả thẻ của nó (phần sau dấu hai chấm, ví dụ: `7b`), được tiền tố bằng `ollama:`. Tiền tố này khiến Pydantic AI sử dụng các cài đặt cụ thể của Ollama cho mô hình, đây là cấu hình được khuyến nghị.
- `LLM_BASE_URL` phải kết thúc bằng `/v1/`, ví dụ: `http://ollama:11434/v1/`.
- Với tiền tố `ollama:`, không cần biến môi trường `OPENAI_API_KEY` hay `OLLAMA_BASE_URL`. Nếu `LLM_BASE_URL` không được đặt, Gramps Web sẽ quay lại `OLLAMA_BASE_URL`.
- Ngoài ra, bạn có thể bỏ qua tiền tố (ví dụ: `LLM_MODEL: qwen2.5:7b`) và sử dụng Ollama thông qua API tương thích với OpenAI của nó. Trong trường hợp này, bạn cũng phải đặt biến môi trường `OPENAI_API_KEY` thành `ollama` (bất kỳ giá trị không rỗng nào cũng hoạt động).

Để khắc phục sự cố với Ollama, bạn có thể kích hoạt ghi nhật ký gỡ lỗi bằng cách đặt biến môi trường `OLLAMA_DEBUG=1` trong môi trường dịch vụ Ollama.

!!! info
    Nếu bạn đang sử dụng Ollama cho trò chuyện AI Gramps Web, vui lòng hỗ trợ cộng đồng bằng cách hoàn thiện tài liệu này với bất kỳ chi tiết nào còn thiếu.

### Sử dụng các nhà cung cấp khác

Xin vui lòng gửi tài liệu cho các nhà cung cấp khác và chia sẻ trải nghiệm của bạn với cộng đồng!
