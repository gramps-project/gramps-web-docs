# Gramps Nesne Sorgu Dili ile Filtreleme

[nesne liste görünümleri](lists.md) (kişiler, aileler, olaylar, ...) ve [görev listesi](tasks.md) bir [Gramps Nesne Sorgu Dili](https://github.com/DavidMStraub/gramps-object-query-language) (GOQL) ifadeleri için bir filtre alanına sahiptir.

Bunu kullanmak için, filtre panelini açın, **GOQL** alanına bir ifade yazın ve Enter tuşuna basın (veya **Uygula**'ya tıklayın). Liste, ifadenin yanı sıra aktif diğer filtrelerle de filtrelenir. Eğer ifade geçersizse, alan bir hata olarak işaretlenir.

İfade, bulunduğunuz listedeki nesnelere her zaman uygulanır: Kişiler listesinde, `surname == 'Smith'` Smith soyadına sahip kişileri bulur.

!!! not
    GOQL alanı Gramps Web API 3.24 veya daha yenisini gerektirir.

## Sözdizimi

Bir GOQL ifadesi, Python programlama dilindeki bir koşul gibi görünür. Kullanmak için Python bilmenize gerek yoktur – aşağıdaki örnekler çoğu ihtiyacı karşılar.

### Karşılaştırmalar

Bir karşılaştırma `field operator value` biçimindedir, örneğin `surname == 'Smith'`.

Operatör | Anlamı
---------|--------
`==` | eşittir
`!=` | eşit değildir
`<`, `<=` | küçüktür, küçük veya eşittir (önce, daha küçük)
`>`, `>=` | büyüktür, büyük veya eşittir (sonra, daha büyük)
`in [ ... ]` | listelenen değerlerden biridir, örneğin `surname in ['Meyer', 'Maier']`
`not in [ ... ]` | listelenen değerlerden hiçbiri değildir
`'text' in field` | alan metni içerir, örneğin `'mill' in surname`
`is None` | alan boş veya mevcut değildir, örneğin `death.date.sortval is None`

Metin tek veya çift tırnak içinde yer alır (`'Smith'`), sayılar ise tırnak içinde yer almaz (`1850`). Karşılaştırmalar zincirlenebilir, örneğin `Date('1850') <= birth.date.sortval < Date('1900')`.

### Koşulları birleştirme

Koşullar `and` ve `or` ile birleştirilebilir ve `not` ile tersine çevrilebilir. `and`, `or`'dan önceliklidir; koşulları gruplamak için parantez kullanın:

```python
(gender == Person.MALE and surname == 'Smith') or given_name == 'Mary'
```

### Metin desenleri

- `like(field, 'pattern')` `%`'nin herhangi bir metni ve `_`'nin tek bir karakteri temsil ettiği bir deseni eşleştirir, örneğin "J" ile başlayan tüm verilen adlar için `like(given_name, 'J%')`.
- `regex(field, 'pattern')` bir [düzenli ifade](https://en.wikipedia.org/wiki/Regular_expression) ile eşleşir, örneğin `regex(surname, '^M[ae][iy]er$')`.

`like` ve `'text' in field` büyük ve küçük harf duyarsızdır (SQLite'ta bu yalnızca aksanlı olmayan A–Z harfleri için geçerlidir). `regex` ise büyük/küçük harf duyarlıdır.

### Alanlar

Bir alan, nesnenin bir özelliğinin adıdır, örneğin `gender` veya `gramps_id`, veya `primary_name.first_name` veya `primary_name.surname_list[0].surname` gibi iç içe bir özelliğe giden bir yoldur. Kare parantezler, bir listenin elemanını konumuna göre seçer, 0'dan başlayarak. Mevcut özellikler, [Gramps veri modeli](https://gramps-project.org/wiki/index.php/Gramps_Data_Model) özellikleridir. Bir alan mevcut değilse, hata mesajı mevcut olan alanları listeler.

Birkaç kısayol mevcuttur:

- Kişilerin `given_name` ve `surname`'ı vardır, bu da birincil adın verilen adı ve soyadıdır.
- Kişilerin `birth` ve `death`'ı vardır, doğum ve ölüm olayları, örneğin `birth.date.sortval` veya `death.place.name.value`.
- Ailelerin `father` ve `mother`'ı vardır, örneğin `father.surname == 'Smith'`.
- Olayların `place`'i, alıntıların `source`'u ve yerlerin `enclosed_by`'si, çevreleyen yerdir.

Bunlar zincirlenebilir, örneğin Aileler listesinde `father.birth.place.name.value`. İki alan da birbirleriyle karşılaştırılabilir, örneğin `father.surname == mother.surname`.

### İlgili nesne listeleri

`any(collection, condition)` bir koleksiyonun en az bir öğesi koşulu sağlıyorsa eşleşir ve `len(collection)` öğeleri sayar. Bir koşul olmadan, `any(collection)` koleksiyon boş değilse eşleşir. Koleksiyonlar şunlardır:

- neredeyse her nesnede: `notes`, `citations`, `media`, ve `tags`
- kişilerde: `events`, `families` (bir partner olarak), `parent_families` (bir çocuk olarak), ve `associations`
- ailelerde: `children`
- tüm nesnelerde: `backlinks`, ona referans veren nesneler, bunlar `_class` ile türleri test edilebilir, örneğin `any(backlinks, _class == 'Person')`

`any` ve `len` ayrıca nesnenin kendisinde saklanan listeler için de çalışır, örneğin `alternate_names` veya `primary_name.surname_list`.

### Sabitler ve türler

Gramps'ın sabit değerleri, `Person.MALE`, `Person.FEMALE`, `Person.UNKNOWN` gibi sabitler olarak mevcuttur veya `Citation.CONF_VERY_LOW` ile `Citation.CONF_VERY_HIGH` arasındaki güven düzeyleri gibi. Türler, `EventType.BIRTH`, `FamilyRelType.MARRIED`, `NameType.BIRTH`, `PlaceType.VILLAGE` veya `RepositoryType.ARCHIVE` gibi sabitlerle `value`'ları ile karşılaştırılır:

```python
type.value == EventType.BAPTISM
```

Kendinizin girdiği özel türlerin kendi sabitleri yoktur.

### Tarihler

`Date('...')` metin olarak yazılmış bir tarihi, bir tarih `sortval` ile karşılaştırılabilir bir değere dönüştürür, örneğin `birth.date.sortval < Date('1800')`.

`sortval`, bir zaman dilimini temsil eder ve bir tarihin türünü ve kalitesini göz ardı eder: "1800'den önce", "1800 civarı" ve "1800" hepsinin aynı `sortval`'ı vardır ve bir aralık veya süre için başlangıçtır. Bunları dikkate almak için, tarihin `modifier` veya `quality`'sini `Date.MOD_ABOUT`, `Date.MOD_BEFORE`, `Date.MOD_AFTER`, `Date.MOD_RANGE`, `Date.MOD_SPAN` veya `Date.QUAL_ESTIMATED` gibi sabitlerle karşılaştırın:

```python
date.modifier == Date.MOD_ABOUT
```

## Yorumlu örnekler

Kişiler listesi:

```python
gender == Person.FEMALE and like(given_name, 'Mar%')
```

Verilen adı "Mar" ile başlayan kadınlar.

```python
Date('1850') <= birth.date.sortval < Date('1900')
```

1850 ile 1899 arasında doğan kişiler.

```python
birth.place.name.value == death.place.name.value
```

Aynı isimde bir yerde doğup ölen kişiler.

```python
not any(notes)
```

Notu olmayan kişiler.

```python
any(events, type.value == EventType.BURIAL)
```

Bir defin olayı olan kişiler.

```python
any(alternate_names, surname_list[0].surname == 'Meyer')
```

Meyer soyadına sahip alternatif bir adı olan kişiler.

Aileler listesi:

```python
len(children) > 10
```

10'dan fazla çocuğu olan aileler.

```python
len(children, gender == Person.FEMALE) == 3
```

Üç kızı olan aileler.

```python
mother.death.date.sortval < father.death.date.sortval
```

Annenin babadan önce öldüğü aileler.

Olaylar listesi:

```python
type.value == EventType.BAPTISM and place.name.value == 'Berlin'
```

Berlin adında bir yerde vaftizler.

Alıntılar listesi:

```python
confidence >= Citation.CONF_HIGH
```

Yüksek veya çok yüksek güvene sahip alıntılar.

Notlar listesi:

```python
'David' in text.string and private == True
```

"David" içeren özel notlar.

```python
not any(backlinks)
```

Hiçbir nesneye bağlı olmayan notlar.

## Tam referans

Tam dil referansı için [GOQL belgelerine](https://github.com/DavidMStraub/gramps-object-query-language/blob/main/docs/where_expr.md) bakın.
