# AI sohbeti ayarlama

!!! bilgi
    AI sohbeti, Gramps Web API sürüm 2.5.0 veya daha yüksek bir sürüm gerektirir. Sürüm 3.6.0, daha akıllı etkileşimler için araç çağırma yetenekleri tanıttı.

Gramps Web API, büyük dil modelleri (LLM) aracılığıyla soybilim veritabanı hakkında sorular sormayı destekler ve bu, araç çağırma ile birleştirilmiş bir teknik olan retrieval-augmented generation (RAG) ile gerçekleştirilir.

## Nasıl çalışır

AI asistanı, iki tamamlayıcı yaklaşım kullanır:

**Retrieval-Augmented Generation (RAG)**: Bir *vektör gömme modeli*, Gramps veritabanındaki tüm nesnelerin anlamını kodlayan sayısal vektörler biçiminde bir dizin oluşturur. Bir kullanıcı bir soru sorduğunda, bu soru da bir vektöre dönüştürülür ve veritabanındaki nesnelerle karşılaştırılır. Bu *anlamsal arama*, soruyla en anlamsal olarak benzer nesneleri döndürür.

**Araç Çağırma (v3.6.0+)**: AI asistanı artık soybilim verilerinizi doğrudan sorgulamak için özel araçlar kullanabilir. Bu araçlar, asistanın veritabanında arama yapmasını, belirli kriterlere göre insanlar/olaylar/aileler/yerler filtrelemesini, bireyler arasındaki ilişkileri hesaplamasını ve ayrıntılı nesne bilgilerini almasını sağlar. Bu, asistanın karmaşık soybilim sorularını doğru bir şekilde yanıtlayabilme yeteneğini artırır.

Gramps Web API'de sohbet uç noktasını etkinleştirmek için üç adım gereklidir:

1. Gerekli bağımlılıkların yüklenmesi,
2. Anlamsal aramanın etkinleştirilmesi,
3. Bir LLM sağlayıcısının ayarlanması.

