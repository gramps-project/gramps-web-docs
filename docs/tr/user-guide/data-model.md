# Gramps'ın verileri nasıl organize ettiği

Gramps Web, bir aile ağacını bir şema olarak değil, birbirine bağlı ayrı nesneler – insanlar, aileler, olaylar, yerler, kaynaklar vb. – olarak saklar. Bu nesnelerin nasıl bir araya geldiğini bildiğinizde, veri girişi öngörülebilir hale gelir: bağlamak istediğiniz her şeyin önce var olması gerekir.

Gramps Web, Gramps Desktop ile aynı veri modelini kullanır, bu nedenle bu sayfadaki her şey her iki uygulama için de geçerlidir.

## Temel bileşenler

| Nesne | Neyi temsil eder | Örnekler |
|---|---|---|
| Kişi | Bir birey | Siz, büyükanneniz |
| Aile | Bir çift, çocukları veya her ikisi | Ebeveynleriniz ve onların çocukları |
| Olay | Bir tarihe ve bir yere sahip olan bir şey | Doğum, evlilik, nüfus sayımı, göç |
| Yer | Coğrafi bir konum | Bir köy, bir pariş, bir ülke |
| Kaynak | Bir belge veya bilgi koleksiyonu | Bir pariş kaydı, bir nüfus sayımı, bir kitap |
| Alıntı | Bir kaynak içindeki belirli bir referans | Pariş kaydının sayfa 12, giriş 3 |
| Depo | Bir kaynağın saklandığı yer | Bir arşiv, bir kütüphane, bir web sitesi |
| Not | Serbest metin | Bir transkripsiyon, araştırma notları |
| Medya nesnesi | Bir dosya | Bir fotoğraf, taranmış bir sertifika |

Her nesne türünün Gramps Web'de kendi listesi vardır, [Listeler](lists.md) bölümüne bakın.

## İnsanlar ve aileler

Ebeveynler ve çocuklar doğrudan birbirine bağlı değildir, ancak bir **aile** aracılığıyla bağlıdır. Bir aile en fazla iki ortak ve herhangi bir sayıda çocuk içerebilir:

- Ebeveynleriniz ve siz, bir çocuk olduğunuz aile aracılığıyla bağlısınız.
- Kardeşleriniz, aynı ailenin diğer çocuklarıdır.
- Siz ve eşiniz, çocuklarınızla birlikte başka bir aile oluşturursunuz.

Bir kişi bir ailede çocuk olabilir ve birden fazla ailede ortak olabilir. Her çocuğun her ebeveynle bir ilişkisi vardır, örneğin doğum, evlat edinme veya üvey çocuk, ve her ailenin bir ilişki türü vardır, örneğin evli veya medeni birlik.

Bu nedenle, bir kişiye "ebeveyn eklemek", o kişiyi bir aileye çocuk olarak eklemek anlamına gelir – bu, [ağaç şeması](tree-edit.md) tarafından sizin için tek bir adımda yapılır.

## Olaylar

Bir doğum, ölüm veya evlilik, bir kişinin alanı değil, kendi **olayıdır**, bir tür, bir tarih, bir yer ve bir açıklama ile birlikte. İnsanlar bir olaya bir **rol** ile bağlıdır: doğumun sahibi olan kişi "Birincil" rolüne sahiptir, oysa başka biri aynı olaya tanık olarak bağlı olabilir.

Bir çifti ilgilendiren olaylar, örneğin bir evlilik, aileye ait olup, her iki ortağa ait değildir. Bir olay, birden fazla kişi tarafından da paylaşılabilir – örneğin, bir hanehalkını listeleyen bir nüfus sayımı kaydı – her kişi için bir kez girilmek yerine.

## Paylaşılan nesneler: yerler ve kaynaklar

Yerler, kaynaklar, alıntılar, depolar, notlar ve medya nesneleri kendi başlarına var olur ve diğer nesnelerin herhangi bir sayısı aynı nesneye atıfta bulunabilir. Bunun birkaç sonucu vardır:

- **Bir kez oluştur, birçok kez seç.** On tane atalarınızın doğduğu köy bir yerdir, on doğum olayında seçilir. Adını veya koordinatlarını düzeltirseniz, düzeltme her yerde geçerli olur.
- **Seçmeden önce oluştur.** Gramps Web'deki formlar, zaten var olan yerleri ve kaynakları seçer. Öncelikle **+** (Ekle) düğmesini kullanarak yeni bir yer veya kaynak oluşturun.
- **Yerler iç içe geçmiş.** Bir yer, daha büyük bir yer tarafından kapsanabilir – bir köy bir ilçe tarafından, ilçe bir ülke tarafından – böylece her köy için tüm hiyerarşiyi tekrar etmek zorunda kalmazsınız.
- **Kaynaklar ve alıntılar ayrı.** Bir kaynak, pariş kaydının tamamıdır; bir alıntı, bir gerçeği destekleyen belirli bir giriştir, sayfası, tarihi ve ona olan güveninizi içerir. Birçok alıntı aynı kaynağa işaret edebilir.

