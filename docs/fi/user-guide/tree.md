# Sukupuu

Sukupuu-sivu on saatavilla sivupalkista ja se näyttää interaktiivisia kaavioita valitun henkilön ympärillä. Viisi kaaviotyyppiä on saatavilla ylhäällä olevien välilehtien kautta.

## Aloittavan henkilön valitseminen

Kaikki kaaviot alkavat puussa tällä hetkellä valitusta henkilöstä (näkyy työkalupalkissa). Tällä hetkellä keskitetty henkilö on korostettu varjoefektillä. Käytä **Aloitus henkilö** -painiketta palataksesi kotiin, tai **Takaisin** -painiketta palataksesi aiemmin katsottuun henkilöön. Napsauttamalla henkilön korttia missä tahansa kaaviossa keskitetään kaavio uudelleen tälle henkilölle.

Jos kotihenkilöä ei ole asetettu, sivu tarjoaa **Aseta kotihenkilö** -painikkeen, jonka avulla voit etsiä ja valita yhden suoraan. Jos puussa ei vielä ole henkilöitä, Editor-roolin tai sitä korkeamman roolin omaavat käyttäjät näkevät sen sijaan **Uusi henkilö** -painikkeen – ensimmäinen tyhjään puuhun luotu henkilö tulee automaattisesti kotihenkilöksesi, joten kaavio näytetään heti.

## Kaaviotyypit

### Esivanhempien puu

Sukupuu, joka näyttää valitun henkilön esivanhemmat. Vanhemmat näkyvät vasemmalla (tai oikealla, riippuen asettelusta), isovanhemmat kauempana ja niin edelleen.

### Jälkeläisten puu

Näyttää valitun henkilön jälkeläiset – lapset, lastenlapset ja niin edelleen.

### Tiimalasikaavio

Yhdistää esivanhemmat ylhäällä ja jälkeläiset alhaalla valitun henkilön ympärille yhteen näkymään.

### Suhdekaavio

Näyttää suhdepolun kahden henkilön välillä. Valittu henkilö on yksi päätepiste; napsauta mitä tahansa muuta henkilöä kaaviossa asettaaksesi toisen päätepisteen ja näyttääksesi lyhyimmän suhdepolun heidän välillään.

!!! note
    Sama henkilö voi esiintyä useammin kuin kerran kaaviossa – esimerkiksi silloin, kun joku on ollut naimisissa useita kertoja ja esiintyy useissa perhe-yksiköissä polun varrella. Tämä on tarkoituksellista, ei virhe.

### Tuulikaarikaavio

Pyöreä sukupuu. Esivanhemmat säteilevät ulospäin valitusta henkilöstä keskellä.

Työkalupalkin **Väri** -painike värittää segmentit kunkin henkilön ominaisuuden mukaan: tapahtumien tai muistiinpanojen määrä, syntymävuosi, kuolinvuosi, ikä, sukunimi, uskonto tai esivanhempien esiintymistiheys (kuinka usein henkilö esiintyy kaaviossa). Sukunimen mukaan värittäminen käyttää henkilön syntymänimeä tai ensisijaista nimeä, jos syntymänimeä ei ole. Poistaaksesi värittämisen, tyhjennä valitun värin näyttävä siru.

## Liikkuminen sukulaisiin ja oksien laajentaminen

Esivanhempien puussa ja tuulikaarikaaviossa valitulla henkilöllä on nuolipainike, joka avaa valikon heidän lapsistaan. Jälkeläisten puussa se avaa valikon heidän vanhemmistaan sen sijaan. Valitsemalla henkilön valikosta keskitetään kaavio heihin.

Esivanhempien puussa, jälkeläisten puussa ja tiimalasikaaviossa kaavion reunoilla olevilla henkilöillä, joiden vanhempia tai lapsia ei näytetä, on nuoli sivulla, josta heidän oksansa jatkuu. Napsauttamalla sitä lisätään yksi sukupolvi lisää kyseiseen oksaan, kun valittu henkilö pysyy samana. Tällä tavalla voit esimerkiksi tarkastella kaikkia isovanhempia ja sitten seurata vain yhtä linjaa taaksepäin. Laajennetut oksat palautuvat oletusarvoon, kun valitset toisen henkilön tai vaihdat toiseen kaavioon.

## Navigointiohjaimet

Kaikki kaaviotyypit jakavat työkalupalkin seuraavilla painikkeilla:

- **Aloitus henkilö** – hyppää takaisin kotiin
- **Takaisin** – palaa aiemmin keskitettyyn henkilöön
- **Henkilötiedot** – avaa nykyisen keskitetyn henkilön täydellinen profiilisivu
- **Asetukset** – avaa dialogin kaaviokohtaisia näyttöasetuksia varten (katso alla)

Kaikki kaaviot tukevat **pan** (napsauta ja vedä) ja **zoom** (rullauspyörä tai nipistys).

## Kaavioasetukset

**Asetukset**-dialogi (rataskuvake työkalupalkissa) antaa sinun säätää seuraavia vaihtoehtoja kaaviotyypistä riippuen:

- **Maksimi esivanhempien sukupolvet** – kuinka monta sukupolvea esivanhempia näytetään
- **Maksimi jälkeläisten sukupolvet** – kuinka monta sukupolvea jälkeläisiä näytetään
- **Maksimi erottelun aste** – suhdekaaviossa, suurin polun pituus, jota etsitään, enintään 6
- **Maksimi näytettävien kuvien määrä** – rajoittaa kaaviossa näytettävien profiilivalokuvien määrää suorituskyvyn vuoksi
- **Nimen näyttömuoto** – ohjaa, miten nimet näytetään henkilökorteissa

Napsauta **Palauta** palauttaaksesi oletusasetukset tai **Sulje** soveltaaksesi muutoksiasi.

Kaavioasetusten asetukset tallennetaan selaimen paikalliseen tallennustilaan, joten ne säilyvät istuntojen välillä samalla laitteella.

## Oletuskaaviotyyppi

Kaaviotyyppi, joka näytetään, kun avaat Sukupuu-sivun ensimmäisen kerran, voidaan määrittää [Käyttäjäasetuksissa](settings.md). Valitsemasi oletus koskee kaikkia laitteitasi.

## Puun muokkaaminen

Editor-roolin tai sitä korkeamman roolin omaavat käyttäjät voivat lisätä ja linkittää henkilöitä suoraan esivanhempien puusta. Katso [Sukupuun muokkaaminen](tree-edit.md) lisätietoja varten.
