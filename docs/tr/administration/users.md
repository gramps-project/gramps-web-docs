# Kullanıcıları Yönet

Kullanıcı yönetim arayüzü **Ayarlar > Kullanıcıları Yönet** (üst uygulama çubuğundaki kullanıcı simgesi) üzerinden erişilebilir. Sadece Sahip veya Yönetici rolüne sahip kullanıcılara açıktır.

## Kullanıcı rolleri

Mevcut kullanıcı rolleri ve izinleri hakkında tam bir açıklama için [Kullanıcı sistemi](../install_setup/users.md) sayfasına bakın.

## Kullanıcıları görüntüle ve filtrele

Kullanıcıları yönet sayfası, aşağıdaki sütunlarla birlikte tüm kayıtlı kullanıcı hesaplarının bir tablosunu gösterir:

- **Kullanıcı Adı** — giriş adı
- **Tam Ad** — görüntüleme adı
- **E-posta** — kullanıcının e-posta adresi
- **Rol** — atanan rol (Misafir, Üye, Katkıda Bulunan, Editör, Sahip veya Yönetici)
- **Hesap Kaynağı** — "Şifre" (yerel hesap) veya bir dış kimlik sağlayıcısının adı (ör. OIDC kullanıldığında)

Listeyi filtrelemek için tablonun üst kısmındaki arama alanını ve rol açılır menüsünü kullanın. Tüm filtreleri sıfırlamak için filtre temizleme butonuna tıklayın.

## Bir kullanıcıyı düzenle

Herhangi bir satırdaki düzenleme (kalem) simgesine tıklayarak düzenleme penceresini açın. Kullanıcının:

- Tam adını
- E-posta adresini
- Rolünü

değiştirebilirsiniz.

Bu, **yeni kendinden kayıtlı bir kullanıcıyı etkinleştirmenin** birincil yoludur: rolünü *devre dışı* durumdan herhangi bir aktif role (ör. Üye veya Editör) değiştirin.

## Bir kullanıcıyı manuel olarak ekle

Kullanıcıları doğrudan kendinden kayıt gerektirmeden yeni bir kullanıcı hesabı oluşturmak için tablonun üstündeki **kullanıcı ekle** (kişi ekle) simgesine tıklayın. Açılan pencerede kullanıcı adı, tam ad, e-posta adresi, şifre ve rolü doldurun ve **Kaydet** butonuna tıklayın.

## Bir kullanıcıyı sil

Herhangi bir satırdaki silme (çöp kutusu) simgesine tıklayın ve onay penceresini onaylayın. Bu işlem geri alınamaz.

## Kullanıcı hesaplarını dışa ve içe aktar

Bu butonlar, [farklı bir Gramps Web örneğine geçiş yaparken](export.md) kullanışlıdır.

- **Kullanıcı detaylarını dışa aktar** (indirme simgesi) — tüm kullanıcı hesaplarını (şifreler dahil değil, çünkü şifreler şifreli biçimde saklanır) içeren bir JSON dosyası indirir.
- **Kullanıcı hesaplarını içe aktar** (grup ekle simgesi) — daha önce dışa aktarılmış bir JSON dosyasını yükleyerek toplu olarak kullanıcı hesapları oluşturur. Tüm içe aktarılan kullanıcılar, şifreler aktarılmadığı için "Şifremi unuttum" bağlantısı aracılığıyla yeni bir şifre belirlemek zorundadır.

## Kayıt bağlantısı (çoklu ağaç kurulumu yalnızca)

Çoklu ağaç kurulumunda yeni kullanıcılar için kayıt bağlantısı, kullanıcıları yönet sayfasının üst kısmında gösterilir. Bu bağlantıyı kopyalayabilir ve hesabını ağaçta kaydetmek için davet etmek istediğiniz kişilerle paylaşabilirsiniz.

!!! not
    Tek ağaç kurulumunda giriş sayfasında genel bir "Kayıt Ol" bağlantısı vardır; ağaç başına kayıt bağlantısı yalnızca çoklu ağaç kurulumlarında gereklidir.

## AI sohbet izinleri

Eğer sunucuda AI sohbet etkinleştirildiyse, sayfanın üst kısmındaki açılır menü, hangi kullanıcı rollerinin sohbet özelliğini kullanabileceğini kontrol etmenizi sağlar:

- Herkes (misafirler dahil)
- Üye ve üstü
- Katkıda Bulunan ve üstü
- Editör ve üstü
- Sadece sahipler ve yöneticiler
- Hiçbiri (tüm kullanıcılar için sohbeti devre dışı bırak)