Bu üç adım aşağıda sırayla açıklanmaktadır. Son olarak, bir sahip veya yönetici, [kullanıcıların sohbet özelliğine erişimini yapılandırmalıdır](users.md#configuring-who-can-use-ai-chat) Kullanıcıları Yönet ayarlarında.

## Gerekli bağımlılıkların yüklenmesi

AI sohbeti, Sentence Transformers ve PyTorch kütüphanelerinin yüklenmesini gerektirir.

Gramps Web için standart docker görüntüleri, `amd64` (örneğin 64-bit masaüstü PC) ve `arm64` (örneğin 64-bit Raspberry Pi) mimarileri için bunları önceden yüklenmiş olarak içerir. Ne yazık ki, AI sohbeti, PyTorch desteğinin eksikliği nedeniyle `armv7` (örneğin 32-bit Raspberry Pi) mimarisinde desteklenmemektedir.

Gramps Web API'yi `pip` ile yüklerken (Docker görüntülerini kullanırken bu gerekli değildir) gerekli bağımlılıklar şu komutla yüklenir:

```bash
pip install gramps_webapi[ai]
```

## Anlamsal aramanın etkinleştirilmesi

Gerekli bağımlılıklar yüklendiyse, anlamsal aramanın etkinleştirilmesi, `VECTOR_EMBEDDING_MODEL` yapılandırma seçeneğini ayarlamak kadar basit olabilir (örneğin, `GRAMPSWEB_VECTOR_EMBEDDING_MODEL` ortam değişkenini ayarlayarak), bkz. [Sunucu Yapılandırması](configuration.md). Bu, [Sentence Transformers](https://sbert.net/) kütüphanesi tarafından desteklenen herhangi bir modelin bir dizesi olabilir. Ayrıntılar ve mevcut modeller için bu projenin belgelerine bakın.

!!! uyarı
    Varsayılan docker görüntülerinin GPU desteği olan bir PyTorch sürümünü içermediğini unutmayın. Eğer bir GPU'ya erişiminiz varsa (bu, anlamsal dizinlemeyi önemli ölçüde hızlandırır), lütfen GPU destekli bir PyTorch sürümünü yükleyin.

Bir modeli seçerken dikkate alınması gereken birkaç husus vardır.

- Modeli değiştirdiğinizde, ağacınız için (veya çoklu ağaç kurulumunda tüm ağaçlar için) anlamsal arama dizinini manuel olarak yeniden oluşturmanız gerekir, aksi takdirde hatalarla veya anlamsız sonuçlarla karşılaşırsınız. Gramps Web, yapılandırılmış gömme modelinin mevcut dizinle artık eşleşmediğini algılar ve yöneticilere [Yönetim Ayarları](../administration/settings.md#semantic-search-index) üzerinden tam bir yeniden dizinleme tetiklemeleri için sürekli bir bildirim gösterir.
- Modeller, bir yandan doğruluk/genellik ile diğer yandan hesaplama süresi/depolama alanı arasında bir denge gerektirir. Gramps Web API'yi güçlü bir GPU'ya erişimi olan bir sistemde çalıştırmıyorsanız, daha büyük modeller genellikle pratikte çok yavaştır.
- Tüm veritabanınız İngilizce değilse ve tüm kullanıcılarınızın yalnızca İngilizce olarak sohbet soruları sorması beklenmiyorsa, daha nadir olan çok dilli bir gömme modeline ihtiyacınız olacaktır.

Model yerel önbellekte yoksa, Gramps Web API ilk kez yeni yapılandırma ile başlatıldığında indirilecektir. `sentence-transformers/distiluse-base-multilingual-cased-v2` modeli, standart docker görüntülerini kullanırken zaten yerel olarak mevcuttur. Bu model iyi bir başlangıç noktasıdır ve çok dilli girişi destekler.

Farklı modeller hakkında öğrendiklerinizi toplulukla paylaşın!

!!! bilgi
    Sentence transformers kütüphanesi önemli miktarda bellek tüketir, bu da işçi süreçlerinin öldürülmesine neden olabilir. Genel bir kural olarak, anlamsal arama etkinleştirildiğinde, her Gunicorn işçisi yaklaşık 200 MB bellek tüketir ve her celery işçisi, boşta bile yaklaşık 500 MB bellek tüketir ve gömme hesaplama sırasında 1 GB'a kadar çıkabilir. Bellek kullanımını sınırlayan ayarlar için [CPU ve bellek kullanımını sınırlama](cpu-limited.md) bölümüne bakın. Ayrıca, geçici bellek kullanımındaki ani artışlardan dolayı OOM hatalarını önlemek için yeterince büyük bir takas bölümü sağlamanız önerilir.

## Uzaktan gömme API'si kullanma

Yerel bir Sentence Transformers modelini çalıştırmanın bir alternatifi olarak, anlamsal arama için uzaktan OpenAI uyumlu bir gömme API'si kullanabilirsiniz. Bu, gömme hesaplamasını ayrı bir hizmete (örneğin, [Ollama](https://ollama.com/)) devretmek, bir bulut gömme sağlayıcısı (örneğin OpenAI) kullanmak veya Sentence Transformers ve PyTorch kütüphanelerini belleğe yüklemekten kaçınmak istiyorsanız faydalıdır.

Uzaktan API, [OpenAI gömme uç noktası](https://platform.openai.com/docs/api-reference/embeddings) (`/v1/embeddings`) ile uyumlu olmalıdır.

Uzaktan bir gömme API'si kullanmak için aşağıdaki yapılandırma seçeneklerini ayarlayın (bkz. [Sunucu Yapılandırması](configuration.md)):

Anahtar | Açıklama
----|-------------
`VECTOR_EMBEDDING_MODEL` | Uzaktan sağlayıcıya iletilecek model adı
`VECTOR_EMBEDDING_BASE_URL` | Uzaktan API'nin temel URL'si
`VECTOR_EMBEDDING_API_KEY` | API anahtarı (yalnızca sağlayıcı kimlik doğrulama gerektiriyorsa gereklidir)

### Gömme için Ollama kullanma

Gramps Web'i Docker Compose ile dağıtırken, bir Ollama hizmeti ekleyebilir ve hem gömme hem de (isteğe bağlı olarak) LLM için kullanabilirsiniz:

```yaml
services:
  grampsweb: &grampsweb
    # ... mevcut yapılandırma ...
    environment:
      GRAMPSWEB_VECTOR_EMBEDDING_MODEL: nomic-embed-text
      GRAMPSWEB_VECTOR_EMBEDDING_BASE_URL: http://ollama:11434

  grampsweb_celery: &grampsweb_celery
    # ... mevcut yapılandırma ...
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

Hizmetleri başlattıktan sonra, gömme modelini Ollama'ya çekin:

```bash
docker compose exec ollama ollama pull nomic-embed-text
```

!!! bilgi
    Gömme için Ollama kullanırken, Sentence Transformers ve PyTorch kütüphanelerine ihtiyaç yoktur, bu da Gramps Web API işçilerinin bellek kullanımını önemli ölçüde azaltır.

### Gömme için OpenAI kullanma

OpenAI gömme API'sini kullanmak için temel URL'yi OpenAI API'sine ayarlayın ve API anahtarınızı sağlayın:

```yaml
environment:
  GRAMPSWEB_VECTOR_EMBEDDING_MODEL: text-embedding-3-small
  GRAMPSWEB_VECTOR_EMBEDDING_BASE_URL: https://api.openai.com
  GRAMPSWEB_VECTOR_EMBEDDING_API_KEY: sk-...
```

!!! uyarı
    Gömme modelini değiştirmek, ağacınızdaki (veya çoklu ağaç kurulumundaki tüm ağaçlar için) tüm kayıtların yeniden dizinlenmesini gerektirir, çünkü farklı modeller farklı boyutlarda vektörler üretir.

## LLM sağlayıcısını ayarlama

LLM ile iletişim, OpenAI uyumlu API'leri destekleyen Pydantic AI çerçevesini kullanır. Bu, Ollama aracılığıyla yerel olarak dağıtılmış bir LLM kullanmayı (bkz. [Ollama OpenAI uyumluluğu](https://ollama.com/blog/openai-compatibility)) veya OpenAI, Anthropic veya Hugging Face TGI (Metin Üretimi Çıkarımı) gibi barındırılan API'leri kullanmayı sağlar. LLM, `LLM_MODEL` ve `LLM_BASE_URL` yapılandırma parametreleri aracılığıyla yapılandırılır.

### OpenAI API'si aracılığıyla barındırılan LLM kullanma

OpenAI API'sini kullanırken, `LLM_BASE_URL` ayarlanmamış bırakılabilirken, `LLM_MODEL` OpenAI modellerinden birine (örneğin `gpt-4o-mini`) ayarlanmalıdır. LLM, soruları yanıtlamak için hem RAG hem de araç çağırmayı kullanır: anlamsal arama sonuçlarından ilgili bilgileri seçer ve özel araçlar kullanarak doğrudan veritabanını sorgulayabilir. Derin soybilim veya tarih bilgisi gerektirmez. Bu nedenle, küçük/ucuz bir modelin yeterli olup olmadığını deneyebilirsiniz.

Ayrıca bir hesap oluşturmanız, bir API anahtarı almanız ve bunu `OPENAI_API_KEY` ortam değişkeninde saklamanız gerekecektir.

!!! bilgi
    `LLM_MODEL`, bir yapılandırma parametresidir; eğer bir ortam değişkeni aracılığıyla ayarlamak istiyorsanız, `GRAMPSWEB_LLM_MODEL` kullanın (bkz. [Yapılandırma](configuration.md)). `OPENAI_API_KEY` bir yapılandırma parametresi değildir, ancak doğrudan Pydantic AI kütüphanesi tarafından kullanılan bir ortam değişkenidir, bu nedenle ön ek olmamalıdır.

### Mistral AI kullanma

Mistral AI'nın barındırılan modellerini kullanmak için, `LLM_MODEL` ayarlarken model adının önüne `mistral:` ekleyin.

Bir Mistral AI hesabı oluşturmanız, bir API anahtarı almanız ve bunu `MISTRAL_API_KEY` ortam değişkeninde saklamanız gerekecektir. Pydantic AI, doğru Mistral API uç noktasını otomatik olarak kullanacağından `LLM_BASE_URL` ayarlamanıza gerek yoktur.

Ortam değişkenleri ile docker compose kullanırken örnek yapılandırma:
```yaml
environment:
  GRAMPSWEB_LLM_MODEL: mistral:mistral-large-latest
  MISTRAL_API_KEY: your-mistral-api-key-here
  GRAMPSWEB_VECTOR_EMBEDDING_MODEL: sentence-transformers/distiluse-base-multilingual-cased-v2
```

### Ollama aracılığıyla yerel bir LLM kullanma

[Ollama](https://ollama.com/) LLM'leri yerel olarak çalıştırmanın pratik bir yoludur. Ayrıntılar için Ollama belgelerine başvurun. LLM'lerin önemli hesaplama kaynakları gerektirdiğini ve en küçük modeller dışında tüm modellerin GPU desteği olmadan muhtemelen çok yavaş olacağını lütfen unutmayın. Asistan araç çağırmaya dayandığı için, [`qwen2.5`](https://ollama.com/library/qwen2.5) gibi araçları destekleyen bir model seçin. `qwen2.5:7b` gibi küçük bir varyantla başlayın ve cevaplar yeterince iyi değilse daha büyük birini deneyin. Lütfen toplulukla herhangi bir deneyiminizi paylaşın!

Gramps Web'i Docker Compose ile dağıtırken, bir Ollama hizmeti ekleyebilir ve Gramps Web'i ona yönlendirebilirsiniz:

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

Hizmetleri başlattıktan sonra, modeli Ollama'ya çekin:

```bash
docker compose exec ollama ollama pull qwen2.5:7b
```

Dikkate alınması gereken birkaç şey:

- `LLM_MODEL`'i, etiketini (noktalı virgülden sonraki kısım, örneğin `7b`) de içerecek şekilde Ollama model adıyla ayarlayın ve önüne `ollama:` ekleyin. Ön ek, Pydantic AI'nın model için Ollama'ya özgü ayarlarını kullanmasını sağlar ve bu önerilen ayardır.
- `LLM_BASE_URL` `/v1/` ile bitmelidir, örneğin `http://ollama:11434/v1/`.
- `ollama:` ön eki ile, `OPENAI_API_KEY` veya `OLLAMA_BASE_URL` ortam değişkenine ihtiyaç yoktur. Eğer `LLM_BASE_URL` ayarlanmamışsa, Gramps Web `OLLAMA_BASE_URL`'ye geri döner.
- Alternatif olarak, ön eki (örneğin `LLM_MODEL: qwen2.5:7b`) çıkarabilir ve Ollama'yı genel OpenAI uyumlu API'si aracılığıyla kullanabilirsiniz. Bu durumda, `OPENAI_API_KEY` ortam değişkenini `ollama` (herhangi bir boş olmayan değer işe yarar) olarak ayarlamanız gerekir.

Ollama ile ilgili sorunları gidermek için, Ollama hizmeti ortamında `OLLAMA_DEBUG=1` ortam değişkenini ayarlayarak hata ayıklama günlüklerini etkinleştirebilirsiniz.

!!! bilgi
    Gramps Web AI sohbeti için Ollama kullanıyorsanız, lütfen topluluğa destek olmak için bu belgeleri eksik ayrıntılarla tamamlayın.

### Diğer sağlayıcıları kullanma

Lütfen diğer sağlayıcılar için belgeleri göndermekten ve deneyimlerinizi toplulukla paylaşmaktan çekinmeyin!
