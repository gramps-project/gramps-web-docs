# AI-chatin asetukset

!!! info
    AI-chat vaatii Gramps Web API -version 2.5.0 tai uudemman. Versio 3.6.0 esitteli työkalukutsumismahdollisuuksia älykkäämpiin vuorovaikutuksiin.


Gramps Web API tukee kysymysten esittämistä sukututkimustietokannasta suurten kielimallien (LLM) avulla tekniikalla, jota kutsutaan hakua parantavaksi generoinniksi (RAG), yhdistettynä työkalukutsumiseen.

## Kuinka se toimii

AI-avustaja käyttää kahta täydentävää lähestymistapaa:

**Hakua parantava generointi (RAG)**: *vektorin upotuksen malli* luo indeksin kaikista objekteista Gramps-tietokannassa numeeristen vektoreiden muodossa, jotka koodaavat objektien merkityksen. Kun käyttäjä esittää kysymyksen, kysymys muunnetaan myös vektoriksi ja verrataan tietokannan objekteihin. Tämä *semanttinen haku* palauttaa objektit, jotka ovat semanttisesti lähimpänä kysymystä.

**Työkalukutsuminen (v3.6.0+)**: AI-avustaja voi nyt käyttää erikoistyökaluja sukututkimustietojesi kyselyyn suoraan. Nämä työkalut mahdollistavat avustajan etsiä tietokannasta, suodattaa henkilöitä/tapahtumia/perheitä/paikkoja tietyillä kriteereillä, laskea suhteita yksilöiden välillä ja noutaa yksityiskohtaista objektitietoa. Tämä tekee avustajasta paljon kykenevämmän vastaamaan monimutkaisiin sukututkimuskysymyksiin tarkasti.

AI-chat-päätepisteen mahdollistamiseksi Gramps Web API:ssa tarvitaan kolme vaihetta:

1. Vaadittavien riippuvuuksien asentaminen,
2. Semanttisen haun mahdollistaminen,
3. LLM-toimittajan määrittäminen.

