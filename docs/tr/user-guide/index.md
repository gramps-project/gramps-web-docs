---
hide:
  - toc
---

# Kullanıcı Kılavuzu

Bu bölüm, Gramps Web kullanıcılarına sunulan özellikleri belgeler.

!!! note "Tüm özellikleri göremiyor musunuz?"
    Gramps Web, rol tabanlı bir izin sistemi kullanır. Veri düzenleme, etiket yönetimi veya özel kayıtları görüntüleme gibi bazı özellikler yalnızca yeterli izinlere sahip kullanıcılara açıktır. Mevcut rolünüzü [Kullanıcı Ayarları](settings.md) bölümünde kontrol edebilirsiniz. Daha fazla erişime ihtiyacınız varsa, ağaç sahibi veya yöneticinizle iletişime geçin. Tüm rollerin tanımı için [Kullanıcı sistemi](../install_setup/users.md) bölümüne bakın.

## Arayüzde gezinme

### Ana navigasyon

Yan panel (veya mobildeki hamburger menü), bölümler arasında geçiş yapmanın birincil yoludur:

- **Ana Sayfa** – kontrol paneli (aşağıya bakın)
- **Blog** – blog yazısı olarak yazılmış aile tarihi hikayeleri
- **Aile Ağacı** – etkileşimli ağaç grafikleri
- **Zaman Çizelgesi** – ağaçtaki olayların kronolojik görünümü (yeterince güncel bir Gramps Web API sürümü gerektirir)
- **Harita** – ağaçtaki yerlerin coğrafi görünümü
- **DNA** – DNA eşleşme analiz araçları
- **Listeler** – her tür nesneyi tarayın: İnsanlar, Aileler, Olaylar, Yerler, Kaynaklar, Alıntılar, Depolar, Notlar
- **Medya** – tüm medya dosyalarını (fotoğraflar, belgeler vb.) tarayın
- **Asistan** – AI sohbet asistanı (yönetici tarafından etkinleştirildiyse)
- **Geçmiş** – son değiştirilen nesneler
- **Yer İşaretleri** – kaydedilmiş yer işaretleriniz
- **Görevler** – araştırma görevleri
- **Raporlar** – rapor oluşturun
- **Dışa Aktar** – aile ağacını dışa aktarın
- **Revizyonlar** – tam işlem geçmişi (üye ve üstü için görünür)
- **Bildirimler** – geçmiş bildirimler

!!! note
    Etiketler artık yan panelden yönetilmiyor – etiket yönetimi [Yönetim Ayarları](../administration/settings.md#tags) bölümüne taşındı (Sahip/Yönetici yalnızca). Etiketlerin nasıl kullanıldığı hakkında bilgi için [Etiketler](tags.md) bölümüne bakın.

### Üst uygulama çubuğu

Her sayfanın üst kısmındaki çubuk şunları içerir:

- **Ekle** (artı simgesi, katkıda bulunanlar ve üstü için görünür) – yeni bir nesne oluşturmak için bir menü açar: Kişi, Aile, Olay, Yer, Kaynak, Alıntı, Depo, Not, Medya Nesnesi veya Görev
- **Ara** (büyüteç) – arama sayfasını açar
- **Kullanıcı simgesi** – ayarlar menüsünü açar: Kullanıcı Ayarları, Yönetim (sahipler için yalnızca), Kullanıcıları Yönet (sahipler için yalnızca), Sistem Bilgisi

## Ana sayfa (kontrol paneli)

Kontrol paneli, ilk giriş yaptığınızda gösterilir. İki sütun içerir:

**Sol sütun:**

- **Ana kişi kartı** – seçtiğiniz ana kişinin adını, fotoğrafını (varsa) ve temel bilgilerini gösterir; tam profiline bağlantı ve aile ağacına hızlı navigasyon sağlar. Karttaki **Ana Kişiyi Ayarla** butonuna tıklayarak farklı bir kişiyi arayıp seçebilirsiniz.
- **Yıldönümleri** – bugünün tarihine göre ağaçtan yaklaşan doğum günleri ve yıldönümleri.
- **Son değişiklikler** – en son değiştirilen nesnelerin kısa bir listesi, işbirlikçi düzenlemeleri takip etmek için faydalıdır.

**Sağ sütun:**

- **Son blog yazıları** – [blog](blog.md) bölümünden en son girişler, varsa.
- **İstatistikler** – ağaçtaki nesne sayılarının özeti (insan sayısı, aile sayısı, olay sayısı vb.).

Ağaç yöneticisi bir **ana sayfa notu** ve/veya bir **ana sayfa resmi** yapılandırdıysa, bunlar ana sütunların üzerinde belirgin bir şekilde görüntülenir. Her ikisi de ayarlandığında resim, not metninin yanında görünür. Bunları yapılandırmak için [Yönetim Ayarları](../administration/settings.md#customization) bölümüne bakın.

!!! tip
    Ağaç boşsa ve düzenleme izinleriniz varsa, kontrol paneli ilk kişinizi eklemek veya bir aile ağacı dosyası içe aktarmak için butonlar içeren bir "Başlayın" istemi gösterir.

## Gramps Web'i uygulama olarak yükleme

Gramps Web, tarayıcınızın diğer uygulamalarınızla birlikte yükleyebileceğiniz bir ilerici web uygulamasıdır (PWA), bu da onu bir tarayıcı sekmesinde tutmak yerine yükleyebileceğiniz anlamına gelir. Kendi simgesini alır ve adres çubuğu ve tarayıcı araç çubukları olmadan kendi penceresinde açılır.

Nasıl yükleyeceğiniz tarayıcınıza bağlıdır:

- **Android (Chrome)** – menüyü açın ve "Uygulamayı Yükle" veya "Ana Ekrana Ekle" seçeneğini seçin.
- **iOS/iPadOS (Safari)** – paylaşım butonuna dokunun ve "Ana Ekrana Ekle" seçeneğini seçin.
- **Masaüstü (Chrome, Edge)** – adres çubuğunun sağ ucundaki yükleme simgesine tıklayın veya tarayıcı menüsündeki "Yükle" seçeneğini kullanın.
- **Masaüstü (Firefox, Safari)** – yükleme desteklenmiyor; normal bir tarayıcı sekmesi veya penceresi kullanın.

Gramps Web'in çalışma şekli değişmez ve veriler farklı bir şekilde saklanmaz – bu, yalnızca bağımsız bir uygulama olarak sunulan aynı uygulamadır.

!!! note
    Gramps Web, verilerinizi göstermek için hala sunucunuza ulaşması gerektiğinden, yüklenmiş bir uygulama aile ağacınızı çevrimdışı olarak taramanıza izin vermez.
