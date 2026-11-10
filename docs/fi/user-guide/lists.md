# Luettelot

Jokaisella objektityypillä Gramps Webissä on luettelonäkymä: Ihmiset, Perheet, Tapahtumat, Paikat, Lähteet, Viittaukset, Arkistot, Muistiinpanot ja Media. Ne toimivat kaikki samalla tavalla ja jakavat samat työkalut lajitteluun, suodattamiseen ja massamuokkaukseen.

## Lajittelu ja sivutus

Napsauta sarakeotsikkoa lajitellaksesi sen mukaan; napsauta sitä uudelleen kääntääksesi järjestyksen. Lajittelu suoritetaan palvelimella, joten se koskee koko luetteloa, ei vain sivua, jota katsot.

Pitkät luettelot jaetaan sivuille. Käytä sivutuskontrolleja alareunassa siirtyäksesi niiden välillä.

Kapeilla näytöillä taulukko vaihtuu automaattisesti kompaktimuotoon, joten luettelonäkymät pysyvät käytettävissä puhelimessa.

## Sarakkeiden valinta

Napsauta työkalupalkin oikeassa päässä olevaa rataskuvaketta avataksesi **Sarakkeet**-valintaikkunan. Valitse tai poista valinta sarakkeelta näyttääksesi tai piilottaaksesi sen. **Palauta** palauttaa oletusvalinnan kyseiselle luettelolle.

Ainakin yhden sarakkeen on pysyttävä näkyvissä, joten viimeistä jäljellä olevaa saraketta ei voi poistaa valinnasta.

Sarakkeiden valintasi muistetaan objektityypin ja sukupuun mukaan. Se tallennetaan selaimeesi, joten se ei ole näkyvissä muille käyttäjille – mutta se ei myöskään seuraa sinua toiseen selaimeen tai laitteeseen.

## Suodatus

Napsauta **suodatin**-painiketta avataksesi suodatinpaneelin. Se tarjoaa kolme tapaa suodattaa, joita voidaan yhdistää:

- **Valmiit suodattimet** taitettavissa osioissa, jotka riippuvat objektityypistä. Esimerkiksi ihmisille voit suodattaa nimen, syntymävuoden, kuolinvuoden, eri henkilön ominaisuudet, yhdistysten määrän, tunnisteet ja sen, onko objekti yksityinen vai julkinen. Perheitä voidaan suodattaa isän, äidin tai lapsen nimen mukaan, lähteitä kirjoittajan mukaan, ja paikkoja ja arkistoja niiden tyypin mukaan.
- **Edistynyt suodatin** – ehtojen rakentaja suodattimille, joita valmiit suodattimet eivät voi ilmaista, kuvattu [alla](#edistynyt-suodatin).
- **GOQL** – tekstikenttä lausekkeelle [Gramps Object Query Language](goql.md), syntaksin korostuksella. Kirjoita lauseke ja paina Enter tai napsauta **Käytä**. Jos lauseke on virheellinen, kenttä merkitään virheeksi. Lauseke vaikuttaa muiden suodattimien päällä.

Aktiiviset suodattimet näkyvät siruina rivinä työkalupalkin alapuolella. Poista yksittäinen suodatin napsauttamalla sirun tyhjennyspainiketta tai käytä **Tyhjennä kaikki suodattimet** poistaaksesi ne kaikki kerralla.

### Edistynyt suodatin

Napsauta **Edistynyt suodatin** suodatinpaneelin alareunassa avataksesi ehtojen rakentajan. Sen ehdot ovat suodatussääntöjä, jotka tunnetaan Gramps Desktopista, kuten "Ihmiset, joilla on &lt;nimi&gt;" tai "Esivanhemmat &lt;henkilö&gt;".

- Napsauta **Lisää ehto** valitaksesi säännön. Säännöt on ryhmitelty kategorioihin ja niitä voidaan etsiä nimen tai kuvauksen mukaan.
- Täytä säännön parametrit. Jokaisella parametrilla on vastaava syöte, esimerkiksi päivämääräkenttä, tunnistevalitsin tai objektivalitsin henkilölle tai paikalle.
- Valitse, kuinka ryhmän ehdot yhdistetään: **Kaikki ehdot**, **Mikään ehto**, tai – valikosta niiden vieressä – **Täsmälleen yksi ehto**.
- Napsauta **Lisää ryhmä** lisätäksesi ehtoryhmän toisen ryhmän sisälle, omalla yhdistämistavallaan.
- Valitse **Ei** ehdolle tai ryhmälle kääntääksesi sen.

Napsauta **Käytä** suodattaaksesi luetteloa.

Valmiit suodattimet ja GOQL-lauseke, jotka ovat aktiivisia, kun avaat rakentajan, näkyvät siellä ehtona. GOQL-lauseke voidaan myös lisätä omaksi ehdokseen, esimerkiksi yhdistämään useita lausekkeita **Mikään ehto**. Jos rakentamasi suodatin voidaan ilmaista valmiilla suodattimilla, se näytetään niiden kanssa soveltamisen jälkeen. Muussa tapauksessa se näkyy yksittäisenä **Edistyneenä suodattimena** siruna, ja suodatinpaneeli tarjoaa **Muokkaa**-painikkeen uudelleen avatakseen rakentajan.

!!! note
    Säännöt, jotka viittaavat mukautettuihin suodattimiin, jotka on tallennettu Gramps Desktopiin, eivät ole saatavilla rakentajassa. Säännöt näytetään omalla kielelläsi Gramps Web API 3.24 tai uudemmalla versiolla.

## Objektien valitseminen ja niihin kohdistaminen massana

Muokkausoikeudet omaavat käyttäjät näkevät **Valitse**-painikkeen suodatinpainikkeen vieressä. Napsauta sitä siirtyäksesi valintatilaan, joka lisää valintaruudun jokaiseen riviin.

Valitse haluamasi objektit, ja työkalupalkki ilmestyy näyttäen, kuinka monta on valittu, yhdessä **Toiminto**-pudotusvalikon ja **Käytä**-painikkeen kanssa.

Taulukon otsikkoruutu valitsee kaikki objektit nykyisellä sivulla. Jos enemmän objekteja vastaa nykyisiä suodattimia, työkalupalkki tarjoaa sitten **Valitse kaikki (N)**, joka valitsee kaikki N vastaavaa objektia kaikilta sivuilta. Rivin poistaminen valinnasta, sivun tai suodattimien vaihtaminen tai valintatilasta poistuminen päättää tämän valinnan.

### Poista

Valitse yksi tai useampi objekti, valitse **Poista**, ja napsauta **Käytä**. Vahvistusdialogi kysyy sinulta vahvistusta, varoittaen, että toimintoa ei voida peruuttaa.

Yli kymmenen objektin poistaminen suoritetaan taustatehtävänä. Sen edistyminen näkyy **Käytä**-painikkeen vieressä ja [Ilmoituksissa](notifications.md), ja luettelo latautuu uudelleen, kun se on valmis.

!!! tip
    Poistot tallennetaan [muutoshistoriaan](revisions.md) kuten mikä tahansa muu muutos, joten virheellinen massapoisto voidaan peruuttaa kumoamalla vastaava tapahtuma.

### Yhdistä

Valitse **täsmälleen kaksi** objektia, valitse **Yhdistä**, ja napsauta **Käytä**. Dialogi kysyy, mikä kahdesta pitäisi antaa ensisijaiset tiedot yhdistetyille objekteille; napsauta sitä, jonka haluat pitää ensisijaisena. Toisen objektin tiedot yhdistetään siihen ja viittaukset päivitetään.

Yhdistäminen on saatavilla ihmisille, perheille, tapahtumille, paikoille, lähteille ja viittauksille. Se ei ole saatavilla arkistoille, muistiinpanoille ja mediaobjekteille.

Media-näkymässä valinta toimii sekä gallerian että luettelonäkymän osalta: valintatilassa napsauttamalla laatikkoa tai riviä kytketään se päälle tai pois. **Poista** on ainoa toiminto, joka on saatavilla medialle.

Jos valitset toiminnon ilman voimassa olevaa valintaa – esimerkiksi yhdistämisen vain yhdellä objektilla valittuna – dialogi selittää, mitä vaaditaan.
