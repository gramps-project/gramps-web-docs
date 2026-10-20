# Yönetim Ayarları

**Ayarlar > Yönetim** sayfasına üst uygulama çubuğundaki kullanıcı simgesi aracılığıyla erişilebilir. Bu sayfa yalnızca Sahip veya Yönetici rolüne sahip kullanıcılara açıktır ve aile ağacı veritabanını yönetmek için araçlar sağlar.

Sayfa, katlanabilir bölümlere düzenlenmiştir. Bir bölüm başlığına tıklayarak genişletebilirsiniz.

## Veri

Kullanım kotalarını, veri içe aktarmayı ve medya dosyası yönetimini kapsar.

### Kullanım Kotaları

Bölümün üst kısmı, yapılandırılmış herhangi bir sınıra göre mevcut kullanımı gösterir:

- **Kişiler** – ağaçtaki kişi nesnelerinin sayısı ile yapılandırılmış maksimum (sınırsızsa ∞)
- **Medya depolama** – yüklenen medya dosyalarının toplam boyutu ile yapılandırılmış depolama kotası (sınırsızsa ∞)

Kotalar sunucu yöneticisi tarafından ayarlanır; ayrıntılar için [Sunucu yapılandırması](../install_setup/configuration.md) sayfasına bakın.

### Veri İçe Aktarma

İçe aktarma bölümü, bir aile ağacı dosyası veya bir medya arşivi yüklemenize olanak tanır. Tam talimatlar için [Veri İçe Aktarma](import.md) sayfasına bakın.

### Medya Dosyası Durumu

Bu bölüm şunları gösterir:

- Ağaçtaki toplam medya nesne sayısı ve herhangi birinin kontrol toplamının eksik olup olmadığı
- Sunucudan eksik olan ilişkili dosya sayısı

Yeşil bir onay işareti her şeyin yolunda olduğunu gösterir. Problemler tespit edilirse, etkilenen nesnelere bağlantılar gösterilir. Eksik kontrol toplamları genellikle, medya referanslarını içeren ancak gerçek dosyaları içermeyen GEDCOM gibi bir formatta veri içe aktarıldığında meydana gelir. Eksik dosyalar, medya arşivini içe aktarma özelliği aracılığıyla yüklenebilir.

### Medya Arşivini İçe Aktarma

Eksik dosyaları doldurmak için medya dosyalarının bir ZIP dosyasını yüklemeye olanak tanır. Tam talimatlar için [Veri İçe Aktarma](import.md) sayfasına bakın.

## Arama İndeksi

### Arama İndeksini Yönet

Gramps Web, veri değiştiğinde otomatik olarak güncellenen tam metin arama indeksini sürdürür. Durum göstergesi, şu anda kaç nesnenin dizinlendiğini ve toplam nesne sayısını gösterir.

Tam bir yeniden inşa başlatmak için **Arama indeksini güncelle** butonuna tıklayın. Görev arka planda çalışırken bir ilerleme göstergesi gösterilir. Bu genellikle yalnızca bir sunucu güncellemesinden sonra gereklidir.

### Anlamsal Arama İndeksi

!!! uyarı "Kaldırıldı"
    Anlamsal arama kaldırılmıştır ve Gramps Web API 3.25 ile birlikte bu bölüm de kaldırılacaktır. AI sohbetine ihtiyaç yoktur çünkü Gramps Web API 3.24'te mevcut değildir.

