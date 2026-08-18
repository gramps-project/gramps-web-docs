# AI sohbetini ayarlama

!!! bilgi
    AI sohbeti, Gramps Web API sürüm 2.5.0 veya daha yüksek bir sürüm gerektirir. Sürüm 3.6.0, daha akıllı etkileşimler için araç çağırma yeteneklerini tanıttı.

Gramps Web API, büyük dil modelleri (LLM) aracılığıyla soybilim veritabanı hakkında soru sormayı destekler; bu, araç çağırma ile birleştirilmiş bir teknik olan geri alma artırımlı üretim (RAG) ile gerçekleştirilir.

## Nasıl çalışır

AI asistanı, iki tamamlayıcı yaklaşım kullanır:

**Geri Alma Artırımlı Üretim (RAG)**: Bir *vektör gömme modeli*, Gramps veritabanındaki tüm nesnelerin anlamını kodlayan sayısal vektörler biçiminde bir dizin oluşturur. Bir kullanıcı soru sorduğunda, bu soru da bir vektöre dönüştürülür ve veritabanındaki nesnelerle karşılaştırılır. Bu *anlamsal arama*, soruyla en anlamsal olarak benzer nesneleri döndürür.

**Araç Çağırma (v3.6.0+)**: AI asistanı artık soybilim verilerinizi doğrudan sorgulamak için özel araçlar kullanabilir. Bu araçlar, asistanın veritabanında arama yapmasına, belirli kriterlere göre kişiler/olaylar/aileler/yerler filtrelemesine, bireyler arasındaki ilişkileri hesaplamasına ve ayrıntılı nesne bilgilerini almasına olanak tanır. Bu, asistanın karmaşık soybilim sorularını doğru bir şekilde yanıtlama yeteneğini büyük ölçüde artırır.

Gramps Web API'de sohbet uç noktasını etkinleştirmek için üç adım gereklidir:

1. Gerekli bağımlılıkların yüklenmesi,
2. Anlamsal aramanın etkinleştirilmesi,
3. Bir LLM sağlayıcısının ayarlanması.

