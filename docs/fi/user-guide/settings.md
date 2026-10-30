# Käyttäjäasetukset

Käyttäjäasetukset ovat saatavilla käyttäjäkuvakkeen kautta ylävalikkopalkissa, sitten **Käyttäjäasetukset**. Sivusto on järjestetty laajennettaviin osioihin. Muutokset astuvat voimaan heti, ellei toisin mainita.

!!! note
    Muutokset käyttäjäasetuksissa vaikuttavat vain omaan tiliisi. Asetuksia, jotka vaikuttavat kaikkiin puun käyttäjiin, hallitaan [Hallinta-asetuksissa](../administration/settings.md).

## Tili

Katsoo profiilitietojasi, tunnistetietojasi ja tilin turvallisuutta.

### Käyttäjätiedot

Näyttää **käyttäjänimesi** ja nykyisen **käyttäjäroolisi** (esim. Vieraana, Jäsenenä, Toimittajana). Nämä ovat vain lukuoikeudella.

### Vaihda sähköposti

Syötä uusi sähköpostiosoite ja napsauta **Lähetä** päivittääksesi tilisi liitetyn osoitteen. Sähköpostiosoitetta käytetään salasanan palautuksiin ja (jos määritetty) ilmoituksiin.

### Vaihda salasana

Syötä nykyinen salasanasi ja uusi salasana, ja napsauta sitten **Lähetä**. Jos olet unohtanut nykyisen salasanasi, käytä **Unohditko salasanan** -linkkiä kirjautumissivulla sen sijaan.

### Liitetyt kirjautumistavat

Jos palvelimesi tarjoaa kertakirjautumisen (katso [OIDC-todennus](../install_setup/oidc.md)), voit liittää tilin palveluntarjoajalta, kuten Googlelta tai organisaatiosi kirjautumiselta, Gramps Web -tiliisi. Voit sitten kirjautua sisään kyseisen palveluntarjoajan kautta ja siirtyä olemassa olevaan tiliisi, roolisi ja muokkauksesi kanssa. Tämä osio näkyy vain, kun kertakirjautuminen on käytössä ja palvelin tukee liittämistä (Gramps Web API 3.24 ja uudemmat).

Liittääksesi tilin, napsauta **Liitä** ja palveluntarjoajan nimeä, kirjaudu sisään palveluntarjoajalle, ja sinut ohjataan takaisin asetuksiisi. Jos et ole kirjautunut sisään äskettäin, sinua pyydetään kirjautumaan sisään uudelleen ensin.

Palveluntarjoajan tili voidaan liittää vain yhteen Gramps Web -tiliin. Jos näet "Tämä kirjautuminen on jo liitetty toiseen tiliin", se on liitetty muualle, esimerkiksi tiliin, joka luotiin, kun kirjauduit ensimmäisen kerran sisään kyseisen palveluntarjoajan kautta. Järjestelmänvalvoja voi poistaa tuon toisen tilin, jonka jälkeen voit liittää sen omaasi.

Poistaaksesi tilin liitännästä, napsauta **Poista liitos**. Jos se on viimeinen liitetty kirjautumistapasi, sinun on myös syötettävä salasana, jotta voit silti kirjautua sisään sen jälkeen. Jos tilisi on luotu kertakirjautumisen kautta etkä koskaan asettanut salasanaa, käytä **Unohditko salasanan** -linkkiä kirjautumissivulla asettaaksesi ensin salasanan (tämä vaatii palvelimen lähettämään sähköposteja). Jos palvelin sallii vain kirjautumisen palveluntarjoajan kautta, viimeistä liitettyä tiliä ei voi poistaa liitännästä.

## Ulkoasu

Hallinnoi laitteellasi tallennettuja näyttöasetuksia.

### Kieli

Valitse kieli Gramps Web -käyttöliittymälle. Kieli-asetus tallennetaan selaimen paikalliseen tallennustilaan ja se koskee vain nykyistä laitetta.

### Teema

Valitse seuraavista:

- **Järjestelmä** – seuraa käyttöjärjestelmän vaaleaa/tumma asetusta (oletus)
- **Vaalea** – käytä aina vaaleaa teemaa
- **Tumma** – käytä aina tummaa teemaa

Teema-asetus tallennetaan selaimen paikalliseen tallennustilaan.

### Sukupuuasetukset

#### Oletussukupuun näkymä

Määrittää, mikä kaaviotyyppi avautuu oletuksena, kun navigoit [Sukupuu](tree.md) -sivulle. Vaihtoehtoja ovat Esivanhempien puu, Jälkeläisten puu, Tiimalasikaavio, Suhdekaavio ja Tuulettimikaavio.

Tämä asetus tallennetaan selaimen paikalliseen tallennustilaan.

## Kehittäjätyökalut

### API-tunnus

Kopioi nykyinen istuntotunnuksesi leikepöydälle. Tunnusta voidaan käyttää todennukseen suoraan REST API:ta vastaan, esimerkiksi interaktiivisessa Swagger UI:ssa, joka on käytettävissä Gramps Web -instanssissasi osoitteessa `/api/swagger-ui`.

Napsauta **Aloita Swagger** avataksesi Swagger UI:n uudessa välilehdessä, jossa istuntosi on jo käytettävissä.

!!! note
    Istuntotunnus on lyhytikäinen. Kopioi se heti ennen kuin käytät sitä Swaggerissa, sillä se voi vanhentua.
