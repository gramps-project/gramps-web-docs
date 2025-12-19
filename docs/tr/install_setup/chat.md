# AI sohbeti kurma

!!! bilgi
    AI sohbeti, Gramps Web API sürüm 2.5.0 veya daha yüksek bir sürüm gerektirir. Sürüm 3.6.0, daha akıllı etkileşimler için araç çağırma yeteneklerini tanıttı.


Gramps Web API, büyük dil modelleri (LLM) aracılığıyla soybilim veritabanı hakkında sorular sormayı destekler; bu, araç çağırma ile birleştirilmiş bir teknik olan retrieval-augmented generation (RAG) kullanılarak gerçekleştirilir.

## Nasıl çalışır

AI asistanı, iki tamamlayıcı yaklaşım kullanır:

**Retrieval-Augmented Generation (RAG)**: Bir *vektör gömme modeli*, Gramps veritabanındaki tüm nesnelerin anlamını kodlayan sayısal vektörler biçiminde bir dizin oluşturur. Bir kullanıcı bir soru sorduğunda, o soru da bir vektöre dönüştürülür ve veritabanındaki nesnelerle karşılaştırılır. Bu *anlamsal arama*, soruyla en anlamsal olarak benzer nesneleri döndürür.

**Araç Çağırma (v3.6.0+)**: AI asistanı artık soybilim verilerinizi doğrudan sorgulamak için özel araçlar kullanabilir. Bu araçlar, asistanın veritabanında arama yapmasına, belirli kriterlere göre insanlar/olaylar/aileler/yerler filtrelemesine, bireyler arasındaki ilişkileri hesaplamasına ve ayrıntılı nesne bilgilerini almasına olanak tanır. Bu, asistanın karmaşık soybilim sorularını doğru bir şekilde yanıtlamasını çok daha yetenekli hale getirir.

Gramps Web API'de sohbet uç noktasını etkinleştirmek için üç adım gereklidir:

1. Gerekli bağımlılıkların yüklenmesi,
2. Anlamsal aramanın etkinleştirilmesi,
3. Bir LLM sağlayıcısının ayarlanması.

