# Verileri Kontrol Et ve Doğrula

**Ağaç İşleme** bölümü [Yönetim ayarları](settings.md) iki aracı içerir: biri veritabanındaki teknik sorunları kontrol eder, diğeri ise mantıksız verileri kontrol eder.

## Veritabanını Kontrol Et ve Onar

Bu araç Gramps veritabanını içsel tutarsızlıklar için kontrol eder ve düzeltebildiklerini onarır – Gramps Masaüstü'ndeki [Veritabanını Kontrol Et ve Onar aracı](https://www.gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Tools#Check_and_Repair_Database) ile benzerlik gösterir.

**Kontrol Et ve Onar** butonuna tıklayın ve ilerleme göstergesinin tamamlanmasını bekleyin. Sonuç butonun altında gösterilir:

- Hiçbir hata bulunmazsa, bir onay mesajı görüntülenir.
- Hatalar bulunursa, uygulanan düzeltmelerin özeti gösterilir.

Bu aracı, veritabanı tutarsızlıklarından kaynaklanabilecek beklenmedik hatalar veya davranışlarla karşılaşırsanız çalıştırın; örneğin, nesneler arasında kaybolmuş ilişkiler gibi.

## Verileri Doğrula

[Veritabanını Kontrol Et ve Onar](#check-and-repair-database) *teknik* tutarsızlıkları ararken, bu araç *mantıksız* verileri arar – Gramps Masaüstü'ndeki [Verileri Doğrula aracı](https://gramps-project.org/wiki/index.php/Gramps_5.0_Wiki_Manual_-_Tools#Verify_the_Data) ile benzerlik gösterir. İmkansız olmayan ancak ikinci bir bakış açısına değer kadar olası olmayan şeyleri raporlar; örneğin, 12 yaşında bir anne veya 130 yaşına kadar yaşayan bir kişi.

**Seçenekler** altında testlerin kullandığı eşik değerlerini ayarlayabilirsiniz – maksimum yaş, evlenmek veya çocuk sahibi olmak için minimum ve maksimum yaş, maksimum çocuk sayısı ve benzeri – ayrıca eksik veya belirsiz tarihleri tahmin edip etmeyeceğinizi ve 31 Şubat gibi geçersiz tarihleri rapor edip etmeyeceğinizi de ayarlayabilirsiniz.

Başlamak için **Verileri Doğrula** butonuna tıklayın. Kontrol, arka planda bir görev olarak çalışır ve bulgular daha sonra **Veri Doğrulama Sonuçları** altında listelenir. Bu araç hiçbir şeyi değiştirmez: yalnızca bulduğu şeyleri rapor eder.

!!! not
    Bir bulgu, bir hatanın kanıtı değildir. Uzun yaşamlar ve büyük yaş farkları meydana gelebilir, bu nedenle sonuçları düzeltilecek şeyler listesi yerine kontrol edilmesi gereken şeyler listesi olarak değerlendirin.
