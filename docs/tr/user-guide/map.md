# Harita

Harita sayfası, ağaçtaki tüm yerleri coğrafi harita üzerinde etkileşimli işaretleyiciler olarak gösterir. Kenar çubuğundan erişilebilir.

## Yer işaretleri

Haritada yalnızca Gramps veritabanında GPS koordinatları saklanan yerler gösterilir. Koordinatları olmayan yerler sessizce atlanır. GPS koordinatları, yer detay sayfasında ayarlanabilir (yeri düzenleyin ve enlem ile boylam alanlarını doldurun).

!!! ipucu
    Haritanızda birçok yer eksikse, bir yer detay sayfasını açın ve enlem ile boylamın ayarlanıp ayarlanmadığını kontrol edin. Koordinatları, yerin düzenleme görünümünden doğrudan ekleyebilir veya düzeltebilirsiniz.

Koordinatları olan her yer bir işaretçi olarak gösterilir. Bir işaretçiye tıkladığınızda, yerin adı ve bağlantılı olaylar ile kişiler hakkında bilgi veren bir özet kartı açılır. Karttaki yer adına tıklayarak tam yer detay sayfasını açabilirsiniz.

## Arama

Haritanın sol üst köşesindeki arama kutusu, yazdıkça arama yapar ve sonuçları üç başlık altında gruplar:

- **Yerler** – ağaçtaki yerler. Birini seçtiğinizde haritayı o yere kaydırır ve işaretçisini vurgular.
- **Kişiler** – ağaçtaki kişiler. Birini seçtiğinizde haritayı [aşağıda](#bir-kisiyi-harita-uzerinde-takip-etmek) tanımlanan kişi görünümüne geçirir.
- **Dış** – [OpenStreetMap](https://www.openstreetmap.org/) üzerindeki, dünyanın herhangi bir yerindeki konumlar. Birini seçtiğinizde haritayı o konuma kaydırır ve yakınlaştırır; ağaçtaki yerleri filtrelemez veya değiştirmez.

Dış sonuçlar, bir yere koordinat eklerken de faydalıdır: buradan konumu arayarak enlem ve boylamı girmeden önce nerede olduğunu görebilirsiniz.

## Bir kişiyi harita üzerinde takip etmek

Bir kişiyi seçmek – haritanın arama kutusundan veya bir kişinin detay sayfasındaki **Haritada Aç** butonuyla – o kişinin olaylarıyla bağlantılı yerleri, kronolojik sırayla çizgilerle birleştirerek gösterir. Her çizgi boyunca küçük oklar, seyahat yönünü belirtir, böylece bir kişinin yaşamını doğumdan ölüme kadar harita üzerinde takip edebilirsiniz.

Bir yer detay sayfasındaki yerler de **Haritada Aç** butonuna sahiptir; bu buton, haritayı o yerin merkezine açar.

## Zaman kaydırıcı

Sayfanın altındaki zaman kaydırıcı, hangi yer işaretlerinin gösterileceğini, ilişkili olayların yılına göre filtreler:

- Bir yılı seçmek için kaydırıcıyı sürükleyin.
- Seçilen zaman dilimine düşen olaylarla bağlantılı olan yerler gösterilir.
- Bu, atalarınızın tarih boyunca belirli bir noktada nerede yaşadığını takip etmek için kullanılır.

## Harita katmanları

Bir katman anahtarı butonu (yığılmış katmanlar simgesi, sol alt) iki temel harita arasında seçim yapmanıza olanak tanır. Altında, "Sizin haritalarınız" altında kendi harita katmanlarınızı listeler (bkz. [Özel harita örtüleri](#ozel-harita-ortuleri) ve [Yerlerin harita dosyaları](#yerlerin-harita-dosyalari)) ve "Dış" altında [Wikidata binaları](#wikidata-binalari) katmanını, her birini açıp kapatabileceğiniz şekilde gösterir.

Her iki temel haritanın etiketleri, Gramps Web'de seçtiğiniz dilde gösterilir; harita verisinin o dilde bir adı varsa, yerel adıyla birlikte gösterilir.

### Temel Harita

Varsayılan katman, [OpenFreeMap](https://openfreemap.org) tarafından desteklenmektedir (açık mod için Liberty stili, koyu mod için koyu stil). Bu, yerleri bulmak için uygun modern genel amaçlı bir haritadır.

### Tarihsel Harita

Temel haritayı [OpenHistoricalMap](https://www.openhistoricalmap.org) (OHM) ile değiştirir; bu, dünyanın farklı zaman dilimlerinde nasıl göründüğünü haritalayan topluluk destekli bir projedir – bunu OpenStreetMap'in tarihsel bir karşılığı olarak düşünebilirsiniz.

Tarihsel Harita katmanı aktif olduğunda, zaman kaydırıcı aynı zamanda harita karolarını da filtreler: OHM, haritanın seçilen yıldaki görünümünü oluşturur, bu nedenle tarihsel sınırlar, yer adları ve özellikler modern olanların yerine gösterilir. Bu, hem atalarınızın konumunu hem de çağdaş coğrafi ve siyasi bağlamı tek bir görünümde görmenizi sağlar.

!!! not
    OpenHistoricalMap kapsamı bölge ve döneme göre değişir. Katkıların az olduğu alanlar veya dönemler sınırlı tarihsel detay gösterebilir. Eksik veya hatalı tarihsel veriler fark ederseniz, [OpenHistoricalMap'e katkıda bulunmayı](https://www.openhistoricalmap.org) düşünün – bu, herkesin düzenleyebileceği açık bir topluluk projesidir.

## Özel harita örtüleri

Yerleşik temel katmanların yanı sıra, Gramps'te **Medya** nesnesi olarak saklanan herhangi bir taranmış tarihsel harita görüntüsünü, canlı harita üzerinde konumlandırılmış özel bir örtü haline getirebilirsiniz. Bu, eski şehir planları, pariş haritaları veya modern veya tarihsel coğrafya ile doğrudan karşılaştırmak istediğiniz mülk haritalarının taramaları için faydalıdır.

### Bir görüntüyü coğrafi referanslama

1. Taranmış harita görüntüsü için medya nesnesini açın ve düzenleme moduna geçin.
2. "Harita" sekmesini açın ve **Koordinatları Düzenle**'ye tıklayın. Bu, görüntü ile birlikte bir harita içeren bir coğrafi referanslama iletişim kutusu açar.
3. **Haritada bir nokta seçin**'e tıklayın, ardından görüntüdeki bir noktanın karşılık gelmesi gereken haritadaki konuma tıklayın. Bir nokta seçildiğinde, görüntü haritada ilk kez yerleştirilir.
4. Görüntüyü yeniden boyutlandırmak için **Ölçek** kaydırıcısını kullanın ve konumlandırırken temel haritayı görmek için **Saydamlık** kaydırıcısını kullanın.
5. **Görüntüyü Hizala**'ya tıklayın ve görüntüyü, sabitlenen noktanın tam olarak hizalanması için haritada tekrar tıklayın.
6. Görüntü, altındaki coğrafyayı eşleştirene kadar ölçek, saydamlık ve hizalama adımlarını tekrarlayın, ardından kaydedin.

Arka planda, bu, görüntünün köşe koordinatlarını medya nesnesinde bir `map:bounds` niteliğinde saklar.

### Harita sayfasında örtüleri görüntüleme

Bir medya nesnesi bu şekilde coğrafi referanslandığında, otomatik olarak Harita sayfasında açılıp kapatılabilen bir katman olarak kullanılabilir hale gelir. Her örtüyü temel haritadan bağımsız olarak göstermek veya gizlemek için katman anahtarını açın (yığılmış katmanlar simgesi, sol alt). Örtüler, medya nesnesinin başlığı ile listelenir.

## Yerlerin harita dosyaları

Yerler, medya nesneleri olarak harita dosyaları eklenebilir – örneğin bir parişin, bir bölgenin veya bir mülkün sınırları veya bir güzergah. Desteklenen dosya türleri KML (`.kml`), GeoJSON (`.geojson`) ve GPX (`.gpx`) dosyalarıdır.

Haritada bir yeri seçtiğinizde, harita dosyaları haritanın üstünde çizilir ve dosyada varsa renkler kullanılır. Bu, koordinatları olmayan yerler için de çalışır: harita, dosyaların kapsadığı alana yakınlaştırılır. Yer seçili iken, dosyaları "Sizin haritalarınız" altında katman anahtarında listelenir; burada her birini kapatabilirsiniz.

Bir harita dosyasını bir yere eklemek için, onu diğer [medya dosyaları](media.md) gibi yerin galerisine ekleyin.

## Wikidata binaları

"Wikidata binaları" katmanı, [Wikidata](https://www.wikidata.org/) üzerinde kaydedilen binaları gösterir; örneğin kiliseler, çiftlikler veya apartmanlar. Varsayılan olarak kapalıdır ve "Dış" altında katman anahtarında açılabilir. Binalar, harita yeterince yakınlaştırıldığında gösterilir. Zaman kaydırıcı aktif olduğunda, yalnızca seçilen zamanda var olan binalar gösterilir.

Bir binaya tıklayarak, ne zaman inşa edildiği veya yıkıldığı, adresleri, sakinleri ve sahipleri gibi Wikidata'dan detaylarını görebilirsiniz.

### Bir binayı yer olarak kaydetme

Nesne ekleyebilen kullanıcılar, binanın detaylarında **Yeri Kaydet** butonunu görür. Bu, yeni bir yer için formu açar; form, binanın adını kendi dilinizde, bir yer türünü (`Çiftlik` çiftlikler için, aksi takdirde `Bina`), koordinatlarını ve Wikidata öğesine bir bağlantıyı önceden doldurur. Formu tamamlayın, örneğin kapsayıcı yeri seçerek ve kaydedin.

Eğer ağaçtaki bir yer, binanın bulunduğu konumda ise, buton **Kaydedilen yeri aç** olarak değişir ve o yeri gösterir.

!!! bilgi
    Sunucu yöneticisi, `mapWikidata` seçeneği ile Wikidata binaları katmanını [ön uç yapılandırmasından](../install_setup/frontend-config.md) kaldırabilir.
