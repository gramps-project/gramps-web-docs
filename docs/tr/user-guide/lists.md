# Listeler

Gramps Web'deki her nesne türünün bir liste görünümü vardır: İnsanlar, Aileler, Olaylar, Yerler, Kaynaklar, Alıntılar, Depolar, Notlar ve Medya. Hepsi aynı şekilde çalışır ve sıralama, filtreleme ve toplu düzenleme için aynı araçları paylaşır.

## Sıralama ve sayfalama

Bir sütun başlığına tıklayarak o sütuna göre sıralama yapabilirsiniz; tekrar tıklarsanız sıralama tersine döner. Sıralama sunucu tarafından gerçekleştirilir, bu nedenle yalnızca baktığınız sayfayı değil, tüm listeyi etkiler.

Uzun listeler sayfalara bölünmüştür. Aralarına geçmek için alt kısımdaki sayfalama kontrollerini kullanın.

Dar ekranlarda tablo otomatik olarak kompakt bir düzenle geçiş yapar, böylece liste görünümleri telefonda kullanılabilir kalır.

## Sütunları Seçme

Liste üzerindeki araç çubuğunun sağ ucundaki dişli simgesine tıklayarak **Sütunlar** iletişim kutusunu açın. Bir sütunu göstermek veya gizlemek için işaretleyin veya işaretini kaldırın. **Sıfırla**, o liste için varsayılan seçimi geri yükler.

En az bir sütun görünür kalmalıdır, bu nedenle son kalan sütun işaretini kaldıramazsınız.

Varsayılan sütunların yanı sıra, her liste bir **Etiketler** sütunu ve özel kayıtları görüntüleyebilen kullanıcılar için her özel nesne için bir kilit gösteren bir **Gizlilik** sütunu sunar. Daha önce bir listenin sütun seçimlerini değiştirdiyseniz, **Etiketler** gibi yeni sütunlar otomatik olarak eklenmez; bunları iletişim kutusunda işaretleyin.

Sütun seçiminiz nesne türüne ve aile ağacına göre hatırlanır. Tarayıcınızda saklanır, bu nedenle diğer kullanıcılar tarafından görünmez – ancak farklı bir tarayıcıya veya cihaza geçildiğinde de takip edilmez.

## Filtreleme

Filtre panelini açmak için **filtre** butonuna tıklayın. Birleştirilebilen üç filtreleme yöntemi sunar:

