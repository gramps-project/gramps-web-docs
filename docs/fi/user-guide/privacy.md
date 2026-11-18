# Yksityiset tiedot

Mikä tahansa tietue puussa voidaan merkitä yksityiseksi. Yhdessä [käyttäjäroolien](../install_setup/users.md#user-roles) kanssa tämä päättää, kuka näkee mitä.

## Kuka näkee mitä

Gramps Web ei koskaan ole avoin julkiselle: vain käyttäjät, joilla on tili, voivat nähdä mitään. "Julkinen" Grampsissa tarkoittaa yksinkertaisesti "ei yksityinen", eli näkyvissä kaikille sisäänkirjautuneille käyttäjille puussa.

| Rooli | Julkiset tiedot | Yksityiset tiedot |
|---|---|---|
| Vieras | katso | – |
| Jäsen | katso | katso |
| Avustaja | katso, lisää | katso, lisää |
| Toimittaja, Omistaja, Ylläpitäjä | katso, lisää, muokkaa, poista | katso, lisää, muokkaa, poista |

Vierailla yksityiset tiedot eivät ole olemassa: ne jätetään pois sivuilta, listoista, hakutuloksista, kaavioista, raporteista, vientitiedostoista ja tekoälyavustajan vastauksista. Tämä toteutuu siellä, missä palvelin lukee tietokantaa, ei piilottamalla asioita sovelluksessa, joten vieras ei voi päästä yksityisiin tietoihin millään muulla tavalla.

Tilin, jota ei ole vielä hyväksytty (itse [rekisteröinnin](registration.md) jälkeen), ei voi kirjautua sisään lainkaan.

Joten jos sukulaiset tai muut vierastilit eivät saisi nähdä tiettyjä tietoja, merkitse ne yksityisiksi. Jos kaikki puun käyttäjät voivat nähdä kaiken, anna heille jäsenrooli (tai korkeampi), eikä mitään tarvitse merkitä yksityiseksi.

## Elävät ihmiset eivät ole automaattisesti yksityisiä

Mikään ei tule automaattisesti yksityiseksi – ei edes ihmiset, jotka ovat vielä elossa. Elävien ihmisten tiedot ovat näkyvissä vieraille, kunnes merkitset ne yksityisiksi. Tämä koskee myös tuotuja puita.

Merkitäksesi todennäköisesti elävät ihmiset yksityisiksi Gramps Webissä:

1. Ihmisluettelossa avaa [edistynyt suodatin](lists.md#advanced-filter) ja lisää ehto "Todennäköisesti elävät ihmiset" (jätä päivämäärä tyhjäksi tänään). Käytä suodatinta.
2. Napsauta **Valitse**, rastita valintaruutu otsikossa ja valitse **Valitse kaikki**.
3. Valitse **Yksityisyys**-toiminto ja merkitse tiedot yksityisiksi.

"Todennäköisesti elävät" arvioidaan henkilön ja heidän sukulaistensa päivämäärien perusteella. Ihmiset, joilla ei ole käytettävissä olevia päivämääriä, katsotaan eloonjääneiksi. Tarkista tulos ja pidä mielessä, että arvio voi muuttua, kun lisäät tietoja.

Henkilön merkitseminen yksityiseksi piilottaa henkilön, mutta ei heidän tapahtumiaan, muistiinpanojaan, medioitaan tai perheitään – katso alla. Gramps Desktopissa on enemmän työkaluja monien liittyvien tietojen yksityisyyden asettamiseen kerralla, joita voit käyttää [Sync-lisäosan](../administration/sync.md) kanssa.

Myöhemmin kuolevat ihmiset eivät myöskään tule automaattisesti julkisiksi. Halutaanko se, on sinun päätettävissäsi – monet tutkijat suosivat kerättyjen tietojen pitämistä yksityisinä jonkin aikaa.

## Lukkoikoneiden lukeminen

Käyttäjät, jotka voivat nähdä yksityisiä tietoja, näkevät lukon yksityisten kohteiden vieressä. On kahta tyyppiä:

- **Täytetty lukko** – itse tietue on yksityinen. Esimerkiksi henkilön sivulla täytetty lukko tapahtuman vieressä tarkoittaa, että tapahtuma on yksityinen, ja lapsen vieressä, että lapsi on yksityinen.
- **Ääriviivalukko** – vain *linkki* on yksityinen, ei tietue, johon se johtaa. Esimerkiksi henkilön linkki tapahtumaan voi olla yksityinen, kun taas itse tapahtuma on julkinen. Tapahtuma on sitten piilotettu kyseisen henkilön sivulta, mutta näkyvissä muualla, kuten muiden osallistujien sivuilla tai tapahtumalistassa.

Jos sekä tietue että sen linkki ovat yksityisiä, näytetään täytetty lukko.

Sama erottelu koskee lapsia (lapsi tai lapsen linkki perheeseen), yhdistyksiä, lähteen arkistointilinkkejä ja medioita galleriassa. Nimet, attribuutit, osoitteet ja URL-osoitteet kuuluvat niiden tietueeseen ja niillä on vain täytetty lukko.

## Jotain yksityiseksi tekeminen

Tarvitset muokkausoikeudet muuttaaksesi yksityisyyttä.

- **Koko tietue**: avaa sen sivu, siirry muokkaustilaan ja napsauta lukko-painiketta työkalupalkissa.
- **Osa tietuetta** – vaihtoehtoinen nimi, attribuutti, osoite, URL, yhdistys, lapsilinkki tai arkistointilinkki: avaa kyseisen kohteen muokkausdialogi ja kytke **Yksityinen**-kytkin päälle. Pääasiallisella nimellä ei ole kytkintä, koska henkilö muuten näyttäisi olevan "Yksityinen".
- **Tapahtuma henkilön tai perheen sivulta**: tapahtuman muokkausdialogissa on yksityisyyskytkin itse tapahtumalle. Jos tapahtuma jaetaan muiden kanssa, se voidaan muokata vain sen jälkeen, kun valitset **Muokkaa kaikille**, koska se on yksityinen kaikille heille.
- **Henkilön linkki tapahtumaan**: tapahtumasivulla avaa osallistujan rivi muokkaustilassa. Yksityisyyskytkin siellä koskee vain kyseisen osallistujan linkkiä, joten tapahtuma pysyy näkyvissä muille osallistujille.
- **Mediaobjekti galleriassa**: muokkaustilassa napsauta lukkoa laatikon kulmassa.
- **Monet tietueet kerralla**: valitse ne listasta ja käytä **Yksityisyys**-toimintoa, katso [Listat](lists.md#tags-and-privacy).

Tarkistaaksesi, mitkä tietueet listassa ovat yksityisiä, kytke **Yksityisyys**-sarake päälle listan sarakevalitsimessa.

## Asioita, joita on hyvä pitää mielessä

- Tietueen merkitseminen yksityiseksi ei tee siihen linkitettyjä tietueita yksityisiksi. Jos henkilö on yksityinen, heidän tapahtumansa, perheet, joihin he kuuluvat, ja niihin liitetyt muistiinpanot ovat edelleen näkyvissä, elleivät ne ole itse yksityisiä. Käytä edistynyttä suodatinta tai **Yksityisyys**-saraketta tarkistaaksesi liittyvät tietueet.
- Perheen tai tapahtuman merkitseminen yksityiseksi piilottaa sen, mutta ei sen sisällä olevia ihmisiä.
- [DNA-ottelut ja Y-DNA-tiedot](dna-matches.md#private-matches) sisältävät oman **Yksityinen**-kytkimen dialogeissaan.
- Vientitiedostot ja media-arkistot, joita käyttäjä ei voi nähdä yksityisiä tietoja, eivät sisällä yksityisiä tietueita tai tiedostoja.
- Yksityisyys on Grampsin ominaisuus, joten Gramps Desktopissa merkittyjen yksityisten tietueiden on oltava yksityisiä myös Gramps Webissä ja päinvastoin.
