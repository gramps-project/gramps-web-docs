# OIDC Kimlik Doğrulaması

Gramps Web, kullanıcıların harici kimlik sağlayıcıları kullanarak oturum açmalarına olanak tanıyan OpenID Connect (OIDC) kimlik doğrulamasını destekler. Bu, yerleşik sağlayıcılar olan Google ve Microsoft'un yanı sıra Keycloak, Authentik ve Authelia gibi özel OIDC sağlayıcılarını da içerir.

!!! warning "GitHub bir OIDC sağlayıcısı olarak artık desteklenmiyor"
    Eğer daha önceki bir sürümden `OIDC_GITHUB_CLIENT_ID` / `OIDC_GITHUB_CLIENT_SECRET` ayarlarını yaptıysanız, bunları kaldırın – artık göz ardı ediliyor ve daha önce GitHub üzerinden oturum açan kullanıcılar bu şekilde oturum açamaz. GitHub, bir OAuth 2.0 sağlayıcısıdır, OpenID Connect sağlayıcısı değildir ve Gramps Web'in kimlik için güvendiği talebi asla döndürmediği için tam olarak güvenilir olmamıştır.

## Genel Bakış

OIDC kimlik doğrulaması, aşağıdakileri yapmanıza olanak tanır:

- Kullanıcı kimlik doğrulaması için harici kimlik sağlayıcıları kullanma
- Aynı anda birden fazla kimlik doğrulama sağlayıcısını destekleme
- OIDC gruplarını/rollerini Gramps Web kullanıcı rollerine eşleme
- Tek Oturum Açma (SSO) ve Tek Oturum Kapatma uygulama
- İsteğe bağlı olarak yerel kullanıcı adı/şifre kimlik doğrulamasını devre dışı bırakma

## Yapılandırma

