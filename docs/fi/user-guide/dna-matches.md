# Työskentely DNA-yhteensopivuuksien kanssa

DNA-yhteensopivuudet ovat DNA-segmenttejä, jotka ovat yhteensopivia kahden henkilön välillä, ja ne tunnistetaan merkkien, niin kutsuttujen SNP:iden (yksittäisten nukleotidipolymorfismien, ääntämys "snips") avulla.

Tämän tiedon saamiseksi tarvitset pääsyn DNA-testiin, joka on ladattu yhteensopivuustietokantaan, joka mahdollistaa DNA-segmenttien yhteensopivuustietojen tarkastelun (esim. MyHeritage, Gedmatch, FamilytreeDNA). Gramps Web ei suorita yhteensopivuuksia itse, sillä sillä on vain pääsy ladattuihin tietoihin.

## DNA-yhteensopivuustietojen syöttäminen

Syöttääksesi DNA-yhteensopivuustietoja, tarvitset [muokkausoikeudet](../install_setup/users.md), sillä tiedot tallennetaan muistiin Gramps-tietokannassa. DNA-näkymä, johon pääsee päävalikosta, tarjoaa kätevän tavan syöttää nämä tiedot oikeassa muodossa.

Syöttääksesi uuden yhteensopivuuden, napsauta + -painiketta oikeassa alakulmassa. Avautuvassa valintaikkunassa valitse kaksi henkilöä. Huomaa, että "Ensimmäistä henkilöä" ja "Toista henkilöä" käsitellään eri tavalla: yhteensopivuus tallennetaan assosiaationa ensimmäisestä toiselle henkilölle. Vain ensimmäinen henkilö on valittavissa DNA-yhteensopivuusnäkymässä ja kromosomiselain. Tyypillisesti ensimmäinen henkilö on se, jonka DNA-testiin sinulla on pääsy, ja toinen henkilö on kaukaisempia sukulaisia.

Jos toista henkilöä ei ole tietokannassa, sinun on ensin luotava se käyttämällä "Luo henkilö" -painiketta käyttöliittymän oikeassa yläkulmassa. Kun olet luonut henkilön, voit palata DNA-yhteensopivuusnäkymään ja valita juuri luodun henkilön.

Seuraavaksi liitä raakadata tekstikenttään. Datan tulisi olla pilkulla tai tabilla eroteltu taulukko yhteensopivuuksista, joka tyypillisesti sisältää kromosomin numeron, yhteensopivuuden aloitus- ja lopetuspaikan, yhteensopivuuden SNP-määrän ja yhteensopivuuden pituuden sentimorganina (cM). Voit myös raahata ja pudottaa tiedoston, jossa on yhteensopivuustiedot, tekstikenttään.

Minimalistinen esimerkki tällaisesta taulukosta on:

```csv
Kromosomi,Aloituspaikka,Lopetuspaikka,Sentimorganit,SNP:t
6,6358001,18115715,19.6,7424
7,150135758,154205894,10.9,2816
```

Jos muoto on voimassa, esikatselu näytetään tekstikentän alapuolella taulukkona.

Lopuksi napsauta "Tallenna" -painiketta tallentaaksesi yhteensopivuuden tietokantaan.

## DNA-yhteensopivuustietojen tarkastelu

DNA-yhteensopivuusnäkymässä on avattava valikko, joka mahdollistaa jokaisen tietokannassa olevan henkilön valitsemisen, jolla on siihen liittyvä DNA-yhteensopivuus. Kun henkilö on valittu, DNA-yhteensopivuustiedot näytetään taulukossa avattavan valikon alapuolella. Se näyttää sen henkilön nimen, johon yhteensopivuus liittyy, suhteen valittuun henkilöön avattavassa valikossa (automaattisesti määritetty Gramps-tietokannasta), jaetun DNA:n kokonaispituuden sentimorgina (cM), jaettujen segmenttien määrän sekä suurimman näistä segmenteistä pituuden.

Kun napsautat yksittäistä yhteensopivuutta, se avaa yksityiskohtaisen sivun, joka näyttää kaikki segmentit ja onko yhteensopivuus äidin vai isän puolelta. Tämä tieto voidaan joko syöttää manuaalisesti (antamalla `P` isän puolelle tai `M` äidin puolelle raakadatan `Side`-sarakkeeseen) tai Gramps voi määrittää sen automaattisesti viimeisimmän yhteisen esi-isän perusteella.

## Yhteensopivuuden muokkaaminen

Voit muokata yhteensopivuutta napsauttamalla kynäpainiketta oikeassa alakulmassa yhteensopivuuden yksityiskohtaisessa näkymässä. Tämä avaa samanlaisen valintaikkunan kuin uuden yhteensopivuuden luominen, mutta tiedot on esitäytetty. Huomaa, että voit muuttaa raakadataa, mutta et yhteensopivuuteen liittyviä henkilöitä – sinun on poistettava yhteensopivuus ja luotava uusi, jos haluat vaihtaa henkilöitä.

## Työskentely yhteensopivuustietojen kanssa Gramps Desktopissa

DNA-yhteensopivuustiedot tallennetaan muistiin Gramps-tietokannassa. Muoto on yhteensopiva 
[DNA Segment Map Addon](https://gramps-project.org/wiki/index.php/Addon:DNASegmentMapGramplet)
saatavilla Gramps Desktopille. Sen wiki-sivulla on lisätietoja siitä, miten tiedot saadaan, miten niitä tulkitaan ja miten tiedot syötetään Grampsiin.

!!! info
    Gramps Web API v2.8.0 toi mukanaan muutoksia, jotta se hyväksyy laajemman valikoiman raakadataa DNA-yhteensopivuuksista, jota ei vielä ole saatavilla Gramps Desktop -lisäosassa. Gramps Desktop -lisäosaa päivitetään tulevaisuudessa tukemaan samoja muotoja.
