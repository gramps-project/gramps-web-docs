# Käytä sisäänrakennettua tehtävien hallintaa

Gramps Web sisältää sisäänrakennetun geneologisen tehtävien hallintatyökalun. Sen tarkoitus on mahdollistaa tutkijoiden suunnitella ja priorisoida, mutta myös dokumentoida tehtävänsä. Tästä syystä tehtävät esitetään lähteinä Gramps-tietokannassa. Tehtävän valmistuttua siihen liittyvä sisältö voi toimia lähteenä, joka dokumentoi tutkimusprosessia.

## Tehtävien perusteet

Tehtävillä on seuraavat ominaisuudet:

- Tila. Tämä voi olla "Avoin", "Käynnissä", "Estetty" tai "Valmis"
- Prioriteetti. Tämä voi olla "Matala", "Keskitaso" tai "Korkea"
- Tunnisteet. Tunnisteet ovat normaaleja Gramps-tunnisteita taustalla olevalle lähteelle. (Huomaa, että kaikilla tehtävillä on lisäksi `ToDo`-tunniste, joka tunnistaa ne tehtäviksi, mutta tämä tunniste on piilotettu tehtäväluettelossa häiriön välttämiseksi.)
- Otsikko. Näkyy tehtäväluettelossa
- Kuvaus. Rikkaan tekstin kenttä, jota voidaan käyttää ongelman kuvauksen tekemiseen, mutta myös edistymisen dokumentointiin
- Media. Kaikki mediapaketit, jotka on liitetty tehtävään

## Luo tehtävä

Koska tehtävät ovat normaaleja Gramps-objekteja, niitä voivat muokata tai luoda samat käyttäjäryhmät, jotka voivat muokata tai luoda muita objekteja (kuten henkilöitä tai tapahtumia).

Luoaksesi tehtävä, napsauta + -painiketta tehtäväluettelon sivulla. Syötä vähintään otsikko ja valinnaisesti prioriteetti, kuvaus, liitteet ja tunnisteet. Tila on aina "Avoin" luotaessa.

## Tehtäväluettelo

Tehtäväluettelo on järjestetty tilan mukaan – valmiit tehtävät viimeisenä – ja kunkin tilan sisällä prioriteetin mukaan, korkein ensin.

Napsauta tehtävää avataksesi sen. Muokkausoikeudet omaavat käyttäjät voivat myös napsauttaa tehtävän tilakuvaketta muuttaakseen sen tilaa suoraan luettelossa, esimerkiksi merkitäkseen sen valmiiksi.

**Suodatin**-painike luettelon yläpuolella suodattaa tehtävät tunnisteen, [GOQL](goql.md) -ilmaisun tai [kehittyneen suodattimen](lists.md#advanced-filter) mukaan.

## Muokkaa tehtävää

Tehtäväsivulla ei ole erillistä "muokkaustilaa" kuten muilla Gramps-objekteilla:

- Napsauta otsikkoa muokataksesi sitä. Paina Enter, napsauta ✓ tai napsauta muualle tallentaaksesi; paina Escape tai napsauta ✕ peruuttaaksesi.
- Muutokset tilassa ja prioriteetissa tulevat voimaan heti.
- Muokataksesi kuvausta tai liitteitä, napsauta muokkauspainiketta osion otsikon vieressä. Kuvaus tallennetaan "tallenna" -painikkeella sen alapuolella; liitteiden muokkaaminen päättyy **Valmis**.
- Lukituspainike määrittää, onko tehtävä yksityinen. Tehtävän kuvaus saa saman yksityisyyden.

Käyttäjät, joilla ei ole muokkausoikeuksia, näkevät tilan ja prioriteetin tekstinä, ja osiot, joissa ei ole sisältöä, on piilotettu.

Otsikon alla muokkaajat näkevät kaksi muuta painiketta: **Muokkaa lähdettä** avaa lähteen, joka edustaa tehtävää, jossa sen muut muistiinpanot, viittaukset ja attribuutit voidaan muokata. **Poista** poistaa tehtävän vahvistuksen jälkeen ja palaa tehtäväluetteloon; ilmestyvässä viestissä on kumoa-painike, jolla tehtävän voi palauttaa.

## Tehtävien ominaisuuksien massamuutos

Käyttäjät, joilla on muokkausoikeudet, näkevät valintaruudun jokaisella rivillä tehtäväluettelossa. Valitse tehtävät ja käytä **Aseta prioriteetti** tai **Aseta tila** -painiketta luettelon yläpuolella muuttaaksesi kaikki valitut tehtävät kerralla.

## Tehtävät Gramps Desktopissa

Kun lisäät tehtäviä Gramps Webin kautta, sekä lähteet että muistiinpanot saavat `ToDo`-tunnisteen, joten tehtävät näkyvät työpöydän [To Do Notes Gramplet](https://gramps-project.org/wiki/index.php/Addon:ToDoNotesGramplet) -sovelluksessa sekä [To Do Report](https://gramps-project.org/wiki/index.php/Addon:ToDoReport) -raportissa.

Lisätäksesi tai muokataksesi tehtävää Gramps Desktopissa, käytä seuraavia ohjeita:

- Lisää lähde tunnisteella `ToDo` ja tehtävän otsikko otsikkona
- Valinnaisesti, lisää muistiinpano lähteeseen tunnisteella `ToDo`, kirjoita "To Do" ja kuvaus tekstinä
- Lisää attribuutti "Tila" ja aseta se "Avoin", "Käynnissä", "Estetty" tai "Valmis"
- Lisää attribuutti "Prioriteetti" ja aseta se 9 matalalle, 5 keskitasolle tai 1 korkealle (nämä vastoin intuitiota olevat arvot on otettu iCalendar-määrityksestä)
