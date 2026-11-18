# Veri İçe Aktarma

Mevcut bir aile ağacını, başka bir soybilim programından, çevrimiçi bir hizmetten veya Gramps Masaüstü'nden dışa aktarılan bir dosyayı yükleyerek Gramps Web'e getirebilirsiniz.

İçe aktarma işleminin kendine ait bir sayfası vardır ve bu sayfa ağaç sahipleri ve yöneticilere açıktır. Bunu, [Yönetim ayarları](settings.md) bölümündeki **Veri** kısmında **Aile Ağacını İçe Aktar** ile açabilirsiniz (üst uygulama çubuğundaki kullanıcı simgesi ▸ Yönetim). Ağaç henüz boşken, ana sayfadaki "Başlayın" kartındaki **Aile Ağacını İçe Aktar** butonu, aile ağacında ve listelerde de oraya yönlendirir.

## Hangi dosya kullanılmalı

| Nereden geliyor | Ağacınızı dışa aktarın | Dosya uzantısı |
|---|---|---|
| Başka bir soybilim programı veya çevrimiçi hizmet | GEDCOM | `.ged` |
| Gramps Masaüstü | Gramps XML | `.gramps` |
| GeneWeb | GeneWeb | `.gw` |
| Pro-Gen | Pro-Gen | `.def` |
| Bir elektronik tablo | Gramps CSV | `.csv` |
| Bir rehber | vCard | `.vcf` |

GEDCOM, neredeyse her soybilim programının ve çevrimiçi hizmetin dışa aktarabileceği ortak değişim formatıdır. Programınızda veya web sitesinde "Dışa Aktar" veya "İndir" seçeneğini arayın ve birden fazla format sunuluyorsa GEDCOM'u seçin. Gramps Wiki sayfası [Başka bir soybilim programından içe aktarma](https://www.gramps-project.org/wiki/index.php/Import_from_another_genealogy_program) belirli programlar hakkında notlar içermektedir.

