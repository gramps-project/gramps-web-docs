# Tuo dataa

Voit tuoda olemassa olevan sukupuun Gramps Webiin lataamalla tiedoston, joka on viety toisesta sukututkimusohjelmasta, verkkopalvelusta tai Gramps Desktopista.

Tuonti löytyy **Data**-osiosta [Hallinta-asetuksista](settings.md) (käyttäjäkuvake ylävalikossa ▸ Hallinta), joka on saatavilla puun omistajille ja ylläpitäjille. Kun puu on vielä tyhjillään, **Tuo sukupuu** -painike etusivun "Aloita" -kortissa vie myös sinne.

## Mikä tiedosto käytetään

| Tulee | Vie puusi muodossa | Tiedostopääte |
|---|---|---|
| Toinen sukututkimusohjelma tai verkkopalvelu | GEDCOM | `.ged` |
| Gramps Desktop | Gramps XML | `.gramps` |
| GeneWeb | GeneWeb | `.gw` |
| Pro-Gen | Pro-Gen | `.def` |
| Taulukkolaskentaohjelma | Gramps CSV | `.csv` |
| Osoitekirja | vCard | `.vcf` |

GEDCOM on yleinen vaihtoformaatti, jota lähes jokainen sukututkimusohjelma ja verkkopalvelu voi viedä. Etsi ohjelmastasi tai verkkosivustolta "Vie" tai "Lataa" -vaihtoehto ja valitse GEDCOM, jos sinulle tarjotaan useita formaatteja. Grampsin Wiki-sivulla [Tuo toisesta sukututkimusohjelmasta](https://www.gramps-project.org/wiki/index.php/Import_from_another_genealogy_program) on huomautuksia erityisistä ohjelmista.

Jos käytät Gramps Desktopia, valitse Gramps XML (`.gramps`) GEDCOMin sijaan. Se sisältää kaikki Grampsin tiedot ilman hävikkiä, ja verkkopuun ja offline-puun tunnisteet pysyvät samoina, joten ne voidaan [synkronoida](sync.md). Katso [Tulee Gramps Desktopista](#coming-from-gramps-desktop) alla.

## Tuo sukupuutiedosto

1. Avaa **Data**-osio Hallinta-asetuksista.
2. "Tuo sukupuu" -kohdassa valitse tiedostosi ja napsauta **Tuo**.
3. Tiedosto analysoidaan ensin, ja "Vahvista tuonti" -valintaikkuna näyttää, kuinka monta objektia se sisältää (ihmisiä, perheitä, tapahtumia, paikkoja jne.). Mikään ei ole vielä lisätty puuhusi. Tarkista, että laskelmat näyttävät uskottavilta, napsauta sitten **Tuo** jatkaaksesi tai **Peruuta** keskeyttääksesi ilman muutoksia.
4. Tuo tapahtuu taustalla, ja edistymisindikaattori näytetään. Kun tiedot on tuotu, hakemisto päivitetään, mikä voi kestää hetken suurelle puulle. Jos tuonti epäonnistuu, syy näytetään.

Kun tuonti on valmis, tarkista tulos: vertaa ihmisten määrää **Tilastot**-paneelissa etusivulla vanhan ohjelmasi lukumäärään ja avaa perhe, jonka tunnet hyvin, nähdäksesi, että vanhemmat, lapset, päivämäärät ja paikat tulivat odotetusti.

!!! warning
    Tavallinen tuonti on täysin lisäys: se luo aina uusia objekteja eikä koskaan päivitä tai poista olemassa olevia, edes objekteilta, jotka jo ovat puussasi saman Gramps ID:n tai käsitteen alla. Samojen tiedostojen tuominen kahdesti – tai tiedoston tuominen, joka päällekkäin olemassa olevien tietojen kanssa puussa – tuo jokaisen vastaavan objektin uudelleen sen sijaan, että se yhdistettäisiin tai ohitettaisiin.

    Jos sinun tarvitsee tuoda muutoksia, jotka on tehty muualla puuhun, joka on jo tuotu, käytä [Palauta varmuuskopiosta](backups.md#restore-from-backup) sen sijaan, mikä korvasi puun vastaamaan ladattua tiedostoa sen sijaan, että lisäisi siihen. Tämä vaatii Gramps XML -tiedoston tai Gramps Web -varmuuskopion.

## Käyttökiintiöt

Palvelimen ylläpitäjä voi asettaa rajoja puullesi (katso [Palvelimen kokoonpano](../install_setup/configuration.md)). **Data**-osion yläosassa näkyy nykyinen käyttö suhteessa näihin rajoihin:

- **Ihmiset** – henkilöobjektien määrä puussa verrattuna määritettyyn maksimiin (∞, jos rajoittamaton)
- **Media tallennus** – ladattujen mediafilejen kokonaiskoko verrattuna määritettyyn tallennuskiintiöön (∞, jos rajoittamaton)

Tuonti, joka ylittää ihmisten määrän rajan, hylätään kokonaisuudessaan.

## GEDCOM-tiedostot

Sekä GEDCOM 5.5.1 että GEDCOM 7 -tiedostoja voidaan tuoda. On muutamia asioita, joista on syytä olla tietoinen.

### Merkkikoodaus

GEDCOM 5.5.1 -tiedosto ilmoittaa merkkikoodauksensa otsikossaan. UTF-8, UTF-16, ANSEL ja Windows (ANSI) -koodaukset ovat tuettuja. Jos aksentteja tai muita erikoismerkkejä sisältävät nimet näyttävät suttuisilta tuonnin jälkeen (esimerkiksi `MÃ¼ller` sen sijaan, että `Müller`), tiedosto on todennäköisesti viety eri koodauksella kuin se ilmoittaa. Vie tiedosto uudelleen vanhasta ohjelmastasi, valitse UTF-8, jos se tarjoaa vaihtoehdon, ja [aloita alusta](#starting-over).

GEDCOM 7 -tiedostot on aina koodattava UTF-8-muodossa; muut tiedostot hylätään "Virheellinen GEDCOM-tiedosto" -virheellä.

### Ohjelmakohtaiset tiedot

Monet ohjelmat lisäävät omia laajennuksiaan GEDCOMiin, joita muut ohjelmat eivät ymmärrä. Gramps ei hiljaa pudota tällaisia tietoja: rivit, joita se ei voi tulkita, kerätään "GEDCOM tuonti" -tyyppiseen muistiinpanoon, joka liitetään henkilöön, perheeseen tai muuhun objektiin, johon ne kuuluvat. Tarkista nämä muistiinpanot nähdäksesi, tuliko mitään tärkeää perille.

### Mediafilet

GEDCOM-tiedosto sisältää viittauksia mediafileihin (kuten valokuviin tai skannattuihin asiakirjoihin), mutta ei itse tiedostoja. Tuonnin jälkeen mediaobjektit ovat olemassa puussasi, mutta niiden tiedostot puuttuvat, mikä näkyy [Mediafilejen tilassa](import-media.md#media-file-status). Tiedostojen lisäämiseksi katso [Tuo mediafilejä](import-media.md).

## Tulee Gramps Desktopista

Jos käytät Gramps Desktopia, on kaksi vaihetta, joilla voit valmistella tietokannan varmistaaksesi, että kaikki toimii sujuvasti seuraavassa.

1. Tarkista ja korjaa tietokanta
    - Valinnainen: luo tietokannan varmuuskopio viemällä se Gramps XML:ään
    - Suorita [Tarkista ja korjaa tietokanta -työkalu](https://gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Tools#Check_and_Repair_Database). Tämä korjaa joitakin sisäisiä epäjohdonmukaisuuksia, jotka voisivat aiheuttaa ongelmia Gramps Webissä.
2. Muunna mediapolut suhteellisiksi
    - Käytä Gramps Media Manageria [muuttaaksesi kaikki mediapolut absoluuttisista suhteellisiksi](https://gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Tools#Convert_paths_from_relative_to_absolute). Huomaa, että vaikka suhteelliset polut ovat käytössä, kaikki mediafilet, jotka ovat Grampsin mediahakemistosi ulkopuolella, eivät toimi oikein synkronoidessasi Gramps Webin kanssa.

Vie sitten puusi Gramps XML:ään (`.gramps`), tuo se yllä kuvatulla tavalla ja [lataa mediafilejäsi](import-media.md). Jatka työskentelyä samalla puulla tietokoneellasi ja verkossa käyttämällä [Gramps Web Sync -lisäosaa](sync.md).

### Miksi Gramps XML -pakettia ei tueta?

Vaikka Gramps XML (`.gramps`) on suosituin formaatti tietojen tuontiin, Gramps XML *pakettia* (`.gpkg`) ei tueta Gramps Webissä. Tämä johtuu siitä, että mediafilejen tuonti- ja vientimenettelyt eivät sovellu käytettäväksi verkkopalvelimella.

## Yleiset ongelmat

**"Tuettu formaatti".** Vain yllä luetellut tiedostopäätteet [voivat olla tuotuja](#which-file-to-use). Jos ohjelmasi tai verkkopalvelusi antoi sinulle ZIP-arkiston, pura se ja lataa sisällä oleva `.ged`-tiedosto.

**Kaikki näkyy kahdesti.** Sama tiedosto on tuotu kahdesti. Koska tuonnit eivät koskaan yhdistä, [aloita alusta](#starting-over).

**Suttuinen erikoismerkistö.** Katso [Merkkikoodaus](#character-encoding).

**Valokuvat puuttuvat.** Katso [Tuo mediafilejä](import-media.md).

### Aloita alusta

Jos tuonti meni pieleen tai haluat korjata jotain vanhassa ohjelmassasi ja tuoda uudelleen, tyhjennä ensin puu käyttämällä [Poista kaikki objektit](#delete-all-objects), ja tuo sitten korjattu tiedosto. Huomaa, että tämä poistaa myös kaikki muutokset, joita olet tehnyt Gramps Webissä tuonnin jälkeen.

### Poista kaikki objektit

!!! danger
    Objektien poistaminen on **palautumaton**. Tee [varmuuskopio](backups.md) ennen jatkamista.

**Poista kaikki objektit** löytyy [Hallinta-asetusten](settings.md) **Vaaravyöhykkeestä**. Napsauttamalla **Poista** avautuu valintaikkuna, jossa voit valita poistettavaksi:

- **Kaikki objektit** – tyhjentää puun kokonaan
- **Tietyt objektityypit** – esimerkiksi vain tapahtumat tai vain mediaobjektit

Sinua pyydetään vahvistamaan toiminto kirjautumalla uudelleen. Poisto tapahtuu taustatehtävänä, ja edistymisindikaattori näytetään.

!!! warning
    Vain osan objektityypeistä poistaminen (eikä kaikkia objekteja kerralla) voi kestää hyvin pitkään suurilla puilla, koska palvelimen on tarkistettava ja päivitettävä kaikki suhteet objektien välillä.
