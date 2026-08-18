# Sunucu Yapılandırması

Varsayılan Docker imajını kullanarak, gerekli tüm yapılandırmalar tarayıcıdan yapılabilir. Ancak, dağıtıma bağlı olarak sunucu yapılandırmasının özelleştirilmesi gerekebilir.

Bu sayfa, yapılandırmayı değiştirme yöntemlerini ve mevcut tüm yapılandırma seçeneklerini listeler.


## Yapılandırma dosyası vs. ortam değişkenleri

Ayarlar için ya bir yapılandırma dosyası ya da ortam değişkenleri kullanabilirsiniz.

[Eğer Docker Compose tabanlı bir kurulum](deployment.md) kullanıyorsanız, `grampsweb:` bloğundaki `volumes:` anahtarının altına aşağıdaki liste öğesini ekleyerek bir yapılandırma dosyası dahil edebilirsiniz:

```yaml
      - /path/to/config.cfg:/app/config/config.cfg
```
burada `/path/to/config.cfg`, sunucunuzun dosya sistemindeki yapılandırma dosyasının yoludur (sağ taraf, konteynerdeki yola atıfta bulunur ve değiştirilmemelidir).

Ortam değişkenleri kullanıldığında,

- her ayar adını `GRAMPSWEB_` ile ön ekleyin, böylece ortam değişkeninin adını elde edersiniz
- İç içe sözlük ayarları için çift alt çizgi kullanın, örneğin `GRAMPSWEB_THUMBNAIL_CACHE_CONFIG__CACHE_DEFAULT_TIMEOUT`, `THUMBNAIL_CACHE_CONFIG['CACHE_DEFAULT_TIMEOUT']` yapılandırma seçeneğinin değerini ayarlayacaktır

Ortam aracılığıyla ayarlanan yapılandırma seçeneklerinin, yapılandırma dosyasındakilerden önceliği olduğunu unutmayın. Her ikisi de mevcutsa, ortam değişkeni "kazanır".

!!! uyarı "Ön eklenmemiş ortam değişkenleri kullanılmaktan kaldırılmıştır"
    Tarihsel nedenlerden dolayı, bir avuç ayar – `TREE`, `SECRET_KEY`, `USER_DB_URI`, `POSTGRES_USER`, `POSTGRES_PASSWORD`, `MEDIA_BASE_DIR`, `SEARCH_INDEX_DIR`, `EMAIL_HOST`, `EMAIL_PORT`, `EMAIL_HOST_USER`, `EMAIL_HOST_PASSWORD`, `DEFAULT_FROM_EMAIL`, `BASE_URL`, ve `STATIC_PATH` – hala `GRAMPSWEB_` ön eki olmadan bir ortam değişkeni aracılığıyla ayarlanabilir. Bu kullanım dışıdır, başlangıçta bir uyarı kaydeder ve gelecekteki bir sürümde çalışmayı durduracaktır. Her zaman ön ekli biçimi kullanın, örneğin `TREE` yerine `GRAMPSWEB_TREE`.

    Bunun yalnızca ortam değişkenlerini ilgilendirdiğini unutmayın. Bir yapılandırma dosyasında, ayar adları her zaman ön ek olmadan kullanılır.

## Mevcut yapılandırma ayarları
Aşağıdaki yapılandırma seçenekleri mevcuttur.

### Gerekli ayarlar

Anahtar | Açıklama
----|-------------
`TREE` | Kullanılacak aile ağacı veritabanının adı. Mevcut ağaçları `gramps -l` ile gösterin. Bu isimde bir ağaç yoksa, yeni boş bir ağaç oluşturulacaktır.
`SECRET_KEY` | Flask için gizli anahtar. Gizli anahtar kamuya açık olarak paylaşılmamalıdır. Değiştirilmesi, tüm erişim jetonlarını geçersiz kılacaktır.
`USER_DB_URI` | Kullanıcı veritabanının veritabanı URL'si. SQLAlchemy ile uyumlu herhangi bir URL kabul edilir.

!!! bilgi
    Güvenli bir gizli anahtar oluşturmak için örneğin şu komutu kullanabilirsiniz:

    ```
    python3 -c "import secrets;print(secrets.token_urlsafe(32))"
    ```

### Opsiyonel ayarlar

