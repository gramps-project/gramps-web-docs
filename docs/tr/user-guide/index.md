---
hide:
  - toc
---

# Kullanıcı Kılavuzu

Bu bölüm, Gramps Web kullanıcılarına sunulan özellikleri belgelemektedir.

!!! note "Tüm özellikleri göremiyor musunuz?"
    Gramps Web, rol tabanlı bir izin sistemi kullanır. Veri düzenleme, etiket yönetimi veya özel kayıtları görüntüleme gibi bazı özellikler yalnızca yeterli izinlere sahip kullanıcılara açıktır. Mevcut rolünüzü [Kullanıcı Ayarları](settings.md) bölümünde kontrol edebilirsiniz. Daha fazla erişim ihtiyacınız varsa, ağaç sahibinizle veya yöneticinizle iletişime geçin. Tüm rollerin açıklaması için [Kullanıcı sistemi](../install_setup/users.md) sayfasına bakın.

## Arayüzde gezinme

### Ana navigasyon

Yan panel (veya mobildeki hamburger menüsü), bölümler arasında geçiş yapmanın birincil yoludur:

- **Ana Sayfa** – kontrol paneli (aşağıya bakınız)
- **Blog** – blog yazısı olarak yazılmış aile tarihi hikayeleri
- **Ağaç** – etkileşimli ağaç grafikleri
- **Zaman Çizelgesi** – ağaçtaki olayların kronolojik görünümü (yeterince güncel bir Gramps Web API sürümü gerektirir)
- **Harita** – ağaçtaki yerlerin coğrafi görünümü
- **DNA** – DNA eşleşme analiz araçları
- **Listeler** – her tür nesneyi gözden geçirin: İnsanlar, Aileler, Olaylar, Yerler, Kaynaklar, Alıntılar, Depolar, Notlar
- **Medya** – tüm medya dosyalarını (fotoğraflar, belgeler vb.) gözden geçirin
- **Asistan** – AI sohbet asistanı (yönetici tarafından etkinleştirildiyse)
- **Geçmiş** – son değiştirilen nesneler
- **Yer İmleri** – kaydedilmiş yer imleriniz
- **Görevler** – araştırma görevleri
- **Raporlar** – rapor oluşturma
- **Dışa Aktar** – aile ağacını dışa aktarma
- **Revizyonlar** – tam işlem geçmişi (üye ve üzeri için görünür)
- **Bildirimler** – geçmiş bildirimler

!!! note
    Etiketler artık yan panelden yönetilmiyor – etiket yönetimi [Yönetim Ayarları](../administration/settings.md#tags) bölümüne taşınmıştır (Sahip/Yönetici sadece). Etiketlerin nasıl kullanıldığı hakkında bilgi için [Etiketler](tags.md) sayfasına bakın.

### Üst uygulama çubuğu

Her sayfanın üst kısmındaki çubuk şunları içerir:

- **Ekle** (artı simgesi, katkıda bulunanlar ve üzeri için görünür) – yeni bir nesne oluşturmak için bir menü açar: Kişi, Aile, Olay, Yer, Kaynak, Alıntı, Depo, Not, Medya Nesnesi veya Görev
- **Ara** (büyüteç) – arama sayfasını açar
- **Kullanıcı simgesi** – ayarlar menüsünü açar: Kullanıcı Ayarları, Yönetim (sahipler için sadece), Kullanıcıları Yönet (sahipler için sadece), Sistem Bilgisi

## Ana sayfa (kontrol paneli)

Kontrol paneli, ilk giriş yaptığınızda gösterilir. İki sütun içerir:

**Sol sütun:**

- **Ana kişi kartı** – seçtiğiniz ana kişinin adını, fotoğrafını (varsa) ve temel bilgilerini gösterir; tam profiline ve aile ağacına hızlı geçiş için bir bağlantı içerir. Karttaki **Ana Kişiyi Ayarla** butonuna tıklayarak farklı bir kişiyi arayıp seçebilirsiniz.
- **Yıldönümleri** – bugünün tarihine göre ağaçtan gelen yaklaşan doğum günleri ve yıldönümleri.
- **Son değişiklikler** – en son değiştirilen nesnelerin kısa bir listesi, işbirlikçi düzenlemeleri takip etmek için faydalıdır.

**Sağ sütun:**

- **Son blog yazıları** – [blog](blog.md) sayfasından en son girişler, varsa.
- **İstatistikler** – ağaçtaki nesne sayılarının özeti (insan sayısı, aile sayısı, olay sayısı vb.).

Eğer ağaç yöneticisi bir **ana sayfa notu** ve/veya bir **ana sayfa resmi** yapılandırmışsa, bunlar ana sütunların üzerinde belirgin bir şekilde görüntülenir. Her ikisi de ayarlandığında resim, not metninin yanında görünür. Bunları nasıl yapılandıracağınız hakkında bilgi için [Yönetim Ayarları](../administration/settings.md#customization) sayfasına bakın.

!!! tip
    Eğer ağaç boşsa ve düzenleme izinleriniz varsa, kontrol paneli ilk kişinizi eklemek veya bir aile ağacı dosyası içe aktarmak için butonlar içeren bir "Başlayın" istemi gösterir.
