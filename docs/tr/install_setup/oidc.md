# OIDC Kimlik Doğrulama

Gramps Web, kullanıcıların harici kimlik sağlayıcıları kullanarak oturum açmalarına olanak tanıyan OpenID Connect (OIDC) kimlik doğrulamasını destekler. Bu, yerleşik sağlayıcılar olan Google ve Microsoft'un yanı sıra Keycloak, Authentik ve Authelia gibi özel OIDC sağlayıcılarını da içerir.

!!! warning "GitHub bir OIDC sağlayıcısı olarak artık desteklenmiyor"
    Eğer daha önceki bir versiyondan `OIDC_GITHUB_CLIENT_ID` / `OIDC_GITHUB_CLIENT_SECRET` ayarını yaptıysanız, bunları kaldırın – artık göz ardı ediliyor ve daha önce GitHub üzerinden oturum açan kullanıcılar bu şekilde oturum açamaz. GitHub bir OAuth 2.0 sağlayıcısıdır, OpenID Connect sağlayıcısı değildir ve Gramps Web'in kimlik için güvendiği talebi asla döndürmediği için tam olarak güvenilir olmamıştır.

## Genel Bakış

OIDC kimlik doğrulaması ile şunları yapabilirsiniz:

- Kullanıcı kimlik doğrulaması için harici kimlik sağlayıcıları kullanın
- Aynı anda birden fazla kimlik doğrulama sağlayıcısını destekleyin
- OIDC gruplarını/rollerini Gramps Web kullanıcı rollerine eşleyin
- Tek Oturum Açma (SSO) ve Tek Oturum Kapatma uygulayın
- İsteğe bağlı olarak yerel kullanıcı adı/parola kimlik doğrulamasını devre dışı bırakın

## Yapılandırma

