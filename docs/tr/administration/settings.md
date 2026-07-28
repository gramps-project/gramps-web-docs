# Yönetim Ayarları

**Ayarlar > Yönetim** sayfası, üst uygulama çubuğundaki kullanıcı simgesi aracılığıyla erişilebilir. Bu sayfa yalnızca Sahip veya Yönetici rolüne sahip kullanıcılara açıktır ve aile ağacı veritabanını yönetmek için araçlar sağlar.

Sayfa, katlanabilir bölümlere organize edilmiştir. Bir bölüm başlığına tıklayarak genişletebilirsiniz.

## Veri

Kullanım kotalarını, veri içe aktarmayı ve medya dosyası yönetimini kapsar.

### Kullanım kotaları

Bölümün üst kısmı, yapılandırılmış herhangi bir limite göre mevcut kullanımı gösterir:

- **Kişiler** – ağaçtaki kişi nesnelerinin sayısı ile yapılandırılmış maksimum (sınırsızsa ∞)
- **Medya depolama** – yüklenen medya dosyalarının toplam boyutu ile yapılandırılmış depolama kotası (sınırsızsa ∞)

Kotalar sunucu yöneticisi tarafından ayarlanır; ayrıntılar için [Sunucu yapılandırması](../install_setup/configuration.md) sayfasına bakın.

### Veri içe aktarma

İçe aktarma bölümü, bir aile ağacı dosyası veya bir medya arşivi yüklemenize olanak tanır. Tam talimatlar için [Veri içe aktarma](import.md) sayfasına bakın.

### Medya dosyası durumu

Bu bölüm şunları gösterir:

- Ağaçtaki toplam medya nesne sayısı ve herhangi birinin kontrol toplamının eksik olup olmadığı
- Sunucudan eksik olan dosyaya sahip medya nesnelerinin sayısı

Yeşil bir onay işareti her şeyin yolunda olduğunu gösterir. Sorunlar tespit edilirse, etkilenen nesnelere bağlantılar gösterilir. Eksik kontrol toplamları genellikle, medya referanslarını içeren ancak gerçek dosyaları içermeyen GEDCOM gibi bir formatta veri içe aktarıldığında meydana gelir. Eksik dosyalar, medya arşivi içe aktarma özelliği aracılığıyla yüklenebilir.

### Medya arşivini içe aktarma

Eksik dosyaları doldurmak için medya dosyalarının bir ZIP dosyasını yüklemeye olanak tanır. Tam talimatlar için [Veri içe aktarma](import.md) sayfasına bakın.

## Arama dizini

### Arama dizinini yönetme

Gramps Web, veriler değiştiğinde otomatik olarak güncellenen tam metin arama dizini tutar. Durum göstergesi, şu anda kaç nesnenin dizinlendiğini ve toplam nesne sayısını gösterir.

Tam bir yeniden inşa başlatmak için **Arama dizinini güncelle** butonuna tıklayın. Görev arka planda çalışırken bir ilerleme göstergesi gösterilir. Bu genellikle yalnızca bir sunucu yükseltmesinden sonra gereklidir.

### Anlamsal arama dizini

Eğer sunucuda [anlamsal (AI destekli) arama etkinse](../install_setup/configuration.md), iki işlemle ek bir bölüm görünür:

- **Anlamsal arama dizinini yeniden oluştur** – tüm anlamsal dizini sıfırdan yeniden inşa eder. Bu işlem hesaplama açısından maliyetlidir ve uzun sürebilir.
- **Anlamsal arama dizinini güncelle** – yalnızca henüz dizinlenmemiş nesneleri ekleyerek artımlı bir güncelleme yapar. Tam bir yeniden inşa işleminden daha hızlıdır.

## Ağaç ayarları

### Aile Ağacı adı

!!! not
    Ağacın yeniden adlandırılması yalnızca bir [çoklu-ağaç kurulumu](../install_setup/multi-tree.md) veya `TREE_ID` açıkça [sunucu yapılandırmasında](../install_setup/configuration.md) ayarlandığında çalışır. `TREE_ID` ayarlanmamış bir varsayılan tek-ağaç kurulumunda bu bir hata oluşturur.

