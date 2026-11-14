# Vienti

Vienti-sivu antaa sinun ladata sukupuu-tiedot eri muodoissa sekä arkiston kaikista mediatiedostoista.

## Vie sukupuu Gramps XML -muodossa

Saadaksesi kopion sukupuu-tiedoista, avaa Vienti-sivu Gramps Webissä ja valitse Gramps XML -muoto. Klikkaamalla "vienti" luodaan tiedosto ja lataus alkaa, kun se on valmis.

Huomaa, että jos Gramps Web -käyttäjälläsi ei ole lupaa nähdä yksityisiä tietoja, vienti ei sisällä mitään yksityisiä tietoja.

## Varmuuskopioi sukupuusi

Sukupuun täydellisiä varmuuskopioita varten – mukaan lukien sen asetukset ja käyttäjät – katso [Varmuuskopioi ja palauta](backups.md). Gramps XML -vienti voi toimia vain sukupuu-tietojen varmuuskopiona ja se voidaan palauttaa [Palauta varmuuskopiosta](backups.md#restore-from-backup) -toiminnolla.

## Jaa sukupuusi muiden sukututkimusohjelmien käyttäjien kanssa

Kun sukututkimustietojen jakaminen Gramps XML -muodossa ei ole vaihtoehto, voit myös viedä GEDCOM-tiedoston. Huomaa, että tämä ei sovellu Gramps Web -sukupuusi varmuuskopioksi.

## Varmuuskopioi mediatafilesi

Varmuuskopioidaksesi mediatafilesi voit luoda ja ladata ZIP-arkiston kaikista mediatafileista Vienti-sivulla.

Huomaa, että erityisesti suurille puille tämä voi olla kallis operaatio palvelimelle, ja se tulisi tehdä vain, jos se on ehdottoman tarpeellista. Tästä syystä luotavien media-arkistojen määrä on rajoitettu (oletuksena yksi tunnissa). Jos saavut rajan, virheilmoitus näyttää sen.

Parempi vaihtoehto varmuuskopioida mediatafilesi säännöllisesti on käyttää [Gramps Web Sync -lisäosaa](sync.md) (joka itsessään ei ole varmuuskopioratkaisu) ja luoda inkrementaalisia varmuuskopioita paikalliselle tietokoneellesi.

Molemmissa tapauksissa, jos Gramps Web -käyttäjälläsi ei ole lupaa nähdä yksityisiä tietoja, vienti ei sisällä tiedostoja yksityisistä mediakohteista.

## Siirry toiseen Gramps Web -instanssiin

Gramps Web ei lukitse sinua tiettyyn palveluntarjoajaan, ja voit aina siirtyä toiseen Gramps Web -instanssiin menettämättä mitään tietoja, eikä sinulla ole suoraa pääsyä kumpaankaan palvelimeen.

Täydellisen siirron saavuttamiseksi seuraa näitä vaiheita (olettaen, että sinulla on puun omistajan oikeudet):

1. Siirry Vienti-sivulle ja vie puusi Gramps XML (`.gramps`) -tiedostona. Jos käytät [Sync-lisäosaa](sync.md), voit myös luoda viennin Grampsin työpöytäversiossa.
2. Vienti-sivulla luo ja lataa media-arkisto. Jos käytät [Sync-lisäosaa](sync.md), voit myös yksinkertaisesti ZIP-tiedostaa paikallisen Gramps-mediakansiosi.
3. Siirry Asetukset > Hallinta > Hallitse käyttäjiä ja napsauta "Vie käyttäjätiedot" -painiketta. Se lataa JSON-tiedoston.
4. Uudessa Gramps Web -instanssissa avaa Tuonti-sivu. Tuo `.gramps`-tiedosto, joka viedään vaiheessa 1.
5. Uuden Gramps Web -instanssin Tuonti-sivulla lataa media-arkisto (ZIP).
6. Siirry Asetukset > Hallinta > Hallitse käyttäjiä uuden Gramps Web -instanssin. Napsauta "Tuo käyttäjätilit" -painiketta ja lataa vaiheessa 3 ladattu JSON-tiedosto.

Huomaa, että vaikka käyttäjätilisi siirretään, kaikkien käyttäjiesi on asetettava uudet salasanat käyttämällä "unohtunut salasana" -linkkiä, koska salasanat tallennetaan salattuna ja niitä ei voida viedä.
