# Sunucu Yapılandırması

Varsayılan Docker görüntüsünü kullanarak, gerekli tüm yapılandırmalar tarayıcıdan yapılabilir. Ancak, dağıtıma bağlı olarak sunucu yapılandırmasını özelleştirmek gerekebilir.

Bu sayfa, yapılandırmayı değiştirmek için tüm yöntemleri ve mevcut tüm yapılandırma seçeneklerini listeler.


## Yapılandırma dosyası vs. ortam değişkenleri

Ayarlar için ya bir yapılandırma dosyası ya da ortam değişkenleri kullanabilirsiniz.

[Eğer Docker Compose tabanlı bir kurulum](deployment.md) kullanıyorsanız, `grampsweb:` bloğundaki `volumes:` anahtarının altına aşağıdaki liste öğesini ekleyerek bir yapılandırma dosyası dahil edebilirsiniz:

```yaml
      - /path/to/config.cfg:/app/config/config.cfg
```
burada `/path/to/config.cfg`, sunucunuzun dosya sistemindeki yapılandırma dosyasının yoludur (sağ tarafta konteynerdeki yol belirtilmiştir ve değiştirilmemelidir).

Ortam değişkenleri kullanıldığında,

- her ayar adını `GRAMPSWEB_` ile öne ekleyerek ortam değişkeninin adını elde edin
- İç içe sözlük ayarları için çift alt çizgi kullanın, örneğin `GRAMPSWEB_THUMBNAIL_CACHE_CONFIG__CACHE_DEFAULT_TIMEOUT`, `THUMBNAIL_CACHE_CONFIG['CACHE_DEFAULT_TIMEOUT']` yapılandırma seçeneğinin değerini ayarlayacaktır.

Ortam aracılığıyla ayarlanan yapılandırma seçeneklerinin, yapılandırma dosyasındaki seçeneklerden önceliği vardır. Her ikisi de mevcutsa, ortam değişkeni "kazanır".

!!! warning "Öne eklenmemiş ortam değişkenleri kullanım dışıdır"
    Tarihsel nedenlerden dolayı, bir avuç ayar – `TREE`, `SECRET_KEY`, `USER_DB_URI`, `POSTGRES_USER`, `POSTGRES_PASSWORD`, `MEDIA_BASE_DIR`, `SEARCH_INDEX_DIR`, `EMAIL_HOST`, `EMAIL_PORT`, `EMAIL_HOST_USER`, `EMAIL_HOST_PASSWORD`, `DEFAULT_FROM_EMAIL`, `BASE_URL` ve `STATIC_PATH` – hala `GRAMPSWEB_` öne eki olmadan bir ortam değişkeni aracılığıyla ayarlanabilir. Bu kullanım dışıdır, başlangıçta bir uyarı kaydeder ve gelecekteki bir sürümde çalışmayı durduracaktır. Her zaman öne ekli formu kullanın, örneğin `GRAMPSWEB_TREE` yerine `TREE`.

    Bunun yalnızca ortam değişkenlerini ilgilendirdiğini unutmayın. Bir yapılandırma dosyasında, ayar adları her zaman öne ek olmadan kullanılır.

!!! tip "Kullanım dışı seçenekleri kontrol etme"
    Sunucunuzun hala bağımlı olduğu kullanım dışı yapılandırma seçenekleri – öne eklenmemiş ortam değişkenleri, `SEARCH_INDEX_DIR` veya `EMAIL_USE_TLS` gibi – başlangıçta uyarı olarak kaydedilir. Gramps Web API 3.22'den itibaren, bunlar ayrıca, yerini alacakları ve desteklerinin kaldırılacağı sürüm ile birlikte **Sistem Bilgileri** sayfasının en üstünde listelenir (yönetici olarak oturum açtığınızda üst uygulama çubuğundaki kullanıcı simgesinden erişilebilir).

## Mevcut yapılandırma ayarları
Aşağıdaki yapılandırma seçenekleri mevcuttur.

### Gerekli ayarlar

Anahtar | Açıklama
----|-------------
`TREE` | Kullanılacak aile ağacı veritabanının adı. Mevcut ağaçları `gramps -l` ile gösterin. Bu isimde bir ağaç yoksa, yeni boş bir tane oluşturulacaktır.
`SECRET_KEY` | Flask için gizli anahtar. Gizli anahtar kamuya açık olarak paylaşılmamalıdır. Değiştirilmesi, tüm erişim jetonlarını geçersiz kılacaktır.
`USER_DB_URI` | Kullanıcı veritabanının veritabanı URL'si. SQLAlchemy ile uyumlu herhangi bir URL kabul edilir.

