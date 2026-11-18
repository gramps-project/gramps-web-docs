# Tuo dataa

Voit tuoda olemassa olevan sukupuusi Gramps Webiin lataamalla tiedoston, joka on viety toisesta sukututkimusohjelmasta, verkkopalvelusta tai Gramps Desktopista.

Tuonnilla on oma sivunsa, joka on käytettävissä puun omistajille ja ylläpitäjille. Avaa se valitsemalla **Tuo sukupuu** **Data**-osiossa [Hallintasettings](settings.md) (käyttäjäkuvake ylävalikkopalkissa ▸ Hallinta). Kun puu on vielä tyhjillään, **Tuo sukupuu** -painike "Aloita" -kortissa etusivulla, sukupuussa ja listoissa vie myös sinne.

## Mikä tiedosto tulisi käyttää

| Tulee | Vie puusi muodossa | Tiedostopääte |
|---|---|---|
| Toinen sukututkimusohjelma tai verkkopalvelu | GEDCOM | `.ged` |
| Gramps Desktop | Gramps XML | `.gramps` |
| GeneWeb | GeneWeb | `.gw` |
| Pro-Gen | Pro-Gen | `.def` |
| Taulukkolaskentaohjelma | Gramps CSV | `.csv` |
| Osoitekirja | vCard | `.vcf` |

