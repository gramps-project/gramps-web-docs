# Kartta

Karttasivu näyttää kaikki paikat perhepuussasi interaktiivisina merkkeinä maantieteellisellä kartalla. Se on saatavilla sivupalkista.

## Paikkamerkit

Kartalla näytetään vain paikat, joilla on GPS-koordinaatit tallennettuna Gramps-tietokantaan. Paikat, joilla ei ole koordinaatteja, jätetään hiljaa pois. GPS-koordinaatit voidaan asettaa paikan yksityiskohtasivulla (muokkaa paikkaa ja täytä leveys- ja pituusasteen kentät).

!!! tip
    Jos monet paikoistasi puuttuvat kartalta, avaa paikan yksityiskohtasivu ja tarkista, onko leveys- ja pituusasteet asetettu. Voit lisätä tai korjata koordinaatteja suoraan paikan muokkausnäkymästä.

Jokainen paikka, jolla on koordinaatit, näytetään merkkinä. Klikkaamalla merkkiä avautuu yhteenvetokortti, jossa näkyy paikan nimi sekä siihen liittyvät tapahtumat ja henkilöt. Klikkaa paikan nimeä kortissa avataksesi koko paikan yksityiskohtasivun.

## Haku

Karttan vasemmassa yläkulmassa oleva hakukenttä antaa sinun hypätä mihin tahansa sijaintiin maailmassa nimen perusteella. Tämä ei suodata puun paikkoja – se vain liikuttaa ja zoomaa karttaa haettuun sijaintiin.

## Aikajousto

Sivun alareunassa oleva aikajousto suodattaa, mitkä paikkamerkit näytetään niiden liitettyjen tapahtumien vuoden perusteella:

- Vedä kahvaa valitaksesi vuosi.
- Vain paikat, jotka liittyvät tapahtumiin, jotka osuvat valitun aikavälin sisälle, näytetään.
- Käytä tätä jäljittääksesi, missä esi-isäsi asuivat tietyllä hetkellä historiassa.

## Karttakerrokset

Kerrosvalintapainike (kerrostetut kerrokset -ikoni, vasemmassa alakulmassa) antaa sinun valita kahden peruskartan välillä:

### Peruskartta

Oletuskerros, jota tukee [OpenFreeMap](https://openfreemap.org) (Liberty-tyyli vaaleassa tilassa, tumma tyyli tummassa tilassa). Tämä on moderni yleiskartta, joka soveltuu paikkojen paikantamiseen.

### Historiallinen kartta

Vaihda peruskartta [OpenHistoricalMap](https://www.openhistoricalmap.org) (OHM) -karttaan, joka on yhteisön ylläpitämä projekti, joka kartoittaa maailman sellaisena kuin se oli eri aikapisteissä – ajattele sitä historiallisena vastineena OpenStreetMapille.

Kun historiallinen karttakerros on aktiivinen, aikajousto suodattaa myös karttalaatat: OHM renderöi kartan sellaisena kuin se näytti valittuna vuonna, joten historialliset rajat, paikan nimet ja ominaisuudet näkyvät nykyaikaisten sijaan. Tämä mahdollistaa esi-isäsi sijainnin ja nykyaikaisen maantieteellisen ja poliittisen kontekstin näkemisen yhdellä näkymällä.

!!! note
    OpenHistoricalMapin kattavuus vaihtelee alueittain ja aikakausittain. Alueet tai aikakaudet, joilla on harvinaisia kontribuutioita, saattavat näyttää rajoitettua historiallista tietoa. Jos huomaat puuttuvaa tai epätarkkaa historiallista tietoa, harkitse [kontribuointia OpenHistoricalMapiin](https://www.openhistoricalmap.org) – se on avoin yhteisöprojekti, jota kuka tahansa voi muokata.
