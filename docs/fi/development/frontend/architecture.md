# Arkkitehtuuri

## Komponentit

Frontend on rakennettu web-komponenteista. Ne on määritelty Javascript-tiedostoissa `src`-hakemistossa.

Tyypillisesti jokainen tiedosto määrittelee yhden komponentin, joka alkaa
```javascript
class GrampsjsSomeElement extends LitElement
```
ja päättyy
```javascript
customElements.define('grampsjs-some-element', GrampsjsSomeElement)`
```
joka määrittelee uuden HTML-elementin `grampsjs-some-element`, jota voidaan käyttää muualla.

Pääsisäänkäynti, joka on sisällytetty `index.html`-tiedostoon, on `gramps-js`-elementti, joka on määritelty `GrampsJs.js`-tiedostossa. Tämä sisältää kaikkien yksittäisten sivujen määrittelyn (jotka vastaavat yksinkertaisesti elementtejä, jotka näytetään tai piilotetaan reitin/URL:n mukaan), valikon ja reitityksen.

`src/views`-hakemiston komponentit vastaavat yleensä koko sivun komponentteja, jotka noutavat tietoja taustajärjestelmästä (esim. henkilöluettelon näkymä), kun taas `src/components`-hakemiston komponentit ovat yleensä pienempiä rakennuspalikoita, joita käytetään näkymien sisällä ja jotka saavat tietonsa vanhemman elementin tarjoamista attribuuteista. Tämä erottelu ei kuitenkaan ole tiukka.

## Tietovirta

Tietoja vaihdetaan Backend/API:n kanssa `apiGet`, `apiPut` ja `apiPost` -menetelmien kautta `src/api.js`-tiedostossa, jotka huolehtivat automaattisesti todennuksesta.

Tietoja siirretään vanhemmilta komponenteilta lapsikomponenteille ominaisuuksien kautta (katso esim. [Lit-dokumentaatio](https://lit.dev/docs/components/properties/)).

Kun tietoja tarvitsee palauttaa lapsikomponentilta vanhemmalle komponentille, käytetään mukautettuja tapahtumia, jotka voidaan laukaista `fireEvent`-funktion avulla `src/api.js`-tiedostossa ja joita voidaan kuunnella Litin `@`-syntaksilla [(dokumentaatio)](https://lit.dev/docs/components/events/).

## Todennus

Päivitystunnus ja todennustunnus tallennetaan selaimen paikalliseen tallennustilaan. Aina kun API-kutsu tehdään ja tunnus on vanhentunut, tallennettua päivitystunnusta käytetään uuden käyttöoikeustunnuksen hakemiseen ja API-kutsu toistetaan.

Käyttäjän valtuutusskooppia, joka on tallennettu käyttöoikeustunnuksen vaatimuksiin, saadaan `getPermissions`-funktion avulla ja käytetään ylimmän tason `GrampsJs`-elementissä asettamaan totuusarvo-ominaisuudet `canAdd`, `canEdit`, `canManageUsers`, jotka siirtyvät lapsielementeille toteuttamaan valtuutukseen liittyvää toiminnallisuutta.
