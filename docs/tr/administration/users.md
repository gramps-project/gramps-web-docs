# Kullanıcıları Yönet

Kullanıcı yönetim arayüzü **Ayarlar > Kullanıcıları Yönet** (üst uygulama çubuğundaki kullanıcı simgesi) üzerinden erişilebilir. Sadece Sahip veya Yönetici rolüne sahip kullanıcılara açıktır.

## Kullanıcı rolleri

Mevcut kullanıcı rolleri ve izinleri hakkında tam bir açıklama için [Kullanıcı sistemi](../install_setup/users.md) sayfasına bakın.

## Kullanıcıları görüntüle ve filtrele

Kullanıcıları yönet sayfası, aşağıdaki sütunlarla birlikte tüm kayıtlı kullanıcı hesaplarının bir tablosunu gösterir:

- **Kullanıcı Adı** – giriş adı
- **Tam Ad** – görüntü adı
- **E-posta** – kullanıcının e-posta adresi
- **Rol** – atanan rol (Misafir, Üye, Katkıda Bulunan, Editör, Sahip veya Yönetici)
- **Hesap Kaynağı** – ya "Şifre" (yerel hesap) ya da bir dış kimlik sağlayıcısının adı (örneğin OIDC kullanırken)

Listeyi filtrelemek için tablonun üstündeki arama alanını ve rol açılır menüsünü kullanın. Tüm filtreleri sıfırlamak için filtre temizleme butonuna tıklayın.

## Bir kullanıcıyı düzenle

Düzenlemek istediğiniz satırdaki düzenleme (kalem) simgesine tıklayarak düzenleme penceresini açın. Kullanıcının:

- Tam adını
- E-posta adresini
- Rolünü

değiştirebilirsiniz.

Bu, **yeni kendinden kayıtlı bir kullanıcıyı etkinleştirmenin** birincil yoludur: rolünü *devre dışı* durumdan herhangi bir aktif role (örneğin Üye veya Editör) değiştirin.

E-posta adreslerinin benzersiz olması gerekmez (Gramps Web API 3.22'den itibaren), bu nedenle birkaç hesap aynı adresi paylaşabilir.

Bir kullanıcıyı devre dışı bırakmak veya şifresini değiştirmek, tüm oturumlarını 15 dakika içinde sonlandırır.

!!! not
    Sahipler, site yöneticisi gibi daha yüksek bir role sahip kullanıcıları düzenleyemez, şifrelerini değiştiremez veya silemez. Aynı role sahip kullanıcılar, örneğin bir ağacın iki sahibi, birbirlerini yönetebilirler.

## Bir kullanıcıyı manuel olarak ekle

Kullanıcıları yönet tablosunun üzerinde bulunan **kullanıcı ekle** (kişi ekle) simgesine tıklayarak yeni bir kullanıcı hesabı oluşturun. Düzenleme penceresinde kullanıcı adı, tam ad, e-posta adresi, şifre ve rolü doldurun ve **Kaydet** butonuna tıklayın.

## Bir kullanıcıyı sil

Herhangi bir satırdaki silme (çöp kutusu) simgesine tıklayın ve onay penceresini onaylayın. Bu işlem geri alınamaz.

!!! not
    Bir ağacın yönetiminden yoksun kalmaması için, eğer ağacın tek Sahibi veya Yöneticisiyseniz, kendi rolünüzü Sahip'in altına düşüremez veya kendi hesabınızı silemezsiniz. Öncelikle başka bir kullanıcıyı Sahip olarak terfi ettirin. Bir yönetici, başka bir kullanıcının ağacının son sahibini değiştirebilir veya kaldırabilir, çünkü yeni birini atayabilir.

## Kullanıcı hesaplarını dışa ve içe aktar

Bu butonlar, [farklı bir Gramps Web örneğine geçiş yaparken](export.md) faydalıdır.

- **Kullanıcı detaylarını dışa aktar** (indirme simgesi) – tüm kullanıcı hesaplarını (şifreler olmadan, çünkü şifreler şifreli biçimde saklanır) içeren bir JSON dosyası indirir.
- **Kullanıcı hesaplarını içe aktar** (grup ekle simgesi) – daha önce dışa aktarılmış bir JSON dosyasını yükleyerek toplu olarak kullanıcı hesapları oluşturur. Tüm içe aktarılan kullanıcılar, şifreler aktarılamayacağı için "Şifremi unuttum" bağlantısı aracılığıyla yeni bir şifre belirlemek zorundadır.

## Kayıt bağlantısı (çoklu-ağaç kurulumu için)

Çoklu-ağaç kurulumunda yeni kullanıcılar için kayıt bağlantısı, kullanıcıları yönet sayfasının üst kısmında gösterilir. Bu bağlantıyı kopyalayabilir ve hesabını ağacınıza kaydetmek için davet etmek istediğiniz kişilerle paylaşabilirsiniz.

!!! not
    Tek ağaç kurulumunda giriş sayfasında genel bir "Kaydol" bağlantısı vardır; ağaç başına kayıt bağlantısı yalnızca çoklu-ağaç kurulumlarında gereklidir.

## AI sohbet izinleri

Eğer sunucuda AI sohbet etkinleştirildiyse, sayfanın üst kısmındaki açılır menü, hangi kullanıcı rollerinin sohbet özelliğini kullanabileceğini kontrol etmenizi sağlar:

- Herkes (misafirler dahil)
- Üye ve üzeri
- Katkıda Bulunan ve üzeri
- Editör ve üzeri
- Sadece sahipler ve yöneticiler
- Hiçbiri (tüm kullanıcılar için sohbeti devre dışı bırak)