!!! info
    Güvenli bir gizli anahtar oluşturmak için örneğin şu komutu kullanabilirsiniz:

    ```
    python3 -c "import secrets;print(secrets.token_urlsafe(32))"
    ```

### İsteğe Bağlı Ayarlar

Anahtar | Açıklama
----|-------------
`MEDIA_BASE_DIR` | Medya dosyaları için temel dizin olarak kullanılacak yol, Gramps'ta ayarlanan medya temel dizinini geçersiz kılar. [S3](s3.md) kullanıldığında, `s3://<bucket_name>` biçiminde olmalıdır.
`TREE_ID` | Tek ağaç modunda kullanılacak aile ağacı veritabanının dizin adı (eğer `TREE` `*` olarak ayarlanmamışsa). Ayarlandığında, sunucu ağacı dizin adıyla tanımlar, bu da yeniden adlandırmalara karşı daha sağlamdır. API aracılığıyla ağacı yeniden adlandırmak istiyorsanız gereklidir. Dizin adı `GET /api/trees/-` ile bulunabilir ( `id` alanı).
`SEARCH_INDEX_DB_URI` | Arama dizini için veritabanı URL'si. Yalnızca `sqlite` veya `postgresql` arka uçları kabul edilir. Varsayılan olarak `sqlite:///indexdir/search_index.db` olarak ayarlanır ve `indexdir` klasöründe bir SQLite dosyası oluşturur.
`SEARCH_INDEX_DIR` | **Kullanım dışı** (bunun yerine `SEARCH_INDEX_DB_URI` kullanın). Arama dizinini içeren dizin. `SEARCH_INDEX_DB_URI` ayarlanmamışken ayarlanırsa, arama dizini URL'si `sqlite:///<SEARCH_INDEX_DIR>/search_index.db` olarak türetilir.
`STATIC_PATH` | Statik dosyaların sunulacağı yol (örneğin, statik bir web ön ucu)
`BASE_URL` | API'nin ulaşılabileceği temel URL (örneğin, `https://mygramps.mydomain.com/`). Bu, doğru şifre sıfırlama bağlantıları oluşturmak için gereklidir. Web Push ayrıca kamuya açık erişilebilir bir HTTPS URL'si gerektirir; varsayılan `http://localhost/` Web Push'ı devre dışı bırakır. Bu ayarı ortam aracılığıyla yapılandırırken, `GRAMPSWEB_BASE_URL` kullanın.
`CORS_ORIGINS` | CORS isteklerinin izin verildiği kökenler. Varsayılan olarak, tümü yasaktır. Herhangi bir alan adından istekleri izin vermek için `"*"` kullanın.
`EMAIL_HOST` | SMTP sunucu ana bilgisayarı (örneğin, şifre sıfırlama e-postalarını göndermek için)
`EMAIL_PORT` | SMTP sunucu portu. varsayılan olarak 465
`EMAIL_HOST_USER` | SMTP sunucu kullanıcı adı
`EMAIL_HOST_PASSWORD` | SMTP sunucu şifresi
`EMAIL_USE_TLS` | **Kullanım dışı** (bunun yerine `EMAIL_USE_SSL` veya `EMAIL_USE_STARTTLS` kullanın). E-postaları göndermek için TLS kullanılıp kullanılmayacağını belirten Boolean. Varsayılan olarak `True`'dur. STARTTLS kullanırken, bunu `False` olarak ayarlayın ve 25'ten farklı bir port kullanın.
`EMAIL_USE_SSL` | SMTP için örtük SSL/TLS kullanılıp kullanılmayacağını belirten Boolean (v3.6.0+). `EMAIL_USE_TLS` açıkça ayarlanmamışsa varsayılan olarak `True`'dur. Genellikle 465 portu ile kullanılır.
`EMAIL_USE_STARTTLS` | SMTP için açık STARTTLS kullanılıp kullanılmayacağını belirten Boolean (v3.6.0+). Varsayılan olarak `False`'dır. Genellikle 587 veya 25 portu ile kullanılır.
`DEFAULT_FROM_EMAIL` | Otomatik e-postalar için "Gönderen" adresi
`THUMBNAIL_CACHE_CONFIG` | Küçük resim önbelleği için ayarları içeren sözlük. Olası ayarlar için [Flask-Caching](https://flask-caching.readthedocs.io/en/latest/) sayfasına bakın.
`REQUEST_CACHE_CONFIG` | İstek önbelleği için ayarları içeren sözlük. Olası ayarlar için [Flask-Caching](https://flask-caching.readthedocs.io/en/latest/) sayfasına bakın.
`PERSISTENT_CACHE_CONFIG` | Sürekli önbellek için ayarları içeren sözlük, örneğin telemetri için kullanılır. Olası ayarlar için [Flask-Caching](https://flask-caching.readthedocs.io/en/latest/) sayfasına bakın.
`CELERY_CONFIG` | Celery arka plan görev kuyruğu için ayarlar. Olası ayarlar için [Celery](https://docs.celeryq.dev/en/stable/userguide/configuration.html) sayfasına bakın.
`REPORT_DIR` | Gramps raporlarının çıktısının saklanacağı geçici dizin
`EXPORT_DIR` | Gramps veritabanasının dışa aktarım çıktısının saklanacağı geçici dizin
`BACKUP_DIR` | [yedeklerin](../administration/settings.md#backups) saklandığı dizin, her ağaç için bir alt dizin içinde (v3.24.0+). Ayarlanmazsa (varsayılan), yedekler sunucuda saklanamaz, ancak yüklenen bir dosyadan geri yüklenebilir. Kalıcı bir konum kullanın, örneğin bir Docker hacmi ve tercihen kendisi de yedeklenen veya başka bir yerde senkronize edilen bir konum.
`BACKUP_KEEP` | Her ağaç için saklanan yedek sayısı; daha eski olanlar yeni bir yedek oluşturulduğunda silinir (v3.24.0+). Varsayılan olarak `5`
`RATE_LIMIT_BACKUP` | Yedek oluşturma için hız limiti, ağaç başına (v3.24.0+). Varsayılan olarak `"günde 10"`
`RATE_LIMIT_MEDIA_ARCHIVE` | Dışa Aktarma sayfasında medya arşivleri oluşturma için hız limiti. Varsayılan olarak `"saate 1"`
`REGISTRATION_DISABLED` | `True` ise, yeni kullanıcı kaydını yasakla (varsayılan `False`)
`DISABLE_TELEMETRY` | `True` ise, istatistik telemetrisini devre dışı bırak (varsayılan `False`). Ayrıntılar için [telemetri](telemetry.md) sayfasına bakın.
`PILLOW_MAX_IMAGE_PIXELS` | İşlenen görüntünün içerebileceği piksel sayısını belirten PIL.Image.MAX_IMAGE_PIXELS parametresini ayarlar. Ayrıntılar için [belgelere](https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.MAX_IMAGE_PIXELS) bakın.
`MAX_THUMBNAIL_FILE_BYTES` | Küçük resimler için katı maksimum dosya boyutunu ayarlar. Varsayılan olarak `50 * 1024 * 1024` (50 MB) olarak ayarlanmıştır. Bunu artırmak, bellek kullanımını büyük ölçüde artırabilir ve büyük dosyaların bellekte açılması durumunda bellek yetersizliği çökmesine veya veri kaybına yol açabilir.


!!! info
    Yapılandırma için ortam değişkenleri kullanıldığında, `EMAIL_USE_SSL` gibi Boolean seçeneklerin ya `true` ya da `false` (büyük/küçük harf duyarlı!) olarak ayarlanması gerekir.


### PostgreSQL veritabanları için ayarlar

Bu ayarlar, aile ağaçlarınız [PostgreSQL veritabanında](postgres.md) SharedPostgreSQL eklentisi kullanılarak barındırılıyorsa gereklidir.

Anahtar | Açıklama
----|-------------
`POSTGRES_USER` | Veritabanı bağlantısı için kullanıcı adı
`POSTGRES_PASSWORD` | Veritabanı kullanıcısı için şifre


### Birden fazla ağaç barındırma ile ilgili ayarlar

Aşağıdaki ayarlar, [birden fazla ağaç barındırırken](multi-tree.md) geçerlidir.

Anahtar | Açıklama
----|-------------
`MEDIA_PREFIX_TREE` | Her ağacın medya dosyaları için ayrı bir alt klasör kullanılıp kullanılmayacağını belirten Boolean. Varsayılan olarak `False`, ancak çoklu ağaç kurulumunda `True` kullanılması şiddetle önerilir.
`NEW_DB_BACKEND` | Yeni oluşturulan aile ağaçları için kullanılacak veritabanı arka ucu. `sqlite` veya `sharedpostgresql`'dan biri olmalıdır. Varsayılan olarak `sqlite`'dır. `postgresql` değeri hala kabul edilir ancak kullanım dışıdır, çünkü PostgreSQL arka ucu Gramps Web API 4.0'da kaldırılacaktır.
`POSTGRES_HOST` | SharedPostgreSQL arka ucunu kullanan çoklu ağaç kurulumunda yeni ağaçlar oluşturmak için kullanılan PostgreSQL sunucusunun ana bilgisayar adı
`POSTGRES_PORT` | SharedPostgreSQL arka ucunu kullanan çoklu ağaç kurulumunda yeni ağaçlar oluşturmak için kullanılan PostgreSQL sunucusunun portu


### OIDC kimlik doğrulaması için ayarlar

Bu ayarlar, harici sağlayıcılarla OpenID Connect (OIDC) kimlik doğrulaması kullanmak istiyorsanız gereklidir. Ayrıntılı kurulum talimatları ve örnekler için [OIDC Kimlik Doğrulaması](oidc.md) sayfasına bakın.

Anahtar | Açıklama
----|-------------
`OIDC_ENABLED` | OIDC kimlik doğrulamasını etkinleştirip etkinleştirmeyeceğini belirten Boolean. Varsayılan olarak `False`.
`OIDC_ISSUER` | OIDC sağlayıcı yayımlayıcı URL'si (özel OIDC sağlayıcıları için)
`OIDC_CLIENT_ID` | OAuth istemci kimliği (özel OIDC sağlayıcıları için)
`OIDC_CLIENT_SECRET` | OAuth istemci sırrı (özel OIDC sağlayıcıları için)
`OIDC_NAME` | Sağlayıcı için özel görüntüleme adı. Varsayılan olarak "OIDC"
`OIDC_SCOPES` | OAuth kapsamları. Varsayılan olarak "openid email profile"
`OIDC_USERNAME_CLAIM` | Kullanıcı adı için kullanılacak talep. Varsayılan olarak "preferred_username"
`OIDC_OPENID_CONFIG_URL` | İsteğe bağlı: OpenID Connect yapılandırma uç noktasının URL'si (standart `/.well-known/openid-configuration` kullanılmıyorsa)
`OIDC_PKCE` | PKCE kullanılıp kullanılmayacağını belirten Boolean. Ayarlanmazsa, sağlayıcının keşif belgesi `S256` listelendiğinde PKCE kullanılır. [PKCE](oidc.md#pkce) sayfasına bakın.
`OIDC_DISABLE_LOCAL_AUTH` | Yerel kullanıcı adı/şifre kimlik doğrulamasını devre dışı bırakıp bırakmayacağını belirten Boolean. Varsayılan olarak `False`
`OIDC_AUTO_REDIRECT` | Sadece bir sağlayıcı yapılandırıldığında otomatik olarak OIDC'ye yönlendirilip yönlendirilmeyeceğini belirten Boolean. Varsayılan olarak `False`

#### Yerleşik OIDC sağlayıcıları

Yerleşik sağlayıcılar (Google, Microsoft) için bu ayarları kullanın:

Anahtar | Açıklama
----|-------------
`OIDC_GOOGLE_CLIENT_ID` | Google OAuth için istemci kimliği
`OIDC_GOOGLE_CLIENT_SECRET` | Google OAuth için istemci sırrı
`OIDC_MICROSOFT_CLIENT_ID` | Microsoft OAuth için istemci kimliği
`OIDC_MICROSOFT_CLIENT_SECRET` | Microsoft OAuth için istemci sırrı
`OIDC_GOOGLE_PKCE` | Google için PKCE ayarı, [PKCE](oidc.md#pkce) sayfasına bakın
`OIDC_MICROSOFT_PKCE` | Microsoft için PKCE ayarı, [PKCE](oidc.md#pkce) sayfasına bakın

#### OIDC Rol Eşlemesi

Bu ayarlar, kimlik sağlayıcınızdan OIDC gruplarını/rollerini Gramps Web kullanıcı rollerine eşlemenizi sağlar:

Anahtar | Açıklama
----|-------------
`OIDC_ROLE_CLAIM` | Kullanıcının gruplarını/rollerini içeren OIDC jetonundaki talep adı. Varsayılan olarak "groups"
`OIDC_GROUP_ADMIN` | Gramps "Yönetici" rolüne eşlenen OIDC sağlayıcınızdan grup/rol adı
`OIDC_GROUP_OWNER` | Gramps "Sahip" rolüne eşlenen OIDC sağlayıcınızdan grup/rol adı
`OIDC_GROUP_EDITOR` | Gramps "Editör" rolüne eşlenen OIDC sağlayıcınızdan grup/rol adı
`OIDC_GROUP_CONTRIBUTOR` | Gramps "Katkıda Bulunan" rolüne eşlenen OIDC sağlayıcınızdan grup/rol adı
`OIDC_GROUP_MEMBER` | Gramps "Üye" rolüne eşlenen OIDC sağlayıcınızdan grup/rol adı
`OIDC_GROUP_GUEST` | Gramps "Misafir" rolüne eşlenen OIDC sağlayıcınızdan grup/rol adı

### Sadece AI özellikleri için ayarlar

Bu ayarlar, sohbet veya anlamsal arama gibi AI destekli özellikleri kullanmak istiyorsanız gereklidir. Ayrıntılar için [AI sohbetini ayarlama](chat.md) sayfasına bakın.

!!! warning "Anlamsal arama kullanım dışıdır"
    Anlamsal arama ve bununla birlikte `VECTOR_EMBEDDING_*` ayarları kullanım dışıdır ve Gramps Web API 3.25'te kaldırılacaktır. Bundan sonra, `VECTOR_EMBEDDING_MODEL` hala kabul edilir ancak göz ardı edilir. Gramps Web API 3.24'ten itibaren, AI sohbeti yalnızca `LLM_MODEL` gerektirir.

Anahtar | Açıklama
----|-------------
`LLM_BASE_URL` | OpenAI ile uyumlu sohbet API'si için temel URL. Varsayılan olarak `None`, bu OpenAI API'sini kullanır.
`LLM_MODEL` | OpenAI ile uyumlu sohbet API'si için kullanılacak model. Ayarlanmazsa (varsayılan), sohbet devre dışıdır. v3.6.0 itibarıyla, AI asistanı araç çağırma yetenekleri ile Pydantic AI kullanır.
`VECTOR_EMBEDDING_MODEL` | **Kullanım dışıdır**, 3.25'te kaldırılacaktır. Anlamsal arama vektör gömme işlemleri için kullanılacak model. Yerel bir model kullanıldığında, bu bir [Sentence Transformers](https://sbert.net/) model adı olmalıdır. Uzak bir API kullanıldığında (bkz. `VECTOR_EMBEDDING_BASE_URL`), bu uzak sağlayıcıya iletilen model adıdır. Ayarlanmazsa (varsayılan), anlamsal arama devre dışıdır. Gramps Web API 3.24'ten önce, sohbet de devre dışıydı.
`VECTOR_EMBEDDING_BASE_URL` | **Kullanım dışıdır**, 3.25'te kaldırılacaktır. Uzak OpenAI ile uyumlu gömme API'si için temel URL (örneğin, Ollama, OpenAI, LiteLLM). Ayarlanmazsa (varsayılan), yerel bir Sentence Transformers modeli kullanılır. Ayrıntılar için [Uzak bir gömme API'si kullanma](chat.md#using-a-remote-embedding-api) sayfasına bakın.
`VECTOR_EMBEDDING_API_KEY` | **Kullanım dışıdır**, 3.25'te kaldırılacaktır. Kimlik doğrulamalı uzak gömme sağlayıcıları için API anahtarı. Sadece `VECTOR_EMBEDDING_BASE_URL` ayarlandığında ve sağlayıcı kimlik doğrulaması gerektiriyorsa gereklidir.
`LLM_MAX_CONTEXT_LENGTH` | LLM'ye sağlanan aile ağacı bağlamı için karakter sınırı. Varsayılan olarak 50000'dir.
`LLM_SYSTEM_PROMPT` | LLM sohbet asistanı için özel sistem istemi (v3.6.0+). Ayarlanmazsa, varsayılan soydan optimize edilmiş istemi kullanır.


## Örnek yapılandırma dosyası

Üretim için minimal bir yapılandırma dosyası şu şekilde görünebilir:
```python
TREE="Ailem Ağacı"
BASE_URL="https://mytree.example.com"
SECRET_KEY="..."  # gizli anahtarınız
USER_DB_URI="sqlite:////path/to/users.sqlite"
EMAIL_HOST="mail.example.com"
EMAIL_PORT=465
EMAIL_USE_SSL=True  # 465 portu için örtük SSL kullanın
EMAIL_HOST_USER="gramps@example.com"
EMAIL_HOST_PASSWORD="..." # SMTP şifreniz
DEFAULT_FROM_EMAIL="gramps@example.com"
