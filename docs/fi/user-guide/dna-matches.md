# Työskentely DNA-yhteensopivuuksien kanssa

DNA-yhteensopivuudet ovat DNA-segmenttejä, jotka ovat samat kahden henkilön välillä, ja ne tunnistetaan merkkien, niin kutsuttujen SNP:iden (yksittäisten nukleotidipolyformismien, ääntämys "snips") avulla.

Tämän tiedon saamiseksi tarvitset pääsyn DNA-testiin, joka on ladattu yhteensopivuustietokantaan, joka mahdollistaa DNA-segmenttien yhteensopivuustietojen tarkastelun (esim. MyHeritage, Gedmatch, FamilytreeDNA). Gramps Web ei itse suorita yhteensopivuutta, sillä sillä on vain pääsy ladattuihin tietoihin.

## DNA-yhteensopivuustietojen syöttäminen

Syöttääksesi DNA-yhteensopivuustietoja, tarvitset [muokkausoikeudet](../install_setup/users.md), sillä tiedot tallennetaan muistiin Gramps-tietokannassa. DNA-näkymä, johon pääsee päävalikosta, tarjoaa kätevän tavan syöttää nämä tiedot oikeassa muodossa.

Syöttääksesi uuden yhteensopivuuden, napsauta + -painiketta oikeassa alakulmassa. Avautuvassa valintaikkunassa valitse kaksi henkilöä. Huomaa, että "Ensimmäistä henkilöä" ja "Toista henkilöä" käsitellään eri tavalla: yhteensopivuus tallennetaan assosiaationa ensimmäisestä toiselle henkilölle. Vain ensimmäinen henkilö on valittavissa DNA-yhteensopivuusnäkymässä ja kromosomiselain. Tyypillisesti ensimmäinen henkilö on se, jonka DNA-testiin sinulla on pääsy, ja toinen henkilö on kaukaisempi sukulainen.

Jos toista henkilöä ei ole tietokannassa, sinun on ensin luotava se käyttämällä "Luo henkilö" -painiketta käyttöliittymän oikeassa yläkulmassa. Kun olet luonut henkilön, voit palata DNA-yhteensopivuusnäkymään ja valita juuri luodun henkilön.

Seuraavaksi liitä raakadata tekstikenttään. Datan tulisi olla pilkulla tai tabilla eroteltu taulukko yhteensopivuuksista, joka tyypillisesti sisältää kromosomin numeron, yhteensopivuuden aloitus- ja lopetuspaikan, yhteensopivuuden SNP:iden määrän ja yhteensopivuuden pituuden sentimorganien (cM) yksiköissä. Voit myös raahata ja pudottaa tiedoston, jossa on yhteensopivuustiedot, tekstikenttään.

Minimalistinen esimerkki tällaisesta taulukosta on:

```csv
Kromosomi,Aloituspaikka,Lopetuspaikka,Sentimorganit,SNP:t
6,6358001,18115715,19.6,7424
7,150135758,154205894,10.9,2816
```

Jos muoto on voimassa, esikatselu näytetään tekstikentän alapuolella taulukkona.

Lopuksi napsauta "Tallenna" -painiketta tallentaaksesi yhteensopivuuden tietokantaan.

## DNA-yhteensopivuustietojen tarkastelu

DNA-yhteensopivuusnäkymässä on avattava valikko, joka mahdollistaa jokaisen tietokannassa olevan henkilön valitsemisen, jolla on liittyvä DNA-yhteensopivuus. Kun henkilö on valittu, heidän yhteensopivuutensa luetellaan taulukossa: yhteensopivuuden nimi, heidän suhteensa valittuun henkilöön, jaettu DNA:n kokonaispituus sentimorganina (cM), ja jaettujen segmenttien määrä sekä suurimman näistä segmenteistä pituus.

Yhteensopivuuksille, jotka on jo sijoitettu puuhun, suhde-sarake näyttää puussa tallennetun suhteen (automaattisesti määritetty Gramps-tietokannasta). Yhteensopivuuksille, jotka eivät ole sukua valitulle henkilölle puussa, se näyttää suhteen, joka on arvioitu jaetun DNA:n perusteella, merkitty "≈".

