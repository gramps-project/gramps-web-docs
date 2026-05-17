# Yönetim Ayarları

**Ayarlar > Yönetim** sayfası, üst uygulama çubuğundaki kullanıcı simgesi aracılığıyla erişilebilir. Bu sayfa yalnızca Sahip veya Yönetici rolüne sahip kullanıcılara açıktır ve aile ağacı veritabanını yönetmek için araçlar sağlar.

Sayfa, katlanabilir bölümlere organize edilmiştir. Bir bölüm başlığına tıklayarak genişletebilirsiniz.

## Veri

Kullanım kotalarını, veri içe aktarmayı ve medya dosyası yönetimini kapsar.

### Kullanım kotaları

Bölümün üst kısmı, yapılandırılmış limitlere göre mevcut kullanımı gösterir:

- **Kişiler** – ağaçtaki kişi nesnelerinin sayısı ile yapılandırılmış maksimum (sınırsızsa ∞)
- **Medya depolama** – yüklenen medya dosyalarının toplam boyutu ile yapılandırılmış depolama kotası (sınırsızsa ∞)

Kotalar sunucu yöneticisi tarafından ayarlanır; ayrıntılar için [Sunucu yapılandırması](../install_setup/configuration.md) sayfasına bakın.

### Veri içe aktar

İçe aktarma bölümü, bir aile ağacı dosyası veya medya arşivi yüklemenize olanak tanır. Tam talimatlar için [Veri içe aktar](import.md) sayfasına bakın.

### Medya dosyası durumu

Bu bölüm şunları gösterir:

- Ağaçtaki toplam medya nesne sayısı ve herhangi birinin kontrol toplamının eksik olup olmadığı
- Sunucudan eksik olan ilişkili dosyaların sayısı

Yeşil onay işareti, her şeyin yolunda olduğunu gösterir. Problemler tespit edilirse, etkilenen nesnelere bağlantılar gösterilir. Eksik kontrol toplamları genellikle, medya referanslarını içeren ancak gerçek dosyaları içermeyen GEDCOM gibi bir formatta veri içe aktarıldığında ortaya çıkar. Eksik dosyalar, medya arşivini içe aktarma özelliği aracılığıyla yüklenebilir.

### Medya arşivini içe aktar

Eksik dosyaları doldurmak için medya dosyalarının bulunduğu bir ZIP dosyası yüklemeye olanak tanır. Tam talimatlar için [Veri içe aktar](import.md) sayfasına bakın.

## Arama dizini

### Arama dizinini yönet

Gramps Web, veri değiştiğinde genellikle otomatik olarak güncellenen tam metin arama dizini tutar. Durum göstergesi, şu anda kaç nesnenin dizinlendiğini ve toplam nesne sayısını gösterir.

Tam bir yeniden inşa tetiklemek için **Arama dizinini güncelle** butonuna tıklayın. Görev arka planda çalışırken bir ilerleme göstergesi gösterilir. Bu genellikle yalnızca bir sunucu yükseltmesinden sonra gereklidir.

### Anlamsal arama dizini

Eğer sunucuda [anlamsal (AI destekli) arama etkinleştirilmişse](../install_setup/configuration.md), iki eylemle birlikte ek bir bölüm görünür:

- **Anlamsal arama dizinini yeniden oluştur** – tüm anlamsal dizini sıfırdan yeniden inşa eder. Bu işlem hesaplama açısından maliyetlidir ve uzun sürebilir.
- **Anlamsal arama dizinini güncelle** – yalnızca henüz dizinlenmemiş nesneleri ekleyerek artımlı bir güncelleme yapar. Tam bir yeniden inşa işleminden daha hızlıdır.

## Ağaç ayarları

### Aile Ağacı adı

!!! note
    Ağacın yeniden adlandırılması yalnızca bir [çoklu-ağaç kurulumu](../install_setup/multi-tree.md) veya `TREE_ID` açıkça [sunucu yapılandırmasında](../install_setup/configuration.md) ayarlandığında çalışır. `TREE_ID` ayarlanmadığı varsayılan tek-ağaç kurulumunda bu bir hata oluşturur.

Bu, temel Gramps aile ağacı veritabanının adını değiştirmeye olanak tanır. Yeni bir ad girin ve uygulamak için **Yeniden Adlandır** butonuna tıklayın.

