# AI sohbeti kurma

!!! bilgi
    AI sohbeti, Gramps Web API sürüm 2.5.0 veya daha yüksek bir sürüm gerektirir. Sürüm 3.6.0, daha akıllı etkileşimler için araç çağırma yetenekleri tanıttı.

Gramps Web API, büyük dil modelleri (LLM) ile araç çağırma kullanarak soybilim veritabanı hakkında soru sormayı destekler.

## Nasıl çalışır

AI asistanı, soybilim verilerinizi doğrudan sorgulamak için özel araçlar kullanır. Bu araçlar, asistanın veritabanında tam metin araması yapmasına, belirli kriterlere göre insanlar/olaylar/aileler/yerler filtrelemesine, bireyler arasındaki ilişkileri hesaplamasına ve notlar dahil olmak üzere tam kayıtları almasına olanak tanır. Asistan, baktığı kayıtlara dayanarak yanıt verir ve yanıtında bu kayıtlara bağlantılar sağlar. Sadece ağaçtan yanıt verir, genel bilgiden değil: eğer ağaçta bir şey kaydedilmemişse, asistan bunu belirtir. Mevcut olmayan veya kullanıcı için özel olan nesnelere bağlantılar, metinleriyle değiştirilir.

AI sohbetinin bir vektör gömme modeline ihtiyacı yoktur. Gramps Web API'nin 3.24 öncesi sürümleri, veritabanındaki tüm nesneler için hesaplanan sayısal vektörlerin bir dizini ile bir sorunun anlamını karşılaştıran *anlamsal arama* (retrieval-augmented generation, RAG) kullanıyordu. Anlamsal arama, Gramps Web API 3.25'te kaldırılmıştır; `VECTOR_EMBEDDING_MODEL`, `VECTOR_EMBEDDING_BASE_URL` ve `VECTOR_EMBEDDING_API_KEY` ayarları göz ardı edilir ve yapılandırmanızdan kaldırılabilir.

Gramps Web API'de sohbet uç noktasını etkinleştirmek için iki adım gereklidir:

1. Gerekli bağımlılıkların yüklenmesi,
2. Bir LLM sağlayıcısının ayarlanması.

