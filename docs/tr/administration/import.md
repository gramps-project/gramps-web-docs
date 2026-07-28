## Gramps veritabanınızı hazırlayın

Eğer Gramps Masaüstü kullanıyorsanız, aşağıdaki adımları izleyerek veritabanınızı hazırlamanız gerekmektedir. Eğer farklı bir soy ağacı programından geçiş yapıyorsanız, bu adımı atlayabilirsiniz.

1. Veritabanını kontrol edin ve onarın
    - İsteğe bağlı: Gramps XML formatında veritabanı yedeği oluşturun
    - [Veritabanını kontrol et ve onar aracı](https://gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Tools#Check_and_Repair_Database)'nı çalıştırın. Bu, Gramps Web'de sorunlara yol açabilecek bazı iç tutarsızlıkları düzeltir.
2. Medya yollarını göreceli hale getirin
    - Gramps Medya Yöneticisi'ni kullanarak [tüm medya yollarını mutlak olanlardan göreceli olanlara dönüştürün](https://gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Tools#Convert_paths_from_relative_to_absolute). Göreceli yollar kullanılsa bile, Gramps medya dizininiz dışında bulunan medya dosyalarının Gramps Web ile senkronize edildiğinde düzgün çalışmayacağını unutmayın.

## Soybilgisi verilerini içe aktarın

Mevcut bir aile ağacını içe aktarmak için "İçe Aktar" sayfasını kullanın ve Gramps tarafından desteklenen dosya formatlarından herhangi birinde bir dosya yükleyin &ndash; Gramps Wiki'deki [Başka bir soy ağacı programından içe aktarma](https://www.gramps-project.org/wiki/index.php/Import_from_another_genealogy_program) sayfasına bakın.

Eğer zaten Gramps Masaüstü kullanıyorsanız, çevrimiçi ve çevrimdışı ağaçlarınızın aynı tanımlayıcıları kullanmasını sağlamak için Gramps XML (`.gramps`) formatını kullanmanız şiddetle önerilir ve bu sayede [senkronize edilebilirler](sync.md).

"İçe Aktar" butonuna tıkladıktan sonra, dosya önce ayrıştırılır ve "İçe Aktarmayı Onayla" iletişim kutusu, dosyanın içerdiği nesnelerin (kişiler, aileler, olaylar, yerler vb.) önizlemesini gösterir. Sayımları gözden geçirin, ardından devam etmek için iletişim kutusundaki "İçe Aktar" butonuna tıklayın veya hiçbir şeyi değiştirmeden iptal etmek için "İptal" butonuna tıklayın.

!!! uyarı
    Normal bir içe aktarma tamamen ekleyicidir: her zaman yeni nesneler oluşturur ve mevcut olanları güncellemez veya silmez, aynı Gramps ID veya tanıtıcı altında zaten ağaçta bulunan nesneler için bile. Aynı dosyayı iki kez içe aktarmak &ndash; veya ağaçta zaten bulunan verilerle örtüşen bir dosyayı içe aktarmak &ndash; her eşleşen nesneyi çoğaltır, birleştirmez veya atlamaz.

    Eğer daha önce içe aktarılan bir ağaçta başka yerlerde yapılan değişiklikleri dahil etmeniz gerekiyorsa, bunun yerine [Yedekten Geri Yükle](settings.md#restore-from-backup) seçeneğini kullanın; bu, yüklenen dosyaya uyması için ağacı değiştirir, eklemek yerine.

## Neden Gramps XML paketi desteği yok?

Gramps XML (`.gramps`) veri içe aktarmak için tercih edilen format olmasına rağmen, Gramps XML *paketi* (`.gpkg`) Gramps Web tarafından desteklenmemektedir. Bunun nedeni, medya dosyaları için içe aktarma ve dışa aktarma rutinlerinin bir web sunucusunda kullanılmak üzere uygun olmamasıdır.

İçe aktarılan bir `.gramps` dosyasına ait medya dosyalarını içe aktarmak için, bir sonraki bölüme bakın.

## Medya dosyalarını içe aktarın

Eğer bir aile ağacını yüklediyseniz ve ilgili medya dosyalarını yüklemeniz gerekiyorsa, "İçe Aktar" sayfasındaki "medya arşivini içe aktar" butonunu kullanabilirsiniz.

Bu, içinde eksik medya dosyalarının bulunduğu bir ZIP dosyası bekler. ZIP dosyasındaki klasör yapısının Gramps medya klasöründeki klasör yapısıyla aynı olması gerekmez, çünkü dosyalar kontrol toplamlarıyla medya nesneleriyle eşleştirilir.

Bu özelliğin yalnızca Gramps veritabanında doğru kontrol toplamına sahip dosyalar için çalıştığını unutmayın (bu, ilk adımda kontrol et ve onar aracını çalıştırarak sağlanmalıdır).

Medya dosyalarını içeren farklı bir soy ağacı programından Gramps Web'e geçerken, öncelikle her şeyi Gramps Masaüstü'ne içe aktarmanız önerilir; bu, mevcut medya dosyalarını içe aktarılan bir ağaçla ilişkilendirmek için daha fazla seçeneğe sahiptir.