Anahtar | Açıklama
----|-------------
`MEDIA_BASE_DIR` | Medya dosyaları için temel dizin olarak kullanılacak yol, Gramps'ta ayarlanan medya temel dizinini geçersiz kılar. [S3](s3.md) kullanırken, `s3://<bucket_name>` biçiminde olmalıdır.
`TREE_ID` | Tek ağaç modunda kullanılacak aile ağacı veritabanının dizin adı (eğer `TREE` `*` olarak ayarlanmamışsa). Ayarlandığında, sunucu ağacı, görüntüleme adı yerine dizin adıyla tanımlar, bu da yeniden adlandırmalara karşı daha dayanıklıdır. API aracılığıyla ağacı yeniden adlandırmak istiyorsanız gereklidir. Dizin adı `GET /api/trees/-` ile bulunabilir ( `id` alanı).
`SEARCH_INDEX_DB_URI` | Arama dizini için veritabanı URL'si. Yalnızca `sqlite` veya `postgresql` arka uçları kabul edilir. Varsayılan olarak `sqlite:///indexdir/search_index.db`'dir, bu da `indexdir` klasöründe bir SQLite dosyası oluşturur, scriptin çalıştığı yola göre.
`SEARCH_INDEX_DIR` | **Kullanımdan kaldırılmıştır** (bunun yerine `SEARCH_INDEX_DB_URI` kullanın). Arama dizinini içeren dizin. `SEARCH_INDEX_DB_URI` ayarlanmamışken ayarlanırsa, arama dizini URL'si `sqlite:///<SEARCH_INDEX_DIR>/search_index.db` olarak türetilir.
`STATIC_PATH` | Statik dosyaların sunulacağı yol (örneğin, statik bir web ön yüzü)
`BASE_URL` | API'nin ulaşılabileceği temel URL (örneğin, `https://mygramps.mydomain.com/`). Bu, doğru şifre sıfırlama bağlantıları oluşturmak için gereklidir.
`CORS_ORIGINS` | CORS isteklerinin izin verildiği kökenler. Varsayılan olarak, hepsi yasaklanmıştır. Herhangi bir alan adından istekleri izin vermek için `"*"` kullanın.
`EMAIL_HOST` | SMTP sunucu ana bilgisayarı (örneğin, şifre sıfırlama e-postalarını göndermek için)
`EMAIL_PORT` | SMTP sunucu portu. Varsayılan olarak 465'tir.
`EMAIL_HOST_USER` | SMTP sunucu kullanıcı adı
`EMAIL_HOST_PASSWORD` | SMTP sunucu şifresi
`EMAIL_USE_TLS` | **Kullanımdan kaldırılmıştır** (bunun yerine `EMAIL_USE_SSL` veya `EMAIL_USE_STARTTLS` kullanın). E-postaları göndermek için TLS kullanılıp kullanılmayacağını belirten boolean. Varsayılan olarak `True`'dur. STARTTLS kullanırken, bunu `False` olarak ayarlayın ve 25'ten farklı bir port kullanın.
`EMAIL_USE_SSL` | SMTP için örtük SSL/TLS kullanılıp kullanılmayacağını belirten boolean (v3.6.0+). `EMAIL_USE_TLS` açıkça ayarlanmamışsa varsayılan olarak `True`'dur. Genellikle 465 portu ile kullanılır.
`EMAIL_USE_STARTTLS` | SMTP için açık STARTTLS kullanılıp kullanılmayacağını belirten boolean (v3.6.0+). Varsayılan olarak `False`'dır. Genellikle 587 veya 25 portu ile kullanılır.
`DEFAULT_FROM_EMAIL` | Otomatik e-postalar için "From" adresi
`THUMBNAIL_CACHE_CONFIG` | Küçük resim önbelleği için ayarları içeren sözlük. Olası ayarlar için [Flask-Caching](https://flask-caching.readthedocs.io/en/latest/) sayfasına bakın.
`REQUEST_CACHE_CONFIG` | İstek önbelleği için ayarları içeren sözlük. Olası ayarlar için [Flask-Caching](https://flask-caching.readthedocs.io/en/latest/) sayfasına bakın.
`PERSISTENT_CACHE_CONFIG` | Kalıcı önbellek için ayarları içeren sözlük, örneğin telemetri için kullanılır. Olası ayarlar için [Flask-Caching](https://flask-caching.readthedocs.io/en/latest/) sayfasına bakın.
`CELERY_CONFIG` | Celery arka plan görev kuyruğu için ayarlar. Olası ayarlar için [Celery](https://docs.celeryq.dev/en/stable/userguide/configuration.html) sayfasına bakın.
`REPORT_DIR` | Gramps raporlarının çıktısının saklanacağı geçici dizin
`EXPORT_DIR` | Gramps veritabanasının dışa aktarımının çıktısının saklanacağı geçici dizin
`REGISTRATION_DISABLED` | Eğer `True` ise, yeni kullanıcı kaydını yasakla (varsayılan `False`)
`DISABLE_TELEMETRY` | Eğer `True` ise, istatistik telemetrisini devre dışı bırak (varsayılan `False`). Ayrıntılar için [telemetri](telemetry.md) sayfasına bakın.
`PILLOW_MAX_IMAGE_PIXELS` | İşlenen görüntünün içerebileceği maksimum piksel sayısını belirten PIL.Image.MAX_IMAGE_PIXELS parametresini ayarlar. Ayrıntılar için [belgelere](https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.MAX_IMAGE_PIXELS) bakın.
`MAX_THUMBNAIL_FILE_BYTES` | Küçük resimler için katı maksimum dosya boyutunu ayarlar. Varsayılan olarak `50 * 1024 * 1024` (50 MB) olarak ayarlanmıştır. Bunu artırmak, bellek kullanımını büyük ölçüde artırabilir ve büyük dosyaların bellekte açılması durumunda bellek yetersizliği çökmesine veya veri kaybına yol açabilir.


!!! bilgi
    Yapılandırma için ortam değişkenleri kullanıldığında, `EMAIL_USE_SSL` gibi boolean seçenekler ya `true` ya da `false` (büyük/küçük harfe duyarlıdır!) olmalıdır.


### Sadece PostgreSQL arka uç veritabanı için ayarlar

Eğer Gramps veritabanınızı [PostgreSQL eklentisi](https://gramps-project.org/wiki/index.php/Addon:PostgreSQL) ile çalışacak şekilde yapılandırdıysanız, bu gereklidir.

Anahtar | Açıklama
----|-------------
`POSTGRES_USER` | Veritabanı bağlantısı için kullanıcı adı
`POSTGRES_PASSWORD` | Veritabanı kullanıcısı için şifre


### Birden fazla ağaç barındırma ile ilgili ayarlar

[Ağaçları birden fazla barındırma](multi-tree.md) durumunda aşağıdaki ayarlar geçerlidir.


Anahtar | Açıklama
----|-------------
`MEDIA_PREFIX_TREE` | Her ağacın medya dosyaları için ayrı bir alt klasör kullanılıp kullanılmayacağını belirten boolean. Varsayılan olarak `False`'dur, ancak çoklu ağaç kurulumunda `True` kullanılması şiddetle önerilir.
`NEW_DB_BACKEND` | Yeni oluşturulan aile ağaçları için kullanılacak veritabanı arka ucu. `sqlite`, `postgresql` veya `sharedpostgresql`'dan biri olmalıdır. Varsayılan olarak `sqlite`'dır.
`POSTGRES_HOST` | Paylaşılan PostgreSQL arka ucu ile çoklu ağaç kurulumunda yeni ağaçlar oluşturmak için kullanılan PostgreSQL sunucusunun ana bilgisayar adı
`POSTGRES_PORT` | Paylaşılan PostgreSQL arka ucu ile çoklu ağaç kurulumunda yeni ağaçlar oluşturmak için kullanılan PostgreSQL sunucusunun portu


### OIDC kimlik doğrulama ayarları

Dış sağlayıcılarla OpenID Connect (OIDC) kimlik doğrulaması kullanmak istiyorsanız bu ayarlar gereklidir. Ayrıntılı kurulum talimatları ve örnekler için [OIDC Kimlik Doğrulaması](oidc.md) sayfasına bakın.

Anahtar | Açıklama
----|-------------
`OIDC_ENABLED` | OIDC kimlik doğrulamasını etkinleştirip etkinleştirmeyeceğini belirten boolean. Varsayılan olarak `False`'dır.
`OIDC_ISSUER` | OIDC sağlayıcı yayımlayıcı URL'si (özel OIDC sağlayıcıları için)
`OIDC_CLIENT_ID` | OAuth istemci kimliği (özel OIDC sağlayıcıları için)
`OIDC_CLIENT_SECRET` | OAuth istemci sırrı (özel OIDC sağlayıcıları için)
`OIDC_NAME` | Sağlayıcı için özel görüntüleme adı. Varsayılan olarak "OIDC"dır.
`OIDC_SCOPES` | OAuth kapsamları. Varsayılan olarak "openid email profile"dır.
`OIDC_USERNAME_CLAIM` | Kullanıcı adı için kullanılacak talep. Varsayılan olarak "preferred_username"dır.
`OIDC_OPENID_CONFIG_URL` | Opsiyonel: OpenID Connect yapılandırma uç noktasının URL'si (standart `/.well-known/openid-configuration` kullanılmıyorsa)
`OIDC_DISABLE_LOCAL_AUTH` | Yerel kullanıcı adı/şifre kimlik doğrulamasını devre dışı bırakıp bırakmayacağını belirten boolean. Varsayılan olarak `False`'dır.
`OIDC_AUTO_REDIRECT` | Yalnızca bir sağlayıcı yapılandırıldığında otomatik olarak OIDC'ye yönlendirilip yönlendirilmeyeceğini belirten boolean. Varsayılan olarak `False`'dır.

#### Yerleşik OIDC sağlayıcıları

Yerleşik sağlayıcılar (Google, Microsoft) için bu ayarları kullanın:

Anahtar | Açıklama
----|-------------
`OIDC_GOOGLE_CLIENT_ID` | Google OAuth için istemci kimliği
`OIDC_GOOGLE_CLIENT_SECRET` | Google OAuth için istemci sırrı
`OIDC_MICROSOFT_CLIENT_ID` | Microsoft OAuth için istemci kimliği
`OIDC_MICROSOFT_CLIENT_SECRET` | Microsoft OAuth için istemci sırrı

#### OIDC Rol Haritalama

Bu ayarlar, kimlik sağlayıcınızdan OIDC gruplarını/rollerini Gramps Web kullanıcı rollerine eşlemenizi sağlar:

Anahtar | Açıklama
----|-------------
`OIDC_ROLE_CLAIM` | Kullanıcının gruplarını/rollerini içeren OIDC jetonundaki talep adı. Varsayılan olarak "groups"dır.
`OIDC_GROUP_ADMIN` | Gramps "Admin" rolüne eşlenen OIDC sağlayıcınızdan grup/rol adı
`OIDC_GROUP_OWNER` | Gramps "Owner" rolüne eşlenen OIDC sağlayıcınızdan grup/rol adı
`OIDC_GROUP_EDITOR` | Gramps "Editor" rolüne eşlenen OIDC sağlayıcınızdan grup/rol adı
`OIDC_GROUP_CONTRIBUTOR` | Gramps "Contributor" rolüne eşlenen OIDC sağlayıcınızdan grup/rol adı
`OIDC_GROUP_MEMBER` | Gramps "Member" rolüne eşlenen OIDC sağlayıcınızdan grup/rol adı
`OIDC_GROUP_GUEST` | Gramps "Guest" rolüne eşlenen OIDC sağlayıcınızdan grup/rol adı

### Sadece AI özellikleri için ayarlar

Chat veya anlamsal arama gibi AI destekli özellikleri kullanmak istiyorsanız bu ayarlar gereklidir.

Anahtar | Açıklama
----|-------------
`LLM_BASE_URL` | OpenAI ile uyumlu chat API'si için temel URL. Varsayılan olarak `None`'dır, bu OpenAI API'sini kullanır.
`LLM_MODEL` | OpenAI ile uyumlu chat API'si için kullanılacak model. Ayarlanmadığında (varsayılan), chat devre dışıdır. v3.6.0 itibarıyla, AI asistanı araç çağırma yetenekleri ile Pydantic AI kullanır.
`VECTOR_EMBEDDING_MODEL` | Anlamsal arama vektör gömme işlemleri için kullanılacak model. Yerel bir model kullanıldığında, bu bir [Sentence Transformers](https://sbert.net/) model adı olmalıdır. Uzak bir API kullanıldığında (bkz. `VECTOR_EMBEDDING_BASE_URL`), bu uzak sağlayıcıya iletilen model adıdır. Ayarlanmadığında (varsayılan), anlamsal arama ve chat devre dışıdır.
`VECTOR_EMBEDDING_BASE_URL` | Uzak OpenAI ile uyumlu gömme API'si için temel URL (örneğin, Ollama, OpenAI, LiteLLM). Ayarlanmadığında (varsayılan), yerel bir Sentence Transformers modeli kullanılır. Ayrıntılar için [Uzak bir gömme API'si kullanma](chat.md#using-a-remote-embedding-api) sayfasına bakın.
`VECTOR_EMBEDDING_API_KEY` | Kimlik doğrulamalı uzak gömme sağlayıcıları için API anahtarı. Sadece `VECTOR_EMBEDDING_BASE_URL` ayarlandığında ve sağlayıcı kimlik doğrulaması gerektirdiğinde gereklidir.
`LLM_MAX_CONTEXT_LENGTH` | LLM'ye sağlanan aile ağacı bağlamı için karakter sınırı. Varsayılan olarak 50000'dir.
`LLM_SYSTEM_PROMPT` | LLM chat asistanı için özel sistem istemi (v3.6.0+). Ayarlanmadığında, varsayılan genetik optimize edilmiş istemi kullanır.


## Örnek yapılandırma dosyası

Üretim için minimal bir yapılandırma dosyası şu şekilde görünebilir:
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
