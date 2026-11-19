---
hide:
  - toc
  - navigation
---

# Özellikler

Gramps Web, işbirlikçi soybilim için bir web uygulamasıdır. Açık kaynaklı soybilim programı [Gramps](https://gramps-project.org/) üzerine inşa edilmiştir ve aynı verilerle çalışır. Kendi sunucunuzda çalıştırabilir veya bir barındırma sağlayıcısı kullanabilirsiniz.

[Demoyu deneyin](#demo){ .md-button .md-button--primary } [Başlayın](../install_setup/setup.md){ .md-button }

## Aile ağacınızı keşfedin { .feature-group }

![Yedi nesil atayı gösteren fan grafiği](screenshots/fan.png){ align=right width="400"}

### Etkileşimli aile ağacı grafikleri

Aile ağacınızı, yüksek kaliteli etkileşimli grafiklerle ve yapılandırılabilir nesil sayısıyla bir ata ağacı, soy ağacı, kum saati grafiği, ilişki grafiği veya fan grafiği olarak gezin.

Herhangi bir kişinin üzerine gelerek ana bilgileri içeren bir önizleme kartı görebilir ve grafikten tam detay sayfasına doğrudan geçiş yapabilirsiniz.

<div style="clear:both;"></div>

---

![1940'lar ve 1970'ler arasındaki aile olaylarının zaman çizelgesi](screenshots/timeline.png){ align=left width="400"}

### Kronolojik zaman çizelgesi

Aile ağacınızdaki her olayı yatay, yakınlaştırılabilir bir zaman çizelgesinde görün. Yüzyıllar boyunca kaydırın ve yakınlaştırın, ardından tek bir kişiye – ya da tüm atalarına veya soyundan gelenlerine – ya da bir yerde gerçekleşen her şeye filtreleyin.

[Zaman Çizelgesi](../user-guide/timeline.md) sayfasına bakın.

<div style="clear:both;"></div>

---

![Seçili bir yerin fotoğrafı ve olaylarını gösteren Londra haritası](screenshots/map.png){ align=right width="400"}

### Etkileşimli harita

Ağaçınızdaki tüm yerleri etkileşimli, aranabilir bir haritada görüntüleyin. Bir yer oluştururken OpenStreetMap'te yeni yerler arayın, veritabanınızdaki kişileri coğrafi olarak haritada yerleştirin ve bir kişinin yaşamını haritadaki olaylarını birbirine bağlayarak takip edin.

<div style="clear:both;"></div>

---

![Zaman kaydırıcısının 1707'ye ayarlandığı OpenHistoricalMap katmanındaki Londra](screenshots/ohm.png){ align=left width="400"}

### Tarihsel haritalar

Gramps'ta medya nesnesi olarak saklanan bir tarihsel haritayı özel bir harita örtüsü haline getirin.

Ayrıca, [OpenHistoricalMap](https://www.openhistoricalmap.org/) projesinin tarihsel vektör haritalarına geçiş yapabilirsiniz. Zaman kaydırıcısını kullanarak aile tarihinizdeki yerlerin evrimini gözlemleyin ve atalarınızın yaşadığı veya olayların gerçekleştiği yerleri görüntüleyin.

<div style="clear:both;"></div>

---

![Kişiler, olaylar ve medya için "Albert" arama sonuçları](screenshots/search.png){ align=right width="400"}

### Her şeyi bulun

Tam metin arama motoru, metin notlarının içeriği de dahil olmak üzere tüm Gramps nesne türlerini kapsar ve joker karakterler ile mantıksal operatörleri destekler.

Kesin sorgular için, nesne liste görünümleri, [Gramps Nesne Sorgu Dili](../user-guide/goql.md) temelinde gelişmiş bir filtreleme modu sunar ve metin, etiket ve gizlilikle hızlı filtreler sağlar.

Herhangi bir kişinin sayfasından, [Dış Arama](../user-guide/external-search.md) FamilySearch, Ancestry, CompGen ve diğer sitelerde önceden doldurulmuş bir arama açar – ve kendi aramalarınızı ekleyebilirsiniz.

<div style="clear:both;"></div>

## İnşa et ve araştır { .feature-group }

![Aile üyesi ekleme iletişimi ile düzenleme modundaki ata ağacı](screenshots/tree-edit.png){ align=left width="400"}

### Ağacınızı doğrudan grafikte oluşturun

Ağaç görünümünü düzenleme moduna geçirin ve aile ağacınızı grafiği terk etmeden büyütün. Her kişi kartı, bir baba, anne, çocuk veya eş eklemek için bir **+** butonu alır – ya mevcut veritabanınızdaki birine bağlantı kurarak ya da yerinde tamamen yeni bir kişi oluşturarak. Her değişiklik hemen kaydedilir.

[Aile Ağacını Düzenleme](../user-guide/tree-edit.md) sayfasına bakın.

<div style="clear:both;"></div>

---

![Bir doğum belgesini okuyan ve yeni kayıtlar öneren AI asistanı](screenshots/chat.png){ align=right width="400"}

### Entegre AI asistanı

Aile ağacınız hakkında kendi dilinizde sorular sorun ve verilerinize dayalı yanıtlar alın.

Asistan sadece arama yapmakla kalmaz: veritabanınıza doğrudan bir dizi araçla sorgular yapar, kişileri, olayları, aileleri ve yerleri filtreler ve bireyler arasındaki ilişkileri hesaplar. Bir yanıt oluştururken hangi araçları kullandığını izleyebilirsiniz ve daha uzun sorular arka plan görevleri olarak çalışır, böylece başka bir yere geçip geri dönebilirsiniz.

Asistan isteğe bağlıdır ve bir AI modeli sağlayıcısıyla [sunucu yöneticisi tarafından ayarlanması](../install_setup/chat.md) gerekir.

<div style="clear:both;"></div>

---

![On bir eşleşmenin paylaşılan DNA segmentlerini gösteren kromozom tarayıcısı](screenshots/dna.png){ align=left width="400"}

### DNA eşleşmeleri, kromozom tarayıcısı & Y-DNA

DNA test sağlayıcınızdan DNA eşleşme verilerini yükleyin, bunları aile ağacınızla birlikte saklayın ve eşleşmelerinizi etkileşimli bir kromozom tarayıcısında görüntüleyin.

Ham Y kromozomu SNP verileri, bir kişinin en olası [Y-DNA haplogrupunu](../user-guide/y-dna.md) belirlemek için kullanılabilir ve zaman tahminleri ile insan Y kromozomu ağacında babasal atalarını görüntüleyebilirsiniz. Analiz tamamen kendi sunucunuzda çalışır – hiçbir veri üçüncü taraflara gönderilmez.

<div style="clear:both;"></div>

---

![İki kişinin etiketlendiği ve diğer tespit edilen yüzlerin çizildiği bir resim](screenshots/tag.png){ align=right width="400"}

### Otomatik yüz tanıma ile fotoğraflardaki kişileri etiketleyin

Eski aile fotoğraflarındaki ataları akrabalarınızla birlikte tanımlayın. Yüzler otomatik olarak tespit edilir, bu nedenle bir kişiyi etiketlemek iki tıklama alır.

<div style="clear:both;"></div>

---

![Durum, öncelik ve etiketlerle araştırma görevleri listesi](screenshots/tasks.png){ align=left width="400"}

### Entegre görev yönetim uygulaması

Gramps Web, soybilim araştırmanızı organize etmek ve planlamak için entegre bir görev yönetim uygulaması ile birlikte gelir. Her göreve bir durum, öncelik ve etiket verin, ilerlemenizi zengin metin açıklamasıyla belgeleyin ve topladığınız medyayı ekleyin.

Görevler, Gramps veritabanında kaynaklar olarak saklanır, bu nedenle soybilim verilerinizin bir parçasını oluşturur ve Gramps Desktop'ta da erişilip düzenlenebilir.

<div style="clear:both;"></div>

---

![Bir aile fotoğrafındaki kişileri tanımlama hakkında blog yazısı](screenshots/blog.png){ align=right width="400"}

### Dahil olan soybilim blogu

Araştırmanızı resimlerle birlikte blog hikayeleri şeklinde özetleyin ve akrabalarınızla paylaşın. Yeni bir gönderi yazmayı kolaylaştıran özel bir editör vardır. Tüm veriler Gramps veritabanında saklanır.

<div style="clear:both;"></div>

## Birlikte çalışın { .feature-group }

![Aile ağacındaki kişilerin listesi](screenshots/list.png){ align=left width="400"}

### Gizlilik seviyeleri & kullanıcı erişimi

Kayıtları [özel olarak işaretleyebilirsiniz](../user-guide/privacy.md) – tek bir isim, olay bağlantısı veya DNA eşleşmesine kadar – ve hangi kullanıcıların özel kayıtlara erişebileceğini kontrol edebilirsiniz. Özel kayıtlar, maksimum güvenlik için veritabanı katmanında filtrelenir. Ayrıca, kullanıcıların ekleyip düzenleyebileceği şeyleri kontrol edebilirsiniz.

Kullanıcılar bir şifre ile veya [OpenID Connect](../install_setup/oidc.md) kullanarak bir dış kimlik sağlayıcısı aracılığıyla – kutudan çıkar çıkmaz Google ve Microsoft, ayrıca Keycloak, Authentik ve Authelia gibi özel sağlayıcılar ile – oturum açabilirler.

<div style="clear:both;"></div>

---

![Bir kişi kaydındaki değiştirilen alanları gösteren bir revizyon](screenshots/revisions.png){ align=right width="400"}

### Tam revizyon geçmişi – geri alma ile

Aile ağacınızdaki her düzenleme kaydedilir. İşlemlerle gruplandırılmış tam geçmişi gözden geçirin, herhangi bir bireysel değişikliğe inin ve hangi alanların eklendiğini, kaldırıldığını veya değiştirildiğini tam olarak görün, ve bir işlem hatalıysa geri alın. Her nesnenin sayfasında ayrıca kimin ve ne zaman değiştirdiğini gösteren kendi revizyon sekmesi vardır.

[Revizyon Geçmişi](../user-guide/revisions.md) sayfasına bakın.

<div style="clear:both;"></div>

---

![Gramps Desktop'un Araçlar menüsünde Gramps Web Senkronizasyonu girişi](screenshots/sync.png){ align=left width="300"}

### Gramps Desktop ile tam entegrasyon

Gramps Web, [Gramps Desktop](https://gramps-project.org/) ile aynı veri modeli ve veritabanını kullanır. Tüm aynı [kayıt türlerini](https://gramps-project.org/wiki/index.php/Gramps_Data_Model): kişiler, aileler, olaylar, yerler, depolar, kaynaklar, alıntılar, medya nesneleri ve notlar üzerinde gezinebilir ve düzenleyebilirsiniz.

Gramps Desktop için [Gramps Web Senkronizasyonu eklentisi](../administration/sync.md) ile verilerinizi her iki yönde senkronize edebilir, böylece Gramps Desktop ve Gramps Web'de yan yana çalışmaya devam edebilirsiniz.

<div style="clear:both;"></div>

## Raporlar ve veri dışa aktarma { .feature-group }

![PDF olarak oluşturulmuş bir ata raporu](screenshots/report.png){ align=right width="400"}

### Yazdırılabilir raporlar oluşturun

Gramps Web, Gramps Desktop ile aynı çekirdek üzerine inşa edilmiştir, bu nedenle masaüstü uygulamanın desteklediği hemen hemen tüm [raporları](https://gramps-project.org/wiki/index.php/Gramps_6.0_Wiki_Manual_-_Reports) tarayıcıdan oluşturabilirsiniz, ilişki grafiklerini veya kitap raporlarını PDF olarak dahil.

<div style="clear:both;"></div>

---

![Mevcut dosya formatlarının listesini içeren dışa aktarma sayfası](screenshots/export.png){ align=left width="300"}

### Kilitlenme yok – veri içe aktarma ve dışa aktarma

Verileri çeşitli formatlarda içe aktarın, Gramps XML ve GEDCOM dahil, ve tüm verilerinizi herhangi bir zamanda – aile ağacı verileri, medya dosyaları ve kullanıcı hesapları – yedekleme veya farklı bir sunucuya geçiş için indirin.

İçe aktarımlar, herhangi bir şey yazılmadan önce bir deneme olarak önizlenebilir ve tam bir yedekleme ağaca geri yüklenebilir.

<div style="clear:both;"></div>

## Her yerde kullanın { .feature-group }

![Aynı kişi sayfası masaüstünde ve telefonda](screenshots/mobile.png){ align=right width="400"}

### Her cihazda çalışır

Gramps Web'i web tarayıcısına sahip herhangi bir cihazda kullanın: fotoğrafları yükleyin, kayıt oluşturun veya düzenleyin veya aile ağacınızı bir sonraki aile buluşmasında akrabalarınıza gösterin.

Gramps Web, ilerici bir web uygulamasıdır: ana ekranınıza veya masaüstünüze yükleyin ve yerel bir uygulama gibi davranır. Masaüstünde, [klavye kısayolları](../user-guide/shortcuts.md) birkaç tuş vuruşuyla her yere ulaşmanızı sağlar – hepsini görmek için `?` tuşuna basın.

<div style="clear:both;"></div>

---

![Dil seçim menüsü](screenshots/lang.png){ align=left width="300"}

### Tamamen uluslararasılaştırılmış

Arayüzü Gramps topluluğu tarafından çevrilen 50'den fazla dilde kullanın.

<div style="clear:both;"></div>

## Ve daha fazlası

- **Bildirimler ve arka plan görevleri** – içe aktarmalar, dışa aktarmalar, raporlar ve indeks yeniden oluşturma işlemleri arka planda çalışır, ilerleme ve hatalar tek bir yerde toplanır
- **Etiketler, yer işaretleri ve geçmiş** – nesneleri renk kodlu etiketlerle organize edin ve üzerinde çalıştığınız şeye geri dönün
- **Toplu düzenleme** – liste görünümlerinde birden fazla nesneyi seçerek hepsini birden silin veya yinelenen nesneleri birleştirin
- **Özelleştirilebilir liste görünümleri** – hangi sütunların gösterileceğini seçin ve metin, etiket veya gizlilikle filtreleyin
- **Metin tanıma (OCR)** – medya galerinizdeki taranmış belgelerden metin çıkarın
- **Veri doğrulama** – ağacınızı mantıksız tarihler ve diğer veri sorunları için kontrol edin
- **Takvimler** – tarihleri Gregoryen, Julian, İbrani, Fransız Cumhuriyeti, Pers, İslam veya İsveç takvimine göre girin
- **Kendinize ait hale getirin** – sitenize kendi adını, tema renklerini ve ana sayfa metni ve resmini verin

## Demo

Demoya giriş yapmak için aşağıdaki kullanıcı adı/şifre çiftlerinden birini kullanın. Her biri Gramps Web'deki kullanıcı rollerinden birini temsil eder.

`owner / owner` <br>
`editor / editor` <br>
`contributor / contributor` <br>
`member / member`

Demo her iki saatte bir sıfırlanır, bu nedenle yaptığınız değişiklikler geçicidir.

[Demo Girişine Git](https://demo.grampsweb.org/){ .md-button .md-button--primary target="_blank"}

### Teşekkürler

Demo, DigitalOcean tarafından nazikçe desteklenmektedir.

<a href="https://www.digitalocean.com/?refcode=b1d13ebe86ac&utm_campaign=Referral_Invite&utm_medium=Referral_Program&utm_source=badge"><img src="https://web-platforms.sfo2.cdn.digitaloceanspaces.com/WWW/Badge%202.svg" alt="DigitalOcean Referral Badge" /></a>
