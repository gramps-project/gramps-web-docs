# Gramps Web ile Y-DNA Analizi Yapma

!!! note "Not"
    Bu özellik, Gramps Web API sürüm 3.3.0 veya daha yenisi ve Gramps Web ön yüzü sürüm 25.9.0 veya daha yenisini gerektirir.

Gramps Web'deki Y-DNA görünümü, bir kişinin en olası Y-DNA haplogrubunu belirlemek ve türetilmiş ataları insan Y kromozomu ağacında zaman tahminleri ile birlikte görüntülemek için ham Y kromozomu tek nükleotid polimorfizmi (SNP) verilerini kullanabilir.

## Y-DNA SNP verilerini nasıl elde edilir ve saklanır

Y-DNA SNP verilerini elde etmek için, bir genetik test hizmeti aracılığıyla Y-DNA testi yaptırmanız gerekir. Sonuç, her biri bir dizi mutasyon (SNP) olarak temsil edilir; her biri bir dize (örneğin, `R-BY44535`) ile tanımlanır ve mutasyonun mevcut olup olmadığını gösteren bir `+` veya `-` işareti içerir. Gramps Web, tüm test edilen SNP'lerin dizesinin `SNP1+, SNP2-, SNP3+,...` formatında, özel türde bir kişi niteliği olan `Y-DNA` (büyük/küçük harf duyarlı) olarak saklanmasını bekler. Bu niteliği Gramps Web veya Gramps Desktop'ta manuel olarak oluşturabilir veya Gramps Web'deki Y-DNA görünümüne gidip mavi "Ekle" butonuna tıklayarak verileri eklemek istediğiniz kişiyi seçip SNP dizesini yapıştırabilirsiniz. Her durumda, veriler Gramps veritabanınızdaki bir kişi niteliği olarak saklanacaktır.

Çeşitli test hizmetlerinden SNP verilerini elde etme talimatları için [aşağıya bakın](#instructions-for-obtaining-snp-data-from-testing-services).

## Nasıl çalışır

Bir kişinin SNP verilerini içeren bir `Y-DNA` niteliği olduğunda, Gramps Web, kişinin insan Y kromozomu ağacındaki en olası konumunu belirlemek için açık kaynaklı [yclade](https://github.com/DavidMStraub/yclade) Python kütüphanesini kullanacaktır. Ağaç, on binlerce Y-DNA testine dayanarak [YFull](https://www.yfull.com/) projesi tarafından oluşturulmuştur. Gramps Web'in YFull ağacının yerel bir kopyasını kullandığını ve bu nedenle hiçbir verinin üçüncü taraflara gönderilmediğini unutmayın.

Ağaç, kökten yapraklara doğru geçilir ve her düğümde, o düğümle ilişkili SNP'ler kişinin pozitif ve negatif olarak test edilen SNP'leri ile karşılaştırılır ve uygun dal takip edilir.

Sonuç, ağacın kökünden (Y kromozomal "Adam" ([Y-chromosomal "Adam"](https://en.wikipedia.org/wiki/Y-chromosomal_Adam))) kişinin SNP verileri ile tutarlı en türetilmiş kladın bulunduğu yere kadar bir klad dizisidir. Her klad, o klada ait YFull veritabanındaki örneklerin yaşlarına dayanan tahmini bir yaşa sahiptir.

Y kromozomları babadan oğula miras alındığından, bu ardışıklık kişinin patrilineal soyunun bir kesitine karşılık gelir.

## Sonuçları nasıl yorumlayabilirsiniz

En önemli bilgi, sayfanın üst kısmında gösterilen kişinin en olası haplogrubudur. İsim, o haplogrupa ait test edilen örneklerin köken ülkesinin yanı sıra daha fazla bilgi içeren [YFull](https://www.yfull.com/) web sitesindeki ilgili sayfaya bağlantılıdır.

Gramps Web'de gösterilen patrilineal ata ağacında, test edilen kişinin hemen üzerindeki kutu, kişinin haplogrubuna ait tüm test edilen örneklerin en son ortak atasıdır (MRCA). Bu ata için gösterilen tarih, tahmini doğum tarihidir. Onun üzerindeki ata, bu haplogrubun tanımlayıcı mutasyonunun ilk ortaya çıktığı atadır.

Y kromozomlarının yavaş mutasyon oranı nedeniyle, MRCA geçmişte yüzlerce yıl öncesine gidebilir. Nadir haplogruplar (yani, şimdiye kadar az sayıda insanın test edildiği haplogruplar) için bu, binlerce yıl bile olabilir.

MRCA ile test edilen kişi arasında, grafik, ağacınızdaki belgelenmiş olduğu kadar babasal hattı gösterir: baba, onun babası ve devam eder, en yaşlıdan en gence. En yaşlı belgelenmiş atanın üzerindeki kesik çizgi, belgelenmemiş nesilleri temsil eder ve sayı tahmini ile birlikte gelir. Sadece biyolojik babalar takip edilir – hat, evlat edinilmiş bir baba veya üvey baba ile durur, çünkü Y kromozomunu aktarmamışlardır. Hattaki bir kişiye tıklayarak onların sayfasını açabilirsiniz.

Her klad kutusundaki simge, o kladı YFull web sitesinde açar.

## Özel Y-DNA verileri

Y-DNA verilerini ekleme ve düzenleme diyaloglarında bir **Özel** anahtarı vardır. Özel Y-DNA verileri, özel kayıtları görüntüleyemeyen kullanıcılardan gizlenir. [Özel kayıtlar](privacy.md) için bakın.

## Test hizmetlerinden SNP verilerini elde etme talimatları

### [YSEQ](https://www.yseq.net/)

"Benim Hesabım" kısmına giriş yaptıktan sonra, "Sonuçlarım / Allele'lerimi Görüntüle" kısmına gidin ve sayfanın en altına inin. "Allele list compact" metin alanı, Gramps Web için özel olarak eklenmiştir ve `Y-DNA` niteliğine yapıştırmak için tam olarak doğru formatta bulunmaktadır.
