# Sunucu Yapılandırması

Varsayılan Docker görüntüsünü kullanarak, gerekli tüm yapılandırmalar tarayıcıdan yapılabilir. Ancak, dağıtıma bağlı olarak sunucu yapılandırmasını özelleştirmek gerekebilir.

Bu sayfa, yapılandırmayı değiştirme yöntemlerini ve mevcut tüm yapılandırma seçeneklerini listeler.


## Yapılandırma dosyası vs. ortam değişkenleri

Ayarlar için ya bir yapılandırma dosyası ya da ortam değişkenleri kullanabilirsiniz.

[Eğer Docker Compose tabanlı bir kurulum](deployment.md) kullanıyorsanız, `grampsweb:` bloğundaki `volumes:` anahtarının altına aşağıdaki liste öğesini ekleyerek bir yapılandırma dosyası dahil edebilirsiniz:

```yaml
      - /path/to/config.cfg:/app/config/config.cfg
```
burada `/path/to/config.cfg`, sunucunuzun dosya sistemindeki yapılandırma dosyasının yoludur (sağ taraf, konteynerdeki yolu ifade eder ve değiştirilmemelidir).

Ortam değişkenleri kullanırken,

- her ayar adını `GRAMPSWEB_` ile ön ekleyin, böylece ortam değişkeninin adını elde edersiniz
- İç içe sözlük ayarları için çift alt çizgi kullanın, örneğin `GRAMPSWEB_THUMBNAIL_CACHE_CONFIG__CACHE_DEFAULT_TIMEOUT` ayarı, `THUMBNAIL_CACHE_CONFIG['CACHE_DEFAULT_TIMEOUT']` yapılandırma seçeneğinin değerini ayarlayacaktır.

Ortam üzerinden ayarlanan yapılandırma seçeneklerinin, yapılandırma dosyasındaki seçeneklere göre önceliği olduğunu unutmayın. Her ikisi de mevcutsa, ortam değişkeni "kazanır".

!!! warning "Ön eklenmemiş ortam değişkenleri kullanımdan kaldırılmıştır"
    Tarihsel nedenlerden dolayı, bir avuç ayar – `TREE`, `SECRET_KEY`, `USER_DB_URI`, `POSTGRES_USER`, `POSTGRES_PASSWORD`, `MEDIA_BASE_DIR`, `SEARCH_INDEX_DIR`, `EMAIL_HOST`, `EMAIL_PORT`, `EMAIL_HOST_USER`, `EMAIL_HOST_PASSWORD`, `DEFAULT_FROM_EMAIL`, `BASE_URL` ve `STATIC_PATH` – hala `GRAMPSWEB_` ön eki olmadan bir ortam değişkeni aracılığıyla ayarlanabilir. Bu artık kullanımdan kaldırılmıştır, başlangıçta bir uyarı kaydeder ve gelecekteki bir sürümde çalışmayı durduracaktır. Her zaman ön ekli biçimi kullanın, örneğin `TREE` yerine `GRAMPSWEB_TREE`.

    Bunun yalnızca ortam değişkenlerini ilgilendirdiğini unutmayın. Bir yapılandırma dosyasında, ayar adları her zaman ön ek olmadan kullanılır.

!!! tip "Kullanımdan kaldırılmış seçenekleri kontrol etme"
    Sunucunuzun hala bağımlı olduğu kullanımdan kaldırılmış yapılandırma seçenekleri – ön eklenmemiş ortam değişkenleri, `SEARCH_INDEX_DIR` veya `EMAIL_USE_TLS` gibi – başlangıçta uyarı olarak kaydedilir. Gramps Web API 3.22'den itibaren, bunlar ayrıca, yerel bir yönetici olarak oturum açtığınızda **Sistem Bilgileri** sayfasının en üstünde, yerini alacakları ve desteklerinin kaldırılacağı sürümü ile birlikte listelenir.

## Mevcut yapılandırma ayarları
Aşağıdaki yapılandırma seçenekleri mevcuttur.

