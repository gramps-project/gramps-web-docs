# Yerleşik görev yönetimini kullanma

Gramps Web, yerleşik bir soybilimsel görev yönetim aracı içerir. Bu, araştırmacıların görevlerini planlamalarına ve önceliklendirmelerine, ayrıca belgelerini tutmalarına olanak tanımak amacıyla tasarlanmıştır. Bu nedenle görevler, Gramps veritabanında kaynaklar olarak temsil edilir. Bir görev tamamlandığında, ilişkili içerik araştırma sürecini belgeleyen bir kaynak olarak hizmet edebilir.

## Görev temelleri

Görevlerin aşağıdaki özellikleri vardır:

- Durum. Bu "Açık", "Devam Ediyor", "Engellenmiş" veya "Tamamlandı" olabilir
- Öncelik. Bu "Düşük", "Orta" veya "Yüksek" olabilir
- Etiketler. Etiketler, temel kaynağın normal Gramps etiketleridir. (Tüm görevlerin ayrıca görev olarak tanımlanması için `ToDo` etiketi vardır, ancak bu etiket görev listesindeki karmaşayı önlemek için gizlidir.)
- Başlık. Görev listesinde gösterilir
- Açıklama. Problem ifadesini tanımlamak için kullanılabilecek zengin metin alanı, ayrıca yapılan ilerlemeyi belgelemek için de kullanılabilir
- Medya. Göreve eklenmiş herhangi bir medya dosyası

## Görev oluşturma

Görevler normal Gramps nesneleri olduğundan, diğer nesneleri (insanlar veya olaylar gibi) düzenleyebilen veya oluşturabilen aynı kullanıcı grubu tarafından düzenlenebilir veya oluşturulabilir.

Bir görev oluşturmak için, görev listesi sayfasındaki + butonuna tıklayın. En az bir başlık girin. Oluşturma sırasında durum her zaman "Açık" olacaktır.

## Görevi düzenleme

Görevin herhangi bir detayına tıklayarak görev listesindeki detay sayfasına gidin.

Görev detay sayfasının, diğer Gramps nesneleri gibi ayrı bir "düzenleme modu" yoktur. Başlık, durum ve öncelik üzerindeki değişiklikler hemen uygulanır. Zengin metin açıklamasındaki değişiklikler, altında bulunan "kaydet" butonuna tıklamayı gerektirir.

## Görev özelliklerinin toplu değişimi

Görevlerin öncelik ve durumu, görev listesindeki seçim için onay kutularını kullanarak ve görev listesinin üstündeki uygun butonları kullanarak toplu olarak değiştirilebilir.

## Gramps Masaüstünde Görevler

Gramps Web aracılığıyla görev eklerken, hem kaynaklar hem de notlar `ToDo` etiketi ile ilişkilendirilecektir, bu nedenle görevler masaüstündeki [Yapılacak Notlar Grampleti](https://gramps-project.org/wiki/index.php/Addon:ToDoNotesGramplet) ve [Yapılacak Raporu](https://gramps-project.org/wiki/index.php/Addon:ToDoReport) içinde görünecektir.

Gramps Masaüstünde bir görev eklemek veya düzenlemek için aşağıdaki yönergeleri kullanın:

- `ToDo` etiketi ile bir kaynak ekleyin ve görev başlığını başlık olarak kullanın
- İsteğe bağlı olarak, `ToDo` etiketi ile bir not ekleyin, "Yapılacak" yazın ve açıklamayı metin olarak ekleyin
- "Durum" adında bir nitelik ekleyin ve bunu "Açık", "Devam Ediyor", "Engellenmiş" veya "Tamamlandı" olarak ayarlayın
- "Öncelik" adında bir nitelik ekleyin ve bunu düşük için 9, orta için 5 veya yüksek için 1 olarak ayarlayın (bu sezgisel olmayan değerler iCalendar spesifikasyonundan alınmıştır)
