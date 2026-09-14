# Veri İçe Aktarma

Mevcut bir aile ağacını Gramps Web'e, başka bir soybilim programından, çevrimiçi bir hizmetten veya Gramps Desktop'tan dışa aktarılan bir dosyayı yükleyerek getirebilirsiniz.

İçe aktarma, ağaç sahipleri ve yöneticiler için mevcut olan [Yönetim ayarları](settings.md) **Veri** bölümünde bulunur (üst uygulama çubuğundaki kullanıcı simgesi ▸ Yönetim). Ağaç henüz boşken, ana sayfadaki "Başlayın" kartındaki **Aile Ağacını İçe Aktar** düğmesi de buraya yönlendirir.

## Hangi dosyayı kullanmalısınız

| Nereden geliyor | Ağacınızı dışa aktarın | Dosya uzantısı |
|---|---|---|
| Başka bir soybilim programı veya çevrimiçi hizmet | GEDCOM | `.ged` |
| Gramps Desktop | Gramps XML | `.gramps` |
| GeneWeb | GeneWeb | `.gw` |
| Pro-Gen | Pro-Gen | `.def` |
| Bir elektronik tablo | Gramps CSV | `.csv` |
| Bir adres defteri | vCard | `.vcf` |

GEDCOM, neredeyse her soybilim programının ve çevrimiçi hizmetin dışa aktarabileceği ortak değişim formatıdır. Programınızda veya web sitesinde "Dışa Aktar" veya "İndir" seçeneğini arayın ve birden fazla format sunulursa GEDCOM'u seçin. Gramps Wiki sayfası [Başka bir soybilim programından içe aktarma](https://www.gramps-project.org/wiki/index.php/Import_from_another_genealogy_program) belirli programlarla ilgili notlar içermektedir.

