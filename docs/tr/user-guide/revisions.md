# Revizyon Geçmişi

Revizyon geçmişi görünümü, aile ağacında yapılan tüm düzenlemeleri gösterir.

Liste görünümü, düzenlemeleri "işlemler" olarak gruplandırılmış şekilde gösterir. Bir işlem, Gramps nesnelerine yapılan bir veya daha fazla ekleme, silme veya değişiklik grubudur. Örneğin, iki mevcut kişinin baba ve anne olarak yer aldığı yeni bir ailenin eklenmesi, bir eklenen aile nesnesi ve iki değiştirilen kişi nesnesi ile bir işlem oluşturur (çünkü bu nesneler yeni aile nesnesine bağlantıyı içerir).

Bir işleme tıkladığınızda, işlem detay görünümü açılır. Bu görünüm, Gramps nesnesine göre bireysel eklemelerin, silmelerin ve güncellemelerin listesini içerir.

Bireysel bir değişikliği seçmek, eklemelerin yeşil ve silmelerin kırmızı ile vurgulandığı Gramps nesnesinin ham JSON temsilinin bir görünümünü açar. Farklılıkların üzerinde bulunan bir düğme, sizi doğrudan nesnenin kendi sayfasına götürür.

## Tek bir nesnenin revizyonları

Belirli bir kişi, aile, olay veya diğer nesnelerin geçmişini görmek için, sayfasını açın ve **Revizyonlar** sekmesine geçin. Bu sekme, o nesneye yapılan her değişikliği, en yenisi en üstte olacak şekilde, değişiklik türü (eklenmiş, güncellenmiş veya silinmiş), değişikliği yapan kullanıcı ve zaman bilgisi ile listeler. Bir girişe tıkladığınızda, ait olduğu işlemi açar; burada farkı inceleyebilir veya geri alabilirsiniz.

Eski girişleri yüklemek için **Daha fazla göster** butonuna tıklayın; çok uzun bir geçmişe sahip nesneler için yalnızca en son revizyonlar gösterilir. Revizyon geçmişinin kaydedilmesinden önce son değişikliği yapılan nesneler için, sekme yalnızca son değişiklik zamanını gösterir.

!!! not
    Revizyonlar sekmesi, üyeler ve üstü için görünürdür ve Gramps Web API sürümü 3.22 veya daha yenisini gerektirir.

## Bir revizyonu geri alma

İşlem detay sayfasında, bir işlemi geri almanıza olanak tanıyan bir **Geri Al** düğmesi bulunur. Bu düğmeye tıkladığınızda, geri almanın temiz bir şekilde yapılıp yapılamayacağı kontrol edilir.

**Temiz geri alma** – eğer işlemden etkilenen nesnelerden hiçbiri o zamandan beri değiştirilmemişse, geri alma risksiz bir şekilde devam edebilir. Bir onay penceresi gösterilir ve **Geri Al** butonuna tıklamak işlemi geri alır.

**Zorunlu geri alma** – eğer bir veya daha fazla etkilenen nesne sonraki bir işlemle değiştirilmişse, temiz bir geri alma mümkün değildir. Pencere, geri almanın zorlanmasının veri tutarsızlıklarına yol açabileceği konusunda uyarır; çünkü söz konusu nesnelere bağlı sonraki değişiklikler, temel nesneler geri alınsa bile olduğu gibi korunacaktır. Bu durumda, geri almayı iptal edebilir veya yine de devam etmek için **Zorla geri al** butonuna tıklayabilirsiniz.

Her iki durumda da geri alma, bir arka plan görevi olarak çalışır ve bir ilerleme göstergesi gösterilir.
