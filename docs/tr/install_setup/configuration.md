# Sunucu Yapılandırması

Varsayılan Docker görüntüsünü kullanarak, gerekli tüm yapılandırmalar tarayıcıdan yapılabilir. Ancak, dağıtıma bağlı olarak, sunucu yapılandırmasını özelleştirmek gerekebilir.

Bu sayfa, yapılandırmayı değiştirmek için tüm yöntemleri ve mevcut tüm yapılandırma seçeneklerini listeler.

## Yapılandırma dosyası vs. ortam değişkenleri

Ayarlar için ya bir yapılandırma dosyası ya da ortam değişkenleri kullanabilirsiniz.

[Docker Compose tabanlı kurulum](deployment.md) kullanıyorsanız, `grampsweb:` bloğundaki `volumes:` anahtarının altına aşağıdaki liste öğesini ekleyerek bir yapılandırma dosyası dahil edebilirsiniz:

```yaml
      - /path/to/config.cfg:/app/config/config.cfg
```
burada `/path/to/config.cfg`, sunucunuzun dosya sistemindeki yapılandırma dosyasının yoludur (sağ taraftaki kısım, konteynerdeki yolu ifade eder ve değiştirilmemelidir).

Ortam değişkenleri kullanırken,

- her ayar adını `GRAMPSWEB_` ile önekiyle başlatın, böylece ortam değişkeninin adını elde edersiniz
- İç içe sözlük ayarları için çift alt çizgi kullanın, örneğin `GRAMPSWEB_THUMBNAIL_CACHE_CONFIG__CACHE_DEFAULT_TIMEOUT`, `THUMBNAIL_CACHE_CONFIG['CACHE_DEFAULT_TIMEOUT']` yapılandırma seçeneğinin değerini ayarlayacaktır

Ortam üzerinden ayarlanan yapılandırma seçeneklerinin, yapılandırma dosyasındaki seçeneklere göre önceliği olduğunu unutmayın. Her ikisi de mevcutsa, ortam değişkeni "kazanır".

## Mevcut yapılandırma ayarları
Aşağıdaki yapılandırma seçenekleri mevcuttur.

### Gerekli ayarlar

Anahtar | Açıklama
----|-------------
`TREE` | Kullanılacak aile ağacı veritabanının adı. Mevcut ağaçları `gramps -l` ile gösterin. Bu isimde bir ağaç yoksa, yeni boş bir ağaç oluşturulacaktır.
`SECRET_KEY` | Flask için gizli anahtar. Gizli anahtar kamuya açık olarak paylaşılmamalıdır. Değiştirilmesi, tüm erişim belirteçlerini geçersiz kılacaktır.
`USER_DB_URI` | Kullanıcı veritabanının veritabanı URL'si. SQLAlchemy ile uyumlu herhangi bir URL kabul edilir.

!!! info
    Güvenli bir gizli anahtar oluşturmak için örneğin şu komutu kullanabilirsiniz:

    ```
    python3 -c "import secrets;print(secrets.token_urlsafe(32))"
    ```

### İsteğe bağlı ayarlar

