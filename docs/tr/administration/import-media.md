# Medya dosyalarını içe aktar

Eğer bir [ağaç içe aktardıysanız](import.md) ve ilgili medya dosyalarını yüklemeniz gerekiyorsa, [Yönetim ayarları](settings.md) bölümündeki **Medya Dosyalarını İçe Aktar** seçeneğini kullanın. Bu, eksik medya dosyalarını içeren bir ZIP dosyası bekler. Dosyalar, ağacınızdaki medya nesneleri ile iki şekilde eşleştirilir:

- **Checksum ile.** Bir checksum'a sahip medya nesneleri için – Gramps Desktop'tan içe aktarılan ağaçlar için olduğu gibi – eşleşen checksum'a sahip dosya kullanılır; dosyanın adı veya ZIP dosyasındaki klasör yapısı dikkate alınmaz. Bu, Gramps veritabanındaki checksum'ların doğru olması durumunda çalışır; bu da kontrol ve onarım aracını çalıştırarak sağlanır.
- **Yol ile.** Checksum'a sahip olmayan medya nesneleri – GEDCOM içe aktarımdan sonra tipik olan – yollarına göre eşleştirilir: ZIP dosyası, medya nesnesinde saklanan tam olarak göreceli yol altında dosyayı içermelidir.

Eğer GEDCOM dosyanızda saklanan yollar mutlak ise (örneğin `C:\Users\...\photo.jpg`), yol ile eşleştirme çalışmayacaktır. Bu durumda, mevcut medya dosyalarını içe aktarılan bir ağaç ile ilişkilendirmek için daha fazla seçeneğe sahip olan Gramps Desktop'a her şeyi önce içe aktarmanız önerilir ve ardından [Gramps Desktop'tan gelme](import.md#coming-from-gramps-desktop) bölümünde açıklandığı gibi Gramps Web'e geçebilirsiniz.
