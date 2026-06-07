# Yönetim Ayarları

**Ayarlar > Yönetim** sayfası, üst uygulama çubuğundaki kullanıcı simgesi aracılığıyla erişilebilir. Sadece Sahip veya Yönetici rolüne sahip kullanıcılara açıktır ve aile ağacı veritabanını yönetmek için araçlar sağlar.

Sayfa, katlanabilir bölümler halinde düzenlenmiştir. Bir bölüm başlığına tıklayarak genişletebilirsiniz.

## Veri

Kullanım kotalarını, veri içe aktarmayı ve medya dosyası yönetimini kapsar.

### Kullanım kotaları

Bölümün üst kısmı, yapılandırılmış herhangi bir sınırla ilgili mevcut kullanımı gösterir:

- **Kişiler** – ağaçtaki kişi nesnelerinin sayısı ile yapılandırılmış maksimum (sınırsızsa ∞)
- **Medya depolama** – yüklenen medya dosyalarının toplam boyutu ile yapılandırılmış depolama kotası (sınırsızsa ∞)

Kotalar, sunucu yöneticisi tarafından ayarlanır; detaylar için [Sunucu yapılandırması](../install_setup/configuration.md) sayfasına bakın.

### Veri içe aktarma

İçe aktarma bölümü, bir aile ağacı dosyası veya bir medya arşivi yüklemenize olanak tanır. Tam talimatlar için [Veri içe aktarma](import.md) sayfasına bakın.

### Medya dosyası durumu

Bu bölüm şunları gösterir:

- Ağaçtaki toplam medya nesne sayısı ve herhangi birinin kontrol toplamının eksik olup olmadığı
- Sunucudan eksik olan ilişkili dosyaların sayısı

Yeşil bir onay işareti her şeyin yolunda olduğunu gösterir. Sorunlar tespit edilirse, etkilenen nesnelere bağlantılar gösterilir. Eksik kontrol toplamları genellikle medya referanslarını içeren ancak gerçek dosyaları içermeyen GEDCOM gibi bir formatta veri içe aktarıldığında meydana gelir. Eksik dosyalar, medya arşivini içe aktarma özelliği aracılığıyla yüklenebilir.

### Medya arşivini içe aktarma

Eksik dosyaları doldurmak için medya dosyalarının bulunduğu bir ZIP dosyasını yüklemeye olanak tanır. Tam talimatlar için [Veri içe aktarma](import.md) sayfasına bakın.

## Arama dizini

### Arama dizinini yönetme

Gramps Web, veriler değiştiğinde otomatik olarak güncellenen tam metin arama dizini tutar. Durum göstergesi, şu anda kaç nesnenin dizinlendiğini ve toplam nesne sayısını gösterir.

Tam bir yeniden oluşturma tetiklemek için **Arama dizinini güncelle** butonuna tıklayın. Görev arka planda çalışırken bir ilerleme göstergesi gösterilir. Bu genellikle yalnızca bir sunucu yükseltmesinden sonra gereklidir.

### Anlamsal arama dizini

Eğer sunucuda [anlamsal (AI destekli) arama etkinse](../install_setup/configuration.md), iki işlemle birlikte ek bir bölüm görünür:

- **Anlamsal arama dizinini yeniden oluştur** – tüm anlamsal dizini sıfırdan yeniden oluşturur. Bu işlem hesaplama açısından maliyetlidir ve uzun sürebilir.
- **Anlamsal arama dizinini güncelle** – yalnızca henüz dizinlenmemiş nesneleri ekleyerek artımlı bir güncelleme gerçekleştirir. Tam bir yeniden oluşturma işleminden daha hızlıdır.

## Ağaç ayarları

### Aile Ağacı adı

!!! not
    Ağacın yeniden adlandırılması yalnızca bir [çoklu-ağaç kurulumunda](../install_setup/multi-tree.md) veya `TREE_ID` açıkça [sunucu yapılandırmasında](../install_setup/configuration.md) ayarlandığında çalışır. `TREE_ID` ayarlanmadan varsayılan tek ağaç kurulumunda bu bir hata oluşturur.

Bu, temel Gramps aile ağacı veritabanının adını değiştirmeye olanak tanır. Yeni bir ad girin ve uygulamak için **Yeniden Adlandır** butonuna tıklayın.

