# Muutoshistoria

Muutoshistoriankatselu näyttää kaikki muokkaukset, jotka on tehty sukupuuhun.

Luettelonäkymä näyttää muokkaukset ryhmiteltyinä "transaktioihin". Transaktio on ryhmä yhdestä tai useammasta lisäyksestä, poistosta tai muutoksesta Gramps-objekteihin. Esimerkiksi uuden perheen lisääminen, jossa on kaksi olemassa olevaa henkilöä isänä ja äitinä, luo transaktion, jossa on yksi lisätty perhe-objekti ja kaksi muokattua henkilö-objektia (koska ne sisältävät linkin uuteen perhe-objektiin).

Klikkaamalla transaktiota avataan transaktion yksityiskohtanäkymä. Se sisältää luettelon yksittäisistä lisäyksistä, poistosta ja päivityksistä Gramps-objektin mukaan.

Yksittäisen muutoksen valitseminen avaa näkymän Gramps-objektin raakajson-esityksestä, jossa lisäykset ja poistot on korostettu vihreällä ja punaisella, vastaavasti. Painike diffin yläpuolella vie sinut suoraan objektin omalle sivulle.

## Yhden objektin muutokset

Jos haluat nähdä yhden tietyn henkilön, perheen, tapahtuman tai muun objektin historian, avaa sen sivu ja vaihda **Muokkaukset**-välilehteen. Se listaa kaikki muutokset, jotka on tehty kyseiseen objektiin, uusimmasta vanhimpaan, muutoksen tyypin (lisätty, päivitetty tai poistettu), sen käyttäjän, joka sen teki, ja ajankohdan. Klikkaamalla merkintää avataan siihen liittyvä transaktio, jossa voit tarkastella diffiä tai peruuttaa sen.

Klikkaa **Näytä lisää** ladataksesi vanhempia merkintöjä; erittäin pitkän historian omaaville objekteille näytetään vain uusimmat muokkaukset. Jos objekteja on viimeksi muutettu ennen kuin muutoshistoria tallennettiin, välilehti näyttää vain viimeisen muutoksen ajan.

!!! huomautus
    Muokkaukset-välilehti on näkyvissä jäsenille ja sitä korkeammille ja vaatii Gramps Web API -version 3.22 tai uudemman.

## Muutoksen peruuttaminen

Transaktion yksityiskohtasivulla **Peruuta**-painike mahdollistaa kyseisen transaktion kumoamisen. Klikkaamalla sitä tarkistetaan, voidaanko peruuttaminen suorittaa puhtaasti.

**Puhdas peruuttaminen** – jos mikään transaktiossa vaikuttavista objekteista ei ole muuttunut sen jälkeen, peruuttaminen voidaan suorittaa ilman riskiä. Vahvistusdialogi näytetään ja klikkaamalla **Peruuta** kumotaan transaktio.

**Pakotettu peruuttaminen** – jos yksi tai useampi vaikuttava objekti on muutettu myöhemmässä transaktiossa, puhdasta peruuttamista ei voida suorittaa. Dialogi varoittaa, että peruuttamisen pakottaminen voi johtaa tietojen epäjohdonmukaisuuksiin, koska myöhemmät muutokset, jotka riippuvat kyseisistä objekteista, säilytetään ennallaan, vaikka taustalla olevat objektit palautetaan. Voit sitten joko peruuttaa tai klikata **Pakota peruuttaminen** jatkaaksesi silti.

Molemmissa tapauksissa peruuttaminen suoritetaan taustatehtävänä ja edistymisen osoitin näytetään.
