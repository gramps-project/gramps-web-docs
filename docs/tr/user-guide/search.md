# Arama

Arama sayfasına, üst uygulama çubuğundaki büyüteç simgesine tıklayarak veya `s` [kısayol tuşuna](shortcuts.md) basarak erişebilirsiniz.

## Tam metin araması

Arama alanına herhangi bir sorgu yazın ve Enter'a basın (veya arama düğmesine tıklayın). Gramps Web, tüm nesne türlerinde – insanlar, aileler, olaylar, yerler, kaynaklar, alıntılar, havuzlar, notlar ve medya – arama yapar ve eşleşen sonuçları alaka düzeyine göre sıralayarak döndürür.

Sonuçlar nesne türünü, adını ve kısa bir özetini gösterir. İlgili detay sayfasını açmak için herhangi bir sonuca tıklayın.

## Arama sözdizimi

- **Tüm kelimeler eşleşmelidir.** `Müller Berlin`, her iki kelimeyi içeren nesneleri bulur.
- **`or`** herhangi bir kelimeyi içeren nesneleri bulur, örneğin `Meyer or Maier`. `and` kelimeler arasında da yazılabilir, ancak fark etmez.
- `or`, hemen yanındaki kelimelere uygulanır: `Meyer or Maier Berlin`, "(Meyer or Maier) ve Berlin" anlamına gelir. Parantezler desteklenmez.
- **Tırnak işaretleri** bir ifadeyi eşleştirir, yani bu sıradaki kelimeler: `"Johann Georg"`.
- **Joker karakter:** sonundaki `*`, herhangi bir sonu eşleştirir, örneğin `Mey*` "Meyer", "Meyers", "Meyerhofer" vb. ile eşleşir. Bu, ifadeler için de çalışır: `"Johann Georg"*`.
- `or` ve `and` her durumda tanınır. Bu kelimelerden birini aramak için, tırnak içinde yazın.
- Kelimeler hariç tutulamaz; "değil" yoktur.

## Aramanın buldukları

- Aksanların eşleşmesine gerek yoktur: "Müller" aynı zamanda "Muller" bulur ve "muller" "Müller" bulur.
- Aileler ve olaylar, insanlarının isimleriyle de bulunur, örneğin "Müller", adı Müller olan herkesin ailelerini ve olaylarını bulur. Bu sonuçlar, doğrudan eşleşmelerin altında sıralanır.
- Standart türler, arayüz dilinizdeki isimleriyle bulunur, örneğin "Taufe", Almanca arayüzde vaftizleri bulur.
- Alt çizgiler kelimeleri ayırır, bu nedenle "microfilm", `scanned_microfilm.png` adlı bir medya dosyasını bulur.
- Özel kayıtları göremeyen kullanıcılar, özel bir üyenin adı gibi özel bilgiler aracılığıyla nesneleri bulamazlar.

## Nesne türüne göre filtreleme

Arama alanının altında, her nesne türü için (İnsanlar, Aileler, Olaylar, Yerler, …) açma kapama düğmeleri, sonuçları bir veya daha fazla belirli türle daraltmanıza olanak tanır. Varsayılan olarak tüm türler aranır. Bir veya daha fazla düğmenin etkinleştirilmesi, sonuçları yalnızca bu türlerle sınırlı hale getirir.
