# Käyttäjäjärjestelmä

Gramps Web ei ole tarkoitettu julkiseksi internet-käyttöön, vaan vain todennetuille käyttäjille. Käyttäjätilit voidaan luoda sivuston omistajan toimesta komentoriviltä tai verkkoliittymästä, tai itseilmoittautumisen ja sen jälkeisen hyväksynnän kautta sivuston omistajalta.

## Käyttäjäroolit

Seuraavat käyttäjäroolit on tällä hetkellä määritelty.

Rooli | Rooli-ID | Oikeudet
-----|---------|------------
Vieras | 0 | Näytä ei-yksityisiä kohteita
Jäsen | 1 | Vieras + näytä yksityiset kohteet
Myötävaikuttaja* | 2 | Jäsen + lisää kohteita
Toimittaja | 3 | Myötävaikuttaja + muokkaa ja poista kohteita
Omistaja | 4 | Toimittaja + hallinnoi käyttäjiä
Ylläpitäjä | 5 | Omistaja + muokkaa muita puita monipuu-asetuksessa

\* Huomaa, että "Myötävaikuttaja" rooli on tällä hetkellä vain osittain tuettu; esim. perheobjekteja ei voida lisätä, koska ne edellyttävät perheenjäsenten taustalla olevien Gramps-henkilöobjektien muokkaamista. On suositeltavaa käyttää muita rooleja aina kun mahdollista.

## AI-chatin käyttöoikeuksien määrittäminen

Jos olet [määrittänyt AI-chatin](chat.md), näet täällä vaihtoehdon valita, mitkä käyttäjäryhmät saavat käyttää chat-ominaisuutta.

## Käyttäjien hallinta

Käyttäjien hallintaan on kaksi tapaa:

- Omistajan oikeuksilla verkkoliittymän kautta
- Komentorivillä palvelimella

Omistajatili, joka vaaditaan ensimmäiseen pääsyyn verkkosovellukseen, voidaan lisätä onboarding-velhoon, joka käynnistyy automaattisesti, kun Gramps Webiin päästään tyhjällä käyttäjädatabasella.

### Käyttäjien hallinta komentorivillä

Kun käytetään [Docker Composea](deployment.md), peruskäsky on

```bash
docker compose run grampsweb python3 -m gramps_webapi user COMMAND [ARGS]
```

`COMMAND` voi olla `add` tai `delete`. Käytä `--help`-komentoa `[ARGS]`-parametrille näyttämään syntaksin ja mahdolliset konfigurointivaihtoehdot.

### Itseilmoittautuneiden käyttäjien hyväksyminen

Kun käyttäjä itseilmoittautuu, hänelle ei myönnetä välitöntä pääsyä. Sähköposti lähetetään puun omistajalle uudesta käyttäjäilmoittautumisesta, ja käyttäjälle lähetetään sähköpostipyyntö vahvistaa sähköpostiosoitteensa. Sähköpostiosoitteen onnistunut vahvistaminen muuttaa heidän roolinsa `unconfirmed`-tilasta `disabled`-tilaan. Kun käyttäjätili on jommassakummassa näistä kahdesta roolista, käyttäjä ei voi kirjautua sisään. Puun omistajan on tarkasteltava käyttäjän pyyntö ja annettava käyttäjälle sopiva rooli ennen kuin hän saa kirjautua sisään.
