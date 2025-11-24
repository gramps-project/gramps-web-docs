## Gramps veritabanınızı hazırlayın

Eğer Gramps Masaüstü kullanıyorsanız, veritabanınızı hazırlamak için iki adım vardır; böylece her şeyin sorunsuz çalışmasını sağlarsınız. Eğer farklı bir soy ağacı programından geçiş yapıyorsanız, bu adımı atlayabilirsiniz.

1. Veritabanını kontrol edin ve onarın
    - Opsiyonel: Gramps XML formatında veritabanı yedeği oluşturun
    - [Veritabanını kontrol et ve onar aracı](https://gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Tools#Check_and_Repair_Database)'nı çalıştırın. Bu, Gramps Web'de sorunlara yol açabilecek bazı iç tutarsızlıkları düzeltir.
2. Medya yollarını göreceli hale getirin
    - Gramps Medya Yöneticisi'ni kullanarak [tüm medya yollarını mutlak olanlardan göreceli hale dönüştürün](https://gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Tools#Convert_paths_from_relative_to_absolute). Göreceli yollarla bile, Gramps medya dizininiz dışında bulunan herhangi bir medya dosyasının Gramps Web ile senkronize edildiğinde düzgün çalışmayacağını unutmayın.

## Soybilgisi verilerini içe aktarın

Mevcut bir aile ağacını içe aktarmak için "İçe Aktar" sayfasını kullanın ve Gramps tarafından desteklenen herhangi bir dosya formatında bir dosya yükleyin &ndash; Gramps Wiki'deki [Başka bir soybilgisi programından içe aktar](https://www.gramps-project.org/wiki/index.php/Import_from_another_genealogy_program) bölümüne bakın.

Eğer zaten Gramps Masaüstü kullanıyorsanız, çevrimiçi ve çevrimdışı ağaçlarınızın aynı tanımlayıcıları kullanmasını sağlamak için Gramps XML (`.gramps`) formatını kullanmanız şiddetle tavsiye edilir ve bu sayede [senkronize edilebilirler](sync.md).

## Neden Gramps XML paketi için destek yok?

Gramps XML (`.gramps`) veri içe aktarmak için tercih edilen format olmasına rağmen, Gramps XML *paketi* (`.gpkg`) Gramps Web tarafından desteklenmemektedir. Bunun nedeni, medya dosyaları için içe aktarma ve dışa aktarma rutinlerinin bir web sunucusunda kullanılmak için uygun olmamasıdır.

İçe aktarılan bir `.gramps` dosyasına ait medya dosyalarını içe aktarmak için, bir sonraki bölüme bakın.

## Medya dosyalarını içe aktarın

Eğer bir aile ağacını yüklediyseniz ve ilgili medya dosyalarını yüklemeniz gerekiyorsa, "İçe Aktar" sayfasındaki "medya arşivini içe aktar" butonunu kullanabilirsiniz.

Bu, içinde eksik medya dosyalarının bulunduğu bir ZIP dosyası bekler. ZIP dosyasındaki klasör yapısının Gramps medya klasörü içindeki klasör yapısıyla aynı olması gerekmez; dosyalar, kontrol toplamları ile medya nesnelerine eşleştirilir.

Bu özelliğin yalnızca Gramps veritabanında doğru kontrol toplamına sahip dosyalar için çalıştığını unutmayın (bu, ilk adımda kontrol et ve onar aracını çalıştırarak sağlanmalıdır).

Medya dosyalarını içeren farklı bir soybilgisi programından Gramps Web'e geçerken, mevcut medya dosyalarını içe aktarılan bir ağaçla ilişkilendirmek için daha fazla seçeneğe sahip olan Gramps Masaüstü'ne her şeyi önce içe aktarmanız önerilir.
