# AI-keskustelun asetukset

!!! info
    AI-keskustelu vaatii Gramps Web API -version 2.5.0 tai uudemman. Versiossa 3.6.0 esiteltiin työkalujen kutsumismahdollisuuksia älykkäämpiin vuorovaikutuksiin.


Gramps Web API tukee kysymysten esittämistä sukututkimustietokannasta käyttäen suuria kielimalleja (LLM) työkalujen kutsumisen avulla.

## Kuinka se toimii

AI-avustaja käyttää erikoistyökaluja kyselyjen tekemiseen sukututkimustiedoistasi suoraan. Nämä työkalut mahdollistavat avustajalle tietokannan hakemisen täysimääräisellä tekstihakuominaisuudella, ihmisten/tapahtumien/perheiden/paikkojen suodattamisen erityisten kriteerien mukaan, suhteiden laskemisen yksilöiden välillä ja täydellisten tietueiden hakemisen, mukaan lukien muistiinpanot. Avustaja vastaa sitten sen perusteella, mitä tietueita se on etsinyt, ja linkittää niihin vastauksessaan. Se vastaa vain puusta, ei yleisestä tiedosta: jos puu ei tallenna jotain, avustaja ilmoittaa siitä. Linkit olemattomiin tai käyttäjälle yksityisiin kohteisiin korvataan niiden tekstillä.

AI-keskustelu ei tarvitse vektoriupotusta. Gramps Web API:n versiot ennen 3.24 käyttivät myös *semanttista hakua* (retrieval-augmented generation, RAG), joka vertasi kysymyksen merkitystä tietokannan kaikkien objektien laskettujen numeeristen vektoreiden indeksiin. Semanttinen haku poistettiin Gramps Web API:sta versiossa 3.25; asetuksia `VECTOR_EMBEDDING_MODEL`, `VECTOR_EMBEDDING_BASE_URL` ja `VECTOR_EMBEDDING_API_KEY` ei oteta huomioon, ja ne voidaan poistaa konfiguraatiostasi.

Chat-päätepisteen mahdollistamiseksi Gramps Web API:ssa tarvitaan kaksi vaihetta:

1. Vaadittavien riippuvuuksien asentaminen,
2. LLM-toimittajan määrittäminen.

