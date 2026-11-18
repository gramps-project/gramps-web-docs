# Gramps Verileri Nasıl Organize Eder

Gramps Web, bir aile ağacını bir grafik olarak değil, birbirine bağlı ayrı nesneler – insanlar, aileler, olaylar, yerler, kaynaklar vb. – olarak saklar. Bu nesnelerin nasıl bir araya geldiğini bildiğinizde, veri girişi öngörülebilir hale gelir: bağlantı kurmak istediğiniz her şey öncelikle var olmalıdır.

Gramps Web, Gramps Desktop ile aynı veri modelini kullanır, bu nedenle bu sayfadaki her şey her iki uygulama için de geçerlidir.

## Temel Bileşenler

| Nesne | Neyi Temsil Eder | Örnekler |
|---|---|---|
| Kişi | Bir birey | Siz, büyükanneniz |
| Aile | Bir çift, çocukları veya her ikisi | Ebeveynleriniz ve çocukları |
| Olay | Bir tarihte ve bir yerde gerçekleşen bir şey | Doğum, evlilik, nüfus sayımı, göç |
| Yer | Coğrafi bir konum | Bir köy, bir ilçe, bir ülke |
| Kaynak | Bir belge veya bilgi koleksiyonu | Bir kilise kaydı, bir nüfus sayımı, bir kitap |
| Alıntı | Bir kaynak içindeki belirli bir referans | Kilise kaydının sayfa 12, giriş 3 |
| Depo | Bir kaynağın saklandığı yer | Bir arşiv, bir kütüphane, bir web sitesi |
| Not | Serbest metin | Bir transkripsiyon, araştırma notları |
| Medya nesnesi | Bir dosya | Bir fotoğraf, taranmış bir belge |

Her nesne türünün Gramps Web'de kendi listesi vardır, [Listeler](lists.md) bölümüne bakın.

## İnsanlar ve Aileler

Ebeveynler ve çocuklar birbirine doğrudan bağlı değildir, ancak bir **aile** aracılığıyla bağlıdır. Bir aile en fazla iki ortağa ve herhangi bir sayıda çocuğa sahip olabilir:

- Ebeveynleriniz ve siz, bir çocuk olduğunuz aile aracılığıyla bağlısınız.
- Kardeşleriniz, aynı ailenin diğer çocuklarıdır.
- Siz ve eşiniz, çocuklarınızla birlikte başka bir aile oluşturursunuz.

Bir kişi bir ailede çocuk olabilir ve birden fazla ailede ortak olabilir. Her çocuğun ebeveynlerden her biriyle bir ilişkisi vardır; bu ilişkiler doğum, evlat edinme veya üvey çocuk gibi olabilir ve her ailenin evli veya medeni birlik gibi bir ilişki türü vardır.

Bu nedenle, bir kişiye "ebeveyn eklemek", o kişiyi bir aileye çocuk olarak eklemek anlamına gelir – bu, [ağaç grafiği](tree-edit.md) tarafından sizin için tek bir adımda yapılır.

## Olaylar

Bir doğum, ölüm veya evlilik, bir kişinin alanı değil, kendi başına bir **olay**dır; bir türü, tarihi, yeri ve açıklaması vardır. İnsanlar bir olaya **rol** ile bağlıdır: doğumun sahibi "Birincil" rolüne sahiptir, başka biri aynı olaya tanık olarak bağlı olabilir.

Bir çifti ilgilendiren olaylar, örneğin bir evlilik, aileye aittir, herhangi bir ortağa değil. Bir olay, birden fazla kişi tarafından da paylaşılabilir – örneğin, bir hanehalkını listeleyen bir nüfus sayımı kaydı – her kişi için bir kez girilmek yerine.

Bu, düzenlemeyi etkiler. Olayın kendisi – türü, tarihi, yeri ve açıklaması – ona bağlı olan herkes için aynıdır, bu nedenle bir kişinin sayfasından paylaşılan bir olayı düzenlemek, hepsi için değişiklik yapar. Bu nedenle, düzenleme penceresi önce diğer katılımcıları listeler ve alanlar yalnızca **Herkes için Düzenle** seçeneğinden sonra düzenlenebilir hale gelir. Olayla bir kişinin bağlantısına ait olan – rol, alıntılar, notlar ve yalnızca o kişiye uygulanan nitelikler – olayın sayfasında, düzenleme modundaki **Katılımcılar** sekmesinde düzenlenir. Orada katılımcıları ekleyebilir ve çıkarabilirsiniz. Örneğin, bir vaftiz için vaftiz babasının rolü ve "bir işaretle imzalandı" notu, vaftizle değil, vaftiz babasının bağlantısına aittir.