!!! ipucu
    Eğer veritabanının adını değiştirmeden yalnızca uygulama çubuğunda gösterilen adı değiştirmek istiyorsanız, bunun yerine [Uygulama başlığı](#app-title) ayarını kullanın.

### Araştırmacı Bilgileri

Ana araştırmacının adını, adresini ve iletişim bilgilerini ayarlayın. Bu bilgiler, dışa aktarımlarda (örneğin GEDCOM dosyaları) yer alır.

## Özelleştirme

### Tema renkleri

Gramps Web arayüzü için özel bir **birincil renk** ve **vurgulayıcı renk** ayarlayın. Bu renkler, bu ağacın tüm kullanıcılarına uygulanır ve kaydedildikten hemen sonra etkili olur.

Renk seçicileri kullanarak renkleri seçin, ardından **Kaydet** butonuna tıklayın. Varsayılan ayarlara geri dönmek için **Sıfırla** butonuna tıklayın.

### Uygulama başlığı

Uygulama için özel bir başlık ayarlayın. Ayarlandığında, bu, tarayıcı başlık çubuğundaki aile ağacı adını ve üst uygulama çubuğunu geçersiz kılar.

Bir başlık girin ve **Kaydet** butonuna tıklayın. Varsayılanı kullanmak için boş bırakın (aile ağacı adı).

### Ana sayfa notu

Gösterilecek bir Gramps **Not** nesnesi seçin. Not içeriği, ana gösterge paneli sütunlarının altında render edilir ve ağaç erişimi olan tüm kullanıcılar tarafından görünür.

Bir not aramak ve seçmek için nesne seçicisini kullanın, ardından kaydedin. Mevcut ana sayfa notasını temizlemek için **Kaldır** butonuna tıklayın.

### Ana sayfa resmi

Gösterge paneli ana sayfasında bir resim olarak görüntülenecek bir Gramps **Medya** nesnesi seçin. Ana sayfa notu ile birleştirildiğinde, resim not metninin yanında görünür. Not olmadan yalnızca resim gösterilir.

Bir medya nesnesini aramak ve seçmek için nesne seçicisini kullanın, ardından kaydedin. Mevcut ana sayfa resmini temizlemek için **Kaldır** butonuna tıklayın.

### Dışa Aktarma/İçe Aktarma ayarları

Ağaç düzeyindeki ayarlar (uygulama başlığı, tema renkleri, ana sayfa notu/resmi vb.) yedekleme veya başka bir Gramps Web örneğine kopyalamak için JSON dosyası olarak dışa aktarılabilir.

- Mevcut ayarları JSON dosyası olarak indirmek için **Ayarları Dışa Aktar** butonuna tıklayın.
- Daha önce dışa aktarılan bir JSON dosyasını yüklemek ve ayarları uygulamak için **Ağaç ayarlarını İçe Aktar** butonuna tıklayın.

## Aile Ağacı İşleme

### Veritabanını Kontrol Et ve Onar

Bu araç, Gramps veritabanını içsel tutarsızlıklar için kontrol eder ve mümkün olanları düzeltir – Gramps Masaüstü'ndeki [Veritabanını Kontrol Et ve Onar aracı](https://www.gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Tools#Check_and_Repair_Database) ile benzerlik gösterir.

**Kontrol Et ve Onar** butonuna tıklayın ve ilerleme göstergesinin tamamlanmasını bekleyin. Sonuç butonun altında gösterilir:

- Eğer hata bulunmadıysa, bir onay mesajı görüntülenir.
- Eğer hatalar bulunduysa, uygulanan düzeltmelerin özeti gösterilir.

Beklenmedik hatalar veya nesneler arasındaki ilişkilerin eksik olduğu gibi veritabanı tutarsızlıklarından kaynaklanabilecek davranışlarla karşılaşırsanız bu aracı çalıştırın.

## Etiketler

### Etiketleri yönetme

Aile ağacı için [etiketler](../user-guide/tags.md) oluşturun, yeniden adlandırın, renk değiştirin ve silin. Etiketler, Gramps veritabanında saklanır, tüm kullanıcılar arasında paylaşılır ve Gramps Masaüstü ile tamamen uyumludur.

Bir etiket oluşturmak için **Yeni Etiket** butonuna tıklayın. Mevcut bir etiketin yanındaki kontrolleri kullanarak onu yeniden adlandırabilir (kalem simgesi), rengini değiştirebilir (renk seçici) veya silebilirsiniz (silme simgesi).

!!! not
    Bir etiketi silmek, uygulandığı tüm nesnelerden kaldırır.

Etiketlerin Gramps Web'de nasıl kullanıldığı hakkında daha fazla bilgi için [Etiketler](../user-guide/tags.md) sayfasına bakın; özel `Blog` ve `ToDo` etiketleri de dahil.

## Tehlike Bölgesi

!!! tehlike
    Tehlike Bölgesi'ndeki işlemler **geri alınamaz**. Devam etmeden önce bir yedek alın.

### Tüm nesneleri sil

Aile ağacından nesneleri kaldırır. **Sil** butonuna tıkladığınızda, silmek için seçebileceğiniz bir diyalog açılır:

- **Tüm nesneler** – ağacı tamamen temizler
- **Belirli nesne türleri** – örneğin, yalnızca olaylar veya yalnızca medya nesneleri

İşlemi onaylamak için yeniden kimlik doğrulamanız (yeniden giriş yapmanız) istenecektir. Silme işlemi arka planda bir görev olarak çalışır ve bir ilerleme göstergesi gösterilir.

!!! uyarı
    Yalnızca bir nesne türü alt kümesini silmek (tüm nesneleri bir kerede silmek yerine) büyük ağaçlar için çok uzun sürebilir, çünkü sunucu tüm nesneler arasındaki ilişkileri kontrol edip güncellemek zorundadır.

!!! ipucu
    Yeni bir ağaç içe aktarmadan önce taze bir başlangıç yapmak veya yanlış içe aktarılan belirli nesne türlerini kaldırmak için bunu kullanın.
