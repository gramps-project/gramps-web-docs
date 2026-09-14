# Tuo tietoja

Voit tuoda olemassa olevan sukupuun Gramps Webiin lataamalla tiedoston, joka on viety toisesta sukututkimusohjelmasta, verkkopalvelusta tai Gramps Desktopista.

Tuo-toiminto löytyy **Tieto**-osiosta [Hallintasettings](settings.md) (käyttäjäkuvake ylävalikossa ▸ Hallinta), joka on saatavilla puun omistajille ja ylläpitäjille. Kun puu on vielä tyhjillään, **Tuo sukupuu** -painike etusivun "Aloita" -kortissa vie myös sinne.

## Mikä tiedosto käyttää

| Tulee | Vie puusi muodossa | Tiedostopääte |
|---|---|---|
| Toinen sukututkimusohjelma tai verkkopalvelu | GEDCOM | `.ged` |
| Gramps Desktop | Gramps XML | `.gramps` |
| GeneWeb | GeneWeb | `.gw` |
| Pro-Gen | Pro-Gen | `.def` |
| Taulukkolaskentaohjelma | Gramps CSV | `.csv` |
| Osoitekirja | vCard | `.vcf` |

GEDCOM on yleinen vaihtomuoto, jota lähes jokainen sukututkimusohjelma ja verkkopalvelu voi viedä. Etsi ohjelmastasi tai verkkosivustolta "Vie" tai "Lataa" -vaihtoehto ja valitse GEDCOM, jos sinulle tarjotaan useita muotoja. Grampsin Wiki-sivulla [Tuo toisesta sukututkimusohjelmasta](https://www.gramps-project.org/wiki/index.php/Import_from_another_genealogy_program) on huomautuksia tietyistä ohjelmista.

Jos käytät Gramps Desktopia, valitse Gramps XML (`.gramps`) GEDCOMin sijaan. Se sisältää kaikki Gramps-tiedot ilman hävikkiä, ja verkkopuun ja offline-puun tunnisteet pysyvät samoina, joten ne voidaan [synkronoida](sync.md). Katso [Tulee Gramps Desktopista](#coming-from-gramps-desktop) alla.

## Tuo sukupuutiedosto

1. Avaa **Tieto**-osio Hallintasettings.
2. "Tuo sukupuu" -kohdassa valitse tiedostosi ja napsauta **Tuo**.
3. Tiedosto analysoidaan ensin, ja "Vahvista tuonti" -valintaikkuna näyttää, kuinka monta objektia se sisältää (ihmisiä, perheitä, tapahtumia, paikkoja jne.). Mikään ei ole vielä lisätty puuhusi. Tarkista, että laskelmat näyttävät uskottavilta, napsauta sitten **Tuo** jatkaaksesi tai **Peruuta** keskeyttääksesi ilman muutoksia.
4. Tuo tapahtuu taustalla, ja edistymisindikaattori näkyy. Kun tiedot on tuotu, hakemisto päivitetään, mikä voi kestää hetken suurelle puulle.

Kun tuonti on valmis, tarkista tulos: vertaa ihmisten määrää **Tilastot**-paneelissa etusivulla vanhan ohjelmasi lukumäärään ja avaa perhe, jonka tunnet hyvin, nähdäksesi, että vanhemmat, lapset, päivämäärät ja paikat siirtyivät odotetusti.

!!! warning
    Tavallinen tuonti on puhtaasti lisäävä: se luo aina uusia objekteja eikä koskaan päivitä tai poista olemassa olevia, edes objekteilta, jotka jo ovat puussasi saman Gramps ID:n tai käsittelyn alla. Samojen tiedostojen tuominen kahdesti – tai tiedoston tuominen, joka päällekkäin olemassa olevan datan kanssa puussa – tulee kaksinkertaistamaan jokaisen vastaavan objektin sen sijaan, että se yhdistettäisiin tai ohitettaisiin.

    Jos sinun on tuotava muutoksia, jotka on tehty muualla puuhun, joka on jo tuotu, käytä [Palauta varmuuskopiosta](settings.md#restore-from-backup) sen sijaan, mikä korvasi puun vastaamaan ladattua tiedostoa sen sijaan, että lisäisi siihen. Tämä vaatii Gramps XML -tiedoston.

Jos puullesi on asetettu raja ihmisten määrälle (katso [Käyttökiintiöt](settings.md#usage-quotas)), tuonti, joka ylittää sen, hylätään kokonaisuudessaan.

## GEDCOM-tiedostot

Sekä GEDCOM 5.5.1 että GEDCOM 7 -tiedostoja voidaan tuoda. On muutamia asioita, joista on syytä olla tietoinen.

### Merkkikoodaus

GEDCOM 5.5.1 -tiedosto ilmoittaa merkkikoodauksensa otsikossaan. UTF-8, UTF-16, ANSEL ja Windows (ANSI) -koodaukset ovat tuettuja. Jos aksentteja tai muita erikoismerkkejä sisältävät nimet näyttävät epäselviltä tuonnin jälkeen (esimerkiksi `MÃ¼ller` sen sijaan, että `Müller`), tiedosto on todennäköisesti viety eri koodauksella kuin se ilmoittaa. Vie tiedosto uudelleen vanhasta ohjelmastasi, valitse UTF-8, jos se tarjoaa vaihtoehdon, ja [aloita alusta](#starting-over).

GEDCOM 7 -tiedostot on aina koodattava UTF-8:ksi; muut tiedostot hylätään "Virheellinen GEDCOM-tiedosto" -virheellä.

### Ohjelmaerityiset tiedot

Monet ohjelmat lisäävät omia laajennuksiaan GEDCOMiin, joita muut ohjelmat eivät ymmärrä. Gramps ei hiljaa pudota tällaisia tietoja: rivit, joita se ei voi tulkita, kerätään "GEDCOM-tuo" -tyyppiseen muistiinpanoon, joka liitetään henkilöön, perheeseen tai muuhun objektiin, johon ne kuuluvat. Tarkista nämä muistiinpanot nähdäksesi, onko mitään tärkeää jäänyt siirtymättä.

### Mediataidot

GEDCOM-tiedosto sisältää viittauksia mediataitoihin (kuten valokuviin tai skannattuihin asiakirjoihin), mutta ei itse tiedostoja. Tuonnin jälkeen mediakohteet ovat olemassa puussasi, mutta niiden tiedostot puuttuvat, mikä näkyy [Mediatiedoston tila](settings.md#media-file-status) -kohdassa. Lisätäksesi tiedostot, katso [Tuo mediataidot](#import-media-files) alla.

## Tulee Gramps Desktopista

Jos käytät Gramps Desktopia, on kaksi vaihetta valmistella tietokantaasi varmistaaksesi, että kaikki sujuu ongelmitta seuraavassa.

1. Tarkista ja korjaa tietokanta
    - Valinnainen: luo tietokannan varmuuskopio viemällä Gramps XML:ään
    - Suorita [Tarkista ja korjaa tietokanta -työkalu](https://gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Tools#Check_and_Repair_Database). Tämä korjaa joitakin sisäisiä epäjohdonmukaisuuksia, jotka voisivat aiheuttaa ongelmia Gramps Webissä.
2. Muunna mediapolut suhteellisiksi
    - Käytä Grampsin Mediatoimintoa [muuntaaksesi kaikki mediapolut absoluuttisista suhteellisiksi](https://gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Tools#Convert_paths_from_relative_to_absolute). Huomaa, että vaikka suhteellisilla poluilla, kaikki mediataidot, jotka ovat Grampsin mediakansiosi ulkopuolella, eivät toimi oikein synkronoidessasi Gramps Webin kanssa.

Vie sitten puusi Gramps XML:ään (`.gramps`), tuo se yllä kuvatulla tavalla ja lataa mediataitosi seuraavassa osassa kuvatulla tavalla. Jatka työskentelyä samalla puulla tietokoneellasi ja verkossa käyttämällä [Gramps Web Sync -lisäosaa](sync.md).

### Miksi ei tukea Gramps XML -paketille?

Vaikka Gramps XML (`.gramps`) on suositeltu muoto tietojen tuomiseen, Gramps XML *pakettia* (`.gpkg`) ei tueta Gramps Webissä. Tämä johtuu siitä, että mediataitojen tuonti- ja vientimenettelyt eivät sovellu käytettäväksi verkkopalvelimella.

## Tuo mediataidot

Jos olet tuonut sukupuun ja sinun on ladattava vastaavat mediataidot, käytä **Tuo mediataidot** Hallintasettingsin Tieto-osiossa. Se odottaa ZIP-tiedostoa, joka sisältää puuttuvat mediataidot. Tiedostot yhdistetään puussasi oleviin mediakohteisiin kahdella tavalla:

- **Tarkistussumman mukaan.** Mediakohteille, joilla on tarkistussumma – kuten on tapauksessa puista, jotka on tuotu Gramps Desktopista – käytetään tiedostoa, jonka tarkistussumma vastaa, riippumatta sen nimestä tai ZIP-tiedoston kansiorakenteesta. Tämä toimii vain, jos Grampsin tietokannan tarkistussummat ovat oikein, mikä varmistetaan tarkistus- ja korjaustyökalun suorittamisella.
- **Polun mukaan.** Mediakohteet ilman tarkistussummaa – kuten on tyypillistä GEDCOM-tuonnin jälkeen – yhdistetään niiden polun mukaan: ZIP-tiedoston on sisällettävä tiedosto tarkalleen suhteellisella polulla, joka on tallennettu mediakohteeseen.

Jos GEDCOM-tiedostossasi tallennetut polut ovat absoluuttisia (esimerkiksi `C:\Users\...\photo.jpg`), yhdistäminen polun mukaan ei toimi. Tässä tapauksessa suositellaan ensin tuomaan kaikki Gramps Desktopiin, jossa on enemmän vaihtoehtoja liittää olemassa olevat mediataidot tuotuun puuhun, ja siirtymään sitten Gramps Webiin, kuten on kuvattu [Tulee Gramps Desktopista](#coming-from-gramps-desktop).

## Yleiset ongelmat

**"Tuettu muoto ei ole."** Vain yllä luetellut tiedostopäätteet [voivat olla tuotu](#which-file-to-use). Jos ohjelmasi tai verkkopalvelusi antoi sinulle ZIP-arkiston, pura se ja lataa sisällä oleva `.ged`-tiedosto.

**Kaikki näkyy kahdesti.** Sama tiedosto on tuotu kahdesti. Koska tuonnit eivät koskaan yhdisty, [aloita alusta](#starting-over).

**Epäselvät erikoismerkit.** Katso [Merkkikoodaus](#character-encoding).

**Valokuvat puuttuvat.** Katso [Tuo mediataidot](#import-media-files).

### Aloita alusta

Jos tuonti meni pieleen tai haluat korjata jotain vanhassa ohjelmassasi ja tuoda uudelleen, tyhjennä ensin puu käyttämällä [Poista kaikki objektit](settings.md#delete-all-objects) Hallintasettingsin Vaaravyöhykkeessä, ja tuo sitten korjattu tiedosto. Huomaa, että tämä poistaa myös kaikki muutokset, joita olet tehnyt Gramps Webissä tuonnin jälkeen.