!!! tip
    Veritabanının adını değiştirmeden yalnızca uygulama çubuğunda gösterilen adı değiştirmek istiyorsanız, bunun yerine [Uygulama başlığı](#app-title) ayarını kullanın.

### Araştırmacı Bilgileri

Ana araştırmacının adını, adresini ve iletişim bilgilerini ayarlayın. Bu bilgiler, dışa aktarımlarda (örneğin GEDCOM dosyaları) gömülüdür.

## Özelleştirme

### Tema renkleri

Gramps Web arayüzü için özel bir **birincil renk** ve **vurgulayıcı renk** ayarlayın. Bu renkler, bu ağacın tüm kullanıcılarına uygulanır ve kaydedildikten hemen sonra etkili olur.

Renk seçicileri kullanarak renkleri seçin, ardından **Kaydet** butonuna tıklayın. Varsayılan ayarlara geri dönmek için **Sıfırla** butonuna tıklayın.

### Uygulama başlığı

Uygulama için özel bir başlık ayarlayın. Eğer ayarlanmışsa, bu, tarayıcı başlık çubuğundaki aile ağacı adını geçersiz kılar.

Bir başlık girin ve **Kaydet** butonuna tıklayın. Varsayılanı kullanmak için boş bırakın (aile ağacı adı).

### Ana sayfa notu

Gösterilecek bir Gramps **Not** nesnesi seçin. Not içeriği, ana gösterge panosu sütunlarının altında render edilir ve ağaç erişimi olan tüm kullanıcılar tarafından görünür.

Bir not aramak ve seçmek için nesne seçicisini kullanın, ardından kaydedin. Mevcut ana sayfa notasını temizlemek için **Kaldır** butonuna tıklayın.

### Ana sayfa resmi

Gösterge panosu ana sayfasında bir resim olarak görüntülenecek bir Gramps **Medya** nesnesi seçin. Ana sayfa notu ile birleştirildiğinde, resim not metninin yanında görünür. Bir not olmadan, yalnızca resim gösterilir.

Bir medya nesnesini aramak ve seçmek için nesne seçicisini kullanın, ardından kaydedin. Mevcut ana sayfa resmini temizlemek için **Kaldır** butonuna tıklayın.

### Dışa Aktarma/İçe Aktarma ayarları

Ağaç düzeyindeki ayarlar (uygulama başlığı, tema renkleri, ana sayfa notu/resmi vb.) yedekleme veya başka bir Gramps Web örneğine kopyalama için bir JSON dosyası olarak dışa aktarılabilir.

- Mevcut ayarları JSON dosyası olarak indirmek için **Ayarları dışa aktar** butonuna tıklayın.
- Daha önce dışa aktarılmış bir JSON dosyasını yüklemek ve ayarları uygulamak için **Ağaç ayarlarını içe aktar** butonuna tıklayın.

## Aile Ağacı İşleme

### Veritabanını Kontrol Et ve Onar

Bu araç, Gramps veritabanını içsel tutarsızlıklar için kontrol eder ve düzeltebildiklerini düzeltir – Gramps Masaüstü'ndeki [Veritabanını Kontrol Et ve Onar aracı](https://www.gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Tools#Check_and_Repair_Database) ile benzerlik gösterir.

**Kontrol Et ve Onar** butonuna tıklayın ve ilerleme göstergesinin tamamlanmasını bekleyin. Sonuç butonun altında gösterilir:

- Eğer hata bulunmazsa, bir onay mesajı görüntülenir.
- Eğer hatalar bulunursa, uygulanan düzeltmelerin bir özeti gösterilir.

Beklenmedik hatalar veya nesneler arasındaki eksik ilişkiler gibi veritabanı tutarsızlıklarından kaynaklanabilecek davranışlarla karşılaşırsanız bu aracı çalıştırın.

## Tehlike Bölgesi

!!! danger
    Tehlike Bölgesindeki eylemler **geri alınamaz**. Devam etmeden önce bir yedek alın.

### Tüm nesneleri sil

Aile ağacından nesneleri kaldırır. **Sil** butonuna tıkladığınızda, silmek için seçebileceğiniz bir diyalog açılır:

- **Tüm nesneler** – ağacı tamamen temizler
- **Belirli nesne türleri** – örneğin, yalnızca olaylar veya yalnızca medya nesneleri

Eylemi onaylamak için yeniden kimlik doğrulamanız (tekrar giriş yapmanız) istenecektir. Silme işlemi arka planda bir görev olarak çalışır ve bir ilerleme göstergesi gösterilir.

!!! warning
    Yalnızca nesne türlerinin bir alt kümesini silmek (tüm nesneleri bir anda silmek yerine) büyük ağaçlar için çok uzun sürebilir, çünkü sunucu tüm nesneler arasındaki ilişkileri kontrol etmek ve güncellemek zorundadır.

!!! tip
    Yeni bir ağaç içe aktarmadan önce taze bir başlangıç yapmak veya yanlış içe aktarılan belirli nesne türlerini kaldırmak için bunu kullanın.
