# Bildirimler

**Bildirimler**, bir çan simgesi ile gösterilen bir yan menü öğesidir. Hatalar meydana geldiğinde veya arka planda görevler çalışırken, okunmamış bildirimlerin sayısını gösteren bir rozet görünür. Bildirim günlüğünü açmak için üzerine tıklayın.

Bildirim günlüğü iki amaca hizmet eder:

- Oturumunuz sırasında meydana gelen hataların kaydıdır – başarısız API istekleri, arka plan görev hataları, kaydetme hataları veya tarayıcı düzeyindeki hatalar.
- Uzun süren arka plan görevlerinin ilerlemesini takip eder – örneğin, içe aktarma ve dışa aktarma, rapor oluşturma, OCR metin tanıma, veritabanı güncellemeleri ve arama/anlam dizini yeniden oluşturma – durumlarını (örneğin, beklemede, başlatıldı, devam ediyor) gösterir ve tamamlandıklarında veya başarısız olduklarında sizi bilgilendirir.

Her giriş, kısa bir mesaj, kaynak (Ağ, Görev, Kaydetme veya Tarayıcı) ve bir zaman damgası gösterir. Tamamlanan görevler "Görev tamamlandı" veya "Görev başarısız oldu" olarak okunur.

Bazı bildirimler, başarısız bir görevin hata mesajı gibi yapılandırılmış detaylar içerir. Böyle bir girişe tıkladığınızda, hata verilerinin ayrıntılarını gösteren bir diyalog açılır ve bir **JSON Kopyala** butonu bulunur. Bu, bir hatayı rapor ederken faydalıdır, çünkü JSON sunucudan alınan tam hata bilgilerini içerir.

Tüm bildirimleri kaldırmak için **Tümünü Temizle** seçeneğini kullanın.

Tüm ağaç yapısını değiştiren görevler, örneğin bir içe aktarma, bir geri yükleme, tüm nesneleri silme veya arama dizinini yeniden oluşturma, aynı anda çalışamaz. Bir görev çalışırken diğerini başlatırsanız, başka bir görevin bu ağaçta zaten çalıştığına dair bir mesaj görüntülenir ve çalışan görev ilerlemesi ile gösterilir.

!!! not
    Bildirimler yalnızca bellekte saklanır ve sayfayı yeniden yüklediğinizde silinir.