GEDCOM on yleinen vaihtoformaatti, jonka lähes jokainen sukututkimusohjelma ja verkkopalvelu voi viedä. Etsi ohjelmastasi tai verkkosivustolta "Vie" tai "Lataa" -vaihtoehto ja valitse GEDCOM, jos sinulle tarjotaan useita formaatteja. Grampsin Wiki-sivulla [Tuo toisesta sukututkimusohjelmasta](https://www.gramps-project.org/wiki/index.php/Import_from_another_genealogy_program) on huomautuksia erityisistä ohjelmista.

Jos käytät Gramps Desktopia, valitse Gramps XML (`.gramps`) GEDCOMin sijaan. Se sisältää kaikki Grampsin tiedot ilman hävikkiä, ja online- ja offline-puusi säilyttävät samat tunnisteet, joten ne voidaan [synkronoida](sync.md). Katso [Tulee Gramps Desktopista](#coming-from-gramps-desktop) alla.

## Tuo sukupuutiedosto

1. Avaa Tuo-sivu kuten yllä on kuvattu.
2. "Tuo sukupuu" -kohdassa valitse tiedostosi ja napsauta **Tuo**. Latauksen edistyminen näkyy.
3. Tiedosto luetaan ensin, ja "Vahvista tuonti" -dialogi näyttää, kuinka monta objektia se sisältää (ihmisiä, perheitä, tapahtumia, paikkoja jne.), sekä tuojan [raportin](#the-import-report), jos sellainen on. Mikään ei ole vielä lisätty puuhusi. Tarkista, että laskelmat näyttävät uskottavilta, ja napsauta sitten **Tuo** jatkaaksesi tai **Peruuta** keskeyttääksesi ilman muutoksia. Jos puusi sisältää jo ihmisiä, dialogi varoittaa, että saman tiedon tuominen uudelleen luo kaksoiskappaleita.
4. Tuo tapahtuu taustalla, ja edistymisindikaattori näkyy. Kun tiedot on tuotu, hakemisto päivitetään, mikä voi kestää hetken suurelle puulle. Jos tuonti epäonnistuu, syy näkyy.
5. Jos puulla ei vielä ole kotihenkilöä, sinulle tarjotaan mahdollisuus valita yksi.

Kun tuonti on valmis, tarkista tulos: vertaa ihmisten määrää **Tilastot**-paneelissa etusivulla vanhan ohjelmasi lukumäärään ja avaa perhe, jonka tunnet hyvin, nähdäksesi, että vanhemmat, lapset, päivämäärät ja paikat ovat tulleet odotetusti. Jos tiedosto viittaa valokuviin tai muihin mediafileihin, lisää ne seuraavaksi [Tuo mediafilejä](import-media.md) samalla sivulla.

!!! warning
    Tavallinen tuonti on täysin lisäysperusteinen: se luo aina uusia objekteja eikä koskaan päivitä tai poista olemassa olevia, edes objekteilta, jotka jo ovat puussasi saman Gramps ID:n tai käsittelyn alla. Saman tiedoston tuominen kahdesti – tai tiedoston tuominen, joka osuu jo puussa oleviin tietoihin – luo kaksoiskappaleita jokaisesta vastaavasta objektista sen sijaan, että se yhdistäisi tai ohittaisi sen.

    Jos sinun tarvitsee tuoda muutoksia, jotka on tehty muualla puuhun, joka on jo tuotu, käytä sen sijaan [Palauta varmuuskopiosta](backups.md#restore-from-backup), joka korvasi puun vastaamaan ladattua tiedostoa sen sijaan, että lisäisi siihen. Tämä vaatii Gramps XML -tiedoston tai Gramps Web -varmuuskopion.

## Tuontiraportti

Tuoja raportoi, mitä se ei voinut tuoda täysin, esimerkiksi GEDCOM-rivejä, joita se ei ymmärtänyt, viittauksia tiedostoista puuttuville rekistereille tai vanhentuneelle tiedostomuodolle. Raportti näkyy **Raportti**-kohdassa sekä vahvistusdialogissa että tuonnin jälkeen. Lue se ennen vahvistamista: se selittää usein ongelmia, joita muuten huomaisit vasta myöhemmin puussa.

Ei jokainen viesti ole ongelma – monet GEDCOM-tiedostot sisältävät ohjelmakohtaisia tietoja, jotka raportoidaan mutta pidetään, katso [Ohjelmakohtaiset tiedot](#program-specific-data). Käytä raportin vieressä olevia painikkeita kopioidaksesi sen tai ladata se tekstimuotoisena tiedostona, esimerkiksi pyytääksesi apua [foorumissa](../help/help.md).

## Käyttökiintiöt

Palvelimen ylläpitäjä voi asettaa rajoja puullesi (katso [Palvelimen kokoonpano](../install_setup/configuration.md)). **Data**-osion yläosassa näkyy nykyinen käyttö suhteessa näihin rajoihin:

- **Ihmiset** – henkilöobjektien määrä puussa verrattuna määritettyyn maksimiin (∞, jos rajoittamaton)
- **Media tallennus** – ladattujen mediafilejen kokonaiskoko verrattuna määritettyyn tallennuskiintiöön (∞, jos rajoittamaton)

Tuo, joka ylittää ihmisten määrän rajan, hylätään kokonaisuudessaan.

## GEDCOM-tiedostot

Sekä GEDCOM 5.5.1 että GEDCOM 7 -tiedostoja voidaan tuoda. On muutamia asioita, joista on syytä olla tietoinen.

### Merkkikoodaus

GEDCOM 5.5.1 -tiedosto ilmoittaa merkkikoodauksensa otsikossaan. UTF-8, UTF-16, ANSEL ja Windows (ANSI) -koodaukset ovat tuettuja. Jos aksentteja tai muita erikoismerkkejä sisältävät nimet näyttävät olevan sekaisin tuonnin jälkeen (esimerkiksi `MÃ¼ller` sen sijaan, että olisi `Müller`), tiedosto on todennäköisesti viety eri koodauksella kuin se ilmoittaa. Vie tiedosto uudelleen vanhasta ohjelmastasi, valitsemalla UTF-8, jos se tarjoaa vaihtoehdon, ja [aloita alusta](#starting-over).

GEDCOM 7 -tiedostot on aina koodattava UTF-8-muodossa; muut tiedostot hylätään "Virheellinen GEDCOM-tiedosto" -virheellä.

### Ohjelmakohtaiset tiedot

Monet ohjelmat lisäävät omia laajennuksiaan GEDCOMiin, joita muut ohjelmat eivät ymmärrä. Gramps ei hiljaa hylkää tällaisia tietoja: rivit, joita se ei voi tulkita, kerätään "GEDCOM-tuonti" -tyyppiseen muistiinpanoon, joka liitetään henkilöön, perheeseen tai muuhun objektiin, johon ne kuuluvat. Tarkista nämä muistiinpanot nähdäksesi, onko mitään tärkeää jäänyt tulematta.

### Mediafilet

GEDCOM-tiedosto sisältää viittauksia mediafileihin (kuten valokuviin tai skannattuihin asiakirjoihin), mutta ei itse tiedostoja. Tuonnin jälkeen mediaobjektit ovat olemassa puussasi, mutta niiden tiedostot puuttuvat, mikä näkyy [Mediafilejen tila](import-media.md#media-file-status) -kohdassa. Lisätäksesi tiedostot, katso [Tuo mediafilejä](import-media.md).

## Tulee Gramps Desktopista

Jos käytät Gramps Desktopia, on kaksi vaihetta, joilla voit valmistella tietokannan varmistaaksesi, että kaikki toimii sujuvasti seuraavassa.

1. Tarkista ja korjaa tietokanta
    - Valinnainen: luo tietokannan varmuuskopio viemällä se Gramps XML:ään
    - Suorita [Tarkista ja korjaa tietokanta -työkalu](https://gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Tools#Check_and_Repair_Database). Tämä korjaa joitakin sisäisiä epäjohdonmukaisuuksia, jotka voisivat aiheuttaa ongelmia Gramps Webissä.
2. Muunna mediapolut suhteellisiksi
    - Käytä Gramps Media Manageria [muuntaaksesi kaikki mediapolut absoluuttisista suhteellisiksi](https://gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Tools#Convert_paths_from_relative_to_absolute). Huomaa, että vaikka suhteellisilla poluilla, kaikki mediafilet Grampsin mediahakemistosi ulkopuolella eivät toimi kunnolla synkronoitaessa Gramps Webin kanssa.

Vie sitten sukupuusi Gramps XML:ään (`.gramps`), tuo se yllä kuvatulla tavalla ja [lataa mediafilet](import-media.md). Jatkaaksesi työskentelyä samalla puulla tietokoneellasi ja verkossa, käytä [Gramps Web Sync -lisäosaa](sync.md).

### Miksi Gramps XML -pakettia ei tueta?

Vaikka Gramps XML (`.gramps`) on suosituin formaatti tietojen tuomiseen, Gramps XML *pakettia* (`.gpkg`) ei tueta Gramps Webissä. Tämä johtuu siitä, että mediafilejen tuonti- ja vientimenettelyt eivät ole soveltuvia käytettäväksi verkkopalvelimella.

## Yleiset ongelmat

**"Tuettu formaatti".** Vain yllä luetellut tiedostopäätteet [voivat olla tuotu](#which-file-to-use). Jos ohjelmasi tai verkkopalvelusi antoi sinulle ZIP-arkiston, pura se ja lataa sisällä oleva `.ged`-tiedosto.

**Kaikki näkyy kaksinkertaisena.** Sama tiedosto on tuotu kahdesti. Koska tuonnit eivät koskaan yhdistä, [aloita alusta](#starting-over).

**Sekaannuttavat erikoismerkit.** Katso [Merkkikoodaus](#character-encoding).

**Valokuvat puuttuvat.** Katso [Tuo mediafilejä](import-media.md).

### Aloita alusta

Jos tuonti meni pieleen tai haluat korjata jotain vanhassa ohjelmassasi ja tuoda uudelleen, tyhjennä ensin puu käyttämällä [Poista kaikki objektit](#delete-all-objects), ja tuo sitten korjattu tiedosto. Huomaa, että tämä myös poistaa kaikki muutokset, joita olet tehnyt Gramps Webissä tuonnin jälkeen.

### Poista kaikki objektit

!!! danger
    Objektien poistaminen on **palautumaton**. Tee [varmuuskopio](backups.md) ennen jatkamista.

**Poista kaikki objektit** löytyy [Hallintasettings](settings.md) **Vaaravyöhykkeeltä**. Napsauttamalla **Poista** avautuu dialogi, jossa voit valita poistettavat:

- **Kaikki objektit** – tyhjentää puun kokonaan
- **Erityiset objektityypit** – esimerkiksi vain tapahtumat tai vain mediaobjektit

Sinua pyydetään kirjautumaan uudelleen vahvistaaksesi toiminnon. Poisto tapahtuu taustatehtävänä, ja edistymisindikaattori näkyy.

!!! warning
    Vain osan objektityypeistä poistaminen (eikä kaikkia objekteja kerralla) voi kestää hyvin pitkään suurilla puilla, sillä palvelimen on tarkistettava ja päivitettävä kaikki suhteet objektien välillä.
