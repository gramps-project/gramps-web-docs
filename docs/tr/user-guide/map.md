# Harita

Harita sayfası, aile ağacınızdaki tüm yerleri coğrafi harita üzerinde etkileşimli işaretçiler olarak gösterir. Kenar çubuğundan erişilebilir.

## Yer işaretçileri

Sadece Gramps veritabanında GPS koordinatları saklanan yerler haritada gösterilir. Koordinatları olmayan yerler sessizce atlanır. GPS koordinatları, yer detay sayfasında ayarlanabilir (yeri düzenleyin ve enlem ile boylam alanlarını doldurun).

!!! ipucu
    Haritanızda birçok yer eksikse, bir yer detay sayfasını açın ve enlem ile boylamın ayarlanıp ayarlanmadığını kontrol edin. Koordinatları, yerin düzenleme görünümünden doğrudan ekleyebilir veya düzeltebilirsiniz.

Koordinatları olan her yer bir işaretçi olarak gösterilir. Bir işaretçiye tıkladığınızda, yerin adını ve bağlantılı olayları ile kişileri gösteren bir özet kartı açılır. Karttaki yer adına tıklayarak tam yer detay sayfasını açabilirsiniz.

## Arama

Haritanın sol üst köşesindeki arama kutusu, yazdıkça arama yapar ve sonuçları üç başlık altında gruplar:

- **Yerler** – aile ağacınızdaki yerler. Birini seçmek, haritayı o yere kaydırır ve işaretçisini vurgular.
- **Kişiler** – aile ağacınızdaki kişiler. Birini seçmek, haritayı [aşağıda](#bir-kisinin-harita-üzerinde-takibi) açıklanan kişi görünümüne geçirir.
- **Dış** – [OpenStreetMap](https://www.openstreetmap.org/) üzerindeki dünya genelindeki konumlar. Birini seçmek, haritayı o konuma kaydırır ve yakınlaştırır; ağaçtaki yerleri filtrelemez veya değiştirmez.

Dış sonuçlar, bir yere koordinat eklerken de faydalıdır: buradan konumu kontrol edebilir ve enlem ile boylamı girmeden önce nerede olduğunu görebilirsiniz.

## Bir kişiyi harita üzerinde takip etme

Bir kişiyi seçmek – haritanın arama kutusundan veya bir kişinin detay sayfasındaki **Haritada Aç** butonuyla – o kişinin olaylarıyla bağlantılı yerleri gösterir – ailelerinin olayları, örneğin evlilikler gibi – kronolojik sırayla çizgilerle birleştirilmiştir. Her çizgi boyunca küçük oklar, seyahat yönünü gösterir, böylece bir kişinin yaşamını doğumundan ölümüne kadar harita üzerinde takip edebilirsiniz.

Bir yer detay sayfasındaki yerler de **Haritada Aç** butonuna sahiptir ve bu buton, haritayı o yerin merkezine alır.

## Zaman kaydırıcı

Sayfanın altındaki zaman kaydırıcı, hangi yer işaretçilerinin gösterileceğini, ilişkili olayların yılına göre filtreler:

- Bir yılı seçmek için kaydırıcıyı sürükleyin.
- Sadece seçilen zaman diliminde yer alan olaylarla bağlantılı yerler gösterilir.
- Bu, atalarınızın tarih boyunca belirli bir noktada nerede yaşadığını takip etmek için kullanılabilir.

## Harita katmanları

Bir katman değiştirici butonu (yığılmış katmanlar simgesi, sol alt) iki temel harita arasında seçim yapmanıza olanak tanır. Altında, "Kendi haritalarınız" altında kendi harita katmanlarınızı listeler (bkz. [Özel harita örtüleri](#özel-harita-örtüleri) ve [Yerlerin harita dosyaları](#yerlerin-harita-dosyaları)) ve "Dış" altında [Wikidata binaları](#wikidata-binaları) katmanını, her birini açıp kapatabileceğiniz şekilde gösterir.

Her iki temel haritanın etiketleri, Gramps Web'de seçtiğiniz dilde gösterilir; harita verisinin o dilde bir adı varsa, aksi takdirde yerel adı gösterilir.

### Temel Harita

Varsayılan katman, [OpenFreeMap](https://openfreemap.org) tarafından desteklenmektedir (açık mod için Liberty tarzı, koyu mod için koyu tarz). Bu, yerleri bulmak için uygun modern genel amaçlı bir haritadır.

### Tarihsel Harita

Temel haritayı [OpenHistoricalMap](https://www.openhistoricalmap.org) (OHM) ile değiştirir; bu, dünyanın farklı zaman dilimlerinde nasıl göründüğünü haritalayan topluluk destekli bir projedir – bunu OpenStreetMap'in tarihsel bir karşıtı olarak düşünebilirsiniz.

Tarihsel Harita katmanı aktif olduğunda, zaman kaydırıcı aynı zamanda harita karolarını da filtreler: OHM, haritanın seçilen yılda nasıl göründüğünü render eder, bu nedenle tarihsel sınırlar, yer adları ve özellikler modern olanların yerine gösterilir. Bu, hem atalarınızın konumunu hem de çağdaş coğrafi ve siyasi bağlamı tek bir görünümde görmenizi sağlar.

!!! not
    OpenHistoricalMap kapsamı bölge ve döneme göre değişir. Seyrek katkılara sahip alanlar veya dönemler sınırlı tarihsel detay gösterebilir. Eksik veya yanlış tarihsel veriler fark ederseniz, [OpenHistoricalMap'e katkıda bulunmayı](https://www.openhistoricalmap.org) düşünün – herkesin düzenleyebileceği açık bir topluluk projesidir.

## Özel harita örtüleri

Yerleşik temel katmanların yanı sıra, Gramps'ta **Medya** nesnesi olarak saklanan herhangi bir taranmış tarihsel harita görüntüsünü, canlı harita üzerinde konumlandırılmış özel bir örtü haline getirebilirsiniz. Bu, eski şehir planları, pariş haritaları veya modern veya tarihsel coğrafya ile doğrudan karşılaştırmak istediğiniz mülk haritaları için faydalıdır.

### Bir görüntüyü coğrafi referanslama

1. Taranmış harita görüntüsü için medya nesnesini açın ve düzenleme moduna geçin.
2. "Harita" sekmesini açın ve **Koordinatları Düzenle**'ye tıklayın. Bu, bir harita ile birlikte görüntüyü içeren bir coğrafi referanslama iletişim kutusu açar.
3. **Haritada bir nokta seçin**'e tıklayın, ardından görüntüdeki bir noktanın karşılık gelmesi gereken haritadaki konuma tıklayın. Bir nokta seçildiği anda görüntü haritada ilk kez yerleştirilir.
4. Görüntüyü yeniden boyutlandırmak için **Ölçek** kaydırıcısını ve konumlandırma sırasında temel haritayı görmeniz için **Opaklık** kaydırıcısını kullanın.
5. **Görüntüyü Hizala**'ya tıklayın ve görüntüyü tam olarak hizalamak için haritada tekrar tıklayın.
6. Görüntü, altındaki coğrafya ile eşleşene kadar ölçek, opaklık ve hizalama adımlarını tekrarlayın, ardından kaydedin.

Arka planda, bu, görüntünün köşe koordinatlarını medya nesnesindeki `map:bounds` niteliğinde saklar.

### Harita sayfasında örtüleri görüntüleme

Bir medya nesnesi bu şekilde coğrafi referanslandığında, otomatik olarak Harita sayfasında açılıp kapatılabilir bir katman olarak kullanılabilir hale gelir. Katman değiştiriciyi açın (yığılmış katmanlar simgesi, sol alt) ve her örtüyü temel haritadan bağımsız olarak gösterip gizleyin. Örtüler, medya nesnesinin başlığına göre listelenir.

Her örtünün adının altında bir opaklık kaydırıcısı vardır, böylece temel haritayı onun üzerinden görebilirsiniz.

## Yerlerin harita dosyaları

Yerler, medya nesneleri olarak harita dosyaları eklenebilir – örneğin bir parişin, bir bölgenin veya bir mülkün sınırları veya bir rota. Desteklenen dosya türleri KML (`.kml`), GeoJSON (`.geojson`) ve GPX (`.gpx`) dosyalarıdır.

Haritada bir yeri seçtiğinizde, harita dosyaları haritanın üstünde çizilir ve dosyada varsa renkler kullanılır. Bu, koordinatları olmayan yerler için de çalışır: harita, dosyaların kapsadığı alana yakınlaştırılır. Yer seçili olduğu sürece, dosyaları "Kendi haritalarınız" altında katman değiştiricide listelenir ve her birini kapatabilirsiniz.

Bir yerin harita dosyasını eklemek için, onu diğer [medya dosyaları](media.md) gibi yerin galerisine ekleyin.

## Wikidata binaları

"Wikidata binaları" katmanı, [Wikidata](https://www.wikidata.org/) üzerinde kaydedilen binaları gösterir; örneğin kiliseler, çiftlikler veya şehir evleri. Varsayılan olarak kapalıdır ve "Dış" altında katman değiştiricide açılabilir. Binalar, harita yeterince yakınlaştırıldığında gösterilir. Zaman kaydırıcı aktif olduğunda, yalnızca seçilen zamanda var olan binalar gösterilir.

Bir binaya tıklayarak, Wikidata'dan ne zaman inşa edildiği veya yıkıldığı, adresleri, sakinleri ve sahipleri gibi detaylarını görebilirsiniz.

### Bir binayı yer olarak kaydetme

Nesne ekleyebilen kullanıcılar, binanın detaylarında **Yeri kaydet** butonunu görür. Bu, yeni bir yer için formu açar; bina adını kendi dilinizde, bir yer türünü (`Çiftlik` çiftlikler için, aksi takdirde `Bina`), koordinatlarını ve Wikidata öğesine bir bağlantıyı önceden doldurur. Formu tamamlayın, örneğin kapsayıcı yeri seçerek ve kaydedin.

Eğer ağaçınızdaki bir yer, binanın bulunduğu aynı konumdaysa, buton **Kaydedilen yeri aç** olarak değişir ve o yeri gösterir.

!!! bilgi
    Sunucu yöneticisi, `mapWikidata` seçeneği ile [ön uç yapılandırması](../install_setup/frontend-config.md) aracılığıyla Wikidata binaları katmanını kaldırabilir.
