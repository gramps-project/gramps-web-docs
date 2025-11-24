# AI sohbeti kurma

!!! bilgi
    AI sohbeti, Gramps Web API sürüm 2.5.0 veya daha yüksek bir sürüm gerektirir.


Gramps Web API, büyük dil modelleri (LLM) aracılığıyla soybilim veritabanı hakkında sorular sormayı destekler. Bu işlem, retrieval-augmented generation (RAG) adı verilen bir teknikle gerçekleştirilir.

RAG şu şekilde çalışır. Öncelikle, bir *vektör gömme modeli* kullanılarak Gramps veritabanındaki tüm nesnelerin anlamını kodlayan sayısal vektörler biçiminde bir indeks oluşturulur. Bu işlem, tam metin arama indeksinin oluşturulmasına benzer, ancak daha fazla hesaplama gücü gerektirir.

Daha sonra, bir kullanıcı sohbet uç noktası aracılığıyla bir soru sorduğunda, bu soru da aynı gömme modeli tarafından bir vektöre dönüştürülür ve Gramps veritabanındaki nesnelerle karşılaştırılır. Bu *anlamsal arama*, veritabanında soruyla en anlamsal olarak benzer nesneleri döndürür.

Son adımda, soru ve elde edilen nesneler, sağlanan bilgilere dayanarak bir cevap oluşturmak için bir LLM'ye gönderilir. Bu şekilde, chatbot, yalnızca önceden var olan bilgiye dayanmak yerine soybilim veritabanının içeriği hakkında ayrıntılı bilgilere erişim sağlar.

Gramps Web API'de sohbet uç noktasını etkinleştirmek için üç adım gereklidir:

1. Gerekli bağımlılıkların yüklenmesi,
2. Anlamsal aramanın etkinleştirilmesi,
3. Bir LLM sağlayıcısının ayarlanması.

