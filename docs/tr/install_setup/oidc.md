# OIDC Kimlik Doğrulama

Gramps Web, kullanıcıların harici kimlik sağlayıcıları kullanarak giriş yapmalarına olanak tanıyan OpenID Connect (OIDC) kimlik doğrulamasını destekler. Bu, yerleşik sağlayıcılar olan Google ve Microsoft'un yanı sıra Keycloak, Authentik ve Authelia gibi özel OIDC sağlayıcılarını da içerir.

!!! warning "GitHub OIDC sağlayıcısı artık desteklenmiyor"
    Eğer daha önceki bir sürümden `OIDC_GITHUB_CLIENT_ID` / `OIDC_GITHUB_CLIENT_SECRET` ayarlarını yaptıysanız, bunları kaldırın – artık göz ardı ediliyorlar ve daha önce GitHub üzerinden giriş yapan kullanıcılar bu şekilde giriş yapamazlar. GitHub bir OAuth 2.0 sağlayıcısıdır, OpenID Connect sağlayıcısı değildir ve Gramps Web'in kimlik için güvendiği talebi asla geri döndürmediği için tam olarak güvenilir olmamıştır.

## Genel Bakış

OIDC kimlik doğrulaması, şunları yapmanıza olanak tanır:

- Kullanıcı kimlik doğrulaması için harici kimlik sağlayıcıları kullanma
- Aynı anda birden fazla kimlik doğrulama sağlayıcısını destekleme
- OIDC gruplarını/rollerini Gramps Web kullanıcı rollerine eşleme
- Tek Oturum Açma (SSO) ve Tek Oturum Kapatma uygulama
- İsteğe bağlı olarak yerel kullanıcı adı/parola kimlik doğrulamasını devre dışı bırakma

## Yapılandırma

