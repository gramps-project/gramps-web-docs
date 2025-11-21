# DNA eşleşmeleri ile çalışma

DNA eşleşmeleri, iki birey arasında uyum gösteren DNA segmentleridir ve belirli işaretleyicilerin, yani SNP'lerin (tek nükleotid polimorfizmleri için kısaltma, "snips" olarak telaffuz edilir) varlığı ile tanımlanır.

Bu verilere erişmek için, DNA segment eşleşme verilerini görüntülemeye olanak tanıyan bir eşleşme veritabanına yüklenmiş bir DNA testine erişiminiz olmalıdır (örneğin, MyHeritage, Gedmatch, FamilytreeDNA). Gramps Web, yalnızca yüklediğiniz verilere erişim sağladığı için eşleşmeyi kendisi gerçekleştirmez.

## DNA eşleşme verilerini girme

DNA eşleşme verilerini girmek için, verilerin Gramps veritabanında bir not olarak saklandığı için [düzenleme izinlerine](../install_setup/users.md) ihtiyacınız vardır. Ana menüden erişilebilen DNA görünümü, bu verileri doğru formatta girmek için uygun bir yol sunar.

Yeni bir eşleşme girmek için, sağ alttaki + butonuna tıklayın. Açılan pencerede, iki bireyi seçin. "İlk kişi" ve "İkinci kişi"nin farklı şekilde ele alındığını unutmayın: eşleşme, ilk kişiden ikinci kişiye bir ilişki olarak saklanır. DNA eşleşme görünümü ve kromozom tarayıcısı için yalnızca ilk kişi seçilebilir. Genellikle, ilk kişi erişiminiz olan DNA testine sahip olan kişidir ve ikinci kişi daha uzak bir akrabadır.

Eğer ikinci kişi veritabanında yoksa, önce kullanıcı arayüzünün sağ üst köşesindeki "Kişi oluştur" butonunu kullanarak onu oluşturmanız gerekir. Kişiyi oluşturduktan sonra, DNA eşleşme görünümüne geri dönebilir ve yeni oluşturulan kişiyi seçebilirsiniz.

Sonra, ham verileri metin alanına yapıştırın. Veriler, genellikle kromozom numarasını, eşleşmenin başlangıç ve bitiş konumunu, eşleşmedeki SNP sayısını ve eşleşmenin santimorgan (cM) birimindeki uzunluğunu içeren virgül veya sekme ile ayrılmış bir eşleşme tablosu olmalıdır. Ayrıca, eşleşme verileri içeren bir dosyayı metin alanına sürükleyip bırakabilirsiniz.

Böyle bir tablonun minimal bir örneği:

```csv
Kromozom,Başlangıç Konumu,Bitiş Konumu,Santimorgan,SNP'ler
6,6358001,18115715,19.6,7424
7,150135758,154205894,10.9,2816
```

Format geçerliyse, metin alanının altında bir önizleme tablo olarak gösterilir.

Son olarak, eşleşmeyi veritabanında saklamak için "Kaydet" butonuna tıklayın.

## DNA eşleşme verilerini görüntüleme

DNA eşleşme görünümünde, veritabanında ilişkilendirilmiş DNA eşleşmesine sahip her kişiyi seçmenizi sağlayan bir açılır menü bulunmaktadır. Bir kişi seçildiğinde, DNA eşleşme verileri açılır menünün altında bir tabloda gösterilir. Bu tablo, eşleşmenin ilişkili olduğu kişinin adını, açılır menüde seçilen kişiyle olan ilişkisini (Gramps veritabanından otomatik olarak belirlenir), paylaşılan DNA'nın toplam uzunluğunu santimorgan (cM) cinsinden, paylaşılan segment sayısını ve bu segmentlerin en büyüğünün uzunluğunu gösterir.

Bireysel bir eşleşmeye tıkladığınızda, tüm segmentleri ve eşleşmenin anne veya baba tarafında olup olmadığını gösteren bir detay sayfası açılır. Bu bilgi, ham verilerde `Side` adlı bir sütunda babasal için `P` veya annesel için `M` belirterek manuel olarak girilebilir veya Gramps tarafından en son ortak ataya dayanarak otomatik olarak belirlenebilir.

## Eşleşmeyi düzenleme

Eşleşmeyi, eşleşme detay görünümündeki sağ alttaki kalem butonuna tıklayarak düzenleyebilirsiniz. Bu, yeni bir eşleşme oluştururken açılan benzer bir diyalog penceresini açar, ancak veriler önceden doldurulmuştur. Ham verileri değiştirebileceğinizi, ancak eşleşmeyle ilişkili bireyleri değiştiremeyeceğinizi unutmayın - bireyleri değiştirmek istiyorsanız eşleşmeyi silip yeni bir tane oluşturmanız gerekir.

## Gramps Masaüstünde eşleşme verileri ile çalışma

DNA eşleşme verileri, Gramps veritabanında bir not olarak saklanır. Format, Gramps Masaüstü için mevcut olan 
[DNA Segment Haritası Eklentisi](https://gramps-project.org/wiki/index.php/Addon:DNASegmentMapGramplet) ile uyumludur. Wiki sayfası, verileri nasıl elde edeceğiniz, nasıl yorumlayacağınız ve verileri Gramps'a nasıl gireceğiniz hakkında daha fazla ayrıntı içermektedir.

!!! info
    Gramps Web API v2.8.0, daha geniş bir ham DNA eşleşme verisi yelpazesini kabul etmek için bazı değişiklikler getirmiştir, bu henüz Gramps Masaüstü Eklentisi'nde mevcut değildir. Gramps Masaüstü Eklentisi, gelecekte aynı formatları desteklemek için güncellenecektir.