### Gerekli ayarlar

Anahtar | Açıklama
----|-------------
`TREE` | Kullanılacak aile ağacı veritabanının adı. Mevcut ağaçları `gramps -l` ile gösterin. Bu isimde bir ağaç yoksa, yeni boş bir ağaç oluşturulacaktır.
`SECRET_KEY` | Flask için gizli anahtar. Gizli anahtar kamuya açık olarak paylaşılmamalıdır. Değiştirilmesi, tüm erişim jetonlarını geçersiz kılar.
`USER_DB_URI` | Kullanıcı veritabanının veritabanı URL'si. SQLAlchemy ile uyumlu herhangi bir URL kabul edilir.

!!! info
    Güvenli bir gizli anahtar oluşturmak için örneğin şu komutu kullanabilirsiniz:

    ```
    python3 -c "import secrets;print(secrets.token_urlsafe(32))"
    ```

### Opsiyonel ayarlar

Anahtar | Açıklama
----|-------------
`MEDIA_BASE_DIR` | Medya dosyaları için temel dizin olarak kullanılacak yol, Gramps'ta ayarlanan medya temel dizinini geçersiz kılar. [S3](s3.md) kullanırken, `s3://<bucket_name>` biçiminde olmalıdır.
`TREE_ID` | Tek ağaç modunda kullanılacak aile ağacı veritabanının dizin adı (eğer `TREE` `*` olarak ayarlanmamışsa). Ayarlandığında, sunucu ağacı dizin adıyla tanımlar, bu da yeniden adlandırmalara karşı daha dayanıklıdır. API aracılığıyla ağacı yeniden adlandırmak istiyorsanız gereklidir. Dizin adı `GET /api/trees/-` (id alanı) aracılığıyla bulunabilir.
`SEARCH_INDEX_DB_URI` | Arama dizini için veritabanı URL'si. Yalnızca `sqlite` veya `postgresql` arka uçları kabul edilir. Varsayılan olarak `sqlite:///indexdir/search_index.db` olup, scriptin çalıştığı yola göre `indexdir` klasöründe bir SQLite dosyası oluşturur.
`SEARCH_INDEX_DIR` | **Kullanımdan kaldırılmıştır** (bunun yerine `SEARCH_INDEX_DB_URI` kullanın). Arama dizinini içeren dizin. `SEARCH_INDEX_DB_URI` ayarlanmamışken ayarlanırsa, arama dizini URL'si `sqlite:///<SEARCH_INDEX_DIR>/search_index.db` olarak türetilir.
`STATIC_PATH` | Statik dosyaların sunulacağı yol (örneğin, statik bir web ön yüzü)
`BASE_URL` | API'nin erişilebileceği temel URL (örneğin, `https://mygramps.mydomain.com/`). Bu, doğru şifre sıfırlama bağlantıları oluşturmak için gereklidir.
`CORS_ORIGINS` | CORS isteklerinin izin verildiği kökenler. Varsayılan olarak, hepsi yasaktır. Herhangi bir alan adından istekleri izin vermek için `"*"` kullanın.
`EMAIL_HOST` | SMTP sunucu ana bilgisayarı (örneğin, şifre sıfırlama e-postalarını göndermek için)
`EMAIL_PORT` | SMTP sunucu portu. Varsayılan olarak 465
`EMAIL_HOST_USER` | SMTP sunucu kullanıcı adı
`EMAIL_HOST_PASSWORD` | SMTP sunucu şifresi
`EMAIL_USE_TLS` | **Kullanımdan kaldırılmıştır** (bunun yerine `EMAIL_USE_SSL` veya `EMAIL_USE_STARTTLS` kullanın). E-postaları göndermek için TLS kullanılıp kullanılmayacağını belirten boolean. Varsayılan olarak `True`'dur. STARTTLS kullanırken, bunu `False` olarak ayarlayın ve 25'ten farklı bir port kullanın.
`EMAIL_USE_SSL` | SMTP için örtük SSL/TLS kullanılıp kullanılmayacağını belirten boolean (v3.6.0+). `EMAIL_USE_TLS` açıkça ayarlanmamışsa varsayılan olarak `True`'dur. Genellikle 465 portu ile kullanılır.
`EMAIL_USE_STARTTLS` | SMTP için açık STARTTLS kullanılıp kullanılmayacağını belirten boolean (v3.6.0+). Varsayılan olarak `False`'dır. Genellikle 587 veya 25 portu ile kullanılır.
`DEFAULT_FROM_EMAIL` | Otomatik e-postalar için "Gönderen" adresi
`THUMBNAIL_CACHE_CONFIG` | Küçük resim önbelleği için ayarları içeren sözlük. Olası ayarlar için [Flask-Caching](https://flask-caching.readthedocs.io/en/latest/) sayfasına bakın.
`REQUEST_CACHE_CONFIG` | İstek önbelleği için ayarları içeren sözlük. Olası ayarlar için [Flask-Caching](https://flask-caching.readthedocs.io/en/latest/) sayfasına bakın.
`PERSISTENT_CACHE_CONFIG` | Kalıcı önbellek için ayarları içeren sözlük, örneğin telemetri için kullanılır. Olası ayarlar için [Flask-Caching](https://flask-caching.readthedocs.io/en/latest/) sayfasına bakın.
`CELERY_CONFIG` | Celery arka plan görev kuyruğu için ayarlar. Olası ayarlar için [Celery](https://docs.celeryq.dev/en/stable/userguide/configuration.html) sayfasına bakın.
`REPORT_DIR` | Gramps raporlarının çıktısının depolanacağı geçici dizin
`EXPORT_DIR` | Gramps veritabanasının dışa aktarım çıktısının depolanacağı geçici dizin
`REGISTRATION_DISABLED` | Eğer `True` ise, yeni kullanıcı kaydını engelle (varsayılan `False`)
`DISABLE_TELEMETRY` | Eğer `True` ise, istatistik telemetrisini devre dışı bırak (varsayılan `False`). Detaylar için [telemetri](telemetry.md) sayfasına bakın.
`PILLOW_MAX_IMAGE_PIXELS` | İşlenen görüntünün içerebileceği piksel sayısını belirten PIL.Image.MAX_IMAGE_PIXELS parametresini ayarlar. Detaylar için [docs](https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.MAX_IMAGE_PIXELS) sayfasına bakın.
`MAX_THUMBNAIL_FILE_BYTES` | Küçük resimler için zorunlu maksimum dosya boyutunu ayarlar. Varsayılan olarak `50 * 1024 * 1024` (50 MB) olarak ayarlanmıştır. Bunu artırmak, bellek kullanımını büyük ölçüde artırabilir ve büyük dosyaların bellekte açılması durumunda bellek yetersizliği hatalarına veya veri kaybına yol açabilir.

!!! info
    Yapılandırma için ortam değişkenleri kullanırken, `EMAIL_USE_SSL` gibi boolean seçeneklerin ya `true` ya da `false` (büyük/küçük harf duyarlı!) olarak ayarlanması gerektiğini unutmayın.

### Sadece PostgreSQL arka uç veritabanı için ayarlar

Bu, Gramps veritabanınızı [PostgreSQL eklentisi](https://gramps-project.org/wiki/index.php/Addon:PostgreSQL) ile çalışacak şekilde yapılandırdıysanız gereklidir.

Anahtar | Açıklama
----|-------------
`POSTGRES_USER` | Veritabanı bağlantısı için kullanıcı adı
`POSTGRES_PASSWORD` | Veritabanı kullanıcısı için şifre

### Birden fazla ağaç barındırmak için ilgili ayarlar

[Ağaçları birden fazla barındırırken](multi-tree.md) aşağıdaki ayarlar geçerlidir.

Anahtar | Açıklama
----|-------------
`MEDIA_PREFIX_TREE` | Her ağacın medya dosyaları için ayrı bir alt klasör kullanılıp kullanılmayacağını belirten boolean. Varsayılan olarak `False`'dur, ancak çoklu ağaç kurulumunda `True` kullanılması şiddetle önerilir.
`NEW_DB_BACKEND` | Yeni oluşturulan aile ağaçları için kullanılacak veritabanı arka ucu. `sqlite`, `postgresql` veya `sharedpostgresql`'den biri olmalıdır. Varsayılan olarak `sqlite`'dır.
`POSTGRES_HOST` | Paylaşılan PostgreSQL arka ucu ile çoklu ağaç kurulumunda yeni ağaçlar oluşturmak için kullanılan PostgreSQL sunucusunun ana bilgisayar adı
`POSTGRES_PORT` | Paylaşılan PostgreSQL arka ucu ile çoklu ağaç kurulumunda yeni ağaçlar oluşturmak için kullanılan PostgreSQL sunucusunun portu

### OIDC kimlik doğrulaması için ayarlar

Bu ayarlar, dış sağlayıcılarla OpenID Connect (OIDC) kimlik doğrulaması kullanmak istiyorsanız gereklidir. Ayrıntılı kurulum talimatları ve örnekler için [OIDC Kimlik Doğrulaması](oidc.md) sayfasına bakın.

Anahtar | Açıklama
----|-------------
`OIDC_ENABLED` | OIDC kimlik doğrulamasını etkinleştirip etkinleştirmeyeceğini belirten boolean. Varsayılan olarak `False`'dır.
`OIDC_ISSUER` | OIDC sağlayıcı yayımlayıcı URL'si (özel OIDC sağlayıcıları için)
`OIDC_CLIENT_ID` | OAuth istemci kimliği (özel OIDC sağlayıcıları için)
`OIDC_CLIENT_SECRET` | OAuth istemci sırrı (özel OIDC sağlayıcıları için)
`OIDC_NAME` | Sağlayıcı için özel görüntüleme adı. Varsayılan olarak "OIDC"dır.
`OIDC_SCOPES` | OAuth kapsamları. Varsayılan olarak "openid email profile"dır.
`OIDC_USERNAME_CLAIM` | Kullanıcı adı için kullanılacak talep. Varsayılan olarak "preferred_username"dır.
`OIDC_OPENID_CONFIG_URL` | İsteğe bağlı: OpenID Connect yapılandırma uç noktasının URL'si (standart `/.well-known/openid-configuration` kullanılmıyorsa)
`OIDC_DISABLE_LOCAL_AUTH` | Yerel kullanıcı adı/şifre kimlik doğrulamasını devre dışı bırakıp bırakmayacağını belirten boolean. Varsayılan olarak `False`'dır.
`OIDC_AUTO_REDIRECT` | Sadece bir sağlayıcı yapılandırıldığında otomatik olarak OIDC'ye yönlendirilip yönlendirilmeyeceğini belirten boolean. Varsayılan olarak `False`'dır.

#### Yerleşik OIDC sağlayıcıları

Yerleşik sağlayıcılar (Google, Microsoft) için bu ayarları kullanın:

Anahtar | Açıklama
----|-------------
`OIDC_GOOGLE_CLIENT_ID` | Google OAuth için istemci kimliği
`OIDC_GOOGLE_CLIENT_SECRET` | Google OAuth için istemci sırrı
`OIDC_MICROSOFT_CLIENT_ID` | Microsoft OAuth için istemci kimliği
`OIDC_MICROSOFT_CLIENT_SECRET` | Microsoft OAuth için istemci sırrı

#### OIDC Rol Eşlemesi

Bu ayarlar, kimlik sağlayıcınızdan OIDC gruplarını/rollerini Gramps Web kullanıcı rollerine eşlemenizi sağlar:

Anahtar | Açıklama
----|-------------
`OIDC_ROLE_CLAIM` | Kullanıcının gruplarını/rollerini içeren OIDC jetonundaki talep adı. Varsayılan olarak "groups"dır.
`OIDC_GROUP_ADMIN` | Gramps "Yönetici" rolüne eşlenen OIDC sağlayıcınızdaki grup/rol adı
`OIDC_GROUP_OWNER` | Gramps "Sahip" rolüne eşlenen OIDC sağlayıcınızdaki grup/rol adı
`OIDC_GROUP_EDITOR` | Gramps "Editör" rolüne eşlenen OIDC sağlayıcınızdaki grup/rol adı
`OIDC_GROUP_CONTRIBUTOR` | Gramps "Katkıda Bulunan" rolüne eşlenen OIDC sağlayıcınızdaki grup/rol adı
`OIDC_GROUP_MEMBER` | Gramps "Üye" rolüne eşlenen OIDC sağlayıcınızdaki grup/rol adı
`OIDC_GROUP_GUEST` | Gramps "Misafir" rolüne eşlenen OIDC sağlayıcınızdaki grup/rol adı

### Sadece AI özellikleri için ayarlar

Bu ayarlar, sohbet veya anlamsal arama gibi AI destekli özellikleri kullanmak istiyorsanız gereklidir.

Anahtar | Açıklama
----|-------------
`LLM_BASE_URL` | OpenAI uyumlu sohbet API'si için temel URL. Varsayılan olarak `None` olup, OpenAI API'sini kullanır.
`LLM_MODEL` | OpenAI uyumlu sohbet API'si için kullanılacak model. Ayarlanmazsa (varsayılan), sohbet devre dışıdır. v3.6.0'dan itibaren, AI asistanı araç çağırma yetenekleri ile Pydantic AI kullanır.
`VECTOR_EMBEDDING_MODEL` | Anlamsal arama vektör gömme işlemleri için kullanılacak model. Yerel bir model kullanıyorsanız, bu bir [Sentence Transformers](https://sbert.net/) model adı olmalıdır. Uzaktan bir API kullanıyorsanız (bkz. `VECTOR_EMBEDDING_BASE_URL`), bu uzaktan sağlayıcıya iletilen model adıdır. Ayarlanmazsa (varsayılan), anlamsal arama ve sohbet devre dışıdır.
`VECTOR_EMBEDDING_BASE_URL` | Uzaktan OpenAI uyumlu gömme API'si için temel URL (örneğin, Ollama, OpenAI, LiteLLM). Ayarlanmazsa (varsayılan), yerel bir Sentence Transformers modeli kullanılır. Ayrıntılar için [Uzaktan bir gömme API'si kullanma](chat.md#using-a-remote-embedding-api) sayfasına bakın.
`VECTOR_EMBEDDING_API_KEY` | Kimlik doğrulamalı uzaktan gömme sağlayıcıları için API anahtarı. Sadece `VECTOR_EMBEDDING_BASE_URL` ayarlandığında ve sağlayıcı kimlik doğrulaması gerektiriyorsa gereklidir.
`LLM_MAX_CONTEXT_LENGTH` | LLM'ye sağlanan aile ağacı bağlamı için karakter sınırı. Varsayılan olarak 50000'dir.
`LLM_SYSTEM_PROMPT` | LLM sohbet asistanı için özel sistem istemi (v3.6.0+). Ayarlanmazsa, varsayılan soydan optimize edilmiş istemi kullanır.

## Örnek yapılandırma dosyası

Üretim için minimal bir yapılandırma dosyası şöyle görünebilir:
```python
TREE="Ailem Ağacı"
BASE_URL="https://mytree.example.com"
SECRET_KEY="..."  # gizli anahtarınız
USER_DB_URI="sqlite:////path/to/users.sqlite"
EMAIL_HOST="mail.example.com"
EMAIL_PORT=465
EMAIL_USE_SSL=True  # 465 portu için örtük SSL kullan
EMAIL_HOST_USER="gramps@example.com"
EMAIL_HOST_PASSWORD="..." # SMTP şifreniz
DEFAULT_FROM_EMAIL="gramps@example.com"