OIDC kimlik doğrulamasını etkinleştirmek için, Gramps Web yapılandırma dosyanızda veya ortam değişkenlerinde uygun ayarları yapılandırmanız gerekir. Mevcut OIDC ayarlarının tam listesini görmek için [Sunucu Yapılandırması](configuration.md#settings-for-oidc-authentication) sayfasına bakın.

!!! info
    Ortam değişkenlerini kullanırken, her ayar adını `GRAMPSWEB_` ile ön eklemeyi unutmayın (örneğin, `GRAMPSWEB_OIDC_ENABLED`). Ayrıntılar için [Yapılandırma dosyası vs. ortam değişkenleri](configuration.md#configuration-file-vs-environment-variables) sayfasına bakın.

### Yerleşik Sağlayıcılar

Gramps Web, popüler kimlik sağlayıcıları için yerleşik destek sunar. Bunları kullanmak için yalnızca istemci kimliğini ve istemci sırrını sağlamanız gerekir:

- **Google**: `OIDC_GOOGLE_CLIENT_ID` ve `OIDC_GOOGLE_CLIENT_SECRET`
- **Microsoft**: `OIDC_MICROSOFT_CLIENT_ID` ve `OIDC_MICROSOFT_CLIENT_SECRET`

Birden fazla sağlayıcıyı aynı anda yapılandırabilirsiniz. Sistem, yapılandırma değerlerine dayanarak hangi sağlayıcıların mevcut olduğunu otomatik olarak algılayacaktır.

!!! tip "Microsoft: tek kiracı dağıtımları"
    Yerleşik Microsoft sağlayıcısı, tasarımı gereği çok kiracılı `/common` uç noktasını kullanır ve herhangi bir Microsoft hesabından girişleri kabul eder. Sadece kendi kiracınızdaki kullanıcıların giriş yapmasına izin vermek istiyorsanız, bunun yerine kiracınıza özel verici URL'si ile [özel OIDC sağlayıcısını](#custom-oidc-providers) kullanın; bu, verici doğrulamasını aktif tutar ve girişleri o kiracı ile sınırlar.

### Özel OIDC Sağlayıcıları

Özel OIDC sağlayıcıları (örneğin Keycloak, Authentik, Authelia veya tek kiracı Microsoft Entra kiracısı) için bu ayarları kullanın:

Anahtar | Açıklama
----|-------------
`OIDC_ENABLED` | OIDC kimlik doğrulamasını etkinleştirmek için Boolean. `True` olarak ayarlayın.
`OIDC_ISSUER` | Sağlayıcınızın verici URL'si. Keşif `<issuer>/.well-known/openid-configuration` adresinden alınır.
`OIDC_CLIENT_ID` | OIDC sağlayıcınız için istemci kimliği
`OIDC_CLIENT_SECRET` | OIDC sağlayıcınız için istemci sırrı
`OIDC_NAME` | Özel görüntü adı (isteğe bağlı, varsayılan "OIDC")
`OIDC_SCOPES` | OAuth kapsamları (isteğe bağlı, varsayılan "openid email profile")
`OIDC_USERNAME_CLAIM` | Kullanıcı adını oluşturmak için kullanılan talep (isteğe bağlı, varsayılan "preferred_username")
`OIDC_PKCE` | PKCE kullanılıp kullanılmayacağı, [PKCE](#pkce) sayfasına bakın (isteğe bağlı, sağlayıcı destekliyorsa otomatik olarak etkinleştirilir)

### PKCE

Gramps Web API 3.23 itibarıyla, Gramps Web [PKCE](https://datatracker.ietf.org/doc/html/rfc7636) (Kod Değişimi için Kanıt Anahtarı, `S256` yöntemi) için yetkilendirme kodu akışını destekler. Pocket ID gibi bazı kimlik sağlayıcıları, bir istemci için PKCE'yi *gerektirecek* şekilde yapılandırılabilir ve bunu kullanmayan girişleri reddeder. Gramps Web API'nin eski sürümleri PKCE'yi asla kullanmaz, bu nedenle böyle bir istemci ile girişler başarısız olur.

PKCE'nin kullanılıp kullanılmadığı, giriş sırasında şu şekilde belirlenir:

- `OIDC_PKCE` `True` olarak ayarlandığında, PKCE kullanılır.
- `OIDC_PKCE` `False` olarak ayarlandığında, PKCE kullanılmaz, sağlayıcı desteklese bile.
- `OIDC_PKCE` ayarlanmamışsa veya ayarlanmış ama boşsa, sağlayıcının keşif belgesinde (`/.well-known/openid-configuration`) `code_challenge_methods_supported` içinde `S256` listeleniyorsa PKCE kullanılır, aksi takdirde kullanılmaz.

Çoğu yapılandırma için herhangi bir şey ayarlamanıza gerek yoktur. Sağlayıcınız PKCE gerektiriyorsa ancak keşif belgesinde `S256`'yı bildirmiyorsa `OIDC_PKCE`'yi `True` olarak ayarlayın ve `S256`'yı bildirdiği ancak yanlış yönettiği durumlarda `False` olarak ayarlayın. Ortam değişkenleri olarak, boolean değerler küçük harfle yazılmalıdır (`GRAMPSWEB_OIDC_PKCE=true`), [Yapılandırma](configuration.md) sayfasına bakın.

Yerleşik sağlayıcılar için karşılık gelen seçenekler `OIDC_GOOGLE_PKCE` ve `OIDC_MICROSOFT_PKCE`'dir.

PKCE kod doğrulayıcı, sağlayıcıya yönlendirme ile geri çağırma arasındaki kullanıcının oturumunda tutulur, bu nedenle yönlendirme URI'lerinde herhangi bir değişiklik gerektirmez.

### Çok Ağaçlı Yapılandırmalar

Çok ağaçlı bir sunucuda, Gramps Web hesabına zaten bağlı bir kimlik ile giriş yapan bir kullanıcı, o hesabın ağacına giriş yapar, bu nedenle düz giriş sayfası onlar için çalışır.

OIDC kimliği ile *yeni* bir hesap oluşturmak için, Gramps Web'in hangi ağaca ait olduğunu bilmesi gerekir. Bu nedenle yeni kullanıcılar, ağacın kayıt bağlantısından (`/register/<tree_id>`, [Kayıt bağlantısı](../administration/users.md#registration-link-multi-tree-setup-only) sayfasına bakın) veya ağacın giriş sayfasından (`/login/<tree_id>`) başlamalıdır. Her ikisi de yapılandırılmış sağlayıcıları sunar. Düz giriş sayfasından bilinmeyen bir kimlik ile giriş yapmak, kayıt bağlantısına işaret eden bir mesajla reddedilir. Bu, Gramps Web API 3.25.3 ve Gramps Web 26.11.2 veya daha yenisini gerektirir.

Arka planda, giriş şu şekilde başlar:

```
GET /api/oidc/login/?provider=<id>&tree=<tree_id>
```

Burada `tree` isteğe bağlıdır, yeni bir hesap oluşturulmadıkça. Mevcut olmayan bir ağacın ID'sini geçmek, girişin başarısız olmasına neden olur. Tek ağaçlı bir sunucuda `tree` isteğe bağlıdır, ancak verildiğinde yapılandırılmış `TREE` ile eşleşmelidir.

Bir OIDC kimliği tam olarak bir Gramps Web hesabına bağlıdır ve bu da tam olarak bir ağaca aittir – farklı bir ağaçta giriş yapmak, hesabı taşımak yerine başarısız olur. Sağlayıcıda tek bir kimliği birden fazla ağaçta hesaplara bağlamanın bir yolu yoktur; birden fazla ağaca erişim ihtiyacı olan kullanıcıların sağlayıcıda ayrı kimliklere sahip olmaları gerekir (örneğin, farklı kullanıcı adları veya hesaplar).

!!! warning
    İlişkili bir ağaç olmayan bir site yöneticisi hesabı (bkz. [bir yönetici hesabı oluşturma](../administration/owner.md)) OIDC aracılığıyla oluşturulamaz, çünkü OIDC girişi ile oluşturulan bir hesap her zaman bir ağaca aittir. Bu tür hesapları yerel kullanıcı adı ve parolayla oluşturun.

### Yerel Uygulamalar

Gramps Web için mobil uygulamalar gibi yerel uygulamalar, kullanıcının sistem tarayıcısında giriş yapmasına ve sonucu uygulamanın `https` bağlantısında almasına olanak tanıyabilir. Gramps Web API 3.26'dan itibaren, bu, bağlantının `OIDC_ALLOWED_REDIRECT_URIS` içinde listelenmesi durumunda çalışır, örneğin:

```
GRAMPSWEB_OIDC_ALLOWED_REDIRECT_URIS='["https://app.example.com/oidc-callback"]'
```

Uygulamanın belgeleri hangi bağlantının eklenmesi gerektiğini belirtir. Kimlik sağlayıcısında kayıtlı olan yönlendirme URI'leri aynı kalır.

## Gerekli Yönlendirme URI'leri

OIDC sağlayıcınızı yapılandırırken, aşağıdaki yönlendirme URI'sini kaydetmelisiniz:

**Wildcard'ları destekleyen OIDC sağlayıcıları için: (örneğin, Authentik)**

- `https://your-gramps-backend.com/api/oidc/callback/*`

Burada `*` bir regex wildcard'ıdır. Sağlayıcınızın regex yorumlayıcısına bağlı olarak bu aynı zamanda `.*` veya benzeri de olabilir. Sağlayıcınızın bunu gerektirmesi durumunda regex'in etkin olduğundan emin olun (örneğin, Authentik).

**Wildcard'ları desteklemeyen OIDC sağlayıcıları için: (örneğin, Authelia)**

- `https://your-gramps-backend.com/api/oidc/callback/custom`

Ağaç, yönlendirme URI'sinin bir parçası değildir, çok ağaçlı sunucularda bile – oturumda ayrı olarak taşınır, çünkü sağlayıcılar yönlendirme URI'sinin kaydedilen ile tam olarak eşleşmesini gerektirir.

## Rol Eşlemesi

Gramps Web, kimlik sağlayıcınızdan OIDC gruplarını veya rollerini Gramps Web kullanıcı rollerine otomatik olarak eşleyebilir. Bu, kullanıcı izinlerini merkezi olarak kimlik sağlayıcınızda yönetmenizi sağlar. Rol eşlemesi, tüm sağlayıcılar için aynı şekilde çalışır, ister yerleşik ister özel olsun.

### Yapılandırma

Rol eşlemesini yapılandırmak için bu ayarları kullanın:

Anahtar | Açıklama
----|-------------
`OIDC_ROLE_CLAIM` | Kullanıcının gruplarını/rollerini içeren OIDC token'ındaki talep adı. Varsayılan "groups". Noktalı yollar desteklenir, örneğin `realm_access.roles`.
`OIDC_GROUP_ADMIN` | Gramps "Admin" rolüne eşlenen OIDC sağlayıcınızdan grup/rol adı
`OIDC_GROUP_OWNER` | Gramps "Owner" rolüne eşlenen OIDC sağlayıcınızdan grup/rol adı
`OIDC_GROUP_EDITOR` | Gramps "Editor" rolüne eşlenen OIDC sağlayıcınızdan grup/rol adı
`OIDC_GROUP_CONTRIBUTOR` | Gramps "Contributor" rolüne eşlenen OIDC sağlayıcınızdan grup/rol adı
`OIDC_GROUP_MEMBER` | Gramps "Member" rolüne eşlenen OIDC sağlayıcınızdan grup/rol adı
`OIDC_GROUP_GUEST` | Gramps "Guest" rolüne eşlenen OIDC sağlayıcınızdan grup/rol adı

### Rol Eşlemesi Davranışı

Hiçbir `OIDC_GROUP_*` ayarı yapılandırılmamışsa, rol eşlemesi kapalıdır ve roller Gramps Web'de manuel olarak yönetilir; yeni OIDC hesapları devre dışı olarak oluşturulur ve mevcut bir sahip veya yönetici tarafından onaylanması gerekir (bkz. [İlk Giriş ve Başlatma](#first-login-and-bootstrapping) aşağıda).

Rol eşlemesi yapılandırıldıktan sonra, her girişte:

- Rol talebi mevcutsa ve kullanıcı eşlenen bir gruba ait ise, ilgili rolü alır.
- Rol talebi mevcutsa ancak kullanıcı eşlenen bir gruba ait değilse, rolü devre dışı olarak ayarlanır. Bu, kapalı bir varsayılan olup, bir grubun tanınmadığı durumlarda Gramps Web'in bir rol çıkarımı yapamamasıdır.
- Rol talebi token'dan tamamen yoksa, mevcut rol değiştirilmez; yeni bir hesap yine devre dışı olarak varsayılan ayara sahiptir.

!!! warning "Google bir gruplar talebi göndermez"
    Google'ın token'ları asla `groups` talebini içermez, bu nedenle rol eşlemesi etkinleştirildiğinde, Google girişleri yukarıdaki "talep yok" durumuna girer: mevcut kullanıcılar rollerini korur, ancak yeni Google kullanıcıları devre dışı olarak oluşturulur ve manuel onay gerektirir. Başka bir sağlayıcı için rol eşlemesini etkinleştirmeden önce bunu göz önünde bulundurun – bu, mevcut Google kullanıcılarını kendiliğinden devre dışı bırakmaz.

Microsoft Entra, uygulama rollerini ve grup üyeliklerini yalnızca ID token'ında döndürür, kullanıcı bilgisi uç noktasından değil. Gramps Web, ID token'ının taleplerini kullanıcı bilgisi yanıtına birleştirir, böylece `OIDC_ROLE_CLAIM` diğer sağlayıcılar için olduğu gibi çalışır; her ikisi de bir talep içeriyorsa, kullanıcı bilgisi değeri önceliğe sahiptir.

## İlk Giriş ve Başlatma

OIDC aracılığıyla oluşturulan yeni hesaplar, rol eşlemesi onlara bir rol atamadıkça devre dışı olarak başlar (bkz. yukarıda). Yepyeni bir örnekte kimse devre dışı bir hesabı onaylayamaz ve `OIDC_DISABLE_LOCAL_AUTH` da etkinse, geri dönmek için bir parola girişi de yoktur.

!!! warning "İlk girişten önce bir sahip/yönetici grubunu yapılandırın"
    Kimse OIDC aracılığıyla ilk kez giriş yapmadan önce, `OIDC_GROUP_OWNER` (veya `OIDC_GROUP_ADMIN`) ayarını yapın ve ilk kullanıcının sağlayıcıda o gruba ait olduğundan emin olun. Aksi takdirde, örnek OIDC aracılığıyla başlatılamaz.

## Hesaplar ve Kullanıcı Adları

OIDC aracılığıyla oluşturulan hesaplar, hesap oluşturma sırasında bir kez atanan ve sonraki girişlerde asla değiştirilmeyen bir kullanıcı adı alır:

- Yerleşik sağlayıcılar: `<provider>_<claim value>`, örneğin `microsoft_alice@contoso.com`
- Özel sağlayıcı: sade talep değeri, örneğin `alice`

Çakışma durumunda bir sayısal ek eklenir. OIDC ile oluşturulan bir hesabın kullanıcı adını daha sonra yeniden adlandırmanın bir yolu yoktur; aksine, tam ad ve e-posta adresi her girişte yenilenir.

Bir OIDC girişi, e-posta adresini paylaşan mevcut bir yerel hesaba asla bağlanmaz – bu kasıtlıdır, çünkü hesapları e-posta ile bağlamak bir hesap ele geçirme vektörüdür. Zaten bir yerel hesabı olan bir kullanıcı, OIDC aracılığıyla ilk kez giriş yaptığında ikinci, ayrı bir hesap alır, eğer önce sağlayıcıyı hesabına bağlamazsa.

Gramps Web API 3.24 itibarıyla, kullanıcılar OIDC kimliklerini mevcut hesaplarına bağlayabilir ve bunları listeleyip ayırabilirler, [Kullanıcı Ayarları > Bağlı giriş yöntemleri](../user-guide/settings.md#linked-sign-in-methods) altında. Bağlama, yakın zamanda bir giriş gerektirir ve kullanıcının kendi token'ı ile onaylanır, bu nedenle ön uç API'den farklı bir kökene sahip olsa bile çalışır. Bir kimlik yalnızca bir hesaba ait olabilir; zaten kendi hesabı olan bir kimliği bağlamak için, bir yönetici önce o hesabı silmelidir (değişiklikleri kalır, ancak revizyon geçmişi artık adını göstermez). Son bağlı kimlik yalnızca hesabın mevcut parolası ile ayrılabilir ve `OIDC_DISABLE_LOCAL_AUTH` ayarı yapıldıysa hiç ayrılamaz.

Sağlayıcıdan gelen e-posta adresleri yalnızca sağlayıcı bunları doğrulanmış olarak işaretlerse (veya `email_verified` talebini tamamen atlıyorsa) saklanır; aksi takdirde giriş, bir e-posta adresi saklamadan devam eder. E-posta adreslerinin benzersiz olması gerekmediğinden (Gramps Web API 3.22 itibarıyla), başka bir hesap zaten kullanıyorsa bile bir adres saklanır.

## OIDC Çıkışı

Gramps Web, OIDC sağlayıcıları için Tek Oturum Kapatma (SSO çıkışı) destekler. `GET /api/oidc/logout/` sağlayıcının `end_session_endpoint`'ini arar ve yanıt olarak `logout_url` olarak döndürür; tarayıcıyı oraya yönlendiren Gramps Web ön yüzüdür, böylece kimlik sağlayıcısındaki oturum gerçekten sonlanır. `logout_url`, sağlayıcının `end_session_endpoint`'i yoksa `null` olur.

!!! warning "Çıkışta token'lar iptal edilmez"
    Çıkış yapmak yalnızca tarayıcı oturumunu sonlandırır; şu anda daha önce verilmiş bir Gramps Web token'ını iptal etmenin bir yolu yoktur. Token'lar, kullanıcı Gramps Web'de veya kimlik sağlayıcısında çıkış yapsa bile, süresi dolana kadar geçerli kalır (`JWT_ACCESS_TOKEN_EXPIRES`, varsayılan 15 dakika erişim token'ları için).

## Sorun Giderme

Girişin durduğu noktadan başlayın ve dalı takip edin. Gramps Web, başarısız bir geri çağırmanın nedenini kaydeder (sunucu kaydında `OIDC callback error for provider` arayın), bu genellikle tarayıcıda gösterilen mesajdan daha spesifiktir.

**1. Giriş düğmesi eksik mi?**

- `<BASE_URL>/api/oidc/config/` adresini kontrol edin. Eğer `enabled` `false` veya `providers` boşsa, OIDC yapılandırılmamıştır: `OIDC_ENABLED` `True` olmalıdır ve özel bir sağlayıcı için hem `OIDC_ISSUER` hem de `OIDC_CLIENT_ID` ayarlanmalıdır.
- Bir yerleşik sağlayıcı (Google, Microsoft) yalnızca istemci kimliği ve istemci sırrı ayarlandığında kaydedilir.
- Sunucu kaydında başlangıçta `Could not load discovery document` mesajını arayın. Bu, sunucunun `<issuer>/.well-known/openid-configuration` (veya `OIDC_OPENID_CONFIG_URL`) adresine ulaşamadığı anlamına gelir. İlk kullanımda yeniden dener, ancak Gramps Web konteynerinin verici URL'sini kendisinin çözebilmesi ve ulaşabilmesi gerekir, yalnızca tarayıcınız değil.

**2. Tarayıcı, sağlayıcıya gönderildikten hemen sonra bir hata alıyor mu?**

Hata, giriş yapmadan önce kimlik sağlayıcısı tarafından gösterilir.

- *"yönlendirme URI'si uyuşmazlığı"* (veya benzeri): sağlayıcıda kayıtlı yönlendirme URI'si tam olarak eşleşmelidir, şeması, ana bilgisayarı, portu ve sağlayıcı kimliği dahil. [Gerekli Yönlendirme URI'leri](#required-redirect-uris) sayfasına bakın. Bunun `BASE_URL`'den oluşturulduğunu unutmayın, bu nedenle yanlış bir `BASE_URL` yanlış bir yönlendirme URI'si verir.
- *Bir PKCE hatası* (örneğin `invalid_request`, "kod zorluğu gerekli" veya eksik `code_challenge` parametresi): sağlayıcı PKCE'yi gerektiriyor ancak Gramps Web bunu göndermedi. Aşağıdaki [PKCE dalına](#pkce-branch) gidin.

**3. Sağlayıcı girişi kabul ediyor ancak Gramps Web ardından bir hata gösteriyor mu?**

- *`mismatching_state`, veya hata oturum veya durumdan bahsediyorsa*: tarayıcı, Gramps Web'in giriş başladığında ayarladığı oturum çerezini geri göndermedi. Bu çerez ayrıca PKCE kod doğrulayıcısını da taşır. Tarayıcıdaki adresin `BASE_URL` ile eşleştiğinden (aynı şema ve ana bilgisayar), ters proxy'nin çerezleri ve orijinal ana bilgisayarı geçirdiğinden ve girişin aynı tarayıcı sekmesinde veya penceresinde başlatılıp tamamlandığından emin olun.
- *`OIDC authentication failed for <provider>` (HTTP 401)*: temel nedeni görmek için sunucu kaydını kontrol edin. Yaygın nedenler yanlış bir istemci sırrı, token'ların `iss` talebi ile eşleşmeyen bir verici URL'si ve sağlayıcının geri çağrıya bir hata döndürmesi (örneğin PKCE, aşağıda) olabilir.
- *Çok fazla deneme*: giriş ve geri çağırma uç noktaları oran sınırlıdır (dakikada 5 istek). Bir dakika bekleyin ve yeniden deneyin.

**4. Giriş başarılı ancak "Hesap İnceleme Altında" mesajını mı görüyorsunuz, yoksa hiçbir şey yapamıyor musunuz?**

Yeni hesaplar, rol eşlemesi bir rol atamadıkça devre dışı olarak oluşturulur. [İlk Giriş ve Başlatma](#first-login-and-bootstrapping) ve [Rol Eşlemesi Davranışı](#role-mapping-behavior) sayfasına bakın. Bir yönetici, Hesaplar > Yönetim > Kullanıcıları Yönet altında hesabı etkinleştirebilir.

### PKCE dalı

Gramps Web, bir giriş başladığında PKCE kullanılıp kullanılmayacağına karar verir (bkz. [PKCE](#pkce)). Yapılandırmanız için ne olduğunu bulmak için bu soruları sırayla yanıtlayın:

1. **`OIDC_PKCE` ayarlandı mı?** (Yerleşik sağlayıcılar için, `OIDC_GOOGLE_PKCE` veya `OIDC_MICROSOFT_PKCE`.)
    - `True`: PKCE kullanılır. Soru 3'e geçin.
    - `False`: PKCE kasıtlı olarak kapalıdır ve sağlayıcının keşif belgesi göz ardı edilir. Sağlayıcınız PKCE'yi gerektiriyorsa, ayarı kaldırın veya `True` olarak ayarlayın.
    - Ayarlanmamış veya boş: soru 2 ile devam edin.
2. **Keşif belgesi `S256` listeliyor mu?** `<issuer>/.well-known/openid-configuration` adresini açın ve `code_challenge_methods_supported` içinde `S256`'yı arayın.
    - Evet: PKCE otomatik olarak kullanılır. Soru 3 ile devam edin.
    - Hayır veya alan eksik: PKCE **kullanılmıyor**. Sağlayıcınız bunu gerektiriyorsa `OIDC_PKCE`'yi `True` olarak ayarlayın. Ayrıca sunucu kaydında `Could not check the provider for PKCE support` mesajını kontrol edin, bu, keşif belgesinin alınamadığı ve bu nedenle PKCE'nin kapalı kaldığı anlamına gelir.
3. **PKCE gerçekten gönderildi mi?** Bir giriş başlatın ve sağlayıcının giriş sayfasının adresine (veya tarayıcınızın ağ sekmesindeki ilk yönlendirmeye) bakın. `code_challenge=` ve `code_challenge_method=S256` içermelidir.
    - Varsa, ancak giriş hala geri çağırmada başarısız oluyorsa: sağlayıcı kod doğrulayıcıyı reddetti. Yönlendirme ile geri çağırma arasında oturum çerezi kaybolmuş olabilir (yukarıdaki dal 3'e bakın), veya sağlayıcı `S256`'yı desteklemiyordur, bu durumda sağlayıcı PKCE'yi gerektirmiyorsa `OIDC_PKCE`'yi `False` olarak ayarlayın.
    - Yoksa: yukarıdaki ayarlar uygulanmamış. Ortam değişkeninin doğru öneki ve küçük harfli bir değeri olduğundan emin olun (örneğin `GRAMPSWEB_OIDC_PKCE=true` Docker'da; `True` bir boolean olarak okunmaz), sunucuyu yeniden başlatın ve yapılandırmayı tekrar kontrol edin.

!!! note
    Sağlayıcıda PKCE *isteğe bağlı* olarak etkinse veya hiç etkin değilse, Gramps Web bir zorluk gönderip göndermediğine bakılmaksızın girişler çalışır. Sadece PKCE'yi *gerektiren* sağlayıcılar (veya istemciler) bu ayarın önemli olmasını sağlar.

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
OIDC_AUTO_REDIRECT=True  # İsteğe bağlı: otomatik olarak SSO girişine yönlendirin
OIDC_DISABLE_LOCAL_AUTH=True  # İsteğe bağlı: kullanıcı adı/parola girişini devre dışı bırakın

# İsteğe bağlı: OIDC gruplarından Gramps rollerine rol eşlemesi
OIDC_ROLE_CLAIM="groups"  # veya sağlayıcınıza bağlı olarak "roles"
OIDC_GROUP_ADMIN="gramps-admins"
OIDC_GROUP_EDITOR="gramps-editors"
OIDC_GROUP_MEMBER="gramps-members"

EMAIL_HOST="mail.example.com"
EMAIL_PORT=465
EMAIL_USE_SSL=True  # Port 465 için örtük SSL kullanın
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

### Pocket ID

Pocket ID'de `<BASE_URL>/api/oidc/callback/custom` yönlendirme URI'si ile bir OIDC istemcisi oluşturun (bkz. [Gerekli Yönlendirme URI'leri](#required-redirect-uris)). Eğer istemci için "PKCE'yi Gerektir" seçeneğini etkinleştirirseniz, ek bir Gramps Web yapılandırması gerekmez, çünkü Pocket ID keşif belgesinde PKCE desteğini bildirir. Ardından yapılandırın:

```
GRAMPSWEB_OIDC_ENABLED=True
GRAMPSWEB_OIDC_ISSUER=https://id.example.com
GRAMPSWEB_OIDC_CLIENT_ID=<client id>
GRAMPSWEB_OIDC_CLIENT_SECRET=<client secret>
GRAMPSWEB_OIDC_NAME=Pocket ID
```

### Authelia

Gramps Web için topluluk tarafından oluşturulmuş bir OIDC yapılandırma kılavuzu [resmi Authelia belgeleri web sitesinde](https://www.authelia.com/integration/openid-connect/clients/gramps/) mevcuttur.

### Keycloak

Keycloak için yapılandırmanın çoğu varsayılan ayarlarında bırakılabilir (*İstemci → İstemci oluştur → İstemci kimlik doğrulaması AÇIK*).
Birkaç istisna vardır:

1. **OpenID kapsamı** – `openid` kapsamı tüm Keycloak sürümlerinde varsayılan olarak dahil edilmez. Sorun yaşamamak için manuel olarak ekleyin: *İstemci → [Gramps istemcisi] → İstemci kapsamları → Kapsam ekle → Ad: `openid` → Varsayılan olarak ayarla.*
2. **Roller** – Roller, ya istemci düzeyinde ya da realm başına küresel olarak atanabilir.

    * İstemci rollerini kullanıyorsanız, `OIDC_ROLE_CLAIM` yapılandırma seçeneğini şu şekilde ayarlayın: `resource_access.[gramps-client-name].roles`
    * Roller Gramps'a görünür hale getirmek için *İstemci Kapsamları* (belirli istemcinin altında değil, üst düzey bölüm) bölümüne gidin, ardından: *Roller → Haritalayıcılar → istemci rolleri → kullanıcı bilgisine ekle → AÇIK.*
