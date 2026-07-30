# OIDC Kimlik Doğrulama

Gramps Web, kullanıcıların harici kimlik sağlayıcılarını kullanarak giriş yapmalarına olanak tanıyan OpenID Connect (OIDC) kimlik doğrulamasını destekler. Bu, yerleşik sağlayıcılar olan Google ve Microsoft'un yanı sıra Keycloak, Authentik ve Authelia gibi özel OIDC sağlayıcılarını da içerir.

!!! warning "GitHub bir OIDC sağlayıcısı olarak artık desteklenmiyor"
    Eğer daha önceki bir sürümden `OIDC_GITHUB_CLIENT_ID` / `OIDC_GITHUB_CLIENT_SECRET` ayarlarını yaptıysanız, bunları kaldırın – artık göz ardı ediliyor ve daha önce GitHub üzerinden giriş yapan kullanıcılar bu şekilde giriş yapamaz. GitHub bir OAuth 2.0 sağlayıcısıdır, OpenID Connect sağlayıcısı değildir ve Gramps Web'in kimlik için güvendiği talebi asla döndürmedi, bu nedenle tam olarak güvenilir olmamıştır.

## Genel Bakış

OIDC kimlik doğrulaması, şunları yapmanıza olanak tanır:

- Kullanıcı kimlik doğrulaması için harici kimlik sağlayıcıları kullanma
- Aynı anda birden fazla kimlik doğrulama sağlayıcısını destekleme
- OIDC gruplarını/rollerini Gramps Web kullanıcı rollerine eşleme
- Tek Oturum Açma (SSO) ve Tek Oturum Kapatma uygulama
- İsteğe bağlı olarak yerel kullanıcı adı/şifre kimlik doğrulamasını devre dışı bırakma

## Yapılandırma

