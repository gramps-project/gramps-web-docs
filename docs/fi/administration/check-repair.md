# Tarkista ja varmista tiedot

**Perhepuun käsittely** -osiossa [Hallinta-asetukset](settings.md) on kaksi työkalua, jotka tarkistavat perhepuun: yksi teknisten ongelmien varalta tietokannassa ja toinen epäuskottavien tietojen varalta.

## Tarkista ja korjaa tietokanta

Tämä työkalu tarkistaa Gramps-tietokannan sisäiset epäjohdonmukaisuudet ja korjaa ne, jotka se pystyy – vastaavasti [Tarkista ja korjaa tietokanta -työkalun](https://www.gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Tools#Check_and_Repair_Database) kanssa Gramps Desktopissa.

Napsauta **Tarkista ja korjaa** ja odota edistymisen osoittimen valmistumista. Tulos näkyy painikkeen alapuolella:

- Jos virheitä ei löydy, vahvistusviesti näytetään.
- Jos virheitä löytyy, näytetään yhteenveto tehdyistä korjauksista.

Käynnistä tämä työkalu, jos kohtaat odottamattomia virheitä tai käyttäytymistä, joka voi johtua tietokannan epäjohdonmukaisuuksista, kuten puuttuvista suhteista objektien välillä.

## Vahvista tiedot

Kun [Tarkista ja korjaa tietokanta](#check-and-repair-database) etsii *teknisiä* epäjohdonmukaisuuksia, tämä työkalu etsii *epäuskottavia* tietoja – vastaavasti [Vahvista tiedot -työkalun](https://gramps-project.org/wiki/index.php/Gramps_5.0_Wiki_Manual_-_Tools#Verify_the_Data) kanssa Gramps Desktopissa. Se raportoi asioista, jotka eivät ole mahdottomia, mutta ovat riittävän epätodennäköisiä ollakseen tarkistamisen arvoisia, kuten 12-vuotias äiti tai henkilö, joka eli 130-vuotiaaksi.

**Asetukset**-kohdassa voit säätää testien käyttämät kynnysarvot – maksimi-ikä, minimija maksimi-ikä naimisiin menemiselle tai lasten saamiselle, maksimi lasten määrä ja niin edelleen – sekä arvioida puuttuvia tai epätarkkoja päivämääriä ja raportoida virheellisiä päivämääriä, kuten 31. helmikuuta.

Napsauta **Vahvista tiedot** aloittaaksesi. Tarkistus suoritetaan taustatehtävänä, ja löydökset listataan sitten **Tietojen vahvistustulokset** -kohdassa. Tämä työkalu ei muuta mitään: se vain raportoi, mitä se löytää.

!!! note
    Löydös ei ole todiste virheestä. Pitkät eliniät ja suuret ikäerot tapahtuvat, joten käsittele tuloksia tarkistettavien asioiden listana sen sijaan, että pitäisit niitä korjattavien asioiden listana.
