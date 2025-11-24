# OIDC Kimlik Doğrulaması

Gramps Web, kullanıcıların dış kimlik sağlayıcıları kullanarak oturum açmalarına olanak tanıyan OpenID Connect (OIDC) kimlik doğrulamasını destekler. Bu, Google, Microsoft ve GitHub gibi popüler sağlayıcıların yanı sıra Keycloak, Authentik ve diğer özel OIDC sağlayıcılarını da içerir.

## Genel Bakış

OIDC kimlik doğrulaması ile şunları yapabilirsiniz:

- Kullanıcı kimlik doğrulaması için dış kimlik sağlayıcılarını kullanın
- Aynı anda birden fazla kimlik doğrulama sağlayıcısını destekleyin
- OIDC gruplarını/rollerini Gramps Web kullanıcı rollerine eşleyin
- Tek Oturum Açma (SSO) ve Tek Oturum Kapatma uygulayın
- İsteğe bağlı olarak yerel kullanıcı adı/parola kimlik doğrulamasını devre dışı bırakın

## Yapılandırma

OIDC kimlik doğrulamasını etkinleştirmek için Gramps Web yapılandırma dosyanızda veya ortam değişkenlerinizde uygun ayarları yapılandırmanız gerekir. Mevcut OIDC ayarlarının tam listesi için [Sunucu Yapılandırması](configuration.md#settings-for-oidc-authentication) sayfasına bakın.

!!! info
    Ortam değişkenlerini kullanırken, her ayar adını `GRAMPSWEB_` ile ön eklemeyi unutmayın (örneğin, `GRAMPSWEB_OIDC_ENABLED`). Ayrıntılar için [Yapılandırma dosyası vs. ortam değişkenleri](configuration.md#configuration-file-vs-environment-variables) sayfasına bakın.

### Yerleşik Sağlayıcılar

Gramps Web, popüler kimlik sağlayıcıları için yerleşik destek sunar. Bunları kullanmak için yalnızca istemci kimliği ve istemci sırrını sağlamanız yeterlidir:

- **Google**: `OIDC_GOOGLE_CLIENT_ID` ve `OIDC_GOOGLE_CLIENT_SECRET`
- **Microsoft**: `OIDC_MICROSOFT_CLIENT_ID` ve `OIDC_MICROSOFT_CLIENT_SECRET`
- **GitHub**: `OIDC_GITHUB_CLIENT_ID` ve `OIDC_GITHUB_CLIENT_SECRET`

Birden fazla sağlayıcıyı aynı anda yapılandırabilirsiniz. Sistem, yapılandırma değerlerine göre hangi sağlayıcıların mevcut olduğunu otomatik olarak algılayacaktır.

### Özel OIDC Sağlayıcıları

Özel OIDC sağlayıcıları (Keycloak, Authentik veya herhangi bir standart OIDC uyumlu sağlayıcı gibi) için bu ayarları kullanın:

Anahtar | Açıklama
----|-------------
`OIDC_ENABLED` | OIDC kimlik doğrulamasını etkinleştirip etkinleştirmeyeceğinizi belirten Boolean. `True` olarak ayarlayın.
`OIDC_ISSUER` | Sağlayıcınızın verici URL'si
`OIDC_CLIENT_ID` | OIDC sağlayıcınız için istemci kimliği
`OIDC_CLIENT_SECRET` | OIDC sağlayıcınız için istemci sırrı
`OIDC_NAME` | Özel görüntü adı (isteğe bağlı, varsayılan "OIDC"dır)
`OIDC_SCOPES` | OAuth kapsamları (isteğe bağlı, varsayılan "openid email profile"dır)

## Gerekli Yönlendirme URI'leri

OIDC sağlayıcınızı yapılandırırken, aşağıdaki yönlendirme URI'sini kaydetmelisiniz:

**Wildcard'ları destekleyen OIDC sağlayıcıları için: (örneğin, Authentik)**

- `https://your-gramps-backend.com/api/oidc/callback/*`

Burada `*` bir regex wildcard'dır. Sağlayıcınızın regex yorumlayıcısına bağlı olarak bu aynı zamanda `.*` veya benzeri olabilir.
Eğer sağlayıcınız bunu gerektiriyorsa regex'in etkin olduğundan emin olun (örneğin, Authentik).

**Wildcard'ları desteklemeyen OIDC sağlayıcıları için: (örneğin, Authelia)**

- `https://your-gramps-backend.com/api/oidc/callback/?provider=custom`

## Rol Eşleme

Gramps Web, kimlik sağlayıcınızdan OIDC gruplarını veya rollerini Gramps Web kullanıcı rollerine otomatik olarak eşleyebilir. Bu, kullanıcı izinlerini merkezi olarak kimlik sağlayıcınızda yönetmenizi sağlar.

### Yapılandırma

Rol eşlemesini yapılandırmak için bu ayarları kullanın:

Anahtar | Açıklama
----|-------------
`OIDC_ROLE_CLAIM` | Kullanıcının gruplarını/rollerini içeren OIDC token'ındaki talep adı. Varsayılan "groups"
`OIDC_GROUP_ADMIN` | Gramps "Admin" rolüne eşlenen OIDC sağlayıcınızdaki grup/rol adı
`OIDC_GROUP_OWNER` | Gramps "Owner" rolüne eşlenen OIDC sağlayıcınızdaki grup/rol adı
`OIDC_GROUP_EDITOR` | Gramps "Editor" rolüne eşlenen OIDC sağlayıcınızdaki grup/rol adı
`OIDC_GROUP_CONTRIBUTOR` | Gramps "Contributor" rolüne eşlenen OIDC sağlayıcınızdaki grup/rol adı
`OIDC_GROUP_MEMBER` | Gramps "Member" rolüne eşlenen OIDC sağlayıcınızdaki grup/rol adı
`OIDC_GROUP_GUEST` | Gramps "Guest" rolüne eşlenen OIDC sağlayıcınızdaki grup/rol adı

### Rol Eşleme Davranışı

- Eğer rol eşlemesi yapılandırılmamışsa (hiçbir `OIDC_GROUP_*` değişkeni ayarlanmamışsa), mevcut kullanıcı rolleri korunur
- Kullanıcılara grup üyeliklerine göre hak kazandıkları en yüksek rol atanır
- Rol eşlemesi varsayılan olarak büyük/küçük harf duyarlıdır (OIDC sağlayıcınıza bağlıdır)

## OIDC Çıkışı

Gramps Web, OIDC sağlayıcıları için Tek Oturum Kapatma (SSO çıkışı) desteği sunar. Bir kullanıcı OIDC aracılığıyla kimlik doğruladıktan sonra Gramps Web'den çıkış yaptığında, sağlayıcı `end_session_endpoint`'i destekliyorsa otomatik olarak kimlik sağlayıcısının çıkış sayfasına yönlendirilir.

### Arka Kanal Çıkışı

Gramps Web, OpenID Connect Arka Kanal Çıkışı spesifikasyonunu uygular. Bu, kimlik sağlayıcılarının bir kullanıcının başka bir uygulamadan veya kimlik sağlayıcısından çıkış yaptığında Gramps Web'e bildirim göndermesine olanak tanır.

#### Yapılandırma

Kimlik sağlayıcınızla arka kanal çıkışını yapılandırmak için:

1. **Kimlik sağlayıcınızın istemci yapılandırmasında arka kanal çıkış uç noktasını kaydedin:**
   ```
   https://your-gramps-backend.com/api/oidc/backchannel-logout/
   ```

2. **Sağlayıcınızı çıkış bildirimlerini gönderecek şekilde yapılandırın.** Kesin adımlar sağlayıcınıza bağlıdır:

   **Keycloak:**

   - İstemci yapılandırmanızda "Ayarlar" bölümüne gidin
   - "Arka Kanal Çıkış URL'si"ni `https://your-gramps-backend.com/api/oidc/backchannel-logout/` olarak ayarlayın
   - Oturum tabanlı çıkış istiyorsanız "Arka Kanal Çıkış Oturumu Gerektirir" seçeneğini etkinleştirin

   **Authentik:**

   - Sağlayıcı yapılandırmanızda arka kanal çıkış URL'sini ekleyin
   - Sağlayıcının çıkış token'larını gönderecek şekilde yapılandırıldığından emin olun

!!! warning "Token Süresi"
    JWT token'larının durumsuz doğası nedeniyle, arka kanal çıkışı şu anda çıkış olayını kaydeder ancak zaten verilmiş olan JWT token'larını hemen iptal edemez. Token'lar süresi dolana kadar geçerli kalacaktır (varsayılan: erişim token'ları için 15 dakika).

    Güvenliği artırmak için, şunları dikkate alın:

    - JWT token süresini azaltma (`JWT_ACCESS_TOKEN_EXPIRES`)
    - Kullanıcıları kimlik sağlayıcınızdan çıkış yaparken Gramps Web'den manuel olarak çıkış yapmaları konusunda bilgilendirme

!!! tip "Nasıl Çalışır"
    Bir kullanıcı kimlik sağlayıcınızdan veya başka bir uygulamadan çıkış yaptığında:

    1. Sağlayıcı, Gramps Web'in arka kanal çıkış uç noktasına bir `logout_token` JWT gönderir
    2. Gramps Web token'ı doğrular ve çıkış olayını kaydeder
    3. Çıkış token'ının JTI'si yeniden oynatma saldırılarını önlemek için bir kara listeye eklenir
    4. Kullanıcının JWT'si ile yapılan yeni API talepleri, token'lar süresi dolduğunda reddedilecektir

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

# GitHub OAuth
OIDC_GITHUB_CLIENT_ID="your-github-client-id"
OIDC_GITHUB_CLIENT_SECRET="your-github-client-secret"
```

### Authelia

Gramps Web için topluluk tarafından oluşturulmuş bir OIDC kurulum kılavuzu, [resmi Authelia belgeleri web sitesinde](https://www.authelia.com/integration/openid-connect/clients/gramps/) mevcuttur.
