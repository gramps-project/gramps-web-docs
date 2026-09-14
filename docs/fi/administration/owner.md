# Luo tili puun omistajalle

Ennen kuin voit alkaa käyttää Gramps Webiä, sinun on luotava tili puun omistajalle. Jos tietylle puulle ei ole olemassa käyttäjätiliä, näytetään lomake tilin luomiseksi. Lomake riippuu siitä, onko palvelin asetettu yhdelle puulle tai useammalle puulle.

## Yhden puun asennus: luo ylläpitäjätili

Yhdellä puulla varustetulla palvelimella, kun käyttäjätiliä ei vielä ole, Gramps Webin avaaminen näyttää lomakkeen ylläpitäjätilin luomiseksi. Ylläpitäjäkäyttäjä on sekä (yksittäisen) puun omistaja että asennuksen ylläpitäjä. Lomake mahdollistaa myös sähköpostikonfiguraation asettamisen, jota tarvitaan sähköposti-ilmoituksiin (esim. käyttäjän salasanan palauttamiseen). Jos sähköpostikonfiguraatio on jo lisätty konfiguraatiotiedoston tai ympäristömuuttujien kautta palvelimella, tämä osa lomakkeesta voidaan jättää tyhjäksi.

Salasana on syötettävä kahdesti; lomake voidaan lähettää vain, kun molemmat syötteet täsmäävät.

Jos instanssi on jo asetettu, lomakkeen osoitteen avaaminen näyttää viestin, joka pyytää sinua kirjautumaan sisään olemassa olevalla tilillä.

## Usean puun asennus: luo ylläpitäjätili

Usean puun asennuksessa sama lomake ylläpitäjätilin luomiseksi näytetään, jos käyttäjiä ei ole *missään puussa*, eli kun palvelin on juuri luotu.

## Usean puun asennus: luo puun omistajatili

Usean puun asennuksessa jokainen käyttäjä on sidottu yhteen puuhun. Vaikka käyttäjiä olisi jo olemassa muissa puissa, puun omistaja voidaan luoda verkkoliittymässä, jos omistajaa ei vielä ole *tälle puulle*.

Kuitenkin, omistajan luomislomaketta ei näytetä automaattisesti Gramps Webin etusivulla, joka on sama kaikille puille. Sen sijaan se voidaan saavuttaa osoitteessa `https://my-gramps-instance/firstrun/my-tree-id`, jossa `https://my-gramps-instance` on Gramps Web -asennuksesi perusosoite ja `my-tree-id` on puusi ID.

Mahdollinen työnkulku sivuston ylläpitäjälle uuden puun luomiseksi on

- Luo puu REST API:n kautta, hankkien uuden puun ID:n
- Jaa linkki omistajan luomislomakkeeseen, jossa on asianmukainen puun ID, mahdolliselle puun omistajalle

Puun omistajan luomislomake on analoginen ylläpitäjän luomislomakkeen kanssa, paitsi että se ei salli sähköpostikonfiguraation muuttamista (mikä on sallittua vain ylläpitäjille).