Eğer Gramps Masaüstü kullanıyorsanız, GEDCOM yerine Gramps XML (`.gramps`) seçin. Bu, tüm Gramps verilerini kayıpsız taşır ve çevrimiçi ve çevrimdışı ağaçlar aynı tanımlayıcıları korur, böylece [senkronize](sync.md) edilebilirler. Aşağıda [Gramps Masaüstünden Gelenler](#coming-from-gramps-desktop) bölümüne bakın.

## Bir aile ağacı dosyasını içe aktar

1. Yukarıda açıklandığı gibi İçe Aktarma sayfasını açın.
2. "Aile Ağacını İçe Aktar" altında dosyanızı seçin ve **İçe Aktar** butonuna tıklayın. Yükleme ilerlemesi gösterilecektir.
3. Dosya önce okunur ve "İçe Aktarmayı Onayla" iletişim kutusu, kaç nesne içerdiğini (kişiler, aileler, olaylar, yerler vb.) ve varsa içe aktarıcının [raporunu](#the-import-report) gösterir. Henüz ağacınıza hiçbir şey eklenmemiştir. Sayımın mantıklı göründüğünden emin olun, ardından devam etmek için **İçe Aktar** butonuna veya hiçbir şeyi değiştirmeden iptal etmek için **İptal** butonuna tıklayın. Eğer ağacınızda zaten kişiler varsa, iletişim kutusu aynı verileri tekrar içe aktarmanın kopyalar oluşturacağına dair uyarıda bulunur.
4. İçe aktarma arka planda çalışır ve bir ilerleme göstergesi gösterilir. Veriler içe aktarıldıktan sonra arama dizini güncellenir, bu büyük bir ağaç için biraz zaman alabilir. İçe aktarma başarısız olursa, sebebi gösterilir.
5. Eğer ağaçta henüz bir ev sahibi yoksa, birini seçmeniz istenir.

İçe aktarma tamamlandığında, sonucu kontrol edin: ana sayfadaki **İstatistikler** panelindeki kişi sayısını eski programınızdaki sayı ile karşılaştırın ve iyi bildiğiniz bir aileyi açarak ebeveynlerin, çocukların, tarihler ve yerlerin beklenildiği gibi geldiğini görün. Dosya fotoğraflara veya diğer medya dosyalarına atıfta bulunuyorsa, bunları eklemek için aynı sayfadaki [Medya Dosyalarını İçe Aktar](import-media.md) bölümüne bakın.

!!! warning
    Normal bir içe aktarma tamamen ekleyicidir: her zaman yeni nesneler oluşturur ve mevcut olanları asla güncellemez veya silmez, aynı Gramps ID veya tanıtıcı altında zaten var olan nesneler için bile. Aynı dosyayı iki kez içe aktarmak - veya ağaçta zaten bulunan verilerle örtüşen bir dosyayı içe aktarmak - her eşleşen nesneyi çoğaltır, birleştirmez veya atlamaz.

    Eğer başka bir yerde yapılan değişiklikleri daha önce içe aktarılan bir ağaca getirmek istiyorsanız, bunun yerine [Yedekten Geri Yükle](backups.md#restore-from-backup) seçeneğini kullanın; bu, yüklenen dosyaya uyması için ağacı değiştirir, eklemek yerine. Bu, bir Gramps XML dosyası veya bir Gramps Web yedeği gerektirir.

## İçe aktarma raporu

İçe aktarıcılar, tamamen içe aktaramadıkları şeyleri rapor eder; örneğin, anlamadıkları GEDCOM satırları, dosyadan eksik kayıt referansları veya eski bir dosya formatı. Rapor, hem onay iletişim kutusunda hem de içe aktarma sonrasında **Rapor** altında gösterilir. Onaylamadan önce okuyun: genellikle, aksi takdirde ağaçta daha sonra fark edeceğiniz sorunları açıklar.

Her mesaj bir sorun değildir - birçok GEDCOM dosyası, rapor edilen ancak saklanan program özel verileri içerir, bkz. [Program özel verileri](#program-specific-data). Raporun yanındaki butonları kullanarak raporu kopyalayabilir veya metin dosyası olarak indirebilirsiniz; örneğin, [forumda](../help/help.md) yardım istemek için.

## Kullanım kotaları

Sunucu yöneticisi, ağacınız için sınırlar belirleyebilir (bkz. [Sunucu yapılandırması](../install_setup/configuration.md)). **Veri** bölümünün üst kısmı, bu sınırlara göre mevcut kullanımı gösterir:

- **Kişiler** – ağaçtaki kişi nesnelerinin sayısı ile yapılandırılmış maksimum (sınırsızsa ∞)
- **Medya depolama** – yüklenen medya dosyalarının toplam boyutu ile yapılandırılmış depolama kotası (sınırsızsa ∞)

Kişi sayısını aşacak bir içe aktarma, tamamen reddedilir.

## GEDCOM dosyaları

Hem GEDCOM 5.5.1 hem de GEDCOM 7 dosyaları içe aktarılabilir. Bilmeniz gereken birkaç şey var.

### Karakter kodlaması

Bir GEDCOM 5.5.1 dosyası, karakter kodlamasını başlığında belirtir. UTF-8, UTF-16, ANSEL ve Windows (ANSI) kodlamaları desteklenmektedir. İçe aktarımdan sonra aksanlı veya diğer özel karakterlere sahip isimler bozuk görünüyorsa (örneğin `MÃ¼ller` yerine `Müller`), dosya muhtemelen belirttiğinden farklı bir kodlama ile dışa aktarılmıştır. Eski programınızdan dosyayı tekrar dışa aktarın, eğer bir seçenek sunuluyorsa UTF-8'i seçin ve [yeniden başlayın](#starting-over).

GEDCOM 7 dosyaları her zaman UTF-8 olarak kodlanmalıdır; diğer dosyalar "Geçersiz GEDCOM dosyası" hatası ile reddedilir.

### Program özel verileri

Birçok program, diğer programların anlamadığı GEDCOM'a kendi uzantılarını ekler. Gramps, bu tür verileri sessizce atmaz: yorumlayamadığı satırlar, ait oldukları kişi, aile veya diğer nesneye ekli bir "GEDCOM içe aktarma" türünde notta toplanır. Önemli bir şeyin gelmediğini görmek için bu notları gözden geçirin.

### Medya dosyaları

Bir GEDCOM dosyası, medya dosyalarına (fotoğraflar veya taranmış belgeler gibi) atıflar içerir, ancak dosyaların kendilerini içermez. İçe aktarımdan sonra, medya nesneleri ağacınızda var olur, ancak dosyaları eksiktir; bu durum [Medya dosyası durumu](import-media.md#media-file-status) altında gösterilir. Dosyaları eklemek için [Medya dosyalarını içe aktar](import-media.md) bölümüne bakın.

## Gramps Masaüstünden Gelenler

Eğer Gramps Masaüstü kullanıyorsanız, her şeyin sorunsuz çalışmasını sağlamak için veritabanınızı hazırlamak için iki adım vardır.

1. Veritabanını kontrol et ve onar
    - İsteğe bağlı: Gramps XML'e dışa aktararak bir veritabanı yedeği oluşturun
    - [Veritabanını kontrol et ve onar aracı](https://gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Tools#Check_and_Repair_Database) çalıştırın. Bu, Gramps Web'de sorunlara yol açabilecek bazı iç tutarsızlıkları düzeltir.
2. Medya yollarını göreceli hale getir
    - Gramps Medya Yöneticisi'ni kullanarak [tüm medya yollarını mutlak yoldan göreceli hale getirin](https://gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Tools#Convert_paths_from_relative_to_absolute). Göreceli yollarla bile, Gramps medya dizininiz dışındaki medya dosyaları Gramps Web ile senkronize edildiğinde düzgün çalışmayacaktır.

Sonra ağacınızı Gramps XML (`.gramps`) formatında dışa aktarın, yukarıda açıklandığı gibi içe aktarın ve [medya dosyalarınızı yükleyin](import-media.md). Bilgisayarınızda ve webde aynı ağaç üzerinde çalışmaya devam etmek için [Gramps Web Senkronizasyon eklentisini](sync.md) kullanın.

### Neden Gramps XML paketi desteği yok?

Gramps XML (`.gramps`) veri içe aktarmak için tercih edilen format olsa da, Gramps XML *paketi* (`.gpkg`) Gramps Web tarafından desteklenmemektedir. Bunun nedeni, medya dosyaları için içe aktarma ve dışa aktarma rutinlerinin bir web sunucusunda kullanılmak üzere uygun olmamasıdır.

## Yaygın sorunlar

**"Desteklenmeyen format".** Sadece [yukarıda](#which-file-to-use) listelenen dosya uzantıları içe aktarılabilir. Eğer programınız veya çevrimiçi hizmetiniz size bir ZIP arşivi verdiyse, bunu açın ve içindeki `.ged` dosyasını yükleyin.

**Her şey iki kez görünüyor.** Aynı dosya iki kez içe aktarılmıştır. İçe aktarmalar asla birleştirilmediğinden, [yeniden başlayın](#starting-over).

**Bozuk özel karakterler.** [Karakter kodlaması](#character-encoding) bölümüne bakın.

**Fotoğraflar eksik.** [Medya dosyalarını içe aktar](import-media.md) bölümüne bakın.

### Yeniden başlamak

Eğer bir içe aktarma yanlış gittiyse veya eski programınızda bir şeyi düzeltmek ve tekrar içe aktarmak istiyorsanız, önce [Tüm nesneleri sil](#delete-all-objects) seçeneğini kullanarak ağacı boşaltın, ardından düzeltilmiş dosyayı içe aktarın. Bu, içe aktarma işleminden bu yana Gramps Web'de yaptığınız değişiklikleri de siler.

### Tüm nesneleri sil

!!! danger
    Nesneleri silmek **geri alınamaz**. Devam etmeden önce bir [yedek](backups.md) oluşturun.

**Tüm nesneleri sil** seçeneği, [Yönetim ayarları](settings.md) bölümündeki **Tehlikeli Bölge** kısmında bulunur. **Sil** butonuna tıklamak, silmek için seçiminizi yapabileceğiniz bir iletişim kutusunu açar:

- **Tüm nesneler** – ağacı tamamen temizler
- **Belirli nesne türleri** – örneğin, yalnızca olaylar veya yalnızca medya nesneleri

Eylemi onaylamak için tekrar kimlik doğrulamanız (yeniden giriş yapmanız) istenir. Silme işlemi arka planda bir görev olarak çalışır ve bir ilerleme göstergesi gösterilir.

!!! warning
    Sadece nesne türlerinin bir alt kümesini silmek (tüm nesneleri bir anda silmek yerine) büyük ağaçlar için çok uzun sürebilir, çünkü sunucu nesneler arasındaki tüm ilişkileri kontrol etmek ve güncellemek zorundadır.
