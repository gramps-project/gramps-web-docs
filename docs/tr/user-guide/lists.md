# Listeler

Gramps Web'deki her nesne türünün bir liste görünümü vardır: İnsanlar, Aileler, Etkinlikler, Yerler, Kaynaklar, Alıntılar, Depolar, Notlar ve Medya. Hepsi aynı şekilde çalışır ve sıralama, filtreleme ve toplu düzenleme için aynı araçları paylaşır.

## Sıralama ve sayfalama

Bir sütun başlığına tıklayarak o sütuna göre sıralama yapabilirsiniz; tekrar tıklarsanız sıralama tersine döner. Sıralama sunucu tarafından gerçekleştirilir, bu nedenle tüm listeye uygulanır, sadece baktığınız sayfaya değil.

Uzun listeler sayfalara bölünmüştür. Aralarına geçmek için alt kısımdaki sayfalama kontrolünü kullanın.

Dar ekranlarda tablo otomatik olarak kompakt bir düzene geçer, böylece liste görünümleri telefonda kullanılabilir kalır.

## Sütunları Seçme

Liste üzerinde **Sütunlar** iletişim kutusunu açmak için dişli simgesine tıklayın. Bir sütunu göstermek veya gizlemek için işaretleyin veya işaretini kaldırın. **Sıfırla**, o liste için varsayılan seçimi geri yükler.

En az bir sütun görünür kalmalıdır, bu nedenle son kalan sütun işaretini kaldıramazsınız.

Sütun seçiminiz nesne türüne ve aile ağacına göre hatırlanır. Tarayıcınızda saklanır, bu nedenle diğer kullanıcılar tarafından görünmez – ancak farklı bir tarayıcıya veya cihaza geçiş yaptığınızda da sizi takip etmez.

## Filtreleme

Filtre panelini açmak için **filtre** butonuna tıklayın. Birlikte kullanılabilen üç filtreleme yöntemi sunar:

