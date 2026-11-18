# Bildirimler

Üst uygulama çubuğundaki çan, bildirimleri açar. Çandaki bir rozet, okunmamış bildirimlerin sayısını gösterir. Menü, çalışan görevleri ve en son bildirimleri listeler; **Hepsini Göster** tüm bildirim günlüğünü açar. Küçük ekranlarda, çan doğrudan günlüğü açar.

Bildirimler şunlarla ilgilidir:

- **Diğer kullanıcılar tarafından yapılan değişiklikler.** Diğer kullanıcılar Gramps Web'i kullanırken ağacı değiştirdiğinde, bir bildirim kimin neyi değiştirdiğini söyler, örneğin "Kişiyi Düzenle" veya "12 değişiklik". Değişikliği açmak için tıklayın [revizyon geçmişi](revisions.md). Gramps Web kullanıcısı olmayan, örneğin Gramps Desktop ile paylaşılan bir veritabanına doğrudan yapılan değişiklikler, isimsiz olarak gösterilir. Bu, revizyon geçmişini görebilen (üye ve üstü) kullanıcılara özeldir.
- **Arka plan görevleri** – içe aktarmalar ve dışa aktarmalar, rapor oluşturma, OCR metin tanıma, veritabanı yükseltmeleri, birçok nesneyi silme veya düzenleme ve arama dizini yeniden oluşturma gibi – durumlarını (örneğin beklemede, başlatıldı, devam ediyor) gösterir ve tamamlandıklarında veya başarısız olduklarında sizi bilgilendirir.
- **Oturumunuz sırasında meydana gelen hatalar** – başarısız API istekleri, arka plan görevi hataları, kaydetme hataları veya tarayıcı düzeyindeki hatalar.

Tamamlanmış dışa aktarımlar ve medya arşivleri, [Dışa Aktarma sayfasını](../administration/export.md) terk ettikten sonra bile bildirimlerinden indirilebilir.

Bazı bildirimler, başarısız bir görevin hata mesajı gibi yapılandırılmış ayrıntılar içerir. Bildirim günlüğündeki böyle bir girişe tıkladığınızda, hata verilerinin ayrıntılı bir dökümünü ve **JSON'u Kopyala** düğmesini içeren bir diyalog açılır. Bu, bir hatayı bildirdiğinizde faydalıdır, çünkü JSON sunucudan gelen tam hata bilgilerini içerir.

Tüm bildirimleri kaldırmak için bildirim günlüğünde **Hepsini Temizle** seçeneğini kullanın.

Tüm ağacı değiştiren görevler, örneğin bir içe aktarma, bir geri yükleme, tüm nesneleri silme veya arama dizinini yeniden oluşturma, aynı anda çalışamaz. Bir görev çalışırken başka birini başlatırsanız, başka bir görevin bu ağaçta zaten çalıştığını belirten bir mesaj gösterilir ve çalışan görev ilerlemesiyle birlikte gösterilir.

!!! not
    Bildirimler yalnızca bellekte saklanır ve sayfayı yeniden yüklediğinizde silinir. Gramps Web, yalnızca açıkken diğer kullanıcılar tarafından yapılan değişiklikleri kontrol eder, bu nedenle yokken yapılan değişiklikler bildirilmez; bunlar için [Revizyon geçmişi](revisions.md) sayfasına bakın.
