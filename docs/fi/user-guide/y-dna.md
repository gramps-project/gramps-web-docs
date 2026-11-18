# Gramps Webin käyttö Y-DNA-analyysissä

!!! note "Huomautus"
    Tämä ominaisuus vaatii Gramps Web API -version 3.3.0 tai uudemman ja Gramps Web -frontend-version 25.9.0 tai uudemman.

Gramps Webin Y-DNA-näkymä voi käyttää raakadataa Y-kromosomin yksittäisistä nukleotidipolymorfismeista (SNP) määrittääkseen henkilön todennäköisimmän Y-DNA-haplogrupi ja näyttää johdetut esi-isät ihmisen Y-kromosomipuussa aikahaarukoiden kanssa.

## Kuinka hankkia ja tallentaa Y-DNA SNP -data

Hankkiaksesi Y-DNA SNP -datan, sinun on suoritettava Y-DNA-testi geenitestipalvelun kautta. Tulos esitetään mutaatioiden (SNP) joukkona, joista kukin on tunnistettu merkkijonolla (esim. `R-BY44535`) ja `+` tai `-` -merkillä, joka osoittaa, onko mutaatio läsnä vai poissa. Gramps Web odottaa kaikkien testattujen SNP:iden merkkijonoa muodossa `SNP1+, SNP2-, SNP3+,...`, joka tallennetaan henkilön attribuuttina mukautetulla tyypillä `Y-DNA` (isot ja pienet kirjaimet huomioiden). Voit joko luoda tämän attribuutin manuaalisesti Gramps Webissä tai Gramps Desktopissa tai siirtyä Y-DNA-näkymään Gramps Webissä ja napsauttaa sinistä "Lisää" -painiketta, valita henkilön, johon tiedot lisätään, ja liittää SNP-merkkijonon. Joka tapauksessa tiedot tallennetaan henkilön attribuuttina Gramps-tietokantaasi.

[Katso alla](#instructions-for-obtaining-snp-data-from-testing-services) ohjeet siitä, kuinka hankkia SNP-data eri testauspalveluista.

## Kuinka se toimii

Kun henkilöllä on `Y-DNA`-attribuutti, joka sisältää SNP-datan, Gramps Web käyttää avointa lähdekoodia [yclade](https://github.com/DavidMStraub/yclade) Python-kirjastoa määrittääkseen henkilön todennäköisen sijainnin ihmisen Y-kromosomipuussa. Puu on luotu [YFull](https://www.yfull.com/) -projektin toimesta kymmenien tuhansien Y-DNA-testien perusteella. Huomaa, että Gramps Web käyttää paikallista kopiota YFull-puusta, joten mitään tietoja ei lähetetä kolmansille osapuolille.

Puu kuljetaan juuresta lehtiin, ja jokaisessa solmussa verrataan siihen liittyviä SNP:itä henkilön positiivisesti ja negatiivisesti testattuihin SNP:ihin, ja asianmukaista haaraa seurataan.

Lopullinen tulos on kladien peräkkäisyys puun juuresta (Y-kromosomaalinen "Adam" [Y-chromosomal "Adam"](https://en.wikipedia.org/wiki/Y-chromosomal_Adam)) kaikkein johdetuimpaan kladiin, joka on yhdenmukainen henkilön SNP-datan kanssa. Jokaisella kladilla on arvioitu ikä, joka perustuu YFull-tietokannan näytteiden ikään, jotka kuuluvat kyseiseen kladiin.

Koska Y-kromosomit periytyvät isältä pojalle, tämä peräkkäisyys vastaa otetta henkilön patrilineaarisesta sukupuusta.

## Kuinka tulkita tuloksia

Tärkein tieto on henkilön todennäköisin haplogruppi, joka näkyy sivun yläosassa. Nimi on linkitetty vastaavalle sivulle [YFull](https://www.yfull.com/) -verkkosivustolla, joka sisältää lisätietoja, kuten testattujen näytteiden alkuperämaan, jotka kuuluvat kyseiseen haplogrupiin.

Gramps Webissä näkyvässä patrilineaarisessa esi-isäpuussa testatun henkilön yläpuolella oleva laatikko on kaikkien testattujen näytteiden viimeisin yhteinen esi-isä (MRCA), jotka kuuluvat henkilön haplogrupiin. Tälle esi-isälle näytettävä päivämäärä on hänen arvioitu syntymäaikansa. Hänen yläpuolellaan oleva esi-isä on se esi-isä, jossa tämä haplogruppia määrittävä mutaatio ilmestyi ensimmäisen kerran.

Y-kromosomien hitaasta mutaatiotahtista johtuen MRCA voi olla monia satoja vuosia menneisyydessä. Harvinaisten haplogruppejen (eli haplogruppejen, joissa vain muutama henkilö on testattu tähän mennessä) kohdalla se voi olla jopa tuhansia vuosia.

MRCA:n ja testatun henkilön välillä kaavio näyttää isälinjan niin pitkälle kuin se on dokumentoitu puussasi: isä, hänen isänsä ja niin edelleen, vanhin ensin. Viivan yläpuolella oleva katkoviiva vanhimman dokumentoidun esi-isän kohdalla tarkoittaa sukupolvia, joita ei ole dokumentoitu, arvioidulla määrällä. Vain biologisia isiä seurataan – viiva pysähtyy adoptiovanhemman tai isäpuolen kohdalla, koska he eivät siirtäneet Y-kromosomia. Napsauta henkilöä viivalla avataksesi heidän sivunsa.

Jokaisen kladilaatikon kuvake avaa kyseisen kladin YFull-verkkosivustolla.

## Y-DNA-datan yksityisyys

Y-DNA-datan lisäämiseen ja muokkaamiseen tarkoitetuissa dialogeissa on **Yksityinen** kytkin. Yksityiset Y-DNA-tiedot ovat piilossa käyttäjiltä, jotka eivät voi nähdä yksityisiä tietueita. Katso [Yksityiset tietueet](privacy.md).

## Ohjeet SNP-datan hankkimiseksi testauspalveluista

### [YSEQ](https://www.yseq.net/)

Kun olet kirjautunut sisään "Oma tili", siirry kohtaan "Tulokseni / Näytä alleelit" ja siirry sivun alaosaan. Tekstikenttä "Alleelilista tiivistetty" on lisätty erityisesti Gramps Webiä varten ja se on juuri oikeassa muodossa liitettäväksi `Y-DNA`-attribuuttiin.
