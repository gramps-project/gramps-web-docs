# Gramps Web Asennus / Asetus

Tässä osiossa käsitellään Gramps Webin asennusta ja asetusta sekä muita vaihtoehtoja aloittamiseen.

## Aloittaminen Gramps Webin kanssa

Gramps Web on verkkosovellus, joka toimii palvelimella ja johon pääsee käsiksi verkkoselaimen kautta. Sen on tarkoitus olla käytettävissä todennetuille käyttäjille internetin kautta.

Jos haluat käyttää Gramps Webiä sukututkimustietojesi hallintaan, sinun on valittava jokin seuraavista vaihtoehdoista:

1. Itse isännöinti omalla laitteistolla
2. Itse isännöinti pilvessä
3. Rekisteröidy isännöityyn instanssiin

Vaikka ensimmäinen vaihtoehto antaa sinulle maksimaalisen joustavuuden ja hallinnan, se voi myös olla teknisesti haastavaa.

!!! vinkki
    Yksi Gramps Webin pääperiaatteista on antaa käyttäjille hallinta omista tiedoistaan milloin tahansa, joten tietojen siirtäminen yhdestä instanssista toiseen on yksinkertaista. Älä huoli, ettet voi siirtyä toiseen vaihtoehtoon sen jälkeen, kun olet valinnut yhden!

## Itse isännöinti omalla laitteistolla

Kätevintä itse isännöidä Gramps Web on Docker Composen avulla. Tarjoamme myös Docker-kuvia ARM-arkkitehtuurille, joten voit ajaa Gramps Webiä Raspberry Pi:llä kellarissasi.

Katso [Asenna Dockerin avulla](deployment.md) asennusohjeita varten.

## Itse isännöinti pilvessä

Gramps Webin asentaminen voi olla haastavampaa kuin muiden yksinkertaisten verkkosovellusten, eikä se ole yhteensopiva tavallisten "jaettujen isännöintipalveluiden" kanssa. Voit rekisteröityä virtuaalipalvelimelle ja asentaa Gramps Webin [manuaalisesti](deployment.md).

Yksinkertaisempi vaihtoehto on käyttää esiasennettua pilvikuvaa. Esimerkki on meidän [DigitalOcean 1-napin sovellus](digital_ocean.md).

## Rekisteröidy isännöityyn instanssiin

Isännöity Gramps Web on helpoin tapa aloittaa Gramps Webin käyttö, sillä asennusta tai konfigurointia ei vaadita.

Tässä on lista omistetuista isännöintipalveluntarjoajista Gramps Webille (Grampsin avoimen lähdekoodin yhteisö ei ota vastuuta heidän palveluistaan):

- Grampshub ([www.grampshub.com](https://www.grampshub.com)), jota tarjoaa yksi Gramps Webin päätekijöistä

Jos käytät isännöityä vaihtoehtoa Gramps Webille, voit ohittaa tämän osion loput ja siirtyä suoraan [Hallinta](../administration/admin.md) -osioon.