Eğer yanlışlıkla aynı yer veya kaynağı iki kez oluşturduysanız, [kopyaları birleştirebilirsiniz](lists.md#merge).

## Ana Kişi

Ana Kişi, aile ağacı şemalarının başladığı kişidir ve raporlar için varsayılan başlangıç noktasıdır. Bunu nasıl ayarlayacağınızı görmek için [İlk giriş](first-login.md) bölümüne bakın.

!!! not "Gramps Desktop'tan farklı"
    Gramps Desktop'ta, Ana Kişi aile ağacı veritabanında saklanır, bu nedenle o veritabanını açan herkes için aynıdır. Gramps Web bunu kullanmaz. Bunun yerine, Ana Kişi tarayıcınızda, her ağaç için ayrı olarak saklanır: diğer kullanıcılarla paylaşılmaz ve farklı bir tarayıcıya veya cihaza geçiş yaptığınızda sizi takip etmez. Gramps Desktop'tan bir ağaç içe aktardıktan sonra veya Gramps Web'i başka bir cihazda kullandığınızda, bunu yeniden ayarlamanız gerekir.

## Önerilen bir sıra

Yeni bir aileyi elle girerken, bu sıra formlar arasında gidip gelmeyi önler:

1. **Yerler ve kaynaklar.** Gerekli yerleri oluşturun ve kaynakları kaydediyorsanız, üzerinde çalıştığınız kaynağı oluşturun.
2. **İnsanlar.** Doğum ve ölüm tarihleri ile yerleri olan insanları ekleyin. Bu, aile ağacı şemasının düzenleme modunda en hızlıdır, bu mod aileleri sizin için oluşturur – [Yeni bir ağaç başlat](start-tree.md) ve [Aile ağacını düzenleme](tree-edit.md) bölümüne bakın.
3. **Diğer olaylar.** Evliliği eklemek için bir aileyi açın (örneğin bir kişinin İlişkiler sekmesinden) ve diğer olayları eklemek için bir kişinin sayfasını açın.
4. **Alıntılar.** Bir kaynağın desteklediği kişi, olay veya diğer nesnenin Kaynak Alıntıları sekmesinde, yeni bir alıntı ekleyin, kaynağı seçin ve sayfayı girin.
5. **Notlar ve medya.** Transkripsiyonları, fotoğrafları ve taramaları ekleyin – [Medya dosyaları ekle](media.md) bölümüne bakın.

## Tarih girme

Bir tarih, ayrı yıl, ay ve gün alanları olarak girilir; bu alanlar bir tarih seçici kullanılarak da doldurulabilir. Bilmediğiniz kısımları atlayın: yalnızca bir yıl geçerli bir tarihtir.

Kesin bir günü tahmin etmek yerine, tarih ile ilgili bildiğiniz şeyleri **Tür** ile tanımlayın:

| Bildiğiniz şey | Tür | Örnek |
|---|---|---|
| Kesin tarih veya bir kısmı | Normal | 12 Mart 1850, ya da sadece 1850 |
| Yaklaşık bir tarih | yaklaşık | yaklaşık 1850 |
| Bir sınır | önce, sonra | 1900'den önce |
| Tarih bir dönem içinde bir yerde | Aralık | 1850 ile 1855 arasında |
| Bir şey bir süre boyunca sürdü | Süre | 1850'den 1855'e kadar |
| Sadece bir dönemin başlangıcı veya sonu | dan, e kadar | 1850'den |

**Kalite** alanı, bir tarihe nasıl ulaştığınızı kaydeder: "Tahmin" eğitilmiş bir tahmin için, "Hesaplanmış" diğer bilgilerden türetilen bir tarih için, örneğin ölüm yaşından hesaplanan bir doğum yılı için.

!!! uyarı "Yaklaşık ve tahmin edilen tarihler her iki yönde 50 yılı kapsar"
    Gramps tarihler arasında karşılaştırma yaptığında, "yaklaşık" türündeki bir tarihi – ve "Tahmin" kalitesine sahip herhangi bir tarihi – verilen tarihten 50 yıl öncesine kadar ve 50 yıl sonrasına kadar bir aralık olarak ele alır. Örneğin, 1840 ile 1860 arasında doğan kişiler için İnsanlar listesini filtrelemek, "yaklaşık 1880" doğumlu bir kişiyi de bulur, çünkü bu tarih 1830'dan 1930'a kadar geçerli kabul edilir. Aynı şekilde, "önce" ve "sonra" tarihten 50 yıl öncesine veya sonrasına kadar ulaşacak şekilde alınır.

    Bu, sürpriz sonuçlara yol açabilir, bu nedenle "yaklaşık" ve "Tahmin" terimlerini yalnızca tarihi daraltamadığınızda kullanın. Daha kısa bir dönem biliyorsanız, "1878 ile 1882 arasında" gibi bir Aralık daha kesin bir sonuç verir.

**Takvim** alanı, tarihi orijinal kayıtta kullanılan takvimde, örneğin Jülyen takviminde girmeyi sağlar; kendiniz dönüştürmek yerine.
