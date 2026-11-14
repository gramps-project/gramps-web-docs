# Sunucu Yapılandırması

Varsayılan Docker görüntüsünü kullanarak, gerekli tüm yapılandırmalar tarayıcıdan yapılabilir. Ancak, dağıtıma bağlı olarak sunucu yapılandırmasını özelleştirmek gerekebilir.

Bu sayfa, yapılandırmayı değiştirmek için tüm yöntemleri ve mevcut tüm yapılandırma seçeneklerini listeler.


## Yapılandırma dosyası vs. ortam değişkenleri

Ayarlar için ya bir yapılandırma dosyası ya da ortam değişkenleri kullanabilirsiniz.

[Docker Compose tabanlı kurulum](deployment.md) kullanıyorsanız, `grampsweb:` bloğundaki `volumes:` anahtarının altına aşağıdaki liste öğesini ekleyerek bir yapılandırma dosyası dahil edebilirsiniz:

```yaml
      - /path/to/config.cfg:/app/config/config.cfg
```
burada `/path/to/config.cfg`, sunucunuzun dosya sistemindeki yapılandırma dosyasının yoludur (sağ taraf, konteynerdeki yolu ifade eder ve değiştirilmemelidir).

Ortam değişkenleri kullanırken,

- her ayar adını `GRAMPSWEB_` ile öne ekleyerek ortam değişkeninin adını elde edin
- İç içe sözlük ayarları için çift alt çizgi kullanın, örneğin `GRAMPSWEB_THUMBNAIL_CACHE_CONFIG__CACHE_DEFAULT_TIMEOUT`, `THUMBNAIL_CACHE_CONFIG['CACHE_DEFAULT_TIMEOUT']` yapılandırma seçeneğinin değerini ayarlayacaktır.

Ortam üzerinden ayarlanan yapılandırma seçeneklerinin, yapılandırma dosyasındaki seçeneklerden önceliği olduğunu unutmayın. Her ikisi de mevcutsa, ortam değişkeni "kazanır".

!!! uyarı "Öne eklenmemiş ortam değişkenleri kullanımdan kaldırılmıştır"
    Tarihsel nedenlerden ötürü, bir avuç ayar – `TREE`, `SECRET_KEY`, `USER_DB_URI`, `POSTGRES_USER`, `POSTGRES_PASSWORD`, `MEDIA_BASE_DIR`, `SEARCH_INDEX_DIR`, `EMAIL_HOST`, `EMAIL_PORT`, `EMAIL_HOST_USER`, `EMAIL_HOST_PASSWORD`, `DEFAULT_FROM_EMAIL`, `BASE_URL` ve `STATIC_PATH` – hala `GRAMPSWEB_` öne eki olmadan bir ortam değişkeni aracılığıyla ayarlanabilir. Bu kullanımdan kaldırılmıştır, başlangıçta bir uyarı kaydeder ve gelecekteki bir sürümde çalışmayı durduracaktır. Her zaman öne ekli biçimi kullanın, örneğin `GRAMPSWEB_TREE` yerine `TREE`.

    Bunun yalnızca ortam değişkenlerini ilgilendirdiğini unutmayın. Bir yapılandırma dosyasında, ayar adları her zaman öne ek olmadan kullanılır.

!!! ipucu "Kullanımdan kaldırılmış seçenekleri kontrol etme"
    Sunucunuzun hala bağımlı olduğu kullanımdan kaldırılmış yapılandırma seçenekleri – öne eklenmemiş ortam değişkenleri, `SEARCH_INDEX_DIR` veya `EMAIL_USE_TLS` gibi – başlangıçta uyarı olarak kaydedilir. Gramps Web API 3.22'den itibaren, bunlar ayrıca, yerel yönetici olarak oturum açtığınızda **Sistem Bilgileri** sayfasının en üstünde, değiştirilmesi gereken değerleri ve desteklerin kaldırılacağı sürümü ile birlikte listelenir.

    Eski sürümlerin ilk çalıştırma sihirbazının veritabanında sakladığı e-posta ayarları ve temel URL de burada listelenir. Bunları yapılandırmanızda saklanan değerlere ayarlayın; eşleştiğinde uyarı kaybolur.

