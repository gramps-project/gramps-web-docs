# Harita

Harita sayfası, aile ağacınızdaki tüm yerleri coğrafi harita üzerinde etkileşimli işaretçiler olarak gösterir. Yan menüden erişilebilir.

## Yer işaretçileri

Harita üzerinde yalnızca Gramps veritabanında GPS koordinatları saklanan yerler gösterilir. Koordinatları olmayan yerler sessizce atlanır. GPS koordinatları, yerin detay sayfasında ayarlanabilir (yeri düzenleyin ve enlem ile boylam alanlarını doldurun).

!!! ipucu
    Eğer haritanızda birçok yer eksikse, bir yer detay sayfasını açın ve enlem ile boylamın ayarlanıp ayarlanmadığını kontrol edin. Koordinatları doğrudan yerin düzenleme görünümünden ekleyebilir veya düzeltebilirsiniz.

Koordinatları olan her yer bir işaretçi olarak gösterilir. Bir işaretçiye tıkladığınızda, yerin adını ve bağlantılı etkinlikler ile kişileri gösteren bir özet kartı açılır. Karttaki yer adına tıklayarak tam yer detay sayfasını açabilirsiniz.

## Arama

Haritanın sol üst köşesindeki arama kutusu, dünya üzerindeki herhangi bir konuma ismiyle atlamanızı sağlar. Bu, ağacın yerlerini filtrelemez – sadece haritayı aranan konuma kaydırır ve yakınlaştırır.

## Zaman kaydırıcı

Sayfanın altındaki zaman kaydırıcı, hangi yer işaretçilerinin gösterileceğini, bunların ilişkili etkinliklerinin yılına göre filtreler:

- Bir yılı seçmek için kaydırıcıyı sürükleyin.
- Seçilen zaman dilimine düşen etkinliklerle bağlantılı yerler gösterilir.
- Bunu, atalarınızın tarih boyunca belirli bir noktada nerede yaşadığını izlemek için kullanın.

## Harita katmanları

Bir katman değiştirici düğmesi (üst üste katmanlar simgesi, sol alt) iki temel harita arasında seçim yapmanızı sağlar:

### Temel Harita

Varsayılan katman, [OpenFreeMap](https://openfreemap.org) tarafından desteklenmektedir (açık mod için Liberty stili, koyu mod için koyu stil). Bu, yerleri bulmak için uygun modern genel amaçlı bir haritadır.

### Tarihsel Harita

Temel haritayı [OpenHistoricalMap](https://www.openhistoricalmap.org) (OHM) ile değiştirir; bu, dünyanın farklı zaman dilimlerinde nasıl göründüğünü haritalayan topluluk destekli bir projedir – bunu OpenStreetMap'in tarihsel bir karşılığı olarak düşünebilirsiniz.

Tarihsel Harita katmanı aktif olduğunda, zaman kaydırıcı aynı zamanda harita karolarını da filtreler: OHM, haritayı seçilen yılda nasıl göründüğüne göre render eder, bu nedenle tarihsel sınırlar, yer isimleri ve özellikler modern olanların yerine gösterilir. Bu, atalarınızın konumunu ve çağdaş coğrafi ve siyasi bağlamı tek bir görünümde görmenizi sağlar.

!!! not
    OpenHistoricalMap kapsamı bölgeye ve döneme göre değişir. Seyrek katkılara sahip alanlar veya dönemler sınırlı tarihsel detaylar gösterebilir. Eksik veya hatalı tarihsel veriler fark ederseniz, [OpenHistoricalMap'e katkıda bulunmayı](https://www.openhistoricalmap.org) düşünün – bu, herkesin düzenleyebileceği açık bir topluluk projesidir.

## Özel harita örtüleri

Yerleşik temel katmanların yanı sıra, Gramps'ta **Medya** nesnesi olarak saklanan herhangi bir taranmış tarihsel harita görüntüsünü canlı harita üzerinde konumlandırılmış özel bir örtü haline getirebilirsiniz. Bu, eski şehir planları, pariş haritaları veya modern veya tarihsel coğrafya ile doğrudan karşılaştırmak istediğiniz mülk haritalarının taramaları için yararlıdır.

### Bir görüntüyü coğrafi referanslama

1. Taranmış harita görüntüsü için medya nesnesini açın ve düzenleme moduna geçin.
2. "Harita" sekmesini açın ve **Koordinatları Düzenle**'ye tıklayın. Bu, görüntü ile birlikte bir harita içeren bir coğrafi referanslama iletişim kutusu açar.
3. **Harita üzerinde bir nokta seçin**'e tıklayın, ardından görüntüdeki bir noktanın karşılık gelmesi gereken harita üzerindeki konuma tıklayın. Bir nokta seçildiği anda görüntü harita üzerinde ilk kez yerleştirilir.
4. Görüntüyü yeniden boyutlandırmak için **Ölçek** kaydırıcısını ve konumlandırma sırasında temel haritayı görmenizi sağlamak için **Şeffaflık** kaydırıcısını kullanın.
5. **Görüntüyü Hizala**'ya tıklayın ve görüntüyü tam olarak hizalamak için harita üzerinde tekrar tıklayın.
6. Görüntü, alttaki coğrafya ile eşleşene kadar ölçek, şeffaflık ve hizalama adımlarını tekrarlayın, ardından kaydedin.

Arka planda, bu, görüntünün köşe koordinatlarını medya nesnesinde bir `map:bounds` niteliğinde saklar.

### Harita sayfasında örtüleri görüntüleme

Bir medya nesnesi bu şekilde coğrafi referanslandığında, otomatik olarak Harita sayfasında açılıp kapatılabilen bir katman olarak kullanılabilir hale gelir. Temel haritadan bağımsız olarak her örtüyü göstermek veya gizlemek için katman değiştiriciyi (üst üste katmanlar simgesi, sol alt) açın. Örtüler, medya nesnesinin başlığına göre listelenir.
