# Medya dosyalarını içe aktar

Eğer bir [ağaç içe aktardıysanız](import.md) ve ilgili medya dosyalarını yüklemeniz gerekiyorsa, **Medya Dosyalarını İçe Aktar** seçeneğini [İçe Aktarma sayfasında](import.md), aile ağacı içe aktarmasının altında kullanın. Eksik medya dosyalarını içeren bir ZIP dosyası bekler. Yükleme, ağaçta medya nesneleri bulunduğunda mümkündür, çünkü dosyalar mevcut medya nesneleriyle eşleştirilir – bir aile ağacı dosyası yalnızca kendi medya dosyalarına atıfta bulunur, bu yüzden önce onu içe aktarın.

Dosyalar, ağacınızdaki medya nesneleriyle iki şekilde eşleştirilir:

- **Checksum ile.** Bir checksum'a sahip medya nesneleri için – Gramps Desktop'tan içe aktarılan ağaçlar için olduğu gibi – eşleşen checksum'a sahip dosya kullanılır, dosyanın adı veya ZIP dosyasındaki klasör yapısı dikkate alınmaz. Bu, Gramps veritabanındaki checksum'ların doğru olması durumunda çalışır; bu, kontrol ve onarım aracını çalıştırarak sağlanır.
- **Yol veya dosya adı ile.** Bir checksum'a sahip olmayan medya nesneleri – GEDCOM içe aktarıldıktan sonra tipik olarak – medya nesnesinde saklanan göreli yol ile eşleştirilir. ZIP dosyasında bu yola sahip bir dosya yoksa, yalnızca dosya adı ile eşleştirilir, büyük ve küçük harf dikkate alınmaz (Gramps Web API 3.26'dan itibaren). Bu, `C:\Users\...\Family\grandpa.jpg` gibi diğer programlardan gelen mutlak yollar için de çalışır, bu yüzden tüm dosyaları ZIP dosyasına koyabilirsiniz. Bir dosya adı yalnızca ZIP dosyasında ve hala dosyası olmayan medya nesneleri arasında benzersizse kullanılır.

Yüklemeden sonra, kaç medya nesnesi için bir dosya bulunduğunu belirten bir sonuç görüntülenir ve ZIP dosyasında dosyası olmayanları, Gramps ID'leri ve saklanan yolları ile listeler. Bu listeyi eksik dosyaları bulmak için kullanın, ardından sadece bunlarla birlikte başka bir ZIP dosyası yükleyin – sunucuda zaten bulunan dosyalar etkilenmez.

Farklı klasörlerde aynı dosya adına sahip birkaç medya nesnesi varsa, dosya adına göre eşleştirme onlara çalışmaz. Ya ZIP dosyasındaki saklanan yollardan klasör yapısını yeniden oluşturun ya da her şeyi önce Gramps Desktop'a içe aktarın; bu, mevcut medya dosyalarını içe aktarılan bir ağaçla ilişkilendirmek için daha fazla seçeneğe sahiptir, ardından [Gramps Desktop'tan Gelirken](import.md#coming-from-gramps-desktop) açıklandığı gibi Gramps Web'e geçin.

## Medya dosyası durumu

[İdare ayarları](settings.md) bölümündeki **Veri** kısmı şunları gösterir:

- Ağaçtaki toplam medya nesnesi sayısı ve herhangi birinin checksum'unun eksik olup olmadığı
- Sunucudan eksik olan ilişkili dosyası olan medya nesnelerinin sayısı

Yeşil bir onay işareti her şeyin yolunda olduğunu gösterir. Problemler tespit edilirse, etkilenen nesnelere bağlantılar gösterilir. Eksik checksum'lar genellikle medya referanslarını içeren ancak gerçek dosyaları içermeyen bir format olan GEDCOM'dan veri içe aktarıldığında meydana gelir. Eksik dosyalar yukarıda açıklandığı gibi yüklenebilir.
