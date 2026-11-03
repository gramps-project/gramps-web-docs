# Luettelot

Jokaisella objektityypillä Gramps Webissä on luettelonäkymä: Ihmiset, Perheet, Tapahtumat, Paikat, Lähteet, Viittaukset, Arkistot, Muistiinpanot ja Media. Ne kaikki toimivat samalla tavalla ja jakavat samat työkalut lajitteluun, suodattamiseen ja massamuokkaukseen.

## Lajittelu ja sivutus

Napsauta sarakeotsikkoa lajitellaksesi sen mukaan; napsauta sitä uudelleen kääntääksesi järjestyksen. Lajittelu suoritetaan palvelimella, joten se koskee koko luetteloa, ei vain sivua, jota tarkastelet.

Pitkät luettelot jaetaan sivuille. Käytä sivutuskontrolleja alareunassa siirtyäksesi niiden välillä.

Kapeilla näytöillä taulukko vaihtuu automaattisesti kompaktimuotoon, jotta luettelonäkymät pysyvät käytettävissä puhelimessa.

## Sarakkeiden valinta

Napsauta rataskuvaketta luettelon yläpuolella avataksesi **Sarakkeet**-valintaikkunan. Valitse tai poista valinta sarakkeelta, jotta se näkyy tai piilotetaan. **Nollaa** palauttaa oletusvalinnan kyseiselle luettelolle.

Ainakin yhden sarakkeen on oltava näkyvissä, joten viimeistä jäljellä olevaa saraketta ei voi poistaa valinnasta.

Sarakevalintasi muistetaan objektityypin ja sukupuun mukaan. Se tallennetaan selaimeesi, joten se ei ole näkyvissä muille käyttäjille – mutta se ei myöskään seuraa sinua toiseen selaimeen tai laitteeseen.

## Suodattaminen

Napsauta **suodatin**-painiketta avataksesi suodatinpaneelin. Se tarjoaa kolme tapaa suodattaa, joita voidaan yhdistää:

- **Valmiit suodattimet** taitettavissa osioissa, jotka riippuvat objektityypistä. Esimerkiksi ihmisille voit suodattaa syntymävuoden, kuolinvuoden, erilaiset henkilön ominaisuudet, yhdistysten määrän, tunnisteet ja sen, onko objekti yksityinen vai julkinen.
- **Edistynyt suodatin** – ehtorakentaja suodattimille, joita valmiit suodattimet eivät voi ilmaista, kuvattu [alla](#edistynyt-suodatin).
- **GQL** – tekstikenttä kyselylle [Gramps-kyselykielellä](gql.md). Kirjoita kysely ja paina Enter tai napsauta **Käytä**. Jos kysely on virheellinen, kentän kehys muuttuu punaiseksi. Kysely vaikuttaa muiden suodattimien päälle.

Aktiiviset suodattimet näkyvät siruina luettelon yläpuolella. Poista yksi suodatin napsauttamalla sirun tyhjennyspainiketta tai käytä **Tyhjennä kaikki suodattimet** poistaaksesi ne kaikki kerralla.

### Edistynyt suodatin

Napsauta **Edistynyt suodatin** suodatinpaneelin alareunassa avataksesi ehtorakentajan. Sen ehdot ovat suodatin säännöt, jotka tunnet Gramps Desktopista, kuten "Ihmiset, joilla on &lt;nimi&gt;" tai "Esivanhemmat &lt;henkilö&gt;".

- Napsauta **Lisää ehto** valitaksesi säännön. Säännöt on ryhmitelty kategorioihin ja niitä voidaan etsiä nimen tai kuvauksen mukaan.
- Täytä säännön parametrit. Jokaisella parametrilla on vastaava syötekenttä, esimerkiksi päivämääräkenttä, tunnistevalitsin tai objektivalitsin henkilölle tai paikalle.
- Valitse, kuinka ryhmän ehdot yhdistetään: **Kaikki ehdot**, **Mikään ehto**, tai – valikosta niiden vieressä – **Täsmälleen yksi ehto**.
- Napsauta **Lisää ryhmä** lisätäksesi ehtoryhmän toisen ryhmän sisään, omalla tavallaan yhdistää niitä.
- Valitse **Ei** ehdolle tai ryhmälle kääntääksesi sen.

Napsauta **Käytä** suodattaaksesi luetteloa.

Valmiit suodattimet, jotka ovat aktiivisia, kun avaat rakentajan, näkyvät siellä ehdoina. Jos rakentamasi suodatin voidaan ilmaista valmiilla suodattimilla, se näytetään niiden kanssa käytön jälkeen. Muuten se näytetään yksittäisenä **Edistyneenä suodattimena** siruna, ja suodatinpaneeli tarjoaa **Muokkaa**-painikkeen uudelleen avatakseen rakentajan.

!!! huomautus
    Säännöt, jotka viittaavat mukautettuihin suodattimiin, jotka on tallennettu Gramps Desktopiin, eivät ole saatavilla rakentajassa. Säännöt näytetään kielelläsi Gramps Web API 3.24 tai uudemmassa.

## Objektien valitseminen ja niiden käsittely massana

Käyttäjät, joilla on muokkausoikeudet, näkevät **Valitse**-painikkeen suodatinpainikkeen vieressä. Napsauta sitä siirtyäksesi valintatilaan, joka lisää valintaruudun jokaiseen riviin.

Valitse haluamasi objektit, ja työkalupalkki ilmestyy näyttämään, kuinka monta on valittu, yhdessä **Toiminto**-pudotusvalikon ja **Käytä**-painikkeen kanssa.

Taulukon otsikkoruutu valitsee kaikki objektit nykyisellä sivulla. Jos enemmän objekteja vastaa nykyisiä suodattimia, työkalupalkki tarjoaa sitten **Valitse kaikki (N)**, joka valitsee kaikki N vastaavaa objektia kaikilta sivuilta. Riviä poistettaessa, sivua tai suodattimia vaihdettaessa tai valintatilasta poistuttaessa tämä valinta päättyy.

### Poista

Valitse yksi tai useampi objekti, valitse **Poista** ja napsauta **Käytä**. Vahvistusdialogi pyytää sinua vahvistamaan, varoittaen, että toimenpidettä ei voi peruuttaa.

Yli kymmenen objektin poistaminen suoritetaan taustatehtävänä. Sen edistymistä näytetään **Käytä**-painikkeen vieressä ja [Ilmoituksissa](notifications.md), ja luettelo ladataan uudelleen, kun se on valmis.

!!! vinkki
    Poistot kirjataan [muutoshistoriaan](revisions.md) kuten mikä tahansa muu muutos, joten virheellinen massapoisto voidaan peruuttaa kumoamalla vastaava tapahtuma.

### Yhdistä

Valitse **täsmälleen kaksi** objektia, valitse **Yhdistä** ja napsauta **Käytä**. Dialogi kysyy, mikä kahdesta pitäisi antaa pääasialliset tiedot yhdistettävälle objektille; napsauta sitä, jonka haluat pitää pääasiallisena. Toisen objektin tiedot yhdistetään siihen ja viittaukset päivitetään.

Yhdistäminen on saatavilla ihmisille, perheille, tapahtumille, paikoille, lähteille ja viittauksille. Se ei ole saatavilla arkistoille, muistiinpanoille ja mediaobjekteille.

Media-näkymässä valinta toimii sekä gallerian että luettelonäkymän osalta: valintatilassa napsauttaminen laattaa tai riviä vaihtaa sen tilaa. **Poista** on ainoa toiminto, joka on saatavilla medialle.

Jos valitset toiminnon ilman voimassa olevaa valintaa – esimerkiksi yhdistämisen vain yhdellä valitulla objektilla – dialogi selittää, mitä vaaditaan.
