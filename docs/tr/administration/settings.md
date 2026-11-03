# Yönetim Ayarları

**Ayarlar > Yönetim** sayfası, üst uygulama çubuğundaki kullanıcı simgesi aracılığıyla erişilebilir. Bu sayfa yalnızca Sahip veya Yönetici rolüne sahip kullanıcılara açıktır ve aile ağacı veritabanını yönetmek için araçlar sağlar.

Sayfa, katlanabilir bölümler halinde düzenlenmiştir. Bir bölüm başlığına tıklayarak genişletebilirsiniz.

## Veri

Kullanım kotalarını, veri içe aktarmayı ve medya dosyası yönetimini kapsar.

### Kullanım kotaları

Bölümün üst kısmı, yapılandırılmış sınırlara göre mevcut kullanımı gösterir:

- **Kişiler** – ağaçtaki kişi nesnelerinin sayısı ile yapılandırılmış maksimum (sınırsız ise ∞)
- **Medya depolama** – yüklenen medya dosyalarının toplam boyutu ile yapılandırılmış depolama kotası (sınırsız ise ∞)

Kotalar sunucu yöneticisi tarafından ayarlanır; ayrıntılar için [Sunucu yapılandırması](../install_setup/configuration.md) sayfasına bakın.

### Veri içe aktarma

İçe aktarma bölümü, bir aile ağacı dosyası veya bir medya arşivi yüklemenizi sağlar. Tam talimatlar için [Veri içe aktarma](import.md) sayfasına bakın.

### Medya dosyası durumu

Bu bölüm şunları gösterir:

- Ağaçtaki toplam medya nesne sayısı ve herhangi birinin kontrol toplamı eksik olup olmadığı
- Sunucudan eksik olan ilişkili dosyaların sayısı

Yeşil bir onay işareti her şeyin yolunda olduğunu gösterir. Problemler tespit edilirse, etkilenen nesnelere bağlantılar gösterilir. Eksik kontrol toplamları genellikle medya referanslarını içeren ancak gerçek dosyaları içermeyen GEDCOM gibi bir formatta veri içe aktarıldığında meydana gelir. Eksik dosyalar, medya arşivini içe aktarma özelliği aracılığıyla yüklenebilir.

### Medya arşivini içe aktarma

Eksik dosyaları doldurmak için medya dosyalarının bir ZIP dosyasını yüklemeye olanak tanır. Tam talimatlar için [Veri içe aktarma](import.md) sayfasına bakın.

## Arama dizini

### Arama dizinini yönetme

Gramps Web, veriler değiştiğinde otomatik olarak güncellenen tam metin arama dizini tutar. Durum göstergesi, şu anda dizinlenen nesne sayısını toplam nesne sayısına göre gösterir.

Tam bir yeniden inşa başlatmak için **Arama dizinini güncelle** butonuna tıklayın. Görev arka planda çalışırken bir ilerleme göstergesi gösterilir. Bu nadiren gereklidir.

Eğer bir ağaç henüz bir arama dizinine sahip değilse, örneğin dizin formatını değiştiren bir sunucu yükseltmesinden sonra, Gramps Web, ağacın ilk kez açıldığında arka planda oluşturur. Oluşturulurken bölüm "Arama dizini oluşturuluyor." şeklinde görünür, **Arama dizinini güncelle** devre dışı bırakılır ve arama sonuçları eksik olabilir. Oluşturma, [Bildirimler](../user-guide/notifications.md) bölümünde "Arama dizinini güncelle" görevi olarak görünür.

## Ağaç ayarları

### Aile Ağacı adı

!!! not
    Ağacı yeniden adlandırmak yalnızca bir [çoklu-ağaç yapılandırması](../install_setup/multi-tree.md) veya `TREE_ID` açıkça [sunucu yapılandırmasında](../install_setup/configuration.md) ayarlandığında çalışır. `TREE_ID` ayarlanmamış varsayılan tek ağaç kurulumunda bu bir hata oluşturur.

Bu, temel Gramps aile ağacı veritabanının adını değiştirmeye olanak tanır. Yeni bir ad girin ve uygulamak için **Yeniden Adlandır** butonuna tıklayın.

