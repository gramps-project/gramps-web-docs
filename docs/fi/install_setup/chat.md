# AI-keskustelun asetukset

!!! info
    AI-keskustelu vaatii Gramps Web API -version 2.5.0 tai uudemman. Versio 3.6.0 esitteli työkalujen kutsumismahdollisuuksia älykkäämpiin vuorovaikutuksiin.


Gramps Web API tukee kysymysten esittämistä sukututkimustietokannasta suurten kielimallien (LLM) avulla tekniikalla, jota kutsutaan hakua parantavaksi generoinniksi (RAG) yhdistettynä työkalujen kutsumiseen.

## Kuinka se toimii

AI-avustaja käyttää kahta täydentävää lähestymistapaa:

**Hakua Parantava Generointi (RAG)**: *vektorin upotuksen malli* luo indeksin kaikista objekteista Gramps-tietokannassa numeeristen vektorien muodossa, jotka koodavat objektien merkityksen. Kun käyttäjä esittää kysymyksen, kysymys muunnetaan myös vektoriksi ja verrataan tietokannan objekteihin. Tämä *semanttinen haku* palauttaa objektit, jotka ovat semanttiselta merkitykseltään lähimpänä kysymystä.

**Työkalujen Kutsuminen (v3.6.0+)**: AI-avustaja voi nyt käyttää erikoistyökaluja sukututkimustietojesi kyselyyn suoraan. Nämä työkalut mahdollistavat avustajan etsiä tietokannasta, suodattaa henkilöitä/tapahtumia/perheitä/paikkoja tiettyjen kriteerien mukaan, laskea suhteita yksilöiden välillä ja noutaa yksityiskohtaista objektitietoa. Tämä tekee avustajasta paljon kykenevämmän vastaamaan monimutkaisiin sukututkimuskysymyksiin tarkasti.

Ottaaksesi käyttöön keskustelupisteen Gramps Web API:ssa, tarvitaan kolme vaihetta:

1. Tarvittavien riippuvuuksien asentaminen,
2. Semanttisen haun mahdollistaminen,
3. LLM-toimittajan määrittäminen.

