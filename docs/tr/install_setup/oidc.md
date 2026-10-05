# OIDC Kimlik Doğrulama

Gramps Web, kullanıcıların harici kimlik sağlayıcılarını kullanarak giriş yapmalarına olanak tanıyan OpenID Connect (OIDC) kimlik doğrulamasını destekler. Bu, yerleşik sağlayıcılar olan Google ve Microsoft'un yanı sıra Keycloak, Authentik ve Authelia gibi özel OIDC sağlayıcılarını da içerir.

!!! warning "GitHub, OIDC sağlayıcısı olarak artık desteklenmiyor"
    Eğer daha önceki bir sürümden `OIDC_GITHUB_CLIENT_ID` / `OIDC_GITHUB_CLIENT_SECRET` ayarlarını yaptıysanız, bunları kaldırın – artık göz ardı ediliyor ve daha önce GitHub aracılığıyla giriş yapan kullanıcılar bu şekilde giriş yapamaz. GitHub, bir OAuth 2.0 sağlayıcısıdır, OpenID Connect sağlayıcısı değildir ve Gramps Web'in kimlik için güvendiği talebi asla döndürmediği için tam olarak güvenilir olmamıştır.

## Genel Bakış

OIDC kimlik doğrulaması, şunları yapmanıza olanak tanır:

- Kullanıcı kimlik doğrulaması için harici kimlik sağlayıcıları kullanma
- Aynı anda birden fazla kimlik doğrulama sağlayıcısını destekleme
- OIDC gruplarını/rollerini Gramps Web kullanıcı rollerine eşleme
- Tek Oturum Açma (SSO) ve Tek Oturum Kapatma uygulama
- İsteğe bağlı olarak yerel kullanıcı adı/parola kimlik doğrulamasını devre dışı bırakma

## Yapılandırma