Eğer sunucuda [anlamsal (AI destekli) arama etkinleştirilmişse](../install_setup/chat.md#semantic-search-deprecated), iki eylem ile birlikte ek bir bölüm görünür:

- **Anlamsal arama indeksini yeniden oluştur** – tüm anlamsal indeksi sıfırdan yeniden inşa eder. Bu işlem hesaplama açısından pahalıdır ve uzun sürebilir.
- **Anlamsal arama indeksini güncelle** – yalnızca henüz dizinlenmemiş nesneleri ekleyerek artımlı bir güncelleme yapar. Tam bir yeniden inşa işleminden daha hızlıdır.

## Ağaç Ayarları

### Aile Ağacı Adı

!!! not
    Ağacı yeniden adlandırma işlemi yalnızca [çoklu-ağaç yapılandırmasında](../install_setup/multi-tree.md) veya `TREE_ID` açıkça [sunucu yapılandırmasında](../install_setup/configuration.md) ayarlandığında çalışır. `TREE_ID` ayarlanmadan varsayılan tek ağaç kurulumu üzerinde bu bir hata oluşturur.

Bu, temel Gramps aile ağacı veritabanının adını değiştirmeye olanak tanır. Yeni bir ad girin ve uygulamak için **Yeniden Adlandır** butonuna tıklayın.

!!! ipucu
    Eğer yalnızca uygulama çubuğunda gösterilen adı değiştirmek istiyorsanız ve veritabanını yeniden adlandırmak istemiyorsanız, bunun yerine [Uygulama başlığı](#app-title) ayarını kullanın.

### Araştırmacı Bilgileri

Ana araştırmacının adını, adresini ve iletişim bilgilerini ayarlayın. Bu bilgiler, dışa aktarımlara (örneğin, GEDCOM dosyaları) gömülür.

## Özelleştirme

### Tema Renkleri

Gramps Web arayüzü için özel bir **birincil renk** ve **vurgulayıcı renk** ayarlayın. Bu renkler, bu ağacın tüm kullanıcılarına uygulanır ve kaydedildikten hemen sonra etkili olur.

Renk seçicileri kullanarak renkleri seçin, ardından **Kaydet** butonuna tıklayın. Varsayılan ayarlara geri dönmek için **Sıfırla** butonuna tıklayın.

### Uygulama Başlığı

Uygulama için özel bir başlık ayarlayın. Ayarlandığında, bu, tarayıcı başlık çubuğundaki aile ağacı adını ve üst uygulama çubuğunu geçersiz kılar.

Bir başlık girin ve **Kaydet** butonuna tıklayın. Varsayılanı kullanmak için boş bırakın (aile ağacı adı).

### Ana Sayfa Notu

Gösterilecek bir Gramps **Not** nesnesi seçin. Not içeriği, ana gösterge panosu sütunlarının altında render edilir ve ağaca erişimi olan tüm kullanıcılar tarafından görünür.

Bir not aramak ve seçmek için nesne seçicisini kullanın, ardından kaydedin. Mevcut ana sayfa notasını temizlemek için **Kaldır** butonuna tıklayın.

### Ana Sayfa Görseli

Gösterge panosu ana sayfasında bir görüntü olarak görüntülenecek bir Gramps **Medya** nesnesi seçin. Bir ana sayfa notu ile birleştirildiğinde, görüntü not metninin yanında görünür. Bir not olmadan yalnızca görüntü gösterilir.

Bir medya nesnesini aramak ve seçmek için nesne seçicisini kullanın, ardından kaydedin. Mevcut ana sayfa görselini temizlemek için **Kaldır** butonuna tıklayın.

### Dışa Aktarma/İçe Aktarma Ayarları

Ağaç düzeyindeki ayarlar (uygulama başlığı, tema renkleri, ana sayfa notu/görseli vb.) yedekleme veya başka bir Gramps Web örneğine kopyalamak için JSON dosyası olarak dışa aktarılabilir.

- Mevcut ayarları JSON dosyası olarak indirmek için **Ayarları Dışa Aktar** butonuna tıklayın.
- Daha önce dışa aktarılmış bir JSON dosyasını yüklemek ve ayarları uygulamak için **Ağaç ayarlarını İçe Aktar** butonuna tıklayın.

## Aile Ağacı İşleme

### Veritabanını Kontrol Et ve Onar

Bu araç, Gramps veritabanını içsel tutarsızlıklar için kontrol eder ve düzeltebildiği sorunları giderir – Gramps Masaüstü'ndeki [Veritabanını Kontrol Et ve Onar aracı](https://www.gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Tools#Check_and_Repair_Database) ile benzerlik gösterir.

**Kontrol Et ve Onar** butonuna tıklayın ve ilerleme göstergesinin tamamlanmasını bekleyin. Sonuç butonun altında gösterilir:

- Hiç hata bulunmadıysa, bir onay mesajı görüntülenir.
- Hatalar bulunduysa, uygulanan düzeltmelerin bir özeti gösterilir.

Beklenmedik hatalar veya nesneler arasındaki ilişkilerin eksik olması gibi veritabanı tutarsızlıklarından kaynaklanabilecek davranışlarla karşılaşırsanız bu aracı çalıştırın.

### Veriyi Doğrula

[Veritabanını Kontrol Et ve Onar](#check-and-repair-database) aracı *teknik* tutarsızlıkları ararken, bu araç *inanılmaz* verileri arar – Gramps Masaüstü'ndeki [Veriyi Doğrula aracı](https://gramps-project.org/wiki/index.php/Gramps_5.0_Wiki_Manual_-_Tools#Verify_the_Data) ile benzerlik gösterir. İmkansız olmayan ancak kontrol etmeye değer kadar olasılığı düşük olan şeyleri raporlar, örneğin 12 yaşında bir anne veya 130 yaşına kadar yaşayan bir kişi.

**Seçenekler** altında testlerin kullandığı eşikleri ayarlayabilirsiniz – maksimum yaş, evlenmek veya çocuk sahibi olmak için minimum ve maksimum yaş, maksimum çocuk sayısı vb. – ayrıca eksik veya belirsiz tarihleri tahmin edip etmeyeceğinizi ve 31 Şubat gibi geçersiz tarihleri rapor edip etmeyeceğinizi ayarlayabilirsiniz.

Başlamak için **Veriyi Doğrula** butonuna tıklayın. Kontrol, arka planda bir görev olarak çalışır ve bulgular daha sonra **Veri Doğrulama Sonuçları** altında listelenir. Bu araç hiçbir şeyi değiştirmez: yalnızca bulduğu şeyleri rapor eder.

!!! not
    Bir bulgu hata kanıtı değildir. Uzun yaşamlar ve büyük yaş farkları meydana gelebilir, bu nedenle sonuçları kontrol edilmesi gereken şeyler listesi olarak değerlendirin, düzeltilecek şeyler listesi olarak değil.

## Etiketler

### Etiketleri Yönet

Aile ağacı için [etiketler](../user-guide/tags.md) oluşturun, yeniden adlandırın, renklerini değiştirin ve silin. Etiketler Gramps veritabanında saklanır, tüm kullanıcılar arasında paylaşılır ve Gramps Masaüstü ile tamamen uyumludur.

Bir etiket oluşturmak için **Yeni Etiket** butonuna tıklayın. Mevcut bir etiketin yanındaki kontrolleri kullanarak onu yeniden adlandırın (kalem simgesi), rengini değiştirin (renk seçici) veya silin (silme simgesi).

!!! not
    Bir etiketi silmek, uygulandığı tüm nesnelerden kaldırır.

Etiketlerin Gramps Web'de nasıl kullanıldığı hakkında daha fazla bilgi için [Etiketler](../user-guide/tags.md) sayfasına bakın; özel `Blog` ve `ToDo` etiketleri dahil.

## Yedeklemeler

Bir yedekleme, aile ağacı verilerini, özel kayıtları, ağaç ayarlarını ve ağacın kullanıcılarını içerir. Medya dosyaları dahil değildir; [medya dosyalarınızı yedekleyin](export.md#back-up-your-media-files) sayfasına bakın.

### Saklanan Yedeklemeler

Eğer sunucu yöneticisi bir yedekleme dizini (`BACKUP_DIR`, bkz. [Sunucu yapılandırması](../install_setup/configuration.md)) ayarladıysa, yedeklemeler sunucuda saklanabilir. Aksi takdirde, bölüm yedekleme saklamanın yapılandırılmadığına dair bir bildirim gösterir ve yalnızca yüklenmiş bir dosyadan geri yükleme işlemi mevcuttur.

Bir yedekleme oluşturmak için **Yedekleme Yap...** butonuna tıklayın. Arka planda bir görev olarak oluşturulur ve ardından saklanan yedeklemeler listesinde, tarihi, kişi sayısını ve boyutunu göstererek görünür. Sunucu yalnızca en yeni yedeklemeleri (varsayılan olarak beş) saklar ve daha eski olanları otomatik olarak siler. Günlük olarak oluşturulabilecek yedekleme sayısı da sınırlıdır.

Her saklanan yedekleme için şunları yapabilirsiniz:

- **İndir** – başka bir yerde bir kopyasını saklamak için `.tar` dosyası olarak indirin.
- **Geri Yükle** – aşağıda açıklandığı gibi geri yükleyin.
- **Sil** – onayladıktan sonra silin.

Sunucu üzerinde çalışan Gramps Web sürümünden daha yeni bir sürümle yapılmış bir yedekleme, bir uyarı simgesi ile işaretlenir ve geri yüklenemez.

### Yedekten Geri Yükle

Ağacı saklanan bir yedekten veya yüklenmiş bir dosyadan geri yükler. Saklanan bir yedeği geri yüklemek için, yanındaki geri yükleme butonuna tıklayın. Bir dosyadan geri yüklemek için, bir Gramps Web yedeği (`.tar`) veya bir Gramps XML dosyası (`.gramps`) seçin ve **Geri Yükle** butonuna tıklayın.

!!! tehlike
    Verileri geri yüklemek, yıkıcı bir değiştirme işlemidir, birleştirme değil. Yedekte mevcut olmayan herhangi bir nesne silinecektir.

Bir Gramps Web yedeği için, yedeklemenin ne zaman yapıldığı, hangi ağaç için yapıldığı ve hangi sürümle yapıldığı hakkında bir diyalog gösterilir ve hangi kısımların geri yükleneceğini seçmenize olanak tanır:

- **Veri** – aile ağacının nesneleri
- **Ağaç ayarları** – bu sayfanın ayarları, tema renkleri, uygulama başlığı ve ana sayfa notu gibi
- **Kullanıcılar** – ağacın kullanıcıları

Geri yüklemenin neyi değiştireceğini görmek için **Önizleme** butonuna tıklayın. Bir Gramps XML dosyası yalnızca veri içerdiğinden, böyle bir dosya için önizleme hemen başlar. Oturumunuz yeterince taze değilse yeniden kimlik doğrulamanız istenir. Önizleme, arka planda bir görev olarak çalışır ve tamamlandığında, nesne türüne göre (kişiler, aileler, olaylar, yerler, alıntılar, kaynaklar, depolar, medya nesneleri, notlar, etiketler) ve seçilirse ağaç ayarları ve kullanıcılar için değişikliklerin özetini gösteren bir diyalog açar:

- **Ekle** – yedekte mevcut ancak mevcut ağaçta eksik olan nesneler
- **Güncelle** – her ikisinde de bulunan ancak farklı olan nesneler
- **Sil** – mevcut ağaçta yedekte bulunmayan nesneler
- **Değişmemiş** – her ikisinde de aynı olan nesneler

Herhangi bir nesne silinecekse, diyalog kaç tane olduğunu uyarır. Özeti gözden geçirin, ardından değişiklikleri uygulamak için **Geri Yükle** butonuna tıklayın veya işlemi iptal etmek için **İptal** butonuna tıklayın.

Geri yüklemeden sonra, yedekten eklenen kullanıcılar listelenir. Rastgele bir şifre alırlar, bu nedenle oturum açmadan önce şifrelerini sıfırlamaları gerekir. Sunucuda zaten mevcut olan kullanıcılar asla değiştirilmez. Sunucuda dosyaları eksik olan medya nesneleri de listelenir; bunları [Medya arşivini içe aktar](#import-media-archive) özelliği aracılığıyla yükleyin.

!!! not
    Verileri geri yüklemek yalnızca nesne verilerini ve medya referanslarını geri yükler. İkili medya dosyaları ve ağaç meta verileri (varsayılan kişi, yer imleri, ad grupları) etkilenmez.

!!! ipucu
    Bunu, kötü bir içe aktarma veya istenmeyen toplu düzenleme sonrasında, bir ağacı bilinen iyi bir yedeğe geri döndürmek için kullanın.

## Tehlike Bölgesi

!!! tehlike
    Tehlike Bölgesi'ndeki işlemler **geri alınamaz**. Devam etmeden önce bir [yedekleme](#backups) yapın.

### Tüm Nesneleri Sil

Aile ağacından nesneleri kaldırır. **Sil** butonuna tıkladığınızda, silmek istediğiniz seçenekleri seçebileceğiniz bir diyalog açılır:

- **Tüm nesneler** – ağacı tamamen temizler
- **Belirli nesne türleri** – örneğin, yalnızca olaylar veya yalnızca medya nesneleri

Eylemi onaylamak için yeniden kimlik doğrulamanız (tekrar giriş yapmanız) istenir. Silme işlemi arka planda bir görev olarak çalışır ve bir ilerleme göstergesi gösterilir.

!!! uyarı
    Sadece nesne türlerinin bir alt kümesini silmek (tüm nesneleri birden silmek yerine) büyük ağaçlar için çok uzun sürebilir, çünkü sunucu nesneler arasındaki tüm ilişkileri kontrol etmek ve güncellemek zorundadır.

!!! ipucu
    Bunu yeni bir ağaç içe aktarmadan önce taze bir başlangıç yapmak veya yanlış içe aktarılan belirli nesne türlerini kaldırmak için kullanın.
