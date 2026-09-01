# Tunnisteet

Tunnisteet ovat etikettejä, joita voidaan soveltaa mihin tahansa objektiin Gramps-tietokannassa – ihmisiin, perheisiin, tapahtumiin, paikkoihin, lähteisiin, viittauksiin, arkistoihin, muistiinpanoihin ja mediaan. Ne ovat hyödyllisiä objektien ryhmittelyssä ja suodattamisessa. Tunnisteet tallennetaan Gramps-perhesuhdetietokantaan ja ne jaetaan kaikkien käyttäjien kesken; ne ovat myös täysin yhteensopivia Gramps Desktopissa luotujen tunnisteiden kanssa.

## Tunnisteiden hallinta

Tunnisteita hallitaan **Tunnisteet**-osiossa [Hallintasettings](../administration/settings.md#tags), joka on saatavilla vain omistaja- tai ylläpitäjäroolissa oleville käyttäjille. Se näyttää kaikki olemassa olevat tunnisteet ja mahdollistaa:

- **Luo** uusi tunniste **Uusi tunniste** -painikkeella
- **Nimeä** tunniste uudelleen muokkaus (kynä) kuvaketta käyttäen
- **Vaihda tunnisteen väri** värivalitsimella
- **Poista** tunniste poistoikonia käyttäen

!!! huomautus
    Tunnisteen poistaminen poistaa sen kaikista objekteista, joihin se oli sovellettu.

## Tunnisteiden soveltaminen objekteihin

Tunnisteita voidaan soveltaa tai poistaa objektista sen yksityiskohtasivulla muokkaustilassa.

## Suodattaminen tunnisteen mukaan

Kaikilla [objektin luettelon sivuilla](lists.md) (Ihmiset, Perheet, Tapahtumat, Paikat, Lähteet, Viittaukset, Arkistot, Muistiinpanot, Media) on tunnistesuodatin. Käytä sitä näyttääksesi vain ne objektit, joihin on sovellettu tietty tunniste.

## Erityiset tunnisteet

Kaksi tunnistetta on erityistä merkitystä Gramps Webissä:

- **`Blog`** – mikä tahansa lähde, johon on merkitty `Blog`, käsitellään blogikirjoituksena ja se näkyy [Blogi](blog.md) -näkymässä
- **`ToDo`** – mikä tahansa muistiinpano, johon on merkitty `ToDo`, käsitellään tutkimustehtävänä ja se näkyy [Tehtävät](tasks.md) -näkymässä

Nämä tunnisteet luodaan automaattisesti, kun käytät ensimmäisen kerran Blogi- tai Tehtävät-ominaisuuksia. Niiden nimeäminen uudelleen tai poistaminen rikkoo vastaavaa ominaisuutta.
