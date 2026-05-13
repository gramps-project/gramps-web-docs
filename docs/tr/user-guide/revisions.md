# Revizyon Geçmişi

Revizyon geçmişi görünümü, aile ağacında yapılan tüm düzenlemeleri gösterir.

Liste görünümü, düzenlemeleri "işlemler" tarafından gruplandırılmış olarak gösterir. Bir işlem, Gramps nesnelerine yapılan bir veya daha fazla ekleme, silme veya değişiklik grubudur. Örneğin, iki mevcut kişi (baba ve anne) ile yeni bir aile eklemek, bir eklenmiş aile nesnesi ve iki değiştirilmiş kişi nesnesi ile bir işlem oluşturur (çünkü bunlar yeni aile nesnesine bağlantıyı içerir).

Bir işleme tıkladığınızda, işlem detay görünümü açılır. Bu görünüm, Gramps nesnesine göre bireysel eklemelerin, silmelerin ve güncellemelerin listesini içerir.

Bireysel bir değişikliği seçmek, eklemeler ve silmelerin sırasıyla yeşil ve kırmızı renkte vurgulandığı Gramps nesnesinin ham JSON temsilinin bir görünümünü açar.

## Bir revizyonu geri alma

İşlem detay sayfasında, bir **Geri Al** butonu, o işlemi geri almanıza olanak tanır. Üzerine tıkladığınızda, geri almanın temiz bir şekilde yapılıp yapılamayacağını kontrol eder.

**Temiz geri alma** – eğer işlemden etkilenen nesnelerden hiçbiri o zamandan beri değiştirilmemişse, geri alma riske girmeden devam edebilir. Bir onay penceresi gösterilir ve **Geri Al** butonuna tıklamak işlemi geri alır.

**Zorunlu güç** – eğer bir veya daha fazla etkilenen nesne, sonraki bir işlem tarafından değiştirilmişse, temiz bir geri alma mümkün değildir. Pencere, geri almanın zorlanmasının veri tutarsızlıklarına yol açabileceğini uyarır, çünkü söz konusu nesnelere bağlı sonraki değişiklikler olduğu gibi korunacak, oysa temel nesneler geri alınacaktır. Bu durumda ya iptal edebilir ya da yine de devam etmek için **Zorla geri al** butonuna tıklayabilirsiniz.

Her iki durumda da geri alma arka planda bir görev olarak çalışır ve bir ilerleme göstergesi gösterilir.