OIDC kimlik doğrulamasını etkinleştirmek için Gramps Web yapılandırma dosyanızda veya ortam değişkenlerinde uygun ayarları yapılandırmanız gerekir. Mevcut OIDC ayarlarının tam listesi için [Sunucu Yapılandırması](configuration.md#settings-for-oidc-authentication) sayfasına bakın.

!!! info
    Ortam değişkenlerini kullanırken, her ayar adını `GRAMPSWEB_` ile ön eklemeyi unutmayın (örneğin, `GRAMPSWEB_OIDC_ENABLED`). Ayrıntılar için [Yapılandırma dosyası ile ortam değişkenleri](configuration.md#configuration-file-vs-environment-variables) sayfasına bakın.

### Yerleşik Sağlayıcılar

Gramps Web, popüler kimlik sağlayıcıları için yerleşik destek sunar. Bunları kullanmak için yalnızca istemci kimliği ve istemci sırrını sağlamanız gerekir:

- **Google**: `OIDC_GOOGLE_CLIENT_ID` ve `OIDC_GOOGLE_CLIENT_SECRET`
- **Microsoft**: `OIDC_MICROSOFT_CLIENT_ID` ve `OIDC_MICROSOFT_CLIENT_SECRET`

Birden fazla sağlayıcıyı aynı anda yapılandırabilirsiniz. Sistem, yapılandırma değerlerine göre hangi sağlayıcıların mevcut olduğunu otomatik olarak algılayacaktır.

!!! tip "Microsoft: tek kiracı dağıtımları"
    Yerleşik Microsoft sağlayıcısı, tasarımı gereği çok kiracılı `/common` uç noktasını kullanır ve herhangi bir Microsoft hesabından oturum açılmasına izin verir. Sadece kendi kiracınızdaki kullanıcıların oturum açmasına izin vermek istiyorsanız, bunun yerine kiracıya özgü verici URL'si ile [özel OIDC sağlayıcısını](#custom-oidc-providers) kullanın; bu, verici doğrulamasını aktif tutar ve oturum açmayı o kiracı ile sınırlar.

### Özel OIDC Sağlayıcıları

Özel OIDC sağlayıcıları (Keycloak, Authentik, Authelia veya tek kiracı Microsoft Entra kiracısı gibi) için bu ayarları kullanın:

Anahtar | Açıklama
----|-------------
`OIDC_ENABLED` | OIDC kimlik doğrulamasını etkinleştirip etkinleştirmeyeceğini belirten boolean. `True` olarak ayarlayın.
`OIDC_ISSUER` | Sağlayıcınızın verici URL'si. Keşif, `<issuer>/.well-known/openid-configuration` adresinden alınır.
`OIDC_CLIENT_ID` | OIDC sağlayıcınız için istemci kimliği
`OIDC_CLIENT_SECRET` | OIDC sağlayıcınız için istemci sırrı
`OIDC_NAME` | Özel görüntü adı (isteğe bağlı, varsayılan "OIDC")
`OIDC_SCOPES` | OAuth kapsamları (isteğe bağlı, varsayılan "openid email profile")
`OIDC_USERNAME_CLAIM` | Kullanıcı adını oluşturmak için kullanılan talep (isteğe bağlı, varsayılan "preferred_username")
`OIDC_PKCE` | PKCE kullanılıp kullanılmayacağı, bkz. [PKCE](#pkce) (isteğe bağlı, sağlayıcı destekliyorsa otomatik olarak etkinleştirilir)

### PKCE

Gramps Web API 3.23 itibarıyla, Gramps Web [PKCE](https://datatracker.ietf.org/doc/html/rfc7636) (Kod Değişimi için Kanıt Anahtarı, `S256` yöntemi) için yetkilendirme kodu akışını destekler. Pocket ID gibi bazı kimlik sağlayıcıları, bir istemci için PKCE'yi *zorunlu kılacak* şekilde yapılandırılabilir ve bunu kullanmayan oturum açmaları reddeder. Gramps Web API'nin daha eski sürümleri PKCE'yi hiç kullanmaz, bu nedenle böyle bir istemci ile oturum açma başarısız olur.

PKCE'nin kullanılıp kullanılmadığı, oturum açma sırasında şu şekilde belirlenir:

- `OIDC_PKCE` `True` olarak ayarlandığında, PKCE kullanılır.
- `OIDC_PKCE` `False` olarak ayarlandığında, sağlayıcı desteklese bile PKCE kullanılmaz.
- `OIDC_PKCE` ayarlanmadığında veya ayarlanmış ama boş olduğunda, sağlayıcının keşif belgesi (`/.well-known/openid-configuration`) `code_challenge_methods_supported` içinde `S256` listeliyorsa PKCE kullanılır, aksi takdirde kullanılmaz.

Çoğu kurulum için hiçbir şey ayarlamanıza gerek yoktur. Sağlayıcınız PKCE'yi gerektiriyorsa ancak keşif belgesinde `S256`'yı belirtmiyorsa `OIDC_PKCE`'yi `True` olarak ayarlayın, eğer sağlayıcınız `S256`'yı belirtip yanlış işliyorsa `False` olarak ayarlayın. Ortam değişkenleri olarak, boolean değerler küçük harfle olmalıdır (`GRAMPSWEB_OIDC_PKCE=true`), bkz. [Yapılandırma](configuration.md).

Yerleşik sağlayıcılar için karşılık gelen seçenekler `OIDC_GOOGLE_PKCE` ve `OIDC_MICROSOFT_PKCE`'dir.

PKCE kod doğrulayıcı, sağlayıcıya yönlendirme ile geri çağırma arasındaki kullanıcının oturumunda saklanır, bu nedenle yönlendirme URI'lerinde herhangi bir değişiklik gerektirmez.

### Çok Ağaçlı Kurulumlar

Çok ağaçlı bir sunucuda, kullanıcının oturum açtığı ağacın, Gramps Web'in kimlik sağlayıcısına yönlendirmeden önce bilinmesi gerekir, bu nedenle oturum açma şu şekilde başlar:

```
GET /api/oidc/login/?provider=<id>&tree=<tree_id>
```

`tree`, çok ağaçlı kurulumlarda gereklidir; bunu atlamak veya mevcut olmayan bir ağacın kimliğini geçmek, oturum açmayı başarısız kılar. Tek ağaçlı bir sunucuda `tree` isteğe bağlıdır, ancak verildiğinde yapılandırılmış `TREE` ile eşleşmelidir.

Bir OIDC kimliği, tam olarak bir Gramps Web hesabına bağlıdır ve bu hesap da tam olarak bir ağaca aittir – farklı bir ağaçta oturum açmak, hesabı taşımak yerine başarısız olur. Sağlayıcıda tek bir kimliği birden fazla ağaçtaki hesaplarla bağlamanın bir yolu yoktur; birden fazla ağaca erişim ihtiyacı olan kullanıcılar, sağlayıcıda ayrı kimliklere ihtiyaç duyar (örneğin, farklı kullanıcı adları veya hesaplar).

!!! warning
    İlişkili bir ağaç olmayan bir site yöneticisi hesabı (bkz. [yönetici hesabı oluşturma](../administration/owner.md)) OIDC üzerinden oturum açamaz, çünkü OIDC oturum açma her zaman bir ağaç gerektirir. Bu tür hesaplar, bunun yerine yerel kullanıcı adı/şifre ile oluşturulmalı ve kimlik doğrulaması yapılmalıdır.

## Gerekli Yönlendirme URI'leri

OIDC sağlayıcınızı yapılandırırken, aşağıdaki yönlendirme URI'sini kaydetmelisiniz:

**Wildcard'ları destekleyen OIDC sağlayıcıları için: (örneğin, Authentik)**

- `https://your-gramps-backend.com/api/oidc/callback/*`

Burada `*` bir regex wildcard'dır. Sağlayıcınızın regex yorumlayıcısına bağlı olarak bu aynı zamanda `.*` veya benzeri bir şey de olabilir. Sağlayıcınızın bunu gerektiriyorsa regex'in etkin olduğundan emin olun (örneğin, Authentik).

**Wildcard'ları desteklemeyen OIDC sağlayıcıları için: (örneğin, Authelia)**

- `https://your-gramps-backend.com/api/oidc/callback/custom`

Ağaç, yönlendirme URI'sinin bir parçası değildir, hatta çok ağaçlı sunucularda bile – oturum açma, oturumda ayrı olarak taşınır, çünkü sağlayıcılar yönlendirme URI'sinin tam olarak kaydedilen ile eşleşmesini gerektirir.

## Rol Eşleme

Gramps Web, kimlik sağlayıcınızdan OIDC gruplarını veya rollerini Gramps Web kullanıcı rollerine otomatik olarak eşleyebilir. Bu, kullanıcı izinlerini merkezi olarak kimlik sağlayıcınızda yönetmenizi sağlar. Rol eşleme, tüm sağlayıcılar için aynı şekilde çalışır, ister yerleşik ister özel olsun.

### Yapılandırma

Rol eşlemesini yapılandırmak için bu ayarları kullanın:

Anahtar | Açıklama
----|-------------
`OIDC_ROLE_CLAIM` | Kullanıcının gruplarını/rollerini içeren OIDC belirteçindeki talep adı. Varsayılan "groups". Noktalı yollar desteklenir, örneğin `realm_access.roles`.
`OIDC_GROUP_ADMIN` | Gramps "Yönetici" rolüne eşlenen OIDC sağlayıcınızdan grup/rol adı
`OIDC_GROUP_OWNER` | Gramps "Sahip" rolüne eşlenen OIDC sağlayıcınızdan grup/rol adı
`OIDC_GROUP_EDITOR` | Gramps "Editör" rolüne eşlenen OIDC sağlayıcınızdan grup/rol adı
`OIDC_GROUP_CONTRIBUTOR` | Gramps "Katkıda Bulunan" rolüne eşlenen OIDC sağlayıcınızdan grup/rol adı
`OIDC_GROUP_MEMBER` | Gramps "Üye" rolüne eşlenen OIDC sağlayıcınızdan grup/rol adı
`OIDC_GROUP_GUEST` | Gramps "Misafir" rolüne eşlenen OIDC sağlayıcınızdan grup/rol adı

### Rol Eşleme Davranışı

Hiçbir `OIDC_GROUP_*` ayarı yapılandırılmadığında, rol eşleme kapalıdır ve roller Gramps Web'de manuel olarak yönetilir; yeni OIDC hesapları devre dışı olarak oluşturulur ve mevcut bir sahip veya yönetici tarafından onaylanması gerekir (bkz. [İlk Oturum Açma ve Başlatma](#first-login-and-bootstrapping) aşağıda).

Rol eşleme yapılandırıldığında, her oturum açmada:

- Eğer rol talebi mevcutsa ve kullanıcı eşlenen bir gruba ait ise, karşılık gelen rolü alır.
- Eğer rol talebi mevcutsa ancak kullanıcı eşlenen hiçbir gruba ait değilse, rolü devre dışı olarak ayarlanır. Bu, bir hata değil, kapalı bir varsayılandır – Gramps Web, tanımadığı bir grup için bir rol çıkaramaz.
- Eğer rol talebi tamamen belirteçten yoksa, mevcut rol değişmeden bırakılır; yeni bir hesap yine de varsayılan olarak devre dışı kalır.

!!! warning "Google bir gruplar talebi göndermez"
    Google'ın belirteçleri asla `groups` talebini içermez, bu nedenle rol eşleme etkinleştirildiğinde, Google oturum açmaları yukarıdaki "talep yok" durumuna girer: mevcut kullanıcılar rollerini korur, ancak yeni Google kullanıcıları devre dışı olarak oluşturulur ve manuel onay gerektirir. Başka bir sağlayıcı için rol eşlemeyi etkinleştirmeden önce bunu aklınızda bulundurun – bu, mevcut Google kullanıcılarını otomatik olarak devre dışı bırakmaz.

Microsoft Entra, uygulama rollerini ve grup üyeliklerini yalnızca ID belirtecinde döndürür, kullanıcı bilgisi uç noktasından değil. Gramps Web, ID belirtecinin taleplerini kullanıcı bilgisi yanıtına birleştirir, böylece `OIDC_ROLE_CLAIM` diğer sağlayıcılar için olduğu gibi çalışır; her ikisi de bir talep içeriyorsa, kullanıcı bilgisi değeri önceliklidir.

## İlk Oturum Açma ve Başlatma

OIDC aracılığıyla oluşturulan yeni hesaplar, rol eşleme onlara bir rol atamadıkça devre dışı olarak başlar (bkz. yukarıda). Yepyeni bir örnekte kimse devre dışı bir hesabı onaylayamaz ve eğer `OIDC_DISABLE_LOCAL_AUTH` da etkinse, geri dönmek için bir şifre oturumu da yoktur.

!!! warning "İlk oturum açmadan önce bir sahip/yönetici grubunu yapılandırın"
    Kimse OIDC üzerinden ilk kez oturum açmadan önce, `OIDC_GROUP_OWNER` (veya `OIDC_GROUP_ADMIN`) ayarını yapın ve ilk kullanıcının sağlayıcıda o gruba ait olduğundan emin olun. Aksi takdirde, örnek OIDC üzerinden başlatılamaz.

## Hesaplar ve Kullanıcı Adları

OIDC aracılığıyla oluşturulan hesaplar, hesap oluşturma sırasında bir kez atanan ve sonraki oturum açmalarda asla değiştirilmeyen bir kullanıcı adı alır:

- Yerleşik sağlayıcılar: `<provider>_<claim value>`, örneğin `microsoft_alice@contoso.com`
- Özel sağlayıcı: yalnızca talep değeri, örneğin `alice`

Çakışma durumunda sayısal bir ek eklenir. OIDC ile oluşturulan bir hesabın kullanıcı adını daha sonra yeniden adlandırmanın bir yolu yoktur; tam ad ve e-posta adresi, aksine, her oturum açmada yenilenir.

Bir OIDC oturumu, e-posta adresini paylaşan mevcut bir yerel hesaba asla bağlanmaz – bu kasıtlıdır, çünkü hesapları e-posta ile bağlamak bir hesap ele geçirme vektörüdür. Zaten yerel bir hesabı olan bir kullanıcı, OIDC üzerinden ilk kez oturum açtığında ikinci, ayrı bir hesap alır, aksi takdirde önce sağlayıcıyı hesabıyla bağlamazsa.

Gramps Web API 3.24 itibarıyla, kullanıcılar OIDC kimliklerini mevcut hesaplarına bağlayabilir ve bunları listeleyip ayırabilirler, [Kullanıcı Ayarları > Bağlı oturum açma yöntemleri](../user-guide/settings.md#linked-sign-in-methods) altında. Bağlama, yakın zamanda yapılmış bir oturum açma gerektirir ve kullanıcının kendi belirteci ile onaylanır, bu nedenle ön uç API'den farklı bir kökene sahip olduğunda da çalışır. Bir kimlik yalnızca bir hesaba ait olabilir; zaten kendi hesabı olan bir kimliği bağlamak için, bir yönetici önce o hesabı silmelidir (düzenlemeleri kalır, ancak revizyon geçmişi artık adını göstermez). Son bağlı kimlik, yalnızca hesabın mevcut şifresi ile ayrılabilir ve `OIDC_DISABLE_LOCAL_AUTH` ayarlandığında hiç ayrılamaz.

Sağlayıcıdan gelen e-posta adresleri yalnızca sağlayıcı bunları doğrulanmış olarak işaretlerse (veya `email_verified` talebini tamamen atlarlarsa) saklanır; aksi takdirde oturum açma, bir e-posta adresi saklamadan devam eder. E-posta adreslerinin benzersiz olması gerekmediğinden (Gramps Web API 3.22 itibarıyla), başka bir hesap zaten kullanıyorsa bile bir adres saklanır.

## OIDC Oturum Kapatma

Gramps Web, OIDC sağlayıcıları için Tek Oturum Kapatma (SSO oturum kapatma) desteği sunar. `GET /api/oidc/logout/` sağlayıcının `end_session_endpoint`'ini arar ve yanıt olarak `logout_url` olarak döndürür; oturumun gerçekten kimlik sağlayıcısında sona ermesi için Gramps Web ön ucu tarayıcıyı oraya yönlendirir. `logout_url`, sağlayıcının `end_session_endpoint`'i yoksa `null` olur.

!!! warning "Oturum kapatma sırasında belirteçler iptal edilmez"
    Oturum kapatma yalnızca tarayıcı oturumunu sona erdirir; şu anda daha önce verilmiş bir Gramps Web belirtecini iptal etmenin bir yolu yoktur. Belirteçler, süresi dolana kadar geçerli kalır (`JWT_ACCESS_TOKEN_EXPIRES`, varsayılan 15 dakika erişim belirteçleri için), kullanıcı Gramps Web'de veya kimlik sağlayıcısında oturum kapatmış olsa bile.

## Sorun Giderme

Oturum açmanın durduğu noktadan başlayın ve dalı takip edin. Gramps Web, başarısız bir geri çağırma için nedeni kaydeder (sunucu günlüğünde `OIDC callback error for provider` arayın), bu genellikle tarayıcıda gösterilen mesajdan daha spesifiktir.

**1. Oturum açma düğmesi eksik mi?**

- `<BASE_URL>/api/oidc/config/` adresini kontrol edin. Eğer `enabled` `false` ise veya `providers` boşsa, OIDC yapılandırılmamıştır: `OIDC_ENABLED` `True` olmalıdır ve özel bir sağlayıcının hem `OIDC_ISSUER` hem de `OIDC_CLIENT_ID`'ye ihtiyacı vardır.
- Bir yerleşik sağlayıcı (Google, Microsoft) yalnızca hem istemci kimliği hem de istemci sırrı ayarlandığında kaydedilir.
- Sunucu günlüğünde başlangıçta `Keşif belgesi yüklenemedi` mesajını arayın. Bu, sunucunun `<issuer>/.well-known/openid-configuration` (veya `OIDC_OPENID_CONFIG_URL`) adresine ulaşamadığı anlamına gelir. İlk kullanımda yeniden dener, ancak Gramps Web konteynerinin verici URL'sini kendisinin çözebilmesi ve ulaşabilmesi gerekir, yalnızca tarayıcınızın değil.

**2. Tarayıcı, sağlayıcıya gönderildikten hemen sonra bir hata alıyor mu?**

Hata, oturum açmadan önce kimlik sağlayıcısı tarafından gösterilir.

- *"yönlendirme URI'si uyuşmazlığı"* (veya benzeri): sağlayıcıda kaydedilen yönlendirme URI'si tam olarak eşleşmelidir; şeması, ana bilgisayarı, bağlantı noktası ve sağlayıcı kimliği dahil. Bkz. [Gerekli Yönlendirme URI'leri](#required-redirect-uris). Bunun `BASE_URL`'den oluşturulduğunu unutmayın, bu nedenle yanlış bir `BASE_URL` yanlış bir yönlendirme URI'si verir.
- *Bir PKCE hatası* (örneğin `invalid_request`, "kod zorluğu gerekli" veya eksik bir `code_challenge` parametresi): sağlayıcı PKCE'yi gerektiriyor ancak Gramps Web bunu göndermedi. Aşağıdaki [PKCE dalına](#pkce-branch) gidin.

**3. Sağlayıcı oturumu kabul ediyor ancak Gramps Web sonra bir hata gösteriyor mu?**

- *`mismatching_state`, veya hata oturum veya durumdan bahsediyorsa*: tarayıcı, Gramps Web'in oturum açma başladığında ayarladığı oturum çerezini geri göndermedi. Bu çerez ayrıca PKCE kod doğrulayıcısını taşır. Tarayıcıdaki adresin `BASE_URL` ile eşleştiğinden (aynı şema ve ana bilgisayar) emin olun, ters proxy çerezleri ve orijinal ana bilgisayarı geçiriyor ve oturum açma aynı tarayıcı sekmesinde veya penceresinde başlatılıp tamamlanmalıdır.
- *`OIDC authentication failed for <provider>` (HTTP 401)*: temel nedeni görmek için sunucu günlüğünü kontrol edin. Yaygın nedenler yanlış bir istemci sırrı, belirteçlerin `iss` talebi ile eşleşmeyen bir verici URL'si ve sağlayıcının geri çağırmaya bir hata döndürmesidir (örneğin PKCE, aşağıya bakın).
- *Çok fazla deneme*: oturum açma ve geri çağırma uç noktaları oran sınırlıdır (dakikada 5 istek). Bir dakika bekleyin ve tekrar deneyin.

**4. Oturum açma başarılı ancak "Hesap İnceleniyor" görüyorsanız veya hiçbir şey yapamıyorsanız?**

Yeni hesaplar, rol eşleme bir rol atamadıkça devre dışı olarak oluşturulur. Bkz. [İlk Oturum Açma ve Başlatma](#first-login-and-bootstrapping) ve [Rol Eşleme Davranışı](#role-mapping-behavior). Bir yönetici ayrıca Hesaplar > Yönetici > Kullanıcıları Yönet altında hesabı etkinleştirebilir.

### PKCE dalı

Gramps Web, bir oturum açma başladığında PKCE'yi kullanıp kullanmamaya karar verir (bkz. [PKCE](#pkce)). Kurulumunuz için ne olduğunu öğrenmek için bu soruları sırayla yanıtlayın:

1. **`OIDC_PKCE` ayarlandı mı?** (Yerleşik sağlayıcılar için, `OIDC_GOOGLE_PKCE` veya `OIDC_MICROSOFT_PKCE`.)
    - `True`: PKCE kullanılır. 3. soruya geçin.
    - `False`: PKCE kasıtlı olarak kapalıdır ve sağlayıcının keşif belgesi göz ardı edilir. Sağlayıcınız PKCE'yi gerektiriyorsa, ayarı kaldırın veya `True` olarak ayarlayın.
    - Ayarlanmadı veya boş: 2. soruya devam edin.
2. **Keşif belgesi `S256` listeliyor mu?** `<issuer>/.well-known/openid-configuration` adresini açın ve `code_challenge_methods_supported` içinde `S256` arayın.
    - Evet: PKCE otomatik olarak kullanılır. 3. soruya devam edin.
    - Hayır veya alan eksik: PKCE **kullanılmıyor**. Sağlayıcınız bunu gerektiriyorsa `OIDC_PKCE`'yi `True` olarak ayarlayın. Ayrıca sunucu günlüğünde `Sağlayıcıdan PKCE desteği kontrol edilemedi` mesajını kontrol edin, bu, keşif belgesinin alınamadığı ve bu nedenle PKCE'nin kapalı kaldığı anlamına gelir.
3. **PKCE gerçekten gönderildi mi?** Bir oturum açma başlatın ve sağlayıcının oturum açma sayfasının adresine (veya tarayıcınızın ağ sekmesindeki ilk yönlendirmeye) bakın. `code_challenge=` ve `code_challenge_method=S256` içermelidir.
    - Mevcut, ancak oturum açma hala geri çağırmada başarısız oluyorsa: sağlayıcı kod doğrulayıcıyı reddetti. Yönlendirme ile geri çağırma arasında oturum çerezi kaybolmuş olabilir (yukarıdaki dal 3'e bakın), veya sağlayıcı `S256`'yı desteklemiyor, bu durumda sağlayıcı PKCE'yi gerektirmiyorsa `OIDC_PKCE`'yi `False` olarak ayarlayın.
    - Yok: yukarıdaki ayarlar uygulanmadı. Ortam değişkeninin doğru ön eki ve küçük harfli bir değere sahip olduğundan emin olun (örneğin, Docker'da `GRAMPSWEB_OIDC_PKCE=true`; `True` boolean olarak okunmaz), sunucuyu yeniden başlatın ve yapılandırmayı tekrar kontrol edin.

!!! note
    Sağlayıcıda PKCE *isteğe bağlı* olarak etkinleştirildiğinde veya hiç etkinleştirilmediğinde, Gramps Web'in bir zorluk gönderip göndermediğine bakılmaksızın oturum açmalar çalışır. Sadece PKCE'yi *zorunlu* kılacak şekilde yapılandırılmış sağlayıcılar (veya istemciler) bu ayarın önemli olmasını sağlar.

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
OIDC_DISABLE_LOCAL_AUTH=True  # İsteğe bağlı: kullanıcı adı/şifre oturum açmayı devre dışı bırak

# İsteğe bağlı: OIDC gruplarından Gramps rollerine rol eşleme
OIDC_ROLE_CLAIM="groups"  # veya sağlayıcınıza bağlı olarak "roles"
OIDC_GROUP_ADMIN="gramps-admins"
OIDC_GROUP_EDITOR="gramps-editors"
OIDC_GROUP_MEMBER="gramps-members"

EMAIL_HOST="mail.example.com"
EMAIL_PORT=465
EMAIL_USE_SSL=True  # 465 numaralı port için örtük SSL kullan
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

### Pocket ID

Pocket ID'de `<BASE_URL>/api/oidc/callback/custom` yönlendirme URI'si ile bir OIDC istemcisi oluşturun (bkz. [Gerekli Yönlendirme URI'leri](#required-redirect-uris)). İstemci için "PKCE'yi Zorunlu Kıl" seçeneğini etkinleştirirseniz, ek bir Gramps Web yapılandırmasına gerek yoktur, çünkü Pocket ID keşif belgesinde PKCE desteğini belirtir. Ardından yapılandırın:

```
GRAMPSWEB_OIDC_ENABLED=True
GRAMPSWEB_OIDC_ISSUER=https://id.example.com
GRAMPSWEB_OIDC_CLIENT_ID=<client id>
GRAMPSWEB_OIDC_CLIENT_SECRET=<client secret>
GRAMPSWEB_OIDC_NAME=Pocket ID
```

### Authelia

Gramps Web için topluluk tarafından hazırlanmış bir OIDC kurulum kılavuzu [resmi Authelia belgeleri web sitesinde](https://www.authelia.com/integration/openid-connect/clients/gramps/) mevcuttur.

### Keycloak

Keycloak için yapılandırmanın çoğu varsayılan olarak bırakılabilir (*İstemci → İstemci oluştur → İstemci kimlik doğrulaması AÇIK*).
Birkaç istisna vardır:

1. **OpenID kapsamı** – `openid` kapsamı, tüm Keycloak sürümlerinde varsayılan olarak dahil edilmez. Sorun yaşamamak için manuel olarak ekleyin: *İstemci → [Gramps istemcisi] → İstemci kapsamları → Kapsam ekle → Ad: `openid` → Varsayılan olarak ayarla.*
2. **Roller** – Roller, ya istemci düzeyinde ya da realm başına küresel olarak atanabilir.

    * İstemci rollerini kullanıyorsanız, `OIDC_ROLE_CLAIM` yapılandırma seçeneğini şu şekilde ayarlayın: `resource_access.[gramps-client-name].roles`
    * Roller Gramps'a görünür hale getirmek için *İstemci Kapsamları* (belirli istemci altında değil, üst düzey bölüm) kısmına gidin, ardından: *Roller → Haritalayıcılar → istemci rolleri → Kullanıcı bilgisine ekle → AÇIK.*
