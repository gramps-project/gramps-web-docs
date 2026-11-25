# Sunucu Yapılandırması

Varsayılan Docker görüntüsünü kullanarak gerekli tüm yapılandırmalar tarayıcı üzerinden yapılabilir. Ancak dağıtıma bağlı olarak sunucu yapılandırmasını özelleştirmeniz gerekebilir.

Bu sayfada yapılandırmayı değiştirmek için kullanılabilecek tüm yöntemler ve mevcut tüm yapılandırma seçenekleri listelenmektedir.


## Yapılandırma dosyası ve ortam değişkenleri

Ayarlar için bir yapılandırma dosyası veya ortam değişkenleri kullanabilirsiniz.

[Docker Compose tabanlı kurulumu](deployment.md) kullandığınızda, `grampsweb:` bloğundaki `volumes:` anahtarının altına aşağıdaki liste öğesini ekleyerek bir yapılandırma dosyası ekleyebilirsiniz:

```yaml
      - /path/to/config.cfg:/app/config/config.cfg
```
Burada `/path/to/config.cfg`, sunucunuzun dosya sistemindeki yapılandırma dosyasının yoludur (sağ taraf kapsayıcıdaki yolu ifade eder ve değiştirilmemelidir).

Ortam değişkenlerini kullanırken:

- ortam değişkeninin adını elde etmek için her ayar adının başına `GRAMPSWEB_` ekleyin
- İç içe sözlük ayarları için çift alt çizgi kullanın; örneğin `GRAMPSWEB_THUMBNAIL_CACHE_CONFIG__CACHE_DEFAULT_TIMEOUT`, `THUMBNAIL_CACHE_CONFIG['CACHE_DEFAULT_TIMEOUT']` yapılandırma seçeneğinin değerini ayarlar

Ortam üzerinden ayarlanan yapılandırma seçeneklerinin, yapılandırma dosyasındakilere göre öncelikli olduğunu unutmayın. Her ikisi de mevcutsa ortam değişkeni “kazanır”.

!!! warning "Öneksiz ortam değişkenleri kullanımdan kaldırılmıştır"
    Geçmiş nedenlerden dolayı bazı ayarlar – `TREE`, `SECRET_KEY`, `USER_DB_URI`, `POSTGRES_USER`, `POSTGRES_PASSWORD`, `MEDIA_BASE_DIR`, `SEARCH_INDEX_DIR`, `EMAIL_HOST`, `EMAIL_PORT`, `EMAIL_HOST_USER`, `EMAIL_HOST_PASSWORD`, `DEFAULT_FROM_EMAIL`, `BASE_URL` ve `STATIC_PATH` – hâlâ `GRAMPSWEB_` öneki olmadan bir ortam değişkeni üzerinden ayarlanabilir. Bu kullanım artık önerilmemektedir, başlangıçta bir uyarı günlüğe kaydedilir ve gelecekteki bir sürümde çalışmayı durduracaktır. Her zaman önekli biçimi kullanın; örneğin `TREE` yerine `GRAMPSWEB_TREE`.

    Bunun yalnızca ortam değişkenleriyle ilgili olduğunu unutmayın. Yapılandırma dosyasında ayar adları her zaman öneksiz olarak kullanılır.

!!! tip "Kullanımdan kaldırılmış seçenekleri denetleme"
    Sunucunuzun hâlâ dayandığı, öneksiz ortam değişkenleri, `SEARCH_INDEX_DIR` veya `EMAIL_USE_TLS` gibi kullanımdan kaldırılmış yapılandırma seçenekleri başlangıçta uyarı olarak günlüğe kaydedilir. Gramps Web API 3.22 sürümünden itibaren, yönetici olarak oturum açtığınızda bunlar, yerine geçen seçenek ve desteğin kaldırılacağı sürümle birlikte **Sistem Bilgileri** sayfasının üst kısmında da listelenir (üst uygulama çubuğundaki kullanıcı simgesi üzerinden erişilebilir).

    Eski sürümlerin ilk çalıştırma sihirbazının veritabanında depoladığı e-posta ayarları ve temel URL de burada listelenir. Bunları depolanan değerlerle eşleşecek şekilde yapılandırmanızda ayarlayın; eşleştiklerinde uyarı kaybolur.

