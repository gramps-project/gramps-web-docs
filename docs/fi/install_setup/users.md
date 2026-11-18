# Käyttäjäjärjestelmä

Gramps Web ei ole tarkoitettu julkiseksi internet-käyttöön, vaan vain todennetuille käyttäjille. Käyttäjätilit voidaan luoda sivuston omistajan toimesta komentoriviltä tai verkkoliittymästä, tai itse rekisteröitymällä ja sen jälkeen sivuston omistajan hyväksynnällä.

## Käyttäjäroolit

Seuraavat käyttäjäroolit on tällä hetkellä määritelty.

Rooli | Rooli-ID | Oikeudet
-----|---------|------------
Vieras | 0 | Näytä ei-yksityisiä objekteja
Jäsen | 1 | Vieras + näytä yksityisiä objekteja
Myöntäjä* | 2 | Jäsen + lisää objekteja
Toimittaja | 3 | Myöntäjä + muokkaa ja poista objekteja
Omistaja | 4 | Toimittaja + hallinnoi käyttäjiä
Ylläpitäjä | 5 | Omistaja + muokkaa muita puita monipuu-asetuksessa

Se, onko tietue yksityinen, määritetään tietueittain, katso [Yksityiset tietueet](../user-guide/privacy.md). Mikään ei ole oletusarvoisesti yksityistä, ei edes elävät ihmiset.

\* Huomaa, että "Myöntäjä" rooli on tällä hetkellä vain osittain tuettu; esim. perheobjekteja ei voida lisätä, koska ne merkitsevät perheenjäsenten taustalla olevien Gramps-henkilöobjektien muokkaamista. Suositellaan käyttämään muita rooleja aina kun mahdollista.

## AI-chatin käyttöoikeuden määrittäminen

Jos olet [määrittänyt AI-chatin](chat.md), näet täällä vaihtoehdon valita, mitkä käyttäjäryhmät saavat käyttää chat-ominaisuutta.

## Käyttäjien hallinta

Käyttäjiä voidaan hallita kahdella tavalla:

- Omistajan oikeuksilla verkkoliittymän kautta
- Komentorivillä palvelimella

Omistajatili, joka tarvitaan ensimmäiseen pääsyyn verkkosovellukseen, voidaan lisätä onboarding-velhoon, joka käynnistyy automaattisesti, kun Gramps Webiin pääsee tyhjällä käyttäjädatalla.

### Käyttäjien hallinta komentorivillä

Kun käytetään [Docker Composea](deployment.md), peruskäsky on

```bash
docker compose run grampsweb python3 -m gramps_webapi user COMMAND [ARGS]
```

`COMMAND` voi olla `add`, `set-password` tai `delete`. Käytä `--help`-komentoa `[ARGS]`-osiossa näyttääksesi syntaksin ja mahdolliset konfigurointivaihtoehdot.

`set-password NAME` asettaa uuden salasanan olemassa olevalle käyttäjälle ilman, että vanhaa tarvitaan, esimerkiksi silloin kun kukaan ei voi enää kirjautua sisään ja sähköpostia ei ole asetettu salasanan palautuksia varten (Gramps Web API 3.26+). Se kysyy salasanaa kaksi kertaa näyttämättä sitä, jotta salasana ei päädy shell-historiaan. Kaikki käyttäjän istunnot lopetetaan.

### Itse rekisteröityneiden käyttäjien hyväksyminen

Kun käyttäjä rekisteröityy itse, hänelle ei myönnetä välitöntä pääsyä. Sähköposti lähetetään puun omistajalle uudesta käyttäjärekisteröinnistä, ja käyttäjälle lähetetään sähköpostipyyntö vahvistaa sähköpostiosoitteensa. Sähköpostiosoitteen onnistunut vahvistaminen muuttaa heidän roolinsa `unconfirmed`-tilasta `disabled`-tilaan. Kun käyttäjätili on jommassakummassa näistä kahdesta roolista, käyttäjä ei voi kirjautua sisään. Puun omistajan on tarkasteltava käyttäjän pyyntö ja myönnettävä käyttäjälle sopiva rooli ennen kuin he saavat kirjautua sisään.
