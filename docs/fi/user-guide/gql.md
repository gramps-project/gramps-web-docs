# Suodatin Grampsin kyselykielellä

Objektin listanäkymät (henkilöt, perheet, tapahtumat, ...) sisältävät valinnaisen edistyneen suodatinmoodin, joka perustuu [Grampsin kyselykieleen](https://github.com/DavidMStraub/gramps-ql) (GQL).

Käyttääksesi sitä, kirjoita kysely GQL-syntaksissa ja paina enter (tai napsauta "käytä" -painiketta). Näkymä suodatetaan kyselyn mukaan. Jos kysely on virheellinen, syöttökentän kehys muuttuu punaiseksi.

GQL-syntaksi on kuvattu alla, kopioituna GQL-dokumentaatiosta.

## Syntaksi

GQL-kysely on merkkijono, joka koostuu lauseista muodossa `property operator value`, jotka voidaan yhdistää valinnaisesti avainsanoilla `and` ja `or` sekä sulkujen avulla.

### Ominaisuudet

#### `class`

Suodattaa Gramps-objektin luokan mukaan ja voi olla yksi seuraavista: `person`, `family`, `event`, `place`, `citation`, `source`, `repository`, `media` tai `note`.

#### Objektin ominaisuudet

GQL tukee Gramps-objektien sisäisten ominaisuuksien kyselyä, esim. `primary_name.date.calendar`. Katso alla täydellinen lista ominaisuuksista – katso myös [Grampsin tietomalli](https://gramps-project.org/wiki/index.php/Gramps_Data_Model).

#### Listan elementit indeksin mukaan

Yksittäisiin elementteihin listan kaltaisissa ominaisuuksissa voidaan päästä käsiksi paikkatietojen avulla neliömäisissä sulkuissa. Tämä voidaan yhdistää sisäisiin ominaisuuksiin, esim. `primary_name.surname_list[0].surname`.

#### `length`

Tämä on erityinen ominaisuus, joka palauttaa taulukon kaltaisen Gramps-ominaisuuden pituuden, esim. `media_list.length > 0` saadaksesi objekteja, joilla on media viittauksia.

#### `all`, `any`

Kaksi muuta erityistä ominaisuutta taulukon kaltaisille Gramps-ominaisuuksille. `all` vaatii ehdon pätevän kaikille listan kohteille, `any` vaatii sen pätevän ainakin yhteen kohteeseen. Molempia ominaisuuksia voidaan yhdistää muihin ominaisuuksiin ennen ja jälkeen. Esimerkkejä: `media_list.any.citation_list.length > 0` palauttaa objekteja, joilla on media viittauksia, joilla on viittauksia; `media_list.all.citation_list.length = 0` palauttaa objekteja, joissa kaikilla mediaobjekteilla ei ole viittauksia.

#### Taulukon indeksi

Numerollista taulukon indeksiä voidaan käyttää tiettyjen listan elementtien käsittelemiseen, esim. `child_ref_list[0]` ensimmäiselle lapselle.

#### `get_person`, jne.

Vaikka kaikki edelliset ominaisuudet viittaavat yhteen Gramps-objektiin, on myös mahdollista suodattaa eri objekteja, joihin alkuperäinen objekti viittaa. Esimerkiksi tapahtumalla on paikkaohjain sen `place`-ominaisuudessa. Käyttämällä `get_place`-pseudo-ominaisuutta GQL siirtyy kyseisen objektin ominaisuuksiin. Esimerkiksi on mahdollista etsiä `class = event and place.get_place.name.value ~ York`. Tämä voidaan myös yhdistää `any` tai `all`, esim. `class = person and event_ref_list.any.ref.get_event.description ~ farmer`.

### Operaattorit

#### `=`, `!=`

Yhtä suuri tai ei yhtä suuri. Esimerkkejä: `class = person`, `class != family`

#### `>`, `>=`, `<`, `<=`

Vertailu. Toimii sekä merkkijonoille että numeroille. Esimerkkejä: `confidence <= 1`, `change > 1712477760 `, `gramps_id > "I2015"`

#### `~`, `!~`

Sisältää tai ei sisällä. Toimii sekä listoille että merkkijonoille. Esimerkkejä: `gramps_id !~ F00`, `author ~ David`, `family_list ~ "3a16680f7d226e3ac3eefc8b57a"`

#### Ei operaattoria/arvoa

Jos operaattoria ja arvoa ei anneta, arvoa tulkitaan booleanina (true tai false). Tämä toimii
kaikkien tyyppisten ominaisuuksien kanssa, ja Pythonin säännöt totuuden/epätotuuden muuntamiseksi otetaan huomioon. Esimerkiksi kysely `private` palauttaa yksityiset objektit; `confidence` palauttaa objektit, joissa luottamus on suurempi kuin 0; `media_list` palauttaa objektit, joilla on vähintään yksi media viittaus.

### Arvot

Arvot voivat olla numeroita tai merkkijonoja. Jos numeroita tulisi tulkita merkkijonoina tai erityisiä merkkejä kuten = on mukana, sulje arvo merkkijonoihin. Esimerkkejä: `gramps_id = F0001`, mutta `gramps_id = "0001"`.

## Kommentoidut esimerkit

```sql
class = note and private and text.string ~ David
```

Kaikki yksityiset muistiinpanot, jotka sisältävät merkkijonon "David" tekstissään


```sql
media_list.length >= 10
```

Kaikki objektit (mikä tahansa luokka) joilla on 10 tai enemmän media viittauksia

```sql
class != person and media_list.any.rect
```

Kaikki objektit, jotka *eivät* ole henkilöitä mutta joilla on media viittaus, joka on osa kuvaa. Tässä `media_list.any.rect` tarkoittaa, että jokaiselle media listan kohteelle tarkistetaan, onko `rect` (suorakulmio) ominaisuudella totuudenmukainen arvo, mikä tarkoittaa, että se on ei-tyhjää lista. (`media_list.any.rect.length > 0` olisi sama vaikutus.)

```sql
class = family and child_ref_list.length > 10
```

Perheet, joilla on yli 10 lasta.

```sql
class = event and date.modifier = 0 and date.dateval[2] > 2020
```

Tapahtumat, joissa päivämäärä on normaali päivämäärä (ei aikaväli jne.) ja vuosi on vuoden 2020 jälkeen.

```sql
note_list.any.get_note.text.string ~ "David"
```

Kaikki objektit, joilla on vähintään yksi muistiinpano, joka sisältää merkkijonon "David" tekstissään.


```sql
class = family and child_ref_list.all.ref.get_person.gender = 0 and child_ref_list.length = 3
```

Kaikki perheet, joilla on kolme tytärtä.


## Täydellinen lista Grampsin ominaisuuksista

Täydellisen listan Grampsin ominaisuuksista löydät [GQL-dokumentaatiosta](https://github.com/DavidMStraub/gramps-ql#full-list-of-gramps-properties).
