# Arama

Arama sayfasına, üst uygulama çubuğundaki büyüteç simgesine tıklayarak veya `s` [klavye kısayolu](shortcuts.md) ile erişebilirsiniz.

## Tam metin araması

Arama alanına bir sorgu yazın. Sonuçlar, ikinci karakterden itibaren yazdıkça görünür; tek bir karakter aramak için Enter tuşuna basın. Gramps Web, tüm nesne türlerinde – insanlar, aileler, etkinlikler, yerler, kaynaklar, alıntılar, depolar, notlar ve medya – arama yapar ve eşleşen sonuçları alaka düzeyine göre sıralayarak döndürür. Aramayı temizlemek için, alandaki temizleme butonuna tıklayın veya Escape tuşuna basın.

Her sonuç, nesne türünü, adını ve bazı ayrıntıları gösterir; örneğin bir kişinin doğumu ve ölümü, bir ailenin evliliği, bir kaynağın yazarı veya bir notun ilk satırı. İlgili detay sayfasını açmak için herhangi bir sonuca tıklayın.

## Arama sözdizimi

- **Tüm kelimeler eşleşmelidir.** `Müller Berlin`, her iki kelimeyi de içeren nesneleri bulur.
- **`or`** herhangi bir kelimeyi içeren nesneleri bulur, örneğin `Meyer or Maier`. `and` kelimeler arasında da yazılabilir, ancak fark etmez.
- `or`, doğrudan yanındaki kelimelere uygulanır: `Meyer or Maier Berlin`, "(Meyer or Maier) ve Berlin" anlamına gelir. Parantezler desteklenmez.
- **Tırnak işaretleri** bir ifadeyi eşleştirir, yani bu sıradaki kelimeleri: `"Johann Georg"`.
- **Joker karakter:** sonuna eklenen `*`, herhangi bir sonu eşleştirir; örneğin `Mey*`, "Meyer", "Meyers", "Meyerhofer" vb. ile eşleşir. Bu, ifadeler için de geçerlidir: `"Johann Georg"*`.
- **Son kelime tamamlanır.** Sorgu bir harf veya rakam ile bitiyorsa, `*` ile bitiyormuş gibi aranır; bu nedenle `Anna Smi` zaten "Anna Smith" bulur. Son kelimeyi tam olarak aramak için sorguyu bir boşlukla bitirin veya kelimeyi tırnak içine alın. Bu, nesne seçicilerin arama kutuları ve [harita](map.md#search) için de geçerlidir.
- `or` ve `and` her durumda tanınır. Bu kelimelerden birini aramak için, onu tırnak içine alın.
- Kelimeler hariç tutulamaz; "değil" yoktur.

## Aramanın bulduğu şeyler

- Aksanların eşleşmesine gerek yoktur: "Müller" aynı zamanda "Muller" bulur ve "muller" de "Müller" bulur.
- Aileler ve etkinlikler, insanlarının isimleriyle de bulunur; örneğin "Müller", adı Müller olan herkesin ailelerini ve etkinliklerini bulur. Bu sonuçlar, doğrudan eşleşmelerin altında sıralanır.
- Standart türler, arayüz dilinizdeki isimleriyle bulunur; örneğin "Taufe", Almanca arayüzde vaftizleri bulur.
- Alt çizgiler kelimeleri ayırır, bu nedenle "microfilm", `scanned_microfilm.png` adlı bir medya dosyasını bulur.
- Özel kayıtları göremeyen kullanıcılar, özel bir üyenin adı gibi özel bilgiler aracılığıyla nesneleri bulamazlar.

## Nesne türüne göre filtreleme

Arama alanının altında, her nesne türü (İnsanlar, Aileler, Etkinlikler, Yerler, …) için geçiş butonları, sonuçları bir veya daha fazla belirli türle daraltmanıza olanak tanır. Varsayılan olarak tüm türler aranır. Bir veya daha fazla geçişi etkinleştirmek, sonuçları yalnızca o türlerle sınırlı hale getirir.
