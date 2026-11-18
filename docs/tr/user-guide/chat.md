# AI Asistanını Kullanma

Gramps Web'deki **Asistan** görünümü (kurulumunuzda etkinleştirildiyse), aile ağacınızla ilgili soruları yanıtlayan bir AI asistanına erişim sağlar.

!!! uyarı
    Her AI asistanında olduğu gibi, yanıtlar yanlış olabilir. Yanıtın dayandığı kayıtları kontrol etmek için bağlantıları kullanın.

## Nasıl çalışır

Asistan, ağacınızı önceden bilmez. Bir soruyu yanıtlamak için, büyük bir dil modeli ihtiyaç duyduğu kayıtları arar, tıpkı sizin kendinizin yapacağı gibi:

- [tam metin araması](search.md) ile ağacı arar,
- isimler, tarihler, yerler veya çocuk sayısı gibi kriterlere göre insanları, olayları ve aileleri filtreler,
- bir kişinin atalarını, torunlarını ve diğer akrabalarını, aralarındaki ilişki ile birlikte bulur,
- insanların, ailelerin, olayların, yerlerin ve notların tam kayıtlarını okur.

Sonrasında bulduğu kayıtlara dayanarak yanıt verir ve onlara bağlantılar sağlar. Çalışırken kullandığı araçlar gösterilir, böylece süreci takip edebilirsiniz. Daha uzun süren sorular arka planda çalışır – başka sayfalara geçebilir ve geri dönebilirsiniz.

Asistan yalnızca sizin ağacınızdan yanıt verir, dil modelinin genel bilgisinden değil – tanınmış kişiler hakkında bile. Eğer ağaçta bir şey kaydedilmemişse, bunu belirtir ve bulduğu ilgili bilgileri, örneğin bir notta, belirtir. Sadece sizin görebileceğiniz şeyleri görür: özel kayıtlara bağlantılar, bunları göremeyen kullanıcılar için düz metin olarak gösterilir.

Takip soruları, aynı konuşmadaki önceki soruların bağlamını korur, böylece bir kişi hakkında sorduğunuzdan sonra "Ve ne zaman öldü?" diye sorabilirsiniz.

## Ne sorabilirsiniz

- **İnsanlar hakkında gerçekler**: "Mary Smith ne zaman doğdu?" veya "John Doe'nun çocuklarının isimleri nelerdir?"
- **Akrabalar**: "Jane Smith'in büyükanne ve büyükbabaları kimlerdir?" veya "Johann Meyer'in hangi torunları Amerika'ya göç etti?"
- **Kriterlerle aramalar**: "1850'den sonra Londra'da kim doğdu?", "1920 ile 1950 arasındaki evlilikleri listele" veya "Beş veya daha fazla çocuğu olan çiftler kimlerdir?"
- **Yerler**: "Paris'te hangi olaylar gerçekleşti?" veya "Kim Danimarka'da doğdu?" – daha büyük bir yer içindeki yerler de dahil edilir.
- **Notlar**: "Meyer ailesinin çiftliği hakkında notlar ne diyor?"

Tüm ağacı bir anda gerektiren sorular, örneğin "En yaygın ilk isim nedir?", asistanın her aramada sınırlı sayıda kaydı görebilmesi nedeniyle daha az etkili çalışır.

## Görseller hakkında sorma

Eğer sunucu yöneticisi bunu etkinleştirdiyse, istemde görsel eklemek için bir düğme vardır. Ayrıca bir görseli yapıştırabilir veya isteme görsel dosyaları sürükleyip bırakabilirsiniz. Bir soruya kadar dört görsel eklenebilir, örneğin "Bu kayıtta kim bahsediliyor ve benim ağacımda var mı?" diye sormak için bir kilise kaydının taramasını ekleyebilirsiniz.

Görseller yalnızca ekli oldukları soruyla birlikte gönderilir. Takip soruları, asistanın bunlar hakkında söylediklerine atıfta bulunabilir, ancak görsellere değil, bu nedenle gerekirse onları tekrar ekleyin. Eğer ağacınızda AI kullanımına bir sınır varsa, her görsel ek bir soru gibi sayılır.

## Asistanın ağacınızı değiştirmesine izin verme

Eğer sunucu yöneticisi bunu etkinleştirdiyse, editörler, sahipler ve yöneticiler asistanın ağacı değiştirmesini isteyebilir, örneğin "Johann Meyer için 3 Mayıs 1802'de St. Mary's'te bir vaftiz ekle" veya "Anna Smith'in doğum yılını düzelt, 1871 olmalı" gibi.

Asistan asla kendi başına bir şeyi değiştirmez. Eklemek, düzenlemek veya silmek istediği her kaydı listeleyen bir **Önerilen değişiklikler** kartı ile yanıt verir; eski değerler üstü çizili, yeni değerler ise vurgulanmış olarak gösterilir. **Uygula** butonuna tıklamadığınız sürece hiçbir şey gerçekleşmez. Değişiklikler, diğer düzenlemeler gibi geri alabileceğiniz bir mesajdan veya [revizyon geçmişinden](revisions.md) tek adımda yapılır.

Bir öneriyi uygulamadan önce dikkatlice kontrol edin – özellikle asistanın doğru kişiyi seçtiğinden ve ağacınızda zaten var olan (bir yer veya kaynak gibi) yeni bir kayıt eklemediğinden emin olun, bu kayıt biraz farklı bir isimle mevcut olabilir. Eğer bir öneri tam doğru değilse, neyin değiştirilmesi gerektiğini belirtin ve asistan tekrar öneride bulunsun.

Bir öneri uygulandıktan sonra, aynı konuşmadaki daha eski öneriler artık uygulanamaz, çünkü bunlar ağacın öncesi için yapılmıştı. Aynı şey, etkilenen kayıtlardan biri bu süre zarfında değiştirilirse de geçerlidir.

## Soru sorma ipuçları

- **İnsanları adlandırın.** Asistan sizin kim olduğunuzu veya evdeki kişinin kim olduğunu bilmez, bu yüzden "büyükanne" yerine "Anna Smith'in (1950 doğumlu) büyükanne" hakkında sorun. Ayrıca Gramps ID'lerini de kullanabilirsiniz, örneğin "I0042'nin çocukları".
- **Belirgin olun** isimler yaygın olduğunda: "1850'de Boston'da doğan John Smith ne zaman evlendi?" demek, "John Smith ne zaman evlendi?" demekten daha iyidir.
- **Kendi dilinizi kullanın.** Kendi dilinizde sorabilirsiniz ve aynı dilde yanıt alabilirsiniz.
- **Farklı bir şekilde tekrar sorun** eğer bir yanıt eksik görünüyorsa – örneğin, ilgilendiğiniz yer veya zaman dilimini belirterek.

!!! ipucu
    Lütfen toplulukla işe yarayan ve işe yaramayan şeyler hakkında deneyimlerinizi paylaşın.
