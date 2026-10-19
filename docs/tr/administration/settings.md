# Yönetim Ayarları

**Ayarlar > Yönetim** sayfası, üst uygulama çubuğundaki kullanıcı simgesi aracılığıyla erişilebilir. Bu sayfa yalnızca Sahip veya Yönetici rolüne sahip kullanıcılara açıktır ve aile ağacı veritabanını yönetmek için araçlar sağlar.

Sayfa, katlanabilir bölümlere organize edilmiştir. Bir bölüm başlığına tıklayarak genişletebilirsiniz.

## Veri

Kullanım kotalarını, veri içe aktarmayı ve medya dosyası yönetimini kapsar.

### Kullanım Kotaları

Bölümün üst kısmı, yapılandırılmış herhangi bir sınıra göre mevcut kullanımı gösterir:

- **Kişiler** – ağaçtaki kişi nesnelerinin sayısı ile yapılandırılmış maksimum (sınırsız ise ∞)
- **Medya depolama** – yüklenen medya dosyalarının toplam boyutu ile yapılandırılmış depolama kotası (sınırsız ise ∞)

Kotalar sunucu yöneticisi tarafından ayarlanır; ayrıntılar için [Sunucu yapılandırması](../install_setup/configuration.md) sayfasına bakın.

### Veri İçe Aktarma

İçe aktarma bölümü, bir aile ağacı dosyası veya bir medya arşivi yüklemenize olanak tanır. Tam talimatlar için [Veri İçe Aktarma](import.md) sayfasına bakın.

### Medya Dosyası Durumu

Bu bölüm şunları gösterir:

- Ağaçtaki toplam medya nesne sayısı ve herhangi birinin kontrol toplamının eksik olup olmadığı
- Sunucudan eksik olan dosyaların sayısı

Yeşil onay işareti, her şeyin yolunda olduğunu gösterir. Sorunlar tespit edilirse, etkilenen nesnelere bağlantılar gösterilir. Eksik kontrol toplamları genellikle medya referanslarını içeren ancak gerçek dosyaları içermeyen GEDCOM gibi bir formatta veri içe aktarıldığında meydana gelir. Eksik dosyalar, medya arşivini içe aktarma özelliği aracılığıyla yüklenebilir.

### Medya Arşivini İçe Aktarma

Eksik dosyaları doldurmak için medya dosyalarının bir ZIP dosyasını yüklemeye olanak tanır. Tam talimatlar için [Veri İçe Aktarma](import.md) sayfasına bakın.

## Arama İndeksi

### Arama İndeksini Yönet

Gramps Web, veriler değiştiğinde otomatik olarak güncellenen tam metin arama indeksini sürdürmektedir. Durum göstergesi, şu anda kaç nesnenin indekslendiğini ve toplam nesne sayısını gösterir.

Tam bir yeniden oluşturma başlatmak için **Arama indeksini güncelle** butonuna tıklayın. Görev arka planda çalışırken bir ilerleme göstergesi gösterilir. Bu genellikle yalnızca bir sunucu yükseltmesinden sonra gereklidir.

### Anlamsal Arama İndeksi

!!! uyarı "Kullanımdan Kaldırıldı"
    Anlamsal arama, kullanımdan kaldırılmıştır ve Gramps Web API 3.25 ile birlikte bu bölüm de kaldırılacaktır. AI sohbeti buna ihtiyaç duymamaktadır çünkü Gramps Web API 3.24 ile birlikte gelmektedir.

