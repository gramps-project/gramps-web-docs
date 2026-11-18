# Käytä sisäänrakennettua tehtävien hallintaa

Gramps Web sisältää sisäänrakennetun sukututkimustehtävien hallintatyökalun. Sen tarkoituksena on mahdollistaa tutkijoiden suunnitella ja priorisoida, mutta myös dokumentoida tehtävänsä. Tästä syystä tehtävät esitetään lähteinä Gramps-tietokannassa. Tehtävän valmistuttua siihen liittyvä sisältö voi toimia lähteenä, joka dokumentoi tutkimusprosessia.

## Tehtävien perusteet

Tehtävillä on seuraavat ominaisuudet:

- Tila. Tämä voi olla "Avoin", "Käynnissä", "Estetty" tai "Valmis"
- Prioriteetti. Tämä voi olla "Matala", "Keskitaso" tai "Korkea"
- Tunnisteet. Tunnisteet ovat normaaleja Gramps-tunnisteita taustalla olevasta lähteestä. (Huomaa, että kaikilla tehtävillä on lisäksi `ToDo`-tunniste, joka tunnistaa ne tehtäviksi, mutta tämä tunniste on piilotettu tehtävälistassa, jotta se ei aiheuta häiriötä.)
- Otsikko. Näkyy tehtävälistassa
- Kuvaus. Rikkaan tekstin kenttä, jota voidaan käyttää ongelman kuvauksen tekemiseen, mutta myös dokumentoimaan mahdollisia edistysaskeleita
- Media. Kaikki mediafilet, jotka on liitetty tehtävään

## Luo tehtävä

Koska tehtävät ovat normaaleja Gramps-objekteja, niitä voivat muokata tai luoda samat käyttäjäryhmät, jotka voivat muokata tai luoda muita objekteja (kuten henkilöitä tai tapahtumia).

Luoaksesi tehtävä, napsauta + painiketta tehtävälistan sivulla. Syötä vähintään otsikko ja valinnaisesti prioriteetti, kuvaus, liitteet ja tunnisteet. Tila on aina "Avoin" luotaessa.

## Tehtävälista

Oletusarvoisesti tehtävälista on järjestetty tilan mukaan – valmiit tehtävät viimeisenä – ja kunkin tilan sisällä prioriteetin mukaan, korkein ensin. Suodatusvalikko suodatuspalkissa lajittelee myös prioriteetin, otsikon tai viimeisen muutoksen (uusin ensin).

Napsauta tehtävää avataksesi sen. Muokkausoikeudet omaavat käyttäjät voivat myös napsauttaa tehtävän tilakuvaketta muuttaakseen sen tilaa suoraan listassa, esimerkiksi merkitäkseen sen valmiiksi.

**Suodatin**-painike listan yläpuolella suodattaa tehtävät otsikon, tilan, prioriteetin tai tunnisteen mukaan, GOQL-ilmaisulla tai [edistyneellä suodattimella](lists.md#advanced-filter). Useiden tilojen tai prioriteettien valitseminen näyttää tehtäviä, joilla on jokin niistä, esimerkiksi kaikki avoimet ja estetyt tehtävät.

## Muokkaa tehtävää

Tehtäväsivulla ei ole erillistä "muokkaustilaa" kuten muilla Gramps-objekteilla:

- Napsauta otsikkoa muokataksesi sitä. Paina Enter, napsauta ✓ tai napsauta muualle tallentaaksesi; paina Escape tai napsauta ✕ peruuttaaksesi.
- Muutokset tilassa ja prioriteetissa tulevat voimaan heti.
- Muokataksesi kuvausta tai liitteitä, napsauta muokkauspainiketta osion otsikon vieressä. Kuvaus tallennetaan "tallenna"-painikkeella sen alapuolella; liitteiden muokkaaminen päättyy **Valmis**.
- Lukituspainike asettaa, onko tehtävä yksityinen. Tehtävän kuvaus saa saman yksityisyyden.

Muokkausoikeudet ilman käyttäjät näkevät tilan ja prioriteetin tekstinä, ja osiot ilman sisältöä on piilotettu.

Otsikon alla muokkaajat näkevät kaksi muuta painiketta: **Muokkaa lähdettä** avaa lähteen, joka edustaa tehtävää, jossa sen muut muistiinpanot, viittaukset ja attribuutit voidaan muokata. **Poista** poistaa tehtävän vahvistuksen jälkeen ja palaa tehtävälistaan; näkyvä viesti sisältää kumoa-painikkeen tehtävän palauttamiseksi.

## Tehtävien ominaisuuksien joukkomuutos

Muokkausoikeudet omaavat käyttäjät näkevät valintaruudun jokaisella rivillä tehtävälistassa. Valitse tehtävät ja käytä **Aseta prioriteetti** tai **Aseta tila** listan yläpuolella muuttaaksesi kaikki valitut tehtävät kerralla.

## Tehtävät Gramps Desktopissa

Kun lisäät tehtäviä Gramps Webin kautta, sekä lähteet että muistiinpanot saavat `ToDo`-tunnisteen, joten tehtävät näkyvät työpöydän [To Do Notes Gramplet](https://gramps-project.org/wiki/index.php/Addon:ToDoNotesGramplet) sekä [To Do Report](https://gramps-project.org/wiki/index.php/Addon:ToDoReport) -raportissa.

Lisätäksesi tai muokataksesi tehtävää Gramps Desktopissa, käytä seuraavia ohjeita

- Lisää lähde tunnisteella `ToDo` ja tehtävän otsikko otsikkona
- Valinnaisesti, lisää muistiinpano lähteeseen tunnisteella `ToDo`, kirjoita "To Do" ja kuvaus tekstinä
- Lisää attribuutti "Tila" ja aseta se "Avoin", "Käynnissä", "Estetty" tai "Valmis"
- Lisää attribuutti "Prioriteetti" ja aseta se 9 matalalle, 5 keskitasolle tai 1 korkealle (nämä vastakkaiset arvot on otettu iCalendar-määrityksestä)
