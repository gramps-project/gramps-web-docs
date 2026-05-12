# Yönetim Ayarları

**Ayarlar > Yönetim** sayfası, üst uygulama çubuğundaki kullanıcı simgesi aracılığıyla erişilebilir. Bu sayfa yalnızca Sahip veya Yönetici rolüne sahip kullanıcılara açıktır ve aile ağacı veritabanını yönetmek için araçlar sağlar.

## Kullanım kotaları

Sayfanın üst kısmı, yapılandırılmış herhangi bir sınıra göre mevcut kullanımı gösterir:

- **Kişiler** — ağaçtaki kişi nesnelerinin sayısı ile yapılandırılmış maksimum (sınırsızsa ∞)
- **Medya depolama** — yüklenen medya dosyalarının toplam boyutu ile yapılandırılmış depolama kotası (sınırsızsa ∞)

Kotalar sunucu yöneticisi tarafından ayarlanır; detaylar için [Sunucu yapılandırması](../install_setup/configuration.md) sayfasına bakın.

## Veri İçe Aktarma

İçe aktarma bölümü, bir aile ağacı dosyası veya bir medya arşivi yüklemenizi sağlar. Tam talimatlar için [Veri İçe Aktarma](import.md) sayfasına bakın.

## Medya dosyası durumu

Bu bölüm şunları gösterir:

- Ağaçtaki toplam medya nesne sayısı ve herhangi birinin kontrol toplamının eksik olup olmadığı
- Sunucudan kaybolan ilişkili dosyası olan medya nesnelerinin sayısı

Yeşil bir onay işareti, her şeyin yolunda olduğunu gösterir. Sorunlar tespit edilirse, etkilenen nesnelere bağlantılar gösterilir. Eksik kontrol toplamları genellikle medya referanslarını içeren ancak gerçek dosyaları içermeyen GEDCOM gibi bir formatta veri içe aktarıldığında meydana gelir. Eksik dosyalar, medya arşivini içe aktarma özelliği aracılığıyla yüklenebilir.

## Medya arşivini içe aktarma

Eksik dosyaları doldurmak için medya dosyalarının ZIP dosyasını yüklemeye olanak tanır. Tam talimatlar için [Veri İçe Aktarma](import.md) sayfasına bakın.

## Arama dizinini yönetme

Gramps Web, veriler değiştiğinde genellikle otomatik olarak güncellenen tam metin arama dizinini sürdürür. Durum göstergesi, şu anda dizinlenmiş nesne sayısını toplam nesne sayısına göre gösterir.

Tam bir yeniden oluşturma başlatmak için **Arama dizinini güncelle** butonuna tıklayın. Görev arka planda çalışırken bir ilerleme göstergesi gösterilir. Bu genellikle yalnızca bir sunucu yükseltmesinden sonra gereklidir.

### Anlamsal arama dizini

Eğer sunucuda [anlamsal (Yapay Zeka destekli) arama etkinse](../install_setup/configuration.md), iki işlemle birlikte ek bir bölüm görünür:

- **Anlamsal arama dizinini yeniden oluştur** — tüm anlamsal dizini sıfırdan yeniden oluşturur. Bu işlem hesaplama açısından maliyetlidir ve uzun zaman alabilir.
- **Anlamsal arama dizinini güncelle** — yalnızca henüz dizinlenmemiş nesneleri ekleyerek kısmi bir güncelleme yapar. Tam bir yeniden oluşturma işleminden daha hızlıdır.

## Aile Ağacı Adı

!!! note
    Ağacın yeniden adlandırılması, yalnızca [çoklu ağaç kurulumu](../install_setup/multi-tree.md) veya `TREE_ID`'nin [sunucu yapılandırmasında](../install_setup/configuration.md) açıkça ayarlandığı durumlarda çalışır. `TREE_ID` ayarlanmamış varsayılan tek ağaç kurulumunda, bu bir hata verecektir.

Bu, temel Gramps aile ağacı veritabanının adını değiştirmeye olanak tanır. Yeni bir ad girin ve uygulamak için **Yeniden Adlandır** butonuna tıklayın.

## Veritabanını Kontrol Et ve Onar

Bu araç, Gramps veritabanını içsel tutarsızlıklar için kontrol eder ve düzeltebildiklerini onarır — Gramps Masaüstü'ndeki [Veritabanını Kontrol Et ve Onar aracı](https://www.gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Tools#Check_and_Repair_Database) ile benzer şekilde.

**Kontrol Et ve Onar** butonuna tıklayın ve ilerleme göstergesinin tamamlanmasını bekleyin. Sonuç butonun altında gösterilir:

- Eğer hata bulunmazsa, bir onay mesajı görüntülenir.
- Eğer hatalar bulunursa, uygulanan düzeltmelerin özeti gösterilir.

Veritabanı tutarsızlıklarının neden olabileceği beklenmedik hatalar veya davranışlarla karşılaşırsanız bu aracı çalıştırın, örneğin nesneler arasındaki eksik ilişkiler gibi.

## Tehlike Bölgesi

!!! danger
    Tehlike Bölgesi'ndeki işlemler **geri alınamaz**. Devam etmeden önce bir yedek alın.

### Tüm nesneleri sil

Aile ağacından nesneleri kaldırır. **Sil** butonuna tıklamak, silmek için seçim yapabileceğiniz bir diyalog açar:

- **Tüm nesneler** — ağacı tamamen temizler
- **Belirli nesne türleri** — örneğin, yalnızca olaylar veya yalnızca medya nesneleri

İşlemi onaylamak için yeniden kimlik doğrulamanız (tekrar giriş yapmanız) istenecektir. Silme işlemi arka planda bir görev olarak çalışır ve bir ilerleme göstergesi gösterilir.

!!! warning
    Sadece nesne türlerinin bir alt kümesini silmek (tüm nesneleri bir anda silmek yerine) büyük ağaçlar için çok uzun sürebilir, çünkü sunucu nesneler arasındaki tüm ilişkileri kontrol etmek ve güncellemek zorundadır.

!!! tip
    Yeni bir ağaç içe aktarmadan önce sıfırdan başlamak veya yanlış içe aktarılan belirli nesne türlerini kaldırmak için bunu kullanın.
