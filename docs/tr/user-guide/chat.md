# AI sohbeti kullanma

!!! bilgi
    AI sohbeti, Gramps Web API sürüm 2.5.0 veya daha yüksek ve Gramps Web sürüm 24.10.0 veya daha yüksek gerektirir.

Gramps Web'deki sohbet görünümü (kurulumunuzda mevcutsa), aile ağacınızla ilgili soruları yanıtlayabilen bir AI asistanına erişim sağlar.

!!! uyarı
    Bu hala yeni ve gelişen bir özellik olduğundan, bazı soru türleri iyi çalışırken diğerleri çalışmayabilir. Ayrıca, herhangi bir AI asistanında olduğu gibi, gerçek olarak yanlış yanıtlar verebilir, bu yüzden her zaman iki kez kontrol ettiğinizden emin olun.

## Nasıl çalışır

Asistanın hangi tür soruları yanıtlayabileceğini anlamak için, aşağıda nasıl çalıştığını anlamak faydalıdır:

1. Kullanıcı bir soru sorar.
2. Gramps Web, sorunun yanıtını içerebilecek (örneğin, on) Gramps nesnesini belirler. Bu amaçla, "anlamsal arama" adı verilen bir teknik kullanır. Örneğin, "John Doe'nun çocuklarının adı nedir?" diye sorarsanız, John Doe'nun baba olduğu bir aile varsa, muhtemelen en üst sonuçlar arasında yer alır.
3. Gramps Web, kullanıcı sorusunu ve alınan bağlam bilgilerini büyük bir dil modeline ("sohbet botu") iletir ve doğru yanıtı çıkarmasını ister.
4. Yanıt kullanıcıya gösterilir.

## Nasıl soru sorulur

Sohbetin çalışma şekli nedeniyle, AI asistanının ebeveynler veya çocuklar dışındaki belirli ilişkiler hakkında soruları yanıtlaması (şu anda) mümkün değildir, bu bilgi bir notta metin olarak yer almadıkça.

Her yanıt, sınırlı sayıda en iyi anlamsal arama sonuçlarına dayandığından, istatistikler hakkında ("veritabanımda kaç kişi var ...") soruları da yanıtlayamaz.

Belirsizlikleri ve yanlış anlamaları önlemek için, soruyu mümkün olduğunca ayrıntılı bir şekilde formüle etmek faydalıdır.

Büyük dil modellerinin çok dilli olduğunu unutmayın, bu nedenle kendi dilinizde onunla konuşabilirsiniz ve o da aynı dilde yanıt verecektir.

!!! ipucu
    Lütfen toplulukla işe yarayan ve yaramayan şeyler hakkında deneyimlerinizi paylaşın.
