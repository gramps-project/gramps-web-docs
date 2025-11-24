# Gramps Webin käyttäminen Y-DNA-analyysiin

!!! note "Huomautus"
    Tämä ominaisuus vaatii Gramps Web API -version 3.3.0 tai uudemman ja Gramps Web -frontend-version 25.9.0 tai uudemman.

Gramps Webin Y-DNA-näkymä voi käyttää raakadataa Y-kromosomin yksittäisistä nukleotidipolymorfismeista (SNP) määrittääkseen henkilön todennäköisimmän Y-DNA-haplogruunun ja näyttää periytyneet esi-isät ihmisen Y-kromosomipuussa aikahaarukoineen.

## Kuinka hankkia ja tallentaa Y-DNA SNP -data

Hankkiaksesi Y-DNA SNP -datan, sinun on suoritettava Y-DNA-testi geneettisen testauspalvelun kautta. Tulos esitetään mutaatioiden (SNP) joukkona, joista kukin on tunnistettu merkkijonolla (esim. `R-BY44535`) ja `+` tai `-` merkki, joka osoittaa, onko mutaatio läsnä vai poissa. Gramps Web odottaa kaikkien testattujen SNP:iden merkkijonoa muodossa `SNP1+, SNP2-, SNP3+,...`, joka tallennetaan henkilön mukautetun tyypin `Y-DNA` (kirjainten koko on merkityksellinen) attribuuttiin. Voit joko luoda tämän attribuutin manuaalisesti Gramps Webissä tai Gramps Desktopissa, tai siirtyä Y-DNA-näkymään Gramps Webissä ja napsauttaa sinistä "Lisää" -painiketta, valita henkilön, jolle tiedot lisätään, ja liittää SNP-merkkijono. Joka tapauksessa tiedot tallennetaan henkilön attribuuttina Gramps-tietokantaasi.

[Katso alla](#instructions-for-obtaining-snp-data-from-testing-services) ohjeet siitä, kuinka hankkia SNP-data eri testauspalveluista.

## Kuinka se toimii

Kun henkilöllä on `Y-DNA`-attribuutti, joka sisältää SNP-datan, Gramps Web käyttää avointa lähdekoodia [yclade](https://github.com/DavidMStraub/yclade) Python-kirjastoa määrittääkseen henkilön todennäköisimmän sijainnin ihmisen Y-kromosomipuussa. Puu on luotu [YFull](https://www.yfull.com/) -projektin toimesta kymmenien tuhansien Y-DNA-testien perusteella. Huomaa, että Gramps Web käyttää paikallista kopiota YFull-puusta, joten tietoja ei lähetetä kolmansille osapuolille.

Puu kuljetaan juuresta lehtiin, ja jokaisessa solmussa verrataan kyseiseen solmuun liittyviä SNP:itä henkilön positiivisesti ja negatiivisesti testattuihin SNP:ihin, ja asianmukaista haaraa seurataan.

Lopullinen tulos on kladien peräkkäisyys puun juuresta (Y-kromosomaalinen "Adam" [Adam](https://en.wikipedia.org/wiki/Y-chromosomal_Adam)) kaikkein kehittyneimpään kladiin, joka on johdonmukainen henkilön SNP-datan kanssa. Jokaisella kladilla on arvioitu ikä, joka perustuu YFull-tietokannan näytteiden ikään, jotka kuuluvat kyseiseen kladiin.

Koska Y-kromosomit periytyvät isältä pojalle, tämä peräkkäisyys vastaa henkilön patrilineaarista esi-isyyttä.

## Kuinka tulkita tuloksia

Tärkein tieto on henkilön todennäköisin haplogruunu, joka näkyy sivun yläosassa. Nimi on linkitetty vastaavalle sivulle [YFull](https://www.yfull.com/) -verkkosivustolla, joka sisältää lisätietoja, kuten testattujen näytteiden alkuperämaan, jotka kuuluvat kyseiseen haplogruunuun.

Gramps Webissä näkyvässä patrilineaarisessa esi-isäpuussa testatun henkilön yläpuolella oleva laatikko on kaikkien testattujen näytteiden viimeisin yhteinen esi-isä (MRCA), jotka kuuluvat henkilön haplogruunuun. Tälle esi-isälle näytettävä päivämäärä on hänen arvioitu syntymäaikansa. Hänen yläpuolellaan oleva esi-isä on se esi-isä, jossa tämä haplogruunia määrittävä mutaatio ilmestyi ensimmäisen kerran.

Y-kromosomien hitaasta mutaatiovauhdista johtuen MRCA voi olla useita satoja vuosia menneisyydessä. Harvinaisille haplogruunoille (ts. haplogruunoille, joista vain harvoja ihmisiä on testattu tähän mennessä) se voi olla jopa tuhansia vuosia.

## Ohjeet SNP-datan hankkimiseen testauspalveluista

### [YSEQ](https://www.yseq.net/)

Kun olet kirjautunut "Oma tili" -osioon, siirry kohtaan "Omat tulokset / Näytä alleelit" ja siirry sivun alaosaan. Tekstikenttä "Alleelilista tiivistetty" on lisätty erityisesti Gramps Webiä varten ja se on juuri oikeassa muodossa liitettäväksi `Y-DNA`-attribuuttiin.
