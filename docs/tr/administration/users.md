# Kullanıcıları Yönet

Kullanıcı yönetim arayüzü **Ayarlar > Kullanıcıları Yönet** (üst uygulama çubuğundaki kullanıcı simgesi) üzerinden erişilebilir. Sadece Sahip veya Yöneticilik rolüne sahip kullanıcılara açıktır.

## Kullanıcı rolleri

Mevcut kullanıcı rolleri ve izinleri hakkında tam bir açıklama için [Kullanıcı sistemi](../install_setup/users.md) sayfasına bakın. Misafirler ile üyeler arasındaki ana fark, misafirlerin [özel kayıtları](../user-guide/privacy.md) görememesidir, bu nedenle rolü, özel olarak işaretlediğiniz şeyle birlikte seçin.

## Kullanıcıları Görüntüle ve Filtrele

Kullanıcıları yönet sayfası, aşağıdaki sütunlarla birlikte tüm kayıtlı kullanıcı hesaplarının bir tablosunu gösterir:

- **Kullanıcı Adı** – giriş adı
- **Tam Ad** – görüntü adı
- **E-posta** – kullanıcının e-posta adresi
- **Rol** – atanan rol (Misafir, Üye, Katkıda Bulunan, Editör, Sahip veya Yönetici)
- **Hesap Kaynağı** – "Şifre" (yerel hesap) veya bir dış kimlik sağlayıcısının adı (örneğin OIDC kullanırken)

Listeyi filtrelemek için tablonun üstündeki arama alanını ve rol açılır menüsünü kullanın. Tüm filtreleri sıfırlamak için filtre temizleme butonuna tıklayın.

## Bir Kullanıcıyı Düzenle

Herhangi bir satırdaki düzenle (kalem) simgesine tıklayarak düzenleme penceresini açın. Kullanıcının:

- Tam adını
- E-posta adresini
- Rolünü

değiştirebilirsiniz.

Bu, **yeni kendine kayıtlı bir kullanıcıyı etkinleştirmenin** birincil yoludur: rolünü *devre dışı* durumdan herhangi bir aktif role (örneğin Üye veya Editör) değiştirin.

E-posta adreslerinin benzersiz olması gerekmez (Gramps Web API 3.22'den itibaren), bu nedenle birkaç hesap aynı adresi paylaşabilir.

Bir kullanıcıyı devre dışı bırakmak veya şifresini değiştirmek, tüm oturumlarını 15 dakika içinde sonlandırır.

!!! not
    Sahipler, daha yüksek bir role sahip kullanıcıları düzenleyemez, şifrelerini değiştiremez veya silemez, örneğin site yöneticisi. Aynı role sahip kullanıcılar, örneğin bir ağacın iki sahibi, birbirlerini yönetebilir.

## Kullanıcıyı Manuel Olarak Ekle

Tablonun üstündeki **kullanıcı ekle** (kişi ekle) simgesine tıklayarak yeni bir kullanıcı hesabı oluşturun. Diyalogda kullanıcı adını, tam adını, e-posta adresini, şifreyi ve rolü doldurun ve **Kaydet** butonuna tıklayın.

## Bir Kullanıcıyı Sil

Herhangi bir satırdaki sil (çöp kutusu) simgesine tıklayın ve onay penceresini onaylayın. Bu işlem geri alınamaz.

!!! not
    Bir ağacın yönetiminden kimsenin kalmamasını önlemek için, kendi rolünüzü Sahip'in altına düşüremez veya kendi hesabınızı silemezsiniz eğer ağacın tek Sahibi veya Yöneticisiyseniz. Öncelikle başka bir kullanıcıyı Sahip olarak terfi ettirin. Bir yönetici, başka bir kullanıcının ağacının son sahibini değiştirebilir veya kaldırabilir, çünkü yeni birini atayabilir.

## Kullanıcı Hesaplarını Dışa Aktarma ve İçe Aktarma

Bu butonlar, [farklı bir Gramps Web örneğine geçiş yaparken](export.md) kullanışlıdır.

- **Kullanıcı detaylarını dışa aktar** (indirme simgesi) – tüm kullanıcı hesaplarını (şifreler olmadan, çünkü şifreler şifreli biçimde saklanır) içeren bir JSON dosyası indirir.
- **Kullanıcı hesaplarını içe aktar** (grup ekle simgesi) – toplu olarak kullanıcı hesapları oluşturmak için daha önce dışa aktarılmış bir JSON dosyasını yükler. Tüm içe aktarılan kullanıcılar, şifreler aktarılmadığı için "Şifremi unuttum" bağlantısı aracılığıyla yeni bir şifre belirlemek zorundadır.

## Kayıt Bağlantısı (çoklu-ağaç kurulumu için yalnızca)

Çoklu-ağaç kurulumunda, yeni kullanıcılar için kayıt bağlantısı kullanıcıları yönet sayfasının üst kısmında gösterilir. Bu bağlantıyı kopyalayabilir ve hesabını ağacınıza kaydetmek için davet etmek istediğiniz kişilerle paylaşabilirsiniz.

!!! not
    Tek ağaç kurulumunda, giriş sayfasında genel bir "Kayıt Ol" bağlantısı vardır; ağaç başına kayıt bağlantısı yalnızca çoklu-ağaç kurulumlarında gereklidir.

## AI sohbet izinleri

Eğer sunucuda AI sohbet etkinleştirildiyse, sayfanın üst kısmındaki bir açılır menü, hangi kullanıcı rollerinin sohbet özelliğini kullanabileceğini kontrol etmenizi sağlar:

- Herkes (misafirler dahil)
- Üye ve üzeri
- Katkıda Bulunan ve üzeri
- Editör ve üzeri
- Sadece sahipler ve yöneticiler
- Hiç kimse (tüm kullanıcılar için sohbeti devre dışı bırak)