Bu, temel Gramps aile ağacı veritabanının adını değiştirmeye olanak tanır. Yeni bir ad girin ve uygulamak için **Yeniden Adlandır** butonuna tıklayın.

!!! ipucu
    Veritabanının adını değiştirmeden yalnızca uygulama çubuğunda gösterilen adı değiştirmek istiyorsanız, [Uygulama başlığı](#app-title) ayarını kullanın.

### Araştırmacı Bilgileri

Ana araştırmacının adını, adresini ve iletişim bilgilerini ayarlayın. Bu bilgiler, dışa aktarımlarda (örneğin GEDCOM dosyaları) gömülüdür.

## Özelleştirme

### Tema renkleri

Gramps Web arayüzü için özel bir **birincil renk** ve **vurgulu renk** ayarlayın. Bu renkler, bu ağacın tüm kullanıcılarına uygulanır ve kaydedildikten hemen sonra geçerlilik kazanır.

Renk seçicileri kullanarak renkleri seçin, ardından **Kaydet** butonuna tıklayın. Varsayılan ayarlara geri dönmek için **Sıfırla** butonuna tıklayın.

### Uygulama başlığı

Uygulama için özel bir başlık ayarlayın. Ayarlandığında, bu, tarayıcı başlık çubuğundaki aile ağacı adını ve üst uygulama çubuğunu geçersiz kılar.

Bir başlık girin ve **Kaydet** butonuna tıklayın. Varsayılan (aile ağacı adı) kullanmak için boş bırakın.

### Ana sayfa notu

Gösterilecek bir Gramps **Not** nesnesi seçin. Not içeriği, ana gösterge panosu sütunlarının altında render edilir ve ağaç erişimi olan tüm kullanıcılar tarafından görünür.

Bir not aramak ve seçmek için nesne seçicisini kullanın, ardından kaydedin. Mevcut ana sayfa notasını temizlemek için **Kaldır** butonuna tıklayın.

### Ana sayfa resmi

Gösterge panosu ana sayfasında bir resim olarak görüntülenecek bir Gramps **Medya** nesnesi seçin. Ana sayfa notu ile birleştirildiğinde, resim not metninin yanında görünür. Bir not olmadan yalnızca resim gösterilir.

Bir medya nesnesini aramak ve seçmek için nesne seçicisini kullanın, ardından kaydedin. Mevcut ana sayfa resmini temizlemek için **Kaldır** butonuna tıklayın.

### Dışa Aktarma/İçe Aktarma ayarları

Ağaç düzeyindeki ayarlar (uygulama başlığı, tema renkleri, ana sayfa notu/resmi vb.) yedekleme veya başka bir Gramps Web örneğine kopyalama için bir JSON dosyası olarak dışa aktarılabilir.

- Mevcut ayarları JSON dosyası olarak indirmek için **Ayarları Dışa Aktar** butonuna tıklayın.
- Daha önce dışa aktarılan bir JSON dosyasını yüklemek ve ayarları uygulamak için **Ağaç ayarlarını İçe Aktar** butonuna tıklayın.

## Aile Ağacı İşleme

### Veritabanını Kontrol Et ve Onar

Bu araç, Gramps veritabanını içsel tutarsızlıklar için kontrol eder ve düzeltebildiklerini onarır - Gramps Masaüstü'ndeki [Veritabanını Kontrol Et ve Onar aracı](https://www.gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Tools#Check_and_Repair_Database) ile benzer bir işlevsellik sunar.

**Kontrol Et ve Onar** butonuna tıklayın ve ilerleme göstergesinin tamamlanmasını bekleyin. Sonuç butonun altında gösterilir:

- Hata bulunmadıysa, bir onay mesajı görüntülenir.
- Hatalar bulunduysa, uygulanan düzeltmelerin bir özeti gösterilir.

Veritabanı tutarsızlıkları nedeniyle beklenmedik hatalar veya davranışlarla karşılaşırsanız bu aracı çalıştırın; örneğin nesneler arasında eksik ilişkiler gibi.

## Etiketler

### Etiketleri yönetme

Aile ağacı için [etiketler](../user-guide/tags.md) oluşturun, yeniden adlandırın, renk değiştirin ve silin. Etiketler Gramps veritabanında saklanır, tüm kullanıcılar arasında paylaşılır ve Gramps Masaüstü ile tamamen uyumludur.

Bir etiket oluşturmak için **Yeni Etiket** butonuna tıklayın. Mevcut bir etiketin yanındaki kontrolleri kullanarak onu yeniden adlandırabilir (kalem simgesi), rengini değiştirebilir (renk seçici) veya silebilirsiniz (silme simgesi).

!!! not
    Bir etiketi silmek, onun uygulandığı tüm nesnelerden kaldırır.

Etiketlerin Gramps Web'de nasıl kullanıldığını görmek için [Etiketler](../user-guide/tags.md) sayfasına bakın; özel `Blog` ve `ToDo` etiketleri dahil.

## Tehlike Bölgesi

!!! tehlike
    Tehlike Bölgesi'ndeki işlemler **geri alınamaz**. Devam etmeden önce bir yedek alın.

### Tüm nesneleri sil

Aile ağacından nesneleri kaldırır. **Sil** butonuna tıkladığınızda, silmek istediğiniz seçeneği belirleyebileceğiniz bir diyalog açılır:

- **Tüm nesneler** – ağacı tamamen temizler
- **Belirli nesne türleri** – örneğin, yalnızca olaylar veya yalnızca medya nesneleri

İşlemi onaylamak için yeniden kimlik doğrulamanız (tekrar giriş yapmanız) istenecektir. Silme işlemi arka planda bir görev olarak çalışır ve bir ilerleme göstergesi gösterilir.

!!! uyarı
    Sadece bir nesne türü alt kümesini silmek (tüm nesneleri bir kerede silmek yerine) büyük ağaçlar için çok uzun sürebilir, çünkü sunucu tüm nesneler arasındaki ilişkileri kontrol etmek ve güncellemek zorundadır.

!!! ipucu
    Yeni bir ağaç içe aktarmadan önce sıfırdan başlamak veya yanlış içe aktarılan belirli nesne türlerini kaldırmak için bunu kullanın.

### Yedekten Geri Yükle

Ağacı, yüklenen bir Gramps XML (`.gramps`) yedek dosyası ile eşleşecek şekilde sıfırlar; nesneleri ekler, günceller ve siler, böylece ağaç yedekle tamamen aynı hale gelir.

!!! tehlike
    Bu, yıkıcı bir değiştirme işlemidir, bir birleştirme değil. Yüklenen yedekte mevcut olmayan herhangi bir nesne silinecektir.

Bir `.gramps` dosyası yükleyin, ardından **Geri Yüklemeyi Önizle** butonuna tıklayın. Oturumunuz yeterince taze değilse yeniden kimlik doğrulamanız istenecektir. Önizleme, arka planda bir görev olarak çalışır ve tamamlandığında, nesne türüne göre (kişiler, aileler, olaylar, yerler, alıntılar, kaynaklar, depo, medya nesneleri, notlar, etiketler) yapılan değişiklikleri özetleyen bir diyalog açar:

- **Ekle** – yedekte mevcut ancak mevcut ağaçta eksik olan nesneler
- **Güncelle** – her iki yerde de mevcut olan ancak farklı olan nesneler
- **Sil** – mevcut ağaçta yedekte bulunmayan nesneler
- **Değişmedi** – her iki yerde de aynı olan nesneler

Herhangi bir nesne silinecekse, diyalogda kaç tane olduğunu uyarır. Özeti gözden geçirin, ardından değişiklikleri uygulamak için **Geri Yükle** butonuna tıklayın veya iptal etmek için **İptal** butonuna tıklayın.

!!! not
    Sadece nesne verileri ve medya referansları geri yüklenir. İkili medya dosyaları ve ağaç meta verileri (varsayılan kişi, yer işaretleri, ad grupları) etkilenmez. Gerekirse eksik medya dosyalarını ayrı olarak [Medya arşivini içe aktarma](#import-media-archive) özelliği aracılığıyla geri yükleyin.

!!! ipucu
    Bunu, kötü bir içe aktarma veya istenmeyen bir toplu düzenlemeden sonra, bilinen iyi bir Gramps XML yedeğine geri dönmek için kullanın.