Kolme vaihetta kuvataan alla vuorotellen. Lopuksi omistajan tai ylläpitäjän on [määritettävä, mitkä käyttäjät voivat käyttää chat-ominaisuutta](users.md#configuring-who-can-use-ai-chat) Hallitse käyttäjiä -asetuksissa.

## Vaadittavien riippuvuuksien asentaminen

AI-chat vaatii Sentence Transformers- ja PyTorch-kirjastojen asentamista.

Gramps Webin standardidocker-kuvat sisältävät nämä kirjastot jo valmiiksi `amd64` (esim. 64-bittinen pöytätietokone) ja `arm64` (esim. 64-bittinen Raspberry Pi) arkkitehtuureille. Valitettavasti AI-chat ei ole tuettu `armv7` (esim. 32-bittinen Raspberry Pi) arkkitehtuurilla PyTorch-tuen puutteen vuoksi.

Kun asennat Gramps Web API:n `pip`-komennolla (tätä ei tarvita Docker-kuvia käytettäessä), tarvittavat riippuvuudet asennetaan komennolla

```bash
pip install gramps_webapi[ai]
```

## Semanttisen haun mahdollistaminen

Jos tarvittavat riippuvuudet on asennettu, semanttisen haun mahdollistaminen voi olla niin yksinkertaista kuin `VECTOR_EMBEDDING_MODEL` -konfiguraatio-option asettaminen (esim. asettamalla `GRAMPSWEB_VECTOR_EMBEDDING_MODEL` ympäristömuuttuja), katso [Palvelimen konfigurointi](configuration.md). Tämä voi olla mikä tahansa merkkijono, joka vastaa [Sentence Transformers](https://sbert.net/) -kirjaston tukemaa mallia. Katso tämän projektin dokumentaatio yksityiskohtia ja saatavilla olevia malleja varten.

!!! warning
    Huomaa, että oletusarvoiset docker-kuvat eivät sisällä PyTorch-versiota, jossa on GPU-tuki. Jos sinulla on pääsy GPU:hun (mikä nopeuttaa semanttista indeksointia merkittävästi), asenna GPU-yhteensopiva versio PyTorchista.

Mallin valinnassa on useita huomioitavia seikkoja.

- Kun vaihdat mallia, sinun on manuaalisesti luotava semanttinen hakuintressi uudelleen puullesi (tai kaikille puillesi monipuuliasetuksessa), muuten kohtaat virheitä tai merkityksettömiä tuloksia. Gramps Web havaitsee, kun määritetty upotusmalli ei enää vastaa olemassa olevaa indeksiä ja näyttää jatkuvan ilmoituksen ylläpitäjille, kehottaen heitä käynnistämään täydellinen uudelleenindeksointi [Hallinta-asetuksista](../administration/settings.md#semantic-search-index).
- Mallit ovat kompromissi tarkkuuden/yhteensopivuuden ja laskenta-ajan/tallennustilan välillä. Jos et käytä Gramps Web API:a järjestelmässä, jossa on pääsy tehokkaaseen GPU:hun, suuremmat mallit ovat yleensä käytännössä liian hitaita.
- Ellei koko tietokantasi ole englanniksi ja kaikkien käyttäjiesi odotetaan kysyvän chat-kysymyksiä vain englanniksi, tarvitset monikielisen upotusmallin, joita on harvinaisempia kuin puhtaat englanninkieliset mallit.

Jos mallia ei ole paikallisessa välimuistissa, se ladataan, kun Gramps Web API käynnistetään ensimmäistä kertaa uuden konfiguraation kanssa. Malli `sentence-transformers/distiluse-base-multilingual-cased-v2` on jo saatavilla paikallisesti käytettäessä standardidocker-kuvia. Tämä malli on hyvä lähtökohta ja tukee monikielistä syötettä.

Jaa oppimiasi asioita eri malleista yhteisön kanssa!

!!! info
    Sentence Transformers -kirjasto kuluttaa merkittävän määrän muistia, mikä voi aiheuttaa työntekijäprosessien tappamisen. Yleisenä sääntönä, kun semanttinen haku on käytössä, jokainen Gunicorn-työntekijä kuluttaa noin 200 MB muistia ja jokainen celery-työntekijä noin 500 MB muistia jopa lepotilassa, ja jopa 1 GB laskettaessa upotuksia. Katso [Rajoita CPU- ja muistinkäyttöä](cpu-limited.md) asetuksista, jotka rajoittavat muistinkäyttöä. Lisäksi on suositeltavaa varata riittävän suuri swap-osio estämään OOM-virheitä tilapäisten muistinkäyttöpiikkien vuoksi.

## Etäupotus-API:n käyttäminen

Paikallisen Sentence Transformers -mallin käyttämisen vaihtoehtona voit käyttää etäistä OpenAI-yhteensopivaa upotus-API:a semanttiseen hakuun. Tämä on hyödyllistä, jos haluat siirtää upotusten laskennan erilliseen palveluun (esim. [Ollama](https://ollama.com/)), käyttää pilvipalveluntarjoajaa (esim. OpenAI) tai välttää Sentence Transformers- ja PyTorch-kirjastojen lataamista muistiin.

Etä-API:n on oltava yhteensopiva [OpenAI upotusten päätepisteen](https://platform.openai.com/docs/api-reference/embeddings) (`/v1/embeddings`) kanssa.

Käyttääksesi etäupotus-API:a, aseta seuraavat konfiguraatio-optiot (katso [Palvelimen konfigurointi](configuration.md)):

Avain | Kuvaus
----|-------------
`VECTOR_EMBEDDING_MODEL` | Mallin nimi, joka annetaan etätoimittajalle
`VECTOR_EMBEDDING_BASE_URL` | Etä-API:n perus-URL
`VECTOR_EMBEDDING_API_KEY` | API-avain (vaaditaan vain, jos toimittaja vaatii todennusta)

### Ollaman käyttäminen upotuksiin

Kun otat Gramps Webin käyttöön Docker Compose -ympäristössä, voit lisätä Ollama-palvelun ja käyttää sitä sekä upotuksiin että (valinnaisesti) LLM:ään:

```yaml
services:
  grampsweb: &grampsweb
    # ... olemassa oleva konfiguraatio ...
    environment:
      GRAMPSWEB_VECTOR_EMBEDDING_MODEL: nomic-embed-text
      GRAMPSWEB_VECTOR_EMBEDDING_BASE_URL: http://ollama:11434

  grampsweb_celery: &grampsweb_celery
    # ... olemassa oleva konfiguraatio ...
    environment:
      GRAMPSWEB_VECTOR_EMBEDDING_MODEL: nomic-embed-text
      GRAMPSWEB_VECTOR_EMBEDDING_BASE_URL: http://ollama:11434

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

Kun olet käynnistänyt palvelut, lataa upotusmalli Ollamaan:

```bash
docker compose exec ollama ollama pull nomic-embed-text
```

!!! info
    Kun käytät Ollamaa upotuksiin, Sentence Transformers- ja PyTorch-kirjastoja ei tarvita, mikä vähentää merkittävästi Gramps Web API:n työntekijöiden muistinkäyttöä.

### OpenAI:n käyttäminen upotuksiin

Käyttääksesi OpenAI upotusten API:a, aseta perus-URL OpenAI API:lle ja anna API-avaimesi:

```yaml
environment:
  GRAMPSWEB_VECTOR_EMBEDDING_MODEL: text-embedding-3-small
  GRAMPSWEB_VECTOR_EMBEDDING_BASE_URL: https://api.openai.com
  GRAMPSWEB_VECTOR_EMBEDDING_API_KEY: sk-...
```

!!! warning
    Upotusmallin muuttaminen vaatii kaikkien tietueiden uudelleenindeksoimista puullesi (tai kaikille puillesi monipuuliasetuksessa), koska eri mallit tuottavat vektoreita eri ulottuvuuksilla.

## LLM-toimittajan määrittäminen

Viestintä LLM:n kanssa käyttää Pydantic AI -kehystä, joka tukee OpenAI-yhteensopivia API:ita. Tämä mahdollistaa paikallisesti otetun LLM:n käytön Ollaman kautta (katso [Ollama OpenAI -yhteensopivuus](https://ollama.com/blog/openai-compatibility)) tai isännöityjä API:ita, kuten OpenAI, Anthropic tai Hugging Face TGI (Tekstin Generoinnin Inference). LLM määritetään konfiguraatioparametreilla `LLM_MODEL` ja `LLM_BASE_URL`.

### Isännöidyn LLM:n käyttäminen OpenAI API:n kautta

Käyttäessäsi OpenAI API:a, `LLM_BASE_URL` voidaan jättää asettamatta, kun taas `LLM_MODEL` on asetettava yhdeksi OpenAI:n malleista, esim. `gpt-4o-mini`. LLM käyttää sekä RAG:ta että työkalukutsumista vastatakseen kysymyksiin: se valitsee relevanttia tietoa semanttisen haun tuloksista ja voi suoraan kysyä tietokannasta erikoistyökalujen avulla. Se ei vaadi syvällistä sukututkimus- tai historiallista tietämystä. Siksi voit kokeilla, riittääkö pieni/halpa malli.

Sinun on myös rekisteröidyttävä tilille, saatava API-avain ja tallennettava se `OPENAI_API_KEY` ympäristömuuttujaan.

!!! info
    `LLM_MODEL` on konfiguraatioparametri; jos haluat asettaa sen ympäristömuuttujan kautta, käytä `GRAMPSWEB_LLM_MODEL` (katso [Konfigurointi](configuration.md)). `OPENAI_API_KEY` ei ole konfiguraatioparametri, vaan ympäristömuuttuja, jota Pydantic AI -kirjasto käyttää suoraan, joten sitä ei tule etuliittää.

### Mistral AI:n käyttäminen

Käyttääksesi Mistral AI:n isännöityjä malleja, etuliitä mallin nimi `mistral:` -etuliitteellä, kun asetat `LLM_MODEL`.

Sinun on rekisteröidyttävä Mistral AI -tilille, saatava API-avain ja tallennettava se `MISTRAL_API_KEY` ympäristömuuttujaan. `LLM_BASE_URL` -asetusta ei tarvitse asettaa, sillä Pydantic AI käyttää automaattisesti oikeaa Mistral API -päätepistettä.

Esimerkkikonfiguraatio käytettäessä docker composea ympäristömuuttujilla:
```yaml
environment:
  GRAMPSWEB_LLM_MODEL: mistral:mistral-large-latest
  MISTRAL_API_KEY: your-mistral-api-key-here
  GRAMPSWEB_VECTOR_EMBEDDING_MODEL: sentence-transformers/distiluse-base-multilingual-cased-v2
```

### Paikallisen LLM:n käyttäminen Ollaman kautta

[Ollama](https://ollama.com/) on kätevä tapa ajaa LLM:iä paikallisesti. Tarkista Ollaman dokumentaatio yksityiskohtia varten. Huomaa, että LLM:t vaativat merkittäviä laskentatehoja, ja kaikki paitsi pienimmät mallit ovat todennäköisesti liian hitaita ilman GPU-tukea. Voit kokeilla, täyttääkö [`tinyllama`](https://ollama.com/library/tinyllama) tarpeesi. Jos ei, kokeile yhtä suuremmista malleista. Jaa kokemuksesi yhteisön kanssa!

Kun otat Gramps Webin käyttöön Docker Compose -ympäristössä, voit lisätä Ollama-palvelun

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

ja asettaa sitten `LLM_BASE_URL` -konfiguraatioparametrin arvoon `http://ollama:11434/v1`. Aseta `LLM_MODEL` malliksi, jota Ollama tukee, ja lataa se säiliöösi komennolla `ollama pull <malli>`. Lopuksi aseta `OPENAI_API_KEY` arvoksi `ollama`.

Ongelmatilanteiden ratkaisemiseksi Ollaman kanssa voit ottaa käyttöön virheenkorjauslokituksen asettamalla ympäristömuuttuja `OLLAMA_DEBUG=1` Ollama-palvelun ympäristöön.

!!! info
    Jos käytät Ollamaa Gramps Web AI-chatissa, tue yhteisöä täydentämällä tätä dokumentaatiota kaikilla puuttuvilla tiedoilla.

### Muiden toimittajien käyttäminen

Älä epäröi lähettää dokumentaatiota muista toimittajista ja jakaa kokemuksiasi yhteisön kanssa!
