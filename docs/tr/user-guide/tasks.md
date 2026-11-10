# Yerleşik görev yönetimini kullanma

Gramps Web, yerleşik bir soyluk görev yönetim aracı içerir. Araştırmacıların görevlerini planlamalarına ve önceliklendirmelerine, ayrıca görevlerini belgelemelerine olanak tanımak için tasarlanmıştır. Bu nedenle görevler, Gramps veritabanında kaynaklar olarak temsil edilir. Bir görev tamamlandığında, ilişkili içerik araştırma sürecini belgeleyen bir kaynak olarak hizmet edebilir.

## Görev temelleri

Görevlerin aşağıdaki özellikleri vardır:

- Durum. Bu "Açık", "Devam Ediyor", "Engellendi" veya "Tamamlandı" olabilir.
- Öncelik. Bu "Düşük", "Orta" veya "Yüksek" olabilir.
- Etiketler. Etiketler, temel kaynağın normal Gramps etiketleridir. (Tüm görevlerin ayrıca görev olarak tanımlanmasını sağlamak için `ToDo` etiketine sahip olduğunu unutmayın, ancak bu etiket, karışıklığı önlemek için görev listesinde gizlidir.)
- Başlık. Görev listesinde gösterilir.
- Açıklama. Problemi tanımlamak için kullanılabilecek zengin metin alanı, ayrıca yapılan ilerlemeyi belgelemek için de kullanılabilir.
- Medya. Göreve eklenmiş herhangi bir medya dosyası.

## Görev oluşturma

Görevler normal Gramps nesneleri olduğundan, diğer nesneleri (insanlar veya olaylar gibi) düzenleyebilen veya oluşturabilen aynı kullanıcı grubu tarafından düzenlenebilir veya oluşturulabilir.

Bir görev oluşturmak için, görev listesi sayfasındaki + butonuna tıklayın. En az bir başlık girin ve isteğe bağlı olarak bir öncelik, açıklama, ekler ve etiketler ekleyin. Oluşturma sırasında durum her zaman "Açık" olacaktır.

## Görev listesi

Görev listesi, durumlarına göre sıralanmıştır - tamamlanan görevler en altta - ve her durum içinde önceliğe göre, en yüksekten en düşüğe.

Bir görevi açmak için üzerine tıklayın. Düzenleme izinlerine sahip kullanıcılar, bir görevin durum simgesine tıklayarak durumunu doğrudan listede değiştirebilir, örneğin tamamlandığını işaretlemek için.

Liste üzerindeki **filtre** butonu, görevleri etiketle, bir [GOQL](goql.md) ifadesiyle veya [gelişmiş filtre](lists.md#advanced-filter) ile filtreler.

## Görevi düzenleme

Görev sayfasının diğer Gramps nesneleri gibi ayrı bir "düzenleme modu" yoktur:

- Başlığı düzenlemek için üzerine tıklayın. Kaydetmek için Enter tuşuna basın, ✓'ye tıklayın veya başka bir yere tıklayın; iptal etmek için Escape tuşuna basın veya ✕'ye tıklayın.
- Durum ve öncelik değişiklikleri hemen uygulanır.
- Açıklamayı veya ekleri düzenlemek için, bölüm başlığının yanındaki düzenleme butonuna tıklayın. Açıklama, altında bulunan "kaydet" butonuyla kaydedilir; ekleri düzenleme **Tamamlandı** ile sona erer.
- Kilit butonu, görevin özel olup olmadığını ayarlar. Görevin açıklaması aynı gizliliği alır.

Düzenleme izinlerine sahip olmayan kullanıcılar, durumu ve önceliği metin olarak görür ve içeriği olmayan bölümler gizlenir.

Başlığın altında, editörler iki ek buton görür: **Kaynağı Düzenle**, görevi temsil eden kaynağı açar; burada diğer notlar, alıntılar ve nitelikler düzenlenebilir. **Sil**, bir onaydan sonra görevi siler ve görev listesine geri döner; görünen mesaj, görevi geri yüklemek için bir geri alma butonuna sahiptir.

## Görev özelliklerinin toplu değişimi

Düzenleme izinlerine sahip kullanıcılar, görev listesi her satırda bir onay kutusu görür. Görevleri seçin ve seçilen tüm görevleri bir kerede değiştirmek için listenin üstündeki **Önceliği Ayarla** veya **Durumu Ayarla** seçeneklerini kullanın.

## Gramps Masaüstünde Görevler

Gramps Web üzerinden görev eklerken, hem kaynaklar hem de notlar `ToDo` etiketi ile ilişkilendirilecektir, böylece görevler masaüstündeki [Yapılacak Notlar Grampleti](https://gramps-project.org/wiki/index.php/Addon:ToDoNotesGramplet) ve [Yapılacak Rapor](https://gramps-project.org/wiki/index.php/Addon:ToDoReport) içinde görünecektir.

Gramps Masaüstünde bir görevi eklemek veya düzenlemek için aşağıdaki yönergeleri kullanın:

- `ToDo` etiketi ile bir kaynak ekleyin ve görev başlığını başlık olarak kullanın.
- İsteğe bağlı olarak, `ToDo` etiketi ile kaynağa bir not ekleyin, "Yapılacak" yazın ve açıklamayı metin olarak ekleyin.
- "Durum" adında bir nitelik ekleyin ve "Açık", "Devam Ediyor", "Engellendi" veya "Tamamlandı" olarak ayarlayın.
- "Öncelik" adında bir nitelik ekleyin ve bunu düşük için 9, orta için 5 veya yüksek için 1 olarak ayarlayın (bu sezgisel olmayan değerler iCalendar spesifikasyonundan alınmıştır).
