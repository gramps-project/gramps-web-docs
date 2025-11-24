# Frontend-kehityksen asetukset

Tämä sivu kuvaa vaiheet, jotka tarvitaan frontend-kehityksen aloittamiseen.

## Esivaatimukset

Suositeltu kehitysympäristö käyttää Visual Studio Codea devcontainerien kanssa. Tämä lähestymistapa luo esikonfiguroidun kehitysympäristön kaikilla tarvittavilla työkaluilla.

Katso [Backend-kehityksen asetukset](../backend/setup.md#prerequisites) tarvittavista esivaatimuksista.

## Aloittaminen

1. Avaa [Gramps Web frontend -varasto](https://github.com/gramps-project/gramps-web) ja napsauta "fork"
2. Kloonaa forkattu varasto paikalliselle koneellesi Gitin avulla
3. Avaa kloonattu varasto Visual Studio Codessa. Kun sinua pyydetään, valitse "Avaa uudelleen säiliössä" tai avaa manuaalisesti komentoikkuna (Ctrl+Shift+P tai Cmd+Shift+P) ja valitse "Dev Containers: Rakennus ja avaa uudelleen säiliössä".
4. Odota, että dev-säiliö rakennetaan ja käynnistyy. Tämä voi kestää muutaman minuutin, erityisesti ensimmäisellä kerralla.

## Frontend-kehityspalvelimen ajaminen

Ajaaksesi frontend-kehityspalvelinta ja esikatsellaksesi muutosten vaikutusta selaimessa, voit käyttää dev-säiliössä määriteltyjä tehtäviä.

Jotta tämä toimisi, sinun on ensin käynnistettävä [Gramps Web API -backendin](../backend/setup.md#tasks) instanssi. Helpoin tapa tehdä tämä on käyttää backendin dev-säiliötä ja [suorittaa "Serve Web API" -tehtävä](../backend/setup.md#tasks) erillisessä VS Code -ikkunassa.

Kun backend on käynnissä, voit ajaa frontend-kehityspalvelinta valitsemalla "Tehtävät: Suorita tehtävä" komentoikkunasta (Ctrl+Shift+P tai Cmd+Shift+P) ja valitsemalla sitten "Serve Gramps Web frontend".

Tämä käynnistää frontend-kehityspalvelimen portissa 8001, johon voit päästä selaimessasi osoitteessa `http://localhost:8001`. Selaimen pitäisi ladata automaattisesti uudelleen, kun teet muutoksia frontend-koodiin, jolloin voit nähdä muutosten vaikutuksen heti.
