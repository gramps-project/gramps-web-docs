# Tarkista ja vahvista tiedot

**Perhepuun käsittely** -osio [Hallintasettingeissä](settings.md) sisältää kaksi työkalua, jotka tarkistavat perhepuun: yhden teknisten ongelmien varalta tietokannassa ja toisen epäuskottavien tietojen varalta.

## Tarkista ja korjaa tietokanta

Tämä työkalu tarkistaa Gramps-tietokannan sisäiset epäjohdonmukaisuudet ja korjaa ne, joita se voi – vastaavasti [Tarkista ja korjaa tietokanta -työkaluun](https://www.gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Tools#Check_and_Repair_Database) Gramps Desktopissa.

Napsauta **Tarkista ja korjaa** ja odota, että edistymisindikaattori valmistuu. Tulos näytetään painikkeen alapuolella:

- Jos virheitä ei löytynyt, näytetään vahvistusviesti.
- Jos virheitä löytyi, näytetään yhteenveto tehdyistä korjauksista.

Suorita tämä työkalu, jos kohtaat odottamattomia virheitä tai käyttäytymistä, joka voi johtua tietokannan epäjohdonmukaisuuksista, kuten puuttuvista suhteista objektien välillä.

## Vahvista tiedot

Kun [Tarkista ja korjaa tietokanta](#check-and-repair-database) etsii *teknisiä* epäjohdonmukaisuuksia, tämä työkalu etsii *epäuskottavia* tietoja – vastaavasti [Vahvista tiedot -työkaluun](https://gramps-project.org/wiki/index.php/Gramps_5.0_Wiki_Manual_-_Tools#Verify_the_Data) Gramps Desktopissa. Se raportoi asioita, jotka eivät ole mahdottomia, mutta ovat tarpeeksi epätodennäköisiä ollakseen tarkistamisen arvoisia, kuten 12-vuotias äiti tai henkilö, joka eli 130-vuotiaaksi.

**Asetukset**-kohdassa voit säätää testien käyttämät kynnysarvot – maksimi-ikä, minim- ja maksimi-ikä naimisiin menemiselle tai lasten saamiselle, lasten maksimi määrä ja niin edelleen – sekä arvioida puuttuvia tai epätarkkoja päivämääriä ja raportoida virheellisiä päivämääriä, kuten 31. helmikuuta. Muuttamasi asetukset muistetaan selaimessasi seuraavaa kertaa varten; **Nollaa** palauttaa oletusasetukset.

Napsauta **Vahvista tiedot** aloittaaksesi. Tarkistus suoritetaan taustatehtävänä, ja löydökset luetellaan sitten **Tietojen vahvistustulokset** -kohdassa. Tämä työkalu ei muuta mitään: se raportoi vain, mitä se löytää.

!!! note
    Löydös ei ole todiste virheestä. Pitkät elinajat ja suuret ikäerot esiintyvät, joten käsittele tuloksia tarkistettavien asioiden luettelona sen sijaan, että pitäisit niitä korjattavien asioiden luettelona.
