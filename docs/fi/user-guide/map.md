# Kartta

Karttasivu näyttää kaikki paikat perhepuussasi interaktiivisina merkkeinä maantieteellisellä kartalla. Se on saatavilla sivupalkista.

## Paikkamerkit

Vain paikat, joilla on GPS-koordinaatit tallennettuna Gramps-tietokantaan, näkyvät kartalla. Paikat ilman koordinaatteja jätetään hiljaa pois. GPS-koordinaatit voidaan asettaa paikan tietosivulla (muokkaa paikkaa ja täytä leveys- ja pituusasteen kentät).

!!! vinkki
    Jos monet paikoistasi puuttuvat kartalta, avaa paikan tietosivu ja tarkista, onko leveys- ja pituusasteet asetettu. Voit lisätä tai korjata koordinaatteja suoraan paikan muokkausnäkymästä.

Jokainen paikka, jolla on koordinaatit, näkyy merkkinä. Klikkaamalla merkkiä avautuu yhteenvetokortti, jossa näkyy paikan nimi sekä siihen liittyvät tapahtumat ja henkilöt. Klikkaa paikan nimeä kortissa avataksesi koko paikan tietosivun.

## Haku

Karttanäkymän vasemmassa yläkulmassa oleva hakukenttä etsii kirjoittaessasi ja ryhmittelee tulokset kolmeen otsikkoon:

- **Paikat** – paikat perhepuussasi. Valitsemalla yhden kartta siirtyy siihen ja korostaa sen merkkiä.
- **Henkilöt** – henkilöt perhepuussasi. Valitsemalla yhden kartta siirtyy henkilön näkymään, joka on kuvattu [alla](#following-a-person-across-the-map).
- **Ulkoiset** – sijainnit [OpenStreetMap](https://www.openstreetmap.org/):ista, mistä tahansa maailmassa. Valitsemalla yhden kartta siirtyy ja zoomaa kyseiseen sijaintiin; se ei suodata tai muuta puusi paikkoja.

Ulkoiset tulokset ovat myös hyödyllisiä, kun lisäät koordinaatteja paikkaan: voit etsiä sijaintia täältä nähdäksesi, missä se sijaitsee ennen kuin syötät sen leveys- ja pituusasteet.

## Henkilön seuraaminen kartalla

Henkilön valitseminen – kartan hakukentästä tai **Avaa kartassa** -painikkeella henkilön tietosivulla – näyttää paikat, jotka liittyvät kyseisen henkilön tapahtumiin, yhdistettyinä viivoilla aikajärjestyksessä. Pienet nuolet jokaisen viivan varrella osoittavat matkasuunnan, joten voit seurata henkilön elämää syntymästä kuolemaan kartalla.

Paikoilla paikan tietosivulla on myös **Avaa kartassa** -painike, joka avaa kartan keskittyen kyseiseen paikkaan.

## Aikajousi

Sivun alareunassa oleva aikajousi suodattaa, mitkä paikkamerkit näkyvät niiden liittyvien tapahtumien vuoden perusteella:

- Vedä kahvaa valitaksesi vuosi.
- Vain paikat, jotka liittyvät tapahtumiin, jotka kuuluvat valittuun aikaväliin, näkyvät.
- Käytä tätä jäljittääksesi, missä esi-isäsi asuivat tietyllä hetkellä historiassa.

## Karttakerrokset

Kerrosvalitsinpainike (kerroksittain pinottu ikoni, vasemmassa alakulmassa) antaa sinun valita kahden peruskartan välillä. Niiden alla se listaa omat karttakerroksesi "Omat kartat" -otsikon alla (katso [Mukautetut karttakerrokset](#custom-map-overlays) ja [Paikkojen karttatiedostot](#map-files-of-places)) ja [Wikidata-rakennukset](#wikidata-buildings) -kerroksen "Ulkoiset" -otsikon alla, jotka voidaan kytkeä päälle ja pois.

Molempien peruskarttojen nimilaput näkyvät valitsemassasi kielessä Gramps Webissä, jossa karttatiedoilla on nimi kyseisellä kielellä, ja paikallisessa nimessä muuten.

### Peruskartta

Oletuskerros, jota ylläpitää [OpenFreeMap](https://openfreemap.org) (Liberty-tyyli vaaleassa tilassa, tumma tyyli tummassa tilassa). Tämä on moderni yleiskartta, joka soveltuu paikkojen paikantamiseen.

### Historiallinen kartta

Vaihda peruskartta [OpenHistoricalMap](https://www.openhistoricalmap.org):iin (OHM), yhteisön ylläpitämään projektiin, joka kartoittaa maailmaa eri aikakausina – ajattele sitä historiallisena vastineena OpenStreetMapille.

Kun historiallinen karttakerros on aktiivinen, aikajousi suodattaa myös itse karttalaatat: OHM renderöi kartan sellaisena kuin se näytti valittuna vuonna, joten historialliset rajat, paikannimet ja ominaisuudet näkyvät modernien sijaan. Tämä mahdollistaa sekä esi-isäsi sijainnin että nykyaikaisen maantieteellisen ja poliittisen kontekstin näkemisen yhdellä näkymällä.

!!! huomautus
    OpenHistoricalMapin kattavuus vaihtelee alueittain ja aikakausittain. Alueet tai aikakaudet, joilla on harvinaisia kontribuutioita, saattavat näyttää rajoitettua historiallista tietoa. Jos huomaat puuttuvaa tai epätarkkaa historiallista dataa, harkitse [kontribuoimista OpenHistoricalMapiin](https://www.openhistoricalmap.org) – se on avoin yhteisöprojekti, jota kuka tahansa voi muokata.

## Mukautetut karttakerrokset

Sisäänrakennettujen peruskerrosten lisäksi voit muuttaa minkä tahansa skannatun historiallisten karttakuva – tallennettuna Grampsissa **Media**-objektina – mukautetuksi kerrokseksi, joka on sijoitettu live-kartalle. Tämä on hyödyllistä vanhojen kaupunkisuunnitelmien, seurakuntakarttojen tai kiinteistökarttojen skannauksille, joita haluat verrata suoraan nykyaikaiseen tai historiallisten maantieteeseen.

### Kuvan georeferointi

1. Avaa skannatun karttakuva mediaobjekti ja vaihda muokkaustilaan.
2. Avaa "Kartta"-välilehti ja napsauta **Muokkaa koordinaatteja**. Tämä avaa georeferointidialogin, jossa on kuva kartan vieressä.
3. Napsauta **Valitse piste kartalta**, sitten napsauta kartalla sijaintia, johon kuvan pisteen tulisi vastata. Kuva sijoitetaan kartalle ensimmäisen kerran heti, kun piste on valittu.
4. Käytä **Skaala**-liukusäädintä muuttaaksesi kuvan kokoa ja **Läpinäkyvyys**-liukusäädintä nähdäksesi peruskartan sen läpi samalla kun sijoitat.
5. Napsauta **Tasaa kuva** ja napsauta kartalla uudelleen siirtääksesi kuvaa niin, että kiinnitetty piste on tarkasti linjassa.
6. Toista skaala-, läpinäkyvyys- ja tasoaskelia, kunnes kuva vastaa alla olevaa maantiedettä, ja tallenna sitten.

Taustalla tämä tallentaa kuvan kulmakoordinaatit `map:bounds`-attribuuttiin mediaobjektissa.

### Ylitysten tarkastelu Karttasivulla

Kun mediaobjekti on georeferoitu tällä tavalla, se tulee automaattisesti saataville kytkettävänä kerroksena Karttasivulla. Avaa kerrosvalitsin (kerroksittain pinottu ikoni, vasemmassa alakulmassa) näyttääksesi tai piilottaaksesi jokaisen ylityksen erikseen peruskartasta. Ylitykset on listattu mediaobjektin otsikon mukaan.

## Paikkojen karttatiedostot

Paikoilla voi olla karttatiedostoja liitettyinä mediaobjekteina – esimerkiksi seurakunnan, alueen tai tilan rajat tai reitti. Tuettuina ovat KML (`.kml`), GeoJSON (`.geojson`) ja GPX (`.gpx`) tiedostot.

Kun valitset paikan kartalla, sen karttatiedostot piirretään kartan päälle, käyttäen tiedostossa tallennettuja värejä, jos niitä on. Tämä toimii myös paikoille ilman koordinaatteja: kartta zoomaa sitten tiedostojen kattamalle alueelle. Kun paikka on valittuna, sen tiedostot on listattu kerrosvalitsimessa "Omat kartat" -otsikon alla, jossa voit kytkeä jokaisen niistä pois.

Lisätäksesi karttatiedoston paikkaan, lisää se paikan galleriaan kuten mikä tahansa muu [mediafile](media.md).

## Wikidata-rakennukset

"Wikidata-rakennukset" -kerros näyttää rakennuksia, jotka on kirjattu [Wikidata](https://www.wikidata.org/):an, kuten kirkkoja, maatiloja tai kaupunkitaloja. Se on oletuksena pois päältä ja voidaan kytkeä päälle kerrosvalitsimessa "Ulkoiset" -otsikon alla. Rakennukset näkyvät vain, kun kartta on tarpeeksi suurennettuna. Kun aikajousi on aktiivinen, näkyvät vain rakennukset, jotka olivat olemassa valittuna aikana.

Napsauta rakennusta nähdäksesi sen tiedot Wikidatasta, kuten milloin se rakennettiin tai purettiin, sen osoitteet, asukkaat ja omistajat.

### Rakennuksen tallentaminen paikaksi

Käyttäjät, joilla on oikeus lisätä objekteja, näkevät rakennuksen tiedoissa **Tallenna paikaksi** -painikkeen. Se avaa lomakkeen uudelle paikalle, joka on esitäytetty rakennuksen nimellä omalla kielelläsi, paikantyyppillä (`Maatila` maatiloille, muuten `Rakennus`), sen koordinaateilla ja linkillä Wikidata-objektiin. Täytä lomake, esimerkiksi valitsemalla ympäröivä paikka, ja tallenna se.

Jos paikassa puussasi on sama sijainti kuin rakennuksessa, painike lukee **Avaa tallennettu paikka** sen sijaan ja näyttää sen paikan.

!!! info
    Palvelimen ylläpitäjä voi poistaa Wikidata-rakennukset -kerroksen `mapWikidata`-vaihtoehdolla [frontend-konfiguraatiossa](../install_setup/frontend-config.md).