OIDC kimlik doğrulamasını etkinleştirmek için Gramps Web yapılandırma dosyanızda veya ortam değişkenlerinde uygun ayarları yapılandırmanız gerekir. Mevcut OIDC ayarlarının tam listesi için [Sunucu Yapılandırması](configuration.md#settings-for-oidc-authentication) sayfasına bakın.

!!! info
    Ortam değişkenleri kullanırken, her ayar adını `GRAMPSWEB_` ile ön eklemeyi unutmayın (örneğin, `GRAMPSWEB_OIDC_ENABLED`). Ayrıntılar için [Yapılandırma dosyası vs. ortam değişkenleri](configuration.md#configuration-file-vs-environment-variables) sayfasına bakın.

### Yerleşik Sağlayıcılar

Gramps Web, popüler kimlik sağlayıcıları için yerleşik destek sunar. Bunları kullanmak için yalnızca istemci kimliğini ve istemci sırrını sağlamanız yeterlidir:

- **Google**: `OIDC_GOOGLE_CLIENT_ID` ve `OIDC_GOOGLE_CLIENT_SECRET`
- **Microsoft**: `OIDC_MICROSOFT_CLIENT_ID` ve `OIDC_MICROSOFT_CLIENT_SECRET`

Birden fazla sağlayıcıyı aynı anda yapılandırabilirsiniz. Sistem, yapılandırma değerlerine göre hangi sağlayıcıların mevcut olduğunu otomatik olarak algılayacaktır.

!!! tip "Microsoft: tek kiracı dağıtımları"
    Yerleşik Microsoft sağlayıcısı, çok kiracılı `/common` uç noktasını kullanır ve tasarımı gereği herhangi bir Microsoft hesabından oturum açmayı kabul eder. Sadece kendi kiracınızdaki kullanıcıların oturum açmasına izin vermek istiyorsanız, bunun yerine kiracıya özel verici URL'si ile [özel OIDC sağlayıcısını](#custom-oidc-providers) kullanın; bu, verici doğrulamasını aktif tutar ve oturum açmayı o kiracı ile kısıtlar.

### Özel OIDC Sağlayıcıları

Özel OIDC sağlayıcıları (Keycloak, Authentik, Authelia veya tek kiracı Microsoft Entra kiracısı gibi) için bu ayarları kullanın:

Anahtar | Açıklama
----|-------------
`OIDC_ENABLED` | OIDC kimlik doğrulamasını etkinleştirip etkinleştirmeyeceğinizi belirten Boolean. `True` olarak ayarlayın.
`OIDC_ISSUER` | Sağlayıcınızın verici URL'si. Keşif `<issuer>/.well-known/openid-configuration` adresinden alınır.
`OIDC_CLIENT_ID` | OIDC sağlayıcınız için istemci kimliği
`OIDC_CLIENT_SECRET` | OIDC sağlayıcınız için istemci sırrı
`OIDC_NAME` | Özel görüntü adı (isteğe bağlı, varsayılan "OIDC")
`OIDC_SCOPES` | OAuth kapsamları (isteğe bağlı, varsayılan "openid email profile")
`OIDC_USERNAME_CLAIM` | Kullanıcı adını oluşturmak için kullanılan talep (isteğe bağlı, varsayılan "preferred_username")

### Çok Ağaçlı Kurulumlar

Çok ağaçlı bir sunucuda, kullanıcının oturum açtığı ağacın, Gramps Web'in kimlik sağlayıcısına yönlendirmeden önce bilinmesi gerekir, bu nedenle oturum açma şu şekilde başlar:

```
GET /api/oidc/login/?provider=<id>&tree=<tree_id>
```

`tree`, çok ağaçlı kurulumlarda gereklidir; bunu atlamak veya mevcut olmayan bir ağacın kimliğini vermek, oturum açmayı başarısız kılar. Tek ağaçlı bir sunucuda `tree` isteğe bağlıdır, ancak verilirse yapılandırılmış `TREE` ile eşleşmelidir.

Bir OIDC kimliği tam olarak bir Gramps Web hesabına bağlıdır ve bu hesap da tam olarak bir ağaca aittir – farklı bir ağaçta oturum açmak, hesabı taşımak yerine başarısız olur. Sağlayıcıda tek bir kimliği birden fazla ağaçtaki hesaplarla ilişkilendirmenin bir yolu yoktur; birden fazla ağaca erişim ihtiyacı olan kullanıcıların sağlayıcıda ayrı kimliklere sahip olmaları gerekir (örneğin, farklı kullanıcı adları veya hesaplar).

!!! warning
    İlişkili bir ağaç olmayan bir site yöneticisi hesabı (bkz. [bir yönetici hesabı oluşturma](../administration/owner.md)) OIDC üzerinden oturum açamaz, çünkü OIDC oturumu her zaman bir ağaç gerektirir. Bu tür hesaplar, bunun yerine yerel kullanıcı adı/parola ile oluşturulmalı ve kimlik doğrulaması yapılmalıdır.

## Gerekli Yönlendirme URI'leri

OIDC sağlayıcınızı yapılandırırken, aşağıdaki yönlendirme URI'sini kaydetmelisiniz:

**Wildcard'ları destekleyen OIDC sağlayıcıları için: (örneğin, Authentik)**

- `https://your-gramps-backend.com/api/oidc/callback/*`

Burada `*` bir regex wildcard'dır. Sağlayıcınızın regex yorumlayıcısına bağlı olarak bu aynı zamanda `.*` veya benzeri de olabilir. Sağlayıcınız bunu gerektiriyorsa regex'in etkin olduğundan emin olun (örneğin, Authentik).

**Wildcard'ları desteklemeyen OIDC sağlayıcıları için: (örneğin, Authelia)**

- `https://your-gramps-backend.com/api/oidc/callback/custom`

Ağaç, yönlendirme URI'sinin bir parçası değildir, hatta çok ağaçlı sunucularda bile – oturum açma, yönlendirme URI'sinin kaydedilen ile tam olarak eşleşmesini gerektirdiğinden, ayrı olarak oturumda taşınır.

## Rol Eşleme

Gramps Web, kimlik sağlayıcınızdan OIDC gruplarını veya rollerini Gramps Web kullanıcı rollerine otomatik olarak eşleyebilir. Bu, kullanıcı izinlerini merkezi olarak kimlik sağlayıcınızda yönetmenizi sağlar. Rol eşleme, tüm sağlayıcılar için aynı şekilde çalışır, ister yerleşik ister özel olsun.

### Yapılandırma

Rol eşlemesini yapılandırmak için bu ayarları kullanın:

Anahtar | Açıklama
----|-------------
`OIDC_ROLE_CLAIM` | Kullanıcının gruplarını/rollerini içeren OIDC jetonundaki talep adı. Varsayılan "groups" olarak ayarlanmıştır. Noktalı yollar desteklenir, örneğin `realm_access.roles`.
`OIDC_GROUP_ADMIN` | Gramps "Admin" rolüne eşlenen OIDC sağlayıcınızdaki grup/rol adı
`OIDC_GROUP_OWNER` | Gramps "Owner" rolüne eşlenen OIDC sağlayıcınızdaki grup/rol adı
`OIDC_GROUP_EDITOR` | Gramps "Editor" rolüne eşlenen OIDC sağlayıcınızdaki grup/rol adı
`OIDC_GROUP_CONTRIBUTOR` | Gramps "Contributor" rolüne eşlenen OIDC sağlayıcınızdaki grup/rol adı
`OIDC_GROUP_MEMBER` | Gramps "Member" rolüne eşlenen OIDC sağlayıcınızdaki grup/rol adı
`OIDC_GROUP_GUEST` | Gramps "Guest" rolüne eşlenen OIDC sağlayıcınızdaki grup/rol adı

### Rol Eşleme Davranışı

Hiçbir `OIDC_GROUP_*` ayarı yapılandırılmadığında, rol eşleme kapalıdır ve roller Gramps Web'de manuel olarak yönetilir; yeni OIDC hesapları devre dışı olarak oluşturulur ve mevcut bir sahip veya yönetici tarafından onaylanması gerekir (aşağıdaki [İlk Oturum Açma ve Başlatma](#first-login-and-bootstrapping) bölümüne bakın).

Rol eşleme yapılandırıldıktan sonra, her oturum açmada:

- Eğer rol talebi mevcutsa ve kullanıcı eşlenmiş bir gruba ait ise, ilgili rolü alır.
- Eğer rol talebi mevcutsa ancak kullanıcı eşlenmiş bir gruba ait değilse, rolü devre dışı olarak ayarlanır. Bu, bir hata değil, kapalı bir varsayılandır – Gramps Web, tanımadığı bir grup için bir rol çıkaramaz.
- Eğer rol talebi tamamen jetondan yoksa, mevcut rol değişmeden kalır; yeni bir hesap yine de devre dışı olarak varsayılan ayara sahiptir.

!!! warning "Google bir gruplar talebi göndermez"
    Google'ın jetonları asla `groups` talebini içermez, bu nedenle rol eşleme etkinleştirildiğinde, Google oturum açmaları yukarıdaki "talep yok" durumuna girer: mevcut kullanıcılar rollerini korur, ancak yeni Google kullanıcıları devre dışı olarak oluşturulur ve manuel onay gerektirir. Başka bir sağlayıcı için rol eşlemeyi yalnızca etkinleştirmeden önce bunu aklınızda bulundurun – bu, mevcut Google kullanıcılarını devre dışı bırakmaz.

Microsoft Entra, uygulama rollerini ve grup üyeliklerini yalnızca ID jetonunda döndürür, kullanıcı bilgileri uç noktasından değil. Gramps Web, ID jetonunun taleplerini kullanıcı bilgisi yanıtına birleştirir, böylece `OIDC_ROLE_CLAIM` diğer sağlayıcılar için olduğu gibi çalışır; her iki yerde de bir talep varsa, kullanıcı bilgisi değeri önceliklidir.

## İlk Oturum Açma ve Başlatma

OIDC aracılığıyla oluşturulan yeni hesaplar, rol eşleme bir rol atamadıkça devre dışı olarak başlar (yukarıya bakın). Yepyeni bir örnekte kimse devre dışı bir hesabı onaylayamaz ve eğer `OIDC_DISABLE_LOCAL_AUTH` da etkinse, geri dönmek için bir parola oturumu da yoktur.

!!! warning "İlk oturum açmadan önce bir sahip/yönetici grubunu yapılandırın"
    Kimse OIDC üzerinden ilk kez oturum açmadan önce, `OIDC_GROUP_OWNER` (veya `OIDC_GROUP_ADMIN`) ayarını yapın ve ilk kullanıcının sağlayıcıda bu gruba ait olduğundan emin olun. Aksi takdirde, örnek OIDC üzerinden başlatılamaz.

## Hesaplar ve Kullanıcı Adları

OIDC aracılığıyla oluşturulan hesaplar, hesap oluşturma sırasında bir kez atanan ve sonraki oturum açmalarda asla değiştirilmeyen bir kullanıcı adı alır:

- Yerleşik sağlayıcılar: `<provider>_<claim value>`, örneğin `microsoft_alice@contoso.com`
- Özel sağlayıcı: sade talep değeri, örneğin `alice`

Çakışma durumunda sayısal bir ek eklenir. OIDC ile oluşturulan bir hesabın kullanıcı adını sonradan yeniden adlandırmanın bir yolu yoktur; aksine, tam ad ve e-posta adresi her oturum açmada yenilenir.

Bir OIDC oturumu, e-posta adresini paylaşan mevcut bir yerel hesaba asla eklenmez – bu kasıtlıdır, çünkü hesapları e-posta ile bağlamak bir hesap ele geçirme vektörüdür. Zaten bir yerel hesabı olan bir kullanıcı, OIDC üzerinden ilk kez oturum açtığında ikinci, ayrı bir hesap alır.

Sağlayıcıdan gelen e-posta adresleri yalnızca sağlayıcı bunları doğrulanmış olarak işaretlerse (veya `email_verified` talebini tamamen atlayarak) saklanır; aksi takdirde oturum açma, e-posta adresini saklamadan devam eder. E-posta adreslerinin benzersiz olması gerekmediğinden (Gramps Web API 3.22'den itibaren), başka bir hesap zaten kullanıyorsa bile bir adres saklanır.

## OIDC Çıkışı

Gramps Web, OIDC sağlayıcıları için Tek Oturum Kapatma (SSO çıkışı) desteği sunar. `GET /api/oidc/logout/` sağlayıcının `end_session_endpoint`'ini arar ve yanıt olarak `logout_url` olarak döndürür; oturumu gerçekten sonlandırmak için tarayıcıyı oraya yönlendiren Gramps Web ön yüzüdür. Sağlayıcının `end_session_endpoint`'i yoksa `logout_url` `null` olur.

!!! warning "Çıkışta jetonlar iptal edilmez"
    Çıkış yapmak yalnızca tarayıcı oturumunu sonlandırır; şu anda daha önce verilmiş bir Gramps Web jetonunu iptal etmenin bir yolu yoktur. Jetonlar, süresi dolana kadar geçerli kalır (`JWT_ACCESS_TOKEN_EXPIRES`, erişim jetonları için varsayılan 15 dakika), kullanıcı Gramps Web'de veya kimlik sağlayıcısında çıkış yapmış olsa bile.

## Örnek Yapılandırmalar

### Özel OIDC Sağlayıcı (Keycloak)

```python
TREE="Ailem Ağacı"
BASE_URL="https://mytree.example.com"
SECRET_KEY="..."  # gizli anahtarınız
USER_DB_URI="sqlite:////path/to/users.sqlite"

# Özel OIDC Yapılandırması
OIDC_ENABLED=True
OIDC_ISSUER="https://auth.example.com/realms/myrealm"
OIDC_CLIENT_ID="gramps-web"
OIDC_CLIENT_SECRET="your-client-secret"
OIDC_NAME="Aile SSO"
OIDC_SCOPES="openid email profile"
OIDC_AUTO_REDIRECT=True  # İsteğe bağlı: SSO oturum açma için otomatik yönlendirme
OIDC_DISABLE_LOCAL_AUTH=True  # İsteğe bağlı: kullanıcı adı/parola oturum açmayı devre dışı bırak

# İsteğe bağlı: OIDC gruplarından Gramps rollerine rol eşleme
OIDC_ROLE_CLAIM="groups"  # veya sağlayıcınıza bağlı olarak "roles"
OIDC_GROUP_ADMIN="gramps-admins"
OIDC_GROUP_EDITOR="gramps-editors"
OIDC_GROUP_MEMBER="gramps-members"

EMAIL_HOST="mail.example.com"
EMAIL_PORT=465
EMAIL_USE_SSL=True  # 465 numaralı port için örtük SSL kullan
EMAIL_HOST_USER="gramps@example.com"
EMAIL_HOST_PASSWORD="..." # SMTP parolanız
DEFAULT_FROM_EMAIL="gramps@example.com"
```

### Yerleşik Sağlayıcı (Google)

```python
TREE="Ailem Ağacı"
BASE_URL="https://mytree.example.com"
SECRET_KEY="..."  # gizli anahtarınız
USER_DB_URI="sqlite:////path/to/users.sqlite"

# Google OAuth
OIDC_GOOGLE_CLIENT_ID="your-google-client-id"
OIDC_GOOGLE_CLIENT_SECRET="your-google-client-secret"
```

### Birden Fazla Sağlayıcı

Birden fazla OIDC sağlayıcısını aynı anda etkinleştirebilirsiniz:

```python
TREE="Ailem Ağacı"
BASE_URL="https://mytree.example.com"
SECRET_KEY="..."  # gizli anahtarınız
USER_DB_URI="sqlite:////path/to/users.sqlite"

# Özel sağlayıcı
OIDC_ENABLED=True
OIDC_ISSUER="https://auth.example.com/realms/myrealm"
OIDC_CLIENT_ID="gramps-web"
OIDC_CLIENT_SECRET="your-client-secret"
OIDC_NAME="Şirket SSO"

# Google OAuth
OIDC_GOOGLE_CLIENT_ID="your-google-client-id"
OIDC_GOOGLE_CLIENT_SECRET="your-google-client-secret"

# Microsoft OAuth
OIDC_MICROSOFT_CLIENT_ID="your-microsoft-client-id"
OIDC_MICROSOFT_CLIENT_SECRET="your-microsoft-client-secret"
```

### Authelia

Gramps Web için topluluk tarafından yapılmış bir OIDC kurulum kılavuzu [resmi Authelia belgeleri web sitesinde](https://www.authelia.com/integration/openid-connect/clients/gramps/) mevcuttur.

### Keycloak

Keycloak için yapılandırmanın çoğu varsayılan olarak bırakılabilir (*Client → Create client → Client authentication ON*).
Birkaç istisna vardır:

1. **OpenID kapsamı** – `openid` kapsamı, tüm Keycloak sürümlerinde varsayılan olarak dahil edilmez. Sorun yaşamamak için bunu manuel olarak ekleyin: *Client → [Gramps client] → Client scopes → Add scope → Name: `openid` → Set as default.*
2. **Roller** – Roller, ya istemci düzeyinde ya da realm başına küresel olarak atanabilir.

    * İstemci rollerini kullanıyorsanız, `OIDC_ROLE_CLAIM` yapılandırma seçeneğini şu şekilde ayarlayın: `resource_access.[gramps-client-name].roles`
    * Roller Gramps'a görünür hale getirmek için *Client Scopes* bölümüne gidin (belirli istemci altında değil, üst düzey bölüm), ardından: *Roles → Mappers → client roles → Add to userinfo → ON.*
