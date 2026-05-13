# Harita

Harita sayfası, aile ağacınızdaki tüm yerleri coğrafi harita üzerinde etkileşimli işaretçiler olarak gösterir. Yan menüden erişilebilir.

## Yer işaretçileri

Yalnızca Gramps veritabanında GPS koordinatları saklanan yerler haritada gösterilir. Koordinatları olmayan yerler sessizce atlanır. GPS koordinatları, yerin detay sayfasında ayarlanabilir (yeri düzenleyin ve enlem ile boylam alanlarını doldurun).

!!! ipucu
    Haritanızda birçok yer eksikse, bir yer detay sayfasını açın ve enlem ile boylamın ayarlanıp ayarlanmadığını kontrol edin. Koordinatları doğrudan yerin düzenleme görünümünden ekleyebilir veya düzeltebilirsiniz.

Koordinatları olan her yer, bir işaretçi olarak gösterilir. Bir işaretçiye tıkladığınızda, yer adı ve bağlantılı etkinlikler ile kişiler gösteren bir özet kartı açılır. Karttaki yer adına tıklayarak tam yer detay sayfasını açabilirsiniz.

## Arama

Haritanın sol üst köşesindeki arama kutusu, dünya üzerindeki herhangi bir konuma ismiyle atlamanızı sağlar. Bu, ağacın yerlerini filtrelemez – sadece haritayı aranan konuma kaydırır ve yakınlaştırır.

## Zaman kaydırıcı

Sayfanın altındaki zaman kaydırıcı, hangi yer işaretçilerinin gösterileceğini, bunların ilişkili etkinliklerinin yılına göre filtreler:

- Bir yılı seçmek için kaydırıcıyı sürükleyin.
- Seçilen zaman dilimine düşen etkinliklerle bağlantılı yerler gösterilir.
- Bu, atalarınızın belirli bir tarihsel noktada nerede yaşadığını takip etmek için kullanılabilir.

## Harita katmanları

Bir katman değiştirici düğmesi (üst üste katman simgesi, sol alt) iki temel harita arasında seçim yapmanıza olanak tanır:

### Temel Harita

Varsayılan katman, [OpenFreeMap](https://openfreemap.org) tarafından desteklenmektedir (aydınlık mod için Liberty stili, karanlık mod için koyu stil). Bu, yerleri bulmak için uygun modern genel amaçlı bir haritadır.

### Tarihsel Harita

Temel haritayı [OpenHistoricalMap](https://www.openhistoricalmap.org) (OHM) ile değiştirir; bu, dünyanın farklı zaman dilimlerinde nasıl göründüğünü haritalayan topluluk destekli bir projedir – bunu OpenStreetMap'in tarihsel bir karşıtı olarak düşünebilirsiniz.

Tarihsel Harita katmanı aktif olduğunda, zaman kaydırıcı harita karolarını da filtreler: OHM, haritayı seçilen yılda nasıl göründüğü gibi render eder, bu nedenle tarihsel sınırlar, yer adları ve özellikler modern olanların yerine gösterilir. Bu, hem atalarınızın konumunu hem de çağdaş coğrafi ve siyasi bağlamı tek bir görünümde görmenizi sağlar.

!!! not
    OpenHistoricalMap kapsamı bölge ve dönemlere göre değişir. Seyrek katkılara sahip alanlar veya dönemler sınırlı tarihsel detay gösterebilir. Eksik veya hatalı tarihsel veriler fark ederseniz, [OpenHistoricalMap'a katkıda bulunmayı](https://www.openhistoricalmap.org) düşünün – bu, herkesin düzenleyebileceği açık bir topluluk projesidir.