## Paylaşılan Nesneler: Yerler ve Kaynaklar

Yerler, kaynaklar, alıntılar, depolar, notlar ve medya nesneleri kendi başlarına var olur ve herhangi bir sayıda diğer nesne aynı nesneye atıfta bulunabilir. Bunun birkaç sonucu vardır:

- **Bir kez oluştur, birçok kez seç.** On tane atalarınızın doğduğu köy bir yerdir ve on doğum olayında seçilir. Adını veya koordinatlarını düzeltirseniz, düzeltme her yerde geçerli olur.
- **Seçmeden önce oluştur.** Gramps Web'deki formlar, zaten var olan yerleri ve kaynakları seçer. Öncelikle **+** (Ekle) düğmesi ile yeni bir yer veya kaynak oluşturun.
- **Yerler iç içe geçmiş.** Bir yer, daha büyük bir yer tarafından kapsanabilir – bir köy bir ilçe tarafından, ilçe bir ülke tarafından – böylece her köy için tüm hiyerarşiyi tekrar etmek zorunda kalmazsınız.
- **Kaynaklar ve alıntılar ayrıdır.** Bir kaynak, kilise kaydının tamamıdır; bir alıntı, bir gerçeği destekleyen belirli bir giriş olup, sayfası, tarihi ve ona olan güveninizi içerir. Birçok alıntı aynı kaynağa işaret edebilir.

