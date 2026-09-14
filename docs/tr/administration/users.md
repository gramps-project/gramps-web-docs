# Kullanıcıları Yönet

Kullanıcı yönetim arayüzü **Ayarlar > Kullanıcıları Yönet** (üst uygulama çubuğundaki kullanıcı simgesi) üzerinden erişilebilir. Sadece Sahip veya Yönetici rolüne sahip kullanıcılara açıktır.

## Kullanıcı rolleri

Mevcut kullanıcı rolleri ve izinleri hakkında tam açıklama için [Kullanıcı sistemi](../install_setup/users.md) sayfasına bakın.

## Kullanıcıları görüntüle ve filtrele

Kullanıcıları yönet sayfası, aşağıdaki sütunlarla birlikte tüm kayıtlı kullanıcı hesaplarının bir tablosunu gösterir:

- **Kullanıcı Adı** – giriş adı
- **Tam İsim** – görüntüleme adı
- **E-posta** – kullanıcının e-posta adresi
- **Rol** – atanan rol (Misafir, Üye, Katkıda Bulunan, Editör, Sahip veya Yönetici)
- **Hesap Kaynağı** – "Şifre" (yerel hesap) veya bir dış kimlik sağlayıcısının adı (örneğin, OIDC kullanıldığında)

Listeyi filtrelemek için tablonun üst kısmındaki arama alanını ve rol açılır menüsünü kullanın. Tüm filtreleri sıfırlamak için filtre temizleme butonuna tıklayın.

## Bir kullanıcıyı düzenle

Herhangi bir satırdaki düzenleme (kalem) simgesine tıklayarak düzenleme iletişim kutusunu açın. Kullanıcının:

- Tam adını
- E-posta adresini
- Rolünü

değiştirebilirsiniz.

Bu, **yeni kendinden kayıtlı bir kullanıcıyı etkinleştirmenin** birincil yoludur: rolünü *devre dışı* durumdan herhangi bir aktif role (örneğin, Üye veya Editör) değiştirin.

E-posta adreslerinin benzersiz olması gerekmez (Gramps Web API 3.22'den itibaren), bu nedenle birkaç hesap aynı adresi paylaşabilir.

## Bir kullanıcıyı manuel olarak ekle

Kullanıcıları yönet tablosunun üstündeki **kullanıcı ekle** (kişi ekle) simgesine tıklayarak yeni bir kullanıcı hesabı oluşturun. İletişim kutusuna kullanıcı adını, tam adını, e-posta adresini, şifreyi ve rolü doldurun ve **Kaydet** butonuna tıklayın.

## Bir kullanıcıyı sil

Herhangi bir satırdaki silme (çöp) simgesine tıklayın ve iletişim kutusunu onaylayın. Bu işlem geri alınamaz.

!!! not
    Bir ağacın yönetiminden sorumlu kimse kalmamasını önlemek için, kendi rolünüzü Sahip'in altına düşüremez veya eğer ağacın tek Sahibi veya Yöneticisiyseniz kendi hesabınızı silemezsiniz. Önce başka bir kullanıcıyı Sahip olarak terfi ettirin. Bir yönetici, başka bir kullanıcının ağacının son sahibini değiştirebilir veya kaldırabilir, çünkü yeni birini atayabilir.

## Kullanıcı hesaplarını dışa ve içe aktar

Bu butonlar, [farklı bir Gramps Web örneğine geçiş yaparken](export.md) kullanışlıdır.

- **Kullanıcı detaylarını dışa aktar** (indirme simgesi) – tüm kullanıcı hesaplarını (şifreler dahil değil, çünkü şifreler şifreli formda saklanır) içeren bir JSON dosyası indirir.
- **Kullanıcı hesaplarını içe aktar** (grup ekle simgesi) – daha önce dışa aktarılmış bir JSON dosyasını yükleyerek toplu olarak kullanıcı hesapları oluşturur. Tüm içe aktarılan kullanıcıların şifrelerini "Şifremi unuttum" bağlantısı aracılığıyla ayarlamaları gerekecektir, çünkü şifreler transfer edilemez.

## Kayıt bağlantısı (çoklu ağaç kurulumu için)

Çoklu ağaç kurulumunda, yeni kullanıcılar için kayıt bağlantısı kullanıcıları yönet sayfasının üst kısmında gösterilir. Bu bağlantıyı kopyalayabilir ve hesabını ağacınıza kaydetmek için davet etmek istediğiniz kişilerle paylaşabilirsiniz.

!!! not
    Tek ağaç kurulumunda giriş sayfasında genel bir "Kaydol" bağlantısı vardır; ağaç başına kayıt bağlantısı yalnızca çoklu ağaç kurulumlarında gereklidir.

## AI sohbet izinleri

Eğer sunucuda AI sohbet etkinleştirildiyse, sayfanın üst kısmındaki bir açılır menü, hangi kullanıcı rollerinin sohbet özelliğini kullanabileceğini kontrol etmenizi sağlar:

- Herkes (misafirler dahil)
- Üye ve üzeri
- Katkıda bulunan ve üzeri
- Editör ve üzeri
- Sadece sahipler ve yöneticiler
- Hiç kimse (tüm kullanıcılar için sohbeti devre dışı bırak)
