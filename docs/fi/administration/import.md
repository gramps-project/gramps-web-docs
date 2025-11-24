## Valmistele Gramps-tietokantaasi

Jos käytät Gramps Desktopia, on kaksi vaihetta, joilla voit valmistella tietokantaasi varmistaaksesi, että kaikki sujuu ongelmitta seuraavassa. Jos siirryt toisesta sukututkimusohjelmasta, voit ohittaa tämän vaiheen.

1. Tarkista ja korjaa tietokanta
    - Valinnainen: luo tietokannan varmuuskopio viemällä se Gramps XML:ään
    - Suorita [Tarkista ja korjaa tietokanta -työkalu](https://gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Tools#Check_and_Repair_Database). Tämä korjaa joitakin sisäisiä epäjohdonmukaisuuksia, jotka voisivat aiheuttaa ongelmia Gramps Webissä.
2. Muunna median polut suhteellisiksi
    - Käytä Gramps Media Manageria [muuntaaksesi kaikki median polut absoluuttisista suhteellisiksi](https://gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Tools#Convert_paths_from_relative_to_absolute). Huomaa, että vaikka suhteellisilla poluilla, kaikki median tiedostot, jotka ovat Grampsin mediahakemiston ulkopuolella, eivät toimi oikein synkronoidessa Gramps Webin kanssa.

## Tuo sukututkimustietoja

Jos haluat tuoda olemassa olevan sukupuun, käytä "Tuo" -sivua ja lataa tiedosto missä tahansa Grampsin tukemassa tiedostomuodossa &ndash; katso [Tuo toisesta sukututkimusohjelmasta](https://www.gramps-project.org/wiki/index.php/Import_from_another_genealogy_program) Gramps Wikistä.

Jos käytät jo Gramps Desktopia, on vahvasti suositeltavaa käyttää Gramps XML (`.gramps`) -muotoa varmistaaksesi, että verkkopuut ja offline-puut käyttävät samoja tunnisteita ja voivat olla [synkronoitu](sync.md).

## Miksi ei tukea Gramps XML -paketille?

Vaikka Gramps XML (`.gramps`) on suosituin muoto tietojen tuomiseen, Gramps XML *pakettia* (`.gpkg`) ei tueta Gramps Webissä. Tämä johtuu siitä, että median tiedostojen tuonti- ja vientimenettelyt eivät sovellu käytettäväksi verkkopalvelimella.

Tuodaksesi median tiedostot, jotka kuuluvat tuodulle `.gramps`-tiedostolle, katso seuraava osio.

## Tuo median tiedostot

Jos olet ladannut sukupuun ja sinun on ladattava vastaavat median tiedostot, voit käyttää "tuo media-arkisto" -painiketta "Tuo" -sivulla.

Se odottaa ZIP-tiedostoa, jossa on puuttuvat median tiedostot. ZIP-tiedoston kansiorakenteen ei tarvitse olla sama kuin Grampsin mediahakemiston kansiorakenne, koska tiedostot yhdistetään mediaobjekteihin niiden tarkistussumman perusteella.

Huomaa, että tämä ominaisuus toimii vain tiedostoille, joilla on oikea tarkistussumma Gramps-tietokannassa (mikä tulisi varmistaa suorittamalla tarkistus- ja korjaustyökalu ensimmäisessä vaiheessa).

Siirryttäessä Gramps Webiin toisesta sukututkimusohjelmasta, joka sisältää median tiedostoja, on suositeltavaa ensin tuoda kaikki Gramps Desktopiin, jossa on enemmän vaihtoehtoja yhdistää olemassa olevia median tiedostoja tuodun puun kanssa.
