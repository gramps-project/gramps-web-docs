# Gramps'ın Verileri Organize Etme Şekli

Gramps Web, bir aile ağacını bir grafik olarak değil, birbirine bağlı ayrı nesneler – insanlar, aileler, olaylar, yerler, kaynaklar vb. – olarak depolar. Bu nesnelerin nasıl bir araya geldiğini bildiğinizde, veri girişi öngörülebilir hale gelir: bağlamak istediğiniz her şeyin önce var olması gerekir.

Gramps Web, Gramps Desktop ile aynı veri modelini kullanır, bu nedenle bu sayfadaki her şey her iki uygulama için de geçerlidir.

## Temel Bileşenler

| Nesne | Neyi Temsil Eder | Örnekler |
|---|---|---|
| Kişi | Bir birey | Siz, büyükanneniz |
| Aile | Bir çift, çocukları veya her ikisi | Ebeveynleriniz ve çocukları |
| Olay | Bir tarih ve yer ile gerçekleşen bir şey | Doğum, evlilik, nüfus sayımı, göç |
| Yer | Coğrafi bir konum | Bir köy, bir ilçe, bir ülke |
| Kaynak | Bir belge veya bilgi koleksiyonu | Bir kilise kaydı, bir nüfus sayımı, bir kitap |
| Alıntı | Bir kaynak içindeki belirli bir referans | Kilise kaydının 12. sayfası, 3. girişi |
| Depo | Bir kaynağın saklandığı yer | Bir arşiv, bir kütüphane, bir web sitesi |
| Not | Serbest metin | Bir transkripsiyon, araştırma notları |
| Medya nesnesi | Bir dosya | Bir fotoğraf, taranmış bir belge |

Her nesne türünün Gramps Web'de kendi listesi vardır, [Listeler](lists.md) sayfasına bakın.

## İnsanlar ve Aileler

Ebeveynler ve çocuklar doğrudan birbirine bağlı değildir, ancak bir **aile** aracılığıyla bağlıdır. Bir ailede en fazla iki partner ve herhangi bir sayıda çocuk bulunabilir:

- Ebeveynleriniz ve siz, bir çocuk olduğunuz aile aracılığıyla bağlısınız.
- Kardeşleriniz, aynı ailenin diğer çocuklarıdır.
- Siz ve eşiniz, çocuklarınızla birlikte başka bir aile oluşturursunuz.

Bir kişi bir ailede çocuk olabilir ve birkaç ailede partner olabilir. Her çocuğun ebeveynlerden biriyle doğum, evlat edinme veya üvey çocuk gibi bir ilişkisi vardır ve her ailenin evli veya medeni birlik gibi bir ilişki türü vardır.

Bu nedenle, bir kişiye "ebeveyn eklemek", o kişiyi bir aileye çocuk olarak eklemek anlamına gelir – bu, [ağaç grafiği](tree-edit.md) tarafından sizin için tek bir adımda yapılır.

## Olaylar

Bir doğum, ölüm veya evlilik, bir kişinin alanı değil, kendi başına bir **olay**dır; bir tür, bir tarih, bir yer ve bir açıklama içerir. İnsanlar, bir olayla bir **rol** aracılığıyla bağlantılıdır: doğumun sahibi "Birincil" rolüne sahiptir, diğer bir kişi aynı olaya tanık olarak bağlanabilir.

Bir çifti ilgilendiren olaylar, evlilik gibi, aileye ait olup, partnerlerden birine ait değildir. Bir olay, birkaç kişi tarafından da paylaşılabilir – örneğin, bir hanehalkını listeleyen bir nüfus sayımı kaydı – her kişi için bir kez girilmek yerine.

## Paylaşılan Nesneler: Yerler ve Kaynaklar

Yerler, kaynaklar, alıntılar, depolar, notlar ve medya nesneleri kendi başlarına varlık gösterir ve başka nesneler aynı nesneye atıfta bulunabilir. Bunun birkaç sonucu vardır:

- **Bir kez oluştur, birçok kez seç.** On tane atalarınızın doğduğu köy bir yerdir, on doğum olayında seçilir. Adını veya koordinatlarını düzeltirseniz, düzeltme her yerde geçerli olur.
- **Seçmeden önce oluşturun.** Gramps Web'deki formlar, zaten var olan yerleri ve kaynakları seçer. Önce **+** (Ekle) butonunu kullanarak yeni bir yer veya kaynak oluşturun.
- **Yerler iç içe geçebilir.** Bir yer, daha büyük bir yer tarafından kapsanabilir – bir köy bir ilçe tarafından, ilçe bir ülke tarafından – bu nedenle her köy için tüm hiyerarşiyi tekrar etmenize gerek yoktur.
- **Kaynaklar ve alıntılar ayrıdır.** Bir kaynak, kilise kaydının tamamıdır; bir alıntı, bir gerçeği destekleyen belirli bir giriştir, sayfası, tarihi ve güven dereceniz ile birlikte. Birçok alıntı aynı kaynağa işaret edebilir.

