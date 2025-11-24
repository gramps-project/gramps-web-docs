# Luo tili puun omistajalle

Ennen kuin voit alkaa käyttää Gramps Webiä, sinun on luotava tili puun omistajalle. Jos tietylle puulle ei ole olemassa käyttäjätiliä, näytetään lomake tilin luomiseksi. Lomake riippuu palvelimen asetuksista, jotka voivat olla joko yhden puun tai usean puun käyttöä varten.

## Yhden puun asennus: luo ylläpitäjätili

Yhden puun asennuksessa, kun käyttäjätiliä ei vielä ole, Gramps Webin avaaminen näyttää lomakkeen ylläpitäjätilin luomiseksi. Ylläpitäjäkäyttäjä on sekä (yksittäisen) puun omistaja että asennuksen ylläpitäjä. Lomake mahdollistaa myös sähköpostiasetusten määrittämisen, joita tarvitaan sähköpostihälytyksiin (esim. käyttäjän salasanan palauttamiseen). Jos sähköpostiasetukset on jo lisätty konfiguraatiotiedoston tai ympäristömuuttujien kautta palvelimelle, tämän osan lomakkeesta voi jättää tyhjiksi.

## Usean puun asennus: luo ylläpitäjätili

Usean puun asennuksessa sama lomake ylläpitäjätilin luomiseksi näytetään, jos käyttäjiä ei ole *missään puussa*, eli kun palvelin on juuri luotu.

## Usean puun asennus: luo puun omistajatili

Usean puun asennuksessa jokainen käyttäjä on sidottu yhteen puuhun. Vaikka käyttäjiä jo olisi muissa puissa, puun omistaja voidaan luoda verkkoliittymässä, jos omistajaa ei vielä ole *tälle puulle*.

Kuitenkin, omistajan luomislomaketta ei näytetä automaattisesti Gramps Webin etusivulla, joka on sama kaikille puille. Sen sijaan se voidaan saavuttaa osoitteessa `https://my-gramps-instance/firstrun/my-tree-id`, jossa `https://my-gramps-instance` on Gramps Web -asennuksesi perusosoite ja `my-tree-id` on puusi ID.

Mahdollinen työnkulku sivuston ylläpitäjälle uuden puun luomiseksi on:

- Luo puu REST API:n kautta, hankkimalla uuden puun ID
- Jaa linkki omistajan luomislomakkeeseen, jossa on asianmukainen puun ID, mahdolliselle puun omistajalle

Puun omistajan luomislomake on analoginen ylläpitäjän luomislomakkeen kanssa, lukuun ottamatta sitä, että se ei salli sähköpostiasetusten muuttamista (mikä on sallittua vain ylläpitäjille).
