---
hide:
  - toc
  - navigation
---

# Ominaisuudet

Gramps Web on verkkosovellus yhteistyöhön sukututkimuksessa. Se on rakennettu [Gramps](https://gramps-project.org/) -avointa lähdekoodia olevan sukututkimusohjelman päälle ja toimii samoilla tiedoilla. Voit käyttää sitä omalla palvelimellasi tai käyttää hosting-palvelua.

[Kokeile demoa](#demo){ .md-button .md-button--primary } [Aloita](../install_setup/setup.md){ .md-button }

## Tutki sukupuuta { .feature-group }

![Fanikaavio, joka näyttää seitsemän sukupolvea esi-isiä](screenshots/fan.png){ align=right width="400"}

### Interaktiiviset sukupuu-kaaviot

Selaa sukupuuta esi-isäpuuna, jälkeläispuuna, tiimalasikaaviona, sukulaissuhteiden kaaviona tai fanikaaviona, korkealaatuisilla interaktiivisilla grafiikoilla ja säädettävällä sukupolvien määrällä.

Vie hiiri minkä tahansa henkilön päälle nähdäksesi esikatselukortin heidän keskeisistä tiedoistaan, ja siirry suoraan kaaviosta täydelle yksityiskohtasivulle.

<div style="clear:both;"></div>

---

![Aikajana perhetilanteista 1940- ja 1970-lukujen välillä](screenshots/timeline.png){ align=left width="400"}

### Aikajana

Näe jokainen tapahtuma sukupuussasi esitettynä vaakasuoralla, zoomattavalla aikajanalla. Selaa ja zoomaa vuosisatojen läpi, sitten suodata yhteen henkilöön – tai kaikkiin heidän esi-isiinsä tai jälkeläisiinsä – tai kaikkeen, mitä tapahtui yhdessä paikassa.

Katso [Aikajana](../user-guide/timeline.md).

<div style="clear:both;"></div>

---

![Lontoon kartta valitulla paikalla, joka näyttää sen kuvan ja tapahtumat](screenshots/map.png){ align=right width="400"}

### Interaktiivinen kartta

Näytä kaikki paikat sukupuussasi interaktiivisella, haettavalla kartalla. Etsi uusia paikkoja suoraan OpenStreetMapista luodessasi paikkaa, paikanna tietokannassasi olevat ihmiset maantieteellisesti ja seuraa yhden henkilön elämää yhdistämällä heidän tapahtumansa viivoilla kartalla.

<div style="clear:both;"></div>

---

![Lontoo OpenHistoricalMap-kerroksella, aikajänne säädettynä vuoteen 1707](screenshots/ohm.png){ align=left width="400"}

### Historialliset kartat

Muunna historiallinen kartta, joka on tallennettu mediaobjektina Grampsissa, mukautetuksi karttakerrokseksi.

Voit myös vaihtaa [OpenHistoricalMap](https://www.openhistoricalmap.org/) -projektin historiallisille vektorkartoille. Käytä aikajännettä selataksesi sukusi historian paikkojen kehitystä ja näytä paikat, joissa esi-isät asuivat tai tapahtumat tapahtuivat.

<div style="clear:both;"></div>

---

![Hakutulokset "Albert" henkilöistä, tapahtumista ja medioista](screenshots/search.png){ align=right width="400"}

### Löydä mitä tahansa

Koko tekstihaku kattaa kaikki Gramps-objekti-tyypit, mukaan lukien tekstimuistiinpanojen sisällön, ja tukee jokerimerkkejä ja loogisia operaattoreita.

Tarkkoja kyselyjä varten objektin luettelonäkymät tarjoavat edistyneen suodatinmoodin, joka perustuu [Gramps Object Query Language](../user-guide/goql.md) -kieleen, sekä nopeita suodattimia tekstin, tunnisteen ja yksityisyyden mukaan.

Minkä tahansa henkilön sivulta, [Ulkoinen haku](../user-guide/external-search.md) avaa esitäytetyn haun FamilySearchissä, Ancestryssä, CompGenissä ja muilla sivustoilla – ja voit lisätä omasi.

<div style="clear:both;"></div>

## Rakenna ja tutki { .feature-group }

![Esi-isäpuu muokkaustilassa perheenjäsenen lisäämistä varten](screenshots/tree-edit.png){ align=left width="400"}

### Rakenna sukupuusi suoraan kaaviossa

Vaihda puunäkymä muokkaustilaan ja kasvata sukupuuta poistumatta kaaviosta. Jokaisessa henkilökortissa on **+** -painike isän, äidin, lapsen tai puolison lisäämiseksi – joko linkittämällä joku, joka on jo tietokannassasi tai luomalla täysin uusi henkilö paikan päällä. Jokainen muutos tallennetaan heti.

Katso [Sukupuun muokkaaminen](../user-guide/tree-edit.md).

<div style="clear:both;"></div>

---

![AI-avustaja lukemassa syntymätodistusta ja ehdottamassa uusia tietoja](screenshots/chat.png){ align=right width="400"}

### Integroitu AI-avustaja

Kysy kysymyksiä sukupuustasi omalla kielelläsi ja saat vastauksia perustuen tietoihisi.

Avustaja ei vain hae: se kysyy suoraan tietokannastasi työkalusarjalla, suodattamalla ihmisiä, tapahtumia, perheitä ja paikkoja, ja laskemalla suhteita yksilöiden välillä. Voit seurata, mitä työkaluja se käyttää rakentaessaan vastausta, ja pidemmät kysymykset toimivat taustatehtävinä, joten voit siirtyä muualle ja palata takaisin.

Avustaja on valinnainen ja se on [asetettava palvelimen ylläpitäjän](../install_setup/chat.md) toimesta AI-mallin tarjoajan kanssa.

<div style="clear:both;"></div>

---

![Kromosomiselain, joka näyttää yhteiset DNA-segmentit yhdestätoista osumasta](screenshots/dna.png){ align=left width="400"}

### DNA-osumat, kromosomiselain & Y-DNA

Lataa DNA-osumatiedot DNA-testauksen tarjoajaltasi, tallenna ne sukupuusi rinnalle ja tarkastele osumiasi interaktiivisessa kromosomiselain.

Raaka Y-kromosomi SNP -dataa voidaan käyttää henkilön todennäköisimmän [Y-DNA haplogrupi](../user-guide/y-dna.md) määrittämiseen ja näyttää heidän isälinjaiset esi-isänsä ihmisen Y-kromosomipuussa aikaraja-arvioilla. Analyysi suoritetaan kokonaan omalla palvelimellasi – mitään tietoja ei lähetetä kolmannelle osapuolelle.

<div style="clear:both;"></div>

---

![Maalaus, jossa kaksi henkilöä on merkitty ja muut tunnistetut kasvot on rajattu](screenshots/tag.png){ align=right width="400"}

### Merkitse ihmisiä valokuvissa automaattisella kasvojentunnistuksella

Tunnista esi-isät vanhoista perhekuvista yhdessä sukulaistesi kanssa. Kasvot tunnistetaan automaattisesti, joten henkilön merkitseminen vie vain kaksi klikkausta.

<div style="clear:both;"></div>

---

![Tutkimustehtävien luettelo tilan, prioriteetin ja tunnisteiden kanssa](screenshots/tasks.png){ align=left width="400"}

### Integroitu tehtävienhallintasovellus

Gramps Web sisältää integroidun tehtävienhallintasovelluksen sukututkimuksesi järjestämiseen ja suunnitteluun. Anna jokaiselle tehtävälle tila, prioriteetti ja tunnisteet, dokumentoi edistymisesi rikkaassa tekstikuvauksessa ja liitä keräämäsi media matkan varrelta.

Tehtävät tallennetaan lähteinä Gramps-tietokantaan, joten ne muodostavat osan sukututkimustiedoistasi ja niitä voidaan käyttää ja muokata myös Gramps Desktopissa.

<div style="clear:both;"></div>

---

![Blogikirjoitus perhekuvassa olevien henkilöiden tunnistamisesta](screenshots/blog.png){ align=right width="400"}

### Sukututkimusblogi mukana

Tiivistä tutkimuksesi blogitarinoiden muodossa kuvien kanssa ja jaa ne sukulaistesi kanssa. Erityinen editori tekee uuden postauksen kirjoittamisesta vaivatonta. Kaikki tiedot tallennetaan Gramps-tietokantaan.

<div style="clear:both;"></div>

## Tee yhteistyötä { .feature-group }

![Luettelo ihmisistä sukupuussa](screenshots/list.png){ align=left width="400"}

### Yksityisyystasot & käyttäjäoikeudet

Voit [merkitä tietueita yksityisiksi](../user-guide/privacy.md) – jopa yksittäiselle nimelle, tapahtumalinkille tai DNA-osumalle – ja hallita, mitkä käyttäjät saavat nähdä yksityiset tietueet. Yksityiset tietueet suodatetaan tietokantatasolla maksimaalisen turvallisuuden takaamiseksi. Lisäksi voit hallita, mitä käyttäjät voivat lisätä ja muokata.

Käyttäjät voivat kirjautua sisään salasanalla tai ulkoisen identiteettipalveluntarjoajan kautta käyttäen [OpenID Connect](../install_setup/oidc.md) – Google ja Microsoft valmiina, plus mukautetut tarjoajat kuten Keycloak, Authentik ja Authelia.

<div style="clear:both;"></div>

---

![Muutos, joka näyttää kentät, joita on muutettu henkilötietueessa](screenshots/revisions.png){ align=right width="400"}

### Täydellinen muutoshistoria – kumoa

Jokainen muutos sukupuussasi tallennetaan. Selaa koko historiaa ryhmiteltynä tapahtumittain, syvenny mihin tahansa yksittäiseen muutokseen nähdäksesi tarkalleen, mitkä kentät on lisätty, poistettu tai muutettu, ja kumoa tapahtuma, jos se osoittautuu virheeksi. Jokaisen objektin sivulla on myös oma muutosvälilehti, joka näyttää, kuka sen muutti ja milloin.

Katso [Muutoshistoria](../user-guide/revisions.md).

<div style="clear:both;"></div>

---

![Gramps Desktopin Työkalut-valikko Gramps Web Sync -merkinnällä](screenshots/sync.png){ align=left width="300"}

### Täydellinen integraatio Gramps Desktopin kanssa

Gramps Web käyttää samaa tietomallia ja tietokantaa kuin [Gramps Desktop](https://gramps-project.org/). Voit selata ja muokata kaikkia samoja [tietuetyyppejä](https://gramps-project.org/wiki/index.php/Gramps_Data_Model): ihmiset, perheet, tapahtumat, paikat, arkistot, lähteet, viittaukset, mediaobjektit ja muistiinpanot.

[Gramps Web Sync -lisäosan](../administration/sync.md) avulla Gramps Desktopissa voit synkronoida tietosi molempiin suuntiin, joten voit jatkaa työskentelyä Gramps Desktopissa ja Gramps Webissä rinnakkain.

<div style="clear:both;"></div>

## Raportit ja tietojen vienti { .feature-group }

![Esi-isäraportti, joka on luotu PDF-muodossa](screenshots/report.png){ align=right width="400"}

### Tuota tulostettavia raportteja

Gramps Web on rakennettu saman ytimen päälle kuin Gramps Desktop, joten voit luoda lähes kaikki [raportit](https://gramps-project.org/wiki/index.php/Gramps_6.0_Wiki_Manual_-_Reports), joita työpöytäsovellus tukee suoraan selaimesta, mukaan lukien sukulaissuhteiden kaaviot tai kirjaraportit PDF-muodossa.

<div style="clear:both;"></div>

---

![Vientisivu, jossa on saatavilla olevien tiedostomuotojen luettelo](screenshots/export.png){ align=left width="300"}

### Ei lukitusta – tietojen tuonti ja vienti

Tuo tietoja eri muodoissa, mukaan lukien Gramps XML ja GEDCOM, ja lataa kaikki tietosi milloin tahansa – sukupuutatiedot, mediatiedostot ja käyttäjätilit – varmuuskopioita varten tai siirtääksesi toiseen palvelimeen.

Tuontia voidaan esikatsella kuivaharjoituksena ennen kuin mitään kirjoitetaan, ja täydellinen varmuuskopio voidaan palauttaa takaisin puuhun.

<div style="clear:both;"></div>

## Käytä sitä missä tahansa { .feature-group }

![Sama henkilösivu tietokoneella ja puhelimella](screenshots/mobile.png){ align=right width="400"}

### Toimii kaikilla laitteilla

Käytä Gramps Webiä millä tahansa laitteella, jossa on verkkoselain: lataa valokuvia, luo tai muokkaa tietueita tai näytä sukupuusi sukulaisillesi seuraavassa perhekokouksessa.

Gramps Web on progressiivinen verkkosovellus: asenna se aloitusnäyttöösi tai työpöydällesi ja se käyttäytyy kuin natiivisovellus. Työpöydällä [näppäinoikotiet](../user-guide/shortcuts.md) vievät sinut minne tahansa muutamalla näppäinpainalluksella – paina `?` nähdäksesi kaikki.

<div style="clear:both;"></div>

---

![Kielivalintavalikko](screenshots/lang.png){ align=left width="300"}

### Täysin kansainvälistetty

Käytä käyttöliittymää missä tahansa yli 50 kielessä, jotka Gramps-yhteisö on kääntänyt.

<div style="clear:both;"></div>

## Ja lisää

- **Ilmoitukset ja taustatehtävät** – tuonnit, viennit, raportit ja indeksin uudelleenrakentamiset toimivat taustalla, ja edistymistä ja virheitä kerätään yhteen paikkaan
- **Tunnisteet, kirjanmerkit ja historia** – järjestä objekteja väriin perustuvilla tunnisteilla ja palaa siihen, mitä olit tekemässä
- **Massamuokkaus** – valitse useita objekteja luettelonäkymistä poistaaksesi ne kerralla tai yhdistääksesi kaksoiskappaleet
- **Mukautettavat luettelonäkymät** – valitse, mitkä sarakkeet näytetään, ja suodata tekstin, tunnisteen tai yksityisyyden mukaan
- **Tekstintunnistus (OCR)** – poimi tekstiä skannatuista asiakirjoista mediagalleriassasi
- **Tietojen tarkistus** – tarkista puusi epäuskottavien päivämäärien ja muiden tietojen ongelmien varalta
- **Kalenterit** – syötä päivämääriä gregoriaaniseen, juliaaniseen, heprealaiseen, ranskalais-republikaaliseen, persialaiseen, islamilaiseen tai ruotsalaiseen kalenteriin
- **Tee siitä oma** – anna sivustollesi oma nimi, teema värit ja etusivun teksti ja kuva

## Demo

Kirjautuaksesi demoon, käytä yhtä seuraavista käyttäjätunnus/salasana-parista. Kukin edustaa yhtä käyttäjäroolia Gramps Webissä.

`owner / owner` <br>
`editor / editor` <br>
`contributor / contributor` <br>
`member / member`

Demo nollataan kahden tunnin välein, joten tekemäsi muutokset ovat väliaikaisia.

[Mene demokirjautumiseen](https://demo.grampsweb.org/){ .md-button .md-button--primary target="_blank"}

### Kiitos

Demoa tukee ystävällisesti DigitalOcean.

<a href="https://www.digitalocean.com/?refcode=b1d13ebe86ac&utm_campaign=Referral_Invite&utm_medium=Referral_Program&utm_source=badge"><img src="https://web-platforms.sfo2.cdn.digitaloceanspaces.com/WWW/Badge%202.svg" alt="DigitalOcean Referral Badge" /></a>