Eğer yanlışlıkla aynı yer veya kaynağı iki kez oluşturduysanız, [kopyaları birleştirebilirsiniz](lists.md#merge).

## Bir Nesnenin Sayfasını Düzenleme

Bir kaynak, depo veya medya nesnesinin sayfasında, düzenleme modunda başlığına tıklayarak bunu değiştirebilirsiniz (bir medya nesnesi için, açıklamasını). Kaydetmek için Enter tuşuna basın, ✓'ye tıklayın veya başka bir yere tıklayın; iptal etmek için Escape tuşuna basın veya ✕'ye tıklayın.

Bir nesnenin sayfasındaki çoğu liste, verdiğiniz sırayı korur; örneğin olaylar, isimler, özellikler, adresler, alıntılar veya bir ailenin çocukları. Düzenleme modunda, bir satırı seçin ve yukarı ve aşağı butonlarıyla hareket ettirin veya yeni konumuna sürükleyin: fare ile satıra basın ve hareket ettirin; dokunmatik ekranda, satıra basılı tutun. Sürükleme sırasında iptal etmek için Escape tuşuna basın. Galerideki medya da aynı şekilde yeniden sıralanabilir, [Profil resimleri](media.md#profile-pictures) sayfasına bakın.

## Ana Kişi

Ana Kişi, aile ağacı grafiklerinin başladığı kişidir ve raporlar için varsayılan başlangıç noktasıdır. Bunu ayarlamak için [İlk giriş](first-login.md) sayfasına bakın.

!!! not "Gramps Desktop'tan Farklı"
    Gramps Desktop'ta, Ana Kişi aile ağacı veritabanında saklanır, bu nedenle o veritabanını açan herkes için aynıdır. Gramps Web bunu kullanmaz. Bunun yerine, Ana Kişi tarayıcınızda, her ağaç için ayrı olarak saklanır: diğer kullanıcılarla paylaşılmaz ve farklı bir tarayıcıya veya cihaza geçmez. Gramps Desktop'tan bir ağaç içe aktardıktan sonra veya Gramps Web'i başka bir cihazda kullandığınızda, bunu tekrar ayarlamanız gerekir.

## Önerilen Sıra

Yeni bir aileyi elle girerken, bu sıra formlar arasında gidip gelmeyi önler:

1. **Yerler ve kaynaklar.** Gerekli yerleri oluşturun ve kaynakları kaydediyorsanız, üzerinde çalıştığınız kaynağı oluşturun.
2. **İnsanlar.** Doğum ve ölüm tarihleri ile yerleri olan kişileri ekleyin. Bu, aile ağacı grafiğinin düzenleme modunda en hızlıdır; bu mod, aileleri sizin için oluşturur – [Yeni bir ağaç başlatın](start-tree.md) ve [Aile ağacını düzenleme](tree-edit.md) sayfalarına bakın.
3. **Diğer olaylar.** Evliliği eklemek için bir aileyi açın (örneğin bir kişinin İlişkiler sekmesinden) ve diğer olayları eklemek için bir kişinin sayfasını açın.
4. **Alıntılar.** Bir kaynağın desteklediği kişi, olay veya diğer nesnenin Kaynak Alıntıları sekmesinde, yeni bir alıntı ekleyin, kaynağı seçin ve sayfayı girin.
5. **Notlar ve medya.** Transkripsiyonlar, fotoğraflar ve taramalar ekleyin – [Medya dosyası ekleyin](media.md) sayfasına bakın.

## Tarih Girişi

Bir tarih, ayrı yıl, ay ve gün alanları olarak girilir; bunlar ayrıca bir tarih seçici kullanılarak da doldurulabilir. Bilmediğiniz kısımları atlayın: yalnızca bir yıl geçerli bir tarihtir. 
Kesin bir günü tahmin etmek yerine, alanların üzerindeki çiplerle tarihin türünü seçerek gerçekten bildiğiniz şeyi tanımlayın. Çiplerin altında bir ipucu, seçilen türü açıklar:

| Ne bildiğiniz | Tür | Örnek |
|---|---|---|
| Kesin tarih veya bir kısmı | Normal | 12 Mart 1850, veya sadece 1850 |
| Yaklaşık bir tarih | Yaklaşık | yaklaşık 1850 |
| Bir sınır | Önce, Sonra | 1900'den önce |
| Tarih bir dönem içinde bir yerde | Aralık | 1850 ile 1855 arasında (en erken ve en geç alanları) |
| Bir şey bir süre devam etti | Süre | 1850'den 1855'e kadar |

Bir Süre için, iki tarihten ("Başlangıç" ve "Bitiş") biri boş bırakılabilir, bu nedenle "1850'den" veya "1855'e kadar" ifadesi yalnızca bir tarih ile bir Süre oluşturur.

**Kalite** ve **Takvim** alanları, bir tarih bunlardan birini kullandığında otomatik olarak açılan **Daha fazla seçenek** altında bulunur. Kalite, bir tarihe nasıl ulaştığınızı kaydeder: "Tahmini" bir tahmin için, "Hesaplanan" ise ölüm yaşından hesaplanan doğum yılı gibi diğer bilgilerden türetilen bir tarih için.

!!! uyarı "Yaklaşık ve tahmini tarihler her iki yönde 50 yıl kapsar"
    Gramps tarihler arasında karşılaştırma yaptığında, "yaklaşık" türündeki bir tarihi – ve "Tahmini" kalitesine sahip herhangi bir tarihi – verilen tarihten 50 yıl önceye kadar ve 50 yıl sonrasına kadar uzanan bir aralık olarak ele alır. Örneğin, 1840 ile 1860 arasında doğan kişileri listelemek için İnsanlar listesini filtrelemek, "yaklaşık 1880" doğumlu bir kişiyi de bulur, çünkü bu tarih 1830 ile 1930'u kapsar. Aynı şekilde, "önce" ve "sonra" tarihin 50 yıl öncesine veya sonrasına kadar uzandığı kabul edilir.

    Bu, sürpriz sonuçlara yol açabilir, bu nedenle "yaklaşık" ve "Tahmini" terimlerini yalnızca tarihi daraltamadığınızda kullanın. Daha kısa bir dönem biliyorsanız, "1878 ile 1882 arasında" gibi bir Aralık daha kesin bir sonuçtur.

Takvim, orijinal kayıtta kullanılan takvimde bir tarih girmenizi sağlar; örneğin, Julian takvimi gibi, kendiniz dönüştürmek yerine.