Bu üç adım sırayla aşağıda açıklanmıştır. Son olarak, bir sahip veya yönetici, [kullanıcıların sohbet özelliğine erişimini yapılandırmalıdır](users.md#configuring-who-can-use-ai-chat) Yönetici Kullanıcı ayarlarında.

## Gerekli bağımlılıkların yüklenmesi

AI sohbeti, Sentence Transformers ve PyTorch kütüphanelerinin yüklenmesini gerektirir.

Gramps Web için standart docker görüntüleri, `amd64` (örneğin 64-bit masaüstü PC) ve `arm64` (örneğin 64-bit Raspberry Pi) mimarileri için önceden yüklenmiş olarak gelir. Ne yazık ki, AI sohbeti, PyTorch desteği eksik olduğu için `armv7` (örneğin 32-bit Raspberry Pi) mimarisinde desteklenmemektedir.

Gramps Web API'yi `pip` ile yüklerken (Docker görüntüleri kullanıldığında bu gerekli değildir) gerekli bağımlılıklar şu komutla yüklenir:

```bash
pip install gramps_webapi[ai]
```

## Anlamsal aramanın etkinleştirilmesi

Gerekli bağımlılıklar yüklendiyse, anlamsal aramanın etkinleştirilmesi, `VECTOR_EMBEDDING_MODEL` yapılandırma seçeneğini ayarlamak kadar basit olabilir (örneğin, `GRAMPSWEB_VECTOR_EMBEDDING_MODEL` ortam değişkenini ayarlayarak), bkz. [Sunucu Yapılandırması](configuration.md). Bu, [Sentence Transformers](https://sbert.net/) kütüphanesi tarafından desteklenen bir modelin herhangi bir dizesi olabilir. Detaylar ve mevcut modeller için bu projenin belgelerine bakın.

!!! uyarı
    Varsayılan docker görüntülerinin GPU desteği olan bir PyTorch sürümünü içermediğini unutmayın. Eğer bir GPU'ya erişiminiz varsa (bu, anlamsal dizinlemeyi önemli ölçüde hızlandıracaktır), lütfen GPU destekli bir PyTorch sürümünü yükleyin.

Bir model seçerken dikkate alınması gereken birkaç husus vardır.

- Modeli değiştirdiğinizde, ağacınız için (veya çoklu ağaç kurulumunda tüm ağaçlar için) anlamsal arama dizinini manuel olarak yeniden oluşturmanız gerekir; aksi takdirde hatalarla veya anlamsız sonuçlarla karşılaşırsınız. Gramps Web, yapılandırılan gömme modelinin mevcut dizinle artık eşleşmediğini algılar ve yöneticilere [Yönetim Ayarları](../administration/settings.md#semantic-search-index) üzerinden tam bir yeniden dizinleme başlatmaları için sürekli bir bildirim gösterir.
- Modeller, bir yandan doğruluk/genellik ile diğer yandan hesaplama süresi/depolama alanı arasında bir denge gerektirir. Eğer Gramps Web API'yi güçlü bir GPU'ya erişimi olan bir sistemde çalıştırmıyorsanız, daha büyük modeller genellikle pratikte çok yavaş olur.
- Tüm veritabanınız İngilizce değilse ve tüm kullanıcılarınızın yalnızca İngilizce olarak sohbet soruları sorması beklenmiyorsa, daha nadir olan çok dilli bir gömme modeline ihtiyacınız olacaktır; bu modeller saf İngilizce modellerden daha nadirdir.

Model yerel önbellekte mevcut değilse, Gramps Web API ilk kez yeni yapılandırma ile başlatıldığında indirilecektir. `sentence-transformers/distiluse-base-multilingual-cased-v2` modeli, standart docker görüntüleri kullanıldığında zaten yerel olarak mevcuttur. Bu model iyi bir başlangıç noktasıdır ve çok dilli girişi destekler.

Farklı modeller hakkında öğrenimlerinizi toplulukla paylaşın!

!!! bilgi
    Sentence transformers kütüphanesi önemli miktarda bellek tüketir, bu da işçi süreçlerinin öldürülmesine neden olabilir. Genel bir kural olarak, anlamsal arama etkinleştirildiğinde, her Gunicorn işçisi yaklaşık 200 MB bellek tüketirken, her celery işçisi boşta bile yaklaşık 500 MB bellek tüketir ve gömme hesaplaması yaparken 1 GB'a kadar çıkabilir. Bellek kullanımını sınırlayan ayarlar için [CPU ve bellek kullanımını sınırlama](cpu-limited.md) sayfasına bakın. Ayrıca, geçici bellek kullanımındaki ani artışlar nedeniyle OOM hatalarını önlemek için yeterince büyük bir takas bölümü sağlamanız önerilir.

## Uzaktan gömme API'si kullanma

Yerel bir Sentence Transformers modelini çalıştırmanın bir alternatifi olarak, anlamsal arama için uzaktan OpenAI uyumlu bir gömme API'si kullanabilirsiniz. Bu, gömme hesaplamasını ayrı bir hizmete (örneğin, [Ollama](https://ollama.com/)) devretmek, bir bulut gömme sağlayıcısı (örneğin OpenAI) kullanmak veya Sentence Transformers ve PyTorch kütüphanelerini belleğe yüklemekten kaçınmak istediğinizde faydalıdır.

Uzaktan API, [OpenAI gömme uç noktası](https://platform.openai.com/docs/api-reference/embeddings) (`/v1/embeddings`) ile uyumlu olmalıdır.

Uzaktan bir gömme API'si kullanmak için aşağıdaki yapılandırma seçeneklerini ayarlayın (bkz. [Sunucu Yapılandırması](configuration.md)):

Anahtar | Açıklama
----|-------------
`VECTOR_EMBEDDING_MODEL` | Uzaktan sağlayıcıya iletilecek model adı
`VECTOR_EMBEDDING_BASE_URL` | Uzaktan API'nin temel URL'si
`VECTOR_EMBEDDING_API_KEY` | API anahtarı (yalnızca sağlayıcı kimlik doğrulama gerektiriyorsa gereklidir)

### Gömme için Ollama kullanma

Gramps Web'i Docker Compose ile dağıtırken, bir Ollama hizmeti ekleyebilir ve bunu hem gömme hem de (isteğe bağlı olarak) LLM için kullanabilirsiniz:

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

OpenAI gömme API'sini kullanmak için, temel URL'yi OpenAI API'sine ayarlayın ve API anahtarınızı sağlayın:

```yaml
environment:
  GRAMPSWEB_VECTOR_EMBEDDING_MODEL: text-embedding-3-small
  GRAMPSWEB_VECTOR_EMBEDDING_BASE_URL: https://api.openai.com
  GRAMPSWEB_VECTOR_EMBEDDING_API_KEY: sk-...
```

!!! uyarı
    Gömme modelini değiştirmek, ağacınızdaki (veya çoklu ağaç kurulumunda tüm ağaçlardaki) tüm kayıtların yeniden dizinlenmesini gerektirir, çünkü farklı modeller farklı boyutlarda vektörler üretir.

## Bir LLM sağlayıcısını ayarlama

LLM ile iletişim, OpenAI uyumlu API'leri destekleyen Pydantic AI çerçevesini kullanır. Bu, Ollama aracılığıyla yerel olarak dağıtılan bir LLM kullanmayı (bkz. [Ollama OpenAI uyumluluğu](https://ollama.com/blog/openai-compatibility)) veya OpenAI, Anthropic veya Hugging Face TGI (Metin Üretimi Çıkarımı) gibi barındırılan API'leri kullanmayı sağlar. LLM, `LLM_MODEL` ve `LLM_BASE_URL` yapılandırma parametreleri aracılığıyla yapılandırılır.

### OpenAI API'si aracılığıyla barındırılan bir LLM kullanma

OpenAI API'sini kullanırken, `LLM_BASE_URL` ayarlanmamış bırakılabilirken, `LLM_MODEL` OpenAI modellerinden birine (örneğin, `gpt-4o-mini`) ayarlanmalıdır. LLM, soruları yanıtlamak için hem RAG hem de araç çağırmayı kullanır: anlamsal arama sonuçlarından ilgili bilgileri seçer ve özel araçlar kullanarak veritabanını doğrudan sorgulayabilir. Derin soybilim veya tarih bilgisi gerektirmez. Bu nedenle, küçük/ucuz bir modelin yeterli olup olmadığını deneyebilirsiniz.

Ayrıca bir hesap oluşturmanız, bir API anahtarı almanız ve bunu `OPENAI_API_KEY` ortam değişkeninde saklamanız gerekecektir.

!!! bilgi
    `LLM_MODEL`, bir yapılandırma parametresidir; eğer bunu bir ortam değişkeni aracılığıyla ayarlamak istiyorsanız, `GRAMPSWEB_LLM_MODEL` kullanın (bkz. [Yapılandırma](configuration.md)). `OPENAI_API_KEY`, bir yapılandırma parametresi değil, Pydantic AI kütüphanesi tarafından doğrudan kullanılan bir ortam değişkenidir, bu nedenle ön ek kullanılmamalıdır.

### Mistral AI kullanma

Mistral AI'nın barındırılan modellerini kullanmak için, `LLM_MODEL` ayarlarken model adını `mistral:` ile ön ekleyin.

Bir Mistral AI hesabı oluşturmanız, bir API anahtarı almanız ve bunu `MISTRAL_API_KEY` ortam değişkeninde saklamanız gerekecektir. Pydantic AI, doğru Mistral API uç noktasını otomatik olarak kullanacağından `LLM_BASE_URL` ayarlamanıza gerek yoktur.

Ortam değişkenleri ile docker compose kullanırken örnek yapılandırma:
```yaml
environment:
  GRAMPSWEB_LLM_MODEL: mistral:mistral-large-latest
  MISTRAL_API_KEY: your-mistral-api-key-here
  GRAMPSWEB_VECTOR_EMBEDDING_MODEL: sentence-transformers/distiluse-base-multilingual-cased-v2
```

### Ollama aracılığıyla yerel bir LLM kullanma

[Ollama](https://ollama.com/) yerel olarak LLM'leri çalıştırmanın pratik bir yoludur. Detaylar için Ollama belgelerine başvurun. LLM'lerin önemli hesaplama kaynakları gerektirdiğini ve en küçük modeller dışında tüm modellerin GPU desteği olmadan muhtemelen çok yavaş olacağını lütfen unutmayın. İhtiyaçlarınızı karşılayıp karşılamadığını görmek için [`tinyllama`](https://ollama.com/library/tinyllama) deneyebilirsiniz. Eğer değilse, daha büyük modellerden birini deneyin. Herhangi bir deneyiminizi toplulukla paylaşın!

Gramps Web'i Docker Compose ile dağıtırken, bir Ollama hizmeti ekleyebilirsiniz:

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

Ardından, `LLM_BASE_URL` yapılandırma parametresini `http://ollama:11434/v1` olarak ayarlayın. `LLM_MODEL`'i Ollama tarafından desteklenen bir modele ayarlayın ve konteynerinizde `ollama pull <model>` ile indirin. Son olarak, `OPENAI_API_KEY`'i `ollama` olarak ayarlayın.

Ollama ile ilgili sorunları gidermek için, Ollama hizmeti ortamında `OLLAMA_DEBUG=1` ortam değişkenini ayarlayarak hata ayıklama günlüklemesini etkinleştirebilirsiniz.

!!! bilgi
    Gramps Web AI sohbeti için Ollama kullanıyorsanız, lütfen topluluğu desteklemek için bu belgeleri eksik ayrıntılarla tamamlayın.

### Diğer sağlayıcıları kullanma

Lütfen diğer sağlayıcılar için belgeler göndermekten çekinmeyin ve deneyimlerinizi toplulukla paylaşın!