Eğer sunucuda [anlamsal (AI destekli) arama etkinleştirilmişse](../install_setup/chat.md#semantic-search-deprecated), iki eylem ile birlikte ek bir bölüm görünür:

- **Anlamsal arama indeksini yeniden oluştur** – tüm anlamsal indeksi sıfırdan yeniden oluşturur. Bu hesaplama açısından maliyetli olup uzun zaman alabilir.
- **Anlamsal arama indeksini güncelle** – yalnızca henüz indekslenmemiş nesneleri ekleyerek artımlı bir güncelleme yapar. Tam bir yeniden oluşturma işleminden daha hızlıdır.

## Ağaç Ayarları

### Aile Ağacı Adı

!!! not
    Ağacın yeniden adlandırılması yalnızca [çoklu ağaç kurulumu](../install_setup/multi-tree.md) veya `TREE_ID` açıkça [sunucu yapılandırmasında](../install_setup/configuration.md) ayarlandığında çalışır. `TREE_ID` ayarlanmamış varsayılan tek ağaç kurulumunda, bu bir hata oluşturur.

Bu, temel Gramps aile ağacı veritabanının adını değiştirmeye olanak tanır. Yeni bir ad girin ve uygulamak için **Yeniden Adlandır** butonuna tıklayın.

!!! ipucu
    Eğer yalnızca uygulama çubuğunda gösterilen adı değiştirmek istiyorsanız, veritabanını yeniden adlandırmadan [Uygulama başlığı](#app-title) ayarını kullanın.

### Araştırmacı Bilgileri

Ana araştırmacının adını, adresini ve iletişim bilgilerini ayarlayın. Bu bilgiler, dışa aktarımlarda (örneğin GEDCOM dosyaları) yer alır.

## Özelleştirme

### Tema Renkleri

Gramps Web arayüzü için özel bir **birincil renk** ve **vurgulu renk** ayarlayın. Bu renkler, bu ağacın tüm kullanıcılarına uygulanır ve kaydedildikten hemen sonra etkili olur.

Renk seçicileri kullanarak renkleri seçin, ardından **Kaydet** butonuna tıklayın. Varsayılan ayarlara geri dönmek için **Sıfırla** butonuna tıklayın.

### Uygulama Başlığı

Uygulama için özel bir başlık ayarlayın. Ayarlandığında, bu, tarayıcı başlık çubuğundaki aile ağacı adını ve üst uygulama çubuğunu geçersiz kılar.

Bir başlık girin ve **Kaydet** butonuna tıklayın. Varsayılanı kullanmak için boş bırakın (aile ağacı adı).

### Ana Sayfa Notu

Gösterilecek bir Gramps **Not** nesnesi seçin. Not içeriği, ana gösterge panosu sütunlarının altında render edilir ve ağaç erişimi olan tüm kullanıcılar tarafından görünür.

Bir not aramak ve seçmek için nesne seçiciyi kullanın, ardından kaydedin. Mevcut ana sayfa notasını temizlemek için **Kaldır** butonuna tıklayın.

### Ana Sayfa Görseli

Gösterge panosu ana sayfasında görüntü olarak gösterilecek bir Gramps **Medya** nesnesi seçin. Ana sayfa notu ile birleştirildiğinde, görsel not metninin yanında görünür. Not olmadan yalnızca görsel gösterilir.

Bir medya nesnesini aramak ve seçmek için nesne seçiciyi kullanın, ardından kaydedin. Mevcut ana sayfa görselini temizlemek için **Kaldır** butonuna tıklayın.

### Dışa Aktarma/İçe Aktarma Ayarları

Ağaç düzeyindeki ayarlar (uygulama başlığı, tema renkleri, ana sayfa notu/görseli vb.) yedekleme veya başka bir Gramps Web örneğine kopyalamak için bir JSON dosyası olarak dışa aktarılabilir.

- Mevcut ayarları JSON dosyası olarak indirmek için **Ayarları Dışa Aktar** butonuna tıklayın.
- Daha önce dışa aktarılmış bir JSON dosyasını yüklemek ve ayarları uygulamak için **Ağaç Ayarlarını İçe Aktar** butonuna tıklayın.

## Aile Ağacı İşleme

### Veritabanını Kontrol Et ve Onar

Bu araç, Gramps veritabanını içsel tutarsızlıklar için kontrol eder ve mümkün olanları düzeltir – Gramps Masaüstü'ndeki [Veritabanını Kontrol Et ve Onar aracı](https://www.gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Tools#Check_and_Repair_Database) ile benzerlik gösterir.

**Kontrol Et ve Onar** butonuna tıklayın ve ilerleme göstergesinin tamamlanmasını bekleyin. Sonuç butonun altında gösterilir:

- Eğer hata bulunmazsa, bir onay mesajı görüntülenir.
- Eğer hatalar bulunursa, uygulanan düzeltmelerin bir özeti gösterilir.

Beklenmedik hatalar veya nesneler arasındaki ilişkilerin eksik olması gibi veritabanı tutarsızlıklarından kaynaklanabilecek davranışlar ile karşılaşırsanız bu aracı çalıştırın.

### Veriyi Doğrula

[Veritabanını Kontrol Et ve Onar](#check-and-repair-database) aracı *teknik* tutarsızlıkları ararken, bu araç *inanılmaz* verileri arar – Gramps Masaüstü'ndeki [Veriyi Doğrula aracı](https://gramps-project.org/wiki/index.php/Gramps_5.0_Wiki_Manual_-_Tools#Verify_the_Data) ile benzerlik gösterir. İmkansız olmayan ancak ikinci bir göz atmayı gerektirecek kadar olası olmayan şeyleri raporlar, örneğin 12 yaşında bir anne veya 130 yaşına kadar yaşayan bir kişi.

**Seçenekler** altında, testlerin kullandığı eşik değerlerini ayarlayabilirsiniz – maksimum yaş, evlenmek veya çocuk sahibi olmak için minimum ve maksimum yaş, maksimum çocuk sayısı vb. – ayrıca eksik veya belirsiz tarihleri tahmin etme ve 31 Şubat gibi geçersiz tarihleri raporlama seçeneklerini de ayarlayabilirsiniz.

Başlatmak için **Veriyi Doğrula** butonuna tıklayın. Kontrol, arka planda bir görev olarak çalışır ve bulgular daha sonra **Veri Doğrulama Sonuçları** altında listelenir. Bu araç hiçbir şeyi değiştirmez: yalnızca bulduğu şeyleri raporlar.

!!! not
    Bir bulgu, bir hatanın kanıtı değildir. Uzun yaşamlar ve büyük yaş farkları meydana gelebilir, bu nedenle sonuçları düzeltilecek şeyler listesi yerine kontrol edilecek şeyler listesi olarak değerlendirin.

## Etiketler

### Etiketleri Yönet

Aile ağacı için [etiketler](../user-guide/tags.md) oluşturun, yeniden adlandırın, renklerini değiştirin ve silin. Etiketler Gramps veritabanında saklanır, tüm kullanıcılar arasında paylaşılır ve Gramps Masaüstü ile tamamen uyumludur.

Bir etiket oluşturmak için **Yeni Etiket** butonuna tıklayın. Mevcut bir etiketin yanındaki kontrolleri kullanarak onu yeniden adlandırın (kalem simgesi), rengini değiştirin (renk seçici) veya silin (silme simgesi).

!!! not
    Bir etiketi silmek, onun uygulandığı tüm nesnelerden kaldırır.

Etiketlerin Gramps Web'de nasıl kullanıldığı hakkında daha fazla bilgi için [Etiketler](../user-guide/tags.md) sayfasına bakın; özel `Blog` ve `ToDo` etiketleri de dahil.

## Tehlike Bölgesi

!!! tehlike
    Tehlike Bölgesi'ndeki işlemler **geri alınamaz**. Devam etmeden önce bir yedek alın.

### Tüm Nesneleri Sil

Aile ağacından nesneleri kaldırır. **Sil** butonuna tıkladığınızda, silmek için seçebileceğiniz bir diyalog açılır:

- **Tüm nesneler** – ağacı tamamen temizler
- **Belirli nesne türleri** – örneğin, yalnızca olaylar veya yalnızca medya nesneleri

İşlemi onaylamak için yeniden kimlik doğrulamanız (tekrar giriş yapmanız) istenecektir. Silme işlemi arka planda bir görev olarak çalışır ve bir ilerleme göstergesi gösterilir.

!!! uyarı
    Sadece nesne türlerinin bir alt kümesini silmek (tüm nesneleri bir anda silmek yerine) büyük ağaçlar için çok uzun sürebilir, çünkü sunucu nesneler arasındaki tüm ilişkileri kontrol etmek ve güncellemek zorundadır.

!!! ipucu
    Yeni bir ağaç içe aktarmadan önce sıfırdan başlamak veya yanlış içe aktarılan belirli nesne türlerini kaldırmak için bunu kullanın.

### Yedekten Geri Yükle

Ağacı, yüklenen bir Gramps XML (`.gramps`) yedek dosyasına eşleştirecek şekilde sıfırlar; nesneleri ekleyerek, güncelleyerek ve silerek ağacın yedeğe tamamen eşit olmasını sağlar.

!!! tehlike
    Bu, yıkıcı bir değiştirme işlemidir, bir birleştirme değil. Yüklenen yedekte mevcut olmayan herhangi bir nesne silinecektir.

Bir `.gramps` dosyası yükleyin, ardından **Geri Yüklemeyi Önizle** butonuna tıklayın. Oturumunuz yeterince taze değilse yeniden kimlik doğrulamanız istenecektir. Önizleme, arka planda bir görev olarak çalışır ve tamamlandığında, nesne türüne göre (kişiler, aileler, olaylar, yerler, alıntılar, kaynaklar, depolar, medya nesneleri, notlar, etiketler) değişikliklerin bir özetini gösteren bir diyalog açılır:

- **Ekle** – yedekte mevcut ancak mevcut ağaçta eksik nesneler
- **Güncelle** – her iki yerde de mevcut olan ancak farklı olan nesneler
- **Sil** – mevcut ağaçta yedekte bulunmayan nesneler
- **Değişmemiş** – her iki yerde de özdeş nesneler

Herhangi bir nesne silinecekse, diyalogda kaç tane olduğunu uyarır. Özeti gözden geçirin, ardından değişiklikleri uygulamak için **Geri Yükle** butonuna tıklayın veya işlemi iptal etmek için **İptal** butonuna tıklayın.

!!! not
    Yalnızca nesne verileri ve medya referansları geri yüklenir. İkili medya dosyaları ve ağaç meta verileri (varsayılan kişi, yer işaretleri, ad grupları) etkilenmez. Gerekirse eksik medya dosyalarını ayrı olarak [Medya Arşivini İçe Aktarma](#import-media-archive) özelliği aracılığıyla geri yükleyin.

!!! ipucu
    Bunu, kötü bir içe aktarma veya istenmeyen bir toplu düzenlemeden sonra, bilinen iyi bir Gramps XML yedeğine geri dönmek için kullanın.