Kaksi vaihetta kuvataan alla vuorotellen. Lopuksi omistajan tai ylläpitäjän on [määritettävä, mitkä käyttäjät voivat käyttää keskustelutoimintoa](users.md#configuring-who-can-use-ai-chat) Käyttäjien hallinta -asetuksissa.

## Vaadittavien riippuvuuksien asentaminen

Gramps Webin standardidocker-kuvat sisältävät jo kaikki AI-keskusteluun tarvittavat riippuvuudet esiasennettuna.

Kun asennat Gramps Web API:n `pip`-komennolla (tätä ei tarvita, kun käytät Docker-kuvia), tarvittavat riippuvuudet asennetaan komennolla

```bash
pip install gramps_webapi[ai]
```


## LLM-toimittajan määrittäminen

Viestintä LLM:n kanssa käyttää Pydantic AI -kehystä, joka tukee OpenAI-yhteensopivia API:ita. Tämä mahdollistaa paikallisesti käyttöönotetun LLM:n käytön Ollaman kautta (katso [Ollama OpenAI -yhteensopivuus](https://ollama.com/blog/openai-compatibility)) tai isännöityjen API:iden, kuten OpenAI, Anthropic tai Hugging Face TGI (Text Generation Inference), kautta. LLM määritetään konfiguraatioparametrien `LLM_MODEL` ja `LLM_BASE_URL` avulla.

OpenAI-yhteensopivien API:iden lisäksi Pydantic AI:n toimittajakohtaisia mallien etuliitteitä voidaan käyttää OpenAI:lle, Anthropicille, Googlelle, Mistralille, Groqille, AWS Bedrockille ja Ollamalle. Muut toimittajat, kuten Cohere, Hugging Face ja xAI, eivät ole asennettu; Hugging Face Inference Providers -palveluja voidaan silti käyttää niiden OpenAI-yhteensopivalla päätepisteellä (`LLM_BASE_URL` asetettuna `https://router.huggingface.co/v1`).

Jos mallipalvelimesi ei rajoita vastauksen pituutta, aseta `LLM_MAX_OUTPUT_TOKENS` mallin mahdollisten tokenien maksimimääräksi per vastaus (katso [Konfiguraatio](configuration.md)).


### Isännöidyn LLM:n käyttäminen OpenAI API:n kautta

Kun käytät OpenAI API:a, `LLM_BASE_URL` voidaan jättää määrittämättä, kun taas `LLM_MODEL` on asetettava yhdeksi OpenAI-malleista, esim. `gpt-4o-mini`. LLM käyttää työkalujen kutsumista kysymyksiin vastaamiseen: se kysyy tietokannasta suoraan erikoistyökalujen avulla ja vastaa sen perusteella, mitä tietueita se löytää. Se ei vaadi syvällistä sukututkimus- tai historiallista tietoa. Siksi voit kokeilla, onko pieni/halpa malli riittävä.

Sinun on myös rekisteröidyttävä tilille, saatava API-avain ja tallennettava se `OPENAI_API_KEY` ympäristömuuttujaan.

!!! info
    `LLM_MODEL` on konfiguraatioparametri; jos haluat asettaa sen ympäristömuuttujan kautta, käytä `GRAMPSWEB_LLM_MODEL` (katso [Konfiguraatio](configuration.md)). `OPENAI_API_KEY` ei ole konfiguraatioparametri, vaan ympäristömuuttuja, jota Pydantic AI -kirjasto käyttää suoraan, joten sitä ei tule etuliittää.


### Mistral AI:n käyttäminen

Jos haluat käyttää Mistral AI:n isännöityjä malleja, etuliitä mallin nimi `mistral:`-etuliitteellä, kun asetat `LLM_MODEL`.

Sinun on rekisteröidyttävä Mistral AI -tilille, saatava API-avain ja tallennettava se `MISTRAL_API_KEY` ympäristömuuttujaan. `LLM_BASE_URL`-asetusta ei tarvitse määrittää, koska Pydantic AI käyttää automaattisesti oikeaa Mistral API -päätepistettä.

Esimerkkikonfiguraatio käytettäessä docker composea ympäristömuuttujien kanssa:
```yaml
environment:
  GRAMPSWEB_LLM_MODEL: mistral:mistral-large-latest
  MISTRAL_API_KEY: your-mistral-api-key-here
```


### Paikallisen LLM:n käyttäminen Ollaman kautta

[Ollama](https://ollama.com/) on kätevä tapa ajaa LLM:iä paikallisesti. Tarkista Ollama-dokumentaatio yksityiskohtia varten. Huomaa, että LLM:t vaativat merkittäviä laskentatehoja, ja kaikki paitsi pienimmät mallit ovat todennäköisesti liian hitaita ilman GPU-tukea. Koska avustaja luottaa työkalujen kutsumiseen, valitse malli, joka tukee työkaluja, kuten [`qwen2.5`](https://ollama.com/library/qwen2.5). Aloita pienellä variantilla, kuten `qwen2.5:7b`, ja kokeile suurempaa, jos vastaukset eivät ole riittävän hyviä. Jaa kokemuksesi yhteisön kanssa!

Kun otat Gramps Webin käyttöön Docker Composen avulla, voit lisätä Ollama-palvelun ja ohjata Gramps Webin siihen:

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

Kun palvelut on käynnistetty, tuo malli Ollamaan:

```bash
docker compose exec ollama ollama pull qwen2.5:7b
```

Muutama asia, joista on syytä huomioida:

- Aseta `LLM_MODEL` Ollama-mallin nimeksi, mukaan lukien sen tagi (osa kaksoispisteen jälkeen, esim. `7b`), etuliitteellä `ollama:`. Etuliite saa Pydantic AIn käyttämään sen Ollama-spesifisiä asetuksia mallille, mikä on suositeltu asetus.
- `LLM_BASE_URL` on päätyttävä `/v1/`, esim. `http://ollama:11434/v1/`.
- `ollama:`-etuliitteellä ei tarvita `OPENAI_API_KEY`- eikä `OLLAMA_BASE_URL`-ympäristömuuttujaa. Jos `LLM_BASE_URL` ei ole asetettu, Gramps Web palautuu `OLLAMA_BASE_URL`:iin.
- Vaihtoehtoisesti voit jättää etuliitteen pois (esim. `LLM_MODEL: qwen2.5:7b`) ja käyttää Ollamaa sen yleisen OpenAI-yhteensopivan API:n kautta. Tässä tapauksessa sinun on myös asetettava `OPENAI_API_KEY` ympäristömuuttujaan arvo `ollama` (mikä tahansa ei-tyhjää arvoa toimii).

Jos kohtaat ongelmia Ollaman kanssa, voit ottaa käyttöön virheenkorjauslokit asettamalla ympäristömuuttujan `OLLAMA_DEBUG=1` Ollama-palvelun ympäristöön.

!!! info
    Jos käytät Ollamaa Gramps Web AI -keskustelussa, tue yhteisöä täydentämällä tätä dokumentaatiota puuttuvilla tiedoilla.

### Muiden toimittajien käyttäminen

Älä epäröi lähettää dokumentaatiota muista toimittajista ja jakaa kokemuksiasi yhteisön kanssa!

## Valinnaiset ominaisuudet

### Kuvien käyttö kysymyksissä

Jos mallisi hyväksyy kuvia, aseta `LLM_VISION` arvoon `True`, jotta käyttäjät voivat liittää kuvia kysymyksiinsä, esimerkiksi tietueiden skannauksia (Gramps Web API 3.26+). Kuvia pienennetään enintään 1568 pikseliin pitkällä sivulla ennen kuin ne lähetetään mallille. Tarkista, että malli todella tukee kuvasyötteitä: monet pienet paikalliset mallit eivät tue tätä, ja toimittaja hylkää kysymykset, joissa on kuvia.

### Anna avustajan ehdottaa muutoksia

Kun `LLM_ALLOW_WRITE_PROPOSALS` on asetettu arvoon `True` (Gramps Web API 3.26+), avustaja voi [ehdottaa muutoksia puuhun](../user-guide/chat.md#letting-the-assistant-change-your-tree), jotka käyttäjät hyväksyvät tarkastelun jälkeen. Avustaja ei koskaan kirjoita tietokantaan. Ehdotuksia tarjotaan vain käyttäjille, joilla on oikeus lisätä, muokata ja poistaa kohteita, eli toimittajille ja sitä korkeammille, ja jotka saavat käyttää keskustelua.

Oikeiden ehdotusten kirjoittaminen on mallille vaikeampaa kuin kysymyksiin vastaaminen, joten testaa se mallisi kanssa ennen kuin otat sen käyttöön käyttäjillesi. Lisätyökalut tekevät myös jokaisesta pyynnöstä mallille hieman suuremman.
