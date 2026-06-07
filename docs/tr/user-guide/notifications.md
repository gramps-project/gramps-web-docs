# Bildirimler

**Bildirimler**, bir çan simgesi ile birlikte yan menü öğesidir. Hatalar meydana geldiğinde veya arka planda görevler çalıştığında, okunmamış bildirimlerin sayısını gösteren bir rozet görünür. Bildirim günlüğünü açmak için üzerine tıklayın.

Bildirim günlüğü iki amaca hizmet eder:

- Oturumunuz sırasında meydana gelen hataların kaydıdır – başarısız API istekleri, arka plan görev hataları, kaydetme hataları veya tarayıcı düzeyindeki hatalar.
- Uzun süren arka plan görevlerinin ilerlemesini takip eder – örneğin, içe aktarma ve dışa aktarma, rapor oluşturma, OCR metin tanıma, veritabanı yükseltmeleri ve arama/ anlamsal indeks yeniden oluşturma – durumlarını (örneğin, beklemede, başlatıldı, devam ediyor) gösterir ve tamamlandıklarında veya başarısız olduklarında sizi bilgilendirir.

Her giriş, kısa bir mesaj, kaynak (Ağ, Görev, Kaydet veya Tarayıcı) ve bir zaman damgası gösterir.

Bazı bildirimler yapılandırılmış ayrıntılar içerir. Böyle bir girişe tıkladığınızda, hata verilerinin ayrıntılı bir dökümünü ve bir **JSON Kopyala** düğmesini içeren bir iletişim kutusu açılır. Bu, bir hatayı rapor ederken faydalıdır, çünkü JSON sunucudan gelen tam hata bilgilerini içerir.

Tüm bildirimleri kapatmak için **Tümünü Temizle** seçeneğini kullanın.

!!! not
    Bildirimler yalnızca bellekte saklanır ve sayfayı yeniden yüklediğinizde silinir.
