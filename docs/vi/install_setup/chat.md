# Thiết lập trò chuyện AI

!!! info
    Trò chuyện AI yêu cầu Gramps Web API phiên bản 2.5.0 hoặc cao hơn.


Gramps Web API hỗ trợ việc đặt câu hỏi về cơ sở dữ liệu gia phả bằng cách sử dụng các mô hình ngôn ngữ lớn (LLM) thông qua một kỹ thuật gọi là tạo ra tăng cường truy xuất (RAG).

RAG hoạt động như sau. Đầu tiên, một *mô hình nhúng vector* được sử dụng để tạo ra một chỉ mục của tất cả các đối tượng trong cơ sở dữ liệu Gramps dưới dạng các vector số, mã hóa ý nghĩa của các đối tượng. Quy trình này tương tự như việc tạo chỉ mục tìm kiếm toàn văn, nhưng tốn kém về mặt tính toán hơn.

Tiếp theo, khi một người dùng đặt câu hỏi qua điểm cuối trò chuyện, câu hỏi đó cũng được chuyển đổi thành một vector, bởi cùng một mô hình nhúng, và so sánh với các đối tượng trong cơ sở dữ liệu Gramps. Tìm kiếm *ngữ nghĩa* này sẽ trả về các đối tượng trong cơ sở dữ liệu mà có sự tương đồng ngữ nghĩa nhất với câu hỏi.

Trong bước cuối cùng, câu hỏi và các đối tượng được truy xuất sẽ được gửi đến một LLM để xây dựng câu trả lời dựa trên thông tin đã cung cấp. Bằng cách này, chatbot có quyền truy cập vào thông tin chi tiết về nội dung của cơ sở dữ liệu gia phả thay vì chỉ dựa vào kiến thức có sẵn.

Để kích hoạt điểm cuối trò chuyện trong Gramps Web API, cần thực hiện ba bước:

1. Cài đặt các phụ thuộc cần thiết,
2. Kích hoạt tìm kiếm ngữ nghĩa,
3. Thiết lập nhà cung cấp LLM.

