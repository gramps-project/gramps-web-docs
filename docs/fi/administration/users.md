# Hallinnoi käyttäjiä

Käyttäjien hallintaliittymä on saatavilla **Asetukset > Hallinnoi käyttäjiä** (käyttäjäkuvake yläosassa sovelluspalkissa). Se on vain käyttäjien saatavilla, joilla on Omistaja- tai Ylläpitäjärooli.

## Käyttäjäroolit

Katso [Käyttäjäjärjestelmä](../install_setup/users.md) saadaksesi täydellisen kuvauksen saatavilla olevista käyttäjärooleista ja niiden oikeuksista.

## Näytä ja suodata käyttäjiä

Käyttäjien hallintasivulla näkyy taulukko kaikista rekisteröidyistä käyttäjätilistä seuraavilla sarakkeilla:

- **Käyttäjänimi** – kirjautumisnimi
- **Koko nimi** – näyttönimi
- **Sähköposti** – käyttäjän sähköpostiosoite
- **Rooli** – määritetty rooli (Vieras, Jäsen, Avustaja, Toimittaja, Omistaja tai Ylläpitäjä)
- **Tilin lähde** – joko "Salasana" (paikallinen tili) tai ulkoisen identiteettipalveluntarjoajan nimi (esim. OIDC:n käytön yhteydessä)

Käytä taulukon yläosassa olevaa hakukenttää ja roolivalikkoa suodattaaksesi luetteloa. Napsauta suodattimen tyhjennyspainiketta palauttaaksesi kaikki suodattimet.

## Muokkaa käyttäjää

Napsauta muokkaus (kynä) kuvaketta missä tahansa rivissä avataksesi muokkausdialogin. Voit muuttaa käyttäjän:

- Koko nimi
- Sähköpostiosoite
- Rooli

Tämä on ensisijainen tapa **ottaa käyttöön uusi itse rekisteröitynyt käyttäjä**: muuta heidän roolinsa *pois käytöstä* mihin tahansa aktiiviseen rooliin (esim. Jäsen tai Toimittaja).

Sähköpostiosoitteiden ei tarvitse olla ainutlaatuisia (koska Gramps Web API 3.22), joten useat tilit voivat jakaa saman osoitteen.

Käyttäjän poistaminen käytöstä tai salasanan muuttaminen päättää kaikki heidän istuntonsa 15 minuutissa.

!!! huomautus
    Omistajat eivät voi muokata, muuttaa salasanan tai poistaa käyttäjiä, joilla on korkeampi rooli, kuten sivuston ylläpitäjä. Samalla roolilla olevat käyttäjät, kuten kaksi puun omistajaa, voivat hallita toisiaan.

## Lisää käyttäjä manuaalisesti

Napsauta **lisää käyttäjä** (henkilö-lisää) kuvaketta taulukon yläpuolella luodaksesi uuden käyttäjätilin suoraan ilman itse rekisteröitymistä. Täytä muokkausdialogissa käyttäjänimi, koko nimi, sähköpostiosoite, salasana ja rooli ja napsauta **Tallenna**.

## Poista käyttäjä

Napsauta poisto (roskakori) kuvaketta missä tahansa rivissä ja vahvista dialogissa. Tätä toimintoa ei voi peruuttaa.

!!! huomautus
    Estääksesi puun jäämisen ilman ketään, joka voi hallita sitä, et voi laskea omaa rooliasi alle Omistajan tai poistaa omaa tiliäsi, jos olet puun ainoa Omistaja tai Ylläpitäjä. Nosta ensin toinen käyttäjä Omistajaksi. Ylläpitäjä voi silti muuttaa tai poistaa toisen käyttäjän puun viimeisen omistajan, koska he voivat nimittää uuden.

## Vie ja tuo käyttäjätilit

Nämä painikkeet ovat hyödyllisiä [siirryttäessä toiseen Gramps Web -instanssiin](export.md).

- **Vie käyttäjätiedot** (lataa kuvake) – lataa JSON-tiedosto, joka sisältää kaikki käyttäjätilit (ilman salasanoja, koska salasanat tallennetaan salattuna).
- **Tuo käyttäjätilit** (ryhmä-lisää kuvake) – lataa aiemmin viety JSON-tiedosto luodaksesi käyttäjätilit suurina erinä. Kaikkien tuotuja käyttäjiä on asetettava uusi salasana "Unohditko salasanan" -linkin kautta, koska salasanoja ei voi siirtää.

## Rekisteröintilinkki (monipuun asetukset vain)

Monipuun asetuksissa rekisteröintilinkki uusille käyttäjille näkyy käyttäjien hallintasivun yläosassa. Voit kopioida tämän linkin ja jakaa sen henkilöille, joita haluat kutsua rekisteröimään tilin puussasi.

!!! huomautus
    Yksittäisessä puu-asetuksessa on yleinen "Rekisteröidy" -linkki kirjautumissivulla; puukohtainen rekisteröintilinkki on tarpeen vain monipuun asennuksissa.

## AI-keskusteluoikeudet

Jos AI-keskustelu on otettu käyttöön palvelimella, sivun yläosassa oleva avattava valikko antaa sinun hallita, mitkä käyttäjäroolit saavat käyttää keskustelutoimintoa:

- Kaikki (mukaan lukien vieraat)
- Jäsenet ja sitä korkeammat
- Avustajat ja sitä korkeammat
- Toimittajat ja sitä korkeammat
- Vain omistajat ja ylläpitäjät
- Kukaan (poista keskustelu käytöstä kaikilta käyttäjiltä)
