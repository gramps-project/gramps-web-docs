---
hide:
  - navigation
---

Jos kohtaat ongelmia tai tarvitset apua Gramps Webin kanssa, valitse jokin seuraavista vaihtoehdoista.

[Forum :material-forum:](https://gramps.discourse.group/c/gramps-web/){ .md-button }
[Backend-ongelmat :material-github:](https://github.com/gramps-project/gramps-web-api/issues){ .md-button }
[Frontend-ongelmat :material-github:](https://github.com/gramps-project/gramps-web/issues){ .md-button }

Katso alla ohjeita siitä, mihin kannattaa ensiksi suunnata.

## Kysymysten esittäminen

Virallinen Gramps Discourse -foorumi sisältää [erillisen kategorian Gramps Webille](https://gramps.discourse.group/c/gramps-web/). Käytä sitä kysyäksesi mitä tahansa kysymyksiä, joita sinulla saattaa olla Gramps Webistä, esimerkiksi

- Kysymyksiä Gramps Webin käytöstä
- Kysymyksiä Gramps Webin konfiguroinnista
- Ongelmanratkaisu Gramps Webin käyttöönotossa
- Ideoita parannuksista Gramps Webiin
- ...

## Ongelmien ilmoittaminen

Jos kohtaat ongelman, jonka uskot olevan virhe Gramps Webissä, ilmoita siitä GitHubissa.

Gramps Webissä käytettävälle koodille on kaksi erillistä GitHub-repoa, yksi käyttöliittymälle ("frontend") ja yksi palvelinkoodille ("backend"):

- [Frontend-ongelmat](https://github.com/gramps-project/gramps-web/issues)
- [Backend-ongelmat](https://github.com/gramps-project/gramps-web-api/issues)

Jos et ole varma, mihin ilmoittaa ongelma, älä huoli ja valitse vain jompikumpi – ylläpitäjät pystyvät siirtämään ongelman tarvittaessa.

Molemmissa tapauksissa, muista aina liittää raporttiisi seuraavat tiedot:

- Tiedot asetuksistasi (esim. docker-compose-tiedosto, jossa arkaluontoiset arvot on peitetty, tai käytätkö isännöityä versiota, kuten Grampshub, tai esikonfiguroitua kuvaa, kuten DigitalOcean)
- Versiotiedot. Saat ne menemällä "Järjestelmätiedot" -välilehdelle Asetukset-sivulla Gramps Webissä ja kopioimalla/liittämällä arvot laatikosta, joka näyttää suunnilleen tältä:

```
Gramps 5.1.6
Gramps Web API 1.5.1
Gramps.js 24.1.0
locale: en
multi-tree: false
task queue: true
```

## Parannusehdotusten tekeminen

Yleisiä ideoita ja keskustelua tulevista parannuksista varten voit avata keskustelun [foorumilla](https://gramps.discourse.group/c/gramps-web/). Saatat myös haluta tarkistaa ongelmasivut (katso yllä olevat linkit) nähdäksesi, onko tietty ominaisuus jo suunnitteilla tai työn alla.

Erityisten parannusten osalta, joilla on rajattu laajuus, voit avata suoraan ongelman ominaisuuspyynnöllä asianmukaisessa frontend- tai backend-GitHub-repossa.
