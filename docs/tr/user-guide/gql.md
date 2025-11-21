# Gramps Sorgu Dili ile Filtreleme

Nesne liste görünümleri (kişiler, aileler, olaylar, ...) [Gramps Sorgu Dili](https://github.com/DavidMStraub/gramps-ql) (GQL) tabanlı isteğe bağlı bir gelişmiş filtreleme moduna sahiptir.

Kullanmak için, GQL sözdiziminde bir sorgu yazın ve enter tuşuna basın (veya "uygula" düğmesine tıklayın). Görünüm, sorguya göre filtrelenecektir. Sorgu geçersizse, giriş alanının çerçevesi kırmızıya döner.

GQL sözdizimi aşağıda açıklanmıştır, GQL belgelerinden kopyalanmıştır.

## Sözdizimi

Bir GQL sorgusu, `property operator value` biçimindeki ifadelerden oluşan bir dizedir ve isteğe bağlı olarak `and` ve `or` anahtar kelimeleri ile parantezler ile birleştirilebilir.

### Özellikler

#### `class`

Gramps nesne sınıfını filtreler ve `person`, `family`, `event`, `place`, `citation`, `source`, `repository`, `media` veya `note` değerlerinden biri olabilir.

#### Nesne özellikleri

GQL, Gramps nesnelerinin iç içe geçmiş özelliklerini sorgulamayı destekler, örneğin `primary_name.date.calendar`. Aşağıda özelliklerin tam listesi için bakın – ayrıca [Gramps Veri Modeli](https://gramps-project.org/wiki/index.php/Gramps_Data_Model) sayfasına da bakın.

#### İndeks ile liste elemanları

Liste benzeri özelliklerdeki bireysel elemanlar, kare parantez içinde pozisyonel indeks ile erişilebilir. Bu, iç içe geçmiş özelliklerle birleştirilebilir, örneğin `primary_name.surname_list[0].surname`.

#### `length`

Bu, bir dizi benzeri Gramps özelliğinin uzunluğunu döndüren özel bir özelliktir, örneğin `media_list.length > 0` medya referanslarına sahip nesneleri almak için.

#### `all`, `any`

Dizi benzeri Gramps özellikleri için iki özel özellik daha. `all`, koşulun listenin tüm öğelerine uygulanmasını gerektirirken, `any` en az bir öğeye uygulanmasını gerektirir. Her iki özellik de öncesinde ve sonrasında diğer özelliklerle birleştirilebilir. Örnekler: `media_list.any.citation_list.length > 0` medya referanslarına sahip ve alıntı içeren nesneleri döndürür; `media_list.all.citation_list.length = 0` tüm medya nesnelerinin alıntı içermediği nesneleri döndürür.

#### Dizi indeksi

Belirli liste elemanlarına erişmek için sayısal bir dizi indeksi kullanılabilir, örneğin ilk çocuk için `child_ref_list[0]`.

#### `get_person`, vb.

Önceki tüm özellikler tek bir Gramps nesnesine atıfta bulunurken, başlangıç nesnesi tarafından atıfta bulunulan farklı nesneler üzerinde filtreleme yapmak da mümkündür. Örneğin, bir olayın `place` özelliğinde bir yer tanıtıcısı vardır. `get_place` sahte özelliğini kullanarak, GQL o nesnenin özelliklerine geçiş yapar. Örneğin, `class = event and place.get_place.name.value ~ York` sorgusunu aramak mümkündür. Bu, `any` veya `all` ile de birleştirilebilir, örneğin `class = person and event_ref_list.any.ref.get_event.description ~ farmer`.

### Operatörler

#### `=`, `!=`

Eşitlik veya eşitsizlik. Örnekler: `class = person`, `class != family`

#### `>`, `>=`, `<`, `<=`

Karşılaştırma. Hem dizeler hem de sayılar için çalışır. Örnekler: `confidence <= 1`, `change > 1712477760`, `gramps_id > "I2015"`

#### `~`, `!~`

İçerir veya içermez. Hem listeler hem de dizeler için çalışır. Örnekler: `gramps_id !~ F00`, `author ~ David`, `family_list ~ "3a16680f7d226e3ac3eefc8b57a"`

#### Operatör/değer yok

Eğer hiçbir operatör ve değer verilmezse, değer bir boolean (doğru veya yanlış) olarak yorumlanır. Bu, tüm özellik türleri için geçerlidir ve true/false'a dönüştürme için Python kuralları uygulanır. Örneğin, `private` sorgusu özel nesneleri döndürür; `confidence` 0'dan büyük olan nesneleri döndürür; `media_list` en az bir medya referansına sahip nesneleri döndürür.

### Değerler

Değerler sayılar veya dizeler olabilir. Eğer sayılar dizeler olarak yorumlanacaksa veya `=` gibi özel karakterler varsa, değeri dizeler içinde kapatın. Örnekler: `gramps_id = F0001`, ancak `gramps_id = "0001"`.

## Yorumlu örnekler

```sql
class = note and private and text.string ~ David
```

Metinlerinde "David" dizesini içeren tüm özel notlar


```sql
media_list.length >= 10
```

10 veya daha fazla medya referansına sahip tüm nesneler (herhangi bir sınıftan)

```sql
class != person and media_list.any.rect
```

Bir kişi *olmayan* ancak bir görüntünün parçası olan bir medya referansına sahip tüm nesneler. Burada, `media_list.any.rect` ifadesi, medya listesindeki her bir öğe için `rect` (dikdörtgen) özelliğinin doğru bir değere sahip olup olmadığını kontrol eder, yani boş olmayan bir listedir. (`media_list.any.rect.length > 0` aynı etkiye sahip olacaktır.)

```sql
class = family and child_ref_list.length > 10
```

10'dan fazla çocuğa sahip aileler.

```sql
class = event and date.modifier = 0 and date.dateval[2] > 2020
```

Tarihi normal bir tarih (aralık değil vb.) olan ve yılı 2020'den sonraki olaylar.

```sql
note_list.any.get_note.text.string ~ "David"
```

Metinlerinde "David" dizesini içeren en az bir notu olan tüm nesneler.


```sql
class = family and child_ref_list.all.ref.get_person.gender = 0 and child_ref_list.length = 3
```

Üç kızı olan tüm aileler.


## Gramps Özelliklerinin Tam Listesi

Gramps özelliklerinin tam listesi için [GQL belgelerine](https://github.com/DavidMStraub/gramps-ql#full-list-of-gramps-properties) bakın.