Nämä kolme vaihetta kuvataan alla vuorotellen. Lopuksi omistajan tai ylläpitäjän on [määritettävä, mitkä käyttäjät voivat käyttää keskustelutoimintoa](users.md#configuring-who-can-use-ai-chat) Hallitse käyttäjiä -asetuksissa.

## Tarvittavien riippuvuuksien asentaminen

AI-keskustelu vaatii Sentence Transformers- ja PyTorch-kirjastojen asentamista.

Gramps Webin standardi Docker-kuvat sisältävät jo nämä esiasennettuna `amd64` (esim. 64-bittinen työpöytä-PC) ja `arm64` (esim. 64-bittinen Raspberry Pi) arkkitehtuureille. Valitettavasti AI-keskustelua ei tueta `armv7` (esim. 32-bittinen Raspberry Pi) arkkitehtuurilla PyTorch-tuen puutteen vuoksi.

Kun asennat Gramps Web API:n `pip`-komennolla (tätä ei tarvitse tehdä, kun käytät Docker-kuvia), tarvittavat riippuvuudet asennetaan komennolla

```bash
pip install gramps_webapi[ai]
```


## Semanttisen haun mahdollistaminen

Jos tarvittavat riippuvuudet on asennettu, semanttisen haun mahdollistaminen voi olla niin yksinkertaista kuin `VECTOR_EMBEDDING_MODEL` -konfiguraatio-option asettaminen (esim. asettamalla `GRAMPSWEB_VECTOR_EMBEDDING_MODEL` ympäristömuuttuja), katso [Palvelimen konfigurointi](configuration.md). Tämä voi olla mikä tahansa merkkijono mallista, jota tukee [Sentence Transformers](https://sbert.net/) -kirjasto. Katso tämän projektin dokumentaatiosta lisätietoja ja saatavilla olevat mallit.


!!! warning
    Huomaa, että oletusarvoiset Docker-kuvat eivät sisällä PyTorch-versiota, jossa on GPU-tuki. Jos sinulla on pääsy GPU:hun (mikä nopeuttaa semanttista indeksointia merkittävästi), asenna GPU-tukea tarjoava versio PyTorchista.

Mallin valinnassa on useita huomioitavia seikkoja.

- Kun vaihdat mallia, sinun on manuaalisesti luotava semanttinen hakuintressi uudelleen puullesi (tai kaikille puille monipuuliasetuksessa), muuten kohtaat virheitä tai merkityksettömiä tuloksia. Gramps Web havaitsee, kun määritetty upotuksen malli ei enää vastaa olemassa olevaa indeksiä ja näyttää pysyvän ilmoituksen ylläpitäjille, joka kehottaa heitä käynnistämään täydellisen uudelleenindeksoinnin [Hallinta-asetuksista](../administration/settings.md#semantic-search-index).
- Mallit ovat kompromissi tarkkuuden/yhteensopivuuden ja laskenta-ajan/tallennustilan välillä. Jos et käytä Gramps Web API:a järjestelmässä, jossa on pääsy tehokkaaseen GPU:hun, suuremmat mallit ovat käytännössä yleensä liian hitaita.
- Ellet koko tietokantaasi ole englanniksi ja kaikkien käyttäjiesi odotetaan kysyvän keskustelukysymyksiä vain englanniksi, tarvitset monikielisen upotuksen mallin, joita on harvinaisempia kuin puhtaasti englanninkieliset mallit.


Jos mallia ei ole paikallisessa välimuistissa, se ladataan, kun Gramps Web API käynnistetään ensimmäistä kertaa uuden konfiguraation kanssa. Malli `sentence-transformers/distiluse-base-multilingual-cased-v2` on jo saatavilla paikallisesti käytettäessä standardeja Docker-kuvia. Tämä malli on hyvä lähtökohta ja tukee monikielistä syötettä.

Jaa oppimiasi asioita eri malleista yhteisön kanssa!

!!! info
    Sentence Transformers -kirjasto kuluttaa merkittävän määrän muistia, mikä voi aiheuttaa työntekijäprosessien kaatumisen. Nyrkkisääntönä, kun semanttinen haku on käytössä, jokainen Gunicorn-työntekijä kuluttaa noin 200 MB muistia ja jokainen celery-työntekijä noin 500 MB muistia jopa silloin, kun se on käyttämättömänä, ja jopa 1 GB, kun se laskee upotuksia. Katso [Rajoita CPU- ja muistinkäyttöä](cpu-limited.md) asetuksista, jotka rajoittavat muistinkäyttöä. Lisäksi on suositeltavaa varata riittävän suuri swap-osio estämään OOM-virheitä tilapäisten muistinkäyttöpiikkien vuoksi.

## LLM-toimittajan määrittäminen

Viestintä LLM:n kanssa käyttää Pydantic AI -kehystä, joka tukee OpenAI-yhteensopivia API:ita. Tämä mahdollistaa paikallisesti käyttöönotetun LLM:n käytön Ollaman kautta (katso [Ollama OpenAI -yhteensopivuus](https://ollama.com/blog/openai-compatibility)) tai isännöityjä API:ita, kuten OpenAI, Anthropic tai Hugging Face TGI (Tekstigeneroinnin päättely). LLM määritetään konfiguraatioparametreilla `LLM_MODEL` ja `LLM_BASE_URL`.


### Isännöidyn LLM:n käyttäminen OpenAI API:n kautta

Kun käytät OpenAI API:a, `LLM_BASE_URL` voidaan jättää asettamatta, kun taas `LLM_MODEL` on asetettava yhdeksi OpenAI-malleista, esim. `gpt-4o-mini`. LLM käyttää sekä RAG:ta että työkalujen kutsumista kysymyksiin vastaamiseen: se valitsee merkityksellistä tietoa semanttisen haun tuloksista ja voi suoraan kysyä tietokannasta erikoistyökalujen avulla. Se ei vaadi syvällistä sukututkimus- tai historiallista tietämystä. Siksi voit kokeilla, riittääkö pieni/halpa malli.

Sinun on myös rekisteröidyttävä tilille, saatava API-avain ja tallennettava se `OPENAI_API_KEY` ympäristömuuttujaan.

!!! info
    `LLM_MODEL` on konfiguraatioparametri; jos haluat asettaa sen ympäristömuuttujan kautta, käytä `GRAMPSWEB_LLM_MODEL` (katso [Konfigurointi](configuration.md)). `OPENAI_API_KEY` ei ole konfiguraatioparametri, vaan ympäristömuuttuja, jota Pydantic AI -kirjasto käyttää suoraan, joten sitä ei pitäisi etuliittää.


### Mistral AI:n käyttäminen

Käyttääksesi Mistral AI:n isännöimiä malleja, etuliitä mallin nimi `mistral:`-etuliitteellä, kun asetat `LLM_MODEL`.

Sinun on rekisteröidyttävä Mistral AI -tilille, saatava API-avain ja tallennettava se `MISTRAL_API_KEY` ympäristömuuttujaan. `LLM_BASE_URL`-asetusta ei tarvitse asettaa, koska Pydantic AI käyttää automaattisesti oikeaa Mistral API -päätepistettä.

Esimerkkikonfiguraatio, kun käytetään docker composea ympäristömuuttujilla:
```yaml
environment:
  GRAMPSWEB_LLM_MODEL: mistral:mistral-large-latest
  MISTRAL_API_KEY: your-mistral-api-key-here
  GRAMPSWEB_VECTOR_EMBEDDING_MODEL: sentence-transformers/distiluse-base-multilingual-cased-v2
```


### Paikallisen LLM:n käyttäminen Ollaman kautta

[Ollama](https://ollama.com/) on kätevä tapa käyttää LLM:iä paikallisesti. Tarkista Ollama-dokumentaatio lisätietoja varten. Huomaa, että LLM:t vaativat merkittävästi laskentatehoa, ja kaikki muut kuin pienimmät mallit ovat todennäköisesti liian hitaita ilman GPU-tukea. Voit kokeilla, täyttääkö [`tinyllama`](https://ollama.com/library/tinyllama) tarpeesi. Jos ei, kokeile yhtä suuremmista malleista. Jaa kaikki kokemukset yhteisön kanssa!

Kun otat Gramps Webin käyttöön Docker Compose -palvelulla, voit lisätä Ollama-palvelun

```yaml
services:
  ollama:
    image: ollama/ollama
    container_name: ollama
    ports:
      - "11434:11434"
    volumes:
      - ollama_data:/root/.ollama

volumes:
    ollama_data:
```

ja asettaa sitten `LLM_BASE_URL`-konfiguraatioparametrin arvoksi `http://ollama:11434/v1`. Aseta `LLM_MODEL` malliksi, jota Ollama tukee, ja lataa se säiliöösi komennolla `ollama pull <model>`. Lopuksi aseta `OPENAI_API_KEY` arvoksi `ollama`.

Ongelmien vianetsintään Ollaman kanssa voit ottaa käyttöön virheenkorjauslokituksen asettamalla ympäristömuuttujan `OLLAMA_DEBUG=1` Ollama-palvelun ympäristössä.

!!! info
    Jos käytät Ollamaa Gramps Web AI -keskustelussa, tue yhteisöä täydentämällä tätä dokumentaatiota kaikilla puuttuvilla tiedoilla.

### Muiden toimittajien käyttäminen

Älä epäröi lähettää dokumentaatiota muista toimittajista ja jakaa kokemuksiasi yhteisön kanssa!
