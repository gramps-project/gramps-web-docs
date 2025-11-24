# Gramps Web ile Y-DNA Analizi Yapma

!!! note "Not"
    Bu özellik, Gramps Web API sürüm 3.3.0 veya daha yenisi ve Gramps Web ön yüzü sürüm 25.9.0 veya daha yenisi gerektirir.

Gramps Web'deki Y-DNA görünümü, bir kişinin en olası Y-DNA haplogrubunu belirlemek ve türetilmiş ataları insan Y kromozomu ağacında zaman tahminleri ile birlikte görüntülemek için ham Y kromozomu tek nükleotid polimorfizmi (SNP) verilerini kullanabilir.

## Y-DNA SNP verilerini nasıl elde edilir ve saklanır

Y-DNA SNP verilerini elde etmek için, bir genetik test hizmeti aracılığıyla Y-DNA testi yaptırmanız gerekir. Sonuç, her biri bir dize (örneğin, `R-BY44535`) ile tanımlanan ve mutasyonun mevcut olup olmadığını gösteren bir `+` veya `-` işareti ile temsil edilen bir dizi mutasyon (SNP) olarak gösterilir. Gramps Web, tüm test edilen SNP'lerin dizisini `SNP1+, SNP2-, SNP3+,...` formatında, `Y-DNA` özel türünde bir kişi niteliğinde saklamayı bekler (büyük/küçük harf duyarlıdır). Bu niteliği Gramps Web veya Gramps Desktop'ta manuel olarak oluşturabilir veya Gramps Web'deki Y-DNA görünümüne gidip mavi "Ekle" butonuna tıklayarak verileri eklemek istediğiniz kişiyi seçip SNP dizisini yapıştırabilirsiniz. Her durumda, veriler Gramps veritabanınızdaki bir kişi niteliği olarak saklanacaktır.

Çeşitli test hizmetlerinden SNP verilerini elde etme talimatları için [aşağıya bakın](#instructions-for-obtaining-snp-data-from-testing-services).

## Nasıl çalışır

Bir kişinin SNP verilerini içeren bir `Y-DNA` niteliği olduğunda, Gramps Web, kişinin insan Y kromozomu ağacındaki en olası konumunu belirlemek için açık kaynak [yclade](https://github.com/DavidMStraub/yclade) Python kütüphanesini kullanacaktır. Ağaç, Y-DNA testlerinin on binlerce örneğine dayanan [YFull](https://www.yfull.com/) projesi tarafından oluşturulmuştur. Gramps Web'in YFull ağacının yerel bir kopyasını kullandığını unutmayın, bu nedenle hiçbir veri üçüncü taraflara gönderilmez.

Ağaç, kökten yapraklara doğru geçilir ve her düğümde, o düğümle ilişkili SNP'ler kişinin pozitif ve negatif olarak test edilen SNP'leri ile karşılaştırılır ve uygun dal takip edilir.

Sonuç, ağacın kökünden (Y kromozomal "Adam" ([Y-chromosomal "Adam"](https://en.wikipedia.org/wiki/Y-chromosomal_Adam))) kişinin SNP verileriyle tutarlı en türetilmiş kladın bulunduğu yere kadar bir klad sıralamasıdır. Her klad, o klada ait YFull veritabanındaki örneklerin yaşlarına dayanan bir tahmini yaşa sahiptir.

Y kromozomları babadan oğula miras alındığı için, bu sıralama kişinin patrilineal soyunun bir kesitine karşılık gelir.

## Sonuçları nasıl yorumlayabilirsiniz

En önemli bilgi, sayfanın üst kısmında gösterilen kişinin en olası haplogrubudur. İsim, o haplogrupa ait test edilen örneklerin köken ülkesi gibi daha fazla bilgi içeren [YFull](https://www.yfull.com/) web sitesindeki ilgili sayfaya bağlanmaktadır.

Gramps Web'de gösterilen patrineal atalar ağacında, test edilen kişinin hemen üzerindeki kutu, kişinin haplogrubuna ait tüm test edilen örneklerin en son ortak atasıdır (MRCA). Bu ata için gösterilen tarih, tahmini doğum tarihidir. Onun üzerindeki ata, bu haplogrubun tanımlayıcı mutasyonunun ilk kez ortaya çıktığı atadır.

Y kromozomlarının yavaş mutasyon oranı nedeniyle, MRCA geçmişte yüzlerce yıl öncesine dayanabilir. Nadir haplogruplar (yani, şimdiye kadar çok az kişinin test edildiği haplogruplar) için bu, binlerce yıl bile olabilir.

## Test hizmetlerinden SNP verilerini elde etme talimatları

### [YSEQ](https://www.yseq.net/)

"Benim Hesabım" kısmına giriş yaptıktan sonra, "Sonuçlarım / Allele'lerimi Görüntüle" seçeneğine gidin ve sayfanın en altına inin. "Allele list compact" metin alanı, Gramps Web için özel olarak eklenmiştir ve `Y-DNA` niteliğine yapıştırmak için tam olarak doğru formatta bulunmaktadır.