Bu üç adım aşağıda sırayla açıklanmaktadır. Son olarak, bir sahip veya yönetici, [kullanıcıların sohbet özelliğine erişimini yapılandırmalıdır](users.md#configuring-who-can-use-ai-chat) Kullanıcıları Yönet ayarlarında.

## Gerekli bağımlılıkların yüklenmesi

AI sohbeti, Sentence Transformers ve PyTorch kütüphanelerinin yüklenmesini gerektirir.

Gramps Web için standart docker görüntüleri, `amd64` (örneğin 64-bit masaüstü PC) ve `arm64` (örneğin 64-bit Raspberry Pi) mimarileri için bunları önceden yüklenmiş olarak içerir. Ne yazık ki, AI sohbeti, PyTorch desteğinin olmaması nedeniyle `armv7` (örneğin 32-bit Raspberry Pi) mimarisinde desteklenmemektedir.

Gramps Web API'yi `pip` aracılığıyla yüklerken (Docker görüntülerini kullanırken bu gerekli değildir) gerekli bağımlılıklar şu komutla yüklenir:

```bash
pip install gramps_webapi[ai]
```


## Anlamsal aramanın etkinleştirilmesi

Gerekli bağımlılıklar yüklendiyse, anlamsal aramayı etkinleştirmek, `VECTOR_EMBEDDING_MODEL` yapılandırma seçeneğini ayarlamak kadar basit olabilir (örneğin, `GRAMPSWEB_VECTOR_EMBEDDING_MODEL` ortam değişkenini ayarlayarak), bkz. [Sunucu Yapılandırması](configuration.md). Bu, [Sentence Transformers](https://sbert.net/) kütüphanesi tarafından desteklenen bir modelin herhangi bir dizesi olabilir. Bu proje için ayrıntılar ve mevcut modeller için belgelere bakınız.


!!! uyarı
    Varsayılan docker görüntülerinin GPU desteği olan bir PyTorch sürümünü içermediğini unutmayın. Eğer bir GPU'ya erişiminiz varsa (bu, anlamsal indekslemeyi önemli ölçüde hızlandırır), lütfen GPU destekli bir PyTorch sürümünü yükleyin.

Bir model seçerken dikkate alınması gereken birkaç husus vardır.

- Modeli değiştirdiğinizde, ağacınız için (veya çoklu ağaç yapılandırmasında tüm ağaçlar için) anlamsal arama indeksini manuel olarak yeniden oluşturmanız gerekir, aksi takdirde hatalarla veya anlamsız sonuçlarla karşılaşırsınız.
- Modeller, bir yandan doğruluk/genellik ile diğer yandan hesaplama süresi/depolama alanı arasında bir denge sağlar. Gramps Web API'yi güçlü bir GPU'ya erişimi olan bir sistemde çalıştırmıyorsanız, daha büyük modeller genellikle pratikte çok yavaş olur.
- Tüm veritabanınız İngilizce değilse ve tüm kullanıcılarınızın yalnızca İngilizce olarak sohbet soruları sorması beklenmiyorsa, daha nadir olan çok dilli bir gömme modeline ihtiyacınız olacaktır; saf İngilizce modellerine göre daha nadirdir.


Eğer model yerel önbellekte yoksa, Gramps Web API yeni yapılandırma ile ilk kez başlatıldığında indirilecektir. `sentence-transformers/distiluse-base-multilingual-cased-v2` modeli, standart docker görüntülerini kullanırken zaten yerel olarak mevcuttur. Bu model iyi bir başlangıç noktasıdır ve çok dilli girişi destekler.

Farklı modeller hakkında toplulukla öğrenimlerinizi paylaşın!

!!! bilgi
    Sentence transformers kütüphanesi önemli miktarda bellek tüketir, bu da işçi süreçlerinin sonlandırılmasına neden olabilir. Genel bir kural olarak, anlamsal arama etkinleştirildiğinde, her Gunicorn işçisi yaklaşık 200 MB bellek tüketirken, her celery işçisi boşta bile yaklaşık 500 MB bellek tüketir ve gömme hesaplama sırasında 1 GB'a kadar çıkabilir. Bellek kullanımını sınırlayan ayarlar için [CPU ve bellek kullanımını sınırlama](cpu-limited.md) sayfasına bakın. Ayrıca, geçici bellek kullanımı artışlarına bağlı OOM hatalarını önlemek için yeterince büyük bir takas bölümü sağlamanız önerilir.

## LLM sağlayıcısını ayarlama

LLM ile iletişim, `openai-python` kütüphanesini kullanarak OpenAI uyumlu bir API aracılığıyla gerçekleştirilir. Bu, bir yerel olarak dağıtılan LLM'yi Ollama aracılığıyla (bkz. [Ollama OpenAI uyumluluğu](https://ollama.com/blog/openai-compatibility)) veya OpenAI veya Hugging Face TGI (Metin Üretim Çıkarımı) gibi bir API kullanarak çalıştırmayı sağlar. LLM, `LLM_MODEL` ve `LLM_BASE_URL` yapılandırma parametreleri aracılığıyla yapılandırılır.


### OpenAI API aracılığıyla barındırılan bir LLM kullanma

OpenAI API'sini kullanırken, `LLM_BASE_URL` ayarsız bırakılabilirken, `LLM_MODEL` OpenAI modellerinden birine, örneğin `gpt-4o-mini` olarak ayarlanmalıdır. RAG yaklaşımı nedeniyle, LLM "yalnızca" anlamsal arama sonuçlarından doğru bilgiyi seçmek ve bir cevap oluşturmak için kullanılır; derin soybilimsel veya tarihsel bilgi gerektirmez. Bu nedenle, küçük/ucuz bir modelin yeterli olup olmadığını deneyebilirsiniz.

Ayrıca bir hesap oluşturmanız, bir API anahtarı almanız ve bunu `OPENAI_API_KEY` ortam değişkeninde saklamanız gerekecektir.

!!! bilgi
    `LLM_MODEL` bir yapılandırma parametresidir; eğer bir ortam değişkeni aracılığıyla ayarlamak istiyorsanız, `GRAMPSWEB_LLM_MODEL` kullanın (bkz. [Yapılandırma](configuration.md)). `OPENAI_API_KEY` bir yapılandırma parametresi değil, `openai-python` kütüphanesi tarafından doğrudan kullanılan bir ortam değişkenidir, bu nedenle ön ek olmamalıdır.


### Ollama aracılığıyla yerel bir LLM kullanma

[Ollama](https://ollama.com/) LLM'leri yerel olarak çalıştırmanın pratik bir yoludur. Ayrıntılar için Ollama belgelere başvurun. LLM'lerin önemli hesaplama kaynakları gerektirdiğini ve en küçük modeller dışında hepsinin GPU desteği olmadan muhtemelen çok yavaş olacağını unutmayın. İhtiyaçlarınızı karşılayıp karşılamadığını görmek için [`tinyllama`](https://ollama.com/library/tinyllama) modelini deneyebilirsiniz. Eğer yeterli değilse, daha büyük modellerden birini deneyin. Herhangi bir deneyiminizi toplulukla paylaşın!

Gramps Web'i Docker Compose ile dağıtırken, bir Ollama servisi ekleyebilirsiniz:

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

Ardından, `LLM_BASE_URL` yapılandırma parametresini `http://ollama:11434/v1` olarak ayarlayın. `LLM_MODEL`'i Ollama tarafından desteklenen bir model olarak ayarlayın ve konteynerinizde `ollama pull <model>` ile indirin. Son olarak, `OPENAI_API_KEY`'i `ollama` olarak ayarlayın.

Ollama ile ilgili sorunları gidermek için, Ollama hizmeti ortamında `OLLAMA_DEBUG=1` ortam değişkenini ayarlayarak hata ayıklama günlüğünü etkinleştirebilirsiniz.

!!! bilgi
    Gramps Web AI sohbeti için Ollama kullanıyorsanız, lütfen topluluğa eksik ayrıntıları tamamlayarak bu belgeleri destekleyin.

### Diğer sağlayıcıları kullanma

Lütfen diğer sağlayıcılar için belgeler göndermekten çekinmeyin ve deneyimlerinizi toplulukla paylaşın!
