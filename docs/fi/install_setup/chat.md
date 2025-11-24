# AI-chatin asetukset

!!! info
    AI-chat vaatii Gramps Web API -version 2.5.0 tai uudemman.


Gramps Web API tukee kysymysten esittämistä sukututkimustietokannasta suurten kielimallien (LLM) avulla tekniikalla, jota kutsutaan hakua parantavaksi generoinniksi (RAG).

RAG toimii seuraavasti. Ensin käytetään *vektorin upotuksen mallia* luomaan indeksi kaikista objekteista Gramps-tietokannassa numeeristen vektorien muodossa, jotka koodaavat objektien merkityksen. Tämä prosessi on samanlainen kuin täydellisen tekstihakuindeksin luominen, mutta se on laskennallisesti kalliimpi.

Seuraavaksi, kun käyttäjä esittää kysymyksen chat-pisteen kautta, kysymys muunnetaan myös vektoriksi saman upotusmallin avulla ja verrataan objekteihin Gramps-tietokannassa. Tämä *semanttinen haku* palauttaa tietokannasta objektit, jotka ovat semanttiselta merkitykseltään lähimpänä kysymystä.

Viimeisessä vaiheessa kysymys ja haetut objektit lähetetään LLM:lle, jotta se voi muotoilla vastauksen annettujen tietojen perusteella. Tällä tavoin chatbotilla on pääsy yksityiskohtaisiin tietoihin sukututkimustietokannan sisällöstä sen sijaan, että se luottaisi vain ennestään olemassa olevaan tietoon.

Chat-pisteen mahdollistamiseksi Gramps Web API:ssa tarvitaan kolme vaihetta:

1. Vaadittavien riippuvuuksien asentaminen,
2. Semanttisen haun mahdollistaminen,
3. LLM-palveluntarjoajan määrittäminen.