OIDC kimlik doğrulamasını etkinleştirmek için, Gramps Web yapılandırma dosyanızda veya ortam değişkenlerinde uygun ayarları yapılandırmanız gerekir. Mevcut OIDC ayarlarının tam listesi için [Sunucu Yapılandırması](configuration.md#settings-for-oidc-authentication) sayfasına bakın.

!!! info
    Ortam değişkenlerini kullanırken, her ayar adını `GRAMPSWEB_` ile ön eklemeyi unutmayın (örneğin, `GRAMPSWEB_OIDC_ENABLED`). Ayrıntılar için [Yapılandırma dosyası vs. ortam değişkenleri](configuration.md#configuration-file-vs-environment-variables) sayfasına bakın.

### Yerleşik Sağlayıcılar

Gramps Web, popüler kimlik sağlayıcıları için yerleşik destek sunar. Bunları kullanmak için yalnızca istemci kimliğini ve istemci gizli anahtarını sağlamanız gerekir:

- **Google**: `OIDC_GOOGLE_CLIENT_ID` ve `OIDC_GOOGLE_CLIENT_SECRET`
- **Microsoft**: `OIDC_MICROSOFT_CLIENT_ID` ve `OIDC_MICROSOFT_CLIENT_SECRET`

Birden fazla sağlayıcıyı aynı anda yapılandırabilirsiniz. Sistem, yapılandırma değerlerine dayanarak hangi sağlayıcıların mevcut olduğunu otomatik olarak algılayacaktır.

!!! tip "Microsoft: tek kiracı dağıtımları"
    Yerleşik Microsoft sağlayıcısı, çok kiracılı `/common` uç noktasını kullanır ve tasarımı gereği herhangi bir Microsoft hesabından girişleri kabul eder. Sadece kendi kiracınızdaki kullanıcıların giriş yapmasına izin vermek istiyorsanız, bunun yerine kiracıya özgü sağlayıcı URL'si ile [özel OIDC sağlayıcısını](#custom-oidc-providers) kullanın; bu, sağlayıcı doğrulamasını aktif tutar ve girişleri o kiracı ile sınırlar.

### Özel OIDC Sağlayıcıları

Özel OIDC sağlayıcıları (Keycloak, Authentik, Authelia veya tek kiracı Microsoft Entra kiracısı gibi) için bu ayarları kullanın:

Anahtar | Açıklama
----|-------------
`OIDC_ENABLED` | OIDC kimlik doğrulamasını etkinleştirip etkinleştirmeyeceğini belirten Boolean. `True` olarak ayarlayın.
`OIDC_ISSUER` | Sağlayıcınızın verici URL'si. Keşif, `<issuer>/.well-known/openid-configuration` adresinden alınır.
`OIDC_CLIENT_ID` | OIDC sağlayıcınız için istemci kimliği
`OIDC_CLIENT_SECRET` | OIDC sağlayıcınız için istemci gizli anahtarı
`OIDC_NAME` | Özel görüntü adı (isteğe bağlı, varsayılan "OIDC")
`OIDC_SCOPES` | OAuth kapsamları (isteğe bağlı, varsayılan "openid email profile")
`OIDC_USERNAME_CLAIM` | Kullanıcı adını oluşturmak için kullanılan talep (isteğe bağlı, varsayılan "preferred_username")
`OIDC_PKCE` | PKCE kullanılıp kullanılmayacağını belirtir, bkz. [PKCE](#pkce) (isteğe bağlı, sağlayıcı bunu destekliyorsa otomatik olarak etkinleştirilir)

### PKCE

Gramps Web API 3.23 itibarıyla, Gramps Web [PKCE](https://datatracker.ietf.org/doc/html/rfc7636) (Kod Değişimi için Kanıt Anahtarı, `S256` yöntemi) için yetkilendirme kodu akışını destekler. Pocket ID gibi bazı kimlik sağlayıcıları, bir istemci için PKCE'yi *gerektirecek* şekilde yapılandırılabilir ve bunu kullanmayan girişleri reddeder. Gramps Web API'nin daha eski sürümleri asla PKCE kullanmaz, bu nedenle böyle bir istemci ile girişler başarısız olur.

PKCE'nin kullanılıp kullanılmadığı, giriş sırasında şu şekilde belirlenir:

- `OIDC_PKCE` `True` olarak ayarlandığında, PKCE kullanılır.
- `OIDC_PKCE` `False` olarak ayarlandığında, PKCE kullanılmaz, sağlayıcı bunu desteklese bile.
- `OIDC_PKCE` ayarlanmamışsa veya ayarlanmış ama boşsa, PKCE, sağlayıcının keşif belgesinde (`/.well-known/openid-configuration`) `code_challenge_methods_supported` içinde `S256` listeleniyorsa kullanılır, aksi takdirde kullanılmaz.

Çoğu kurulum için hiçbir şey ayarlamanıza gerek yoktur. Sağlayıcınız PKCE'yi gerektiriyorsa ancak keşif belgesinde `S256`'yı belirtmiyorsa `OIDC_PKCE`'yi `True` olarak ayarlayın, eğer sağlayıcınız `S256`'yı belirtip yanlış yönetiyorsa `False` olarak ayarlayın. Ortam değişkenleri olarak, boolean değerler küçük harfle yazılmalıdır (`GRAMPSWEB_OIDC_PKCE=true`), bkz. [Yapılandırma](configuration.md).

Yerleşik sağlayıcılar için karşılık gelen seçenekler `OIDC_GOOGLE_PKCE` ve `OIDC_MICROSOFT_PKCE`'dir.

PKCE kod doğrulayıcısı, sağlayıcıya yönlendirme ile geri çağırma arasındaki kullanıcının oturumunda saklanır, bu nedenle yönlendirme URI'lerinde herhangi bir değişiklik gerektirmez.

### Çoklu Ağaç Kurulumları

Çoklu ağaç sunucusunda, kullanıcının giriş yaptığı ağacın, Gramps Web'in kimlik sağlayıcısına yönlendirmeden önce bilinmesi gerekir, bu nedenle giriş şu şekilde başlar:

```
GET /api/oidc/login/?provider=<id>&tree=<tree_id>
```

`tree`, çoklu ağaç kurulumlarında gereklidir; bunu atlamak veya mevcut olmayan bir ağacın kimliğini vermek, girişi başarısız kılar. Tek ağaç sunucusunda `tree` isteğe bağlıdır, ancak verildiğinde yapılandırılmış `TREE` ile eşleşmelidir.

Bir OIDC kimliği tam olarak bir Gramps Web hesabına bağlıdır, bu hesap da tam olarak bir ağaca aittir – farklı bir ağaç üzerinde giriş yapmak, hesabı taşımak yerine başarısız olur. Sağlayıcıda tek bir kimliği birden fazla ağaçtaki hesaplarla bağlamanın bir yolu yoktur; birden fazla ağaca erişim ihtiyacı olan kullanıcılar, sağlayıcıda ayrı kimliklere ihtiyaç duyar (örneğin, farklı kullanıcı adları veya hesaplar).

!!! warning
    İlişkili bir ağaç olmayan bir site yöneticisi hesabı (bkz. [yönetici hesabı oluşturma](../administration/owner.md)) OIDC aracılığıyla giriş yapamaz, çünkü OIDC girişi her zaman bir ağaç gerektirir. Bu tür hesaplar, bunun yerine yerel kullanıcı adı/parola ile oluşturulmalı ve kimlik doğrulaması yapılmalıdır.

## Gerekli Yönlendirme URI'leri

OIDC sağlayıcınızı yapılandırırken, aşağıdaki yönlendirme URI'sini kaydetmelisiniz:

**Wildcard'ları destekleyen OIDC sağlayıcıları için: (örneğin, Authentik)**

- `https://your-gramps-backend.com/api/oidc/callback/*`

Burada `*` bir regex wildcard'dır. Sağlayıcınızın regex yorumlayıcısına bağlı olarak bu aynı zamanda `.*` veya benzeri de olabilir. Sağlayıcınız bunu gerektiriyorsa regex'in etkin olduğundan emin olun (örneğin, Authentik).

**Wildcard'ları desteklemeyen OIDC sağlayıcıları için: (örneğin, Authelia)**

- `https://your-gramps-backend.com/api/oidc/callback/custom`

Ağaç, yönlendirme URI'sinin bir parçası değildir, çoklu ağaç sunucularında bile – bu, oturumda ayrı olarak taşınır, çünkü sağlayıcılar yönlendirme URI'sinin kaydedilen ile tam olarak eşleşmesini gerektirir.

## Rol Eşleme

Gramps Web, kimlik sağlayıcınızdan OIDC gruplarını veya rollerini Gramps Web kullanıcı rollerine otomatik olarak eşleyebilir. Bu, kullanıcı izinlerini merkezi olarak kimlik sağlayıcınızda yönetmenizi sağlar. Rol eşleme, tüm sağlayıcılar için, yerleşik veya özel, aynı şekilde çalışır.

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

Hiçbir `OIDC_GROUP_*` ayarı yapılandırılmamışsa, rol eşleme kapalıdır ve roller Gramps Web'de manuel olarak yönetilir; yeni OIDC hesapları bu durumda devre dışı olarak oluşturulur ve mevcut bir sahip veya yöneticinin onayını gerektirir (bkz. [İlk Giriş ve Başlatma](#first-login-and-bootstrapping) aşağıda).

Rol eşleme yapılandırıldıktan sonra, her girişte:

- Eğer rol talebi mevcutsa ve kullanıcı eşlenmiş bir gruba ait ise, ilgili rol verilir.
- Eğer rol talebi mevcutsa ancak kullanıcı eşlenmiş bir gruba ait değilse, rolü devre dışı olarak ayarlanır. Bu, tanımsız bir varsayılandır, bir hata değildir – Gramps Web, tanımadığı bir grup için rol çıkaramaz.
- Eğer rol talebi jetondan tamamen yoksa, mevcut rol değiştirilmez; yeni bir hesap yine devre dışı olarak varsayılan olarak oluşturulur.

!!! warning "Google, grup talebi göndermez"
    Google'ın jetonları asla `groups` talebini içermez, bu nedenle rol eşleme etkinleştirildiğinde, Google girişleri yukarıdaki "talep yok" durumuna girer: mevcut kullanıcılar rollerini korur, ancak yeni Google kullanıcıları devre dışı olarak oluşturulur ve manuel onay gerektirir. Başka bir sağlayıcı için rol eşlemeyi yalnızca etkinleştirmeden önce bunu göz önünde bulundurun – bu, mevcut Google kullanıcılarını kendi başına devre dışı bırakmaz.

Microsoft Entra, uygulama rollerini ve grup üyeliklerini yalnızca ID jetonunda döndürür, kullanıcı bilgisi uç noktasından değil. Gramps Web, ID jetonunun taleplerini kullanıcı bilgisi yanıtına birleştirir, böylece `OIDC_ROLE_CLAIM` diğer sağlayıcılar için olduğu gibi çalışır; her ikisi de bir talep içeriyorsa, kullanıcı bilgisi değeri öncelik alır.

## İlk Giriş ve Başlatma

OIDC aracılığıyla oluşturulan yeni hesaplar, rol eşleme bir rol atamadığı sürece devre dışı olarak başlar (bkz. yukarıda). Yepyeni bir örnekte kimse devre dışı bir hesabı onaylayamaz ve `OIDC_DISABLE_LOCAL_AUTH` da etkinse, geri dönmek için bir parola girişi de yoktur.

!!! warning "İlk girişten önce bir sahip/yönetici grubu yapılandırın"
    Hiç kimse OIDC aracılığıyla ilk kez giriş yapmadan önce, `OIDC_GROUP_OWNER` (veya `OIDC_GROUP_ADMIN`) ayarını yapın ve ilk kullanıcının sağlayıcıda o gruba ait olduğundan emin olun. Aksi takdirde, örnek OIDC aracılığıyla başlatılamaz.

## Hesaplar ve Kullanıcı Adları

OIDC aracılığıyla oluşturulan hesaplar, hesap oluşturma sırasında bir kez atanan ve daha sonraki girişlerde asla değiştirilmeyen bir kullanıcı adı alır:

- Yerleşik sağlayıcılar: `<provider>_<claim value>`, örneğin `microsoft_alice@contoso.com`
- Özel sağlayıcı: çıplak talep değeri, örneğin `alice`

Çakışma durumunda sayısal bir ek eklenir. OIDC ile oluşturulan bir hesabın kullanıcı adını daha sonra yeniden adlandırmanın bir yolu yoktur; tam ad ve e-posta adresi, bunun aksine her girişte yenilenir.

Bir OIDC girişi, e-posta adresini paylaşan mevcut bir yerel hesaba asla bağlanmaz – bu kasıtlıdır, çünkü hesapları e-posta ile bağlamak bir hesap ele geçirme vektörüdür. Zaten yerel bir hesabı olan bir kullanıcı, OIDC aracılığıyla ilk kez giriş yaptığında ikinci, ayrı bir hesap alır.

Sağlayıcıdan gelen e-posta adresleri yalnızca sağlayıcı bunları doğrulanmış olarak işaretlerse (veya `email_verified` talebini tamamen atlarlarsa) saklanır; aksi takdirde giriş, bir e-posta adresi saklamadan devam eder. E-posta adreslerinin benzersiz olması gerekmediğinden (Gramps Web API 3.22'den beri), başka bir hesap zaten kullanıyorsa bile bir adres saklanır.

## OIDC Çıkışı

Gramps Web, OIDC sağlayıcıları için Tek Oturum Kapatma (SSO çıkışı) destekler. `GET /api/oidc/logout/` sağlayıcının `end_session_endpoint`'ini arar ve yanıt olarak `logout_url` olarak döndürür; oturumu kimlik sağlayıcısında gerçekten sonlandırmak için tarayıcıyı oraya yönlendiren Gramps Web ön yüzüdür. Sağlayıcının `end_session_endpoint`'i yoksa `logout_url` `null` olur.

!!! warning "Çıkışta jetonlar iptal edilmez"
    Çıkış yapmak yalnızca tarayıcı oturumunu sonlandırır; şu anda daha önce verilmiş bir Gramps Web jetonunu iptal etmenin bir yolu yoktur. Jetonlar, süresi dolana kadar geçerli kalır (`JWT_ACCESS_TOKEN_EXPIRES`, erişim jetonları için varsayılan 15 dakika), kullanıcı Gramps Web'de veya kimlik sağlayıcısında çıkış yapmış olsa bile.

## Sorun Giderme

Girişin durduğu noktadan başlayın ve dalı takip edin. Gramps Web, başarısız bir geri çağırmanın nedenini kaydeder (sunucu günlüğünde `OIDC callback error for provider` ifadesini arayın), bu genellikle tarayıcıda gösterilen mesajdan daha spesifiktir.

**1. Giriş düğmesi eksik mi?**

- `<BASE_URL>/api/oidc/config/` adresini kontrol edin. Eğer `enabled` `false` ise veya `providers` boşsa, OIDC yapılandırılmamıştır: `OIDC_ENABLED` `True` olmalıdır ve özel bir sağlayıcı için hem `OIDC_ISSUER` hem de `OIDC_CLIENT_ID` ayarlanmalıdır.
- Yerleşik bir sağlayıcı (Google, Microsoft) yalnızca hem istemci kimliği hem de istemci gizli anahtarı ayarlandığında kaydedilir.
- Sunucu günlüğünde başlangıçta `Could not load discovery document` ifadesini arayın. Bu, sunucunun `<issuer>/.well-known/openid-configuration` (veya `OIDC_OPENID_CONFIG_URL`) adresine ulaşamadığı anlamına gelir. İlk kullanımda yeniden dener, ancak Gramps Web konteynerinin kendisinin verici URL'sini çözebilmesi ve ulaşabilmesi gerekir, yalnızca tarayıcınız değil.

**2. Tarayıcı, sağlayıcıya yönlendirildikten hemen sonra bir hata alıyor mu?**

Hata, giriş yapmadan önce kimlik sağlayıcısı tarafından gösterilir.

- *"yönlendirme URI'si uyuşmazlığı"* (veya benzeri): sağlayıcıda kaydedilen yönlendirme URI'si tam olarak eşleşmelidir, şeması, ana bilgisayarı, bağlantı noktası ve sağlayıcı kimliği dahil. Bkz. [Gerekli Yönlendirme URI'leri](#required-redirect-uris). Bunun `BASE_URL`'dan oluşturulduğunu unutmayın, bu nedenle yanlış bir `BASE_URL` yanlış bir yönlendirme URI'si verir.
- *Bir PKCE hatası* (örneğin `invalid_request`, "kod zorluğu gerekli" veya eksik bir `code_challenge` parametresi): sağlayıcı PKCE'yi gerektiriyor ancak Gramps Web bunu göndermedi. Aşağıdaki [PKCE dalına](#pkce-branch) gidin.

**3. Sağlayıcı girişi kabul ediyor ama Gramps Web ardından bir hata gösteriyor mu?**

- *`mismatching_state`, veya hata oturum veya durumdan bahsediyorsa*: tarayıcı, giriş başladığında Gramps Web'in ayarladığı oturum çerezini geri göndermedi. Bu çerez ayrıca PKCE kod doğrulayıcısını taşır. Tarayıcıdaki adresin `BASE_URL` ile eşleştiğinden (aynı şema ve ana bilgisayar), ters proxy'nin çerezleri ve orijinal ana bilgisayarı geçirdiğinden ve girişin aynı tarayıcı sekmesinde veya penceresinde başlatılıp tamamlandığından emin olun.
- *`OIDC authentication failed for <provider>` (HTTP 401)*: altta yatan nedeni görmek için sunucu günlüğünü kontrol edin. Yaygın nedenler yanlış bir istemci gizli anahtarı, jetonların `iss` talebiyle eşleşmeyen bir verici URL'si ve sağlayıcının geri çağırmaya bir hata döndürmesidir (örneğin PKCE, aşağıya bakın).
- *Çok fazla deneme*: giriş ve geri çağırma uç noktaları hız sınırlıdır (dakikada 5 istek). Bir dakika bekleyin ve tekrar deneyin.

**4. Giriş başarılı ama "Hesap İnceleniyor" mesajını mı görüyorsunuz, yoksa hiçbir şey yapamıyor musunuz?**

Yeni hesaplar, rol eşleme bir rol atamadığı sürece devre dışı olarak oluşturulur. Bkz. [İlk Giriş ve Başlatma](#first-login-and-bootstrapping) ve [Rol Eşleme Davranışı](#role-mapping-behavior). Bir yönetici ayrıca hesabı Ayarlar > Yönetim > Kullanıcıları Yönet bölümünden etkinleştirebilir.

### PKCE dalı

Gramps Web, bir giriş başladığında PKCE kullanılıp kullanılmayacağına karar verir (bkz. [PKCE](#pkce)). Kurulumunuz için ne olduğunu öğrenmek için bu soruları sırayla yanıtlayın:

1. **`OIDC_PKCE` ayarlandı mı?** (Yerleşik sağlayıcılar için, `OIDC_GOOGLE_PKCE` veya `OIDC_MICROSOFT_PKCE`.)
    - `True`: PKCE kullanılır. Soru 3'e geçin.
    - `False`: PKCE kasıtlı olarak kapalıdır ve sağlayıcının keşif belgesi göz ardı edilir. Sağlayıcınız PKCE'yi gerektiriyorsa, ayarı kaldırın veya `True` olarak ayarlayın.
    - Ayarlanmamış veya boş: soru 2 ile devam edin.
2. **Keşif belgesi `S256` listeliyor mu?** `<issuer>/.well-known/openid-configuration` adresini açın ve `code_challenge_methods_supported` içinde `S256` arayın.
    - Evet: PKCE otomatik olarak kullanılır. Soru 3 ile devam edin.
    - Hayır veya alan eksik: PKCE **kullanılmıyor**. Sağlayıcınız bunu gerektiriyorsa `OIDC_PKCE`'yi `True` olarak ayarlayın. Ayrıca sunucu günlüğünde `Could not check the provider for PKCE support` ifadesini kontrol edin, bu, keşif belgesinin alınamadığı ve bu nedenle PKCE'nin kapalı kaldığı anlamına gelir.
3. **PKCE gerçekten gönderildi mi?** Bir girişi başlatın ve sağlayıcının giriş sayfasının adresine (veya tarayıcınızın ağ sekmesindeki ilk yönlendirmeye) bakın. `code_challenge=` ve `code_challenge_method=S256` içermelidir.
    - Mevcut, ancak giriş hala geri çağırmada başarısız oluyorsa: sağlayıcı kod doğrulayıcıyı reddetti. Yönlendirme ile geri çağırma arasında oturum çerezi kaybolmuş olabilir (yukarıdaki dal 3'e bakın), veya sağlayıcı `S256`'yı desteklemiyorsa, bu durumda sağlayıcı PKCE'yi gerektirmiyorsa `OIDC_PKCE`'yi `False` olarak ayarlayın.
    - Yok: yukarıdaki ayarlar uygulanmamış. Ortam değişkeninin doğru öneki ve küçük harfli bir değeri olduğundan emin olun (örneğin `GRAMPSWEB_OIDC_PKCE=true` Docker'da; `True` bir boolean olarak okunmaz), sunucuyu yeniden başlatın ve yapılandırmayı tekrar kontrol edin.

!!! note
    Sağlayıcıda PKCE *isteğe bağlı* olarak etkinleştirildiğinde veya hiç etkinleştirilmediğinde, Gramps Web bir zorluk gönderip göndermediğine bakılmaksızın girişler çalışır. Sadece PKCE'yi *gerektiren* yapılandırılmış sağlayıcılar (veya istemciler) bu ayarın önemli olmasını sağlar.

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
OIDC_DISABLE_LOCAL_AUTH=True  # İsteğe bağlı: kullanıcı adı/parola girişini devre dışı bırak

# İsteğe bağlı: OIDC gruplarından Gramps rollerine rol eşleme
OIDC_ROLE_CLAIM="groups"  # veya sağlayıcınıza bağlı olarak "roles"
OIDC_GROUP_ADMIN="gramps-admins"
OIDC_GROUP_EDITOR="gramps-editors"
OIDC_GROUP_MEMBER="gramps-members"

EMAIL_HOST="mail.example.com"
EMAIL_PORT=465
EMAIL_USE_SSL=True  # 465 numaralı bağlantı noktası için örtük SSL kullan
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

Pocket ID'de `<BASE_URL>/api/oidc/callback/custom` yönlendirme URI'si ile bir OIDC istemcisi oluşturun (bkz. [Gerekli Yönlendirme URI'leri](#required-redirect-uris)). İstemci için "PKCE'yi Gerektir" seçeneğini etkinleştirirseniz, ek bir Gramps Web yapılandırması gerekmez, çünkü Pocket ID keşif belgesinde PKCE desteğini belirtir. Ardından yapılandırın:

```
GRAMPSWEB_OIDC_ENABLED=True
GRAMPSWEB_OIDC_ISSUER=https://id.example.com
GRAMPSWEB_OIDC_CLIENT_ID=<client id>
GRAMPSWEB_OIDC_CLIENT_SECRET=<client secret>
GRAMPSWEB_OIDC_NAME=Pocket ID
```

### Authelia

Gramps Web için topluluk tarafından yapılmış bir OIDC kurulum kılavuzu, [resmi Authelia belgeleri web sitesinde](https://www.authelia.com/integration/openid-connect/clients/gramps/) mevcuttur.

### Keycloak

Keycloak için yapılandırmanın çoğu varsayılan ayarlarında bırakılabilir (*İstemci → İstemci oluştur → İstemci kimlik doğrulaması AÇIK*).
Birkaç istisna vardır:

1. **OpenID kapsamı** – `openid` kapsamı, tüm Keycloak sürümlerinde varsayılan olarak dahil edilmez. Sorun yaşamamak için bunu manuel olarak ekleyin: *İstemci → [Gramps istemcisi] → İstemci kapsamları → Kapsam ekle → Ad: `openid` → Varsayılan olarak ayarla.*
2. **Roller** – Roller, ya istemci düzeyinde ya da realm başına küresel olarak atanabilir.

    * İstemci rollerini kullanıyorsanız, `OIDC_ROLE_CLAIM` yapılandırma seçeneğini şu şekilde ayarlayın: `resource_access.[gramps-client-name].roles`
    * Roller Gramps'a görünür hale getirmek için *İstemci Kapsamları* (belirli istemcinin altında değil, üst düzey bölüm) bölümüne gidin, ardından: *Roller → Mapperlar → istemci rolleri → Kullanıcı bilgisine ekle → AÇIK.*
