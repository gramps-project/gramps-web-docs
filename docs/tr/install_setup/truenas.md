# TrueNAS Kurulumu

Bu kılavuz, TrueNAS Community Edition 25.04 üzerinde Gramps Web'in nasıl kurulacağını açıklamaktadır.

!!! warning
    Bu kılavuz, yeni bir Docker Compose tabanlı uygulama sistemini tanıtan TrueNAS Community Edition 25.04 veya daha sonraki sürümler için tasarlanmıştır. Daha önceki TrueNAS sürümlerine uygulanmaz.

## Ön Koşullar

- TrueNAS Community Edition 25.04 veya daha yeni
- TrueNAS web arayüzüne temel aşinalık
- Gramps Web verilerini depolamak için bir veri kümesi

## Genel Bakış

TrueNAS Community Edition 25.04, önceki Helm şeması tabanlı yaklaşımı değiştiren yeni bir Docker Compose tabanlı uygulama sistemi tanıttı. Bu kılavuz, Docker Compose kullanarak Gramps Web için özel bir uygulama oluşturma sürecinde size rehberlik edecektir.

## Adım 1: Depolama Hazırlama

1. TrueNAS web arayüzünde **Datasets** bölümüne gidin
2. Gramps Web için yeni bir veri kümesi oluşturun (örn. `grampsweb`). Bu veri kümesinin tam yolunu not edin, örneğin `/mnt/storage/grampsweb`, çünkü daha sonra buna ihtiyacınız olacak.

Çeşitli bileşenler için alt dizinler oluşturun:
- `users` - Kullanıcı veritabanı
- `database` - Gramps veritabanı dosyası(ları)
- `media` - Medya dosyaları

## Adım 2: Docker Compose Uygulamasını Oluşturma

1. TrueNAS web arayüzünde **Apps** bölümüne gidin
2. **Discover Apps** butonuna tıklayın
3. "Gramps Web" için arama yapın ve üzerine tıklayın
4. "Install" butonuna tıklayın

Bu sizi uygulama yapılandırma sayfasına götürecektir.

## Adım 3: Uygulamayı Yapılandırma

### Gramps Web yapılandırması

- **Zaman Dilimi:** Yerel zaman diliminizi ayarlayın (örn. `Europe/Berlin`)
- **Redis şifresi:** Redis için bir şifre belirleyin. Bu yalnızca uygulama tarafından dahili olarak kullanılacaktır.
- **Telemetriyi devre dışı bırak:** Lütfen bu kutucuğu işaretlemeyin – detaylar için [buraya bakın](telemetry.md).
- **Gizli anahtar:** Bunu güçlü ve benzersiz bir değere ayarlamanız çok önemlidir. Rastgele bir anahtar oluşturma talimatları için [sunucu yapılandırmasına](configuration.md#existing-configuration-settings) bakın.
- **Ek Çevre Değişkenleri:** Tüm ek [yapılandırma seçeneklerini](configuration.md) `GRAMPSWEB_` ile başlayan çevre değişkenleri olarak ayarlamanız gerekecektir. Lütfen [yapılandırma belgelerini](configuration.md) detaylı bir şekilde kontrol edin – örneğin, boolean değerlerin çevre değişkenleri için `true` veya `false` (küçük harfle) olarak ayarlanması gerektiği, yaygın bir tuzaktır.

Lütfen **en azından** `GRAMPSWEB_BASE_URL`'yi Gramps Web örneğinizin erişilebilir olacağı URL'ye ayarlayın – bu, düzgün çalışması için gereklidir.

Bu aşamada e-posta yapılandırmasını da ayarlamak isteyebilirsiniz. Eğer yaparsanız, onboarding sihirbazındaki e-posta yapılandırma adımını atlayabilirsiniz. İlgili çevre değişkenleri şunlardır:

- `GRAMPSWEB_EMAIL_HOST`
- `GRAMPSWEB_EMAIL_HOST_USER`
- `GRAMPSWEB_EMAIL_HOST_PASSWORD`
- `GRAMPSWEB_DEFAULT_FROM_EMAIL`

Tüm yapılandırma ayarları daha sonra TrueNAS Apps arayüzünde "Edit" butonuna tıklayarak değiştirilebilir.

### Depolama Yapılandırması

- **Kullanıcı Depolama:** Daha önce oluşturduğunuz `users` dizininin yolunu seçin.
- **İndeks Depolama:** Varsayılan ayar "ixVolume (Sistem tarafından otomatik olarak oluşturulan veri kümesi)" olarak bırakabilirsiniz.
- **Küçük Resim Önbellek Depolama:** Varsayılan ayar "ixVolume (Sistem tarafından otomatik olarak oluşturulan veri kümesi)" olarak bırakabilirsiniz.
- **Önbellek Depolama:** Varsayılan ayar "ixVolume (Sistem tarafından otomatik olarak oluşturulan veri kümesi)" olarak bırakabilirsiniz.
- **Medya Depolama:** Daha önce oluşturduğunuz `media` dizininin yolunu seçin.
- **Gramps Veritabanı Depolama:** Daha önce oluşturduğunuz `database` dizininin yolunu seçin.

### Kaynaklar Yapılandırması

Sorunsuz bir çalışma sağlamak için en az 2 CPU ve 4096 MB RAM ayırmanızı öneririz.

## Adım 4: Gramps Web'e Erişim

Uygulama dağıtıldıktan sonra, TrueNAS Apps arayüzünde "Web UI" butonuna tıklayarak Gramps Web'e erişebilirsiniz. "Gramps Web'e Hoş Geldiniz" onboarding sihirbazını görmelisiniz.

Kullanıcıların Gramps Web arayüzünü erişmesine izin vermek istiyorsanız, **uygulamayı** doğrudan internete açmayın, ancak bir sonraki adıma geçin.

## Adım 5: Ters Proxy Kurulumu

Gramps Web örneğinizi kullanıcılara güvenli bir şekilde açmak için ters proxy kurulumunu yapmanız önerilir. Bu, SSL/TLS sertifikalarını yönetmenizi ve erişimi kontrol etmenizi sağlar.

En kolay seçenek, resmi TrueNAS Nginx Proxy Manager uygulamasını kullanmaktır. TrueNAS Apps arayüzünde uygulamayı arayın ve yükleyin. Tüm ayarları varsayılanında bırakabilirsiniz, ancak bir ek çevre değişkeni ayarlamanızı öneririz: `DISABLE_IPV6` değerini `true` olarak ayarlayarak olası IPv6 ile ilgili sorunlardan kaçınabilirsiniz.

Dağıtım tamamlandıktan sonra, Nginx Proxy Manager web arayüzünü açın ve aşağıdaki ayarlarla yeni bir proxy ana bilgisayarı oluşturun:

- Şema: `http`
- İletim Ana Bilgisayarı / IP: TrueNAS sunucunuzun ana adı (örn. `truenas`)
- İletim Portu: Gramps Web uygulamanıza atanan port (kesin port için TrueNAS Apps arayüzüne bakın)
- "SSL" sekmesinde, "Force SSL" seçeneğini işaretleyin
- "SSL Sertifikaları" altında, "Add SSL Certificate" > "Let's Encrypt" seçeneğini seçerek alan adınız için yeni bir Let's Encrypt sertifikası oluşturun.

Yönlendiricinizi yapılandırma ve SSL sertifikaları alma hakkında daha fazla bilgi için lütfen [Nginx Proxy Manager belgelerine](https://nginxproxymanager.com/guide/) bakın.