Bu iki adım aşağıda sırayla açıklanmıştır. Son olarak, bir sahip veya yönetici, [kullanıcıların sohbet özelliğine erişimini yapılandırmalıdır](users.md#configuring-who-can-use-ai-chat) Kullanıcıları Yönet ayarlarında.

## Gerekli bağımlılıkların yüklenmesi

Gramps Web için standart docker görüntüleri, AI sohbeti için gerekli tüm bağımlılıkları önceden yüklenmiş olarak içerir.

Gramps Web API'yi `pip` ile yüklerken (Docker görüntülerini kullanırken bu gerekli değildir) gerekli bağımlılıklar şu komutla yüklenir:

```bash
pip install gramps_webapi[ai]
```

## Bir LLM sağlayıcısının ayarlanması

LLM ile iletişim, OpenAI uyumlu API'leri destekleyen Pydantic AI çerçevesini kullanır. Bu, yerel olarak dağıtılmış bir LLM'nin Ollama aracılığıyla (bkz. [Ollama OpenAI uyumluluğu](https://ollama.com/blog/openai-compatibility)) veya OpenAI, Anthropic veya Hugging Face TGI (Metin Üretim Çıkarımı) gibi barındırılan API'ler aracılığıyla kullanılmasına olanak tanır. LLM, `LLM_MODEL` ve `LLM_BASE_URL` yapılandırma parametreleri aracılığıyla yapılandırılır.

OpenAI uyumlu API'lerin yanı sıra, Pydantic AI için sağlayıcıya özgü model ön ekleri OpenAI, Anthropic, Google, Mistral, Groq, AWS Bedrock ve Ollama için kullanılabilir. Cohere, Hugging Face ve xAI gibi diğer sağlayıcılar yüklenmemiştir; ancak Hugging Face Çıkarım Sağlayıcıları, OpenAI uyumlu uç noktaları aracılığıyla kullanılabilir (`LLM_BASE_URL` `https://router.huggingface.co/v1` olarak ayarlandığında).

Model sunucunuz bir yanıtın uzunluğunu sınırlamıyorsa, `LLM_MAX_OUTPUT_TOKENS`'ı modelin her yanıt için üretebileceği maksimum token sayısına ayarlayın (bkz. [Yapılandırma](configuration.md)).

### OpenAI API aracılığıyla barındırılan bir LLM kullanma

OpenAI API'sini kullanırken, `LLM_BASE_URL` ayarsız bırakılabilir, ancak `LLM_MODEL` OpenAI modellerinden birine, örneğin `gpt-4o-mini` olarak ayarlanmalıdır. LLM, soruları yanıtlamak için araç çağırma kullanır: veritabanını doğrudan özel araçlar kullanarak sorgular ve bulduğu kayıtlara dayanarak yanıt verir. Derin soybilimsel veya tarihsel bilgi gerektirmez. Bu nedenle, küçük/ucuz bir modelin yeterli olup olmadığını deneyebilirsiniz.

Ayrıca bir hesap oluşturmanız, bir API anahtarı almanız ve bunu `OPENAI_API_KEY` ortam değişkeninde saklamanız gerekecektir.

!!! bilgi
    `LLM_MODEL` bir yapılandırma parametresidir; eğer bunu bir ortam değişkeni aracılığıyla ayarlamak istiyorsanız, `GRAMPSWEB_LLM_MODEL` kullanın (bkz. [Yapılandırma](configuration.md)). `OPENAI_API_KEY` bir yapılandırma parametresi değil, Pydantic AI kütüphanesi tarafından doğrudan kullanılan bir ortam değişkenidir, bu nedenle ön ek kullanılmamalıdır.

### Mistral AI kullanma

Mistral AI'nın barındırılan modellerini kullanmak için, `LLM_MODEL` ayarını yaparken model adının önüne `mistral:` ekleyin.

Bir Mistral AI hesabı oluşturmanız, bir API anahtarı almanız ve bunu `MISTRAL_API_KEY` ortam değişkeninde saklamanız gerekecektir. Pydantic AI, doğru Mistral API uç noktasını otomatik olarak kullanacağından `LLM_BASE_URL` ayarlamanıza gerek yoktur.

Ortam değişkenleri ile docker compose kullanırken örnek yapılandırma:
```yaml
environment:
  GRAMPSWEB_LLM_MODEL: mistral:mistral-large-latest
  MISTRAL_API_KEY: your-mistral-api-key-here
```

### Ollama aracılığıyla yerel bir LLM kullanma

[Ollama](https://ollama.com/) LLM'leri yerel olarak çalıştırmanın pratik bir yoludur. Detaylar için Ollama belgelerine başvurun. LLM'lerin önemli hesaplama kaynaklarına ihtiyaç duyduğunu ve en küçük modeller dışında tüm modellerin GPU desteği olmadan muhtemelen çok yavaş olacağını lütfen unutmayın. Asistan araç çağırmaya dayandığı için, [`qwen2.5`](https://ollama.com/library/qwen2.5) gibi araçları destekleyen bir model seçin. `qwen2.5:7b` gibi küçük bir varyantla başlayın ve yanıtlar yeterince iyi değilse daha büyük bir model deneyin. Lütfen deneyimlerinizi toplulukla paylaşın!

Gramps Web'i Docker Compose ile dağıtırken, bir Ollama servisi ekleyebilir ve Gramps Web'i ona yönlendirebilirsiniz:

```yaml
services:
  grampsweb: &grampsweb
    # ... mevcut yapılandırma ...
    environment:
      GRAMPSWEB_LLM_MODEL: ollama:qwen2.5:7b
      GRAMPSWEB_LLM_BASE_URL: http://ollama:11434/v1/

  grampsweb_celery: &grampsweb_celery
    # ... mevcut yapılandırma ...
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

Servisleri başlattıktan sonra, modeli Ollama'ya çekin:

```bash
docker compose exec ollama ollama pull qwen2.5:7b
```

Dikkat edilmesi gereken birkaç şey:

- `LLM_MODEL`'i, etiketini (noktalı kısmı, örneğin `7b`) içerecek şekilde, `ollama:` ön eki ile ayarlayın. Ön ek, Pydantic AI'nın model için Ollama'ya özgü ayarlarını kullanmasını sağlar, bu önerilen ayardır.
- `LLM_BASE_URL` `/v1/` ile bitmelidir, örneğin `http://ollama:11434/v1/`.
- `ollama:` ön eki ile, `OPENAI_API_KEY` veya `OLLAMA_BASE_URL` ortam değişkenine ihtiyaç yoktur. Eğer `LLM_BASE_URL` ayarlanmamışsa, Gramps Web `OLLAMA_BASE_URL`'ye geri döner.
- Alternatif olarak, ön eki (örneğin `LLM_MODEL: qwen2.5:7b`) atlayabilir ve Ollama'yı genel OpenAI uyumlu API'si aracılığıyla kullanabilirsiniz. Bu durumda, `OPENAI_API_KEY` ortam değişkenini `ollama` (herhangi bir boş olmayan değer işe yarar) olarak ayarlamanız gerekir.

Ollama ile ilgili sorunları gidermek için, Ollama hizmeti ortamında `OLLAMA_DEBUG=1` ortam değişkenini ayarlayarak hata ayıklama günlüğünü etkinleştirebilirsiniz.

!!! bilgi
    Gramps Web AI sohbeti için Ollama kullanıyorsanız, lütfen topluluğu desteklemek için bu belgeleri eksik ayrıntılarla tamamlayın.

### Diğer sağlayıcıları kullanma

Lütfen diğer sağlayıcılar için belgeler göndermekten çekinmeyin ve deneyimlerinizi toplulukla paylaşın!
