---
hide:
  - toc
---

# Kullanıcı Kılavuzu

Bu bölüm, Gramps Web kullanıcılarına sunulan özellikleri belgelemektedir.

!!! note "Tüm özellikleri göremiyor musunuz?"
    Gramps Web, rol tabanlı bir izin sistemi kullanır. Veri düzenleme, etiket yönetimi veya özel kayıtları görüntüleme gibi bazı özellikler yalnızca yeterli izinlere sahip kullanıcılara açıktır. Mevcut rolünüzü [Kullanıcı Ayarları](settings.md) bölümünden kontrol edebilirsiniz. Daha fazla erişime ihtiyacınız varsa, ağaç sahibinizle veya yöneticinizle iletişime geçin. Tüm rollerin açıklaması için [Kullanıcı sistemi](../install_setup/users.md) bölümüne bakın.

## Arayüzde gezinme

### Ana navigasyon

Yan panel (veya mobildeki hamburger menü), bölümler arasında geçiş yapmanın birincil yoludur:

- **Ana Sayfa** – gösterge paneli (aşağıya bakın)
- **Blog** – blog yazısı olarak yazılmış aile tarihi hikayeleri
- **Aile Ağacı** – etkileşimli ağaç grafikler
- **Zaman Çizelgesi** – ağaçtaki olayların kronolojik görünümü (yeterince güncel bir Gramps Web API sürümü gerektirir)
- **Harita** – ağaçtaki yerlerin coğrafi görünümü
- **DNA** – DNA eşleşme analiz araçları
- **Listeler** – her türden nesneyi gözden geçirin: İnsanlar, Aileler, Olaylar, Yerler, Kaynaklar, Alıntılar, Depolar, Notlar
- **Medya** – tüm medya dosyalarını (fotoğraflar, belgeler vb.) gözden geçirin
- **Asistan** – AI sohbet asistanı (yönetici tarafından etkinleştirildiyse)
- **Geçmiş** – son değiştirilen nesneler
- **Yer İşaretleri** – kaydedilmiş yer işaretleriniz
- **Görevler** – araştırma görevleri
- **Raporlar** – rapor oluşturma
- **Dışa Aktar** – aile ağacını dışa aktarma
- **Revizyonlar** – tam işlem geçmişi (üye ve üstü için görünür)

!!! note
    Etiketler artık yan panelden yönetilmiyor – etiket yönetimi [Yönetim Ayarları](../administration/settings.md#tags) bölümüne taşındı (Sahip/Yönetici sadece). Etiketlerin nasıl kullanıldığını görmek için [Etiketler](tags.md) bölümüne bakın.

### Üst uygulama çubuğu

Her sayfanın üst kısmındaki çubuk şunları içerir:

- **Ekle** (artı simgesi, katkıda bulunanlar ve üstü için görünür) – yeni bir nesne oluşturmak için bir menü açar: Kişi, Aile, Olay, Yer, Kaynak, Alıntı, Depo, Not, Medya Nesnesi veya Görev
- **Ara** (büyüteç) – arama sayfasını açar
- **Çan** – diğer kullanıcılar tarafından yapılan değişiklikler ve tamamlanan arka plan görevlerini içeren [bildirimleri](notifications.md) açar
- **Kullanıcı simgesi** – ayarlar menüsünü açar: Kullanıcı Ayarları, Yönetim (sahipler için yalnızca), Kullanıcıları Yönet (sahipler için yalnızca), Sistem Bilgisi

## Ana sayfa (gösterge paneli)

Gösterge paneli, ilk giriş yaptığınızda gösterilir. İki sütun içerir:

**Sol sütun:**

- **Ana kişi kartı** – seçtiğiniz ana kişinin adı, fotoğrafı (varsa) ve temel bilgilerini gösterir; tam profiline bağlantı ve aile ağacına hızlı navigasyon sağlar. Karttaki **Ana Kişiyi Belirle** butonuna tıklayarak farklı bir kişiyi arayıp seçebilirsiniz.
- **Yıldönümleri** – bugünün tarihine göre ağaçtan yaklaşan doğum günleri ve yıldönümleri.
- **Son değişiklikler** – işbirlikçi düzenlemeleri takip etmek için yararlı olan en son değiştirilen nesnelerin kısa bir listesi.

**Sağ sütun:**

- **Son blog yazıları** – [blog](blog.md) bölümünden en son girişler, varsa.
- **İstatistikler** – ağaçtaki nesne sayılarının özeti (insan sayısı, aileler, olaylar vb.).

Ağaç hala boşken, gösterge paneli gösterilecek hiçbir şeyi olmayan panelleri gizler ve bunun yerine düzenleme izinlerine sahip kullanıcılar için bir **Başlayın** kartı gösterir: ilk olarak bir kişi oluşturmayı veya bir aile ağacı dosyası içe aktarmayı önerir ve insanlar var olduğunda, onları bir aile oluşturarak bağlamayı önerir. Ağaç bir aile içerdiği anda kart kaybolur.

Eğer ağaç yöneticisi bir **ana sayfa notu** ve/veya bir **ana sayfa resmi** yapılandırmışsa, bunlar ana sütunların üzerinde belirgin bir şekilde gösterilir. Her ikisi de ayarlandığında, resim not metninin yanında görünür. Bunları yapılandırmak için [Yönetim Ayarları](../administration/customization.md) bölümüne bakın.

!!! tip
    Ağaç boşsa ve düzenleme izinleriniz varsa, gösterge paneli ilk kişinizi eklemek veya bir aile ağacı dosyası içe aktarmak için butonlarla bir "Başlayın" istemi gösterir.

## Gramps Web'i bir uygulama olarak kurma

Gramps Web, tarayıcınızın diğer uygulamalarınızla birlikte kurabileceği bir ilerici web uygulamasıdır (PWA). Böylece, tarayıcı sekmesinde tutmak yerine kendi simgesini alır ve kendi penceresinde, adres çubuğu ve tarayıcı araç çubukları olmadan açılır.

Nasıl kuracağınız, tarayıcınıza bağlıdır:

- **Android (Chrome)** – menüyü açın ve "Uygulamayı Kur" veya "Ana Ekrana Ekle" seçeneğini seçin.
- **iOS/iPadOS (Safari)** – paylaşım butonuna dokunun ve "Ana Ekrana Ekle" seçeneğini seçin.
- **Masaüstü (Chrome, Edge)** – adres çubuğunun sağ ucundaki kurulum simgesine tıklayın veya tarayıcı menüsündeki "Kur" seçeneğini kullanın.
- **Masaüstü (Firefox, Safari)** – kurulum desteklenmiyor; normal bir tarayıcı sekmesi veya penceresi kullanın.

Gramps Web'in çalışma şekli değişmez ve hiçbir veri farklı bir şekilde saklanmaz – bu, yalnızca bağımsız bir uygulama olarak sunulan aynı uygulamadır.

!!! note
    Gramps Web, verilerinizi gösterebilmek için hala sunucunuza ulaşması gerektiğinden, kurulu bir uygulama aile ağacınızı çevrimdışı olarak gözden geçirmenize izin vermez.
