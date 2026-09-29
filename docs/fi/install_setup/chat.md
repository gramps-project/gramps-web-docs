# AI-keskustelun asettaminen

!!! info
    AI-keskustelu vaatii Gramps Web API -version 2.5.0 tai uudemman. Versio 3.6.0 esitteli työkalujen kutsumismahdollisuudet älykkäämpiin vuorovaikutuksiin.

Gramps Web API tukee kysymysten esittämistä sukututkimustietokannasta suurten kielimallien (LLM) avulla tekniikan nimeltä retrieval-augmented generation (RAG) yhdistettynä työkalujen kutsumiseen.

## Kuinka se toimii

AI-avustaja käyttää kahta täydentävää lähestymistapaa:

**Retrieval-Augmented Generation (RAG)**: *vektorin upotusmalli* luo indeksin kaikista objekteista Gramps-tietokannassa numeeristen vektorien muodossa, jotka koodavat objektien merkityksen. Kun käyttäjä esittää kysymyksen, kysymys muunnetaan myös vektoriksi ja verrataan tietokannan objekteihin. Tämä *semanttinen haku* palauttaa objektit, jotka ovat semanttisesti lähimpänä kysymystä.

**Työkalujen kutsuminen (v3.6.0+)**: AI-avustaja voi nyt käyttää erikoistyökaluja sukututkimustietojesi kyselyyn suoraan. Nämä työkalut mahdollistavat avustajan etsiä tietokannasta, suodattaa ihmisiä/tapahtumia/perheitä/paikkoja tiettyjen kriteerien mukaan, laskea suhteita yksilöiden välillä ja noutaa yksityiskohtaista objektitietoa. Tämä tekee avustajasta paljon kykenevämmän vastaamaan monimutkaisiin sukututkimuskysymyksiin tarkasti.

AI-keskustelupisteen mahdollistamiseksi Gramps Web API:ssa tarvitaan kolme vaihetta:

1. Vaadittavien riippuvuuksien asentaminen,
2. Semanttisen haun mahdollistaminen,
3. LLM-toimittajan määrittäminen.

