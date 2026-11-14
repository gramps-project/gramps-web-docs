# Varmuuskopiointi ja palautus

Puun omistajat voivat luoda, ladata ja palauttaa varmuuskopioita puusta **Varmuuskopiot**-osiossa [Hallinta-asetuksissa](settings.md).

Varmuuskopio sisältää sukupuudun tiedot, mukaan lukien yksityiset tiedot, puun asetukset ja puun käyttäjät. Mediakuvia ei sisällytetä; katso [Varmuuskopioi mediakuvasi](export.md#back-up-your-media-files).

## Tallennetut varmuuskopiot

Jos palvelimen ylläpitäjä on määrittänyt varmuuskopiohakemiston (`BACKUP_DIR`, katso [Palvelimen kokoonpano](../install_setup/configuration.md)), varmuuskopiot voidaan tallentaa palvelimelle. Muuten osiossa näkyy ilmoitus, että varmuuskopioiden tallentaminen ei ole määritetty, ja vain palauttaminen ladatusta tiedostosta on mahdollista.

Napsauta **Luo varmuuskopio...** luodaksesi varmuuskopion. Se luodaan taustatehtävänä ja ilmestyy sitten tallennettujen varmuuskopioiden luetteloon, jossa on sen päivämäärä, henkilöiden määrä ja koko. Palvelin säilyttää vain uusimmat varmuuskopiot (oletuksena viisi) ja poistaa vanhemmat automaattisesti. Varmuuskopioiden luomisen määrä päivässä on myös rajoitettu.

Jokaiselle tallennetulle varmuuskopiolle voit:

- **Ladata** sen `.tar`-tiedostona, esimerkiksi pitääksesi kopion muualla.
- **Palauttaa** sen, kuten alla on kuvattu.
- **Poistaa** sen, vahvistamisen jälkeen.

Uudemmalla Gramps Web -versiolla tehty varmuuskopio, kuin mitä palvelimella on käytössä, merkitään varoituskuvakkeella eikä sitä voi palauttaa.

## Palauta varmuuskopiosta

Palauttaa puun tallennetusta varmuuskopiosta tai ladatusta tiedostosta. Palauttaaksesi tallennetun varmuuskopion, napsauta palautuspainiketta sen vieressä. Palauttaaksesi tiedostosta, valitse Gramps Web -varmuuskopio (`.tar`) tai Gramps XML -tiedosto (`.gramps`) ja napsauta **Palauta**.

!!! danger
    Tietojen palauttaminen on tuhoava korvaus, ei yhdistäminen. Kaikki olemassa olevat objektit, joita ei ole varmuuskopiossa, poistetaan.

Gramps Web -varmuuskopion kohdalla dialogi näyttää, milloin varmuuskopio on tehty, minkä puun osalta ja millä versiolla, ja antaa sinun valita, mitkä osat palautetaan:

- **Tiedot** – sukupuun objektit
- **Puun asetukset** – Hallinta-sivun asetukset, kuten teeman värit, sovelluksen otsikko ja etusivun huomautus
- **Käyttäjät** – puun käyttäjät

Napsauta **Esikatselu** nähdäksesi, mitä palautus muuttaisi. Gramps XML -tiedosto sisältää vain tietoja, joten tällaisen tiedoston esikatselu alkaa heti. Sinua pyydetään vahvistamaan henkilöllisyytesi, jos istuntosi ei ole tarpeeksi tuore. Esikatselu toimii taustatehtävänä ja, kun se on valmis, avaa dialogi, joka tiivistää muutokset objektityypin mukaan (henkilöt, perheet, tapahtumat, paikat, viittaukset, lähteet, arkistot, mediakohteet, muistiinpanot, tunnisteet), sekä puun asetusten ja käyttäjien osalta, jos ne on valittu:

- **Lisää** – objektit, jotka ovat varmuuskopiossa mutta puuttuvat nykyisestä puusta
- **Päivitä** – objektit, jotka ovat molemmissa mutta eroavat
- **Poista** – objektit nykyisessä puussa, joita ei ole varmuuskopiossa
- **Ei muutoksia** – objektit, jotka ovat identtisiä molemmissa

Jos mitään objekteja poistettaisiin, dialogi varoittaa kuinka monta. Tarkista yhteenveto, napsauta sitten **Palauta** soveltaaksesi muutoksia tai **Peruuta** keskeyttääksesi.

Palautuksen jälkeen varmuuskopiosta lisätyt käyttäjät luetellaan. He saavat satunnaisen salasanan, joten heidän on vaihdettava salasanansa ennen kirjautumista. Palvelimella jo olemassa olevia käyttäjiä ei koskaan muuteta. Mediakohteet, joiden tiedostot puuttuvat palvelimelta, luetellaan myös; lataa ne [Tuonti mediakuvista](import-media.md) kautta.

!!! note
    Tietojen palauttaminen palauttaa vain objektitiedot ja mediaviittaukset. Binääriset mediakuvat ja puun metatiedot (oletushenkilö, kirjanmerkit, nimiryhmät) eivät vaikuta.

!!! tip
    Käytä tätä palauttaaksesi puu tunnettuun hyvään varmuuskopioon, esimerkiksi huonon tuonnin tai ei-toivotun massamuokkauksen jälkeen.

## Gramps XML varmuuskopiona

Jos varmuuskopioiden tallentaminen ei ole mahdollista tai haluat vain pitää kopion sukupuudun tiedoista, [vie](export.md) puu Gramps XML -tiedostona. Tällainen tiedosto voidaan palauttaa myös [Palauta varmuuskopiosta](#restore-from-backup).

Huomaa, että jos Gramps Web -käyttäjälläsi ei ole lupaa nähdä yksityisiä tietoja, vienti ei ole täydellinen varmuuskopio, koska se ei sisällä mitään yksityisiä tietoja.
