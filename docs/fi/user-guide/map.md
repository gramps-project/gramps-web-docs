# Kartta

Karttasivu näyttää kaikki paikat perhepuussasi interaktiivisina merkkeinä maantieteellisellä kartalla. Se on saatavilla sivupalkista.

## Paikkamerkit

Vain paikat, joilla on GPS-koordinaatit tallennettuna Gramps-tietokantaan, näkyvät kartalla. Paikat ilman koordinaatteja jätetään hiljaa pois. GPS-koordinaatit voidaan asettaa paikan yksityiskohtasivulla (muokkaa paikkaa ja täytä leveys- ja pituusasteen kentät).

!!! vinkki
    Jos monet paikoistasi puuttuvat kartalta, avaa paikan yksityiskohtasivu ja tarkista, onko leveys- ja pituusasteet asetettu. Voit lisätä tai korjata koordinaatteja suoraan paikan muokkausnäkymästä.

Jokainen paikka, jolla on koordinaatit, näkyy merkkinä. Klikkaamalla merkkiä avautuu yhteenvetokortti, jossa näkyy paikan nimi sekä siihen liittyvät tapahtumat ja henkilöt. Klikkaa paikan nimeä kortissa avataksesi koko paikan yksityiskohtasivun.

## Haku

Karttanäkymän vasemmassa yläkulmassa oleva hakukenttä hakee kirjoittaessasi ja ryhmittelee tulokset kolmen otsikon alle:

- **Paikat** – paikat perhepuussasi. Valitsemalla yhden kartta siirtyy siihen ja korostaa sen merkkiä.
- **Henkilöt** – henkilöt perhepuussasi. Valitsemalla yhden kartta vaihtuu henkilön näkymään, joka on kuvattu [alla](#following-a-person-across-the-map).
- **Ulkoiset** – sijainnit [OpenStreetMap](https://www.openstreetmap.org/) -palvelusta, mistä tahansa maailmassa. Valitsemalla yhden kartta vain siirtyy ja zoomaa kyseiseen sijaintiin; se ei suodata tai muuta puusi paikkoja.

Ulkoiset tulokset ovat myös hyödyllisiä, kun lisäät koordinaatteja paikkaan: voit etsiä sijaintia täältä nähdäksesi, missä se sijaitsee ennen kuin syötät sen leveys- ja pituusasteet.

## Henkilön seuraaminen kartalla

Henkilön valitseminen – kartan hakukentästä tai henkilön yksityiskohtasivun **Avaa kartalla** -painikkeella – näyttää paikat, jotka liittyvät kyseisen henkilön tapahtumiin – mukaan lukien heidän perheidensä tapahtumat, kuten avioliitot – yhdistettyinä viivoilla aikajärjestyksessä. Pienet nuoliviivat jokaisessa viivassa osoittavat matkasuunnan, joten voit seurata henkilön elämää syntymästä kuolemaan kartalla.

Paikoilla paikan yksityiskohtasivulla on myös **Avaa kartalla** -painike, joka avaa kartan keskittyen kyseiseen paikkaan.

## Aikajousi

Sivun alareunassa oleva aikajousi suodattaa, mitkä paikkamerkit näkyvät niiden liitettyjen tapahtumien vuoden perusteella:

- Vedä kahvaa valitaksesi vuosi.
- Vain paikat, jotka liittyvät tapahtumiin, jotka osuvat valitun aikavälin sisälle, näkyvät.
- Käytä tätä jäljittääksesi, missä esi-isäsi asuivat tietyllä hetkellä historiassa.

## Karttakerrokset

Kerrosvalintapainike (kerroksia pinottu ikoni, vasemmassa alakulmassa) antaa sinun valita kahden peruskartan välillä. Niiden alla se luettelee omat karttakerroksesi "Omat kartat" -otsikon alla (katso [Mukautetut karttakerrokset](#custom-map-overlays) ja [Paikkojen karttatiedostot](#map-files-of-places)) sekä [Wikidata-rakennukset](#wikidata-buildings) -kerroksen "Ulkoiset" -otsikon alla, joita voidaan kytkeä päälle ja pois.

Molempien peruskarttojen nimilaput näkyvät valitsemassasi kielessä Gramps Webissä, jossa karttatiedoilla on nimi kyseisellä kielellä, ja paikallisessa nimessä muuten.

### Peruskartta

Oletuskerros, jota ylläpitää [OpenFreeMap](https://openfreemap.org) (Liberty-tyyli vaaleassa tilassa, tumma tyyli tummassa tilassa). Tämä on moderni yleiskartta, joka soveltuu paikkojen paikantamiseen.

### Historiallinen kartta

Vaihtaa peruskartan [OpenHistoricalMap](https://www.openhistoricalmap.org) (OHM) -karttaan, joka on yhteisöohjattu projekti, joka kartoittaa maailman sellaisena kuin se oli eri aikakausina – ajattele sitä historiallisena vastineena OpenStreetMapille.

Kun historiallinen karttakerros on aktiivinen, aikajousi suodattaa myös karttalaatat itse: OHM renderöi kartan sellaisena kuin se näytti valittuna vuonna, joten historialliset rajat, paikannimet ja ominaisuudet näkyvät modernien sijaan. Tämä mahdollistaa esi-isäsi sijainnin ja nykyaikaisen maantieteellisen ja poliittisen kontekstin näkemisen yhdellä näkymällä.

!!! huomautus
    OpenHistoricalMapin kattavuus vaihtelee alueittain ja aikakausittain. Alueet tai aikakaudet, joilla on harvinaisia panoksia, saattavat näyttää rajoitettua historiallista tietoa. Jos huomaat puuttuvaa tai epätarkkaa historiallista tietoa, harkitse [panostamista OpenHistoricalMapiin](https://www.openhistoricalmap.org) – se on avoin yhteisöprojekti, jota kuka tahansa voi muokata.

## Mukautetut karttakerrokset

Sisäänrakennettujen peruskerrosten lisäksi voit muuttaa minkä tahansa skannatun historiallisesti karttakuva – tallennettuna Grampsissa **Media**-objektina – mukautetuksi kerrokseksi, joka on sijoitettu live-kartalle. Tämä on hyödyllistä vanhojen kaupungin suunnitelmien, seurakuntakarttojen tai kiinteistökarttojen skannauksille, joita haluat verrata suoraan nykyaikaiseen tai historiallisten maantieteisiin.

### Kuvan georeferointi

1. Avaa skannatun karttakuvaan liittyvä mediaobjekti ja vaihda muokkaustilaan.
2. Avaa "Kartta" -välilehti ja napsauta **Muokkaa koordinaatteja**. Tämä avaa georeferointidialogin, jossa on kuva kartan vieressä.
3. Napsauta **Valitse piste kartalta**, sitten napsauta kartalla sijaintia, johon kuvan pisteen tulisi vastata. Kuva sijoitetaan kartalle ensimmäistä kertaa heti, kun piste on valittu.
4. Käytä **Skaala**-liukusäädintä muuttaaksesi kuvan kokoa ja **Läpinäkyvyys**-liukusäädintä nähdäksesi peruskartan sen läpi samalla kun sijoitat.
5. Napsauta **Tasaa kuva** ja napsauta kartalla uudelleen siirtääksesi kuvaa niin, että kiinnitetty piste linjautuu tarkasti.
6. Toista skaala-, läpinäkyvyys- ja tasausvaiheet, kunnes kuva vastaa alla olevaa maantiedettä, ja tallenna sitten.

Taustalla tämä tallentaa kuvan kulma-koordinaatit `map:bounds` -attribuuttiin mediaobjektissa.

### Ylikerrosten tarkastelu Karttasivulla

Kun mediaobjekti on georeferoitu tällä tavalla, se tulee automaattisesti saataville kytkettävänä kerroksena Karttasivulla. Avaa kerrosvalitsin (kerroksia pinottu ikoni, vasemmassa alakulmassa) näyttääksesi tai piilottaaksesi jokaisen ylikerroksen itsenäisesti peruskartasta. Ylikerrokset on lueteltu mediaobjektin otsikon mukaan.

Jokaisella ylikerroksella on läpinäkyvyysliukusäädin sen nimen alla, joten voit nähdä peruskartan sen läpi.

## Paikkojen karttatiedostot

Paikoilla voi olla karttatiedostoja liitettyinä mediaobjekteina – esimerkiksi seurakunnan, alueen tai tilan rajat tai reitti. Tuettuina ovat KML (`.kml`), GeoJSON (`.geojson`) ja GPX (`.gpx`) tiedostot.

Kun valitset paikan kartalla, sen karttatiedostot piirretään kartan päälle käyttäen tiedostossa tallennettuja värejä. Tämä toimii myös paikoille ilman koordinaatteja: kartta zoomaa sitten alueelle, jonka tiedostot kattavat. Kun paikka on valittuna, sen tiedostot luetellaan kerrosvalitsimessa "Omat kartat" -otsikon alla, jossa voit kytkeä jokaisen niistä pois.

Lisätäksesi karttatiedoston paikkaan, lisää se paikan galleriaan kuten mikä tahansa muu [mediafile](media.md).

## Wikidata-rakennukset

"Wikidata-rakennukset" -kerros näyttää [Wikidata](https://www.wikidata.org/) -palveluun tallennettuja rakennuksia, kuten kirkkoja, maatiloja tai kaupungin taloja. Se on pois päältä oletuksena ja voidaan kytkeä päälle kerrosvalitsimessa "Ulkoiset" -otsikon alla. Rakennukset näkyvät vain, kun kartta on tarpeeksi suurennettuna. Kun aikajousi on aktiivinen, vain rakennukset, jotka olivat olemassa valittuna aikana, näkyvät.

Klikkaa rakennusta nähdäksesi sen tiedot Wikidatasta, kuten milloin se rakennettiin tai purettiin, sen osoitteet, asukkaat ja omistajat.

### Rakennuksen tallentaminen paikaksi

Käyttäjät, joilla on oikeus lisätä objekteja, näkevät rakennuksen yksityiskohdissa **Tallenna paikaksi** -painikkeen. Se avaa lomakkeen uudelle paikalle, joka on esitäytetty rakennuksen nimellä omalla kielelläsi, paikantyyppillä (`Maatila` maatiloille, muuten `Rakennus`), sen koordinaateilla ja linkillä Wikidata-objektiin. Täydennä lomake, esimerkiksi valitsemalla ympäröivä paikka, ja tallenna se.

Jos paikka puussasi on samassa sijainnissa kuin rakennus, painike lukee **Avaa tallennettu paikka** sen sijaan ja näyttää sen paikan.

!!! info
    Palvelimen ylläpitäjä voi poistaa Wikidata-rakennukset -kerroksen `mapWikidata` -vaihtoehdolla [frontend-konfiguraatiossa](../install_setup/frontend-config.md).
