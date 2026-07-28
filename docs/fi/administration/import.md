## Valmistele Gramps-tietokantaasi

Jos käytät Gramps Desktopia, on kaksi vaihetta, joilla voit valmistella tietokantaasi varmistaaksesi, että kaikki sujuu ongelmitta seuraavassa. Jos siirryt toisesta sukututkimusohjelmasta, voit ohittaa tämän vaiheen.

1. Tarkista ja korjaa tietokanta
    - Valinnainen: luo tietokannan varmuuskopio viemällä se Gramps XML:ään
    - Suorita [Tarkista ja korjaa tietokanta -työkalu](https://gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Tools#Check_and_Repair_Database). Tämä korjaa joitakin sisäisiä epäjohdonmukaisuuksia, jotka voivat aiheuttaa ongelmia Gramps Webissä.
2. Muunna mediasijat suhteellisiksi
    - Käytä Gramps Media Manageria [muuttaaksesi kaikki mediasijat absoluuttisista suhteellisiksi](https://gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Tools#Convert_paths_from_relative_to_absolute). Huomaa, että vaikka käytät suhteellisia polkuja, kaikki mediasisällöt, jotka ovat Grampsin mediasijaintisi ulkopuolella, eivät toimi oikein synkronoituna Gramps Webin kanssa.

## Tuo sukututkimustietoja

Jos haluat tuoda olemassa olevan sukupuun, käytä "Tuo" -sivua ja lataa tiedosto missä tahansa Grampsin tukemassa tiedostomuodossa &ndash; katso [Tuo toisesta sukututkimusohjelmasta](https://www.gramps-project.org/wiki/index.php/Import_from_another_genealogy_program) Grampsin Wikistä.

Jos käytät jo Gramps Desktopia, on vahvasti suositeltavaa käyttää Gramps XML (`.gramps`) -muotoa varmistaaksesi, että online- ja offline-puut käyttävät samoja tunnisteita ja voivat olla [synkronoituna](sync.md).

Kun napsautat "Tuo", tiedosto analysoidaan ensin ja "Vahvista tuonti" -valintaikkuna näyttää esikatselun tiedoston sisältämistä objekteista (ihmiset, perheet, tapahtumat, paikat jne.) ennen kuin mitään lisätään puuhusi. Tarkista laskennat ja napsauta sitten "Tuo" valintaikkunassa jatkaaksesi tai "Peruuta" keskeyttääksesi ilman muutoksia.

!!! warning
    Tavallinen tuonti on puhtaasti lisäys: se luo aina uusia objekteja eikä koskaan päivitä tai poista olemassa olevia, edes objekteilta, jotka jo ovat puussasi saman Gramps ID:n tai käsittelyn alla. Samojen tiedostojen tuominen kahdesti &ndash; tai tiedoston tuominen, joka päällekkäin puussa jo olevan datan kanssa &ndash; tulee tuplaamaan jokaisen vastaavan objektin sen sijaan, että se yhdistettäisiin tai ohitettaisiin.

    Jos sinun tarvitsee tuoda muutoksia, jotka on tehty muualla puuhun, joka on jo tuotu, käytä sen sijaan [Palauta varmuuskopiosta](settings.md#restore-from-backup), joka korvasi puun vastaamaan ladattua tiedostoa sen sijaan, että lisäisi siihen.

## Miksi ei tukea Gramps XML -paketille?

Vaikka Gramps XML (`.gramps`) on suositeltu muoto tietojen tuomiseen, Gramps XML *pakettia* (`.gpkg`) ei tueta Gramps Webissä. Tämä johtuu siitä, että mediasisältöjen tuonti- ja vientimenettelyt eivät sovellu käytettäväksi verkkopalvelimella.

Tuodaksesi mediasisältöjä, jotka kuuluvat tuotu `.gramps` -tiedostoon, katso seuraava osio.

## Tuo mediasisältöjä

Jos olet ladannut sukupuun ja tarvitset vastaavien mediasisältöjen lataamista, voit käyttää "tuo mediasisältöarkisto" -painiketta "Tuo" -sivulla.

Se odottaa ZIP-tiedostoa, jossa on puuttuvat mediasisällöt. ZIP-tiedoston kansiorakenteen ei tarvitse olla sama kuin Grampsin mediasijainnin kansiorakenne, sillä tiedostot yhdistetään mediasisältöobjekteihin niiden tarkistussumman perusteella.

Huomaa, että tämä ominaisuus toimii vain tiedostoille, joilla on oikea tarkistussumma Gramps-tietokannassa (mikä tulisi varmistaa suorittamalla tarkistus- ja korjaustyökalu ensimmäisessä vaiheessa).

Siirtyessäsi Gramps Webiin toisesta sukututkimusohjelmasta, joka sisältää mediasisältöjä, on suositeltavaa tuoda kaikki ensin Gramps Desktopiin, jolla on enemmän vaihtoehtoja yhdistää olemassa olevia mediasisältöjä tuotuun puuhun.
