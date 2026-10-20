# Luettelot

Jokaisella objektityypillä Gramps Webissä on luettelonäkymä: Ihmiset, Perheet, Tapahtumat, Paikat, Lähteet, Viittaukset, Arkistot, Muistiinpanot ja Media. Ne kaikki toimivat samalla tavalla ja jakavat samat työkalut lajitteluun, suodattamiseen ja massamuokkaukseen.

## Lajittelu ja sivutus

Napsauta sarakeotsikkoa lajitellaksesi sen mukaan; napsauta sitä uudelleen kääntääksesi järjestyksen. Lajittelu suoritetaan palvelimella, joten se koskee koko luetteloa, ei vain sivua, jota tarkastelet.

Pitkät luettelot jaetaan sivuille. Käytä sivutuskontrolleja alareunassa siirtyäksesi niiden välillä.

Kapeilla näytöillä taulukko vaihtuu automaattisesti kompaktimuotoon, joten luettelonäkymät pysyvät käytettävissä puhelimella.

## Sarakkeiden valitseminen

Napsauta rataskuvaketta luettelon yläpuolella avataksesi **Sarakkeet**-valintaikkunan. Valitse tai poista valinta sarakkeelta näyttääkseksi tai piilottaaksesi sen. **Palauta** palauttaa oletusvalinnan kyseiselle luettelolle.

Ainakin yhden sarakkeen on pysyttävä näkyvissä, joten viimeistä jäljellä olevaa saraketta ei voi poistaa valinnasta.

Sarakevalintasi muistetaan objektityypin ja sukupuusi mukaan. Se tallennetaan selaimeesi, joten se ei ole näkyvissä muille käyttäjille – mutta se ei myöskään seuraa sinua toiseen selaimeen tai laitteeseen.

## Suodattaminen

Napsauta **suodatin**-painiketta avataksesi suodatinpaneelin. Se tarjoaa kolme tapaa suodattaa, joita voidaan yhdistää:

- **Valmiit suodattimet** taitettavissa osioissa, jotka riippuvat objektityypistä. Esimerkiksi ihmisille voit suodattaa syntymävuoden, kuolinvuoden, erilaiset henkilön ominaisuudet, yhdistysten määrän, tunnisteet ja sen, onko objekti yksityinen vai julkinen.
- **Edistynyt suodatin** – ehtorakentaja suodattimille, joita valmiit suodattimet eivät voi ilmaista, kuvattu [alla](#edistynyt-suodatin).
- **GQL** – tekstikenttä kyselylle [Grampsin kyselykielessä](gql.md). Kirjoita kysely ja paina Enter tai napsauta **Käytä**. Jos kysely on virheellinen, kentän kehys muuttuu punaiseksi. Kysely vaikuttaa muiden suodattimien päälle.

Aktiiviset suodattimet näkyvät siruina luettelon yläpuolella. Poista yksittäinen suodatin napsauttamalla sirun tyhjennysnappia tai käytä **Tyhjennä kaikki suodattimet** poistaaksesi ne kaikki kerralla.

### Edistynyt suodatin

Napsauta **Edistynyt suodatin** suodatinpaneelin alareunassa avataksesi ehtorakentajan. Sen ehdot ovat suodatin säännöt, jotka tunnet Gramps Desktopista, kuten "Ihmiset, joilla on &lt;nimi&gt;" tai "Esivanhemmat &lt;henkilö&gt;".

- Napsauta **Lisää ehto** valitaksesi säännön. Säännöt on ryhmitelty kategorioihin ja niitä voidaan etsiä nimen tai kuvauksen mukaan.
- Täytä säännön parametrit. Jokaisella parametrilla on vastaava syöte, esimerkiksi päivämääräkenttä, tunnistevalitsin tai objektivalitsin henkilölle tai paikalle.
- Valitse, miten ryhmän ehdot yhdistetään: **Kaikki ehdot**, **Mikä tahansa ehto** tai – valikon kautta niiden vieressä – **Täsmälleen yksi ehto**.
- Napsauta **Lisää ryhmä** lisätäksesi ehtoryhmän toiseen ryhmään, jolla on oma tapansa yhdistää ne.
- Valitse **Ei** ehdolle tai ryhmälle kääntääksesi sen.

Napsauta **Käytä** suodattaaksesi luetteloa.

Valmiit suodattimet, jotka ovat aktiivisia kun avaat rakentajan, näkyvät siellä ehtona. Jos rakentamasi suodatin voidaan ilmaista valmiilla suodattimilla, se näytetään niiden kanssa käytön jälkeen. Muuten se näytetään yksittäisenä **Edistyneenä suodattimena** siruna, ja suodatinpaneeli tarjoaa **Muokkaa**-painikkeen uudelleen avatakseen rakentajan.

!!! huomio
    Säännöt, jotka viittaavat mukautettuihin suodattimiin, jotka on tallennettu Gramps Desktopiin, eivät ole saatavilla rakentajassa. Säännöt näytetään kielelläsi Gramps Web API 3.24 tai uudemmalla.

## Objektien valitseminen ja niiden käsittely massana

Muokkausoikeudet omaavat käyttäjät näkevät **Valitse**-painikkeen suodatinpainikkeen vieressä. Napsauta sitä siirtyäksesi valintatilaan, joka lisää valintaruudun jokaiseen riviin.

Valitse haluamasi objektit, ja työkalupalkki ilmestyy näyttäen, kuinka monta on valittu, yhdessä **Toiminto**-pudotusvalikon ja **Käytä**-painikkeen kanssa.

### Poista

Valitse yksi tai useampi objekti, valitse **Poista** ja napsauta **Käytä**. Vahvistusdialogi kysyy sinulta vahvistusta, varoittaen, että toimintoa ei voi peruuttaa.

!!! vinkki
    Poistot kirjataan [muutoshistoriaan](revisions.md) kuten mikä tahansa muu muutos, joten virheellinen massapoisto voidaan peruuttaa kumoamalla vastaava tapahtuma.

### Yhdistä

Valitse **täsmälleen kaksi** objektia, valitse **Yhdistä** ja napsauta **Käytä**. Dialogi kysyy, kumpi kahdesta tulisi antaa ensisijaiseksi tiedoksi yhdistetyssä objektissa; napsauta sitä, jonka haluat pitää ensisijaisena. Toisen objektin tiedot yhdistetään siihen ja viittaukset päivitetään.

Yhdistäminen on saatavilla ihmisille, perheille, tapahtumille, paikoille, lähteille ja viittauksille. Se ei ole saatavilla arkistoille, muistiinpanoille ja mediaobjekteille.

Jos valitset toiminnon ilman voimassa olevaa valintaa – esimerkiksi yhdistämisen vain yhdellä objektilla valittuna – dialogi selittää, mitä vaaditaan.
