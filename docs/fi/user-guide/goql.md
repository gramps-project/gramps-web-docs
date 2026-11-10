# Suodatin Gramps Object Query Language -kielellä

[Objektin listan näkymät](lists.md) (henkilöt, perheet, tapahtumat, ...) ja [tehtävälista](tasks.md) sisältävät suodatin kentän lausekkeille [Gramps Object Query Language](https://github.com/DavidMStraub/gramps-object-query-language) (GOQL) -kielellä.

Käyttääksesi sitä, avaa suodatinpaneeli, kirjoita lauseke **GOQL**-kenttään ja paina Enter (tai napsauta **Käytä**). Lista suodatetaan lausekkeen mukaan, muiden aktiivisten suodattimien lisäksi. Jos lauseke on virheellinen, kenttä merkitään virheeksi.

Lauseke koskee aina listan objekteja, joissa olet: Henkilöt-listassa `surname == 'Smith'` löytää henkilöt, joiden sukunimi on Smith.

!!! huomautus
    GOQL-kenttä tarvitsee Gramps Web API 3.24 tai uudemman.

## Sintaksi

GOQL-lauseke näyttää olosuhteelta Python-ohjelmointikielessä. Sinun ei tarvitse tuntea Pythonia käyttääksesi sitä – alla olevat esimerkit kattavat suurimman osan tarpeista.

### Vertailut

Vertailu on muodoltaan `kenttä operaattori arvo`, esimerkiksi `surname == 'Smith'`.

Operaattori | Merkitys
------------|--------
`==` | on yhtä suuri kuin
`!=` | ei ole yhtä suuri kuin
`<`, `<=` | on pienempi kuin, pienempi tai yhtä suuri kuin (aikaisempi, pienempi)
`>`, `>=` | on suurempi kuin, suurempi tai yhtä suuri kuin (myöhempi, suurempi)
`in [ ... ]` | on yksi luetelluista arvoista, esim. `surname in ['Meyer', 'Maier']`
`not in [ ... ]` | ei ole mikään luetelluista arvoista
`'teksti' in kenttä` | kenttä sisältää tekstin, esim. `'mill' in surname`
`is None` | kenttä on tyhjää tai ei olemassa, esim. `death.date.sortval is None`

Teksti kirjoitetaan yksinkertaisiin tai kaksoislainausmerkkeihin (`'Smith'`), numerot eivät (`1850`). Vertailuja voidaan ketjuttaa, esim. `Date('1850') <= birth.date.sortval < Date('1900')`.

### Ehtojen yhdistäminen

Ehtoja voidaan yhdistää `and` ja `or` -operaattoreilla, ja kääntää `not` -operaattorilla. `and` -operaattori on etusijalla `or` -operaattorin yli; käytä sulkuja ryhmittelyyn:

```python
(gender == Person.MALE and surname == 'Smith') or given_name == 'Mary'
```

### Tekstimuodot

- `like(field, 'pattern')` vastaa muotoa, jossa `%` edustaa mitä tahansa tekstiä ja `_` yhtä merkkiä, esim. `like(given_name, 'J%')` kaikille etunimille, jotka alkavat "J":llä.
- `regex(field, 'pattern')` vastaa [säännöllistä lauseketta](https://en.wikipedia.org/wiki/Regular_expression), esim. `regex(surname, '^M[ae][iy]er$')`.

`like` ja `'teksti' in kenttä` eivät ota huomioon isoja ja pieniä kirjaimia (SQLite:ssä tämä koskee vain A–Z-kirjaimia ilman aksentteja). `regex` on kirjainherkkä.

### Kentät

Kenttä on objektin ominaisuuden nimi, kuten `gender` tai `gramps_id`, tai polku sisäkkäiseen ominaisuuteen, kuten `primary_name.first_name` tai `primary_name.surname_list[0].surname`. Neliösulut valitsevat listan elementin sen sijainnin mukaan, alkaen 0:sta. Saatavilla olevat ominaisuudet ovat [Grampsin tietomallin](https://gramps-project.org/wiki/index.php/Gramps_Data_Model) ominaisuuksia. Jos kenttää ei ole, virheilmoitus luettelee olemassa olevat kentät.

Muutamia oikopolkuja on saatavilla:

- Henkilöillä on `given_name` ja `surname`, etunimi ja sukunimi ensisijaisessa nimessä.
- Henkilöillä on `birth` ja `death`, heidän syntymä- ja kuolematapahtumansa, esim. `birth.date.sortval` tai `death.place.name.value`.
- Perheillä on `father` ja `mother`, esim. `father.surname == 'Smith'`.
- Tapahtumilla on `place`, viittauksilla on `source`, ja paikoilla on `enclosed_by`, ympäröivä paikka.

Näitä voidaan ketjuttaa, esim. `father.birth.place.name.value` Perheiden listassa. Kahta kenttää voidaan myös verrata toisiinsa, esim. `father.surname == mother.surname`.

### Liittyvien objektien listat

`any(collection, condition)` vastaa, jos vähintään yksi kokoelman kohde täyttää ehdon, ja `len(collection)` laskee kohteet. Ilman ehtoa `any(collection)` vastaa, jos kokoelma ei ole tyhjää. Kokoelmat ovat:

- lähes jokaisessa objektissa: `notes`, `citations`, `media`, ja `tags`
- ihmisillä: `events`, `families` (kumppanina), `parent_families` (lapsena), ja `associations`
- perheillä: `children`
- kaikilla objekteilla: `backlinks`, objektit, jotka viittaavat siihen, joita voidaan testata niiden tyypin mukaan `_class`, esim. `any(backlinks, _class == 'Person')`

`any` ja `len` toimivat myös objekteissa itsessään tallennetuissa listoissa, kuten `alternate_names` tai `primary_name.surname_list`.

### Vakiot ja tyypit

Grampsin kiinteät arvot ovat saatavilla vakioina, kuten `Person.MALE`, `Person.FEMALE`, `Person.UNKNOWN`, tai luottamustasot `Citation.CONF_VERY_LOW` - `Citation.CONF_VERY_HIGH`. Tyyppejä verrataan niiden `value` -arvolla vakioihin, kuten `EventType.BIRTH`, `FamilyRelType.MARRIED`, `NameType.BIRTH`, `PlaceType.VILLAGE`, tai `RepositoryType.ARCHIVE`:

```python
type.value == EventType.BAPTISM
```

Omat tyypit, jotka olet itse syöttänyt, eivät omaa omaa vakioita.

### Päivämäärät

`Date('...')` muuttaa tekstinä kirjoitetun päivämäärän arvoksi, jota voidaan verrata päivämäärän `sortval` -arvoon, esim. `birth.date.sortval < Date('1800')`.

`sortval` on yksi hetki ajassa ja se ei ota huomioon päivämäärän tyyppiä ja laatua: "ennen 1800", "noin 1800" ja "1800" kaikki omaavat saman `sortval` -arvon, ja aikavälin tai jakson osalta se on alku. Ottaaksesi nämä huomioon, vertaa päivämäärän `modifier` tai `quality` vakioihin, kuten `Date.MOD_ABOUT`, `Date.MOD_BEFORE`, `Date.MOD_AFTER`, `Date.MOD_RANGE`, `Date.MOD_SPAN`, tai `Date.QUAL_ESTIMATED`:

```python
date.modifier == Date.MOD_ABOUT
```

## Kommentoidut esimerkit

Henkilöiden lista:

```python
gender == Person.FEMALE and like(given_name, 'Mar%')
```

Naiset, joiden etunimi alkaa "Mar":lla.

```python
Date('1850') <= birth.date.sortval < Date('1900')
```

Henkilöt, jotka ovat syntyneet vuosina 1850–1899.

```python
birth.place.name.value == death.place.name.value
```

Henkilöt, jotka ovat syntyneet ja kuolleet paikassa, jolla on sama nimi.

```python
not any(notes)
```

Henkilöt, joilla ei ole muistiinpanoja.

```python
any(events, type.value == EventType.BURIAL)
```

Henkilöt, joilla on hautaustapahtuma.

```python
any(alternate_names, surname_list[0].surname == 'Meyer')
```

Henkilöt, joilla on vaihtoehtoinen nimi sukunimellä Meyer.

Perheiden lista:

```python
len(children) > 10
```

Perheet, joilla on yli 10 lasta.

```python
len(children, gender == Person.FEMALE) == 3
```

Perheet, joilla on kolme tytärtä.

```python
mother.death.date.sortval < father.death.date.sortval
```

Perheet, joissa äiti kuoli ennen isää.

Tapahtumien lista:

```python
type.value == EventType.BAPTISM and place.name.value == 'Berlin'
```

Kasteet paikassa nimeltä Berliini.

Viittausten lista:

```python
confidence >= Citation.CONF_HIGH
```

Viittaukset, joilla on korkea tai erittäin korkea luottamus.

Muistiinpanojen lista:

```python
'David' in text.string and private == True
```

Yksityiset muistiinpanot, jotka sisältävät "David".

```python
not any(backlinks)
```

Muistiinpanot, jotka eivät ole liitetty mihinkään objektiin.

## Täydellinen viittaus

Täydellisen kieliviittauksen löytämiseksi katso [GOQL-dokumentaatio](https://github.com/DavidMStraub/gramps-object-query-language/blob/main/docs/where_expr.md).
