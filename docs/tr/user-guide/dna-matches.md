# DNA eşleşmeleri ile çalışma

DNA eşleşmeleri, iki birey arasında uyumlu olan DNA segmentleridir ve bu segmentler, SNP'ler (tek nükleotid polimorfizmleri, "snips" olarak telaffuz edilir) olarak adlandırılan işaretlerin varlığı ile tanımlanır.

Bu verileri elde etmek için, DNA segment eşleşme verilerini görüntülemeye olanak tanıyan bir eşleştirme veritabanına yüklenmiş bir DNA testine erişiminiz olmalıdır (örneğin, MyHeritage, Gedmatch, FamilytreeDNA). Gramps Web, yalnızca yüklediğiniz verilere erişimi olduğundan, eşleştirmeyi kendisi gerçekleştirmez.

## DNA eşleşme verilerini girme

DNA eşleşme verilerini girmek için, veriler Gramps veritabanında bir not olarak saklandığı için [düzenleme izinlerine](../install_setup/users.md) ihtiyacınız var. Ana menüden erişilebilen DNA görünümü, bu verileri doğru formatta girmek için uygun bir yol sağlar.

Yeni bir eşleşme girmek için, sağ alttaki + butonuna tıklayın. Açılan pencerede, iki bireyi seçin. "İlk kişi" ve "İkinci kişi" farklı şekilde ele alınır: eşleşme, ilk kişiden ikinci kişiye bir ilişki olarak saklanır. DNA eşleşme görünümü ve kromozom tarayıcısı için yalnızca ilk kişi seçilebilir. Genellikle, ilk kişi, erişiminiz olan DNA testine sahip olan kişidir ve ikinci kişi daha uzak bir akrabadır.

Eğer ikinci kişi veritabanında yoksa, kullanıcı arayüzünün sağ üst köşesindeki "Kişi oluştur" butonunu kullanarak önce onu oluşturmanız gerekir. Kişiyi oluşturduktan sonra, DNA eşleşme görünümüne geri dönebilir ve yeni oluşturulan kişiyi seçebilirsiniz.

Sonra, ham veriyi metin alanına yapıştırın. Veri, genellikle kromozom numarasını, eşleşmenin başlangıç ve bitiş konumunu, eşleşmedeki SNP sayısını ve eşleşmenin santimorgan (cM) birimindeki uzunluğunu içeren virgül veya sekme ile ayrılmış bir tablo olmalıdır. Ayrıca, eşleşme verileri içeren bir dosyayı metin alanına sürükleyip bırakabilirsiniz.

Böyle bir tablonun minimal bir örneği:

```csv
Kromozom,Başlangıç Konumu,Bitiş Konumu,Santimorgan,SNP'ler
6,6358001,18115715,19.6,7424
7,150135758,154205894,10.9,2816
```

Eğer format geçerliyse, metin alanının altında bir tablo olarak bir önizleme gösterilir.

Son olarak, eşleşmeyi veritabanında saklamak için "Kaydet" butonuna tıklayın.

## DNA eşleşme verilerini görüntüleme

DNA eşleşme görünümünde, veritabanında ilişkili bir DNA eşleşmesine sahip her kişiyi seçmeye olanak tanıyan bir açılır menü bulunmaktadır. Bir kişi seçildiğinde, eşleşmeleri bir tabloda listelenir: eşleşmenin adı, seçilen kişiyle olan ilişkisi, paylaşılan DNA'nın toplam uzunluğu (cM cinsinden), paylaşılan segment sayısı ve bu segmentlerden en büyüğünün uzunluğu.

Ağaçta zaten yer alan eşleşmeler için, ilişki sütunu ağaçta kaydedilen ilişkiyi gösterir (Gramps veritabanından otomatik olarak belirlenmiştir). Ağaçta seçilen kişiyle ilişkisi olmayan eşleşmeler için, paylaşılan DNA'dan tahmin edilen ilişkiyi gösterir ve "≈" ile işaretlenir.

Bir eşleşmeye tıkladığınızda, paylaşılan DNA'nın bir özeti, [ilişki tahmini](#relationship-estimate), ağaçtaki ilişkiyi gösteren bir grafik ve segmentler listesi ile birlikte sayfası açılır. Her segment, babasal mı yoksa annesel mi olduğunu gösterir. Taraf, ya manuel olarak (ham veride `Taraf` adlı bir sütunda babasal için `P` veya annesel için `M` vererek) ya da en son ortak atadan otomatik olarak belirlenebilir. Segmentlerin yanındaki indirme butonu, onları eşleşme penceresinin kabul ettiği formatta bir CSV dosyası olarak kaydeder.

## İlişki tahmini

Paylaşılan DNA, belirli bir ilişkinin kanıtı değildir: İki akrabanın paylaştığı DNA miktarı çok değişkenlik gösterir ve farklı ilişkiler örtüşebilir. Bu nedenle Gramps Web, paylaşılan segmentlerin sayısı ve uzunluklarından hesaplanan olasılıkları ile birlikte olası ilişkilerin bir aralığını gösterir (Gramps Web API 3.26 veya daha yenisi gereklidir).

