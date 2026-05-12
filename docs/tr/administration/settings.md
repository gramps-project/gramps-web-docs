# Yönetim Ayarları

**Ayarlar > Yönetim** sayfasına üst uygulama çubuğundaki kullanıcı simgesi aracılığıyla erişilebilir. Bu sayfa yalnızca Sahip veya Yönetici rolüne sahip kullanıcılara açıktır ve aile ağacı veritabanını yönetmek için araçlar sağlar.

## Kullanım kotaları

Sayfanın üst kısmında, yapılandırılmış herhangi bir limite göre mevcut kullanım gösterilmektedir:

- **Kişiler** – ağaçtaki kişi nesnelerinin sayısı ile yapılandırılmış maksimum (sınırsızsa ∞)
- **Medya depolama** – yüklenen medya dosyalarının toplam boyutu ile yapılandırılmış depolama kotası (sınırsızsa ∞)

Kotalar sunucu yöneticisi tarafından ayarlanır; ayrıntılar için [Sunucu yapılandırması](../install_setup/configuration.md) sayfasına bakın.

## Veri içe aktarma

İçe aktarma bölümü, bir aile ağacı dosyası veya bir medya arşivi yüklemenizi sağlar. Tam talimatlar için [Veri içe aktarma](import.md) sayfasına bakın.

## Medya dosyası durumu

Bu bölümde gösterilir:

- Ağaçtaki toplam medya nesne sayısı ve herhangi birinin kontrol toplamının eksik olup olmadığı
- Sunucudan eksik olan ilişkili dosyaların sayısı

Yeşil bir onay işareti her şeyin yolunda olduğunu gösterir. Sorunlar tespit edilirse, etkilenen nesnelere bağlantılar gösterilir. Eksik kontrol toplamları genellikle, medya referanslarını içeren ancak gerçek dosyaları içermeyen GEDCOM gibi bir formattan veri içe aktarıldığında meydana gelir. Eksik dosyalar, medya arşivini içe aktarma özelliği aracılığıyla yüklenebilir.

## Medya arşivini içe aktarma

Eksik dosyaları doldurmak için medya dosyalarının ZIP dosyasını yüklemeye olanak tanır. Tam talimatlar için [Veri içe aktarma](import.md) sayfasına bakın.

## Arama dizinini yönetme

Gramps Web, veri değiştiğinde otomatik olarak güncellenen tam metin arama dizini tutar. Durum göstergesi, şu anda kaç nesnenin dizinlendiğini ve toplam nesne sayısını gösterir.

Tam bir yeniden oluşturma başlatmak için **Arama dizinini güncelle** butonuna tıklayın. Görev arka planda çalışırken bir ilerleme göstergesi gösterilir. Bu genellikle yalnızca bir sunucu yükseltmesinden sonra gereklidir.

### Anlamsal arama dizini

Eğer sunucuda [anlamsal (AI destekli) arama etkinse](../install_setup/configuration.md), iki eylem ile ek bir bölüm görünür:

- **Anlamsal arama dizinini yeniden oluştur** – tüm anlamsal dizini sıfırdan yeniden inşa eder. Bu hesaplama açısından maliyetlidir ve uzun zaman alabilir.
- **Anlamsal arama dizinini güncelle** – yalnızca henüz dizinlenmemiş nesneleri ekleyerek artımlı bir güncelleme gerçekleştirir. Tam bir yeniden oluşturma işleminden daha hızlıdır.

## Aile Ağacı adı

!!! note
    Ağacın yeniden adlandırılması yalnızca bir [çoklu ağaç kurulumu](../install_setup/multi-tree.md) veya `TREE_ID`'nin [sunucu yapılandırmasında](../install_setup/configuration.md) açıkça ayarlandığı durumlarda çalışır. `TREE_ID` ayarlanmamış varsayılan tek ağaç kurulumunda bu bir hata oluşturur.

Bu, temel Gramps aile ağacı veritabanının adını değiştirmeye olanak tanır. Yeni bir ad girin ve uygulamak için **Yeniden Adlandır** butonuna tıklayın.

## Veritabanını Kontrol Et ve Onar

Bu araç, Gramps veritabanını içsel tutarsızlıklar için kontrol eder ve mümkün olanları düzeltir – Gramps Masaüstündeki [Veritabanını Kontrol Et ve Onar aracı](https://www.gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Tools#Check_and_Repair_Database) ile benzerlik gösterir.

**Kontrol Et ve Onar** butonuna tıklayın ve ilerleme göstergesinin tamamlanmasını bekleyin. Sonuç butonun altında gösterilir:

- Hata bulunmazsa, bir onay mesajı görüntülenir.
- Hatalar bulunursa, uygulanan düzeltmelerin bir özeti gösterilir.

Veritabanı tutarsızlıklarının neden olabileceği beklenmedik hatalar veya davranışlarla karşılaşırsanız bu aracı çalıştırın; örneğin, nesneler arasında eksik ilişkiler gibi.

## Tehlike Bölgesi

!!! danger
    Tehlike Bölgesi'ndeki işlemler **geri alınamaz**. Devam etmeden önce bir yedek alın.

### Tüm nesneleri sil

Aile ağacından nesneleri kaldırır. **Sil** butonuna tıkladığınızda, silmek için seçebileceğiniz bir iletişim kutusu açılır:

- **Tüm nesneler** – ağacı tamamen temizler
- **Belirli nesne türleri** – örneğin, yalnızca olaylar veya yalnızca medya nesneleri

İşlemi onaylamak için yeniden kimlik doğrulamanız (yeniden giriş yapmanız) istenecektir. Silme işlemi arka planda bir görev olarak çalışır ve bir ilerleme göstergesi gösterilir.

!!! warning
    Sadece nesne türlerinin bir alt kümesini silmek (tüm nesneleri bir anda silmek yerine) büyük ağaçlar için çok uzun sürebilir, çünkü sunucu nesneler arasındaki tüm ilişkileri kontrol etmek ve güncellemek zorundadır.

!!! tip
    Yeni bir ağaç içe aktarmadan önce taze bir başlangıç yapmak veya yanlış içe aktarılan belirli nesne türlerini kaldırmak için bunu kullanın.
