# Tunnisteet

Tunnisteet ovat etikettejä, joita voidaan soveltaa mihin tahansa objektiin Gramps-tietokannassa – ihmisiin, perheisiin, tapahtumiin, paikkoihin, lähteisiin, viittauksiin, arkistoihin, muistiinpanoihin ja mediaan. Ne ovat hyödyllisiä objektien ryhmittelyssä ja suodattamisessa. Tunnisteet tallennetaan Gramps-perhesuunnitelmatietokantaan ja ne ovat kaikkien käyttäjien käytettävissä; ne ovat myös täysin yhteensopivia Gramps Desktopissa luotujen tunnisteiden kanssa.

## Tunnisteiden hallinta

Tunnisteita hallitaan **Tunnisteet**-osiossa [Hallintasettings](../administration/settings.md#tags), joka on saatavilla vain käyttäjille, joilla on Omistaja- tai Ylläpitäjärooli. Se näyttää kaikki olemassa olevat tunnisteet ja mahdollistaa:

- **Luo** uusi tunniste **Uusi tunniste** -painikkeella
- **Nimeä** tunniste uudelleen muokkaus (kynä) kuvaketta käyttäen
- **Vaihda tunnisteen väri** värivalitsimen avulla
- **Poista** tunniste poistoikonia käyttäen

!!! huomautus
    Tunnisteen poistaminen poistaa sen kaikista objekteista, joihin se on sovellettu.

## Tunnisteiden soveltaminen objekteihin

Tunnisteita voidaan soveltaa tai poistaa objektista sen yksityiskohtasivulla muokkaustilassa.

## Suodattaminen tunnisteen mukaan

Kaikki objektin luettelon sivut (Ihmiset, Perheet, Tapahtumat, Paikat, Lähteet, Viittaukset, Arkistot, Muistiinpanot, Media) sisältävät tunnistesuodattimen. Käytä sitä näyttämään vain ne objektit, joihin on sovellettu tiettyä tunnistetta.

## Erityiset tunnisteet

Kaksi tunnistetta on erityistä merkitystä Gramps Webissä:

- **`Blog`** – mikä tahansa lähde, johon on merkitty `Blog`, käsitellään blogikirjoituksena ja se näkyy [Blogi](blog.md) -näkymässä
- **`ToDo`** – mikä tahansa muistiinpano, johon on merkitty `ToDo`, käsitellään tutkimustehtävänä ja se näkyy [Tehtävät](tasks.md) -näkymässä

Nämä tunnisteet luodaan automaattisesti, kun käytät ensimmäistä kertaa Blogi- tai Tehtävät-ominaisuuksia. Niiden nimeäminen uudelleen tai poistaminen rikkoo vastaavaa ominaisuutta.
