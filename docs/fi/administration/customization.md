# Mukauta puuta

Puun omistajat ja ylläpitäjät voivat mukauttaa puun nimeä ja ulkoasua sekä sen etusivua kaikille käyttäjille. Nämä asetukset löytyvät **Puun asetukset** ja **Mukautus** -osioista [Hallinta-asetuksissa](settings.md).

## Sukupuu nimi

!!! note
    Puun nimeäminen uudelleen toimii vain [monipuun asetuksessa](../install_setup/multi-tree.md) tai kun `TREE_ID` on nimenomaan asetettu [palvelimen kokoonpanossa](../install_setup/configuration.md). Oletusarvoisessa yksittäisessä puuasennuksessa ilman asetettua `TREE_ID`:tä tämä aiheuttaa virheen.

Tämä mahdollistaa taustalla olevan Gramps-sukupuutu tietokannan nimen muuttamisen. Syötä uusi nimi ja napsauta **Nimeä uudelleen** ottaaksesi muutoksen käyttöön.

!!! tip
    Jos haluat vain muuttaa sovelluspalkissa näkyvää nimeä ilman tietokannan nimeämistä uudelleen, käytä sen sijaan [Sovelluksen otsikko](#app-title) -asetusta.

## Tutkijan tiedot

Aseta pääasiallisen tutkijan nimi, osoite ja yhteystiedot. Nämä tiedot sisältyvät vientiin (esim. GEDCOM-tiedostot).

## Teeman värit

Aseta mukautettu **pääväri** ja **korostusväri** Gramps Web -käyttöliittymälle. Nämä värit sovelletaan kaikille tämän puun käyttäjille ja ne astuvat voimaan heti tallennuksen jälkeen.

Käytä värivalitsimia valitaksesi värit, ja napsauta sitten **Tallenna**. Napsauta **Palauta** palauttaaksesi oletusasetukset.

## Sovelluksen otsikko

Aseta mukautettu otsikko sovellukselle. Jos asetettu, tämä ohittaa sukupuun nimen selaimen otsikkopalkissa ja yläosassa.

Syötä otsikko ja napsauta **Tallenna**. Jätä tyhjäksi käyttääksesi oletusta (sukupuun nimi).

## Etusivun huomautus

Valitse Gramps **Huomautus** -objekti, joka näytetään ohjauspaneelin etusivulla. Huomautuksen sisältö näkyy pääohjauspaneelin sarakkeiden alla ja on näkyvissä kaikille käyttäjille, joilla on pääsy puuhun.

Käytä objektivalitsinta etsiäksesi ja valitaksesi huomautuksen, ja tallenna sitten. Napsauta **Poista** tyhjentääksesi nykyinen etusivun huomautus.

## Etusivun kuva

Valitse Gramps **Media** -objekti, joka näytetään kuvana ohjauspaneelin etusivulla. Kun se yhdistetään etusivun huomautukseen, kuva näkyy huomautustekstin vieressä. Ilman huomautusta näytetään vain kuva.

Käytä objektivalitsinta etsiäksesi ja valitaksesi mediaobjektin, ja tallenna sitten. Napsauta **Poista** tyhjentääksesi nykyinen etusivun kuva.

## Vienti/tuonti asetukset

Puun tason asetukset (sovelluksen otsikko, teeman värit, etusivun huomautus/kuva jne.) voidaan viedä JSON-tiedostona varmuuskopiota varten tai kopioitavaksi toiseen Gramps Web -instanssiin.

- Napsauta **Vie asetukset** ladataksesi nykyiset asetukset JSON-tiedostona.
- Napsauta **Tuo puun asetukset** ladataksesi aiemmin viedyn JSON-tiedoston ja ottaaksesi asetukset käyttöön.