Bu üç adım sırayla aşağıda açıklanmıştır. Son olarak, bir sahip veya yönetici, [hangi kullanıcıların sohbet özelliğine erişebileceğini yapılandırmalıdır](users.md#configuring-who-can-use-ai-chat) Kullanıcıları Yönet ayarlarında.

## Gerekli bağımlılıkların yüklenmesi

AI sohbeti, Sentence Transformers ve PyTorch kütüphanelerinin yüklenmesini gerektirir.

Gramps Web için standart docker görüntüleri, `amd64` (örneğin 64-bit masaüstü PC) ve `arm64` (örneğin 64-bit Raspberry Pi) mimarileri için önceden yüklenmiş olarak gelir. Ne yazık ki, AI sohbeti `armv7` (örneğin 32-bit Raspberry Pi) mimarisinde PyTorch desteğinin olmaması nedeniyle desteklenmemektedir.

Gramps Web API'yi `pip` aracılığıyla yüklerken (Docker görüntülerini kullanırken bu gerekli değildir) gerekli bağımlılıklar şu komutla yüklenir:

```bash
pip install gramps_webapi[ai]
```

## Anlamsal aramanın etkinleştirilmesi

Gerekli bağımlılıklar yüklendiyse, anlamsal aramanın etkinleştirilmesi, `VECTOR_EMBEDDING_MODEL` yapılandırma seçeneğini ayarlamak kadar basit olabilir (örneğin, `GRAMPSWEB_VECTOR_EMBEDDING_MODEL` ortam değişkenini ayarlayarak), bkz. [Sunucu Yapılandırması](configuration.md). Bu, [Sentence Transformers](https://sbert.net/) kütüphanesi tarafından desteklenen bir modelin herhangi bir dizesi olabilir. Ayrıntılar ve mevcut modeller için bu projenin belgelerine bakın.

!!! uyarı
    Varsayılan docker görüntülerinin GPU desteği olan bir PyTorch sürümünü içermediğini unutmayın. Eğer bir GPU'ya erişiminiz varsa (bu, anlamsal dizinlemeyi önemli ölçüde hızlandıracaktır), lütfen GPU destekli bir PyTorch sürümünü yükleyin.

Bir model seçerken dikkate alınması gereken birkaç husus vardır.

- Modeli değiştirdiğinizde, ağacınız (veya çoklu ağaç kurulumunda tüm ağaçlar) için anlamsal arama dizinini manuel olarak yeniden oluşturmanız gerekir, aksi takdirde hatalarla veya anlamsız sonuçlarla karşılaşırsınız.
- Modeller, bir yandan doğruluk/genellik ile diğer yandan hesaplama süresi/depolama alanı arasında bir denge sağlar. Eğer Gramps Web API'yi güçlü bir GPU'ya erişimi olan bir sistemde çalıştırmıyorsanız, daha büyük modeller genellikle pratikte çok yavaş olur.
- Veritabanınız tamamen İngilizce değilse ve tüm kullanıcılarınızın yalnızca İngilizce sohbet soruları sorması beklenmiyorsa, daha nadir olan çok dilli bir gömme modeline ihtiyacınız olacaktır; bu, saf İngilizce modellerden daha nadirdir.

Model yerel önbellekte yoksa, Gramps Web API ilk kez yeni yapılandırma ile başlatıldığında indirilecektir. `sentence-transformers/distiluse-base-multilingual-cased-v2` modeli, standart docker görüntülerini kullanırken zaten yerel olarak mevcuttur. Bu model iyi bir başlangıç noktasıdır ve çok dilli girişi destekler.

Farklı modeller hakkında öğrendiklerinizi toplulukla paylaşın!

!!! bilgi
    Sentence transformers kütüphanesi önemli miktarda bellek tüketir, bu da işçi süreçlerinin öldürülmesine neden olabilir. Genel bir kural olarak, anlamsal arama etkinleştirildiğinde, her Gunicorn işçisi yaklaşık 200 MB bellek tüketirken, her celery işçisi boşta bile yaklaşık 500 MB bellek tüketir ve gömme hesaplama sırasında 1 GB'a kadar çıkabilir. Bellek kullanımını sınırlayan ayarlar için [CPU ve bellek kullanımını sınırlama](cpu-limited.md) sayfasına bakın. Ayrıca, geçici bellek kullanımındaki ani artışlar nedeniyle OOM hatalarını önlemek için yeterince büyük bir takas bölümü ayırmak önerilir.

## Bir LLM sağlayıcısının ayarlanması

LLM ile iletişim, OpenAI uyumlu API'leri destekleyen Pydantic AI çerçevesini kullanır. Bu, yerel olarak dağıtılmış bir LLM'yi Ollama aracılığıyla (bkz. [Ollama OpenAI uyumluluğu](https://ollama.com/blog/openai-compatibility)) veya OpenAI, Anthropic veya Hugging Face TGI (Metin Üretim Çıkarımı) gibi barındırılan API'leri kullanmayı sağlar. LLM, `LLM_MODEL` ve `LLM_BASE_URL` yapılandırma parametreleri aracılığıyla yapılandırılır.

### OpenAI API aracılığıyla barındırılan bir LLM kullanma

OpenAI API'sini kullanırken, `LLM_BASE_URL` ayarı boş bırakılabilirken, `LLM_MODEL` OpenAI modellerinden birine, örneğin `gpt-4o-mini` olarak ayarlanmalıdır. LLM, soruları yanıtlamak için hem RAG hem de araç çağırmayı kullanır: anlamsal arama sonuçlarından ilgili bilgileri seçer ve özel araçlar kullanarak veritabanını doğrudan sorgulayabilir. Derin soybilim veya tarih bilgisi gerektirmez. Bu nedenle, küçük/ucuz bir modelin yeterli olup olmadığını deneyebilirsiniz.

Ayrıca bir hesap oluşturmanız, bir API anahtarı almanız ve bunu `OPENAI_API_KEY` ortam değişkeninde saklamanız gerekecek.

!!! bilgi
    `LLM_MODEL`, bir yapılandırma parametresidir; eğer bir ortam değişkeni aracılığıyla ayarlamak istiyorsanız, `GRAMPSWEB_LLM_MODEL` kullanın (bkz. [Yapılandırma](configuration.md)). `OPENAI_API_KEY`, bir yapılandırma parametresi değil, Pydantic AI kütüphanesi tarafından doğrudan kullanılan bir ortam değişkenidir, bu nedenle ön ek kullanılmamalıdır.

### Mistral AI kullanma

Mistral AI'nin barındırılan modellerini kullanmak için, `LLM_MODEL` ayarını yaparken model adının önüne `mistral:` ekleyin.

Bir Mistral AI hesabı oluşturmanız, bir API anahtarı almanız ve bunu `MISTRAL_API_KEY` ortam değişkeninde saklamanız gerekecek. `LLM_BASE_URL` ayarını yapmanıza gerek yoktur çünkü Pydantic AI otomatik olarak doğru Mistral API uç noktasını kullanacaktır.

Ortam değişkenleri ile docker compose kullanırken örnek yapılandırma:
```yaml
environment:
  GRAMPSWEB_LLM_MODEL: mistral:mistral-large-latest
  MISTRAL_API_KEY: your-mistral-api-key-here
  GRAMPSWEB_VECTOR_EMBEDDING_MODEL: sentence-transformers/distiluse-base-multilingual-cased-v2
```

### Ollama aracılığıyla yerel bir LLM kullanma

[Ollama](https://ollama.com/) LLM'leri yerel olarak çalıştırmanın pratik bir yoludur. Ayrıntılar için Ollama belgelerine başvurun. LLM'lerin önemli hesaplama kaynakları gerektirdiğini ve en küçük modeller dışında tüm modellerin GPU desteği olmadan muhtemelen çok yavaş olacağını lütfen unutmayın. İhtiyaçlarınızı karşılayıp karşılamadığını görmek için [`tinyllama`](https://ollama.com/library/tinyllama) deneyebilirsiniz. Eğer yeterli değilse, daha büyük modellerden birini deneyin. Herhangi bir deneyiminizi toplulukla paylaşın!

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

Ardından `LLM_BASE_URL` yapılandırma parametresini `http://ollama:11434/v1` olarak ayarlayın. `LLM_MODEL`'i Ollama tarafından desteklenen bir model olarak ayarlayın ve konteynerinizde `ollama pull <model>` komutuyla indirin. Son olarak, `OPENAI_API_KEY`'i `ollama` olarak ayarlayın.

Ollama ile ilgili sorunları gidermek için, Ollama hizmeti ortamında `OLLAMA_DEBUG=1` ortam değişkenini ayarlayarak hata ayıklama günlüğünü etkinleştirebilirsiniz.

!!! bilgi
    Gramps Web AI sohbeti için Ollama kullanıyorsanız, lütfen topluluğu desteklemek için bu belgeleri eksik ayrıntılarla tamamlayın.

### Diğer sağlayıcıları kullanma

Lütfen diğer sağlayıcılar için belgeleri göndermekten çekinmeyin ve deneyimlerinizi toplulukla paylaşın!
