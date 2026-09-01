# Käytä sisäänrakennettua blogia

Blogi on tarkoitettu perhehistorian tutkimustarinoiden esittämiseen.

Gramps-tietokannassa blogikirjoitukset esitetään lähteinä, joihin on liitetty muistiinpano, joka sisältää blogin tekstin ja valinnaisesti media tiedostoja blogikirjoituksen kuvista. Gramps Web käsittelee jokaista `Blog`-tunnisteella varustettua lähdettä blogikirjoituksena.

## Lisää blogikirjoitus

Nopein tapa kirjoittaa kirjoitus on erityinen **Uusi blogikirjoitus** -lomake Gramps Webissä. Avaa se joko sinisestä **+**-painikkeesta Blogi-sivulla tai **Lisää**-valikosta (plus-ikoni) ylävalikossa valitsemalla **Blogikirjoitus**.

Lomakkeessa on kenttiä:

- **Otsikko** – kirjoituksen otsikko (pakollinen)
- **Kirjoittaja** – kuka sen kirjoitti
- **Sisältö** – rikkaan tekstin editori itse kirjoitukselle
- **Media** – yksi tai useampi mediaobjekti. Ensimmäisestä tulee esikatselukuva, joka näytetään tekstin yläpuolella; kaikki ne näkyvät galleriana sen alla.
- **Tunnisteet** ja **yksityinen** kytkin, kuten muissakin objekteissa

Lomakkeen tallentaminen luo sinulle taustalla olevan lähteen, muistiinpanon ja `Blog`-tunnisteen, kuten on kuvattu [alla](#relation-between-blog-and-sources).

### Kirjoituksen lisääminen manuaalisesti

Voit myös luoda kirjoituksen rakentamalla taustalla olevat objektit itse. Tämä on ainoa tapa tehdä se Gramps Desktopissa ([synkronoitu](../administration/sync.md) Gramps Webin kanssa), ja vaiheet ovat samat molemmissa sovelluksissa:

- Lisää uusi lähde. Lähteen otsikko on blogikirjoituksesi otsikko, lähteen kirjoittaja on kirjoituksen kirjoittaja.
- Valinnaisesti, liitä lähde varastoon, joka vastaa Gramps Web -blogiasi.
- Lisää uusi muistiinpano lähteeseen. Kirjoita blogikirjoituksesi ja kopioi teksti muistiinpanoon.
- Valinnaisesti, lisää yksi tai useampi media tiedosto lähteeseesi. Ensimmäinen media tiedosto otetaan kirjoituksen esikatselukuvaksi, joka näytetään tekstin yläpuolella. Kaikki media tiedostot näytetään tekstin alla galleriana.
- Lisää `Blog`-tunniste lähteeseen (luo se, jos sitä ei ole).

## Suhde blogin ja lähteiden välillä

Koska blogikirjoitukset ovat vain lähteitä, kaikki blogiartikkelit näkyvät myös lähteiden luettelossa ja ilmestyvät lähteinä hauissa. Lähdenäkymässä on painike "näytä blogissa", joka vie sinut bloginäkymään kyseiselle blogikirjoitukselle. Blogikirjoituksen URL-osoite sisältää myös vastaavan lähteen Gramps ID:n, joten artikkeli osoitteessa `yourdomain.com/blog/S0123` vastaa lähdettä osoitteessa `yourdomain.com/source/S0123`.

Jokaisen blogikirjoituksen alareunassa on painike "tiedot", joka vie sinut lähdenäkymään.
