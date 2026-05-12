# Käyttäjien hallinta

Käyttäjien hallintaliittymä on saatavilla **Asetukset > Hallitse käyttäjiä** (käyttäjäkuvake sovelluksen yläreunassa). Se on saatavilla vain käyttäjille, joilla on Omistaja- tai Ylläpitäjärooli.

## Käyttäjäroolit

Katso [Käyttäjäjärjestelmä](../install_setup/users.md) saadaksesi täydellisen kuvauksen käytettävissä olevista käyttäjärooleista ja niiden oikeuksista.

## Käyttäjien tarkastelu ja suodatus

Käyttäjien hallintasivulla näkyy taulukko kaikista rekisteröidyistä käyttäjätilistä seuraavilla sarakkeilla:

- **Käyttäjänimi** — kirjautumisnimi
- **Koko nimi** — näyttönimi
- **Sähköposti** — käyttäjän sähköpostiosoite
- **Rooli** — määritetty rooli (Vieras, Jäsen, Avustaja, Toimittaja, Omistaja tai Ylläpitäjä)
- **Tilin lähde** — joko "Salasana" (paikallinen tili) tai ulkoisen identiteettipalveluntarjoajan nimi (esim. OIDC:n käytön yhteydessä)

Käytä taulukon yläosassa olevaa hakukenttää ja roolivalikkoa suodattaaksesi luetteloa. Napsauta suodattimen tyhjennyspainiketta palauttaaksesi kaikki suodattimet.

## Käyttäjän muokkaaminen

Napsauta muokkaus (kynä) kuvaketta missä tahansa rivissä avataksesi muokkausdialogin. Voit muuttaa käyttäjän:

- Koko nimi
- Sähköpostiosoite
- Rooli

Tämä on ensisijainen tapa **ottaa käyttöön uusi itse rekisteröitynyt käyttäjä**: muuta heidän roolinsa *poistettu* -tilasta mihin tahansa aktiiviseen rooliin (esim. Jäsen tai Toimittaja).

## Käyttäjän lisääminen manuaalisesti

Napsauta **lisää käyttäjä** (henkilö-lisää) kuvaketta taulukon yläpuolella luodaksesi uuden käyttäjätilin suoraan ilman itse rekisteröitymistä. Täytä muokkausdialogiin käyttäjänimi, koko nimi, sähköpostiosoite, salasana ja rooli, ja napsauta **Tallenna**.

## Käyttäjän poistaminen

Napsauta poisto (roskakori) kuvaketta missä tahansa rivissä ja vahvista dialogissa. Tätä toimintoa ei voi peruuttaa.

## Käyttäjätilien vienti ja tuonti

Nämä painikkeet ovat hyödyllisiä [siirryttäessä toiseen Gramps Web -instanssiin](export.md).

- **Vie käyttäjätiedot** (latauskuvake) — lataa JSON-tiedosto, joka sisältää kaikki käyttäjätilit (ilman salasanoja, koska salasanat tallennetaan salattuna).
- **Tuo käyttäjätilit** (ryhmä-lisää kuvake) — lataa aikaisemmin viety JSON-tiedosto luodaksesi käyttäjätilit suurina erinä. Kaikkien tuotuja käyttäjiä on asetettava uusi salasana "Unohditko salasanan" -linkin kautta, koska salasanoja ei voida siirtää.

## Rekisteröintilinkki (monipuun asetukset vain)

Monipuun asetuksessa rekisteröintilinkki uusille käyttäjille näkyy käyttäjien hallintasivun yläosassa. Voit kopioida tämän linkin ja jakaa sen henkilöille, joita haluat kutsua rekisteröitymään tilille puussasi.

!!! note
    Yksittäisen puun asetuksessa kirjautumissivulla on yleinen "Rekisteröidy" -linkki; puukohtainen rekisteröintilinkki on tarpeen vain monipuun asennuksissa.

## AI-chat-oikeudet

Jos AI-chat on otettu käyttöön palvelimella, sivun yläosassa oleva pudotusvalikko antaa sinun hallita, mitkä käyttäjäroolit saavat käyttää chat-ominaisuutta:

- Kaikki (mukaan lukien vieraat)
- Jäsenet ja sitä korkeammat
- Avustajat ja sitä korkeammat
- Toimittajat ja sitä korkeammat
- Vain omistajat ja ylläpitäjät
- Kukaan (poista chat käytöstä kaikilta käyttäjiltä)
