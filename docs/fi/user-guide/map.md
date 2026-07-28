# Kartta

Karttasivu näyttää kaikki paikat perhepuussasi interaktiivisina merkkeinä maantieteellisellä kartalla. Se on saatavilla sivupalkista.

## Paikkamerkit

Kartalla näytetään vain paikat, joilla on GPS-koordinaatit tallennettuna Gramps-tietokantaan. Paikat, joilla ei ole koordinaatteja, jätetään hiljaisesti pois. GPS-koordinaatit voidaan asettaa paikan yksityiskohtasivulla (muokkaa paikkaa ja täytä leveys- ja pituusasteen kentät).

!!! vinkki
    Jos monet paikoistasi puuttuvat kartalta, avaa paikan yksityiskohtasivu ja tarkista, onko leveys- ja pituusasteet asetettu. Voit lisätä tai korjata koordinaatteja suoraan paikan muokkausnäkymästä.

Jokainen paikka, jolla on koordinaatit, näytetään merkkinä. Napsauttamalla merkkiä avautuu yhteenvetokortti, jossa näkyy paikan nimi sekä siihen liittyvät tapahtumat ja henkilöt. Napsauta kortin paikan nimeä avataksesi koko paikan yksityiskohtasivun.

## Haku

Karttanäkymän vasemmassa yläkulmassa oleva hakukenttä antaa sinun hypätä mihin tahansa sijaintiin maailmassa nimen perusteella. Tämä ei suodata puun paikkoja – se vain siirtää ja zoomaa karttaa haettuun sijaintiin.

## Aikajana

Sivun alaosassa oleva aikajanan liukusäädin suodattaa, mitkä paikkamerkit näkyvät niiden liitettyjen tapahtumien vuoden perusteella:

- Vedä kahvaa valitaksesi vuosi.
- Näytetään vain paikat, jotka liittyvät tapahtumiin, jotka sijoittuvat valitun aikavälin sisälle.
- Käytä tätä jäljittääksesi, missä esi-isäsi asuivat tietyllä hetkellä historiassa.

## Karttakerrokset

Kerrosvalitsinpainike (pinottujen kerrosten kuvake, vasemmassa alakulmassa) antaa sinun valita kahden peruskartan välillä:

### Peruskartta

Oletuskerros, jota ylläpitää [OpenFreeMap](https://openfreemap.org) (Liberty-tyyli vaaleassa tilassa, tumma tyyli tummassa tilassa). Tämä on moderni yleiskartta, joka sopii paikkojen paikantamiseen.

### Historiallinen kartta

Vaihdetaan peruskartta [OpenHistoricalMap](https://www.openhistoricalmap.org) (OHM), yhteisön ylläpitämä projekti, joka kartoittaa maailman sellaisena kuin se oli eri aikakausina – ajattele sitä historiallisena vastineena OpenStreetMapille.

Kun historiallinen karttakerros on aktiivinen, aikajanan liukusäädin suodattaa myös karttalaatat: OHM renderöi kartan sellaisena kuin se näytti valittuna vuonna, joten historialliset rajat, paikannimet ja ominaisuudet näkyvät nykyaikaisten sijaan. Tämä mahdollistaa sekä esi-isäsi sijainnin että nykyaikaisen maantieteellisen ja poliittisen kontekstin näkemisen yhdellä näkymällä.

!!! huomautus
    OpenHistoricalMapin kattavuus vaihtelee alueittain ja aikakausittain. Alueet tai aikakaudet, joilla on harvinaisia kontribuutioita, saattavat näyttää rajoitettua historiallista tietoa. Jos huomaat puuttuvia tai epätarkkoja historiallisia tietoja, harkitse [kontribuointia OpenHistoricalMapiin](https://www.openhistoricalmap.org) – se on avoin yhteisöprojekti, jota kuka tahansa voi muokata.

## Mukautetut karttapeitteet

Sisäänrakennettujen peruskerrosten lisäksi voit muuttaa minkä tahansa skannatun historiallisesti karttakuvan – tallennettuna Grampsissa **Media**-objektina – mukautetuksi peitteeksi, joka on sijoitettu elävälle kartalle. Tämä on hyödyllistä vanhojen kaupunkisuunnitelmien, seurakuntakarttojen tai kiinteistökarttojen skannauksille, joita haluat verrata suoraan nykyaikaiseen tai historiallisten maantieteeseen.

### Kuvan georeferointi

1. Avaa skannatun karttakuvan mediaobjekti ja vaihda muokkaustilaan.
2. Avaa "Kartta"-välilehti ja napsauta **Muokkaa koordinaatteja**. Tämä avaa georeferointidialogin, jossa on kuva kartan vieressä.
3. Napsauta **Valitse piste kartalta**, ja napsauta sitten kartalla sijaintia, johon kuvan pisteen tulisi vastata. Kuva sijoitetaan kartalle ensimmäistä kertaa heti, kun piste on valittu.
4. Käytä **Mittakaava**-liukusäädintä muuttaaksesi kuvan kokoa ja **Läpinäkyvyys**-liukusäädintä nähdäksesi peruskartan sen läpi samalla kun sijoitat.
5. Napsauta **Tasaa kuva** ja napsauta kartalla uudelleen siirtääksesi kuvaa niin, että kiinnitetty piste on tarkasti linjassa.
6. Toista mittakaava-, läpinäkyvyys- ja tasausvaiheet, kunnes kuva vastaa alla olevaa maantiedettä, ja tallenna sitten.

Kulissien takana tämä tallentaa kuvan kulmakoordinaatit `map:bounds`-attribuuttiin mediaobjektissa.

### Peitteiden tarkastelu Karttasivulla

Kun mediaobjekti on georeferoitu tällä tavalla, se tulee automaattisesti saataville kytkettävänä kerroksena Karttasivulla. Avaa kerrosvalitsin (pinottujen kerrosten kuvake, vasemmassa alakulmassa) näyttääksesi tai piilottaaksesi jokaisen peitteen erikseen peruskartasta. Peitteet on lueteltu mediaobjektin otsikon mukaan.