Ba bước này được mô tả dưới đây. Cuối cùng, một chủ sở hữu hoặc quản trị viên phải [cấu hình ai có thể truy cập tính năng trò chuyện](users.md#configuring-who-can-use-ai-chat) trong cài đặt Quản lý Người dùng.

## Cài đặt các phụ thuộc cần thiết

Trò chuyện AI yêu cầu các thư viện Sentence Transformers và PyTorch được cài đặt.

Các hình ảnh docker tiêu chuẩn cho Gramps Web đã có sẵn các thư viện này được cài đặt sẵn cho các kiến trúc `amd64` (ví dụ: PC để bàn 64-bit) và `arm64` (ví dụ: Raspberry Pi 64-bit). Thật không may, trò chuyện AI không được hỗ trợ trên kiến trúc `armv7` (ví dụ: Raspberry Pi 32-bit) do thiếu hỗ trợ PyTorch.

Khi cài đặt Gramps Web API qua `pip` (điều này không cần thiết khi sử dụng các hình ảnh Docker), các phụ thuộc cần thiết được cài đặt với

```bash
pip install gramps_webapi[ai]
```


## Kích hoạt tìm kiếm ngữ nghĩa

Nếu các phụ thuộc cần thiết đã được cài đặt, việc kích hoạt tìm kiếm ngữ nghĩa có thể đơn giản như việc thiết lập tùy chọn cấu hình `VECTOR_EMBEDDING_MODEL` (ví dụ: bằng cách thiết lập biến môi trường `GRAMPSWEB_VECTOR_EMBEDDING_MODEL`), xem [Cấu hình Máy chủ](configuration.md). Điều này có thể là bất kỳ chuỗi nào của một mô hình được hỗ trợ bởi thư viện [Sentence Transformers](https://sbert.net/). Xem tài liệu của dự án này để biết chi tiết và các mô hình có sẵn.


!!! warning
    Lưu ý rằng các hình ảnh docker mặc định không bao gồm phiên bản PyTorch có hỗ trợ GPU. Nếu bạn có quyền truy cập vào GPU (sẽ tăng tốc độ lập chỉ mục ngữ nghĩa đáng kể), vui lòng cài đặt phiên bản PyTorch có hỗ trợ GPU.

Có một số điều cần xem xét khi chọn mô hình.

- Khi bạn thay đổi mô hình, bạn phải tự tay tái tạo chỉ mục tìm kiếm ngữ nghĩa cho cây của bạn (hoặc tất cả các cây trong một thiết lập đa cây), nếu không bạn sẽ gặp lỗi hoặc kết quả vô nghĩa.
- Các mô hình là một sự đánh đổi giữa độ chính xác/tính tổng quát ở một bên và thời gian tính toán/kho lưu trữ ở bên kia. Nếu bạn không chạy Gramps Web API trên một hệ thống có quyền truy cập vào một GPU mạnh mẽ, các mô hình lớn thường quá chậm trong thực tế.
- Trừ khi toàn bộ cơ sở dữ liệu của bạn là tiếng Anh và tất cả người dùng của bạn chỉ được mong đợi đặt câu hỏi trò chuyện bằng tiếng Anh, bạn sẽ cần một mô hình nhúng đa ngôn ngữ, mà hiếm hơn so với các mô hình tiếng Anh thuần túy.


Nếu mô hình không có trong bộ nhớ cache cục bộ, nó sẽ được tải xuống khi Gramps Web API được khởi động lần đầu tiên với cấu hình mới. Mô hình `sentence-transformers/distiluse-base-multilingual-cased-v2` đã có sẵn cục bộ khi sử dụng các hình ảnh docker tiêu chuẩn. Mô hình này là một điểm khởi đầu tốt và hỗ trợ đầu vào đa ngôn ngữ.

Hãy chia sẻ những hiểu biết về các mô hình khác nhau với cộng đồng!

!!! info
    Thư viện sentence transformers tiêu tốn một lượng lớn bộ nhớ, điều này có thể khiến các tiến trình làm việc bị giết. Như một quy tắc chung, với tìm kiếm ngữ nghĩa được kích hoạt, mỗi tiến trình Gunicorn tiêu tốn khoảng 200 MB bộ nhớ và mỗi tiến trình celery khoảng 500 MB bộ nhớ ngay cả khi không hoạt động, và lên tới 1 GB khi tính toán các nhúng. Xem [Giới hạn CPU và sử dụng bộ nhớ](cpu-limited.md) để biết các cài đặt giới hạn việc sử dụng bộ nhớ. Ngoài ra, nên cung cấp một phân vùng hoán đổi đủ lớn để ngăn chặn lỗi OOM do các đợt tăng đột biến sử dụng bộ nhớ tạm thời.

## Thiết lập nhà cung cấp LLM

Giao tiếp với LLM sử dụng API tương thích với OpenAI thông qua thư viện `openai-python`. Điều này cho phép sử dụng một LLM được triển khai cục bộ qua Ollama (xem [Tính tương thích OpenAI của Ollama](https://ollama.com/blog/openai-compatibility)) hoặc một API như OpenAI hoặc Hugging Face TGI (Text Generation Inference). LLM được cấu hình thông qua các tham số cấu hình `LLM_MODEL` và `LLM_BASE_URL`.


### Sử dụng LLM được lưu trữ qua API OpenAI

Khi sử dụng API OpenAI, `LLM_BASE_URL` có thể để trống, trong khi `LLM_MODEL` phải được thiết lập thành một trong các mô hình OpenAI, ví dụ: `gpt-4o-mini`. Lưu ý rằng, do phương pháp RAG, LLM "chỉ" được sử dụng để chọn thông tin đúng từ các kết quả tìm kiếm ngữ nghĩa và xây dựng câu trả lời, nó không yêu cầu kiến thức sâu về gia phả hoặc lịch sử. Do đó, bạn có thể thử xem một mô hình nhỏ/giá rẻ có đủ không.

Bạn cũng sẽ cần đăng ký một tài khoản, lấy một khóa API và lưu nó trong biến môi trường `OPENAI_API_KEY`.

!!! info
    `LLM_MODEL` là một tham số cấu hình; nếu bạn muốn thiết lập nó qua một biến môi trường, hãy sử dụng `GRAMPSWEB_LLM_MODEL` (xem [Cấu hình](configuration.md)). `OPENAI_API_KEY` không phải là một tham số cấu hình mà là một biến môi trường được thư viện `openai-python` sử dụng trực tiếp, vì vậy nó không nên có tiền tố.


### Sử dụng LLM cục bộ qua Ollama

[Ollama](https://ollama.com/) là một cách thuận tiện để chạy LLM cục bộ. Vui lòng tham khảo tài liệu của Ollama để biết chi tiết. Lưu ý rằng LLM yêu cầu tài nguyên tính toán đáng kể và tất cả các mô hình lớn hơn nhỏ nhất có thể sẽ quá chậm mà không có hỗ trợ GPU. Bạn có thể thử xem [`tinyllama`](https://ollama.com/library/tinyllama) có đáp ứng nhu cầu của bạn không. Nếu không, hãy thử một trong các mô hình lớn hơn. Hãy chia sẻ bất kỳ kinh nghiệm nào với cộng đồng!

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

và sau đó thiết lập tham số cấu hình `LLM_BASE_URL` thành `http://ollama:11434/v1`. Thiết lập `LLM_MODEL` thành một mô hình được Ollama hỗ trợ, và tải nó xuống trong container của bạn với `ollama pull <model>`. Cuối cùng, thiết lập `OPENAI_API_KEY` thành `ollama`.

Để khắc phục sự cố với Ollama, bạn có thể kích hoạt ghi nhật ký gỡ lỗi bằng cách thiết lập biến môi trường `OLLAMA_DEBUG=1` trong môi trường dịch vụ Ollama.

!!! info
    Nếu bạn đang sử dụng Ollama cho trò chuyện AI Gramps Web, hãy hỗ trợ cộng đồng bằng cách hoàn thiện tài liệu này với bất kỳ chi tiết nào còn thiếu.

### Sử dụng các nhà cung cấp khác

Xin vui lòng gửi tài liệu cho các nhà cung cấp khác và chia sẻ kinh nghiệm của bạn với cộng đồng!
