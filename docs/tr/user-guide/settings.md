# Kullanıcı Ayarları

Kullanıcı Ayarları, üst uygulama çubuğundaki kullanıcı simgesi aracılığıyla erişilebilir, ardından **Kullanıcı Ayarları**. Sayfa, katlanabilir bölümler halinde düzenlenmiştir. Değişiklikler, aksi belirtilmedikçe hemen etkili olur.

!!! note
    Kullanıcı Ayarları'ndaki değişiklikler yalnızca kendi hesabınızı etkiler. Tüm ağaç kullanıcılarını etkileyen ayarlar, [Yönetim Ayarları](../administration/settings.md) altında yönetilmektedir.

## Hesap

Profil bilgilerinizi, kimlik bilgilerinizi ve hesap güvenliğinizi kapsar.

### Kullanıcı bilgileri

**kullanıcı adınızı** ve mevcut **kullanıcı rolünüzü** (örneğin, Misafir, Üye, Editör) gösterir. Bunlar yalnızca okunabilir.

### E-posta değiştir

Yeni bir e-posta adresi girin ve hesabınıza bağlı adresi güncellemek için **Gönder** butonuna tıklayın. E-posta adresi, şifre sıfırlamaları ve (eğer yapılandırılmışsa) bildirimler için kullanılır.

### Şifre değiştir

Mevcut şifrenizi ve yeni bir şifre girin, ardından **Gönder** butonuna tıklayın. Mevcut cihazda oturumunuz açık kalır, diğer cihazlar ve tarayıcılardaki oturumlarınız 15 dakika içinde sona erer. Mevcut şifrenizi unuttuysanız, giriş sayfasındaki **Şifremi unuttum** bağlantısını kullanın.

Bu bölüm, sunucunun yalnızca bir dış sağlayıcı aracılığıyla oturum açmaya izin vermesi durumunda gizlidir (bkz. [OIDC kimlik doğrulaması](../install_setup/oidc.md)).

### Bağlı oturum açma yöntemleri

Sunucunuz tek oturum açma (bkz. [OIDC kimlik doğrulaması](../install_setup/oidc.md)) sunuyorsa, bir sağlayıcıdan (örneğin, Google veya kuruluşunuzun girişi) bir hesabı Gramps Web hesabınıza bağlayabilirsiniz. Daha sonra o sağlayıcı ile oturum açabilir ve mevcut hesabınıza, rolünüz ve düzenlemeleriniz ile ulaşabilirsiniz. Bu bölüm yalnızca tek oturum açma etkinleştirildiğinde ve sunucu bağlantıyı desteklediğinde görünür (Gramps Web API 3.24 ve sonrası).

Bir hesabı bağlamak için **Bağla** ve sağlayıcının adını tıklayın, sağlayıcıda oturum açın ve ayarlarınıza geri yönlendirilirsiniz. Eğer yakın zamanda oturum açmadıysanız, önce tekrar oturum açmanız istenir.

Bir sağlayıcı hesabı yalnızca bir Gramps Web hesabına bağlanabilir. "Bu oturum açma zaten başka bir hesaba bağlı" mesajını görüyorsanız, başka bir yerde bağlıdır; örneğin, o sağlayıcı ile ilk oturum açtığınızda oluşturulan bir hesaba. Bir yönetici, o diğer hesabı silebilir; ardından onu kendi hesabınıza bağlayabilirsiniz.

Bir hesabı ayırmak için **Bağlantıyı kes** butonuna tıklayın. Eğer bu, son bağlı oturum açma yönteminizse, daha sonra hala oturum açabilmeniz için şifrenizi de girmeniz gerekir. Hesabınız tek oturum açma ile oluşturulduysa ve hiç şifre ayarlamadıysanız, önce bir şifre ayarlamak için giriş sayfasındaki **Şifremi unuttum** seçeneğini kullanın (bu, sunucunun e-posta göndermesini gerektirir). Sunucu yalnızca bir sağlayıcı aracılığıyla oturum açmaya izin veriyorsa, son bağlı hesap ayrılamaz.

## Görünüm

Cihazınızda kaydedilen görüntü tercihlerini kontrol eder.

### Dil

Gramps Web arayüzü için dili seçin. Dil ayarı, tarayıcının yerel depolamasında saklanır ve yalnızca mevcut cihaza uygulanır.

### Tema

Aşağıdakiler arasında seçim yapın:

- **Sistem** – işletim sisteminin açık/karanlık tercihine uyar (varsayılan)
- **Açık** – her zaman açık temayı kullan
- **Karanlık** – her zaman karanlık temayı kullan

Tema ayarı, tarayıcının yerel depolamasında saklanır.

### Ağaç tercihleri

#### Varsayılan aile ağacı görünümü

[Family Tree](tree.md) sayfasına gittiğinizde varsayılan olarak hangi grafik türünün açılacağını ayarlar. Seçenekler: Ata Ağacı, Soy Ağacı, Kum Saati Grafiği, İlişki Grafiği ve Fan Grafiği.

Bu tercih, tarayıcının yerel depolamasında saklanır.

## Geliştirici araçları

### API jetonu

Mevcut oturum jetonunuzu panoya kopyalar. Jeton, örneğin Gramps Web örneğinizin `/api/swagger-ui` adresinde sunduğu etkileşimli Swagger UI aracılığıyla REST API'sine doğrudan kimlik doğrulamak için kullanılabilir.

Oturumunuz zaten mevcut olan Swagger UI'yi yeni bir sekmede açmak için **Swagger'ı Başlat** butonuna tıklayın.

!!! note
    Oturum jetonu kısa ömürlüdür. Swagger'da kullanmadan önce hemen kopyalayın, çünkü süresi dolabilir.
