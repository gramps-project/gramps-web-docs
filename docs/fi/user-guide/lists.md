# Luettelot

Jokaisella objektityypillä Gramps Webissä on luettelo: Ihmiset, Perheet, Tapahtumat, Paikat, Lähteet, Viittaukset, Arkistot, Muistiinpanot ja Media. Ne kaikki toimivat samalla tavalla ja jakavat samat työkalut lajitteluun, suodattamiseen ja muokkaamiseen massana.

## Lajittelu ja sivutus

Napsauta sarakeotsikkoa lajitellaksesi sen mukaan; napsauta sitä uudelleen kääntääksesi järjestyksen. Lajittelu suoritetaan palvelimella, joten se koskee koko luetteloa, ei vain sivua, jota tarkastelet.

Pitkät luettelot jaetaan sivuille. Käytä sivutustyökaluja alareunassa siirtyäksesi niiden välillä.

Kapeilla näytöillä taulukko vaihtuu automaattisesti kompaktimuotoon, joten luettelo näkymät pysyvät käytettävissä puhelimessa.

## Sarakkeiden valinta

Napsauta työkalupalkin oikeassa reunassa olevaa rataskuvaketta avataksesi **Sarakkeet**-valintaikkunan. Valitse tai poista valinta sarakkeelta näyttääkseen tai piilottaakseen sen. **Palauta** palauttaa oletusvalinnan kyseiselle luettelolle.

Ainakin yhden sarakkeen on oltava näkyvissä, joten viimeistä jäljellä olevaa saraketta ei voi poistaa valinnasta.

Oletussarjojen lisäksi jokainen luettelo tarjoaa **Tunnisteet**-sarakkeen ja, käyttäjille, jotka voivat nähdä yksityiset tiedot, **Yksityisyys**-sarakkeen, joka näyttää lukon jokaiselle yksityiselle objektille. Jos olet aiemmin muuttanut luettelon sarakevalintaa, uusia sarakkeita, kuten **Tunnisteet**, ei lisätä automaattisesti; valitse ne valintaikkunassa.

Sarakevalintasi muistetaan objektityypin ja sukupuusi mukaan. Se tallennetaan selaimeesi, joten se ei ole näkyvissä muille käyttäjille – mutta se ei myöskään seuraa sinua toiseen selaimeen tai laitteeseen.

## Suodatus

Napsauta **suodatin**-painiketta avataksesi suodatinpaneelin. Se tarjoaa kolme tapaa suodattaa, joita voidaan yhdistää:

- **Valmiit suodattimet** taitettavissa osioissa, jotka riippuvat objektityypistä. Esimerkiksi ihmisille voit suodattaa nimen, syntymävuoden, kuolinvuoden, erilaiset henkilön ominaisuudet, yhdistysten määrän, tunnisteet ja sen, onko objekti yksityinen vai julkinen. Perheitä voidaan suodattaa isän, äidin tai lapsen nimen mukaan, lähteitä kirjoittajan mukaan, ja paikkoja ja arkistoja niiden tyypin mukaan.
- **Edistynyt suodatin** – ehtorakentaja suodattimille, joita valmiit suodattimet eivät voi ilmaista, kuvattu [alla](#edistynyt-suodatin).
- **GOQL** – tekstikenttä lausekkeelle [Gramps Object Query Language](goql.md) -kielellä, syntaksin korostuksella. Kirjoita lauseke ja paina Enter tai napsauta **Käytä**. Jos lauseke on virheellinen, kenttä merkitään virheeksi. Lauseke soveltuu muiden suodattimien päälle.

Aktiiviset suodattimet näkyvät siruina rivinä työkalupalkin alapuolella. Poista yksittäinen suodatin napsauttamalla sirun tyhjennyspainiketta tai käytä **Tyhjennä kaikki suodattimet** poistaaksesi ne kaikki kerralla.

### Edistynyt suodatin

Napsauta **Edistynyt suodatin** suodatinpaneelin alareunassa avataksesi ehtorakentajan. Sen ehdot ovat suodatussäännöt, jotka tunnet Gramps Desktopista, kuten "Ihmiset, joilla on &lt;nimi&gt;" tai "Esivanhemmat &lt;henkilö&gt;".

- Napsauta **Lisää ehto** valitaksesi säännön. Säännöt on ryhmitelty kategorioihin ja niitä voidaan etsiä nimen tai kuvauksen mukaan.
- Täytä säännön parametrit. Jokaisella parametrilla on vastaava syöttökenttä, esimerkiksi päivämääräkenttä, tunnistevalitsin tai objektivalitsin henkilölle tai paikalle.
- Valitse, miten ryhmän ehdot yhdistetään: **Kaikki ehdot**, **Mikään ehto**, tai – valikosta niiden vieressä – **Täsmälleen yksi ehto**.
- Napsauta **Lisää ryhmä** lisätäksesi ehtoryhmän toisen ryhmän sisälle, omalla yhdistämistavallaan.
- Valitse **Ei** ehdolle tai ryhmälle kääntääksesi sen.

Napsauta **Käytä** suodattaaksesi luetteloa.

Valmiit suodattimet ja GOQL-lauseke, jotka ovat aktiivisia, kun avaat rakentajan, näkyvät siellä ehtona. GOQL-lauseke voidaan myös lisätä omaksi ehdokseen, esimerkiksi yhdistämään useita lausekkeita **Mikään ehto**. Jos rakentamasi suodatin voidaan ilmaista valmiilla suodattimilla, se näytetään niiden kanssa soveltamisen jälkeen. Muussa tapauksessa se näytetään yksittäisenä **Edistyneenä suodattimena** siruna, ja suodatinpaneeli tarjoaa **Muokkaa**-painikkeen rakentajan uudelleen avaamiseksi.

!!! huomautus
    Säännöt, jotka viittaavat mukautettuihin suodattimiin, jotka on tallennettu Gramps Desktopiin, eivät ole käytettävissä rakentajassa. Säännöt näytetään kielelläsi Gramps Web API 3.24 tai uudemmalla.

#### Tallennetut suodattimet

Uudelleenkäyttääksesi rakentamaasi suodatinta, napsauta **Tallenna** ehtorakentajassa ja anna sille nimi. Tallentaminen olemassa olevaan nimeen korvataan kyseinen suodatin. **Tallennetut suodattimet** rakentajassa listaa tallennetut suodattimet nykyiselle objektityypille; valitsemalla yhden lataa sen rakentajaan, jossa voit muuttaa sitä ennen napsauttamista **Käytä**.

Tallennetut suodattimet tallennetaan selaimeesi, perhepuun ja objektityypin mukaan, joten ne eivät ole muiden käyttäjien tai muiden laitteidesi käytettävissä.

Tallennettu suodatin voi lakata toimimasta, kun puu muuttuu, esimerkiksi jos se viittaa henkilöön, joka on sittemmin poistettu (objektivalitsin näyttää silloin "Ei löytynyt"). Tällöin suodatinta ei voi soveltaa tai tallentaa ennen kuin ehto on korjattu.

## Objektien valitseminen ja niiden käsittely massana

Käyttäjät, joilla on muokkausoikeudet, näkevät **Valitse**-painikkeen suodatinpainikkeen vieressä. Napsauta sitä siirtyäksesi valintatilaan, joka lisää valintaruudun jokaiseen riviin.

Valitse haluamasi objektit, ja työkalupalkki ilmestyy näyttäen, kuinka monta on valittu, yhdessä **Toiminto**-pudotusvalikon ja **Käytä**-painikkeen kanssa.

Valintaruutu taulukon otsikossa valitsee kaikki objektit nykyisellä sivulla. Jos enemmän objekteja vastaa nykyisiä suodattimia, työkalupalkki tarjoaa sitten **Valitse kaikki (N)**, joka valitsee kaikki N vastaavaa objektia kaikilta sivuilta. Riviin poistaminen valinnasta, sivun tai suodattimien muuttaminen tai valintatilasta poistuminen päättää tämän valinnan.

### Poista

Valitse yksi tai useampi objekti, valitse **Poista** ja napsauta **Käytä**. Vahvistusdialogi kysyy sinulta vahvistusta, varoittaen, että toimintoa ei voida peruuttaa.

Yli kymmenen objektin poistaminen tapahtuu taustatehtävänä. Sen edistymistä näytetään **Käytä**-painikkeen vieressä ja [Ilmoituksissa](notifications.md), ja luettelo latautuu uudelleen, kun se on valmis.

!!! vinkki
    Poistot tallennetaan [muutoshistoriaan](revisions.md) kuten mikä tahansa muu muutos, joten virheellinen massapoisto voidaan kumota peruuttamalla vastaava tapahtuma.

### Tunnisteet ja yksityisyys

Toiminnot **Lisää tunniste**, **Poista tunniste** ja **Yksityisyys** muuttavat kaikki valitut objektit kerralla (vaatii Gramps Web API 3.26 tai uudemman):

- **Lisää tunniste** lisää olemassa olevan tunnisteen tai uuden, jonka luot valintaikkunassa.
- **Poista tunniste** poistaa tunnisteen valituista objekteista, joilla se on.
- **Yksityisyys** merkitsee valitut objektit yksityisiksi tai julkisiksi. Tämä muuttaa vain itse objekteja, ei niiden osia tai niihin liittyviä tietoja – katso [Yksityiset tiedot](privacy.md).

Kuten poistamisessa, yli kymmenen objektin muokkaaminen tapahtuu taustatehtävänä. Muutokset tallennetaan [muutoshistoriaan](revisions.md) yhtenä tapahtumana, joten ne voidaan peruuttaa yhdessä.

### Yhdistä

Valitse **täsmälleen kaksi** objektia, valitse **Yhdistä** ja napsauta **Käytä**. Dialogi kysyy, mikä kahdesta pitäisi antaa ensisijaiset tiedot yhdistettävälle objektille; napsauta sitä, jonka haluat pitää ensisijaisena. Toisen objektin tiedot yhdistetään siihen ja viittaukset päivitetään.

Yhdistäminen on saatavilla ihmisille, perheille, tapahtumille, paikoille, lähteille ja viittauksille. Se ei ole saatavilla arkistoille, muistiinpanoille ja mediaobjekteille.

Media-näkymässä valinta toimii sekä gallerian että luettelomuodon osalta: valintatilassa napsauttamalla laatikkoa tai riviä kytketään se päälle tai pois. Mediaobjekteja ei voida yhdistää.

Jos valitset toiminnon ilman voimassa olevaa valintaa – esimerkiksi yhdistämisen vain yhdellä valitulla objektilla – dialogi selittää, mitä vaaditaan.
