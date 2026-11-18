# Käyttäminen AI-avustajaa

**Avustaja**-näkymä Gramps Webissä (jos se on käytössä asennuksessasi) antaa pääsyn AI-avustajaan, joka vastaa kysymyksiin perhepuustasi.

!!! warning
    Kuten minkä tahansa AI-avustajan kanssa, vastaukset voivat olla vääriä. Käytä vastauksessa olevia linkkejä tarkistaaksesi, mihin tietueisiin ne perustuvat.

## Kuinka se toimii

Avustaja ei tunne puuta etukäteen. Vastatakseen kysymykseen suuri kielimalli etsii tarvitsemansa tietueet, aivan kuten sinä itse:

- se etsii puusta [kokotekstihaku](search.md),
- se suodattaa henkilöitä, tapahtumia ja perheitä kriteerien, kuten nimien, päivämäärien, paikkojen tai lasten määrän mukaan,
- se löytää esi-isiä, jälkeläisiä ja muita sukulaisia henkilöstä, heidän suhteensa mukaan,
- se lukee täydelliset tietueet henkilöistä, perheistä, tapahtumista, paikoista ja muistiinpanoista.

Se vastaa sitten löytämistään tietueista, linkkien kera. Kun se työskentelee, käytettävät työkalut näkyvät, joten voit seurata mukana. Kysymykset, jotka vievät enemmän aikaa, toimivat taustalla – voit navigoida muualle ja palata takaisin.

Avustaja vastaa vain puustasi, ei kielimallin yleisestä tiedosta – edes tunnetuista henkilöistä. Jos puu ei tallenna jotain, se ilmoittaa siitä, mainiten siihen liittyvää tietoa, jonka se on löytänyt, esimerkiksi muistiinpanossa. Se näkee vain sen, mitä sinulla on oikeus nähdä: linkit yksityisiin tietueisiin näkyvät tavallisena tekstinä käyttäjille, jotka eivät voi nähdä niitä.

Seurantakysymykset pitävät aikaisempien kysymysten kontekstin samassa keskustelussa, joten voit kysyä "Ja milloin hän kuoli?" kysyttyäsi henkilöstä.

## Mitä voit kysyä

- **Tietoja ihmisistä**: "Milloin Mary Smith syntyi?" tai "Mitkä ovat John Doen lasten nimet?"
- **Sukulaiset**: "Keitä Jane Smithin isovanhemmat ovat?" tai "Mitkä Johann Meyerin jälkeläiset muuttivat Amerikkaan?"
- **Haut kriteereillä**: "Kuka syntyi Lontoossa vuoden 1850 jälkeen?", "Listaa avioliitot vuosina 1920–1950", tai "Mitkä parit saivat viisi tai enemmän lasta?"
- **Paikat**: "Mitkä tapahtumat tapahtuivat Pariisissa?" tai "Kuka syntyi Tanskassa?" – suuremman paikan sisällä olevat paikat sisältyvät.
- **Muistiinpanot**: "Mitä muistiinpanot sanovat Meyer-perheen tilasta?"

Kysymykset, jotka tarvitsevat koko puun kerralla, kuten "Mikä on yleisin etunimi?", toimivat huonommin, koska avustaja näkee vain rajoitetun määrän tietueita jokaisella haulla.

## Kysyminen kuvista

Jos palvelimen ylläpitäjä on mahdollistanut sen, kehotteessa on painike kuvien liittämiseen. Voit myös liittää kuvan tai pudottaa kuvafailit kehotteeseen. Kysymykseen voidaan liittää jopa neljä kuvaa, esimerkiksi kirkon tietueen skannaus kysyessäsi "Kuka mainitaan tässä merkinnässä, ja ovatko he puussani?"

Kuvat lähetetään vain kysymyksen mukana, johon ne on liitetty. Seurantakysymykset voivat viitata siihen, mitä avustaja sanoi niistä, mutta eivät itse kuviin, joten liitä ne uudelleen tarvittaessa. Jos puullasi on rajoitus AI:n käytölle, jokainen kuva lasketaan kuin lisäkysymys.

## Antaa avustajan muuttaa puuta

Jos palvelimen ylläpitäjä on mahdollistanut sen, toimittajat, omistajat ja ylläpitäjät voivat pyytää avustajaa muuttamaan puuta, esimerkiksi "Lisää kaste 3. toukokuuta 1802 St. Maryssä Johann Meyerille" tai "Korjaa Anna Smithin syntymävuosi, sen pitäisi olla 1871".

Avustaja ei koskaan muuta mitään omatoimisesti. Se vastaa **Ehdotetut muutokset** -kortilla, joka listaa jokaisen tietueen, jonka se lisäisi, muokkaisi tai poistaisi, vanhat arvot yliviivattuina ja uudet arvot korostettuina. Mikään ei tapahdu ennen kuin napsautat **Hyväksy**. Muutokset tehdään sitten yhdellä kertaa, ja voit peruuttaa ne kuten minkä tahansa muun muokkauksen, viestistä, joka ilmestyy tai [muutoshistoriasta](revisions.md).

Tarkista ehdotus huolellisesti ennen sen hyväksymistä – erityisesti, että avustaja valitsi oikean henkilön, ja että se ei lisännyt uutta tietuetta (kuten paikkaa tai lähdettä), joka jo olemassa puussasi hieman eri nimellä. Jos ehdotus ei ole aivan oikea, kerro mitä muuttaa, ja avustaja ehdottaa uudelleen.

Kun ehdotus on hyväksytty, aikaisempia ehdotuksia samassa keskustelussa ei voi enää hyväksyä, koska ne tehtiin puulle sellaisena kuin se oli ennen. Sama tapahtuu, jos jokin vaikuttavista tietueista on muuttunut sillä välin.

## Vinkkejä kysymysten esittämiseen

- **Nimeä ihmiset.** Avustaja ei tiedä, kuka olet tai kuka kotihenkilösi on, joten sen sijaan, että kysyisit "isoäitini", kysy "Anna Smithin (s. 1950) isoäidistä". Voit myös käyttää Gramps ID:itä, esim. "I0042:n lapset".
- **Ole tarkka** kun nimet ovat yleisiä: "Milloin vuonna 1850 Bostonissa syntynyt John Smith meni naimisiin?" on parempi kuin "Milloin John Smith meni naimisiin?"
- **Käytä omaa kieltäsi.** Voit kysyä omalla kielelläsi ja saada vastauksia samalla kielellä.
- **Kysy uudelleen eri tavalla** jos vastaus näyttää puutteelliselta – esimerkiksi nimeämällä paikka tai aikakausi, joka sinua kiinnostaa.

!!! tip
    Jaa kokemuksesi asioista, jotka toimivat ja eivät toimi, yhteisön kanssa.
