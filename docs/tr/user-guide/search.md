# Arama

Arama sayfasına, üst uygulama çubuğundaki büyüteç simgesine tıklayarak veya `s` [klavye kısayolu](shortcuts.md) ile erişilebilir.

## Tam metin araması

Arama alanına herhangi bir sorgu yazın ve Enter tuşuna basın (veya arama butonuna tıklayın). Gramps Web, tüm nesne türlerinde – insanlar, aileler, olaylar, yerler, kaynaklar, alıntılar, havuzlar, notlar ve medya – arama yapar ve eşleşen sonuçları alaka derecesine göre sıralayarak döndürür.

Sonuçlar, nesne türünü, adını ve kısa bir özeti gösterir. İlgili detay sayfasını açmak için herhangi bir sonuca tıklayın.

Sonuna eklenen `*`, joker karakter olarak kullanılabilir; örneğin `Mey*`, "Meyer", "Meyers", "Meyerhofer" vb. ile eşleşir.

## Nesne türüne göre filtreleme

Arama alanının altında, her nesne türü için (İnsanlar, Aileler, Olaylar, Yerler, …) geçiş butonları, sonuçları bir veya daha fazla belirli türle daraltmanıza olanak tanır. Varsayılan olarak tüm türler aranır. Bir veya daha fazla geçişi etkinleştirmek, sonuçları yalnızca o türlerle sınırlı hale getirir.

## Anlamsal arama

!!! uyarı "Kullanımdan kaldırıldı"
    Anlamsal arama kullanımdan kaldırılmıştır ve Gramps Web API 3.25'te kaldırılacaktır. Yukarıda açıklanan tam metin araması etkilenmeyecektir.

Sunucu yöneticisi [anlamsal (Yapay Zeka destekli) aramayı](../install_setup/chat.md#semantic-search-deprecated) etkinleştirdiyse, arama sayfasının sağ üst köşesinde iki seçenek içeren bir mod geçişi görünür:

- **Arama** – standart tam metin araması (varsayılan)
- **Anlamsal** – sorgunuzun anlamını anlayan, tam kelimeleri eşleştirmek yerine AI destekli arama

Anlamsal arama, "19. yüzyılda Bavyera'daki çiftçi" gibi doğal dil sorguları için yararlıdır. Anlamsal arama dizininin doldurulması gerekir; dizini nasıl oluşturacağınız veya güncelleyeceğiniz için [Yönetim ayarları](../administration/settings.md) kısmına bakın.