Eğer yanlışlıkla aynı yer veya kaynağı iki kez oluşturduysanız, [kopyaları birleştirebilirsiniz](lists.md#merge).

## Bir Nesnenin Sayfasını Düzenleme

Bir kaynak, depo veya medya nesnesinin sayfasında, düzenleme modunda başlığına tıklayarak onu değiştirebilirsiniz (bir medya nesnesi için, açıklamasını). Kaydetmek için Enter'a basın, ✓'ye tıklayın veya başka bir yere tıklayın; iptal etmek için Escape'e basın veya ✕'ye tıklayın.

Bir nesnenin sayfasındaki çoğu liste, onlara verdiğiniz sırayı korur; örneğin olaylar, isimler, nitelikler, adresler, alıntılar veya bir ailenin çocukları. Düzenleme modunda, bir satırı seçin ve yukarı ve aşağı düğmeleri ile hareket ettirin veya yeni konumuna sürükleyin: fare ile satıra basın ve hareket ettirin; dokunmatik ekranda, satıra basılı tutun ve kaldırın. Sürüklerken iptal etmek için Escape'e basın. Galerideki medyayı da aynı şekilde yeniden sıralayabilirsiniz, [Profil resimleri](media.md#profile-pictures) bölümüne bakın.

## Ana Kişi

Ana Kişi, aile ağacı grafiklerinin başladığı kişidir ve raporlar için varsayılan başlangıç noktasıdır. Bunu nasıl ayarlayacağınızı görmek için [İlk giriş](first-login.md) bölümüne bakın.

!!! not "Gramps Desktop'tan Farklı"
    Gramps Desktop'ta, Ana Kişi aile ağacı veritabanında saklanır, bu nedenle o veritabanını açan herkes için aynıdır. Gramps Web bunu kullanmaz. Bunun yerine, Ana Kişi tarayıcınızda, her ağaç için ayrı olarak saklanır: diğer kullanıcılarla paylaşılmaz ve farklı bir tarayıcıya veya cihaza geçmez. Gramps Desktop'tan bir ağaç içe aktardıktan sonra veya Gramps Web'i başka bir cihazda kullandığınızda, bunu tekrar ayarlamanız gerekir.

## Önerilen Sıra

Yeni bir aileyi elle girerken, bu sıra formlar arasında ileri geri gitmeyi önler:

1. **Yerler ve kaynaklar.** Gerekli yerleri oluşturun ve kaynakları kaydediyorsanız, üzerinde çalıştığınız kaynağı oluşturun.
2. **İnsanlar.** Doğum ve ölüm tarihleri ile yerleri olan insanları ekleyin. Bu, aile ağacı grafiğinin düzenleme modunda en hızlıdır; bu mod, aileleri sizin için oluşturur – [Yeni bir ağaç başlat](start-tree.md) ve [Aile ağacını düzenleme](tree-edit.md) bölümüne bakın.
3. **Diğer olaylar.** Evliliği eklemek için bir aileyi açın (örneğin, bir kişinin İlişkiler sekmesinden) ve diğer olayları eklemek için bir kişinin sayfasını açın.
4. **Alıntılar.** Bir kaynağın desteklediği kişi, olay veya diğer nesnenin Kaynak Alıntıları sekmesinde yeni bir alıntı ekleyin, kaynağı seçin ve sayfayı girin.
5. **Notlar ve medya.** Transkripsiyonları, fotoğrafları ve taramaları ekleyin – [Medya dosyaları ekle](media.md) bölümüne bakın.

## Tarih Girişi

Bir tarih, ayrı yıl, ay ve gün alanları olarak girilir; bu alanlar ayrıca bir tarih seçici kullanılarak da doldurulabilir. Bilmediğiniz kısımları atlayın: yalnızca bir yıl geçerli bir tarihtir. Kesin bir günü tahmin etmek yerine, alanların üzerindeki çiplerle tarihin türünü seçerek gerçekten bildiğiniz şeyi tanımlayın. Çiplerin altında bir ipucu, seçilen türü açıklar:

| Bildiğiniz | Tür | Örnek |
|---|---|---|
| Kesin tarih veya bir kısmı | Normal | 12 Mart 1850 veya sadece 1850 |
| Yaklaşık bir tarih | Hakkında | yaklaşık 1850 |
| Bir sınır | Önce, Sonra | 1900'den önce |
| Tarih bir dönem içinde bir yerde | Aralık | 1850 ile 1855 arasında (alanlar "En Erken" ve "En Geç") |
| Bir şey bir süre boyunca sürdü | Süre | 1850'den 1855'e kadar |

Bir Süre için, iki tarihten ("Başlangıç" ve "Bitiş") biri boş bırakılabilir, böylece "1850'den" veya "1855'e kadar" ifadesi yalnızca bir tarih ile bir Süre oluşturur.

**Kalite** ve **Takvim** alanları, bir tarih bunlardan birini kullandığında kendiliğinden açılan **Daha Fazla Seçenek** altında yer alır. Kalite, bir tarihe nasıl ulaştığınızı kaydeder: "Tahmini" bir tahmin için, "Hesaplanmış" diğer bilgilerden türetilen bir tarih için, örneğin ölümdeki yaşa göre hesaplanan bir doğum yılı.

!!! uyarı "Hakkında ve tahmini tarihler 50 yılı kapsar"
    Gramps tarihler arasında karşılaştırma yaptığında, "hakkında" türündeki bir tarihi – ve "Tahmini" kalitesine sahip herhangi bir tarihi – verilen tarihten 50 yıl öncesine kadar ve 50 yıl sonrasına kadar bir aralık olarak ele alır. Örneğin, 1840 ile 1860 arasında doğan kişiler için İnsanlar listesini filtrelemek, "yaklaşık 1880" doğumlu bir kişiyi de bulur, çünkü bu tarih 1830 ile 1930'u kapsar. Aynı şekilde, "önce" ve "sonra" da tarihten 50 yıl öncesine veya sonrasına kadar uzandığı kabul edilir.

    Bu, sürpriz sonuçlara yol açabilir, bu nedenle "hakkında" ve "Tahmini" terimlerini yalnızca tarihi daraltamadığınızda kullanın. Daha kısa bir dönem biliyorsanız, "1878 ile 1882 arasında" gibi bir Aralık daha kesin bir sonuç verir.

Takvim, orijinal kayıttaki kullanılan takvimde bir tarih girmenizi sağlar; örneğin, Julian takvimi gibi, bunu kendiniz dönüştürmek yerine.
