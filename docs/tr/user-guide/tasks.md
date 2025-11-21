# Yerleşik görev yönetimini kullanma

Gramps Web, yerleşik bir soybilimsel görev yönetim aracı içerir. Bu, araştırmacıların görevlerini planlamalarına ve önceliklendirmelerine, ayrıca belgelerle desteklemelerine olanak tanımak için tasarlanmıştır. Bu nedenle görevler, Gramps veritabanında kaynaklar olarak temsil edilmektedir. Bir görev tamamlandığında, ilişkili içerik araştırma sürecini belgeleyen bir kaynak olarak hizmet edebilir.

## Görev temelleri

Görevlerin aşağıdaki özellikleri vardır:

- Durum. Bu "Açık", "Devam Ediyor", "Engellendi" veya "Tamamlandı" olabilir
- Öncelik. Bu "Düşük", "Orta" veya "Yüksek" olabilir
- Etiketler. Etiketler, temel kaynağın normal Gramps etiketleridir. (Tüm görevlerin ayrıca görev olarak tanımlanması için `ToDo` etiketine sahip olduğunu unutmayın, ancak bu etiket, karmaşayı önlemek için görev listesinde gizlidir.)
- Başlık. Görev listesinde gösterilir
- Açıklama. Problem ifadesini tanımlamak için kullanılabilecek zengin metin alanı, ayrıca yapılan ilerlemeyi belgelemek için de kullanılabilir
- Medya. Göreve eklenmiş herhangi bir medya dosyası

## Görev oluşturma

Görevler normal Gramps nesneleri olduğundan, diğer nesneleri (kişiler veya olaylar gibi) düzenleyebilen veya oluşturabilen aynı kullanıcı grubu tarafından düzenlenebilir veya oluşturulabilir.

Bir görev oluşturmak için, görev listesi sayfasındaki + düğmesine tıklayın. En az bir başlık girin. Oluşturulduğunda durum her zaman "Açık" olacaktır.

## Görevi düzenleme

Görev detaylarından herhangi birine erişmek için, görev listesinde üzerine tıklayın.

Görev detay sayfasının diğer Gramps nesneleri gibi ayrı bir "düzenleme modu" yoktur. Başlık, durum ve öncelik üzerindeki değişiklikler hemen uygulanır. Zengin metin açıklamasındaki değişiklikler, altında bulunan "kaydet" düğmesine tıklamayı gerektirir.

## Görev özelliklerinin toplu olarak değiştirilmesi

Görevlerin öncelik ve durumu, görev listesinde seçim için onay kutularını kullanarak ve görev listesinin üstündeki uygun düğmeleri kullanarak topluca değiştirilebilir.

## Gramps Masaüstünde Görevler

Gramps Web üzerinden görev eklerken, hem kaynaklar hem de notlar `ToDo` etiketi ile ilişkilendirilecektir, bu nedenle görevler masaüstündeki [Yapılacak Notlar Grampleti](https://gramps-project.org/wiki/index.php/Addon:ToDoNotesGramplet) ve [Yapılacak Raporu](https://gramps-project.org/wiki/index.php/Addon:ToDoReport) içinde görünecektir.

Gramps Masaüstünde bir görev eklemek veya düzenlemek için aşağıdaki kılavuzları kullanın:

- `ToDo` etiketi ile bir kaynak ekleyin ve görev başlığını başlık olarak kullanın
- İsteğe bağlı olarak, `ToDo` etiketi ile kaynağa bir not ekleyin, "Yapılacak" yazın ve açıklamayı metin olarak ekleyin
- "Durum" adında bir özellik ekleyin ve bunu "Açık", "Devam Ediyor", "Engellendi" veya "Tamamlandı" olarak ayarlayın
- "Öncelik" adında bir özellik ekleyin ve bunu düşük için 9, orta için 5 veya yüksek için 1 olarak ayarlayın (bu sezgisel olmayan değerler iCalendar spesifikasyonundan alınmıştır)