!!! ipucu
    Veritabanını yeniden adlandırmadan yalnızca uygulama çubuğunda gösterilen adı değiştirmek istiyorsanız, bunun yerine [Uygulama başlığı](#app-title) ayarını kullanın.

### Araştırmacı Bilgileri

Ana araştırmacının adını, adresini ve iletişim bilgilerini ayarlayın. Bu bilgiler, dışa aktarımlarda (örneğin GEDCOM dosyalarında) yer alır.

## Özelleştirme

### Tema renkleri

Gramps Web arayüzü için özel bir **birincil renk** ve **vurgulayıcı renk** ayarlayın. Bu renkler, bu ağacın tüm kullanıcılarına uygulanır ve kaydedildikten hemen sonra etkili olur.

Renk seçicileri kullanarak renkleri seçin, ardından **Kaydet** butonuna tıklayın. Varsayılan ayarlara geri dönmek için **Sıfırla** butonuna tıklayın.

### Uygulama başlığı

Uygulama için özel bir başlık ayarlayın. Eğer ayarlanmışsa, bu, tarayıcı başlık çubuğundaki ve üst uygulama çubuğundaki aile ağacı adını geçersiz kılar.

Bir başlık girin ve **Kaydet** butonuna tıklayın. Varsayılanı kullanmak için boş bırakın (aile ağacı adı).

### Ana sayfa notu

Gösterilecek bir Gramps **Not** nesnesi seçin. Not içeriği, ana gösterge paneli sütunlarının altında render edilir ve ağaca erişimi olan tüm kullanıcılar tarafından görünür.

Bir not aramak ve seçmek için nesne seçicisini kullanın, ardından kaydedin. Mevcut ana sayfa notasını temizlemek için **Kaldır** butonuna tıklayın.

### Ana sayfa resmi

Gösterge paneli ana sayfasında bir resim olarak görüntülenecek bir Gramps **Medya** nesnesi seçin. Bir ana sayfa notu ile birleştirildiğinde, resim not metninin yanında görünür. Bir not olmadan yalnızca resim gösterilir.

Bir medya nesnesini aramak ve seçmek için nesne seçicisini kullanın, ardından kaydedin. Mevcut ana sayfa resmini temizlemek için **Kaldır** butonuna tıklayın.

### Dışa Aktarma/İçe Aktarma ayarları

Ağaç düzeyindeki ayarlar (uygulama başlığı, tema renkleri, ana sayfa notu/resmi vb.) yedekleme veya başka bir Gramps Web örneğine kopyalamak için bir JSON dosyası olarak dışa aktarılabilir.

- Mevcut ayarları bir JSON dosyası olarak indirmek için **Ayarları Dışa Aktar** butonuna tıklayın.
- Daha önce dışa aktarılmış bir JSON dosyasını yüklemek ve ayarları uygulamak için **Ağaç ayarlarını İçe Aktar** butonuna tıklayın.

## Aile Ağacı İşleme

### Veritabanını Kontrol Et ve Onar

Bu araç, Gramps veritabanını içsel tutarsızlıklar için kontrol eder ve onarabileceği sorunları düzeltir – Gramps Masaüstü'ndeki [Veritabanını Kontrol Et ve Onar aracı](https://www.gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Tools#Check_and_Repair_Database) ile benzerlik gösterir.

**Kontrol Et ve Onar** butonuna tıklayın ve ilerleme göstergesinin tamamlanmasını bekleyin. Sonuç butonun altında gösterilir:

- Eğer hata bulunmadıysa, bir onay mesajı görüntülenir.
- Hatalar bulunduysa, uygulanan düzeltmelerin bir özeti gösterilir.

Beklenmedik hatalar veya nesneler arasındaki tutarsızlıklardan kaynaklanabilecek davranışlar ile karşılaşırsanız bu aracı çalıştırın, örneğin nesneler arasındaki eksik ilişkiler gibi.

### Verileri Doğrula

[Veritabanını Kontrol Et ve Onar](#check-and-repair-database) aracı *teknik* tutarsızlıkları ararken, bu araç *plausible* olmayan verileri arar – Gramps Masaüstü'ndeki [Verileri Doğrula aracı](https://gramps-project.org/wiki/index.php/Gramps_5.0_Wiki_Manual_-_Tools#Verify_the_Data) ile benzerlik gösterir. Annesi 12 yaşında olan veya 130 yaşına kadar yaşayan bir kişi gibi, imkansız olmayan ancak tekrar gözden geçirilmesi gereken şeyleri raporlar.

**Seçenekler** altında testlerin kullandığı eşikleri ayarlayabilirsiniz – maksimum yaş, evlenmek veya çocuk sahibi olmak için minimum ve maksimum yaş, maksimum çocuk sayısı vb. – ayrıca eksik veya belirsiz tarihleri tahmin etme ve 31 Şubat gibi geçersiz tarihleri raporlama seçeneklerini de ayarlayabilirsiniz.

Başlamak için **Verileri Doğrula** butonuna tıklayın. Kontrol arka planda bir görev olarak çalışır ve bulgular daha sonra **Veri Doğrulama Sonuçları** altında listelenir. Bu araç hiçbir şeyi değiştirmez: yalnızca bulduklarını rapor eder.

!!! not
    Bir bulgu, bir hatanın kanıtı değildir. Uzun yaşamlar ve büyük yaş farkları meydana gelebilir, bu nedenle sonuçları düzeltilecek şeyler listesi yerine kontrol edilecek şeyler listesi olarak değerlendirin.

## Etiketler

### Etiketleri Yönet

Aile ağacı için [etiketler](../user-guide/tags.md) oluşturun, yeniden adlandırın, renk değiştirin ve silin. Etiketler Gramps veritabanında saklanır, tüm kullanıcılar arasında paylaşılır ve Gramps Masaüstü ile tamamen uyumludur.

Bir etiket oluşturmak için **Yeni Etiket** butonuna tıklayın. Mevcut bir etiketin yanındaki kontrolleri kullanarak onu yeniden adlandırın (kalem simgesi), rengini değiştirin (renk seçici) veya silin (silme simgesi).

!!! not
    Bir etiketi silmek, onun uygulandığı tüm nesnelerden kaldırır.

Etiketlerin Gramps Web'de nasıl kullanıldığı hakkında daha fazla bilgi için [Etiketler](../user-guide/tags.md) sayfasına bakın; burada özel `Blog` ve `ToDo` etiketleri de bulunmaktadır.

## Yedeklemeler

Bir yedek, aile ağacı verilerini, özel kayıtları, ağaç ayarlarını ve ağacın kullanıcılarını içerir. Medya dosyaları dahil edilmez; [Medya dosyalarınızı yedekleyin](export.md#back-up-your-media-files) sayfasına bakın.

### Saklanan yedeklemeler

Eğer sunucu yöneticisi bir yedekleme dizini (`BACKUP_DIR`, bkz. [Sunucu yapılandırması](../install_setup/configuration.md)) ayarladıysa, yedeklemeler sunucuda saklanabilir. Aksi takdirde, bu bölüm yedekleme saklamanın yapılandırılmadığına dair bir bildirim gösterir ve yalnızca yüklenen bir dosyadan geri yükleme yapılabilir.

Bir yedek oluşturmak için **Yedek Oluştur...** butonuna tıklayın. Arka planda bir görev olarak oluşturulur ve ardından saklanan yedekler listesinde, tarihi, kişi sayısını ve boyutunu gösterir. Sunucu yalnızca en yeni yedekleri (varsayılan olarak beş) saklar ve daha eski olanları otomatik olarak siler. Ayrıca, günde oluşturulabilecek yedek sayısı da sınırlıdır.

Her saklanan yedek için şunları yapabilirsiniz:

- **İndir** – başka bir yerde bir kopyasını saklamak için `.tar` dosyası olarak indirin.
- **Geri Yükle** – aşağıda açıklandığı gibi.
- **Sil** – onayladıktan sonra.

Sunucuda çalışan Gramps Web sürümünden daha yeni bir sürümle yapılmış bir yedek, bir uyarı simgesi ile işaretlenir ve geri yüklenemez.

### Yedekten Geri Yükle

Ağacı saklanan bir yedekten veya yüklenen bir dosyadan geri yükler. Saklanan bir yedeği geri yüklemek için, yanındaki geri yükle butonuna tıklayın. Bir dosyadan geri yüklemek için, bir Gramps Web yedeği (`.tar`) veya bir Gramps XML dosyası (`.gramps`) seçin ve **Geri Yükle** butonuna tıklayın.

!!! tehlike
    Verilerin geri yüklenmesi yıkıcı bir değiştirme işlemi olup, birleştirme değildir. Yedekte bulunmayan herhangi bir mevcut nesne silinir.

Bir Gramps Web yedeği için, yedek ne zaman yapıldığı, hangi ağaç için yapıldığı ve hangi sürümle yapıldığı hakkında bir diyalog gösterir ve hangi bölümleri geri yüklemek istediğinizi seçmenize olanak tanır:

- **Veri** – aile ağacının nesneleri
- **Ağaç ayarları** – bu sayfanın ayarları, tema renkleri, uygulama başlığı ve ana sayfa notu gibi
- **Kullanıcılar** – ağacın kullanıcıları

Geri yüklemenin neyi değiştireceğini görmek için **Önizleme** butonuna tıklayın. Bir Gramps XML dosyası yalnızca veri içerdiğinden, böyle bir dosya için önizleme hemen başlar. Eğer oturumunuz yeterince taze değilse yeniden kimlik doğrulaması yapmanız istenecektir. Önizleme arka planda bir görev olarak çalışır ve tamamlandığında, nesne türüne (kişiler, aileler, olaylar, yerler, alıntılar, kaynaklar, depolar, medya nesneleri, notlar, etiketler) göre değişiklikleri özetleyen bir diyalog açılır ve eğer seçilmişse ağaç ayarları ve kullanıcılar için:

- **Ekle** – yedekte mevcut ancak mevcut ağaçta eksik olan nesneler
- **Güncelle** – her iki yerde de mevcut olan ancak farklı olan nesneler
- **Sil** – mevcut ağaçta yedekte bulunmayan nesneler
- **Değişmeden Kal** – her iki yerde de özdeş nesneler

Herhangi bir nesne silinecekse, diyalogda kaç tane olduğunu uyarır. Özeti gözden geçirin, ardından değişiklikleri uygulamak için **Geri Yükle** butonuna tıklayın veya işlemi iptal etmek için **İptal** butonuna tıklayın.

Geri yüklemeden sonra, yedekten eklenen kullanıcılar listelenir. Rastgele bir şifre alırlar, bu nedenle oturum açmadan önce şifrelerini sıfırlamaları gerekir. Sunucuda zaten mevcut olan kullanıcılar asla değiştirilmez. Sunucuda dosyaları eksik olan medya nesneleri de listelenir; bunları [Medya arşivini içe aktarma](#import-media-archive) aracılığıyla yükleyin.

!!! not
    Verilerin geri yüklenmesi yalnızca nesne verilerini ve medya referanslarını geri yükler. İkili medya dosyaları ve ağaç meta verileri (varsayılan kişi, yer işaretleri, ad grupları) etkilenmez.

!!! ipucu
    Bunu, örneğin kötü bir içe aktarma veya istenmeyen toplu düzenleme sonrasında, bir ağacı bilinen iyi bir yedeğe geri döndürmek için kullanın.

## Tehlike Bölgesi

!!! tehlike
    Tehlike Bölgesi'ndeki işlemler **geri alınamaz**. Devam etmeden önce bir [yedekleme](#backups) yapın.

### Tüm nesneleri sil

Aile ağacından nesneleri kaldırır. **Sil** butonuna tıklamak, silmek istediğiniz seçeneği seçebileceğiniz bir diyalog açar:

- **Tüm nesneler** – ağacı tamamen temizler
- **Belirli nesne türleri** – örneğin yalnızca olaylar veya yalnızca medya nesneleri

Eylemi onaylamak için yeniden kimlik doğrulaması (yeniden giriş) yapmanız istenecektir. Silme işlemi arka planda bir görev olarak çalışır ve bir ilerleme göstergesi gösterilir.

!!! uyarı
    Sadece bir nesne türü alt kümesini silmek (tüm nesneleri bir anda silmek yerine) büyük ağaçlar için çok uzun sürebilir, çünkü sunucu nesneler arasındaki tüm ilişkileri kontrol etmek ve güncellemek zorundadır.

!!! ipucu
    Bunu, yeni bir ağaç içe aktarmadan önce taze bir başlangıç yapmak veya yanlış içe aktarılan belirli nesne türlerini kaldırmak için kullanın.