OIDC kimlik doğrulamasını etkinleştirmek için Gramps Web yapılandırma dosyanızda veya ortam değişkenlerinde uygun ayarları yapılandırmanız gerekir. Mevcut OIDC ayarlarının tam listesini görmek için [Sunucu Yapılandırması](configuration.md#settings-for-oidc-authentication) sayfasına bakın.

!!! info
    Ortam değişkenlerini kullanırken, her ayar adını `GRAMPSWEB_` ile ön eklemeyi unutmayın (örneğin, `GRAMPSWEB_OIDC_ENABLED`). Ayrıntılar için [Yapılandırma dosyası vs. ortam değişkenleri](configuration.md#configuration-file-vs-environment-variables) sayfasına bakın.

### Yerleşik Sağlayıcılar

Gramps Web, popüler kimlik sağlayıcıları için yerleşik destek sunar. Bunları kullanmak için yalnızca istemci kimliğini ve istemci sırrını sağlamanız gerekir:

- **Google**: `OIDC_GOOGLE_CLIENT_ID` ve `OIDC_GOOGLE_CLIENT_SECRET`
- **Microsoft**: `OIDC_MICROSOFT_CLIENT_ID` ve `OIDC_MICROSOFT_CLIENT_SECRET`

Birden fazla sağlayıcıyı aynı anda yapılandırabilirsiniz. Sistem, yapılandırma değerlerine dayanarak hangi sağlayıcıların mevcut olduğunu otomatik olarak algılar.

!!! tip "Microsoft: tek kiracı dağıtımları"
    Yerleşik Microsoft sağlayıcısı, tasarım gereği çok kiracılı `/common` uç noktasını kullanır ve herhangi bir Microsoft hesabından girişleri kabul eder. Sadece kendi kiracınızdaki kullanıcıların giriş yapmasına izin vermek istiyorsanız, bunun yerine kiracınıza özgü sağlayıcı URL'si ile [özel OIDC sağlayıcısını](#custom-oidc-providers) kullanın; bu, sağlayıcı doğrulamasını aktif tutar ve girişleri o kiracıyla sınırlar.

### Özel OIDC Sağlayıcıları

Özel OIDC sağlayıcıları (Keycloak, Authentik, Authelia veya tek kiracı Microsoft Entra kiracısı gibi) için bu ayarları kullanın:

Anahtar | Açıklama
----|-------------
`OIDC_ENABLED` | OIDC kimlik doğrulamasını etkinleştirip etkinleştirmeyeceğini belirten Boolean. `True` olarak ayarlayın.
`OIDC_ISSUER` | Sağlayıcınızın verici URL'si. Keşif `<issuer>/.well-known/openid-configuration` adresinden alınır.
`OIDC_CLIENT_ID` | OIDC sağlayıcınız için istemci kimliği
`OIDC_CLIENT_SECRET` | OIDC sağlayıcınız için istemci sırrı
`OIDC_NAME` | Özel görüntü adı (isteğe bağlı, varsayılan "OIDC")
`OIDC_SCOPES` | OAuth kapsamları (isteğe bağlı, varsayılan "openid email profile")
`OIDC_USERNAME_CLAIM` | Kullanıcı adını oluşturmak için kullanılan talep (isteğe bağlı, varsayılan "preferred_username")

### Çok Ağaçlı Kurulumlar

Çok ağaçlı bir sunucuda, kullanıcının giriş yaptığı ağacın, Gramps Web'in kimlik sağlayıcısına yönlendirmeden önce bilinmesi gerekir, bu nedenle giriş şu şekilde başlar:

```
GET /api/oidc/login/?provider=<id>&tree=<tree_id>
```

`tree`, çok ağaçlı kurulumlarda gereklidir; bunu atlamak veya mevcut olmayan bir ağacın kimliğini geçmek girişin başarısız olmasına neden olur. Tek ağaçlı bir sunucuda `tree` isteğe bağlıdır, ancak verilirse yapılandırılmış `TREE` ile eşleşmelidir.

Bir OIDC kimliği tam olarak bir Gramps Web hesabına bağlıdır, bu da tam olarak bir ağaca aittir – farklı bir ağaçta giriş yapmak, hesabı taşımak yerine başarısız olur. Sağlayıcıda tek bir kimliği birden fazla ağaçtaki hesaplarla ilişkilendirmenin bir yolu yoktur; birden fazla ağaca erişim ihtiyacı olan kullanıcıların sağlayıcıda ayrı kimliklere sahip olmaları gerekir (örneğin, farklı kullanıcı adları veya hesaplar).

!!! warning
    İlişkili bir ağacı olmayan bir site yöneticisi hesabı (bkz. [bir yönetici hesabı oluşturma](../administration/owner.md)) OIDC üzerinden giriş yapamaz, çünkü OIDC girişi her zaman bir ağaç gerektirir. Bu tür hesaplar, bunun yerine yerel kullanıcı adı/şifre ile oluşturulmalı ve kimlik doğrulaması yapılmalıdır.

## Gerekli Yönlendirme URI'leri

OIDC sağlayıcınızı yapılandırırken, aşağıdaki yönlendirme URI'sini kaydetmelisiniz:

**Wildcard'ları destekleyen OIDC sağlayıcıları için: (örneğin, Authentik)**

- `https://your-gramps-backend.com/api/oidc/callback/*`

Burada `*` bir regex wildcard'dır. Sağlayıcınızın regex yorumlayıcısına bağlı olarak bu aynı zamanda `.*` veya benzeri bir şey de olabilir. Sağlayıcınızın bunu gerektirmesi durumunda regex'in etkin olduğundan emin olun (örneğin, Authentik).

**Wildcard'ları desteklemeyen OIDC sağlayıcıları için: (örneğin, Authelia)**

- `https://your-gramps-backend.com/api/oidc/callback/custom`

Ağaç, yönlendirme URI'sinin bir parçası değildir, hatta çok ağaçlı sunucularda bile – oturumda ayrı olarak taşınır, çünkü sağlayıcılar yönlendirme URI'sinin kaydedilen ile tam olarak eşleşmesini gerektirir.

## Rol Eşleme

Gramps Web, kimlik sağlayıcınızdan OIDC gruplarını veya rollerini Gramps Web kullanıcı rollerine otomatik olarak eşleyebilir. Bu, kullanıcı izinlerini merkezi olarak kimlik sağlayıcınızda yönetmenizi sağlar. Rol eşleme, tüm sağlayıcılar için aynı şekilde çalışır, ister yerleşik ister özel olsun.

### Yapılandırma

Rol eşlemesini yapılandırmak için bu ayarları kullanın:

Anahtar | Açıklama
----|-------------
`OIDC_ROLE_CLAIM` | Kullanıcının gruplarını/rollerini içeren OIDC jetonundaki talep adı. Varsayılan "groups" olarak ayarlanmıştır. Noktalı yollar desteklenir, örneğin `realm_access.roles`.
`OIDC_GROUP_ADMIN` | Gramps "Admin" rolüne eşlenen OIDC sağlayıcınızdan grup/rol adı
`OIDC_GROUP_OWNER` | Gramps "Owner" rolüne eşlenen OIDC sağlayıcınızdan grup/rol adı
`OIDC_GROUP_EDITOR` | Gramps "Editor" rolüne eşlenen OIDC sağlayıcınızdan grup/rol adı
`OIDC_GROUP_CONTRIBUTOR` | Gramps "Contributor" rolüne eşlenen OIDC sağlayıcınızdan grup/rol adı
`OIDC_GROUP_MEMBER` | Gramps "Member" rolüne eşlenen OIDC sağlayıcınızdan grup/rol adı
`OIDC_GROUP_GUEST` | Gramps "Guest" rolüne eşlenen OIDC sağlayıcınızdan grup/rol adı

### Rol Eşleme Davranışı

Hiçbir `OIDC_GROUP_*` ayarı yapılandırılmadıysa, rol eşleme kapalıdır ve roller Gramps Web'de manuel olarak yönetilir; yeni OIDC hesapları devre dışı olarak oluşturulur ve mevcut bir sahibi veya yöneticisi tarafından onaylanması gerekir (aşağıdaki [İlk Giriş ve Başlatma](#first-login-and-bootstrapping) bölümüne bakın).

Rol eşleme yapılandırıldığında, her girişte:

- Eğer rol talebi mevcutsa ve kullanıcı eşlenen bir gruba ait ise, ilgili rolü alır.
- Eğer rol talebi mevcutsa ancak kullanıcı eşlenen bir gruba ait değilse, rolü devre dışı olarak ayarlanır. Bu, bir hata değil, varsayılan bir kapalı durumdur – Gramps Web, tanımadığı bir grup için bir rol çıkaramaz.
- Eğer rol talebi tamamen jetondan yoksa, mevcut rol değiştirilmez; yeni bir hesap yine de varsayılan olarak devre dışı kalır.

!!! warning "Google bir grup talebi göndermez"
    Google'ın jetonları asla `groups` talebini içermez, bu nedenle rol eşleme etkinleştirildiğinde, Google girişleri yukarıdaki "talep yok" durumuna düşer: mevcut kullanıcılar rollerini korur, ancak yeni Google kullanıcıları devre dışı olarak oluşturulur ve manuel onay gerektirir. Başka bir sağlayıcı için rol eşlemeyi etkinleştirmeden önce bunu aklınızda bulundurun – bu, mevcut Google kullanıcılarını devre dışı bırakmaz.

Microsoft Entra, uygulama rollerini ve grup üyeliklerini yalnızca ID jetonunda döndürür, kullanıcı bilgisi uç noktasından değil. Gramps Web, ID jetonunun taleplerini kullanıcı bilgisi yanıtına birleştirir, böylece `OIDC_ROLE_CLAIM` diğer sağlayıcılar için olduğu gibi çalışır; her ikisi de bir talep içeriyorsa, kullanıcı bilgisi değeri öncelik alır.

## İlk Giriş ve Başlatma

OIDC aracılığıyla oluşturulan yeni hesaplar, rol eşleme onlara bir rol atamadıkça devre dışı başlar (yukarıya bakın). Yepyeni bir örnekte kimse devre dışı bir hesabı onaylayamaz ve `OIDC_DISABLE_LOCAL_AUTH` da etkinleştirildiyse, geri dönmek için bir şifre girişi de yoktur.

!!! warning "İlk girişten önce bir sahip/yönetici grubunu yapılandırın"
    Kimsenin OIDC üzerinden ilk kez giriş yapmadan önce, `OIDC_GROUP_OWNER` (veya `OIDC_GROUP_ADMIN`) ayarını yapın ve ilk kullanıcının sağlayıcıda o gruba ait olduğundan emin olun. Aksi takdirde, örnek OIDC üzerinden başlatılamaz.

## Hesaplar ve Kullanıcı Adları

OIDC aracılığıyla oluşturulan hesaplar, hesap oluşturulurken bir kez atanan ve daha sonraki girişlerde asla değiştirilmeyen bir kullanıcı adı alır:

- Yerleşik sağlayıcılar: `<provider>_<claim value>`, örneğin `microsoft_alice@contoso.com`
- Özel sağlayıcı: sade talep değeri, örneğin `alice`

Çakışma durumunda sayısal bir ek eklenir. OIDC ile oluşturulan bir hesabın kullanıcı adını daha sonra yeniden adlandırmanın bir yolu yoktur; tam ad ve e-posta adresi, aksine, her girişte yenilenir.

Bir OIDC girişi, e-posta adresini paylaşan mevcut bir yerel hesaba bağlanmaz – bu kasıtlıdır, çünkü hesapları e-posta ile bağlamak, hesap ele geçirme vektörüdür. Zaten yerel bir hesabı olan bir kullanıcı, OIDC üzerinden ilk kez giriş yaptığında ikinci, ayrı bir hesap alır.

Sağlayıcıdan gelen e-posta adresleri yalnızca sağlayıcı bunları doğrulanmış olarak işaretlerse (veya `email_verified` talebini tamamen atlarsa) ve adres başka bir hesap tarafından kullanılmıyorsa saklanır; aksi takdirde giriş, bir e-posta adresi saklamadan devam eder.

## OIDC Çıkışı

Gramps Web, OIDC sağlayıcıları için Tek Oturum Kapatma (SSO çıkışı) desteği sunar. `GET /api/oidc/logout/` sağlayıcının `end_session_endpoint`'ini arar ve yanıt olarak `logout_url` olarak döndürür; tarayıcıyı oraya yönlendiren Gramps Web ön yüzüdür, böylece kimlik sağlayıcısında oturum gerçekten sona erer. `logout_url`, sağlayıcının `end_session_endpoint`'i yoksa `null` olur.

!!! warning "Çıkışta jetonlar iptal edilmez"
    Çıkış yapmak yalnızca tarayıcı oturumunu sonlandırır; şu anda daha önce verilmiş bir Gramps Web jetonunu iptal etmenin bir yolu yoktur. Jetonlar, süresi dolana kadar geçerli kalır (`JWT_ACCESS_TOKEN_EXPIRES`, varsayılan 15 dakika erişim jetonları için), kullanıcı Gramps Web'de veya kimlik sağlayıcısında çıkış yapmış olsa bile.

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
OIDC_AUTO_REDIRECT=True  # İsteğe bağlı: SSO girişine otomatik yönlendirme
OIDC_DISABLE_LOCAL_AUTH=True  # İsteğe bağlı: kullanıcı adı/şifre girişini devre dışı bırak

# İsteğe bağlı: OIDC gruplarından Gramps rollerine rol eşleme
OIDC_ROLE_CLAIM="groups"  # veya sağlayıcınıza bağlı olarak "roles"
OIDC_GROUP_ADMIN="gramps-admins"
OIDC_GROUP_EDITOR="gramps-editors"
OIDC_GROUP_MEMBER="gramps-members"

EMAIL_HOST="mail.example.com"
EMAIL_PORT=465
EMAIL_USE_TLS=True
EMAIL_HOST_USER="gramps@example.com"
EMAIL_HOST_PASSWORD="..." # SMTP şifreniz
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

Gramps Web için topluluk tarafından oluşturulmuş bir OIDC kurulum kılavuzu [resmi Authelia dokümantasyon web sitesinde](https://www.authelia.com/integration/openid-connect/clients/gramps/) mevcuttur.

### Keycloak

Keycloak için yapılandırmanın çoğu varsayılan olarak bırakılabilir (*Client → Create client → Client authentication ON*). Birkaç istisna vardır:

1. **OpenID kapsamı** – `openid` kapsamı, tüm Keycloak sürümlerinde varsayılan olarak dahil edilmez. Sorun yaşamamak için manuel olarak ekleyin: *Client → [Gramps client] → Client scopes → Add scope → Name: `openid` → Set as default.*
2. **Roller** – Roller, ya istemci düzeyinde ya da realm başına küresel olarak atanabilir.

    * İstemci rollerini kullanıyorsanız, `OIDC_ROLE_CLAIM` yapılandırma seçeneğini şu şekilde ayarlayın: `resource_access.[gramps-client-name].roles`
    * Rolleri Gramps'a görünür hale getirmek için *Client Scopes* (belirli istemcinin altında değil, üst düzey bölüm) bölümüne gidin, ardından: *Roles → Mappers → client roles → Add to userinfo → ON.*
