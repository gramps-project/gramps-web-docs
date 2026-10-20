## Varmista perhepuusi varmuuskopiot

Puun omistajat voivat luoda, ladata ja palauttaa täydellisiä varmuuskopioita puusta – mukaan lukien sen asetukset ja käyttäjät – [Varmuuskopiot](settings.md#backups) -osiossa Hallinta-asetuksissa.

Vaihtoehtoisesti, jos haluat luoda varmuuskopion vain perhepuun tiedoista, avaa Vie-sivu Gramps Webissä ja valitse Gramps XML -muoto.

"Näytä" -painiketta napsauttamalla luodaan tiedosto ja aloitetaan lataus, kun se on valmis.

Huomaa, että jos Gramps Web -käyttäjälläsi ei ole oikeuksia nähdä yksityisiä tietoja, vienti ei ole täydellinen varmuuskopio, koska se ei sisällä mitään yksityisiä tietoja.

Tätä Gramps XML -tiedostoa voidaan myöhemmin käyttää puun palauttamiseen tähän tarkkaan tilaan [Palauta varmuuskopiosta](settings.md#restore-from-backup) -toiminnon avulla.

## Jaa perhepuusi muiden sukututkimusohjelmien käyttäjien kanssa

Kun sukututkimustietojen jakaminen Gramps XML -muodossa ei ole vaihtoehto, voit myös viedä GEDCOM-tiedoston. Huomaa, että tämä ei sovellu Gramps Web -puusi varmuuskopioksi.

## Varmista mediasi tiedostot

Varmistaaksesi mediasi tiedostot, voit luoda ja ladata ZIP-arkiston kaikista mediasisällöistä Vie-sivulla.

Huomaa, että erityisesti suurille puille tämä voi olla kallis operaatio palvelimelle, ja se tulisi tehdä vain, jos se on ehdottoman tarpeellista. Tämän vuoksi luotavien media-arkistojen määrä on rajoitettu (oletuksena yksi tunnissa). Jos saavutat rajan, virheilmoitus näyttää sen.

Parempi vaihtoehto varmuuskopioida mediasi tiedostot säännöllisesti on käyttää [Gramps Web Sync -lisäosaa](sync.md) (joka itsessään ei ole varmuuskopioratkaisu) ja luoda incrementaalisia varmuuskopioita paikalliselle tietokoneellesi.

Molemmissa tapauksissa, jos Gramps Web -käyttäjälläsi ei ole oikeuksia nähdä yksityisiä tietoja, vienti ei sisällä yksityisten mediasisältöjen tiedostoja.

## Siirry toiseen Gramps Web -instanssiin

Gramps Web ei lukitse sinua tiettyyn palveluntarjoajaan, ja voit aina siirtyä toiseen Gramps Web -instanssiin menettämättä mitään tietoja, eikä sinulla ole suoraa pääsyä kumpaankaan palvelimeen.

Täydellisen migraation saavuttamiseksi noudata näitä vaiheita (olettaen, että sinulla on puun omistajan oikeudet):

1. Siirry Vie-sivulle ja vie puusi Gramps XML (`.gramps`) -tiedostona. Jos käytät [Sync-lisäosaa](sync.md), voit myös luoda viennin Grampsin työpöytäversiossa.
2. Vie-sivulla luo ja lataa media-arkisto. Jos käytät [Sync-lisäosaa](sync.md), voit myös yksinkertaisesti pakata paikallisen Gramps-media-kansiosi ZIP-muotoon.
3. Siirry Asetukset > Hallinta > Hallitse käyttäjiä ja napsauta "Vie käyttäjätiedot" -painiketta. Se lataa JSON-tiedoston.
4. Uudessa Gramps Web -instanssissa avaa Tuo-sivu. Tuo vaiheessa 1 viety `.gramps`-tiedosto.
5. Uuden Gramps Web -instanssin Tuo-sivulla lataa media-arkisto (ZIP).
6. Siirry Asetukset > Hallinta > Hallitse uuden Gramps Web -instanssin käyttäjiä. Napsauta "Tuo käyttäjätilit" -painiketta ja lataa vaiheessa 3 ladattu JSON-tiedosto.

Huomaa, että vaikka käyttäjätilisi siirretään, kaikkien käyttäjiesi on asetettava uudet salasanat käyttämällä "unohtunut salasana" -linkkiä, koska salasanat tallennetaan salatussa muodossa eivätkä ne voi olla vientitiedostoina.