Napsauttamalla yhteensopivuutta avataan sen sivu, jossa on yhteenveto jaetusta DNA:sta, [suhteen arvio](#relationship-estimate), kaavio suhteesta puussa ja segmenttiluettelo. Jokainen segmentti näyttää, onko se isän vai äidin puolella. Puoli voidaan joko syöttää manuaalisesti (antamalla `P` isän puolelle tai `M` äidin puolelle sarakkeeseen nimeltä `Puoli` raakadatassa) tai määrittää automaattisesti viimeisimmän yhteisen esi-isän perusteella. Segmenttien vieressä oleva latauspainike tallentaa ne CSV-tiedostona muodossa, jonka yhteensopivuusdialogi hyväksyy.

## Suhteen arvio

Jaettu DNA ei ole todiste tietystä suhteesta: kahden sukulaisen jakaman DNA:n määrä vaihtelee paljon, ja eri suhteet limittyvät. Gramps Web näyttää siksi joukon mahdollisia suhteita niiden todennäköisyyksineen, jotka on laskettu jaettujen segmenttien määrän ja pituuden perusteella (vaatii Gramps Web API 3.26 tai uudemman).

Suhteet on ryhmitelty niiden *asteen* mukaan:

- **Vanhempi tai lapsi** ja **Täysveli** näytetään omana ryhmänään.
- **Sukulainen asteen 2** sisältää puolisisarukset, isovanhemmat ja lastenlapset sekä tädit, sedät, serkut ja veljenpojat.
- **Sukulainen asteen 3** sisältää ensimmäiset serkut, iso-isovanhemmat, iso-tädit ja iso-sedät sekä puolitädit ja -sedät.
- Jokainen seuraava aste on noin yhden sukupolven verran kauempana, esim. ensimmäiset serkut, jotka on poistettu kerran, ovat asteen 4 ja toiset serkut ovat asteen 5. Asteet 9 ja yli ryhmitellään "9+".

Suhteet, joilla on sama aste, jakavat keskimäärin suunnilleen saman määrän DNA:ta, joten pelkkä DNA ei voi erottaa niitä toisistaan. Käytä ihmisten ikää päätöksenteossa – 30-vuotias asteen 2 sukulainen 60-vuotiaasta on todennäköisemmin sisarentytär kuin isovanhempi.

Arvio on luotettavin läheisille sukulaisille. Kaukaisissa suhteissa yhteensopivuudet jakavat vain muutaman segmentin, ja todennäköisyydet jakautuvat useisiin asteisiin.

### Puun tarkistaminen DNA:n perusteella

Jos yhteensopivuus on sijoitettu puuhun, Gramps Web tarkistaa, sopiiko jaettu DNA siellä tallennettuun suhteeseen. Jos DNA on erittäin epätodennäköistä kyseiselle suhteelle, varoitusikoni näytetään yhteensopivuustaulukossa ja varoitus yhteensopivuussivulla. Sulkujen sisällä oleva numero, esim. "1 : 500", vertaa kuinka todennäköistä DNA on tallennetulle suhteelle verrattuna siihen, kuinka todennäköistä se on todennäköisimmälle suhteelle.

Varoitus on syy tarkastella tarkemmin, ei todiste virheestä. Yleisiä syitä ovat:

- virhe puussa, kuten väärä vanhempi,
- väärin määritetty vanhemmuus, esim. tuntematon adoptointi tai eri biologinen isä,
- puutteelliset yhteensopivuustiedot, esimerkiksi jos vain korkeimman kynnyksen ylittäviä segmenttejä on kopioitu testauspalvelusta,
- suhteet useamman kuin yhden linjan kautta, esim. ihmiset, jotka ovat sukua sekä äidin että isän kautta ("sukupuuromahdus"), jotka jakavat enemmän DNA:ta kuin odotettiin.

Suhteita, jotka eivät ole syntyperäisiä, kuten adoptoinnin kautta, ei tarkisteta.

## Yhteensopivuuden muokkaaminen

Muokataksesi yhteensopivuutta, avaa sen sivu ja napsauta muokkauspainiketta tai paina `e`. Huomaa, että voit muuttaa raakadataa, mutta et yhteensopivuuteen liittyviä henkilöitä – sinun on poistettava yhteensopivuus ja luotava uusi, jos haluat muuttaa henkilöitä.

## Yksityiset yhteensopivuudet

Yhteensopivuuden lisäämiseen ja muokkaamiseen tarkoitetuissa valintaikkunoissa on **Yksityinen** kytkin. Yksityinen yhteensopivuus, mukaan lukien sen segmentit, on piilotettu käyttäjiltä, jotka eivät voi nähdä yksityisiä tietoja. Yksityiset yhteensopivuudet on merkitty lukolla kaikille muille. Katso [Yksityiset tiedot](privacy.md) lisätietoja yksityisyydestä.

## Työskentely yhteensopivuustietojen kanssa Gramps Desktopissa

DNA-yhteensopivuustiedot tallennetaan muistiin Gramps-tietokannassa. Muoto on yhteensopiva 
[DNA Segment Map -lisäosan](https://gramps-project.org/wiki/index.php/Addon:DNASegmentMapGramplet)
kanssa, joka on saatavilla Gramps Desktopille. Sen wiki-sivulla on lisätietoja siitä, miten tiedot hankitaan, miten niitä tulkitaan ja miten tiedot syötetään Grampsiin.

!!! info
    Gramps Web API v2.8.0 toi mukanaan muutoksia, jotka hyväksyvät laajemman valikoiman raakadataa DNA-yhteensopivuuksista, mikä ei ole vielä saatavilla Gramps Desktop -lisäosassa. Gramps Desktop -lisäosa päivitetään tulevaisuudessa tukemaan samoja muotoja.
