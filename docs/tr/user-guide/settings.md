# Kullanıcı Ayarları

Kullanıcı Ayarları, üst uygulama çubuğundaki kullanıcı simgesi aracılığıyla erişilebilir, ardından **Kullanıcı Ayarları**. Sayfa, katlanabilir bölümler halinde düzenlenmiştir. Değişiklikler, aksi belirtilmedikçe hemen etkili olur.

!!! note
    Kullanıcı Ayarları'ndaki değişiklikler yalnızca kendi hesabınızı etkiler. Tüm ağaç kullanıcılarını etkileyen ayarlar, [Yönetim Ayarları](../administration/settings.md) altında yönetilmektedir.

## Hesap

Profil bilgilerinizi, kimlik bilgilerinizi ve hesap güvenliğinizi kapsar.

### Kullanıcı bilgileri

**kullanıcı adınızı** ve mevcut **kullanıcı rolünüzü** (örneğin, Misafir, Üye, Editör) gösterir. Bunlar yalnızca okunabilir.

### E-posta değiştir

Yeni bir e-posta adresi girin ve hesabınıza bağlı adresi güncellemek için **Gönder**'e tıklayın. E-posta adresi, şifre sıfırlamaları ve (eğer yapılandırılmışsa) bildirimler için kullanılır.

### Şifre değiştir

Mevcut şifrenizi ve yeni bir şifre girin, ardından **Gönder**'e tıklayın. Mevcut şifrenizi unuttuysanız, giriş sayfasındaki **Şifremi unuttum** bağlantısını kullanın.

### Bağlı oturum açma yöntemleri

Sunucunuz tek oturum açma (bkz. [OIDC kimlik doğrulama](../install_setup/oidc.md)) sunuyorsa, Google veya kuruluşunuzun girişi gibi bir sağlayıcıdan bir hesabı Gramps Web hesabınıza bağlayabilirsiniz. Daha sonra o sağlayıcı ile oturum açabilir ve mevcut hesabınıza, rolünüzle ve düzenlemelerinizle ulaşabilirsiniz. Bu bölüm yalnızca tek oturum açma etkinleştirildiğinde ve sunucu bağlantıyı desteklediğinde görünür (Gramps Web API 3.24 ve sonrası).

Bir hesabı bağlamak için **Bağla** ve sağlayıcının adını tıklayın, sağlayıcıda oturum açın ve ayarlarınıza geri yönlendirilirsiniz. Eğer yakın zamanda oturum açmadıysanız, önce tekrar oturum açmanız istenir.

Bir sağlayıcı hesabı yalnızca bir Gramps Web hesabına bağlanabilir. "Bu oturum açma başka bir hesaba bağlı" mesajını görüyorsanız, başka bir yerde bağlıdır; örneğin, o sağlayıcı ile ilk oturum açtığınızda oluşturulan bir hesaba. Bir yönetici, o diğer hesabı silebilir; ardından onu kendi hesabınıza bağlayabilirsiniz.

Bir hesabı ayırmak için **Ayrıl**'a tıklayın. Eğer bu, son bağlı oturum açma yönteminizse, ardından hala oturum açabilmeniz için şifrenizi de girmeniz gerekir. Hesabınız tek oturum açma ile oluşturulduysa ve hiç şifre belirlemediyseniz, önce bir tane belirlemek için giriş sayfasındaki **Şifremi unuttum** seçeneğini kullanın (bu, sunucunun e-posta göndermesini gerektirir). Sunucu yalnızca bir sağlayıcı aracılığıyla oturum açmaya izin veriyorsa, son bağlı hesap ayrılamaz.

## Görünüm

Cihazınızda kaydedilen görüntüleme tercihlerini kontrol eder.

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

[Family Tree](tree.md) sayfasına gittiğinizde varsayılan olarak hangi grafik türünün açılacağını ayarlar. Seçenekler, Ata Ağacı, Soy Ağacı, Kum Saati Grafiği, İlişki Grafiği ve Fan Grafiği'dir.

Bu tercih, tarayıcının yerel depolamasında saklanır.

## Geliştirici araçları

### API token

Mevcut oturum belirtecinizi panoya kopyalar. Belirteç, örneğin Gramps Web örneğinizde `/api/swagger-ui` adresinde sunulan etkileşimli Swagger UI'ye doğrudan kimlik doğrulamak için kullanılabilir.

Oturumunuz zaten mevcut olan Swagger UI'yi yeni bir sekmede açmak için **Swagger'ı Başlat**'a tıklayın.

!!! note
    Oturum belirteci kısa ömürlüdür. Swagger'da kullanmadan önce hemen kopyalayın, çünkü süresi dolabilir.