## Mevcut yapılandırma ayarları
Aşağıdaki yapılandırma seçenekleri mevcuttur.

### Gerekli ayarlar

Anahtar | Açıklama
----|-------------
`TREE` | Kullanılacak aile ağacı veritabanının adı. Kullanılabilir ağaçları `gramps -l` ile gösterin. Bu ada sahip bir ağaç yoksa yeni ve boş bir ağaç oluşturulur.
`SECRET_KEY` | Flask için gizli anahtar. Gizli anahtar herkese açık olarak paylaşılmamalıdır. Bu anahtarın değiştirilmesi tüm erişim belirteçlerini geçersiz kılar.
`USER_DB_URI` | Kullanıcı veritabanının veritabanı URL'si. SQLAlchemy ile uyumlu tüm URL'lere izin verilir.

!!! info
    Örneğin aşağıdaki komutla güvenli bir gizli anahtar oluşturabilirsiniz:

    ```
    python3 -c "import secrets;print(secrets.token_urlsafe(32))"
    ```

### İsteğe bağlı ayarlar

Anahtar | Açıklama
----|-------------
`MEDIA_BASE_DIR` | Gramps'te ayarlanan medya temel dizinini geçersiz kılarak medya dosyaları için temel dizin olarak kullanılacak yol. [S3](s3.md) kullanılırken `s3://<bucket_name>` biçiminde olmalıdır.
`TREE_ID` | Tek ağaç modunda (`TREE` değeri `*` olarak ayarlanmadığında) kullanılacak aile ağacı veritabanının dizin adı. Ayarlandığında sunucu, ağacı görünen adı yerine dizin adıyla tanımlar; bu, yeniden adlandırmalara karşı daha dayanıklıdır. Ağacı API üzerinden yeniden adlandırmak istiyorsanız gereklidir. Dizin adı `GET /api/trees/-` üzerinden (`id` alanı) bulunabilir.
`SEARCH_INDEX_DB_URI` | Arama dizininin veritabanı URL'si. Arka uç olarak yalnızca `sqlite` veya `postgresql` kullanılabilir. Varsayılan değer `sqlite:///indexdir/search_index.db`'dir; bu değer, betiğin çalıştırıldığı yola göre `indexdir` klasöründe bir SQLite dosyası oluşturur.
`SEARCH_INDEX_DIR` | **Kullanımdan kaldırılmıştır** (bunun yerine `SEARCH_INDEX_DB_URI` kullanın). Arama dizinini içeren dizin. `SEARCH_INDEX_DB_URI` ayarlanmamışken ayarlanırsa arama dizini URL'si `sqlite:///<SEARCH_INDEX_DIR>/search_index.db` olarak türetilir.
`STATIC_PATH` | Statik dosyaların sunulacağı yol (ör. statik bir web ön yüzü)
`BASE_URL` | API'ye ulaşılabilecek temel URL (ör. `https://mygramps.mydomain.com/`). Örneğin doğru parola sıfırlama bağlantıları oluşturmak için gereklidir. Web Push ayrıca herkese açık şekilde erişilebilen bir HTTPS URL'si gerektirir; varsayılan `http://localhost/` değeri Web Push'ı devre dışı bırakır. Bu ayarı ortam üzerinden yapılandırırken `GRAMPSWEB_BASE_URL` kullanın.
`CORS_ORIGINS` | CORS isteklerine izin verilen kaynaklar. Varsayılan olarak hiçbir kaynağa izin verilmez. Herhangi bir etki alanından gelen isteklere izin vermek için `"*"` kullanın.
`EMAIL_HOST` | SMTP sunucusunun ana bilgisayar adı (ör. parola sıfırlama e-postaları göndermek için)
`EMAIL_PORT` | SMTP sunucusunun bağlantı noktası. Varsayılan değer 465'tir.
`EMAIL_HOST_USER` | SMTP sunucusu kullanıcı adı
`EMAIL_HOST_PASSWORD` | SMTP sunucusu parolası
`EMAIL_USE_TLS` | **Kullanımdan kaldırılmıştır** (bunun yerine `EMAIL_USE_SSL` veya `EMAIL_USE_STARTTLS` kullanın). E-posta gönderirken TLS kullanılıp kullanılmayacağını belirten Boolean değer. Varsayılan değer `True`'dur. STARTTLS kullanırken bunu `False` olarak ayarlayın ve 25'ten farklı bir bağlantı noktası kullanın.
`EMAIL_USE_SSL` | SMTP için örtük SSL/TLS kullanılıp kullanılmayacağını belirten Boolean değer (v3.6.0+). `EMAIL_USE_TLS` açıkça ayarlanmadıysa varsayılan değer `True`'dur. Genellikle 465 numaralı bağlantı noktasıyla kullanılır.
`EMAIL_USE_STARTTLS` | SMTP için açık STARTTLS kullanılıp kullanılmayacağını belirten Boolean değer (v3.6.0+). Varsayılan değer `False`'tur. Genellikle 587 veya 25 numaralı bağlantı noktasıyla kullanılır.
`DEFAULT_FROM_EMAIL` | Otomatik e-postalar için “From” adresi
`THUMBNAIL_CACHE_CONFIG` | Küçük resim önbelleğinin ayarlarını içeren sözlük. Olası ayarlar için [Flask-Caching](https://flask-caching.readthedocs.io/en/latest/) sayfasına bakın.
`REQUEST_CACHE_CONFIG` | İstek önbelleğinin ayarlarını içeren sözlük. Olası ayarlar için [Flask-Caching](https://flask-caching.readthedocs.io/en/latest/) sayfasına bakın.
`PERSISTENT_CACHE_CONFIG` | Örneğin telemetri için kullanılan kalıcı önbelleğin ayarlarını içeren sözlük. Olası ayarlar için [Flask-Caching](https://flask-caching.readthedocs.io/en/latest/) sayfasına bakın.
`CELERY_CONFIG` | Celery arka plan görev kuyruğunun ayarları. Olası ayarlar için [Celery](https://docs.celeryq.dev/en/stable/userguide/configuration.html) sayfasına bakın.
`REPORT_DIR` | Çalıştırılan Gramps raporlarının çıktısının depolanacağı geçici dizin
`EXPORT_DIR` | Gramps veritabanının dışa aktarılmasının çıktısının depolanacağı geçici dizin
`BACKUP_DIR` | [Yedeklerin](../administration/backups.md) ağaç başına bir alt dizinde depolandığı dizin (v3.24.0+). Ayarlanmadığında (varsayılan), yedekler sunucuda depolanamaz; ancak yüklenen bir dosyadan geri yüklenebilir. Kalıcı bir konum, örneğin bir Docker birimi kullanın ve tercihen bu konumun kendisinin de yedeklenmesini veya başka bir konumla eşzamanlanmasını sağlayın.
`BACKUP_KEEP` | Ağaç başına saklanacak yedek sayısı; yeni bir yedek oluşturulduğunda daha eski yedekler silinir (v3.24.0+). Varsayılan değer `5`'tir.
`RATE_LIMIT_BACKUP` | Ağaç başına yedek oluşturma hız sınırı (v3.24.0+). Varsayılan değer `"10 per day"`'dir.
`RATE_LIMIT_MEDIA_ARCHIVE` | Dışa Aktarma sayfasında medya arşivleri oluşturma hız sınırı. Varsayılan değer `"1 per hour"`'dır.
`REGISTRATION_DISABLED` | `True` ise yeni kullanıcı kaydına izin verilmez (varsayılan `False`). Gramps Web API 3.26 sürümünden itibaren oturum açma sayfası kayıt bağlantısını da gizler.
`PROXY_FIX_X_FOR` | Gramps Web'in önündeki güvenilen ters proxy sayısı (v3.26.0+). Tek bir ters proxy arkasında, hız sınırlarının tüm kullanıcılara birlikte değil istemci başına uygulanması için `1` olarak ayarlayın. Varsayılan değer `0`'dır. Yalnızca sunucuya sadece bu proxy'ler üzerinden erişilebiliyorsa ayarlayın.
`DISABLE_TELEMETRY` | `True` ise istatistik telemetrisi devre dışı bırakılır (varsayılan `False`). Ayrıntılar için [telemetri](telemetry.md) sayfasına bakın.
`PILLOW_MAX_IMAGE_PIXELS` | İşlenen görüntünün içerebileceği piksel sayısını belirten `PIL.Image.MAX_IMAGE_PIXELS` parametresini ayarlar. Ayrıntılar için [belgelere](https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.MAX_IMAGE_PIXELS) bakın.
`MAX_THUMBNAIL_FILE_BYTES` | Küçük resimler için kesin bir maksimum dosya boyutu belirler. Varsayılan değer `50 * 1024 * 1024` (50 MB)'tır. Bu değeri artırmak bellek kullanımını büyük ölçüde artırabilir ve büyük dosyaların bellekte sıkıştırmasının açılması durumunda bellek yetersizliği çökmelerine veya veri kaybına yol açabilir.


!!! info
    Yapılandırma için ortam değişkenlerini kullanırken `EMAIL_USE_SSL` gibi Boolean seçenekler, `true` veya `false` dizesi olmalıdır (büyük/küçük harfe duyarlıdır!).


### PostgreSQL veritabanları için ayarlar

Aile ağaçlarınız [SharedPostgreSQL eklentisi](postgres.md) kullanılarak bir [PostgreSQL veritabanında](postgres.md) barındırılıyorsa bu ayarlar gereklidir.

Anahtar | Açıklama
----|-------------
`POSTGRES_USER` | Veritabanı bağlantısı için kullanıcı adı
`POSTGRES_PASSWORD` | Veritabanı kullanıcısının parolası


### Birden fazla ağacı barındırmayla ilgili ayarlar

Aşağıdaki ayarlar [birden fazla ağaç barındırdığınızda](multi-tree.md) geçerlidir.


Anahtar | Açıklama
----|-------------
`MEDIA_PREFIX_TREE` | Her ağacın medya dosyaları için ayrı bir alt klasör kullanılıp kullanılmayacağını belirten Boolean değer. Varsayılan değer `False`'tur; ancak çok ağaçlı bir kurulumda `True` kullanmanız önemle önerilir.
`NEW_DB_BACKEND` | Yeni oluşturulan aile ağaçları için kullanılacak veritabanı arka ucu. `sqlite` veya `sharedpostgresql` değerlerinden biri olmalıdır. Varsayılan değer `sqlite`'tır. PostgreSQL arka ucu Gramps Web API 4.0 sürümünde kaldırılacağından `postgresql` değeri hâlâ kabul edilse de kullanımdan kaldırılmıştır.
`POSTGRES_HOST` | SharedPostgreSQL arka ucuyla çok ağaçlı bir kurulum kullanılırken yeni ağaçlar oluşturmak için kullanılan PostgreSQL sunucusunun ana bilgisayar adı
`POSTGRES_PORT` | SharedPostgreSQL arka ucuyla çok ağaçlı bir kurulum kullanılırken yeni ağaçlar oluşturmak için kullanılan PostgreSQL sunucusunun bağlantı noktası


### OIDC kimlik doğrulaması için ayarlar

Harici sağlayıcılarla OpenID Connect (OIDC) kimlik doğrulamasını kullanmak istiyorsanız bu ayarlar gereklidir. Ayrıntılı kurulum yönergeleri ve örnekler için [OIDC Kimlik Doğrulaması](oidc.md) sayfasına bakın.

Anahtar | Açıklama
----|-------------
`OIDC_ENABLED` | OIDC kimlik doğrulamasının etkinleştirilip etkinleştirilmeyeceğini belirten Boolean değer. Varsayılan değer `False`'tur.
`OIDC_ISSUER` | OIDC sağlayıcısının veren URL'si (özel OIDC sağlayıcıları için)
`OIDC_CLIENT_ID` | OAuth istemci kimliği (özel OIDC sağlayıcıları için)
`OIDC_CLIENT_SECRET` | OAuth istemci gizli anahtarı (özel OIDC sağlayıcıları için)
`OIDC_NAME` | Sağlayıcı için özel görünen ad. Varsayılan değer `"OIDC"`'dir.
`OIDC_SCOPES` | OAuth kapsamları. Varsayılan değer `"openid email profile"`'dır.
`OIDC_USERNAME_CLAIM` | Kullanıcı adı için kullanılacak talep. Varsayılan değer `"preferred_username"`'dir.
`OIDC_OPENID_CONFIG_URL` | İsteğe bağlı: OpenID Connect yapılandırma uç noktasının URL'si (standart `/.well-known/openid-configuration` kullanılmıyorsa)
`OIDC_PKCE` | PKCE kullanılıp kullanılmayacağını belirten Boolean değer. Ayarlanmazsa sağlayıcının keşif belgesinde `S256` listeleniyorsa PKCE kullanılır. Bkz. [PKCE](oidc.md#pkce)
`OIDC_DISABLE_LOCAL_AUTH` | Yerel kullanıcı adı/parola kimlik doğrulamasının devre dışı bırakılıp bırakılmayacağını belirten Boolean değer. Varsayılan değer `False`'tur.
`OIDC_AUTO_REDIRECT` | Yalnızca bir sağlayıcı yapılandırılmışsa OIDC'ye otomatik olarak yönlendirme yapılıp yapılmayacağını belirten Boolean değer. Varsayılan değer `False`'tur.
`OIDC_ALLOWED_REDIRECT_URIS` | Yerel uygulamaların oturum açma sonucunu alabileceği `https` URI'lerinin listesi (v3.26.0+); ortam değişkeninde JSON listesi olarak ayarlanır. Varsayılan olarak boştur. Yalnızca yerel bir uygulamanın belgelerinde isteniyorsa gereklidir. Bkz. [Yerel uygulamalar](oidc.md#native-apps)

#### Yerleşik OIDC sağlayıcıları

Yerleşik sağlayıcılar (Google, Microsoft) için şu ayarları kullanın:

Anahtar | Açıklama
----|-------------
`OIDC_GOOGLE_CLIENT_ID` | Google OAuth istemci kimliği
`OIDC_GOOGLE_CLIENT_SECRET` | Google OAuth istemci gizli anahtarı
`OIDC_MICROSOFT_CLIENT_ID` | Microsoft OAuth istemci kimliği
`OIDC_MICROSOFT_CLIENT_SECRET` | Microsoft OAuth istemci gizli anahtarı
`OIDC_GOOGLE_PKCE` | Google için Boolean PKCE ayarı; bkz. [PKCE](oidc.md#pkce)
`OIDC_MICROSOFT_PKCE` | Microsoft için Boolean PKCE ayarı; bkz. [PKCE](oidc.md#pkce)

#### OIDC Rol Eşleme

Bu ayarlar, kimlik sağlayıcınızdaki OIDC gruplarını/rollerini Gramps Web kullanıcı rollerine eşlemenize olanak tanır:

Anahtar | Açıklama
----|-------------
`OIDC_ROLE_CLAIM` | Kullanıcının gruplarını/rollerini içeren OIDC belirtecindeki talep adı. Varsayılan değer `"groups"`'tur.
`OIDC_GROUP_ADMIN` | OIDC sağlayıcınızdaki Gramps “Admin” rolüne eşlenen grup/rol adı
`OIDC_GROUP_OWNER` | OIDC sağlayıcınızdaki Gramps “Owner” rolüne eşlenen grup/rol adı
`OIDC_GROUP_EDITOR` | OIDC sağlayıcınızdaki Gramps “Editor” rolüne eşlenen grup/rol adı
`OIDC_GROUP_CONTRIBUTOR` | OIDC sağlayıcınızdaki Gramps “Contributor” rolüne eşlenen grup/rol adı
`OIDC_GROUP_MEMBER` | OIDC sağlayıcınızdaki Gramps “Member” rolüne eşlenen grup/rol adı
`OIDC_GROUP_GUEST` | OIDC sağlayıcınızdaki Gramps “Guest” rolüne eşlenen grup/rol adı

### Yalnızca yapay zekâ özellikleri için ayarlar

Yapay zekâ sohbetini kullanmak istiyorsanız bu ayarlar gereklidir. Ayrıntılar için [Yapay zekâ sohbetini ayarlama](chat.md) sayfasına bakın.

!!! note
    Anlamsal arama için kullanılan `VECTOR_EMBEDDING_MODEL`, `VECTOR_EMBEDDING_BASE_URL` ve `VECTOR_EMBEDDING_API_KEY` ayarları, anlamsal aramayı kaldıran Gramps Web API 3.25 sürümünden beri yok sayılmaktadır. Yapay zekâ sohbeti için yalnızca `LLM_MODEL` gereklidir.

Anahtar | Açıklama
----|-------------
`LLM_BASE_URL` | OpenAI uyumlu sohbet API'si için temel URL. Varsayılan değer, OpenAI API'sini kullanan `None`'dır.
`LLM_MODEL` | OpenAI uyumlu sohbet API'si için kullanılacak model. Ayarlanmazsa (varsayılan), sohbet devre dışı bırakılır. v3.6.0 sürümünden itibaren yapay zekâ asistanı, araç çağırma özelliklerine sahip Pydantic AI kullanır.
`LLM_MAX_OUTPUT_TOKENS` | Modelin tek bir yanıtta oluşturabileceği maksimum belirteç sayısı. Varsayılan olarak ayarlanmaz; sınır model sunucusuna bırakılır. Kendi sınırı olmayan model sunucuları için kullanışlıdır; aksi hâlde bir yanıt süresiz olarak devam edebilir.
`LLM_MAX_CONTEXT_LENGTH` | LLM'ye sağlanan aile ağacı bağlamı için karakter sınırı. Varsayılan değer 50000'dir.
`LLM_SYSTEM_PROMPT` | LLM sohbet asistanı için özel sistem istemi (v3.6.0+). Ayarlanmazsa varsayılan, soybilim için optimize edilmiş istem kullanılır.
`LLM_VISION` | Kullanıcıların sorularına görüntü ekleyip ekleyemeyeceğini belirten Boolean değer (v3.26.0+). Yalnızca model görüntüleri kabul ediyorsa etkinleştirin. Varsayılan değer `False`'tur. Bkz. [Sorulardaki görüntüler](chat.md#images-in-questions)
`LLM_ALLOW_WRITE_PROPOSALS` | Asistanın, kullanıcıların inceleyip uygulayabilmesi için ağaçta değişiklik önerip öneremeyeceğini belirten Boolean değer (v3.26.0+). Varsayılan değer `False`'tur. Bkz. [Asistanın değişiklik önermesine izin verme](chat.md#letting-the-assistant-propose-changes)


## Örnek yapılandırma dosyası

Üretim ortamı için minimal bir yapılandırma dosyası aşağıdakine benzeyebilir:
```python
TREE="My Family Tree"
BASE_URL="https://mytree.example.com"
SECRET_KEY="..."  # your secret key
USER_DB_URI="sqlite:////path/to/users.sqlite"
EMAIL_HOST="mail.example.com"
EMAIL_PORT=465
EMAIL_USE_SSL=True  # Use implicit SSL for port 465
EMAIL_HOST_USER="gramps@example.com"
EMAIL_HOST_PASSWORD="..." # your SMTP password
DEFAULT_FROM_EMAIL="gramps@example.com"
```