- **Hazır filtreler**, nesne türüne bağlı olarak katlanabilir bölümlerde bulunur. Örneğin, insanlar için isim, doğum yılı, ölüm yılı, çeşitli kişi özellikleri, ilişki sayısı, etiketler ve bir nesnenin özel mi yoksa kamuya açık mı olduğunu filtreleyebilirsiniz. Aileler baba, anne veya bir çocuğun adıyla, kaynaklar yazarla ve yerler ile depolar türlerine göre filtrelenebilir.
- **Gelişmiş filtre** – hazır filtrelerin ifade edemediği koşullar için bir koşul oluşturucu, [aşağıda](#advanced-filter) açıklanmıştır.
- **GOQL** – [Gramps Nesne Sorgu Dili](goql.md) için bir ifade yazmak üzere bir metin alanı, sözdizimi vurgulaması ile. İfadeyi yazın ve Enter tuşuna basın veya **Uygula** butonuna tıklayın. İfade geçersizse, alan hata olarak işaretlenir. Bir ifade diğer filtrelerin üzerine uygulanır.

Aktif filtreler, araç çubuğunun altında bir satırda çipler olarak gösterilir. Tek bir filtreyi kaldırmak için çipin temizleme butonuna tıklayın veya hepsini birden kaldırmak için **Tüm filtreleri temizle** seçeneğini kullanın.

### Gelişmiş filtre

Filtre panelinin altındaki **Gelişmiş filtre** seçeneğine tıklayarak koşul oluşturucuyu açın. Koşulları, Gramps Masaüstü'nden bilinen filtre kurallarıdır, örneğin "İsimli insanlar" veya "<kişi>nin ataları".

- **Koşul ekle** butonuna tıklayarak bir kural seçin. Kurallar kategorilere ayrılmıştır ve isim veya açıklama ile aranabilir.
- Kuralın parametrelerini doldurun. Her parametreye karşılık gelen bir giriş alanı vardır, örneğin bir tarih alanı, bir etiket seçici veya bir kişi veya yer için bir nesne seçici.
- Bir grubun koşullarının nasıl birleştirileceğini seçin: **Tüm koşullar**, **Herhangi bir koşul** veya – yanlarındaki menüden – **Tam olarak bir koşul**.
- Başka bir grubun içine koşul grubu eklemek için **Grup ekle** butonuna tıklayın; kendi birleştirme yöntemine sahip olacaktır.
- Bir koşul veya grup üzerinde **Değil** seçeneğini seçerek tersini alın.

Listeyi filtrelemek için **Uygula** butonuna tıklayın.

Hazır filtreler ve yapılandırıcıyı açtığınızda aktif olan GOQL ifadesi burada koşul olarak görünür. Bir GOQL ifadesi, kendi koşulu olarak da eklenebilir; örneğin, birkaç ifadeyi **Herhangi bir koşul** ile birleştirmek için. Oluşturduğunuz filtre, hazır filtrelerle ifade edilebiliyorsa, uygulandıktan sonra onlarla birlikte gösterilir. Aksi takdirde, tek bir **Gelişmiş filtre** çipi olarak gösterilir ve filtre paneli, yapılandırıcıyı yeniden açmak için bir **Düzenle** butonu sunar.

!!! not
    Gramps Masaüstü'nde kaydedilen özel filtrelere atıfta bulunan kurallar yapılandırıcıda mevcut değildir. Kurallar, Gramps Web API 3.24 veya daha yenisi ile dilinizde gösterilir.

#### Kaydedilmiş filtreler

Oluşturduğunuz bir filtreyi yeniden kullanmak için, koşul oluşturucuda **Kaydet** butonuna tıklayın ve bir isim verin. Mevcut bir isim altında kaydetmek, o filtreyi değiştirir. **Kaydedilmiş filtreler**, mevcut nesne türü için kaydedilmiş filtreleri listeler; birini seçmek, onu yapılandırıcıya yükler, burada değişiklik yapabilir ve ardından **Uygula** butonuna tıklayabilirsiniz.

Kaydedilmiş filtreler, tarayıcınızda, aile ağacı ve nesne türüne göre saklanır, bu nedenle diğer kullanıcılar veya diğer cihazlarınızda mevcut değildir.

Bir kaydedilmiş filtre, ağaç değiştiğinde çalışmayı durdurabilir; örneğin, silinmiş bir kişiye atıfta bulunuyorsa (nesne seçici "Bulunamadı" olarak gösterilir). Böyle bir filtre, koşul düzeltilene kadar uygulanamaz veya kaydedilemez.

## Nesneleri Seçme ve Toplu İşlem Yapma

Düzenleme izinlerine sahip kullanıcılar, filtre butonunun yanında bir **Seç** butonu görür. Seçim moduna girmek için tıklayın; bu, her satıra bir onay kutusu ekler.

İstediğiniz nesneleri işaretleyin ve seçilen nesne sayısını gösteren bir araç çubuğu ile birlikte bir **Eylem** açılır menüsü ve bir **Uygula** butonu görünür.

Tablo başlığındaki onay kutusu, mevcut sayfadaki tüm nesneleri seçer. Eğer mevcut filtrelerle daha fazla nesne eşleşiyorsa, araç çubuğu **Tümünü Seç (N)** seçeneğini sunar; bu, tüm N eşleşen nesneyi tüm sayfalarda seçer. Bir satırın işaretini kaldırmak, sayfayı değiştirmek veya filtreleri değiştirmek veya seçim modundan çıkmak bu seçimi sonlandırır.

### Sil

Bir veya daha fazla nesneyi seçin, **Sil** seçeneğini seçin ve **Uygula** butonuna tıklayın. Bir onay iletişim kutusu, işlemi onaylamanızı ister ve bu işlemin geri alınamayacağına dair uyarıda bulunur.

On nesneden fazla silme işlemi arka planda bir görev olarak çalışır. İlerleme, **Uygula** butonunun yanında ve [Bildirimler](notifications.md) bölümünde gösterilir ve işlem tamamlandığında liste yeniden yüklenir.

!!! ipucu
    Silme işlemleri, [revizyon geçmişinde](revisions.md) diğer değişiklikler gibi kaydedilir, bu nedenle yanlış bir toplu silme işlemi, ilgili işlemi geri alarak tersine çevrilebilir.

### Etiketler ve gizlilik

**Etiket Ekle**, **Etiket Kaldır** ve **Gizlilik** eylemleri, tüm seçilen nesneleri bir kerede değiştirir (Gramps Web API 3.26 veya daha yenisi gerektirir):

- **Etiket Ekle**, mevcut bir etiketi veya iletişim kutusunda oluşturduğunuz yeni bir etiketi ekler.
- **Etiket Kaldır**, seçilen nesnelerden mevcut olan bir etiketi kaldırır.
- **Gizlilik**, seçilen nesneleri özel veya kamuya açık olarak işaretler. Bu yalnızca nesnelerin kendilerini değiştirir, parçalarını veya bağlantılı kayıtları değil – [Özel kayıtlar](privacy.md) bölümüne bakın.

Silme işlemlerinde olduğu gibi, on nesneden fazla düzenleme işlemi arka planda bir görev olarak çalışır. Değişiklikler, [revizyon geçmişinde](revisions.md) bir işlem olarak kaydedilir, böylece birlikte geri alınabilirler.

### Birleştir

**Tam olarak iki** nesne seçin, **Birleştir** seçeneğini seçin ve **Uygula** butonuna tıklayın. Bir iletişim kutusu, hangisinin birleştirilmiş nesne için birincil verileri sağlaması gerektiğini sorar; birincil olarak tutmak istediğinizi tıklayın. Diğer nesnenin verileri buna birleştirilir ve referanslar güncellenir.

Birleştirme işlemi, insanlar, aileler, olaylar, yerler, kaynaklar ve alıntılar için mevcuttur. Depolar, notlar ve medya nesneleri için mevcut değildir.

Medya görünümünde, seçim hem galeri hem de liste düzeninde çalışır: seçim modunda, bir karoya veya satıra tıklamak onu açar veya kapatır. Medya nesneleri birleştirilemez.

Geçerli bir seçim olmadan bir eylem seçerseniz – örneğin yalnızca bir nesne seçilmişse birleştirme – bir iletişim kutusu, neyin gerekli olduğunu açıklar.
