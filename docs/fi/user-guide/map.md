# Kartta

Karttasivu näyttää kaikki paikat perhepuussasi interaktiivisina merkkeinä maantieteellisellä kartalla. Se on saatavilla sivupalkista.

## Paikkamerkit

Vain paikat, joilla on GPS-koordinaatit tallennettuna Gramps-tietokantaan, näkyvät kartalla. Paikat ilman koordinaatteja jätetään hiljaa pois. GPS-koordinaatit voidaan asettaa paikan yksityiskohtasivulla (muokkaa paikkaa ja täytä leveys- ja pituusasteen kentät).

!!! vinkki
    Jos monet paikoistasi puuttuvat kartalta, avaa paikan yksityiskohtasivu ja tarkista, onko leveys- ja pituusasteet asetettu. Voit lisätä tai korjata koordinaatteja suoraan paikan muokkausnäkymästä.

Jokainen paikka, jolla on koordinaatit, näkyy merkkinä. Klikkaamalla merkkiä avautuu yhteenvetokortti, jossa näkyy paikan nimi sekä sen liitetyt tapahtumat ja henkilöt. Klikkaa paikan nimeä kortissa avataksesi koko paikan yksityiskohtasivun.

## Haku

Karttanäkymän vasemmassa yläkulmassa oleva hakukenttä etsii kirjoittaessasi ja ryhmittelee tulokset kolmen otsikon alle:

- **Paikat** – paikat perhepuussasi. Valitsemalla yhden kartta siirtyy siihen ja korostaa sen merkkiä.
- **Henkilöt** – henkilöt perhepuussasi. Valitsemalla yhden kartta vaihtuu henkilön näkymään, joka on kuvattu [alla](#seuraaminen-henkilön-kautta-kartalla).
- **Ulkoiset** – sijainnit [OpenStreetMap](https://www.openstreetmap.org/) -palvelusta, mistä tahansa maailmassa. Valitsemalla yhden kartta siirtyy ja zoomaa kyseiseen sijaintiin; se ei suodata tai muuta puusi paikkoja.

Ulkoiset tulokset ovat myös hyödyllisiä, kun lisäät koordinaatteja paikkaan: voit etsiä sijaintia täältä nähdäksesi, missä se sijaitsee ennen kuin syötät sen leveys- ja pituusasteet.

## Seuraaminen henkilön kautta kartalla

Henkilön valitseminen – kartan hakukentästä tai henkilön yksityiskohtasivun **Avaa kartalla** -painikkeella – näyttää paikat, jotka liittyvät kyseisen henkilön tapahtumiin, yhdistettyinä viivoilla aikajärjestyksessä. Pienet nuolet jokaisella viivalla osoittavat matkasuunnan, joten voit seurata henkilön elämää syntymästä kuolemaan kartalla.

Paikoilla paikan yksityiskohtasivulla on myös **Avaa kartalla** -painike, joka avaa kartan keskittyen kyseiseen paikkaan.

## Aikajänne

Sivun alareunassa oleva aikajänne suodattaa, mitkä paikkamerkit näkyvät niiden liitettyjen tapahtumien vuoden perusteella:

- Vedä kahvaa valitaksesi vuosi.
- Vain paikat, jotka liittyvät tapahtumiin, jotka osuvat valitun aikavälin sisälle, näkyvät.
- Käytä tätä jäljittääksesi, missä esi-isäsi asuivat tietyllä aikakaudella.

## Karttakerrokset

Kerrosvalintapainike (kerroksia pinottu kuvake, vasemmassa alakulmassa) antaa sinun valita kahden peruskartan välillä:

### Peruskartta

Oletuskerros, jota ylläpitää [OpenFreeMap](https://openfreemap.org) (Liberty-tyyli vaaleassa tilassa, tumma tyyli tummassa tilassa). Tämä on moderni yleiskartta, joka soveltuu paikkojen paikantamiseen.

### Historiallinen kartta

Vaihda peruskartta [OpenHistoricalMap](https://www.openhistoricalmap.org) (OHM) -palveluun, yhteisöohjattuun projektiin, joka kartoittaa maailman sellaisena kuin se oli eri aikakausina – ajattele sitä historiallisena vastineena OpenStreetMapille.

Kun historiallinen karttakerros on aktiivinen, aikajänne suodattaa myös karttalaatat: OHM renderöi kartan sellaisena kuin se näytti valittuna vuonna, joten historialliset rajat, paikannimet ja piirteet näkyvät nykyaikaisten sijaan. Tämä mahdollistaa sekä esi-isäsi sijainnin että nykyaikaisen maantieteellisen ja poliittisen kontekstin näkemisen yhdellä näkymällä.

!!! huomautus
    OpenHistoricalMapin kattavuus vaihtelee alueittain ja aikakausittain. Alueet tai aikakaudet, joilla on harvinaisia kontribuutioita, saattavat näyttää rajoitettua historiallista tietoa. Jos huomaat puuttuvaa tai epätarkkaa historiallista tietoa, harkitse [kontribuointia OpenHistoricalMapiin](https://www.openhistoricalmap.org) – se on avoin yhteisöprojekti, jota kuka tahansa voi muokata.

## Mukautetut karttatehosteet

Sisäänrakennettujen peruskerrosten lisäksi voit muuttaa minkä tahansa skannatun historiallisesti karttakuva – tallennettuna Grampsissa **Media**-objektina – mukautetuksi tehosteeksi, joka on sijoitettu elävälle kartalle. Tämä on hyödyllistä vanhojen kaupunkisuunnitelmien, seurakuntakarttojen tai kiinteistökarttojen skannauksille, joita haluat verrata suoraan nykyaikaiseen tai historiallisten maantieteeseen.

### Kuvan georeferointi

1. Avaa skannatun karttakuvaan liittyvä mediaobjekti ja vaihda muokkaustilaan.
2. Avaa "Kartta"-välilehti ja napsauta **Muokkaa koordinaatteja**. Tämä avaa georeferointidialogin, jossa on kuva ja kartta vierekkäin.
3. Napsauta **Valitse piste kartalta**, ja napsauta sitten kartalla sijaintia, johon kuvan pisteen tulisi vastata. Kuva sijoitetaan kartalle ensimmäistä kertaa heti, kun piste on valittu.
4. Käytä **Skaala**-liukusäädintä muuttaaksesi kuvan kokoa ja **Läpinäkyvyys**-liukusäädintä nähdäksesi peruskartan sen läpi sijoittamisen aikana.
5. Napsauta **Tasaa kuva** ja napsauta kartalla uudelleen siirtääksesi kuvaa niin, että kiinnitetty piste kohdistuu tarkasti.
6. Toista skaala-, läpinäkyvyys- ja tasausvaiheet, kunnes kuva vastaa alla olevaa maantiedettä, ja tallenna sitten.

Taustalla tämä tallentaa kuvan kulmakoordinaatit `map:bounds` -attribuuttiin mediaobjektissa.

### Tehosteiden tarkastelu Karttasivulla

Kun mediaobjekti on georeferoitu tällä tavalla, se tulee automaattisesti saataville kytkettävänä kerroksena Karttasivulla. Avaa kerrosvalitsin (kerroksia pinottu kuvake, vasemmassa alakulmassa) näyttääksesi tai piilottaaksesi jokaisen tehosteen erikseen peruskartasta. Tehosteet on lueteltu mediaobjektin otsikon mukaan.
