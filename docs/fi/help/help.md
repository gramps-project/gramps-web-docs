---
hide:
  - navigation
---

Jos kohtaat ongelmia tai tarvitset apua Gramps Webin kanssa, valitse jokin seuraavista vaihtoehdoista.

[Forum :material-forum:](https://gramps.discourse.group/c/gramps-web/){ .md-button }
[Backend-ongelmat :material-github:](https://github.com/gramps-project/gramps-web-api/issues){ .md-button }
[Frontend-ongelmat :material-github:](https://github.com/gramps-project/gramps-web/issues){ .md-button }

Katso alla ohjeita siitä, mihin kannattaa ensin suunnata.

## Kysymysten esittäminen

Virallinen Gramps Discourse -foorumi sisältää [erillisen kategorian Gramps Webille](https://gramps.discourse.group/c/gramps-web/). Käytä sitä esittääksesi kysymyksiä, joita sinulla saattaa olla Gramps Webistä, esimerkiksi

- Kysymyksiä Gramps Webin käytöstä
- Kysymyksiä Gramps Webin konfiguroinnista
- Ongelmanratkaisu Gramps Webin käyttöönotossa
- Ideoita parannuksista Gramps Webiin
- ...

## Ongelmien raportointi

Jos kohtaat ongelman, jonka uskot olevan bugi Gramps Webissä, tue sitä Githubin kautta.

Gramps Webissä käytettävälle koodille on kaksi erillistä Github-repositoriota, yksi käyttöliittymälle (“frontend”) ja yksi palvelinkoodille (“backend”):

- [Frontend-ongelmat](https://github.com/gramps-project/gramps-web/issues)
- [Backend-ongelmat](https://github.com/gramps-project/gramps-web-api/issues)

Jos et ole varma, mihin ongelma kannattaa raportoida, älä huoli ja valitse vain toinen kahdesta – ylläpitäjät pystyvät siirtämään ongelman tarvittaessa.

Molemmissa tapauksissa, muista aina liittää raporttiisi seuraavat tiedot:

- Tiedot ympäristöstäsi (esim. docker-compose-tiedosto, jossa arkaluontoiset arvot on poistettu, tai käytätkö isännöityä versiota, kuten Grampshub, tai esikonfiguroitua kuvaa, kuten DigitalOcean)
- Versiotiedot. Saadaksesi sen, siirry "Järjestelmätiedot" -välilehdelle Asetukset-sivulla Gramps Webissä ja kopioi/liitä arvot laatikosta, jonka pitäisi näyttää suunnilleen tältä:

```
Gramps 5.1.6
Gramps Web API 1.5.1
Gramps.js 24.1.0
locale: fi
multi-tree: false
task queue: true
```

## Parannusehdotusten tekeminen

Yleisiä ideoita ja keskustelua tulevista parannuksista varten, voit avata keskustelun [foorumilla](https://gramps.discourse.group/c/gramps-web/). Saatat myös haluta tarkistaa ongelmasivut (katso yllä olevat linkit), onko tietty ominaisuus jo suunnitteilla tai työn alla.

Rajoitetun laajuuden erityisiä parannuksia varten, voit avata suoraan ongelman ominaisuuspyynnöllä asianmukaisessa frontend- tai backend-Github-repositoriossa.
