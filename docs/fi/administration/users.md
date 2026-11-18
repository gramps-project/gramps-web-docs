# Käyttäjien hallinta

Käyttäjien hallintaliittymä on saatavilla **Asetukset > Hallitse käyttäjiä** (käyttäjäkuvake ylävalikkopalkissa). Se on vain käyttäjien käytettävissä, joilla on Omistaja- tai Ylläpitäjärooli.

## Käyttäjäroolit

Katso [Käyttäjäjärjestelmä](../install_setup/users.md) saadaksesi täydellisen kuvauksen saatavilla olevista käyttäjärooleista ja niiden oikeuksista. Pääero vieraiden ja jäsenten välillä on se, että vieraat eivät näe [yksityisiä tietoja](../user-guide/privacy.md), joten valitse rooli yhdessä sen kanssa, mitä merkitset yksityiseksi.

## Näytä ja suodata käyttäjiä

Käyttäjien hallintapaneeli näyttää taulukon kaikista rekisteröidyistä käyttäjätilistä seuraavilla sarakkeilla:

- **Käyttäjänimi** – kirjautumisnimi
- **Koko nimi** – näyttönimi
- **Sähköposti** – käyttäjän sähköpostiosoite
- **Rooli** – määritetty rooli (Vieraat, Jäsen, Avustaja, Toimittaja, Omistaja tai Ylläpitäjä)
- **Tilin lähde** – joko "Salasana" (paikallinen tili) tai ulkoisen identiteettipalveluntarjoajan nimi (esim. OIDC:n käytön yhteydessä)

Käytä taulukon yläosassa olevaa hakukenttää ja roolivalikkoa suodattaaksesi luetteloa. Napsauta suodattimen tyhjennyspainiketta nollataksesi kaikki suodattimet.

## Muokkaa käyttäjää

Napsauta muokkaus (kynä) kuvaketta missä tahansa rivissä avataksesi muokkausdialogin. Voit muuttaa käyttäjän:

- Koko nimi
- Sähköpostiosoite
- Rooli

Tämä on ensisijainen tapa **mahdollistaa uuden itse rekisteröityneen käyttäjän**: muuta heidän roolinsa *poistetusta* mihin tahansa aktiiviseen rooliin (esim. Jäsen tai Toimittaja).

Sähköpostiosoitteiden ei tarvitse olla ainutlaatuisia (Gramps Web API 3.22:sta lähtien), joten useat tilit voivat jakaa saman osoitteen.

Käyttäjän poistaminen tai salasanan muuttaminen päättää kaikki heidän istuntonsa 15 minuutin sisällä.

!!! note
    Omistajat eivät voi muokata, muuttaa salasanan tai poistaa käyttäjiä, joilla on korkeampi rooli, kuten sivuston ylläpitäjä. Samalla roolilla olevat käyttäjät, kuten kaksi puun omistajaa, voivat hallita toisiaan.

## Lisää käyttäjä manuaalisesti

Napsauta **lisää käyttäjä** (henkilö-lisää) kuvaketta taulukon yläpuolella luodaksesi uuden käyttäjätilin suoraan ilman itse rekisteröitymistä. Täytä käyttäjänimi, koko nimi, sähköpostiosoite, salasana ja rooli dialogiin ja napsauta **Tallenna**.

## Poista käyttäjä

Napsauta poisto (roskakori) kuvaketta missä tahansa rivissä ja vahvista dialogi. Tätä toimintoa ei voi peruuttaa.

!!! note
    Jotta puu ei jäisi ilman ketään, joka voi hallita sitä, et voi alentaa omaa rooliasi alle Omistajan tai poistaa omaa tiliäsi, jos olet puun ainoa Omistaja tai Ylläpitäjä. Edistä toista käyttäjää ensin Omistajaksi. Ylläpitäjä voi silti muuttaa tai poistaa toisen käyttäjän puun viimeisen omistajan, koska he voivat nimittää uuden.

## Vie ja tuo käyttäjätilit

Nämä painikkeet ovat hyödyllisiä, kun [siirretään toiseen Gramps Web -instanssiin](export.md).

- **Vie käyttäjätiedot** (latauskuvake) – lataa JSON-tiedosto, joka sisältää kaikki käyttäjätilit (ilman salasanoja, koska salasanat tallennetaan salattuna).
- **Tuo käyttäjätilit** (ryhmä-lisää kuvake) – lataa aiemmin viety JSON-tiedosto luodaksesi käyttäjätilit suurina erinä. Kaikkien tuotuja käyttäjiä on asetettava uusi salasana "Unohditko salasanan" linkin kautta, koska salasanoja ei voida siirtää.

## Rekisteröintilinkki (monipuun asetukset vain)

Monipuun asetuksissa rekisteröintilinkki uusille käyttäjille näkyy käyttäjien hallintapaneelin yläosassa. Voit kopioida tämän linkin ja jakaa sen ihmisten kanssa, joita haluat kutsua rekisteröimään tilin puussasi.

!!! note
    Yksittäisen puun asetuksissa on yleinen "Rekisteröidy" linkki kirjautumissivulla; puukohtainen rekisteröintilinkki on tarpeen vain monipuun asennuksissa.

## AI-chat-oikeudet

Jos AI-chat on otettu käyttöön palvelimella, sivun yläosassa oleva pudotusvalikko antaa sinun hallita, mitkä käyttäjäroolit saavat käyttää chat-ominaisuutta:

- Kaikki (mukaan lukien vieraat)
- Jäsenet ja korkeammat
- Avustajat ja korkeammat
- Toimittajat ja korkeammat
- Vain omistajat ja ylläpitäjät
- Kukaan (poista chat käytöstä kaikilta käyttäjiltä)