Anahtar | Açıklama
----|-------------
`MEDIA_BASE_DIR` | Medya dosyaları için temel dizin olarak kullanılacak yol, Gramps'ta ayarlanan medya temel dizinini geçersiz kılar. [S3](s3.md) kullanırken, `s3://<bucket_name>` biçiminde olmalıdır.
`SEARCH_INDEX_DB_URI` | Arama dizini için veritabanı URL'si. Yalnızca `sqlite` veya `postgresql` arka uçları kabul edilir. Varsayılan olarak `sqlite:///indexdir/search_index.db` olup, scriptin çalıştırıldığı yola göre `indexdir` klasöründe bir SQLite dosyası oluşturur.
`STATIC_PATH` | Statik dosyaların sunulacağı yol (örneğin, statik bir web ön yüzü)
`BASE_URL` | API'nin erişilebileceği temel URL (örneğin, `https://mygramps.mydomain.com/`). Bu, doğru şifre sıfırlama bağlantıları oluşturmak için gereklidir.
`CORS_ORIGINS` | CORS isteklerinin izin verildiği kökenler. Varsayılan olarak, tümü yasaktır. Herhangi bir alan adından istekleri izin vermek için `"*"` kullanın.
`EMAIL_HOST` | SMTP sunucu ana bilgisayarı (örneğin, şifre sıfırlama e-postalarını göndermek için)
`EMAIL_PORT` | SMTP sunucu portu. varsayılan 465
`EMAIL_HOST_USER` | SMTP sunucu kullanıcı adı
`EMAIL_HOST_PASSWORD` | SMTP sunucu şifresi
`EMAIL_USE_TLS` | E-postaları göndermek için TLS kullanılıp kullanılmayacağı. Varsayılan `True`. STARTTLS kullanıyorsanız, bunu `False` olarak ayarlayın ve 25'ten farklı bir port kullanın.
`DEFAULT_FROM_EMAIL` | Otomatik e-postalar için "From" adresi
`THUMBNAIL_CACHE_CONFIG` | Küçük resim önbelleği için ayarları içeren sözlük. Olası ayarlar için [Flask-Caching](https://flask-caching.readthedocs.io/en/latest/) sayfasına bakın.
`REQUEST_CACHE_CONFIG` | İstek önbelleği için ayarları içeren sözlük. Olası ayarlar için [Flask-Caching](https://flask-caching.readthedocs.io/en/latest/) sayfasına bakın.
`PERSISTENT_CACHE_CONFIG` | Sürekli önbellek için ayarları içeren sözlük, örneğin telemetri için kullanılır. Olası ayarlar için [Flask-Caching](https://flask-caching.readthedocs.io/en/latest/) sayfasına bakın.
`CELERY_CONFIG` | Celery arka plan görev kuyruğu için ayarlar. Olası ayarlar için [Celery](https://docs.celeryq.dev/en/stable/userguide/configuration.html) sayfasına bakın.
`REPORT_DIR` | Gramps raporlarının çıktısının saklanacağı geçici dizin
`EXPORT_DIR` | Gramps veritabanasının dışa aktarımının çıktısının saklanacağı geçici dizin
`REGISTRATION_DISABLED` | Eğer `True` ise, yeni kullanıcı kaydını engelle (varsayılan `False`)
`DISABLE_TELEMETRY` | Eğer `True` ise, istatistik telemetrisini devre dışı bırak (varsayılan `False`). Ayrıntılar için [telemetri](telemetry.md) sayfasına bakın.

!!! info
    Yapılandırma için ortam değişkenleri kullanırken, `EMAIL_USE_TLS` gibi boolean seçenekler ya `true` ya da `false` (büyük/küçük harf duyarlı!) olmalıdır.

### Sadece PostgreSQL arka uç veritabanı için ayarlar

Bu, Gramps veritabanınızı [PostgreSQL eklentisi](https://gramps-project.org/wiki/index.php/Addon:PostgreSQL) ile çalışacak şekilde yapılandırdıysanız gereklidir.

Anahtar | Açıklama
----|-------------
`POSTGRES_USER` | Veritabanı bağlantısı için kullanıcı adı
`POSTGRES_PASSWORD` | Veritabanı kullanıcısı için şifre

### Birden fazla ağaç barındırma ile ilgili ayarlar

[Ağaçları barındırırken](multi-tree.md) aşağıdaki ayarlar geçerlidir.

Anahtar | Açıklama
----|-------------
`MEDIA_PREFIX_TREE` | Her ağaç için medya dosyaları için ayrı bir alt klasör kullanılıp kullanılmayacağı. Varsayılan `False`, ancak çoklu ağaç kurulumunda `True` kullanılması şiddetle tavsiye edilir.
`NEW_DB_BACKEND` | Yeni oluşturulan aile ağaçları için kullanılacak veritabanı arka ucu. `sqlite`, `postgresql` veya `sharedpostgresql`'dan biri olmalıdır. Varsayılan `sqlite`.
`POSTGRES_HOST` | Paylaşılan PostgreSQL arka ucu ile çoklu ağaç kurulumunda yeni ağaçlar oluşturmak için kullanılan PostgreSQL sunucusunun ana bilgisayarı
`POSTGRES_PORT` | Paylaşılan PostgreSQL arka ucu ile çoklu ağaç kurulumunda yeni ağaçlar oluşturmak için kullanılan PostgreSQL sunucusunun portu

### OIDC kimlik doğrulaması için ayarlar

Bu ayarlar, harici sağlayıcılarla OpenID Connect (OIDC) kimlik doğrulaması kullanmak istiyorsanız gereklidir. Ayrıntılı kurulum talimatları ve örnekler için [OIDC Kimlik Doğrulaması](oidc.md) sayfasına bakın.

Anahtar | Açıklama
----|-------------
`OIDC_ENABLED` | OIDC kimlik doğrulamasını etkinleştirip etkinleştirmeyeceği. Varsayılan `False`.
`OIDC_ISSUER` | OIDC sağlayıcı yayımlayıcı URL'si (özel OIDC sağlayıcıları için)
`OIDC_CLIENT_ID` | OAuth istemci kimliği (özel OIDC sağlayıcıları için)
`OIDC_CLIENT_SECRET` | OAuth istemci gizli anahtarı (özel OIDC sağlayıcıları için)
`OIDC_NAME` | Sağlayıcı için özel görüntüleme adı. Varsayılan "OIDC"
`OIDC_SCOPES` | OAuth kapsamları. Varsayılan "openid email profile"
`OIDC_USERNAME_CLAIM` | Kullanıcı adı için kullanılacak iddia. Varsayılan "preferred_username"
`OIDC_OPENID_CONFIG_URL` | İsteğe bağlı: OpenID Connect yapılandırma uç noktasının URL'si (standart `/.well-known/openid-configuration` kullanılmıyorsa)
`OIDC_DISABLE_LOCAL_AUTH` | Yerel kullanıcı adı/şifre kimlik doğrulamasını devre dışı bırakıp bırakmayacağı. Varsayılan `False`
`OIDC_AUTO_REDIRECT` | Sadece bir sağlayıcı yapılandırıldığında otomatik olarak OIDC'ye yönlendirilip yönlendirilmeyeceği. Varsayılan `False`

#### Yerleşik OIDC sağlayıcıları

Yerleşik sağlayıcılar (Google, Microsoft, GitHub) için bu ayarları kullanın:

Anahtar | Açıklama
----|-------------
`OIDC_GOOGLE_CLIENT_ID` | Google OAuth için istemci kimliği
`OIDC_GOOGLE_CLIENT_SECRET` | Google OAuth için istemci gizli anahtarı
`OIDC_MICROSOFT_CLIENT_ID` | Microsoft OAuth için istemci kimliği
`OIDC_MICROSOFT_CLIENT_SECRET` | Microsoft OAuth için istemci gizli anahtarı
`OIDC_GITHUB_CLIENT_ID` | GitHub OAuth için istemci kimliği
`OIDC_GITHUB_CLIENT_SECRET` | GitHub OAuth için istemci gizli anahtarı

#### OIDC Rol Eşlemesi

Bu ayarlar, kimlik sağlayıcınızdan OIDC gruplarını/rollerini Gramps Web kullanıcı rolleriyle eşlemenizi sağlar:

Anahtar | Açıklama
----|-------------
`OIDC_ROLE_CLAIM` | Kullanıcının gruplarını/rollerini içeren OIDC belirteçindeki iddia adı. Varsayılan "groups"
`OIDC_GROUP_ADMIN` | Gramps "Yönetici" rolüne eşlenen OIDC sağlayıcınızdan grup/rol adı
`OIDC_GROUP_OWNER` | Gramps "Sahip" rolüne eşlenen OIDC sağlayıcınızdan grup/rol adı
`OIDC_GROUP_EDITOR` | Gramps "Editör" rolüne eşlenen OIDC sağlayıcınızdan grup/rol adı
`OIDC_GROUP_CONTRIBUTOR` | Gramps "Katkıda Bulunan" rolüne eşlenen OIDC sağlayıcınızdan grup/rol adı
`OIDC_GROUP_MEMBER` | Gramps "Üye" rolüne eşlenen OIDC sağlayıcınızdan grup/rol adı
`OIDC_GROUP_GUEST` | Gramps "Misafir" rolüne eşlenen OIDC sağlayıcınızdan grup/rol adı

### Sadece AI özellikleri için ayarlar

Bu ayarlar, sohbet veya anlamsal arama gibi AI destekli özellikleri kullanmak istiyorsanız gereklidir.

Anahtar | Açıklama
----|-------------
`LLM_BASE_URL` | OpenAI uyumlu sohbet API'si için temel URL. Varsayılan `None`, bu OpenAI API'sini kullanır.
`LLM_MODEL` | OpenAI uyumlu sohbet API'si için kullanılacak model. Ayarlanmadıysa (varsayılan), sohbet devre dışıdır.
`VECTOR_EMBEDDING_MODEL` | Anlamsal arama vektör gömme işlemleri için kullanılacak [Sentence Transformers](https://sbert.net/) modeli. Ayarlanmadıysa (varsayılan), anlamsal arama ve sohbet devre dışıdır.
`LLM_MAX_CONTEXT_LENGTH` | LLM'ye sağlanan aile ağacı bağlamı için karakter sınırı. Varsayılan 50000.

## Örnek yapılandırma dosyası

Üretim için minimal bir yapılandırma dosyası şu şekilde görünebilir:
```python
TREE="Ailem Ağacı"
BASE_URL="https://mytree.example.com"
SECRET_KEY="..."  # gizli anahtarınız
USER_DB_URI="sqlite:////path/to/users.sqlite"
EMAIL_HOST="mail.example.com"
EMAIL_PORT=465
EMAIL_USE_TLS=True
EMAIL_HOST_USER="gramps@example.com"
EMAIL_HOST_PASSWORD="..." # SMTP şifreniz
DEFAULT_FROM_EMAIL="gramps@example.com"
