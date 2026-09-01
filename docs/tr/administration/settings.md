# Yönetim Ayarları

**Ayarlar > Yönetim** sayfasına üst uygulama çubuğundaki kullanıcı simgesi aracılığıyla erişilebilir. Bu sayfa yalnızca Sahip veya Yönetici rolüne sahip kullanıcılara açıktır ve aile ağacı veritabanını yönetmek için araçlar sağlar.

Sayfa, katlanabilir bölümlere organize edilmiştir. Bir bölüm başlığına tıklayarak genişletebilirsiniz.

## Veri

Kullanım kotalarını, veri içe aktarmayı ve medya dosyası yönetimini kapsar.

### Kullanım kotaları

Bölümün üst kısmında, yapılandırılmış limitlere göre mevcut kullanım gösterilmektedir:

- **Kişiler** – ağaçtaki kişi nesnelerinin sayısı ile yapılandırılmış maksimum (sınırsızsa ∞)
- **Medya depolama** – yüklenen medya dosyalarının toplam boyutu ile yapılandırılmış depolama kotası (sınırsızsa ∞)

Kotalar, sunucu yöneticisi tarafından belirlenir; ayrıntılar için [Sunucu yapılandırması](../install_setup/configuration.md) sayfasına bakın.

### Veri içe aktar

İçe aktarma bölümü, bir aile ağacı dosyası veya bir medya arşivi yüklemenizi sağlar. Tam talimatlar için [Veri içe aktar](import.md) sayfasına bakın.

### Medya dosyası durumu

Bu bölüm şunları gösterir:

- Ağaçtaki toplam medya nesne sayısı ve herhangi birinin kontrol toplamının eksik olup olmadığı
- Sunucudan eksik olan dosyaya sahip medya nesnelerinin sayısı

Yeşil bir onay işareti her şeyin yolunda olduğunu gösterir. Problemler tespit edilirse, etkilenen nesnelere bağlantılar gösterilir. Eksik kontrol toplamları genellikle, medya referanslarını içeren ancak gerçek dosyaları içermeyen GEDCOM gibi bir formatta veri içe aktarıldığında meydana gelir. Eksik dosyalar, medya arşivini içe aktarma özelliği aracılığıyla yüklenebilir.

### Medya arşivini içe aktar

Eksik dosyaları doldurmak için medya dosyalarının bir ZIP dosyasını yüklemeyi sağlar. Tam talimatlar için [Veri içe aktar](import.md) sayfasına bakın.

## Arama dizini

### Arama dizinini yönet

Gramps Web, veriler değiştiğinde otomatik olarak güncellenen tam metin arama dizini tutar. Durum göstergesi, şu anda kaç nesnenin dizinlendiğini ve toplam nesne sayısını gösterir.

Tam bir yeniden oluşturmayı tetiklemek için **Arama dizinini güncelle** butonuna tıklayın. Görev arka planda çalışırken bir ilerleme göstergesi görünür. Bu genellikle yalnızca bir sunucu yükseltmesinden sonra gereklidir.

### Anlamsal arama dizini

Eğer sunucuda [anlamsal (Yapay Zeka destekli) arama etkinse](../install_setup/configuration.md), iki işlemle birlikte ek bir bölüm görünür:

- **Anlamsal arama dizinini yeniden oluştur** – tüm anlamsal dizini sıfırdan yeniden oluşturur. Bu hesaplama açısından maliyetlidir ve uzun sürebilir.
- **Anlamsal arama dizinini güncelle** – yalnızca henüz dizinlenmemiş nesneleri ekleyerek artımlı bir güncelleme yapar. Tam bir yeniden oluşturma işleminden daha hızlıdır.

## Ağaç ayarları

### Aile Ağacı adı

!!! note
    Ağacın yeniden adlandırılması yalnızca bir [çoklu ağaç kurulumu](../install_setup/multi-tree.md) veya `TREE_ID`'nin [sunucu yapılandırmasında](../install_setup/configuration.md) açıkça ayarlandığı durumlarda çalışır. `TREE_ID` ayarlanmamış varsayılan tek ağaç kurulumunda bu bir hata oluşturur.

Bu, temel Gramps aile ağacı veritabanının adını değiştirmeyi sağlar. Yeni bir ad girin ve uygulamak için **Yeniden Adlandır** butonuna tıklayın.

