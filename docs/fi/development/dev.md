---
hide:
  - toc
---

# Gramps Web kehitys: yleiskatsaus

Gramps Web on verkkosovellus, joka koostuu kahdesta erikseen kehitettävästä komponentista:

- **Gramps Web API** on RESTful API, joka on kirjoitettu Pythonilla ja perustuu Flaskiin. Lähdekoodi on isännöity osoitteessa [github.com/gramps-project/gramps-web-api](https://github.com/gramps-project/gramps-web-api/). Se hallinnoi tietokantayhteyksiä ja sukututkimustoimintoja suoraan hyödyntäen Gramps Python -kirjastoa. Se toimii Gramps Webin taustajärjestelmänä. Kehitysdokumentaatiota varten katso [Backend](backend/index.md).
- **Gramps Web Frontend** on Javascript-verkkosovellus, joka toimii Gramps Webin etupäänä. Lähdekoodi on isännöity osoitteessa [github.com/gramps-project/gramps-web](https://github.com/gramps-project/gramps-web/). Kehitysdokumentaatiota varten katso [Frontend](frontend/index.md).

Huomautus versionoinnista: Gramps Web API ja Gramps Web etupää versioidaan itsenäisesti. Tällä hetkellä "Gramps Web" – yhdistetty sovellus – ei omaa erillistä versionumeroa. Molemmat projektit noudattavat [SemVer](https://semver.org/) -standardeja.

Jos et ole Python- tai Javascript-kehittäjä, mutta haluaisit silti osallistua Gramps Webin kehittämiseen, tutustu [Contribute](../contribute/contribute.md).
