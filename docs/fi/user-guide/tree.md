# Sukupuu

Sukupuu-sivu on saatavilla sivupalkista ja se näyttää interaktiivisia kaavioita valitun henkilön ympärillä. Viisi kaaviotyyppiä on saatavilla sivun yläreunassa olevien välilehtien kautta.

## Aloittavan henkilön valitseminen

Kaikki kaaviot alkavat puussa tällä hetkellä valitusta henkilöstä (näkyy työkalupalkissa). Tällä hetkellä keskiössä oleva henkilö on korostettu varjostuksella. Käytä **Aloitus henkilö** -painiketta palataksesi kotiin henkilöön tai **Takaisin** -painiketta palataksesi aikaisemmin katsottuun henkilöön. Napsauttamalla henkilön korttia missä tahansa kaaviossa keskitetään kaavio uudelleen tälle henkilölle.

Jos koti henkilöä ei ole asetettu, sivu tarjoaa **Aseta koti henkilö** -painikkeen, jonka avulla voit etsiä ja valita yhden suoraan. Jos puussa ei vielä ole henkilöitä, Editor-roolin tai korkeamman tason käyttäjät näkevät sen sijaan **Uusi henkilö** -painikkeen – ensimmäinen henkilö, joka luodaan tyhjään puuhun, tulee automaattisesti koti henkilöksesi, joten kaavio näytetään heti.

## Kaaviotyypit

### Esivanhempien puu

Sukupuu-kaavio, joka näyttää valitun henkilön esivanhemmat. Vanhemmat näkyvät vasemmalla (tai oikealla, riippuen asettelusta), isovanhemmat kauempana ja niin edelleen.

### Jälkeläisten puu

Näyttää valitun henkilön jälkeläiset – lapset, lapsenlapset ja niin edelleen.

### Tiimalasikaavio

Yhdistää esivanhemmat valitun henkilön ylle ja jälkeläiset alle yhteen näkymään.

### Sukulaisuuskaavio

Näyttää sukulaisuussuhteen kahden henkilön välillä. Valittu henkilö on yksi päätepiste; napsauta mitä tahansa muuta henkilöä kaaviossa asettaaksesi toisen päätepisteen ja näyttääksesi lyhyimmän sukulaisuussuhteen heidän välillään.

Jokainen pari on yhdistetty pienellä perhesolmulla kahden kumppanin väliin. Vie hiiri sen päälle tai napsauta tai napauta sitä nähdäksesi perheen tiedot – kuten avioliitto päivämäärä ja paikka sekä lapset – poistumatta kaaviosta. **Avaa** -painike esikatselussa vie perhesivulle. Avioliitossa olevien parien solmulla on katkoviiva.

!!! huomautus
    Sama henkilö voi esiintyä useammin kuin kerran kaaviossa – esimerkiksi kun joku on ollut naimisissa useita kertoja ja esiintyy useissa perhe-yksiköissä polulla. Tämä on tarkoituksellista, ei virhe.

### Tuulikaarikaavio

Pyöreä sukupuu-kaavio. Esivanhemmat säteilevät ulospäin valitun henkilön ympäriltä keskellä.

Työkalupalkin **Väri** -painike värittää segmentit kunkin henkilön ominaisuuden mukaan: tapahtumien tai muistiinpanojen määrä, syntymävuosi, kuolinvuosi, ikä, sukunimi, uskonto tai esivanhempien esiintymistiheys (kuinka usein henkilö esiintyy kaaviossa). Sukunimen mukaan värittäminen käyttää henkilön syntymänimeä tai ensisijaista nimeä, jos syntymänimeä ei ole. Poistaaksesi värittämisen, tyhjennä valitun värin näyttävä siru.

## Siirtyminen sukulaisiin ja oksien laajentaminen

Esivanhempien puussa ja tuulikaarikaaviossa valitulla henkilöllä on nuolipainike, joka avaa heidän lastensa valikon. Jälkeläisten puussa se avaa sen sijaan heidän vanhempiensa valikon. Valitsemalla henkilön valikosta keskitetään kaavio heihin.

Esivanhempien puussa, jälkeläisten puussa ja tiimalasikaaviossa kaavion reunoilla olevilla henkilöillä, joiden vanhempia tai lapsia ei näytetä, on nuoli sivulla, josta heidän oksansa jatkuu. Napsauttamalla sitä lisätään yksi sukupolvi tuohon oksaan, kun valittu henkilö pysyy samana. Tällä tavalla voit esimerkiksi tarkastella kaikkia isovanhempia ja sitten seurata vain yhtä linjaa taaksepäin. Laajennettu oksat palautetaan, kun valitset toisen henkilön tai vaihdat toiseen kaavioon.

## Navigointikontrollit

Kaikki kaaviotyypit jakavat työkalupalkin seuraavilla painikkeilla:

- **Aloitus henkilö** – palaa koti henkilöön
- **Takaisin** – palaa aikaisemmin keskitettyyn henkilöön
- **Henkilön tiedot** – avaa tällä hetkellä keskitetyn henkilön täydellinen profiilisivu
- **Asetukset** – avaa dialogin kaaviokohtaisia näyttöasetuksia varten (katso alla)

Kaikki kaaviot tukevat **pan** (napsauta ja vedä) ja **zoom** (vierityspyörä tai nipistys).

## Kaavioasetukset

**Asetukset**-dialogi (rataskuvake työkalupalkissa) antaa sinun säätää seuraavia vaihtoehtoja kaaviotyypistä riippuen:

- **Maksimi esivanhempien sukupolvet** – kuinka monta sukupolvea esivanhempia näytetään
- **Maksimi jälkeläisten sukupolvet** – kuinka monta sukupolvea jälkeläisiä näytetään
- **Maksimi erottelun aste** – sukulaisuuskaaviolle, maksimipituus polulle, jota etsitään. Korkeat arvot voivat tehdä kaaviosta hitaasti latautuvan suurilla puilla.
- **Maksimi näytettävien kuvien määrä** – rajoittaa kaaviossa näytettäviä profiilikuvia suorituskyvyn vuoksi
- **Nimen näyttömuoto** – ohjaa, miten nimet näytetään henkilöiden korteilla

Napsauta **Nollaa** palauttaaksesi oletusasetukset tai **Sulje** ottaaksesi muutoksesi käyttöön.

Kaavioasetusten asetukset tallennetaan selaimen paikalliseen tallennustilaan, joten ne säilyvät istuntojen välillä samalla laitteella.

## Oletuskaaviotyyppi

Kaaviotyyppi, joka näytetään, kun avaat Sukupuu-sivun ensimmäisen kerran, voidaan määrittää [Käyttäjäasetuksissa](settings.md). Valitsemasi oletus koskee kaikkia laitteitasi.

## Puun muokkaaminen

Editor-roolin tai korkeamman tason käyttäjät voivat lisätä ja liittää henkilöitä suoraan esivanhempien puusta. Katso [Perheen puun muokkaaminen](tree-edit.md) lisätietoja varten.