## Mevcut yapılandırma ayarları
Aşağıdaki yapılandırma seçenekleri mevcuttur.

### Gerekli ayarlar

Anahtar | Açıklama
----|-------------
`TREE` | Kullanılacak aile ağacı veritabanının adı. Mevcut ağaçları `gramps -l` ile gösterin. Bu isimde bir ağaç yoksa, yeni boş bir tane oluşturulacaktır.
`SECRET_KEY` | Flask için gizli anahtar. Gizli anahtar kamuya açık olarak paylaşılmamalıdır. Değiştirilmesi, tüm erişim belirteçlerini geçersiz kılacaktır.
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
`TREE_ID` | Tek ağaç modunda (yani `TREE` `*` olarak ayarlanmadığında) kullanılacak aile ağacı veritabanının dizin adı. Ayarlandığında, sunucu ağacı dizin adıyla tanımlar, bu da yeniden adlandırmalara karşı daha sağlamdır. API aracılığıyla ağacı yeniden adlandırmak istiyorsanız gereklidir. Dizin adı `GET /api/trees/-` (id alanı) ile bulunabilir.
`SEARCH_INDEX_DB_URI` | Arama dizini için veritabanı URL'si. Yalnızca `sqlite` veya `postgresql` arka uçları kabul edilir. Varsayılan olarak `sqlite:///indexdir/search_index.db`'dir; bu, scriptin çalıştığı yola göre `indexdir` klasöründe bir SQLite dosyası oluşturur.
`SEARCH_INDEX_DIR` | **Kullanımdan kaldırılmıştır** (bunun yerine `SEARCH_INDEX_DB_URI` kullanın). Arama dizinini içeren dizin. `SEARCH_INDEX_DB_URI` ayarlanmadan ayarlanırsa, arama dizini URL'si `sqlite:///<SEARCH_INDEX_DIR>/search_index.db` olarak türetilir.
`STATIC_PATH` | Statik dosyaların sunulacağı yol (örneğin, statik bir web ön yüzü)
`BASE_URL` | API'nin ulaşılabileceği temel URL (örneğin, `https://mygramps.mydomain.com/`). Bu, doğru şifre sıfırlama bağlantıları oluşturmak için gereklidir. Web Push ayrıca kamuya açık bir HTTPS URL'si gerektirir; varsayılan `http://localhost/` Web Push'ı devre dışı bırakır. Bu ayarı ortam aracılığıyla yapılandırırken, `GRAMPSWEB_BASE_URL` kullanın.
`CORS_ORIGINS` | CORS isteklerinin izin verildiği kökenler. Varsayılan olarak, tümü yasaktır. Herhangi bir alan adından istekleri izin vermek için `"*"` kullanın.
`EMAIL_HOST` | SMTP sunucu ana bilgisayarı (örneğin, şifre sıfırlama e-postalarını göndermek için)
`EMAIL_PORT` | SMTP sunucu bağlantı noktası. Varsayılan olarak 465
`EMAIL_HOST_USER` | SMTP sunucu kullanıcı adı
`EMAIL_HOST_PASSWORD` | SMTP sunucu parolası
`EMAIL_USE_TLS` | **Kullanımdan kaldırılmıştır** (bunun yerine `EMAIL_USE_SSL` veya `EMAIL_USE_STARTTLS` kullanın). E-postaları göndermek için TLS kullanılıp kullanılmayacağını belirten boolean. Varsayılan olarak `True`'dur. STARTTLS kullanırken, bunu `False` olarak ayarlayın ve 25'ten farklı bir bağlantı noktası kullanın.
`EMAIL_USE_SSL` | SMTP için örtük SSL/TLS kullanılıp kullanılmayacağını belirten boolean (v3.6.0+). `EMAIL_USE_TLS` açıkça ayarlanmamışsa varsayılan olarak `True`'dur. Genellikle 465 numaralı bağlantı noktası ile kullanılır.
`EMAIL_USE_STARTTLS` | SMTP için açık STARTTLS kullanılıp kullanılmayacağını belirten boolean (v3.6.0+). Varsayılan olarak `False`'dır. Genellikle 587 veya 25 numaralı bağlantı noktası ile kullanılır.
`DEFAULT_FROM_EMAIL` | Otomatik e-postalar için "Gönderen" adresi
`THUMBNAIL_CACHE_CONFIG` | Küçük resim önbelleği için ayarları içeren sözlük. Olası ayarlar için [Flask-Caching](https://flask-caching.readthedocs.io/en/latest/) sayfasına bakın.
`REQUEST_CACHE_CONFIG` | İstek önbelleği için ayarları içeren sözlük. Olası ayarlar için [Flask-Caching](https://flask-caching.readthedocs.io/en/latest/) sayfasına bakın.
`PERSISTENT_CACHE_CONFIG` | Sürekli önbellek için ayarları içeren sözlük, örneğin telemetri için kullanılır. Olası ayarlar için [Flask-Caching](https://flask-caching.readthedocs.io/en/latest/) sayfasına bakın.
`CELERY_CONFIG` | Celery arka plan görev kuyruğu için ayarlar. Olası ayarlar için [Celery](https://docs.celeryq.dev/en/stable/userguide/configuration.html) sayfasına bakın.
`REPORT_DIR` | Gramps raporlarının çıktısının saklanacağı geçici dizin
`EXPORT_DIR` | Gramps veritabanasının dışa aktarım çıktısının saklanacağı geçici dizin
`BACKUP_DIR` | [yedeklerin](../administration/backups.md) saklandığı dizin, her ağaç için bir alt dizinde (v3.24.0+). Ayarlanmadığında (varsayılan), yedekler sunucuda saklanamaz, ancak yüklenen bir dosyadan geri yüklenebilir. Kalıcı bir konum kullanın, örneğin bir Docker hacmi ve tercihen kendisi de yedeklenen veya başka bir yerde senkronize edilen bir konum.
`BACKUP_KEEP` | Her ağaç için saklanan yedek sayısı; yeni bir yedek oluşturulduğunda daha eski olanlar silinir (v3.24.0+). Varsayılan olarak `5`'tir.
`RATE_LIMIT_BACKUP` | Yedek oluşturma için oran sınırlaması, ağaç başına (v3.24.0+). Varsayılan olarak `"günde 10"`'dur.
`RATE_LIMIT_MEDIA_ARCHIVE` | Dışa Aktarma sayfasında medya arşivleri oluşturma için oran sınırlaması. Varsayılan olarak `"saate 1"`'dir.
`REGISTRATION_DISABLED` | Eğer `True` ise, yeni kullanıcı kaydını engelle (varsayılan `False`).
`DISABLE_TELEMETRY` | Eğer `True` ise, istatistik telemetrisini devre dışı bırak (varsayılan `False`). Ayrıntılar için [telemetri](telemetry.md) sayfasına bakın.
`PILLOW_MAX_IMAGE_PIXELS` | İşlenen görüntünün içerebileceği piksel sayısını belirten PIL.Image.MAX_IMAGE_PIXELS parametresini ayarlar. Ayrıntılar için [belgelere](https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.MAX_IMAGE_PIXELS) bakın.
`MAX_THUMBNAIL_FILE_BYTES` | Küçük resimler için zorunlu maksimum dosya boyutunu ayarlar. Varsayılan olarak `50 * 1024 * 1024` (50 MB) olarak ayarlanmıştır. Bunu artırmak, bellek kullanımını büyük ölçüde artırabilir ve büyük dosyaların bellekte açılması durumunda bellek yetersizliği hatalarına veya veri kaybına yol açabilir.


!!! bilgi
    Yapılandırma için ortam değişkenleri kullanırken, `EMAIL_USE_SSL` gibi boolean seçenekler ya `true` ya da `false` (büyük/küçük harf duyarlı!) olmalıdır.


### PostgreSQL veritabanları için ayarlar

Bu ayarlar, aile ağaçlarınızın [PostgreSQL veritabanında](postgres.md) SharedPostgreSQL eklentisi kullanılarak barındırılması durumunda gereklidir.

Anahtar | Açıklama
----|-------------
`POSTGRES_USER` | Veritabanı bağlantısı için kullanıcı adı
`POSTGRES_PASSWORD` | Veritabanı kullanıcısı için parola


### Birden fazla ağaç barındırmak için ilgili ayarlar

Aşağıdaki ayarlar, [birden fazla ağaç barındırırken](multi-tree.md) geçerlidir.

Anahtar | Açıklama
----|-------------
`MEDIA_PREFIX_TREE` | Her ağacın medya dosyaları için ayrı bir alt klasör kullanılıp kullanılmayacağını belirten boolean. Varsayılan olarak `False`'dur, ancak çoklu ağaç kurulumunda `True` kullanılması şiddetle tavsiye edilir.
`NEW_DB_BACKEND` | Yeni oluşturulan aile ağaçları için kullanılacak veritabanı arka ucu. `sqlite` veya `sharedpostgresql`'dan biri olmalıdır. Varsayılan olarak `sqlite`'dır. `postgresql` değeri hala kabul edilmektedir ancak kullanımdan kaldırılmıştır, çünkü PostgreSQL arka ucu Gramps Web API 4.0'da kaldırılacaktır.
`POSTGRES_HOST` | SharedPostgreSQL arka ucu ile çoklu ağaç kurulumu kullanırken yeni ağaçlar oluşturmak için kullanılan PostgreSQL sunucusunun ana bilgisayar adı
`POSTGRES_PORT` | SharedPostgreSQL arka ucu ile çoklu ağaç kurulumu kullanırken yeni ağaçlar oluşturmak için kullanılan PostgreSQL sunucusunun bağlantı noktası


### OIDC kimlik doğrulaması için ayarlar

Bu ayarlar, harici sağlayıcılarla OpenID Connect (OIDC) kimlik doğrulaması kullanmak istiyorsanız gereklidir. Ayrıntılı kurulum talimatları ve örnekler için [OIDC Kimlik Doğrulaması](oidc.md) sayfasına bakın.

Anahtar | Açıklama
----|-------------
`OIDC_ENABLED` | OIDC kimlik doğrulamasını etkinleştirip etkinleştirmeyeceğini belirten boolean. Varsayılan olarak `False`'dır.
`OIDC_ISSUER` | OIDC sağlayıcı yayımlayıcı URL'si (özel OIDC sağlayıcıları için)
`OIDC_CLIENT_ID` | OAuth istemci kimliği (özel OIDC sağlayıcıları için)
`OIDC_CLIENT_SECRET` | OAuth istemci sırrı (özel OIDC sağlayıcıları için)
`OIDC_NAME` | Sağlayıcı için özel görüntüleme adı. Varsayılan olarak "OIDC"dır.
`OIDC_SCOPES` | OAuth kapsamları. Varsayılan olarak "openid email profile"dır.
`OIDC_USERNAME_CLAIM` | Kullanıcı adı için kullanılacak talep. Varsayılan olarak "preferred_username"dır.
`OIDC_OPENID_CONFIG_URL` | Opsiyonel: OpenID Connect yapılandırma uç noktasına URL (standart `/.well-known/openid-configuration` kullanılmıyorsa)
`OIDC_PKCE` | PKCE kullanılıp kullanılmayacağını belirten boolean. Ayarlanmadığında, sağlayıcının keşif belgesi `S256` listelendiğinde PKCE kullanılır. [PKCE](oidc.md#pkce) sayfasına bakın.
`OIDC_DISABLE_LOCAL_AUTH` | Yerel kullanıcı adı/parola kimlik doğrulamasını devre dışı bırakıp bırakmayacağını belirten boolean. Varsayılan olarak `False`'dır.
`OIDC_AUTO_REDIRECT` | Sadece bir sağlayıcı yapılandırıldığında otomatik olarak OIDC'ye yönlendirilip yönlendirilmeyeceğini belirten boolean. Varsayılan olarak `False`'dır.

#### Yerleşik OIDC sağlayıcıları

Yerleşik sağlayıcılar (Google, Microsoft) için bu ayarları kullanın:

Anahtar | Açıklama
----|-------------
`OIDC_GOOGLE_CLIENT_ID` | Google OAuth için istemci kimliği
`OIDC_GOOGLE_CLIENT_SECRET` | Google OAuth için istemci sırrı
`OIDC_MICROSOFT_CLIENT_ID` | Microsoft OAuth için istemci kimliği
`OIDC_MICROSOFT_CLIENT_SECRET` | Microsoft OAuth için istemci sırrı
`OIDC_GOOGLE_PKCE` | Google için PKCE ayarı, [PKCE](oidc.md#pkce) sayfasına bakın.
`OIDC_MICROSOFT_PKCE` | Microsoft için PKCE ayarı, [PKCE](oidc.md#pkce) sayfasına bakın.

#### OIDC Rol Eşlemesi

Bu ayarlar, kimlik sağlayıcınızdan OIDC gruplarını/rollerini Gramps Web kullanıcı rolleriyle eşleştirmenizi sağlar:

Anahtar | Açıklama
----|-------------
`OIDC_ROLE_CLAIM` | Kullanıcının gruplarını/rollerini içeren OIDC belirteçindeki talep adı. Varsayılan olarak "groups"dır.
`OIDC_GROUP_ADMIN` | Gramps "Yönetici" rolüne eşlenen OIDC sağlayıcınızdan grup/rol adı
`OIDC_GROUP_OWNER` | Gramps "Sahip" rolüne eşlenen OIDC sağlayıcınızdan grup/rol adı
`OIDC_GROUP_EDITOR` | Gramps "Editör" rolüne eşlenen OIDC sağlayıcınızdan grup/rol adı
`OIDC_GROUP_CONTRIBUTOR` | Gramps "Katkıda Bulunan" rolüne eşlenen OIDC sağlayıcınızdan grup/rol adı
`OIDC_GROUP_MEMBER` | Gramps "Üye" rolüne eşlenen OIDC sağlayıcınızdan grup/rol adı
`OIDC_GROUP_GUEST` | Gramps "Misafir" rolüne eşlenen OIDC sağlayıcınızdan grup/rol adı

### Sadece AI özellikleri için ayarlar

AI sohbeti kullanmak istiyorsanız bu ayarlar gereklidir. Ayrıntılar için [AI sohbetini ayarlama](chat.md) sayfasına bakın.

!!! not
    `VECTOR_EMBEDDING_MODEL`, `VECTOR_EMBEDDING_BASE_URL` ve `VECTOR_EMBEDDING_API_KEY` ayarları Gramps Web API 3.25'ten itibaren göz ardı edilmektedir; bu sürümde anlamsal arama kaldırılmıştır. AI sohbeti yalnızca `LLM_MODEL`'a ihtiyaç duyar.

Anahtar | Açıklama
----|-------------
`LLM_BASE_URL` | OpenAI uyumlu sohbet API'si için temel URL. Varsayılan olarak `None`'dır, bu da OpenAI API'sini kullanır.
`LLM_MODEL` | OpenAI uyumlu sohbet API'si için kullanılacak model. Ayarlanmadığında (varsayılan), sohbet devre dışıdır. v3.6.0 itibarıyla, AI asistanı, araç çağırma yeteneklerine sahip Pydantic AI kullanmaktadır.
`LLM_MAX_OUTPUT_TOKENS` | Modelin tek bir yanıt içinde üretebileceği maksimum token sayısı. Varsayılan olarak ayarlanmamış, bu da sınırı model sunucusuna bırakır. Kendi sınırı olmayan model sunucuları için yararlıdır; aksi takdirde bir yanıt sonsuza kadar devam edebilir.
`LLM_MAX_CONTEXT_LENGTH` | LLM'ye sağlanan aile ağacı bağlamı için karakter sınırı. Varsayılan olarak 50000'dir.
`LLM_SYSTEM_PROMPT` | LLM sohbet asistanı için özel sistem istemi (v3.6.0+). Ayarlanmadığında, varsayılan soybilim odaklı istemi kullanır.


## Örnek yapılandırma dosyası

Üretim için minimal bir yapılandırma dosyası şu şekilde görünebilir:
```python
TREE="Ailem Ağacı"
BASE_URL="https://mytree.example.com"
SECRET_KEY="..."  # gizli anahtarınız
USER_DB_URI="sqlite:////path/to/users.sqlite"
EMAIL_HOST="mail.example.com"
EMAIL_PORT=465
EMAIL_USE_SSL=True  # 465 numaralı bağlantı noktası için örtük SSL kullanın
EMAIL_HOST_USER="gramps@example.com"
EMAIL_HOST_PASSWORD="..." # SMTP parolanız
DEFAULT_FROM_EMAIL="gramps@example.com"
