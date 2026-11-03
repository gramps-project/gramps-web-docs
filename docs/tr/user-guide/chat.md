# AI Asistanını Kullanma

!!! bilgi
    AI Asistanı, Gramps Web API sürüm 2.5.0 veya daha yüksek ve Gramps Web sürüm 24.10.0 veya daha yüksek gerektirir. Gramps Web API sürüm 3.6.0, daha akıllı etkileşimler için araç çağırma yeteneklerini tanıttı.

Gramps Web'deki **Asistan** görünümü (kurulumunuzda mevcutsa, eski sürümlerde "Sohbet" olarak etiketlenmiştir) aile ağacınızla ilgili soruları yanıtlayabilen bir AI asistanına erişim sağlar.

!!! uyarı
    Bu hala yeni ve gelişen bir özellik olduğundan, bazı soru türleri iyi çalışırken diğerleri çalışmayabilir. Ayrıca, herhangi bir AI asistanında olduğu gibi, yanlış bilgi verebilir, bu nedenle her zaman iki kez kontrol ettiğinizden emin olun.

## Nasıl çalışır

Asistanın hangi tür soruları yanıtlayabileceğini anlamak için, nasıl çalıştığını anlamak faydalıdır:

1. Kullanıcı bir soru sorar.
2. Asistan, özel araçlar kullanarak doğrudan veritabanınızı sorgular: ağaçta [tam metin araması](search.md) yapar, insanları/olayları/aileleri/yerleri belirli kriterlere göre filtreler, bireyler arasındaki ilişkileri hesaplar ve notları da dahil olmak üzere tam kayıtları arar.
3. Büyük bir dil modeli, bulduğu kayıtlara dayanarak bir cevap oluşturur.
4. Cevap, dayandığı kayıtlara bağlantılarla birlikte size gösterilir.

Asistan, yalnızca sizin ağacınızdan yanıt verir, dil modelinin genel bilgisinden değil – tanınmış kişiler hakkında bile. Ağaç bir şeyi kaydetmiyorsa, bunu belirtir ve bulduğu ilgili bilgileri, örneğin bir notta, belirtir. Görmenize izin verilmeyen nesnelere bağlantılar düz metin olarak gösterilir.

Takip soruları, aynı konuşmadaki önceki soruların bağlamını korur, böylece bir kişi hakkında soru sorduktan sonra "Ve ne zaman öldü?" diye sorabilirsiniz.

Asistan çalışırken, hangi araçları kullandığını gösteren göstergeler vardır (örneğin, insanları arama, ilişkileri araştırma), böylece cevabını oluştururken onu takip edebilirsiniz. Uzun süren sorular arka plan görevleri olarak işlenir – başka bir yere gidebilir ve geri dönebilirsiniz, ilerleme [Bildirimler](notifications.md) bölümünde de yansıtılır. Cevaplar, daha kolay okunabilmesi için Markdown ile biçimlendirilmiştir (listeler, vurgular, bağlantılar vb.).

## Ne sorabilirsiniz

Gramps Web API sürüm 3.6.0 ile tanıtılan araç çağırma yetenekleri sayesinde, AI asistanı artık daha karmaşık soruları da yanıtlayabilir:

- **Aile ilişkileri**: "Jane Smith'in büyük ebeveynleri kimlerdir?" veya "John Doe, Mary Johnson ile nasıl akrabadır?"
- **Filtrelenmiş aramalar**: "1850'den sonra Londra'da doğan tüm insanları göster" veya "Paris'te hangi olaylar oldu?"
- **Tarih tabanlı sorgular**: "1900'den önce kimler öldü?" veya "1920 ile 1950 arasında gerçekleşen evlilikleri listele"
- **Yer bilgisi**: "Fransa'da hangi yerler var?" veya "St. Mary's Kilisesi hakkında bana bilgi ver"
- **Genel sorular**: "John Doe'nun çocuklarının adı nedir?" veya "Mary Smith ne zaman doğdu?"

## Soru sormak için ipuçları

AI asistanından en iyi sonuçları almak için:

- **Açık olun**: Sorunuzu mümkün olduğunca fazla ayrıntıyla formüle edin, belirsizliklerden kaçının. Örneğin, "1850'de Boston'da doğan John Smith ne zaman evlendi?" demek, "John Smith ne zaman evlendi?" demekten daha iyidir.
- **Doğru isimler kullanın**: İlgili olduğunda belirli isimleri, yerleri ve tarihleri belirtin.
- **Tek bir şey sorun**: Karmaşık soruları daha basit parçalara ayırarak daha iyi sonuçlar alın.
- **Kendi dilinizi kullanın**: Büyük dil modelleri çok dilli olduğu için, kendi dilinizde sorular sorabilir ve aynı dilde cevaplar alabilirsiniz.

!!! ipucu
    Lütfen toplulukla işe yarayan ve yaramayan şeyler hakkında deneyimlerinizi paylaşın.
