# Medya dosyalarını içe aktar

Eğer bir [ağaç içe aktardıysanız](import.md) ve ilgili medya dosyalarını yüklemeniz gerekiyorsa, [Yönetim ayarları](settings.md) bölümündeki **Medya Dosyalarını İçe Aktar** seçeneğini kullanın. Eksik medya dosyalarını içeren bir ZIP dosyası beklenir. Dosyalar, ağacınızdaki medya nesneleriyle iki şekilde eşleştirilir:

- **Kontrol toplamına göre.** Kontrol toplamı olan medya nesneleri için – Gramps Desktop'tan içe aktarılan ağaçlar için olduğu gibi – eşleşen kontrol toplamına sahip dosya kullanılır; dosyanın adı veya ZIP dosyasındaki klasör yapısı önemli değildir. Bu, Gramps veritabanındaki kontrol toplamlarının doğru olması durumunda çalışır; bu da kontrol ve onarım aracını çalıştırarak sağlanır.
- **Yola göre.** Kontrol toplamı olmayan medya nesneleri – GEDCOM içe aktarıldıktan sonra tipik olarak olduğu gibi – yollarına göre eşleştirilir: ZIP dosyası, medya nesnesinde saklanan tam göreli yol altında dosyayı içermelidir.

Eğer GEDCOM dosyanızda saklanan yollar mutlaksa (örneğin `C:\Users\...\photo.jpg`), yola göre eşleştirme çalışmayacaktır. Bu durumda, mevcut medya dosyalarını içe aktarılan bir ağaçla ilişkilendirmek için daha fazla seçeneğe sahip olan Gramps Desktop'a her şeyi önce içe aktarmanız ve ardından [Gramps Desktop'tan Gelme](import.md#coming-from-gramps-desktop) bölümünde açıklandığı gibi Gramps Web'e geçmeniz önerilir.

## Medya dosyası durumu

[Yönetim ayarları](settings.md) bölümündeki **Veri** kısmı şunları gösterir:

- Ağaçtaki toplam medya nesnesi sayısı ve herhangi birinin kontrol toplamının eksik olup olmadığı
- Sunucudan eksik olan dosyası olan medya nesnelerinin sayısı

Yeşil bir onay işareti her şeyin yolunda olduğunu gösterir. Problemler tespit edilirse, etkilenen nesnelere bağlantılar gösterilir. Eksik kontrol toplamları genellikle medya referanslarını içeren ancak gerçek dosyaları içermeyen bir format olan GEDCOM'dan veri içe aktarıldığında meydana gelir. Eksik dosyalar yukarıda açıklandığı gibi yüklenebilir.
