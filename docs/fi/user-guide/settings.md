# Käyttäjäasetukset

Käyttäjäasetukset ovat saatavilla käyttäjäkuvakkeen kautta sovelluksen yläreunassa, sitten **Käyttäjäasetukset**. Sivusto on järjestetty taitettaviin osioihin. Muutokset tulevat voimaan heti, ellei toisin mainita.

!!! note
    Muutokset käyttäjäasetuksissa vaikuttavat vain omaan tiliisi. Asetukset, jotka vaikuttavat kaikkiin puun käyttäjiin, hallitaan [Hallinta-asetuksissa](../administration/settings.md).

## Tili

Katsoo profiilitietojasi, tunnistetietojasi ja tilin turvallisuutta.

### Käyttäjätiedot

Näyttää **käyttäjänimesi** ja nykyisen **käyttäjäroolisi** (esim. Vieraana, Jäsenenä, Toimittajana). Nämä ovat vain luku -tilassa.

### Vaihda sähköposti

Syötä uusi sähköpostiosoite ja napsauta **Lähetä** päivittääksesi tilisi liitetyn osoitteen. Sähköpostiosoitetta käytetään salasanan palautuksiin ja (jos määritetty) ilmoituksiin.

### Vaihda salasana

Syötä nykyinen salasanasi ja uusi salasana, sitten napsauta **Lähetä**. Pysyt kirjautuneena nykyisellä laitteella, kun taas istuntosi muilla laitteilla ja selaimilla päättyvät 15 minuutin sisällä. Jos olet unohtanut nykyisen salasanasi, käytä **Unohditko salasanan** -linkkiä kirjautumissivulla sen sijaan.

Tämä osio on piilotettu, jos palvelin sallii kirjautumisen vain ulkoisen tarjoajan kautta (katso [OIDC-todennus](../install_setup/oidc.md)).

### Linkitetyt kirjautumistavat

Jos palvelimesi tarjoaa kertakirjautumisen (katso [OIDC-todennus](../install_setup/oidc.md)), voit linkittää tilin tarjoajalta, kuten Googlelta tai organisaatiosi kirjautumiselta, Gramps Web -tiliisi. Voit sitten kirjautua sisään kyseisen tarjoajan kautta ja siirtyä olemassa olevaan tiliisi, roolisi ja muokkauksesi kanssa. Tämä osio näkyy vain, kun kertakirjautuminen on käytössä ja palvelin tukee linkittämistä (Gramps Web API 3.24 ja uudemmat).

Linkittääksesi tilin, napsauta **Linkitä** ja tarjoajan nimeä, kirjaudu sisään tarjoajalla, ja sinut ohjataan takaisin asetuksiisi. Jos et ole kirjautunut sisään äskettäin, sinua pyydetään kirjautumaan sisään uudelleen ensin.

Tarjoajan tili voidaan linkittää vain yhteen Gramps Web -tiliin. Jos näet "Tämä kirjautuminen on jo linkitetty toiseen tiliin", se on linkitetty muualle, esimerkiksi tiliin, joka luotiin, kun kirjauduit ensimmäisen kerran sisään kyseisellä tarjoajalla. Järjestelmänvalvoja voi poistaa tuon toisen tilin, jonka jälkeen voit linkittää sen omaasi.

Poistaaksesi linkityksen, napsauta **Poista linkitys**. Jos se on viimeinen linkitetty kirjautumistapasi, sinun on myös syötettävä salasanasi, jotta voit silti kirjautua sisään sen jälkeen. Jos tilisi luotiin kertakirjautumisen kautta etkä koskaan asettanut salasanaa, käytä **Unohditko salasanan** -linkkiä kirjautumissivulla asettaaksesi sen ensin (tämä vaatii palvelimen lähettämään sähköposteja). Jos palvelin sallii kirjautumisen vain tarjoajan kautta, viimeistä linkitettyä tiliä ei voi poistaa linkityksestä.

## Ulkoasu

Hallinnoi laitteellasi tallennettuja näyttöasetuksia.

### Kieli

Valitse kieli Gramps Web -käyttöliittymälle. Kieli-asetus tallennetaan selaimen paikalliseen tallennustilaan ja se koskee vain nykyistä laitetta.

### Teema

Valitse seuraavista:

- **Järjestelmä** – seuraa käyttöjärjestelmän vaaleaa/tumma asetusta (oletusarvo)
- **Vaalea** – käytä aina vaaleaa teemaa
- **Tumma** – käytä aina tummaa teemaa

Teema-asetus tallennetaan selaimen paikalliseen tallennustilaan.

### Sukupuupreferenssit

#### Oletussukupuunäkymä

Määrittää, mikä kaaviotyyppi avautuu oletuksena, kun navigoit [Sukupuu](tree.md) -sivulle. Vaihtoehtoja ovat Esivanhempien puu, Jälkeläisten puu, Hiekkakellokaavio, Suhdekaavio ja Tuulettimikaavio.

Tämä mieltymys tallennetaan selaimen paikalliseen tallennustilaan.

## Kehittäjätyökalut

### API-tunnus

Kopioi nykyinen istuntotunnuksesi leikepöydälle. Tunnusta voidaan käyttää suoraan REST API:ta varten, esimerkiksi interaktiivisessa Swagger UI:ssa, jota Gramps Web -instanssisi tarjoaa osoitteessa `/api/swagger-ui`.

Napsauta **Avaa Swagger** avataksesi Swagger UI:n uudessa välilehdessä, jossa istuntosi on jo käytettävissä.

!!! note
    Istuntotunnus on lyhytaikainen. Kopioi se heti ennen kuin käytät sitä Swaggerissa, sillä se saattaa vanhentua.