!!! tip
    Eğer yalnızca uygulama çubuğunda gösterilen adı değiştirmek istiyorsanız, veritabanını yeniden adlandırmadan [Uygulama başlığı](#app-title) ayarını kullanın.

### Araştırmacı Bilgileri

Ana araştırmacının adını, adresini ve iletişim bilgilerini ayarlayın. Bu bilgiler, dışa aktarımlarda (örneğin GEDCOM dosyaları) gömülü olarak bulunur.

## Özelleştirme

### Tema renkleri

Gramps Web arayüzü için özel bir **birincil renk** ve **vurgulu renk** ayarlayın. Bu renkler, bu ağacın tüm kullanıcılarına uygulanır ve kaydedildikten hemen sonra etkili olur.

Renk seçicileri kullanarak renkleri seçin, ardından **Kaydet** butonuna tıklayın. Varsayılan ayarlara geri dönmek için **Sıfırla** butonuna tıklayın.

### Uygulama başlığı

Uygulama için özel bir başlık ayarlayın. Eğer ayarlanırsa, bu tarayıcı başlık çubuğundaki aile ağacı adını geçersiz kılar.

Bir başlık girin ve **Kaydet** butonuna tıklayın. Varsayılanı kullanmak için boş bırakın (aile ağacı adı).

### Ana sayfa notu

Gösterilecek bir Gramps **Not** nesnesi seçin. Not içeriği, ana gösterge panosu sütunlarının altında render edilir ve ağaç erişimi olan tüm kullanıcılar tarafından görünür.

Bir not aramak ve seçmek için nesne seçicisini kullanın, ardından kaydedin. Mevcut ana sayfa notunu temizlemek için **Kaldır** butonuna tıklayın.

### Ana sayfa resmi

Gösterge panosu ana sayfasında görüntü olarak gösterilecek bir Gramps **Medya** nesnesi seçin. Ana sayfa notu ile birleştirildiğinde, resim not metninin yanında görünür. Not olmadan yalnızca resim gösterilir.

Bir medya nesnesini aramak ve seçmek için nesne seçicisini kullanın, ardından kaydedin. Mevcut ana sayfa resmini temizlemek için **Kaldır** butonuna tıklayın.

### Dışa Aktarma/Içe Aktarma ayarları

Ağaç düzeyindeki ayarlar (uygulama başlığı, tema renkleri, ana sayfa notu/resmi vb.) yedekleme veya başka bir Gramps Web örneğine kopyalamak için bir JSON dosyası olarak dışa aktarılabilir.

- Mevcut ayarları JSON dosyası olarak indirmek için **Ayarları Dışa Aktar** butonuna tıklayın.
- Daha önce dışa aktarılmış bir JSON dosyasını yüklemek ve ayarları uygulamak için **Ağaç ayarlarını İçe Aktar** butonuna tıklayın.

## Aile Ağacı İşleme

### Veritabanını Kontrol Et ve Onar

Bu araç, Gramps veritabanını içsel tutarsızlıklar için kontrol eder ve düzeltebildiklerini onarır – Gramps Masaüstündeki [Veritabanını Kontrol Et ve Onar aracı](https://www.gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Tools#Check_and_Repair_Database) ile benzerlik gösterir.

**Kontrol Et ve Onar** butonuna tıklayın ve ilerleme göstergesinin tamamlanmasını bekleyin. Sonuç butonun altında gösterilir:

- Eğer hata bulunmadıysa, bir onay mesajı görüntülenir.
- Eğer hatalar bulunduysa, uygulanan düzeltmelerin bir özeti gösterilir.

Eğer beklenmedik hatalar veya nesneler arasındaki eksik ilişkiler gibi veritabanı tutarsızlıklarından kaynaklanabilecek davranışlarla karşılaşırsanız bu aracı çalıştırın.

### Veriyi Doğrula

[Veritabanını Kontrol Et ve Onar](#check-and-repair-database) *teknik* tutarsızlıkları ararken, bu araç *plausible* olmayan verileri arar – Gramps Masaüstündeki [Veriyi Doğrula aracı](https://gramps-project.org/wiki/index.php/Gramps_5.0_Wiki_Manual_-_Tools#Verify_the_Data) ile benzerlik gösterir. Bu, imkansız olmayan ancak bir göz atmaya değer kadar olası olmayan şeyleri rapor eder, örneğin 12 yaşında bir anne veya 130 yaşına kadar yaşayan bir kişi.

**Seçenekler** altında, testlerin kullandığı eşikleri ayarlayabilirsiniz – maksimum yaş, evlenmek veya çocuk sahibi olmak için minimum ve maksimum yaş, maksimum çocuk sayısı vb. – ayrıca eksik veya belirsiz tarihleri tahmin edip etmeyeceğinizi ve 31 Şubat gibi geçersiz tarihleri raporlama isteğinizi de ayarlayabilirsiniz.

Başlamak için **Veriyi Doğrula** butonuna tıklayın. Kontrol, arka planda bir görev olarak çalışır ve bulgular daha sonra **Veri Doğrulama Sonuçları** altında listelenir. Bu araç hiçbir şeyi değiştirmez: yalnızca bulduklarını rapor eder.

!!! note
    Bir bulgu, bir hatanın kanıtı değildir. Uzun yaşamlar ve büyük yaş farkları meydana gelebilir, bu nedenle sonuçları düzeltilecek şeyler listesi yerine kontrol edilecek şeyler listesi olarak değerlendirin.

## Etiketler

### Etiketleri yönet

Aile ağacı için [etiketler](../user-guide/tags.md) oluşturun, yeniden adlandırın, renklerini değiştirin ve silin. Etiketler, Gramps veritabanında saklanır, tüm kullanıcılar arasında paylaşılır ve Gramps Masaüstü ile tamamen uyumludur.

Bir etiket oluşturmak için **Yeni Etiket** butonuna tıklayın. Mevcut bir etiketin yanındaki kontrolleri kullanarak onu yeniden adlandırın (kalem simgesi), rengini değiştirin (renk seçici) veya silin (silme simgesi).

!!! note
    Bir etiketi silmek, onu uygulandığı tüm nesnelerden kaldırır.

Etiketlerin Gramps Web'de nasıl kullanıldığına dair daha fazla bilgi için [Etiketler](../user-guide/tags.md) sayfasına bakın; özel `Blog` ve `ToDo` etiketleri de dahil.

## Tehlike Bölgesi

!!! danger
    Tehlike Bölgesindeki işlemler **geri alınamaz**. Devam etmeden önce bir yedek alın.

### Tüm nesneleri sil

Aile ağacından nesneleri kaldırır. **Sil** butonuna tıklamak, silmek için seçebileceğiniz bir diyalog açar:

- **Tüm nesneler** – ağacı tamamen temizler
- **Belirli nesne türleri** – örneğin yalnızca olaylar veya yalnızca medya nesneleri

İşlemi onaylamak için yeniden kimlik doğrulamanız (tekrar giriş yapmanız) istenecektir. Silme işlemi arka planda bir görev olarak çalışır ve bir ilerleme göstergesi görünür.

!!! warning
    Yalnızca nesne türlerinin bir alt kümesini silmek (tüm nesneleri bir anda silmek yerine) büyük ağaçlar için çok uzun sürebilir, çünkü sunucu nesneler arasındaki tüm ilişkileri kontrol etmeli ve güncellemelidir.

!!! tip
    Bunu yeni bir ağaç içe aktarmadan önce sıfırdan başlamak veya yanlış içe aktarılan belirli nesne türlerini kaldırmak için kullanın.

### Yedekten Geri Yükle

Ağacı, yüklenen bir Gramps XML (`.gramps`) yedek dosyası ile eşleşecek şekilde sıfırlar; nesneleri ekleyerek, güncelleyerek ve silerek ağacın yedeğe tamamen benzer olmasını sağlar.

!!! danger
    Bu, yıkıcı bir değiştirme işlemidir, birleştirme değil. Yüklenen yedekte mevcut olmayan herhangi bir nesne silinecektir.

Bir `.gramps` dosyası yükleyin, ardından **Geri Yüklemeyi Önizle** butonuna tıklayın. Eğer oturumunuz yeterince yeni değilse yeniden kimlik doğrulamanız istenecektir. Önizleme, arka planda bir görev olarak çalışır ve tamamlandığında, nesne türüne göre değişiklikleri özetleyen bir diyalog açar (kişiler, aileler, olaylar, yerler, alıntılar, kaynaklar, havuzlar, medya nesneleri, notlar, etiketler):

- **Ekle** – yedekte mevcut ancak mevcut ağaçta eksik olan nesneler
- **Güncelle** – her ikisinde de mevcut olan ancak farklı olan nesneler
- **Sil** – mevcut ağaçta yedekte bulunmayan nesneler
- **Değişmemiş** – her ikisinde de aynı olan nesneler

Herhangi bir nesne silinecekse, diyalog kaç tane olduğunu uyarır. Özeti gözden geçirin, ardından değişiklikleri uygulamak için **Geri Yükle** butonuna tıklayın veya işlemi iptal etmek için **İptal** butonuna tıklayın.

!!! note
    Sadece nesne verileri ve medya referansları geri yüklenir. İkili medya dosyaları ve ağaç meta verileri (varsayılan kişi, yer işaretleri, ad grupları) etkilenmez. Gerekirse eksik medya dosyalarını ayrı olarak [Medya arşivini içe aktar](#import-media-archive) özelliği aracılığıyla geri yükleyin.

!!! tip
    Bunu, örneğin kötü bir içe aktarma veya istenmeyen bir toplu düzenlemeden sonra bilinen iyi bir Gramps XML yedeğine geri dönmek için kullanın.
