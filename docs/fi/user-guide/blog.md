# Käytä sisäänrakennettua blogia

Blogi on tarkoitettu perhehistorian tutkimustarinoiden esittämiseen.

Gramps-tietokannassa blogikirjoitukset esitetään lähteinä, joihin on liitetty muistiinpano, joka sisältää blogin tekstin ja valinnaisesti media tiedostoja blogikirjoituksen kuvista. Gramps Web käsittelee jokaista lähdettä, jossa on `Blog`-tunniste, blogiartikkelina.

## Lisää blogikirjoitus

Lisätäksesi blogikirjoituksen, voit käyttää Gramps Webiä tai Gramps Desktopia ([synkronoitu](../administration/sync.md) Gramps Webin kanssa), vaiheet ovat samat molemmissa tapauksissa:

- Lisää uusi lähde. Lähteen otsikko on blogikirjoituksesi otsikko, ja lähteen kirjoittaja on kirjoituksen kirjoittaja.
- Valinnaisesti, liitä lähde repositorioon, joka vastaa Gramps Web -blogiasi.
- Lisää uusi muistiinpano lähteeseen. Kirjoita blogikirjoituksesi ja kopioi teksti muistiinpanoon.
- Valinnaisesti, lisää yksi tai useampi media tiedosto lähteeseesi. Ensimmäinen media tiedosto otetaan kirjoituksen esikatselukuvaksi, joka näytetään tekstin yläpuolella. Kaikki media tiedostot näytetään tekstin alla galleriana.
- Lisää tunniste `Blog` lähteeseen (luo se, jos sitä ei ole).

## Suhde blogin ja lähteiden välillä

Koska blogikirjoitukset ovat vain lähteitä, kaikki blogiartikkelit näkyvät myös lähteiden listalla ja ilmestyvät lähteinä hauissa. Lähdenäkymässä on painike "näytä blogissa", joka vie sinut kyseisen blogikirjoituksen bloginäkymään. Blogikirjoituksen URL sisältää myös vastaavan lähteen Gramps ID:n, joten artikkeli osoitteessa `yourdomain.com/blog/S0123` vastaa lähdettä osoitteessa `yourdomain.com/source/S0123`.

Jokaisen blogikirjoituksen alareunassa on painike "tiedot", joka vie sinut lähdenäkymään.
