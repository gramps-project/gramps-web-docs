# Harita

Harita sayfası, ağaçtaki tüm yerleri etkileşimli işaretçiler olarak coğrafi bir haritada görüntüler. Kenar çubuğundan erişilebilir.

## Yer işaretçileri

Haritada yalnızca Gramps veritabanında GPS koordinatları saklanan yerler gösterilir. Koordinatları olmayan yerler sessizce atlanır. GPS koordinatları, yerin detay sayfasında ayarlanabilir (yeri düzenleyin ve enlem ve boylam alanlarını doldurun).

!!! ipucu
    Haritanızda birçok yer eksikse, bir yer detay sayfasını açın ve enlem ve boylamın ayarlanıp ayarlanmadığını kontrol edin. Koordinatları doğrudan yerin düzenleme görünümünden ekleyebilir veya düzeltebilirsiniz.

Koordinatları olan her yer, bir işaretçi olarak gösterilir. Bir işaretçiye tıkladığınızda, yer adı ve bağlantılı etkinlikler ile kişiler hakkında bir özet kartı açılır. Karttaki yer adına tıklayarak tam yer detay sayfasını açabilirsiniz.

## Arama

Haritanın sol üst köşesindeki arama kutusu, yazdıkça arama yapar ve sonuçları üç başlık altında gruplar:

- **Yerler** – ağaçtaki yerler. Birini seçmek haritayı ona kaydırır ve işaretçisini vurgular.
- **Kişiler** – ağaçtaki kişiler. Birini seçmek, haritayı [aşağıda](#bir-kisiyi-harita-uzerinde-takip-etmek) açıklanan kişi görünümüne geçirir.
- **Dış** – [OpenStreetMap](https://www.openstreetmap.org/) üzerindeki dünya genelindeki konumlar. Birini seçmek, haritayı o konuma kaydırır ve yakınlaştırır; ağaçtaki yerlerin filtrelenmesini veya değiştirilmesini sağlamaz.

Dış sonuçlar, bir yere koordinat eklerken de faydalıdır: burada konumu arayarak enlem ve boylamını girmeden önce nerede olduğunu görebilirsiniz.

## Bir kişiyi harita üzerinde takip etmek

Bir kişiyi seçmek – haritanın arama kutusundan veya bir kişinin detay sayfasındaki **Haritada Aç** düğmesi ile – o kişinin etkinliklerine bağlı yerleri gösterir, bunlar kronolojik sırayla çizgilerle bağlanmıştır. Her çizgi boyunca küçük oklar, seyahat yönünü gösterir, böylece bir kişinin yaşamını doğumdan ölüme kadar harita üzerinde takip edebilirsiniz.

Bir yer detay sayfasındaki yerler de **Haritada Aç** düğmesine sahiptir; bu, haritayı o yerin merkezine alır.

## Zaman kaydırıcı

Sayfanın altındaki zaman kaydırıcı, hangi yer işaretçilerinin gösterileceğini, bunların ilişkili etkinliklerinin yılına göre filtreler:

- Bir yılı seçmek için kaydırıcıyı sürükleyin.
- Seçilen zaman dilimine düşen etkinliklerle bağlantılı yerler gösterilir.
- Bunu, atalarınızın tarihin belirli bir noktasında nerede yaşadığını izlemek için kullanın.

## Harita katmanları

Bir katman anahtarı düğmesi (üst üste katman simgesi, sol alt) iki temel harita arasında seçim yapmanıza olanak tanır:

### Temel Harita

Varsayılan katman, [OpenFreeMap](https://openfreemap.org) tarafından desteklenmektedir (açık mod için Liberty stili, karanlık mod için karanlık stil). Bu, yerleri bulmak için uygun modern genel amaçlı bir haritadır.

### Tarihsel Harita

Temel haritayı [OpenHistoricalMap](https://www.openhistoricalmap.org) (OHM) ile değiştirir, bu da dünyanın farklı zaman dilimlerinde nasıl göründüğünü haritalayan topluluk destekli bir projedir – bunu OpenStreetMap'in tarihsel bir karşılığı olarak düşünebilirsiniz.

Tarihsel Harita katmanı aktif olduğunda, zaman kaydırıcısı aynı zamanda harita karolarını da filtreler: OHM, haritayı seçilen yılda nasıl göründüğüne göre işler, böylece tarihsel sınırlar, yer adları ve özellikler modern olanların yerine gösterilir. Bu, hem atalarınızın konumunu hem de çağdaş coğrafi ve siyasi bağlamı tek bir görünümde görmenizi sağlar.

!!! not
    OpenHistoricalMap kapsamı bölge ve döneme göre değişir. Seyrek katkılara sahip alanlar veya dönemler sınırlı tarihsel detaylar gösterebilir. Eksik veya hatalı tarihsel veriler fark ederseniz, [OpenHistoricalMap'e katkıda bulunmayı](https://www.openhistoricalmap.org) düşünün – bu, herkesin düzenleyebileceği açık bir topluluk projesidir.

## Özel harita örtüleri

Yerleşik temel katmanların yanı sıra, Gramps'ta **Medya** nesnesi olarak saklanan herhangi bir taranmış tarihsel harita görüntüsünü canlı harita üzerinde konumlandırılmış özel bir örtü haline getirebilirsiniz. Bu, eski şehir planları, pariş haritaları veya modern veya tarihsel coğrafya ile doğrudan karşılaştırmak istediğiniz mülk haritaları için faydalıdır.

### Bir görüntüyü coğrafi referanslama

1. Taranmış harita görüntüsü için medya nesnesini açın ve düzenleme moduna geçin.
2. "Harita" sekmesini açın ve **Koordinatları Düzenle**'ye tıklayın. Bu, görüntü ile birlikte bir harita içeren bir coğrafi referanslama iletişim kutusu açar.
3. **Haritada bir nokta seçin**'e tıklayın, ardından görüntüdeki bir noktanın karşılık gelmesi gereken haritadaki konuma tıklayın. Bir nokta seçildiğinde, görüntü haritada ilk kez yerleştirilir.
4. Görüntüyü yeniden boyutlandırmak için **Ölçek** kaydırıcısını ve konumlandırma sırasında temel haritayı görmenizi sağlamak için **Saydamlık** kaydırıcısını kullanın.
5. **Görüntüyü Hizala**'ya tıklayın ve görüntüyü sabit noktanın tam olarak hizalanması için haritada tekrar tıklayarak kaydırın.
6. Görüntü, altındaki coğrafya ile eşleşene kadar ölçek, saydamlık ve hizalama adımlarını tekrarlayın, ardından kaydedin.

Arka planda, bu görüntünün köşe koordinatları medya nesnesinde bir `map:bounds` niteliğinde saklanır.

### Harita sayfasında örtüleri görüntüleme

Bir medya nesnesi bu şekilde coğrafi referanslandığında, otomatik olarak Harita sayfasında açılır kapanır bir katman olarak kullanılabilir hale gelir. Katman anahtarını açın (üst üste katman simgesi, sol alt) ve her örtüyü temel haritadan bağımsız olarak gösterin veya gizleyin. Örtüler, medya nesnesinin başlığına göre listelenir.