Nämä kolme vaihetta kuvataan alla vuorotellen. Lopuksi omistajan tai ylläpitäjän on [määritettävä, mitkä käyttäjät voivat käyttää keskustelutoimintoa](users.md#configuring-who-can-use-ai-chat) Käyttäjien hallinta -asetuksissa.

## Vaadittavien riippuvuuksien asentaminen

AI-keskustelu vaatii Sentence Transformers- ja PyTorch-kirjastojen asentamisen.

Gramps Webin standardi Docker-kuvat sisältävät jo valmiiksi nämä kirjastot `amd64` (esim. 64-bittinen työpöytä-PC) ja `arm64` (esim. 64-bittinen Raspberry Pi) arkkitehtuureille. Valitettavasti AI-keskustelua ei tueta `armv7` (esim. 32-bittinen Raspberry Pi) arkkitehtuurilla PyTorch-tuen puutteen vuoksi.

Kun asennat Gramps Web API:n `pip`-komennolla (tätä ei tarvita Docker-kuvia käytettäessä), tarvittavat riippuvuudet asennetaan komennolla

```bash
pip install gramps_webapi[ai]
```

## Semanttisen haun mahdollistaminen

Jos tarvittavat riippuvuudet on asennettu, semanttisen haun mahdollistaminen voi olla niin yksinkertaista kuin `VECTOR_EMBEDDING_MODEL` -konfiguraatioasetuksen asettaminen (esim. asettamalla `GRAMPSWEB_VECTOR_EMBEDDING_MODEL` ympäristömuuttuja), katso [Palvelimen konfigurointi](configuration.md). Tämä voi olla mikä tahansa merkkijono, joka on tuettu [Sentence Transformers](https://sbert.net/) -kirjastossa. Katso tämän projektin dokumentaatio yksityiskohtia ja saatavilla olevia malleja varten.

!!! warning
    Huomaa, että oletus Docker-kuvat eivät sisällä PyTorch-versiota, jossa on GPU-tuki. Jos sinulla on pääsy GPU:hun (joka nopeuttaa semanttista indeksointia merkittävästi), asenna GPU-yhteensopiva versio PyTorchista.

Valittaessa mallia on useita huomioitavia seikkoja.

- Kun vaihdat mallia, sinun on manuaalisesti luotava semanttinen hakuehto uudelleen puusi (tai kaikkien puiden monipuolisessa asetuksessa) vuoksi, muuten kohtaat virheitä tai merkityksettömiä tuloksia. Gramps Web havaitsee, kun määritetty upotusmalli ei enää vastaa olemassa olevaa indeksiä ja näyttää jatkuvan ilmoituksen ylläpitäjille, joka kehottaa heitä käynnistämään täydellisen uudelleenindeksoinnin [Hallinta-asetuksista](../administration/settings.md#semantic-search-index).
- Mallit ovat kompromissi tarkkuuden/yhteensopivuuden ja laskenta-ajan/tallennustilan välillä. Jos et käytä Gramps Web API:ta järjestelmässä, jossa on pääsy tehokkaaseen GPU:hun, suuremmat mallit ovat yleensä käytännössä liian hitaita.
- Ellei koko tietokantasi ole englanniksi ja kaikkien käyttäjien odoteta kysyvän keskustelukysymyksiä vain englanniksi, tarvitset monikielisen upotusmallin, joita on harvemmin kuin pelkästään englanninkielisiä malleja.

Jos mallia ei ole paikallisessa välimuistissa, se ladataan, kun Gramps Web API käynnistetään ensimmäistä kertaa uuden konfiguraation kanssa. Malli `sentence-transformers/distiluse-base-multilingual-cased-v2` on jo saatavilla paikallisesti käytettäessä standardeja Docker-kuvia. Tämä malli on hyvä lähtökohta ja tukee monikielistä syötettä.

Jaa oppimiasi asioita eri malleista yhteisön kanssa!

!!! info
    Sentence Transformers -kirjasto kuluttaa merkittävän määrän muistia, mikä voi aiheuttaa työntekijäprosessien tappamisen. Nyrkkisääntönä, kun semanttinen haku on käytössä, jokainen Gunicorn-työntekijä kuluttaa noin 200 MB muistia ja jokainen celery-työntekijä noin 500 MB muistia jopa ollessaan käyttämättömänä, ja jopa 1 GB laskettaessa upotuksia. Katso [Rajoita CPU- ja muistinkäyttöä](cpu-limited.md) asetuksista, jotka rajoittavat muistinkäyttöä. Lisäksi on suositeltavaa varata riittävän suuri swap-osio estämään OOM-virheitä tilapäisten muistinkäyttöpiikkien vuoksi.

## Etäupotus-API:n käyttäminen

Paikallisen Sentence Transformers -mallin käyttämisen sijaan voit käyttää etäistä OpenAI-yhteensopivaa upotus-API:a semanttiseen hakuun. Tämä on hyödyllistä, jos haluat siirtää upotusten laskennan erilliseen palveluun (esim. [Ollama](https://ollama.com/)), käyttää pilvipalvelua upotuksille (esim. OpenAI) tai välttää Sentence Transformers- ja PyTorch-kirjastojen lataamista muistiin.

Etä-API:n on oltava yhteensopiva [OpenAI upotusten päätepisteen](https://platform.openai.com/docs/api-reference/embeddings) (`/v1/embeddings`) kanssa.

Käyttääksesi etäupotus-API:a, aseta seuraavat konfiguraatioasetukset (katso [Palvelimen konfigurointi](configuration.md)):

Avain | Kuvaus
----|-------------
`VECTOR_EMBEDDING_MODEL` | Mallin nimi, joka lähetetään etätoimittajalle
`VECTOR_EMBEDDING_BASE_URL` | Etä-API:n perus-URL
`VECTOR_EMBEDDING_API_KEY` | API-avain (vaaditaan vain, jos toimittaja vaatii todennusta)

### Ollaman käyttäminen upotuksiin

Kun otat Gramps Webin käyttöön Docker Compose -työkalulla, voit lisätä Ollama-palvelun ja käyttää sitä sekä upotuksiin että (valinnaisesti) LLM:ään:

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

Kun palvelut on käynnistetty, lataa upotusmalli Ollamaan:

```bash
docker compose exec ollama ollama pull nomic-embed-text
```

!!! info
    Kun käytät Ollamaa upotuksiin, Sentence Transformers- ja PyTorch-kirjastoja ei tarvita, mikä vähentää merkittävästi Gramps Web API:n työntekijöiden muistinkäyttöä.

### OpenAI:n käyttäminen upotuksiin

Käyttääksesi OpenAI upotusten API:a, aseta perus-URL OpenAI API:ksi ja anna API-avaimesi:

```yaml
environment:
  GRAMPSWEB_VECTOR_EMBEDDING_MODEL: text-embedding-3-small
  GRAMPSWEB_VECTOR_EMBEDDING_BASE_URL: https://api.openai.com
  GRAMPSWEB_VECTOR_EMBEDDING_API_KEY: sk-...
```

!!! warning
    Upotusmallin muuttaminen vaatii kaikkien tietojesi (tai kaikkien puiden monipuolisessa asetuksessa) uudelleenindeksoimista, koska eri mallit tuottavat vektoreita, joilla on eri mitat.

## LLM-toimittajan määrittäminen

Viestintä LLM:n kanssa käyttää Pydantic AI -kehystä, joka tukee OpenAI-yhteensopivia API:ita. Tämä mahdollistaa paikallisesti otetun LLM:n käyttämisen Ollaman kautta (katso [Ollama OpenAI -yhteensopivuus](https://ollama.com/blog/openai-compatibility)) tai isännöityjä API:ita, kuten OpenAI, Anthropic tai Hugging Face TGI (Text Generation Inference). LLM määritetään konfiguraatioasetusten `LLM_MODEL` ja `LLM_BASE_URL` avulla.

### Isännöidyn LLM:n käyttäminen OpenAI API:n kautta

Kun käytät OpenAI API:a, `LLM_BASE_URL` voidaan jättää asettamatta, kun taas `LLM_MODEL` on asetettava yhdeksi OpenAI:n malleista, esim. `gpt-4o-mini`. LLM käyttää sekä RAG:ta että työkalujen kutsumista vastatakseen kysymyksiin: se valitsee olennaista tietoa semanttisen haun tuloksista ja voi suoraan kysyä tietokannasta erikoistyökalujen avulla. Se ei vaadi syvällistä sukututkimus- tai historiallista tietoa. Siksi voit kokeilla, riittääkö pieni/halpa malli.

Sinun on myös rekisteröidyttävä tilille, saatava API-avain ja tallennettava se `OPENAI_API_KEY` ympäristömuuttujaan.

!!! info
    `LLM_MODEL` on konfiguraatioasetus; jos haluat asettaa sen ympäristömuuttujan kautta, käytä `GRAMPSWEB_LLM_MODEL` (katso [Konfigurointi](configuration.md)). `OPENAI_API_KEY` ei ole konfiguraatioasetus, vaan ympäristömuuttuja, jota Pydantic AI -kirjasto käyttää suoraan, joten sitä ei pitäisi etuliittää.

### Mistral AI:n käyttäminen

Käyttääksesi Mistral AI:n isännöityjä malleja, etuliitä mallin nimiin `mistral:` asettaessasi `LLM_MODEL`.

Sinun on rekisteröidyttävä Mistral AI -tilille, saatava API-avain ja tallennettava se `MISTRAL_API_KEY` ympäristömuuttujaan. `LLM_BASE_URL` -asetusta ei tarvitse asettaa, sillä Pydantic AI käyttää automaattisesti oikeaa Mistral API -päätepistettä.

Esimerkkikonfiguraatio käytettäessä docker composea ympäristömuuttujilla:
```yaml
environment:
  GRAMPSWEB_LLM_MODEL: mistral:mistral-large-latest
  MISTRAL_API_KEY: your-mistral-api-key-here
  GRAMPSWEB_VECTOR_EMBEDDING_MODEL: sentence-transformers/distiluse-base-multilingual-cased-v2
```

### Paikallisen LLM:n käyttäminen Ollaman kautta

[Ollama](https://ollama.com/) on kätevä tapa käyttää LLM:iä paikallisesti. Tarkista Ollaman dokumentaatio yksityiskohtia varten. Huomaa, että LLM:t vaativat merkittäviä laskentatehoja, ja kaikki muut kuin pienimmät mallit ovat todennäköisesti liian hitaita ilman GPU-tukea. Koska avustaja luottaa työkalujen kutsumiseen, valitse malli, joka tukee työkaluja, kuten [`qwen2.5`](https://ollama.com/library/qwen2.5). Aloita pienellä variantilla, kuten `qwen2.5:7b`, ja kokeile suurempaa, jos vastaukset eivät ole tarpeeksi hyviä. Jaa kokemuksesi yhteisön kanssa!

Kun otat Gramps Webin käyttöön Docker Compose -työkalulla, voit lisätä Ollama-palvelun ja ohjata Gramps Webin siihen:

```yaml
services:
  grampsweb: &grampsweb
    # ... olemassa oleva konfiguraatio ...
    environment:
      GRAMPSWEB_LLM_MODEL: ollama:qwen2.5:7b
      GRAMPSWEB_LLM_BASE_URL: http://ollama:11434/v1/

  grampsweb_celery: &grampsweb_celery
    # ... olemassa oleva konfiguraatio ...
    environment:
      GRAMPSWEB_LLM_MODEL: ollama:qwen2.5:7b
      GRAMPSWEB_LLM_BASE_URL: http://ollama:11434/v1/

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

Kun palvelut on käynnistetty, lataa malli Ollamaan:

```bash
docker compose exec ollama ollama pull qwen2.5:7b
```

Muutamia huomioita:

- Aseta `LLM_MODEL` Ollama-mallin nimeksi, mukaan lukien sen tagi (osa kaksoispisteen jälkeen, esim. `7b`), etuliitteellä `ollama:`. Etuliite saa Pydantic AI:n käyttämään mallille sen Ollama-spesifisiä asetuksia, mikä on suositeltava asetus.
- `LLM_BASE_URL` on päättäväisesti oltava `/v1/`-päätteinen, esim. `http://ollama:11434/v1/`.
- `ollama:`-etuliitteellä ei tarvita `OPENAI_API_KEY` - tai `OLLAMA_BASE_URL` -ympäristömuuttujaa. Jos `LLM_BASE_URL` ei ole asetettu, Gramps Web siirtyy `OLLAMA_BASE_URL`:ään.
- Vaihtoehtoisesti voit jättää etuliitteen pois (esim. `LLM_MODEL: qwen2.5:7b`) ja käyttää Ollamaa sen yleisen OpenAI-yhteensopivan API:n kautta. Tässä tapauksessa sinun on myös asetettava `OPENAI_API_KEY` ympäristömuuttujaan arvo `ollama` (mikä tahansa ei-tyhjää arvo toimii).

Jos kohtaat ongelmia Ollaman kanssa, voit ottaa käyttöön virheenkorjauslokituksen asettamalla ympäristömuuttujan `OLLAMA_DEBUG=1` Ollama-palvelun ympäristöön.

!!! info
    Jos käytät Ollamaa Gramps Web AI -keskustelussa, tue yhteisöä täydentämällä tätä dokumentaatiota kaikilla puuttuvilla tiedoilla.

### Muiden toimittajien käyttäminen

Älä epäröi lähettää dokumentaatiota muista toimittajista ja jakaa kokemuksiasi yhteisön kanssa!