İlişkiler, *derece*lerine göre gruplandırılır:

- **Ebeveyn veya çocuk** ve **Tam kardeş** kendi başlarına gösterilir.
- **Derece 2 akraba**, üvey kardeşler, büyük ebeveynler ve torunlar ile teyzeler, amcalar, yeğenler ve yeğenleri içerir.
- **Derece 3 akraba**, birinci kuzenler, büyük ebeveynler, büyük teyzeler ve büyük amcalar ile üvey teyzeler ve amcaları içerir.
- Her bir sonraki derece, bir nesil daha uzakta olup, örneğin, bir kez çıkarılmış birinci kuzenler derece 4 ve ikinci kuzenler derece 5'tir. Derece 9 ve üzeri "9+" olarak gruplandırılır.

Aynı derecedeki ilişkiler ortalama olarak benzer miktarda DNA paylaşır, bu nedenle DNA tek başına onları ayırt edemez. Aralarındaki farkı belirlemek için kişilerin yaşlarını kullanın – 60 yaşındaki birinin derece 2 akrabası olan 30 yaşındaki bir akraba, daha çok yeğen olma olasılığı taşır.

Tahmin, yakın akrabalar için en güvenilirdir. Uzak ilişkilerde, eşleşmeler yalnızca birkaç segment paylaşır ve olasılıklar birkaç dereceye yayılır.

### DNA ile ağacı kontrol etme

Eşleşme ağaçta yer alıyorsa, Gramps Web, paylaşılan DNA'nın orada kaydedilen ilişkiye uyup uymadığını kontrol eder. Eğer DNA, o ilişki için çok olası değilse, eşleşmeler tablosunda bir uyarı simgesi ve eşleşme sayfasında bir uyarı gösterilir. Parantez içindeki sayı, örneğin "1 : 500", DNA'nın kaydedilen ilişki için ne kadar olası olduğunu, en olası ilişki için ne kadar olası olduğu ile karşılaştırır.

Bir uyarı, daha dikkatli bakmak için bir sebeptir, hata kanıtı değildir. Yaygın nedenler şunlardır:

- Ağaçta bir hata, örneğin yanlış bir ebeveyn,
- Yanlış atfedilmiş ebeveynlik, örneğin bilinmeyen bir evlat edinme veya farklı bir biyolojik baba,
- Tamamlanmamış eşleşme verileri, örneğin yalnızca yüksek bir eşik üzerindeki segmentlerin test hizmetinden kopyalanması durumunda,
- Birden fazla hat üzerinden ilişkiler, örneğin hem annesi hem de babası aracılığıyla akraba olan kişiler ("soy ağacı çökmesi"), beklenenden daha fazla DNA paylaşır.

Doğumla olmayan ilişkiler, örneğin bir evlat edinme yoluyla olanlar, kontrol edilmez.

## Eşleşmeyi düzenleme

Bir eşleşmeyi düzenlemek için, sayfasını açın ve düzenleme butonuna tıklayın veya `e` tuşuna basın. Ham verileri değiştirebileceğinizi, ancak eşleşmeyle ilişkili bireyleri değiştiremeyeceğinizi unutmayın – bireyleri değiştirmek istiyorsanız, eşleşmeyi silip yeni bir tane oluşturmanız gerekir.

## Özel eşleşmeler

Eşleşme ekleme ve düzenleme diyaloglarında bir **Özel** anahtarı bulunmaktadır. Özel bir eşleşme, segmentleri de dahil olmak üzere, özel kayıtları görüntüleyemeyen kullanıcılardan gizlidir. Özel eşleşmeler, diğer herkes için bir kilit ile işaretlenir. Gizlilik hakkında daha fazla bilgi için [Özel kayıtlar](privacy.md) sayfasına bakın.

## Gramps Masaüstünde eşleşme verileri ile çalışma

DNA eşleşme verileri, Gramps veritabanında bir not olarak saklanır. Format, 
[DNA Segment Haritası Eklentisi](https://gramps-project.org/wiki/index.php/Addon:DNASegmentMapGramplet)
Gramps Masaüstü için mevcut olan ile uyumludur. Wiki sayfası, verileri nasıl elde edeceğiniz, nasıl yorumlayacağınız ve verileri Gramps'a nasıl gireceğiniz hakkında daha fazla ayrıntı içerir.

!!! info
    Gramps Web API v2.8.0, daha geniş bir ham DNA eşleşme verisi yelpazesini kabul etmek için bazı değişiklikler getirmiştir; bu, henüz Gramps Masaüstü Eklentisi'nde mevcut değildir. Gramps Masaüstü Eklentisi, gelecekte aynı formatları destekleyecek şekilde güncellenecektir.
