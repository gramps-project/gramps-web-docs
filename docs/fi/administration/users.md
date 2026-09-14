# Käyttäjien hallinta

Käyttäjien hallintaliittymä on saatavilla kohdasta **Asetukset > Hallitse käyttäjiä** (käyttäjäkuvake ylävalikkopalkissa). Se on saatavilla vain omistaja- tai ylläpitäjäroolilla oleville käyttäjille.

## Käyttäjäroolit

Katso [Käyttäjäjärjestelmä](../install_setup/users.md) saadaksesi täydellisen kuvauksen saatavilla olevista käyttäjärooleista ja niiden oikeuksista.

## Käyttäjien tarkastelu ja suodatus

Käyttäjien hallintasivulla on taulukko kaikista rekisteröidyistä käyttäjätilistä seuraavilla sarakkeilla:

- **Käyttäjänimi** – kirjautumisnimi
- **Koko nimi** – näyttönimi
- **Sähköposti** – käyttäjän sähköpostiosoite
- **Rooli** – määritetty rooli (Vieras, Jäsen, Avustaja, Toimittaja, Omistaja tai Ylläpitäjä)
- **Tilin lähde** – joko "Salasana" (paikallinen tili) tai ulkoisen identiteettipalveluntarjoajan nimi (esim. OIDC:tä käytettäessä)

Käytä taulukon yläpuolella olevaa hakukenttää ja roolivalikkoa suodattaaksesi luetteloa. Napsauta suodattimen tyhjennyspainiketta nollataksesi kaikki suodattimet.

## Muokkaa käyttäjää

Napsauta muokkaus (kynä) kuvaketta missä tahansa rivissä avataksesi muokkausdialogin. Voit muuttaa käyttäjän:

- Koko nimi
- Sähköpostiosoite
- Rooli

Tämä on ensisijainen tapa **ottaa käyttöön uusi itse rekisteröitynyt käyttäjä**: muuta heidän roolinsa *poistettu* -tilasta mihin tahansa aktiiviseen rooliin (esim. Jäsen tai Toimittaja).

Sähköpostiosoitteiden ei tarvitse olla ainutlaatuisia (koska Gramps Web API 3.22), joten useat tilit voivat jakaa saman osoitteen.

## Lisää käyttäjä manuaalisesti

Napsauta **lisää käyttäjä** (henkilö-lisää) kuvaketta taulukon yläpuolella luodaksesi uuden käyttäjätilin suoraan ilman itse rekisteröitymistä. Täytä käyttäjänimi, koko nimi, sähköpostiosoite, salasana ja rooli dialogiin ja napsauta **Tallenna**.

## Poista käyttäjä

Napsauta poisto (roskakori) kuvaketta missä tahansa rivissä ja vahvista dialogi. Tätä toimintoa ei voi peruuttaa.

!!! huomautus
    Jotta puuta ei jää ilman ketään, joka voi hallita sitä, et voi alentaa omaa rooliasi alle Omistajan tai poistaa omaa tiliäsi, jos olet ainoa Omistaja tai Ylläpitäjä puussa. Edistä toista käyttäjää ensin Omistajaksi. Ylläpitäjä voi silti muuttaa tai poistaa toisen käyttäjän puun viimeisen omistajan, koska he voivat nimittää uuden.

## Käyttäjätilien vienti ja tuonti

Nämä painikkeet ovat hyödyllisiä [siirryttäessä toiseen Gramps Web -instanssiin](export.md).

- **Vie käyttäjätiedot** (latauskuvake) – lataa JSON-tiedosto, joka sisältää kaikki käyttäjätilit (ilman salasanoja, koska salasanat tallennetaan salattuna).
- **Tuo käyttäjätilit** (ryhmä-lisää kuvake) – lataa aiemmin viety JSON-tiedosto luodaksesi käyttäjätilit suurina erinä. Kaikkien tuotuja käyttäjiä on asetettava uusi salasana "Unohditko salasanan" -linkin kautta, koska salasanoja ei voida siirtää.

## Rekisteröintilinkki (monipuun asetukset vain)

Monipuun asetuksissa rekisteröintilinkki uusille käyttäjille näkyy käyttäjien hallintasivun yläosassa. Voit kopioida tämän linkin ja jakaa sen ihmisten kanssa, joita haluat kutsua rekisteröitymään tilille puussasi.

!!! huomautus
    Yksittäisen puun asetuksissa kirjautumissivulla on yleinen "Rekisteröidy" -linkki; puukohtainen rekisteröintilinkki on tarpeen vain monipuun asennuksissa.

## AI-chat-oikeudet

Jos AI-chat on otettu käyttöön palvelimella, sivun yläosassa oleva pudotusvalikko antaa sinun hallita, mitkä käyttäjäroolit saavat käyttää chat-ominaisuutta:

- Kaikki (mukaan lukien vieraat)
- Jäsenet ja sitä korkeammat
- Avustajat ja sitä korkeammat
- Toimittajat ja sitä korkeammat
- Vain omistajat ja ylläpitäjät
- Kukaan (poista chat käytöstä kaikilta käyttäjiltä)
