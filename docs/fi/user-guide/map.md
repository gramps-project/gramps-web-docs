# Kartta

Karttasivu näyttää kaikki paikat perhepuussasi interaktiivisina merkkeinä maantieteellisellä kartalla. Se on saatavilla sivupalkista.

## Paikkamerkit

Kartalla näkyvät vain ne paikat, joilla on GPS-koordinaatit tallennettuna Gramps-tietokantaan. Paikat, joilla ei ole koordinaatteja, jätetään hiljaa pois. GPS-koordinaatit voidaan asettaa paikan yksityiskohtasivulla (muokkaa paikkaa ja täytä leveys- ja pituusasteen kentät).

!!! vinkki
    Jos monet paikoistasi puuttuvat kartalta, avaa paikan yksityiskohtasivu ja tarkista, onko leveys- ja pituusasteet asetettu. Voit lisätä tai korjata koordinaatteja suoraan paikan muokkausnäkymästä.

Jokainen paikka, jolla on koordinaatit, näkyy merkkinä. Klikkaamalla merkkiä avautuu yhteenvetokortti, jossa näkyy paikan nimi sekä sen liitetyt tapahtumat ja henkilöt. Klikkaa paikan nimeä kortissa avataksesi koko paikan yksityiskohtasivun.

## Haku

Karttanäkymän vasemmassa yläkulmassa oleva hakukenttä etsii kirjoittaessasi ja ryhmittelee tulokset kolmen otsikon alle:

- **Paikat** – paikat perhepuussasi. Valitsemalla yhden kartta siirtyy siihen ja korostaa sen merkkiä.
- **Ihmiset** – ihmiset perhepuussasi. Valitsemalla yhden kartta vaihtuu henkilön näkymään, joka on kuvattu [alla](#following-a-person-across-the-map).
- **Ulkoiset** – sijainnit [OpenStreetMap](https://www.openstreetmap.org/):sta, mistä tahansa maailmassa. Valitsemalla yhden kartta siirtyy ja zoomaa kyseiseen sijaintiin; se ei suodata tai muuta puusi paikkoja.

Ulkoiset tulokset ovat myös hyödyllisiä, kun lisäät koordinaatteja paikkaan: voit etsiä sijaintia täältä nähdäksesi, missä se sijaitsee ennen kuin syötät sen leveys- ja pituusasteet.

## Seuraaminen kartalla

Valitsemalla henkilön – kartan hakukentästä tai henkilön yksityiskohtasivulla olevan **Avaa kartalla** -painikkeen avulla – näet paikat, jotka liittyvät kyseisen henkilön tapahtumiin, yhdistettyinä viivoilla aikajärjestyksessä. Pienet nuolimerkit jokaisen viivan varrella osoittavat matkustussuunnan, joten voit seurata henkilön elämää syntymästä kuolemaan kartalla.

Paikoilla paikan yksityiskohtasivulla on myös **Avaa kartalla** -painike, joka avaa kartan keskittyen kyseiseen paikkaan.

## Aikajänne

Sivun alareunassa oleva aikajänne suodattaa, mitkä paikkamerkit näkyvät niiden liitettyjen tapahtumien vuoden perusteella:

- Vedä kahvaa valitaksesi vuosi.
- Vain paikat, jotka liittyvät tapahtumiin, jotka kuuluvat valittuun aikaväliin, näkyvät.
- Käytä tätä jäljittääksesi, missä esi-isäsi asuivat tietyllä hetkellä historiassa.

## Karttakerrokset

Kerrosvalintapainike (pinoamaton kerroskuvake, vasemmassa alakulmassa) antaa sinun valita kahden peruskartan välillä. Niiden alla se luettelee omat karttakerroksesi "Omat kartat" -otsikon alla (katso [Mukautetut karttapeitteet](#custom-map-overlays) ja [Paikkojen karttatiedostot](#map-files-of-places)) ja [Wikidata-rakennukset](#wikidata-buildings) -kerroksen "Ulkoiset" -otsikon alla, joista jokainen voidaan kytkeä päälle tai pois.

Molempien peruskarttojen nimilaput näkyvät kielellä, jonka valitsit Gramps Webissä, missä karttatiedoilla on nimi kyseisellä kielellä, ja paikallisella nimellä muuten.

### Peruskartta

Oletuskerros, jota ylläpitää [OpenFreeMap](https://openfreemap.org) (Liberty-tyyli vaaleassa tilassa, tumma tyyli tummassa tilassa). Tämä on moderni yleiskartta, joka sopii paikkojen paikantamiseen.

### Historiallinen kartta

Vaihtaa peruskartan [OpenHistoricalMap](https://www.openhistoricalmap.org):iin (OHM), yhteisövetoinen projekti, joka kartoittaa maailman sellaisena kuin se oli eri aikakausina – ajattele sitä historiallisena vastineena OpenStreetMapille.

Kun historiallinen karttakerros on aktiivinen, aikajänne suodattaa myös itse karttalaatat: OHM renderöi kartan sellaisena kuin se näytti valittuna vuonna, joten historialliset rajat, paikannimet ja piirteet näkyvät nykyaikaisten sijaan. Tämä mahdollistaa sekä esi-isäsi sijainnin että aikakauden maantieteellisen ja poliittisen kontekstin näkemisen yhdellä näkymällä.

!!! huomautus
    OpenHistoricalMapin kattavuus vaihtelee alueittain ja aikakausittain. Alueet tai aikakaudet, joilla on harvinaisia kontribuutioita, saattavat näyttää rajoitettua historiallista tietoa. Jos huomaat puuttuvia tai epätarkkoja historiallisia tietoja, harkitse [kontribuointia OpenHistoricalMapiin](https://www.openhistoricalmap.org) – se on avoin yhteisöprojekti, jota kuka tahansa voi muokata.

## Mukautetut karttapeitteet

Sisäänrakennettujen peruskerrosten lisäksi voit muuttaa minkä tahansa skannatun historiallisten karttakuva – tallennettuna Grampsissa **Media**-objektina – mukautetuksi peitteeksi, joka on sijoitettu live-kartalle. Tämä on hyödyllistä vanhojen kaupunkisuunnitelmien, seurakuntakarttojen tai kiinteistökarttojen skannauksille, joita haluat verrata suoraan nykyaikaiseen tai historiallisten maantieteeseen.

### Kuvan georeferointi

1. Avaa skannatun karttakuva mediaobjekti ja vaihda muokkaustilaan.
2. Avaa "Kartta" -välilehti ja napsauta **Muokkaa koordinaatteja**. Tämä avaa georeferointidialogin, jossa on kuva kartan vieressä.
3. Napsauta **Valitse piste kartalta**, ja napsauta sitten kartalla sijaintia, johon kuvan pisteen tulisi vastata. Kuva sijoitetaan kartalle ensimmäistä kertaa heti, kun piste on valittu.
4. Käytä **Skaala**-liukusäädintä muuttaaksesi kuvan kokoa ja **Läpinäkyvyys**-liukusäädintä nähdäksesi peruskartan sen läpi samalla kun sijoitat.
5. Napsauta **Tasaa kuva** ja napsauta kartalla uudelleen siirtääksesi kuvaa niin, että kiinnitetty piste on tarkasti linjassa.
6. Toista skaala-, läpinäkyvyys- ja tasoittamisvaiheet, kunnes kuva vastaa alla olevaa maantiedettä, ja tallenna.

Taustalla tämä tallentaa kuvan kulmakoordinaatit `map:bounds` -attribuuttiin mediaobjektissa.

### Peitteiden tarkastelu Karttasivulla

Kun mediaobjekti on georeferoitu tällä tavalla, se tulee automaattisesti saataville kytkettävänä kerroksena Karttasivulla. Avaa kerrosvalitsin (pinoamaton kerroskuvake, vasemmassa alakulmassa) näyttääksesi tai piilottaaksesi jokaisen peitteen erikseen peruskartasta. Peitteet on lueteltu mediaobjektin otsikon mukaan.

Jokaisella peitteellä on läpinäkyvyysliukusäädin sen nimen alla, joten voit nähdä peruskartan sen läpi.

## Paikkojen karttatiedostot

Paikoilla voi olla karttatiedostoja liitettyinä mediaobjekteina – esimerkiksi seurakunnan, alueen tai tilan rajat tai reitti. Tuetut tiedostotyypit ovat KML (`.kml`), GeoJSON (`.geojson`) ja GPX (`.gpx`).

Kun valitset paikan kartalla, sen karttatiedostot piirretään kartan päälle käyttäen tiedostossa tallennettuja värejä, jos niitä on. Tämä toimii myös paikoille, joilla ei ole koordinaatteja: kartta zoomaa sitten tiedostojen kattamaan alueeseen. Kun paikka on valittuna, sen tiedostot luetellaan kerrosvalitsimessa "Omat kartat" -otsikon alla, jossa voit kytkeä jokaisen niistä pois.

Lisätäksesi karttatiedoston paikkaan, lisää se paikan galleriaan kuten mikä tahansa muu [mediafile](media.md).

## Wikidata-rakennukset

"Wikidata-rakennukset" -kerros näyttää rakennuksia, jotka on tallennettu [Wikidata](https://www.wikidata.org/):an, kuten kirkkoja, maatiloja tai kaupungin taloja. Se on oletuksena pois päältä ja voidaan kytkeä päälle kerrosvalitsimessa "Ulkoiset" -otsikon alla. Rakennukset näkyvät vain, kun kartta on tarpeeksi lähellä. Kun aikajänne on aktiivinen, näkyvät vain rakennukset, jotka olivat olemassa valittuna aikana.

Klikkaa rakennusta nähdäksesi sen tiedot Wikidatasta, kuten milloin se rakennettiin tai purettiin, sen osoitteet, asukkaat ja omistajat.

### Rakennuksen tallentaminen paikaksi

Käyttäjät, jotka voivat lisätä objekteja, näkevät rakennuksen tiedoissa **Tallenna paikaksi** -painikkeen. Se avaa uuden paikan lomakkeen, joka on esitäytetty rakennuksen nimellä omalla kielelläsi, paikantyyppi (`Farm` maatiloille, muuten `Building`), sen koordinaatit ja linkki Wikidata-objektiin. Täytä lomake, esimerkiksi valitsemalla ympäröivä paikka, ja tallenna se.

Jos paikasi puussasi on samalla sijainnilla kuin rakennus, painike lukee **Avaa tallennettu paikka** sen sijaan ja näyttää tuon paikan.

!!! info
    Palvelimen ylläpitäjä voi poistaa Wikidata-rakennukset -kerroksen `mapWikidata`-vaihtoehdolla [frontend-konfiguraatiossa](../install_setup/frontend-config.md).
