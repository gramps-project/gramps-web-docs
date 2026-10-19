# AI sohbeti ayarlama

!!! info
    AI sohbeti, Gramps Web API sürüm 2.5.0 veya daha yüksek bir sürüm gerektirir. Sürüm 3.6.0, daha akıllı etkileşimler için araç çağırma yeteneklerini tanıttı.

Gramps Web API, büyük dil modelleri (LLM) ile araç çağırma kullanarak genealogik veritabanı hakkında soru sormayı destekler.

## Nasıl çalışır

AI asistanı, soybilgisi verilerinizi doğrudan sorgulamak için özel araçlar kullanır. Bu araçlar, asistanın veritabanında tam metin araması yapmasına, belirli kriterlere göre kişiler/olaylar/aileler/yerler filtrelemesine, bireyler arasındaki ilişkileri hesaplamasına ve notlar dahil olmak üzere tam kayıtları almasına olanak tanır. Asistan, ardından baktığı kayıtlara dayanarak cevap verir ve cevaplarında bu kayıtlara bağlantılar ekler.

Gramps Web API 3.24'ten itibaren, AI sohbeti artık bir vektör gömme modeline ihtiyaç duymamaktadır. Önceki sürümler ayrıca *anlamsal arama* (retrieve-augmented generation, RAG) kullanıyordu; bu, bir sorunun anlamını veritabanındaki tüm nesneler için hesaplanan sayısal vektörlerin bir dizini ile karşılaştırır. Anlamsal arama kullanımdan kaldırılmıştır ve Gramps Web API 3.25'te kaldırılacaktır, aşağıda [Anlamsal arama (kaldırıldı)](#anlamsal-arama-kaldırıldı) kısmına bakın.

Gramps Web API'de sohbet uç noktasını etkinleştirmek için iki adım gereklidir:

1. Gerekli bağımlılıkların kurulması,
2. Bir LLM sağlayıcısının ayarlanması.

Bu iki adım aşağıda sırasıyla açıklanmıştır. Son olarak, bir sahibi veya yönetici, [hangi kullanıcıların sohbet özelliğine erişebileceğini yapılandırmalıdır](users.md#configuring-who-can-use-ai-chat) Kullanıcıları Yönet ayarlarında.

## Gerekli bağımlılıkların kurulması

Gramps Web için standart docker görüntüleri, AI sohbeti için gerekli tüm bağımlılıkları önceden yüklenmiş olarak içerir.

Gramps Web API'yi `pip` ile kurarken (Docker görüntülerini kullanırken bu gerekli değildir) gerekli bağımlılıklar şu komutla yüklenir:

```bash
pip install gramps_webapi[ai]
```

## Anlamsal arama (kaldırıldı)

!!! warning "Anlamsal arama kaldırıldı"
    Anlamsal arama, Gramps Web API 3.24'ten beri kaldırılmıştır ve 3.25 sürümünde kaldırılacaktır. AI sohbeti ve [tam metin arama](../user-guide/search.md) buna ihtiyaç duymaz. Kaldırıldıktan sonra, `VECTOR_EMBEDDING_MODEL` ayarı hala kabul edilir ancak göz ardı edilir. Eğer bunu yalnızca AI sohbetini etkinleştirmek için ayarladıysanız, şimdi kaldırabilir ve diğer `VECTOR_EMBEDDING_*` ayarlarıyla birlikte hafızadan tasarruf edebilirsiniz.

Bu bölümün geri kalanı, Gramps Web API 3.24 ile hala bunu kullanan sunucular için anlamsal aramayı tanımlar.

Gerekli bağımlılıklar yüklendiyse, anlamsal aramayı etkinleştirmek, `VECTOR_EMBEDDING_MODEL` yapılandırma seçeneğini ayarlamak kadar basit olabilir (örneğin, `GRAMPSWEB_VECTOR_EMBEDDING_MODEL` ortam değişkenini ayarlayarak), [Sunucu Yapılandırması](configuration.md) kısmına bakın. Bu, [Sentence Transformers](https://sbert.net/) kütüphanesi tarafından desteklenen bir modelin herhangi bir dizesi olabilir. Detaylar ve mevcut modeller için bu projenin belgelerine bakın.

!!! warning
    Varsayılan docker görüntülerinin GPU desteği olan bir PyTorch sürümünü içermediğini unutmayın. Eğer bir GPU'ya erişiminiz varsa (bu, anlamsal dizinlemeyi önemli ölçüde hızlandırır), lütfen GPU destekli bir PyTorch sürümünü kurun.

Bir model seçerken dikkate alınması gereken birkaç husus vardır.

- Modeli değiştirdiğinizde, ağacınız (veya çoklu ağaç kurulumunda tüm ağaçlar) için anlamsal arama dizinini manuel olarak yeniden oluşturmanız gerekir, aksi takdirde hatalarla veya anlamsız sonuçlarla karşılaşırsınız. Gramps Web, yapılandırılan gömme modelinin mevcut dizinle artık eşleşmediğini algılar ve yöneticilere [Yönetim Ayarları](../administration/settings.md#semantic-search-index) kısmından tam bir yeniden dizinleme tetiklemeleri için sürekli bir bildirim gösterir.
- Modeller, bir yandan doğruluk/genellik ile diğer yandan hesaplama süresi/depolama alanı arasında bir denge sağlar. Eğer Gramps Web API'yi güçlü bir GPU'ya erişimi olan bir sistemde çalıştırmıyorsanız, daha büyük modeller genellikle pratikte çok yavaş olur.
- Veritabanınızın tamamı İngilizce değilse ve tüm kullanıcılarınızın yalnızca İngilizce olarak sohbet soruları sorması beklenmiyorsa, daha nadir olan çok dilli bir gömme modeline ihtiyacınız olacaktır.

Eğer model yerel önbellekte yoksa, Gramps Web API ilk kez yeni yapılandırma ile başlatıldığında indirilecektir. Standart docker görüntülerini kullanırken `sentence-transformers/distiluse-base-multilingual-cased-v2` modeli zaten yerel olarak mevcuttur. Bu model iyi bir başlangıç noktasıdır ve çok dilli girişi destekler.

Farklı modeller hakkında öğrendiklerinizi toplulukla paylaşın!

!!! info
    Sentence transformers kütüphanesi önemli miktarda bellek tüketir, bu da işçi süreçlerinin sonlandırılmasına neden olabilir. Genel bir kural olarak, anlamsal arama etkinleştirildiğinde, her Gunicorn işçisi yaklaşık 200 MB bellek tüketir ve her celery işçisi, boşta bile yaklaşık 500 MB bellek tüketir ve gömme hesaplaması yaparken 1 GB'a kadar çıkabilir. Bellek kullanımını sınırlayan ayarlar için [CPU ve bellek kullanımını sınırlama](cpu-limited.md) kısmına bakın. Ayrıca, geçici bellek kullanımındaki ani artışlardan dolayı OOM hatalarını önlemek için yeterince büyük bir takas bölümü sağlamanız önerilir.

### Uzaktan bir gömme API'si kullanma

Yerel bir Sentence Transformers modelini çalıştırmanın bir alternatifi olarak, anlamsal arama için uzaktan OpenAI uyumlu bir gömme API'si kullanabilirsiniz. Bu, gömme hesaplamasını ayrı bir hizmete devretmek (örneğin, [Ollama](https://ollama.com/)), bir bulut gömme sağlayıcısı kullanmak (örneğin, OpenAI) veya Sentence Transformers ve PyTorch kütüphanelerini belleğe yüklemekten kaçınmak için faydalıdır.

Uzaktan API, [OpenAI gömme uç noktasına](https://platform.openai.com/docs/api-reference/embeddings) (`/v1/embeddings`) uyumlu olmalıdır.

Uzaktan bir gömme API'si kullanmak için, aşağıdaki yapılandırma seçeneklerini ayarlayın (bkz. [Sunucu Yapılandırması](configuration.md)):

Anahtar | Açıklama
-------|-------------
`VECTOR_EMBEDDING_MODEL` | Uzaktan sağlayıcıya iletilecek model adı
`VECTOR_EMBEDDING_BASE_URL` | Uzaktan API'nin temel URL'si
`VECTOR_EMBEDDING_API_KEY` | API anahtarı (yalnızca sağlayıcı kimlik doğrulama gerektiriyorsa gereklidir)

#### Gömme için Ollama kullanma

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

!!! info
    Gömme için Ollama kullanırken, Sentence Transformers ve PyTorch kütüphanelerine ihtiyaç yoktur, bu da Gramps Web API işçilerinin bellek kullanımını önemli ölçüde azaltır.

#### Gömme için OpenAI kullanma

OpenAI gömme API'sini kullanmak için, temel URL'yi OpenAI API'sine ayarlayın ve API anahtarınızı sağlayın:

```yaml
environment:
  GRAMPSWEB_VECTOR_EMBEDDING_MODEL: text-embedding-3-small
  GRAMPSWEB_VECTOR_EMBEDDING_BASE_URL: https://api.openai.com
  GRAMPSWEB_VECTOR_EMBEDDING_API_KEY: sk-...
```

!!! warning
    Gömme modelini değiştirmek, ağacınızdaki (veya çoklu ağaç kurulumundaki tüm ağaçlardaki) tüm kayıtların yeniden dizinlenmesini gerektirir, çünkü farklı modeller farklı boyutlarda vektörler üretir.

## Bir LLM sağlayıcısını ayarlama

LLM ile iletişim, OpenAI uyumlu API'leri destekleyen Pydantic AI çerçevesini kullanır. Bu, Ollama aracılığıyla yerel olarak dağıtılan bir LLM kullanmayı (bkz. [Ollama OpenAI uyumluluğu](https://ollama.com/blog/openai-compatibility)) veya OpenAI, Anthropic veya Hugging Face TGI (Metin Üretim Çıkarımı) gibi barındırılan API'leri kullanmayı sağlar. LLM, `LLM_MODEL` ve `LLM_BASE_URL` yapılandırma parametreleri aracılığıyla yapılandırılır.

### OpenAI API'si aracılığıyla barındırılan bir LLM kullanma

OpenAI API'sini kullanırken, `LLM_BASE_URL` ayarsız bırakılabilirken, `LLM_MODEL` OpenAI modellerinden birine, örneğin `gpt-4o-mini` olarak ayarlanmalıdır. LLM, soruları yanıtlamak için araç çağırma kullanır: veritabanını doğrudan özel araçlar kullanarak sorgular ve bulduğu kayıtlara dayanarak cevap verir. Derin soybilgisi veya tarih bilgisi gerektirmez. Bu nedenle, küçük/ucuz bir modelin yeterli olup olmadığını deneyebilirsiniz.

Ayrıca bir hesap oluşturmanız, bir API anahtarı almanız ve bunu `OPENAI_API_KEY` ortam değişkeninde saklamanız gerekecektir.

!!! info
    `LLM_MODEL` bir yapılandırma parametresidir; eğer bunu bir ortam değişkeni aracılığıyla ayarlamak istiyorsanız, `GRAMPSWEB_LLM_MODEL` kullanın (bkz. [Yapılandırma](configuration.md)). `OPENAI_API_KEY` bir yapılandırma parametresi değil, Pydantic AI kütüphanesi tarafından doğrudan kullanılan bir ortam değişkenidir, bu nedenle ön ek kullanılmamalıdır.

### Mistral AI kullanma

Mistral AI'nın barındırılan modellerini kullanmak için, `LLM_MODEL` ayarını yaparken model adını `mistral:` ile ön ekleyin.

Bir Mistral AI hesabı oluşturmanız, bir API anahtarı almanız ve bunu `MISTRAL_API_KEY` ortam değişkeninde saklamanız gerekecektir. `LLM_BASE_URL` ayarlamanıza gerek yoktur çünkü Pydantic AI otomatik olarak doğru Mistral API uç noktasını kullanacaktır.

Ortam değişkenleri ile docker compose kullanırken örnek yapılandırma:
```yaml
environment:
  GRAMPSWEB_LLM_MODEL: mistral:mistral-large-latest
  MISTRAL_API_KEY: your-mistral-api-key-here
```

### Ollama aracılığıyla yerel bir LLM kullanma

[Ollama](https://ollama.com/) yerel olarak LLM'leri çalıştırmanın pratik bir yoludur. Detaylar için Ollama belgelerine başvurun. LLM'lerin önemli hesaplama kaynaklarına ihtiyaç duyduğunu ve en küçük modeller dışında tüm modellerin muhtemelen GPU desteği olmadan çok yavaş olacağını unutmayın. Asistan araç çağırma kullandığı için, [`qwen2.5`](https://ollama.com/library/qwen2.5) gibi araçları destekleyen bir model seçin. `qwen2.5:7b` gibi küçük bir varyantla başlayın ve cevaplar yeterince iyi değilse daha büyük bir model deneyin. Herhangi bir deneyiminizi toplulukla paylaşın!

Gramps Web'i Docker Compose ile dağıtırken, bir Ollama hizmeti ekleyebilir ve Gramps Web'i buna yönlendirebilirsiniz:

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

Dikkat edilmesi gereken birkaç şey:

- `LLM_MODEL`'i, etiketini (noktalı kısımdan sonraki kısmı, örneğin `7b`) de içerecek şekilde, `ollama:` ile ön ekleyerek ayarlayın. Önek, Pydantic AI'nın model için Ollama'ya özel ayarları kullanmasını sağlar; bu, önerilen yapılandırmadır.
- `LLM_BASE_URL` `/v1/` ile bitmelidir, örneğin `http://ollama:11434/v1/`.
- `ollama:` öneki ile, ne `OPENAI_API_KEY` ne de `OLLAMA_BASE_URL` ortam değişkenine ihtiyaç vardır. Eğer `LLM_BASE_URL` ayarlanmamışsa, Gramps Web `OLLAMA_BASE_URL`'ye geri döner.
- Alternatif olarak, öneki atlayabilir (örneğin `LLM_MODEL: qwen2.5:7b`) ve Ollama'yı genel OpenAI uyumlu API'si aracılığıyla kullanabilirsiniz. Bu durumda, `OPENAI_API_KEY` ortam değişkenini `ollama` (herhangi bir boş olmayan değer işe yarar) olarak ayarlamanız gerekir.

Ollama ile ilgili sorunları gidermek için, Ollama hizmetinin ortamında `OLLAMA_DEBUG=1` ortam değişkenini ayarlayarak hata ayıklama günlüğünü etkinleştirebilirsiniz.

!!! info
    Eğer Gramps Web AI sohbeti için Ollama kullanıyorsanız, lütfen topluluğa destek olmak için bu belgeleri eksik detaylarla tamamlayın.

### Diğer sağlayıcıları kullanma

Lütfen diğer sağlayıcılar için belgeleri göndermekten çekinmeyin ve deneyimlerinizi toplulukla paylaşın!
