# Käyttäjäasetukset

Käyttäjäasetukset ovat saatavilla käyttäjäkuvakkeesta ylävalikkopalkissa, sitten **Käyttäjäasetukset**. Sivusto on järjestetty taitettaviin osioihin. Muutokset tulevat voimaan heti, ellei toisin mainita.

!!! note
    Muutokset käyttäjäasetuksissa vaikuttavat vain omaan tiliisi. Asetukset, jotka vaikuttavat kaikkiin puun käyttäjiin, hallitaan [Hallinta-asetuksissa](../administration/settings.md).

## Tili

Kattaa profiilitietosi, tunnistetietosi ja tilin turvallisuuden.

### Käyttäjätiedot

Näyttää **käyttäjänimesi** ja nykyisen **käyttäjäroolisi** (esim. Vieraana, Jäsenenä, Toimittajana). Nämä ovat vain luku -tilassa.

### Vaihda sähköposti

Syötä uusi sähköpostiosoite ja napsauta **Lähetä** päivittääksesi tilisi liitetyn osoitteen. Sähköpostiosoitetta käytetään salasanan palautuksiin ja (jos määritetty) ilmoituksiin.

### Vaihda salasana

Syötä nykyinen salasanasi ja uusi salasana, sitten napsauta **Lähetä**. Jos olet unohtanut nykyisen salasanasi, käytä **Unohditko salasanan** -linkkiä kirjautumissivulla sen sijaan.

## Ulkoasu

Hallinnoi laitteellasi tallennettuja näyttöasetuksia.

### Kieli

Valitse kieli Gramps Web -käyttöliittymälle. Kieli-asetus tallennetaan selaimen paikalliseen tallennustilaan ja se koskee vain nykyistä laitetta.

### Teema

Valitse seuraavista:

- **Järjestelmä** – seuraa käyttöjärjestelmän vaaleaa/tumma mieltymystä (oletusarvo)
- **Vaalea** – käytä aina vaaleaa teemaa
- **Tumma** – käytä aina tummaa teemaa

Teema-asetus tallennetaan selaimen paikalliseen tallennustilaan.

### Sukupuupreferenssit

#### Oletussukupuu näkymä

Määrittää, mikä kaaviotyyppi avautuu oletuksena, kun siirryt [Sukupuuhun](tree.md) sivulle. Vaihtoehtoja ovat Esivanhempien puu, Jälkeläisten puu, Tiimalasikaavio, Suhdekaavio ja Tuulettimikaavio.

Tämä asetus tallennetaan selaimen paikalliseen tallennustilaan.

## Kehittäjätyökalut

### API-tunnus

Kopioi nykyinen istuntotunnuksesi leikepöydälle. Tunnusta voidaan käyttää suoraan REST API:in todennukseen, esimerkiksi Gramps Web -instanssisi tarjoamassa interaktiivisessa Swagger UI:ssa osoitteessa `/api/swagger-ui`.

Napsauta **Avaa Swagger** avataksesi Swagger UI:n uudessa välilehdessä, jossa istuntosi on jo käytettävissä.

!!! note
    Istuntotunnus on lyhytkestoinen. Kopioi se heti ennen sen käyttöä Swaggerissa, sillä se saattaa vanhentua.
