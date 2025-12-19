# AI sohbeti kullanma

!!! bilgi
    AI sohbeti, Gramps Web API sürüm 2.5.0 veya daha yüksek ve Gramps Web sürüm 24.10.0 veya daha yüksek gerektirir. Gramps Web API sürüm 3.6.0, daha akıllı etkileşimler için araç çağırma yeteneklerini tanıttı.

Gramps Web'deki sohbet görünümü (kurulumunuzda mevcutsa), aile ağacınızla ilgili soruları yanıtlayabilen bir AI asistanına erişim sağlar.

!!! uyarı
    Bu hala yeni ve gelişen bir özellik olduğundan, bazı soru türleri iyi çalışırken diğerleri çalışmayabilir. Ayrıca, herhangi bir AI asistanında olduğu gibi, yanlış bilgi verebilir, bu nedenle her zaman kontrol etmeyi unutmayın.

## Nasıl çalışır

Asistanın hangi tür soruları yanıtlayabileceğini anlamak için, nasıl çalıştığını aşağıda anlamak faydalıdır:

1. Kullanıcı bir soru sorar.
2. AI asistanı, cevapları bulmak için birden fazla yaklaşım kullanabilir:
   - **Anlamsal Arama**: Gramps Web, aile ağacınızdaki ilgili bilgileri içermesi en olası nesneleri tanımlar. Örneğin, "John Doe'nun çocuklarının adı nedir?" diye sorarsanız, John Doe'nun baba olduğu aileler en üst sonuçlar arasında yer alır.
   - **Araç Çağırma (Gramps Web API v3.6.0+)**: Asistan, belirli kriterlere göre kişiler/olaylar/aileler/yerler aramak, filtrelemek, bireyler arasındaki ilişkileri hesaplamak ve ayrıntılı bilgi almak için özel araçları kullanarak doğrudan veritabanınızı sorgulayabilir.
3. Gramps Web, soruyu ve alınan bilgileri büyük bir dil modeline ileterek bir cevap oluşturur.
4. Cevap size gösterilir.

## Ne sorabilirsiniz

Gramps Web API sürüm 3.6.0 ile tanıtılan araç çağırma yetenekleri sayesinde, AI asistanı artık daha karmaşık soruları yönetebilir:

- **Aile ilişkileri**: "Jane Smith'in büyük ebeveynleri kimlerdir?" veya "John Doe, Mary Johnson ile nasıl akrabadır?"
- **Filtrelenmiş aramalar**: "1850'den sonra Londra'da doğan tüm insanları göster" veya "Paris'te hangi olaylar oldu?"
- **Tarih bazlı sorgular**: "1900'den önce kim öldü?" veya "1920 ile 1950 arasında gerçekleşen evlilikleri listele"
- **Yer bilgisi**: "Fransa'da hangi yerler var?" veya "St. Mary Kilisesi hakkında bana bilgi ver"
- **Genel sorular**: "John Doe'nun çocuklarının adı nedir?" veya "Mary Smith ne zaman doğdu?"

## Soru sorma ipuçları

AI asistanından en iyi sonuçları almak için:

- **Spesifik olun**: Sorunuzu mümkün olduğunca detaylı bir şekilde formüle edin, belirsizliklerden kaçının. Örneğin, "1850'de Boston'da doğan John Smith ne zaman evlendi?" demek, "John Smith ne zaman evlendi?" demekten daha iyidir.
- **Doğru isimler kullanın**: İlgili olduğunda belirli isimler, yerler ve tarihler belirtin.
- **Tek bir şey sorun**: Karmaşık soruları daha basit parçalara ayırarak daha iyi sonuçlar elde edin.
- **Kendi dilinizi kullanın**: Büyük dil modelleri çok dilli olduğundan, soruları kendi dilinizde sorabilir ve aynı dilde cevap alabilirsiniz.

!!! ipucu
    Lütfen toplulukla işe yarayan ve yaramayan şeyler hakkında deneyimlerinizi paylaşın.
