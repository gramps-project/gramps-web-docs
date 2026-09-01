# Luettelot

Jokaisella objektityypillä Gramps Webissä on luettelonäkymä: Ihmiset, Perheet, Tapahtumat, Paikat, Lähteet, Viittaukset, Arkistot, Muistiinpanot ja Media. Ne kaikki toimivat samalla tavalla ja jakavat samat työkalut lajitteluun, suodattamiseen ja massamuokkaukseen.

## Lajittelu ja sivutus

Napsauta sarakeotsikkoa lajitellaksesi sen mukaan; napsauta sitä uudelleen kääntääksesi järjestyksen. Lajittelu suoritetaan palvelimella, joten se koskee koko luetteloa, ei vain sitä sivua, jota tarkastelet.

Pitkät luettelot jaetaan sivuille. Käytä sivutustyökaluja alareunassa siirtyäksesi niiden välillä.

Kapeilla näytöillä taulukko vaihtuu automaattisesti kompaktimuotoon, joten luettelonäkymät pysyvät käyttökelpoisina puhelimessa.

## Sarakkeiden valinta

Napsauta rataskuvaketta luettelon yläpuolella avataksesi **Sarakkeet**-valintaikkunan. Valitse tai poista valinta sarakkeelta näyttääkseksi tai piilottaaksesi sen. **Palauta** palauttaa oletusvalinnan kyseiselle luettelolle.

Ainakin yhden sarakkeen on pysyttävä näkyvissä, joten viimeistä jäljellä olevaa saraketta ei voi poistaa valinnasta.

Sarakkeiden valintasi muistetaan objektityypin ja sukupuusi mukaan. Se tallennetaan selaimeesi, joten se ei ole näkyvissä muille käyttäjille – mutta se ei myöskään seuraa sinua toiseen selaimeen tai laitteeseen.

## Suodattaminen

Napsauta **suodatin**-painiketta avataksesi suodatinpaneelin. Paneelin yläosassa oleva pilleri-kytkin vaihtaa kahden tilan välillä:

- **yksinkertainen** – joukko valmiita suodattimia, jotka riippuvat objektityypistä. Esimerkiksi ihmisille voit suodattaa syntymävuoden, kuolinvuoden, erilaiset henkilön ominaisuudet, yhdistysten määrän, tunnisteet ja sen, onko objekti yksityinen vai julkinen.
- **GQL** – yksi tekstikenttä edistyneelle kyselylle [Gramps Query Language](gql.md). Kirjoita kysely ja paina Enter tai napsauta **Käytä**. Jos kysely on virheellinen, kentän kehys muuttuu punaiseksi.

Aktiiviset suodattimet näkyvät siruina luettelon yläpuolella. Poista yksittäinen suodatin napsauttamalla sirun tyhjennysnappia tai käytä **Tyhjennä kaikki suodattimet** poistaaksesi ne kaikki kerralla.

!!! note
    Nämä kaksi tilaa ovat vaihtoehtoja, eivät lisäyksiä: GQL-kysely korvataan yksinkertaisilla suodattimilla, ja takaisin yksinkertaiseen tilaan siirtyminen poistaa kyselyn.

## Objektien valitseminen ja niiden massatoiminnot

Muokkausoikeudet omaavat käyttäjät näkevät **Valitse**-painikkeen suodatinpainikkeen vieressä. Napsauta sitä siirtyäksesi valintatilaan, joka lisää valintaruudun jokaiseen riviin.

Valitse haluamasi objektit, ja työkalupalkki ilmestyy näyttäen, kuinka monta on valittu, yhdessä **Toiminto**-pudotusvalikon ja **Käytä**-painikkeen kanssa.

### Poista

Valitse yksi tai useampi objekti, valitse **Poista** ja napsauta **Käytä**. Vahvistusdialogi kysyy sinulta vahvistusta ja varoittaa, että toimintoa ei voi peruuttaa.

!!! tip
    Poistot kirjataan [muutoshistoriaan](revisions.md) kuten mikä tahansa muu muutos, joten virheellinen massapoisto voidaan kumota peruuttamalla vastaava tapahtuma.

### Yhdistä

Valitse **täsmälleen kaksi** objektia, valitse **Yhdistä** ja napsauta **Käytä**. Dialogi kysyy, kumpi kahdesta tulisi antaa pääasialliseksi tiedoksi yhdistetyssä objektissa; napsauta sitä, jonka haluat pitää pääasiallisena. Toisen objektin tiedot yhdistetään siihen ja viittaukset päivitetään.

Yhdistäminen on saatavilla ihmisille, perheille, tapahtumille, paikoille, lähteille ja viittauksille. Se ei ole saatavilla arkistoille, muistiinpanoille ja mediaobjekteille.

Jos valitset toiminnon ilman voimassa olevaa valintaa – esimerkiksi yhdistämisen vain yhdellä objektilla valittuna – dialogi selittää, mitä vaaditaan.