Nämä kolme vaihetta kuvataan alla vuorotellen. Lopuksi omistajan tai ylläpitäjän on [määritettävä, mitkä käyttäjät voivat käyttää chat-ominaisuutta](users.md#configuring-who-can-use-ai-chat) Käyttäjien hallinta -asetuksissa.

## Vaadittavien riippuvuuksien asentaminen

AI-chat vaatii Sentence Transformers- ja PyTorch-kirjastojen asentamista.

Gramps Webin standardi Docker-kuvat sisältävät jo valmiiksi asennettuina `amd64` (esim. 64-bittinen työpöytätietokone) ja `arm64` (esim. 64-bittinen Raspberry Pi) arkkitehtuureille. Valitettavasti AI-chat ei ole tuettu `armv7` (esim. 32-bittinen Raspberry Pi) arkkitehtuurilla PyTorch-tuen puutteen vuoksi.

Kun asennat Gramps Web API:n `pip`-komennolla (tätä ei tarvitse tehdä, kun käytetään Docker-kuvia), tarvittavat riippuvuudet asennetaan komennolla

```bash
pip install gramps_webapi[ai]
```

## Semanttisen haun mahdollistaminen

Jos tarvittavat riippuvuudet on asennettu, semanttisen haun mahdollistaminen voi olla niin yksinkertaista kuin `VECTOR_EMBEDDING_MODEL` -konfiguraatio-option asettaminen (esim. asettamalla `GRAMPSWEB_VECTOR_EMBEDDING_MODEL` ympäristömuuttuja), katso [Palvelimen konfigurointi](configuration.md). Tämä voi olla mikä tahansa merkkijono mallista, jota tukee [Sentence Transformers](https://sbert.net/) -kirjasto. Katso tämän projektin dokumentaatiosta lisätietoja ja saatavilla olevat mallit.

!!! warning
    Huomaa, että oletusarvoiset Docker-kuvat eivät sisällä PyTorch-versiota, jossa on GPU-tuki. Jos sinulla on pääsy GPU:hun (joka nopeuttaa semanttista indeksointia merkittävästi), asenna GPU-tukea tarjoava versio PyTorchista.

Mallin valinnassa on useita huomioitavia seikkoja.

- Kun vaihdat mallia, sinun on manuaalisesti luotava semanttinen hakuindeksi uudelleen puullesi (tai kaikille puille monipuuasetuksessa), muuten kohtaat virheitä tai merkityksettömiä tuloksia.
- Mallit ovat kompromissi tarkkuuden/yhteensopivuuden ja laskenta-ajan/tallennustilan välillä. Jos et käytä Gramps Web API:a järjestelmässä, jolla on pääsy tehokkaaseen GPU:hun, suuremmat mallit ovat yleensä käytännössä liian hitaita.
- Ellet koko tietokantasi ole englanniksi ja kaikkien käyttäjien odotetaan kysyvän chat-kysymyksiä vain englanniksi, tarvitset monikielisen upotusmallin, joita on harvemmassa kuin puhtaasti englanninkielisiä malleja.

Jos mallia ei ole paikallisessa välimuistissa, se ladataan, kun Gramps Web API käynnistetään ensimmäisen kerran uuden konfiguraation kanssa. Malli `sentence-transformers/distiluse-base-multilingual-cased-v2` on jo saatavilla paikallisesti käytettäessä standardeja Docker-kuvia. Tämä malli on hyvä lähtökohta ja tukee monikielistä syötettä.

Jaa oppimiasi asioita eri malleista yhteisön kanssa!

!!! info
    Sentence Transformers -kirjasto kuluttaa merkittävän määrän muistia, mikä voi aiheuttaa työntekijäprosessien tappamisen. Nyrkkisääntönä, kun semanttinen haku on käytössä, jokainen Gunicorn-työntekijä kuluttaa noin 200 MB muistia ja jokainen celery-työntekijä noin 500 MB muistia jopa ollessaan käyttämättömänä, ja jopa 1 GB laskettaessa upotuksia. Katso [Rajoita CPU- ja muistinkäyttöä](cpu-limited.md) asetuksista, jotka rajoittavat muistinkäyttöä. Lisäksi on suositeltavaa varata riittävän suuri swap-osio estämään OOM-virheitä tilapäisten muistinkäyttöpiikkien vuoksi.

## LLM-palveluntarjoajan määrittäminen

Viestintä LLM:n kanssa käyttää OpenAI-yhteensopivaa API:a `openai-python`-kirjaston avulla. Tämä mahdollistaa paikallisesti käyttöönotetun LLM:n käytön Ollaman kautta (katso [Ollama OpenAI -yhteensopivuus](https://ollama.com/blog/openai-compatibility)) tai API:a kuten OpenAI tai Hugging Face TGI (Tekstin Generointi Inference). LLM konfiguroidaan konfiguraatioparametreilla `LLM_MODEL` ja `LLM_BASE_URL`.

### Isännöidyn LLM:n käyttäminen OpenAI API:n kautta

Kun käytät OpenAI API:a, `LLM_BASE_URL` voidaan jättää asettamatta, kun taas `LLM_MODEL` on asetettava yhdeksi OpenAI-malleista, esim. `gpt-4o-mini`. Huomaa, että RAG-lähestymistavan vuoksi LLM:ää käytetään "vain" oikean tiedon valitsemiseen semanttisen haun tuloksista ja vastauksen muotoilemiseen, se ei vaadi syvällistä sukututkimus- tai historiallista tietoa. Siksi voit kokeilla, riittääkö pieni/halpa malli.

Sinun on myös rekisteröidyttävä tilille, saatava API-avain ja tallennettava se `OPENAI_API_KEY` ympäristömuuttujaan.

!!! info
    `LLM_MODEL` on konfiguraatioparametri; jos haluat asettaa sen ympäristömuuttujan kautta, käytä `GRAMPSWEB_LLM_MODEL` (katso [Konfigurointi](configuration.md)). `OPENAI_API_KEY` ei ole konfiguraatioparametri, vaan ympäristömuuttuja, jota `openai-python`-kirjasto käyttää suoraan, joten sitä ei tule etuliittää.

### Paikallisen LLM:n käyttäminen Ollaman kautta

[Ollama](https://ollama.com/) on kätevä tapa käyttää LLM:iä paikallisesti. Katso Ollaman dokumentaatio lisätietoja varten. Huomaa, että LLM:t vaativat merkittäviä laskentatehoja, ja kaikki paitsi pienimmät mallit ovat todennäköisesti liian hitaita ilman GPU-tukea. Voit kokeilla, täyttääkö [`tinyllama`](https://ollama.com/library/tinyllama) tarpeesi. Jos ei, kokeile yhtä suuremmista malleista. Jaa kokemuksesi yhteisön kanssa!

Kun otat Gramps Webin käyttöön Docker Compose:n avulla, voit lisätä Ollama-palvelun

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

ja sitten asettaa `LLM_BASE_URL` -konfiguraatioparametrin arvoon `http://ollama:11434/v1`. Aseta `LLM_MODEL` malliksi, jota Ollama tukee, ja lataa se konttiisi komennolla `ollama pull <model>`. Lopuksi aseta `OPENAI_API_KEY` arvoksi `ollama`.

Ongelmien vianetsintään Ollaman kanssa voit ottaa käyttöön virheenkorjauslokit asettamalla ympäristömuuttujan `OLLAMA_DEBUG=1` Ollama-palvelun ympäristössä.

!!! info
    Jos käytät Ollamaa Gramps Web AI-chatissa, tue yhteisöä täydentämällä tätä dokumentaatiota kaikilla puuttuvilla tiedoilla.

### Muiden palveluntarjoajien käyttäminen

Älä epäröi lähettää dokumentaatiota muista palveluntarjoajista ja jakaa kokemuksiasi yhteisön kanssa!
