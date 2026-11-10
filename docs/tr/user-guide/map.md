# Harita

Harita sayfası, aile ağacınızdaki tüm yerleri etkileşimli işaretçiler olarak coğrafi bir haritada görüntüler. Yan menüden erişilebilir.

## Yer işaretçileri

Sadece Gramps veritabanında GPS koordinatları saklanan yerler haritada gösterilir. Koordinatları olmayan yerler sessizce atlanır. GPS koordinatları, yer detay sayfasında ayarlanabilir (yeri düzenleyin ve enlem ve boylam alanlarını doldurun).

!!! ipucu
    Haritada birçok yeriniz eksikse, bir yer detay sayfasını açın ve enlem ve boylamın ayarlanıp ayarlanmadığını kontrol edin. Koordinatları, yerin düzenleme görünümünden doğrudan ekleyebilir veya düzeltebilirsiniz.

Koordinatları olan her yer bir işaretçi olarak gösterilir. Bir işaretçiye tıkladığınızda, yer adı ve bağlantılı olaylar ile kişiler içeren bir özet kartı açılır. Karttaki yer adına tıklayarak tam yer detay sayfasını açabilirsiniz.

## Arama

Haritanın sol üst köşesindeki arama kutusu, yazdıkça arama yapar ve sonuçları üç başlık altında gruplar:

- **Yerler** – aile ağacınızdaki yerler. Birini seçmek, haritayı ona kaydırır ve işaretçisini vurgular.
- **Kişiler** – aile ağacınızdaki kişiler. Birini seçmek, haritayı [aşağıda](#bir-kisiyi-harita-uzerinde-takip-etme) tanımlanan kişi görünümüne geçirir.
- **Dış** – [OpenStreetMap](https://www.openstreetmap.org/) üzerindeki, dünyanın herhangi bir yerinden konumlar. Birini seçmek, haritayı o konuma kaydırır ve yakınlaştırır; ağaçtaki yerleri filtrelemez veya değiştirmez.

Dış sonuçlar, bir yere koordinat eklerken de faydalıdır: buradan konumu kontrol edebilir ve enlem ve boylamını girmeden önce nerede olduğunu görebilirsiniz.

## Bir kişiyi harita üzerinde takip etme

Bir kişiyi seçmek – haritanın arama kutusundan veya bir kişinin detay sayfasındaki **Haritada Aç** düğmesi ile – o kişinin olaylarıyla bağlantılı yerleri, kronolojik sırayla çizgilerle birleştirerek gösterir. Her çizgi boyunca küçük oklar, seyahat yönünü belirtir, böylece bir kişinin yaşamını doğumundan ölümüne kadar harita üzerinde takip edebilirsiniz.

Bir yer detay sayfasındaki yerler de **Haritada Aç** düğmesine sahiptir; bu, haritayı o yerin merkezine açar.

## Zaman kaydırıcı

Sayfanın altındaki zaman kaydırıcı, hangi yer işaretçilerinin gösterileceğini, bunların ilişkili olaylarının yılına göre filtreler:

- Bir yılı seçmek için tutamağı sürükleyin.
- Seçilen zaman aralığına düşen olaylarla bağlantılı yerler gösterilir.
- Bunu, atalarınızın belirli bir tarihsel noktada nerede yaşadığını izlemek için kullanın.

## Harita katmanları

Bir katman anahtarı düğmesi (yığılmış katmanlar simgesi, sol alt) iki temel harita arasında seçim yapmanıza olanak tanır. Altında, "Sizin haritalarınız" altında kendi harita katmanlarınızı listeler (bkz. [Özel harita örtüleri](#ozel-harita-ortuleri) ve [Yerlerin harita dosyaları](#yerlerin-harita-dosyalari)) ve "Dış" altında [Wikidata binaları](#wikidata-binalari) katmanını, her birini açıp kapatabileceğiniz şekilde gösterir.

Her iki temel haritanın etiketleri, Gramps Web'de seçtiğiniz dilde gösterilir; harita verilerinin o dilde bir adı varsa, yerel adı gösterilir.

### Temel Harita

Varsayılan katman, [OpenFreeMap](https://openfreemap.org) tarafından desteklenmektedir (açık mod için Liberty stili, koyu mod için koyu stil). Bu, yerleri bulmak için uygun modern genel amaçlı bir haritadır.

### Tarihsel Harita

Temel haritayı [OpenHistoricalMap](https://www.openhistoricalmap.org) (OHM) ile değiştirir; bu, dünyanın farklı zaman dilimlerinde nasıl göründüğünü haritalayan topluluk destekli bir projedir – bunu, OpenStreetMap'in tarihsel bir karşıtı olarak düşünün.

Tarihsel Harita katmanı aktif olduğunda, zaman kaydırıcı aynı zamanda harita karolarını da filtreler: OHM, haritayı seçilen yılda nasıl göründüğü gibi işler, böylece tarihsel sınırlar, yer adları ve özellikler modern olanların yerine gösterilir. Bu, hem atalarınızın konumunu hem de çağdaş coğrafi ve siyasi bağlamı tek bir görünümde görmenizi sağlar.

!!! not
    OpenHistoricalMap kapsamı bölge ve döneme göre değişir. Az katkı olan alanlar veya dönemler sınırlı tarihsel detay gösterebilir. Eksik veya hatalı tarihsel veriler fark ederseniz, [OpenHistoricalMap'e katkıda bulunmayı](https://www.openhistoricalmap.org) düşünün – bu, herkesin düzenleyebileceği açık bir topluluk projesidir.

## Özel harita örtüleri

Yerleşik temel katmanların yanı sıra, Gramps'te **Medya** nesnesi olarak saklanan herhangi bir taranmış tarihsel harita görüntüsünü, canlı harita üzerinde konumlandırılmış özel bir örtü haline getirebilirsiniz. Bu, eski şehir planlarının, pariş haritalarının veya modern veya tarihsel coğrafya ile doğrudan karşılaştırmak istediğiniz mülk haritalarının taramaları için faydalıdır.

### Bir görüntüyü coğrafi referanslama

1. Taranmış harita görüntüsü için medya nesnesini açın ve düzenleme moduna geçin.
2. "Harita" sekmesini açın ve **Koordinatları Düzenle**'ye tıklayın. Bu, görüntü ile birlikte bir harita içeren bir coğrafi referanslama iletişim kutusu açar.
3. **Haritada bir nokta seçin**'e tıklayın, ardından görüntüdeki bir noktanın karşılık gelmesi gereken haritadaki konuma tıklayın. Bir nokta seçildiğinde, görüntü haritada ilk kez yerleştirilir.
4. Görüntüyü yeniden boyutlandırmak için **Ölçek** kaydırıcısını ve konumlandırma sırasında temel haritayı görmenizi sağlamak için **Saydamlık** kaydırıcısını kullanın.
5. **Görüntüyü Hizala**'ya tıklayın ve görüntüyü, sabitlenmiş noktanın tam olarak hizalanması için haritada tekrar tıklayarak kaydırın.
6. Görüntü, alttaki coğrafya ile eşleşene kadar ölçek, saydamlık ve hizalama adımlarını tekrarlayın, ardından kaydedin.

Arka planda, bu, görüntünün köşe koordinatlarını medya nesnesinde bir `map:bounds` niteliğinde saklar.

### Harita sayfasında örtüleri görüntüleme

Bir medya nesnesi bu şekilde coğrafi referanslandığında, otomatik olarak Harita sayfasında açılıp kapatılabilir bir katman olarak kullanılabilir hale gelir. Her örtüyü temel haritadan bağımsız olarak göstermek veya gizlemek için katman anahtarını açın (yığılmış katmanlar simgesi, sol alt). Örtüler, medya nesnesinin başlığına göre listelenir.

Her örtünün adının altında bir saydamlık kaydırıcısı vardır, böylece temel haritayı onun üzerinden görebilirsiniz.

## Yerlerin harita dosyaları

Yerlerin, medya nesneleri olarak eklenmiş harita dosyaları olabilir – örneğin bir parişin, bir bölgenin veya bir mülkün sınırları veya bir güzergah. Desteklenen dosya türleri KML (`.kml`), GeoJSON (`.geojson`) ve GPX (`.gpx`) dosyalarıdır.

Haritada bir yeri seçtiğinizde, harita dosyaları haritanın üstünde çizilir ve dosyada varsa renkler kullanılır. Bu, koordinatı olmayan yerler için de çalışır: harita, dosyaların kapsadığı alana yakınlaştırılır. Yer seçili iken, dosyaları "Sizin haritalarınız" altında katman anahtarında listelenir; burada her birini kapatabilirsiniz.

Bir harita dosyasını bir yere eklemek için, onu diğer [medya dosyaları](media.md) gibi yerin galerisine ekleyin.

## Wikidata binaları

"Wikidata binaları" katmanı, [Wikidata](https://www.wikidata.org/) üzerinde kaydedilen binaları gösterir; bunlar arasında kiliseler, çiftlikler veya apartmanlar bulunur. Varsayılan olarak kapalıdır ve "Dış" altında katman anahtarında açılabilir. Binalar, harita yeterince yakınlaştırıldığında yalnızca gösterilir. Zaman kaydırıcı aktif olduğunda, yalnızca seçilen zamanda var olan binalar gösterilir.

Bir binaya tıklayarak, Wikidata'dan ne zaman inşa edildiği veya yıkıldığı, adresleri, sakinleri ve sahipleri gibi detaylarını görebilirsiniz.

### Bir binayı yer olarak kaydetme

Nesne ekleyebilen kullanıcılar, binanın detaylarında **Yeri kaydet** düğmesini görür. Bu, binanın adını kendi dilinizle, bir yer türü (`Çiftlik` çiftlikler için, aksi takdirde `Bina`), koordinatlarını ve Wikidata öğesine bir bağlantıyı önceden doldurulmuş olarak içeren yeni bir yer formunu açar. Formu tamamlayın, örneğin çevreleyen yeri seçerek ve kaydedin.

Eğer ağaçtaki bir yer, binanın bulunduğu konumdaysa, düğme **Kaydedilen yeri aç** olarak değişir ve o yeri gösterir.

!!! bilgi
    Sunucu yöneticisi, `mapWikidata` seçeneği ile [ön uç yapılandırması](../install_setup/frontend-config.md) kullanarak Wikidata binaları katmanını kaldırabilir.
