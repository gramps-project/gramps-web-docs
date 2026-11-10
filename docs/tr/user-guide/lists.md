# Listeler

Gramps Web'deki her nesne türünün bir liste görünümü vardır: İnsanlar, Aileler, Etkinlikler, Yerler, Kaynaklar, Alıntılar, Depolar, Notlar ve Medya. Hepsi aynı şekilde çalışır ve sıralama, filtreleme ve toplu düzenleme için aynı araçları paylaşır.

## Sıralama ve sayfalama

Bir sütun başlığına tıklayarak o sütuna göre sıralama yapabilirsiniz; tekrar tıkladığınızda sıralama tersine döner. Sıralama sunucu tarafından gerçekleştirilir, bu nedenle tüm listeye uygulanır, sadece baktığınız sayfaya değil.

Uzun listeler sayfalara bölünmüştür. Sayfalar arasında geçiş yapmak için alttaki sayfalama kontrollerini kullanın.

Dar ekranlarda tablo otomatik olarak kompakt bir düzene geçer, böylece liste görünümleri telefonda kullanılabilir kalır.

## Sütunları Seçme

Liste üzerindeki araç çubuğunun sağ ucundaki dişli simgesine tıklayarak **Sütunlar** penceresini açın. Bir sütunu göstermek veya gizlemek için işaretleyin veya işaretini kaldırın. **Sıfırla**, o liste için varsayılan seçimi geri yükler.

En az bir sütun görünür kalmalıdır, bu nedenle son kalan sütun işaretini kaldıramazsınız.

Sütun seçiminiz nesne türü ve aile ağacı başına hatırlanır. Tarayıcınızda saklanır, bu nedenle diğer kullanıcılar tarafından görünmez – ancak farklı bir tarayıcıya veya cihaza geçiş yaptığınızda da sizi takip etmez.

## Filtreleme

Filtre panelini açmak için **filtre** butonuna tıklayın. Birleştirilebilen üç filtreleme yöntemi sunar:

- **Hazır filtreler**, nesne türüne bağlı olarak katlanabilir bölümlerde bulunur. Örneğin insanlar için ad, doğum yılı, ölüm yılı, çeşitli kişi özellikleri, ilişkilerin sayısı, etiketler ve bir nesnenin özel mi yoksa genel mi olduğunu filtreleyebilirsiniz. Aileler, baba, anne veya bir çocuğun adıyla filtrelenebilir, kaynaklar yazarına göre ve yerler ile depolar türlerine göre filtrelenebilir.
- **Gelişmiş filtre** – hazır filtrelerin ifade edemediği filtreler için bir koşul oluşturucu, [aşağıda](#advanced-filter) açıklanmıştır.
- **GOQL** – [Gramps Nesne Sorgu Dili](goql.md) için bir ifade yazmak üzere bir metin alanı, sözdizimi vurgulaması ile. İfadeyi yazın ve Enter tuşuna basın veya **Uygula**'ya tıklayın. İfade geçersizse, alan hata olarak işaretlenir. Bir ifade diğer filtrelerin üzerine uygulanır.

Aktif filtreler, araç çubuğunun altında bir satırda çipler olarak gösterilir. Tek bir filtreyi kaldırmak için çipin temizleme butonuna tıklayın veya hepsini bir anda kaldırmak için **Tüm filtreleri temizle** seçeneğini kullanın.

### Gelişmiş filtre

Filtre panelinin altındaki **Gelişmiş filtre** seçeneğine tıklayarak koşul oluşturucuyu açın. Koşulları, "İnsanlar &lt;isim&gt; ile" veya "&lt;kişi&gt;nin Ataları" gibi Gramps Masaüstü'nden bilinen filtre kurallarıdır.

- **Koşul ekle**'ye tıklayarak bir kural seçin. Kurallar kategorilere ayrılmıştır ve isim veya açıklama ile aranabilir.
- Kuralın parametrelerini doldurun. Her parametreye karşılık gelen bir giriş vardır; örneğin bir tarih alanı, bir etiket seçici veya bir kişi veya yer için bir nesne seçici.
- Bir grubun koşullarının nasıl birleştirileceğini seçin: **Tüm koşullar**, **Herhangi bir koşul** veya – yanlarındaki menü aracılığıyla – **Tam olarak bir koşul**.
- Başka bir grubun içine koşul grubu eklemek için **Grup ekle**'ye tıklayın; kendi birleştirme yöntemine sahip olacaktır.
- Bir koşul veya grup üzerinde **Değil** seçeneğini seçerek tersine çevirin.

Listeyi filtrelemek için **Uygula**'ya tıklayın.

Koşul oluşturucuyu açtığınızda aktif olan hazır filtreler ve GOQL ifadesi burada koşul olarak görünür. Bir GOQL ifadesi ayrıca kendi koşulu olarak eklenebilir; örneğin birkaç ifadeyi **Herhangi bir koşul** ile birleştirmek için. Oluşturduğunuz filtre, hazır filtrelerle ifade edilebiliyorsa, uygulandıktan sonra onlarla birlikte gösterilir. Aksi takdirde, tek bir **Gelişmiş filtre** çipi olarak gösterilir ve filtre paneli, oluşturucuyu yeniden açmak için bir **Düzenle** butonu sunar.

!!! not
    Gramps Masaüstü'nde kaydedilen özel filtrelere atıfta bulunan kurallar oluşturucuda mevcut değildir. Kurallar, Gramps Web API 3.24 veya daha yenisi ile kendi dilinizde gösterilir.

## Nesneleri Seçme ve Toplu İşlem Yapma

Düzenleme izinlerine sahip kullanıcılar, filtre butonunun yanında bir **Seç** butonu görür. Seçim moduna girmek için tıklayın; bu, her satıra bir onay kutusu ekler.

İstediğiniz nesneleri işaretleyin ve seçilen nesne sayısını gösteren bir araç çubuğu ile birlikte bir **Eylem** açılır menüsü ve bir **Uygula** butonu görünür.

Tablo başlığındaki onay kutusu, mevcut sayfadaki tüm nesneleri seçer. Eğer daha fazla nesne mevcut filtrelerle eşleşiyorsa, araç çubuğu ardından **Tümünü Seç (N)** seçeneğini sunar; bu, tüm sayfalardaki N eşleşen nesneyi seçer. Bir satırın onayını kaldırmak, sayfayı değiştirmek veya filtreleri değiştirmek ya da seçim modundan çıkmak bu seçimi sonlandırır.

### Sil

Bir veya daha fazla nesneyi seçin, **Sil** seçeneğini belirleyin ve **Uygula**'ya tıklayın. Bir onay penceresi, işlemi onaylamanızı ister ve işlemin geri alınamayacağı konusunda uyarır.

On nesneden fazla silme işlemi arka planda bir görev olarak çalışır. İlerleme, **Uygula** butonunun yanında ve [Bildirimler](notifications.md) bölümünde gösterilir ve işlem tamamlandığında liste yeniden yüklenir.

!!! ipucu
    Silme işlemleri, diğer değişiklikler gibi [revizyon geçmişinde](revisions.md) kaydedilir, bu nedenle yanlış bir toplu silme işlemi, ilgili işlemi geri alarak tersine çevrilebilir.

### Birleştir

**Tam olarak iki** nesne seçin, **Birleştir** seçeneğini belirleyin ve **Uygula**'ya tıklayın. Bir iletişim kutusu, hangisinin birleştirilmiş nesne için ana verileri sağlayacağını sorar; ana olarak tutmak istediğiniz nesneye tıklayın. Diğer nesnenin verileri buna birleştirilir ve referanslar güncellenir.

Birleştirme, insanlar, aileler, etkinlikler, yerler, kaynaklar ve alıntılar için mevcuttur. Depolar, notlar ve medya nesneleri için mevcut değildir.

Medya görünümünde, seçim hem galeri hem de liste düzeninde çalışır: seçim modunda, bir karoya veya satıra tıklamak onu açıp kapatır. Medya için mevcut olan tek eylem **Sil**'dir.

Geçerli bir seçim olmadan bir eylem seçerseniz – örneğin yalnızca bir nesne seçili olduğunda birleştirme – bir iletişim kutusu, neyin gerekli olduğunu açıklar.
