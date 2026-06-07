# AI Asistanını Kullanma

!!! info
    AI Asistanı, Gramps Web API sürüm 2.5.0 veya daha yüksek ve Gramps Web sürüm 24.10.0 veya daha yüksek gerektirir. Gramps Web API sürüm 3.6.0, daha akıllı etkileşimler için araç çağırma yeteneklerini tanıttı.

**Asistan** görünümü Gramps Web'de (kurulumunuzda mevcutsa, eski sürümlerde "Sohbet" olarak etiketlenmiştir) aile ağacınızla ilgili soruları yanıtlayabilen bir AI asistanına erişim sağlar.

!!! warning
    Bu hala yeni ve gelişen bir özellik olduğundan, bazı soru türleri iyi çalışırken diğerleri çalışmayabilir. Ayrıca, herhangi bir AI asistanında olduğu gibi, doğru olmayan yanıtlar verebilir, bu yüzden her zaman iki kez kontrol ettiğinizden emin olun.

## Nasıl çalışır

Asistanın hangi tür soruları yanıtlayabileceğini anlamak için, nasıl çalıştığını anlamak faydalıdır:

1. Kullanıcı bir soru sorar.
2. AI asistanı yanıtları bulmak için birden fazla yaklaşım kullanabilir:
   - **Anlamsal Arama**: Gramps Web, aile ağacınızdaki ilgili bilgileri içermesi muhtemel nesneleri tanımlar. Örneğin, "John Doe'nun çocuklarının adı nedir?" diye sorarsanız, John Doe'nun baba olduğu aileler en üst sonuçlar arasında yer alır.
   - **Araç Çağırma (Gramps Web API v3.6.0+)**: Asistan, belirli kriterlere göre insanları/olayları/aileleri/yerleri aramak, filtrelemek, bireyler arasındaki ilişkileri hesaplamak ve ayrıntılı bilgi almak için özel araçlar kullanarak doğrudan veritabanınızı sorgulayabilir.
3. Gramps Web, soruyu ve alınan bilgileri büyük bir dil modeline ileterek bir yanıt oluşturur.
4. Yanıt size gösterilir.

Asistan çalışırken, hangi araçları kullandığını gösteren göstergeler vardır (örneğin, insanları arama, ilişkileri kontrol etme) böylece yanıtını oluştururken onu takip edebilirsiniz. Uzun süren sorular arka plan görevleri olarak işlenir – uzaklaşabilir ve geri dönebilir, ilerleme [Bildirimler](notifications.md) bölümünde de yansıtılır. Yanıtlar, daha kolay okunabilirlik için Markdown ile biçimlendirilmiştir (listeler, vurgular, bağlantılar vb.).

## Ne sorabilirsiniz

Gramps Web API sürüm 3.6.0 ile tanıtılan araç çağırma yetenekleri sayesinde, AI asistanı artık daha karmaşık soruları ele alabilir:

- **Aile ilişkileri**: "Jane Smith'in büyük ebeveynleri kimlerdir?" veya "John Doe, Mary Johnson ile nasıl akraba?"
- **Filtrelenmiş aramalar**: "1850'den sonra Londra'da doğan tüm insanları göster" veya "Paris'te hangi olaylar oldu?"
- **Tarih tabanlı sorgular**: "1900'den önce kim öldü?" veya "1920 ile 1950 arasında gerçekleşen evlilikleri listele"
- **Yer bilgisi**: "Fransa'da hangi yerler var?" veya "St. Mary Kilisesi hakkında bana bilgi ver"
- **Genel sorular**: "John Doe'nun çocuklarının adı nedir?" veya "Mary Smith ne zaman doğdu?"

## Soru sormak için ipuçları

AI asistanından en iyi sonuçları almak için:

- **Özel olun**: Sorunuzu mümkün olduğunca fazla ayrıntı ile formüle edin, belirsizliklerden kaçının. Örneğin, "1850'de Boston'da doğan John Smith ne zaman evlendi?" "John Smith ne zaman evlendi?" sorusundan daha iyidir.
- **Doğru isimler kullanın**: İlgili olduğunda belirli isimleri, yerleri ve tarihleri belirtin.
- **Tek bir şey sorun**: Karmaşık soruları daha basit parçalara ayırarak daha iyi sonuçlar elde edin.
- **Kendi dilinizi kullanın**: Büyük dil modelleri çok dilli olduğundan, sorularınızı kendi dilinizde sorabilir ve aynı dilde yanıt alabilirsiniz.

!!! tip
    Lütfen toplulukla işe yarayan ve yaramayan şeyler hakkında deneyimlerinizi paylaşın.
