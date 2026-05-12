# Hallitse käyttäjiä

Käyttäjien hallintaliittymä on saatavilla **Asetukset > Hallitse käyttäjiä** (käyttäjäkuvake sovelluksen yläreunassa). Se on saatavilla vain käyttäjille, joilla on Omistaja- tai Ylläpitäjärooli.

## Käyttäjäroolit

Katso [Käyttäjäjärjestelmä](../install_setup/users.md) saadaksesi täydellisen kuvauksen saatavilla olevista käyttäjärooleista ja niiden oikeuksista.

## Näytä ja suodata käyttäjiä

Käyttäjien hallintasivulla näkyy taulukko kaikista rekisteröidyistä käyttäjätilistä seuraavilla sarakkeilla:

- **Käyttäjänimi** – kirjautumisnimi
- **Koko nimi** – näyttönimi
- **Sähköposti** – käyttäjän sähköpostiosoite
- **Rooli** – määritetty rooli (Vieras, Jäsen, Avustaja, Toimittaja, Omistaja tai Ylläpitäjä)
- **Tilin lähde** – joko "Salasana" (paikallinen tili) tai ulkoisen identiteettipalveluntarjoajan nimi (esim. OIDC:tä käytettäessä)

Käytä taulukon yläosassa olevaa hakukenttää ja roolivalikkoa suodattaaksesi luetteloa. Napsauta suodattimen tyhjennyspainiketta palauttaaksesi kaikki suodattimet.

## Muokkaa käyttäjää

Napsauta muokkaus (kynä) kuvaketta missä tahansa rivissä avataksesi muokkausdialogin. Voit muuttaa käyttäjän:

- Koko nimeä
- Sähköpostiosoitetta
- Roolia

Tämä on ensisijainen tapa **ottaa käyttöön uusi itse rekisteröitynyt käyttäjä**: muuta heidän roolinsa *pois käytöstä* mihin tahansa aktiiviseen rooliin (esim. Jäsen tai Toimittaja).

## Lisää käyttäjä manuaalisesti

Napsauta **lisää käyttäjä** (henkilö-lisää) kuvaketta taulukon yläpuolella luodaksesi uuden käyttäjätilin suoraan ilman itse rekisteröitymistä. Täytä dialogiin käyttäjänimi, koko nimi, sähköpostiosoite, salasana ja rooli, ja napsauta **Tallenna**.

## Poista käyttäjä

Napsauta poisto (roskakori) kuvaketta missä tahansa rivissä ja vahvista dialogi. Tätä toimintoa ei voi peruuttaa.

## Vie ja tuo käyttäjätilit

Nämä painikkeet ovat hyödyllisiä [siirryttäessä toiseen Gramps Web -instanssiin](export.md).

- **Vie käyttäjätiedot** (lataa kuvake) – lataa JSON-tiedosto, joka sisältää kaikki käyttäjätilit (ilman salasanoja, koska salasanat tallennetaan salattuna).
- **Tuo käyttäjätilit** (ryhmä-lisää kuvake) – lataa aiemmin viety JSON-tiedosto luodaksesi käyttäjätilit suurina erinä. Kaikkien tuotuja käyttäjiä on asetettava uusi salasana "Unohditko salasanan" -linkin kautta, koska salasanoja ei voi siirtää.

## Rekisteröintilinkki (monipuu-asennus vain)

Monipuu-asennuksessa rekisteröintilinkki uusille käyttäjille näkyy käyttäjien hallintasivun yläosassa. Voit kopioida tämän linkin ja jakaa sen henkilöille, joita haluat kutsua rekisteröitymään tilille puussasi.

!!! huomautus
    Yksipuuhun asennuksessa on yleinen "Rekisteröidy" -linkki kirjautumissivulla; puukohtainen rekisteröintilinkki on tarpeen vain monipuu-asennuksissa.

## AI-chat-oikeudet

Jos AI-chat on otettu käyttöön palvelimella, sivun yläosassa oleva pudotusvalikko antaa sinun hallita, mitkä käyttäjäroolit saavat käyttää chat-ominaisuutta:

- Kaikki (mukaan lukien vieraat)
- Jäsenet ja sitä korkeammat
- Avustajat ja sitä korkeammat
- Toimittajat ja sitä korkeammat
- Vain omistajat ja ylläpitäjät
- Kukaan (poista chat käytöstä kaikilta käyttäjiltä)
