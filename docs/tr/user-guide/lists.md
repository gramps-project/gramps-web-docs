# Listeler

Gramps Web'deki her nesne türünün bir liste görünümü vardır: İnsanlar, Aileler, Etkinlikler, Yerler, Kaynaklar, Alıntılar, Depolar, Notlar ve Medya. Hepsi aynı şekilde çalışır ve sıralama, filtreleme ve toplu düzenleme için aynı araçları paylaşır.

## Sıralama ve sayfalama

Bir sütun başlığına tıklayarak o sütuna göre sıralama yapabilirsiniz; tekrar tıklarsanız sıralama tersine döner. Sıralama sunucu tarafından gerçekleştirilir, bu nedenle tüm listeye uygulanır, yalnızca baktığınız sayfaya değil.

Uzun listeler sayfalara bölünmüştür. Sayfalar arasında geçiş yapmak için alttaki sayfalama kontrolünü kullanın.

Dar ekranlarda tablo otomatik olarak kompakt bir düzene geçer, böylece liste görünümleri telefonda kullanılabilir kalır.

## Sütunları Seçme

Liste üzerindeki dişli simgesine tıklayarak **Sütunlar** iletişim kutusunu açın. Bir sütunu göstermek veya gizlemek için işaretleyin veya işaretini kaldırın. **Sıfırla**, o liste için varsayılan seçimi geri yükler.

En az bir sütun görünür kalmalıdır, bu nedenle son kalan sütun işaretini kaldıramazsınız.

Sütun seçiminiz nesne türüne ve aile ağacına göre hatırlanır. Tarayıcınızda saklanır, bu nedenle diğer kullanıcılar tarafından görünmez – ancak farklı bir tarayıcıya veya cihaza geçiş yaptığınızda da sizi takip etmez.

## Filtreleme

Filtre panelini açmak için **filtre** butonuna tıklayın. Birleştirilebilen üç filtreleme yöntemi sunar:

- **Hazır filtreler**, nesne türüne bağlı olarak katlanabilir bölümlerde yer alır. Örneğin, insanlar için doğum yılı, ölüm yılı, çeşitli kişi özellikleri, ilişki sayısı, etiketler ve bir nesnenin özel mi yoksa kamuya açık mı olduğu gibi filtreleme yapabilirsiniz.
- **Gelişmiş filtre** – hazır filtrelerin ifade edemediği filtreler için bir koşul oluşturucu, [aşağıda](#gelişmiş-filtre) açıklanmıştır.
- **GQL** – [Gramps Sorgu Dili](gql.md) için bir sorgu metin alanı. Sorguyu yazın ve Enter tuşuna basın veya **Uygula**'ya tıklayın. Sorgu geçersizse, alanın çerçevesi kırmızıya döner. Bir sorgu diğer filtrelerin üzerine uygulanır.

Aktif filtreler, listenin üstünde çipler olarak gösterilir. Tek bir filtreyi kaldırmak için çipin temizleme butonuna tıklayın veya hepsini birden kaldırmak için **Tüm filtreleri temizle** seçeneğini kullanın.

### Gelişmiş filtre

Filtre panelinin altındaki **Gelişmiş filtre** seçeneğine tıklayarak koşul oluşturucuyu açın. Koşulları, "İsimli kişiler" veya "Öncüller" gibi Gramps Masaüstü'nden bilinen filtre kurallarıdır.

- **Koşul ekle**'ye tıklayarak bir kural seçin. Kurallar kategorilere ayrılmıştır ve isim veya açıklama ile aranabilir.
- Kuralın parametrelerini doldurun. Her parametrenin eşleşen bir girişi vardır; örneğin bir tarih alanı, bir etiket seçici veya bir kişi veya yer için bir nesne seçici.
- Bir grubun koşullarının nasıl birleştirileceğini seçin: **Tüm koşullar**, **Herhangi bir koşul** veya – yanlarındaki menü aracılığıyla – **Tam olarak bir koşul**.
- Başka bir grubun içine koşul grubu eklemek için **Grup ekle**'ye tıklayın; kendi birleştirme yöntemine sahip olacaktır.
- Bir koşul veya grup üzerinde **Değil** seçeneğini seçerek tersine çevirin.

Listeyi filtrelemek için **Uygula**'ya tıklayın.

Oluşturucu açıldığında aktif olan hazır filtreler, koşullar olarak orada görünür. Oluşturduğunuz filtre, hazır filtrelerle ifade edilebiliyorsa, uygulandıktan sonra onlarla birlikte gösterilir. Aksi takdirde, tek bir **Gelişmiş filtre** çipi olarak gösterilir ve filtre paneli, oluşturucuyu yeniden açmak için bir **Düzenle** butonu sunar.

!!! not
    Gramps Masaüstü'nde kaydedilen özel filtrelere atıfta bulunan kurallar oluşturucuda mevcut değildir. Kurallar, Gramps Web API 3.24 veya daha yenisi ile kendi dilinizde gösterilir.

## Nesneleri Seçme ve Toplu İşlem Yapma

Düzenleme izinlerine sahip kullanıcılar, filtre butonunun yanında bir **Seç** butonu görür. Seçim moduna girmek için tıklayın; bu, her satıra bir onay kutusu ekler.

İstediğiniz nesneleri işaretleyin ve seçilen nesne sayısını gösteren bir araç çubuğu ile birlikte bir **Eylem** açılır menüsü ve bir **Uygula** butonu görünür.

### Sil

Bir veya daha fazla nesneyi seçin, **Sil**'i seçin ve **Uygula**'ya tıklayın. Bir onay iletişim kutusu, işlemi onaylamanızı ister ve işlemin geri alınamayacağı konusunda uyarır.

!!! ipucu
    Silme işlemleri, [revizyon geçmişi](revisions.md) gibi diğer değişiklikler gibi kaydedilir, bu nedenle yanlış bir toplu silme, ilgili işlemi geri alarak düzeltilebilir.

### Birleştir

**Tam olarak iki** nesne seçin, **Birleştir**'i seçin ve **Uygula**'ya tıklayın. Bir iletişim kutusu, hangisinin birleştirilmiş nesne için ana verileri sağlaması gerektiğini sorar; ana olarak tutmak istediğiniz nesneye tıklayın. Diğer nesnenin verileri buna birleştirilir ve referanslar güncellenir.

Birleştirme, insanlar, aileler, etkinlikler, yerler, kaynaklar ve alıntılar için mevcuttur. Depolar, notlar ve medya nesneleri için mevcut değildir.

Geçerli bir seçim olmadan bir eylem seçerseniz – örneğin yalnızca bir nesne seçilmişse birleştirme – bir iletişim kutusu, neyin gerekli olduğunu açıklar.
