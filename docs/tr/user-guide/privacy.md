# Özel kayıtlar

Ağaçtaki herhangi bir kayıt özel olarak işaretlenebilir. Bu, [kullanıcı rolleri](../install_setup/users.md#user-roles) ile birlikte, kimin neyi göreceğini belirler.

## Kimin neyi görebileceği

Gramps Web asla halka açık değildir: yalnızca bir hesabı olan kullanıcılar bir şey görebilir. Gramps'ta "Halka açık" terimi, "özel değil" anlamına gelir; yani, ağaca giriş yapmış her kullanıcı tarafından görülebilir.

| Rol | Halka açık kayıtlar | Özel kayıtlar |
|---|---|---|
| Misafir | görüntüle | – |
| Üye | görüntüle | görüntüle |
| Katkıda Bulunan | görüntüle, ekle | görüntüle, ekle |
| Editör, Sahip, Yönetici | görüntüle, ekle, düzenle, sil | görüntüle, ekle, düzenle, sil |

Misafirler için özel kayıtlar mevcut değildir: sayfalardan, listelerden, arama sonuçlarından, grafiklerden, raporlardan, dışa aktarımlardan ve AI asistanı yanıtlarından çıkarılır. Bu, sunucunun veritabanını okuduğu yerlerde zorunludur, uygulamada bir şeyleri gizlemekle değil, bu nedenle bir misafir başka bir şekilde özel verilere ulaşamaz.

Henüz onaylanmamış hesaplar ([kendiliğinden kayıt](registration.md)) hiç giriş yapamaz.

Bu nedenle, akrabalar veya misafir hesabına sahip diğer kişilerin belirli bilgileri görmemesi gerekiyorsa, bunu özel olarak işaretleyin. Eğer bir ağacın tüm kullanıcıları her şeyi görebiliyorsa, onlara üye rolü (veya daha yüksek) verin ve hiçbir şeyi özel olarak işaretlemenize gerek kalmaz.

## Canlı insanlar otomatik olarak özel değildir

Hiçbir şey otomatik olarak özel yapılmaz – hatta hâlâ yaşayan insanlar bile. Canlı insanların verileri, özel olarak işaretlenene kadar misafirlere görünür. Bu, içe aktarılan ağaçlar için de geçerlidir.

Gramps Web'de muhtemelen yaşayan kişileri özel yapmak için:

1. Kişi listesinde, [gelişmiş filtreyi](lists.md#advanced-filter) açın ve "Muhtemelen yaşayan insanlar" koşulunu ekleyin (bugün için tarihi boş bırakın). Filtreyi uygulayın.
2. **Seç** butonuna tıklayın, başlıktaki onay kutusunu işaretleyin ve **Tümünü Seç** seçeneğini seçin.
3. **Gizlilik** eylemini seçin ve kayıtları özel olarak işaretleyin.

"Muhtemelen yaşayan" durumu, kişinin ve akrabalarının tarihlerinden tahmin edilir. Kullanılabilir tarihi olmayan kişiler, yaşayan olarak kabul edilir. Sonucu kontrol edin ve verileri ekledikçe tahminin değişebileceğini unutmayın.

Bir kişiyi özel olarak işaretlemek, kişiyi gizler, ancak olaylarını, notlarını, medyasını veya ailelerini gizlemez – aşağıya bakın. Gramps Desktop, birçok ilgili kaydın gizliliğini aynı anda ayarlamak için daha fazla araca sahiptir; bunları [Sync eklentisi](../administration/sync.md) ile kullanabilirsiniz.

Daha sonra ölen kişiler de otomatik olarak halka açık hale gelmez. Bunu isteyip istemediğiniz size kalmış – birçok araştırmacı, toplanan bilgileri bir süre özel tutmayı tercih eder.

## Kilit simgelerini okuma

Özel verileri görüntüleyebilen kullanıcılar, özel öğelerin yanında bir kilit görür. İki tür vardır:

- **Dolu kilit** – kayıt kendisi özeldir. Örneğin, bir kişinin sayfasında, bir olayın yanında dolu bir kilit, olayın özel olduğunu; bir çocuğun yanında ise çocuğun özel olduğunu gösterir.
- **Çizgi kilit** – yalnızca *bağlantı* özeldir, gittiği kayıt değil. Örneğin, bir kişinin bir olaya bağlantısı özel olabilirken, olayın kendisi halka açık olabilir. Olay, o kişinin sayfasından gizlenir ancak diğer katılımcıların sayfalarında veya olay listesinde hâlâ görünür.

Eğer hem kayıt hem de bağlantısı özel ise, dolu kilit gösterilir.

Aynı ayrım çocuklar (çocuk veya çocuğun aileye bağlantısı), dernekler, bir kaynağın depo bağlantıları ve bir galerideki medya için de geçerlidir. İsimler, nitelikler, adresler ve URL'ler kendi kayıtlarına aittir ve yalnızca dolu kilide sahiptir.

## Bir şeyi özel yapmak

Gizliliği değiştirmek için düzenleme izinlerine ihtiyacınız var.

- **Bir bütün kayıt**: sayfasını açın, düzenleme moduna geçin ve araç çubuğundaki kilit butonuna tıklayın.
- **Bir kaydın bir kısmı** – alternatif bir isim, nitelik, adres, URL, dernek, çocuk bağlantısı veya depo bağlantısı: o öğenin düzenleme penceresini açın ve **Özel** anahtarını açın. Birincil isimde anahtar yoktur, çünkü aksi takdirde kişi "Özel" olarak görünür.
- **Bir kişinin veya ailenin sayfasından bir olay**: olayın düzenleme penceresinde olayın kendisi için bir gizlilik anahtarı vardır. Olay başka kişilerle paylaşıldıysa, yalnızca **Herkes için Düzenle** sonrasında düzenlenebilir, çünkü tümü için özel durumdadır.
- **Bir kişinin bir olaya bağlantısı**: olay sayfasında, katılımcının satırını düzenleme modunda açın. Oradaki gizlilik anahtarı yalnızca o katılımcının bağlantısına uygulanır, bu nedenle olay diğer katılımcılar için görünür kalır.
- **Bir galerideki medya nesnesi**: düzenleme modunda, karenin köşesindeki kilide tıklayın.
- **Birden fazla kaydı aynı anda**: bir listede seçin ve **Gizlilik** eylemini kullanın, bkz. [Listeler](lists.md#tags-and-privacy).

Bir listede hangi kayıtların özel olduğunu kontrol etmek için, listenin sütun seçicisinde **Gizlilik** sütununu açın.

## Dikkat edilmesi gerekenler

- Bir kaydı özel yapmak, bağlantılı olduğu kayıtları özel yapmaz. Eğer bir kişi özel ise, olayları, ait olduğu aileler ve onlara ekli notlar hâlâ görünür, aksi takdirde özel olmaları gerekir. İlgili kayıtları kontrol etmek için gelişmiş filtreyi veya **Gizlilik** sütununu kullanın.
- Bir aileyi veya olayı özel yapmak, onu gizler, ancak içindeki kişileri gizlemez.
- [DNA eşleşmeleri ve Y-DNA verileri](dna-matches.md#private-matches) kendi **Özel** anahtarına sahiptir.
- Özel verileri görüntüleyemeyen bir kullanıcı tarafından yapılan dışa aktarımlar ve medya arşivleri, özel kayıtlar veya dosyalar içermez.
- Gizlilik, Gramps'ın bir özelliğidir, bu nedenle Gramps Desktop'ta özel olarak işaretlenmiş kayıtlar Gramps Web'de de özeldir ve tersine.
