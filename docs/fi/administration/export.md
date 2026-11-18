# Viedä data

Vientisivulla voit ladata sukupuu-dataa eri muodoissa sekä arkiston kaikista mediatiedostoista.

## Vie sukupuu Gramps XML -muodossa

Saadaksesi kopion sukupuu-datasta, avaa Vientisivu Gramps Webissä ja valitse Gramps XML -muoto. Napsauta **Generoi** luodaksesi tiedoston ja **Lataa** kun se on valmis. Suuren puun kohdalla tiedoston luominen voi kestää jonkin aikaa; voit jättää sivun sillä välin ja ladata tiedoston myöhemmin sen ilmoituksesta [ilmoitukset](../user-guide/notifications.md).

Huomaa, että jos Gramps Web -käyttäjälläsi ei ole lupaa nähdä yksityisiä tietoja, vienti ei sisällä mitään yksityisiä tietoja.

## Varmuuskopioi sukupuusi

Sukupuun täydellisiä varmuuskopioita – mukaan lukien sen asetukset ja käyttäjät – katso [Varmuuskopioi ja palauta](backups.md). Gramps XML -vienti voi toimia vain sukupuu-datan varmuuskopiona ja se voidaan palauttaa [Palauta varmuuskopiosta](backups.md#restore-from-backup) -toiminnon kautta.

## Jaa sukupuusi muiden sukututkimusohjelmien käyttäjien kanssa

Kun sukututkimustietojen jakaminen Gramps XML -muodossa ei ole vaihtoehto, voit myös viedä GEDCOM-tiedoston. Huomaa, että tämä ei sovellu Gramps Web -puusi varmuuskopioksi.

## Varmuuskopioi mediakansiosi

Varmuuskopioidaksesi mediakansiosi voit luoda ja ladata ZIP-arkiston kaikista mediakansioista Vientisivulla.

Huomaa, että erityisesti suurten puiden kohdalla tämä voi olla kallis operaatio palvelimelle ja se tulisi tehdä vain, jos se on ehdottoman välttämätöntä. Tästä syystä luotavien mediakansioiden määrä on rajoitettu (oletuksena yksi tunnissa). Jos saavutat rajan, virheilmoitus näyttää sen.

Parempi vaihtoehto varmuuskopioida mediakansiosi säännöllisesti on käyttää [Gramps Web Sync -lisäosaa](sync.md) (joka itsessään ei ole varmuuskopioratkaisu) ja luoda inkrementaalisia varmuuskopioita paikalliselle tietokoneellesi.

Molemmissa tapauksissa, jos Gramps Web -käyttäjälläsi ei ole lupaa nähdä yksityisiä tietoja, vienti ei sisällä yksityisten mediakohteiden tiedostoja.

## Siirry toiseen Gramps Web -instanssiin

Gramps Web ei lukitse sinua tiettyyn palveluntarjoajaan, ja voit aina siirtyä toiseen Gramps Web -instanssiin menettämättä mitään tietoja, eikä sinulla ole suoraa pääsyä kummallekaan palvelimelle.

Täydellisen siirron saavuttamiseksi seuraa näitä vaiheita (olettaen, että sinulla on puun omistajan oikeudet):

1. Siirry Vientisivulle ja vie puusi Gramps XML (`.gramps`) -tiedostona. Jos käytät [Sync-lisäosaa](sync.md), voit myös luoda viennin Grampsin työpöytäversiossa.
2. Vientisivulla luo ja lataa mediakansio. Jos käytät [Sync-lisäosaa](sync.md), voit myös yksinkertaisesti pakata paikallisen Gramps-mediakansiosi ZIP-muotoon.
3. Siirry Asetukset > Hallinta > Hallitse käyttäjiä ja napsauta "Vie käyttäjätiedot" -painiketta. Se lataa JSON-tiedoston.
4. Uudessa Gramps Web -instanssissa avaa [Tuontisivu](import.md). Tuo vaiheessa 1 viety `.gramps` -tiedosto.
5. Uuden Gramps Web -instanssin Tuontisivulla lataa mediakansio (ZIP) [Tuo mediakansioita](import-media.md) -kohdassa.
6. Siirry Asetukset > Hallinta > Hallitse käyttäjiä uudessa Gramps Web -instanssissa. Napsauta "Tuo käyttäjätilit" -painiketta ja lataa vaiheessa 3 ladattu JSON-tiedosto.

Huomaa, että vaikka käyttäjätilisi siirretään, kaikkien käyttäjiesi on asetettava uudet salasanat käyttämällä "unohtunut salasana" -linkkiä, koska salasanat tallennetaan salattuna eikä niitä voida viedä.
