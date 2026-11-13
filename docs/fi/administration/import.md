# Tuo dataa

Voit tuoda olemassa olevan sukupuun Gramps Webiin lataamalla tiedoston, joka on viety toisesta sukututkimusohjelmasta, verkkopalvelusta tai Gramps Desktopista.

Tuonti löytyy **Data**-osiosta [Hallintasettings](settings.md) (käyttäjäkuvake ylävalikkopalkissa ▸ Hallinta), joka on saatavilla puun omistajille ja ylläpitäjille. Kun puu on vielä tyhjillään, **Tuo sukupuu** -painike etusivun "Aloita" -kortilla vie myös sinne.

## Mikä tiedosto käyttää

| Tulee | Vie puusi muodossa | Tiedostopääte |
|---|---|---|
| Toinen sukututkimusohjelma tai verkkopalvelu | GEDCOM | `.ged` |
| Gramps Desktop | Gramps XML | `.gramps` |
| GeneWeb | GeneWeb | `.gw` |
| Pro-Gen | Pro-Gen | `.def` |
| Taulukkolaskentaohjelma | Gramps CSV | `.csv` |
| Osoitekirja | vCard | `.vcf` |

GEDCOM on yleinen vaihtoformaatti, jota lähes jokainen sukututkimusohjelma ja verkkopalvelu voi viedä. Etsi ohjelmastasi tai verkkosivustolta "Vie" tai "Lataa" -vaihtoehto, ja valitse GEDCOM, jos sinulle tarjotaan useita muotoja. Grampsin Wiki-sivulla [Tuo toisesta sukututkimusohjelmasta](https://www.gramps-project.org/wiki/index.php/Import_from_another_genealogy_program) on huomautuksia erityisistä ohjelmista.

Jos käytät Gramps Desktopia, valitse Gramps XML (`.gramps`) sen sijaan, että käyttäisit GEDCOMia. Se sisältää kaikki Grampsin tiedot ilman hävikkiä, ja verkko- ja offline-puusi säilyttävät samat tunnisteet, joten ne voidaan [synkronoida](sync.md). Katso [Tulee Gramps Desktopista](#coming-from-gramps-desktop) alla.

## Tuo sukupuutiedosto

1. Avaa **Data**-osio Hallintasettings.
2. "Tuo sukupuu" -kohdassa valitse tiedostosi ja napsauta **Tuo**.
3. Tiedosto analysoidaan ensin, ja "Vahvista tuonti" -dialogi näyttää, kuinka monta objektia se sisältää (ihmisiä, perheitä, tapahtumia, paikkoja jne.). Mikään ei ole vielä lisätty puuhusi. Tarkista, että laskelmat näyttävät uskottavilta, napsauta sitten **Tuo** jatkaaksesi tai **Peruuta** keskeyttääksesi ilman muutoksia.
4. Tuo tapahtuu taustalla ja edistymisindikaattori näytetään. Kun tiedot on tuotu, hakemisto päivitetään, mikä voi kestää hetken suurelle puulle. Jos tuonti epäonnistuu, syy näytetään.

Kun tuonti on valmis, tarkista tulos: vertaa ihmisten määrää etusivun **Tilastot**-paneelissa vanhan ohjelmasi lukumäärään ja avaa perhe, jonka tunnet hyvin, nähdäksesi, että vanhemmat, lapset, päivämäärät ja paikat ovat tulleet odotetusti.

!!! warning
    Tavallinen tuonti on puhtaasti lisäävä: se luo aina uusia objekteja eikä koskaan päivitä tai poista olemassa olevia, edes objekteilta, jotka jo ovat puussasi saman Gramps ID:n tai käsitteen alla. Samojen tiedostojen tuominen kahdesti – tai tiedoston tuominen, joka päällekkäin olemassa olevan datan kanssa puussa – tulee kaksoiskappaleeksi jokaiselle vastaavalle objektille sen sijaan, että se yhdistettäisiin tai ohitettaisiin.

    Jos sinun tarvitsee tuoda muutoksia, jotka on tehty muualla puuhun, joka on jo tuotu, käytä [Palauta varmuuskopiosta](settings.md#restore-from-backup) sen sijaan, mikä korvasi puun vastaamaan ladattua tiedostoa sen sijaan, että lisäisi siihen. Tämä vaatii Gramps XML -tiedoston tai Gramps Web -varmuuskopion.

Jos puullesi on asetettu raja ihmisten määrälle (katso [Käyttökiintiöt](settings.md#usage-quotas)), tuonti, joka ylittää sen, hylätään kokonaisuudessaan.

## GEDCOM-tiedostot

Sekä GEDCOM 5.5.1 että GEDCOM 7 -tiedostoja voidaan tuoda. On muutamia asioita, joista on syytä olla tietoinen.

### Merkkikoodaus

GEDCOM 5.5.1 -tiedosto ilmoittaa merkkikoodauksensa otsikossaan. UTF-8, UTF-16, ANSEL ja Windows (ANSI) -koodaukset ovat tuettuja. Jos aksentteja tai muita erikoismerkkejä sisältävät nimet näyttävät epäselviltä tuonnin jälkeen (esimerkiksi `MÃ¼ller` sen sijaan, että olisi `Müller`), tiedosto on todennäköisesti viety eri koodauksella kuin se ilmoittaa. Vie tiedosto uudelleen vanhasta ohjelmastasi, valitse UTF-8, jos se tarjoaa vaihtoehdon, ja [aloita alusta](#starting-over).

GEDCOM 7 -tiedostot on aina koodattava UTF-8-muodossa; muut tiedostot hylätään "Virheellinen GEDCOM-tiedosto" -virheellä.

### Ohjelmakohtaiset tiedot

Monet ohjelmat lisäävät omia laajennuksiaan GEDCOMiin, joita muut ohjelmat eivät ymmärrä. Gramps ei hiljaa hylkää tällaisia tietoja: rivit, joita se ei voi tulkita, kerätään "GEDCOM-tuo" -tyyppiseen muistiinpanoon, joka liitetään henkilöön, perheeseen tai muuhun objektiin, johon ne kuuluvat. Tarkista nämä muistiinpanot nähdäksesi, onko mitään tärkeää jäänyt tulematta.

### Mediatiedostot

GEDCOM-tiedosto sisältää viittauksia mediatiedostoihin (kuten valokuviin tai skannattuihin asiakirjoihin), mutta ei itse tiedostoja. Tuonnin jälkeen mediatiedostot ovat olemassa puussasi, mutta niiden tiedostot puuttuvat, mikä näkyy [Mediatiedoston tila](settings.md#media-file-status) -kohdassa. Tiedostojen lisäämiseksi katso [Tuo mediatiedostot](import-media.md).

## Tulee Gramps Desktopista

Jos käytät Gramps Desktopia, on kaksi vaihetta, joilla voit valmistella tietokannan varmistaaksesi, että kaikki toimii sujuvasti seuraavassa.

1. Tarkista ja korjaa tietokanta
    - Valinnainen: luo tietokannan varmuuskopio viemällä se Gramps XML:ään
    - Suorita [Tarkista ja korjaa tietokanta -työkalu](https://gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Tools#Check_and_Repair_Database). Tämä korjaa joitakin sisäisiä epäjohdonmukaisuuksia, jotka voisivat aiheuttaa ongelmia Gramps Webissä.
2. Muunna mediatiedostopolut suhteellisiksi
    - Käytä Grampsin Mediamanageria [muuntaaksesi kaikki mediatiedostopolut absoluuttisista suhteellisiksi](https://gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Tools#Convert_paths_from_relative_to_absolute). Huomaa, että vaikka suhteelliset polut olisivat käytössä, kaikki mediatiedostot Grampsin mediatiedostohakemiston ulkopuolella eivät toimi oikein, kun niitä synkronoidaan Gramps Webin kanssa.

Vie sitten puusi Gramps XML:ään (`.gramps`), tuo se yllä kuvatulla tavalla ja [lataa mediatiedostosi](import-media.md). Jatka työskentelyä samalla puulla tietokoneellasi ja verkossa käyttämällä [Gramps Web Sync -lisäosaa](sync.md).

### Miksi ei tukea Gramps XML -paketille?

Vaikka Gramps XML (`.gramps`) on suositeltu muoto tietojen tuomiseen, Gramps XML *pakettia* (`.gpkg`) ei tueta Gramps Webissä. Tämä johtuu siitä, että mediatiedostojen tuonti- ja vientirutiinit eivät sovellu käytettäväksi verkkopalvelimella.

## Yleiset ongelmat

**"Tuettu muoto ei ole käytössä".** Vain yllä luetellut tiedostopäätteet [voivat olla tuotu](#which-file-to-use). Jos ohjelmasi tai verkkopalvelusi antoi sinulle ZIP-arkiston, pura se ja lataa sisällä oleva `.ged`-tiedosto.

**Kaikki näkyy kaksinkertaisena.** Sama tiedosto on tuotu kahdesti. Koska tuonnit eivät koskaan yhdisty, [aloita alusta](#starting-over).

**Epäselvät erikoismerkit.** Katso [Merkkikoodaus](#character-encoding).

**Valokuvat puuttuvat.** Katso [Tuo mediatiedostot](import-media.md).

### Aloita alusta

Jos tuonti meni pieleen tai haluat korjata jotain vanhassa ohjelmassasi ja tuoda uudelleen, tyhjennä ensin puu käyttämällä [Poista kaikki objektit](settings.md#delete-all-objects) Hallintasettingsin vaaravyöhykkeessä, ja tuo sitten korjattu tiedosto. Huomaa, että tämä poistaa myös kaikki muutokset, joita olet tehnyt Gramps Webissä tuonnin jälkeen.
