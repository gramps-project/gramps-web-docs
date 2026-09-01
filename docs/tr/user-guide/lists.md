# Listeler

Gramps Web'deki her nesne türünün bir liste görünümü vardır: İnsanlar, Aileler, Olaylar, Yerler, Kaynaklar, Alıntılar, Depolar, Notlar ve Medya. Hepsi aynı şekilde çalışır ve sıralama, filtreleme ve toplu düzenleme için aynı araçları paylaşır.

## Sıralama ve sayfalama

Bir sütun başlığına tıklayarak o sütuna göre sıralama yapabilirsiniz; tekrar tıklarsanız sıralama tersine döner. Sıralama sunucu tarafından gerçekleştirilir, bu nedenle tüm listeye uygulanır, sadece baktığınız sayfaya değil.

Uzun listeler sayfalara bölünmüştür. Sayfalar arasında geçiş yapmak için alttaki sayfalama kontrollerini kullanın.

Dar ekranlarda tablo otomatik olarak kompakt bir düzene geçer, böylece liste görünümleri telefonda kullanılabilir kalır.

## Sütun Seçimi

Liste üstündeki dişli simgesine tıklayarak **Sütunlar** iletişim kutusunu açın. Bir sütunu göstermek veya gizlemek için işaretleyin veya işaretini kaldırın. **Sıfırla**, o liste için varsayılan seçimi geri yükler.

En az bir sütun görünür kalmalıdır, bu nedenle son kalan sütun işaretini kaldıramazsınız.

Sütun seçiminiz nesne türüne ve aile ağacına göre hatırlanır. Tarayıcınızda saklanır, bu nedenle diğer kullanıcılar tarafından görünmez – ancak farklı bir tarayıcıya veya cihaza geçiş yaptığınızda da takip edilmez.

## Filtreleme

Filtre panelini açmak için **filtre** butonuna tıklayın. Panelin üst kısmındaki bir pill anahtarı iki mod arasında geçiş yapar:

- **basit** – nesne türüne bağlı olarak hazır filtreler seti. Örneğin, insanlar için doğum yılı, ölüm yılı, çeşitli kişi özellikleri, ilişki sayısı, etiketler ve bir nesnenin özel mi yoksa genel mi olduğu gibi filtreleme yapabilirsiniz.
- **GQL** – [Gramps Sorgu Dili](gql.md) için gelişmiş bir sorgu için tek bir metin alanı. Sorguyu yazın ve Enter tuşuna basın veya **Uygula**'ya tıklayın. Sorgu geçersizse, alanın çerçevesi kırmızıya döner.

Aktif filtreler, listenin üzerinde çipler olarak gösterilir. Tek bir filtreyi kaldırmak için çipin temizleme butonuna tıklayın veya hepsini birden kaldırmak için **Tüm filtreleri temizle** seçeneğini kullanın.

!!! not
    İki mod alternatiflerdir, eklemeli değildir: bir GQL sorgusu basit filtreleri değiştirir ve basit moda geri dönmek sorguyu kaldırır.

## Nesneleri Seçme ve Toplu İşlem Yapma

Düzenleme izinlerine sahip kullanıcılar, filtre butonunun yanında bir **Seç** butonu görür. Seçim moduna girmek için tıklayın; bu, her satıra bir onay kutusu ekler.

İstediğiniz nesneleri işaretleyin ve seçilen nesne sayısını gösteren bir araç çubuğu ile birlikte bir **Eylem** açılır menüsü ve bir **Uygula** butonu görünür.

### Sil

Bir veya daha fazla nesneyi seçin, **Sil** seçeneğini belirleyin ve **Uygula**'ya tıklayın. Bir onay iletişim kutusu, işlemi onaylamanızı ister ve işlemin geri alınamayacağı konusunda uyarır.

!!! ipucu
    Silme işlemleri, [revizyon geçmişi](revisions.md) gibi diğer değişiklikler gibi kaydedilir, bu nedenle yanlış bir toplu silme, ilgili işlemi geri alarak tersine çevrilebilir.

### Birleştir

**tam olarak iki** nesne seçin, **Birleştir** seçeneğini belirleyin ve **Uygula**'ya tıklayın. Bir iletişim kutusu, iki nesneden hangisinin birleştirilmiş nesne için birincil verileri sağlaması gerektiğini sorar; birincil olarak tutmak istediğinizi tıklayın. Diğer nesnenin verileri buna birleştirilir ve referanslar güncellenir.

Birleştirme, insanlar, aileler, olaylar, yerler, kaynaklar ve alıntılar için mevcuttur. Depolar, notlar ve medya nesneleri için mevcut değildir.

Geçerli bir seçim olmadan bir eylem seçerseniz – örneğin yalnızca bir nesne seçilmişse birleştirme – bir iletişim kutusu neyin gerekli olduğunu açıklar.