Eğer Gramps Desktop kullanıyorsanız, GEDCOM yerine Gramps XML (`.gramps`) seçin. Bu, tüm Gramps verilerini kayıpsız taşır ve çevrimiçi ve çevrimdışı ağaçlar aynı tanımlayıcıları korur, böylece [senkronize](sync.md) edilebilirler. Aşağıda [Gramps Desktop'tan gelenler](#coming-from-gramps-desktop) bölümüne bakın.

## Bir aile ağacı dosyasını içe aktarma

1. Yönetim ayarlarının **Veri** bölümünü açın.
2. "Aile Ağacını İçe Aktar" altında dosyanızı seçin ve **İçe Aktar**'a tıklayın.
3. Dosya önce ayrıştırılır ve "İçe Aktarmayı Onayla" iletişim kutusu, kaç nesne içerdiğini (kişiler, aileler, olaylar, yerler vb.) gösterir. Henüz ağacınıza hiçbir şey eklenmemiştir. Sayıların mantıklı göründüğünü kontrol edin, ardından devam etmek için **İçe Aktar**'a tıklayın veya hiçbir şeyi değiştirmeden iptal etmek için **İptal**'e tıklayın.
4. İçe aktarma arka planda çalışır ve bir ilerleme göstergesi gösterilir. Veriler içe aktarıldıktan sonra, arama dizini güncellenir; bu, büyük bir ağaç için biraz zaman alabilir.

İçe aktarma tamamlandığında, sonucu kontrol edin: ana sayfadaki **İstatistikler** panelindeki kişi sayısını eski programınızdaki sayı ile karşılaştırın ve bildiğiniz bir aileyi açarak ebeveynlerin, çocukların, tarihler ve yerlerin beklendiği gibi geldiğini görün.

!!! uyarı
    Normal bir içe aktarma tamamen ekleyicidir: her zaman yeni nesneler oluşturur ve mevcut olanları asla güncellemez veya silmez, aynı Gramps ID'si veya tanıtıcı altında ağacınızda zaten mevcut olan nesneler için bile. Aynı dosyayı iki kez içe aktarmak - veya ağaçta zaten bulunan verilerle örtüşen bir dosyayı içe aktarmak - her eşleşen nesneyi birleştirmek veya atlamak yerine çoğaltacaktır.

    Daha önce içe aktarılan bir ağaçta başka yerlerde yapılan değişiklikleri getirmek için, [Yedekten Geri Yükle](settings.md#restore-from-backup) seçeneğini kullanın; bu, yüklenen dosyaya uyması için ağacı değiştirir, eklemek yerine. Bu, bir Gramps XML dosyası gerektirir.

Eğer ağacınız için bir kişi sayısı sınırı belirlendiyse (bkz. [Kullanım kotaları](settings.md#usage-quotas)), bunu aşacak bir içe aktarma tamamen reddedilir.

## GEDCOM dosyaları

Hem GEDCOM 5.5.1 hem de GEDCOM 7 dosyaları içe aktarılabilir. Dikkat edilmesi gereken birkaç şey vardır.

### Karakter kodlaması

Bir GEDCOM 5.5.1 dosyası, karakter kodlamasını başlığında belirtir. UTF-8, UTF-16, ANSEL ve Windows (ANSI) kodlamaları desteklenmektedir. İçe aktarma sonrasında aksanlı veya diğer özel karakterlere sahip isimler bozuk görünüyorsa (örneğin `MÃ¼ller` yerine `Müller`), dosya muhtemelen beyan ettiği kodlamadan farklı bir kodlama ile dışa aktarılmıştır. Dosyayı eski programınızdan tekrar dışa aktarın, eğer bir seçenek sunuluyorsa UTF-8'i seçin ve [yeniden başlayın](#starting-over).

GEDCOM 7 dosyaları her zaman UTF-8 olarak kodlanmalıdır; diğer dosyalar "Geçersiz GEDCOM dosyası" hatası ile reddedilir.

### Programa özgü veriler

Birçok program, diğer programların anlamadığı kendi uzantılarını GEDCOM'a ekler. Gramps bu tür verileri sessizce atmaz: yorumlayamadığı satırlar, ait oldukları kişi, aile veya diğer nesneye eklenmiş "GEDCOM içe aktarma" türünde bir notta toplanır. Önemli bir şeyin gelmediğini görmek için bu notları gözden geçirin.

### Medya dosyaları

Bir GEDCOM dosyası, medya dosyalarına (örneğin fotoğraflar veya taranmış belgeler) referanslar içerir, ancak dosyaların kendilerini içermez. İçe aktarımdan sonra, medya nesneleri ağacınızda var olur, ancak dosyaları eksik olur; bu, [Medya dosyası durumu](settings.md#media-file-status) altında gösterilir. Dosyaları eklemek için, aşağıdaki [Medya dosyalarını içe aktar](#import-media-files) bölümüne bakın.

## Gramps Desktop'tan gelenler

Eğer Gramps Desktop kullanıyorsanız, veritabanınızı hazırlamak için her şeyin sorunsuz çalışmasını sağlamak için iki adım vardır.

1. Veritabanını kontrol et ve onar
    - İsteğe bağlı: Gramps XML'e dışa aktararak bir veritabanı yedeği oluşturun
    - [Veritabanını Kontrol Et ve Onar aracı](https://gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Tools#Check_and_Repair_Database)'nı çalıştırın. Bu, Gramps Web'de sorunlara yol açabilecek bazı iç tutarsızlıkları düzeltir.
2. Medya yollarını göreceli hale dönüştür
    - Gramps Medya Yöneticisi'ni kullanarak [tüm medya yollarını mutlak olanlardan göreceli olanlara dönüştürün](https://gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Tools#Convert_paths_from_relative_to_absolute). Göreceli yollarla bile, Gramps medya dizininiz dışında bulunan medya dosyaları Gramps Web ile senkronize edildiğinde düzgün çalışmayacaktır.

Ardından ağacınızı Gramps XML (`.gramps`) formatında dışa aktarın, yukarıda açıklandığı gibi içe aktarın ve bir sonraki bölümde açıklandığı gibi medya dosyalarınızı yükleyin. Bilgisayarınızda ve web'de aynı ağaç üzerinde çalışmaya devam etmek için [Gramps Web Senkronizasyon eklentisini](sync.md) kullanın.

### Neden Gramps XML paketi desteği yok?

Gramps XML (`.gramps`) veri içe aktarmak için tercih edilen formatken, Gramps XML *paketi* (`.gpkg`) Gramps Web tarafından desteklenmemektedir. Bunun nedeni, medya dosyaları için içe aktarma ve dışa aktarma rutinlerinin bir web sunucusunda kullanılmak üzere uygun olmamasıdır.

## Medya dosyalarını içe aktarma

Eğer bir aile ağacını içe aktardıysanız ve karşılık gelen medya dosyalarını yüklemeniz gerekiyorsa, Yönetim ayarlarının Veri bölümünde **Medya Dosyalarını İçe Aktar** seçeneğini kullanın. Eksik medya dosyalarını içeren bir ZIP dosyası bekler. Dosyalar, ağacınızdaki medya nesneleriyle iki şekilde eşleştirilir:

- **Kontrol toplamı ile.** Kontrol toplamı olan medya nesneleri için - Gramps Desktop'tan içe aktarılan ağaçlar için olduğu gibi - eşleşen kontrol toplamına sahip dosya kullanılır; dosyanın adı veya ZIP dosyasındaki klasör yapısı önemli değildir. Bu, Gramps veritabanındaki kontrol toplamlarının doğru olması durumunda çalışır; bu, kontrol et ve onar aracını çalıştırarak sağlanır.
- **Yol ile.** Kontrol toplamı olmayan medya nesneleri - GEDCOM içe aktarımdan sonra tipik olarak - yolları ile eşleştirilir: ZIP dosyası, medya nesnesinde saklanan tam olarak göreceli yol altında dosyayı içermelidir.

Eğer GEDCOM dosyanızda saklanan yollar mutlaksa (örneğin `C:\Users\...\photo.jpg`), yol ile eşleştirme çalışmayacaktır. Bu durumda, mevcut medya dosyalarını içe aktarılan bir ağaçla ilişkilendirmek için daha fazla seçeneğe sahip olan Gramps Desktop'a her şeyi önce içe aktarmanız ve ardından [Gramps Desktop'tan gelenler](#coming-from-gramps-desktop) bölümünde açıklandığı gibi Gramps Web'e geçmeniz önerilir.

## Yaygın sorunlar

**"Desteklenmeyen format".** Yalnızca [yukarıda](#which-file-to-use) listelenen dosya uzantıları içe aktarılabilir. Eğer programınız veya çevrimiçi hizmetiniz size bir ZIP arşivi verdiyse, bunu açın ve içindeki `.ged` dosyasını yükleyin.

**Her şey iki kez görünüyor.** Aynı dosya iki kez içe aktarılmıştır. İçe aktarmalar asla birleştirilmediğinden, [yeniden başlayın](#starting-over).

**Bozuk özel karakterler.** [Karakter kodlaması](#character-encoding) bölümüne bakın.

**Fotoğraflar eksik.** [Medya dosyalarını içe aktarma](#import-media-files) bölümüne bakın.

### Yeniden başlama

Eğer bir içe aktarma yanlış gittiyse veya eski programınızda bir şeyi düzeltmek istiyorsanız ve tekrar içe aktarmak istiyorsanız, önce [Tüm nesneleri sil](settings.md#delete-all-objects) seçeneğini kullanarak ağacı boşaltın, ardından düzeltilmiş dosyayı içe aktarın. Bu, içe aktarma sonrasında Gramps Web'de yaptığınız herhangi bir değişikliği de siler.
