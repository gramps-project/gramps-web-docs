# Verileri Kontrol Et ve Doğrula

**Aile Ağacı İşleme** bölümü [Yönetim ayarları](settings.md) iki aracı içerir: biri veritabanındaki teknik problemleri kontrol eder, diğeri ise mantıksız verileri kontrol eder.

## Veritabanını Kontrol Et ve Onar

Bu araç, Gramps veritabanındaki iç tutarsızlıkları kontrol eder ve düzeltebildiklerini onarır – Gramps Masaüstü'ndeki [Veritabanını Kontrol Et ve Onar aracı](https://www.gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Tools#Check_and_Repair_Database) ile benzerlik gösterir.

**Kontrol Et ve Onar** butonuna tıklayın ve ilerleme göstergesinin tamamlanmasını bekleyin. Sonuç butonun altında gösterilir:

- Eğer hata bulunmazsa, bir onay mesajı görüntülenir.
- Eğer hatalar bulunursa, uygulanan düzeltmelerin özeti gösterilir.

Bu aracı, veritabanı tutarsızlıklarından kaynaklanabilecek beklenmedik hatalar veya davranışlarla karşılaşırsanız çalıştırın; örneğin, nesneler arasında eksik ilişkiler gibi.

## Verileri Doğrula

[Veritabanını Kontrol Et ve Onar](#check-and-repair-database) *teknik* tutarsızlıkları ararken, bu araç *mantıksız* verileri arar – Gramps Masaüstü'ndeki [Verileri Doğrula aracı](https://gramps-project.org/wiki/index.php/Gramps_5.0_Wiki_Manual_-_Tools#Verify_the_Data) ile benzerlik gösterir. İmkansız olmayan ancak ikinci bir bakış açısını gerektirecek kadar olası olmayan durumları raporlar; örneğin, 12 yaşında bir anne veya 130 yaşında yaşayan bir kişi.

**Seçenekler** altında, testlerin kullandığı eşikleri ayarlayabilirsiniz – maksimum yaş, evlenmek veya çocuk sahibi olmak için minimum ve maksimum yaş, maksimum çocuk sayısı vb. – ayrıca eksik veya belirsiz tarihleri tahmin edip etmeyeceğinizi ve 31 Şubat gibi geçersiz tarihleri rapor edip etmeyeceğinizi de ayarlayabilirsiniz. Değiştirdiğiniz seçenekler, bir sonraki çalıştırma için tarayıcınızda hatırlanır; **Sıfırla** varsayılan ayarları geri getirir.

Başlamak için **Verileri Doğrula** butonuna tıklayın. Kontrol, arka planda bir görev olarak çalışır ve bulgular daha sonra **Veri Doğrulama Sonuçları** altında listelenir. Bu araç tarafından hiçbir şey değiştirilmez: sadece bulduğu şeyleri rapor eder.

!!! note
    Bir bulgu, bir hatanın kanıtı değildir. Uzun yaşamlar ve büyük yaş farkları meydana gelebilir, bu nedenle sonuçları düzeltilecek şeyler listesi yerine kontrol edilecek şeyler listesi olarak değerlendirin.
