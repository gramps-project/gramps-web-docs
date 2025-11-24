# Käytä sisäänrakennettua tehtävien hallintaa

Gramps Web sisältää sisäänrakennetun sukututkimustehtävien hallintatyökalun. Sen tarkoituksena on mahdollistaa tutkijoiden suunnitella ja priorisoida, mutta myös dokumentoida tehtävänsä. Tämän vuoksi tehtävät esitetään lähteinä Gramps-tietokannassa. Tehtävän suorittamisen jälkeen siihen liittyvä sisältö voi toimia lähteenä, joka dokumentoi tutkimusprosessia.

## Tehtävien perusteet

Tehtävillä on seuraavat ominaisuudet:

- Tila. Tämä voi olla "Avoin", "Käynnissä", "Estetty" tai "Valmis"
- Prioriteetti. Tämä voi olla "Matala", "Keskitaso" tai "Korkea"
- Tunnisteet. Tunnisteet ovat normaaleja Gramps-tunnisteita taustalla olevasta lähteestä. (Huomaa, että kaikilla tehtävillä on lisäksi `ToDo`-tunniste, joka tunnistaa ne tehtävinä, mutta tämä tunniste on piilotettu tehtäväluettelossa häiriön välttämiseksi.)
- Otsikko. Näytetään tehtäväluettelossa
- Kuvaus. Rikkaan tekstin kenttä, jota voidaan käyttää ongelman kuvauksen tekemiseen, mutta myös dokumentoimaan tehty edistyminen
- Media. Kaikki mediatiedostot, jotka on liitetty tehtävään

## Luo tehtävä

Koska tehtävät ovat normaaleja Gramps-objekteja, niitä voivat muokata tai luoda samat käyttäjäryhmät, jotka voivat muokata tai luoda muita objekteja (kuten henkilöitä tai tapahtumia).

Luoaksesi tehtävä, napsauta + -painiketta tehtäväluettelon sivulla. Syötä vähintään otsikko. Tila on aina "Avoin" luotaessa.

## Muokkaa tehtävää

Muokataksesi mitä tahansa tehtävän tietoja, napsauta sitä tehtäväluettelossa.

Tehtävän yksityiskohtasivulla ei ole erillistä "muokkaustilaa" kuten muilla Gramps-objekteilla. Muutokset otsikossa, tilassa ja prioriteetissa tulevat voimaan heti. Muutokset rikkaan tekstin kuvauksessa vaativat "tallenna" -painikkeen napsauttamista sen alla.

## Tehtävien ominaisuuksien massamuutos

Tehtävien prioriteetti ja tila voidaan muuttaa massana käyttämällä valintaruutuja tehtäväluettelossa valitsemiseen ja asianmukaisia painikkeita tehtäväluettelon yläpuolella.

## Tehtävät Gramps Desktopissa

Kun lisäät tehtäviä Gramps Webin kautta, sekä lähteet että muistiinpanot saavat `ToDo`-tunnisteen, joten tehtävät näkyvät työpöydän [To Do Notes Grampletissä](https://gramps-project.org/wiki/index.php/Addon:ToDoNotesGramplet) sekä [To Do -raportissa](https://gramps-project.org/wiki/index.php/Addon:ToDoReport).

Lisätäksesi tai muokataksesi tehtävää Gramps Desktopissa, käytä seuraavia ohjeita

- Lisää lähde tunnisteella `ToDo` ja tehtävän otsikko otsikkona
- Valinnaisesti, lisää muistiinpano lähteeseen tunnisteella `ToDo`, kirjoita "To Do" ja kuvaus tekstinä
- Lisää attribuutti "Tila" ja aseta se "Avoin", "Käynnissä", "Estetty" tai "Valmis"
- Lisää attribuutti "Prioriteetti" ja aseta se 9 matalalle, 5 keskitasolle tai 1 korkealle (nämä vastoin intuitiota olevat arvot on otettu iCalendar-määrityksestä)