- **Hazır filtreler**, nesne türüne bağlı olarak katlanabilir bölümlerde bulunur. Örneğin, insanlar için doğum yılı, ölüm yılı, çeşitli kişi özellikleri, ilişki sayısı, etiketler ve bir nesnenin özel mi yoksa genel mi olduğunu filtreleyebilirsiniz.
- **Gelişmiş filtre** – hazır filtrelerin ifade edemediği koşullar için bir koşul oluşturucu, [aşağıda](#advanced-filter) açıklanmıştır.
- **GQL** – [Gramps Sorgu Dili](gql.md) için bir sorgu metin alanı. Sorguyu yazın ve Enter tuşuna basın veya **Uygula** butonuna tıklayın. Sorgu geçersizse, alanın çerçevesi kırmızıya döner. Bir sorgu, diğer filtrelerin üzerine uygulanır.

Aktif filtreler, listenin üstünde çipler olarak gösterilir. Tek bir filtreyi kaldırmak için çipin temizleme butonuna tıklayın veya hepsini birden kaldırmak için **Tüm filtreleri temizle** seçeneğini kullanın.

### Gelişmiş filtre

Filtre panelinin altındaki **Gelişmiş filtre** butonuna tıklayarak koşul oluşturucuyu açın. Koşulları, Gramps Masaüstü'nden bilinen filtre kurallarıdır, örneğin "İnsanlar &lt;isim&gt; ile" veya "&lt;kişi&gt;nin ataları".

- **Koşul ekle** butonuna tıklayarak bir kural seçin. Kurallar kategorilere ayrılmıştır ve ad veya açıklama ile aranabilir.
- Kuralın parametrelerini doldurun. Her parametrenin eşleşen bir girişi vardır, örneğin bir tarih alanı, bir etiket seçici veya bir kişi veya yer için bir nesne seçici.
- Bir grubun koşullarının nasıl birleştirileceğini seçin: **Tüm koşullar**, **Herhangi bir koşul** veya – yanlarındaki menü aracılığıyla – **Tam olarak bir koşul**.
- Başka bir grubun içine koşul grubu eklemek için **Grup ekle** butonuna tıklayın, kendi birleştirme yöntemine sahip olacaktır.
- Bir koşul veya grup üzerinde **Değil** seçeneğini seçerek tersini alın.

Listeyi filtrelemek için **Uygula** butonuna tıklayın.

Koşul oluşturucuyu açtığınızda aktif olan hazır filtreler burada koşullar olarak görünür. Oluşturduğunuz filtre, hazır filtrelerle ifade edilebiliyorsa, uygulandıktan sonra onlarla birlikte gösterilir. Aksi takdirde, tek bir **Gelişmiş filtre** çipi olarak gösterilir ve filtre paneli, oluşturucuyu yeniden açmak için bir **Düzenle** butonu sunar.

!!! not
    Gramps Masaüstü'nde kaydedilen özel filtrelere atıfta bulunan kurallar oluşturucuda mevcut değildir. Kurallar, Gramps Web API 3.24 veya daha yenisi ile dilinizde gösterilir.

## Nesneleri Seçme ve Toplu İşlem Yapma

Düzenleme izinlerine sahip kullanıcılar, filtre butonunun yanında bir **Seç** butonu görür. Seçim moduna girmek için tıklayın, bu her satıra bir onay kutusu ekler.

İstediğiniz nesneleri işaretleyin ve seçilen nesne sayısını gösteren bir araç çubuğu belirir; bunun yanında bir **Eylem** açılır menüsü ve bir **Uygula** butonu bulunur.

Tablo başlığındaki onay kutusu, mevcut sayfadaki tüm nesneleri seçer. Eğer daha fazla nesne mevcut filtrelere uyuyorsa, araç çubuğu **Tümünü Seç (N)** seçeneğini sunar; bu, tüm sayfalardaki N eşleşen nesneyi seçer. Bir satırı işaretini kaldırmak, sayfayı değiştirmek veya filtreleri değiştirmek veya seçim modundan çıkmak bu seçimi sonlandırır.

### Sil

Bir veya daha fazla nesneyi seçin, **Sil** seçeneğini seçin ve **Uygula** butonuna tıklayın. Bir onay iletişim kutusu, işlemi onaylamanızı ister ve işlemin geri alınamayacağı konusunda uyarır.

On nesneden fazla silme işlemi arka planda bir görev olarak gerçekleştirilir. İlerlemesi, **Uygula** butonunun yanında ve [Bildirimler](notifications.md) bölümünde gösterilir ve işlem tamamlandığında liste yeniden yüklenir.

!!! ipucu
    Silme işlemleri, herhangi bir diğer değişiklik gibi [revizyon geçmişinde](revisions.md) kaydedilir, bu nedenle yanlış bir toplu silme işlemi, ilgili işlemi geri alarak tersine çevrilebilir.

### Birleştir

**Tam olarak iki** nesne seçin, **Birleştir** seçeneğini seçin ve **Uygula** butonuna tıklayın. Bir iletişim kutusu, hangisinin birleştirilmiş nesne için birincil verileri sağlaması gerektiğini sorar; birincil olarak tutmak istediğinizi tıklayın. Diğer nesnenin verileri buna birleştirilir ve referanslar güncellenir.

Birleştirme, insanlar, aileler, etkinlikler, yerler, kaynaklar ve alıntılar için mevcuttur. Depolar, notlar ve medya nesneleri için mevcut değildir.

Medya görünümünde, seçim hem galeri hem de liste düzeninde çalışır: seçim modunda, bir karoyu veya satırı tıklamak onu açıp kapatır. Medya için mevcut olan tek eylem **Sil**'dir.

Geçerli bir seçim olmadan bir eylem seçerseniz – örneğin yalnızca bir nesne seçilmişse birleştirme – bir iletişim kutusu, neyin gerekli olduğunu açıklar.
