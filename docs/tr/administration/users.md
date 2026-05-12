# Kullanıcıları Yönet

Kullanıcı yönetim arayüzü **Ayarlar > Kullanıcıları Yönet** (üst uygulama çubuğundaki kullanıcı simgesi) üzerinden erişilebilir. Sadece Sahip veya Yöneticilik rolüne sahip kullanıcılara açıktır.

## Kullanıcı rolleri

Mevcut kullanıcı rolleri ve izinleri hakkında tam bir açıklama için [Kullanıcı sistemi](../install_setup/users.md) sayfasına bakın.

## Kullanıcıları görüntüle ve filtrele

Kullanıcıları yönet sayfası, aşağıdaki sütunlarla birlikte tüm kayıtlı kullanıcı hesaplarının bir tablosunu gösterir:

- **Kullanıcı Adı** – giriş adı
- **Tam Ad** – görüntüleme adı
- **E-posta** – kullanıcının e-posta adresi
- **Rol** – atanan rol (Misafir, Üye, Katkıda Bulunan, Editör, Sahip veya Yönetici)
- **Hesap Kaynağı** – ya "Şifre" (yerel hesap) ya da bir dış kimlik sağlayıcısının adı (örneğin, OIDC kullanırken)

Listeyi filtrelemek için tablonun üst kısmındaki arama alanını ve rol açılır menüsünü kullanın. Tüm filtreleri sıfırlamak için filtre temizleme butonuna tıklayın.

## Bir kullanıcıyı düzenle

Düzenlemek istediğiniz herhangi bir satırdaki düzenleme (kalem) simgesine tıklayarak düzenleme penceresini açın. Kullanıcının:

- Tam adını
- E-posta adresini
- Rolünü

değiştirebilirsiniz.

Bu, **yeni kendiliğinden kayıtlı bir kullanıcıyı etkinleştirmenin** ana yoludur: rolünü *devre dışı* durumdan herhangi bir aktif role (örneğin Üye veya Editör) değiştirin.

## Bir kullanıcıyı manuel olarak ekle

Yeni bir kullanıcı hesabı oluşturmak için tablonun üstündeki **kullanıcı ekle** (kişi ekle) simgesine tıklayın; bu, kendiliğinden kayıt gerektirmeden doğrudan yeni bir kullanıcı hesabı oluşturur. Açılan pencerede kullanıcı adı, tam ad, e-posta adresi, şifre ve rolü doldurun ve **Kaydet** butonuna tıklayın.

## Bir kullanıcıyı sil

Herhangi bir satırdaki silme (çöp kutusu) simgesine tıklayın ve onay penceresini onaylayın. Bu işlem geri alınamaz.

## Kullanıcı hesaplarını dışa ve içe aktar

Bu butonlar, [farklı bir Gramps Web örneğine geçiş yaparken](export.md) faydalıdır.

- **Kullanıcı detaylarını dışa aktar** (indirme simgesi) – tüm kullanıcı hesaplarını (şifreler dahil değil, çünkü şifreler şifreli biçimde saklanır) içeren bir JSON dosyasını indirir.
- **Kullanıcı hesaplarını içe aktar** (grup ekle simgesi) – daha önce dışa aktarılmış bir JSON dosyasını yükleyerek toplu olarak kullanıcı hesapları oluşturur. Tüm içe aktarılan kullanıcılar, şifrelerin aktarılamayacağı için "Şifremi unuttum" bağlantısı aracılığıyla yeni bir şifre belirlemeleri gerekecektir.

## Kayıt bağlantısı (çoklu-ağaç kurulumu için)

Çoklu-ağaç kurulumu olan bir sistemde, yeni kullanıcılar için kayıt bağlantısı kullanıcıları yönet sayfasının üst kısmında gösterilir. Bu bağlantıyı kopyalayabilir ve hesabını ağaçta kaydetmek için davet etmek istediğiniz kişilerle paylaşabilirsiniz.

!!! not
    Tek ağaç kurulumunda giriş sayfasında genel bir "Kaydol" bağlantısı vardır; ağaç başına kayıt bağlantısına yalnızca çoklu-ağaç kurulumlarında ihtiyaç vardır.

## AI sohbet izinleri

Eğer sunucuda AI sohbet etkinleştirildiyse, sayfanın üst kısmındaki açılır menü, hangi kullanıcı rollerinin sohbet özelliğini kullanmasına izin verileceğini kontrol etmenizi sağlar:

- Herkes (misafirler dahil)
- Üye ve üzeri
- Katkıda Bulunan ve üzeri
- Editör ve üzeri
- Sadece sahipler ve yöneticiler
- Hiçbiri (tüm kullanıcılar için sohbeti devre dışı bırak)
