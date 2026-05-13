# Muutoshistoria

Muutoshistoriankatsaus näyttää kaikki perhepuuhun tehdyt muokkaukset.

Luettelonäkymä näyttää muokkaukset ryhmiteltyinä "transaktioihin". Transaktio on ryhmä yhdestä tai useammasta lisäyksestä, poistosta tai muutoksesta Gramps-objekteihin. Esimerkiksi uuden perheen lisääminen, jossa on kaksi olemassa olevaa henkilöä isänä ja äitinä, luo transaktion, jossa on yksi lisätty perhe-objekti ja kaksi muokattua henkilö-objektia (koska ne sisältävät linkin uuteen perhe-objektiin).

Klikkaamalla transaktiota avautuu transaktion yksityiskohtien näkymä. Siinä on luettelo yksittäisistä lisäyksistä, poistosta ja päivityksistä Gramps-objekteittain.

Valitsemalla yksittäisen muutoksen avautuu näkymä Gramps-objektin raakajson-esityksestä, jossa lisäykset ja poistot on korostettu vihreällä ja punaisella, vastaavasti.

## Muutoksen kumoaminen

Transaktion yksityiskohtien sivulla **Kumoa**-painike antaa sinun peruuttaa kyseisen transaktion. Klikkaamalla sitä tarkistetaan, voidaanko kumoaminen suorittaa puhtaasti.

**Puhdas kumoaminen** – jos mikään transaktiossa vaikuttavista objekteista ei ole muuttunut sen jälkeen, kumoaminen voidaan suorittaa ilman riskiä. Vahvistusdialogi näytetään ja klikkaamalla **Kumoa** peruutetaan transaktio.

**Pakotettu kumoaminen** – jos yksi tai useampi vaikuttava objekti on muutettu myöhemmässä transaktiossa, puhdasta kumoamista ei voida suorittaa. Dialogi varoittaa, että kumoamisen pakottaminen voi johtaa tietojen epäjohdonmukaisuuksiin, koska myöhemmät muutokset, jotka riippuvat kyseisistä objekteista, säilytetään sellaisinaan, vaikka taustalla olevat objektit palautetaan. Voit sitten joko peruuttaa tai klikata **Pakota kumoaminen** jatkaaksesi silti.

Molemmissa tapauksissa kumoaminen suoritetaan taustatehtävänä ja edistymisen osoitin näytetään.
