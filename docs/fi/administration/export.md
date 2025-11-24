## Varmista perhepuusi varmuuskopio

Luodaksesi varmuuskopion perhepuustasi, avaa vientisivu Gramps Webissä ja valitse Gramps XML -muoto.

"Näytä vienti" -painiketta napsauttamalla luodaan tiedosto ja lataus alkaa, kun se on valmis.

Huomaa, että jos Gramps Web -käyttäjälläsi ei ole oikeuksia nähdä yksityisiä tietoja, vienti ei ole täydellinen varmuuskopio, koska se ei sisällä mitään yksityisiä tietoja.

## Jaa perhepuusi muiden sukututkimusohjelmien käyttäjien kanssa

Kun sukututkimustietojen jakaminen Gramps XML -muodossa ei ole vaihtoehto, voit myös viedä GEDCOM-tiedoston. Huomaa, että tämä ei sovellu Gramps Web -puusi varmuuskopioksi.

## Varmista mediatiedostosi

Varmistaaksesi mediatiedostosi voit luoda ja ladata ZIP-arkiston kaikista mediakuvista vientisivulla.

Huomaa, että erityisesti suurten puiden osalta tämä voi olla kallis operaatio palvelimelle, ja se tulisi tehdä vain, jos se on ehdottoman tarpeellista.

Parempi vaihtoehto varmuuskopioida mediakuvasi säännöllisesti on käyttää [Gramps Web Sync -lisäosaa](sync.md) (joka itsessään ei ole varmuuskopioratkaisu) ja luoda incrementaalisia varmuuskopioita paikalliselle tietokoneellesi.

Molemmissa tapauksissa, jos Gramps Web -käyttäjälläsi ei ole oikeuksia nähdä yksityisiä tietoja, vienti ei sisällä yksityisten mediakohteiden tiedostoja.

## Siirry toiseen Gramps Web -instanssiin

Gramps Web ei lukitse sinua tiettyyn palveluntarjoajaan, ja voit aina siirtyä toiseen Gramps Web -instanssiin ilman tietojen häviämistä ja ilman suoraa pääsyä kumpaankaan palvelimeen.

Täydellisen siirron saavuttamiseksi noudata näitä vaiheita (olettaen, että sinulla on puun omistajan oikeudet):

1. Siirry vientisivulle ja vie puusi Gramps XML (`.gramps`) -tiedostona. Jos käytät [Sync-lisäosaa](sync.md), voit myös luoda viennin Gramps-työpöydällä.
2. Vientisivulla luo ja lataa mediakuvien arkisto. Jos käytät [Sync-lisäosaa](sync.md), voit myös yksinkertaisesti ZIP-tiedostaa paikallisen Gramps-mediakansiosi.
3. Siirry kohtaan Asetukset > Hallinta > Hallitse käyttäjiä ja napsauta "Vie käyttäjätiedot" -painiketta. Se lataa JSON-tiedoston.
4. Uudessa Gramps Web -instanssissa avaa tuontisivu. Tuo vaiheessa 1 viety `.gramps` -tiedosto.
5. Uuden Gramps Web -instanssin tuontisivulla lataa mediakuvien arkisto (ZIP).
6. Siirry kohtaan Asetukset > Hallinta > Hallitse uuden Gramps Web -instanssin käyttäjiä. Napsauta "Tuo käyttäjätilit" -painiketta ja lataa vaiheessa 3 ladattu JSON-tiedosto.

Huomaa, että vaikka käyttäjätilisi siirretään, kaikkien käyttäjiesi on asetettava uudet salasanat käyttämällä "unohtunut salasana" -linkkiä, koska salasanat tallennetaan salattuna eivätkä ne voi olla vientiä varten.
